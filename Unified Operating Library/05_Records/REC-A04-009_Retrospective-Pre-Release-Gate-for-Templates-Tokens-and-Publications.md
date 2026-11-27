# REC-A04-009 — Retrospective Pre-Release Gate for Templates, Tokens & Publications

| Field | Value |
| :--- | :--- |
| **Code** | `REC-A04-009` |
| **Record Type** | Pre-Release Gate (Retrospective) |
| **Date** | `2026-11-27` |
| **Status** | `Open` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Related Standards** | `A01 (v1.2.0)`, `A02 (v1.3.0)`, `A03 (v1.1.1)`, `A04 (v1.1.1)`, `B01 (v2.0.1)`, `B02 (v1.2.0)`, `B03 (v2.0.0)`, `C01 (v1.1.1)`, `D01 (v1.0.3)`, `D04 (v1.2.1)`, `E01 (v2.2.0)`, `E02 (v1.1.0)`, `E03 (v1.0.0)`, `E04 (v2.1.1)`, `Library-Index.md (v1.2.17)` |
| **Expiry Date** | `None` |

## 1. Review Scope & Trigger

This Governance Record (`REC-`) documents a retrospective Pre-Release Gate (`A04 (v1.1.1) §5.1.2`). It covers items promoted to `Approved` or re-released since `2026-11-26` without a gate record in `05_Records/`:

| Item | Register Event | Version Gated |
| :--- | :--- | :--- |
| `TPL-E01-01`, `TPL-E01-04` | Promoted `Library-Index.md (v1.2.2)`; revised `v1.2.6` | Active file on `main` at `0c7d861` |
| `TPL-E04-01`, `TPL-E04-03` | Promoted `Library-Index.md (v1.2.7)` | Active file on `main` at `0c7d861` |
| `TPL-E01-03` | `PDF` to `HTML` change `v1.2.12`; input border sync `v1.2.15` | Active `HTML` authoring master |
| `AST-D01-01` | Re-synced `v1.2.14` and `v1.2.15` | `generatedDate` `2026-11-27` |
| `PUB-01` | Refreshed `v1.2.13`–`v1.2.15` | `v2.0.3` |
| `PUB-02` | Refreshed `v1.2.13`, `v1.2.15` | `v2.0.2` |
| `PUB-03` | Registered `v1.2.10`; refreshed `v1.2.11`, `v1.2.13`, `v1.2.15` | `v1.1.2` |

The trigger is finding 5 of the library evaluation of `2026-11-27`. The register says these items followed Pre-Release Gate verification, but no record held the evidence.

Superseded intermediate versions (for example `PUB-03 v1.0.0`) are no longer active and are not re-gated. Their archived snapshots remain provenance only (`A01 (v1.2.0) §5.7.2`). `AST-B01-05`–`AST-B01-16` are covered by `REC-A04-008` and are out of scope.

## 2. Method

Every result below is measured on the delivered file, not inferred from another document. Measurements were taken on `2026-11-27` against `main` at commit `0c7d861`.

* **`PDF` structure:** `pypdf 6.17.0` and Poppler (`pdfinfo`, `pdffonts`, `pdftotext`). Checks cover page boxes, OutputIntent, embedded fonts, content-stream color operators, and Total Area Coverage (`TAC`).
* **`PDF` geometry:** Poppler render at `300 DPI`, with ink bounding boxes measured in millimeters from the TrimBox.
* **`HTML` behavior:** headless Chromium (Playwright). Checks cover font loading, computed-style contrast for every visible text node, control border colors, a `320 px` overflow test, status and waiver switching, and `@media print` export to `PDF`.
* **Tokens and color:** a script parsed `AST-D01-01`, the `B02` tables, the `PUB-01` embedded `JSON` and `CSS`, and the `PUB-03` front matter. Contrast uses the `WCAG` 2.2 relative-luminance formula.
* **Dependencies:** `SHA-256` of each font and `ICC` file against `Dependencies-Manifest.md (v2.0.0)`.

