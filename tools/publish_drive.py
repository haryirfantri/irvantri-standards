#!/usr/bin/env python3
"""Publish Standards Design one-way from GitHub to Google Drive (A01 §5.9.3).

Roles:
  * GitHub (haryirfantri/irvantri-standards, Standards Design/ on main) is the
    Authoring Repository of Record.
  * Google Drive (folder ID 17-hTsw-2MIT-SzA6pRgzocpKTy1vwYin) is the read-only
    Distribution Mirror (01_Standards/ .. 06_Dependencies/ + Library-Index.md)
    and append-only Cold Archive (99_Archive/).

Behaviour:
  * Never deletes anything inside Google Drive 99_Archive/.
  * Updates existing Drive files in-place so Drive file IDs and shared links
    remain stable.
  * Archive policy (--archive-policy):
      versioned  (default) snapshot the outgoing Drive copy into 99_Archive/
                 only when its `vMAJOR.MINOR` differs from the incoming file
                 (A01 §5.5.3, §5.5.4, §5.7.2), and always before an active file
                 is removed (A01 §5.7.3). ERRATA updates and unversioned assets
                 are updated in place; Git history and release tags hold them.
      all        snapshot every replaced or removed file (legacy behaviour,
                 same as --archive-outgoing).
      none       never snapshot.
    Archive names follow A02 §5.6.1: `_vX.Y.Z` for versioned Markdown, else
    `_YYYY-MM-DD`, with `-rNN` added on collision.
  * Defaults to a dry run; pass --apply to execute mutations.

Backends (--backend, default auto):
  * api   Google Drive REST API v3 with an OAuth 2.0 refresh token for the
          library Owner's account. Used in CI. Reads GDRIVE_OAUTH_CLIENT_ID,
          GDRIVE_OAUTH_CLIENT_SECRET and GDRIVE_OAUTH_REFRESH_TOKEN.
  * cli   the `gdrive` command-line tool, for local or agent sessions.
  auto picks api when GDRIVE_OAUTH_REFRESH_TOKEN is set, else cli.

Usage (from the repository root):
    python3 tools/publish_drive.py --dry-run
    python3 tools/publish_drive.py --apply
    python3 tools/publish_drive.py --dry-run --fail-on-drift --summary plan.md

Exit status: 0 on success; 2 with --fail-on-drift when any action is planned.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import mimetypes
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT / "Standards Design"
DEFAULT_DRIVE_ROOT_ID = os.environ.get("STANDARDS_DESIGN_DRIVE_ID", "17-hTsw-2MIT-SzA6pRgzocpKTy1vwYin")
ACTIVE_TOP = ["Library-Index.md", "01_Standards", "02_Assets", "03_Templates", "04_Publications", "05_Records", "06_Dependencies"]
SKIP_DIRS = {"99_Archive", "98_Drafts"}
FOLDER_MIME = "application/vnd.google-apps.folder"
TEXT_EXTS = {".md", ".json", ".css", ".svg", ".html", ".txt"}
VERSION_RE = re.compile(r"^\|\s*\*\*Version\*\*\s*\|\s*`(v(\d+)\.(\d+)\.(\d+))`\s*\|", re.M)


# --------------------------------------------------------------------------- backends


class DriveBackend:
    """Minimal Drive surface the publisher needs. Items are dicts with
    id, name, mimeType and, for files, size and (when known) md5Checksum."""

    def list(self, folder_id: str) -> list[dict]:
        raise NotImplementedError

    def download(self, file_id: str, out: Path) -> None:
        raise NotImplementedError

    def update(self, file_id: str, src: Path) -> None:
        raise NotImplementedError

    def upload(self, src: Path, parent_id: str, name: str | None = None) -> str:
        raise NotImplementedError

    def mkdir(self, name: str, parent_id: str) -> str:
        raise NotImplementedError

    def trash(self, file_id: str) -> None:
        raise NotImplementedError


class GdriveCliBackend(DriveBackend):
    """Wraps the `gdrive` CLI (readonly/mutate namespaces)."""

    def _run(self, *args: str, parse_json: bool = False):
        cmd = ["gdrive", *args]
        if parse_json:
            cmd.append("--json")
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            raise RuntimeError(f"Command failed ({proc.returncode}): {' '.join(cmd)}\n{proc.stderr.strip()}")
        if parse_json:
            text = proc.stdout.strip()
            return json.loads(text) if text else []
        return proc.stdout.strip()

    def list(self, folder_id: str) -> list[dict]:
        data = self._run("readonly", "ls", folder_id, parse_json=True)
        return data.get("files", []) if isinstance(data, dict) else data

    def download(self, file_id: str, out: Path) -> None:
        self._run("readonly", "download", file_id, "--out", str(out))

    def update(self, file_id: str, src: Path) -> None:
        self._run("mutate", "update", file_id, str(src))

    def upload(self, src: Path, parent_id: str, name: str | None = None) -> str:
        if name and name != src.name:
            with tempfile.TemporaryDirectory() as tmp:
                renamed = Path(tmp) / name
                renamed.write_bytes(src.read_bytes())
                return self.upload(renamed, parent_id)
        self._run("mutate", "upload", str(src), "--parent", parent_id)
        return self._find(parent_id, src.name)

    def mkdir(self, name: str, parent_id: str) -> str:
        self._run("mutate", "mkdir", name, "--parent", parent_id)
        return self._find(parent_id, name)

    def trash(self, file_id: str) -> None:
        self._run("mutate", "trash", file_id)

    def _find(self, parent_id: str, name: str) -> str:
        for item in self.list(parent_id):
            if item["name"] == name:
                return item["id"]
        raise RuntimeError(f"{name} not found in {parent_id} after creation")


class DriveApiBackend(DriveBackend):
    """Google Drive REST API v3 using an OAuth 2.0 refresh token (standard library only).

    The refresh token belongs to the library Owner's personal Google account, so
    files created in My Drive count against the Owner's quota and stay owned by
    the Owner. A service account cannot create files in a personal My Drive.
    """

    API = "https://www.googleapis.com/drive/v3"
    UPLOAD = "https://www.googleapis.com/upload/drive/v3"
    TOKEN_URL = "https://oauth2.googleapis.com/token"
    FIELDS = "id,name,mimeType,size,md5Checksum"

    def __init__(self, client_id: str, client_secret: str, refresh_token: str, opener=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self._open = opener or urllib.request.urlopen
        self._token: str | None = None
        self._expires = 0.0

    @classmethod
    def from_env(cls) -> "DriveApiBackend":
        missing = [k for k in ("GDRIVE_OAUTH_CLIENT_ID", "GDRIVE_OAUTH_CLIENT_SECRET", "GDRIVE_OAUTH_REFRESH_TOKEN") if not os.environ.get(k)]
        if missing:
            raise SystemExit(f"Missing environment variables for the api backend: {', '.join(missing)}")
        return cls(os.environ["GDRIVE_OAUTH_CLIENT_ID"], os.environ["GDRIVE_OAUTH_CLIENT_SECRET"], os.environ["GDRIVE_OAUTH_REFRESH_TOKEN"])

    # -- plumbing
    def _access_token(self) -> str:
        if self._token and time.time() < self._expires - 60:
            return self._token
        body = urllib.parse.urlencode({
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": self.refresh_token,
            "grant_type": "refresh_token",
        }).encode()
        req = urllib.request.Request(self.TOKEN_URL, data=body, method="POST",
                                     headers={"Content-Type": "application/x-www-form-urlencoded"})
        try:
            with self._open(req) as resp:
                data = json.loads(resp.read())
        except urllib.error.HTTPError as e:
            detail = e.read().decode(errors="replace")
            hint = ""
            if "invalid_grant" in detail:
                hint = (" The refresh token was revoked or expired. If the OAuth consent screen is in"
                        " 'Testing', tokens expire after 7 days: publish the app ('In production') and"
                        " mint a new token with tools/drive_oauth_token.py.")
            raise SystemExit(f"OAuth token refresh failed (HTTP {e.code}): {detail}{hint}") from None
        self._token = data["access_token"]
        self._expires = time.time() + int(data.get("expires_in", 3600))
        return self._token

    def _request(self, method: str, url: str, *, data: bytes | None = None, headers: dict | None = None,
                 raw: bool = False, want_headers: bool = False, retries: int = 4):
        for attempt in range(retries + 1):
            h = {"Authorization": f"Bearer {self._access_token()}"}
            h.update(headers or {})
            req = urllib.request.Request(url, data=data, method=method, headers=h)
            try:
                with self._open(req) as resp:
                    payload = resp.read()
                    if want_headers:
                        return dict(resp.headers.items())
                    if raw:
                        return payload
                    return json.loads(payload) if payload else {}
            except urllib.error.HTTPError as e:
                if e.code in (429, 500, 502, 503, 504) and attempt < retries:
                    time.sleep(2 ** attempt)
                    continue
                raise RuntimeError(f"Drive API {method} {url} failed (HTTP {e.code}): {e.read().decode(errors='replace')}") from None
        raise RuntimeError("unreachable")

    # -- operations
    def list(self, folder_id: str) -> list[dict]:
        items: list[dict] = []
        token = None
        while True:
            q = {
                "q": f"'{folder_id}' in parents and trashed = false",
                "fields": f"nextPageToken,files({self.FIELDS})",
                "pageSize": "1000",
                "supportsAllDrives": "true",
                "includeItemsFromAllDrives": "true",
            }
            if token:
                q["pageToken"] = token
            data = self._request("GET", f"{self.API}/files?{urllib.parse.urlencode(q)}")
            items.extend(data.get("files", []))
            token = data.get("nextPageToken")
            if not token:
                return items

    def download(self, file_id: str, out: Path) -> None:
        out.write_bytes(self._request("GET", f"{self.API}/files/{file_id}?alt=media&supportsAllDrives=true", raw=True))

    def _resumable(self, method: str, url: str, meta: dict, src: Path) -> dict:
        mime = mimetypes.guess_type(src.name)[0] or "application/octet-stream"
        hdrs = self._request(method, url, data=json.dumps(meta).encode(), want_headers=True, headers={
            "Content-Type": "application/json; charset=UTF-8",
            "X-Upload-Content-Type": mime,
            "X-Upload-Content-Length": str(src.stat().st_size),
        })
        location = hdrs.get("Location") or hdrs.get("location")
        if not location:
            raise RuntimeError(f"Drive API did not return an upload session for {src}")
        return self._request("PUT", location, data=src.read_bytes(), headers={"Content-Type": mime})

    def update(self, file_id: str, src: Path) -> None:
        self._resumable("PATCH", f"{self.UPLOAD}/files/{file_id}?uploadType=resumable&supportsAllDrives=true&fields={self.FIELDS}", {}, src)

    def upload(self, src: Path, parent_id: str, name: str | None = None) -> str:
        meta = {"name": name or src.name, "parents": [parent_id]}
        res = self._resumable("POST", f"{self.UPLOAD}/files?uploadType=resumable&supportsAllDrives=true&fields={self.FIELDS}", meta, src)
        return res["id"]

    def mkdir(self, name: str, parent_id: str) -> str:
        res = self._request("POST", f"{self.API}/files?supportsAllDrives=true&fields=id",
                            data=json.dumps({"name": name, "mimeType": FOLDER_MIME, "parents": [parent_id]}).encode(),
                            headers={"Content-Type": "application/json; charset=UTF-8"})
        return res["id"]

    def trash(self, file_id: str) -> None:
        self._request("PATCH", f"{self.API}/files/{file_id}?supportsAllDrives=true&fields=id",
                      data=json.dumps({"trashed": True}).encode(),
                      headers={"Content-Type": "application/json; charset=UTF-8"})


def make_backend(name: str) -> DriveBackend:
    if name == "auto":
        name = "api" if os.environ.get("GDRIVE_OAUTH_REFRESH_TOKEN") else "cli"
    return DriveApiBackend.from_env() if name == "api" else GdriveCliBackend()


# --------------------------------------------------------------------------- helpers


def md5_file(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def read_version(text: str) -> tuple[str, int, int] | None:
    """Return (vX.Y.Z, MAJOR, MINOR) from a controlled header, or None."""
    m = VERSION_RE.search(text)
    return (m.group(1), int(m.group(2)), int(m.group(3))) if m else None


def archive_name_for(rel: str, downloaded: Path, existing_archive_names: set[str], today: str) -> str:
    p = Path(rel)
    stem, suffix = p.stem, p.suffix
    ver = None
    if suffix == ".md":
        v = read_version(downloaded.read_text(encoding="utf-8", errors="replace"))
        ver = v[0] if v else None
    tag = ver or today
    candidate = f"{stem}_{tag}{suffix}"
    n = 2
    while candidate in existing_archive_names:
        candidate = f"{stem}_{tag}-r{n:02d}{suffix}"
        n += 1
    existing_archive_names.add(candidate)
    return candidate


def should_archive(policy: str, kind: str, outgoing: Path | None, incoming: Path | None) -> tuple[bool, str]:
    """Decide whether the outgoing Drive copy goes to 99_Archive/ before it is replaced."""
    if policy == "none":
        return False, "archive policy none"
    if policy == "all":
        return True, "archive policy all"
    if kind == "REMOVE":
        return True, "removed active file (A01 §5.7.3)"
    if outgoing is None or incoming is None or outgoing.suffix != ".md":
        return False, "unversioned file: in-place update"
    old = read_version(outgoing.read_text(encoding="utf-8", errors="replace"))
    new = read_version(incoming.read_text(encoding="utf-8", errors="replace"))
    if not old or not new:
        return False, "no version header: in-place update"
    if (old[1], old[2]) != (new[1], new[2]):
        return True, f"{old[0]} -> {new[0]} (MAJOR/MINOR, A01 §5.7.2)"
    return False, f"{old[0]} -> {new[0]} (ERRATA: in-place update)"


# --------------------------------------------------------------------------- planning


@dataclass
class Action:
    kind: str  # MKDIR, UPLOAD, UPDATE, REMOVE, ARCHIVE_SEED, RETIRE_DRAFTS
    target: str
    detail: str
    archive: bool = False
    archive_reason: str = ""


@dataclass
class Plan:
    actions: list[Action] = field(default_factory=list)
    drive_dirs: dict[str, str] = field(default_factory=dict)
    drive_files: dict[str, dict] = field(default_factory=dict)
    local_dirs: list[str] = field(default_factory=list)
    local_files: dict[str, Path] = field(default_factory=dict)
    archive_names: set[str] = field(default_factory=set)
    seed_uploads: list[tuple[str, Path]] = field(default_factory=list)


def crawl_drive(be: DriveBackend, folder_id: str, prefix: str = "") -> tuple[dict[str, str], dict[str, dict]]:
    """Return (dir_rel -> id, file_rel -> item) for active mirror paths."""
    dirs: dict[str, str] = {"": folder_id} if not prefix else {}
    files: dict[str, dict] = {}
    for item in be.list(folder_id):
        rel = f"{prefix}/{item['name']}" if prefix else item["name"]
        if item.get("mimeType") == FOLDER_MIME:
            dirs[rel] = item["id"]
            if rel in SKIP_DIRS:
                continue
            sub_d, sub_f = crawl_drive(be, item["id"], rel)
            dirs.update(sub_d)
            files.update(sub_f)
        else:
            files[rel] = item
    return dirs, files


def local_tree(lib: Path = LIB) -> tuple[list[str], dict[str, Path]]:
    dirs: list[str] = []
    files: dict[str, Path] = {}
    for top in ACTIVE_TOP:
        p = lib / top
        if not p.exists():
            continue
        if p.is_file():
            files[top] = p
            continue
        dirs.append(top)
        for sub in sorted(p.rglob("*")):
            rel = sub.relative_to(lib).as_posix()
            if sub.is_dir():
                dirs.append(rel)
            elif sub.is_file():
                files[rel] = sub
    return dirs, files


def build_plan(be: DriveBackend, root_id: str, lib: Path, policy: str, scratch: Path,
               verify_bytes: bool = False, seed_dir: Path | None = None, retire_drafts: bool = False) -> Plan:
    plan = Plan()
    plan.drive_dirs, plan.drive_files = crawl_drive(be, root_id)
    plan.local_dirs, plan.local_files = local_tree(lib)
    if "99_Archive" in plan.drive_dirs:
        plan.archive_names = {i["name"] for i in be.list(plan.drive_dirs["99_Archive"])}

    for d in plan.local_dirs:
        if d not in plan.drive_dirs:
            plan.actions.append(Action("MKDIR", d, "create missing mirror folder"))

    for rel, path in sorted(plan.local_files.items()):
        size = path.stat().st_size
        remote = plan.drive_files.get(rel)
        if remote is None:
            plan.actions.append(Action("UPLOAD", rel, f"new file ({size} B)"))
            continue
        remote_size = int(remote.get("size", -1))
        remote_md5 = remote.get("md5Checksum")
        outgoing: Path | None = None
        if remote_size != size:
            detail = f"size changed ({remote_size} B -> {size} B)"
        elif remote_md5:
            if remote_md5 == md5_file(path):
                continue
            detail = f"content changed ({size} B, md5 differs)"
        elif path.suffix.lower() in TEXT_EXTS or verify_bytes:
            outgoing = scratch / f"{len(plan.actions)}_{path.name}"
            be.download(remote["id"], outgoing)
            if md5_file(outgoing) == md5_file(path):
                outgoing.unlink(missing_ok=True)
                continue
            detail = f"content changed ({size} B, md5 differs)"
        else:
            continue
        if policy == "versioned" and path.suffix == ".md" and outgoing is None:
            outgoing = scratch / f"{len(plan.actions)}_{path.name}"
            be.download(remote["id"], outgoing)
        arc, why = should_archive(policy, "UPDATE", outgoing, path)
        plan.actions.append(Action("UPDATE", rel, detail, arc, why))

    for rel, remote in sorted(plan.drive_files.items()):
        if rel not in plan.local_files:
            arc, why = should_archive(policy, "REMOVE", None, None)
            plan.actions.append(Action("REMOVE", rel, f"not in GitHub active tree (id={remote['id']})", arc, why))

    if seed_dir and seed_dir.exists():
        for p in sorted(seed_dir.iterdir()):
            if p.is_file() and p.name not in plan.archive_names:
                plan.seed_uploads.append((p.name, p))
                plan.actions.append(Action("ARCHIVE_SEED", f"99_Archive/{p.name}", f"preserve historical file ({p.stat().st_size} B)"))

    if retire_drafts and "98_Drafts" in plan.drive_dirs:
        plan.actions.append(Action("RETIRE_DRAFTS", "98_Drafts", f"trash retired non-controlled folder (id={plan.drive_dirs['98_Drafts']})"))
    return plan


def apply_plan(be: DriveBackend, plan: Plan, root_id: str, today: str, log=print) -> None:
    needs_archive = any(a.archive for a in plan.actions) or plan.seed_uploads
    archive_id = plan.drive_dirs.get("99_Archive")
    if needs_archive and not archive_id:
        archive_id = be.mkdir("99_Archive", root_id)
        plan.drive_dirs["99_Archive"] = archive_id
        log("Created folder 99_Archive")

    for d in plan.local_dirs:  # parents precede children (sorted rglob)
        if d not in plan.drive_dirs:
            parent = Path(d).parent.as_posix()
            parent = "" if parent == "." else parent
            plan.drive_dirs[d] = be.mkdir(Path(d).name, plan.drive_dirs[parent])
            log(f"Created folder {d}")

    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        for a in plan.actions:
            if a.kind in ("UPDATE", "REMOVE"):
                remote = plan.drive_files[a.target]
                if a.archive:
                    dl = tmp_dir / Path(a.target).name
                    be.download(remote["id"], dl)
                    name = archive_name_for(a.target, dl, plan.archive_names, today)
                    be.upload(dl, archive_id, name)
                    log(f"Archived outgoing {a.target} -> 99_Archive/{name} ({a.archive_reason})")
                if a.kind == "UPDATE":
                    be.update(remote["id"], plan.local_files[a.target])
                    log(f"Updated in-place {a.target}")
                else:
                    be.trash(remote["id"])
                    log(f"Trashed retired active file {a.target}")
            elif a.kind == "UPLOAD":
                parent = Path(a.target).parent.as_posix()
                parent = "" if parent == "." else parent
                be.upload(plan.local_files[a.target], plan.drive_dirs[parent])
                log(f"Uploaded new file {a.target}")
            elif a.kind == "ARCHIVE_SEED":
                name = a.target.split("/", 1)[1]
                src = dict(plan.seed_uploads)[name]
                be.upload(src, archive_id, name)
                log(f"Seeded archive {a.target}")
            elif a.kind == "RETIRE_DRAFTS":
                be.trash(plan.drive_dirs["98_Drafts"])
                log("Trashed retired 98_Drafts/")


def render_summary(plan: Plan, mode: str, root_id: str, commit: str | None) -> str:
    lines = [f"## Drive publish ({mode})", ""]
    if commit:
        lines.append(f"- **Commit:** `{commit}`")
    lines += [f"- **Drive folder:** `{root_id}`", f"- **Planned actions:** {len(plan.actions)}", ""]
    if plan.actions:
        lines += ["| Action | Path | Detail | Archive |", "| :--- | :--- | :--- | :--- |"]
        for a in plan.actions:
            arc = f"yes: {a.archive_reason}" if a.archive else (a.archive_reason or "—")
            lines.append(f"| `{a.kind}` | `{a.target}` | {a.detail} | {arc} |")
    else:
        lines.append("Drive mirror matches `Standards Design/` on this commit.")
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------- main


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--drive-root-id", default=DEFAULT_DRIVE_ROOT_ID, help="Google Drive folder ID for Standards Design")
    ap.add_argument("--backend", choices=["auto", "api", "cli"], default="auto", help="Drive access method (default: auto)")
    ap.add_argument("--apply", action="store_true", help="Apply mutations to Google Drive (default is dry-run)")
    ap.add_argument("--dry-run", action="store_true", help="Preview changes without modifying Drive (default)")
    ap.add_argument("--archive-policy", choices=["versioned", "all", "none"], default="versioned",
                    help="When to snapshot outgoing Drive files into 99_Archive/ (default: versioned)")
    ap.add_argument("--archive-outgoing", action="store_true", help="Alias for --archive-policy all")
    ap.add_argument("--retire-drafts", action="store_true", help="Trash retired 98_Drafts/ folder from the mirrored Drive root")
    ap.add_argument("--seed-archive-dir", type=Path, help="Optional local folder of historical archive files to append into Drive 99_Archive/ if absent")
    ap.add_argument("--verify-bytes", action="store_true", help="Download and hash size-matching binaries when Drive gives no checksum")
    ap.add_argument("--summary", type=Path, help="Append a Markdown summary of the plan to this file (e.g. $GITHUB_STEP_SUMMARY)")
    ap.add_argument("--plan-json", type=Path, help="Write the planned actions as JSON to this file")
    ap.add_argument("--fail-on-drift", action="store_true", help="Exit 2 when any action is planned (drift detection)")
    args = ap.parse_args(argv)
    do_apply = args.apply and not args.dry_run
    policy = "all" if args.archive_outgoing else args.archive_policy
    today = dt.date.today().isoformat()

    if not LIB.exists():
        raise SystemExit(f"Library folder not found: {LIB}")

    be = make_backend(args.backend)
    with tempfile.TemporaryDirectory() as scratch:
        plan = build_plan(be, args.drive_root_id, LIB, policy, Path(scratch),
                          verify_bytes=args.verify_bytes, seed_dir=args.seed_archive_dir,
                          retire_drafts=args.retire_drafts)

    mode = "APPLY" if do_apply else "DRY-RUN"
    print(f"=== Standards Design Drive Publish ({mode}, backend={type(be).__name__}, archive={policy}) ===")
    print(f"Source: {LIB}")
    print(f"Target Drive folder ID: {args.drive_root_id}")
    print(f"Planned actions: {len(plan.actions)}")
    for a in plan.actions:
        arc = f"  [archive: {a.archive_reason}]" if a.archive else ""
        print(f"  [{a.kind:13s}] {a.target} — {a.detail}{arc}")

    commit = os.environ.get("GITHUB_SHA")
    if args.summary:
        with args.summary.open("a", encoding="utf-8") as fh:
            fh.write(render_summary(plan, mode, args.drive_root_id, commit))
    if args.plan_json:
        args.plan_json.write_text(json.dumps([a.__dict__ for a in plan.actions], indent=2), encoding="utf-8")

    if do_apply and plan.actions:
        apply_plan(be, plan, args.drive_root_id, today)
        print("\nPublish complete.")
    elif not do_apply:
        print("\nDry-run complete. Re-run with --apply to execute.")
    else:
        print("\nNothing to publish.")

    if args.fail_on_drift and plan.actions and not do_apply:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
