# E01 — Formal Document Layout

| Field | Value |
| :--- | :--- |
| **Code** | `E01` |
| **Version** | `v2.6.1` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-28` |
| **Next Review** | `2027-05-26` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `TPL-E01-03`, `TPL-E01-06` |

## 1. Purpose

This standard defines the cover geometry, metadata panel structure, running header and footer layout, pagination rules, corporate attribution requirements, `HTML` authoring master profile, the link to document body elements (through `E05`), and digital distribution `PDF` profile for formal documents across **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`). It ensures formal documents present a consistent, legible, and authoritative visual structure across print, interactive `HTML` authoring, cloud-native authoring, and digital distribution.

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* Formal documents, governance reports, proposals, specifications, and compiled publications (`PUB-`) produced by **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`).
* Formal document cover pages, metadata panels, running headers, running footers, pagination formatting, and digital `PDF` distribution profiles.
* Executable layout templates (`TPL-E01`)—including full formal document masters with a cover, running header and footer, and body, press-ready print masters, interactive `HTML`/`CSS` authoring masters, digital `PDF` reference masters, and Cloud-Native Office File authoring templates—registered in `Library-Index.md` and Section 7 of this standard.

### 2.2 Out of Scope
This standard does not govern:
* Normative standard anatomy and lifecycle rules for Markdown source standards (governed by `A01`).
* Draft watermarks, revision banner styling, or release status indicator rules (governed by `E02`).
* Paper stock selection, press bleed/trim allowances, or commercial vendor proofing (governed by `E03`).
* Letters, memoranda, slide decks, operational workbooks, or email signatures (governed by `E04`).

## 3. Normative References

The following documents are referenced in this standard. For undated references, the latest approved edition applies.
* `Library-Index.md` — Standards Design Library Index (`v2.0.0` or later).
* `A01` — Document Control & Lifecycle.
* `A02` — Taxonomy, Coding & File Naming.
* `A03` — Entity & Brand Architecture.
* `A04` — Compliance, Reviews & Exceptions.
* `B01` — Marks & Lockups.
* `B02` — Color System.
* `B03` — Typography.
* `B04` — Grids, Spacing & Graphic Devices.
* `C01` — Voice, Tone & Plain Language.
* `C02` — Terminology & Controlled Vocabulary.
* `C03` — Technical & User Experience (`UX`) Writing.
* `C04` — Data, Dates & Citation Formatting.
* `D01` — Design Tokens & Architecture.
* `D03` — Interface Components & Patterns.
* `D04` — Accessibility & Usability.
* `E03` — Print & Production Specifications.
* `E05` — Document Body Elements.

## 4. Terms & Definitions

For terms shared across the library, refer to `C02`, `A01`, `A02`, `B01`, `B03`, `B04`, `D03`, and `D04`. For the purposes of this standard, the following definitions apply:
* **Cover Page:** The front title sheet of a formal document presenting brand identification, document title, metadata summary, and signature visual geometry.
* **Digital Distribution PDF:** An electronic `PDF` deliverable formatted at exact A4 trim dimensions in Standard Red-Green-Blue (`sRGB`) color without print bleed or crop marks for screen viewing and electronic distribution.
* **Filled Copy:** A single `HTML` file, saved from an `HTML` Authoring Master, that holds the master and every value a user entered.
* **HTML Authoring Master:** A standalone `HTML`/`CSS` template file that users fill in a browser and that exports the template's `PDF` editions (`5.3.3`, `5.3.4`).
* **Metadata Panel:** A structured summary block displaying controlled document attributes—such as identifier, version, status, owner, approver, and dates—on a formal document.
* **Press Preview:** An on-screen view of a press export showing the A4 trim, the `3 mm` Bleed, and the crop marks.
* **Running Footer:** The recurring bottom margin region displaying document title, version, attribution, and page numbering across pages.
* **Running Header:** The recurring top margin region displaying brand lockup and document or status context across pages.

## 5. Requirements

### 5.1 Cover Geometry & Metadata Panels
**5.1.1** Formal document covers SHALL place the Parent-Endorsed Lockup (`B01 §5.2.1`) in the upper region with at least `0.25×` Primary Symbol width Clear Space (`B01 §5.3.1`). Covers MAY include the `24%` **Signal Red** (`#DE0029`) and `76%` **Deep Navy** (`#092B55`) split accent bar in horizontal or `4 mm` vertical left-spine orientation (`B04 §5.3.1`).

