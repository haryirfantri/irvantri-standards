# B01 — Marks & Lockups

| Field | Value |
| :--- | :--- |
| **Code** | `B01` |
| **Version** | `v2.0.1` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-27` |
| **Next Review** | `2027-05-22` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `AST-B01-01`, `AST-B01-02`, `AST-B01-03`, `AST-B01-04`, `AST-B01-05`, `AST-B01-06`, `AST-B01-07`, `AST-B01-08`, `AST-B01-09`, `AST-B01-10`, `AST-B01-11`, `AST-B01-12`, `AST-B01-13`, `AST-B01-14`, `AST-B01-15`, `AST-B01-16` |

## 1. Purpose

This standard defines the official brand marks, approved lockup configurations, clear-space rules, minimum reproduction sizes, colorway variants, co-branding layouts, and misuse prohibitions for **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`). It ensures consistent, legible, and authoritative visual identification across digital interfaces, formal documents, and print materials.

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* All official brand symbols, wordmarks, and parent-endorsed lockups representing **Irvantri Standards** (`A03 §5.2.1`).
* All Master Assets (`AST-B01`) registered in `Library-Index.md` and deployed across digital systems (`D01`–`D05`), formal documents (`E01`–`E04`), and compiled publications (`PUB-`).
* All `Tier 3` Endorsed Sub-Brand lockups (`A03 §5.1.5`) and `Tier 4` Co-Branded mark pairings (`A03 §5.5.3`).

### 2.2 Out of Scope
This standard does not govern:
* Brand color palette definitions and contrast ratios (governed by `B02`).
* Brand typeface licensing, type scales, and fallback stacks (governed by `B03`).
* User Interface (`UI`) icons, technical diagrams, and data visualizations (governed by `B05`).
* Corporate entity hierarchy and textual attribution rules (governed by `A03`, which this standard implements visually).
* Normative document anatomy and lifecycle rules (governed by `A01`).

## 3. Normative References

The following documents are referenced in this standard. For undated references, the latest approved edition applies.
* `Library-Index.md` — Irvantri Standards Unified Operating Library Index (`v1.1.26` or later).
* `A01` — Document Control & Lifecycle.
* `A02` — Taxonomy, Coding & File Naming.
* `A03` — Entity & Brand Architecture.
* `A04` — Compliance, Reviews & Exceptions.
* `B02` — Color System.
* `B03` — Typography.
* `B05` — Iconography, Diagrams & Visuals.
* `C02` — Terminology & Controlled Vocabulary.
* `C04` — Data, Dates & Citation Formatting.
* `D01` — Design Tokens & Architecture.
* `D02` — Responsive Shells & Navigation.
* `D04` — Accessibility & Usability.
* `E01` — Formal Document Layout.
* `E03` — Print & Production Specifications.
* `E04` — Correspondence & Presentations.

## 4. Terms & Definitions

For terms shared across the library, refer to `C02` and `A03`. For the purposes of this standard, the following definitions apply:
* **Clear Space:** The mandatory minimum unobstructed margin surrounding a symbol or lockup, measured relative to the width of the primary symbol.
* **Lockup:** A fixed geometric arrangement combining the primary symbol with the Master Brand wordmark and, where required, the Endorsement Line.
* **Optical Parity:** Visual equivalence in perceived weight, height, and area between two paired marks in a co-branded layout.
* **Primary Symbol:** The standalone geometric emblem representing Irvantri Standards without accompanying typography.
* **Reversed Mark:** A single-color white (`#FFFFFF`) rendering of the symbol or lockup designed for dark backgrounds.

## 5. Requirements

### 5.1 Official Marks & Master Asset Governance
**5.1.1** All visual brand expressions of Irvantri Standards SHALL use only the official marks defined in this standard:
* **Primary Symbol:** Standalone geometric emblem in full-color or approved monochrome rendering.
* **Primary Master Lockup:** Symbol paired with the uppercase wordmark `IRVANTRI STANDARDS`.
* **Parent-Endorsed Lockup:** Primary Master Lockup paired with the stacked Endorsement Line `A member of Irvantri Group`.

