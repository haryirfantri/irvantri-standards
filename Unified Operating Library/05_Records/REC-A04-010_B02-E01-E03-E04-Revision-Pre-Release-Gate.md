# REC-A04-010 — B02, E01, E03 & E04 Revision Pre-Release Gate

| Field | Value |
| :--- | :--- |
| **Code** | `REC-A04-010` |
| **Record Type** | Pre-Release Gate |
| **Date** | `2026-11-27` |
| **Status** | `Closed` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Related Standards** | `A01 (v1.2.0)`, `A02 (v1.3.0)`, `A04 (v1.2.0)`, `B02 (v1.3.0)`, `C01 (v1.1.1)`, `D01 (v1.0.3)`, `E01 (v2.3.0)`, `E03 (v1.1.0)`, `E04 (v2.2.0)`, `Library-Index.md (v1.2.20)` |
| **Expiry Date** | `None` |

## 1. Review Scope & Trigger

This Governance Record (`REC-`) documents the Pre-Release Gate (`A04 (v1.2.0) §5.1.2`, `§5.1.5`) for the items below, released together with `Library-Index.md (v1.2.20)`:

| Item | Change | Version Gated |
| :--- | :--- | :--- |
| `B02` | `MINOR`: new `5.6.1` print builds for neutral and semantic colors (`U-01`) | `v1.3.0` |
| `E01` | `MINOR`: new `5.4.5` `±0.5 mm` A4 tolerance for `HTML` master exports (`U-02`) | `v2.3.0` |
| `E03` | `MINOR`: new `5.1.5` Safe Margin measured to the outermost ink (`U-03`) | `v1.1.0` |
| `E04` | `MINOR`: new `5.2.6` slide type scale (`F-02`) | `v2.2.0` |
| `AST-D01-01` | Re-synced: `cmykIsoCoatedV2` builds and slide font sizes | `generatedDate` `2026-11-27` |
| `TPL-E01-01`, `TPL-E04-01` | Footer raised one `4 mm` step; neutral inks moved to `B02 §5.6.1` builds | Active file on this release branch |
| `TPL-E01-02` | Neutral inks moved to `B02 §5.6.1` builds | Active file on this release branch |
| `TPL-E01-04`, `TPL-E04-03` | Footer raised one `4 mm` step | Active file on this release branch |
| `PUB-01`, `PUB-02`, `PUB-03` | Source manifests refreshed; `PUB-03` typography regenerated | `v2.0.5`, `v2.0.4`, `v1.2.0` |

The trigger is the Approver's approval on `2026-11-27` of the values proposed for `REC-A04-009` (`F-02`, `F-03`, `U-01`–`U-03`).

## 2. Method

Every result below was measured on the delivered file on branch `claude/project-thread-tp1jkj`, based on `main` at `d5706e0`. The commit that holds every gated change is named in Section 6.

* **`PDF` structure and color:** `pypdf 6.17.0` read each page content stream and listed every `k`/`K` (`CMYK`) and `rg`/`RG` (`RGB`) operator. Total Area Coverage (`TAC`) is the sum of the four inks.
* **`PDF` geometry:** Poppler `pdftoppm 24.02.0` rendered each page at `300 DPI`. A script measured the ink bounding box in millimeters from the TrimBox.
* **Render comparison:** each template was rendered at `150 DPI` before and after the change, and the changed pixels were located.
* **`HTML` export:** headless Chromium (Playwright `1.63.0`) exported `TPL-E01-03` through `@media print`. Poppler `pdfinfo` read the page size.
* **Color conversion:** Pillow `13.0.0` with littleCMS `2.19` converted each `B02 §5.6.1` build through `06_Dependencies/Color-Profiles/ISOcoated_v2_eci.icc` (relative colorimetric). It reported ΔE76 against the `sRGB` value.
* **Standards text:** a script compared header fields, section order, Section 5 to Section 6 mapping, and Section 3 references, and scanned every added line for prohibited keywords, vague qualifiers, pronouns, and contractions. Sentence length was counted in words.
* **Automated check:** `tools/library_checks.py` (register sync, palette, token parity, contrast, links, `PDF` preflight, and dependencies).

