"""Unit tests for core checks in tools/library_checks.py (good & bad fixtures).

Run from the repository root:
    python3 -m unittest discover -s tools/tests -v
"""
from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import library_checks as lc  # noqa: E402


MINI_B02 = """# B02 — Color System

| Field | Value |
| :--- | :--- |
| **Code** | `B02` |
| **Version** | `v2.0.0` |
| **Status** | `Approved` |
| **Next Review** | `2027-05-22` |

## 5. Requirements

**5.1.1** Primary palette:

| Color Name | HEX | RGB | CMYK |
| :--- | :--- | :--- | :--- |
| **Brand Blue** | `#074C96` | `7, 76, 150` | `100, 62, 0, 12` |
| **Pure White** | `#FFFFFF` | `255, 255, 255` | `0, 0, 0, 0` |
| **Text Primary** | `#0F172A` | `15, 23, 42` | `85, 72, 55, 65` |

## 6. Conformance & Verification
"""

MINI_INDEX = """# Standards Design — Library Index

| Field | Value |
| :--- | :--- |
| **Version** | `v1.0.0` |
| **Status** | `Approved` |

## 4. Normative Standards Register

| Code | Standard | File | Version | Status | Owner | Next Review | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `B02` | Color System | `01_Standards/B_Visual-Foundations/B02_Color-System.md` | `v2.0.0` | `Approved` | Owner | `2027-05-22` | Colors |

## 5. Master Assets & Executable Templates Register

| Code | Type | File | Governing Standard | Pinned Version | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AST-B02-01` | Master Asset | `02_Assets/AST-B02-01_Sample.svg` | `B02` | `B02 (v2.0)` | `Approved` | Sample |

## 6. Compiled Publications Register
## 7. Governance Records Register
## 8. Third-Party Dependencies Reference
"""


class LibraryChecksCoreTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self._tmp.name)
        self.lib = self.repo / "Standards Design"
        for d in lc.ACTIVE_DIRS:
            (self.lib / d).mkdir(parents=True, exist_ok=True)
        (self.lib / "01_Standards/B_Visual-Foundations").mkdir(parents=True, exist_ok=True)
        (self.lib / "01_Standards/B_Visual-Foundations/B02_Color-System.md").write_text(MINI_B02, encoding="utf-8")
        (self.lib / "Library-Index.md").write_text(MINI_INDEX, encoding="utf-8")
        (self.lib / "02_Assets/AST-B02-01_Sample.svg").write_text(
            '<svg xmlns="http://www.w3.org/2000/svg"><rect fill="#074C96"/></svg>\n', encoding="utf-8"
        )
        (self.repo / "README.md").write_text(
            "[Index](Standards%20Design/Library-Index.md)\n", encoding="utf-8"
        )

    def tearDown(self):
        self._tmp.cleanup()

    def _with_repo(self, fn):
        orig_repo, orig_lib = lc.REPO, lc.LIB
        try:
            lc.REPO, lc.LIB = self.repo, self.lib
            return fn()
        finally:
            lc.REPO, lc.LIB = orig_repo, orig_lib

    def test_report_known_issue_active_vs_expired(self):
        rep = lc.Report([
            {"id": "demo.active", "reason": "waived", "reference": "REC-1", "review_by": "2099-01-01"},
            {"id": "demo.expired", "reason": "old", "reference": "REC-2", "review_by": "2020-01-01"},
        ])
        c = rep.check("demo", "Demo", ["A04"])
        rep.fail(c, "demo.active", "active finding")
        rep.fail(c, "demo.expired", "expired finding")
        rep.fail(c, "demo.new", "new finding")
        statuses = {f["id"]: f["status"] for f in c["findings"]}
        self.assertEqual(statuses, {"demo.active": "known", "demo.expired": "fail", "demo.new": "fail"})

    def test_contrast_math_wcag(self):
        # Pure black on white = 21.00:1; Brand Blue #074C96 on white = 8.459.. -> floor2 = 8.45
        self.assertEqual(lc.floor2(lc.contrast("#000000", "#FFFFFF")), 21.0)
        self.assertEqual(lc.floor2(lc.contrast("#074C96", "#FFFFFF")), 8.45)

    def test_register_sync_clean_and_defects(self):
        def run():
            rep = lc.Report([])
            lc.check_register(rep)
            return rep.checks[0]["findings"]

        self.assertEqual(self._with_repo(run), [])
        # Introduce unregistered file and header version mismatch
        (self.lib / "02_Assets/AST-B02-99_Unregistered.svg").write_text("<svg/>", encoding="utf-8")
        b02 = self.lib / "01_Standards/B_Visual-Foundations/B02_Color-System.md"
        b02.write_text(b02.read_text(encoding="utf-8").replace("`v2.0.0`", "`v2.0.1`"), encoding="utf-8")
        ids = {f["id"] for f in self._with_repo(run)}
        self.assertIn("register-sync.version:B02", ids)
        self.assertIn("register-sync.unregistered:02_Assets/AST-B02-99_Unregistered.svg", ids)

    def test_palette_clean_and_off_palette_hex(self):
        def run():
            rep = lc.Report([])
            pal = lc.load_palette()
            lc.check_palette(rep, pal)
            return rep.checks[0]["findings"]

        self.assertEqual(self._with_repo(run), [])
        # Add off-palette and lowercase hex
        svg = self.lib / "02_Assets/AST-B02-01_Sample.svg"
        svg.write_text('<svg><rect fill="#123456"/><rect fill="#074c96"/></svg>', encoding="utf-8")
        ids = {f["id"] for f in self._with_repo(run)}
        self.assertTrue(any(i.startswith("palette.off-palette:") for i in ids), ids)
        self.assertTrue(any(i.startswith("palette.lowercase:") for i in ids), ids)

    def test_links_clean_and_broken(self):
        def run():
            rep = lc.Report([])
            lc.check_links(rep)
            return rep.checks[0]["findings"]

        (self.lib / "06_Dependencies/Dependencies-Manifest.md").write_text("# Manifest\n", encoding="utf-8")
        self.assertEqual(self._with_repo(run), [])
        (self.repo / "README.md").write_text("[Broken](Standards%20Design/No-Such-File.md)\n", encoding="utf-8")
        ids = {f["id"] for f in self._with_repo(run)}
        self.assertTrue(any(i.startswith("links.broken:README.md") for i in ids), ids)

    def test_dependencies_checksum_pass_and_tamper(self):
        font_dir = self.lib / "06_Dependencies/Fonts/Demo"
        font_dir.mkdir(parents=True)
        ttf = font_dir / "Demo-Regular.ttf"
        ttf.write_bytes(b"FAKEFONTBYTES")
        (font_dir / "OFL.txt").write_text(
            "Copyright 2026 Demo Authors.\n\n"
            "SIL OPEN FONT LICENSE Version 1.1 - 26 February 2007\n"
            "PREAMBLE\nPERMISSION & CONDITIONS\nTERMINATION\nDISCLAIMER\n"
            + ("x" * 4000),
            encoding="utf-8",
        )
        sha = hashlib.sha256(b"FAKEFONTBYTES").hexdigest()
        manifest = self.lib / "06_Dependencies/Dependencies-Manifest.md"
        manifest.write_text(
            f"# Manifest\n\n| File | Size | SHA-256 |\n| :--- | :--- | :--- |\n"
            f"| `06_Dependencies/Fonts/Demo/Demo-Regular.ttf` | `{len(b'FAKEFONTBYTES')}` | `{sha}` |\n",
            encoding="utf-8",
        )

        def run():
            rep = lc.Report([])
            lc.check_dependencies(rep)
            return rep.checks[0]["findings"]

        self.assertEqual(self._with_repo(run), [])
        # Tamper with the font binary
        ttf.write_bytes(b"TAMPEREDBYTES")
        ids = {f["id"] for f in self._with_repo(run)}
        self.assertTrue(any("dependencies.sha256" in i for i in ids), ids)


if __name__ == "__main__":
    unittest.main()