> **Informative Note:** The `PDF` checks are structural. They are not a certified `PDF/X-4` (`ISO 15930-7:2010`) validation. Pull request `#3` adds an automated checker (`tools/library_checks.py`). Its first `CI` run (`46052490505`, head `65cffeb`) independently reports the same `PDF` issues as `F-04` and `U-01`. Its register, palette, token-parity, contrast, link, and dependency checks all pass. The run on `main` should be cited here once pull request `#3` is merged.

## 3. Section 6 Verification — Executable Templates

### 3.1 `TPL-E01-01` (Print) and `TPL-E01-04` (Digital) — `E01 (v2.2.0)`, `E02 (v1.1.0)`, `E03 (v1.0.0)`

| Check ID | Status | Measured Evidence |
| :--- | :--- | :--- |
| `E01-C2` | Fail | The header is `16.00 mm` below trim. The `72 mm` lockup sits at `x 20.0 mm` and carries the outlined `A member of Irvantri Group` line. Footer text is `#5F6C7E` on white (`5.34:1`). Footer descenders reach `15.24 mm` above trim, inside the `16 mm` Safe Margin (`F-03`). `Page [X] of [Y]` is present. The `©` line is supplied by the paired cover (`E01 §5.2.2`). |
| `E01-C3` | Pass | Both are registered as `TPL-E01`, pinned to `E01 (v2.0)` in `Library-Index.md` and `E01` Section 7. The Print and Digital ink boxes match within `0.1 mm` (left `19.98 mm`, right `19.90 mm`, bottom `15.24 mm`). |
| `E01-C4` | Pass | `TPL-E01-04` is `595.28 × 841.89 pt` (A4) with equal Media, Bleed, and Trim boxes. It has an `sRGB IEC61966-2.1` OutputIntent and 9 `RGB` fills, all on the `B02` palette. Three Noto fonts are embedded, and the text is extractable. The marks are vector paths with zero raster images. |
| `E02-C1` | Pass | The footer shows `[v1.0.0]` in embedded `NotoSansMono-Medium`. |
| `E02-C2` | Pass | The `Approved` badge is `#166534` on `#F0FDF4` (`6.81:1`), with a text label and a square glyph. |
| `E03-C1` | Pass | `TPL-E01-01` has a TrimBox of `595.28 × 841.89 pt` (A4) and a BleedBox `3.00 mm` beyond trim. The accent bar runs from `3.0 mm` outside trim to `2.0 mm` inside it. Crop marks sit on the trim lines and end `3.1 mm` from trim. |
| `E03-C3` | Pass with upstream gap | All fills use `CMYK` operators, with zero `RGB` operators. Brand colors match `B02 §5.1.1` exactly (`98, 73, 7, 0`; `4, 100, 84, 0`; `100, 85, 35, 30`). Maximum `TAC` is `250%`. Neutral and Success colors use `CMYK` builds that `B02` does not define (`U-01`). |
| `E03-C4` | Pass, structural | The file declares `PDF/X-4` with a `FOGRA39` OutputIntent. The embedded profile is `121,368` bytes. All three fonts are embedded subsets. An undefined font resource is noted in `F-04`. |

### 3.2 `TPL-E04-01` (Print) and `TPL-E04-03` (Digital) — `E04 (v2.1.1)`, `E01 (v2.2.0)`, `E03 (v1.0.0)`, `A03 (v1.1.1)`

