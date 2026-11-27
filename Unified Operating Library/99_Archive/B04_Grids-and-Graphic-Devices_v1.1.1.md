# B04 — Grids, Spacing & Graphic Devices

| Field | Value |
| :--- | :--- |
| **Code** | `B04` |
| **Version** | `v1.1.1` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-25` |
| **Next Review** | `2027-05-22` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `None` |

## 1. Purpose

This standard defines the spatial grid foundations, spacing scale increments, corner radius conventions, and signature graphic accent devices for **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`). It establishes consistent layout geometry, proportion, and visual rhythm across digital interfaces, formal documents, and publications.

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* All digital user interfaces, layout grids, spacing tokens, and component containers (`D01`–`D05`).
* All formal document covers, metadata panels, running headers and footers, presentation masters, and compiled publications (`E01`–`E04`, `PUB-`).
* All signature visual accent bars, divider rules, and container corner radii used in brand deliverables.

### 2.2 Out of Scope
This standard does not govern:
* Brand mark geometry, clear space around marks, or co-branding divider spacing (governed by `B01`).
* Color palette values, contrast ratios, or status color semantics (governed by `B02`).
* Brand typefaces, font sizes, line heights, or tabular numeral alignment (governed by `B03`).
* Responsive screen breakpoints or navigation shell architecture (governed by `D02`).

## 3. Normative References

The following documents are referenced in this standard. For undated references, the latest approved edition applies.
* `A04` — Compliance, Reviews & Exceptions.
* `B01` — Marks & Lockups.
* `B02` — Color System.
* `B03` — Typography.
* `C02` — Terminology & Controlled Vocabulary.
* `C04` — Data, Dates & Citation Formatting.
* `D01` — Design Tokens & Architecture.
* `D02` — Responsive Shells & Navigation.
* `D03` — Interface Components & Patterns.
* `D04` — Accessibility & Usability.
* `E01` — Formal Document Layout.
* `E03` — Print & Production Specifications.

## 4. Terms & Definitions

For terms shared across the library, refer to `C02` and `C04`. For the purposes of this standard, the following definitions apply:
* **Base Unit:** The fundamental spatial increment (`4 px` in digital interfaces; `4 mm` in formal print layouts) from which spacing scales and layout geometry derive.
* **Corner Radius:** The circular arc curvature applied to container, card, button, or badge edges.
* **Graphic Device:** A recurring geometric brand element—such as a hairline rule, accent bar, or structured band—used to organize hierarchy and reinforce visual identity.
* **Gutter:** The fixed spacing channel separating adjacent columns or grid tracks in a layout.
* **Layout Grid:** A structured system of columns, rows, gutters, and margins that aligns visual and typographic elements.

## 5. Requirements

### 5.1 Spatial Grid & Spacing Scale
**5.1.1** Digital user interfaces (`D01`–`D03`) SHALL use a `4 px` Base Unit spatial grid (`C04 §5.3.2`). Spacing values SHALL align to `4 px` multiples (`4`, `8`, `12`, `16`, `24`, `32`, `48`, and `64 px`).

**5.1.2** Formal print documents (`E01`, `E03`) SHALL align structural margins, section gaps, and layout grids to a `4 mm` Base Unit (`8`, `12`, `16`, `20`, and `24 mm`) (`C04 §5.3.2`).

**5.1.3** Multi-column layout grids in web interfaces (`D02`) and formal publications (`E01`, `PUB-`) SHALL maintain consistent gutters across sibling columns within each container.

**5.1.4** Interactive targets (`D03`, `D04`) SHALL provide a `44 px × 44 px` hit area or meet Web Content Accessibility Guidelines (`WCAG`) 2.2 Level AA target-size criteria (`B02 §5.5.1`).

**5.1.5** Adjacent interactive touch targets on Compact viewports (`D02 §5.1.1`) SHALL maintain a minimum separation of `12 px` (`C04 §5.3.2`).

