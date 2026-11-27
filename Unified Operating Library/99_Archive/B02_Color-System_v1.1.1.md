# B02 — Color System

| Field | Value |
| :--- | :--- |
| **Code** | `B02` |
| **Version** | `v1.1.1` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-25` |
| **Next Review** | `2027-05-22` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `None` |

## 1. Purpose

This standard defines the authoritative brand color palettes, digital and print color specifications, surface and text roles, proportional usage ratios, accessibility contrast thresholds, and color misuse rules for **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`). It ensures visual coherence, print color fidelity, and legible contrast across all digital systems, formal documents, and publications.

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* All brand marks, lockups, and colorway variants governed by `B01`.
* All digital user interfaces, design tokens, themes, and web properties (`D01`–`D05`).
* All formal documents, covers, headers, footers, presentation masters, and compiled publications (`E01`–`E04`, `PUB-`).
* All commercial print deliverables and vendor proofing specifications (`E03`).

### 2.2 Out of Scope
This standard does not govern:
* Semantic design token naming conventions or code stylesheet packaging (governed by `D01`, which implements the values defined here).
* Data visualization chart palettes or technical diagram stroke styling (governed by `B05`, which extends this palette).
* Third-party client or partner brand colors displayed in `Tier 4` Co-Branded deliverables (`A03 §5.5`).

## 3. Normative References

The following documents are referenced in this standard. For undated references, the latest approved edition applies.
* `A04` — Compliance, Reviews & Exceptions.
* `B01` — Marks & Lockups.
* `B04` — Grids, Spacing & Graphic Devices.
* `C02` — Terminology & Controlled Vocabulary.
* `C03` — Technical & User Experience (UX) Writing.
* `D01` — Design Tokens & Architecture.
* `D02` — Responsive Shells & Navigation.
* `D03` — Interface Components & Patterns.
* `D04` — Accessibility & Usability.
* `E01` — Formal Document Layout.
* `E03` — Print & Production Specifications.
* `E04` — Correspondence & Presentations.

## 4. Terms & Definitions

For terms shared across the library, refer to `C02` and `B01`. For the purposes of this standard, the following definitions apply:
* **Accent Color:** A high-chroma brand color reserved for focal visual markers, active indicators, and restrained brand emphasis rather than large background fills.
* **Contrast Ratio:** The relative luminance ratio between foreground text or graphic elements and their immediate background surface, calculated per Web Content Accessibility Guidelines (`WCAG`) 2.2.
* **Neutral Scale:** A calibrated sequence of low-chroma slate and gray tones governing page surfaces, borders, dividers, and body typography.
* **Primary Brand Palette:** The core institutional blue, navy, and signal red colors that establish the visual identity of Irvantri Standards.
* **Semantic Color:** A functional color assigned to communicate system state (`Informative`, `Success`, `Warning`, `Danger`, or `Neutral`) independently of decorative branding.

## 5. Requirements

### 5.1 Primary Brand Palette
**5.1.1** All brand expressions, digital interfaces (`D01`), and print materials (`E03`) SHALL use the exact Hexadecimal (`HEX`), Red-Green-Blue (`RGB`), and Cyan-Magenta-Yellow-Key (`CMYK`) values defined below (`C02 §5.2.3`):

| Color Name | Role | HEX | RGB | CMYK (ISO Coated v2) |
| :--- | :--- | :--- | :--- | :--- |
| **Brand Blue** | Primary interactive & identity anchor | `#074C96` | `7, 76, 150` | `98, 73, 7, 0` |
| **Signal Red** | Brand accent & signature rule marker | `#DE0029` | `222, 0, 41` | `4, 100, 84, 0` |
| **Deep Navy** | Primary structural dark & formal header ink | `#092B55` | `9, 43, 85` | `100, 85, 35, 30` |
| **Royal Navy** | Secondary dark surface & hover/active state | `#102F60` | `16, 47, 96` | `98, 82, 28, 22` |