**5.1.2** Digital implementations (`D01`) SHALL source marks from master Scalable Vector Graphics (`SVG`) files or lossless Portable Network Graphics (`PNG`) derivatives exported directly from those `SVG` masters. Print deliverables (`E03`) SHALL use vector masters (`SVG` or Portable Document Format (`PDF`)).

**5.1.3** Every approved master mark file SHALL be registered as an `AST-B01` Master Asset in `Library-Index.md` and Section 7 of this standard, pinned to `B01 (vMAJOR.MINOR)` (`A01 §5.7.4`, `A02 §5.7.2`).

### 5.2 Lockup Selection & Architectural Alignment
**5.2.1** Lockup selection across deliverables and interfaces SHALL follow the architectural rules in `A03 §5.1`–`§5.3`:

| Lockup Variant | Required Touchpoints | Governing Authority |
| :--- | :--- | :--- |
| **Parent-Endorsed Lockup** | Formal document covers (`E01`), compiled publications (`PUB-`), corporate website footers and legal pages (`D02`), and official correspondence or presentation cover/closing slides (`E04`) | `A03 §5.3.3` |
| **Primary Master Lockup** | Product headers, web navigation bars, technical documentation headers, and institutional touchpoints where the Endorsement Line is omitted | `A03 §5.2.2`, `§5.3.4` |
| **Primary Symbol** | Compact navigation headers, application tiles, avatars, watermarks, and constrained spaces below wordmark minimum width | `A03 §5.3.4`, `B01 §5.3.2` |

**5.2.2** In the Parent-Endorsed Lockup, the Endorsement Line SHALL appear verbatim as `A member of Irvantri Group` (`A03 §5.3.1`–`§5.3.2`).

**5.2.3** The Parent-Endorsed Lockup SHOULD NOT be placed in compact navigation bars (`D02`) or constrained containers where the Endorsement Line renders below minimum legible type size (`A03 §5.3.4`, `B03`).

**5.2.4** Every approved `Tier 3` Endorsed Sub-Brand lockup (`A03 §5.1.5`, `C02 §5.3.1`) SHALL display the `Irvantri Standards` Master Brand wordmark or lockup in its primary header or cover.

**5.2.5** Standalone placement of an `Irvantri Group` mark (`Tier 0`) on Irvantri Standards materials SHALL require prior written Approver authorization (`A03 §5.3.5`).

### 5.3 Clear Space & Minimum Dimensions
**5.3.1** Every Primary Symbol and Lockup SHALL maintain a minimum Clear Space equal to `0.25×` the width of the Primary Symbol (`w`) on all four sides (`C04 §5.2.3`). Text, borders, rules, and external graphics SHALL NOT enter this exclusion zone.

**5.3.2** Marks SHALL NOT be reproduced below the following minimum dimensions (`C04 §5.3.2`):

| Mark Variant | Digital Minimum (`UI` / Web) | Print Minimum (`E03`) |
| :--- | :--- | :--- |
| **Primary Symbol** | `28 px × 28 px` | `12 mm × 12 mm` |
| **Primary Master Lockup** | `140 px` width (`28 px` symbol height) | `38 mm` width (`12 mm` symbol height) |
| **Parent-Endorsed Lockup** | `260 px` width (`62.7 px` symbol height) | `64 mm` width (`15.4 mm` symbol height) |

> **Informative Note:** Favicons and compact `16 px` system icons (`B05`) use simplified icon derivatives rather than the full Primary Symbol when rendered below `28 px`. The `260 px` and `64 mm` Parent-Endorsed Lockup floors align to the locked `4.15:1` (`664 × 160`) master geometry (`AST-B01-03` and `AST-B01-04`) so the Endorsement Line stays above the `9 px` / `6 pt` cap-height floor in Clause `5.3.3`.

