# C02 — Terminology & Controlled Vocabulary

| Field | Value |
| :--- | :--- |
| **Code** | `C02` |
| **Version** | `v1.1.0` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-24` |
| **Next Review** | `2027-05-22` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `None` |

## 1. Purpose

This standard establishes the canonical library glossary, controlled acronyms and expansion exemptions, approved offering and sub-brand names, fixed lifecycle status vocabularies, and prohibited term rules for **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`). It ensures consistent terminology across all normative standards, digital interfaces, publications, and corporate communications.

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* All normative standards (`A01`–`H99`), Master Assets (`AST-`), Executable Templates (`TPL-`), Compiled Publications (`PUB-`), Governance Records (`REC-`), and registers tracked in `Library-Index.md`.
* All digital products, user interfaces, system messages, and generated outputs (`D01`–`D05`).
* All formal documents, proposals, presentations, and external corporate communications (`E01`–`E04`).

### 2.2 Out of Scope
This standard does not govern:
* Editorial voice, tone registers, sentence limits, or United States English (`en-US`) spelling mechanics (governed by `C01`).
* User Interface (`UI`) microcopy patterns for error messages, confirmations, and empty states (governed by `C03`).
* Corporate entity hierarchy, brand architecture tiers, or legal attribution rules (governed by `A03`, which this standard mirrors by reference).
* Client-specific domain glossaries mandated by external project contracts.

## 3. Normative References

The following documents are referenced in this standard. For undated references, the latest approved edition applies.
* `Library-Index.md` — Irvantri Standards Unified Operating Library Index (`v1.1.0` or later).
* `A01` — Document Control & Lifecycle.
* `A02` — Taxonomy, Coding & File Naming.
* `A03` — Entity & Brand Architecture.
* `A04` — Compliance, Reviews & Exceptions.
* `C01` — Voice, Tone & Plain Language.
* `C04` — Data, Dates & Citation Formatting.

## 4. Terms & Definitions

This section consolidates shared terms used across the Unified Operating Library. Specialized terms unique to an individual standard are defined in Section 4 of that standard (`A01`, `A02`, `A03`, `A04`, and `C01`).
* **Acronym:** An abbreviation formed from the initial letters of a multi-word phrase and pronounced either as a word or letter-by-letter (an initialism).
* **Controlled Vocabulary:** An approved, finite set of canonical terms, status labels, and identifiers mandated for consistent use across registers, interfaces, and documents.
* **Deprecated Term:** A retired offering name, legacy code prefix, or superseded phrase that is prohibited from active use.
* **Functional Descriptor:** An approved noun or noun phrase appended to the Master Brand (`Irvantri Standards [Descriptor]`) to identify a `Tier 2` Named Offering under `A03`.
* **Glossary:** The authoritative alphabetized register of approved terms and definitions maintained in this standard.
* **Status Vocabulary:** The fixed set of lifecycle state strings permitted for a given class of controlled item or logged record.

## 5. Requirements

### 5.1 Authoritative Library Glossary & Entity Mirror
**5.1.1** Controlled documents, digital interfaces, and corporate communications SHALL use the canonical terms defined in Section 4 and in the authoritative definitions of `A01`, `A02`, `A03`, `A04`, and `C01`.

**5.1.2** Where a domain-specific term is introduced in a normative standard, the Owner SHALL define that term in Section 4 of that standard rather than redefining an existing `C02` term.

**5.1.3** Corporate and legal entity names SHALL reproduce the exact strings locked in `A03 §5.2.1` without alteration:

| Identity Element | Authoritative Value | Governing Source |
| :--- | :--- | :--- |
| **Master Brand** | `Irvantri Standards` | `A03 §5.2.1` |
| **Legal Entity Name** | `Irvantri Standards Pte. Ltd.` | `A03 §5.2.1` |
| **Parent Entity Brand** | `Irvantri Group` | `A03 §5.2.1` |
| **Parent Legal Entity Name** | `Irvantri Group Pte. Ltd.` | `A03 §5.2.1` |
| **Endorsement Line** | `A member of Irvantri Group` | `A03 §5.2.1`, `§5.3.1` |

### 5.2 Acronyms, Initialisms & Expansion Exemptions
**5.2.1** Authors SHALL expand every acronym or initialism on first occurrence in a standalone document or page as `Full Term (ACRONYM)` per `C01 §5.3.3`, unless exempted in Clause `5.2.2`.

