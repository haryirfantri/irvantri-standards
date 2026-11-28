"""Tests for tools/build_readme.py, tools/bump.py, and the governance checks in library_checks.py.

Run from the repository root:
    python3 -m unittest discover -s tools/tests -v
"""
from __future__ import annotations

import datetime as dt
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_readme  # noqa: E402
import bump  # noqa: E402
import library_checks as lc  # noqa: E402


SAMPLE_STD = """# B01 — Marks & Lockups

| Field | Value |
| :--- | :--- |
| **Code** | `B01` |
| **Version** | `v2.1.0` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-27` |
| **Next Review** | `2027-05-22` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |

## 7. Linked Artifacts

| Code | Artifact | File | Pinned Version | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `AST-B01-01` | Primary Symbol | `02_Assets/AST-B01-01_Primary-Symbol.svg` | `B01 (v2.0)` | `Approved` | Emblem |

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v2.1.0` | `2026-11-27` | Minor | Added small-format symbol. | Hary Irfantri |
| `v1.0.0` | `2026-11-22` | Major | Initial release. | Hary Irfantri |
"""

SAMPLE_INDEX = """# Standards Design — Library Index

| Field | Value |
| :--- | :--- |
| **Register** | `Library-Index.md` |
| **Version** | `v2.0.1` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-20` |
| **Last Updated** | `2026-11-28` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |

## 4. Normative Standards Register

| Code | Standard | File | Version | Status | Owner | Next Review | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `B01` | Marks & Lockups | `01_Standards/B_Visual-Foundations/B01_Marks-and-Lockups.md` | `v2.1.0` | `Approved` | Hary Irfantri | `2027-05-22` | Marks |

## 5. Master Assets & Executable Templates Register

| Code | Type | File | Governing Standard | Pinned Version | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AST-B01-01` | Master Asset | `02_Assets/AST-B01-01_Primary-Symbol.svg` | `B01` | `B01 (v2.0)` | `Approved` | Emblem |
| `TPL-E04-02` | Executable Template | `03_Templates/TPL-E04-02_Presentation-Master.html` | `B01` | `B01 (v2.0)` | `Planned` | Deck |

## 6. Compiled Publications Register

| Code | Publication | File | Compiled Date | Source Manifest | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `PUB-01` | Guide (`v1.0.0`) | `04_Publications/PUB-01_Guide.md` | `2026-11-28` | `B01 (v2.1.0)` | `Approved` | Compiled |

## 7. Governance Records Register

| Code | Record | File | Date | Related Standard | Status | Expiry Date | Summary |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `REC-A04-001` | Gate | `05_Records/REC-A04-001_Gate.md` | `2026-11-28` | `B01` | `Closed` | `None` | Done |

## 8. Third-Party Dependencies Reference

## 10. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v2.0.1` | `2026-11-28` | Errata | Initial sync. | Hary Irfantri |
"""

SAMPLE_PUB = """# PUB-01 — Guide

Compiled on `2026-11-28`. Active normative standards prevail in the event of a conflict.
"""

SAMPLE_README = """# Irvantri Standards

<!-- BEGIN:README-STATUS -->
> **Status:** Approved · **Register:** `v1.0.0` · **Last updated:** 2026-01-01
<!-- END:README-STATUS -->

<!-- BEGIN:README-COUNTS -->
stale
<!-- END:README-COUNTS -->
"""


class MiniLibraryMixin:
    def make_repo(self) -> tuple[Path, Path, Path]:
        self._tmp = tempfile.TemporaryDirectory()
        repo = Path(self._tmp.name)
        lib = repo / "Standards Design"
        (lib / "01_Standards/B_Visual-Foundations").mkdir(parents=True)
        (lib / "02_Assets").mkdir(parents=True)
        (lib / "04_Publications").mkdir(parents=True)
        (lib / "05_Records").mkdir(parents=True)
        (lib / "Library-Index.md").write_text(SAMPLE_INDEX, encoding="utf-8")
        (lib / "01_Standards/B_Visual-Foundations/B01_Marks-and-Lockups.md").write_text(SAMPLE_STD, encoding="utf-8")
        (lib / "04_Publications/PUB-01_Guide.md").write_text(SAMPLE_PUB, encoding="utf-8")
        readme = repo / "README.md"
        readme.write_text(build_readme.render_readme(SAMPLE_README, SAMPLE_INDEX), encoding="utf-8")
        return repo, lib, readme

    def tearDown(self):
        if hasattr(self, "_tmp"):
            self._tmp.cleanup()


