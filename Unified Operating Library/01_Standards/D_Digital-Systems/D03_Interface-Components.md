# D03 — Interface Components & Patterns

| Field | Value |
| :--- | :--- |
| **Code** | `D03` |
| **Version** | `v2.0.0` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-25` |
| **Next Review** | `2027-05-22` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `None` |

## 1. Purpose

This standard defines the structural, behavioral, accessibility, and copy alignment rules for reusable user interface components and interaction patterns across **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`). It ensures inputs, forms, data tables, status badges, confirmation dialogs, and interactive states remain consistent, accessible, and predictable across digital products.

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* All interactive controls, buttons, form fields, validation patterns, data tables, status indicators, dialogs, and empty states used in **Irvantri Standards** digital interfaces (`D01`–`D05`).
* All component-tier token bindings and interaction states governed by `D01` and `D02`.

### 2.2 Out of Scope
This standard does not govern:
* Design token hierarchy, `--is-` token naming syntax, or single-source `JSON`/`CSS` token generation (governed by `D01`).
* Responsive viewport breakpoints, shell layout tiers, headers, sidebars, or footers (governed by `D02`).
* Detailed accessibility focus rules, keyboard shortcuts, or Accessible Rich Internet Applications (`ARIA`) attributes (governed by `D04`).
* User Interface (`UI`) microcopy phrasing rules, error message anatomy, or confirmation copy structure (governed by `C03`, which this standard applies).

## 3. Normative References

The following documents are referenced in this standard. For undated references, the latest approved edition applies.
* `A03` — Entity & Brand Architecture.
* `A04` — Compliance, Reviews & Exceptions.
* `B02` — Color System.
* `B03` — Typography.
* `B04` — Grids, Spacing & Graphic Devices.
* `B05` — Iconography, Diagrams & Visuals.
* `C02` — Terminology & Controlled Vocabulary.
* `C03` — Technical & User Experience (UX) Writing.
* `C04` — Data, Dates & Citation Formatting.
* `D02` — Responsive Shells & Navigation.
* `D04` — Accessibility & Usability.

## 4. Terms & Definitions

For terms shared across the library, refer to `C02`, `B02`, `B03`, and `B04`. For the purposes of this standard, the following definitions apply:
* **Component State:** The visual and interactive condition of a `UI` control or container—such as Default, Hover, Focus, Active, Disabled, Error, or Loading.
* **Confirmation Dialog:** A modal or inline prompt requiring explicit user acknowledgment before executing a significant or irreversible action.
* **Data Table:** A structured tabular grid displaying multi-column records, statuses, or quantitative values (`C04`).
* **Form Control:** An interactive input element—such as a text field, select menu, checkbox, or radio group—accepting user input or selection.

## 5. Requirements

### 5.1 Buttons, Controls & Interaction States
**5.1.1** Interactive buttons and controls SHALL open with imperative verb-object labels (`C03 §5.1.1`), use sentence case (`C03 §5.1.2`), and SHALL NOT use `OK`, `Yes`, or `Click Here` as standalone labels.

**5.1.2** Interactive controls SHALL meet the `44 px × 44 px` minimum target size or Web Content Accessibility Guidelines (`WCAG`) 2.2 Level AA target-size requirement (`B04 §5.1.4`, `B02 §5.5.1`). Control spacing and corner radii SHALL align to `B04 §5.1.1` and `§5.2.1`.

**5.1.3** Component states SHALL distinguish Default, Hover, Focus, Active, and Disabled visually without relying on color alone (`B02 §5.5.2`), and keyboard focus indicators SHALL remain clearly visible (`D04`).

**5.1.4** Each view or form footer SHOULD present at most one primary action button, separating destructive actions into explicit confirmation controls (`5.4.1`).

**5.1.5** Disabled interactive controls SHOULD display adjacent helper text stating the unmet prerequisite required to enable the action (`C03 §5.1.3`).

### 5.2 Forms, Validation & Error Feedback
**5.2.1** Every form field SHALL pair a visible text label (`B03 §5.2.2`, `C03 §5.1.2`) with its input control and SHALL NOT rely on placeholder text alone as a field label.

**5.2.2** Inline validation and error messages SHALL identify the affected field and constraint (`C03 §5.2.4`) and state what occurred, why, and how to recover (`C03 §5.2.1`). Error text SHALL use **Danger** (`#A42332`) rather than raw **Signal Red** (`#DE0029`) (`B02 §5.3.2`).

**5.2.3** Error payloads and `UI` error displays SHALL NOT expose internal stack traces, database schemas, or internal project codenames (`C03 §5.2.3`, `A03 §5.4.2`, `C02 §5.3.3`).

**5.2.4** Inline field validation SHALL trigger on field blur or form submission rather than interrupting initial keystroke entry (`C03 §5.2.4`).

### 5.3 Data Tables & Status Indicators
**5.3.1** Data tables SHALL include explicit column headers, contain zero blank cells (`None` or `—` per `C04 §5.4.1`), and state shared units in numeric headers (`C04 §5.4.2`). Numeric columns SHALL use Tabular Numerals (`B03 §5.3.1`).

**5.3.2** Status badges and lifecycle indicators SHALL use exact `C02 §5.4.1` controlled status strings without informal synonyms (`C02 §5.4.2`). Indicators SHALL pair semantic colors (`B02 §5.3.1`) with text or icon cues (`B02 §5.5.2`) and omit exclamation marks (`!`) (`C03 §5.3.3`).