> **Informative Note:** The `PDF` checks are structural. They are not a certified `PDF/X-4` (`ISO 15930-7:2010`) validation.

## 3. Section 6 Verification — Standards

| Check ID | Status | Measured Evidence |
| :--- | :--- | :--- |
| `A01-C2` | Pass | Each of `B02`, `E01`, `E03`, and `E04` has 9 header fields in order. Version, Status, and dates are `ISO` 8601. |
| `A01-C3` | Pass | Each file has level-2 sections `1`–`8` in order. New clauses are numbered (`B02 5.6.1`, `E01 5.4.5`, `E03 5.1.5`, `E04 5.2.6`). Informative notes use the `> **Informative Note:**` prefix. |
| `A01-C4` | Pass | The 64 added lines contain zero `MUST`, `WILL`, or `REQUIRED`, and zero vague qualifiers. Each new `SHALL` states a measurable value: a listed `CMYK` build, a `px` size, a `±0.5 mm` tolerance, or a distance to ink. |
| `A01-C5` | Pass | Each release adds clauses without changing existing `SHALL` text, so each is `MINOR` (`A01 (v1.2.0) §5.5.4`). Section 8 logs each one as `Minor`. |
| `A01-C6`, `A02-C6` | Pass | `99_Archive/` holds `B02_Color-System_v1.2.0.md`, `E01_Formal-Document-Layout_v2.2.0.md`, `E03_Print-and-Production-Specifications_v1.0.0.md`, and `E04_Correspondence-and-Presentations_v2.1.1.md`. Each `SHA-256` equals the outgoing file on `main` at `d5706e0` (`757f41c7…`, `cd1c58df…`, `b705d6d5…`, `b9c31578…`). |
| `A01-C7` | Pass | `tools/library_checks.py` `register-sync` compares 22 standard headers with `Library-Index.md (v1.2.20)` and reports zero mismatches. |
| `A01-C8` | Pass | No `MAJOR` increment, so no dependent item moves to `Sync Required`. |
| `C01-C2`, `C01-C3` | Pass | Zero pronouns and zero contractions in added lines. The longest sentence in each new clause is `21` (`B02`), `28` (`E01`), `22` (`E03`), and `28` (`E04`) words, within the `30`-word limit. Multi-attribute rules use tables (`B02 5.6.1`, `E04 5.2.6`). |
| Section 5 to 6 mapping | Pass | Every new clause is cited by a check: `5.6.1` in `B02-C1`, `5.4.5` in `E01-C4`, `5.1.5` in `E03-C1`, and `5.2.6` in `E04-C2`. Three older permissive clauses have no check (`B02 5.4.1` and `5.4.4`; `E03 5.2.3`). This release did not change them. |
| Section 3 parity | Pass | Every standard code cited in Sections 4–6 is listed in Section 3. `D01` was added to `E04` Section 3 for the `5.2.6` token reference. |

## 4. Section 6 Verification — Released Artifacts

