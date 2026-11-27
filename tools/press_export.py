#!/usr/bin/env python3
"""Turn a press layout PDF from an HTML authoring master into a PDF/X-4 press file.

Governed by E01 §5.3.4 and E03 §5.1.4, §5.3.1, §5.3.5 and §5.4.1.

Input: the PDF saved from the "Export press PDF" button of an HTML authoring
master such as TPL-E01-03. That PDF is a 230 mm x 317 mm sheet in sRGB: the A4
trim sits 10 mm inside each edge, and the sheet carries a 3 mm Bleed and 100% K
crop marks offset 3 mm.

What this does, in order:
  1. Replaces every DeviceRGB fill and stroke with the fixed ISO Coated v2 CMYK
     build that B02 §5.1.1 or §5.6.1 assigns to that exact colour. The table is
     read from the live B02 file. Nothing is converted through an ICC profile,
     and any colour without a fixed build stops the export (E03 §5.3.1).
  2. Sets TrimBox (A4) and BleedBox (3 mm) from the sheet geometry.
  3. Attaches the ISO Coated v2 (ECI) / FOGRA39 OutputIntent from
     06_Dependencies/Color-Profiles/ and writes PDF/X-4 Info and XMP metadata.
  4. Runs the library-checks PDF preflight on the result and fails if it fails.

Usage (from the repository root):
    pip install -r tools/requirements.txt
    python3 tools/press_export.py cover-press.pdf --out cover-press_PDFX4.pdf --title "Annual Report 2027"

This is a structural conversion. The Owner colour proof in E03 §5.4.3 still
applies before any press run.
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
import uuid
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parent))
import library_checks as lc  # noqa: E402

MM = lc.MM
SHEET_MM = (230.0, 317.0)   # A4 trim plus 10 mm on every side
SLUG_MM = 10.0              # trim edge to sheet edge
BLEED_MM = 3.0              # E03 §5.1.4
TOLERANCE_MM = 0.5          # browser rounding, as in E01 §5.4.5
ICC = lc.LIB / "06_Dependencies/Color-Profiles/ISOcoated_v2_eci.icc"


class PressError(Exception):
    pass


def build_table(pal: dict) -> dict[tuple[int, int, int], tuple[float, float, float, float]]:
    """Map exact sRGB triplets (0-255) to their fixed B02 CMYK builds (0-1)."""
    table = {(255, 255, 255): (0.0, 0.0, 0.0, 0.0),   # Pure White: unprinted paper (B02 §5.6.1)
             (0, 0, 0): (0.0, 0.0, 0.0, 1.0)}         # Pure Black: K-only (E03 §5.3.2)
    for hexv, entry in pal["colors"].items():
        if "cmyk" not in entry:
            continue
        rgb = tuple(int(hexv[i:i + 2], 16) for i in (1, 3, 5))
        cmyk = tuple(int(x) / 100 for x in entry["cmyk"].split(", "))
        if sum(cmyk) > 3.0:
            raise PressError(f"B02 build for {hexv} totals {sum(cmyk) * 100:.0f}% ink, above 300% (E03 §5.3.5).")
        table[rgb] = cmyk
    return table


def lookup(table: dict, operands, where: str):
    rgb = tuple(round(float(x) * 255) for x in operands)
    for key, cmyk in table.items():
        if max(abs(a - b) for a, b in zip(rgb, key)) <= 1:
            return cmyk
    hexv = "#%02X%02X%02X" % rgb
    raise PressError(f"{where}: colour {hexv} has no fixed B02 CMYK build. "
                     "Use a B02 palette colour; the press export never converts colours (E01 §5.3.4, E03 §5.3.1).")


def convert_stream(reader, obj, resources, table, where, seen):
    """Rewrite colour operators in one content stream and any Form XObjects it draws."""
    from pypdf.generic import ContentStream, FloatObject
    cs = ContentStream(obj, reader)
    out = []
    for operands, op in cs.operations:
        name = op.decode("latin-1") if isinstance(op, bytes) else op
        if name in ("rg", "RG"):
            cmyk = lookup(table, operands, where)
            out.append(([FloatObject(round(v, 4)) for v in cmyk], b"k" if name == "rg" else b"K"))
            continue
        if name in ("g", "G"):
            level = float(operands[0])
            if level not in (0.0, 1.0):
                raise PressError(f"{where}: grey tint {level} has no B02 build; use K-only builds (E03 §5.3.2).")
            k = 1.0 - level
            out.append(([FloatObject(0), FloatObject(0), FloatObject(0), FloatObject(k)], b"k" if name == "g" else b"K"))
            continue
        if name in ("cs", "CS", "sc", "SC", "scn", "SCN", "sh", "BI", "EI", "ID"):
            raise PressError(f"{where}: operator `{name}` (colour space, shading or inline image) is not supported "
                             "in a press export. The cover should use flat B02 colours only.")
        if name == "Do":
            xo = resources["/XObject"][operands[0]].get_object()
            if xo.get("/Subtype") == "/Image":
                raise PressError(f"{where}: raster image {operands[0]} found. Print marks must be vector (E03 §5.3.3).")
            key = id(xo)
            if key not in seen:
                seen.add(key)
                sub_res = xo.get("/Resources")
                sub_res = sub_res.get_object() if sub_res is not None else resources
                fix_group(xo)
                xo.set_data(convert_stream(reader, xo, sub_res, table, f"{where} form {operands[0]}", seen).get_data())
        out.append((operands, op))
    cs.operations = out
    return cs


def fix_group(obj):
    from pypdf.generic import NameObject
    grp = obj.get("/Group")
    if grp is not None:
        grp = grp.get_object()
        if "/CS" in grp:
            grp[NameObject("/CS")] = NameObject("/DeviceCMYK")


def check_ext_gstates(resources, where):
    gs = resources.get("/ExtGState")
    for name, g in (gs.get_object() if gs is not None else {}).items():
        g = g.get_object()
        smask = g.get("/SMask")
        if smask is not None and str(smask) != "/None":
            raise PressError(f"{where}: graphics state {name} uses a soft mask, which may carry RGB colour.")


def xmp(title: str, now: str, doc_id: str) -> bytes:
    t = escape(title)
    return f"""<?xpacket begin="﻿" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
    <rdf:Description rdf:about=""
      xmlns:pdfxid="http://www.npes.org/pdfx/ns/id/"
      xmlns:pdf="http://ns.adobe.com/pdf/1.3/"
      xmlns:dc="http://purl.org/dc/elements/1.1/"
      xmlns:xmp="http://ns.adobe.com/xap/1.0/"
      xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/">
      <pdfxid:GTS_PDFXVersion>PDF/X-4</pdfxid:GTS_PDFXVersion>
      <pdf:Trapped>False</pdf:Trapped>
      <pdf:Producer>Irvantri Standards tools/press_export.py (pypdf)</pdf:Producer>
      <dc:format>application/pdf</dc:format>
      <dc:title><rdf:Alt><rdf:li xml:lang="x-default">{t}</rdf:li></rdf:Alt></dc:title>
      <dc:creator><rdf:Seq><rdf:li>Irvantri Standards Pte. Ltd.</rdf:li></rdf:Seq></dc:creator>
      <xmp:CreatorTool>Chromium (HTML authoring master press layout)</xmp:CreatorTool>
      <xmp:CreateDate>{now}</xmp:CreateDate>
      <xmp:ModifyDate>{now}</xmp:ModifyDate>
      <xmp:MetadataDate>{now}</xmp:MetadataDate>
      <xmpMM:DocumentID>uuid:{doc_id}</xmpMM:DocumentID>
      <xmpMM:InstanceID>uuid:{doc_id}</xmpMM:InstanceID>
      <xmpMM:VersionID>1</xmpMM:VersionID>
      <xmpMM:RenditionClass>default</xmpMM:RenditionClass>
    </rdf:Description>
  </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>""".encode("utf-8")


def press_export(src: Path, out: Path, title: str | None) -> dict:
    import pypdf
    from pypdf.generic import (ArrayObject, DecodedStreamObject, DictionaryObject, FloatObject,
                               NameObject, NumberObject, TextStringObject)

    pal = lc.load_palette()
    table = build_table(pal)
    reader = pypdf.PdfReader(str(src))
    if reader.is_encrypted:
        raise PressError("the input PDF is encrypted.")
    if reader.trailer["/Root"].get("/AcroForm") is not None:
        raise PressError("the input PDF has form fields; flatten them first.")

    writer = pypdf.PdfWriter(clone_from=reader)
    writer.pdf_header = b"%PDF-1.6"
    seen: set[int] = set()
    measured = []
    for i, page in enumerate(writer.pages, 1):
        where = f"page {i}"
        media = [float(v) for v in page.mediabox]
        w_mm, h_mm = (media[2] - media[0]) / MM, (media[3] - media[1]) / MM
        if abs(w_mm - SHEET_MM[0]) > TOLERANCE_MM or abs(h_mm - SHEET_MM[1]) > TOLERANCE_MM:
            raise PressError(f"{where} is {w_mm:.2f} x {h_mm:.2f} mm. Save it with the \"Export press PDF\" button, "
                             f"which makes a {SHEET_MM[0]:.0f} x {SHEET_MM[1]:.0f} mm sheet.")
        if page.get("/Annots"):
            del page[NameObject("/Annots")]
        res = page.get("/Resources")
        res = res.get_object() if res is not None else DictionaryObject()
        check_ext_gstates(res, where)
        fix_group(page)
        contents = page.get_contents()
        if contents is not None:
            page.replace_contents(convert_stream(writer, contents, res, table, where, seen))

        # The trim sits 10 mm in from the top-left corner, where the browser lays out the A4 sheet.
        left, top = media[0] + SLUG_MM * MM, media[3] - SLUG_MM * MM
        trim = [left, top - 297 * MM, left + 210 * MM, top]
        bleed = [trim[0] - BLEED_MM * MM, trim[1] - BLEED_MM * MM, trim[2] + BLEED_MM * MM, trim[3] + BLEED_MM * MM]
        page[NameObject("/TrimBox")] = ArrayObject(FloatObject(round(v, 3)) for v in trim)
        page[NameObject("/BleedBox")] = ArrayObject(FloatObject(round(v, 3)) for v in bleed)
        page[NameObject("/ArtBox")] = ArrayObject(FloatObject(round(v, 3)) for v in trim)
        measured.append({"page": i, "sheet_mm": [round(w_mm, 2), round(h_mm, 2)]})

    icc_bytes = ICC.read_bytes()
    icc = DecodedStreamObject()
    icc.set_data(icc_bytes)
    icc[NameObject("/N")] = NumberObject(4)
    intent = DictionaryObject({
        NameObject("/Type"): NameObject("/OutputIntent"),
        NameObject("/S"): NameObject("/GTS_PDFX"),
        NameObject("/OutputCondition"): TextStringObject("ISO Coated v2 (ECI) / FOGRA39"),
        NameObject("/OutputConditionIdentifier"): TextStringObject("FOGRA39"),
        NameObject("/RegistryName"): TextStringObject("http://www.color.org"),
        NameObject("/Info"): TextStringObject("ISO Coated v2 (ECI) / FOGRA39"),
        NameObject("/DestOutputProfile"): writer._add_object(icc),
    })
    writer.root_object[NameObject("/OutputIntents")] = ArrayObject([writer._add_object(intent)])

    old = reader.metadata or {}
    title = title or str(old.get("/Title") or src.stem)
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    pdf_date = now.strftime("D:%Y%m%d%H%M%S+00'00'")
    writer.metadata = {
        "/Title": title,
        "/Author": "Irvantri Standards Pte. Ltd.",
        "/Creator": "Chromium (HTML authoring master press layout)",
        "/Producer": "Irvantri Standards tools/press_export.py (pypdf)",
        "/CreationDate": pdf_date,
        "/ModDate": pdf_date,
        "/GTS_PDFXVersion": "PDF/X-4",
    }
    writer._info.get_object()[NameObject("/Trapped")] = NameObject("/False")
    meta = DecodedStreamObject()
    meta.set_data(xmp(title, now.isoformat().replace("+00:00", "Z"), str(uuid.uuid4())))
    meta[NameObject("/Type")] = NameObject("/Metadata")
    meta[NameObject("/Subtype")] = NameObject("/XML")
    writer.root_object[NameObject("/Metadata")] = writer._add_object(meta)

    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("wb") as fh:
        writer.write(fh)

    # Same preflight the library-checks CI runs on print templates.
    rep = lc.Report([])
    lc.pdf_checks(rep, pal, files=[(out, True)])
    check = rep.checks[0]
    return {"pages": measured, "preflight": check["measurements"][0], "findings": check["findings"]}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf", type=Path, help="PDF saved from the \"Export press PDF\" button")
    ap.add_argument("--out", type=Path, help="output path (default: <input>_PDFX4.pdf)")
    ap.add_argument("--title", help="document title for the PDF metadata (default: the input title)")
    args = ap.parse_args()
    out = args.out or args.pdf.with_name(args.pdf.stem + "_PDFX4.pdf")
    try:
        result = press_export(args.pdf, out, args.title)
    except PressError as e:
        print(f"Press export stopped: {e}", file=sys.stderr)
        return 1
    pf = result["preflight"]
    print(f"Wrote {out}")
    print(f"  trim {pf['geometry'][0]['trim_mm']} mm, bleed {pf['geometry'][0]['bleed_mm']} mm, "
          f"output intent {pf.get('output_condition')}, max total ink {pf['max_total_ink_pct']}%")
    print(f"  CMYK builds used: {', '.join(pf['cmyk_values'])}")
    if result["findings"]:
        for f in result["findings"]:
            print(f"  FAIL {f['id']}: {f['message']}", file=sys.stderr)
        return 1
    print("  Preflight passed. Get an Owner colour proof before the press run (E03 §5.4.3).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
