#!/usr/bin/env python3
"""Synchronize generated register stats in README.md from Library-Index.md.

Updates the content between:
  <!-- BEGIN:README-STATUS --> ... <!-- END:README-STATUS -->
  <!-- BEGIN:README-COUNTS --> ... <!-- END:README-COUNTS -->

Usage (from the repository root):
    python3 tools/build_readme.py          # updates README.md in place
    python3 tools/build_readme.py --check  # exit 1 on drift
"""
from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INDEX = ROOT / "Standards Design" / "Library-Index.md"
DEFAULT_README = ROOT / "README.md"

STATUS_RE = re.compile(r"(<!-- BEGIN:README-STATUS -->\n).*?(\n<!-- END:README-STATUS -->)", re.S)
COUNTS_RE = re.compile(r"(<!-- BEGIN:README-COUNTS -->\n).*?(\n<!-- END:README-COUNTS -->)", re.S)


def _ticks(cell: str) -> str:
    m = re.search(r"`([^`]*)`", cell)
    return m.group(1) if m else cell.strip()


def _table_rows(text: str) -> list[list[str]]:
    rows = []
    for line in text.splitlines():
        if line.startswith("|") and not re.match(r"^\|\s*:?-{3,}", line):
            rows.append([c.strip() for c in line.strip().strip("|").split("|")])
    return rows


def parse_index_stats(index_text: str) -> dict:
    """Extract live version, dates, counts, and code ranges from Library-Index.md."""
    header: dict[str, str] = {}
    for line in index_text.splitlines()[:30]:
        m = re.match(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.*?)\s*\|\s*$", line)
        if m:
            header[m.group(1).strip()] = m.group(2).strip().strip("`").strip()

    sec4 = index_text.split("## 4.", 1)[1].split("## 5.", 1)[0]
    sec5 = index_text.split("## 5.", 1)[1].split("## 6.", 1)[0]
    sec6 = index_text.split("## 6.", 1)[1].split("## 7.", 1)[0]
    sec7 = index_text.split("## 7.", 1)[1].split("## 8.", 1)[0]

    stds = []
    for r in _table_rows(sec4):
        if len(r) >= 5 and re.fullmatch(r"[A-H]\d{2}", _ticks(r[0])):
            if _ticks(r[4]) != "Deprecated":
                stds.append(_ticks(r[0]))

    assets_active = []
    tpls_active, tpls_planned = [], []
    for r in _table_rows(sec5):
        if len(r) < 6:
            continue
        code, status = _ticks(r[0]), _ticks(r[5])
        if code.startswith("AST-") and status not in ("Deprecated", "Planned"):
            assets_active.append(code)
        elif code.startswith("TPL-"):
            if status == "Planned":
                tpls_planned.append(code)
            elif status != "Deprecated":
                tpls_active.append(code)

    pubs = []
    for r in _table_rows(sec6):
        if len(r) >= 6 and re.fullmatch(r"PUB-\d{2}", _ticks(r[0])):
            if _ticks(r[5]) != "Deprecated":
                pubs.append(_ticks(r[0]))

    recs = []
    for r in _table_rows(sec7):
        if len(r) >= 6 and re.fullmatch(r"REC-[A-H]\d{2}-\d{3}", _ticks(r[0])):
            recs.append(_ticks(r[0]))

    series = sorted({c[0] for c in stds})
    return {
        "version": header.get("Version", ""),
        "status": header.get("Status", ""),
        "last_updated": header.get("Last Updated", ""),
        "stds": stds,
        "series_range": f"{series[0]}–{series[-1]}" if len(series) > 1 else (series[0] if series else ""),
        "std_range": f"`{stds[0]}`–`{stds[-1]}`" if len(stds) > 1 else (f"`{stds[0]}`" if stds else ""),
        "assets": assets_active,
        "tpls_active": tpls_active,
        "tpls_planned": tpls_planned,
        "pubs": pubs,
        "recs": recs,
    }


