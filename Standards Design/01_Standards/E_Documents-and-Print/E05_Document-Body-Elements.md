# E05 — Document Body Elements

| Field | Value |
| :--- | :--- |
| **Code** | `E05` |
| **Version** | `v2.0.0` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-28` |
| **Next Review** | `2027-05-28` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `None` |

## 1. Purpose

This standard defines the body elements of formal documents produced by **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`): headings, text, lists, tables, code, quotations, callouts, figures, diagrams, references, and document parts. It fixes how each element is written, how it looks, and how it breaks across pages. Authors supply content; the template supplies every visual decision.

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* Body content of formal documents (`E01`) rendered by an `HTML` Authoring Master (`E01 §5.5`).
* Body content of letters, memoranda (`E04`), and compiled publications (`PUB-`) where their governing standard or template adopts this standard.
* Paste conversion of rich text from word processors into an `HTML` Authoring Master.

### 2.2 Out of Scope
This standard does not govern:
* Cover geometry, running header and footer layout, pagination format, or export profiles (governed by `E01`).
* Version display, status badges, status banners, or watermarks (governed by `E02`).
* Paper, bleed, and press production (governed by `E03`).
* Slide decks, email signatures, and workbooks (governed by `E04`).
* Interactive interface components such as inputs, dialogs, and data grids (governed by `D03`).
* Markdown source files of normative standards (governed by `A01`).

## 3. Normative References

The following documents are referenced in this standard. For undated references, the latest approved edition applies.
* `Library-Index.md` — Standards Design Library Index (`v2.0.0` or later).
* `A01` — Document Control & Lifecycle.
* `A02` — Taxonomy, Coding & File Naming.
* `A03` — Entity & Brand Architecture.
* `B02` — Color System.
* `B03` — Typography.
* `B04` — Grids, Spacing & Graphic Devices.
* `B05` — Iconography, Diagrams & Visuals.
* `C01` — Voice, Tone & Plain Language.
* `C04` — Data, Dates & Citation Formatting.
* `D01` — Design Tokens & Architecture.
* `D04` — Accessibility & Usability.
* `E01` — Formal Document Layout.
* `E02` — Versioning & Draft Marking.
* `E03` — Print & Production Specifications.
* CommonMark Specification, version `0.31.2` (2024), and GitHub Flavored Markdown Specification, version `0.29-gfm` (2019).

## 4. Terms & Definitions

For terms shared across the library, refer to `C02`, `A01`, `B03`, `C04`, `E01`, and `E02`. For the purposes of this standard, the following definitions apply:
* **Body Element:** A unit of document content listed in Table 1 (`5.1.2`), such as a heading, list, table, or figure.
* **Callout:** A labelled panel that sets a short passage apart by purpose, using one `B02` semantic role.
* **Continuation Page:** A page on which a table, list, or code block continues from the previous page.
* **Cross-Reference:** A link to a heading, table, figure, or footnote that the master renders as its current number or page.
* **Export Block:** A state in which an `HTML` Authoring Master refuses both `PDF` exports and names the element and fix (`E01 §5.5.5`).
* **Sign-Off Block:** A panel recording the name, role, date, and signature line of each person approving a document.
* **Totals Row:** The final table row that sums or summarizes the rows above it.

## 5. Requirements

### 5.1 Element Set & Authoring Source
**5.1.1** Body content SHALL be authored in CommonMark with GitHub Flavored Markdown extensions and the syntax in Table 1. An `HTML` Authoring Master SHALL convert rich text pasted from a word processor into that syntax.

**5.1.2** An `HTML` Authoring Master SHALL render each element in Table 1 to the styles in Clauses `5.2`–`5.9`. All values SHALL come from `AST-D01-01` tokens (`D01`, `E01 §5.5.3`). Callout, block, and list text SHALL use the body size in `5.2.1` unless a clause sets another size.

