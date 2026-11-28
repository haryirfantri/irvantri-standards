#!/usr/bin/env python3
"""Governance calendar watcher for Standards Design (A01 §5.6, A04 §5.1.2, §5.4.9).

Scans `Standards Design/Library-Index.md` and `tools/known-issues.json` to flag:
  * Normative standards whose `Next Review` is overdue or due within `--review-window` days (default 60).
  * Active waivers (`REC-` rows in `Open`/`Approved` status with a date `Expiry Date`) expired or expiring within `--waiver-window` days (default 30).
  * `tools/known-issues.json` entries expired or due within `--waiver-window` days.
  * Scheduled Consistency Review cadence (`A04 §5.1.2`: 6 months in Year 1, 12 months thereafter).

Usage (from the repository root):
    python3 tools/governance_watch.py
    python3 tools/governance_watch.py --summary watch.md --fail-on-action
    python3 tools/governance_watch.py --date 2027-04-15

Exit status: 0 when no action is due; 2 with `--fail-on-action` when any item is due or overdue.
"""
from __future__ import annotations

import argparse
import calendar
import datetime as dt
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INDEX = ROOT / "Standards Design" / "Library-Index.md"
DEFAULT_KNOWN = ROOT / "tools" / "known-issues.json"


def _ticks(cell: str) -> str:
    m = re.search(r"`([^`]*)`", cell)
    return m.group(1) if m else cell.strip()


def _table_rows(text: str) -> list[list[str]]:
    rows = []
    for line in text.splitlines():
        if line.startswith("|") and not re.match(r"^\|\s*:?-{3,}", line):
            rows.append([c.strip() for c in line.strip().strip("|").split("|")])
    return rows


def _add_months(d: dt.date, months: int) -> dt.date:
    y = d.year + (d.month - 1 + months) // 12
    m = (d.month - 1 + months) % 12 + 1
    return dt.date(y, m, min(d.day, calendar.monthrange(y, m)[1]))


def analyze(
    index_path: Path = DEFAULT_INDEX,
    known_path: Path = DEFAULT_KNOWN,
    *,
    today: dt.date | None = None,
    review_window: int = 60,
    waiver_window: int = 30,
) -> dict:
    today = today or dt.date.today()
    idx = index_path.read_text(encoding="utf-8")

    # Effective date of library (for Year 1 vs subsequent years consistency cadence)
    eff_m = re.search(r"^\|\s*\*\*Effective Date\*\*\s*\|\s*`(\d{4}-\d{2}-\d{2})`\s*\|", idx, re.M)
    lib_start = dt.date.fromisoformat(eff_m.group(1)) if eff_m else today

    # 1. Standard Next Review dates
    sec4 = idx.split("## 4.", 1)[1].split("## 5.", 1)[0]
    reviews_due: list[dict] = []
    for r in _table_rows(sec4):
        if len(r) < 7:
            continue
        code, title, status, raw_due = _ticks(r[0]), r[1], _ticks(r[4]), _ticks(r[6])
        if not re.fullmatch(r"[A-H]\d{2}", code) or status != "Approved":
            continue
        due = dt.date.fromisoformat(raw_due)
        days = (due - today).days
        if days <= review_window:
            severity = "overdue (>30d)" if days < -30 else ("past due" if days < 0 else "upcoming")
            reviews_due.append({"code": code, "title": title, "due": raw_due, "days": days, "severity": severity})

    # 2. Active waivers & last Consistency Review
    sec7 = idx.split("## 7.", 1)[1].split("## 8.", 1)[0]
    waivers_due: list[dict] = []
    review_dates: list[tuple[dt.date, str]] = []
    for r in _table_rows(sec7):
        if len(r) < 7:
            continue
        code, title, raw_date, status, expiry = _ticks(r[0]), r[1], _ticks(r[3]), _ticks(r[5]), _ticks(r[6])
        if not re.fullmatch(r"REC-[A-H]\d{2}-\d{3}", code):
            continue
        if re.search(r"Consistency Review|Full-Library Audit", title, re.I):
            try:
                review_dates.append((dt.date.fromisoformat(raw_date), code))
            except ValueError:
                pass
        if status in ("Open", "Approved") and expiry and expiry.lower() != "none":
            exp = dt.date.fromisoformat(expiry)
            days = (exp - today).days
            if days <= waiver_window:
                waivers_due.append({
                    "code": code,
                    "title": title,
                    "status": status,
                    "expiry": expiry,
                    "days": days,
                    "severity": "expired" if days < 0 else "expiring",
                })

    # 3. Known-issues review_by dates
    known_due: list[dict] = []
    if known_path.exists():
        for item in json.loads(known_path.read_text(encoding="utf-8")).get("issues", []):
            raw = str(item.get("review_by", ""))
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw):
                due = dt.date.fromisoformat(raw)
                days = (due - today).days
                if days <= waiver_window:
                    known_due.append({
                        "id": item.get("id", "unknown"),
                        "review_by": raw,
                        "days": days,
                        "reference": item.get("reference", ""),
                        "severity": "expired" if days < 0 else "expiring",
                    })

    # 4. Next Scheduled Consistency Review (A04 §5.1.2)
    consistency: dict | None = None
    if review_dates:
        last_date, last_code = max(review_dates)
        months = 12 if (today - lib_start).days >= 365 else 6
        next_due = _add_months(last_date, months)
        days = (next_due - today).days
        if days <= review_window:
            consistency = {
                "last_record": last_code,
                "last_date": last_date.isoformat(),
                "next_due": next_due.isoformat(),
                "days": days,
                "severity": "overdue" if days < 0 else "upcoming",
            }

    action_needed = bool(reviews_due or waivers_due or known_due or consistency)
    return {
        "today": today.isoformat(),
        "review_window": review_window,
        "waiver_window": waiver_window,
        "reviews_due": sorted(reviews_due, key=lambda x: (x["days"], x["code"])),
        "waivers_due": sorted(waivers_due, key=lambda x: (x["days"], x["code"])),
        "known_due": sorted(known_due, key=lambda x: (x["days"], x["id"])),
        "consistency_review": consistency,
        "action_needed": action_needed,
    }