**5.3.3** Within the Parent-Endorsed Lockup, the Endorsement Line cap height SHALL NOT render smaller than `6 pt` in print or `9 px` on screen (`B03`).

### 5.4 Colorways & Background Contrast
**5.4.1** Marks SHALL use only the three authorized colorway variants defined in `B02`:
* **Full-Color Primary:** Brand blue and signal red palette applied on white (`#FFFFFF`) or approved light neutral backgrounds (`B02`).
* **Reversed White:** Solid white (`#FFFFFF`) applied on dark brand navy or dark neutral backgrounds (`B02`).
* **Monochrome Black:** Solid black (`#000000`) applied strictly to single-ink print or monochrome reproduction (`E03`).

**5.4.2** Background surfaces behind any mark SHALL maintain at least a `4.5:1` contrast ratio against the primary mark fill per Web Content Accessibility Guidelines (`WCAG`) 2.2 Level AA (`B02`, `D04`).

**5.4.3** Marks SHALL NOT be placed directly over complex photography, textured patterns, or multi-hue gradients unless backed by an approved solid or translucent scrim meeting Clause `5.4.2` (`B02`).

### 5.5 Co-Branding & Partner Lockups
**5.5.1** In `Tier 4` equal-partnership Co-Branded lockups (`A03 §5.5.3`), the Irvantri Standards mark SHALL be sized at Optical Parity with the partner mark.

**5.5.2** Co-Branded lockups SHALL separate the Irvantri Standards and partner marks with a `1 px` vertical divider rule centered inside a minimum `1.0×` Primary Symbol width (`w`) gap.

**5.5.3** Co-Branded lockups SHALL NOT be published without a written co-branding agreement signed by the Approver (`A03 §5.5.3`) and documented rights-holder permission (`A03 §5.5.4`).

### 5.6 Prohibited Mark Misuse
**5.6.1** Authors, designers, and developers SHALL NOT alter or distort any official mark. Prohibited modifications include:
* Stretching, skewing, rotating, or altering the locked aspect ratio.
* Substituting unapproved colors, applying gradients, or adding drop shadows, outlines, or glow effects.
* Rearranging, resizing, or replacing the typography of the symbol, wordmark, or Endorsement Line.
* Cropping, clipping, or enclosing the symbol inside unapproved badges or frames.
* Recreating or redrawing the symbol instead of using registered `AST-B01` master files.

## 6. Conformance & Verification

A mark asset, digital interface, publication, or formal document conforms to `B01` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `B01-C1` | Deliverable uses only official marks (`5.1.1`) sourced from registered `AST-B01` vector/lossless masters (`5.1.2`–`5.1.3`). | Asset & register audit |
| `B01-C2` | Lockup variant matches the required touchpoint tier (`5.2.1`), reproduces `A member of Irvantri Group` verbatim (`5.2.2`), displays Master Brand attribution on `Tier 3` lockups (`5.2.4`), and holds Approver sign-off for any `Tier 0` mark (`5.2.5`). | Layout & record inspection |
| `B01-C3` | Clear Space of at least `0.25×` Primary Symbol width (`w`) is unobstructed on all four sides (`5.3.1`). | Geometry measurement |
| `B01-C4` | Reproduced marks meet minimum digital (`28 px` symbol, `140 px` Primary Master Lockup, `260 px` Parent-Endorsed Lockup) and print (`12 mm` symbol, `38 mm` Primary Master Lockup, `64 mm` Parent-Endorsed Lockup) dimensions (`5.3.2`), with Endorsement Line cap height at least `6 pt` / `9 px` (`5.3.3`). | Dimension & type check |
| `B01-C5` | Mark uses an authorized colorway (`5.4.1`), maintains at least `4.5:1` background contrast (`5.4.2`), and avoids unscreened complex imagery (`5.4.3`). | Color & contrast audit |
| `B01-C6` | `Tier 4` Co-Branded lockups maintain Optical Parity (`5.5.1`), `1.0×` symbol-width divider spacing (`5.5.2`), and signed Approver/rights-holder authorization (`5.5.3`). | Co-branding & record audit |
| `B01-C7` | Reproduced marks exhibit zero stretching, rotation, unapproved effects, typography alterations, cropping, or redrawing (`5.6.1`). | Visual inspection |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with `A04`.