| Group | Element | Syntax |
| :--- | :--- | :--- |
| Headings | Heading levels 1–4 | `#` to `####` |
| Text | Paragraph, bold, italic, strikethrough | Plain text, `**bold**`, `*italic*`, `~~text~~` |
| Text | Superscript, subscript | `^text^`, `~text~` |
| Text | Inline code, keyboard key | `` `code` ``, `[[Ctrl]]` |
| Text | Link | `[text](https://address)` |
| Lists | Bulleted, numbered, checklist (3 levels) | `-`, `1.`, `- [ ]` / `- [x]` |
| Lists | Definition list | `Term` then `: Definition` |
| Tables | Table with caption | `Table: Caption` line before a pipe table |
| Tables | Source or notes line | `Source:` or `Note:` paragraph directly after the table |
| Tables | Totals row | Final row whose first cell starts with `Total` |
| Tables | Landscape table | `{landscape}` at the end of the caption line |
| Code | Code block | Fenced block with optional language and `{lines}` |
| Blocks | Quotation | `>` with an optional final line starting `— ` |
| Blocks | Callout | `> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`, `> [!WARNING]`, `> [!CAUTION]` |
| Blocks | Summary box | `> [!SUMMARY]` |
| Blocks | Informative Note, Example | `> **Informative Note:**`, `> **Example:**` (`A01 §5.2.6`) |
| Blocks | Requirement clause | Paragraph starting with a bold clause number, such as `**5.1.1**` |
| Blocks | Sign-off block | Fenced block with language `signoff` |
| Blocks | Horizontal rule, page break | `---`, `\pagebreak` |
| Figures | Figure, side-by-side figure | `![alt](file "Caption")`, or a `Figure: Caption` line directly below the image; two images in one paragraph sit side by side |
| Figures | Diagram | A figure whose file is an `SVG` drawn to Clause `5.6.4` |
| References | Footnote | `[^1]` with `[^1]: text` |
| References | Cross-reference | `{#id}` after a heading or caption; `[](#id)` or `[](#id "page")` |
| References | References list | `# References` with a numbered list of citations |
| Parts | Appendix | `# Appendix A — Title` |
| Parts | Glossary | `# Glossary` with a definition list |
| Parts | Distribution list | Cover field set (`5.8.5`) |

**5.1.3** An `HTML` Authoring Master SHALL NOT offer syntax or controls for the following:
* Text color, typeface, or size changes, highlighting, or underlining for emphasis.
* Emoji images, raw `HTML`, or merged table cells.
* Embedded audio or video, or mathematical equation layout.

Raw `HTML` in the body SHALL render as literal text.

> **Informative Note:** Equations are excluded because equation layout needs a math typeface outside `B03`. A future revision can add them if a document type needs them.

**5.1.4** Paste conversion SHALL keep headings, paragraphs, emphasis, lists, tables, links, and embedded images. It SHALL discard source typefaces, colors, sizes, and spacing. It SHALL replace each image referenced by a remote `URL` with a visible notice, because masters make no network requests (`E01 §5.5.8`).

### 5.2 Text & Headings
**5.2.1** Body text SHALL use the Text Typeface (`B03 §5.1.1`) at `12 pt` with a `1.5` line height, in **Text Primary** (`B02`). Paragraphs SHALL be separated by `4 mm` (`B04 §5.1.2`). A paragraph SHALL NOT leave fewer than `2` lines at the foot or head of a page.

**5.2.2** Headings SHALL use the values below, with a `1.2` line height (`B03 §5.2.3`):

| Level | Typeface | Size | Weight | Color | Space Above / Below |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Heading 1 | Display Typeface | `22 pt` | `800` | **Deep Navy** | Starts a new page / `6 mm` |
| Heading 2 | Display Typeface | `15 pt` | `700` | **Deep Navy** | `8 mm` / `3 mm` |
| Heading 3 | Display Typeface | `12.5 pt` | `700` | **Text Primary** | `6 mm` / `2 mm` |
| Heading 4 | Text Typeface | `12 pt` | `700` | **Text Primary** | `4 mm` / `1 mm` |

