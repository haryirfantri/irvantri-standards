# Standards Design Tools & Library Checks

`library_checks.py` measures the real files in `Standards Design/` and writes a report that governance records can cite as evidence for the Section 6 checks listed below. It reads its rules from the live library where they are written as data: the palette from `B02` Section 5, versions and statuses from `Library-Index.md`, and checksums from `06_Dependencies/Dependencies-Manifest.md`.

## Run checks

```sh
pip install -r tools/requirements.txt
python3 tools/library_checks.py --report-dir check-report
```

It writes `check-report/check-report.json` (every measurement) and `check-report/check-report.md` (summary), and exits with status `1` if any finding fails and is not listed in `known-issues.json`.

The GitHub Actions workflow `.github/workflows/library-checks.yml` runs the same command on every pull request and every push to `main`, shows the summary on the run page, and keeps the report as an artifact named `library-check-report-<commit>` for 400 days.

## What `library_checks.py` verifies

| Check | What is measured | Evidence for |
| :--- | :--- | :--- |
| `register-sync` | Version, status and next-review date in each standard's header against `Library-Index.md`; every registered path exists (except `Planned`/`Deprecated`); every file in `02_`–`05_` is registered | `A01` header metadata, `A02-C3`, `A02-C5`, `A02-C9` |
| `palette` | Every `#RRGGBB` and `rgb()` value in active `.md` (excluding Revision History and terminal `05_Records/`), `.svg`, `.html`, `.json`, `.css` files is a `B02` value and uppercase | `B02-C1`, `B02-C2`, `D01-C2` |
| `token-parity` | `AST-D01-01` colors, `RGB` and `CMYK` against `B02`; every reference resolves; JSON embedded in HTML equals the master; `--is-` custom properties equal their token values | `D01-C2`, `D01-C3`, `B02-C1` |
| `token-css` | Verifies `AST-D01-02_Design-Tokens.css` matches a fresh build from `AST-D01-01` via `tools/build_tokens_css.py`, and that `AST-D03-01_Component-Kit.css` contains zero raw hexadecimal colors | `D01-C3`, `D03-C1` |
| `contrast` | WCAG 2.2 ratios for the pairings in `contrast-pairs.json`, plus ratios quoted in library text checked against the math | `B02-C5`, `D01-C2`, `D04-C1`, `D04-C2` |
| `links` | Relative links in Markdown, HTML and SVG, and backticked library paths in the register and manifest (revision history skipped) | `A02-C5`, `A02-C7`, `E01-C3` |
| `pdf-preflight` | Print: `PDF/X-4` in Info and XMP, one `FOGRA39` CMYK OutputIntent, A4 trim, 3 mm bleed, embedded fonts, CMYK-only operators on `B02` builds, total ink ≤ 300%, no undefined font resources. Digital: exact A4, no bleed, embedded fonts, `sRGB` values on the `B02` palette | `E03-C1`, `E03-C3`, `E03-C4`, `E01-C4` |
| `press-export` | Runs `press_export.py` on each `fixtures/*press-layout.pdf` sample and preflights the `PDF/X-4` result: A4 trim, 3 mm bleed, `FOGRA39`, only `B02` CMYK builds, total ink ≤ 300%, embedded fonts | `E01-C3`, `E03-C1`, `E03-C3`, `E03-C4` |
| `html-master` | For every registered `HTML` template: literal colors in style rules, free-text fields without a declared character limit, `Save filled copy` and unsaved-changes warning, `Press preview` beside a press export, remote requests, fonts and script libraries embedded byte-identical to `06_Dependencies/` (SHA-256), an `ARIA` Live Region, and that `TPL-E01-06` equals a fresh build from `tools/document-master/`. Enforced only for templates pinned to `E01 (v2.5)` / `E04 (v2.3)` or later (`E01 §5.5.1`) | `E01-C5`, `E04-C4`, `D04-C3` |
| `dependencies` | SHA-256 and byte size of every font, ICC profile and script library against the manifest; no unlisted binaries or scripts; each font folder carries the full OFL-1.1 text and each script folder its MIT `LICENSE`, with a copyright line | `B03-C2`, `A02-C10`, `E03-C4` |

## Generated CSS Tokens (`AST-D01-02`)

`Standards Design/02_Assets/AST-D01-02_Design-Tokens.css` is generated from `AST-D01-01_Design-Tokens.json`. Never edit it by hand:

```sh
python3 tools/build_tokens_css.py          # regenerates AST-D01-02
python3 tools/build_tokens_css.py --check  # exit 1 on drift
```

## Press export (`E01 §5.3.4`)

```sh
pip install -r tools/requirements.txt
python3 tools/press_export.py cover-press.pdf --title "Document title"
```

