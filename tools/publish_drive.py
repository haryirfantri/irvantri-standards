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
  * Before overwriting or removing an active file on Drive, optionally snapshots
    the outgoing Drive copy into 99_Archive/ with a collision-free suffix
    (_vX.Y.Z for versioned Markdown/HTML, or _YYYY-MM-DD[-rNN] for assets/templates).
  * Updates existing Drive files in-place (`gdrive mutate update`) so Drive file
    IDs and shared links remain stable.
  * Defaults to --dry-run; pass --apply to execute mutations.

Usage (from the repository root):
    python3 tools/publish_drive.py --dry-run
    python3 tools/publish_drive.py --apply --archive-outgoing
    python3 tools/publish_drive.py --apply --retire-drafts
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT / "Standards Design"
DEFAULT_DRIVE_ROOT_ID = os.environ.get("STANDARDS_DESIGN_DRIVE_ID", "17-hTsw-2MIT-SzA6pRgzocpKTy1vwYin")
ACTIVE_TOP = ["Library-Index.md", "01_Standards", "02_Assets", "03_Templates", "04_Publications", "05_Records", "06_Dependencies"]


def run_gdrive(*args: str, parse_json: bool = False):
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


def list_drive_folder(folder_id: str) -> list[dict]:
    data = run_gdrive("readonly", "ls", folder_id, parse_json=True)
    if isinstance(data, dict):
        return data.get("files", [])
    return data


def crawl_drive(folder_id: str, prefix: str = "") -> tuple[dict[str, str], dict[str, dict]]:
    """Return (dir_rel -> id, file_rel -> item_dict) for active mirror paths."""
    dirs: dict[str, str] = {"": folder_id}
    files: dict[str, dict] = {}
    items = list_drive_folder(folder_id)
    for item in items:
        name = item["name"]
        rel = f"{prefix}/{name}" if prefix else name
        mime = item.get("mimeType", "")
        if mime == "application/vnd.google-apps.folder":
            dirs[rel] = item["id"]
            if rel in ("99_Archive", "98_Drafts"):
                continue
            sub_d, sub_f = crawl_drive(item["id"], rel)
            dirs.update(sub_d)
            files.update(sub_f)
        else:
            files[rel] = item
    return dirs, files


def local_tree() -> tuple[list[str], dict[str, Path]]:
    dirs: list[str] = []
    files: dict[str, Path] = {}
    for top in ACTIVE_TOP:
        p = LIB / top
        if not p.exists():
            continue
        if p.is_file():
            files[top] = p
            continue
        dirs.append(top)
        for sub in sorted(p.rglob("*")):
            rel = sub.relative_to(LIB).as_posix()
            if sub.is_dir():
                dirs.append(rel)
            elif sub.is_file():
                files[rel] = sub
    return dirs, files


