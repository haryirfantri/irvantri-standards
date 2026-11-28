#!/usr/bin/env python3
"""Automated measurement checks for the Irvantri Standards Unified Operating Library.

Every check measures the real files on the checked-out commit and records the
numbers it measured, so governance records (A04) can cite a run of this script
as evidence instead of a hand-written pass table.

Rules are read from the live library wherever they are written as data:
  * the colour palette (HEX, RGB, CMYK) is parsed from B02 Section 5 tables;
  * register versions and statuses are parsed from Library-Index.md;
  * checksums and sizes are parsed from 06_Dependencies/Dependencies-Manifest.md.
Thresholds and pairings that are written as prose live in tools/contrast-pairs.json
with the clause each one comes from.

Usage (from the repository root):
    python3 tools/library_checks.py --report-dir check-report

Exit status is 1 when any finding fails and is not listed in tools/known-issues.json.
Only dependency outside the standard library: pypdf (PDF checks).
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

REPO = Path(__file__).resolve().parent.parent
LIB = REPO / "Unified Operating Library"
TOOLS = REPO / "tools"

HEX_RE = re.compile(r"(?<![0-9A-Za-z&])#([0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})(?![0-9A-Za-z_-])")
RGB_FN_RE = re.compile(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+)\s*)?\)")
MM = 72 / 25.4  # points per millimetre
A4_PT = (210 * MM, 297 * MM)
ACTIVE_DIRS = ["01_Standards", "02_Assets", "03_Templates", "04_Publications", "05_Records", "06_Dependencies"]


# --------------------------------------------------------------------------- helpers

def rel(p: Path) -> str:
    return p.relative_to(REPO).as_posix()


def lib_rel(p: Path) -> str:
    return p.relative_to(LIB).as_posix()


def active_files(*exts: str) -> list[Path]:
    out = []
    for d in ACTIVE_DIRS:
        for p in sorted((LIB / d).rglob("*")):
            if p.is_file() and p.suffix.lower() in exts:
                out.append(p)
    idx = LIB / "Library-Index.md"
    if ".md" in exts:
        out.append(idx)
    return out


def md_header(path: Path) -> dict[str, str]:
    """Parse the leading `| **Field** | Value |` metadata table of a library Markdown file."""
    fields = {}
    for line in path.read_text(encoding="utf-8").splitlines()[:40]:
        m = re.match(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.*?)\s*\|\s*$", line)
        if m:
            fields[m.group(1).strip()] = m.group(2).strip().strip("`").strip()
    return fields


def table_rows(text: str) -> list[list[str]]:
    rows = []
    for line in text.splitlines():
        if line.startswith("|") and not re.match(r"^\|\s*:?-{3,}", line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rows.append(cells)
    return rows


def ticks(cell: str) -> str:
    m = re.search(r"`([^`]*)`", cell)
    return m.group(1) if m else cell.strip()


def luminance(hex6: str) -> float:
    def ch(c: int) -> float:
        c = c / 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (int(hex6[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def contrast(a: str, b: str) -> float:
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def floor2(x: float) -> float:
    """Truncate (not round) to two decimals so 4.499 never reports as 4.50."""
    return int(x * 100) / 100


class Report:
    def __init__(self, known: list[dict]):
        self.checks: list[dict] = []
        self.known = {k["id"]: k for k in known}
        self.used_known: set[str] = set()

    def check(self, cid: str, title: str, cites: list[str]):
        c = {"id": cid, "title": title, "cites": cites, "measurements": [], "findings": []}
        self.checks.append(c)
        return c

    def measure(self, c: dict, **kw):
        c["measurements"].append(kw)

    def fail(self, c: dict, fid: str, message: str, **detail):
        if any(x["id"] == fid for x in c["findings"]):
            return  # same defect already reported for this check
        f = {"id": fid, "message": message, **detail}
        today = dt.date.today().isoformat()
        if fid in self.known and str(self.known[fid].get("review_by", "9999")) < today:
            self.used_known.add(fid)
            f["status"] = "fail"
            f["message"] += f" (known-issue entry expired on {self.known[fid]['review_by']})"
            c["findings"].append(f)
            return
        if fid in self.known:
            k = self.known[fid]
            f["status"] = "known"
            f["known_issue"] = {x: k.get(x) for x in ("reason", "reference", "review_by")}
            self.used_known.add(fid)
        else:
            f["status"] = "fail"
        c["findings"].append(f)


# --------------------------------------------------------------------------- palette (B02)

def load_palette() -> dict:
    """Parse the B02 Section 5 tables into hex -> {name, rgb, cmyk, clause}."""
    b02 = next((LIB / "01_Standards").rglob("B02_*.md"))
    text = b02.read_text(encoding="utf-8")
    sec5 = text.split("## 5.", 1)[1].split("## 6.", 1)[0]
    palette: dict[str, dict] = {}
    clause = None
    for line in sec5.splitlines():
        m = re.match(r"^\*\*(5\.\d+\.\d+)\*\*", line)
        if m:
            clause = m.group(1)
        if not line.startswith("|") or re.match(r"^\|\s*:?-", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        name = re.sub(r"\*", "", cells[0]).strip()
        hexes = [h for h in (ticks(c) for c in cells) if re.fullmatch(r"#[0-9A-Fa-f]{6}", h)]
        if not hexes or name in ("Color Name", "Neutral Token Role", "Semantic State"):
            continue
        rgbs = [ticks(c) for c in cells if re.fullmatch(r"`\d+, \d+, \d+`", c)]
        cmyks = [ticks(c) for c in cells if re.fullmatch(r"`\d+, \d+, \d+, \d+`", c)]
        if clause == "5.3.1":  # semantic rows: fg, subtle surface, border
            for role, h in zip(("fg", "bg", "border"), hexes):
                palette.setdefault(h.upper(), {"name": f"{name} {role}", "clause": f"B02 §{clause}"})
            if rgbs:
                palette[hexes[0].upper()].setdefault("rgb", rgbs[0])
            continue
        entry = palette.setdefault(hexes[0].upper(), {"name": name, "clause": f"B02 §{clause}"})
        if rgbs:
            entry["rgb"] = rgbs[0]
        if cmyks:
            entry["cmyk"] = cmyks[0]
    return {"source": rel(b02), "colors": palette}


# --------------------------------------------------------------------------- checks

def check_register(rep: Report):
    c = rep.check("register-sync", "Register ↔ file headers and registered paths",
                  ["A01 (header metadata)", "A02-C3", "A02-C5", "A02-C9"])
    idx = (LIB / "Library-Index.md").read_text(encoding="utf-8")
    n_std = n_paths = 0
    for cells in table_rows(idx):
        if len(cells) < 6:
            continue
        code = ticks(cells[0])
        path_cell = next((ticks(x) for x in cells if re.fullmatch(r"`0\d_[^`]+`", x.strip())), None)
        if not path_cell:
            continue
        status = next((ticks(x) for x in cells if ticks(x) in
                       ("Approved", "Planned", "Draft", "In Review", "Deprecated", "Closed", "Open", "Retired")), "")
        p = LIB / path_cell
        n_paths += 1
        if status in ("Planned", "Deprecated", "Retired"):
            rep.measure(c, code=code, path=path_cell, status=status, exists=p.exists(), note="not required to exist")
            continue
        if not p.exists():
            rep.fail(c, f"register-sync.missing:{code}", f"{code} is registered at `{path_cell}` but the file does not exist.")
            continue
        if re.fullmatch(r"[A-H]\d{2}", code):
            n_std += 1
            reg_ver, reg_status, reg_review = ticks(cells[3]), ticks(cells[4]), ticks(cells[6])
            h = md_header(p)
            got = {"Version": h.get("Version"), "Status": h.get("Status"), "Next Review": h.get("Next Review")}
            want = {"Version": reg_ver, "Status": reg_status, "Next Review": reg_review}
            rep.measure(c, code=code, register=want, header=got)
            for k in want:
                if got[k] != want[k]:
                    rep.fail(c, f"register-sync.{k.lower().replace(' ', '-')}:{code}",
                             f"{code} {k}: register says `{want[k]}`, file header says `{got[k]}`.")
    # Every active file in a coded folder is registered
    registered = set(re.findall(r"`(0[2-5]_[^`]+\.[a-z]+)`", idx))
    for d in ("02_Assets", "03_Templates", "04_Publications", "05_Records"):
        for p in sorted((LIB / d).iterdir()):
            if p.is_file() and lib_rel(p) not in registered:
                rep.fail(c, f"register-sync.unregistered:{lib_rel(p)}", f"`{lib_rel(p)}` exists but is not in Library-Index.md.")
    c["summary"] = f"{n_std} standard headers compared; {n_paths} registered paths resolved"


def check_palette(rep: Report, pal: dict):
    c = rep.check("palette", "Hex and rgb() values are on the B02 palette and uppercase",
                  ["B02-C1", "B02-C2", "D01-C2"])
    colors = pal["colors"]
    rgb_set = {tuple(int(x) for x in v["rgb"].split(", ")): h for h, v in colors.items() if "rgb" in v}
    for h in colors:
        rgb_set.setdefault(tuple(int(h[i:i + 2], 16) for i in (1, 3, 5)), h)
    counts = {}
    n_files = 0
    for p in active_files(".md", ".svg", ".html", ".json", ".css"):
        if "06_Dependencies" in p.parts:
            continue
        n_files += 1
        text = p.read_text(encoding="utf-8", errors="replace")
        for ln, line in enumerate(text.splitlines(), 1):
            for m in HEX_RE.finditer(line):
                raw = "#" + m.group(1)
                # skip URL fragments / anchors such as (#main) or href="#abc"
                before = line[max(0, m.start() - 12):m.start()]
                if re.search(r"(href=[\"']|\]\(|url\(|[\w/.-])$", before):
                    continue
                if len(m.group(1)) == 3:
                    if p.suffix in (".svg", ".html", ".css", ".json"):
                        rep.fail(c, f"palette.short-hex:{lib_rel(p)}:{raw}",
                                 f"Short hex `{raw}` in `{lib_rel(p)}` line {ln}; B02 §5.1.2 requires `#RRGGBB`.", file=lib_rel(p), line=ln)
                    continue
                up = raw.upper()
                counts[up] = counts.get(up, 0) + 1
                if up not in colors:
                    rep.fail(c, f"palette.off-palette:{lib_rel(p)}:{up}",
                             f"`{raw}` in `{lib_rel(p)}` line {ln} is not a B02 palette value (B02 §5.4.3).", file=lib_rel(p), line=ln)
                elif raw != up:
                    rep.fail(c, f"palette.lowercase:{lib_rel(p)}:{up}",
                             f"`{raw}` in `{lib_rel(p)}` line {ln} is not uppercase (B02 §5.1.2).", file=lib_rel(p), line=ln)
            if p.suffix in (".svg", ".html", ".css"):
                for m in RGB_FN_RE.finditer(line):
                    t = tuple(int(x) for x in m.groups()[:3])
                    if t not in rgb_set:
                        rep.fail(c, f"palette.off-palette-rgb:{lib_rel(p)}:{t}",
                                 f"`{m.group(0)}` in `{lib_rel(p)}` line {ln} is not a B02 palette value.", file=lib_rel(p), line=ln)
    rep.measure(c, files_scanned=n_files, palette_size=len(colors), occurrences=dict(sorted(counts.items())))
    c["summary"] = f"{n_files} files scanned, {sum(counts.values())} hex values against {len(colors)} palette entries"


def flatten_tokens(node, path=()):
    if isinstance(node, dict):
        if "$value" in node:
            yield ".".join(path), node
            return
        for k, v in node.items():
            if k in ("meta", "$extensions", "$schema"):
                continue
            yield from flatten_tokens(v, path + (k,))


def resolve(tokens: dict, value):
    seen = 0
    while isinstance(value, str) and re.fullmatch(r"\{[^}]+\}", value):
        ref = value[1:-1]
        if ref not in tokens or seen > 10:
            return None
        value = tokens[ref]["$value"]
        seen += 1
    return value


def check_tokens(rep: Report, pal: dict) -> dict:
    c = rep.check("token-parity", "Master tokens match B02; embedded copies match the master",
                  ["D01-C2", "D01-C3", "B02-C1"])
    master_path = LIB / "02_Assets/AST-D01-01_Design-Tokens.json"
    master = json.loads(master_path.read_text(encoding="utf-8"))
    toks = dict(flatten_tokens(master))
    colors = pal["colors"]
    n_color = 0
    for name, t in toks.items():
        v = resolve(toks, t["$value"])
        if v is None:
            rep.fail(c, f"token-parity.unresolved:{name}", f"Token `{name}` references `{t['$value']}`, which does not resolve.")
            continue
        if t.get("$type") == "color" or (isinstance(v, str) and v.startswith("#")):
            n_color += 1
            if v not in colors:
                rep.fail(c, f"token-parity.off-palette:{name}", f"Token `{name}` = `{v}` is not in B02.")
                continue
            ext = t.get("$extensions", {})
            if "rgb" in ext and colors[v].get("rgb") and ext["rgb"] != colors[v]["rgb"]:
                rep.fail(c, f"token-parity.rgb:{name}", f"Token `{name}` rgb `{ext['rgb']}` ≠ B02 `{colors[v]['rgb']}`.")
            if "cmykIsoCoatedV2" in ext and ext["cmykIsoCoatedV2"] != colors[v].get("cmyk"):
                rep.fail(c, f"token-parity.cmyk:{name}", f"Token `{name}` CMYK `{ext['cmykIsoCoatedV2']}` ≠ B02 `{colors[v].get('cmyk')}`.")
    # Every B02 colour is represented by a primitive token
    prim_vals = {resolve(toks, t["$value"]) for n, t in toks.items() if n.startswith("primitive.color")}
    for h, info in colors.items():
        if h not in prim_vals:
            rep.fail(c, f"token-parity.missing-primitive:{h}", f"B02 colour {info['name']} `{h}` has no primitive token in AST-D01-01.")
    rep.measure(c, master=lib_rel(master_path), tokens=len(toks), color_tokens=n_color,
                sha256=hashlib.sha256(master_path.read_bytes()).hexdigest())

    # Embedded copies: GENERATED_JSON in HTML publications/templates must equal the master
    css_expected = {}
    for name, t in toks.items():
        tier, *rest = name.split(".")
        if tier in ("semantic", "component"):
            css_expected["--is-" + "-".join(rest)] = resolve(toks, t["$value"])
    for p in active_files(".html"):
        text = p.read_text(encoding="utf-8")
        m = re.search(r'GENERATED_JSON\s*=\s*("(?:[^"\\]|\\.)*")', text)
        if m:
            embedded = json.loads(json.loads(m.group(1)))
            same = embedded == master
            rep.measure(c, embedded_json=lib_rel(p), identical_to_master=same)
            if not same:
                diff = sorted(k for k in set(dict(flatten_tokens(embedded))) ^ set(toks))[:10]
                rep.fail(c, f"token-parity.embedded-json:{lib_rel(p)}",
                         f"Token JSON embedded in `{lib_rel(p)}` differs from AST-D01-01" + (f" (keys: {diff})" if diff else " (values differ)") + ".")
        n_vars = 0
        for vm in re.finditer(r"(--is-[a-z0-9-]+)\s*:\s*([^;\\]+?)\s*(?:;|\\n)", text):
            var, val = vm.group(1), vm.group(2).strip()
            if var in css_expected and isinstance(css_expected[var], str) and css_expected[var].startswith("#"):
                n_vars += 1
                if val.upper() != css_expected[var]:
                    rep.fail(c, f"token-parity.css-var:{lib_rel(p)}:{var}",
                             f"`{var}: {val}` in `{lib_rel(p)}` ≠ token value `{css_expected[var]}`.")
        if n_vars:
            rep.measure(c, css_custom_properties=lib_rel(p), color_vars_compared=n_vars)
    c["summary"] = f"{len(toks)} tokens ({n_color} colour) compared with B02; embedded copies compared with master"
    return toks


def check_contrast(rep: Report, pal: dict, toks: dict):
    c = rep.check("contrast", "WCAG 2.2 contrast of declared colour pairings",
                  ["B02-C5", "D01-C2", "D04-C1", "D04-C2"])
    cfg = json.loads((TOOLS / "contrast-pairs.json").read_text(encoding="utf-8"))

    def col(ref: str) -> str:
        if ref.startswith("#"):
            return ref.upper()
        v = resolve(toks, toks[ref]["$value"]) if ref in toks else None
        if v is None:
            raise KeyError(ref)
        return v

    for pair in cfg["pairs"]:
        try:
            fg, bg = col(pair["fg"]), col(pair["bg"])
        except KeyError as e:
            rep.fail(c, f"contrast.unknown-token:{e}", f"Contrast pair refers to unknown token {e}.")
            continue
        ratio = contrast(fg, bg)
        ok = ratio >= pair["min"]
        rep.measure(c, fg=pair["fg"], fg_hex=fg, bg=pair["bg"], bg_hex=bg, ratio=round(ratio, 2),
                    min=pair["min"], use=pair["use"], clause=pair["clause"], result="pass" if ok else "fail")
        if not ok:
            rep.fail(c, f"contrast.pair:{pair['fg']}|{pair['bg']}",
                     f"{pair['use']}: `{fg}` on `{bg}` = {ratio:.3f}:1, below {pair['min']}:1 ({pair['clause']}).")
    for pair in cfg.get("informative", []):
        fg, bg = col(pair["fg"]), col(pair["bg"])
        rep.measure(c, fg=pair["fg"], fg_hex=fg, bg=pair["bg"], bg_hex=bg, ratio=round(contrast(fg, bg), 2),
                    use=pair["use"], result="informative (no rule applies)")

    # Ratios quoted inside the library must match the maths (to 0.01)
    for claim in cfg.get("stated_ratios", []):
        p = LIB / claim["file"]
        text = p.read_text(encoding="utf-8")
        actual = floor2(contrast(claim["fg"].upper(), claim["bg"].upper()))
        actual_r = round(contrast(claim["fg"].upper(), claim["bg"].upper()), 2)
        present = claim["text"] in text
        rep.measure(c, stated_in=claim["file"], quote=claim["text"], stated=claim["stated"], measured=actual_r)
        if not present:
            rep.fail(c, f"contrast.stated-missing:{claim['file']}:{claim['stated']}",
                     f"Expected quoted ratio text `{claim['text']}` not found in `{claim['file']}`; update tools/contrast-pairs.json.")
        elif abs(actual_r - claim["stated"]) > 0.01 and abs(actual - claim["stated"]) > 0.01:
            rep.fail(c, f"contrast.stated-wrong:{claim['file']}:{claim['stated']}",
                     f"`{claim['file']}` states {claim['stated']}:1 for `{claim['fg']}` on `{claim['bg']}`; measured {actual_r}:1.")
    n = len(cfg["pairs"])
    c["summary"] = f"{n} required pairings, {len(cfg.get('informative', []))} informative, {len(cfg.get('stated_ratios', []))} quoted ratios verified"


def check_links(rep: Report):
    c = rep.check("links", "Relative links and referenced files resolve",
                  ["A02-C5", "A02-C7", "E01-C3"])
    n = 0
    patterns = [
        (".md", re.compile(r"\]\(([^)\s]+)\)")),
        (".html", re.compile(r"""(?:href|src|xlink:href)\s*=\s*["']([^"']+)["']""")),
        (".svg", re.compile(r"""(?:href|xlink:href)\s*=\s*["']([^"']+)["']""")),
        (".html", re.compile(r"""url\(\s*["']?([^"')]+)["']?\s*\)""")),
    ]
    files = active_files(".md", ".html", ".svg") + [REPO / "README.md"]
    for p in files:
        text = p.read_text(encoding="utf-8", errors="replace")
        for ext, rx in patterns:
            if p.suffix != ext:
                continue
            for m in rx.finditer(text):
                target = m.group(1).strip()
                if re.match(r"^(https?:|mailto:|tel:|data:|#|javascript:|blob:|about:)", target) or "${" in target or "{{" in target:
                    continue
                target = unquote(target.split("#")[0].split("?")[0])
                if not target:
                    continue
                n += 1
                dest = (p.parent / target).resolve()
                if not dest.exists():
                    rep.fail(c, f"links.broken:{rel(p)}:{target}", f"`{rel(p)}` links to `{target}`, which does not exist.")
    # Backticked library paths in the register and manifests must exist (unless the row is Planned)
    for doc in [LIB / "Library-Index.md", LIB / "06_Dependencies/Dependencies-Manifest.md"]:
        live = re.split(r"^## \d+\. Revision History", doc.read_text(encoding="utf-8"), flags=re.M)[0]
        for line in live.splitlines():  # revision history describes past paths, so it is skipped
            if "`Planned`" in line or "`Deprecated`" in line or "Retired" in line or "retired" in line:
                continue
            for m in re.finditer(r"`(0[1-6]_[^`*]+\.(?:md|svg|png|ico|json|pdf|html|ttf|icc|txt))`", line):
                n += 1
                if not (LIB / m.group(1)).exists():
                    rep.fail(c, f"links.register-path:{lib_rel(doc)}:{m.group(1)}",
                             f"`{lib_rel(doc)}` references `{m.group(1)}`, which does not exist.")
    c["summary"] = f"{n} relative references resolved"


def pdf_checks(rep: Report, pal: dict, files: list[tuple[Path, bool]] | None = None):
    """Preflight the registered template PDFs, or the given (path, is_print) pairs."""
    c = rep.check("pdf-preflight", "Structural PDF preflight (print PDF/X-4 and digital A4)",
                  ["E03-C1", "E03-C3", "E03-C4", "E01-C4"])
    try:
        import pypdf
        from pypdf.generic import ContentStream
    except ImportError:
        rep.fail(c, "pdf-preflight.pypdf-missing", "pypdf is not installed; run `pip install -r tools/requirements.txt`.")
        return
    colors = pal["colors"]
    cmyk_ok = {tuple(int(x) for x in v["cmyk"].split(", ")): h for h, v in colors.items() if "cmyk" in v}
    cmyk_ok[(0, 0, 0, 0)] = "paper white"
    cmyk_ok[(0, 0, 0, 100)] = "100% K (E03 §5.3.2)"
    rgb_ok = {}
    for h in colors:
        rgb_ok[tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))] = h
    icc = LIB / "06_Dependencies/Color-Profiles/ISOcoated_v2_eci.icc"

    if files is None:
        files = [(p, "-Print" in p.stem) for p in sorted((LIB / "03_Templates").glob("*.pdf"))]
    for p, is_print in files:
        p = Path(p).resolve()
        name = lib_rel(p) if p.is_relative_to(LIB) else p.name
        code = p.name.split("_")[0]
        r = pypdf.PdfReader(str(p))
        root = r.trailer["/Root"]
        info = r.metadata or {}
        m = {"file": name, "kind": "print" if is_print else "digital", "pdf_version": r.pdf_header,
             "pages": len(r.pages), "producer": info.get("/Producer")}

        def F(key, msg):
            rep.fail(c, f"pdf-preflight.{key}:{code}", f"{code}: {msg}")

        if r.is_encrypted:
            F("encrypted", "file is encrypted.")
        if not info.get("/Title"):
            F("no-title", "document information has no Title.")

        # Fonts, colour operators, ink coverage, undefined resources
        fonts, unembedded, undefined, cmyk_used, rgb_used, other_cs = set(), set(), set(), {}, {}, set()
        max_tac = 0.0
        for pi, page in enumerate(r.pages):
            res = page.get("/Resources", {})
            res = res.get_object() if res else {}
            font_res = res.get("/Font", {})
            font_res = font_res.get_object() if font_res else {}
            for fname, fref in font_res.items():
                fo = fref.get_object()
                base = str(fo.get("/BaseFont", fname))
                fonts.add(base)
                if fo.get("/Subtype") == "/Type3":
                    continue
                fd = fo.get("/FontDescriptor")
                if fd is None and "/DescendantFonts" in fo:
                    fd = fo["/DescendantFonts"][0].get_object().get("/FontDescriptor")
                fd = fd.get_object() if fd is not None else {}
                if not any(k in fd for k in ("/FontFile", "/FontFile2", "/FontFile3")):
                    unembedded.add(base)
            for cs_name, cs in (res.get("/ColorSpace", {}) or {}).items():
                other_cs.add(str(cs.get_object()))
            xobj = res.get("/XObject", {})
            for xn, xo in (xobj.get_object() if xobj else {}).items():
                xo = xo.get_object()
                if xo.get("/Subtype") == "/Image":
                    cs = str(xo.get("/ColorSpace"))
                    if is_print and "RGB" in cs:
                        F(f"rgb-image-{xn}", f"image {xn} on page {pi + 1} uses {cs}; print requires CMYK (E03 §5.3.1).")
            content = page.get_contents()
            if content is None:
                continue
            for operands, op in ContentStream(content, r).operations:
                op = op.decode("latin-1") if isinstance(op, bytes) else op
                if op == "Tf":
                    fn = str(operands[0])
                    if fn not in font_res:
                        undefined.add(fn)
                elif op in ("k", "K"):
                    vals = tuple(round(float(x) * 100) for x in operands)
                    cmyk_used[vals] = cmyk_used.get(vals, 0) + 1
                    max_tac = max(max_tac, sum(float(x) for x in operands) * 100)
                elif op in ("rg", "RG"):
                    vals = tuple(round(float(x) * 255) for x in operands)
                    rgb_used[vals] = rgb_used.get(vals, 0) + 1
                elif op in ("cs", "CS", "sc", "SC", "scn", "SCN", "g", "G"):
                    if op in ("cs", "CS"):
                        other_cs.add(str(operands[0]))
                    elif op in ("g", "G") and is_print and float(operands[0]) not in (0.0, 1.0):
                        F("devicegray", "uses DeviceGray tints; use K-only CMYK (E03 §5.3.2).")
        m.update(fonts=sorted(fonts), cmyk_values=sorted(f"{v}" for v in cmyk_used), rgb_values=sorted(f"{v}" for v in rgb_used),
                 max_total_ink_pct=round(max_tac, 1))
        for f in sorted(unembedded):
            F(f"font-not-embedded-{f}", f"font {f} is not embedded (E03 §5.4.1 / E01 §5.4.3).")
        for fn in sorted(undefined):
            F(f"undefined-font-{fn.strip('/')}", f"content stream selects font `{fn}`, which is not in the page resources (preflight error).")
        if not any("Noto" in f for f in fonts):
            F("no-brand-font", "no B03 Noto font found.")

        if is_print:
            if info.get("/GTS_PDFXVersion") != "PDF/X-4":
                F("pdfx-version", f"Info GTS_PDFXVersion is `{info.get('/GTS_PDFXVersion')}`, expected `PDF/X-4` (E03 §5.4.1).")
            meta = root.get("/Metadata")
            xmp = meta.get_object().get_data() if meta is not None else b""
            if b"PDF/X-4" not in xmp:
                F("pdfx-xmp", "XMP metadata does not declare pdfxid:GTS_PDFXVersion PDF/X-4 (required by ISO 15930-7).")
            if str(info.get("/Trapped")) not in ("/True", "/False"):
                F("trapped", f"Trapped key is `{info.get('/Trapped')}`; PDF/X-4 requires True or False.")
            if float(r.pdf_header.split("-")[1]) < 1.6:
                F("pdf-version", f"header {r.pdf_header}; PDF/X-4 requires PDF 1.6 or later.")
            ois = [o.get_object() for o in (root.get("/OutputIntents") or [])]
            x = [o for o in ois if o.get("/S") == "/GTS_PDFX"]
            if len(x) != 1:
                F("output-intent", f"{len(x)} GTS_PDFX OutputIntents; exactly one is required.")
            else:
                o = x[0]
                ident = str(o.get("/OutputConditionIdentifier"))
                prof = o.get("/DestOutputProfile")
                prof_bytes = prof.get_object().get_data() if prof is not None else b""
                desc = prof_bytes[:4096]
                m.update(output_condition=ident, icc_bytes=len(prof_bytes),
                         icc_colorspace=prof_bytes[16:20].decode("latin-1") if prof_bytes else None)
                if "FOGRA39" not in ident:
                    F("output-condition", f"OutputConditionIdentifier `{ident}` is not FOGRA39 (E03 §5.3.1).")
                if not prof_bytes or prof_bytes[16:20] != b"CMYK":
                    F("output-profile", "DestOutputProfile missing or not a CMYK ICC profile.")
            for pi, page in enumerate(r.pages):
                trim = [float(v) for v in page.get("/TrimBox", page.mediabox)]
                bleed = [float(v) for v in page.get("/BleedBox", page.get("/TrimBox", page.mediabox))]
                media = [float(v) for v in page.mediabox]
                tw, th = (trim[2] - trim[0]) / MM, (trim[3] - trim[1]) / MM
                bl = [(trim[0] - bleed[0]) / MM, (trim[1] - bleed[1]) / MM, (bleed[2] - trim[2]) / MM, (bleed[3] - trim[3]) / MM]
                m.setdefault("geometry", []).append({"page": pi + 1, "trim_mm": [round(tw, 2), round(th, 2)],
                                                     "bleed_mm": [round(b, 2) for b in bl]})
                if "/TrimBox" not in page:
                    F(f"no-trimbox-p{pi + 1}", f"page {pi + 1} has no TrimBox.")
                if abs(tw - 210) > 0.5 or abs(th - 297) > 0.5:
                    F(f"trim-p{pi + 1}", f"page {pi + 1} trim is {tw:.2f} × {th:.2f} mm, not A4 (E03 §5.1.1).")
                if any(abs(b - 3) > 0.1 for b in bl):
                    F(f"bleed-p{pi + 1}", f"page {pi + 1} bleed is {[round(b, 2) for b in bl]} mm, expected 3 mm each side (E03 §5.1.4).")
                if bleed[0] < media[0] - 0.01 or bleed[1] < media[1] - 0.01 or bleed[2] > media[2] + 0.01 or bleed[3] > media[3] + 0.01:
                    F(f"bleed-outside-media-p{pi + 1}", f"page {pi + 1} BleedBox extends past MediaBox.")
            if rgb_used:
                F("rgb-operators", f"uses DeviceRGB colour operators {sorted(rgb_used)} in a print file (E03 §5.3.1).")
            if max_tac > 300.5:
                F("tac", f"total ink coverage reaches {max_tac:.0f}%, above 300% (E03 §5.3.5).")
            off = sorted(v for v in cmyk_used if v not in cmyk_ok)
            m["cmyk_not_in_b02"] = [str(v) for v in off]
            if off:
                F("cmyk-off-palette", f"{len(off)} CMYK values are not B02 §5.1.1 or §5.6.1 builds, paper white or 100% K: "
                  + ", ".join(str(v) for v in off) + " (E03 §5.3.1, B02 §5.1.3, §5.6.1).")
        else:
            for pi, page in enumerate(r.pages):
                media = [float(v) for v in page.mediabox]
                w, h = media[2] - media[0], media[3] - media[1]
                m.setdefault("geometry", []).append({"page": pi + 1, "media_mm": [round(w / MM, 2), round(h / MM, 2)]})
                if abs(w - A4_PT[0]) > 0.5 or abs(h - A4_PT[1]) > 0.5:
                    F(f"a4-p{pi + 1}", f"page {pi + 1} is {w / MM:.2f} × {h / MM:.2f} mm, not exact A4 (E01 §5.4.1).")
                for box in ("/TrimBox", "/BleedBox"):
                    if box in page and [round(float(v), 2) for v in page[box]] != [round(v, 2) for v in media]:
                        F(f"bleed-p{pi + 1}", f"page {pi + 1} {box} differs from MediaBox; digital PDFs carry no bleed (E01 §5.4.1).")
            if cmyk_used:
                F("cmyk-operators", "digital PDF uses CMYK operators; E01 §5.4.2 requires sRGB palette values.")
            off = sorted(v for v in rgb_used if not any(max(abs(a - b) for a, b in zip(v, k)) <= 1 for k in rgb_ok))
            m["rgb_not_in_b02"] = [str(v) for v in off]
            if off:
                F("rgb-off-palette", f"{len(off)} RGB values are not B02 palette values: "
                  + ", ".join(str(v) for v in off) + " (E01 §5.4.2).")
        rep.measure(c, **m)
    c["summary"] = "structural preflight only; not a certified PDF/X validation"


def check_press_export(rep: Report):
    """Run tools/press_export.py on each committed press layout sample (E01 §5.3.4)."""
    import tempfile
    c = rep.check("press-export", "Press export of HTML authoring masters to PDF/X-4",
                  ["E01-C3", "E03-C1", "E03-C3", "E03-C4"])
    samples = sorted((TOOLS / "fixtures").glob("*press-layout.pdf"))
    if not samples:
        rep.fail(c, "press-export.no-sample", "no press layout sample in tools/fixtures/.")
        return
    try:
        import press_export
    except ImportError as e:
        rep.fail(c, "press-export.import", f"tools/press_export.py could not be loaded: {e}")
        return
    for src in samples:
        code = src.name.split("_")[0]
        with tempfile.TemporaryDirectory() as tmp:
            try:
                res = press_export.press_export(src, Path(tmp) / "out.pdf", None)
            except press_export.PressError as e:
                rep.fail(c, f"press-export.stopped:{code}", f"{code}: press export stopped: {e}")
                continue
        pf = res["preflight"]
        rep.measure(c, sample=rel(src), geometry=pf.get("geometry"), output_condition=pf.get("output_condition"),
                    cmyk_values=pf.get("cmyk_values"), max_total_ink_pct=pf.get("max_total_ink_pct"),
                    fonts=pf.get("fonts"), pdf_version=pf.get("pdf_version"))
        for f in res["findings"]:
            rep.fail(c, f"press-export.{f['id'].split('.', 1)[1]}", f"press export of {rel(src)}: {f['message']}")


def check_dependencies(rep: Report):
    c = rep.check("dependencies", "Font and ICC checksums match the Dependencies Manifest; licence text present",
                  ["B03-C2", "A02-C10", "E03-C4"])
    man = LIB / "06_Dependencies/Dependencies-Manifest.md"
    rows = table_rows(man.read_text(encoding="utf-8"))
    listed = set()
    for cells in rows:
        path = next((ticks(x) for x in cells if re.fullmatch(r"`06_Dependencies/[^`]+\.(ttf|otf|icc)`", x.strip())), None)
        sha = next((ticks(x) for x in cells if re.fullmatch(r"`[0-9a-f]{64}`", x.strip())), None)
        size = next((int(ticks(x).replace(",", "")) for x in cells if re.fullmatch(r"`[\d,]+`", x.strip())), None)
        if not path or not sha:
            continue
        listed.add(path)
        p = LIB / path
        if not p.exists():
            rep.fail(c, f"dependencies.missing:{path}", f"`{path}` is in the manifest but missing.")
            continue
        data = p.read_bytes()
        got = hashlib.sha256(data).hexdigest()
        rep.measure(c, file=path, bytes=len(data), sha256=got, manifest_sha256=sha, manifest_bytes=size,
                    result="pass" if got == sha and (size is None or size == len(data)) else "fail")
        if got != sha:
            rep.fail(c, f"dependencies.sha256:{path}", f"`{path}` SHA-256 is `{got}`, manifest says `{sha}`.")
        if size is not None and size != len(data):
            rep.fail(c, f"dependencies.size:{path}", f"`{path}` is {len(data):,} bytes, manifest says {size:,}.")
    for p in sorted((LIB / "06_Dependencies").rglob("*")):
        if p.suffix.lower() in (".ttf", ".otf", ".icc") and lib_rel(p) not in listed:
            rep.fail(c, f"dependencies.unlisted:{lib_rel(p)}", f"`{lib_rel(p)}` is not listed with a checksum in the manifest.")
    for d in sorted((LIB / "06_Dependencies/Fonts").iterdir()):
        if not d.is_dir():
            continue
        ofl = d / "OFL.txt"
        if not ofl.exists():
            rep.fail(c, f"dependencies.ofl-missing:{d.name}", f"`{lib_rel(d)}` has no OFL.txt.")
            continue
        t = ofl.read_text(encoding="utf-8", errors="replace")
        markers = ["SIL OPEN FONT LICENSE Version 1.1", "PREAMBLE", "PERMISSION & CONDITIONS", "TERMINATION", "DISCLAIMER"]
        missing = [mk for mk in markers if mk not in t]
        has_copyright = bool(re.search(r"Copyright", t.split("SIL OPEN FONT LICENSE")[0]))
        rep.measure(c, licence=lib_rel(ofl), bytes=len(t.encode()), sections_missing=missing, copyright_line=has_copyright)
        if missing:
            rep.fail(c, f"dependencies.ofl-incomplete:{d.name}", f"`{lib_rel(ofl)}` is missing OFL-1.1 sections {missing}.")
        if not has_copyright:
            rep.fail(c, f"dependencies.ofl-copyright:{d.name}", f"`{lib_rel(ofl)}` has no upstream copyright line before the licence text.")
    c["summary"] = f"{len(listed)} checksummed files compared"


# --------------------------------------------------------------------------- report

def git(*args: str) -> str:
    try:
        return subprocess.check_output(["git", *args], cwd=REPO, text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return ""


def write_reports(rep: Report, out: Path, pal: dict) -> int:
    out.mkdir(parents=True, exist_ok=True)
    failing = sum(1 for c in rep.checks for f in c["findings"] if f["status"] == "fail")
    known = sum(1 for c in rep.checks for f in c["findings"] if f["status"] == "known")
    stale = sorted(set(rep.known) - rep.used_known)
    run_url = None
    if os.environ.get("GITHUB_RUN_ID"):
        run_url = f"{os.environ.get('GITHUB_SERVER_URL', 'https://github.com')}/{os.environ.get('GITHUB_REPOSITORY')}/actions/runs/{os.environ['GITHUB_RUN_ID']}"
    for c in rep.checks:
        st = {f["status"] for f in c["findings"]}
        c["result"] = "fail" if "fail" in st else ("pass with known issues" if "known" in st else "pass")
    meta = {
        "tool": "tools/library_checks.py",
        "generated_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "commit": os.environ.get("GITHUB_SHA") or git("rev-parse", "HEAD"),
        "ref": os.environ.get("GITHUB_REF") or git("rev-parse", "--abbrev-ref", "HEAD"),
        "run_url": run_url,
        "register_version": md_header(LIB / "Library-Index.md").get("Version"),
        "palette_source": pal["source"],
        "verdict": "fail" if failing else "pass",
        "failing_findings": failing,
        "known_issue_findings": known,
        "stale_known_issues": stale,
    }
    (out / "check-report.json").write_text(json.dumps({"meta": meta, "checks": rep.checks}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    L = ["# Library Check Report", ""]
    L += [f"- **Commit:** `{meta['commit']}` ({meta['ref']})", f"- **Generated (UTC):** {meta['generated_utc']}",
          f"- **Register:** `Library-Index.md` `{meta['register_version']}`"]
    if run_url:
        L.append(f"- **CI run:** {run_url}")
    L += [f"- **Verdict:** **{meta['verdict'].upper()}**: {failing} failing finding(s), {known} known issue(s)", ""]
    L += ["| Check | Cites | Result | Scope |", "| :--- | :--- | :--- | :--- |"]
    for c in rep.checks:
        L.append(f"| `{c['id']}` {c['title']} | {', '.join('`' + x + '`' for x in c['cites'])} | {c['result']} | {c.get('summary', '')} |")
    L.append("")
    for c in rep.checks:
        if not c["findings"]:
            continue
        L += [f"## {c['id']}", ""]
        for f in c["findings"]:
            tag = "FAIL" if f["status"] == "fail" else "KNOWN"
            extra = f" (see {f['known_issue']['reference']})" if f["status"] == "known" else ""
            L.append(f"- **{tag}** `{f['id']}`: {f['message']}{extra}")
        L.append("")
    contrast_c = next((c for c in rep.checks if c["id"] == "contrast"), None)
    if contrast_c:
        L += ["## Measured contrast ratios", "", "| Foreground | Background | Ratio | Minimum | Use | Clause |", "| :--- | :--- | ---: | ---: | :--- | :--- |"]
        for m in contrast_c["measurements"]:
            if "bg_hex" in m:
                L.append(f"| `{m['fg_hex']}` | `{m['bg_hex']}` | {m['ratio']:.2f}:1 | {str(m.get('min', '—'))} | {m['use']} | {m.get('clause', 'informative')} |")
        L.append("")
    if stale:
        L += ["## Known-issue entries no longer triggered", "", *[f"- `{s}`: remove from `tools/known-issues.json`" for s in stale], ""]
    L.append("Full measurements are in `check-report.json`. The PDF check is a structural preflight, not a certified PDF/X validation.")
    (out / "check-report.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))
    return 1 if failing else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--report-dir", default="check-report", help="where to write check-report.json and check-report.md")
    args = ap.parse_args()
    known_path = TOOLS / "known-issues.json"
    known = json.loads(known_path.read_text(encoding="utf-8")).get("issues", []) if known_path.exists() else []
    rep = Report(known)
    pal = load_palette()
    check_register(rep)
    check_palette(rep, pal)
    toks = check_tokens(rep, pal)
    check_contrast(rep, pal, toks)
    check_links(rep)
    pdf_checks(rep, pal)
    check_press_export(rep)
    check_dependencies(rep)
    return write_reports(rep, Path(args.report_dir), pal)


if __name__ == "__main__":
    sys.exit(main())
