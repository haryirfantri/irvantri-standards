# REC-A04-013 — Print Cover Retirement & Press Export Pre-Release Gate

| Field | Value |
| :--- | :--- |
| **Code** | `REC-A04-013` |
| **Record Type** | Pre-Release Gate |
| **Date** | `2026-11-27` |
| **Status** | `Closed` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Related Standards** | `A01 (v1.2.0)`, `A02 (v1.3.0)`, `A04 (v1.2.0)`, `B01 (v2.1.0)`, `B02 (v1.3.0)`, `B03 (v2.0.0)`, `E01 (v2.4.0)`, `E02 (v1.1.0)`, `E03 (v1.1.0)`, `Library-Index.md (v1.2.23)` |
| **Expiry Date** | `None` |

## 1. Review Scope & Trigger

This Governance Record (`REC-`) documents the Pre-Release Gate (`A04 (v1.2.0) §5.1.2`, `§5.1.5`) for the items below, released together with `Library-Index.md (v1.2.23)`:

| Item | Change | Version Gated |
| :--- | :--- | :--- |
| `E01` | `MINOR`: new `5.3.4` lets an `HTML` authoring master serve as both Print and Digital edition through a press export; `E01-C3` extended; `TPL-E01-02` removed from `Governs` | `v2.4.0` |
| `TPL-E01-03` | New "Export press PDF" control: `230 mm × 317 mm` sheet with `3 mm` Bleed and `100%` K crop marks, Approved-only gate; re-pinned to `E01 (v2.4)` | `E01 (v2.4)` |
| `tools/press_export.py` | New tool: maps each `sRGB` value to its fixed `B02` `CMYK` build, sets Trim and Bleed boxes, attaches the `FOGRA39` OutputIntent, writes `PDF/X-4` metadata, and runs the library-checks preflight | New |
| `tools/library_checks.py` | New `press-export` check runs the tool on `tools/fixtures/TPL-E01-03_press-layout.pdf` | — |
| `TPL-E01-02` | `Approved` to `Deprecated`, superseded by `TPL-E01-03`; final file moved to `99_Archive/` | Final `v2.0.0` |
| `PUB-01`, `PUB-02`, `PUB-03` | Build manifests synced to `E01 (v2.4.0)` and `Library-Index.md (v1.2.23)` | `v2.0.7`, `v2.0.6`, `v1.2.2` |

**Trigger.** On `2026-11-27` the Approver asked to revisit the print cover. The baseline review on `main` at `3e52c22` found that `TPL-E01-02` failed `E01-C3`, because its layout no longer matched `TPL-E01-03` (`E01 (v2.3.0) §5.3.2`). The baseline review also found that `TPL-E01-02` could not be filled in: it had no form fields, and its fonts were subset to basic `ASCII`. The Approver decided that the editable `HTML` cover is enough and asked for a press export inside it. On `2026-11-27` the Approver confirmed the four decisions in the proposal: a `MINOR` `E01` change, a two-step press export, no rename of the `TPL-E01-03` file, and a hard stop on off-palette colors.

### 1.1 Baseline Finding (closed by this release)

| Element | `TPL-E01-02` (print) | `TPL-E01-03` (digital) |
| :--- | :--- | :--- |
| Title top edge from trim | `77.4 mm` | `56.5 mm` |
| First metadata label from trim | `194.8 mm` | `213.7 mm` |
| Subtitle and Brand Blue rule | Present | Absent |
| Status badge beside the lockup | Absent | Present |
| Copyright size | `10.5 pt` | `9 pt` |

## 2. Method

Every result below was measured on branch `claude/project-thread-pbk5in`, based on `main` at `3e52c22`.

