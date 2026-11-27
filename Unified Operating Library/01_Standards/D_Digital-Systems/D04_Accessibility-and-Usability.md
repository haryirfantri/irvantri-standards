# D04 — Accessibility & Usability

| Field | Value |
| :--- | :--- |
| **Code** | `D04` |
| **Version** | `v1.2.1` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-25` |
| **Next Review** | `2027-05-22` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `None` |

## 1. Purpose

This standard defines the Web Content Accessibility Guidelines (`WCAG`) conformance targets, keyboard navigation behavior, focus management rules, Accessible Rich Internet Applications (`ARIA`) semantics, and usability safeguards for **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`). It ensures digital interfaces remain operable, perceivable, understandable, and resilient for all users.

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* All digital products, web portals, navigation shells, and interactive components governed by `D01`–`D05`.
* All keyboard interaction paths, focus indicators, landmarks, `ARIA` attributes, and reduced-motion behaviors across **Irvantri Standards** interfaces.

### 2.2 Out of Scope
This standard does not govern:
* Design token naming conventions, `--is-` prefixes, or single-source `JSON`/`CSS` token builds (governed by `D01`).
* Responsive viewport breakpoints, shell layout tiers, or corporate footer attribution placement (governed by `D02`).
* Specific component copy patterns, error message phrasing, or table/dialog layout rules (governed by `C03` and `D03`, which this standard complements).
* Print layout geometry, paper stocks, or commercial print proofing (governed by `E01`–`E03`).

## 3. Normative References

The following documents are referenced in this standard. For undated references, the latest approved edition applies.
* `A04` — Compliance, Reviews & Exceptions.
* `B02` — Color System.
* `B03` — Typography.
* `B04` — Grids, Spacing & Graphic Devices.
* `B05` — Iconography, Diagrams & Visuals.
* `C02` — Terminology & Controlled Vocabulary.
* `D01` — Design Tokens & Architecture.
* `D02` — Responsive Shells & Navigation.
* `D03` — Interface Components & Patterns.

## 4. Terms & Definitions

For terms shared across the library, refer to `C02`, `B02`, `B03`, and `D02`. For the purposes of this standard, the following definitions apply:
* **Focus Indicator:** A visible outline or state cue highlighting the interactive element currently receiving keyboard or programmatic focus.
* **Focus Order:** The sequential path through which keyboard focus moves across interactive controls and landmarks in a view.
* **Live Region:** A dynamically updated interface region (`aria-live`) that announces status or validation changes to assistive technologies without stealing focus.
* **Target Size:** The interactive hit region of a control or link evaluated for pointer and keyboard operability (`B04 §5.1.4`, `D03 §5.1.2`).

## 5. Requirements

### 5.1 Conformance Target & Contrast Alignment
**5.1.1** Digital interfaces (`D01`–`D04`) SHALL conform to `WCAG` 2.2 Level AA success criteria. Conformance includes luminance contrast (`B02 §5.5.1`), text scaling without clipping (`B03 §5.4.2`, `D02 §5.1.2`), and minimum Target Size (`B04 §5.1.4`, `D03 §5.1.2`).

**5.1.2** Status badges, validation alerts, and announcements (`D03 §5.2.2`, `§5.3.2`) SHALL pair color cues with text, icons, or `ARIA` attributes (`B02 §5.5.2`) and SHALL NOT rely on color alone.

**5.1.3** Adjacent interactive touch targets on Compact viewports (`D02 §5.1.1`) SHALL maintain at least `12 px` of separation (`B04 §5.1.5`).

### 5.2 Keyboard Navigation & Focus Management
**5.2.1** All interactive controls, navigation items, and workflows SHALL be operable via keyboard without requiring pointer-only hover or drag gestures (`D02 §5.1.3`, `D03 §5.1.3`).

**5.2.2** Focus Order SHALL follow a logical reading and structural sequence aligned with visual layout (`D02`), and keyboard focus SHALL NOT become trapped inside modals, drawers, or embedded regions.