| Check ID | Status | Measured Evidence |
| :--- | :--- | :--- |
| `E04-C1` | Fail | Trim is A4. The lockup starts at `x 20.0 mm` and `y 16.0 mm`, so it sits inside the margins. Its frame is `72 mm` wide with a `17.4 mm` symbol, at least the `64 mm` minimum. Clear Space is `14 mm` above and `47 mm` to the right, against `4.3 mm` required. `Irvantri Standards Pte. Ltd.`, the Endorsement Line, and `[YYYY-MM-DD]` dates are present. Zero contractions were found. Footer descenders reach `15.32 mm` above trim (`F-03`). |
| `E04-C4` | Pass | Both are registered as `TPL-E04`, pinned to `E04 (v2.0)` in `Library-Index.md` and `E04` Section 7. |
| `A03-C6` | Pass | Extracted text includes `© [YYYY] Irvantri Standards Pte. Ltd. All rights reserved.` |
| `E01-C4` | Pass | `TPL-E04-03` matches `TPL-E01-04` in profile, with 6 `RGB` fills, all on the palette. Text is `#5F6C7E` (`5.34:1`) and `#092B55` (`14.11:1`) on white. Four Noto fonts are embedded. |
| `E03-C3` | Pass with upstream gap | `TPL-E04-01` uses `CMYK` only. Brand builds are exact, maximum `TAC` is `250%`, and neutral builds are as in `U-01`. |
| `E03-C1`, `E03-C4` | Pass, structural | Bleed, crop marks, `PDF/X-4`, and `FOGRA39` measure the same as `TPL-E01-01`. An undefined font resource is noted in `F-04`. |

### 3.3 `TPL-E01-03` (Digital `HTML` authoring master) — `E01 (v2.2.0)`, `E02 (v1.1.0)`, `B02 (v1.2.0)`, `D04 (v1.2.1)`

| Check ID | Status | Measured Evidence |
| :--- | :--- | :--- |
| `E01-C1` | Pass | The cover lockup is a base64 `SVG` whose `SHA-256` equals `AST-B01-03` (`6db18e62…`, `17,700` bytes). Status, `[v1.0.0]`, and `[YYYY-MM-DD]` fields are present. The document uses `lang="en"`, not `en-US` (`F-06`). |
| `E01-C3` | Pass | `@page { size: A4 portrait; margin: 0; }` is declared. `@media print` hides the authoring bar, editor, tabs, and dialogs, as the rendered export confirms. All 11 `@font-face` sources resolve to `../06_Dependencies/Fonts/`. The header symbol paths are identical to `AST-B01-01`. |
| `E01-C4` | Pass | The Chromium export is one page of `594.96 × 841.92 pt` with equal boxes. That is `209.89 × 297.01 mm`, from renderer rounding (`U-02`). Five Noto fonts are embedded as `CID` subsets, the text is extractable, and there are zero raster images. |
| `E02-C2`, `E02-C3`, `E02-C4` | Pass | Switching status shows the verbatim `E02 §5.3.2` notice in a banner with `4 mm` padding and an `8 px` radius. Badges have a `4 px` radius and semantic colors. Enabling a waiver shows `Waiver ID` and `Waiver Expiry` rows. |
| `B02-C2`, `B02-C5` | Fail | All 13 inputs and selects use `#64748B` (`4.55:1` on the `#F8FAFC` fill). The secondary buttons (`Save HTML`, `Export anyway`, `Cancel`) use `#CBD5E1` borders (`1.48:1` on white) (`F-01`). All 25 hex values are on the `B02` palette. |
| `D04-C1`, `D04-C3` | Pass | 48 visible text nodes were scanned, with zero contrast failures and a `12 px` minimum size. There is zero horizontal overflow at `320 px`. A skip link, 9 landmarks or roles, `prefers-reduced-motion`, and `:focus-visible` are present. |

## 4. Section 6 Verification — Master Asset `AST-D01-01` — `D01 (v1.0.3)`, `B02 (v1.2.0)`

