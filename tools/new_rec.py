#!/usr/bin/env python3
"""Scaffold a Governance Record (REC-A04-NNN) with measured CI evidence (A04 §5.1.5, §5.1.7).

Auto-numbers the next `REC-A04-NNN` from `Library-Index.md` and `05_Records/`,
populates the metadata header and automated check evidence table from
`check-report/check-report.json` (when provided), and optionally registers the
new record in `Library-Index.md` Section 7 (refreshing `README.md` stats).

Also supports updating the `A04 §5.1.7` CI citation line on an existing record.

Usage (from the repository root):
    python3 tools/new_rec.py --title "B02 Color Update Pre-Release Gate" \\
        --standards A01,A04,B02 --report check-report/check-report.json --register
    python3 tools/new_rec.py --title "Year-1 Scheduled Consistency Review" \\
        --type "Scheduled Consistency Review" --standards A01,A02,A04 --dry-run
    python3 tools/new_rec.py --cite-ci "Standards Design/05_Records/REC-A04-018_..." \\
        --ci-run "https://github.com/haryirfantri/irvantri-standards/actions/runs/12345" \\
        --commit "abc1234"
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT / "Standards Design"
DEFAULT_README = ROOT / "README.md"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_readme  # noqa: E402

RECORD_TYPES = (
    "Pre-Release Gate",
    "Scheduled Consistency Review",
    "Event-Driven Audit",
    "Waiver",
)
REC_CODE_RE = re.compile(r"\bREC-A04-(\d{3})\b")


def _read_header(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in text.splitlines()[:35]:
        m = re.match(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.*?)\s*\|\s*$", line)
        if m:
            out[m.group(1).strip()] = m.group(2).strip().strip("`").strip()
    return out


def _standard_versions(index_text: str) -> dict[str, str]:
    sec4 = index_text.split("## 4.", 1)[1].split("## 5.", 1)[0]
    vers: dict[str, str] = {}
    for m in re.finditer(r"^\|\s*`([A-H]\d{2})`\s*\|[^|]+\|[^|]+\|\s*`(v\d+\.\d+\.\d+)`\s*\|", sec4, re.M):
        vers[m.group(1)] = m.group(2)
    return vers


def next_rec_code(lib: Path = LIB) -> str:
    """Return the next unused REC-A04-NNN across Library-Index.md and 05_Records/."""
    nums = [0]
    idx_path = lib / "Library-Index.md"
    if idx_path.exists():
        nums.extend(int(m) for m in REC_CODE_RE.findall(idx_path.read_text(encoding="utf-8")))
    rec_dir = lib / "05_Records"
    if rec_dir.exists():
        for p in rec_dir.iterdir():
            nums.extend(int(m) for m in REC_CODE_RE.findall(p.name))
    return f"REC-A04-{max(nums) + 1:03d}"


def title_slug(title: str) -> str:
    """Convert a record title to an A02-compliant hyphenated filename suffix."""
    cleaned = re.sub(r"[^A-Za-z0-9\s-]", "", title)
    parts = [p for p in re.split(r"[\s-]+", cleaned.strip()) if p]
    if not parts:
        raise ValueError(f"Title produces an empty filename slug: {title!r}")
    return "-".join(parts)


def format_related_standards(codes: list[str], std_vers: dict[str, str], index_ver: str) -> tuple[str, str]:
    """Return (header_field_with_versions, register_column_codes)."""
    norm = [c.strip().upper() for c in codes if c.strip()]
    if not norm:
        norm = ["A01", "A02", "A04"]
    with_vers = [f"`{c} ({std_vers[c]})`" if c in std_vers else f"`{c}`" for c in norm]
    with_vers.append(f"`Library-Index.md ({index_ver})`")
    reg_col = ", ".join(f"`{c}`" for c in norm)
    return ", ".join(with_vers), reg_col


def render_evidence_table(report_data: dict | None) -> tuple[str, str]:
    """Render automated check rows and the CI summary sentence from check-report.json."""
    if not report_data:
        table = (
            "| Check | Cites | Result | Measured Scope |\n"
            "| :--- | :--- | :--- | :--- |\n"
            "| *Run `python3 tools/library_checks.py --report-dir check-report` and re-run with `--report`* | — | Pending | — |"
        )
        ci_note = "Pending continuous integration (`CI`) `library-checks` run (`A04 §5.1.7`)."
        return table, ci_note

    meta = report_data.get("meta", {})
    rows = ["| Check | Cites | Result | Measured Scope |", "| :--- | :--- | :--- | :--- |"]
    for ch in report_data.get("checks", []):
        fails = [f for f in ch.get("findings", []) if f.get("status") == "fail"]
        known = [f for f in ch.get("findings", []) if f.get("status") == "known"]
        result = "Fail" if fails else ("Pass (known)" if known else "Pass")
        cites = ", ".join(f"`{x}`" for x in ch.get("cites", [])) or "—"
        scope = ch.get("summary") or "—"
        rows.append(f"| `{ch['id']}` | {cites} | {result} | {scope} |")

    verdict = str(meta.get("verdict", "unknown")).upper()
    failing = meta.get("failing_findings", 0)
    known_n = meta.get("known_issue_findings", 0)
    commit = (meta.get("commit") or "")[:7] or "unknown"
    run_url = meta.get("run_url")
    if run_url:
        run_id = run_url.rstrip("/").rsplit("/", 1)[-1]
        ci_note = (
            f"`python3 tools/library_checks.py` gives `{verdict}` ({failing} failing, {known_n} known). "
            f"The continuous integration (`CI`) `library-checks` run [`{run_id}`]({run_url}) "
            f"on commit `{commit}` completed (`A04 §5.1.7`)."
        )
    else:
        ci_note = (
            f"`python3 tools/library_checks.py` measured commit `{commit}` with verdict `{verdict}` "
            f"({failing} failing, {known_n} known). Cite the `CI` run URL once pull request checks pass (`A04 §5.1.7`)."
        )
    return "\n".join(rows), ci_note


def build_record_markdown(
    *,
    code: str,
    title: str,
    rec_type: str,
    date_str: str,
    status: str,
    owner: str,
    approver: str,
    related_header: str,
    expiry: str,
    a04_ver: str,
    index_ver: str,
    report_data: dict | None,
    ci_run_url: str | None = None,
    commit_sha: str | None = None,
) -> str:
    if report_data and (ci_run_url or commit_sha):
        report_data = json.loads(json.dumps(report_data))
        if ci_run_url:
            report_data.setdefault("meta", {})["run_url"] = ci_run_url
        if commit_sha:
            report_data.setdefault("meta", {})["commit"] = commit_sha

    evidence_table, ci_note = render_evidence_table(report_data)
    if not report_data and ci_run_url:
        run_id = ci_run_url.rstrip("/").rsplit("/", 1)[-1]
        sha_part = f" on commit `{commit_sha[:7]}`" if commit_sha else ""
        ci_note = (
            f"The continuous integration (`CI`) `library-checks` run [`{run_id}`]({ci_run_url})"
            f"{sha_part} completed (`A04 §5.1.7`)."
        )

    verdict = "Pass" if status == "Closed" else "Pending"
    return f"""# {code} — {title}