* **Render:** headless Chromium `158.0.8127.36` (Playwright `1.63.0`) loaded `TPL-E01-03`. A script filled every field with a sample Approved cover, pressed "Export press PDF", and saved the press layout `PDF`. It also saved the `sRGB` A4 export of the same cover for comparison.
* **Conversion:** `tools/press_export.py` converted the press layout `PDF` into the `PDF/X-4` file. Two negative tests checked that it stops: one input had an injected off-palette mid-grey fill (`RGB` `128, 128, 128`), and the other was an A4 digital export.
* **Geometry:** `pdfplumber` measured text, rectangle, and crop mark positions relative to the TrimBox. `pdfinfo` read the page boxes and the `PDF/X` subtype, and `pdffonts` listed the embedded fonts.
* **Interface:** a script drove the export controls with Draft, blank, and Approved covers and recorded the dialog contents and print calls.
* **Regression:** the blank digital export before and after the change was rendered at `60` dots per inch (`DPI`) and compared pixel by pixel.
* **Archive integrity:** `SHA-256` of each archived file compared with the outgoing file on `main` at `3e52c22`.
* **Automated check:** `tools/library_checks.py` (register sync, palette, token parity, contrast, links, `PDF` preflight, press export, and dependencies), run with the pinned `pypdf 6.1.3`.

## 3. Section 6 Verification — `E01 (v2.4.0)` Standard

| Check ID | Status | Measured Evidence |
| :--- | :--- | :--- |
| `A01-C2` | Pass | The header has 9 fields in order with Version `v2.4.0`. `Governs` lists `TPL-E01-01`, `TPL-E01-03`, and `TPL-E01-04`, which are the non-`Deprecated` Section 7 codes (`A01 §5.2.8`). |
| `A01-C3` | Pass | Level-2 sections `1`–`8` remain in order. The new clause is `5.3.4`, and its note uses the `> **Informative Note:**` prefix. |
| `A01-C4` | Pass | Added lines contain zero `MUST`, `WILL`, or `REQUIRED`. Each new `SHALL` names a measurable value or a referenced clause. |
| `A01-C5` | Pass | The release adds `5.3.4` and changes no existing `SHALL` or `SHALL NOT` text, so it is `MINOR` (`A01 (v1.2.0) §5.5.4`). `TPL-E01-01` and `TPL-E01-04` keep their pins. |
| `A01-C6`, `A02-C6` | Pass | `99_Archive/E01_Formal-Document-Layout_v2.3.0.md` has `SHA-256` `e7555eb0…a0dceaf5`, equal to the outgoing file on `main`. |
| `A01-C10` | Pass | `99_Archive/TPL-E01-02_Formal-Cover-Print_v2.0.0.pdf` has `SHA-256` `fd81eebf…ede6e36`, equal to the final file on `main`. `Library-Index.md` and `E01` Section 7 record it as `Deprecated`, superseded by `TPL-E01-03` (`A01 §5.7.3`). The suffix follows the `TPL-E01-03_Formal-Cover-Digital_v2.0.0.pdf` precedent. |
| `C01-C2`, `C01-C3` | Pass | Added lines contain zero pronouns and zero contractions. The longest new sentence is `30` words, counting each code span as one word, which is within the limit. |
| Section 5 to 6 mapping | Pass | `5.3.4` is cited by the extended `E01-C3`. |
| Section 3 parity | Pass | `5.3.4` cites `B02`, `B03`, and `E03`, which are already in Section 3. The `Library-Index.md` floor is `v1.2.23`. |

## 4. Section 6 Verification — `TPL-E01-03` Press Export

