# Irvantri Standards — Unified Operating Library Index

| Field | Value |
| :--- | :--- |
| **Register** | `Library-Index.md` *(Uncoded master register)* |
| **Entity** | Irvantri Standards |
| **Version** | `v1.2.14` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-20` |
| **Last Updated** | `2026-11-27` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Governing Rules** | `A01` (Document Control), `A02` (Taxonomy & Naming) |

---

## 1. Purpose & Scope

This register is the authoritative directory of the **Irvantri Standards Unified Operating Library**. It tracks every normative standard, master asset, executable template, compiled publication, and governance record across the organization, and references the internal third-party dependency manifest (`06_Dependencies/Dependencies-Manifest.md`).

### In Scope
* **Normative Standards (`A01`–`H99`):** Reusable, testable company-wide rules. Strictly one code per standalone Markdown file.
* **Master Assets (`AST-`) & Executable Templates (`TPL-`):** Production files directly governed by an active standard.
* **Compiled Publications (`PUB-`):** Human-facing handbooks or portals synthesized from normative standards.
* **Governance Records (`REC-`):** Dated consistency reviews, audit logs, and approved exception waivers.
* **Third-Party Dependencies (`06_Dependencies/`):** Unmodified externally licensed packages and binaries (typeface suites and International Color Consortium (`ICC`) profiles) tracked in `06_Dependencies/Dependencies-Manifest.md` per `A02 §5.5.4`.

### Out of Scope
* Statutory regulations, external standards, and client contracts (sit above this library in precedence).
* Product specifications, feature Product Requirement Documents (`PRD`s), client briefs, and project deliverables (consume standards without living in this register).
* Fast-changing operational runbooks, tool click-paths, and task checklists.
* Transient business records, meeting notes, invoices, and active work-in-progress.

---

## 2. Authority & Precedence

*Summarized from `A01 §5.1.4`; `A01` is authoritative.*

Where two controlled items conflict, precedence resolves strictly from top to bottom:
1. **Statutory, regulatory, and contractual obligations.**
2. **Series `A` (Governance & Traceability)** — governs how all other standards are created, amended, verified, and waived.
3. **Normative Standards (`B`–`H`)** — where two standards overlap, the more specific standard prevails and the conflict is logged under `A04`.
4. **Master Assets & Executable Templates (`AST-`, `TPL-`)** — authoritative for physical and visual execution; any drift from a governing standard is flagged `Sync Required` and reconciled per `A04 §5.2.1`.
5. **Compiled Publications (`PUB-`)** — informative reference copies; never override their underlying normative standards.
6. **Project & Product Specifications** — SHALL conform to applicable standards unless backed by a time-boxed waiver logged under `A04`.

---

## 3. Series Overview

| Series | Domain | Phase | Allocation |
| :--- | :--- | :--- | :--- |
| **A** | Governance & Traceability | Active | `A01`–`A04` |
| **B** | Visual Foundations | Active | `B01`–`B05` |
| **C** | Information & Verbal Standards | Active | `C01`–`C04` |
| **D** | Digital Systems & Interfaces | Active | `D01`–`D05` |
| **E** | Formal Documents & Print | Active | `E01`–`E04` |
| **F** | Systems & Engineering | Reserved | Activated when operational need justifies formal standards |
| **G** | Processes & Delivery | Reserved | Activated when operational need justifies formal standards |
| **H** | Quality, Security & Information Integrity | Reserved | Activated when operational need justifies formal standards |

*Letters `I` onward remain unallocated for future expansion. Retired codes are locked permanently and never reused.*

---

## 4. Normative Standards Register

**Controlled Status Values:** `Planned` · `Draft` · `In Review` · `Approved` · `Deprecated`

### Series A — Governance & Traceability
| Code | Standard | File | Version | Status | Owner | Next Review | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `A01` | Document Control & Lifecycle | `01_Standards/A_Governance/A01_Document-Control.md` | `v1.2.0` | `Approved` | Hary Irfantri | `2027-05-20` | Ownership, approval, versioning (`vMAJOR.MINOR.ERRATA`), normative keywords, `Governs` header rule, Section 7 errata syncs, archival, register sync rules |
| `A02` | Taxonomy, Coding & File Naming | `01_Standards/A_Governance/A02_Taxonomy-and-Naming.md` | `v1.3.0` | `Approved` | Hary Irfantri | `2027-05-20` | Series `A`–`H`, `CODE_Title-Words.ext`, extensionless Cloud-Native Office Files (`§5.4.6`, `§5.6.3`), English Title Case, artifact prefixes, `06_Dependencies/` third-party package boundary, retirement, library citations |
| `A03` | Entity & Brand Architecture | `01_Standards/A_Governance/A03_Entity-and-Brand-Architecture.md` | `v1.1.1` | `Approved` | Hary Irfantri | `2027-05-20` | `Irvantri Standards Pte. Ltd.`, `Irvantri Group Pte. Ltd.`, Branded House model, Endorsement Line, co-branding, legal attribution |
| `A04` | Compliance, Reviews & Exceptions | `01_Standards/A_Governance/A04_Compliance-and-Exceptions.md` | `v1.1.1` | `Approved` | Hary Irfantri | `2027-05-20` | Consistency audits, Section 6 conformance verification, non-conformity Service Level Agreements (`SLA`s), cross-standard conflicts, time-boxed waivers, `REC-` retention |

### Series B — Visual Foundations
| Code | Standard | File | Version | Status | Owner | Next Review | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `B01` | Marks & Lockups | `01_Standards/B_Visual-Foundations/B01_Marks-and-Lockups.md` | `v2.0.0` | `Approved` | Hary Irfantri | `2027-05-22` | Symbols, lockups, `260 px`/`64 mm` Parent-Endorsed Lockup minimums, clear space, co-branding, misuse; `AST-B01-01`–`AST-B01-04` Approved (Noto Sans curve-outlined lockups synced `2026-11-26`) |
| `B02` | Color System | `01_Standards/B_Visual-Foundations/B02_Color-System.md` | `v1.1.1` | `Approved` | Hary Irfantri | `2027-05-22` | Core, neutral (with `Surface Tint` and `Border Subtle`), and 5-state semantic palettes (Hexadecimal (`HEX`), Red-Green-Blue (`RGB`), Cyan-Magenta-Yellow-Key (`CMYK`)), usage ratios, contrast |
| `B03` | Typography | `01_Standards/B_Visual-Foundations/B03_Typography.md` | `v2.0.0` | `Approved` | Hary Irfantri | `2027-05-26` | Unified Noto Sans superfamily (`Noto Sans Display`, `Noto Sans`, `Noto Sans Mono`, `SIL OFL-1.1`), `Dependencies-Manifest.md` logging, Desktop/Mobile role type scale, uppercase restraint, fallbacks, tabular legibility |
| `B04` | Grids, Spacing & Graphic Devices | `01_Standards/B_Visual-Foundations/B04_Grids-and-Graphic-Devices.md` | `v1.2.0` | `Approved` | Hary Irfantri | `2027-05-22` | Layout geometry, spacing scales, `12 px` Compact touch spacing, border radii, neutral elevation, horizontal or `4 mm` vertical spine cover accent bar, dense work-surface ornament ban |
| `B05` | Iconography, Diagrams & Visuals | `01_Standards/B_Visual-Foundations/B05_Iconography-and-Visuals.md` | `v1.1.0` | `Approved` | Hary Irfantri | `2027-05-22` | Icon grid, technical schematics, charts, photography, illustration, `300 ms` motion guideline & objective flashing/erratic-motion limits |

### Series C — Information & Verbal Standards
| Code | Standard | File | Version | Status | Owner | Next Review | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `C01` | Voice, Tone & Plain Language | `01_Standards/C_Information-and-Verbal/C01_Voice-Tone-and-Plain-Language.md` | `v1.1.1` | `Approved` | Hary Irfantri | `2027-05-22` | Editorial posture, tone register matrix, plain-language rules, objectivity, approved company descriptions, United States English (`en-US`) mechanics |
| `C02` | Terminology & Controlled Vocabulary | `01_Standards/C_Information-and-Verbal/C02_Terminology-and-Vocabulary.md` | `v1.1.0` | `Approved` | Hary Irfantri | `2027-05-22` | Shared library glossary, acronym expansion exemptions, `Tier 2`/`Tier 3` offering register (including `Irvantri Standards Design System`), controlled status vocabularies, and prohibited terms |
| `C03` | Technical & User Experience (`UX`) Writing | `01_Standards/C_Information-and-Verbal/C03_Technical-and-UX-Writing.md` | `v1.0.1` | `Approved` | Hary Irfantri | `2027-05-22` | User Interface (`UI`) copy, sentence-case microcopy, error messages, confirmations, empty states, and procedural writing (normative keywords governed by `A01 §5.3`) |
| `C04` | Data, Dates & Citation Formatting | `01_Standards/C_Information-and-Verbal/C04_Data-Dates-and-Citations.md` | `v1.0.1` | `Approved` | Hary Irfantri | `2027-05-22` | International Organization for Standardization (`ISO`) 8601 dates/timestamps, units, tables, numbering, and external/bibliographic citations (complements `A02 §5.7`) |

### Series D — Digital Systems & Interfaces
| Code | Standard | File | Version | Status | Owner | Next Review | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `D01` | Design Tokens & Architecture | `01_Standards/D_Digital-Systems/D01_Design-Tokens.md` | `v1.0.3` | `Approved` | Hary Irfantri | `2027-05-22` | Semantic token naming, theming, design-to-code synchronization, `AST-D01-01` Approved and synced to `B03 (v2.0.0)` |
| `D02` | Responsive Shells & Navigation | `01_Standards/D_Digital-Systems/D02_Responsive-Shells-and-Navigation.md` | `v2.0.1` | `Approved` | Hary Irfantri | `2027-05-22` | Breakpoints, `320 px` reflow floor, tenant/parent brand separation, headers, sidebars, structural layouts |
| `D03` | Interface Components & Patterns | `01_Standards/D_Digital-Systems/D03_Interface-Components.md` | `v2.0.0` | `Approved` | Hary Irfantri | `2027-05-22` | Inputs, forms, blur/submit validation, `320 px`–`767 px` Compact table cards, provenance callouts, `C02`-aligned lifecycle statuses & distinct domain flags, dialogs, operational interface discipline |
| `D04` | Accessibility & Usability | `01_Standards/D_Digital-Systems/D04_Accessibility-and-Usability.md` | `v1.2.1` | `Approved` | Hary Irfantri | `2027-05-22` | Web Content Accessibility Guidelines (`WCAG`) conformance targets, `12 px` Compact touch spacing, `3 px` Focus Indicator default, keyboard navigation, Accessible Rich Internet Applications (`ARIA`) rules |
| `D05` | Generated Outputs & Exports | `01_Standards/D_Digital-Systems/D05_Generated-Outputs-and-Exports.md` | `v1.1.1` | `Approved` | Hary Irfantri | `2027-05-22` | System-generated documents, Comma-Separated Values (`CSV`) and Portable Document Format (`PDF`) exports, Coordinated Universal Time (`UTC`) storage/local display, explicit export triggers, `Draft`/`In Review` export marking |

### Series E — Formal Documents & Print
| Code | Standard | File | Version | Status | Owner | Next Review | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `E01` | Formal Document Layout | `01_Standards/E_Documents-and-Print/E01_Formal-Document-Layout.md` | `v2.2.0` | `Approved` | Hary Irfantri | `2027-05-26` | Cover geometry (horizontal or `4 mm` vertical spine accent bar), `B03`-decoupled Display Typeface rule, metadata panels, headers, footers, pagination, interactive `HTML` authoring masters (`§5.3.3`), Digital Distribution `PDF` Profile (`§5.4`, including `≥ 300 DPI` lossless `PNG` marks on Cloud-Native Office File exports); governs `TPL-E01-01`–`04` (all `4` Approved) |
| `E02` | Versioning & Draft Marking | `01_Standards/E_Documents-and-Print/E02_Versioning-and-Draft-Marking.md` | `v1.1.0` | `Approved` | Hary Irfantri | `2027-05-23` | Semantic version display, `C02` status badges, non-approved banners, `B03`-decoupled Display Typeface watermarks, waiver disclosures, archival marking |
| `E03` | Print & Production Specifications | `01_Standards/E_Documents-and-Print/E03_Print-and-Production-Specifications.md` | `v1.0.0` | `Approved` | Hary Irfantri | `2027-05-23` | A4 trim, `4 mm`/`16 mm`/`20 mm` margins, `3 mm` bleed, `100`–`250 g/m²` stocks, `ISO` Coated v2 `CMYK`, `PDF/X-4` prepress, Owner color proofs |
| `E04` | Correspondence & Presentations | `01_Standards/E_Documents-and-Print/E04_Correspondence-and-Presentations.md` | `v2.1.1` | `Approved` | Hary Irfantri | `2027-05-26` | A4 print and digital letterheads/memos (`E01 §5.4`), `16:9` slide masters (`B03` Display/Text roles), six-line corporate email signatures, `C01` boilerplates, operational spreadsheets and workbooks (`§5.5`); governs `TPL-E04-01`–`03` (`01`/`03` Approved, `02` `Planned`) |

---

## 5. Master Assets & Executable Templates Register

**Controlled Status Values:** `Planned` · `Approved` · `Sync Required` · `Deprecated`

| Code | Type | File | Governing Standard | Pinned Version | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AST-B01-01` | Master Asset | `02_Assets/AST-B01-01_Primary-Symbol.svg` | `B01` | `B01 (v2.0)` | `Approved` | Full-color primary emblem master (`28 px` / `12 mm` minimum, `#074C96` & `#DE0029`; re-pinned `2026-11-25`) |
| `AST-B01-02` | Master Asset | `02_Assets/AST-B01-02_White-Symbol.svg` | `B01` | `B01 (v2.0)` | `Approved` | Reversed single-color `#FFFFFF` symbol master for dark surfaces (re-pinned `2026-11-25`) |
| `AST-B01-03` | Master Asset | `02_Assets/AST-B01-03_Parent-Lockup.svg` | `B01` | `B01 (v2.0)` | `Approved` | Full-color `664 × 160` (`4.15:1`) curve-outlined Parent-Endorsed Lockup for light surfaces (`260 px` / `64 mm` minimum, `9.26 px` / `6.46 pt` Endorsement Line cap height; synced to `B03 v2.0.0` Noto Sans and Approved `2026-11-26`) |
| `AST-B01-04` | Master Asset | `02_Assets/AST-B01-04_Parent-Lockup-White.svg` | `B01` | `B01 (v2.0)` | `Approved` | Reversed `#FFFFFF` `664 × 160` (`4.15:1`) curve-outlined Parent-Endorsed Lockup for dark surfaces (`260 px` / `64 mm` minimum, `9.26 px` / `6.46 pt` Endorsement Line cap height; synced to `B03 v2.0.0` Noto Sans and Approved `2026-11-26`) |
| `AST-D01-01` | Master Asset | `02_Assets/AST-D01-01_Design-Tokens.json` | `D01` | `D01 (v1.0)` | `Approved` | Canonical single-source design token schema generating `CSS` custom properties (Approved `2026-11-24`; synced `2026-11-27` to `B03 v2.0.0` Noto font stacks and `B01 v2.0.0` / `E01 v2.2.0` / `E02 v1.1.0` metadata) |
| `TPL-E01-01` | Executable Template | `03_Templates/TPL-E01-01_Header-and-Footer-Print.pdf` | `E01` | `E01 (v2.0)` | `Approved` | Press-ready A4 running header and footer template (`E03` `PDF/X-4`, `FOGRA39` / `ISO` Coated v2 `CMYK`, `2 mm` full-bleed top `24%` / `76%` split accent bar with `3 mm` bleed and `3 mm`-offset `100%` K crop marks, `20 mm` L/R and `16 mm` T/B Safe Margins, rule-free header with `72 mm` curve-outlined `AST-B01-03` lockup and `C02` `Approved` badge, ultra-clean single-line footer with `[v1.0.0]` monospace version and `Page [X] of [Y]`, embedded `B03 (v2.0.0)` Noto fonts; pair with `E01` cover/colophon for `A03 §5.6.1` copyright; revised and Approved `2026-11-26`) |
| `TPL-E01-02` | Executable Template | `03_Templates/TPL-E01-02_Formal-Cover-Print.pdf` | `E01` | `E01 (v2.0)` | `Approved` | Press-ready A4 cover template (`E03` `PDF/X-4`, `FOGRA39` / `ISO` Coated v2 `CMYK`, `3 mm` bleed and `3 mm`-offset `100%` K crop marks, `24 mm` inner / `20 mm` outer margins, embedded `B03 (v2.0.0)` Noto fonts, `80 mm` `AST-B01-03` lockup, and `4 mm` `76%` / `24%` vertical left-spine bar; recompiled and Approved `2026-11-26`) |
| `TPL-E01-03` | Executable Template | `03_Templates/TPL-E01-03_Formal-Cover-Digital.html` | `E01` | `E01 (v2.2)` | `Approved` | Editable interactive `HTML`/`CSS` A4 cover authoring master (`E01 §5.3.3`, `§5.4` `sRGB` `PDF` export, zero bleed/crop marks, `24 mm` inner / `20 mm` outer margins, `16 mm` T/B Safe Margins, `4 mm` `76%` / `24%` vertical left-spine bar, `80 mm` curve-outlined `AST-B01-03` lockup, local `06_Dependencies/Fonts/` `B03 (v2.0.0)` Noto fonts, non-printing browser authoring bar with `contenteditable` fields, `C02` status switcher, `E02` banners/waiver controls, live preflight, and `@media print` A4 `PDF` export; upgraded from static `PDF` and Approved `2026-11-27`) |
| `TPL-E01-04` | Executable Template | `03_Templates/TPL-E01-04_Header-and-Footer-Digital.pdf` | `E01` | `E01 (v2.0)` | `Approved` | Digital A4 running header and footer template (`E01 §5.4` `sRGB`, zero bleed/crop marks, `2 mm` top-edge `24%` / `76%` split accent bar, `20 mm` L/R and `16 mm` T/B Safe Margins, rule-free header with `72 mm` curve-outlined `AST-B01-03` lockup and `C02` `Approved` badge, ultra-clean single-line footer with `[v1.0.0]` monospace version and `Page [X] of [Y]`, embedded `B03 (v2.0.0)` Noto fonts, selectable live text; pair with `E01` cover/colophon for `A03 §5.6.1` copyright; revised and Approved `2026-11-26`) |
| `TPL-E04-01` | Executable Template | `03_Templates/TPL-E04-01_Official-Letterhead-Print.pdf` | `E04` | `E04 (v2.0)` | `Approved` | Press-ready A4 official letterhead (`E03` `PDF/X-4`, `FOGRA39` / `ISO` Coated v2 `CMYK`, `2 mm` full-bleed top `24%` / `76%` split accent bar with `3 mm` bleed and `3 mm`-offset `100%` K crop marks, `20 mm` L/R and `16 mm` T/B Safe Margins, rule-free header with `72 mm` curve-outlined `AST-B01-03` lockup and `ISO` 8601 Date/Reference block, rule-free stationery footer with `A03` attribution, embedded `B03 (v2.0.0)` Noto fonts; print on `≥ 120 g/m²` archival stock; Approved `2026-11-26`) |
| `TPL-E04-02` | Executable Template | `03_Templates/TPL-E04-02_Presentation-Master.html` | `E04` | `E04 (v2.1)` | `Planned` | `16:9` widescreen concise pitch deck master (`HTML/CSS` to `sRGB` `PDF`, `E04 §5.2`, `E01 §5.4`) with minimalist `B03` Display/Text hierarchy, `B02` palette, and cover/closing attribution slides |
| `TPL-E04-03` | Executable Template | `03_Templates/TPL-E04-03_Official-Letterhead-Digital.pdf` | `E04` | `E04 (v2.0)` | `Approved` | Digital A4 official letterhead (`E01 §5.4` `sRGB`, zero bleed/crop marks, `2 mm` top-edge `24%` / `76%` split accent bar, `20 mm` L/R and `16 mm` T/B Safe Margins, rule-free header with `72 mm` curve-outlined `AST-B01-03` lockup and `ISO` 8601 Date/Reference block, rule-free stationery footer with `A03` attribution, embedded `B03 (v2.0.0)` Noto fonts, live selectable text; Approved `2026-11-26`) |