**5.2.2** The following established technical format and protocol initialisms MAY appear without first-occurrence expansion in technical specifications, digital interfaces, and normative standards, provided their uppercase casing matches `A02 §5.4.4`:

| Initialism | Full Term | Permitted Context |
| :--- | :--- | :--- |
| `ASCII` | American Standard Code for Information Interchange | Technical specifications, encoding rules, and standards |
| `CSS` | Cascading Style Sheets | Digital systems specifications and code documentation |
| `CSV` | Comma-Separated Values | Data export specifications, interfaces, and standards |
| `HTML` | HyperText Markup Language | Digital systems specifications and web documentation |
| `JSON` | JavaScript Object Notation | Data interchange specifications and token schemas |
| `PDF` | Portable Document Format | Document layout, export, and print standards |
| `PNG` | Portable Network Graphics | Visual asset and export specifications |
| `SVG` | Scalable Vector Graphics | Visual asset, mark, and iconography specifications |
| `URL` | Uniform Resource Locator | Digital interfaces, documentation, and standards |

**5.2.3** The following governance, quality, accessibility, and color-model acronyms SHALL be expanded on first occurrence per `C01 §5.3.3`:
* Application Programming Interface (`API`)
* Accessible Rich Internet Applications (`ARIA`)
* Cyan-Magenta-Yellow-Key (`CMYK`)
* Hexadecimal (`HEX`)
* Irvantri Standards (`IS`)
* International Organization for Standardization (`ISO`)
* Product Requirement Document (`PRD`)
* Red-Green-Blue (`RGB`)
* Service Level Agreement (`SLA`)
* User Interface (`UI`)
* User Experience (`UX`)
* Web Content Accessibility Guidelines (`WCAG`)

**5.2.4** Authors SHALL NOT invent unofficial abbreviations or shortened internal acronyms for standards, artifacts, or corporate entities.

### 5.3 Offering Names, Functional Descriptors & Retirement
**5.3.1** Every external-facing Offering name and `Tier 3` Sub-Brand SHALL be registered in the table below prior to public release in accordance with `A03 §5.1.3` and `§5.4.3`.

**5.3.2** `Tier 2` Named Offerings SHALL follow the pattern `Irvantri Standards [Descriptor]` using approved functional descriptors from the table below (`A03 §5.4.1`):

| Approved Functional Descriptors (`Tier 2`) |
| :--- |
| `Advisory` · `Design System` · `Framework` · `Library` · `Platform` · `Portal` · `Studio` · `System` · `Unified Operating Library` · `Workspace` |