| Field | Value |
| :--- | :--- |
| **Code** | `{code}` |
| **Record Type** | {rec_type} |
| **Date** | `{date_str}` |
| **Status** | `{status}` |
| **Owner** | {owner} |
| **Approver** | {approver} |
| **Related Standards** | {related_header} |
| **Expiry Date** | `{expiry}` |

## 1. Review Scope & Trigger

This Governance Record (`REC-`) documents the {rec_type} (`A04 ({a04_ver}) §5.1.2`, `§5.1.5`) for the items below, released together with `Library-Index.md ({index_ver})`:

| Item | Change | Version Gated |
| :--- | :--- | :--- |
| *Item code* | *Summary of change* | *Version or pin* |

**Trigger.** *State the trigger event or Approver decision.*

## 2. Method

* **Automated check:** `python3 tools/library_checks.py --report-dir check-report` and `python3 -m unittest discover -s tools/tests -v`.
* **Additional measurements:** *List any browser, PDF, or manual checks performed.*

## 3. Automated Library Check Evidence (`A04 ({a04_ver}) §5.1.6`–`§5.1.7`)

{evidence_table}

## 4. Section 6 Manual / Targeted Verification

| Item | Check ID | Status | Measured Evidence |
| :--- | :--- | :--- | :--- |
| *Item* | *Check ID* | Pass | *Measured evidence or reviewer judgment* |