**5.2.3** Focused elements SHALL display a visible Focus Indicator (`B04 §5.1.4`, `D03 §5.1.3`) meeting `B02 §5.5.1` contrast rules. Focus Indicators SHALL NOT be suppressed (`outline: none`) without a compliant replacement.

**5.2.4** Keyboard Focus Indicators (`5.2.3`) SHOULD render as a `3 px` solid outline with a `3 px` offset using **Brand Blue** (`#074C96`) on light surfaces (`B02 §5.1.1`, `B04 §5.1.1`).

### 5.3 Semantic Structure, ARIA & Motion Safeguards
**5.3.1** Page shells and components (`D02`, `D03`) SHALL use semantic landmarks (`header`, `nav`, `main`, `footer`), explicit accessible labels (`D03 §5.2.1`), and valid `ARIA` roles and states rather than unsemantic elements alone.

**5.3.2** Dynamic status or validation updates SHALL expose valid `ARIA` states or Live Regions (`polite` or `assertive`) without interrupting active text entry or exposing internal system details (`D03 §5.2.3`).

**5.3.3** Interfaces SHALL honor `prefers-reduced-motion` (`B05 §5.4.2`) and SHALL NOT present flashing or motion patterns that violate `WCAG` 2.2 Level AA safety rules (`B05 §5.4.1`).

## 6. Conformance & Verification

A digital interface, component, or portal conforms to `D04` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `D04-C1` | Interface meets `WCAG` 2.2 Level AA contrast, text scaling, Target Size (`5.1.1`), and `12 px` Compact touch-target separation (`5.1.3`) requirements and avoids color-only state signaling (`5.1.2`). | Contrast, zoom & target audit |
| `D04-C2` | Workflows are keyboard-operable (`5.2.1`), Focus Order is logical with zero focus traps (`5.2.2`), and focused controls show a compliant visible Focus Indicator (`5.2.3`). | Keyboard & focus traversal audit |
| `D04-C3` | Markup uses semantic landmarks, accessible labels, and valid `ARIA` (`5.3.1`), dynamic updates use compliant `ARIA`/Live Regions (`5.3.2`), and reduced-motion/flashing safeguards hold (`5.3.3`). | Accessibility & `ARIA` audit |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with `A04`.

## 7. Linked Artifacts

None.

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v1.2.1` | `2026-11-25` | Errata | Tightened or split 30+ word sentences in `5.1.1`–`5.1.2` and `5.2.3` and confirmed `D02 (v2.0.0)` and `D03 (v2.0.0)` alignment per `REC-A04-005` (`F-10`). | Hary Irfantri |
| `v1.2.0` | `2026-11-24` | Minor | Added `12 px` minimum touch-target separation on Compact viewports (`5.1.3`), added recommended `3 px` solid `#074C96` Focus Indicator geometry with `3 px` offset (`5.2.4`), and updated `D04-C1`. | Hary Irfantri |
| `v1.1.0` | `2026-11-23` | Minor | Replaced prohibited vague qualifier `appropriate` with `valid` in `5.3.2`, standardized `SHALL NOT be suppressed` in `5.2.3`, and trimmed unused Section 3 references (`Library-Index.md`, `A01`, `A02`, `A03`, `B01`, `C01`, `C03`, `C04`, `D05`) per `REC-A04-004` (`F-01`, `F-04`). | Hary Irfantri |
| `v1.0.0` | `2026-11-22` | Major | Initial approved baseline of `D04` (Accessibility & Usability), locking `WCAG` 2.2 Level AA conformance targets, keyboard operability and focus management rules, semantic landmark and `ARIA` requirements, and reduced-motion safeguards. | Hary Irfantri |
| `v0.1.0` | `2026-11-22` | Pre-Release | Initial draft establishing `WCAG` 2.2 Level AA conformance targets, keyboard operability and focus management rules, semantic landmark and `ARIA` requirements, and reduced-motion safeguards. | Hary Irfantri |