def md5_file(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def archive_name_for(rel: str, downloaded: Path, existing_archive_names: set[str], today: str) -> str:
    p = Path(rel)
    stem, suffix = p.stem, p.suffix
    ver = None
    if suffix == ".md":
        text = downloaded.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"^\|\s*\*\*Version\*\*\s*\|\s*`(v\d+\.\d+\.\d+)`\s*\|", text, flags=re.M)
        if m:
            ver = m.group(1)
    tag = ver or today
    candidate = f"{stem}_{tag}{suffix}"
    n = 2
    while candidate in existing_archive_names:
        candidate = f"{stem}_{tag}-r{n:02d}{suffix}"
        n += 1
    existing_archive_names.add(candidate)
    return candidate


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--drive-root-id", default=DEFAULT_DRIVE_ROOT_ID, help="Google Drive folder ID for Standards Design")
    ap.add_argument("--apply", action="store_true", help="Apply mutations to Google Drive (default is dry-run)")
    ap.add_argument("--dry-run", action="store_true", help="Preview changes without modifying Drive (default)")
    ap.add_argument("--archive-outgoing", action="store_true", help="Snapshot replaced/removed Drive files into 99_Archive/ before updating")
    ap.add_argument("--retire-drafts", action="store_true", help="Trash retired 98_Drafts/ folder from the mirrored Drive root")
    ap.add_argument("--seed-archive-dir", type=Path, help="Optional local folder of historical archive files to append into Drive 99_Archive/ if absent")
    ap.add_argument("--verify-bytes", action="store_true", help="Download and hash even size-matching binary files")
    args = ap.parse_args()
    do_apply = args.apply and not args.dry_run
    today = dt.date.today().isoformat()

    if not LIB.exists():
        raise SystemExit(f"Library folder not found: {LIB}")

    drive_dirs, drive_files = crawl_drive(args.drive_root_id)
    local_dirs, local_files = local_tree()

    archive_id = drive_dirs.get("99_Archive")
    existing_archive_names: set[str] = set()
    if archive_id:
        for item in list_drive_folder(archive_id):
            existing_archive_names.add(item["name"])

    actions: list[tuple[str, str, str]] = []

    # 1. Folders to create
    for d in local_dirs:
        if d not in drive_dirs:
            actions.append(("MKDIR", d, "create missing mirror folder"))

    # 2. Files to upload or update in-place
    text_exts = {".md", ".json", ".css", ".svg", ".html", ".txt"}
    with tempfile.TemporaryDirectory() as check_tmp:
        check_dir = Path(check_tmp)
        for rel, path in sorted(local_files.items()):
            local_size = path.stat().st_size
            if rel not in drive_files:
                actions.append(("UPLOAD", rel, f"new file ({local_size} B)"))
                continue
            remote = drive_files[rel]
            remote_size = int(remote.get("size", -1))
            if remote_size != local_size:
                actions.append(("UPDATE", rel, f"size changed ({remote_size} B -> {local_size} B)"))
            elif path.suffix.lower() in text_exts or args.verify_bytes:
                dl = check_dir / Path(rel).name
                run_gdrive("readonly", "download", remote["id"], "--out", str(dl))
                if md5_file(dl) != md5_file(path):
                    actions.append(("UPDATE", rel, f"content changed ({local_size} B, md5 differs)"))
                dl.unlink(missing_ok=True)

    # 3. Active files on Drive no longer present in GitHub Standards Design/
    for rel, remote in sorted(drive_files.items()):
        if rel not in local_files:
            actions.append(("REMOVE", rel, f"not in GitHub active tree (id={remote['id']})"))

    # 4. Optional seed archive uploads (append-only)
    seed_uploads: list[tuple[str, Path]] = []
    if args.seed_archive_dir and args.seed_archive_dir.exists():
        for p in sorted(args.seed_archive_dir.iterdir()):
            if p.is_file() and p.name not in existing_archive_names:
                seed_uploads.append((p.name, p))
                actions.append(("ARCHIVE_SEED", f"99_Archive/{p.name}", f"preserve historical file ({p.stat().st_size} B)"))

    # 5. Optional retire 98_Drafts/
    if args.retire_drafts and "98_Drafts" in drive_dirs:
        actions.append(("RETIRE_DRAFTS", "98_Drafts", f"trash retired non-controlled folder (id={drive_dirs['98_Drafts']})"))

    mode = "APPLY" if do_apply else "DRY-RUN"
    print(f"=== Standards Design Drive Publish ({mode}) ===")
    print(f"Source: {LIB}")
    print(f"Target Drive folder ID: {args.drive_root_id}")
    print(f"Planned actions: {len(actions)}")
    for kind, target, detail in actions:
        print(f"  [{kind:13s}] {target} — {detail}")

    if not do_apply:
        print("\nDry-run complete. Re-run with --apply to execute.")
        return 0

    # Ensure 99_Archive exists if needed
    if (args.archive_outgoing or seed_uploads) and not archive_id:
        out = run_gdrive("mutate", "mkdir", "99_Archive", "--parent", args.drive_root_id)
        print(out)
        drive_dirs, _ = crawl_drive(args.drive_root_id)
        archive_id = drive_dirs["99_Archive"]

    # Execute MKDIR in topological order
    for d in local_dirs:
        if d not in drive_dirs:
            parent_rel = str(Path(d).parent)
            parent_rel = "" if parent_rel == "." else parent_rel
            parent_id = drive_dirs[parent_rel]
            name = Path(d).name
            run_gdrive("mutate", "mkdir", name, "--parent", parent_id)
            for item in list_drive_folder(parent_id):
                if item["name"] == name:
                    drive_dirs[d] = item["id"]
                    break
            print(f"Created folder {d} ({drive_dirs[d]})")

    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        # Execute UPDATE and REMOVE (archiving outgoing if requested)
        for kind, rel, _ in actions:
            if kind in ("UPDATE", "REMOVE"):
                remote = drive_files[rel]
                if args.archive_outgoing and archive_id:
                    dl = tmp_dir / Path(rel).name
                    run_gdrive("readonly", "download", remote["id"], "--out", str(dl))
                    arc_name = archive_name_for(rel, dl, existing_archive_names, today)
                    arc_path = tmp_dir / arc_name
                    dl.rename(arc_path)
                    run_gdrive("mutate", "upload", str(arc_path), "--parent", archive_id)
                    print(f"Archived outgoing {rel} -> 99_Archive/{arc_name}")
                if kind == "UPDATE":
                    run_gdrive("mutate", "update", remote["id"], str(local_files[rel]))
                    print(f"Updated in-place {rel}")
                else:
                    run_gdrive("mutate", "trash", remote["id"])
                    print(f"Trashed retired active file {rel}")
            elif kind == "UPLOAD":
                parent_rel = str(Path(rel).parent)
                parent_rel = "" if parent_rel == "." else parent_rel
                run_gdrive("mutate", "upload", str(local_files[rel]), "--parent", drive_dirs[parent_rel])
                print(f"Uploaded new file {rel}")

        # Seed append-only archive files
        for name, p in seed_uploads:
            run_gdrive("mutate", "upload", str(p), "--parent", archive_id)
            print(f"Seeded archive 99_Archive/{name}")

        # Retire 98_Drafts if requested
        if args.retire_drafts and "98_Drafts" in drive_dirs:
            run_gdrive("mutate", "trash", drive_dirs["98_Drafts"])
            print("Trashed retired 98_Drafts/")

    print("\nPublish complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