**5.1.2** Cover titles and section headings SHALL use the Display Typeface (`B03 §5.1.1`) in United States English (`en-US`) (`C01 §5.6.1`), and SHALL NOT display internal project codenames (`A03 §5.4.2`, `C02 §5.3.3`).

**5.1.3** Cover and document metadata panels SHALL record `Version` in `vMAJOR.MINOR.ERRATA` format (`A01 §5.5.1`) and `Status` using exact `C02 §5.4.1` controlled status strings without informal synonyms (`C02 §5.4.2`). Metadata dates SHALL use International Organization for Standardization (`ISO`) 8601 format (`YYYY-MM-DD`) (`A01 §5.2.7`, `C04 §5.1.1`).

### 5.2 Running Headers, Footers & Pagination
**5.2.1** Running headers and footers SHALL align to the `4 mm` print Base Unit grid (`B04 §5.1.2`, `C04 §5.3.2`) and maintain `B02 §5.5.1` contrast and `B03 §5.2.2` legibility rules.

**5.2.2** Formal documents SHALL display the verbatim Endorsement Line `A member of Irvantri Group` (`A03 §5.2.1`, `§5.3.3`). Documents SHALL also display `© [YYYY] Irvantri Standards Pte. Ltd. All rights reserved.` (`A03 §5.6.1`) on the cover, colophon, or running header or footer.

**5.2.3** Running footers or page margins SHALL display sequential page numbering (`Page X of Y` or `X / Y`) (`C04 §5.2.1`, `§5.4.3`). Required header and footer metadata fields SHALL NOT be left blank (`C04 §5.4.1`).

### 5.3 Executable Layout Templates (`TPL-E01`)
**5.3.1** Formal document layout templates SHALL be registered as `TPL-E01` Executable Templates in `Library-Index.md` and Section 7, pinned to `E01 (vMAJOR.MINOR)` (`A01 §5.7.4`, `A02 §5.7.2`).

**5.3.2** Page-based `TPL-E01` templates deployed across print and electronic channels SHALL maintain paired Print (`E03`) and Digital (`5.4`) editions derived from identical layout geometry.

**5.3.3** Digital `TPL-E01` templates MAY be maintained as standalone interactive `HTML` authoring masters whose exported `PDF` output conforms to Section `5.4`. Non-printing authoring controls SHALL be suppressed in `@media print` output. Each `HTML` template SHALL reference licensed `06_Dependencies/Fonts/` packages (`A02 §5.5.4`, `B03 §5.1.3`) and embed `AST-B01` vector marks (`B01 §5.1.2`).

**5.3.4** An `HTML` authoring master (`5.3.3`) MAY serve as both the Print and Digital edition required by Clause `5.3.2` when it provides a press export from the same layout geometry. The press export SHALL add a `3 mm` Bleed and `3 mm`-offset crop marks (`E03 §5.1.4`). The press export SHALL replace each `sRGB` fill with its fixed `B02 §5.1.1` or `§5.6.1` `CMYK` build without automated conversion (`E03 §5.3.1`). The press export SHALL deliver `PDF/X-4` with embedded `B03` fonts (`E03 §5.4.1`). A color without a fixed `B02` `CMYK` build SHALL stop the press export.

> **Informative Note:** `TPL-E01-03` provides the press export in two steps. Its "Export press PDF" control saves a `230 mm × 317 mm` sheet in `sRGB`. Running `tools/press_export.py` on that sheet writes the `PDF/X-4` file and runs the library-checks preflight.

### 5.4 Digital Distribution PDF Profile
**5.4.1** Formal documents and compiled publications (`PUB-`) distributed digitally as `PDF` files SHALL use exact A4 (`210 mm × 297 mm`) trim dimensions (`C04 §5.3.2`). Digital `PDF` files SHALL omit print bleed extensions, slug areas, and crop marks.

**5.4.2** Digital distribution `PDF` files SHALL use `sRGB` color matching exact `B02 §5.1.1`–`§5.3.1` Hexadecimal (`HEX`) and Red-Green-Blue (`RGB`) values (`B02 §5.5.1`).

**5.4.3** Digital distribution `PDF` files SHALL embed all licensed `B03` fonts (`B03 §5.1.3`) and preserve selectable live text. Digital distribution `PDF` files SHALL retain vector brand marks sourced from `AST-B01` masters (`B01 §5.1.2`), except as permitted in Clause `5.4.4`.

