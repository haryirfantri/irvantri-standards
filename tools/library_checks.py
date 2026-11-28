#!/usr/bin/env python3
"""Automated measurement checks for Standards Design (Irvantri Standards).

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
LIB = REPO / "Standards Design"
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
        if "06_Dependencies" in p.parts or "05_Records" in p.parts:
            continue
        n_files += 1
        text = p.read_text(encoding="utf-8", errors="replace")
        if p.suffix == ".md":
            text = re.split(r"^(?:## (?:\d+(?:\.\d+)?\.|Appendix [A-Z] —).*Revision History|\*\*Table \d+\.\*\* Revision History)", text, flags=re.M)[0]
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
            for m in re.finditer(r"`(0[1-6]_[^`*]+\.(?:md|svg|png|ico|json|pdf|html|css|ttf|icc|txt))`", line):
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
    c = rep.check("dependencies", "Font, ICC and script checksums match the Dependencies Manifest; licence text present",
                  ["B03-C2", "A02-C10", "E03-C4"])
    man = LIB / "06_Dependencies/Dependencies-Manifest.md"
    rows = table_rows(man.read_text(encoding="utf-8"))
    listed = set()
    for cells in rows:
        path = next((ticks(x) for x in cells if re.fullmatch(r"`06_Dependencies/[^`]+\.(ttf|otf|icc|js)`", x.strip())), None)
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
        if p.is_file() and p.suffix.lower() in (".ttf", ".otf", ".icc", ".js") and lib_rel(p) not in listed:
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
    scripts = LIB / "06_Dependencies/Scripts"
    for d in sorted(scripts.iterdir()) if scripts.is_dir() else []:
        if not d.is_dir():
            continue
        lic = next((d / n for n in ("LICENSE", "LICENSE.md", "LICENSE.txt") if (d / n).exists()), None)
        if lic is None:
            rep.fail(c, f"dependencies.licence-missing:{d.name}", f"`{lib_rel(d)}` has no upstream LICENSE file (A02 §5.5.4).")
            continue
        t = lic.read_text(encoding="utf-8", errors="replace")
        mit = "Permission is hereby granted, free of charge" in t and bool(re.search(r"Copyright", t))
        rep.measure(c, licence=lib_rel(lic), bytes=len(t.encode()), mit_text=mit)
        if not mit:
            rep.fail(c, f"dependencies.licence-incomplete:{d.name}", f"`{lib_rel(lic)}` does not carry the MIT permission notice and copyright line.")
    c["summary"] = f"{len(listed)} checksummed files compared"


# --------------------------------------------------------------------------- HTML authoring masters (E01 §5.5)

PROFILE_FROM = {"E01": (2, 5), "E04": (2, 3)}  # first versions carrying the HTML Authoring Master Profile
REMOTE_RE = re.compile(r"""(?:<(?:link|script|img|iframe|source|video|audio)\b[^>]*\b(?:href|src)\s*=\s*["']\s*(?:https?:)?//)"""
                       r"""|(?:url\(\s*["']?\s*(?:https?:)?//)|(?:@import\s+(?:url\()?\s*["']?\s*(?:https?:)?//)""", re.I)
FIELD_RE = re.compile(r"<(textarea|input|[a-z]+[^>]*\bcontenteditable(?:\s*=\s*[\"']?(?:true|plaintext-only)[\"']?)?)\b[^>]*>", re.I)


def html_master_pins() -> list[tuple[str, Path, str, bool]]:
    """(code, file, pin, profile applies) for every HTML template in the register."""
    idx = (LIB / "Library-Index.md").read_text(encoding="utf-8")
    out = []
    for cells in table_rows(idx):
        if len(cells) < 6 or not ticks(cells[0]).startswith("TPL-"):
            continue
        path, pin, status = ticks(cells[2]), ticks(cells[4]), ticks(cells[5])
        if not path.endswith(".html") or status in ("Planned", "Deprecated"):
            continue
        m = re.fullmatch(r"([A-H]\d{2}) \(v(\d+)\.(\d+)\)", pin)
        applies = bool(m and m.group(1) in PROFILE_FROM and (int(m.group(2)), int(m.group(3))) >= PROFILE_FROM[m.group(1)])
        out.append((ticks(cells[0]), LIB / path, pin, applies))
    return out


def measure_html_master(text: str, manifest_sha: set[str]) -> dict:
    """Static measurements for E01 §5.5.3, §5.5.4, §5.5.6–§5.5.9. Behaviour (overflow, keyboard) needs a browser."""
    import base64
    styles = "\n".join(re.findall(r"<style\b[^>]*>(.*?)</style>", text, flags=re.S | re.I)
                       + re.findall(r"<script\b[^>]*\bdata-stylesheet\b[^>]*>(.*?)</script>", text, flags=re.S | re.I))
    styles = re.sub(r"/\*.*?\*/", "", styles, flags=re.S)
    literal = []
    for m in re.finditer(r"(?<![\w-])([a-z-]+)\s*:\s*([^;{}]+)", styles):
        prop, val = m.group(1), m.group(2)
        if prop.startswith("--") or styles[max(0, m.start() - 2):m.start()].endswith("--"):
            continue
        if HEX_RE.search(val) or RGB_FN_RE.search(val):
            literal.append(f"{prop}: {val.strip()[:40]}")
    for m in re.finditer(r"""\bstyle\s*=\s*["']([^"']*)["']""", text):
        if HEX_RE.search(m.group(1)) or RGB_FN_RE.search(m.group(1)):
            literal.append(f"style=\"{m.group(1)[:40]}\"")
    remote = sorted({m.group(0)[:80] for m in REMOTE_RE.finditer(text)})
    fonts, font_fail = [], []
    for m in re.finditer(r"@font-face\s*{(.*?)}", styles, flags=re.S):
        src = re.search(r"""url\(\s*["']?([^"')]+)""", m.group(1))
        ref = src.group(1) if src else ""
        if ref.startswith("data:"):
            sha = hashlib.sha256(base64.b64decode(ref.split(",", 1)[1])).hexdigest()
            fonts.append({"embedded": True, "sha256": sha, "in_manifest": sha in manifest_sha})
            if sha not in manifest_sha:
                font_fail.append(f"embedded font {sha[:12]} is not byte-identical to a 06_Dependencies file")
        else:
            fonts.append({"embedded": False, "ref": ref[:80]})
            font_fail.append(f"font not embedded: {ref[:60]}")
    scripts, script_fail = [], []
    for m in re.finditer(r"""<script\b[^>]*\bsrc\s*=\s*["']data:[^;,"']*;base64,([A-Za-z0-9+/=]+)["'][^>]*>""", text):
        sha = hashlib.sha256(base64.b64decode(m.group(1))).hexdigest()
        dep = re.search(r"""data-dependency\s*=\s*["']([^"']+)""", m.group(0))
        scripts.append({"dependency": dep.group(1) if dep else None, "sha256": sha, "in_manifest": sha in manifest_sha})
        if sha not in manifest_sha:
            script_fail.append(f"embedded script {dep.group(1) if dep else sha[:12]} is not byte-identical to a 06_Dependencies file")
    fields = [f.group(0) for f in FIELD_RE.finditer(text)
              if not re.search(r"""type\s*=\s*["']?(?:button|submit|reset|checkbox|radio|hidden|file|color|range|date)""", f.group(0), re.I)]
    unlimited = [f[:60] for f in fields if not re.search(r"\b(?:maxlength|data-max(?:length|chars)?)\s*=", f, re.I)]
    words = re.sub(r"<[^>]+>", " ", text)
    press = bool(re.search(r"Export press PDF", words))
    return {
        "literal_colors": literal,                                                  # 5.5.3
        "fields": len(fields), "fields_without_limit": unlimited,                  # 5.5.4
        "save_filled_copy": bool(re.search(r"Save filled copy", words, re.I)),      # 5.5.6
        "unsaved_warning": "beforeunload" in text,                                 # 5.5.6
        "press_export": press,
        "press_preview": bool(re.search(r"Press preview", words, re.I)) if press else None,  # 5.5.7
        "remote_requests": remote, "fonts": fonts, "font_failures": font_fail,     # 5.5.8
        "scripts": scripts, "script_failures": script_fail,                        # 5.5.8, A02 §5.5.4
        "aria_live": len(re.findall(r"aria-live\s*=", text)) + len(re.findall(r"""role\s*=\s*["'](?:status|alert)["']""", text)),  # 5.5.9
    }


def check_html_masters(rep: Report):
    c = rep.check("html-master", "HTML authoring master profile: tokens, field limits, saving, press preview, offline single file",
                  ["E01-C5", "E04-C4", "D04-C3"])
    man = (LIB / "06_Dependencies/Dependencies-Manifest.md").read_text(encoding="utf-8")
    manifest_sha = set(re.findall(r"`([0-9a-f]{64})`", man))
    n_applies = 0
    for code, path, pin, applies in html_master_pins():
        if not path.exists():
            continue
        m = measure_html_master(path.read_text(encoding="utf-8"), manifest_sha)
        rep.measure(c, code=code, file=lib_rel(path), pin=pin, profile_applies=applies, **m)
        if not applies:
            continue  # pinned before the profile existed (E01 §5.5.1): measured, never failed
        n_applies += 1
        problems = []
        if m["literal_colors"]:
            problems.append(("literal-color", f"literal colour values in style rules (E01 §5.5.3): {m['literal_colors'][:3]}"))
        if m["fields_without_limit"]:
            problems.append(("field-limit", f"{len(m['fields_without_limit'])} field(s) without a declared character limit (E01 §5.5.4)"))
        if not m["save_filled_copy"]:
            problems.append(("save", "no `Save filled copy` control (E01 §5.5.6)"))
        if not m["unsaved_warning"]:
            problems.append(("unsaved-warning", "no unsaved-changes warning (E01 §5.5.6)"))
        if m["press_export"] and not m["press_preview"]:
            problems.append(("press-preview", "press export without a `Press preview` control (E01 §5.5.7)"))
        if m["remote_requests"]:
            problems.append(("remote", f"requests remote resources (E01 §5.5.8): {m['remote_requests'][:3]}"))
        if m["font_failures"]:
            problems.append(("fonts", f"fonts not embedded byte-identical (E01 §5.5.8): {m['font_failures'][:3]}"))
        if m["script_failures"]:
            problems.append(("scripts", f"script libraries not embedded byte-identical (E01 §5.5.8, A02 §5.5.4): {m['script_failures'][:3]}"))
        if not m["aria_live"]:
            problems.append(("live-region", "no ARIA Live Region for messages (E01 §5.5.9)"))
        for pid, msg in problems:
            rep.fail(c, f"html-master.{pid}:{code}", f"{code}: {msg}.")
    # TPL-E01-06 is generated from tools/document-master/; the committed file must equal a fresh build.
    try:
        import build_document_master as bdm
        if bdm.OUT.exists():
            same = bdm.OUT.read_text(encoding="utf-8") == bdm.build()
            rep.measure(c, code="TPL-E01-06", built_from="tools/document-master/", matches_source=same)
            if not same:
                rep.fail(c, "html-master.build:TPL-E01-06",
                         "TPL-E01-06: the committed template differs from tools/document-master/; run tools/build_document_master.py.")
    except ImportError:
        pass
    c["summary"] = f"{len(html_master_pins())} HTML templates measured; {n_applies} pinned to a profile version and enforced"


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


def check_token_css(rep: Report):
    c = rep.check("token-css", "Generated CSS tokens (AST-D01-02) drift-free, component kit hex-free, and all --is-* vars defined",
                  ["D01-C3", "D03-C1"])
    sys.path.insert(0, str(TOOLS))
    import build_tokens_css as btc
    css_path = LIB / "02_Assets/AST-D01-02_Design-Tokens.css"
    kit_path = LIB / "02_Assets/AST-D03-01_Component-Kit.css"
    defined_vars: set[str] = set()
    if not css_path.exists():
        rep.fail(c, "token-css.missing:AST-D01-02", "`02_Assets/AST-D01-02_Design-Tokens.css` does not exist; run tools/build_tokens_css.py.")
    else:
        same, diff_text, count = btc.check_drift(LIB / "02_Assets/AST-D01-01_Design-Tokens.json", css_path)
        defined_vars = set(re.findall(r"(--is-[a-z0-9-]+)\s*:", css_path.read_text(encoding="utf-8")))
        rep.measure(c, file=lib_rel(css_path), custom_properties=count, drift_free=same)
        if not same:
            rep.fail(c, "token-css.drift:AST-D01-02",
                     "AST-D01-02 differs from AST-D01-01; run `python3 tools/build_tokens_css.py`.", diff=diff_text[:500])
    if kit_path.exists():
        kit_text = kit_path.read_text(encoding="utf-8")
        raw_hex = [m.group(0) for m in HEX_RE.finditer(kit_text)]
        rep.measure(c, file=lib_rel(kit_path), raw_hex_count=len(raw_hex))
        if raw_hex:
            rep.fail(c, "token-css.kit-raw-hex:AST-D03-01",
                     f"AST-D03-01 contains raw hexadecimal color(s): {raw_hex[:5]} (D01 §5.3.1).")
    # Every var(--is-...) used in kit, gallery, and HTML templates must resolve to AST-D01-02 or a local declaration
    if defined_vars:
        consumers = [p for p in [kit_path, LIB / "02_Assets/AST-D03-02_Component-Gallery.html"] if p.exists()]
        tpl_dir = LIB / "03_Templates"
        if tpl_dir.exists():
            consumers.extend(sorted(tpl_dir.glob("*.html")))
        checked_refs = 0
        for p in consumers:
            text = p.read_text(encoding="utf-8", errors="replace")
            local_defs = set(re.findall(r"(--is-[a-z0-9-]+)\s*:", text))
            used = sorted(set(re.findall(r"var\(\s*(--is-[a-z0-9-]+)\s*[,)]", text)))
            checked_refs += len(used)
            undefined = [v for v in used if v not in defined_vars and v not in local_defs]
            rep.measure(c, file=lib_rel(p), is_vars_used=len(used), undefined=undefined)
            for v in undefined:
                rep.fail(c, f"token-css.undefined-var:{lib_rel(p)}:{v}",
                         f"`{lib_rel(p)}` uses `var({v})`, which is not declared in AST-D01-02 or locally (D01 §5.3.1).")
        c["summary"] = f"AST-D01-02 drift-free; AST-D03-01 hex-free; {checked_refs} --is-* references resolved across {len(consumers)} files"
    else:
        c["summary"] = "AST-D01-02 missing; AST-D03-01 verified hex-free"


def _load_standards_from_index() -> dict[str, dict]:
    idx = (LIB / "Library-Index.md").read_text(encoding="utf-8")
    sec4 = idx.split("## 4.", 1)[1].split("## 5.", 1)[0]
    stds: dict[str, dict] = {}
    for cells in table_rows(sec4):
        if len(cells) < 7:
            continue
        code = ticks(cells[0])
        if re.fullmatch(r"[A-H]\d{2}", code):
            stds[code] = {
                "path": ticks(cells[2]),
                "version": ticks(cells[3]),
                "status": ticks(cells[4]),
                "next_review": ticks(cells[6]),
            }
    return stds


def check_readme_sync(rep: Report):
    c = rep.check("readme-sync", "README.md register version and counts match Library-Index.md",
                  ["A01 §5.8.1"])
    sys.path.insert(0, str(TOOLS))
    import build_readme
    readme_path = REPO / "README.md"
    if not readme_path.exists():
        rep.fail(c, "readme-sync.missing", "README.md does not exist.")
        return
    try:
        same, diff_text, stats = build_readme.check_drift(LIB / "Library-Index.md", readme_path)
    except ValueError as e:
        rep.fail(c, "readme-sync.markers", str(e))
        return
    rep.measure(c, register=stats["version"], standards=len(stats["stds"]),
                assets=len(stats["assets"]), templates_active=len(stats["tpls_active"]),
                publications=len(stats["pubs"]), records=len(stats["recs"]), drift_free=same)
    if not same:
        rep.fail(c, "readme-sync.drift",
                 "README.md stats differ from Library-Index.md; run `python3 tools/build_readme.py`.",
                 diff=diff_text[:500])
    c["summary"] = f"README.md checked against Library-Index.md ({stats['version']})"


def check_pin_sync(rep: Report):
    c = rep.check("pin-sync", "AST-/TPL- pins match governing standard MAJOR version and Section 7",
                  ["A01 §5.5.3", "A01 §5.7.4", "A02 §5.7.2"])
    idx = (LIB / "Library-Index.md").read_text(encoding="utf-8")
    stds = _load_standards_from_index()
    sec5 = idx.split("## 5.", 1)[1].split("## 6.", 1)[0]

    # Parse Section 7 tables from governing standards once
    sec7_cache: dict[str, dict[str, tuple[str, str]]] = {}
    for scode, info in stds.items():
        p = LIB / info["path"]
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        if "## 7." not in text or "## 8." not in text:
            continue
        sec7 = text.split("## 7.", 1)[1].split("## 8.", 1)[0]
        rows_map: dict[str, tuple[str, str]] = {}
        for r in table_rows(sec7):
            if len(r) >= 5 and re.fullmatch(r"(?:AST|TPL)-[A-H]\d{2}-\d{2}", ticks(r[0])):
                rows_map[ticks(r[0])] = (ticks(r[3]), ticks(r[4]))
        sec7_cache[scode] = rows_map

    checked = 0
    for cells in table_rows(sec5):
        if len(cells) < 6:
            continue
        code = ticks(cells[0])
        if not re.fullmatch(r"(?:AST|TPL)-[A-H]\d{2}-\d{2}", code):
            continue
        gov, pin, status = ticks(cells[3]), ticks(cells[4]), ticks(cells[5])
        if status in ("Planned", "Deprecated"):
            continue
        checked += 1
        std = stds.get(gov)
        if not std:
            rep.fail(c, f"pin-sync.unknown-std:{code}", f"{code} references unknown governing standard `{gov}`.")
            continue
        pm = re.fullmatch(r"([A-H]\d{2})\s*\(v(\d+)\.(\d+)\)", pin)
        sm = re.fullmatch(r"v(\d+)\.(\d+)\.\d+", std["version"])
        if not pm or pm.group(1) != gov:
            rep.fail(c, f"pin-sync.format:{code}", f"{code} pin `{pin}` does not match `{gov} (vMAJOR.MINOR)` (A01 §5.7.4).")
            continue
        p_maj, p_min = int(pm.group(2)), int(pm.group(3))
        s_maj, s_min = int(sm.group(1)), int(sm.group(2))
        rep.measure(c, code=code, governing=gov, pin=pin, std_version=std["version"], status=status)
        if (p_maj, p_min) > (s_maj, s_min):
            rep.fail(c, f"pin-sync.ahead:{code}", f"{code} pin `{pin}` is ahead of {gov} `{std['version']}`.")
        elif p_maj < s_maj and status != "Sync Required":
            rep.fail(c, f"pin-sync.major-drift:{code}",
                     f"{code} is pinned to `{pin}` but {gov} is `{std['version']}`; status must be `Sync Required` (A01 §5.5.3).")
        sec7_entry = sec7_cache.get(gov, {}).get(code)
        if sec7_entry is None:
            rep.fail(c, f"pin-sync.missing-sec7:{code}", f"{code} is not listed in {gov} Section 7 Linked Artifacts (A01 §5.7.4).")
        elif sec7_entry != (pin, status):
            rep.fail(c, f"pin-sync.sec7-mismatch:{code}",
                     f"{code} in Library-Index.md (`{pin}`, `{status}`) differs from {gov} Section 7 (`{sec7_entry[0]}`, `{sec7_entry[1]}`).")
    c["summary"] = f"{checked} active AST-/TPL- pins verified against governing standards and Section 7"


def check_pub_manifests(rep: Report):
    c = rep.check("pub-manifest", "Compiled publication manifests cite current source standards and precedence notice",
                  ["A01-C10", "A01 §5.7.5"])
    idx = (LIB / "Library-Index.md").read_text(encoding="utf-8")
    stds = _load_standards_from_index()
    sec6 = idx.split("## 6.", 1)[1].split("## 7.", 1)[0]
    checked_pubs = checked_refs = 0
    for cells in table_rows(sec6):
        if len(cells) < 6:
            continue
        pcode = ticks(cells[0])
        if not re.fullmatch(r"PUB-\d{2}", pcode):
            continue
        fpath, compiled_date, manifest, status = ticks(cells[2]), ticks(cells[3]), cells[4], ticks(cells[5])
        if status in ("Planned", "Deprecated"):
            continue
        checked_pubs += 1
        refs = re.findall(r"`([A-H]\d{2})\s*\((v\d+\.\d+\.\d+)\)`", manifest)
        for sc, sv in refs:
            checked_refs += 1
            live = stds.get(sc, {}).get("version")
            if live and live != sv and status == "Approved":
                rep.fail(c, f"pub-manifest.stale-ref:{pcode}:{sc}",
                         f"{pcode} Source Manifest cites `{sc} ({sv})`, but live {sc} is `{live}` (A01 §5.7.5).")
        p = LIB / fpath
        if p.exists():
            text = p.read_text(encoding="utf-8", errors="replace")
            has_notice = bool(re.search(r"prevail", text, re.I))
            has_date = compiled_date in text
            rep.measure(c, code=pcode, refs=len(refs), compiled_date=compiled_date,
                        precedence_notice=has_notice, date_present=has_date)
            if not has_notice:
                rep.fail(c, f"pub-manifest.no-precedence:{pcode}",
                         f"{pcode} (`{fpath}`) is missing a visible precedence notice (A01 §5.7.5).")
            if not has_date:
                rep.fail(c, f"pub-manifest.no-date:{pcode}",
                         f"{pcode} (`{fpath}`) does not contain its registered compile date `{compiled_date}` (A01 §5.7.5).")
    c["summary"] = f"{checked_pubs} publications checked ({checked_refs} source standard references verified)"


def check_revision_history(rep: Report):
    c = rep.check("revision-history", "Newest Revision History row matches document header Version",
                  ["A01 §5.2", "A01 §5.5.5"])
    stds = _load_standards_from_index()
    checked = 0
    for code, info in sorted(stds.items()):
        if info["status"] in ("Planned", "Deprecated"):
            continue
        p = LIB / info["path"]
        if not p.exists():
            continue
        checked += 1
        text = p.read_text(encoding="utf-8")
        hdr_ver = md_header(p).get("Version")
        parts = re.split(r"^##\s+8\.\s+Revision History", text, maxsplit=1, flags=re.M)
        if len(parts) < 2:
            rep.fail(c, f"revision-history.missing:{code}", f"{code} is missing Section 8 Revision History.")
            continue
        m = re.search(r"^\|\s*`(v\d+\.\d+\.\d+)`\s*\|", parts[1], re.M)
        top_ver = m.group(1) if m else None
        rep.measure(c, code=code, header=hdr_ver, newest_row=top_ver)
        if top_ver != hdr_ver:
            rep.fail(c, f"revision-history.mismatch:{code}",
                     f"{code} header Version is `{hdr_ver}` but newest Section 8 row is `{top_ver}`.")
    # Also check Library-Index.md Section 10
    idx_path = LIB / "Library-Index.md"
    idx_text = idx_path.read_text(encoding="utf-8")
    idx_ver = md_header(idx_path).get("Version")
    parts = re.split(r"^##\s+10\.\s+Revision History", idx_text, maxsplit=1, flags=re.M)
    top_idx = re.search(r"^\|\s*`(v\d+\.\d+\.\d+)`\s*\|", parts[1], re.M).group(1) if len(parts) > 1 else None
    checked += 1
    rep.measure(c, code="Library-Index.md", header=idx_ver, newest_row=top_idx)
    if top_idx != idx_ver:
        rep.fail(c, "revision-history.mismatch:Library-Index.md",
                 f"Library-Index.md header Version is `{idx_ver}` but newest Section 10 row is `{top_idx}`.")
    c["summary"] = f"{checked} documents verified (header Version == newest Revision History row)"


def check_review_due(rep: Report, today: dt.date | None = None):
    c = rep.check("review-due", "Standard Next Review dates and active waiver Expiry Dates are current",
                  ["A01 §5.6.5", "A04 §5.1.3", "A04 §5.4.9"])
    today = today or dt.date.today()
    stds = _load_standards_from_index()
    checked_stds = upcoming = 0
    for code, info in sorted(stds.items()):
        if info["status"] != "Approved":
            continue
        checked_stds += 1
        raw = info["next_review"]
        try:
            due = dt.date.fromisoformat(raw)
        except ValueError:
            rep.fail(c, f"review-due.bad-date:{code}", f"{code} has invalid Next Review date `{raw}`.")
            continue
        days_left = (due - today).days
        rep.measure(c, code=code, next_review=raw, days_remaining=days_left)
        if days_left < -30:
            rep.fail(c, f"review-due.overdue:{code}",
                     f"{code} Next Review `{raw}` is overdue by {-days_left} days (> 30 calendar days, A01 §5.6.5).")
        elif days_left <= 30:
            upcoming += 1

    idx = (LIB / "Library-Index.md").read_text(encoding="utf-8")
    sec7 = idx.split("## 7.", 1)[1].split("## 8.", 1)[0]
    checked_recs = 0
    for cells in table_rows(sec7):
        if len(cells) < 7:
            continue
        rcode = ticks(cells[0])
        if not re.fullmatch(r"REC-[A-H]\d{2}-\d{3}", rcode):
            continue
        status, expiry = ticks(cells[5]), ticks(cells[6])
        checked_recs += 1
        if status in ("Open", "Approved") and expiry and expiry.lower() != "none":
            try:
                exp = dt.date.fromisoformat(expiry)
            except ValueError:
                rep.fail(c, f"review-due.bad-expiry:{rcode}", f"{rcode} has invalid Expiry Date `{expiry}`.")
                continue
            rep.measure(c, code=rcode, status=status, expiry_date=expiry, days_remaining=(exp - today).days)
            if exp < today:
                rep.fail(c, f"review-due.waiver-expired:{rcode}",
                         f"{rcode} (`{status}`) passed Expiry Date `{expiry}` without closure or renewal (A04 §5.4.9).")
    c["summary"] = f"{checked_stds} standard review dates ({upcoming} due within 30d) and {checked_recs} governance records checked"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--report-dir", default="check-report", help="where to write check-report.json and check-report.md")
    args = ap.parse_args()
    known_path = TOOLS / "known-issues.json"
    known = json.loads(known_path.read_text(encoding="utf-8")).get("issues", []) if known_path.exists() else []
    rep = Report(known)
    pal = load_palette()
    check_register(rep)
    check_readme_sync(rep)
    check_pin_sync(rep)
    check_pub_manifests(rep)
    check_revision_history(rep)
    check_review_due(rep)
    check_palette(rep, pal)
    toks = check_tokens(rep, pal)
    check_token_css(rep)
    check_contrast(rep, pal, toks)
    check_links(rep)
    pdf_checks(rep, pal)
    check_press_export(rep)
    check_html_masters(rep)
    check_dependencies(rep)
    return write_reports(rep, Path(args.report_dir), pal)


if __name__ == "__main__":
    sys.exit(main())