**5.2.3** Headings 1–3 SHALL be numbered automatically with dot-delimited Arabic numerals (`1`, `1.1`, `1.1.1`) (`C04 §5.4.3`). The number SHALL render in **Brand Blue** (`B02 §5.1.1`). Heading 4 SHALL NOT be numbered. A heading SHALL NOT be the last line on a page.

**5.2.4** Inline elements SHALL render as follows:
* Bold at weight `700`; italic in the Text Typeface italic.
* Strikethrough as a single `1 px` line through the text.
* Superscript and subscript at `75%` of the surrounding size.
* Inline code in `Noto Sans Mono` (`B03 §5.1.2`) at `0.875 em` on **Surface Muted** with a `4 px` radius (`B04 §5.2.1`).
* Keyboard keys in `Noto Sans Mono` at `0.875 em` with a `1 px` **Text Muted** outline and a `4 px` radius.
* Links in **Brand Blue** with an underline. Links SHALL remain live in the digital `PDF`.

### 5.3 Lists
**5.3.1** Lists SHALL nest no deeper than three levels. A fourth level SHALL cause an Export Block.

**5.3.2** Bulleted list markers SHALL be squares (`B04 §5.3.2`). Level 1 SHALL use a `1.6 mm` solid **Deep Navy** square, level 2 a `1.6 mm` outlined **Deep Navy** square, and level 3 a `1.2 mm` solid **Text Muted** square.

**5.3.3** Numbered lists SHALL use decimal numerals at level 1, lowercase letters at level 2, and lowercase Roman numerals at level 3. Numbers SHALL render in **Brand Blue** at weight `700`.

**5.3.4** Checklist items SHALL render a `3 mm` square box with a `1 px` **Text Muted** outline. A checked item SHALL fill the box with **Brand Blue** and a **Pure White** tick.

**5.3.5** Definition list terms SHALL render at weight `700`. Definitions SHALL indent `6 mm` below their term.

### 5.4 Tables
**5.4.1** Every table SHALL carry a caption above it labelled `Table N.` in sequence (`C04 §5.4.4`). Captions SHALL use the Text Typeface at `10 pt` with the label in **Text Primary** at `700` and the description in **Text Muted**. A table without a caption SHALL cause an Export Block.

**5.4.2** Table text SHALL use the Text Typeface at `10.5 pt` with a `1.4` line height and Tabular Numerals (`B03 §5.3.1`). Header cells SHALL use `8 pt` uppercase at weight `700` and `0.08 em` tracking in **Text Muted** on **Canvas Subtle** (`B03 §5.2.7`). Rows SHALL be ruled with `1 px` **Border Subtle**; the header row SHALL be ruled with `1 px` **Border Default**.

**5.4.3** Right-aligned columns SHALL be used for numeric data, and numeric headers SHALL state shared units (`C04 §5.4.2`).

**5.4.4** A table that continues onto another page SHALL repeat its header row on each Continuation Page. A table row SHALL NOT split across pages.

**5.4.5** A blank data cell SHALL cause an Export Block that names the table number, row, and column (`C04 §5.4.1`).

**5.4.6** A source or notes line SHALL render directly below its table in the Text Typeface at `9 pt` in **Text Muted**, starting with `Source:` or `Note:`.

**5.4.7** A Totals Row SHALL render at weight `700` above a `1 px` **Text Muted** rule.

**5.4.8** A table marked `{landscape}` SHALL render alone on a portrait page, rotated `90°` counter-clockwise so its top faces the binding edge. It SHALL fit a `222 mm` × `170 mm` area inside the body region. The page keeps its portrait running header and footer, so every page of the `PDF` shares one A4 portrait size (`E01 §5.4`). A landscape table that does not fit that area SHALL cause an Export Block asking for it to be split. A table wider than the `170 mm` text block and not marked `{landscape}` SHALL cause an Export Block.

> **Informative Note:** Rotating the table instead of the page keeps one page size through the file, which digital viewers, the press sheet (`E01 §5.3.4`), and duplex printers all expect.