### 5.2 Corner Radii & Structural Containers
**5.2.1** Corner radii in digital interfaces (`D01`, `D03`) and formal document boxes (`E01`) SHALL use four restrained increments (`C04 §5.3.2`). Permitted values are `0 px` (architectural corners), `4 px` (compact controls and tags), `8 px` (cards and panels), and `12 px` (feature containers).

**5.2.2** Decorative rounded pills, excessive border rounding that distorts rectangular panels, and ad-hoc corner radii outside Clause `5.2.1` SHALL NOT be used in controlled templates (`TPL-`) or standard layouts.

**5.2.3** Digital cards and primary action buttons MAY apply subtle neutral elevation shadows aligned to `B02 §5.4.4` without heavy blur radii or decorative glow effects.

### 5.3 Signature Graphic Devices & Accent Rules
**5.3.1** Formal document covers (`E01`) MAY use a horizontal split accent bar composed of `24%` **Signal Red** (`#DE0029`) and `76%` **Deep Navy** (`#092B55`) (`B02 §5.1.1`, `C04 §5.2.3`).

**5.3.2** Section dividers, metadata rules, and accent bars SHALL use straight geometric lines aligned to the active layout grid (`B04 §5.1.1`–`§5.1.2`). They SHALL NOT use wavy rules, drop shadows, or unapproved color fills (`B02 §5.4.2`–`§5.4.3`).

**5.3.3** Graphic devices SHALL support content hierarchy and readability and SHALL NOT crowd text, obstruct lockup Clear Space (`B01 §5.3.1`), or compete with primary headings (`B03 §5.2.1`).

**5.3.4** Decorative rings, wave textures, and ornamental brand motifs SHALL NOT appear inside dense operational work surfaces, forms, or data tables (`D03`).

## 6. Conformance & Verification

A layout, template, interface, or publication conforms to `B04` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `B04-C1` | Digital layouts use a `4 px` Base Unit spacing scale (`5.1.1`), print layouts align to a `4 mm` Base Unit (`5.1.2`), and sibling columns keep uniform gutters (`5.1.3`). | Grid & spacing audit |
| `B04-C2` | Interactive targets meet the `44 px × 44 px` minimum or `WCAG` 2.2 Level AA target size (`5.1.4`) and maintain at least `12 px` separation on Compact viewports (`5.1.5`). | Accessibility & layout check |
| `B04-C3` | Corner radii follow `0 px`, `4 px`, `8 px`, or `12 px` (`5.2.1`), with zero unapproved radii or decorative rounding (`5.2.2`). | Token & visual inspection |
| `B04-C4` | Graphic devices and accent bars use straight geometric lines (`5.3.2`), preserve text readability and `B01` Clear Space (`5.3.3`), and omit decorative graphics on dense work surfaces (`5.3.4`). | Layout & geometry audit |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with `A04`.

## 7. Linked Artifacts

None.

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v1.1.1` | `2026-11-25` | Errata | Tightened or split 30+ word sentences in `5.1.1`–`5.1.2`, `5.1.4`, `5.2.1`, and `5.3.2` and confirmed `D02 (v2.0.0)` and `D03 (v2.0.0)` alignment per `REC-A04-005` (`F-10`). | Hary Irfantri |
| `v1.1.0` | `2026-11-24` | Minor | Added `12 px` minimum touch-target separation on Compact viewports (`5.1.5`), permitted subtle neutral elevation on cards and primary buttons (`5.2.3`), prohibited decorative motifs on dense operational work surfaces (`5.3.4`), updated `B04-C2` and `B04-C4`, and aligned Section 3 normative references. | Hary Irfantri |
| `v1.0.0` | `2026-11-22` | Major | Initial approved baseline of `B04` (Grids, Spacing & Graphic Devices), locking the `4 px` digital and `4 mm` print spacing scales, `44 px × 44 px` target-size floor, `0 px`–`12 px` corner radii, and signature graphic device rules. | Hary Irfantri |
| `v0.1.0` | `2026-11-22` | Pre-Release | Initial draft establishing the `4 px` digital and `4 mm` print spacing scales, `44 px × 44 px` target-size floor, `0 px`–`12 px` corner radii, and signature graphic device rules. | Hary Irfantri |