def render_blocks(stats: dict) -> tuple[str, str]:
    status_line = (
        f"> **Status:** {stats['status']} · **Register:** `{stats['version']}` "
        f"· **Last updated:** {stats['last_updated']}"
    )

    pub_range = f"`{stats['pubs'][0]}`–`{stats['pubs'][-1]}`" if len(stats["pubs"]) > 1 else f"`{stats['pubs'][0]}`"
    rec_last = stats["recs"][-1].rsplit("-", 1)[-1] if stats["recs"] else ""
    rec_range = f"`{stats['recs'][0]}`–`{rec_last}`" if len(stats["recs"]) > 1 else f"`{stats['recs'][0]}`"
    planned_note = (
        f"; {', '.join(f'`{t}`' for t in stats['tpls_planned'])} `Planned`"
        if stats["tpls_planned"] else ""
    )

    table = "\n".join([
        "| Resource | Count | Purpose |",
        "| --- | ---: | --- |",
        f"| Normative standards | {len(stats['stds'])} | Binding rules across active Series {stats['series_range']} ({stats['std_range']}) |",
        f"| Master assets | {len(stats['assets'])} | Canonical marks, favicons/app icons, design tokens (`JSON` + `CSS`), component kit, and gallery |",
        f"| Executable templates | {len(stats['tpls_active'])} active | Single-file `HTML` authoring masters (`TPL-E01-03`, `TPL-E01-06`) and official letterheads (`TPL-E04-01`/`03`){planned_note} |",
        f"| Compiled publications | {len(stats['pubs'])} | Human-facing and AI-facing reference documents ({pub_range}) |",
        f"| Governance records | {len(stats['recs'])} | Reviews, audits, and measured Pre-Release Gates ({rec_range}) |",
    ])
    return status_line, table


def render_readme(readme_text: str, index_text: str) -> str:
    stats = parse_index_stats(index_text)
    status_block, counts_block = render_blocks(stats)
    if not STATUS_RE.search(readme_text) or not COUNTS_RE.search(readme_text):
        raise ValueError("README.md is missing BEGIN/END README-STATUS or README-COUNTS markers.")
    out = STATUS_RE.sub(lambda m: m.group(1) + status_block + m.group(2), readme_text, count=1)
    out = COUNTS_RE.sub(lambda m: m.group(1) + counts_block + m.group(2), out, count=1)
    return out


def check_drift(index_path: Path = DEFAULT_INDEX, readme_path: Path = DEFAULT_README) -> tuple[bool, str, dict]:
    index_text = index_path.read_text(encoding="utf-8")
    current = readme_path.read_text(encoding="utf-8")
    expected = render_readme(current, index_text)
    stats = parse_index_stats(index_text)
    if current == expected:
        return True, "", stats
    diff = "".join(difflib.unified_diff(
        current.splitlines(keepends=True),
        expected.splitlines(keepends=True),
        fromfile=readme_path.name,
        tofile=f"{readme_path.name} (expected)",
    ))
    return False, diff, stats


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--index", type=Path, default=DEFAULT_INDEX, help="path to Library-Index.md")
    ap.add_argument("--readme", type=Path, default=DEFAULT_README, help="path to README.md")
    ap.add_argument("--check", action="store_true", help="exit 1 if README.md differs from generated stats")
    args = ap.parse_args(argv)

    if args.check:
        same, diff, stats = check_drift(args.index, args.readme)
        if same:
            print(f"README.md matches Library-Index.md ({stats['version']})")
            return 0
        print("README.md is out of sync with Library-Index.md; run `python3 tools/build_readme.py`:\n" + diff, file=sys.stderr)
        return 1

    index_text = args.index.read_text(encoding="utf-8")
    updated = render_readme(args.readme.read_text(encoding="utf-8"), index_text)
    args.readme.write_text(updated, encoding="utf-8")
    stats = parse_index_stats(index_text)
    print(f"Updated {args.readme} from Library-Index.md ({stats['version']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