---

## 6. Compiled Publications Register

**Controlled Status Values:** `Planned` · `Approved` · `Sync Required` · `Deprecated`

| Code | Publication | File | Compiled Date | Source Manifest | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `PUB-01` | Brand and Design System Guide (`v2.0.2`) | `04_Publications/PUB-01_Brand-and-Design-System-Guide.html` | `2026-11-27` | `A01 (v1.2.0)`, `A02 (v1.3.0)`, `A03 (v1.1.1)`, `A04 (v1.1.1)`, `B01 (v2.0.0)`, `B02 (v1.1.1)`, `B03 (v2.0.0)`, `B04 (v1.2.0)`, `B05 (v1.1.0)`, `C01 (v1.1.1)`, `C02 (v1.1.0)`, `C03 (v1.0.1)`, `C04 (v1.0.1)`, `D01 (v1.0.3)`, `D02 (v2.0.1)`, `D03 (v2.0.0)`, `D04 (v1.2.1)`, `D05 (v1.1.1)`, `E01 (v2.2.0)`, `E02 (v1.1.0)`, `E03 (v1.0.0)`, `E04 (v2.1.1)`, `AST-B01-01`–`AST-B01-04`, `AST-D01-01`, `TPL-E01-01`–`TPL-E01-04`, `Dependencies-Manifest.md (v2.0.0)`, `Library-Index.md (v1.2.14)` | `Approved` | Refreshed to `v2.0.2` (`2026-11-27`) with synchronized AST-D01-01 E01 source metadata and corrected build metadata |
| `PUB-02` | Company Overview (`v2.0.1`) | `04_Publications/PUB-02_Company-Overview.md` | `2026-11-27` | `A01 (v1.2.0)`, `A02 (v1.3.0)`, `A03 (v1.1.1)`, `A04 (v1.1.1)`, `B01 (v2.0.0)`, `B02 (v1.1.1)`, `B03 (v2.0.0)`, `B04 (v1.2.0)`, `B05 (v1.1.0)`, `C01 (v1.1.1)`, `C02 (v1.1.0)`, `C03 (v1.0.1)`, `C04 (v1.0.1)`, `D01 (v1.0.3)`, `D02 (v2.0.1)`, `D03 (v2.0.0)`, `D04 (v1.2.1)`, `D05 (v1.1.1)`, `E01 (v2.2.0)`, `E02 (v1.1.0)`, `E03 (v1.0.0)`, `E04 (v2.1.1)`, `AST-B01-01`–`AST-B01-04`, `AST-D01-01`, `TPL-E01-01`–`TPL-E01-04`, `PUB-01 (v2.0.2)`, `Dependencies-Manifest.md (v2.0.0)`, `Library-Index.md (v1.2.14)` | `Approved` | Refreshed to `v2.0.1` (`2026-11-27`) with current governing-standard and register citations |
| `PUB-03` | AI Design System Context (`v1.1.1`, `DESIGN.md`) | `04_Publications/PUB-03_AI-Design-System-Context.md` | `2026-11-27` | `A01 (v1.2.0)`, `A02 (v1.3.0)`, `A03 (v1.1.1)`, `A04 (v1.1.1)`, `B01 (v2.0.0)`, `B02 (v1.1.1)`, `B03 (v2.0.0)`, `B04 (v1.2.0)`, `B05 (v1.1.0)`, `C01 (v1.1.1)`, `C02 (v1.1.0)`, `C04 (v1.0.1)`, `D01 (v1.0.3)`, `D02 (v2.0.1)`, `D03 (v2.0.0)`, `D04 (v1.2.1)`, `E01 (v2.2.0)`, `E02 (v1.1.0)`, `E04 (v2.1.1)`, `AST-B01-01`–`AST-B01-04`, `AST-D01-01`, `Dependencies-Manifest.md (v2.0.0)`, `Library-Index.md (v1.2.14)` | `Approved` | Refreshed to `v1.1.1` (`2026-11-27`) with current E01, E04, and Library-Index citations |

