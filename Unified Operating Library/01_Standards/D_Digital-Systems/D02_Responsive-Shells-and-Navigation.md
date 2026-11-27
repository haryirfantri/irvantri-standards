# D02 — Responsive Shells & Navigation

| Field | Value |
| :--- | :--- |
| **Code** | `D02` |
| **Version** | `v2.0.1` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-25` |
| **Next Review** | `2027-05-22` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `None` |

## 1. Purpose

This standard defines the responsive viewport breakpoints, application and web page shell structures, navigation patterns, landmark organization, and footer attribution rules for **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`). It ensures digital interfaces remain structured, scannable, and consistent across desktop, tablet, and mobile viewports.

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* All web portals, digital products, and application shells representing **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`).
* All responsive breakpoints, persistent headers, sidebars, drawers, breadcrumbs, and footers governed by Series D (`D01`–`D05`).
* All corporate website footers and legal pages governed by `A03 §5.3.3` and `C01 §5.5.1`.

### 2.2 Out of Scope
This standard does not govern:
* Design token definitions, `--is-` naming, or single-source `JSON`/`CSS` token builds (governed by `D01`).
* Specific form inputs, tables, modals, or status badge component behavior (governed by `D03`).
* Detailed accessibility focus rules, keyboard shortcuts, or Accessible Rich Internet Applications (`ARIA`) attributes (governed by `D04`).
* Brand mark geometry, color tokens, or typography scales (governed by `B01`–`B03`, which this standard applies).

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
* `C03` — Technical & User Experience (UX) Writing.
* `C04` — Data, Dates & Citation Formatting.
* `D01` — Design Tokens & Architecture.
* `D03` — Interface Components & Patterns.
* `D04` — Accessibility & Usability.

## 4. Terms & Definitions

For terms shared across the library, refer to `C02`, `B01`, and `B04`. For the purposes of this standard, the following definitions apply:
* **Breakpoint:** A viewport width threshold at which layout geometry, navigation chrome, or shell panels adapt to screen size.
* **Navigation Chrome:** Persistent structural framing—such as top headers, sidebars, drawers, breadcrumbs, and footers—that orients users across views.
* **Page Shell:** The outer structural layout container framing primary content, navigation regions, and supporting panels.
* **Skip Link:** A hidden-until-focused control allowing keyboard users to bypass repeated navigation links directly to main content.

## 5. Requirements

### 5.1 Responsive Breakpoints & Shell Geometry
**5.1.1** Digital interfaces (`D01`–`D04`) SHALL support responsive viewports across three layout tiers aligned to the `4 px` Base Unit grid (`B04 §5.1.1`, `C04 §5.3.2`):

| Viewport Tier | Width Range | Shell & Navigation Behavior |
| :--- | :--- | :--- |
| **Compact (Mobile)** | Below `768 px` | Single-column content flow, collapsible navigation drawer, and top header limited to essential brand and menu controls |
| **Medium (Tablet)** | `768 px` through `1279 px` (`C04 §5.3.2`) | Collapsible or icon-rail sidebar paired with single or two-column content layout |
| **Expanded (Desktop)** | `1280 px` and above | Persistent navigation shell and multi-column or bounded content container |

**5.1.2** Page shells SHALL prevent horizontal page overflow from `320 px` through `1440 px` (`C04 §5.3.2`). Shells SHALL NOT clip primary content at `200%` text scaling (`B03 §5.4.2`, `C04 §5.2.3`).

**5.1.3** Every page shell SHALL provide a skip-to-content control (`Skip to main content`) that becomes visible on keyboard focus and moves focus to the primary content region (`D04`).

### 5.2 Headers, Navigation & Wayfinding
**5.2.1** Top navigation bars and headers SHALL use official `B01` marks (Primary Master Lockup or Primary Symbol) (`B01 §5.2.1`, `§5.3.2`). Headers SHALL NOT place the Parent-Endorsed Lockup inside compact navigation bars (`B01 §5.2.3`, `A03 §5.3.4`).

**5.2.2** Navigation labels and controls SHALL follow `C03 §5.1.1`–`§5.1.5` (sentence case, imperative or concise object labels, zero trailing periods). Navigation labels SHALL NOT display internal project codenames (`A03 §5.4.2`, `C02 §5.3.3`).

**5.2.3** Active navigation states SHALL indicate the current section using both semantic styling (`B02 §5.3.1`, `§5.5.2`) and a non-color state indicator (`aria-current` or explicit label).

**5.2.4** Multi-tenant or client-facing page shells SHALL NOT mix tenant branding and `Irvantri Group` parent branding within the same interface view (`A03 §5.3.5`, `§5.5.1`–`§5.5.2`).

### 5.3 Footers & Corporate Attribution
**5.3.1** Corporate website footers and legal pages SHALL display the verbatim Endorsement Line `A member of Irvantri Group` (`A03 §5.2.1`, `§5.3.3`, `C01 §5.5.1`). Footers and legal pages SHALL also display `© [YYYY] Irvantri Standards Pte. Ltd. All rights reserved.` (`A03 §5.6.1`).

**5.3.2** Footer links and legal notices SHALL conform to `B02 §5.5.1` contrast minimums and `B03 §5.2.2` body legibility rules.

## 6. Conformance & Verification

A digital interface, portal, or page shell conforms to `D02` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `D02-C1` | Shell adapts across Compact (`< 768 px`), Medium (`768 px` through `1279 px`), and Expanded (`≥ 1280 px`) viewports (`5.1.1`), prevents horizontal overflow from `320 px` through `1440 px` and `200%` text clipping (`5.1.2`), and provides a keyboard-accessible skip link (`5.1.3`). | Responsive & keyboard audit |
| `D02-C2` | Top headers follow `B01` lockup placement rules without putting the Parent-Endorsed Lockup in compact bars (`5.2.1`), labels follow `C03` without codenames (`5.2.2`), active items use non-color state cues (`5.2.3`), and views do not mix tenant and parent branding (`5.2.4`). | Header & navigation audit |
| `D02-C3` | Corporate footers and legal pages reproduce `A member of Irvantri Group` and `© [YYYY] Irvantri Standards Pte. Ltd. All rights reserved.` verbatim (`5.3.1`) while meeting contrast and size rules (`5.3.2`). | Footer & attribution audit |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with `A04`.

## 7. Linked Artifacts

None.

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v2.0.1` | `2026-11-25` | Errata | Removed misdirected `C04 §5.1.3` date-interval citations from pixel ranges in `5.1.1`–`5.1.2`, expanded Web Content Accessibility Guidelines (`WCAG`) and Success Criterion (`SC`) in the `v2.0.0` changelog entry, and confirmed `D03 (v2.0.0)` alignment per `REC-A04-005` (`F-10`). | Hary Irfantri |
| `v2.0.0` | `2026-11-24` | Major | Tightened horizontal overflow prevention floor from `375 px` to `320 px` to align with Web Content Accessibility Guidelines (`WCAG`) 2.2 Success Criterion (`SC`) 1.4.10 Reflow (`5.1.2`), prohibited mixing tenant and parent branding in multi-tenant views (`5.2.4`), and updated `D02-C1` and `D02-C2`. | Hary Irfantri |
| `v1.0.1` | `2026-11-23` | Errata | Removed leaked chat citation strings, trimmed unused Section 3 references (`Library-Index.md`, `A01`, `A02`, `B05`, `D05`, `E01`, `E04`), removed misdirected `C04 §5.4.1` citation in `5.3.1`, and split long Section 5 sentences per `REC-A04-004` (`F-02`, `F-04`). | Hary Irfantri |
| `v1.0.0` | `2026-11-22` | Major | Initial approved baseline of `D02` (Responsive Shells & Navigation), locking responsive viewport tiers, overflow and `200%` zoom resilience, skip-link navigation, `B01`/`C03` header and label rules, and verbatim corporate footer attribution. | Hary Irfantri |
| `v0.1.0` | `2026-11-22` | Pre-Release | Initial draft establishing responsive viewport tiers, overflow and `200%` zoom resilience, skip-link navigation, `B01`/`C03` header and label rules, and verbatim corporate footer attribution. | Hary Irfantri |
