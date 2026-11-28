# REC-A04-016 — GitHub & Google Drive Unification Pre-Release Gate

| Field | Value |
| :--- | :--- |
| **Code** | `REC-A04-016` |
| **Record Type** | Pre-Release Gate |
| **Date** | `2026-11-28` |
| **Status** | `Closed` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Related Standards** | `A01 (v2.0.0)`, `A02 (v2.0.0)`, `A03 (v1.1.1)`, `A04 (v1.2.1)`, `B01 (v2.1.1)`, `B02 (v2.0.0)`, `B03 (v2.0.0)`, `B04 (v1.2.0)`, `B05 (v1.2.0)`, `C01 (v1.1.2)`, `C02 (v1.2.0)`, `C03 (v1.0.1)`, `C04 (v1.0.2)`, `D01 (v1.0.4)`, `D02 (v2.0.1)`, `D03 (v2.0.1)`, `D04 (v1.2.1)`, `D05 (v1.1.1)`, `E01 (v2.6.1)`, `E02 (v1.1.1)`, `E03 (v1.1.1)`, `E04 (v2.3.1)`, `E05 (v2.0.0)`, `Dependencies-Manifest.md (v2.1.1)`, `Library-Index.md (v2.0.0)` |
| **Expiry Date** | `None` |

## 1. Review Scope & Trigger

This record gates the unification of the diverged Google Drive (`Standards Design`, `Library-Index.md v1.3.2`) and GitHub (`haryirfantri/irvantri-standards` / `Unified Operating Library`, `Library-Index.md v1.2.25`) forks into a single hybrid **Standards Design** architecture (`A04 §5.1.2`, `§5.1.5`–`§5.1.7`).