---

## 7. Governance Records Register

**Controlled Status Values:** `Open` · `Approved` · `Rejected` · `Expired` · `Revoked` · `Closed`

| Code | Record | File | Date | Related Standard | Status | Expiry Date | Summary |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `REC-A04-001` | Initial Consistency Review | `05_Records/REC-A04-001_Initial-Consistency-Review.md` | `2026-11-22` | `A01`, `A02`, `A03`, `A04`, `C01` | `Closed` | `None` | Initial Year-1 review and cross-standard conflict log (`F-01`–`F-09`); all findings verified closed via `v1.1.0` releases |
| `REC-A04-002` | Series C Milestone Consistency Review | `05_Records/REC-A04-002_Series-C-Milestone-Review.md` | `2026-11-22` | `A01`, `A02`, `A03`, `A04`, `C01`, `C02`, `C03`, `C04` | `Closed` | `None` | Series C completion audit across all 8 Approved standards (`A01`–`A04`, `C01`–`C04`) and 64 active checks; zero non-conformities or cross-standard conflicts found |
| `REC-A04-003` | Series B Milestone Consistency Review | `05_Records/REC-A04-003_Series-B-Milestone-Review.md` | `2026-11-22` | `A01`, `A02`, `A03`, `A04`, `B01`, `B02`, `B03`, `B04`, `B05`, `C01`, `C02`, `C03`, `C04` | `Closed` | `None` | Series B completion audit across all 13 Approved standards (`A01`–`A04`, `B01`–`B05`, `C01`–`C04`) and 90 active checks; zero non-conformities or cross-standard conflicts found |
| `REC-A04-004` | Series D & E Milestone Consistency Review | `05_Records/REC-A04-004_Series-D-and-E-Milestone-Review.md` | `2026-11-23` | `A01`–`A04`, `B01`–`B05`, `C01`–`C04`, `D01`–`D05`, `E01`–`E04` | `Closed` | `None` | Full-library Series D & E completion audit across all 22 Approved standards and 121 active checks (`F-01`–`F-04`); all findings verified closed via `D01`–`D03`, `D05`, `E01` (`v1.0.1`) and `D04` (`v1.1.0`) |
| `REC-A04-005` | Full-Library Audit & D02/D03 Event-Driven Review | `05_Records/REC-A04-005_Full-Library-Audit-and-D02-Event-Review.md` | `2026-11-25` | `A01`–`A04`, `B01`–`B05`, `C01`–`C04`, `D01`–`D05`, `E01`–`E04` | `Closed` | `None` | Full-library audit (`F-01`–`F-10`) and `D02 (v2.0.0)` / `D03 (v2.0.0)` event-driven reviews; retired `Conformance-Checklist.md` to `99_Archive/`, archived `A01 v1.1.0`, `D03 v1.1.0`, and `B05 v1.0.0`, published `AST-B01-01`/`AST-B01-02`, synced `AST-D01-01` and `PUB-01 (v1.0.0)`, and verified all 10 findings and 19 review rows closed |
| `REC-A04-006` | B01 v2.0.0 Conflict Resolution & Event-Driven Audit | `05_Records/REC-A04-006_B01-v2-Event-Driven-Audit.md` | `2026-11-25` | `A03`, `B01`, `B02`, `B03`, `B04`, `B05`, `D02`, `E01`, `E03`, `E04` | `Closed` | `None` | Closed cross-clause conflict `F-01` (`U-01`) via `B01 (v2.0.0)` (`260 px` / `64 mm` minimums), verified all 9 citing standards and `AST-B01-01`–`AST-B01-04` (`B01 (v2.0)`), and verified `F-02` closed via `PUB-01 (v2.0.0)` and `PUB-02 (v2.0.0)` on `2026-11-26` |
| `REC-A04-007` | B03 v2.0.0 Typography Migration Event-Driven Audit | `05_Records/REC-A04-007_B03-v2-Typography-Migration-Audit.md` | `2026-11-26` | `A01`, `A02`, `A03`, `A04`, `B01`, `B03`, `D01`, `E01`, `E02`, `E03`, `E04` | `Closed` | `None` | Verified `B03 (v2.0.0)` Noto Sans superfamily migration, paired `E01`/`E02`/`E04` decoupling releases, `AST-D01-01` and `Dependencies-Manifest.md (v2.0.0)` sync, and full closure of `F-01` (`AST-B01-03`/`04`), `F-02` (`TPL-E01-02`/`03`), and `F-03` (`PUB-01`/`PUB-02 v2.0.0`) on `2026-11-26` |