def render_markdown(res: dict) -> str:
    lines = [f"## Governance Calendar Watch ({res['today']})", ""]
    if not res["action_needed"]:
        lines.append(
            f"All clear: no standard reviews due within {res['review_window']} days, "
            f"no waivers or known issues expiring within {res['waiver_window']} days, "
            "and no Scheduled Consistency Review due yet."
        )
        return "\n".join(lines) + "\n"

    if res["consistency_review"]:
        cr = res["consistency_review"]
        lines += [
            "### Scheduled Consistency Review (`A04 §5.1.2`)",
            "",
            f"- Last review: `{cr['last_record']}` ({cr['last_date']}) → Next due: **`{cr['next_due']}`** ({cr['days']} days, `{cr['severity']}`).",
            "- Scaffold with: `python3 tools/new_rec.py --title \"Scheduled Consistency Review\" --type \"Scheduled Consistency Review\" --report check-report/check-report.json --register`",
            "",
        ]

    if res["reviews_due"]:
        lines += [
            f"### Standard Reviews Due / Overdue (within {res['review_window']} days, `A01 §5.6`)",
            "",
            "| Standard | Title | Next Review | Days | State |",
            "| :--- | :--- | :--- | ---: | :--- |",
        ]
        for r in res["reviews_due"]:
            lines.append(f"| `{r['code']}` | {r['title']} | `{r['due']}` | {r['days']} | `{r['severity']}` |")
        lines.append("")

    if res["waivers_due"]:
        lines += [
            f"### Active Waivers Expiring / Expired (within {res['waiver_window']} days, `A04 §5.4.9`)",
            "",
            "| Record | Title | Status | Expiry Date | Days | State |",
            "| :--- | :--- | :--- | :--- | ---: | :--- |",
        ]
        for w in res["waivers_due"]:
            lines.append(f"| `{w['code']}` | {w['title']} | `{w['status']}` | `{w['expiry']}` | {w['days']} | `{w['severity']}` |")
        lines.append("")

    if res["known_due"]:
        lines += [
            f"### Known Issues Expiring / Expired (`tools/known-issues.json`)",
            "",
            "| Finding ID | Review By | Days | Reference | State |",
            "| :--- | :--- | ---: | :--- | :--- |",
        ]
        for k in res["known_due"]:
            lines.append(f"| `{k['id']}` | `{k['review_by']}` | {k['days']} | {k['reference']} | `{k['severity']}` |")
        lines.append("")

    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    ap.add_argument("--known-issues", type=Path, default=DEFAULT_KNOWN)
    ap.add_argument("--date", help="Override ISO 8601 date (default: today)")
    ap.add_argument("--review-window", type=int, default=60, help="Lookahead days for standard reviews (default: 60)")
    ap.add_argument("--waiver-window", type=int, default=30, help="Lookahead days for waivers & known issues (default: 30)")
    ap.add_argument("--summary", type=Path, help="Write Markdown report to this path")
    ap.add_argument("--fail-on-action", action="store_true", help="Exit 2 when any governance item is due or overdue")
    args = ap.parse_args(argv)

    today = dt.date.fromisoformat(args.date) if args.date else dt.date.today()
    res = analyze(args.index, args.known_issues, today=today,
                  review_window=args.review_window, waiver_window=args.waiver_window)
    md = render_markdown(res)
    print(md)
    if args.summary:
        args.summary.write_text(md, encoding="utf-8")
    if args.fail_on_action and res["action_needed"]:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