| Check ID | Status | Measured Evidence |
| :--- | :--- | :--- |
| `D01-C1` | Pass | There are 171 token leaves in three tiers (`primitive`, `semantic`, `component`). All 92 generated `CSS` properties match `--is-[a-z0-9-]+`. |
| `D01-C2` | Fail | All 29 hex values are uppercase, and the 25 unique values equal the `B02` palette exactly. Every `rgb` extension matches its hex, and the four `CMYK` builds match `B02 §5.1.1`. `component.input.border` resolves to `#64748B`. `component.button.secondary-border` resolves to `#CBD5E1` (`1.48:1`), which conflicts with `B02 §5.2.2` (`F-01`). |
| `D01-C3` | Pass | The file is registered as `AST-D01-01`, pinned to `D01 (v1.0)`. `PUB-01`'s embedded `JSON` parses equal to the master file. Its 92 page-level `--is-` properties equal the generated `CSS` exactly. |
| `B02-C1` | Pass | The values match the token audit above. |

## 5. Section 6 Verification — Compiled Publications — `A01 (v1.2.0)`, `A03 (v1.1.1)`, `B02 (v1.2.0)`, `D01 (v1.0.3)`, `D04 (v1.2.1)`

| Item | Check ID | Status | Measured Evidence |
| :--- | :--- | :--- | :--- |
| `PUB-01 (v2.0.3)` | `A01-C10` | Fail | It shows a visible build manifest, a compile date of `2026-11-27` in all five places, and a precedence notice. Table 6 states `TPL-E01-01`–`TPL-E01-04` are pinned to `E01 (v2.2)`, but only `TPL-E01-03` is (`F-05`). |
| `PUB-01 (v2.0.3)` | `D04-C1`, `D04-C3` | Pass | 465 visible text nodes were scanned, with zero contrast failures and a `12 px` minimum. It uses `lang="en-US"`, with zero overflow at `320 px`, 7 landmarks, a skip link, reduced motion, and `:focus-visible`. |
| `PUB-01 (v2.0.3)` | `B02-C2`, `B02-C5` | Fail | 12 buttons use `#CBD5E1` borders (`1.48:1`): 11 `is-btn--secondary` buttons, such as `Download JSON` and `Save draft`, and the `Publish release` demo button. Inputs use `#64748B` (`F-01`). |
| `PUB-01 (v2.0.3)` | `A03-C6` | Pass | The `©` and Endorsement Line strings are present. |
| `PUB-02 (v2.0.2)` | `A01-C10` | Fail | The manifest, compile date `2026-11-27`, and precedence notice are present. The `TPL-E01` pin statement is the same as in `PUB-01` (`F-05`). |
| `PUB-02 (v2.0.2)` | `A03-C6`, `C01` | Pass | The `©` and Endorsement Line strings are present, with zero contractions. |
| `PUB-03 (v1.1.2)` | `A01-C10` | Fail | The manifest (Table 4), compile date `2026-11-27`, and precedence notice are present. The `TPL-E01` pin statement is the same as in `PUB-01` (`F-05`). |
| `PUB-03 (v1.1.2)` | `B02-C1`, `B02-C2` | Pass | All 31 front-matter colors are on the `B02` palette, including `border-strong` `#64748B`. |
| `PUB-03 (v1.1.2)` | `D01-C3` | Fail | The front-matter typography is not derived from `AST-D01-01` (`F-02`). |

## 6. Library Control Checks

| Control Area | Governing Clause | Status | Evidence & Notes |
| :--- | :--- | :--- | :--- |
| **Dependencies** | `A02 (v1.3.0) §5.5.4`, `B03 (v2.0.0) §5.1.3` | Pass | 16 of 16 font and `ICC` files match their manifest `SHA-256`. All three `OFL.txt` files contain the full `SIL OFL-1.1` text (`4,352` bytes each). |
| **Font Embedding** | `B03 (v2.0.0) §5.1.1`, `E01 (v2.2.0) §5.4.3` | Pass | Every embedded font in the six `PDF` files is a Noto family. |
| **Register Sync** | `A01 (v1.2.0) §5.8.1`, `A04 (v1.1.1) §5.5.2` | Pass | `REC-A04-009` is registered as `Open` in `Library-Index.md (v1.2.17)` on `2026-11-27`. |
| **Naming** | `A02 (v1.3.0) §5.4.1` | Pass | This file follows `REC-[StandardCode]-[001–999]_Title-Words.md`. |

