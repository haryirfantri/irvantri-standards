# B03 — Typography

| Field | Value |
| :--- | :--- |
| **Code** | `B03` |
| **Version** | `v2.0.0` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-26` |
| **Next Review** | `2027-05-26` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `None` |

## 1. Purpose

This standard defines the official brand typefaces, font licensing and fallback rules, digital and print typographic hierarchies, line-height and measure guidelines, and tabular numeral rules for **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`). It ensures consistent typographic hierarchy, legibility, and compliance across all digital interfaces, formal documents, and publications.

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* All digital user interfaces, design tokens, themes, and web properties (`D01`–`D05`).
* All formal documents, covers, headers, footers, presentation masters, and compiled publications (`E01`–`E04`, `PUB-`).
* All lockup typography and Endorsement Line legibility thresholds referenced in `B01` and `A03`.

### 2.2 Out of Scope
This standard does not govern:
* Brand color palette Hexadecimal (`HEX`) values or contrast ratios (governed by `B02`, which this standard pairs with).
* Semantic Cascading Style Sheets (`CSS`) typography token names or code packaging (governed by `D01`).
* User Interface (`UI`) microcopy phrasing, sentence case rules, or button length targets (governed by `C03`).

## 3. Normative References

The following documents are referenced in this standard. For undated references, the latest approved edition applies.
* `A02` — Taxonomy, Coding & File Naming.
* `A03` — Entity & Brand Architecture.
* `A04` — Compliance, Reviews & Exceptions.
* `B01` — Marks & Lockups.
* `B02` — Color System.
* `C02` — Terminology & Controlled Vocabulary.
* `C03` — Technical & User Experience (`UX`) Writing.
* `C04` — Data, Dates & Citation Formatting.
* `D01` — Design Tokens & Architecture.
* `D02` — Responsive Shells & Navigation.
* `D03` — Interface Components & Patterns.
* `D04` — Accessibility & Usability.
* `D05` — Generated Outputs & Exports.
* `E01` — Formal Document Layout.
* `E02` — Versioning & Draft Marking.
* `E03` — Print & Production Specifications.
* `E04` — Correspondence & Presentations.

## 4. Terms & Definitions

For terms shared across the library, refer to `C02` and `C04`. For the purposes of this standard, the following definitions apply:
* **Display Typeface:** The primary typeface assigned to headings, cover titles, section headers, and institutional display roles (`Noto Sans Display`).
* **Fallback Stack:** An ordered list of backup typefaces used when a primary web or system font fails to load or is unavailable.
* **Line Height:** The vertical distance between consecutive baselines of text, expressed as a unitless multiplier of font size or a measured length (`C04 §5.3.2`).
* **Measure:** The horizontal character or column width of a text block, governing comfortable reading flow.
* **Text Typeface:** The primary typeface assigned to body prose, tables, forms, and technical documentation (`Noto Sans`).

## 5. Requirements

### 5.1 Official Typefaces, Licensing & Fallback Stacks
**5.1.1** Controlled documents, digital interfaces (`D01`), and publications (`PUB-`) SHALL use `Noto Sans Display` as the Display Typeface and `Noto Sans` as the Text Typeface.

**5.1.2** Monospace code blocks, file paths, identifiers, and technical tokens (`A02 §5.4`, `C03 §5.5.4`) SHALL use `Noto Sans Mono`. Approved fallbacks are `Liberation Mono`, `DejaVu Sans Mono`, and system monospace.

**5.1.3** Every font family deployed in digital products (`D01`), templates (`TPL-`), or print production (`E03`) SHALL hold a valid license permitting its intended distribution and embedding scope. Third-party font packages stored internally SHALL be logged in `06_Dependencies/Dependencies-Manifest.md` (`A02 §5.5.4`).

**5.1.4** Digital implementations (`D01`) SHALL define explicit Fallback Stacks after `Noto Sans Display` and `Noto Sans` using standard sans-serif families (`-apple-system, BlinkMacSystemFont, Segoe UI, Liberation Sans, Arial, sans-serif`).

### 5.2 Type Hierarchy, Line Height & Measure
**5.2.1** Digital interfaces (`D01`–`D03`) and formal documents (`E01`) SHALL maintain a clear visual hierarchy distinguishing display headings (`Noto Sans Display`) from body text (`Noto Sans`).

**5.2.2** Body prose SHALL use a minimum font size of `14 px` (`10.5 pt`) for standard interface copy. Long-form documentation SHALL use at least `16 px` (`12 pt`) (`C04 §5.3.2`).

**5.2.3** Line height for body prose SHOULD be between `1.4` and `1.6` times font size, and heading line height SHOULD be between `1.15` and `1.3` times font size (`C04 §5.2.3`).

**5.2.4** Long-form body prose columns in digital interfaces and formal documents SHOULD maintain a comfortable measure between `50` and `85` characters per line (`C04 §5.2.1`).

**5.2.5** Within the Parent-Endorsed Lockup (`B01 §5.2.2`), the Endorsement Line SHALL maintain a minimum cap height of `6 pt` in print or `9 px` on screen (`B01 §5.3.3`, `C04 §5.3.2`).

