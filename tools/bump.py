#!/usr/bin/env python3
"""Bump a normative standard or Library-Index.md version cleanly (A01 §5.5, §5.8).

Automates the repetitive metadata edits for a release:
  1. Increments `vMAJOR.MINOR.ERRATA` in the target's header (`Effective Date`
     on standards; `Last Updated` on `Library-Index.md`).
  2. Prepends a Revision History row (Section 8 on standards; Section 10 on
     `Library-Index.md`).
  3. Synchronizes the standard's row in `Library-Index.md` (and bumps the
     register version by `errata` unless `--no-index-bump` is passed).
  4. On a `MAJOR` bump (`A01 §5.5.3`), marks dependent `AST-`/`TPL-` items
     pinned to the prior `MAJOR` as `Sync Required` in both `Library-Index.md`
     and the standard's Section 7, and lists all `AST-`/`TPL-`/`PUB-` items
     affected by the change.
  5. Refreshes `README.md` via `tools/build_readme.py`.

Usage (from the repository root):
    python3 tools/bump.py B02 minor --note "Add XYZ color rule"
    python3 tools/bump.py B02 errata --note "Fix typo" --dry-run
    python3 tools/bump.py B02 major --note "Breaking palette change" --bump-review
    python3 tools/bump.py INDEX errata --note "Routine register synchronization"
"""
from __future__ import annotations

import argparse
import calendar
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT / "Standards Design"
DEFAULT_INDEX = LIB / "Library-Index.md"
DEFAULT_README = ROOT / "README.md"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_readme  # noqa: E402

VER_RE = re.compile(r"^v(\d+)\.(\d+)\.(\d+)$")
TYPE_LABEL = {"major": "Major", "minor": "Minor", "errata": "Errata"}


def next_version(current: str, level: str) -> str:
    m = VER_RE.fullmatch(current.strip())
    if not m:
        raise ValueError(f"Invalid semantic version: {current!r}")
    maj, min_, err = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if level == "major":
        return f"v{maj + 1}.0.0"
    if level == "minor":
        return f"v{maj}.{min_ + 1}.0"
    if level == "errata":
        return f"v{maj}.{min_}.{err + 1}"
    raise ValueError(f"Unknown bump level: {level!r}")


def add_months(d: dt.date, months: int) -> dt.date:
    y = d.year + (d.month - 1 + months) // 12
    m = (d.month - 1 + months) % 12 + 1
    day = min(d.day, calendar.monthrange(y, m)[1])
    return dt.date(y, m, day)


def compute_next_review(today: dt.date, initial_approval: dt.date | None = None) -> str:
    """A01 §5.6.2: 6 months during Year 1 after initial approval, 12 months thereafter."""
    if initial_approval and (today - initial_approval).days >= 365:
        return add_months(today, 12).isoformat()
    return add_months(today, 6).isoformat()