| Check ID | Status | Measured Evidence |
| :--- | :--- | :--- |
| `E01-C3` (`5.3.2`, `5.3.4`) | Pass | The press and `sRGB` exports share one layout. Measured from the trim, the first text is at `20.56` vs `20.51 mm`, the title at `66.92` vs `66.87 mm`, the first metadata label at `213.44` vs `213.66 mm`, and the copyright at `277.47` vs `277.42 mm`. The largest difference is `0.22 mm`, which comes from browser pixel snapping. |
| `E01-C3` (`5.3.3`) | Pass | The press marks render only under `html.press` in `@media print`. The authoring bar stays hidden in print. The blank digital export is pixel-identical before and after the change (difference bounding box `None`). |
| `E01-C1` | Pass | The press file keeps the `80 mm` `AST-B01-03` lockup as vector paths, the `4 mm` spine split at `225.74 mm` (`76.0%` of the trim), the Display Typeface title, and `C02` and `ISO` 8601 metadata. |
| `E03-C1` (`5.1.1`, `5.1.4`) | Pass | TrimBox `210.0 × 297.0 mm`, and BleedBox `3.0 mm` on each side. The spine bar runs `3.12 mm` past the top trim and `3.09 mm` past the bottom trim. Eight `100%` K crop marks run from the sheet edge to `3.12 mm` outside the trim. |
| `E03-C1` (`5.1.2`, `5.1.5`) | Pass | The lowest text box sits `16.35 mm` above the trim, measured on the font bounding box, which sits below the ink. The top text is `20.56 mm` below the trim, the left text `23.99 mm` from the trim, and the right text `23.49 mm` from the trim. |
| `E03-C3` (`5.3.1`, `5.3.5`) | Pass | The file uses 13 `CMYK` values and zero `RGB` operators. All 13 are `B02 §5.1.1` or `§5.6.1` builds, paper white, or `100%` K. The highest total ink is `250%` (Deep Navy). An injected off-palette mid-grey fill (`RGB` `128, 128, 128`) stopped the export with an error and wrote no file. |
| `E03-C3` (`5.3.3`) | Pass | The file has zero image objects. Every mark is vector. |
| `E03-C4` (`5.4.1`) | Pass | `PDF` 1.6 with `GTS_PDFXVersion` `PDF/X-4` in Info and XMP, `Trapped` `False`, and one `GTS_PDFX` OutputIntent `FOGRA39` carrying the `1,829,077`-byte `ISOcoated_v2_eci.icc` from `06_Dependencies/`. All 5 Noto fonts are embedded: Sans Regular, SemiBold, and Bold, Display ExtraBold, and Mono SemiBold. |
| `E03-C4` (`5.4.2`) | Pass | "Export press PDF" stops with "Press files need Approved status" for a Draft cover. It lists 8 open fields for a blank cover. It offers no "Export anyway" in either case and makes zero print calls. An Approved, complete cover prints once, and the press class and page size are removed after printing. The digital export still offers "Export anyway". |
| `E03-C4` (`5.4.3`) | Not tested | The Owner color proof applies to each press job, not to the template. The tool prints this reminder after every export. |

## 5. Section 6 Verification — Register & Publications

| Item | Check ID | Status | Measured Evidence |
| :--- | :--- | :--- | :--- |
| `Library-Index.md (v1.2.23)` | `A01-C7` | Pass | `register-sync` reports zero mismatches. Every registered path exists, including the archived `TPL-E01-02` path. |
| `PUB-01 (v2.0.7)`, `PUB-02 (v2.0.6)`, `PUB-03 (v1.2.2)` | `A01-C10` | Pass | Each build manifest cites `E01 (v2.4.0)`, `Library-Index.md (v1.2.23)`, and a compile date of `2026-11-27`, and keeps its precedence notice. `PUB-01` and `PUB-02` list `TPL-E01-03` at `E01 (v2.4)` and no longer list `TPL-E01-02`. `PUB-02` cites `PUB-01 (v2.0.7)`. |
| `PUB-01`–`PUB-03` | `B02-C1` | Pass | `palette` reports zero off-palette values. |

## 6. Non-Conformity Register (`A04 (v1.2.0) §5.2.2`)

None. Zero non-conformities were found. The baseline `E01-C3` failure in Section 1.1 closes because `TPL-E01-02` moves to `Deprecated`.

## 7. Closure Verification (`A04 (v1.2.0) §5.2.3`, `§5.1.7`)

* **Gate Verdict:** `Pass`. The items in Section 1 are released as listed.
* **Automated Check:** `python3 tools/library_checks.py` gives `PASS` with zero failing findings and zero known issues. Continuous integration (`CI`) run `46079411485` measured commit `020b6d0`, which holds every gated change, and passed. The `press-export` check converted the committed sample to a `210.0 × 297.0 mm` trim with `3.0 mm` Bleed, `FOGRA39`, and a highest total ink of `250%`.
* **Follow-Up:** The header and footer (`TPL-E01-01`, `TPL-E01-04`) and the letterheads (`TPL-E04-01`, `TPL-E04-03`) remain static `PDF` pairs. The Approver plans to move them to `HTML` masters on the pattern set here.
* **Approver Sign-Off:** The Approver confirmed the proposal on `2026-11-27`. Merging the release pull request records sign-off and puts the release into effect.
* **Approver:** Hary Irfantri