**5.4.4** Digital distribution `PDF` files exported from Cloud-Native Office Files (`A02 §5.4.6`) MAY embed lossless Portable Network Graphics (`PNG`) brand marks (`B01 §5.1.2`). Each `PNG` derivative SHALL be exported directly from an `AST-B01` Scalable Vector Graphics (`SVG`) master at `300` dots per inch (`DPI`) minimum. Commercial print files (`E03`) and programmatically compiled publications SHALL retain vector marks.

**5.4.5** A digital distribution `PDF` exported from an `HTML` authoring master (`5.3.3`) meets the A4 trim in Clause `5.4.1` when each page dimension is within `±0.5 mm` of A4. The master SHALL declare an A4 `@page` size (for example, `@page { size: A4 }`). The tolerance covers browser rounding during export.

### 5.5 HTML Authoring Master Profile
**5.5.1** A page-based `TPL-E01` template created or revised on or after `2026-11-28` SHALL be an `HTML` Authoring Master (`5.3.3`). Where the template serves print, the master SHALL provide a press export (`5.3.4`) and serve as both editions (`5.3.2`). Static `PDF` templates `Approved` before that date MAY remain in use until their next revision.

**5.5.2** A Cloud-Native Office File (`A02 §5.4.6`) or native office file MAY be registered alongside an `HTML` Authoring Master under its own `TPL-` code where its users author in that tool. It SHALL apply the master's `B02` and `B03` values and place the lockup, title, and metadata panel within `±0.5 mm` of the master's positions. Its digital `PDF` exports SHALL conform to Section `5.4`.

**5.5.3** The master SHALL declare color, type, and spacing values as `CSS` custom properties whose values equal the `AST-D01-01` tokens (`D01`). Style rules SHALL use those custom properties and SHALL NOT contain literal `HEX` or `RGB` color values.

**5.5.4** Each editable field SHALL pair a visible text label with its input (`D03 §5.2.1`). Each field SHALL show placeholder text stating the expected content. Each free-text field SHALL declare a maximum character count and SHALL stop input beyond that count.

**5.5.5** The master SHALL measure each field against its layout box after each edit. Where content overflows its box or the A4 trim, the master SHALL name the field and the fix in an error message on field blur (`D03 §5.2.2`, `§5.2.4`). The master SHALL NOT produce either export while any overflow remains.

**5.5.6** The master SHALL provide a `Save filled copy` control that downloads a Filled Copy. Opening the Filled Copy SHALL restore every entered value. The master SHALL warn the user before a reload or close discards unsaved changes. The master SHOULD also autosave entered values in browser storage and offer to restore them when reopened.

> **Informative Note:** Browser storage stays on the device and browser that saved it. The Filled Copy is the file people share or keep; autosave only protects work in progress.

**5.5.7** Where the master provides a press export, it SHALL provide a Press Preview control adjacent to the press export control. The Press Preview SHALL render on screen the trim, `3 mm` Bleed, and crop marks of the press export from the same layout geometry.

**5.5.8** The master SHALL be a single file that operates with no network connection. It SHALL NOT request scripts, style sheets, fonts, or images from a remote host. It SHALL embed each `B03` font it uses as a data Uniform Resource Identifier (`URI`) byte-identical to its `06_Dependencies/Fonts/` file, which satisfies the reference in Clause `5.3.3`. It SHALL embed `AST-B01` marks as inline vector paths (`B01 §5.1.2`).

**5.5.9** The authoring interface SHALL conform to `D04 §5.1`–`§5.3`. Every field and control SHALL be operable by keyboard alone in visual order and SHALL expose an accessible name. Validation, overflow, and save messages SHALL be announced through an Accessible Rich Internet Applications (`ARIA`) Live Region (`D04 §5.3.2`).

**5.5.10** The Pre-Release Gate record (`A04 §5.1.5`) for an `HTML` Authoring Master SHALL cite measured evidence (`A04 §5.1.6`) from exports made at the release commit. The evidence SHALL include a digital `PDF` preflight against Section `5.4`. Where Clause `5.3.4` applies, it SHALL include a press `PDF` with its `PDF/X-4` preflight output, TrimBox and BleedBox sizes, and `CMYK` ink table. It SHALL also include results for Clauses `5.5.3`–`5.5.9`.