---

## 8. Third-Party Dependencies Reference

*Authoritative package inventory, rights holders, licenses, and checksums reside in `06_Dependencies/Dependencies-Manifest.md` (`v2.0.0`, `Approved`, governed by `A02 §5.5.4` and `A03 §5.6.2`).*

| Category | Directory | Packages / Files | Governing Standards | License / Scope |
| :--- | :--- | :--- | :--- | :--- |
| **Brand Typefaces** | `06_Dependencies/Fonts/` | `3` packages (`Noto Sans Display/`, `Noto Sans/`, `Noto Sans Mono/` — static template binaries + `OFL.txt`) | `B03` | `SIL OFL-1.1` |
| **Print Color Profiles** | `06_Dependencies/Color-Profiles/` | `1` profile (`ISOcoated_v2_eci.icc`) | `B02`, `E03` | European Color Initiative (`ECI`) / Heidelberger Druckmaschinen AG (`ISO Coated v2 (ECI)`, internal prepress & `PDF/X-4` OutputIntent only) |

---

## 9. Coverage Summary

| Status | Count | Codes |
| :--- | :--- | :--- |
| **Approved** | `22` | `A01`, `A02`, `A03`, `A04`, `B01`, `B02`, `B03`, `B04`, `B05`, `C01`, `C02`, `C03`, `C04`, `D01`, `D02`, `D03`, `D04`, `D05`, `E01`, `E02`, `E03`, `E04` |
| **In Review** | `0` | `—` |
| **Draft** | `0` | `—` |
| **Planned** | `0` | `—` |
| **Deprecated** | `0` | `—` |
| **Reserved Series** | `3` | `F`, `G`, `H` |

