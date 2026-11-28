# REC-A04-015 — Document Master Pre-Release Gate

| Field | Value |
| :--- | :--- |
| **Code** | `REC-A04-015` |
| **Record Type** | Pre-Release Gate |
| **Date** | `2026-11-28` |
| **Status** | `Closed` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Related Standards** | `A01 (v1.2.0)`, `A02 (v1.3.0)`, `A03 (v1.1.1)`, `A04 (v1.2.0)`, `B01 (v2.1.0)`, `B02 (v1.3.0)`, `B03 (v2.0.0)`, `B04 (v1.2.0)`, `B05 (v1.2.0)`, `C01 (v1.1.1)`, `C02 (v1.1.0)`, `C04 (v1.0.1)`, `D01 (v1.0.3)`, `D04 (v1.2.1)`, `E01 (v2.6.0)`, `E02 (v1.1.0)`, `E03 (v1.1.0)`, `E05 (v1.0.0)`, `Library-Index.md (v1.2.25)` |
| **Expiry Date** | `None` |

## 1. Review Scope & Trigger

This Governance Record (`REC-`) documents the Pre-Release Gate (`A04 (v1.2.0) §5.1.2`, `§5.1.5`) for the items below, released together with `Library-Index.md (v1.2.25)`:

| Item | Change | Version Gated |
| :--- | :--- | :--- |
| `E05` | New standard: Document Body Elements (47 clauses `5.1.1`–`5.9.3`, checks `E05-C1`–`E05-C9`) | `v1.0.0` |
| `E01` | `MINOR`: new `5.5.11` (free body content renders to `E05` with the running header and footer on every page after the cover); `E01-C5` extended; `E05` added to Section 3; Section 7 and `Governs` updated | `v2.6.0` |
| `TPL-E01-06` | New Formal Document Master, `Approved`, pinned to `E01 (v2.6)` | `E01 (v2.6)` |
| `TPL-E01-01`, `TPL-E01-04` | `Deprecated`, superseded by `TPL-E01-06`; final files moved unmodified to `99_Archive/` as `_v2.0.0` | `E01 (v2.0)` |
| `Dependencies-Manifest.md` | `MINOR`: new Section 4 registering four `MIT` script libraries in `06_Dependencies/Scripts/` | `v2.1.0` |
| `tools/` | New `build_document_master.py` and `pdf_finish.py`; `press_export.py` reads the cover title and Owner and tidies bookmarks; `library_checks.py` checks embedded scripts, script checksums and licences, and that `TPL-E01-06` equals a fresh build; new fixture `TPL-E01-06_press-layout.pdf` | — |
| `PUB-01`, `PUB-02`, `PUB-03` | Build manifests synced; `PUB-03` gains a Formal Document Bodies summary | `v2.0.9`, `v2.0.8`, `v1.2.4` |

**Trigger.** On `2026-11-28` the Approver asked for one full `HTML` document master in place of the separate header and footer templates, with a locked frame, labelled fields, a Markdown body with paste from Word and Google Docs, and defined styles for every body element, and asked for the element set to be exhaustive. The proposal (`proposals/document-master/Document-Master-Proposal_2026-11-28.md` in the project files) and drafts of `E05 v0.1.0` and the `E01 v2.6.0` changes were reviewed. The Approver approved:

1. A new standard `E05` for the element styles.
2. Embedding Paged.js, marked, Turndown and turndown-plugin-gfm (`MIT`), logged in the Dependencies Manifest.
3. Deprecating `TPL-E01-01` and `TPL-E01-04` once `TPL-E01-06` is `Approved`.
4. Diagrams as embedded `SVG` or `PNG` figures drawn to `B05`, with no Mermaid.
5. The full element catalogue (groups A and B), with group C excluded.
6. Strict export blocking; body `12 pt`, tables and code `10.5 pt`, footnotes and source lines `9 pt`; Heading 1 on a new page and on a right-hand page in two-sided print; bookmarks and document properties as `SHALL`.

Against the `v0.1.0` draft, the release text records four build findings: Paged.js gives every page one size, so `{landscape}` tables rotate on a portrait page (`E05 §5.4.8`); the press route has no raster conversion, so raster figures are digital-only (`§5.6.2`); `{wide}` figures were dropped because every figure already spans at most the text block (`§5.6.3`); and `tools/pdf_finish.py` writes document properties that browsers omit (`§5.9.2`).

## 2. Method

Every result below was measured on branch `claude/project-thread-a83cq9`, based on `main` at `bbeb66d`.