**5.1.2** Digital `HEX` values SHALL be written in uppercase (`#074C96`) with a leading `#` symbol in specifications and token schemas (`D01`).

**5.1.3** Commercial offset and digital print production (`E03`) SHALL use the International Organization for Standardization (`ISO`) Coated v2 `CMYK` builds in Clause `5.1.1` rather than automated `RGB`-to-`CMYK` software conversions.

### 5.2 Neutral Surface & Typography Scale
**5.2.1** Interfaces (`D01`, `D02`, and `D03`) and formal documents (`E01`) SHALL use the calibrated neutral scale below for backgrounds, borders, and typography:

| Neutral Token Role | HEX | RGB | Permitted Application |
| :--- | :--- | :--- | :--- |
| **Pure White** | `#FFFFFF` | `255, 255, 255` | Primary page canvas, cards, and reversed marks (`B01 §5.4.1`) |
| **Canvas Subtle** | `#F8FAFC` | `248, 250, 252` | Secondary panel backgrounds, table headers, and code blocks |
| **Surface Muted** | `#F1F5F9` | `241, 245, 249` | Hover fills, subtle badges, and alternating row surfaces |
| **Surface Tint** | `#EFF6FF` | `239, 246, 255` | Interactive hover washes, active navigation fills, and provenance callout surfaces |
| **Border Subtle** | `#E2E8F0` | `226, 232, 240` | Hairline structural dividers, table row rules, and secondary container borders |
| **Border Default** | `#CBD5E1` | `203, 213, 225` | Hairline rules, table grids, and form input borders |
| **Text Muted** | `#5F6C7E` | `95, 108, 126` | Secondary metadata, captions, and helper text on light surfaces |
| **Text Primary** | `#0F172A` | `15, 23, 42` | Body copy, headings, and primary User Interface (`UI`) labels on light surfaces |
| **Pure Black** | `#000000` | `0, 0, 0` | Monochrome single-ink print reproduction (`B01 §5.4.1`, `E03`) |

### 5.3 Semantic & Status Color Palette
**5.3.1** System status badges, validation alerts, and feedback banners (`C03 §5.2`–`§5.3`, `D03`) SHALL use the semantic palette below:

| Semantic State | Foreground / Fill HEX | RGB | Subtle Surface HEX | Border HEX |
| :--- | :--- | :--- | :--- | :--- |
| **Informative** | `#074C96` | `7, 76, 150` | `#EFF6FF` | `#BFDBFE` |
| **Success** | `#166534` | `22, 101, 52` | `#F0FDF4` | `#BBF7D0` |
| **Warning** | `#92400E` | `146, 64, 14` | `#FFFBEB` | `#FDE68A` |
| **Danger** | `#A42332` | `164, 35, 50` | `#FEF2F2` | `#FECACA` |
| **Neutral** | `#475569` | `71, 85, 105` | `#F1F5F9` | `#CBD5E1` |

**5.3.2** Raw **Signal Red** (`#DE0029`) SHALL NOT be used for body text, form validation messages, or error text on white (`#FFFFFF`) or light neutral surfaces (`#F8FAFC`, `#F1F5F9`). Error and danger text SHALL use **Danger** (`#A42332`) to preserve `WCAG` 2.2 Level AA contrast (`D04`).

### 5.4 Proportional Color Ratios & Surface Rules
**5.4.1** Page compositions, presentation slides (`E04`), and publications (`PUB-`) SHOULD target a `75%` light neutral (`#FFFFFF` / `#F8FAFC`), `20%` blue or navy (`#074C96` / `#092B55`), and `5%` **Signal Red** (`#DE0029`) balance.

**5.4.2** **Signal Red** (`#DE0029`) SHALL be restricted to brand mark elements (`B01 §5.4.1`), signature accent rules (`E01`), and focused active markers. It SHALL NOT be used as a full-page background fill or primary body text color.

