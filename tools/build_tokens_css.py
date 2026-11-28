#!/usr/bin/env python3
"""Generate CSS custom properties from the D01 master token file (AST-D01-01).

Usage (from the repository root):
  python3 tools/build_tokens_css.py
  python3 tools/build_tokens_css.py --check
  python3 tools/build_tokens_css.py TOKENS.json OUT.css [--date YYYY-MM-DD]
  python3 tools/build_tokens_css.py TOKENS.json --check EXISTING.css

Rules applied (D01 §5.1–§5.3):
  * 5.1.1 three tiers: primitives are resolved; semantic and component tiers are emitted.
  * 5.1.2 names come from each token's $extensions.cssVar and must match --is-[a-z0-9-]+.
  * 5.3.1 the CSS is generated, never edited by hand; --check proves zero drift.
"""
from __future__ import annotations

import datetime
import difflib
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT / "Standards Design"
DEFAULT_SRC = LIB / "02_Assets/AST-D01-01_Design-Tokens.json"
DEFAULT_OUT = LIB / "02_Assets/AST-D01-02_Design-Tokens.css"


def flatten(node, path=()):
    if isinstance(node, dict):
        if "$value" in node:
            yield ".".join(path), node
            return
        for k, v in node.items():
            if k in ("meta", "$schema", "$extensions"):
                continue
            yield from flatten(v, path + (k,))


def resolve(toks, v, depth=0):
    while isinstance(v, str) and re.fullmatch(r"\{[^}]+\}", v):
        ref = v[1:-1]
        if ref not in toks or depth > 10:
            raise SystemExit(f"Unresolved reference {v}")
        v = toks[ref]["$value"]
        depth += 1
    return v


def build(master: dict, date: str) -> str:
    toks = dict(flatten(master))
    meta = master["meta"]
    out = [
        "/*",
        " * Standards Design (Irvantri Standards Design System) — Generated CSS Custom Properties",
        f" * Single Source: {meta['file']} | Pinned: {meta['pinnedVersion']}",
        f" * Compiled: {date} | Generated programmatically by tools/build_tokens_css.py; do not edit manually (D01 §5.3.1)",
        " */",
        ":root {",
    ]
    seen = set()
    for tier, label in (("semantic", "Semantic Tier"), ("component", "Component Tier")):
        out.append(f"  /* {label} */")
        for name, t in toks.items():
            if not name.startswith(tier + "."):
                continue
            var = t.get("$extensions", {}).get("cssVar")
            if not var or not re.fullmatch(r"--is-[a-z0-9]+(-[a-z0-9]+)*", var):
                raise SystemExit(f"{name}: missing or invalid cssVar {var!r} (D01 §5.1.2)")
            if var in seen:
                raise SystemExit(f"Duplicate custom property {var}")
            seen.add(var)
            out.append(f"  {var}: {resolve(toks, t['$value'])};")
    out.append("}")
    return "\n".join(out)


def check_drift(src: Path = DEFAULT_SRC, css_path: Path = DEFAULT_OUT) -> tuple[bool, str, int]:
    master = json.loads(src.read_text(encoding="utf-8"))
    existing = css_path.read_text(encoding="utf-8")
    m = re.search(r"Compiled: (\d{4}-\d{2}-\d{2})", existing)
    expected = build(master, m.group(1) if m else master.get("meta", {}).get("generatedDate", ""))
    same = existing.rstrip("\n") == expected
    diff_text = ""
    if not same:
        diff_text = "".join(
            difflib.unified_diff(
                expected.splitlines(True),
                existing.rstrip("\n").splitlines(True),
                "generated",
                "existing",
            )
        )
    return same, diff_text, expected.count("--is-")


def main(argv: list[str]) -> int:
    args = argv[1:]
    if not args:
        src, out_path, check_mode = DEFAULT_SRC, DEFAULT_OUT, False
        date = None
    elif args == ["--check"]:
        src, out_path, check_mode = DEFAULT_SRC, DEFAULT_OUT, True
        date = None
    else:
        src = Path(args[0])
        check_mode = "--check" in args
        if check_mode:
            idx = args.index("--check")
            out_path = Path(args[idx + 1]) if idx + 1 < len(args) else DEFAULT_OUT
            date = None
        else:
            out_path = Path(args[1]) if len(args) > 1 and not args[1].startswith("--") else DEFAULT_OUT
            date = args[args.index("--date") + 1] if "--date" in args else None

    if check_mode:
        same, diff_text, count = check_drift(src, out_path)
        print(f"drift-free: {same} ({count} custom properties)")
        if diff_text:
            sys.stdout.write(diff_text)
        return 0 if same else 1

    master = json.loads(src.read_text(encoding="utf-8"))
    compile_date = date or master.get("meta", {}).get("generatedDate") or datetime.date.today().isoformat()
    css = build(master, compile_date) + "\n"
    out_path.write_text(css, encoding="utf-8")
    sha = hashlib.sha256(src.read_bytes()).hexdigest()
    print(f"wrote {out_path}: {css.count('--is-')} custom properties, source sha256 {sha}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