* **Exports:** Chromium (Playwright) opened `03_Templates/TPL-E01-06_Formal-Document-Master.html` (`7,657,182` bytes, `SHA-256` `dd0998a7…fe972233db`) from disk with the sample document. Scripts pressed **Export A4 PDF** and **Export press PDF** with the print call captured, then saved each as a `PDF` with `preferCSSPageSize`. `tools/pdf_finish.py` finished the digital file; `tools/press_export.py` converted the press file.
* **Measurements:** `getComputedStyle` and `getBoundingClientRect` on the laid-out pages, converted to `pt` and `mm`. `PDF` structure from `pypdf 6.1.3` and the `pdf-preflight` functions of `tools/library_checks.py`.
* **Behaviour:** scripted browser runs for the Draft banner, watermark, two-sided layout, Export Blocks, overflow, paste, Filled Copy, autosave, keyboard order, and network requests.
* **Text:** a Python script parsed the headers and sections of `E05` and `E01`, scanned `E05` and every line added to `E01` for keywords, pronouns, contractions and sentence length, and mapped each `E05` clause to Section 6.
* **Archive integrity:** `SHA-256` of each archived file against the outgoing file on `main` at `bbeb66d`.
* **Automated check:** `tools/library_checks.py`, run with the pinned `pypdf 6.1.3`.

## 3. Section 6 Verification — Standards Text

| Check ID | Status | Measured Evidence |
| :--- | :--- | :--- |
| `A01-C2` | Pass | Both headers have 9 fields in order. `E05` shows `v1.0.0` `Approved`, Next Review `2027-05-28`, `Governs` `None`. `E01` shows `v2.6.0` and `Governs` `TPL-E01-03`, `TPL-E01-06`, matching its Section 7 `Approved` rows. |
| `A01-C3` | Pass | Both files keep level-2 sections `1`–`8` in order. `E05` numbers 47 clauses `5.1.1`–`5.9.3` in 9 subsections; `E01` adds `5.5.11`. Informative notes use the `> **Informative Note:**` prefix. |
| `A01-C4` | Pass | `E05` and the `E01` additions contain zero `MUST`, `WILL`, or `REQUIRED` and zero lowercase `shall`, `should`, or `may`. `E05` holds 108 `SHALL` and 6 `MAY`; each `SHALL` names a value, a control, or a referenced clause. |
| `A01-C5` | Pass | `git diff` lists the removed `E01` lines as the old Version, `Governs`, Section 1 sentence, Section 2.1 bullet, `Library-Index.md` floor, `E01-C5` text (repeated in full with an added clause), and the `TPL-E01-01` and `TPL-E01-04` rows (replaced with `Deprecated` rows). No `SHALL` changes and no clause is renumbered, so the release is `MINOR` (`A01 §5.5.4`). |
| `A01-C6`, `A02-C6` | Pass | Archive `SHA-256` equals `main`: `E01_Formal-Document-Layout_v2.5.0.md` `3adedaed…98d466c2`, `Dependencies-Manifest_v2.0.0.md` `a19301e2…4432c3ec`, `TPL-E01-01_Header-and-Footer-Print_v2.0.0.pdf` `38b46765…60fde53`, `TPL-E01-04_Header-and-Footer-Digital_v2.0.0.pdf` `a4b6e790…5bfcfa`. |
| `A02-C3`, `A02-C5` | Pass | `E05_Document-Body-Elements.md` and `TPL-E01-06_Formal-Document-Master.html` follow the code and Title Slug patterns; `TPL-E01-05` (cancelled) is not reused. |
| `C01-C2` | Pass | Zero first- or second-person pronouns and zero contractions. |
| `C01-C3`, `C02-C2` | Pass | The longest `E05` Section 5 sentence is `30` words; `E01 §5.5.11` peaks at `19`. `JPEG`, `CMYK`, and `ARIA` are expanded at first use; `HTML`, `PDF`, `PNG`, `SVG`, and `URL` are `C02 §5.2.2` exemptions. |
| Section 5 to 6 mapping | Pass | All 47 `E05` clauses are cited by `E05-C1`–`E05-C9`; `E01 §5.5.11` is cited by the extended `E01-C5`. |
| Section 3 parity | Pass | Every standard cited in `E05` Section 5 is in its Section 3. Each clause citation (37 distinct citations, such as `B03 §5.3.1`, `C04 §5.4.1`, and `D04 §5.3.2`) resolves to an existing clause. Both floors are `Library-Index.md` `v1.2.25`. |

## 4. Section 6 Verification — `E05 (v1.0.0)` on `TPL-E01-06`

The sample document lays out as 18 A4 pages in `0.41`–`0.48 s`: cover, distribution list, contents, lists of tables and figures, summary, body, Appendix A, Glossary, References, Revision History, and back page.

