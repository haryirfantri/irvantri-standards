# A03 — Entity & Brand Architecture

| Field | Value |
| :--- | :--- |
| **Code** | `A03` |
| **Version** | `v1.1.1` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-25` |
| **Next Review** | `2027-05-20` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `None` |

## 1. Purpose

This standard defines the corporate identity hierarchy, authoritative legal and brand names, brand architecture model, parent-entity affiliation rules, offering and sub-brand relationships, co-branding boundaries, and legal attribution requirements for **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`). It ensures every product, portal, publication, and client deliverable carries unambiguous provenance and corporate authority.

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* All corporate, legal, and brand names used across Irvantri Standards products, portals, services, and internal or external communications.
* All brand architecture classifications, including Parent Entity affiliation (`Irvantri Group`), Master Brand usage, Named Offerings, Endorsed Sub-Brands, and Co-Branded deliverables.
* All legal entity, copyright, licensing, and third-party attribution notices published across formal documents, compiled publications, and digital interfaces.

### 2.2 Out of Scope
This standard does not govern:
* Logo geometry, minimum sizes, clear space, or visual lockup construction (governed by `B01`).
* Controlled glossaries, acronyms, or editorial tone rules (governed by `C01` and `C02`).
* Internal governance or brand standards of `Irvantri Group Pte. Ltd.` or other member companies of `Irvantri Group`.
* Statutory corporate filings or tax registrations whose wording is mandated by applicable law (which supersede this library per `A01 §5.1.4`).

## 3. Normative References

The following documents are referenced in this standard. For undated references, the latest approved edition applies.
* `A01` — Document Control & Lifecycle.
* `A02` — Taxonomy, Coding & File Naming.
* `A04` — Compliance, Reviews & Exceptions.
* `B01` — Marks & Lockups.
* `B03` — Typography.
* `C01` — Voice, Tone & Plain Language.
* `C02` — Terminology & Controlled Vocabulary.
* `D02` — Responsive Shells & Navigation.
* `E01` — Formal Document Layout.
* `E04` — Correspondence & Presentations.

## 4. Terms & Definitions

For terms shared across the library, refer to `C02`, `A01`, and `A02`. For the purposes of this standard, the following definitions apply:
* **Brand Architecture:** The formal hierarchy defining how the Parent Entity, Master Brand, Offerings, Sub-Brands, and external parties relate in naming, authority, and attribution.
* **Branded House:** An architecture model in which offerings, portals, and services operate directly under the Master Brand name rather than as independent standalone brands.
* **Co-Branding:** The deliberate pairing of the Irvantri Standards identity with one or more client, partner, or external organization identities on a shared deliverable, system, event, or publication.
* **Endorsement Line:** The fixed textual attribution statement linking Irvantri Standards to its Parent Entity: `A member of Irvantri Group`.
* **Legal Entity Name:** The formally registered corporate name of the company (`Irvantri Standards Pte. Ltd.`) used in contracts, invoices, statutory filings, and legal notices.
* **Master Brand:** The primary public-facing identity of the company: `Irvantri Standards`.
* **Offering:** Any software product, portal, service line, framework, or publication developed, operated, or maintained by Irvantri Standards.
* **Parent Entity:** The overarching corporate group of which `Irvantri Standards Pte. Ltd.` is a member company: `Irvantri Group` (`Irvantri Group Pte. Ltd.`).
* **Sub-Brand:** A formally approved offering identity carrying a distinctive name paired with mandatory attribution to the Master Brand.

## 5. Requirements

### 5.1 Brand Architecture Model & Tiers
**5.1.1** Irvantri Standards SHALL operate under a **Branded House** architecture as its default model, in which offerings, portals, and publications operate directly under the Master Brand (`Irvantri Standards`).

**5.1.2** Every brand expression, offering, or joint deliverable SHALL belong to exactly one of the following five architectural tiers:

| Tier | Classification | Authority Rule |
| :--- | :--- | :--- |
| **Tier 0** | Parent Entity | `Irvantri Group` (`Irvantri Group Pte. Ltd.`); active institutional affiliation governed by Clause `5.3`. |
| **Tier 1** | Master Brand | `Irvantri Standards` (`Irvantri Standards Pte. Ltd.`); primary authority for all corporate, standards, and general company work. |
| **Tier 2** | Named Offerings & Portals | Descriptive offerings operating directly under the Master Brand (`Irvantri Standards [Descriptor]`). |
| **Tier 3** | Endorsed Sub-Brands | Distinctive offering names paired with mandatory Master Brand attribution; permitted by exception only. |
| **Tier 4** | Co-Branded & Client Deliverables | Joint or client-commissioned work with explicitly declared party roles and ownership boundaries. |

**5.1.3** An offering SHALL NOT be created as a `Tier 3` Endorsed Sub-Brand or an independent unendorsed brand without prior written Approver sign-off. That authorization SHALL be recorded as `REC-A03` and registered in `C02`.

**5.1.4** A `Tier 3` Endorsed Sub-Brand SHOULD be approved only when at least one of the following criteria is documented in the `REC-A03` approval record:
* The offering serves a distinct external market segment whose positioning differs materially from core Irvantri Standards services.
* The offering requires commercial, licensing, or regulatory separation (such as a standalone software product or corporate spin-out).
* The offering is bound by joint-venture or partnership governance obligations requiring a distinct name.

**5.1.5** Every approved `Tier 3` Endorsed Sub-Brand SHALL display the Master Brand name (`Irvantri Standards`) in its primary header, cover, or lockup in accordance with `B01` and `C02`.

### 5.2 Authoritative Corporate & Legal Identity
**5.2.1** This standard is the single authoritative source of truth for the corporate and legal entity identifiers of Irvantri Standards. The exact strings below SHALL be reproduced without alteration across all in-scope touchpoints in Clause `2.1`. `C02` SHALL mirror these entries by reference to `A03`:

| Identity Element | Authoritative Value |
| :--- | :--- |
| **Master Brand** | `Irvantri Standards` |
| **Legal Entity Name** | `Irvantri Standards Pte. Ltd.` |
| **Parent Entity Brand** | `Irvantri Group` |
| **Parent Legal Entity Name** | `Irvantri Group Pte. Ltd.` |
| **Endorsement Line** | `A member of Irvantri Group` |

**5.2.2** The Master Brand name SHALL be written strictly as `Irvantri Standards` across all prose, user interfaces, and formal documents. It SHALL NOT be abbreviated to `IS` in external body text unless first written in full in that document (`Irvantri Standards (IS)`). Controlled citation codes permitted by `A02 §5.2.5` are exempt.

**5.2.3** Contracts, invoices, purchase orders, formal terms of engagement, legal notices, and statutory declarations SHALL state the full Legal Entity Name (`Irvantri Standards Pte. Ltd.`) on first reference. General publications, websites, and internal standards SHOULD use the Master Brand name (`Irvantri Standards`) unless legal, contractual, or copyright requirements specify the Legal Entity Name.

**5.2.4** `Irvantri Standards Pte. Ltd.` is a distinct legal entity from `Irvantri Group Pte. Ltd.` Contracts, invoices, proposals, and binding obligations entered into by Irvantri Standards SHALL name `Irvantri Standards Pte. Ltd.` as the contracting party. They SHALL NOT name or bind `Irvantri Group Pte. Ltd.` without explicit written authorization from `Irvantri Group Pte. Ltd.`

### 5.3 Parent Entity Affiliation & Endorsement Line
**5.3.1** `Irvantri Standards Pte. Ltd.` is an authorized member company of `Irvantri Group` (`Irvantri Group Pte. Ltd.`). Institutional affiliation SHALL be expressed using the exact verbatim Endorsement Line: `A member of Irvantri Group`.