**5.2.6** Digital interfaces (`D01`–`D03`) SHOULD apply the role-based typographic hierarchy below, aligning Key Performance Indicator (`KPI`) readouts and data tables to Tabular Numerals (`5.3.1`):

| Role | Typeface | Desktop / Mobile Size | Weight | Tracking |
| :--- | :--- | :--- | :--- | :--- |
| **Page Title** | `Noto Sans Display` | `32 px` / `24 px` | `800` | `-0.03em` |
| **Metric / KPI Value** | `Noto Sans Display` | `28 px` / `24 px` | `700`–`800` | `-0.04em` |
| **Section Title** | `Noto Sans Display` | `20 px` / `18 px` | `700`–`800` | `-0.03em` |
| **Panel Title** | `Noto Sans Display` | `16 px` / `16 px` | `700` | `-0.02em` |
| **Body Copy** | `Noto Sans` | `14 px`–`16 px` (`5.2.2`) | `400`–`500` | `0` |
| **Forms & Tables** | `Noto Sans` | `14 px` (`5.2.2`) | `500`–`700` | `0` |
| **Eyebrow / Overline** | `Noto Sans` | `12 px` | `700`–`800` | `+0.12em` |

**5.2.7** Uppercase letter styling SHOULD be restricted to short labels, navigation eyebrows, table headers, and brand wordmarks rather than multi-sentence prose.

### 5.3 Tabular Numerals & Numeric Alignment
**5.3.1** Multi-row tables, financial schedules, version registers, and numeric readouts (`C04 §5.4.2`) SHALL use Tabular Numerals (`tabular-nums`) or monospaced alignment so digits align vertically across rows.

**5.3.2** Mixed-case or all-caps labels SHALL NOT substitute for tabular numeral alignment in numeric data columns (`C04 §5.4.2`).

### 5.4 Typographic Misuse & Accessibility
**5.4.1** Authors and designers SHALL NOT apply decorative script fonts, novelty display typefaces, or unapproved font substitutions in controlled deliverables (`D01`, `E01`, `E04`).

**5.4.2** Text sizing and scaling SHALL support Web Content Accessibility Guidelines (`WCAG`) 2.2 Level AA readability (`B02 §5.5.1`, `D04`). Implementations SHALL NOT clip text or lock zoom against user resizing.

## 6. Conformance & Verification

A digital interface, document, template, or publication conforms to `B03` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `B03-C1` | Deliverable uses `Noto Sans Display` for display roles, `Noto Sans` for body/`UI` roles (`5.1.1`), and `Noto Sans Mono` or approved monospace fallbacks for code/identifiers (`5.1.2`). | Font & stylesheet audit |
| `B03-C2` | Deployed fonts hold valid licenses for their scope, log internal packages in `Dependencies-Manifest.md` (`5.1.3`), and include sans-serif fallback stacks (`5.1.4`). | License, manifest & `CSS` inspection |
| `B03-C3` | Display and body hierarchy is distinct (`5.2.1`), body text meets `14 px` / `16 px` minimums (`5.2.2`), and Parent-Endorsed Lockup Endorsement Line meets `6 pt` / `9 px` minimum cap height (`5.2.5`). | Layout & size audit |
| `B03-C4` | Multi-row tables and numeric columns use Tabular Numerals or monospaced digit alignment (`5.3.1`–`5.3.2`). | Table & token inspection |
| `B03-C5` | Zero unapproved typefaces appear (`5.4.1`), and text scales cleanly per `WCAG` 2.2 Level AA without clipping (`5.4.2`). | Visual & accessibility check |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with `A04`.

## 7. Linked Artifacts

None.

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v2.0.0` | `2026-11-26` | Major | Migrated official brand typefaces from `Montserrat`, `Inter`, and `JetBrains Mono` to the unified `SIL OFL-1.1` Noto Sans superfamily (`Noto Sans Display`, `Noto Sans`, `Noto Sans Mono`) across Clauses `5.1.1`–`5.1.4`, `5.2.1`, `5.2.6`, and `B03-C1`–`B03-C2`; aligned internal font package logging with `A02 (v1.2.0) §5.5.4` (`Dependencies-Manifest.md`); tightened Section 5 sentences below 30 words (`C01 §5.3.1`); and restored Section 3 reference parity (`A03`, `D05`, `E02`). | Hary Irfantri |
| `v1.1.0` | `2026-11-24` | Minor | Added recommended Desktop/Mobile role-based typographic hierarchy (`5.2.6`), added uppercase restraint guidance (`5.2.7`), expanded `WCAG` and `KPI` on first occurrence, and aligned Section 3 normative references. | Hary Irfantri |
| `v1.0.0` | `2026-11-22` | Major | Initial approved baseline of `B03` (Typography), locking `Montserrat` and `Inter` type roles, licensing and fallback stack rules, screen and print body size minimums, Tabular Numerals for numeric columns, and `WCAG` 2.2 Level AA typographic scaling rules. | Hary Irfantri |
| `v0.1.0` | `2026-11-22` | Pre-Release | Initial draft establishing `Montserrat` and `Inter` type roles, licensing and fallback stack rules, screen and print body size minimums, Tabular Numerals for numeric columns, and `WCAG` 2.2 Level AA typographic scaling rules. | Hary Irfantri |