---

## 10. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v1.2.14` | `2026-11-27` | Errata | Synchronized `AST-D01-01` to `E01 (v2.2.0)`, updated its generated date, and refreshed `PUB-01` to `v2.0.2` with aligned build metadata. | Hary Irfantri |
| `v1.2.13` | `2026-11-27` | Errata | Refreshed `PUB-01` to `v2.0.1`, `PUB-02` to `v2.0.1`, and `PUB-03` to `v1.1.1`; synchronized their governing standards and register references to `A02 (v1.3.0)`, `E01 (v2.2.0)`, `E04 (v2.1.1)`, and `Library-Index.md (v1.2.13)` in Section 6. | Hary Irfantri |
| `v1.2.12` | `2026-11-27` | Errata | Synced `E01` (`v2.2.0`, `MINOR`, permitting standalone interactive `HTML` authoring masters under `§5.3.3`) in Section 4 and promoted `TPL-E01-03` (`03_Templates/TPL-E01-03_Formal-Cover-Digital.html`, pinned to `E01 (v2.2)`) in Section 5 following archival of outgoing `E01_Formal-Document-Layout_v2.1.1.md` and `TPL-E01-03_Formal-Cover-Digital_v2.0.0.pdf` to `99_Archive/` per `A01 §5.5.6`, `§5.7.2`, and `§5.8.1`. | Hary Irfantri |
| `v1.2.11` | `2026-11-26` | Errata | Synced `PUB-03` (`04_Publications/PUB-03_AI-Design-System-Context.md`, `v1.1.0`, `Approved`, external deployment filename `DESIGN.md`) in Section 6 following `@google/design.md` / Superdesign YAML frontmatter update, Superdesign parser confirmation, and archival of outgoing `PUB-03_AI-Design-System-Context_v1.0.0.md` to `99_Archive/` per `A01 §5.5.6`, `§5.7.2`, `§5.7.5`, and `§5.8.1`. | Hary Irfantri |
| `v1.2.10` | `2026-11-26` | Errata | Registered `PUB-03` (`04_Publications/PUB-03_AI-Design-System-Context.md`, `v1.0.0`, `Approved`, external deployment filename `DESIGN.md`) in Section 6 following Pre-Release Gate verification and Approver approval per `A01 §5.5.6`, `§5.7.5`, and `§5.8.1`. | Hary Irfantri |
| `v1.2.9` | `2026-11-26` | Errata | Synced `E01` (`v2.1.1`, `ERRATA`) and `E04` (`v2.1.1`, `ERRATA`) in Section 4; removed cancelled `Planned` Google Workspace rows (`TPL-E01-05`, `TPL-E04-04`, `TPL-E04-05`) and aligned `TPL-E04-02` (`Planned`) to `HTML/CSS` to `sRGB` `PDF` concise pitch deck scope in Section 5 following Approver cancellation of the Google Workspace template migration (`A01 §5.5.6`, `§5.5.7`, `§5.8.1`, `A02 §5.3.1`). | Hary Irfantri |
| `v1.2.8` | `2026-11-26` | Errata | Synced approved `MINOR` Google Workspace integration releases `A02` (`v1.3.0`, Cloud-Native Office File naming and archival), `E01` (`v2.1.0`, `≥ 300 DPI` lossless `PNG` marks on Cloud-Native Office File digital `PDF` exports), and `E04` (`v2.1.0`, operational workbooks `§5.5`) in Section 4; registered `TPL-E01-05` (`Google Docs`, `Planned`), `TPL-E04-04` (`Google Docs`, `Planned`), and `TPL-E04-05` (`Google Sheets`, `Planned`) and aligned `TPL-E04-02` (`Google Slides`, `Planned`, `E04 (v2.1)`) in Section 5 following archival of outgoing snapshots to `99_Archive/` per `A01 §5.5.6`, `§5.7.2`, and `§5.8.1`. | Hary Irfantri |
| `v1.2.7` | `2026-11-26` | Errata | Synced `E04` (`v2.0.1`, `ERRATA`) in Section 4 and promoted `TPL-E04-01` (`03_Templates/TPL-E04-01_Official-Letterhead-Print.pdf`) and `TPL-E04-03` (`03_Templates/TPL-E04-03_Official-Letterhead-Digital.pdf`), both pinned to `E04 (v2.0)`, from `Planned` to `Approved` in Section 5 per `A01 §5.5.6`, `§5.5.7`, and `§5.8.1`. | Hary Irfantri |
| `v1.2.6` | `2026-11-26` | Errata | Synced `E01` (`v2.0.3`, `ERRATA`) in Section 4 and updated `TPL-E01-01` (`03_Templates/TPL-E01-01_Header-and-Footer-Print.pdf`) and `TPL-E01-04` (`03_Templates/TPL-E01-04_Header-and-Footer-Digital.pdf`) notes in Section 5 following minimalist layout revision (`2 mm` full-bleed top `24%` / `76%` split accent bar, rule-free header and single-line footer, `3 mm` Print bleed/crop marks) and archival of outgoing `v1.0.0` snapshots per `A01 §5.5.6`, `§5.5.7`, `§5.7.2`, and `§5.8.1`. | Hary Irfantri |
| `v1.2.5` | `2026-11-26` | Errata | Promoted `PUB-01` (`04_Publications/PUB-01_Brand-and-Design-System-Guide.html`, `v2.0.0`) and `PUB-02` (`04_Publications/PUB-02_Company-Overview.md`, `v2.0.0`) from `Sync Required` to `Approved` in Section 6 following archival of outgoing `v1.0.0` snapshots to `99_Archive/`; transitioned `REC-A04-006` (`F-02` closed) and `REC-A04-007` (`F-03` closed) to immutable terminal `Closed` status in Section 7 per `A01 §5.5.6`, `§5.8.1`, and `A04 §5.5.2`–`§5.5.3`. | Hary Irfantri |
| `v1.2.4` | `2026-11-26` | Errata | Synced `E01` (`v2.0.2`, `ERRATA`) in Section 4; restored `TPL-E01-02` (`03_Templates/TPL-E01-02_Formal-Cover-Print.pdf`) and `TPL-E01-03` (`03_Templates/TPL-E01-03_Formal-Cover-Digital.pdf`) from `Sync Required` to `Approved` and re-pinned both to `E01 (v2.0)` in Section 5 following `B03 (v2.0.0)` Noto Sans recompilation and archival of outgoing `v1.0.0` snapshots; and logged `F-02` closure in `REC-A04-007` (Section 7) per `A01 §5.5.6`, `§5.5.7`, `§5.8.1`, and `A04 §5.5.2`. | Hary Irfantri |
| `v1.2.3` | `2026-11-26` | Errata | Restored `AST-B01-03` (`02_Assets/AST-B01-03_Parent-Lockup.svg`) and `AST-B01-04` (`02_Assets/AST-B01-04_Parent-Lockup-White.svg`), both pinned to `B01 (v2.0)`, from `Sync Required` to `Approved` in Section 5 following `B03 (v2.0.0)` Noto Sans curve-outlined rebuild and archival of outgoing `v1.0.0` snapshots; updated `B01` notes in Section 4 and logged `F-01` closure in `REC-A04-007` (Section 7) per `A01 §5.5.6`, `§5.8.1`, and `A04 §5.5.2`. | Hary Irfantri |
| `v1.2.2` | `2026-11-26` | Errata | Synced `E01` (`v2.0.1`, `ERRATA`) in Section 4 and promoted `TPL-E01-01` (`03_Templates/TPL-E01-01_Header-and-Footer-Print.pdf`) and `TPL-E01-04` (`03_Templates/TPL-E01-04_Header-and-Footer-Digital.pdf`), both pinned to `E01 (v2.0)`, from `Planned` to `Approved` in Section 5 per `A01 §5.5.6`, `§5.5.7`, and `§5.8.1`. | Hary Irfantri |
| `v1.2.1` | `2026-11-26` | Errata | Synced `B03 (v2.0.0)` (`MAJOR` Noto Sans superfamily migration), `E01 (v2.0.0)` (`MAJOR`), `E02 (v1.1.0)` (`MINOR`), and `E04 (v2.0.0)` (`MAJOR`) in Section 4; synced `AST-D01-01` (`Approved`), re-pinned `TPL-E01-01`/`04` and `TPL-E04-01`–`03` (`Planned`), and flagged `AST-B01-03`/`04` and `TPL-E01-02`/`03` `Sync Required` in Section 5; flagged `PUB-02` `Sync Required` and updated `PUB-01` notes in Section 6; registered `REC-A04-007` (`Open`) in Section 7; and synced Section 8 to `Dependencies-Manifest.md (v2.0.0)` per `A01 §5.5.6`, `§5.8.1`, and `A04 §5.5.2`. | Hary Irfantri |
| `v1.2.0` | `2026-11-26` | Minor | Added Section 8 (Third-Party Dependencies Reference pointing to `06_Dependencies/Dependencies-Manifest.md`) and updated Section 1 scope per `A02 (v1.2.0) §5.5.4`; synced `A02 (v1.2.0)`, `E01 (v1.2.0)`, and `E04 (v1.1.0)` in Section 4; refined `TPL-E01-01`/`02` and `TPL-E04-01` Title Slugs (`-Print`) per `A02 §5.3.3`; and registered `TPL-E01-03` (`Approved`), `TPL-E01-04` (`Planned`), and `TPL-E04-03` (`Planned`) in Section 5. | Hary Irfantri |
| `v1.1.28` | `2026-11-26` | Errata | Synced `E01` (`v1.1.1`, `ERRATA`) in Section 4 and promoted `TPL-E01-02` (`03_Templates/TPL-E01-02_Formal-Cover.pdf`, pinned to `E01 (v1.1)`) from `Planned` to `Approved` in Section 5 per `A01 §5.5.6`, `§5.5.7`, and `§5.8.1`. | Hary Irfantri |
| `v1.1.27` | `2026-11-25` | Errata | Synced `B04` (`v1.2.0`, `MINOR`, permitting horizontal or `4 mm` vertical left-spine `24%` / `76%` cover accent bar) and `E01` (`v1.1.0`, `MINOR`, aligned cover accent bar orientation) in Section 4; re-pinned `TPL-E01-01` and `TPL-E01-02` to `E01 (v1.1)` in Section 5; and updated `PUB-01`/`PUB-02` sync notes in Section 6 per `A01 §5.5.6`, `§5.7.4`, and `§5.8.1`. | Hary Irfantri |
| `v1.1.26` | `2026-11-25` | Errata | Synced `B01` (`v2.0.0`, `MAJOR`, `260 px` / `64 mm` Parent-Endorsed Lockup minimums) in Section 4; promoted `AST-B01-03` to `Approved`, registered `AST-B01-04` (`Approved`), and re-pinned `AST-B01-01`–`AST-B01-04` to `B01 (v2.0)` in Section 5; flagged `PUB-01` as `Sync Required` in Section 6; and registered `REC-A04-006` (`Open`) in Section 7 per `A01 §5.5.6`, `§5.8.1`, and `A04 §5.5.2`. | Hary Irfantri |
| `v1.1.25` | `2026-11-25` | Errata | Registered `PUB-02` (`04_Publications/PUB-02_Company-Overview.md`, `v1.0.0`, `Approved`, compiled `2026-11-25`) in Section 6 following Pre-Release Gate remediation and Approver sign-off per `A01 §5.5.6` and `§5.8.1`. | Hary Irfantri |
| `v1.1.24` | `2026-11-25` | Errata | Closed `REC-A04-005` (`Closed`) in Section 7; synced Batch B standard releases (`A02`–`A04 v1.1.1`, `B01 v1.0.1`, `B02`/`B04 v1.1.1`, `B05 v1.1.0`, `C01 v1.1.1`, `C03`–`C04 v1.0.1`, `D01 v1.0.3`, `D02 v2.0.1`, `D04 v1.2.1`, `D05 v1.1.1`, `E01 v1.0.2`, `E04 v1.0.1`) in Section 4; promoted `AST-B01-01` and `AST-B01-02` to `Approved` and synced `AST-D01-01` in Section 5; synced `PUB-01 (v1.0.0)` build manifest (`2026-11-25`) in Section 6 per `A01 §5.5.6` and `A04 §5.5.2`. | Hary Irfantri |
| `v1.1.23` | `2026-11-25` | Errata | Synced `A01` (`v1.2.0`) and `D03` (`v2.0.0`) in Section 4, registered `REC-A04-005` (`Open`) in Section 7 recording `Conformance-Checklist.md` retirement to `99_Archive/`, and expanded `UTC` in Section 4 `D05` notes per `A01 §5.5.6` and `A04 §5.5.2`. | Hary Irfantri |
| `v1.1.22` | `2026-11-24` | Errata | Synced `D01` (`v1.0.2`) in Section 4, promoted `AST-D01-01` (`02_Assets/AST-D01-01_Design-Tokens.json`) from `Planned` to `Approved` in Section 5, and registered `PUB-01` (`04_Publications/PUB-01_Brand-and-Design-System-Guide.html`, `v1.0.0`, `Approved`) in Section 6 per `A01 §5.5.6` and `§5.8.1`. | Hary Irfantri |
| `v1.1.21` | `2026-11-24` | Errata | Synced approved design-system upstream revisions in Section 4: `B02` (`v1.1.0`), `B03` (`v1.1.0`), `B04` (`v1.1.0`), `C02` (`v1.1.0`, registering `Irvantri Standards Design System`), `D02` (`v2.0.0`, Major `320 px` reflow floor), `D03` (`v1.1.0`), `D04` (`v1.2.0`), and `D05` (`v1.1.0`) per `A01 §5.5.6`. | Hary Irfantri |
| `v1.1.20` | `2026-11-23` | Errata | Registered `REC-A04-004` (`Closed`) in Section 7 and synced remediation releases `D01`–`D03`, `D05`, `E01` (`v1.0.1`) and `D04` (`v1.1.0`) in Section 4 per `A01 §5.5.6` and `A04 §5.5.2`. | Hary Irfantri |
| `v1.1.19` | `2026-11-23` | Errata | Synced `E04` (`v1.0.0`, `Approved`) in Section 4, registered `TPL-E04-01` and `TPL-E04-02` (`Planned`, pinned to `E04 (v1.0)`) in Section 5, and updated Coverage Summary (`22` Approved, `0` Planned) per `A01 §5.5.6`, completing the active Series A–E baseline. | Hary Irfantri |
| `v1.1.18` | `2026-11-23` | Errata | Synced `E03` (`v1.0.0`, `Approved`) in Section 4 and updated Coverage Summary (`21` Approved, `1` Planned) per `A01 §5.5.6`. | Hary Irfantri |
| `v1.1.17` | `2026-11-23` | Errata | Synced `E02` (`v1.0.0`, `Approved`) in Section 4 and updated Coverage Summary (`20` Approved, `2` Planned) per `A01 §5.5.6`. | Hary Irfantri |
| `v1.1.16` | `2026-11-22` | Errata | Synced `E01` (`v1.0.0`, `Approved`) in Section 4, registered `TPL-E01-01` and `TPL-E01-02` (`Planned`, pinned to `E01 (v1.0)`) in Section 5, and updated Coverage Summary (`19` Approved, `3` Planned) per `A01 §5.5.6`. | Hary Irfantri |
| `v1.1.15` | `2026-11-22` | Errata | Synced `D05` (`v1.0.0`, `Approved`) in Section 4 and updated Coverage Summary (`18` Approved, `4` Planned) per `A01 §5.5.6`, completing the Series D baseline. | Hary Irfantri |
| `v1.1.14` | `2026-11-22` | Errata | Synced `D04` (`v1.0.0`, `Approved`) in Section 4 and updated Coverage Summary (`17` Approved, `5` Planned) per `A01 §5.5.6`. | Hary Irfantri |
| `v1.1.13` | `2026-11-22` | Errata | Synced `D03` (`v1.0.0`, `Approved`) in Section 4 and updated Coverage Summary (`16` Approved, `6` Planned) per `A01 §5.5.6`. | Hary Irfantri |
| `v1.1.12` | `2026-11-22` | Errata | Synced `D02` (`v1.0.0`, `Approved`) in Section 4 and updated Coverage Summary (`15` Approved, `7` Planned) per `A01 §5.5.6`. | Hary Irfantri |
| `v1.1.11` | `2026-11-22` | Errata | Synced `D01` (`v1.0.0`, `Approved`) in Section 4, registered `AST-D01-01` (`Planned`, pinned to `D01 (v1.0)`) in Section 5, and updated Coverage Summary (`14` Approved, `8` Planned) per `A01 §5.5.6`. | Hary Irfantri |
| `v1.1.10` | `2026-11-22` | Errata | Registered `REC-A04-003` (`Closed`) in Section 7 following the Series B milestone consistency review across `A01`–`A04`, `B01`–`B05`, and `C01`–`C04` per `A01 §5.5.6` and `A04 §5.5.2`. | Hary Irfantri |
| `v1.1.9` | `2026-11-22` | Errata | Synced `B05` (`v1.0.0`, `Approved`) in Section 4 and updated Coverage Summary (`13` Approved, `9` Planned) per `A01 §5.5.6`, completing the Series B baseline. | Hary Irfantri |
| `v1.1.8` | `2026-11-22` | Errata | Synced `B04` (`v1.0.0`, `Approved`) in Section 4 and updated Coverage Summary (`12` Approved, `10` Planned) per `A01 §5.5.6`. | Hary Irfantri |
| `v1.1.7` | `2026-11-22` | Errata | Synced `B03` (`v1.0.0`, `Approved`) in Section 4 and updated Coverage Summary (`11` Approved, `11` Planned) per `A01 §5.5.6`. | Hary Irfantri |
| `v1.1.6` | `2026-11-22` | Errata | Synced `B02` (`v1.0.0`, `Approved`) in Section 4 and updated Coverage Summary (`10` Approved, `12` Planned) per `A01 §5.5.6`. | Hary Irfantri |
| `v1.1.5` | `2026-11-22` | Errata | Synced `B01` (`v1.0.0`, `Approved`) in Section 4, registered `AST-B01-01`–`AST-B01-03` (`Planned`, pinned to `B01 (v1.0)`) in Section 5, and updated Coverage Summary (`9` Approved, `13` Planned) per `A01 §5.5.6`. | Hary Irfantri |
| `v1.1.4` | `2026-11-22` | Errata | Registered `REC-A04-002` (`Closed`) in Section 7 following the Series C milestone consistency review across `A01`–`A04` and `C01`–`C04` per `A01 §5.5.6` and `A04 §5.5.2`. | Hary Irfantri |
| `v1.1.3` | `2026-11-22` | Errata | Synced `C04` (`v1.0.0`, `Approved`) in the Normative Standards Register and updated Coverage Summary (`8` Approved, `14` Planned) per `A01 §5.5.6`, completing the Series C baseline. | Hary Irfantri |
| `v1.1.2` | `2026-11-22` | Errata | Synced `C03` (`v1.0.0`, `Approved`) in the Normative Standards Register and updated Coverage Summary (`7` Approved, `15` Planned) per `A01 §5.5.6`. | Hary Irfantri |
| `v1.1.1` | `2026-11-22` | Errata | Synced `C02` (`v1.0.0`, `Approved`) in the Normative Standards Register and updated Coverage Summary (`6` Approved, `16` Planned) per `A01 §5.5.6`. | Hary Irfantri |
| `v1.1.0` | `2026-11-22` | Minor | Added controlled status lists to Sections 6–7, added Status and Expiry Date columns to Section 7, registered `REC-A04-001` (`Closed`), synced `A01`–`A04` and `C01` (`v1.1.0`), refined `C03`/`C04` scope notes, aligned `E03` filename with `-and-` convention, expanded acronyms, and updated Section 2 phrasing per `REC-A04-001`. | Hary Irfantri |
| `v1.0.8` | `2026-11-22` | Errata | Synced `C01` (`v1.0.0`, `Approved`) in the Normative Standards Register and updated Coverage Summary (`5` Approved, `0` Draft, `17` Planned). | Hary Irfantri |
| `v1.0.7` | `2026-11-20` | Errata | Synced `A04` (`v1.0.0`, `Approved`) in the Normative Standards Register and updated Coverage Summary (`4` Approved, `0` Draft, `18` Planned), completing the Series A baseline. | Hary Irfantri |
| `v1.0.6` | `2026-11-20` | Errata | Synced `A04` (`v0.1.0`, `Draft`) in the Normative Standards Register and updated Coverage Summary (`3` Approved, `1` Draft, `18` Planned). | Hary Irfantri |
| `v1.0.5` | `2026-11-20` | Errata | Synced `A03` (`v1.0.0`, `Approved`) in the Normative Standards Register and updated Coverage Summary (`3` Approved, `0` Draft, `19` Planned). | Hary Irfantri |
| `v1.0.4` | `2026-11-20` | Errata | Synced `A03` (`v0.2.0`, `Draft`) with authoritative legal entity names (`Irvantri Standards Pte. Ltd.`, `Irvantri Group Pte. Ltd.`) and active `Tier 0` affiliation. | Hary Irfantri |
| `v1.0.3` | `2026-11-20` | Errata | Synced `A03` (`v0.1.0`, `Draft`) in the Normative Standards Register and updated Coverage Summary (`2` Approved, `1` Draft, `19` Planned). | Hary Irfantri |
| `v1.0.2` | `2026-11-20` | Errata | Synced `A02` (`v1.0.0`, `Approved`) in the Normative Standards Register and updated Coverage Summary (`2` Approved, `20` Planned). | Hary Irfantri |
| `v1.0.1` | `2026-11-20` | Errata | Updated all repository folder paths to English Title Case; synced `A01` (`v1.0.1`, `Approved`) and `A02` (`v0.1.0`, `Draft`) in register and coverage summary. | Hary Irfantri |
| `v1.0.0` | `2026-11-20` | Major | Initial approved baseline of the Unified Operating Library Index (`A01`–`E04` active roster; `F`–`H` reserved). | Hary Irfantri |
| `v0.1.0` | `2026-11-20` | Pre-Release | Initial draft register created with `A01`–`E04` roster and `F`–`H` reserved series. | Hary Irfantri |