**5.3.2** The Endorsement Line SHALL be reproduced with exact capitalization, wording, and punctuation. Informal or altered variants (such as *Part of Irvantri Group*, *An Irvantri Group Company*, or *Powered by Irvantri Group*) SHALL NOT be used. When placed at the end of a prose paragraph or approved boilerplate (`C01 §5.5.1`), a single trailing period (`A member of Irvantri Group.`) is permitted without altering wording or capitalization.

**5.3.3** The Endorsement Line SHALL appear in the following institutional touchpoints while keeping Irvantri Standards visually primary:
* Formal document covers or cover metadata panels (`E01`).
* Compiled corporate publications (`PUB-`).
* Primary corporate website footers and corporate overview or legal pages (`D02`).
* Formal corporate correspondence and official presentation cover or closing slides (`E04`).

**5.3.4** The Endorsement Line SHOULD NOT appear in compact navigation bars, application icons, or constrained placements where text falls below `B01` and `B03` legibility thresholds.

**5.3.5** Placement of a standalone `Irvantri Group` mark or lockup on Irvantri Standards materials SHALL require explicit Approver authorization and SHALL conform to `B01` and the visual standards of `Irvantri Group`.

### 5.4 Offering, Product & Portal Naming
**5.4.1** `Tier 2` Named Offerings SHALL follow the naming pattern `Irvantri Standards [Descriptor]`, where `[Descriptor]` uses approved functional terms registered in `C02`.

**5.4.2** Internal project codenames SHALL NOT appear in external deliverables, public Uniform Resource Locators (`URL`s), client portals, compiled publications (`PUB-`), or approved normative standards.

**5.4.3** Every external-facing offering name SHALL be registered in `C02` prior to public release.

### 5.5 Co-Branding, Client Deliverables & Non-Endorsement
**5.5.1** Every `Tier 4` Co-Branded publication, joint system, or partnership deliverable SHALL declare each participating organization's role in its metadata block or colophon. Examples include Author, Developer, Maintainer, Sponsor, or Client.

**5.5.2** Client-commissioned deliverables produced by Irvantri Standards SHALL observe the following ownership distinction:
* **Client-owned deliverables:** Present the client identity as primary and, where contractually permitted, attribute Irvantri Standards strictly inside a designated metadata field, colophon, or footer attribution line.
* **Irvantri Standards proprietary systems, standards, or frameworks:** Retain Irvantri Standards as the primary Master Brand authority.

**5.5.3** In equal-partnership Co-Branded pairings, the Irvantri Standards mark SHALL be sized at optical parity with partner marks in accordance with `B01`. The mark SHALL NOT appear alongside third-party product claims, endorsements, or certifications without a written agreement signed by the Approver.

**5.5.4** Third-party trademarks, partner logos, and client names SHALL NOT be displayed on Irvantri Standards websites, publications, or proposals without documented permission from the respective rights holder.

### 5.6 Legal Attribution & Copyright Notices
**5.6.1** Every formal document (`E01`), compiled publication (`PUB-`), and external digital portal (`D02`) SHALL carry the notice `© [YYYY] Irvantri Standards Pte. Ltd. All rights reserved.` Items published under an explicitly stated open license or client-assigned copyright notice are exempt.

**5.6.2** References to third-party standards, specifications, or trademarks SHALL cite the owning organization by its published name and SHALL NOT state or imply official affiliation or ownership where none exists.

### 5.7 Architectural Changes & Name Retirement
**5.7.1** Establishing a `Tier 3` Sub-Brand, changing any entry in Clause `5.2.1`, or retiring an Offering name SHALL require Approver sign-off and a corresponding `C02` update. Each change SHALL also trigger a `MAJOR` or `MINOR` revision of this standard per `A01 §5.5`.

**5.7.2** Retired offering names SHALL be marked as deprecated in `C02` and SHALL NOT be reassigned to unrelated offerings for a minimum of `24` months following retirement.

## 6. Conformance & Verification