### 5.5 Code, Quotations, Callouts & Blocks
**5.5.1** Code blocks SHALL use `Noto Sans Mono` at `10.5 pt` with a `1.5` line height, in **Text Primary** only. They SHALL sit on **Canvas Subtle** with a `1 px` **Border Subtle** outline, a `4 px` radius, and `4 mm` padding. Lines longer than the block SHALL wrap. A language label MAY render above the code in `7.5 pt` uppercase **Text Muted**. Line numbers MAY render in **Text Muted** and SHALL NOT be copied with the code.

> **Informative Note:** Syntax coloring is excluded because token colors would fall outside the `B02` palette.

**5.5.2** Quotations SHALL render in italic with a `2 px` **Deep Navy** left rule and `6 mm` indent. An attribution line starting with `— ` SHALL render upright at `10.5 pt` in **Text Muted**.

**5.5.3** Callouts SHALL use the `B02 §5.3.1` semantic role below as a `4 mm`-padded panel with a role surface, a `1 px` role border, a `4 px` role-foreground left bar, and a `4 px` radius. Each callout SHALL display its label as text, so color is not the only cue (`D04 §5.1.2`). A callout SHALL NOT split across pages.

| Callout | Label | `B02` Semantic Role | Use |
| :--- | :--- | :--- | :--- |
| `NOTE` | Note | Informative | Context the reader needs |
| `TIP` | Tip | Success | A better way to do something |
| `IMPORTANT` | Important | Neutral | A rule the reader must not miss |
| `WARNING` | Warning | Warning | A step that causes rework if skipped |
| `CAUTION` | Caution | Danger | A step that can cause loss or harm |

**5.5.4** A summary box SHALL render on **Surface Tint** with a `2 px` **Deep Navy** top rule and the label `Summary`. A document SHALL contain no more than one summary box.

**5.5.5** Informative Note and Example blocks SHALL render on **Canvas Subtle** with a `2 px` **Border Default** left rule and their label at weight `700`.

**5.5.6** A requirement clause SHALL render its clause number at weight `700` in **Brand Blue** with a `16 mm` hanging indent. Normative keywords inside clauses SHALL follow `A01 §5.3`.

**5.5.7** A Sign-Off Block SHALL show, for each signatory, `Name`, `Role`, `Date` (`YYYY-MM-DD`, `C04 §5.1.1`), and a `60 mm` **Text Muted** signature line. A Sign-Off Block SHALL NOT split across pages. An empty `Name` or `Role` SHALL cause an Export Block.

**5.5.8** Horizontal rules SHALL render as a `1 px` **Border Default** line with `6 mm` space above and below (`B04 §5.3.2`).

### 5.6 Figures & Diagrams
**5.6.1** Every figure SHALL carry a caption below it labelled `Figure N.` in sequence (`C04 §5.4.4`), styled as table captions (`5.4.1`). Every figure SHALL carry alternative text describing its content (`D04 §5.1.1`). A figure without a caption or alternative text SHALL cause an Export Block.

**5.6.2** Figure images SHALL be embedded in the file (`E01 §5.5.8`). Raster images in `PNG` or Joint Photographic Experts Group (`JPEG`) format SHALL be placed at `300` pixels per inch of their native size and never enlarged. They MAY appear in the digital edition. A press export containing a raster image SHALL cause a press Export Block naming the figure. Press files carry only fixed `B02` Cyan-Magenta-Yellow-Key (`CMYK`) builds, and no automated raster conversion is approved (`E03 §5.3.1`). Figures for printed documents SHALL be `SVG`.

**5.6.3** Figures SHALL center within the `170 mm` text block, SHALL NOT exceed it, and SHALL NOT split across pages. Two images in one figure SHALL sit side by side at equal width with an `8 mm` gutter (`B04 §5.1.3`). They SHALL carry sub-labels `(a)` and `(b)` from their alternative text and one caption from a `Figure:` line.