| Item | Check ID | Status | Measured Evidence |
| :--- | :--- | :--- | :--- |
| `B02 5.6.1` builds | `B02-C1` | Pass | Re-converting all 21 builds gives the ΔE76 values in the `B02` table, from `0.0` (**Success**, **Danger Surface**) to `12.1` (**Success Border**, out of gamut). The highest `TAC` is `240%` (**Success**), within `E03 §5.3.5`. |
| `AST-D01-01` | `B02-C1`, `D01-C2` | Pass | `token-parity` compares 177 tokens (76 color) with `B02` with zero mismatches. Every `cmykIsoCoatedV2` extension equals its `B02` build. **Informative** foreground carries the **Brand Blue** build. |
| `AST-D01-01` | `D01-C1`, `D01-C3` | Pass | The new primitives `slide-title` (`64px`), `slide-heading` (`40px`), and `slide-body` (`24px`) have semantic tokens with `--is-font-size-slide-*` names. `PUB-01`'s embedded `JSON` parses equal to the master, and the generated `CSS` lists all three. |
| `TPL-E01-01`, `TPL-E01-02`, `TPL-E04-01` | `B02-C1`, `E03-C3` | Pass | Every `k`/`K` value is a `B02 §5.1.1` or `§5.6.1` build, paper white, or `100%` K. There are zero `RGB` operators. Maximum `TAC` is `250%` (**Deep Navy**). `pdf-preflight` reports zero `cmyk-off-palette` findings. |
| `TPL-E01-01`, `TPL-E04-01` | `E03-C1` | Pass | The lowest footer ink is `19.30 mm` and `19.39 mm` above trim, clear of the `16 mm` Safe Margin measured to outermost ink (`E03 §5.1.5`). The footer baseline is `20 mm`, on the `4 mm` grid. The header lockup top is `16.00 mm` below trim, from its placement at `796.54 pt` on an `841.89 pt` page. |
| `TPL-E01-04`, `TPL-E04-03` | `E01-C2`, `E04-C1` | Pass | The lowest footer ink is `19.22 mm` and `19.30 mm` above trim. The `150 DPI` before-and-after renders differ only in the band `15.4`–`28.1 mm` above the bottom edge, which is the footer. |
| `TPL-E01-01`–`TPL-E01-04`, `TPL-E04-01`, `TPL-E04-03` | `E03-C4`, `E01-C4` | Pass | Each `PDF` keeps its `%PDF-1.6` header, page boxes, OutputIntent, and embedded Noto fonts. `pdf-preflight` reports zero findings. |
| `TPL-E01-03` | `E01-C4` | Pass | The Chromium export is `594.96 × 841.92 pt` (`209.89 × 297.01 mm`), within `±0.5 mm` of A4. The master declares `@page { size: A4 portrait; margin: 0; }` (`E01 §5.4.5`). The scan finds 0 contrast failures and 0 console errors. |
| `PUB-03 (v1.2.0)` | `D01-C3`, `E04-C2` | Pass | A script regenerates the front-matter typography from `AST-D01-01` and finds it identical to the file. It has 12 roles, sizes `12`–`64 px`, and line heights `1.2` and `1.5` only. The slide roles are `64`, `40`, and `24 px`. Table 3 lists no slide size below `24 px`. |
| `PUB-01 (v2.0.5)`, `PUB-02 (v2.0.4)`, `PUB-03 (v1.2.0)` | `A01-C10` | Pass | Each build manifest cites `A04 (v1.2.0)`, `B02 (v1.3.0)`, `E01 (v2.3.0)`, and `E04 (v2.2.0)`. `PUB-01` and `PUB-02` also cite `E03 (v1.1.0)`. Each cites `Library-Index.md (v1.2.20)`, a compile date of `2026-11-27`, and a precedence notice. |

> **Informative Note:** No slide deck exists to measure against `E04-C2`. `TPL-E04-02` remains `Planned`, so `5.2.6` applies when it is built.

## 5. Non-Conformity Register (`A04 (v1.2.0) §5.2.2`)

None. Zero non-conformities were found.

## 6. Closure Verification (`A04 (v1.2.0) §5.2.3`, `§5.1.7`)

* **Gate Verdict:** `Pass`. The items in Section 1 are released as listed.
* **Automated Check:** `python3 tools/library_checks.py` gives `PASS` with zero failing findings and zero known issues. The commit and continuous integration (`CI`) run are recorded in the pull request for this release.
* **Approver Sign-Off:** The Approver approved the released values on `2026-11-27`. Merging the release pull request records sign-off and puts the release into effect.
* **Approver:** Hary Irfantri