> **Informative Note:** The `html-master` check in `tools/library_checks.py` measures Clauses `5.5.3`, `5.5.4`, and `5.5.6`–`5.5.9` statically for every `HTML` template pinned to `E01 (v2.5)` or later. Overflow blocking (`5.5.5`), restoring a Filled Copy (`5.5.6`), and keyboard operation (`5.5.9`) need a browser run recorded in the gate record.

**5.5.11** A page-based `TPL-E01` master that accepts free body content SHALL render that content to `E05`. It SHALL apply the running header and footer (`5.2`) to every page after the cover except the back page. This includes pages that hold a rotated landscape table (`E05 §5.4.8`) and intentionally blank pages (`E05 §5.8.7`).

## 6. Conformance & Verification

A formal document or layout template conforms to `E01` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `E01-C1` | Cover applies `B01` lockup and Clear Space rules, optional horizontal or `4 mm` vertical spine `24%` / `76%` accent bar (`5.1.1`), the `B03` Display Typeface and `en-US` text without codenames (`5.1.2`), and `vMAJOR.MINOR.ERRATA`, `C02` status, and `YYYY-MM-DD` metadata (`5.1.3`). | Cover & metadata audit |
| `E01-C2` | Running headers and footers align to `4 mm` increments and meet contrast and size rules (`5.2.1`), preserve `A member of Irvantri Group` and `© [YYYY] Irvantri Standards Pte. Ltd. All rights reserved.` (`5.2.2`), and include page numbers without blank fields (`5.2.3`). | Header, footer & pagination check |
| `E01-C3` | Formal layout templates are registered as `TPL-E01` in `Library-Index.md` and Section 7 pinned to `E01 (vMAJOR.MINOR)` (`5.3.1`), maintain paired Print and Digital editions (`5.3.2`), and any `HTML` authoring template suppresses controls in `@media print` while referencing `06_Dependencies/Fonts/` and vector `AST-B01` marks (`5.3.3`). Any `HTML` master serving as the Print edition provides a press export with `3 mm` Bleed, crop marks, fixed `B02` `CMYK` builds, and `PDF/X-4` output that stops on unmapped colors (`5.3.4`). | Template & register audit |
| `E01-C4` | Digital distribution `PDF` files use exact A4 trim without bleed or crop marks (`5.4.1`), or A4 within `±0.5 mm` for `HTML` authoring master exports declaring an A4 `@page` size (`5.4.5`), apply exact `B02` `sRGB` palette values (`5.4.2`), and embed licensed `B03` fonts, selectable text, and vector `AST-B01` marks or `≥ 300 DPI` lossless `PNG` derivatives for Cloud-Native Office File exports (`5.4.3`, `5.4.4`). | Digital `PDF` preflight audit |
| `E01-C5` | New or revised page templates are `HTML` Authoring Masters with a press export where they serve print (`5.5.1`); any native companion file matches `B02`/`B03` values and `±0.5 mm` positions (`5.5.2`); colors and type come from `AST-D01-01` custom properties with no literal colors (`5.5.3`); fields have visible labels, placeholders, and enforced character limits (`5.5.4`); overflow is named and blocks export (`5.5.5`); a Filled Copy restores every value and unsaved changes trigger a warning (`5.5.6`); a Press Preview sits beside the press export (`5.5.7`); the file makes zero remote requests and embeds byte-identical fonts and inline marks (`5.5.8`); the interface passes `D04` keyboard, accessible name, and Live Region checks (`5.5.9`); and the gate record holds the measured export evidence (`5.5.10`); and any master that accepts free body content renders it to `E05` with the running header and footer on every page after the cover except the back page (`5.5.11`). | Template, network, checksum & accessibility audit |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with `A04`.

## 7. Linked Artifacts

