# B05 — Iconography, Diagrams & Visuals

| Field | Value |
| :--- | :--- |
| **Code** | `B05` |
| **Version** | `v1.2.0` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-27` |
| **Next Review** | `2027-05-22` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `None` |

## 1. Purpose

This standard defines the iconography grid and sizing rules, technical schematics and diagrams, data charts, photography, illustration, and motion principles for **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`). It ensures non-brand visual elements remain clear, consistent, accessible, and distinct from official brand marks (`B01`).

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* All User Interface (`UI`) icons, system status glyphs, and small-format icon derivatives (`D01`–`D05`).
* All technical schematics, architecture diagrams, workflows, and data charts across standards, publications (`PUB-`), and formal documents (`E01`–`E04`).
* All editorial photography, illustrations, and motion transitions governed by `B02`–`B04` and `D01`–`D05`.

### 2.2 Out of Scope
This standard does not govern:
* Official brand marks, lockups, clear space, or co-branding rules (governed by `B01`).
* Core brand palette definitions, neutral scales, or semantic status colors (governed by `B02`).
* Display and body typefaces, font sizes, or tabular numeral alignment (governed by `B03`).
* Spatial grid base units (`4 px` / `4 mm`), corner radii, or signature graphic bars (governed by `B04`).

## 3. Normative References

The following documents are referenced in this standard. For undated references, the latest approved edition applies.
* `A03` — Entity & Brand Architecture.
* `A04` — Compliance, Reviews & Exceptions.
* `B01` — Marks & Lockups.
* `B02` — Color System.
* `B03` — Typography.
* `B04` — Grids, Spacing & Graphic Devices.
* `C01` — Voice, Tone & Plain Language.
* `C02` — Terminology & Controlled Vocabulary.
* `C04` — Data, Dates & Citation Formatting.
* `D01` — Design Tokens & Architecture.
* `D02` — Responsive Shells & Navigation.
* `D03` — Interface Components & Patterns.
* `D04` — Accessibility & Usability.
* `E04` — Correspondence & Presentations.

## 4. Terms & Definitions

For terms shared across the library, refer to `C02`, `B01`, and `B04`. For the purposes of this standard, the following definitions apply:
* **Data Chart:** A structured visual representation—such as a bar, line, or table-backed chart—displaying quantitative series and comparisons (`C04`).
* **Icon Grid:** A square design frame (`16 px × 16 px`, `20 px × 20 px`, or `24 px × 24 px`) and uniform stroke weight governing icon alignment and optical sizing (`B04 §5.1.1`).
* **Reduced Motion:** A system or user preference (`prefers-reduced-motion`) minimizing non-essential animation, movement, or auto-scrolling transitions.
* **Technical Schematic:** A structured diagram depicting system components, flows, taxonomies, or governance relationships using geometric shapes and labeled connectors.

## 5. Requirements

### 5.1 Iconography Grid, Strokes & Formats
**5.1.1** `UI` icons SHALL use a `4 px` Base Unit grid (`16 px`, `20 px`, or `24 px` square) (`B04 §5.1.1`, `C04 §5.3.2`). Sibling icons SHALL share a uniform stroke weight of `1.5 px` or `2 px`.

**5.1.2** Digital icons SHALL use Scalable Vector Graphics (`SVG`) masters or lossless Portable Network Graphics (`PNG`) derivatives exported at exact integer pixel dimensions (`C04 §5.3.2`).

**5.1.3** Icons SHALL NOT be substituted for the official `B01` Primary Symbol or lockups, and `16 px` small-format derivatives SHALL simplify fine geometric detail rather than compressing intricate artwork (`B01 §5.3.2`).

**5.1.4** Where the brand symbol appears on screen from `16 px` to below `28 px`, interfaces SHALL use the registered Small-Format Symbol (`AST-B01-17` or `AST-B01-18`) under `B01 §5.3.4`. Interfaces SHALL NOT draw a separate icon version of the symbol.

> **Informative Note:** The Small-Format Symbol is a `B01` mark, not a `UI` icon. Its stroke widths follow `B01 §5.3.5`, so the uniform `1.5 px` or `2 px` stroke rule in Clause `5.1.1` does not apply to it.

### 5.2 Technical Schematics & Data Charts
**5.2.1** Technical schematics and architecture diagrams SHALL use straight or orthogonal connectors (`90°` bends) (`C04 §5.3.2`), consistent node styling, and legible labels (`B03 §5.2.2`).