class BuildReadmeTests(MiniLibraryMixin, unittest.TestCase):
    def test_sync_and_drift_detection(self):
        _, lib, readme = self.make_repo()
        same, diff, stats = build_readme.check_drift(lib / "Library-Index.md", readme)
        self.assertTrue(same, diff)
        self.assertEqual(stats["version"], "v2.0.1")
        self.assertEqual(len(stats["stds"]), 1)
        self.assertEqual(len(stats["assets"]), 1)
        self.assertEqual(len(stats["tpls_planned"]), 1)
        self.assertEqual(len(stats["pubs"]), 1)
        self.assertEqual(len(stats["recs"]), 1)

        # Introduce drift
        readme.write_text(SAMPLE_README, encoding="utf-8")
        same, diff, _ = build_readme.check_drift(lib / "Library-Index.md", readme)
        self.assertFalse(same)
        self.assertIn("v2.0.1", diff)


class BumpTests(MiniLibraryMixin, unittest.TestCase):
    def test_version_and_review_math(self):
        self.assertEqual(bump.next_version("v2.1.3", "errata"), "v2.1.4")
        self.assertEqual(bump.next_version("v2.1.3", "minor"), "v2.2.0")
        self.assertEqual(bump.next_version("v2.1.3", "major"), "v3.0.0")
        # Year 1 (<365 days since v1.0.0) -> +6 months; Year 2+ -> +12 months
        self.assertEqual(bump.compute_next_review(dt.date(2026, 11, 28), dt.date(2026, 11, 22)), "2027-05-28")
        self.assertEqual(bump.compute_next_review(dt.date(2027, 12, 1), dt.date(2026, 11, 22)), "2028-12-01")

    def test_dry_run_does_not_write(self):
        _, lib, readme = self.make_repo()
        before_idx = (lib / "Library-Index.md").read_text(encoding="utf-8")
        res = bump.bump("B01", "minor", "Add rule", lib=lib, readme_path=readme,
                        today=dt.date(2026, 12, 1), dry_run=True)
        self.assertEqual(res["new_version"], "v2.2.0")
        self.assertEqual(res["index_new_version"], "v2.0.2")
        self.assertEqual((lib / "Library-Index.md").read_text(encoding="utf-8"), before_idx)

    def test_major_bump_marks_sync_required_and_updates_readme(self):
        _, lib, readme = self.make_repo()
        res = bump.bump("B01", "major", "Breaking mark change", lib=lib, readme_path=readme,
                        today=dt.date(2026, 12, 1), bump_review=True)
        self.assertEqual(res["new_version"], "v3.0.0")
        self.assertEqual(res["next_review"], "2027-06-01")
        self.assertEqual(res["sync_required"], ["AST-B01-01"])
        self.assertEqual(res["citing_pubs"], ["PUB-01"])

        std_text = (lib / "01_Standards/B_Visual-Foundations/B01_Marks-and-Lockups.md").read_text(encoding="utf-8")
        idx_text = (lib / "Library-Index.md").read_text(encoding="utf-8")
        self.assertIn("| **Version** | `v3.0.0` |", std_text)
        self.assertIn("| `v3.0.0` | `2026-12-01` | Major | Breaking mark change | Hary Irfantri |", std_text)
        self.assertIn("| `AST-B01-01` | Primary Symbol | `02_Assets/AST-B01-01_Primary-Symbol.svg` | `B01 (v2.0)` | `Sync Required` |", std_text)
        self.assertIn("| `AST-B01-01` | Master Asset | `02_Assets/AST-B01-01_Primary-Symbol.svg` | `B01` | `B01 (v2.0)` | `Sync Required` |", idx_text)
        self.assertIn("| **Version** | `v2.0.2` |", idx_text)
        same, _, _ = build_readme.check_drift(lib / "Library-Index.md", readme)
        self.assertTrue(same)

    def test_index_only_bump(self):
        _, lib, readme = self.make_repo()
        res = bump.bump("INDEX", "errata", "Routine sync", lib=lib, readme_path=readme, today=dt.date(2026, 12, 2))
        self.assertEqual(res["new_version"], "v2.0.2")
        same, _, _ = build_readme.check_drift(lib / "Library-Index.md", readme)
        self.assertTrue(same)


