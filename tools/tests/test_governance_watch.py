"""Tests for tools/governance_watch.py.

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
import governance_watch as gw  # noqa: E402
from test_release_tools import SAMPLE_INDEX  # noqa: E402


class GovernanceWatchTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.idx = self.root / "Library-Index.md"
        self.known = self.root / "known-issues.json"
        self.idx.write_text(
            SAMPLE_INDEX.replace("| `REC-A04-001` | Gate |", "| `REC-A04-001` | Initial Consistency Review |"),
            encoding="utf-8",
        )
        self.known.write_text(json.dumps({"issues": []}), encoding="utf-8")

    def tearDown(self):
        self._tmp.cleanup()

    def test_clear_when_far_from_deadlines(self):
        res = gw.analyze(self.idx, self.known, today=dt.date(2026, 12, 1))
        self.assertFalse(res["action_needed"])
        self.assertIn("All clear", gw.render_markdown(res))

    def test_flags_upcoming_review_and_consistency_cadence(self):
        # 2027-04-15 is within 60 days of 2027-05-22 (B01 Next Review) and 2027-05-28 (6m consistency review)
        res = gw.analyze(self.idx, self.known, today=dt.date(2027, 4, 15))
        self.assertTrue(res["action_needed"])
        self.assertEqual([r["code"] for r in res["reviews_due"]], ["B01"])
        self.assertEqual(res["reviews_due"][0]["severity"], "upcoming")
        self.assertIsNotNone(res["consistency_review"])
        self.assertEqual(res["consistency_review"]["next_due"], "2027-05-28")
        md = gw.render_markdown(res)
        self.assertIn("Scheduled Consistency Review", md)
        self.assertIn("`B01`", md)

    def test_flags_expiring_waiver_and_known_issue(self):
        self.idx.write_text(
            self.idx.read_text(encoding="utf-8").replace("| `Closed` | `None` |", "| `Open` | `2026-12-20` |"),
            encoding="utf-8",
        )
        self.known.write_text(
            json.dumps({"issues": [{"id": "palette.test", "review_by": "2026-11-30", "reference": "REC-A04-001"}]}),
            encoding="utf-8",
        )
        res = gw.analyze(self.idx, self.known, today=dt.date(2026, 12, 1))
        self.assertTrue(res["action_needed"])
        self.assertEqual(res["waivers_due"][0]["severity"], "expiring")
        self.assertEqual(res["known_due"][0]["severity"], "expired")


if __name__ == "__main__":
    unittest.main()