**5.2.2** Data charts SHALL label axes and series explicitly (`C04 §5.4.2`, `§5.4.4`) and SHALL NOT rely on color alone to distinguish data series (`B02 §5.5.2`).

**5.2.3** Diagrams and charts SHALL NOT display internal project codenames (`A03 §5.4.2`, `C02 §5.3.3`) or unsubstantiated promotional claims (`C01 §5.1.2`).

### 5.3 Photography & Illustration
**5.3.1** Photography and illustrations in communications (`E04`), publications (`PUB-`), and interfaces (`D02`) SHALL maintain an objective editorial tone (`C01 §5.1.1`, `§5.1.4`). Visuals SHALL avoid staged clichés and unverified claims (`C01 §5.4.1`).

**5.3.2** Photography and illustrations paired with overlaid text or `B01` marks SHALL meet `B02 §5.4.2`–`§5.4.3` and `§5.5.1` contrast rules. Third-party imagery SHALL NOT be used without documented rights clearance (`A03 §5.5.4`).

### 5.4 Motion & Reduced-Motion Support
**5.4.1** Motion transitions in digital interfaces (`D01`, `D03`) SHOULD NOT exceed `300 ms` in duration (`C04 §5.3.2`). Interfaces SHALL NOT present flashing exceeding three flashes per second or unpausable erratic movement (`D04`).

**5.4.2** Digital interfaces (`D01`, `D03`) SHALL honor user reduced-motion preferences (`prefers-reduced-motion`) by disabling or simplifying non-essential motion transitions.

## 6. Conformance & Verification

A visual asset, diagram, chart, interface, or publication conforms to `B05` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `B05-C1` | `UI` icons align to `16 px`, `20 px`, or `24 px` grids with uniform `1.5 px` or `2 px` strokes (`5.1.1`), use `SVG`/`PNG` masters (`5.1.2`), and avoid `B01` mark substitution or over-compressed detail (`5.1.3`). Brand symbols rendered from `16 px` to below `28 px` use `AST-B01-17` or `AST-B01-18` (`5.1.4`). | Icon & asset audit |
| `B05-C2` | Technical schematics use orthogonal/straight connectors and clear labels (`5.2.1`), and data charts pair color with non-color series cues (`5.2.2`). | Diagram & chart review |
| `B05-C3` | Diagrams and charts contain zero internal codenames or promotional hype (`5.2.3`). | Content & glossary audit |
| `B05-C4` | Photography and illustrations match objective editorial tone (`5.3.1`), preserve contrast and rights clearance (`5.3.2`), and avoid third-party non-affiliation claims (`A03 §5.6.2`). | Visual & rights inspection |
| `B05-C5` | Motion transitions avoid flashing above three flashes per second or unpausable erratic movement (`5.4.1`) and honor reduced-motion preferences (`5.4.2`). | Interaction & `D04` audit |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with `A04`.

## 7. Linked Artifacts

None.

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v1.2.0` | `2026-11-27` | Minor | Added `5.1.4` requiring the registered `B01 (v2.1.0)` Small-Format Symbol (`AST-B01-17`, `AST-B01-18`) for brand symbols rendered from `16 px` to below `28 px`, with an informative note separating it from `UI` icon stroke rules, and extended `B05-C1`. | Hary Irfantri |
| `v1.1.0` | `2026-11-25` | Minor | Replaced subjective motion qualifiers in `5.4.1` with a recommended `300 ms` duration cap and objective `SHALL NOT` limits on flashing (`> 3` flashes per second) and unpausable erratic movement (`B05-C5`), restored Section 3 normative reference parity (added `D02`, removed six unused references and obsolete pre-approval note), split 30+ word sentences in `5.1.1` and `5.3.1`–`5.3.2`, and confirmed `D03 (v2.0.0)` alignment per `REC-A04-005` (`F-08`, `F-09`, `F-10`). | Hary Irfantri |
| `v1.0.0` | `2026-11-22` | Major | Initial approved baseline of `B05` (Iconography, Diagrams & Visuals), locking the `16 px`–`24 px` icon grid and stroke rules, schematic and data chart accessibility rules, editorial photography/illustration standards, and reduced-motion requirements. | Hary Irfantri |
| `v0.1.0` | `2026-11-22` | Pre-Release | Initial draft establishing the `16 px`–`24 px` icon grid and stroke rules, schematic and data chart accessibility rules, editorial photography/illustration standards, and reduced-motion requirements. | Hary Irfantri |
