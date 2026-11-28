# D01 — Design Tokens & Architecture

| Field | Value |
| :--- | :--- |
| **Code** | `D01` |
| **Version** | `v1.0.4` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-28` |
| **Next Review** | `2027-05-22` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `AST-D01-01`, `AST-D01-02` |

## 1. Purpose

This standard defines the design token hierarchy, naming conventions, theme architecture, and design-to-code synchronization rules for **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`). It translates the visual foundations in Series B (`B01`–`B05`) into deterministic, version-pinned tokens across digital products and design tools.

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* All design token definitions, JavaScript Object Notation (`JSON`) token schemas, and Cascading Style Sheets (`CSS`) custom property outputs (`AST-D01`).
* All digital user interfaces, design libraries, component systems, and web properties governed by `D02`–`D05`.
* All design-to-code handoff, validation, and release synchronization workflows for **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`).

### 2.2 Out of Scope
This standard does not govern:
* Brand mark geometry, clear space, or co-branding rules (governed by `B01`).
* Color palette values, contrast ratios, or status color semantics (governed by `B02`, which this standard codifies as tokens).
* Typeface selection, body size minimums, or tabular numeral rules (governed by `B03`).
* Spatial grid base units (`4 px` / `4 mm`), corner radii, or graphic devices (governed by `B04`).
* Icon grids, schematic connectors, or reduced-motion behavior (governed by `B05`).

## 3. Normative References

The following documents are referenced in this standard. For undated references, the latest approved edition applies.
* `Library-Index.md` — Standards Design Library Index (`v2.0.0` or later).
* `A01` — Document Control & Lifecycle.
* `A02` — Taxonomy, Coding & File Naming.
* `A03` — Entity & Brand Architecture.
* `A04` — Compliance, Reviews & Exceptions.
* `B02` — Color System.
* `B03` — Typography.
* `B04` — Grids, Spacing & Graphic Devices.
* `C02` — Terminology & Controlled Vocabulary.
* `C04` — Data, Dates & Citation Formatting.
* `D02` — Responsive Shells & Navigation.
* `D03` — Interface Components & Patterns.
* `D04` — Accessibility & Usability.

## 4. Terms & Definitions

For terms shared across the library, refer to `C02`, `B02`, `B03`, and `B04`. For the purposes of this standard, the following definitions apply:
* **Alias Token:** A semantic token referencing a primitive token by functional role or User Interface (`UI`) state rather than raw visual value.
* **Design Token:** A named, machine-readable key-value pair representing an atomic visual or typographic property (Hexadecimal (`HEX`) color, spacing length, font family, or radius).
* **Primitive Token:** A foundational token storing an approved raw value from `B02`, `B03`, or `B04` without context-specific role assignment.
* **Token Tier:** A layered token abstraction (`Primitive`, `Semantic`, or `Component`) that separates raw brand values from contextual roles.

## 5. Requirements

### 5.1 Token Hierarchy & Naming Syntax
**5.1.1** Design tokens SHALL follow a three-tier structure:
* **Primitive Tier:** Raw palette, typography, spacing, and radius values from `B02`–`B04`.
* **Semantic Tier:** Role-based tokens mapped to surfaces, text, borders, and states (`--is-color-bg-canvas`, `--is-color-text-primary`, `--is-color-status-danger`).
* **Component Tier:** Scoped tokens bound to specific `D03` component slots.

**5.1.2** Semantic and component token names in `CSS` custom properties SHALL use lowercase kebab-case with the `is-` prefix (`--is-[category]-[role]-[variant]`), such as `--is-color-brand-primary`.

**5.1.3** Token names and values SHALL NOT contain internal project codenames (`A03 §5.4.2`, `C02 §5.3.3`) or unapproved status synonyms (`C02 §5.4.2`).

### 5.2 Value Fidelity, Units & Theme Architecture
**5.2.1** Color token values SHALL match the exact uppercase `HEX` values (`#RRGGBB`) in `B02 §5.1.1`–`§5.3.1`. Error and danger text tokens SHALL reference `#A42332` rather than `#DE0029` (`B02 §5.3.2`).

**5.2.2** Typography and spacing token values SHALL conform to `B03` and `B04`. Numeric unit formatting in token schemas and documentation SHALL follow `C04 §5.3.1`–`§5.3.4` (`16px` or `16 px` per syntax context).

**5.2.3** Digital interfaces (`D01`–`D04`) SHALL use the approved light surface theme (`#FFFFFF` / `#F8FAFC`) as the default theme. Unapproved themes or dark-surface overrides SHALL NOT be introduced without `B02 §5.5.1` contrast verification.

