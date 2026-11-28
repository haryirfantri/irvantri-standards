# Agent & Contributor Playbook (`irvantri-standards`)

Read this before modifying files in `Standards Design/` or `tools/`.

## 1. Repository rules
- **Authoring Repository of Record (`A01 §5.9.1`):** `Standards Design/` on GitHub `main`. Never edit files directly in Google Drive.
- **Branching (`A01 §5.9.2`):** Author all changes on a feature branch and open a Pull Request. Never commit directly to `main`. Never create a `98_Drafts/` folder.
- **No version suffixes in active filenames (`A01 §5.7.1`):** Active files in `01_Standards/`–`05_Records/` follow `CODE_Title-Words.ext` with no version number.

## 2. Never hand-edit generated files
Rebuild these from their sources and verify with `--check`:

| Generated file | Source | Rebuild command |
| :--- | :--- | :--- |
| `Standards Design/02_Assets/AST-D01-02_Design-Tokens.css` | `AST-D01-01_Design-Tokens.json` | `python3 tools/build_tokens_css.py` |
| `Standards Design/03_Templates/TPL-E01-06_Formal-Document-Master.html` | `tools/document-master/*` | `python3 tools/build_document_master.py` |
| `README.md` (status & counts blocks) | `Standards Design/Library-Index.md` | `python3 tools/build_readme.py` |

## 3. Release checklist (before opening a PR)
1. Use `python3 tools/bump.py <CODE|INDEX> <major|minor|errata> --note "..."` (preview with `--dry-run` first) to update headers, Section 8/10 Revision History, `Library-Index.md`, `Sync Required` transitions on `MAJOR` bumps (`A01 §5.5.3`), and `README.md` stats together.
2. Refresh any `PUB-` build manifests listed by `bump.py` and update `AST-`/`TPL-` pins (`A01 §5.7.4`) as needed.
3. Add a `REC-A04-0xx` Pre-Release Gate record in `05_Records/` and register it in `Library-Index.md` (`A04 §5.1.5`).
4. Run checks locally:
   ```sh
   python3 -m unittest discover -s tools/tests -v
   python3 tools/library_checks.py --report-dir check-report
   python3 tools/build_tokens_css.py --check
   python3 tools/build_document_master.py --check
   python3 tools/build_readme.py --check
   ```
5. After CI passes on the PR, cite the CI run URL and commit SHA in the `REC-A04-0xx` record (`A04 §5.1.7`).

## 4. After merging to `main` (Google Drive publish — required)
Google Drive (`Standards Design/`, folder ID `17-hTsw-2MIT-SzA6pRgzocpKTy1vwYin`) is published **one-way from `main`** by the agent or Owner using the signed-in `gdrive` CLI (`A01 §5.9.3`):

```sh
git checkout main && git pull --ff-only
python3 tools/publish_drive.py --dry-run   # review planned actions
python3 tools/publish_drive.py --apply     # updates in place; archives MAJOR/MINOR & removals only
python3 tools/publish_drive.py --dry-run --fail-on-drift  # confirm 0 pending actions
```

- Always run on `main` **after** the PR is merged (never from a feature branch).
- The default `--archive-policy versioned` snapshots outgoing files to `99_Archive/` only on `MAJOR`/`MINOR` changes (`A01 §5.7.2`) or file removals (`A01 §5.7.3`). Never delete anything in `99_Archive/`.
- If `gdrive` is not connected in your session, tell the Owner clearly that Drive still needs publishing from `main`.
- GitHub Actions (`.github/workflows/tag-release.yml`) automatically creates the annotated `register-vX.Y.Z` tag on `main` when `Library-Index.md` changes.