**5.3.3** On Compact viewports (`320 px` through `767 px` per `D02 §5.1.1`–`§5.1.2`), multi-column Data Tables SHOULD reflow into summary cards preserving status semantics (`5.3.2`) and reading order (`D04 §5.2.2`).

### 5.4 Confirmation Dialogs, Empty States & Provenance
**5.4.1** Destructive action confirmations SHALL state the target item and permanent consequence (`C03 §5.3.1`) and provide a specific verb-object primary action button (`C03 §5.3.2`).

**5.4.2** Empty states SHALL explain why no items appear (`C03 §5.4.1`) and provide a valid primary recovery action where actionable (`C03 §5.4.2`).

**5.4.3** Read-only or version-pinned records SHALL display a visually distinct provenance callout stating snapshot status and revision requirements without relying on color alone (`B02 §5.5.2`).

### 5.5 Operational Interface Discipline
**5.5.1** Operational interfaces SHALL display active lifecycle states (such as `Open`, `In Review`, `Sync Required`, or `Waived`) using exact `C02 §5.4.1` controlled status indicators (`5.3.2`). Interfaces SHALL NOT use prohibited status synonyms (such as `Pending` per `C02 §5.5.1`). Domain-specific record attributes (such as incomplete, exempt, or locked flags) SHALL render as explicit non-color attribute badges or provenance callouts (`5.4.3`) distinct from controlled lifecycle status badges.

**5.5.2** Operational dashboards SHOULD prioritize open reviews, active assignments, and required user decisions ahead of decorative summary charts (`B05 §5.2.2`).

**5.5.3** Dense work surfaces, forms, and data tables SHALL NOT include decorative waves, orbital rings, or ornamental background graphics (`B04 §5.3.4`).

## 6. Conformance & Verification

A digital component, form, table, dialog, or interface conforms to `D03` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `D03-C1` | Buttons and controls follow `C03` verb-object and sentence-case rules without `OK`, `Yes`, or `Click Here` (`5.1.1`), meet `B04` target-size/spacing/radius rules (`5.1.2`), and distinguish states with visible focus and non-color cues (`5.1.3`). | Component & interaction audit |
| `D03-C2` | Form controls have visible labels rather than placeholder-only labels (`5.2.1`), validation and error text follow `C03` and use `#A42332` rather than `#DE0029` (`5.2.2`), zero stack traces, schemas, or codenames appear (`5.2.3`), and inline validation triggers on blur or submit (`5.2.4`). | Form & error state audit |
| `D03-C3` | Data tables include headers, zero blank cells, shared units, and Tabular Numerals (`5.3.1`), and status indicators use `C02` controlled strings, non-color cues, and zero exclamation marks (`5.3.2`). | Table & status badge audit |
| `D03-C4` | Destructive confirmations state item, consequence, and verb-object action (`5.4.1`), empty states explain absence and provide valid recovery actions (`5.4.2`), and read-only or version-pinned records display non-color provenance callouts (`5.4.3`). | Dialog, empty-state & provenance review |
| `D03-C5` | Operational views display controlled lifecycle states per `C02 §5.4.1` with zero prohibited synonyms, render domain flags (incomplete, exempt, locked) distinct from lifecycle badges (`5.5.1`), and omit decorative background graphics on dense work surfaces (`5.5.3`). | Operational `UI` audit |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with `A04`.

## 7. Linked Artifacts

None.

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v2.0.0` | `2026-11-25` | Major | Resolved `C02` status conflict by restricting controlled lifecycle badges in `5.5.1` strictly to `C02 §5.4.1` values, prohibiting `Pending`, and separating domain record flags (`incomplete`, `exempt`, `locked`) into distinct non-color badges or provenance callouts; replaced `pending` in `5.5.2`; aligned `5.3.3` with `D02 (v2.0.0)` `320 px` reflow; and updated `D03-C5` per `REC-A04-005` (`F-05`). | Hary Irfantri |
| `v1.1.0` | `2026-11-24` | Minor | Added single primary action (`5.1.4`) and explained disabled control (`5.1.5`) defaults, blur/submit inline validation (`5.2.4`), Compact table summary-card reflow (`5.3.3`), version-pinned provenance callouts (`5.4.3`), Operational Interface Discipline (`5.5.1`–`5.5.3`), `D03-C5`, and `B05`/`D02` references. | Hary Irfantri |
| `v1.0.1` | `2026-11-23` | Errata | Expanded `WCAG` on first occurrence in `5.1.2`, trimmed unused Section 3 references (`Library-Index.md`, `A01`, `A02`, `B01`, `B05`, `C01`, `D01`, `D02`, `D05`), and split long Section 5 sentences per `REC-A04-004` (`F-03`, `F-04`). | Hary Irfantri |
| `v1.0.0` | `2026-11-22` | Major | Initial approved baseline of `D03` (Interface Components & Patterns), locking button/control labeling and state rules, form label and `#A42332` error/validation requirements, data table and `C02` status indicator rules, and destructive confirmation and empty-state patterns. | Hary Irfantri |
| `v0.1.0` | `2026-11-22` | Pre-Release | Initial draft establishing button/control labeling and state rules, form label and `#A42332` error/validation requirements, data table and `C02` status indicator rules, and destructive confirmation and empty-state patterns. | Hary Irfantri |