| Check ID | Status | Measured Evidence |
| :--- | :--- | :--- |
| `E05-C1` | Pass | The sample uses every Table 1 syntax. The `html-master` check finds zero literal colors in style rules, including the document stylesheet. Raw `<b>raw</b> <script>x</script>` renders as literal text with zero `script` elements in the pages. A Word-style paste kept the heading, bold, italic, sub/superscript, numbered list, table, and a Google Docs bold run, dropped `Calibri`, red, and `20pt`, and replaced a remote image with a visible notice. |
| `E05-C2` | Pass | Body `Noto Sans` `12 pt` / `1.5`, Text Primary, `4 mm` paragraph gap, `orphans`/`widows` `2`. Headings: H1 `Noto Sans Display` `22 pt` `800` Deep Navy with a page break and `6 mm` below; H2 `15 pt` `700` Deep Navy, `8 mm` / `3 mm`; H3 `12.5 pt` `700` Text Primary, `6 mm` / `2 mm`; H4 `Noto Sans` `12 pt` `700`, `4 mm` / `1 mm`, unnumbered. Numbers `1`, `1.1`, `1.1.1` in Brand Blue; `break-after: avoid` on all headings. Inline code and keys `Noto Sans Mono` `0.875 em` (`10.5 pt`), code on Surface Muted. Links are live in the digital `PDF`. |
| `E05-C3` | Pass | A fourth list level raises an Export Block. Markers: level 1 `1.6 mm` Deep Navy square, level 2 `1.6 mm` outline (`1 px`), level 3 `1.2 mm` Border Strong. Numbered markers `12 pt` `700` Brand Blue, decimal then lower-alpha then lower-roman. Checkbox `3.00 mm`; definitions indent `6.00 mm`. |
| `E05-C4` | Pass | Captions `10 pt`, label `700` Text Primary. Cells `10.5 pt` / `1.4`, tabular numerals. Header `8 pt` `700` uppercase, `0.08 em`, Text Muted on Canvas Subtle. Table 2 continues onto a second page with its header row repeated (1 continuation `thead`); rows never split. A blank cell blocks export as "Table 4, row 1, B". Source line `9 pt` Text Muted. Totals Row `700` over Border Strong. Table 3 `{landscape}` renders rotated on page 11 inside `222 mm` × `170 mm` with the portrait header and footer. |
| `E05-C5` | Pass | Code `10.5 pt` / `1.5` on Canvas Subtle, `4 mm` padding, language label `7.5 pt` uppercase Text Muted, line numbers as unselectable text. Quotation `2 px` Deep Navy rule, italic; attribution `10.5 pt` Text Muted. Five callouts with text labels, `4 px` left bar, `12 pt` text, unsplit. Summary on Surface Tint with a `2 px` Deep Navy top rule. Note and Example blocks on Canvas Subtle with a `2 px` Border Default rule. Clause hanging indent `16.00 mm`. Sign-off line `60.00 mm`; an empty Name raises an Export Block. Rule `1 px` Border Default, `6.00 mm` above and below. |
| `E05-C6` | Pass | Figure 1 has a caption below and alternative text; a figure without either raises two Export Blocks. The `SVG` diagram is `169.3 mm` wide, uses only `B02` hex values, `1.5 px` Border Strong nodes with `4 px` radius, one Deep Navy key node, right-angle Deep Navy connectors, and `9 pt` minimum labels. A `600 px` raster test image placed at `50.80 mm` (`300` pixels per inch) and raised the press block "Figure 2 is a raster image". |
| `E05-C7` | Pass | Footnote text `9 pt` Text Muted at the page foot below a `30 mm` `1 px` Border Default rule; calls in Brand Blue. A cross-reference prints "Table 2 on page 9"; an unknown target raises an Export Block. References use `[n]` with an `8 mm` hanging indent. |
| `E05-C8` | Pass | Part order matches `5.8.1`. Contents lists H1 and H2 entries with page numbers computed from the layout; lists of tables and figures hold 5 tables and 1 figure. Appendix numbering `A.1` and `Table A1`. Distribution list is captioned Table 1. The back page holds the lockup and copyright line. Two-sided mode inserted 10 blank pages with "This page is intentionally left blank." and the running header and footer, so every part starts on an odd page and the document ends on page 28. |
| `E05-C9` | Pass | Section names fit the `84 mm` header region with ellipsis. The finished digital `PDF` has 20 bookmarks (H1–H4 and appendices), Title "Document Master Element Reference", Author "Hary Irfantri", and `/Lang en-US`. With its bookmarks removed, `pdf_finish.py` rebuilt them from the Contents page as 9 top-level entries with their `1.1`-style children. Blocked exports announce "Export stopped. 4 items need fixing; see Export checks." in the assertive Live Region and move focus to the first item. |

## 5. Section 6 Verification — `E01 (v2.6.0)` on `TPL-E01-06`

