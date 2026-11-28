"""Tests for tools/new_rec.py (auto-numbering, evidence rendering, registration, CI citation).

Run from the repository root:
    python3 -m unittest discover -s tools/tests -v
"""
from __future__ import annotations

import datetime as dt
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_readme  # noqa: E402
import new_rec  # noqa: E402
from test_release_tools import SAMPLE_INDEX, SAMPLE_PUB, SAMPLE_README, SAMPLE_STD  # noqa: E402


SAMPLE_REPORT = {
    "meta": {
        "commit": "abcdef1234567890",
        "run_url": None,
        "verdict": "pass",
        "failing_findings": 0,
        "known_issue_findings": 0,
    },
    "checks": [
        {
            "id": "register-sync",
            "cites": ["A01"],
            "summary": "23 standard headers compared",
            "findings": [],
        },
        {
            "id": "contrast",
            "cites": ["B02-C5", "D04-C1"],
            "summary": "42 required pairings verified",
            "findings": [],
        },
    ],
}


class NewRecTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self._tmp.name)
        self.lib = self.repo / "Standards Design"
        (self.lib / "01_Standards/B_Visual-Foundations").mkdir(parents=True)
        (self.lib / "04_Publications").mkdir(parents=True)
        (self.lib / "05_Records").mkdir(parents=True)
        (self.lib / "Library-Index.md").write_text(SAMPLE_INDEX, encoding="utf-8")
        (self.lib / "01_Standards/B_Visual-Foundations/B01_Marks-and-Lockups.md").write_text(SAMPLE_STD, encoding="utf-8")
        (self.lib / "04_Publications/PUB-01_Guide.md").write_text(SAMPLE_PUB, encoding="utf-8")
        self.readme = self.repo / "README.md"
        self.readme.write_text(build_readme.render_readme(SAMPLE_README, SAMPLE_INDEX), encoding="utf-8")
        self.report = self.repo / "check-report.json"
        self.report.write_text(json.dumps(SAMPLE_REPORT), encoding="utf-8")

    def tearDown(self):
        self._tmp.cleanup()

    def test_next_rec_code_and_slug(self):
        self.assertEqual(new_rec.next_rec_code(self.lib), "REC-A04-002")
        self.assertEqual(new_rec.title_slug("B02 & E01 Pre-Release Gate!"), "B02-E01-Pre-Release-Gate")

    def test_dry_run_creates_nothing(self):
        res = new_rec.create_rec(
            title="Test Gate",
            standards=["A01", "B01"],
            report_path=self.report,
            today=dt.date(2026, 12, 1),
            register=True,
            dry_run=True,
            lib=self.lib,
            readme_path=self.readme,
        )
        self.assertEqual(res["code"], "REC-A04-002")
        self.assertFalse((self.lib / res["file"]).exists())

    def test_create_with_report_and_register_updates_index_and_readme(self):
        res = new_rec.create_rec(
            title="B01 Update Pre-Release Gate",
            standards=["A01", "B01"],
            summary="Pre-Release Gate for B01 update",
            report_path=self.report,
            today=dt.date(2026, 12, 1),
            register=True,
            lib=self.lib,
            readme_path=self.readme,
        )
        self.assertEqual(res["code"], "REC-A04-002")
        self.assertTrue(res["registered"])

        rec_path = self.lib / res["file"]
        text = rec_path.read_text(encoding="utf-8")
        self.assertIn("# REC-A04-002 — B01 Update Pre-Release Gate", text)
        self.assertIn("`B01 (v2.1.0)`", text)
        self.assertIn("| `register-sync` | `A01` | Pass | 23 standard headers compared |", text)
        self.assertIn("| `contrast` | `B02-C5`, `D04-C1` | Pass | 42 required pairings verified |", text)

        idx = (self.lib / "Library-Index.md").read_text(encoding="utf-8")
        self.assertIn("| `REC-A04-002` | B01 Update Pre-Release Gate | `05_Records/REC-A04-002_B01-Update-Pre-Release-Gate.md` |", idx)
        same, diff, stats = build_readme.check_drift(self.lib / "Library-Index.md", self.readme)
        self.assertTrue(same, diff)
        self.assertEqual(len(stats["recs"]), 2)

    def test_cite_ci_updates_existing_record(self):
        res = new_rec.create_rec(
            title="CI Citation Test Gate",
            today=dt.date(2026, 12, 1),
            lib=self.lib,
            readme_path=self.readme,
        )
        rec_path = self.lib / res["file"]
        updated = new_rec.cite_ci_in_record(
            rec_path,
            "https://github.com/haryirfantri/irvantri-standards/actions/runs/99999",
            "1234567890abcdef",
        )
        self.assertIn("[`99999`](https://github.com/haryirfantri/irvantri-standards/actions/runs/99999)", updated)
        self.assertIn("commit `1234567`", updated)


if __name__ == "__main__":
    unittest.main()