## 7. Linked Artifacts

| Code | Artifact | File | Pinned Version | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `AST-B01-01` | Primary Symbol (`SVG`) | `02_Assets/AST-B01-01_Primary-Symbol.svg` | `B01 (v2.0)` | `Approved` | Full-color primary emblem master (`28 px` / `12 mm` minimum) |
| `AST-B01-02` | Reversed White Symbol (`SVG`) | `02_Assets/AST-B01-02_White-Symbol.svg` | `B01 (v2.0)` | `Approved` | Single-color `#FFFFFF` symbol master for dark surfaces |
| `AST-B01-03` | Parent-Endorsed Lockup (`SVG`) | `02_Assets/AST-B01-03_Parent-Lockup.svg` | `B01 (v2.0)` | `Approved` | Full-color `664 × 160` (`4.15:1`) symbol, `IRVANTRI STANDARDS` wordmark, and `A member of Irvantri Group` endorsement for light surfaces (`260 px` / `64 mm` minimum) |
| `AST-B01-04` | Reversed White Parent-Endorsed Lockup (`SVG`) | `02_Assets/AST-B01-04_Parent-Lockup-White.svg` | `B01 (v2.0)` | `Approved` | Reversed `#FFFFFF` `664 × 160` (`4.15:1`) Parent-Endorsed Lockup for dark surfaces (`260 px` / `64 mm` minimum) |
| `AST-B01-05` | Primary Master Lockup (`SVG`) | `02_Assets/AST-B01-05_Primary-Lockup.svg` | `B01 (v2.0)` | `Approved` | Full-color `800 × 160` (`5:1`) symbol and single-line `IRVANTRI STANDARDS` wordmark without Endorsement Line for light surfaces (`140 px` / `38 mm` minimum) |
| `AST-B01-06` | Reversed White Primary Master Lockup (`SVG`) | `02_Assets/AST-B01-06_Primary-Lockup-White.svg` | `B01 (v2.0)` | `Approved` | Reversed `#FFFFFF` `800 × 160` (`5:1`) Primary Master Lockup for dark surfaces (`140 px` / `38 mm` minimum) |
| `AST-B01-07` | Monochrome Black Primary Master Lockup (`SVG`) | `02_Assets/AST-B01-07_Primary-Lockup-Black.svg` | `B01 (v2.0)` | `Approved` | Solid `#000000` `800 × 160` (`5:1`) Primary Master Lockup for single-ink print and monochrome reproduction (`140 px` / `38 mm` minimum) |
| `AST-B01-08` | Monochrome Black Symbol (`SVG`) | `02_Assets/AST-B01-08_Black-Symbol.svg` | `B01 (v2.0)` | `Approved` | Solid `#000000` symbol master for single-ink print and monochrome reproduction (`28 px` / `12 mm` minimum) |
| `AST-B01-09` | Primary Symbol (`PNG`) | `02_Assets/AST-B01-09_Primary-Symbol.png` | `B01 (v2.0)` | `Approved` | Lossless `1080 × 1080` `300 DPI` derivative exported directly from `AST-B01-01` |
| `AST-B01-10` | Reversed White Symbol (`PNG`) | `02_Assets/AST-B01-10_White-Symbol.png` | `B01 (v2.0)` | `Approved` | Lossless transparent `1080 × 1080` `300 DPI` derivative exported directly from `AST-B01-02` |
| `AST-B01-11` | Parent-Endorsed Lockup (`PNG`) | `02_Assets/AST-B01-11_Parent-Lockup.png` | `B01 (v2.0)` | `Approved` | Lossless `2656 × 640` `300 DPI` derivative exported directly from `AST-B01-03` |
| `AST-B01-12` | Reversed White Parent-Endorsed Lockup (`PNG`) | `02_Assets/AST-B01-12_Parent-Lockup-White.png` | `B01 (v2.0)` | `Approved` | Lossless transparent `2656 × 640` `300 DPI` derivative exported directly from `AST-B01-04` |
| `AST-B01-13` | Primary Master Lockup (`PNG`) | `02_Assets/AST-B01-13_Primary-Lockup.png` | `B01 (v2.0)` | `Approved` | Lossless `3200 × 640` `300 DPI` derivative exported directly from `AST-B01-05` |
| `AST-B01-14` | Reversed White Primary Master Lockup (`PNG`) | `02_Assets/AST-B01-14_Primary-Lockup-White.png` | `B01 (v2.0)` | `Approved` | Lossless transparent `3200 × 640` `300 DPI` derivative exported directly from `AST-B01-06` |
| `AST-B01-15` | Monochrome Black Primary Master Lockup (`PNG`) | `02_Assets/AST-B01-15_Primary-Lockup-Black.png` | `B01 (v2.0)` | `Approved` | Lossless `3200 × 640` `300 DPI` derivative exported directly from `AST-B01-07` |
| `AST-B01-16` | Monochrome Black Symbol (`PNG`) | `02_Assets/AST-B01-16_Black-Symbol.png` | `B01 (v2.0)` | `Approved` | Lossless `1080 × 1080` `300 DPI` derivative exported directly from `AST-B01-08` |

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v2.0.1` | `2026-11-27` | Errata | Registered and approved `AST-B01-05`–`AST-B01-07` (Primary Master Lockup in Full-Color Primary, Reversed White, and Monochrome Black colorways, `800 × 160`, `5:1`), `AST-B01-08` (Monochrome Black Symbol), and `AST-B01-09`–`AST-B01-16` (lossless `300 DPI` `PNG` derivatives of every `SVG` master per `5.1.2`) in Section 7, pinned to `B01 (v2.0)`, and updated the `Governs` header (`A01 §5.2.8`, `§5.5.7`) per `REC-A04-008`. Sections 2 through 6 are unchanged. | Hary Irfantri |
| `v2.0.0` | `2026-11-25` | Major | Resolved geometric conflict (`U-01`) between `5.3.2` and `5.3.3`/`B03 §5.2.5` by raising Parent-Endorsed Lockup minimums to `260 px` width (`62.7 px` symbol) digital and `64 mm` width (`15.4 mm` symbol) print (`B01-C4`); promoted `AST-B01-03` to `Approved`, allocated and approved `AST-B01-04` (reversed white lockup), updated `Governs` header, and re-pinned `AST-B01-01`–`AST-B01-04` to `B01 (v2.0)` per `REC-A04-006`. | Hary Irfantri |
| `v1.0.1` | `2026-11-25` | Errata | Populated `Governs` header (`AST-B01-01`, `AST-B01-02`, `AST-B01-03` per `A01 §5.2.8`), promoted `AST-B01-01` and `AST-B01-02` to `Approved` in Section 7 (`A01 §5.5.7`), removed obsolete pre-approval note and updated `Library-Index.md` floor in Section 3, tightened `5.5.2` below 30 words, and confirmed `D02 (v2.0.0)` alignment per `REC-A04-005` (`F-07`, `F-10`). | Hary Irfantri |
| `v1.0.0` | `2026-11-22` | Major | Initial approved baseline of `B01` (Marks & Lockups), locking official marks, `AST-B01` master asset governance, touchpoint lockup selection, `0.25×` Clear Space, minimum digital and print dimensions, authorized colorways, `Tier 4` co-branding spacing, and mark misuse prohibitions. | Hary Irfantri |
| `v0.1.0` | `2026-11-22` | Pre-Release | Initial draft establishing official marks, `AST-B01` master governance, touchpoint lockup selection, `0.25×` Clear Space, minimum digital and print dimensions, authorized colorways, `Tier 4` co-branding spacing, and mark misuse prohibitions. | Hary Irfantri |