def read_header(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in text.splitlines()[:35]:
        m = re.match(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.*?)\s*\|\s*$", line)
        if m:
            out[m.group(1).strip()] = m.group(2).strip().strip("`").strip()
    return out


def set_header_field(text: str, field: str, value: str, backtick: bool = True) -> str:
    formatted = f"`{value}`" if backtick else value
    pat = re.compile(rf"^(\|\s*\*\*{re.escape(field)}\*\*\s*\|\s*)(.*?)(\s*\|\s*)$", re.M)
    new_text, n = pat.subn(rf"\g<1>{formatted}\g<3>", text, count=1)
    if n != 1:
        raise ValueError(f"Header field **{field}** not found")
    return new_text


def prepend_revision_row(text: str, section_heading: str, version: str, date_str: str,
                         level: str, note: str, approver: str) -> str:
    """Insert a new row immediately after the table separator under section_heading."""
    pat = re.compile(
        rf"(^{re.escape(section_heading)}[^\n]*\n+\|[^\n]+\|\n\|(?:\s*:?-{{3,}}:?\s*\|)+\s*\n)",
        re.M,
    )
    row = f"| `{version}` | `{date_str}` | {TYPE_LABEL[level]} | {note} | {approver} |\n"
    new_text, n = pat.subn(lambda m: m.group(1) + row, text, count=1)
    if n != 1:
        raise ValueError(f"Revision History table under '{section_heading}' not found")
    return new_text


def find_initial_v1_date(text: str) -> dt.date | None:
    m = re.search(r"^\|\s*`v1\.0\.0`\s*\|\s*`(\d{4}-\d{2}-\d{2})`\s*\|", text, re.M)
    return dt.date.fromisoformat(m.group(1)) if m else None


def find_standard_row(index_text: str, code: str) -> tuple[str, str, str]:
    """Return (rel_path, version, next_review) for standard `code` in Library-Index.md."""
    pat = re.compile(
        rf"^\|\s*`{re.escape(code)}`\s*\|[^|]+\|\s*`([^`]+)`\s*\|\s*`(v\d+\.\d+\.\d+)`\s*\|\s*`([^`]+)`\s*\|[^|]+\|\s*`([^`]+)`",
        re.M,
    )
    m = pat.search(index_text)
    if not m:
        raise ValueError(f"Standard {code} not found in Library-Index.md")
    return m.group(1), m.group(2), m.group(4)


def update_index_standard_row(index_text: str, code: str, new_ver: str, new_review: str | None) -> str:
    lines = index_text.splitlines(keepends=True)
    updated = False
    for i, line in enumerate(lines):
        if re.match(rf"^\|\s*`{re.escape(code)}`\s*\|", line):
            parts = line.rstrip("\n").split("|")
            # parts: ['', ' `CODE` ', ' Name ', ' `File` ', ' `Ver` ', ' `Status` ', ' Owner ', ' `NextReview` ', ' Notes ', '']
            if len(parts) < 9:
                raise ValueError(f"Unexpected table columns for {code} in Library-Index.md")
            parts[4] = f" `{new_ver}` "
            if new_review is not None:
                parts[7] = f" `{new_review}` "
            lines[i] = "|".join(parts) + "\n"
            updated = True
            break
    if not updated:
        raise ValueError(f"Standard row for {code} not found in Library-Index.md")
    return "".join(lines)


def mark_sync_required_in_index(index_text: str, code: str, new_major: int) -> tuple[str, list[str]]:
    """Mark active AST-/TPL- rows governed by `code` pinned to < new_major as Sync Required."""
    sec5_start = index_text.index("## 5.")
    sec6_start = index_text.index("## 6.")
    head, sec5, tail = index_text[:sec5_start], index_text[sec5_start:sec6_start], index_text[sec6_start:]
    affected: list[str] = []
    out_lines = []
    for line in sec5.splitlines(keepends=True):
        m = re.match(
            rf"^\|\s*`((?:AST|TPL)-[^`]+)`\s*\|[^|]+\|[^|]+\|\s*`{re.escape(code)}`\s*\|\s*`{re.escape(code)}\s*\(v(\d+)\.\d+\)`\s*\|\s*`([^`]+)`\s*\|",
            line,
        )
        if m and int(m.group(2)) < new_major and m.group(3) == "Approved":
            affected.append(m.group(1))
            parts = line.rstrip("\n").split("|")
            parts[6] = " `Sync Required` "
            line = "|".join(parts) + "\n"
        out_lines.append(line)
    return head + "".join(out_lines) + tail, affected


def mark_sync_required_in_standard(std_text: str, code: str, new_major: int) -> str:
    """Mirror `Sync Required` in the governing standard's Section 7 table."""
    if "## 7." not in std_text or "## 8." not in std_text:
        return std_text
    s7 = std_text.index("## 7.")
    s8 = std_text.index("## 8.")
    head, sec7, tail = std_text[:s7], std_text[s7:s8], std_text[s8:]
    out_lines = []
    for line in sec7.splitlines(keepends=True):
        m = re.match(
            rf"^\|\s*`((?:AST|TPL)-[^`]+)`\s*\|[^|]+\|[^|]+\|\s*`{re.escape(code)}\s*\(v(\d+)\.\d+\)`\s*\|\s*`Approved`\s*\|",
            line,
        )
        if m and int(m.group(2)) < new_major:
            parts = line.rstrip("\n").split("|")
            parts[5] = " `Sync Required` "
            line = "|".join(parts) + "\n"
        out_lines.append(line)
    return head + "".join(out_lines) + tail


def find_citing_pubs(index_text: str, code: str) -> list[str]:
    sec6 = index_text.split("## 6.", 1)[1].split("## 7.", 1)[0]
    pubs = []
    for line in sec6.splitlines():
        m = re.match(r"^\|\s*`(PUB-\d{2})`\s*\|", line)
        if m and re.search(rf"`{re.escape(code)}\s*\(v\d+\.\d+\.\d+\)`", line):
            pubs.append(m.group(1))
    return pubs


def bump(
    target: str,
    level: str,
    note: str,
    *,
    lib: Path = LIB,
    readme_path: Path = DEFAULT_README,
    today: dt.date | None = None,
    approver: str | None = None,
    next_review: str | None = None,
    bump_review: bool = False,
    index_level: str | None = "errata",
    sync_required: bool = True,
    dry_run: bool = False,
) -> dict:
    today = today or dt.date.today()
    date_str = today.isoformat()
    index_path = lib / "Library-Index.md"
    index_text = index_path.read_text(encoding="utf-8")
    idx_header = read_header(index_text)
    default_approver = approver or idx_header.get("Approver", "Hary Irfantri")

    target_upper = target.upper()
    summary: dict = {"target": target_upper, "level": level, "date": date_str, "sync_required": [], "citing_pubs": []}

    if target_upper == "INDEX":
        old_ver = idx_header["Version"]
        new_ver = next_version(old_ver, level)
        new_index = set_header_field(index_text, "Version", new_ver)
        new_index = set_header_field(new_index, "Last Updated", date_str)
        new_index = prepend_revision_row(new_index, "## 10. Revision History", new_ver, date_str, level, note, default_approver)
        summary.update({"old_version": old_ver, "new_version": new_ver})
        if not dry_run:
            index_path.write_text(new_index, encoding="utf-8")
            if readme_path.exists():
                readme_path.write_text(build_readme.render_readme(readme_path.read_text(encoding="utf-8"), new_index), encoding="utf-8")
        return summary

    if not re.fullmatch(r"[A-H]\d{2}", target_upper):
        raise ValueError(f"Target must be a standard code (e.g. B02) or INDEX, got: {target!r}")

    rel_path, reg_ver, _ = find_standard_row(index_text, target_upper)
    std_path = lib / rel_path
    std_text = std_path.read_text(encoding="utf-8")
    std_header = read_header(std_text)
    old_ver = std_header["Version"]
    if old_ver != reg_ver:
        raise ValueError(f"{target_upper} header ({old_ver}) disagrees with Library-Index.md ({reg_ver}); resolve first.")

    new_ver = next_version(old_ver, level)
    std_approver = approver or std_header.get("Approver", default_approver)
    computed_review = next_review
    if computed_review is None and bump_review:
        computed_review = compute_next_review(today, find_initial_v1_date(std_text))

    new_std = set_header_field(std_text, "Version", new_ver)
    new_std = set_header_field(new_std, "Effective Date", date_str)
    if computed_review is not None:
        new_std = set_header_field(new_std, "Next Review", computed_review)
    new_std = prepend_revision_row(new_std, "## 8. Revision History", new_ver, date_str, level, note, std_approver)

    new_index = update_index_standard_row(index_text, target_upper, new_ver, computed_review)
    new_index = set_header_field(new_index, "Last Updated", date_str)

    if level == "major" and sync_required:
        new_major = int(VER_RE.fullmatch(new_ver).group(1))
        new_index, affected = mark_sync_required_in_index(new_index, target_upper, new_major)
        if affected:
            new_std = mark_sync_required_in_standard(new_std, target_upper, new_major)
        summary["sync_required"] = affected

    if index_level:
        old_idx_ver = idx_header["Version"]
        new_idx_ver = next_version(old_idx_ver, index_level)
        idx_note = f"Synced `{target_upper}` (`{new_ver}`, `{level.upper()}`): {note}"
        new_index = set_header_field(new_index, "Version", new_idx_ver)
        new_index = prepend_revision_row(new_index, "## 10. Revision History", new_idx_ver, date_str, index_level, idx_note, default_approver)
        summary["index_old_version"] = old_idx_ver
        summary["index_new_version"] = new_idx_ver

    summary.update({
        "file": rel_path,
        "old_version": old_ver,
        "new_version": new_ver,
        "next_review": computed_review or std_header.get("Next Review"),
        "citing_pubs": find_citing_pubs(index_text, target_upper),
    })

    if not dry_run:
        std_path.write_text(new_std, encoding="utf-8")
        index_path.write_text(new_index, encoding="utf-8")
        if readme_path.exists():
            readme_path.write_text(build_readme.render_readme(readme_path.read_text(encoding="utf-8"), new_index), encoding="utf-8")
    return summary


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target", help="Standard code (e.g. B02) or INDEX for Library-Index.md")
    ap.add_argument("level", choices=["major", "minor", "errata"], help="Version increment level (A01 §5.5)")
    ap.add_argument("--note", required=True, help="Summary of changes for the Revision History row")
    ap.add_argument("--date", help="Override ISO 8601 date (default: today)")
    ap.add_argument("--approver", help="Override Approver name (default: read from header)")
    ap.add_argument("--next-review", help="Explicit Next Review date (YYYY-MM-DD)")
    ap.add_argument("--bump-review", action="store_true", help="Advance Next Review per A01 §5.6.2 (6m Year 1, 12m thereafter)")
    ap.add_argument("--index-level", choices=["errata", "minor", "major"], default="errata",
                    help="How to bump Library-Index.md when bumping a standard (default: errata)")
    ap.add_argument("--no-index-bump", action="store_true", help="Sync standard row in Library-Index.md without bumping the register version")
    ap.add_argument("--no-sync-required", action="store_true", help="Do not mark dependent AST-/TPL- items Sync Required on MAJOR bump")
    ap.add_argument("--dry-run", action="store_true", help="Preview version changes without writing files")
    args = ap.parse_args(argv)

    today = dt.date.fromisoformat(args.date) if args.date else dt.date.today()
    res = bump(
        args.target,
        args.level,
        args.note,
        today=today,
        approver=args.approver,
        next_review=args.next_review,
        bump_review=args.bump_review,
        index_level=None if args.no_index_bump else args.index_level,
        sync_required=not args.no_sync_required,
        dry_run=args.dry_run,
    )

    mode = "DRY-RUN" if args.dry_run else "UPDATED"
    print(f"[{mode}] {res['target']}: {res['old_version']} -> {res['new_version']} ({res['date']})")
    if "index_new_version" in res:
        print(f"[{mode}] Library-Index.md: {res['index_old_version']} -> {res['index_new_version']}")
    if res.get("next_review"):
        print(f"  Next Review: {res['next_review']}")
    if res["sync_required"]:
        print(f"  Marked Sync Required (A01 §5.5.3): {', '.join(res['sync_required'])}")
    if res["citing_pubs"]:
        print(f"  PUB manifests citing {res['target']} (refresh before release): {', '.join(res['citing_pubs'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