### 5.3 Design-to-Code Synchronization & Master Assets
**5.3.1** Published token packages SHALL be generated from a single source-of-truth `JSON` token definition. Generated `CSS` or style files SHALL NOT be edited manually downstream without re-running token validation.

**5.3.2** Whenever an upstream `B02`, `B03`, or `B04` standard increments `MAJOR` (`A01 §5.5.3`), dependent `AST-D01` token packages SHALL transition to `Sync Required` until reconciled and re-verified.

**5.3.3** Every approved master token file SHALL be registered as an `AST-D01` Master Asset in `Library-Index.md` and Section 7, pinned to `D01 (vMAJOR.MINOR)` (`A01 §5.7.4`, `A02 §5.7.2`).

## 6. Conformance & Verification

A token schema, stylesheet, or digital implementation conforms to `D01` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `D01-C1` | Tokens follow the three-tier hierarchy (`5.1.1`), use `--is-` kebab-case naming (`5.1.2`), and contain zero codenames or informal status labels (`5.1.3`). | Token & lint audit |
| `D01-C2` | Color tokens match `B02` `#RRGGBB` values and use `#A42332` for danger/error text (`5.2.1`), typography/spacing/units match `B03`, `B04`, and `C04` (`5.2.2`), and default theme contrast is verified (`5.2.3`). | Schema & contrast audit |
| `D01-C3` | Token packages derive from a single `JSON` source without manual downstream drift (`5.3.1`), `MAJOR` governing updates trigger `Sync Required` (`5.3.2`), and master token files are registered as `AST-D01` (`5.3.3`). | Build & register audit |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with `A04`.

## 7. Linked Artifacts

| Code | Artifact | File | Pinned Version | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `AST-D01-01` | Design Tokens Master Schema (`JSON`) | `02_Assets/AST-D01-01_Design-Tokens.json` | `D01 (v1.0)` | `Approved` | Canonical single-source design token schema generating `CSS` custom properties |
| `AST-D01-02` | Design Tokens Stylesheet (`CSS`) | `02_Assets/AST-D01-02_Design-Tokens.css` | `D01 (v1.0)` | `Approved` | `CSS` custom properties generated from `AST-D01-01` by `tools/build_tokens_css.py` (`5.3.1`); regenerate, never edit by hand |

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v1.0.4` | `2026-11-28` | Errata | Registered `AST-D01-02` (generated `CSS` custom properties) in the `Governs` header and Section 7, renamed the library reference in Section 3 to `Standards Design`, and raised the `Library-Index.md` reference floor to `v2.0.0` per `A01 §5.2.8`, `§5.5.7`, and `REC-A04-016`. | Hary Irfantri |
| `v1.0.3` | `2026-11-25` | Errata | Populated `Governs` header (`AST-D01-01` per `A01 §5.2.8`), updated `Library-Index.md` reference floor in Section 3 (`A01 §5.5.7`), and confirmed `D02 (v2.0.0)` and `D03 (v2.0.0)` alignment alongside `AST-D01-01` metadata sync per `REC-A04-005` (`F-03`, `F-07`). | Hary Irfantri |
| `v1.0.2` | `2026-11-24` | Errata | Promoted `AST-D01-01` (`02_Assets/AST-D01-01_Design-Tokens.json`, pinned to `D01 (v1.0)`) from `Planned` to `Approved` in Section 7 and updated `Library-Index.md` reference floor per `A01 §5.5.5`. | Hary Irfantri |
| `v1.0.1` | `2026-11-23` | Errata | Expanded `UI` and `HEX` on first occurrence in Section 4, trimmed unused Section 3 references (`B01`, `B05`, `C03`, `D05`), and tightened long Section 5 sentences per `REC-A04-004` (`F-03`, `F-04`). | Hary Irfantri |
| `v1.0.0` | `2026-11-22` | Major | Initial approved baseline of `D01` (Design Tokens & Architecture), locking the three-tier token hierarchy, `--is-` kebab-case naming, `B02`–`B04` and `C04` value/unit alignment, default theme governance, single-source `JSON` build sync, and `AST-D01-01` asset registration. | Hary Irfantri |
| `v0.1.0` | `2026-11-22` | Pre-Release | Initial draft establishing the three-tier token hierarchy, `--is-` kebab-case naming, `B02`–`B04` and `C04` value/unit alignment, default theme governance, single-source `JSON` build sync, and `AST-D01-01` asset governance. | Hary Irfantri |