Replaces each sRGB color with its fixed `B02 §5.1.1` or `§5.6.1` CMYK build from a lookup table, sets A4 TrimBox and 3 mm BleedBox, attaches `ISOcoated_v2_eci.icc` (`FOGRA39`), writes `PDF/X-4` metadata, and preflights the output.

## Formal Document Master (`TPL-E01-06`)

`Standards Design/03_Templates/TPL-E01-06_Formal-Document-Master.html` is generated from `tools/document-master/`:

```sh
python3 tools/build_document_master.py          # writes the template
python3 tools/build_document_master.py --check  # exit 1 if stale
```

The template opens as a blank `Draft` with a **How to use this template** panel, **Start blank document** and **Load sample document** buttons, and a **Markdown cheat sheet**. The sample (`sampleState()` in `app.js`) is the document behind `fixtures/TPL-E01-06_press-layout.pdf`; load it before saving a fresh fixture. The one-page author guide is `Standards Design/04_Publications/PUB-04_Document-Master-Quick-Start.md`; update it when the workflow or the Export Block messages change.

After **Export A4 PDF**, finish the digital PDF so document properties and bookmarks match `E05 §5.9.2`:

```sh
python3 tools/pdf_finish.py "REF-001 Title v1.0.0.pdf"
```

## Publishing one-way to Google Drive (`A01 §5.9.3`)

Google Drive (`Standards Design/`, folder ID `17-hTsw-2MIT-SzA6pRgzocpKTy1vwYin`) mirrors `Standards Design/` one-way from GitHub `main` and hosts the append-only `99_Archive/` Cold Archive.

### Automatic: every merge to `main`

| Workflow | When | What it does |
| :--- | :--- | :--- |
| `.github/workflows/publish-drive.yml` | Every push to `main` that changes `Standards Design/` (each merged pull request); manual run with an optional dry run | Runs `library_checks.py`, then `publish_drive.py --apply`, one run at a time in merge order. Writes the plan to the run summary. Creates the annotated tag `register-vX.Y.Z` for the `Library-Index.md` version if it does not exist yet (`A01 §5.7.2`). |
| `.github/workflows/drive-drift.yml` | Daily 06:17 UTC; manual | Read-only comparison of Drive with `main`. Opens one issue labelled `drive-drift` when Drive differs or authentication fails, and closes it when Drive matches again. |

Files are updated in place, so Drive file IDs and shared links never change. With the default `--archive-policy versioned`, the outgoing Drive copy goes to `99_Archive/` only when its `vMAJOR.MINOR` changes (`A01 §5.5.3`, `§5.5.4`, `§5.7.2`) or the file is removed (`A01 §5.7.3`); `ERRATA` updates and unversioned assets are updated in place, with Git history and release tags as their record. Nothing in `99_Archive/` is ever modified or deleted.

### One-time setup (library Owner)

Drive is in a personal Google account, so CI signs in as the Owner with an OAuth refresh token (a service account cannot create files in a personal My Drive).

1. In the [Google Cloud Console](https://console.cloud.google.com/), create a project (for example `irvantri-standards-publish`) and enable the **Google Drive API**.
2. **OAuth consent screen:** User type *External*; app name `Standards Design Publisher`; add your Google account as a test user; then press **Publish app** so the status reads *In production*. Refresh tokens of apps left in *Testing* expire after 7 days. Google shows an "unverified app" warning when you sign in; choose *Advanced → Go to … (unsafe)*. That is expected for a private app only you use.
3. **Credentials → Create credentials → OAuth client ID →** application type *Desktop app*. Note the client ID and client secret.
4. On your own computer, signed in to the Google account that owns `Standards Design`:

   ```sh
   python3 tools/drive_oauth_token.py --client-id "<client id>" --client-secret "<client secret>"
   ```

   Approve access in the browser; the script prints the refresh token.
5. In GitHub: **Settings → Secrets and variables → Actions → New repository secret**, add `GDRIVE_OAUTH_CLIENT_ID`, `GDRIVE_OAUTH_CLIENT_SECRET`, and `GDRIVE_OAUTH_REFRESH_TOKEN`.
6. **Actions → Publish to Google Drive → Run workflow** with *dry run* ticked to confirm access, then once more unticked to publish.

The token grants Drive access to your account: keep it only in GitHub Secrets. To revoke it, remove the app at <https://myaccount.google.com/permissions>; the next drift check will open an issue until a new token is stored.

### Manual (local or agent session)

```sh
python3 tools/publish_drive.py --dry-run          # preview (gdrive CLI, or the API when GDRIVE_OAUTH_* is set)
python3 tools/publish_drive.py --apply            # publish with the versioned archive policy
python3 -m unittest discover -s tools/tests -v    # publisher tests
```

## Citing a run in a record

Cite the commit, the run URL and the check ID (`A04 §5.1.7`), for example: "`contrast` passed, 39 pairings, minimum 5.10:1 (library checks run `<url>`, commit `<sha>`)".
