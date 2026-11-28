"""Tests for tools/publish_drive.py: planning, archive policy, apply, and the REST backend.

Run from the repository root:
    python3 -m unittest discover -s tools/tests -v
"""
from __future__ import annotations

import hashlib
import io
import json
import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import publish_drive as pd  # noqa: E402

ROOT_ID = "root"


def md(version: str, body: str = "text") -> str:
    return f"# Doc\n\n| Field | Value |\n| :--- | :--- |\n| **Version** | `{version}` |\n\n{body}\n"


class FakeDrive(pd.DriveBackend):
    """In-memory Drive: id -> {name, parent, mimeType, data}."""

    def __init__(self, with_md5: bool = True):
        self.items: dict[str, dict] = {ROOT_ID: {"name": "root", "parent": None, "mimeType": pd.FOLDER_MIME}}
        self.log: list[tuple] = []
        self.with_md5 = with_md5
        self._n = 0

    def _id(self) -> str:
        self._n += 1
        return f"id{self._n}"

    def add_folder(self, name, parent=ROOT_ID):
        i = self._id()
        self.items[i] = {"name": name, "parent": parent, "mimeType": pd.FOLDER_MIME}
        return i

    def add_file(self, name, data: bytes, parent=ROOT_ID):
        i = self._id()
        self.items[i] = {"name": name, "parent": parent, "mimeType": "text/plain", "data": data}
        return i

    def path_of(self, i):
        parts = []
        while self.items[i]["parent"] is not None:
            parts.append(self.items[i]["name"])
            i = self.items[i]["parent"]
        return "/".join(reversed(parts))

    def by_path(self, rel):
        for i, it in self.items.items():
            if it["parent"] is not None and not it.get("trashed") and self.path_of(i) == rel:
                return it
        return None

    # backend API
    def list(self, folder_id):
        out = []
        for i, it in self.items.items():
            if it["parent"] == folder_id and not it.get("trashed"):
                d = {"id": i, "name": it["name"], "mimeType": it["mimeType"]}
                if "data" in it:
                    d["size"] = str(len(it["data"]))
                    if self.with_md5:
                        d["md5Checksum"] = hashlib.md5(it["data"]).hexdigest()
                out.append(d)
        return out

    def download(self, file_id, out):
        self.log.append(("download", file_id))
        out.write_bytes(self.items[file_id]["data"])

    def update(self, file_id, src):
        self.log.append(("update", self.path_of(file_id)))
        self.items[file_id]["data"] = src.read_bytes()

    def upload(self, src, parent_id, name=None):
        i = self.add_file(name or src.name, src.read_bytes(), parent_id)
        self.log.append(("upload", self.path_of(i)))
        return i

    def mkdir(self, name, parent_id):
        i = self.add_folder(name, parent_id)
        self.log.append(("mkdir", self.path_of(i)))
        return i

    def trash(self, file_id):
        self.log.append(("trash", self.path_of(file_id)))
        self.items[file_id]["trashed"] = True


class PublishTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.lib = Path(self.tmp.name) / "lib"
        (self.lib / "01_Standards").mkdir(parents=True)
        self.scratch = Path(self.tmp.name) / "scratch"
        self.scratch.mkdir()

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, rel, text):
        p = self.lib / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        return p

    def mirror(self, drive: FakeDrive):
        """Make Drive an exact copy of the local library."""
        folders = {"": ROOT_ID}
        dirs, files = pd.local_tree(self.lib)
        for d in dirs:
            parent = Path(d).parent.as_posix()
            folders[d] = drive.add_folder(Path(d).name, folders["" if parent == "." else parent])
        for rel, p in files.items():
            parent = Path(rel).parent.as_posix()
            drive.add_file(Path(rel).name, p.read_bytes(), folders["" if parent == "." else parent])

    def plan(self, drive, policy="versioned"):
        return pd.build_plan(drive, ROOT_ID, self.lib, policy, self.scratch)

    def kinds(self, plan):
        return [(a.kind, a.target, a.archive) for a in plan.actions]

    # --- planning
    def test_in_sync_plans_nothing(self):
        self.write("Library-Index.md", md("v1.0.0"))
        self.write("01_Standards/A01.md", md("v1.0.0"))
        for with_md5 in (True, False):
            d = FakeDrive(with_md5=with_md5)
            self.mirror(d)
            self.assertEqual(self.plan(d).actions, [], f"with_md5={with_md5}")

    def test_new_changed_and_removed(self):
        self.write("Library-Index.md", md("v1.0.0"))
        self.write("01_Standards/A01.md", md("v1.0.0"))
        d = FakeDrive()
        self.mirror(d)
        self.write("01_Standards/A01.md", md("v1.0.1", "fixed typo"))
        self.write("01_Standards/A02.md", md("v1.0.0"))
        self.write("02_Assets/logo.svg", "<svg/>")
        (self.lib / "Library-Index.md").unlink()
        got = self.kinds(self.plan(d))
        self.assertIn(("MKDIR", "02_Assets", False), got)
        self.assertIn(("UPLOAD", "01_Standards/A02.md", False), got)
        self.assertIn(("UPLOAD", "02_Assets/logo.svg", False), got)
        self.assertIn(("UPDATE", "01_Standards/A01.md", False), got)  # ERRATA: no archive
        self.assertIn(("REMOVE", "Library-Index.md", True), got)  # A01 §5.7.3

    def test_same_size_change_detected_by_md5(self):
        self.write("01_Standards/A01.md", md("v1.0.0", "aaaa"))
        d = FakeDrive()
        self.mirror(d)
        self.write("01_Standards/A01.md", md("v1.0.0", "bbbb"))
        self.assertEqual(self.kinds(self.plan(d)), [("UPDATE", "01_Standards/A01.md", False)])

    def test_archive_dirs_are_never_crawled(self):
        self.write("01_Standards/A01.md", md("v1.0.0"))
        d = FakeDrive()
        self.mirror(d)
        arc = d.add_folder("99_Archive")
        d.add_file("A01_v0.9.0.md", b"old", arc)
        self.assertEqual(self.plan(d).actions, [])

    # --- archive policy
    def test_archive_policy(self):
        old = self.write("old.md", md("v1.2.3"))
        for new_v, expect in (("v1.2.4", False), ("v1.3.0", True), ("v2.0.0", True)):
            new = self.write("new.md", md(new_v))
            self.assertEqual(pd.should_archive("versioned", "UPDATE", old, new)[0], expect, new_v)
        svg = self.write("a.svg", "<svg/>")
        self.assertFalse(pd.should_archive("versioned", "UPDATE", svg, svg)[0])
        self.assertTrue(pd.should_archive("all", "UPDATE", svg, svg)[0])
        self.assertFalse(pd.should_archive("none", "REMOVE", None, None)[0])

    def test_archive_name_collision(self):
        dl = self.write("dl.md", md("v1.2.3"))
        names = {"A01_v1.2.3.md"}
        self.assertEqual(pd.archive_name_for("01_Standards/A01.md", dl, names, "2026-11-28"), "A01_v1.2.3-r02.md")
        svg = self.write("dl.svg", "<svg/>")
        self.assertEqual(pd.archive_name_for("02_Assets/a.svg", svg, set(), "2026-11-28"), "a_2026-11-28.svg")

    # --- apply
    def test_apply_minor_bump_archives_then_updates_in_place(self):
        self.write("01_Standards/A01.md", md("v1.2.3"))
        d = FakeDrive()
        self.mirror(d)
        file_id = next(i for i, it in d.items.items() if it["name"] == "A01.md")
        self.write("01_Standards/A01.md", md("v1.3.0", "new clause"))
        self.write("01_Standards/A02.md", md("v1.0.0"))
        plan = self.plan(d)
        pd.apply_plan(d, plan, ROOT_ID, "2026-11-28", log=lambda *_: None)
        self.assertEqual(d.by_path("99_Archive/A01_v1.2.3.md")["data"], md("v1.2.3").encode())
        self.assertEqual(d.items[file_id]["data"], md("v1.3.0", "new clause").encode())  # same id: links stable
        self.assertIsNotNone(d.by_path("01_Standards/A02.md"))
        self.assertEqual(self.plan(d).actions, [])  # converged
        ops = [op for op, _ in d.log]
        self.assertLess(ops.index("upload"), ops.index("update"))  # archive before overwrite

    def test_apply_creates_nested_folders(self):
        self.write("01_Standards/A01.md", md("v1.0.0"))
        d = FakeDrive()
        self.mirror(d)
        self.write("06_Dependencies/Fonts/Noto/OFL.txt", "licence")
        pd.apply_plan(d, self.plan(d), ROOT_ID, "2026-11-28", log=lambda *_: None)
        self.assertIsNotNone(d.by_path("06_Dependencies/Fonts/Noto/OFL.txt"))

    def test_summary_and_drift_exit(self):
        self.write("01_Standards/A01.md", md("v1.0.0"))
        d = FakeDrive()
        plan = self.plan(d)
        s = pd.render_summary(plan, "DRY-RUN", ROOT_ID, "abc123")
        self.assertIn("`UPLOAD`", s)
        self.assertIn("abc123", s)