## 7. Non-Conformity Register (`A04 (v1.1.1) §5.2.2`)

Due dates are calculated from `2026-11-27` per `A04 (v1.1.1) §5.2.1`. `Major` findings close within 15 business days (`2026-12-18`). `Minor` findings close within 30 calendar days (`2026-12-27`).

| Finding ID | Affected Item | Violated Clause / Check ID | Severity | Assigned Owner | Due Date | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `F-01` | `AST-D01-01`, `PUB-01`, `TPL-E01-03` | `B02 (v1.2.0) §5.2.2`, `§5.5.1` (`B02-C2`, `B02-C5`); `D01 (v1.0.3) §5.2.1` (`D01-C2`) | `Major` | Hary Irfantri | `2026-12-18` | `Open` |
| `F-02` | `PUB-03` | `D01 (v1.0.3) §5.3.1` (`D01-C3`) | `Major` | Hary Irfantri | `2026-12-18` | `Open` |
| `F-03` | `TPL-E01-01`, `TPL-E01-04`, `TPL-E04-01`, `TPL-E04-03` | `E03 (v1.0.0) §5.1.2` (`E03-C1`); `E01 (v2.2.0) §5.2.1` (`E01-C2`); `E04 (v2.1.1) §5.1.1` (`E04-C1`) | `Major` | Hary Irfantri | `2026-12-18` | `Open` |
| `F-04` | `TPL-E01-01`, `TPL-E01-02`, `TPL-E01-04`, `TPL-E04-01`, `TPL-E04-03` | `E03 (v1.0.0) §5.4.1` (`E03-C4`) | `Minor` | Hary Irfantri | `2026-12-27` | `Open` |
| `F-05` | `PUB-01`, `PUB-02`, `PUB-03` | `A01 (v1.2.0) §5.7.5` (`A01-C10`) | `Minor` | Hary Irfantri | `2026-12-27` | `Open` |
| `F-06` | `TPL-E01-03` | `C01 (v1.1.1) §5.6.1`; `E01 (v2.2.0) §5.1.2` (`E01-C1`) | `Minor` | Hary Irfantri | `2026-12-27` | `Open` |

## 8. Detailed Finding Descriptions