| Registered Name | Architectural Tier | Status | Effective Date | Retirement Date | Scope & Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Irvantri Standards Unified Operating Library` | `Tier 2` | `Active` | `2026-11-20` | `—` | Authoritative library of normative standards, master assets, templates, and compiled publications |
| `Irvantri Standards Design System` | `Tier 2` | `Active` | `2026-11-24` | `—` | Authoritative digital design system, token architecture, component patterns, and compiled brand guide |

**5.3.3** Internal project codenames SHALL NOT appear in external deliverables, public `URL` paths, client portals, or Approved standards (`A03 §5.4.2`).

**5.3.4** Upon retiring an Offering name or Sub-Brand, the Owner SHALL update its status to `Deprecated` in Clause `5.3.2` with an `ISO` 8601 retirement date per `C04` (`A03 §5.7.2`).

**5.3.5** A `Deprecated` Offering name or Sub-Brand SHALL NOT be reassigned to an unrelated offering for at least `24` months following its recorded retirement date (`A03 §5.7.2`).

### 5.4 Fixed Controlled Status Vocabularies
**5.4.1** Registers (`Library-Index.md`), metadata headers, and system interfaces SHALL use only the exact Title Case status strings assigned to each controlled item class in the table below:

| Controlled Class | Permitted Status Strings | Authoritative Clause |
| :--- | :--- | :--- |
| **Normative Standards (`A01`–`H99`)** | `Planned`, `Draft`, `In Review`, `Approved`, `Deprecated` | `A01 §5.4.1` |
| **Master Assets (`AST-`)** | `Planned`, `Approved`, `Sync Required`, `Deprecated` | `A01 §5.4.3` |
| **Executable Templates (`TPL-`)** | `Planned`, `Approved`, `Sync Required`, `Deprecated` | `A01 §5.4.3` |
| **Compiled Publications (`PUB-`)** | `Planned`, `Approved`, `Sync Required`, `Deprecated` | `A01 §5.4.5` |
| **Governance Records (`REC-`)** | `Open`, `Approved`, `Rejected`, `Expired`, `Revoked`, `Closed` | `A01 §5.4.6` |
| **Logged Audit Findings (`REC-A04`)** | `Open`, `Waived`, `Closed` | `A04 §5.2.2` |
| **Registered Offerings & Sub-Brands (`C02`)** | `Active`, `Deprecated` | `A03 §5.7.2`, `C02 §5.3.2` |

**5.4.2** Controlled status values SHALL NOT be replaced with informal synonyms—such as Work in Progress (`WIP`), `Final`, `Active Standard`, `Pending`, or `Retired`—in registers or headers.

### 5.5 Prohibited Terms & Deprecated Variants
**5.5.1** Controlled documents, interfaces, and communications SHALL NOT use any prohibited term or variant listed in the following table:

| Prohibited Term / Variant | Required Replacement | Governing Authority |
| :--- | :--- | :--- |
| `MUST`, `WILL`, `REQUIRED` *(in normative clauses)* | `SHALL` or `SHALL NOT` | `A01 §5.3.3` |
| `STD-` or `ARC-` code prefixes | Bare standard code (`A01`) or `99_Archive/` path | `A02 §5.2.2`, `§5.6.1` |
| `Part of Irvantri Group`, `An Irvantri Group Company`, `Powered by Irvantri Group` | `A member of Irvantri Group` | `A03 §5.3.2` |
| `blacklist` / `whitelist` | `denylist` / `allowlist` | `C01 §5.6.2` |
| `master` / `slave` *(in technical architectures)* | `primary` / `replica` | `C01 §5.6.2` |
| `WIP`, `Final`, `Pending`, `Retired` *(as controlled statuses)* | Exact status strings in Clause `5.4.1` | `C02 §5.4.1` |

**5.5.2** Adding new Offering registrations, acronym exemptions, or prohibited terms to this standard SHALL require Approver sign-off through a `MINOR` or `MAJOR` revision per `A01 §5.5`.

## 6. Conformance & Verification

A document, register, interface, offering, or corporate communication conforms to `C02` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `C02-C1` | Controlled texts use canonical glossary terms (`5.1.1`), domain-specific terms are defined locally without redefining `C02` terms (`5.1.2`), and corporate strings match `A03 §5.2.1` (`5.1.3`). | Editorial & glossary audit |
| `C02-C2` | Non-exempt acronyms are expanded on first occurrence (`5.2.1`, `5.2.3`), exempt technical initialisms preserve uppercase casing (`5.2.2`), and zero unofficial abbreviations appear (`5.2.4`). | Text & acronym lint |
| `C02-C3` | All external-facing Offering names and `Tier 3` Sub-Brands are registered prior to release (`5.3.1`), `Tier 2` names use approved descriptors (`5.3.2`), and zero internal codenames appear externally (`5.3.3`). | Registry & release audit |
| `C02-C4` | Retired Offering names carry `Deprecated` status with an `ISO` 8601 retirement date (`5.3.4`) and observe the 24-month non-reuse window (`5.3.5`). | Registry history check |
| `C02-C5` | Registers, headers, and interfaces use exact controlled status strings (`5.4.1`) with zero informal status synonyms (`5.4.2`). | Schema & register audit |
| `C02-C6` | Controlled artifacts contain zero prohibited terms or deprecated variants listed in Clause `5.5.1`, and `C02` registry additions carry Approver sign-off (`5.5.2`). | Keyword & revision audit |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with `A04`.

## 7. Linked Artifacts

None.

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v1.1.0` | `2026-11-24` | Minor | Registered `Irvantri Standards Design System` (`Tier 2`, `Active`) in the Offering Register (`5.3.2`) per `5.5.2` and removed obsolete pre-approval reference note. | Hary Irfantri |
| `v1.0.0` | `2026-11-22` | Major | Initial approved baseline of `C02` (Terminology & Controlled Vocabulary), establishing the shared library glossary rules, acronym expansion and exemption registry, `Tier 2`/`Tier 3` offering name register, fixed controlled status vocabularies, and prohibited terms table. | Hary Irfantri |
| `v0.1.0` | `2026-11-22` | Pre-Release | Initial draft establishing the shared library glossary rules, acronym expansion and exemption registry, `Tier 2`/`Tier 3` offering name register, fixed controlled status vocabularies, and prohibited terms table. | Hary Irfantri |