**5.6.4** Diagrams SHALL follow `B05 §5.2.1`. Nodes SHALL use a `1.5 px` **Text Muted** outline and a `4 px` radius on **Pure White**. One emphasized node MAY use a **Deep Navy** fill with **Pure White** text. Connectors SHALL be `1.5 px` **Deep Navy** straight or right-angle lines with solid arrowheads. Labels SHALL use the Text Typeface at `9 pt` minimum. Diagrams SHALL use only `B02` colors and SHALL be vector `SVG`.

**5.6.5** Data charts SHALL follow `B05 §5.2.2`–`§5.2.3` and SHALL be embedded as vector `SVG`.

### 5.7 References & Cross-References
**5.7.1** Footnote markers SHALL render as superscript numerals in **Brand Blue**, numbered in sequence through the document. Footnote text SHALL render at the foot of the same page in the Text Typeface at `9 pt` in **Text Muted**, below a `30 mm` **Border Default** rule.

**5.7.2** Cross-references SHALL render the current label of their target (`Section 2.1`, `Table 3`, `Figure 2`) and, where requested, its page number. A cross-reference to a missing target SHALL cause an Export Block.

**5.7.3** A References section SHALL list citations as a numbered list with an `8 mm` hanging indent. Entries SHALL follow `C04 §5.5.1`–`§5.5.4`.

### 5.8 Document Parts & Order
**5.8.1** Formal documents SHALL present their parts in the order below. Parts marked optional MAY be omitted:
1. Cover (`E01 §5.1`).
2. Distribution list (optional).
3. Contents.
4. List of Tables and List of Figures (optional).
5. Summary box (optional, `5.5.4`).
6. Body.
7. Appendices (optional).
8. Glossary (optional).
9. References (optional).
10. Revision History (`E02 §5.1.3`).
11. Back page (optional).

**5.8.2** The Contents SHALL list Heading 1 and Heading 2 entries, appendices, and back-matter sections with their numbers and page numbers, generated from the layout. Lists of Tables and Figures SHALL list each label, caption, and page number.

**5.8.3** Each appendix SHALL start a new page and be lettered in sequence (`Appendix A`). Its headings SHALL be numbered `A.1`, `A.1.1`. Its tables and figures SHALL be numbered `Table A1` and `Figure A1`.

**5.8.4** Glossary terms SHALL be a definition list in alphabetical order. Acronyms SHALL follow `C01 §5.3.3`.

**5.8.5** A distribution list SHALL be a table with the columns `Name`, `Role`, and `Organization`, captioned as Clause `5.4.1` requires.

**5.8.6** A back page SHALL carry the Parent-Endorsed Lockup and the notice `© [YYYY] Irvantri Standards Pte. Ltd. All rights reserved.` (`A03 §5.6.1`, `E01 §5.2.2`).

**5.8.7** Where a document is set for two-sided print, each Heading 1 and appendix SHALL start on a right-hand page. An inserted empty page SHALL display `This page is intentionally left blank.` centered in the Text Typeface at `10 pt` in **Text Muted**, with the running header and footer kept.

### 5.9 Page Furniture & PDF Structure
**5.9.1** The running header MAY display the current Heading 1 text at `8 pt` in **Text Muted** within the `E01 §5.2` header region.

**5.9.2** Digital and press `PDF` exports SHALL contain bookmarks for Headings 1–3 and appendices. They SHALL set the document title and author properties from the cover title and Owner fields and the language to `en-US` (`C01 §5.6.1`). Where the browser does not write these, `tools/pdf_finish.py` SHALL add them to the digital `PDF` before distribution; `tools/press_export.py` sets them on the press file.

**5.9.3** An `HTML` Authoring Master SHALL list every active Export Block in an Accessible Rich Internet Applications (`ARIA`) Live Region (`D04 §5.3.2`), each naming the element and the fix (`E01 §5.5.5`).

## 6. Conformance & Verification