* **`F-01` (`Major` — Secondary button borders below `3.0:1`):** `B02 (v1.2.0) §5.2.1` assigns **Border Strong** to "boundaries that identify an interactive control", and `§5.2.2` requires it for control boundaries. `AST-D01-01` `component.button.secondary-border` resolves to **Border Default** (`#CBD5E1`). This measures `1.48:1` on white. The token flows into 12 buttons in `PUB-01` and three `.btn-line` buttons in `TPL-E01-03`. The `B02 v1.2.0` sync (`Library-Index.md (v1.2.15)`) moved only input borders. **Remediation:** point `component.button.secondary-border` to `semantic.color.border-strong` (`#64748B`, `4.76:1`), then regenerate `PUB-01` and update `TPL-E01-03`.
* **`F-02` (`Major` — `PUB-03` token values not derived from `AST-D01-01`):** `PUB-03` front matter is a published token package for design and Artificial Intelligence (`AI`) tools. Two font sizes have no `AST-D01-01` font-size token: `headline-display` `48px` and `body-slide` `22px`. Four line heights are not tokens: `1.15`, `1.25`, `1.4`, and `1.45` (the tokens are `1.2` and `1.5`). `48px` and `22px` appear in no normative standard. **Remediation:** generate `PUB-03` front matter from `AST-D01-01`. Either add the missing type steps to `AST-D01-01` through an `E04` slide type-scale clause, or remove them from `PUB-03`.
* **`F-03` (`Major` — Footer text inside the `16 mm` Safe Margin):** `E03 (v1.0.0) §4` defines the Safe Margin as the distance within which "all essential text, marks, and legal attribution" stay protected. Footer baselines sit on the `16 mm` line, so descenders reach `15.24 mm` (`TPL-E01-01`, `TPL-E01-04`) and `15.32 mm` (`TPL-E04-01`, `TPL-E04-03`) from trim. In the letterhead, this line is the `A03 §5.6.1` copyright notice. **Remediation:** raise the footer block so its lowest ink clears `16 mm`. Alternatively, the Approver may rule that Safe Margins are measured to the text baseline (`U-03`).
* **`F-04` (`Minor` — Undefined font resource `/F1`):** each template `PDF` opens a text object with `/F1 12 Tf`, but `/F1` is absent from the page `/Font` resources. That text object draws zero glyphs, so nothing is visibly affected. Poppler reports `Syntax Error: Unknown font tag 'F1'`. A certified `PDF/X-4` preflight may reject this. If it does, the Approver should reclassify the finding as `Major`. **Remediation:** remove the empty text object or the `/F1` selection when the templates are next rebuilt.
* **`F-05` (`Minor` — Incorrect template pin in build manifests):** `PUB-01` Table 6, `PUB-02` Table 6, and `PUB-03` Table 4 list `TPL-E01-01`–`TPL-E01-04` as pinned to `E01 (v2.2)`. `Library-Index.md` Section 5 and `E01` Section 7 pin `TPL-E01-01`, `TPL-E01-02`, and `TPL-E01-04` to `E01 (v2.0)`. Only `TPL-E01-03` is pinned to `E01 (v2.2)`. **Remediation:** correct the three manifests in the next `ERRATA` refresh.
* **`F-06` (`Minor` — Document language tag):** `TPL-E01-03` declares `<html lang="en">`, while `C01 §5.6.1` sets `en-US` and `PUB-01` declares `lang="en-US"`. The visible copy is United States English. **Remediation:** set `lang="en-US"`.

## 9. Upstream Observations for Approver Decision (`A04 (v1.1.1) §5.3`)

These items are not non-conformities. They are clauses whose current wording leaves a measured gap. Each needs an Approver decision on whether to revise the upstream standard under `A01 (v1.2.0) §5.5`.

* **`U-01` — No `CMYK` builds for neutral and semantic colors:** `E03 (v1.0.0) §5.3.1` requires the `B02 §5.1.1` `ISO` Coated v2 builds. `B02 (v1.2.0)` defines builds only for the four brand colors. The print templates use undefined builds for **Text Muted** (`25, 14, 0, 51`), **Border Default** (`19, 12, 6, 0`), and the **Success** set (`86, 25, 88, 27`; `6, 0, 4, 0`; `26, 0, 24, 0`). The proposed fix is to add `CMYK` builds to the `B02 §5.2.1` and `§5.3.1` tables, ideally checked by a press proof.
* **`U-02` — "Exact A4" has no tolerance for browser export:** Chromium rounds `@page { size: A4 }` to `594.96 × 841.92 pt` (`−0.11 mm` width). The template declares exact A4, but `E01 (v2.2.0) §5.4.1` states no tolerance. The proposed fix is to add a `±0.5 mm` export tolerance to `E01 §5.4.1`.
* **`U-03` — Safe Margin measurement point:** the `E03 (v1.0.0) §4` definition does not say whether to measure to the text baseline or to the lowest ink. The Approver may confirm lowest ink (keeping `F-03`) or revise the definition.

## 10. Closure Verification (`A04 (v1.1.1) §5.2.3`)

* **Gate Verdict:** `Hold` for `F-01`–`F-03` until they close or receive a waiver. The items remain `Approved` in the register, because this gate is retrospective. Release blocking under `A04 (v1.1.1) §5.2.4` applies only if a finding passes its due date while still open.
* **Approver Sign-Off Date:** Pending.
* **Approver:** Hary Irfantri
* **Objective Closure Evidence:** Pending. This record stays `Open` until each finding is closed with evidence or waived. It becomes immutable when it reaches `Closed` (`A04 (v1.1.1) §5.5.3`).