A document, offering, portal, or partnership deliverable conforms to `A03` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `A03-C1` | Item maps to a single architectural tier (`5.1.2`); any `Tier 3` Sub-Brand has a logged `REC-A03` approval (`5.1.3`) and displays Master Brand attribution (`5.1.5`). | Register & asset audit |
| `A03-C2` | Master Brand appears strictly as `Irvantri Standards` with zero unexpanded `IS` abbreviations in external prose (`5.2.2`); legal and commercial instruments state `Irvantri Standards Pte. Ltd.` (`5.2.3`) and do not improperly bind `Irvantri Group Pte. Ltd.` (`5.2.4`). | Editorial & legal inspection |
| `A03-C3` | Endorsement Line appears verbatim as `A member of Irvantri Group` across mandatory institutional touchpoints (`5.3.1`–`5.3.3`) with zero unauthorized variants, and any standalone `Irvantri Group` mark holds documented Approver authorization (`5.3.5`). | Document & web audit |
| `A03-C4` | All external offering names are registered in `C02` and contain zero internal codenames (`5.4.2`–`5.4.3`). | Glossary cross-check |
| `A03-C5` | `Tier 4` Co-Branded and client deliverables explicitly declare party roles (`5.5.1`) and hold documented permission for every third-party mark displayed (`5.5.4`). | Deliverable & record review |
| `A03-C6` | Formal documents, publications, and portals display `© [YYYY] Irvantri Standards Pte. Ltd. All rights reserved.` or an authorized license/client notice (`5.6.1`). | Layout inspection |
| `A03-C7` | Retired offering names are marked deprecated in `C02` and observe the 24-month non-reuse window (`5.7.2`). | Glossary history audit |
| `A03-C8` | Zero unauthorized unendorsed brands exist (`5.1.3`); `Tier 2` names follow `Irvantri Standards [Descriptor]` (`5.4.1`); client vs. proprietary ownership attribution (`5.5.2`), optical parity and written co-branding agreements (`5.5.3`), third-party non-affiliation (`5.6.2`), and architectural revision gates (`5.7.1`) are satisfied. | Deliverable & register audit |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with `A04`.

## 7. Linked Artifacts

None.

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v1.1.1` | `2026-11-25` | Errata | Restored Section 3 normative reference parity (added `C01`, removed unused `Library-Index.md` and obsolete pre-approval note), tightened or split 30+ word sentences in `5.1.3`, `5.2.1`–`5.2.2`, `5.3.4`, `5.5.1`, `5.6.1`, and `5.7.1`, and confirmed `D02 (v2.0.0)` alignment per `REC-A04-005` (`F-09`, `F-10`). | Hary Irfantri |
| `v1.1.0` | `2026-11-22` | Minor | Permitted single trailing period on Endorsement Line in prose boilerplates (`5.3.2`), removed unused `C01` normative reference, tightened `A03-C3`, added `A03-C8`, replaced vague qualifier in `5.2.1`, fixed double period in `5.2.4` and list punctuation in `5.3.3`, expanded `URL`, and split 30+ word sentences per `REC-A04-001`. | Hary Irfantri |
| `v1.0.0` | `2026-11-20` | Major | Initial approved baseline of `A03` (Entity & Brand Architecture), locking Branded House model, authoritative legal entities (`Irvantri Standards Pte. Ltd.`, `Irvantri Group Pte. Ltd.`), verbatim Endorsement Line, co-branding rules, and copyright attribution. | Hary Irfantri |
| `v0.2.0` | `2026-11-20` | Pre-Release | Activated `Tier 0` (`Irvantri Group` / `Irvantri Group Pte. Ltd.`), locked verbatim Endorsement Line (`A member of Irvantri Group`), established Authoritative Corporate & Legal Identity table (`Irvantri Standards Pte. Ltd.`) with entity separation rule, added `Tier 3` qualification criteria, and standardized copyright attribution. | Hary Irfantri |
| `v0.1.0` | `2026-11-20` | Pre-Release | Initial draft establishing Branded House default model, five architectural tiers, corporate and legal identity rules, parent-entity affiliation governance, offering naming, co-branding boundaries, and legal attribution requirements. | Hary Irfantri |