| Check ID | Status | Measured Evidence |
| :--- | :--- | :--- |
| `E01-C1` | Pass | Cover `80 mm` `AST-B01-03` lockup; `4 mm` spine split `225.72 mm` Deep Navy over Signal Red; metadata panel with Identifier, Version, Status, Issue Date, Owner, Approver; Superseded By and waiver rows appear when filled. |
| `E01-C2` | Pass | Body pages: `72 mm` lockup at `16 mm` from the top, body area `40`–`265 mm` by `20`–`190 mm`, `2 mm` top bar split `24%` / `76%`, footer title and mono version with `Page X of Y`, lowest footer ink `21.3 mm` above the trim. Headers appear on pages `2`–`17` and not on the cover or back page (`5.5.11`). A Draft shows the `E02 §5.3.2` banner on the cover and in the header, and the watermark on 16 body pages. |
| `E01-C3`, `E01-C4` | Pass | Digital: 18 pages at `209.89 × 297.01 mm` (inside `±0.5 mm`, `5.4.5`), fonts embedded, 23 `sRGB` values all on `B02`, zero findings. Press: 18 pages, TrimBox `210 × 297 mm`, BleedBox `3 mm` on every side, `PDF/X-4`, `FOGRA39` OutputIntent, 24 fixed `B02` `CMYK` builds, maximum total ink `250%`, preflight passed. |
| `E01-C5` | Pass | `html-master`: zero literal colors, 14 fields all limited, `Save filled copy`, `beforeunload`, `Press preview` beside `Export press PDF`, zero remote references, 9 fonts and 4 scripts byte-identical to `06_Dependencies/`, 6 Live Regions, and the file equals a fresh build. Browser: zero network requests in every run; a 90-character title and 140-character subtitle raise both overflow blocks; a Filled Copy (`7,669,686` bytes) reopens with every value and image, and a second save from it works; an edit triggers the `beforeunload` warning, and after reload the autosave banner restores it; Tab reaches every field, toolbar button, option and export control in visual order; Press preview sets `aria-pressed="true"` and shows 18 sheets with bleed and crop marks. The body renders to `E05` (Section 4). |

## 6. Section 6 Verification — Register, Dependencies & Publications

| Item | Check ID | Status | Measured Evidence |
| :--- | :--- | :--- | :--- |
| `Library-Index.md (v1.2.25)` | `A01-C7` | Pass | `register-sync` compares 23 standard headers with zero mismatches. Series `E` allocation reads `E01`–`E05`; Coverage Summary `23` Approved. `TPL-E01-01` and `TPL-E01-04` rows point to their archive paths. |
| `Dependencies-Manifest.md (v2.1.0)` | `A02-C10`, `B03-C2` | Pass | `dependencies` matches size and `SHA-256` for 20 files, including `paged.js` (`920,798` bytes), `marked.umd.js` (`55,534`), `turndown.browser.umd.js` (`27,166`), and `turndown-plugin-gfm.js` (`4,191`); each script folder holds its `MIT` `LICENSE` with a copyright line. |
| `PUB-01 (v2.0.9)`, `PUB-02 (v2.0.8)`, `PUB-03 (v1.2.4)` | `A01-C10` | Pass | Each build manifest cites `E01 (v2.6.0)`, `E05 (v1.0.0)`, `Dependencies-Manifest.md (v2.1.0)`, and `Library-Index.md (v1.2.25)`; template pins show `TPL-E01-03` and `TPL-E01-06`. `PUB-02` cites `PUB-01 (v2.0.9)`. |
| `PUB-01`–`PUB-03`, `TPL-E01-06` | `B02-C1` | Pass | `palette` reports zero off-palette values across 55 files. |

## 7. Non-Conformity Register (`A04 (v1.2.0) §5.2.2`)

None. Zero non-conformities remain. Defects found during the build were fixed before this record: footnotes rendered at `12 pt` until their style moved outside the body scope; Chromium dropped H1 numbers from bookmarks, now restored by `pdf_finish.py` and `press_export.py`; and the raster press block now names the figure.

## 8. Closure Verification (`A04 (v1.2.0) §5.2.3`, `§5.1.7`)

* **Gate Verdict:** `Pass`. The items in Section 1 are released as listed.
* **Automated Check:** `python3 tools/library_checks.py` gives `PASS` with zero failing findings and zero known issues on the release branch. The `html-master` check measured 2 `HTML` templates and enforced 1 (`TPL-E01-06`). The continuous integration (`CI`) run on the release pull request is cited when it completes.
* **Risk Accepted:** Paged.js has had no upstream release since `0.4.3` (`2023`). If a browser change breaks it, the approved fallback is an in-house paginator for the fixed `E05` element set, released through this gate.
* **Follow-Up:** Letterheads and memos (`TPL-E04-01`, `TPL-E04-03`) move to short variants of this master in a later release. `TPL-E01-03` stays the standalone cover.
* **Approver Sign-Off:** The Approver approved the proposal and the build on `2026-11-28`. Merging the release pull request records sign-off and puts the release into effect.
* **Approver:** Hary Irfantri
