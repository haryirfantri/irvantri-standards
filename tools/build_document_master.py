#!/usr/bin/env python3
"""Build TPL-E01-06 Formal Document Master (E01 §5.5, E05) as one offline HTML file.

Assembles tools/document-master/master.src.html with:
  * fonts from 06_Dependencies/Fonts/, embedded byte-identical as data URIs (E01 §5.5.8);
  * script libraries from 06_Dependencies/Scripts/, embedded byte-identical (A02 §5.5.4);
  * the AST-B01-03 lockup and AST-B01-01 symbol, inlined;
  * the sample diagram and tools/document-master/app.js.

Usage: python3 tools/build_document_master.py [--check]
  --check  exit 1 if the committed template differs from a fresh build.
"""
import base64
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT / "Standards Design"
SRC = ROOT / "tools/document-master"
OUT = LIB / "03_Templates/TPL-E01-06_Formal-Document-Master.html"

FONTS = [  # family, file, weight, style
    ("Noto Sans Display Local", "Noto Sans Display/NotoSansDisplay-Bold.ttf", 700, "normal"),
    ("Noto Sans Display Local", "Noto Sans Display/NotoSansDisplay-ExtraBold.ttf", 800, "normal"),
    ("Noto Sans Local", "Noto Sans/NotoSans-Regular.ttf", 400, "normal"),
    ("Noto Sans Local", "Noto Sans/NotoSans-Italic.ttf", 400, "italic"),
    ("Noto Sans Local", "Noto Sans/NotoSans-Medium.ttf", 500, "normal"),
    ("Noto Sans Local", "Noto Sans/NotoSans-SemiBold.ttf", 600, "normal"),
    ("Noto Sans Local", "Noto Sans/NotoSans-Bold.ttf", 700, "normal"),
    ("Noto Sans Mono Local", "Noto Sans Mono/NotoSansMono-Regular.ttf", 400, "normal"),
    ("Noto Sans Mono Local", "Noto Sans Mono/NotoSansMono-SemiBold.ttf", 600, "normal"),
]
SCRIPTS = {
    "JS_MARKED": "marked/marked.umd.js",
    "JS_TURNDOWN": "Turndown/turndown.browser.umd.js",
    "JS_GFM": "turndown-plugin-gfm/turndown-plugin-gfm.js",
    "JS_PAGED": "Paged.js/paged.js",
}


def b64(p: Path) -> str:
    return base64.b64encode(p.read_bytes()).decode("ascii")


def inline_svg(p: Path, label: str) -> str:
    s = p.read_text(encoding="utf-8")
    s = re.sub(r"<\?xml[^>]*\?>\s*", "", s)
    s = re.sub(r"<title\b.*?</title>\s*|<desc\b.*?</desc>\s*", "", s, flags=re.S)
    s = re.sub(r'\s(?:aria-labelledby|role)="[^"]*"', "", s)
    s = re.sub(r'\sid="[^"]*"', "", s)
    s = re.sub(r"<svg\b", f'<svg role="img" aria-label="{label}"', s, count=1)
    return re.sub(r">\s+<", "><", s.strip())


def build() -> str:
    html = (SRC / "master.src.html").read_text(encoding="utf-8")
    fonts = "\n".join(
        f"@font-face {{ font-family: '{fam}'; src: url('data:font/ttf;base64,{b64(LIB / '06_Dependencies/Fonts' / f)}') format('truetype'); "
        f"font-weight: {w}; font-style: {st}; font-display: block; }}"
        for fam, f, w, st in FONTS)
    parts = {
        "FONTS": fonts,
        "SYMBOL": inline_svg(LIB / "02_Assets/AST-B01-01_Primary-Symbol.svg", "Irvantri Standards"),
        "LOCKUP": inline_svg(LIB / "02_Assets/AST-B01-03_Parent-Lockup.svg", "Irvantri Standards"),
        "DIAGRAM": (SRC / "authoring-flow.svg").read_text(encoding="utf-8").strip(),
        "APP_JS": (SRC / "app.js").read_text(encoding="utf-8"),
    }
    for k, rel in SCRIPTS.items():
        parts[k] = b64(LIB / "06_Dependencies/Scripts" / rel)
    for k, v in parts.items():
        token = "{{" + k + "}}"
        if token not in html:
            raise SystemExit(f"placeholder {token} missing from master.src.html")
        html = html.replace(token, v)
    left = re.findall(r"\{\{[A-Z_]+\}\}", html)
    if left:
        raise SystemExit(f"unfilled placeholders: {left}")
    return html


def main() -> int:
    html = build()
    if "--check" in sys.argv:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != html:
            print(f"{OUT.relative_to(ROOT)} is out of date; run tools/build_document_master.py")
            return 1
        print("TPL-E01-06 matches its source")
        return 0
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(html.encode()) / 1e6:.2f} MB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