**5.4.3** Unapproved gradients, neon hues, drop-shadow color tints, and ad-hoc hex values outside Clauses `5.1.1`, `5.2.1`, and `5.3.1` SHALL NOT be introduced into brand templates (`TPL-`) or user interfaces (`D01`).

**5.4.4** Subtle neutral elevation shadows defined in `B04 §5.2.3` MAY be applied to cards and primary action buttons when zero unapproved color tints are introduced.

### 5.5 Accessibility Contrast & Non-Color Indicators
**5.5.1** All text and essential `UI` components SHALL meet or exceed `WCAG` 2.2 Level AA luminance contrast minimums (`D04`):
* Normal body text (under `18 pt` or `24 px` regular) SHALL achieve at least a `4.5:1` contrast ratio against its background.
* Large text (`18 pt` / `24 px` regular or `14 pt` / `18.66 px` bold and above) and non-text `UI` boundaries SHALL achieve at least a `3.0:1` contrast ratio.

**5.5.2** Semantic state communication in interfaces and status badges (`C02 §5.4.1`, `D03`) SHALL NOT rely on color alone. Every color-coded status indicator SHALL pair color with an explicit text label, icon, or status glyph.

## 6. Conformance & Verification

A digital interface, token file, publication, or print deliverable conforms to `B02` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `B02-C1` | Brand colors match exact `HEX`, `RGB`, and `ISO` Coated v2 `CMYK` builds (`5.1.1`, `5.1.3`), with uppercase `#RRGGBB` syntax (`5.1.2`). | Token & prepress audit |
| `B02-C2` | Neutral surfaces and typography use only calibrated neutral scale tokens (`5.2.1`), with zero ad-hoc hex values in templates or interfaces (`5.4.3`). | Stylesheet & layout lint |
| `B02-C3` | Semantic alerts and status indicators use the approved semantic palette (`5.3.1`), and error text uses `#A42332` rather than `#DE0029` (`5.3.2`). | `UI` & contrast inspection |
| `B02-C4` | **Signal Red** (`#DE0029`) is restricted to approved mark, rule, and accent roles (`5.4.2`). | Visual & layout review |
| `B02-C5` | All text (`4.5:1`) and large text / `UI` controls (`3.0:1`) satisfy `WCAG` 2.2 Level AA contrast (`5.5.1`), and status badges include non-color text or icon cues (`5.5.2`). | Accessibility contrast audit |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with `A04`.

## 7. Linked Artifacts

None.

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v1.1.1` | `2026-11-25` | Errata | Added `D02` to Section 3 normative references (covering `D01`–`D03` in `5.2.1`), tightened `5.4.1` below 30 words, and confirmed `D03 (v2.0.0)` alignment per `REC-A04-005` (`F-09`, `F-10`). | Hary Irfantri |
| `v1.1.0` | `2026-11-24` | Minor | Added `Surface Tint` (`#EFF6FF`) and `Border Subtle` (`#E2E8F0`) neutral tokens (`5.2.1`), added the fifth `Neutral` semantic status row (`#475569` / `#F1F5F9` / `#CBD5E1`) (`5.3.1`), added subtle neutral elevation allowance (`5.4.4`), expanded `ISO` and `UI` on first occurrence, and aligned Section 3 normative references. | Hary Irfantri |
| `v1.0.0` | `2026-11-22` | Major | Initial approved baseline of `B02` (Color System), locking the Primary Brand Palette (`HEX`, `RGB`, and `ISO` Coated v2 `CMYK`), Neutral Scale, Semantic Status Palette (`#A42332` Danger), proportional usage ratios, `WCAG` 2.2 Level AA contrast rules, and non-color status cue requirements. | Hary Irfantri |
| `v0.1.0` | `2026-11-22` | Pre-Release | Initial draft establishing the Primary Brand Palette (`HEX`, `RGB`, and `ISO` Coated v2 `CMYK`), Neutral Scale, Semantic Status Palette (`#A42332` Danger), proportional usage ratios, `WCAG` 2.2 Level AA contrast rules, and non-color status cue requirements. | Hary Irfantri |