A formal document body or `HTML` Authoring Master conforms to `E05` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `E05-C1` | Body syntax follows Table 1 (`5.1.1`), every element renders from `AST-D01-01` tokens (`5.1.2`), excluded features are absent and raw `HTML` renders as text (`5.1.3`), and paste conversion keeps structure, drops styling, and replaces remote images (`5.1.4`). | Template & paste test |
| `E05-C2` | Body text, paragraph spacing, and widow and orphan control (`5.2.1`), heading values (`5.2.2`), numbering and keep-with-next (`5.2.3`), and inline styles with live links (`5.2.4`) match. | Rendered `PDF` measurement |
| `E05-C3` | Lists stop at three levels (`5.3.1`) and use the specified markers, numerals, checkboxes, and definition indent (`5.3.2`–`5.3.5`). | Rendered `PDF` measurement |
| `E05-C4` | Tables carry sequential captions (`5.4.1`), specified text and rules (`5.4.2`), aligned numeric columns with units (`5.4.3`), repeated headers and unsplit rows (`5.4.4`), blank-cell blocking (`5.4.5`), source lines (`5.4.6`), Totals Rows (`5.4.7`), and landscape handling (`5.4.8`). | Rendered `PDF` & block test |
| `E05-C5` | Code blocks (`5.5.1`), quotations (`5.5.2`), callouts with text labels (`5.5.3`), summary box (`5.5.4`), note and example blocks (`5.5.5`), requirement clauses (`5.5.6`), Sign-Off Blocks (`5.5.7`), and rules (`5.5.8`) match. | Rendered `PDF` measurement |
| `E05-C6` | Figures carry captions and alternative text (`5.6.1`), are embedded at `300` pixels per inch with raster images blocked from press export (`5.6.2`), follow placement rules (`5.6.3`), and diagrams and charts follow `B05` and the specified styles (`5.6.4`, `5.6.5`). | Figure audit & block test |
| `E05-C7` | Footnotes (`5.7.1`), cross-references with missing-target blocking (`5.7.2`), and References entries (`5.7.3`) match. | Rendered `PDF` & block test |
| `E05-C8` | Parts follow the required order (`5.8.1`) with generated contents and lists (`5.8.2`), appendix numbering (`5.8.3`), glossary order (`5.8.4`), distribution list (`5.8.5`), back page (`5.8.6`), and two-sided handling (`5.8.7`). | Document structure audit |
| `E05-C9` | Running header section text, if used, fits the `E01` header region (`5.9.1`); `PDF` exports carry bookmarks, title, author, and `en-US` language (`5.9.2`); and Export Blocks are announced in a Live Region (`5.9.3`). | `PDF` metadata & accessibility audit |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with `A04`.

## 7. Linked Artifacts

None. `TPL-E01-06` renders its body to this standard and is registered under `E01` (`E01 §5.5.11`).

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v2.0.0` | `2026-11-28` | Major | Aligned document strokes, markers, rules, and diagram node outlines (`5.2.4`, `5.3.2`, `5.3.4`, `5.4.7`, `5.5.7`, `5.6.4`) to **Text Muted** (`B02 v2.0.0 §5.2.2`), renamed the Section 3 library reference to `Standards Design`, and raised the `Library-Index.md` reference floor to `v2.0.0` per `REC-A04-016`. | Hary Irfantri |
| `v1.0.0` | `2026-11-28` | Major | Initial approved release. Set `{landscape}` tables to rotate on a portrait page (`5.4.8`), raster figures to digital-only with a press Export Block (`5.6.2`), dropped `{wide}` figures and added `Figure:` caption lines (`5.6.3`, Table 1), named `tools/pdf_finish.py` for bookmarks and document properties (`5.9.2`), and fixed callout and list text at the body size (`5.1.2`). Pre-Release Gate `REC-A04-015`. | Hary Irfantri |
| `v0.1.0` | `2026-11-28` | Pre-Release | Initial draft establishing the body element catalogue, Markdown syntax, paste conversion, text, heading, list, table, code, quotation, callout, block, figure, diagram, reference, document-part, and `PDF` structure rules for formal documents rendered by `HTML` Authoring Masters. | Hary Irfantri |
