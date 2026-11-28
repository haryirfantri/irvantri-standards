"""Tests for design-system tooling: sync_pub01.py, build_tokens_exports.py, and --is-* var checks.

Run from the repository root:
    python3 -m unittest discover -s tools/tests -v
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_tokens_exports as bte  # noqa: E402
import library_checks as lc  # noqa: E402
import sync_pub01  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
LIB = REPO / "Standards Design"


class SyncPub01Tests(unittest.TestCase):
    def test_sync_and_drift_detection(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            tjson = d / "tokens.json"
            tcss = d / "tokens.css"
            pub = d / "PUB-01.html"
            tjson.write_text('{"a": 1}\n', encoding="utf-8")
            tcss.write_text(":root { --is-x: #FFFFFF; }\n", encoding="utf-8")
            pub.write_text(
                "<script>\n"
                '  const GENERATED_CSS = "stale";\n'
                '  const GENERATED_JSON = "{}";\n'
                "  downloadFile('AST-D01-01_Design-Tokens.css', GENERATED_CSS, 'text/css');\n"
                "</script>\n",
                encoding="utf-8",
            )
            same, diff = sync_pub01.check_drift(pub, tjson, tcss)
            self.assertFalse(same)
            self.assertIn("AST-D01-02_Design-Tokens.css", diff)

            synced = sync_pub01.render_pub01(pub.read_text(), tjson.read_text(), tcss.read_text())
            pub.write_text(synced, encoding="utf-8")
            same2, diff2 = sync_pub01.check_drift(pub, tjson, tcss)
            self.assertTrue(same2, diff2)
            self.assertIn("downloadFile('AST-D01-02_Design-Tokens.css', GENERATED_CSS", synced)


class TokenExportsTests(unittest.TestCase):
    def test_export_bundle_from_live_tokens(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "dist"
            written = bte.export_bundle(out)
            self.assertEqual(
                set(written.keys()),
                {"tokens.css", "components.css", "tokens.ts", "tokens.tailwind.css", "tailwind.preset.cjs", "package.json"},
            )
            ts = (out / "tokens.ts").read_text(encoding="utf-8")
            self.assertIn('"semantic.color.brand-primary": "#074C96"', ts)
            self.assertIn('"var(--is-color-brand-primary)"', ts)

            tw4 = (out / "tokens.tailwind.css").read_text(encoding="utf-8")
            self.assertIn("@theme {", tw4)
            self.assertIn("--color-is-brand-primary: var(--is-color-brand-primary);", tw4)

            pkg = json.loads((out / "package.json").read_text(encoding="utf-8"))
            self.assertEqual(pkg["name"], "@irvantri/design-system")
            self.assertIn("./tailwind.css", pkg["exports"])

            # Verify Tailwind v3 CommonJS preset is valid JS and loads in Node
            proc = subprocess.run(
                ["node", "-e", f"const p = require({json.dumps(str(out / 'tailwind.preset.cjs'))}); if (!p.theme.extend.colors['is-brand-primary']) process.exit(1);"],
                capture_output=True,
                text=True,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)


class UndefinedCssVarTests(unittest.TestCase):
    def test_catches_undefined_is_var_in_component_kit(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            lib = repo / "Standards Design"
            (lib / "02_Assets").mkdir(parents=True)
            (lib / "03_Templates").mkdir(parents=True)
            src_json = LIB / "02_Assets/AST-D01-01_Design-Tokens.json"
            src_css = LIB / "02_Assets/AST-D01-02_Design-Tokens.css"
            (lib / "02_Assets/AST-D01-01_Design-Tokens.json").write_bytes(src_json.read_bytes())
            (lib / "02_Assets/AST-D01-02_Design-Tokens.css").write_bytes(src_css.read_bytes())
            (lib / "02_Assets/AST-D03-01_Component-Kit.css").write_text(
                ".ok { color: var(--is-color-brand-primary); }\n.bad { margin: var(--is-does-not-exist); }\n",
                encoding="utf-8",
            )
            orig_repo, orig_lib = lc.REPO, lc.LIB
            try:
                lc.REPO, lc.LIB = repo, lib
                rep = lc.Report([])
                lc.check_token_css(rep)
                ids = {f["id"] for f in rep.checks[0]["findings"]}
            finally:
                lc.REPO, lc.LIB = orig_repo, orig_lib
            self.assertIn("token-css.undefined-var:02_Assets/AST-D03-01_Component-Kit.css:--is-does-not-exist", ids)


if __name__ == "__main__":
    unittest.main()