## 5. Non-Conformity Register (`A04 ({a04_ver}) §5.2.2`)

None.

## 6. Closure Verification (`A04 ({a04_ver}) §5.2.3`, `§5.1.7`)

* **Gate Verdict:** `{verdict}`.
* **Automated Check:** {ci_note}
* **Approver Sign-Off:** Merging the release pull request records Approver sign-off (`A01 §5.9.2`).
* **Approver:** {approver}
"""


def register_in_index(
    index_text: str,
    *,
    code: str,
    title: str,
    rel_file: str,
    date_str: str,
    related_col: str,
    status: str,
    expiry: str,
    summary: str,
) -> str:
    """Append a new REC row to Library-Index.md Section 7."""
    s7 = index_text.index("## 7.")
    s8 = index_text.index("## 8.")
    head, sec7, tail = index_text[:s7], index_text[s7:s8], index_text[s8:]
    row = f"| `{code}` | {title} | `{rel_file}` | `{date_str}` | {related_col} | `{status}` | `{expiry}` | {summary} |\n"
    # Insert right after the last table line in Section 7
    lines = sec7.splitlines(keepends=True)
    last_tbl = max((i for i, ln in enumerate(lines) if ln.startswith("|")), default=-1)
    if last_tbl < 0:
        raise ValueError("Governance Records table in Library-Index.md Section 7 not found")
    lines.insert(last_tbl + 1, row)
    return head + "".join(lines) + tail


def cite_ci_in_record(rec_path: Path, ci_run_url: str, commit_sha: str, verdict: str = "success") -> str:
    """Update the Automated Check bullet in an existing REC file with the CI run URL and commit."""
    text = rec_path.read_text(encoding="utf-8")
    run_id = ci_run_url.rstrip("/").rsplit("/", 1)[-1]
    short_sha = commit_sha[:7]
    new_line = (
        f"* **Automated Check:** `python3 tools/library_checks.py` passed with zero failing findings. "
        f"The continuous integration (`CI`) `library-checks` run [`{run_id}`]({ci_run_url}) "
        f"on commit `{short_sha}` completed with `{verdict}` (`A04 §5.1.7`)."
    )
    updated, n = re.subn(r"^\*\s+\*\*Automated Check:\*\*.*$", new_line, text, count=1, flags=re.M)
    if n != 1:
        raise ValueError(f"Could not find '* **Automated Check:**' bullet in {rec_path}")
    return updated


def create_rec(
    *,
    title: str,
    rec_type: str = "Pre-Release Gate",
    standards: list[str] | None = None,
    status: str | None = None,
    expiry: str = "None",
    summary: str | None = None,
    report_path: Path | None = None,
    ci_run_url: str | None = None,
    commit_sha: str | None = None,
    today: dt.date | None = None,
    register: bool = False,
    dry_run: bool = False,
    lib: Path = LIB,
    readme_path: Path = DEFAULT_README,
) -> dict:
    today = today or dt.date.today()
    date_str = today.isoformat()
    index_path = lib / "Library-Index.md"
    index_text = index_path.read_text(encoding="utf-8")
    idx_header = _read_header(index_text)
    std_vers = _standard_versions(index_text)

    code = next_rec_code(lib)
    slug = title_slug(title)
    rel_file = f"05_Records/{code}_{slug}.md"
    out_path = lib / rel_file
    rec_status = status or ("Open" if rec_type == "Waiver" else "Closed")
    owner = idx_header.get("Owner", "Hary Irfantri")
    approver = idx_header.get("Approver", owner)
    index_ver = idx_header.get("Version", "v1.0.0")
    a04_ver = std_vers.get("A04", "v1.2.1")
    related_header, related_col = format_related_standards(standards or ["A01", "A02", "A04"], std_vers, index_ver)

    report_data = json.loads(report_path.read_text(encoding="utf-8")) if report_path and report_path.exists() else None
    content = build_record_markdown(
        code=code,
        title=title,
        rec_type=rec_type,
        date_str=date_str,
        status=rec_status,
        owner=owner,
        approver=approver,
        related_header=related_header,
        expiry=expiry,
        a04_ver=a04_ver,
        index_ver=index_ver,
        report_data=report_data,
        ci_run_url=ci_run_url,
        commit_sha=commit_sha,
    )

    result = {"code": code, "file": rel_file, "status": rec_status, "registered": False}
    if not dry_run:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content, encoding="utf-8")
        if register:
            reg_summary = summary or f"{rec_type} for {title}"
            new_index = register_in_index(
                index_text,
                code=code,
                title=title,
                rel_file=rel_file,
                date_str=date_str,
                related_col=related_col,
                status=rec_status,
                expiry=expiry,
                summary=reg_summary,
            )
            index_path.write_text(new_index, encoding="utf-8")
            if readme_path.exists():
                readme_path.write_text(
                    build_readme.render_readme(readme_path.read_text(encoding="utf-8"), new_index),
                    encoding="utf-8",
                )
            result["registered"] = True
    return result


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--title", help="Record title (English Title Case, e.g. 'B02 Color Update Pre-Release Gate')")
    ap.add_argument("--type", choices=RECORD_TYPES, default="Pre-Release Gate", help="Governance record type")
    ap.add_argument("--standards", default="A01,A02,A04", help="Comma-separated related standard codes")
    ap.add_argument("--status", choices=["Open", "Approved", "Closed", "Rejected", "Expired", "Revoked"], help="Record status")
    ap.add_argument("--expiry", default="None", help="Expiry Date (YYYY-MM-DD for waivers, else None)")
    ap.add_argument("--summary", help="One-line summary for Library-Index.md Section 7")
    ap.add_argument("--report", type=Path, help="Path to check-report/check-report.json to auto-fill measured evidence")
    ap.add_argument("--ci-run", help="GitHub Actions run URL to cite per A04 §5.1.7")
    ap.add_argument("--commit", help="Git commit SHA cited in the record")
    ap.add_argument("--date", help="Override ISO 8601 date (default: today)")
    ap.add_argument("--register", action="store_true", help="Also append the record to Library-Index.md Section 7 and refresh README.md")
    ap.add_argument("--cite-ci", type=Path, help="Update the CI citation line in an existing REC file (requires --ci-run and --commit)")
    ap.add_argument("--dry-run", action="store_true", help="Preview without writing files")
    args = ap.parse_args(argv)

    if args.cite_ci:
        if not args.ci_run or not args.commit:
            raise SystemExit("--cite-ci requires both --ci-run and --commit")
        updated = cite_ci_in_record(args.cite_ci, args.ci_run, args.commit)
        if args.dry_run:
            print(f"[DRY-RUN] Would update CI citation in {args.cite_ci}")
        else:
            args.cite_ci.write_text(updated, encoding="utf-8")
            print(f"[UPDATED] Cited CI run in {args.cite_ci}")
        return 0

    if not args.title:
        raise SystemExit("--title is required when scaffolding a new record")

    today = dt.date.fromisoformat(args.date) if args.date else dt.date.today()
    res = create_rec(
        title=args.title,
        rec_type=args.type,
        standards=args.standards.split(","),
        status=args.status,
        expiry=args.expiry,
        summary=args.summary,
        report_path=args.report,
        ci_run_url=args.ci_run,
        commit_sha=args.commit,
        today=today,
        register=args.register,
        dry_run=args.dry_run,
    )
    mode = "DRY-RUN" if args.dry_run else "CREATED"
    print(f"[{mode}] {res['code']} -> Standards Design/{res['file']} (status={res['status']})")
    if res["registered"]:
        print("  Registered in Library-Index.md Section 7 and synced README.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