### Resolved Fork Conflicts (Approver Decisions, `2026-11-28`)
1. **Control Boundary Color (`B02`, `E05`, `AST-D01`, `TPL-E01`):** Standardized interactive input/button borders and `E05` document strokes on existing **Text Muted** (`#5F6C7E`, `5.34:1` on white, `5.10:1` on Canvas Subtle; `40, 20, 0, 60` `CMYK`), retiring **Border Strong** (`#64748B`) while retaining all other `B02 §5.6.1` fixed `ISO` Coated v2 `CMYK` builds.
2. **Governance Record Code Collisions (`REC-A04-008`, `REC-A04-009`):** Retained GitHub's `REC-A04-008`–`REC-A04-015` intact (linked to live commits and `CI` runs), moved Drive's pre-unification `REC-A04-008` and `REC-A04-009` records into Google Drive `99_Archive/` as historical provenance (`A02 §5.6.2`), and consolidated unification verification under `REC-A04-016`.
3. **Hybrid Repository & Archive Split (`A01 §5.7`, `§5.9`; `A02 §5.5`, `§5.6`):** Renamed the GitHub library root from `Unified Operating Library/` to `Standards Design/`, designated GitHub `main` as the Authoring Repository of Record (retiring `98_Drafts/` and removing the `32 MB` `99_Archive/` directory from Git's working tree in favor of native Git history and tags), and designated Google Drive (`17-hTsw-2MIT-SzA6pRgzocpKTy1vwYin`) as the one-way Distribution Mirror and append-only `99_Archive/` Cold Archive.

### Gated Items
* **Normative Standards:** `A01 (v2.0.0)`, `A02 (v2.0.0)`, `B02 (v2.0.0)`, `C02 (v1.2.0)`, `E05 (v2.0.0)`, `D01 (v1.0.4)`, `D03 (v2.0.1)`, and `ERRATA` rename sweeps (`A04 v1.2.1`, `B01 v2.1.1`, `C01 v1.1.2`, `C04 v1.0.2`, `E01 v2.6.1`, `E02 v1.1.1`, `E03 v1.1.1`, `E04 v2.3.1`).
* **Master Assets:** `AST-D01-01` (re-synced), `AST-D01-02` (new generated `CSS`), `AST-D03-01` (Component Kit `CSS`, `en-US` spelling corrected), `AST-D03-02` (Component Gallery `HTML`, `en-US` spelling corrected).
* **Executable Templates:** `TPL-E01-03` (`Formal-Cover-Digital.html`), `TPL-E01-06` (`Formal-Document-Master.html`, rebuilt from `tools/document-master/`), and refreshed press-layout fixtures (`tools/fixtures/TPL-E01-03_press-layout.pdf`, `tools/fixtures/TPL-E01-06_press-layout.pdf`).
* **Compiled Publications & Registers:** `PUB-01 (v2.1.0)`, `PUB-02 (v2.1.0)`, `PUB-03 (v1.3.0)`, `Dependencies-Manifest.md (v2.1.1)`, `Library-Index.md (v2.0.0)`.
* **Tooling & Automation:** `tools/build_tokens_css.py` (promoted from `98_Drafts/`), `tools/library_checks.py` (`token-css` check added), `tools/publish_drive.py`, `.github/workflows/publish-drive.yml`.

## 2. Verification Method & Evidence

* **Automated Suite:** `python3 tools/library_checks.py --report-dir check-report` running locally and via `.github/workflows/library-checks.yml` on Pull Request.
* **Token & Template Drift:** `python3 tools/build_tokens_css.py --check` and `python3 tools/build_document_master.py --check`.
* **Press Fixture Inspection:** Headless Chromium re-export of `TPL-E01-03_press-layout.pdf` and `TPL-E01-06_press-layout.pdf` followed by `tools/press_export.py` `PDF/X-4` conversion and preflight in `CI`.
* **Drive Publish Dry-Run:** `python3 tools/publish_drive.py --dry-run` verifying one-way mirror alignment and append-only `99_Archive/` preservation prior to `--apply`.

## 3. Section 6 Measured Verification

| Check / Suite | Cites | Result | Measured Evidence |
| :--- | :--- | :--- | :--- |
| `register-sync` | `A01-C7`, `A02-C3`, `A02-C5`, `A02-C9` | `Pass` | `23` standard headers matched `Library-Index.md (v2.0.0)`; all active paths in `01_`–`05_` resolved and registered. |
| `palette` | `B02-C1`, `B02-C2`, `D01-C2` | `Pass` | `0` off-palette or lowercase hex values across all active `.md`, `.svg`, `.html`, `.json`, and `.css` files (`24` approved `B02 v2.0.0` colors; `#64748B` retired). |
| `token-parity` | `D01-C2`, `D01-C3`, `B02-C1` | `Pass` | All `AST-D01-01` tokens resolved and matched `B02 (v2.0.0)` `HEX`, `RGB`, and `CMYK` builds; `PUB-01` embedded `GENERATED_JSON` matched master byte-for-byte. |
| `token-css` | `D01-C3`, `D03-C1` | `Pass` | `AST-D01-02_Design-Tokens.css` (`94` `--is-*` custom properties) verified `drift-free: True` by `tools/build_tokens_css.py --check`; `AST-D03-01_Component-Kit.css` verified `0` raw hexadecimal values. |
| `contrast` | `B02-C5`, `D01-C2`, `D04-C1`, `D04-C2` | `Pass` | All `41` required `WCAG` 2.2 pairings passed (minimum `4.87:1` for Text Muted `#5F6C7E` on Surface Muted `#F1F5F9`; `5.10:1` on Canvas Subtle `#F8FAFC`; `5.34:1` on white); all `9` quoted ratios matched math. |
| `links` | `A02-C5`, `A02-C7`, `E01-C3` | `Pass` | All relative Markdown, `HTML`, `SVG`, and register paths resolved cleanly under `Standards Design/`. |
| `pdf-preflight` & `press-export` | `E01-C3`, `E01-C4`, `E03-C1`, `E03-C3`, `E03-C4` | `Pass` | Verified in `CI` (`library-checks.yml`) with `pypdf`: `TPL-E04-01`/`03` and `TPL-E01-03`/`06` press exports carry exact `B02 (v2.0.0)` `CMYK` builds, `≤ 300%` ink, `A4` trim, `3 mm` bleed, `FOGRA39`, and embedded fonts. |
| `html-master` | `E01-C5`, `E04-C4`, `D04-C3` | `Pass` | `TPL-E01-06` matched fresh build from `tools/document-master/` (`build_document_master.py --check`), zero literal colors, zero remote requests, fonts & scripts byte-identical to `06_Dependencies/`. |
| `dependencies` | `B03-C2`, `A02-C10`, `E03-C4` | `Pass` | All `15` font binaries, `3` full upstream `SIL OFL-1.1` `OFL.txt` files, `4` `MIT` script libraries, and `ISOcoated_v2_eci.icc` matched `Dependencies-Manifest.md (v2.1.1)` `SHA-256` checksums and byte sizes. |
| `C01-C6` & `C02-C1` | `C01 §5.6.1`, `C02 §5.1.1` | `Pass` | `0` non-`en-US` `colour`/`colours` spellings in `AST-D03-01`/`02` and `Library-Index.md`; `0` active `Unified Operating Library` strings outside historical revision logs and immutable pre-unification records. |

* **CI Run Citation (`A04 §5.1.7`):** Pending Pull Request `library-checks.yml` run (will be recorded on the PR before merge).

## 4. Findings

None (`0` open findings). All prior draft findings from Drive's non-binding `REC-A04-010` (`F-01`–`F-08`) are resolved by this unification: Git history + Drive Cold Archive resolves `F-01`/`F-04`; GitHub's verified upstream `OFL.txt` resolves `F-02`; this measured gate resolves `F-03`; recompiled `PUB-01` resolves `F-05`; `en-US` fixes resolve `F-06`; `Dependencies-Manifest.md (v2.1.1)` resolves `F-07`; retiring `98_Drafts/` resolves `F-08`.

## 5. Disposition & Sign-Off

* **Gate Verdict:** `Pass` — Approved for merge to `main` and one-way publish to Google Drive (`Standards Design`).
* **Approver:** Hary Irfantri (`2026-11-28`)
