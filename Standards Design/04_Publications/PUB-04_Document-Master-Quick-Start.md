# PUB-04 — Formal Document Master Quick-Start

| Field | Value |
| :--- | :--- |
| **Code** | `PUB-04` |
| **Title** | Formal Document Master Quick-Start |
| **Entity** | Irvantri Standards (`Irvantri Standards Pte. Ltd.`) |
| **Affiliation** | A member of Irvantri Group |
| **Version** | `v1.0.0` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-28` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Governing Standards** | `C03 (v1.0.1)`, `C04 (v1.0.2)`, `E01 (v2.6.1)`, `E02 (v1.1.1)`, `E03 (v1.1.1)`, `E05 (v2.0.0)` |

---

> **Precedence Notice (`A01 §5.1.4`, `§5.7.5`):** This compiled publication (`PUB-04`) is an informative reference copy compiled on `2026-11-28` from **Standards Design**. Active normative standards prevail in the event of any conflict between this publication and an underlying standard.

---

## 1. What the Document Master Is

`03_Templates/TPL-E01-06_Formal-Document-Master.html` is one file that makes every formal document: proposals, procedures, reports and specifications. It works in any current browser with no internet connection. The cover, running header and footer, fonts and colors are locked, so every document matches the brand without design work (`E01 §5.5`). The author supplies the cover fields and the body text.

## 2. Make a Document in Six Steps

1. Open `TPL-E01-06_Formal-Document-Master.html` from the library in a browser. A blank document opens with the **How to use this template** panel; the master itself never changes, because each document is saved as a separate file.
2. Fill **Cover and metadata**. **Document title**, **Identifier**, **Version**, **Issue date**, **Owner** and **Approver** are required. A new document starts as `Draft` at `v0.1.0` (`E02 §5.1.4`).
3. Write the body in **Body** in Markdown, or paste from Word or Google Docs. Pasting keeps headings, lists, tables and images and drops fonts and colors (`E05 §5.1.4`). Open **Markdown cheat sheet** for the syntax of each element, or press **Load sample document** to see every element rendered.
4. Read **Export checks**. Each item states what to change; press its **Go to** button to jump to the field or the line in the body.
5. Press **Save filled copy**. The saved `HTML` file holds every value and image; open it in a browser to continue editing (`E01 §5.5.6`).
6. Export the document:
   * **Export A4 PDF** for screen, email and office printing. In the print dialog, choose **Save as PDF** with margins set to **None**. The Owner then runs `tools/pdf_finish.py` on the file to set its title, author and language (`E05 §5.9.2`).
   * **Export press PDF** only for an `Approved` document going to a commercial printer. Check the bleed and crop marks with **Press preview** first. The Owner converts the saved file with `tools/press_export.py`, and an Owner color proof precedes any press run (`E01 §5.3.4`, `E03 §5.4.3`).

## 3. The Five Most Common Export Blocks

The master refuses both exports while any check fails (`E01 §5.5.5`). These five are the most frequent for a new author:

Table: Common export blocks and their fixes

| Message starts with | Why it blocks | Fix |
| :--- | :--- | :--- |
| `Document title is empty` (also Identifier, Owner, Approver) | Cover metadata has no blank required fields (`E01 §5.1.3`). | Fill the named field. |
| `The newest revision history row is …` | The first Revision History row records the current version (`E02 §5.1.3`). | Add a row for the version at the top of **Revision history**, or correct **Version**. |
| `Table N has no caption` or `… the cell is blank` | Tables carry captions and no blank cells (`E05 §5.4.1`, `§5.4.5`). | Add a `Table: caption` line above the table; enter `None` or `—` in empty cells. |
| `Figure N has no alternative text` or `… is not in Images` | Figures are described and stored inside the file, which works offline (`E05 §5.6.1`, `E01 §5.5.8`). | Describe the image inside `![...]`; add the file with **Add image** and refer to it by name. |
| `Press files need Approved status` or `… is a raster image` | Press files are for Approved documents and accept vector figures only (`E03 §5.3.1`, `§5.4.2`). | Use **Export A4 PDF** for drafts; replace photos and screenshots with `SVG` figures for press. |

## 4. Where the Rules Live

* Body elements and their styles: `E05` Document Body Elements.
* Cover, header, footer and the master's behavior: `E01 §5.1`, `§5.2` and `§5.5`.
* Status, version and banners: `E02`.
* Print specification: `E03`.

## 5. Publication Build Manifest & Revision History (`A01 §5.7.5`, `E02 §5.1.3`)

### 5.1 Source Manifest (`A01 §5.7.5`)

| Source | Version |
| :--- | :--- |
| `C03` | `v1.0.1` |
| `C04` | `v1.0.2` |
| `E01` | `v2.6.1` |
| `E02` | `v1.1.1` |
| `E03` | `v1.1.1` |
| `E05` | `v2.0.0` |
| `TPL-E01-06` | `E01 (v2.6)` |
| `Library-Index.md` | `v2.0.1` |

### 5.2 Revision History (`E02 §5.1.3`)

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v1.0.0` | `2026-11-28` | Major | Initial approved quick-start for `TPL-E01-06` authors: six-step workflow and the five most common export blocks. | Hary Irfantri |
