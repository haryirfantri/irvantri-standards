# Irvantri Standards — Conformance Checklist

| Field | Value |
| :-: | :-: |
| **Code** | CHK-01 |
| **Type** | Active Verification Register |
| **Status** | Active |
| **Last Synced** | 2026-11-25 |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Governing Standard** | A04 (v1.1.0) §5.1.1 |
| **Active Checks** | 121 Checks (Series A–E) |

---

## 1. Overview & Usage

This checklist serves as the authoritative operational verification registry for the **Irvantri Standards Unified Operating Library** per **A04 §5.1.1**. All binding `SHALL` and `SHALL NOT` clauses across Approved normative standards (Series A–E) are mapped into discrete verification checks.

### 1.1 Pre-Release Audit Mandate
Per **A04 §5.1.2**, every `v0.Y.0` draft advancing to `v1.0.0`, every `MAJOR` or `MINOR` revision, and every controlled `AST-`, `TPL-`, or `PUB-` release MUST undergo a strict audit against this checklist before approval and publication.

### 1.2 Evaluation Severity Classifications (A04 §5.2.1)
* **Critical:** Direct contradiction of core identity, legal entity branding, accessibility compliance, or standard conflict. Requires immediate remediation before release.
* **Major:** Omission of mandatory metadata fields, incorrect section structure, unexpanded acronyms, or non-compliant document formatting. SLA: 15 business days.
* **Minor:** Stylistic inconsistencies, minor sentence length overruns (>30 words), or non-critical formatting defects. SLA: 30 calendar days.

---

## 2. Active Verification Checks

### Series A — Governance & Foundation Standards

#### A01 — Governance Framework & Document Hierarchy
* **`[A01-C1]` Metadata Table Integrity:** Verify standard header contains exact 9-field metadata table (Code, Title, Series, Version, Status, Owner, Approver, Effective Date, Next Review) in required order.
* **`[A01-C2]` Section Structure Parity:** Verify standard strictly adheres to the 8 mandatory top-level sections (1. Metadata, 2. Purpose & Scope, 3. Normative References, 4. Terms & Definitions, 5. Normative Standards, 6. Conformance & Verification, 7. Asset & Template Register, 8. Document History).
* **`[A01-C3]` Citation Syntax:** Verify all internal and external standard references follow standard code format `[CODE] (vX.Y)` or `[CODE] (vX.Y.Z)`.
* **`[A01-C4]` Versioning & Lifecycle:** Verify version bump matches lifecycle state transitions (`v0.Y.0` Draft, `v1.0.0` Initial Release, `MINOR` feature addition, `MAJOR` breaking change, `ERRATA` bug fix).
* **`[A01-C5]` Review Schedule Alignment:** Verify `Next Review` date is set exactly 6 months (Initial/Major) or aligned with existing schedule without exceeding 6-month cap.