class FakeResp(io.BytesIO):
    def __init__(self, body: bytes = b"", headers: dict | None = None):
        super().__init__(body)
        self.headers = headers or {}

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


class ApiBackendTests(unittest.TestCase):
    def make(self, responses):
        calls = []

        def opener(req):
            calls.append(req)
            r = responses.pop(0)
            if isinstance(r, Exception):
                raise r
            return r

        be = pd.DriveApiBackend("cid", "secret", "refresh", opener=opener)
        return be, calls

    def token(self):
        return FakeResp(json.dumps({"access_token": "AT", "expires_in": 3600}).encode())

    def test_list_paginates_and_reuses_token(self):
        be, calls = self.make([
            self.token(),
            FakeResp(json.dumps({"files": [{"id": "1", "name": "a"}], "nextPageToken": "p2"}).encode()),
            FakeResp(json.dumps({"files": [{"id": "2", "name": "b"}]}).encode()),
        ])
        self.assertEqual([f["id"] for f in be.list("FOLDER")], ["1", "2"])
        self.assertEqual(calls[0].full_url, pd.DriveApiBackend.TOKEN_URL)
        self.assertIn("pageToken=p2", calls[2].full_url)
        self.assertEqual(calls[1].get_header("Authorization"), "Bearer AT")

    def test_update_uses_resumable_patch_on_same_id(self):
        with tempfile.TemporaryDirectory() as t:
            src = Path(t) / "x.md"
            src.write_text("hello")
            be, calls = self.make([
                self.token(),
                FakeResp(b"", {"Location": "https://upload.example/session"}),
                FakeResp(json.dumps({"id": "F1"}).encode()),
            ])
            be.update("F1", src)
        self.assertEqual(calls[1].get_method(), "PATCH")
        self.assertIn("/upload/drive/v3/files/F1?uploadType=resumable", calls[1].full_url)
        self.assertEqual(calls[2].get_method(), "PUT")
        self.assertEqual(calls[2].data, b"hello")

    def test_retries_transient_errors(self):
        pd.time.sleep = lambda s: None  # no real waiting in tests
        err = urllib.error.HTTPError("u", 503, "busy", {}, io.BytesIO(b"busy"))
        be, calls = self.make([self.token(), err, FakeResp(json.dumps({"id": "D"}).encode())])
        self.assertEqual(be.mkdir("dir", "P"), "D")
        self.assertEqual(len(calls), 3)

    def test_invalid_grant_explains_testing_mode(self):
        err = urllib.error.HTTPError("u", 400, "bad", {}, io.BytesIO(b'{"error":"invalid_grant"}'))
        be, _ = self.make([err])
        with self.assertRaises(SystemExit) as cm:
            be.list("F")
        self.assertIn("7 days", str(cm.exception))


if __name__ == "__main__":
    unittest.main()