| Code | Artifact | File | Pinned Version | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `TPL-E01-01` | Header & Footer Layout Template (Print) | `99_Archive/TPL-E01-01_Header-and-Footer-Print_v2.0.0.pdf` | `E01 (v2.0)` | `Deprecated` | Static press-ready A4 running header and footer `PDF`. Superseded by `TPL-E01-06`, whose running header and footer, `Page X of Y` footer, and press export (`5.3.4`) replace it; moved unmodified to `99_Archive/` per `REC-A04-015` (`A01 §5.7.3`); code locked against reuse (`A02 §5.3.2`) |
| `TPL-E01-02` | Formal Document Cover Template (Print) | `99_Archive/TPL-E01-02_Formal-Cover-Print_v2.0.0.pdf` | `E01 (v2.0)` | `Deprecated` | Static press-ready A4 cover `PDF` (`E03` `PDF/X-4`, `FOGRA39`, `3 mm` bleed, `80 mm` `AST-B01-03` lockup, `4 mm` vertical left-spine bar). Failed `E01-C3` (`5.3.2`) against `TPL-E01-03` geometry and offered no fillable fields. Superseded by the `TPL-E01-03` press export (`5.3.4`) and moved to `99_Archive/` on `2026-11-27` per `REC-A04-013` (`A01 §5.7.3`). Code locked against reuse (`A02`). |
| `TPL-E01-03` | Formal Document Cover Template | `03_Templates/TPL-E01-03_Formal-Cover-Digital.html` | `E01 (v2.4)` | `Approved` | Editable interactive `HTML`/`CSS` A4 cover authoring master (`5.3.3`, `5.4` `sRGB` `PDF` export, zero bleed/crop marks, `24 mm` inner / `20 mm` outer margins, `16 mm` T/B Safe Margins, `4 mm` `76%` / `24%` vertical left-spine bar, `80 mm` curve-outlined `AST-B01-03` lockup, local `06_Dependencies/Fonts/` `B03 (v2.0.0)` Noto fonts, non-printing browser authoring bar with `contenteditable` fields, `C02` status switcher, `E02` banners/waiver controls, live preflight, and `@media print` A4 `PDF` export; upgraded from static `PDF` and Approved `2026-11-27`; header comment re-aligned to `E01 v2.3.0`, `B02 v1.3.0`, and `A04 v1.2.0` on `2026-11-27`; press layout export (`230 mm × 317 mm` sheet, `3 mm` Bleed, `100%` K crop marks offset `3 mm`) converted to `PDF/X-4` by `tools/press_export.py`, serving as both Print and Digital edition (`5.3.4`), re-pinned to `E01 (v2.4)` on `2026-11-27` per `REC-A04-013`) |
| `TPL-E01-04` | Header & Footer Layout Template (Digital) | `99_Archive/TPL-E01-04_Header-and-Footer-Digital_v2.0.0.pdf` | `E01 (v2.0)` | `Deprecated` | Static digital A4 running header and footer `PDF`. Superseded by `TPL-E01-06`, which renders the same header and footer on every body page of the digital export; moved unmodified to `99_Archive/` per `REC-A04-015` (`A01 §5.7.3`); code locked against reuse (`A02 §5.3.2`) |
| `TPL-E01-06` | Formal Document Master | `03_Templates/TPL-E01-06_Formal-Document-Master.html` | `E01 (v2.6)` | `Approved` | Single-file `HTML` Authoring Master (`5.5`) for full formal documents: `TPL-E01-03` cover geometry with `E02` badge, banner, waiver and Superseded By fields; running header with the `72 mm` `AST-B01-03` lockup, status badge and optional section name; footer with title, version and `Page X of Y`; generated contents, lists of tables and figures, distribution list, Revision History and back page; Markdown body with Word and Google Docs paste conversion rendered to `E05 (v1.0)`; two-sided print, review watermark, Filled Copy with autosave, digital A4 export finished by `tools/pdf_finish.py`, and press export with Press Preview (`5.3.4`) for `tools/press_export.py`; embeds `06_Dependencies/Fonts/` and `06_Dependencies/Scripts/` byte-identical; built from `tools/document-master/` by `tools/build_document_master.py` |

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v2.6.1` | `2026-11-28` | Errata | Renamed library references to `Standards Design` and raised the `Library-Index.md` reference floor to `v2.0.0` per `A01 §5.5.5`, `§5.5.7`, and `REC-A04-016`. | Hary Irfantri |
| `v2.6.0` | `2026-11-28` | Minor | Added `5.5.11` requiring page-based `TPL-E01` masters that accept free body content to render it to `E05` with the running header and footer on every page after the cover; extended Check `E01-C5`; added `E05` and raised the `Library-Index.md` reference floor (`v1.2.25`) in Section 3; registered `TPL-E01-06` Formal Document Master (`Approved`, `E01 (v2.6)`) and moved `TPL-E01-01` and `TPL-E01-04` to `Deprecated` (superseded by `TPL-E01-06`, archived unmodified to `99_Archive/`) in Section 7; updated Governs, per `REC-A04-015`. No existing `SHALL` changed. | Hary Irfantri |
| `v2.5.0` | `2026-11-28` | Minor | Added Section `5.5` (`5.5.1`–`5.5.10`), the `HTML` Authoring Master Profile, making an `HTML` master with press export the default for page-based `TPL-E01` templates created or revised from `2026-11-28`, with field label and limit, overflow, Filled Copy, Press Preview, offline single-file, accessibility, and gate-evidence requirements; added Check `E01-C5`; defined Filled Copy, `HTML` Authoring Master, and Press Preview in Section 4; added `C03`, `D01`, `D03`, and `D04` and updated the `Library-Index.md` reference floor (`v1.2.24`) in Section 3, per `REC-A04-014`. Existing templates keep their pins. | Hary Irfantri |
| `v2.4.0` | `2026-11-27` | Minor | Added `5.3.4` permitting an `HTML` authoring master with a press export (`3 mm` Bleed, crop marks, fixed `B02` `CMYK` builds, `PDF/X-4`) to serve as both Print and Digital edition, and extended `E01-C3`; re-pinned `TPL-E01-03` to `E01 (v2.4)` with its press layout export; transitioned `TPL-E01-02` to `Deprecated` (superseded by `TPL-E01-03`) and removed it from `Governs`; updated the `Library-Index.md` reference floor (`v1.2.23`) in Section 3, per `REC-A04-013`. | Hary Irfantri |
| `v2.3.0` | `2026-11-27` | Minor | Added `5.4.5` `±0.5 mm` A4 trim tolerance for digital `PDF` exports from `HTML` authoring masters declaring an A4 `@page` size, and extended `E01-C4`, per `REC-A04-009` (`U-02`); updated Section 7 notes for `TPL-E01-01`–`TPL-E01-04` after the footer move and `B02 (v1.3.0)` ink sync (`F-03`, `U-01`). | Hary Irfantri |
| `v2.2.0` | `2026-11-27` | Minor | Added `5.3.3` permitting standalone interactive `HTML` authoring masters for digital `TPL-E01` templates with `@media print` control suppression, local `06_Dependencies/Fonts/` references, and embedded `AST-B01` vector marks; aligned Sections 1, 2.1, and `E01-C3`; promoted `TPL-E01-03` (`03_Templates/TPL-E01-03_Formal-Cover-Digital.html`, pinned to `E01 (v2.2)`) in Section 7 following archival of outgoing `TPL-E01-03_Formal-Cover-Digital_v2.0.0.pdf` and `E01_Formal-Document-Layout_v2.1.1.md` to `99_Archive/`; and updated the `Library-Index.md` reference floor (`v1.2.12`) in Section 3. | Hary Irfantri |
| `v2.1.1` | `2026-11-26` | Errata | Removed cancelled `Planned` Google Docs row `TPL-E01-05` from `Governs` and Section 7 following Approver cancellation of the Google Workspace template migration (`A02 §5.3.1`), and updated the `Library-Index.md` reference floor (`v1.2.9`) in Section 3 per `A01 §5.5.7`. | Hary Irfantri |
| `v2.1.0` | `2026-11-26` | Minor | Added `5.4.4` permitting `≥ 300 DPI` lossless `PNG` brand marks derived from `AST-B01` `SVG` masters in Cloud-Native Office File digital `PDF` exports while preserving mandatory vector marks for `E03` print and compiled publications; aligned `5.4.3`, `E01-C4`, and Sections 1–4; registered `TPL-E01-05` (`Google Docs`, `Planned`, pinned to `E01 (v2.1)`) in `Governs` and Section 7; and updated the `Library-Index.md` reference floor (`v1.2.8`). | Hary Irfantri |
| `v2.0.3` | `2026-11-26` | Errata | Updated `TPL-E01-01` and `TPL-E01-04` Section 7 notes following minimalist layout revision (`2 mm` full-bleed top `24%` / `76%` split accent bar, rule-free header and single-line footer, `3 mm` Print bleed/crop marks, and `99_Archive/` archival of outgoing `v1.0.0` snapshots) and updated the `Library-Index.md` reference floor (`v1.2.6`) in Section 3 per `A01 §5.5.7`. | Hary Irfantri |
| `v2.0.2` | `2026-11-26` | Errata | Restored `TPL-E01-02` (`03_Templates/TPL-E01-02_Formal-Cover-Print.pdf`) and `TPL-E01-03` (`03_Templates/TPL-E01-03_Formal-Cover-Digital.pdf`) from `Sync Required` to `Approved` and re-pinned both to `E01 (v2.0)` in Section 7 following `B03 (v2.0.0)` Noto Sans recompilation (`REC-A04-007` `F-02`), and updated the `Library-Index.md` reference floor (`v1.2.4`) in Section 3 per `A01 §5.5.7`. | Hary Irfantri |
| `v2.0.1` | `2026-11-26` | Errata | Promoted `TPL-E01-01` (`03_Templates/TPL-E01-01_Header-and-Footer-Print.pdf`) and `TPL-E01-04` (`03_Templates/TPL-E01-04_Header-and-Footer-Digital.pdf`), both pinned to `E01 (v2.0)`, from `Planned` to `Approved` in Section 7 and updated the `Library-Index.md` reference floor (`v1.2.2`) in Section 3 per `A01 §5.5.7`. | Hary Irfantri |
| `v2.0.0` | `2026-11-26` | Major | Decoupled Clause `5.1.2` and Check `E01-C1` from the retired hardcoded `Montserrat` typeface name to reference the Display Typeface (`B03 §5.1.1`) in alignment with `B03 (v2.0.0)`; updated `Library-Index.md` reference floor (`v1.2.1`); re-pinned `TPL-E01-01`/`04` (`Planned`) to `E01 (v2.0)`; and transitioned `TPL-E01-02`/`03` to `Sync Required` pending `B03 (v2.0.0)` recompilation (`A01 §5.5.3`, `REC-A04-007`). | Hary Irfantri |
| `v1.2.0` | `2026-11-26` | Minor | Added Digital Distribution `PDF` Profile (`5.4.1`–`5.4.3`, `E01-C4`), mandated paired Print and Digital editions for dual-channel `TPL-E01` templates (`5.3.2`, `E01-C3`), added `E03` to Section 3, refined `TPL-E01-01`/`02` Title Slugs (`-Print`) per `A02 §5.3.3`, registered `TPL-E01-03` (`Approved`) and `TPL-E01-04` (`Planned`), and re-pinned `TPL-E01-01`–`04` to `E01 (v1.2)`. | Hary Irfantri |
| `v1.1.1` | `2026-11-26` | Errata | Promoted `TPL-E01-02` (`03_Templates/TPL-E01-02_Formal-Cover.pdf`) from `Planned` to `Approved` in Section 7 and updated the `Library-Index.md` reference floor (`v1.1.28`) in Section 3 per `A01 §5.5.7`. | Hary Irfantri |
| `v1.1.0` | `2026-11-25` | Minor | Expanded `5.1.1` and `E01-C1` to permit either horizontal or `4 mm` vertical left-spine orientation for the `24%` **Signal Red** / `76%` **Deep Navy** cover accent bar per `B04 (v1.2.0) §5.3.1`, updated `Library-Index.md` reference floor in Section 3, and re-pinned `TPL-E01-01` and `TPL-E01-02` to `E01 (v1.1)` in Section 7. | Hary Irfantri |
| `v1.0.2` | `2026-11-25` | Errata | Populated `Governs` header (`TPL-E01-01`, `TPL-E01-02`) to match active Section 7 artifacts per `A01 (v1.2.0) §5.2.8` and `REC-A04-005` (`F-07`). | Hary Irfantri |
| `v1.0.1` | `2026-11-23` | Errata | Trimmed unused Section 3 references (`D02`, `D05`, `E02`, `E03`, `E04`), removed misdirected `C04 §5.4.1` citation in `5.2.2`, and split long Section 5 sentences (`5.1.1`, `5.1.3`, `5.2.2`, `5.2.3`) per `REC-A04-004` (`F-04`). | Hary Irfantri |
| `v1.0.0` | `2026-11-22` | Major | Initial approved baseline of `E01` (Formal Document Layout), locking cover lockup and accent bar geometry, `vMAJOR.MINOR.ERRATA` and `C02` status metadata rules, `4 mm` running header/footer and pagination rules, corporate attribution placement, and `TPL-E01` template registration. | Hary Irfantri |
| `v0.1.0` | `2026-11-22` | Pre-Release | Initial draft establishing cover lockup and accent bar geometry, `vMAJOR.MINOR.ERRATA` and `C02` status metadata rules, `4 mm` running header/footer and pagination rules, corporate attribution placement, and `TPL-E01` template registration. | Hary Irfantri |