#### A02 — Standard Authoring & Maintenance Procedures
* **`[A02-C1]` File Naming & Pathing:** Verify filename matches `[CODE]_[Title-In-Kebab-Case].md` and resides in designated series subdirectory within `01_Standards/`.
* **`[A02-C2]` Fenced Text Blocks:** Verify mandatory legal, disclaimer, copyright, or fixed copy blocks are enclosed in Markdown fenced blocks (` ```text `).
* **`[A02-C3]` Mandatory Section 6 Mapping:** Verify every binding `SHALL` and `SHALL NOT` clause in Section 5 maps to a corresponding `[CODE-C#]` check in Section 6.
* **`[A02-C4]` Section 3 Normative Reference Parity:** Verify every standard cited in Sections 4–7 appears in Section 3, and no uncited standards are listed in Section 3.
* **`[A02-C5]` Change Log Integrity:** Verify Section 8 Document History logs revision date, version, author/editor, and clear summary of changes.

#### A03 — Group Brand & Entity Identity
* **`[A03-C1]` Legal Entity Strings:** Verify verbatim accuracy of corporate entity names (`Irvantri Standards`, `Irvantri Standards Pte. Ltd.`, `Irvantri Group`, `Irvantri Group Pte. Ltd.`).
* **`[A03-C2]` Group Endorsement Line:** Verify verbatim endorsement `A member of Irvantri Group` in all corporate headers, footers, and official publications.
* **`[A03-C3]` Co-Branding Hierarchy:** Verify Irvantri Group brand mark maintains dominant clear space and primary visual positioning in co-branded contexts.
* **`[A03-C4]` Copyright Formatting:** Verify copyright notices use standard format `Copyright © [Year] Irvantri Group Pte. Ltd. All rights reserved.`

#### A04 — Compliance Auditing & Deviation Waiver Management
* **`[A04-C1]` Audit Logging:** Verify consistency reviews produce a formal `REC-A04-XXX` governance record stored in `05_Records/`.
* **`[A04-C2]` Waiver Protocol:** Verify non-conformance waivers are formally requested, assigned an SLA due date, approved by Lead Approver, and logged in active waiver register.
* **`[A04-C3]` Pre-Release Gate Audit:** Verify pre-release gate audit executes 100% check verification with zero unhandled Critical or Major findings.

---

### Series B — Visual Foundations

#### B01 — Brand Marks & Visual Identity
* **`[B01-C1]` Mark Geometry & Protection Zone:** Verify minimum clear space surrounding primary logo is at least 0.25× mark height.
* **`[B01-C2]` Minimum Display Sizes:** Verify primary logo display height is not rendered below 28 px (digital) or 12 mm (print).
* **`[B01-C3]` Unapproved Variations:** Verify logo geometry, proportions, colors, and spatial arrangements are un-manipulated.

#### B02 — Color Palette & System Architecture
* **`[B02-C1]` Palette Codes:** Verify exact HEX (`#074C96`, `#DE0029`, `#092B55`, `#102F60`), RGB, and CMYK values for Primary Brand and Accent colors.
* **`[B02-C2]` Contrast Compliance:** Verify text-to-background contrast meets WCAG 2.2 Level AA standards (4.5:1 normal text, 3:1 large text/UI components).
* **`[B02-C3]` Non-Color Reliance:** Verify UI states and data visualizations do not rely solely on color to convey critical information.

#### B03 — Typography & Type Systems
* **`[B03-C1]` Primary Typefaces:** Verify Montserrat for Headings/Display and Inter for Body/UI text.
* **`[B03-C2]` Fallback Stacks:** Verify approved web-safe font fallback stacks are defined for all digital styles.
* **`[B03-C3]` Minimum Text Sizes:** Verify body text is not rendered below 14 px (digital) or 9 pt (print).
* **`[B03-C4]` Tabular Numerals:** Verify numeric tables use tabular figures (`tabular-nums` / fixed-width alignment).

#### B04 — Layout, Grids & Spatial Systems
* **`[B04-C1]` Spatial Scale Base Unit:** Verify layouts adhere to 4 px (digital) or 4 mm (print) base spatial unit grid.
* **`[B04-C2]` Touch/Click Target Floor:** Verify interactive components meet 44 px × 44 px minimum touch target dimensions.
* **`[B04-C3]` Corner Radii Consistency:** Verify corner radii strictly follow 0 px–12 px design token scale.

#### B05 — Iconography & Visual Assets
* **`[B05-C1]` Icon Grid & Stroke Weight:** Verify icons are built on 16 px / 20 px / 24 px grids with uniform 1.5 px or 2 px stroke widths.
* **`[B05-C2]` SVG Asset Optimization:** Verify SVG files are minified, stripped of editor metadata, and include accessible `<title>` attributes.

---

### Series C — Information & Verbal Standards

#### C01 — Editorial Style & Verbal Tone
* **`[C01-C1]` Sentence Length Cap:** Verify no sentence in normative body text exceeds 30 words.
* **`[C01-C2]` Prohibited Keywords:** Verify absence of non-standard RFC keywords (`MUST`, `WILL`, `REQUIRED`), vague qualifiers (`appropriate`, `adequate`), and promotional hype.
* **`[C01-C3]` Acronym First-Occurrence Expansion:** Verify non-exempt acronyms are expanded upon first appearance in the document.
* **`[C01-C4]` Contraction Policy:** Verify absence of contractions in formal governance, legal, or normative standards text.

#### C02 — Controlled Vocabularies & Technical Glossary
* **`[C02-C1]` Status Terminology:** Verify lifecycle statuses use only approved values (`Draft`, `In Review`, `Approved`, `Deprecated`, `Archived`).
* **`[C02-C2]` Standard Acronym Definitions:** Verify standard acronym list matches global glossary mappings.

#### C03 — Content Formatting & Structuring
* **`[C03-C1]` Heading Hierarchy:** Verify logical non-skipping heading structure (H1 -> H2 -> H3 -> H4).
* **`[C03-C2]` List Formatting:** Verify consistent punctuation and capitalization across bulleted and numbered lists.

#### C04 — Data Notation, Units & Localization
* **`[C04-C1]` ISO 8601 Dates:** Verify all dates follow strictly `YYYY-MM-DD` format.
* **`[C04-C2]` ISO 4217 Currency Notation:** Verify currency figures explicitly state 3-letter currency code (e.g., `SGD 1,500`, `USD 500`) without bare `$` symbols.
* **`[C04-C3]` SI Units & Spacing:** Verify technical measurements use standard International System of Units (SI) symbols with non-breaking space between value and unit.

---

### Series D — Digital Systems & Interfaces

#### D01 — Web Architecture & Component Systems
* **`[D01-C1]` Component Naming & Tokens:** Verify components reference central design token names (`AST-D01-01`).
* **`[D01-C2]` Semantic HTML Markup:** Verify use of standard HTML5 landmarks and structural elements.

#### D02 — Responsive Shells & Navigation
* **`[D02-C1]` Breakpoint Tokens:** Verify layouts adapt cleanly across defined breakpoints (Mobile, Tablet, Desktop, Wide).
* **`[D02-C2]` Clean Markdown & Outputs:** Verify output files are free of conversational, transient, or leaked internal artifacts.

#### D03 — Interaction Design & User State Controls
* **`[D03-C1]` Interactive Feedback States:** Verify components support Default, Hover, Focus, Active, Disabled, and Loading states.
* **`[D03-C2]` Focus Rings & Keyboard Access:** Verify visible focus rings and complete keyboard navigation support.

#### D04 — Digital Accessibility & Usability Standards
* **`[D04-C1]` WCAG 2.2 Level AA Compliance:** Verify compliance across contrast, scaling, structural markup, and screen reader announcements.
* **`[D04-C2]` ARIA Attribute Integrity:** Verify valid Accessible Rich Internet Applications (ARIA) roles, states, and properties without unmeasured qualifiers.

#### D05 — Generated Outputs & Export Artifacts
* **`[D05-C1]` Single-File Mandate:** Verify Web/React deliverables are bundled into a single self-contained executable file.
* **`[D05-C2]` Clean Technical Artifacts:** Verify generated artifacts contain zero residual AI chat citations or chat transcript strings.

---

### Series E — Documents & Print Specifications

#### E01 — Document Layout, Page Geometry & Grid
* **`[E01-C1]` Standard Page Geometry:** Verify page dimensions follow A4 or US Letter standards with defined uniform margins.
* **`[E01-C2]` Grid Structure & Headers:** Verify running headers and footers contain exact document codes and entity attributions.

#### E02 — PDF & Print Preparation Standards
* **`[E02-C1]` PDF/A Compliance:** Verify generated archival PDF files meet PDF/A standards with embedded fonts.
* **`[E02-C2]` CMYK & High-Resolution Assets:** Verify print graphics use CMYK color space at 300 DPI or vector format.

#### E03 — Email, Messaging & Communications Formatting
* **`[E03-C1]` Email Signature Block:** Verify email templates strictly follow corporate signature lockup and group endorsement standards.
* **`[E03-C2]` Cross-Client Rendering:** Verify HTML email templates render reliably across major mobile and desktop email clients.

#### E04 — Presentation Slides & Visual Deck Systems
* **`[E04-C1]` Standard Aspect Ratio:** Verify slide decks use 16:9 widescreen layout aspect ratio.
* **`[E04-C2]` Slide Master Templates:** Verify presentations use approved slide master themes (`TPL-E04-01`, `TPL-E04-02`).

---

## 3. Google Drive Repository & Pre-Release Audit Protocol

### 3.1 Repository Hygiene & Grounding Checklist
* **Authoritative repository root:** Store and maintain all active library files inside `Irvantri Group / Irvantri Standards / Unified Operating Library` in Google Drive, following the directory layout in `A02 §5.5.1`.
* **Active grounding sources:** Read `Library-Index.md`, `Conformance-Checklist.md`, and applicable `Approved` standards under `01_Standards/` live before authoring or auditing (`A01 §5.4.2`, `A04 §5.1.1`). Exclude `Planned`, `Draft`, `In Review`, and `Deprecated` standards from binding audit criteria.
* **Excluded historical sources:** Exclude immutable snapshots in `99_Archive/` (`A02 §5.6`) and terminal `REC-` files (`Closed`, `Rejected`, `Expired`, or `Revoked` in `05_Records/` per `A04 §5.5.3`) when resolving active normative rules so superseded editions and past defect logs do not override active `Approved` standards.
* **Active naming & archive boundary (`A01 §5.7`, `A02 §5.4`–`§5.6`):** Keep active files in `01_Standards/`, `02_Assets/`, `03_Templates/`, `04_Publications/`, and `05_Records/` free of version suffixes. Before publishing a `MAJOR` or `MINOR` revision of an `Approved` standard (or deprecating a non-`REC-` controlled item), copy the outgoing file unmodified into `99_Archive/` with `_vMAJOR.MINOR.ERRATA` appended before the file extension, and never modify or rename archived files afterward.
* **Approval & same-day sync (`A01 §5.1.3`, `§5.8.1`, `A04 §5.5.2`):** Do not promote drafts or overwrite approved files in Google Drive without explicit Approver sign-off. Upon approval, synchronize the active file, `99_Archive/` snapshot (when triggered), `Library-Index.md`, and `Conformance-Checklist.md` on the same calendar date.

### 3.2 Reusable Pre-Release Gate Audit Prompt (`A04 §5.1.2`)
Run this prompt in a **fresh chat** grounded in the live `Unified Operating Library` folder in Google Drive before approving any `v0.Y.0` draft to `v1.0.0`, promoting any `MAJOR` or `MINOR` revision, or releasing a controlled `AST-`, `TPL-`, or `PUB-` artifact:

```text
Run a strict A04 §5.1.2 Pre-Release Gate audit on the draft below against the live Conformance-Checklist.md, Library-Index.md, and Approved standards in the Unified Operating Library Google Drive folder (excluding 99_Archive/ snapshots and terminal 05_Records/ files).
Return a Pass/Fail table verifying:
1. Every applicable [CODE]-C# check in Conformance-Checklist.md Section 2 (A04 §5.1.1).
2. Complete mapping of every Section 5 SHALL / SHALL NOT clause into Section 6 checks of the draft (for normative standards).
3. First-occurrence expansion of every non-exempt acronym per C01 §5.3.3 and C02 §5.2.2.
4. Every Section 5 sentence exceeding 30 words flagged with its exact word count (C01 §5.3.1).
5. Zero prohibited keywords (MUST, WILL, REQUIRED), unauthorized contractions, first- or second-person pronouns in normative clauses, vague qualifiers, promotional hype terms, or cross-standard conflicts.
6. Exact 9-field metadata header, 8 fixed sections, A02 §5.4–§5.5 filename and directory placement in English Title Case, ISO 8601 dates, fenced text blocks for mandatory copy, and valid citation syntax ([CODE] (vX.Y) / [CODE] (vX.Y.Z)).
7. Exact Section 3 Normative References parity: every listed reference is cited in Sections 4–7 and no cited standard is omitted from Section 3.
List every defect with exact clause citations and severity (Critical, Major, or Minor per A04 §5.2.1) before issuing a Release Verdict (Pass or Hold).
```