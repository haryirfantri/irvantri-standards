#!/usr/bin/env python3
"""Synchronize embedded design tokens inside PUB-01_Brand-and-Design-System-Guide.html.

Updates:
  * `const GENERATED_CSS = ...` from `02_Assets/AST-D01-02_Design-Tokens.css`
  * `const GENERATED_JSON = ...` from `02_Assets/AST-D01-01_Design-Tokens.json`
  * CSS download filename (`AST-D01-02_Design-Tokens.css`)

Usage (from the repository root):
    python3 tools/sync_pub01.py          # updates PUB-01 in place
    python3 tools/sync_pub01.py --check  # exit 1 on drift
"""
from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT / "Standards Design"
DEFAULT_JSON = LIB / "02_Assets/AST-D01-01_Design-Tokens.json"
DEFAULT_CSS = LIB / "02_Assets/AST-D01-02_Design-Tokens.css"
DEFAULT_PUB01 = LIB / "04_Publications/PUB-01_Brand-and-Design-System-Guide.html"

GEN_CSS_RE = re.compile(r'^(  const GENERATED_CSS = )"(?:[^"\\]|\\.)*";?$', re.M)
GEN_JSON_RE = re.compile(r'^(  const GENERATED_JSON = )"(?:[^"\\]|\\.)*";?$', re.M)
CSS_DL_RE = re.compile(r"downloadFile\('AST-D01-01_Design-Tokens\.css',\s*GENERATED_CSS")


def render_pub01(pub_text: str, json_text: str, css_text: str) -> str:
    css_literal = json.dumps(css_text.rstrip("\n") + "\n")
    json_literal = json.dumps(json_text.rstrip("\n") + "\n")

    out, n1 = GEN_CSS_RE.subn(lambda m: m.group(1) + css_literal + ";", pub_text, count=1)
    if n1 != 1:
        raise ValueError("Could not find `const GENERATED_CSS = ...` in PUB-01")
    out, n2 = GEN_JSON_RE.subn(lambda m: m.group(1) + json_literal + ";", out, count=1)
    if n2 != 1:
        raise ValueError("Could not find `const GENERATED_JSON = ...` in PUB-01")
    out = CSS_DL_RE.sub("downloadFile('AST-D01-02_Design-Tokens.css', GENERATED_CSS", out)
    return out


def check_drift(
    pub_path: Path = DEFAULT_PUB01,
    json_path: Path = DEFAULT_JSON,
    css_path: Path = DEFAULT_CSS,
) -> tuple[bool, str]:
    current = pub_path.read_text(encoding="utf-8")
    expected = render_pub01(
        current,
        json_path.read_text(encoding="utf-8"),
        css_path.read_text(encoding="utf-8"),
    )
    if current == expected:
        return True, ""
    diff = "".join(difflib.unified_diff(
        current.splitlines(keepends=True),
        expected.splitlines(keepends=True),
        fromfile=pub_path.name,
        tofile=f"{pub_path.name} (expected)",
        n=1,
    ))
    return False, diff


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pub01", type=Path, default=DEFAULT_PUB01)
    ap.add_argument("--tokens-json", type=Path, default=DEFAULT_JSON)
    ap.add_argument("--tokens-css", type=Path, default=DEFAULT_CSS)
    ap.add_argument("--check", action="store_true", help="exit 1 if PUB-01 embedded tokens or download filename drifted")
    args = ap.parse_args(argv)

    if args.check:
        same, diff = check_drift(args.pub01, args.tokens_json, args.tokens_css)
        if same:
            print("PUB-01 embedded tokens and download filename are in sync")
            return 0
        print("PUB-01 is out of sync; run `python3 tools/sync_pub01.py`:\n" + diff[:1500], file=sys.stderr)
        return 1

    updated = render_pub01(
        args.pub01.read_text(encoding="utf-8"),
        args.tokens_json.read_text(encoding="utf-8"),
        args.tokens_css.read_text(encoding="utf-8"),
    )
    args.pub01.write_text(updated, encoding="utf-8")
    print(f"Synced embedded tokens and CSS download filename in {args.pub01}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