class GovernanceCheckTests(MiniLibraryMixin, unittest.TestCase):
    def _run_with_repo(self, repo: Path, fn, *args):
        orig_repo, orig_lib = lc.REPO, lc.LIB
        try:
            lc.REPO, lc.LIB = repo, repo / "Standards Design"
            rep = lc.Report([])
            fn(rep, *args)
            return rep.checks[0]
        finally:
            lc.REPO, lc.LIB = orig_repo, orig_lib

    def test_all_new_checks_pass_on_clean_library(self):
        repo, _, _ = self.make_repo()
        for fn, args in [
            (lc.check_readme_sync, ()),
            (lc.check_pin_sync, ()),
            (lc.check_pub_manifests, ()),
            (lc.check_revision_history, ()),
            (lc.check_review_due, (dt.date(2026, 11, 28),)),
        ]:
            c = self._run_with_repo(repo, fn, *args)
            self.assertEqual(c["findings"], [], f"{c['id']} had unexpected findings: {c['findings']}")

    def test_pin_sync_catches_major_drift_and_sec7_mismatch(self):
        repo, lib, _ = self.make_repo()
        idx = lib / "Library-Index.md"
        idx.write_text(idx.read_text(encoding="utf-8").replace("`v2.1.0`", "`v3.0.0`", 1), encoding="utf-8")
        c = self._run_with_repo(repo, lc.check_pin_sync)
        ids = {f["id"] for f in c["findings"]}
        self.assertIn("pin-sync.major-drift:AST-B01-01", ids)

    def test_pub_manifest_catches_stale_standard_and_missing_notice(self):
        repo, lib, _ = self.make_repo()
        idx = lib / "Library-Index.md"
        idx.write_text(idx.read_text(encoding="utf-8").replace("`B01 (v2.1.0)`", "`B01 (v2.0.0)`"), encoding="utf-8")
        (lib / "04_Publications/PUB-01_Guide.md").write_text("# PUB-01\nNo date or notice.\n", encoding="utf-8")
        c = self._run_with_repo(repo, lc.check_pub_manifests)
        ids = {f["id"] for f in c["findings"]}
        self.assertIn("pub-manifest.stale-ref:PUB-01:B01", ids)
        self.assertIn("pub-manifest.no-precedence:PUB-01", ids)
        self.assertIn("pub-manifest.no-date:PUB-01", ids)

    def test_revision_history_catches_mismatch(self):
        repo, lib, _ = self.make_repo()
        std = lib / "01_Standards/B_Visual-Foundations/B01_Marks-and-Lockups.md"
        std.write_text(std.read_text(encoding="utf-8").replace("| **Version** | `v2.1.0` |", "| **Version** | `v2.1.1` |"), encoding="utf-8")
        c = self._run_with_repo(repo, lc.check_revision_history)
        self.assertEqual([f["id"] for f in c["findings"]], ["revision-history.mismatch:B01"])

    def test_review_due_catches_overdue_standard_and_expired_waiver(self):
        repo, lib, _ = self.make_repo()
        idx = lib / "Library-Index.md"
        idx.write_text(
            idx.read_text(encoding="utf-8").replace("| `Closed` | `None` |", "| `Open` | `2026-11-01` |"),
            encoding="utf-8",
        )
        # 2027-07-01 is > 30 days past 2027-05-22, and past waiver expiry 2026-11-01
        c = self._run_with_repo(repo, lc.check_review_due, dt.date(2027, 7, 1))
        ids = {f["id"] for f in c["findings"]}
        self.assertIn("review-due.overdue:B01", ids)
        self.assertIn("review-due.waiver-expired:REC-A04-001", ids)


if __name__ == "__main__":
    unittest.main()
