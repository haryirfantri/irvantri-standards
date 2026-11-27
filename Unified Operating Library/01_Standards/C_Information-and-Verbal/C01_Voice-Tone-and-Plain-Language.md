# C01 — Voice, Tone & Plain Language

| Field | Value |
| :--- | :--- |
| **Code** | `C01` |
| **Version** | `v1.1.1` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-25` |
| **Next Review** | `2027-05-22` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `None` |

## 1. Purpose

This standard establishes the editorial voice, contextual tone register, plain-language structure, objectivity rules, English conventions, and approved company descriptions for **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`). It ensures all normative standards, technical documentation, digital interfaces, publications, and corporate communications are clear, consistent, credible, and free of ambiguity or promotional exaggeration.

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* All normative standards (`A01`–`H99`), compiled publications (`PUB-`), and governance records (`REC-`) tracked in `Library-Index.md`.
* All product documentation, technical guides, user interface copy, system messages, and generated outputs (`D01`–`D05`).
* All formal documents, proposals, corporate web pages, presentations, and external correspondence (`E01`–`E04`).

### 2.2 Out of Scope
This standard does not govern:
* Controlled glossaries, product names, and fixed status vocabularies (governed by `C02`).
* Detailed interface microcopy patterns for errors, empty states, and confirmations (governed by `C03`, which extends this standard).
* Date, timestamp, numeric, unit, and citation formatting (governed by `C04`).
* Verbatim statutory text, regulatory filings, or external third-party quotations reproduced for reference.

## 3. Normative References

The following documents are referenced in this standard. For undated references, the latest approved edition applies.
* `Library-Index.md` — Irvantri Standards Unified Operating Library Index (`v1.1.0` or later).
* `A01` — Document Control & Lifecycle.
* `A03` — Entity & Brand Architecture.
* `A04` — Compliance, Reviews & Exceptions.
* `C02` — Terminology & Controlled Vocabulary.
* `C03` — Technical & User Experience (UX) Writing.
* `C04` — Data, Dates & Citation Formatting.
* `D02` — Responsive Shells & Navigation.
* `E04` — Correspondence & Presentations.

## 4. Terms & Definitions

For terms shared across the library, refer to `C02`, `A01`, and `A03`. For the purposes of this standard, the following definitions apply:
* **Boilerplate:** A standardized, pre-approved block of descriptive text describing Irvantri Standards for reuse across proposals, publications, and corporate touchpoints.
* **Plain Language:** Writing structured and worded so the intended audience can find what they need, understand it on first reading, and act on it reliably without specialist translation.
* **Register:** The degree of formality, grammatical person, and structural strictness appropriate to a specific communication context.
* **Tone:** The situational adaptation of the brand voice to match user intent, operational stakes, and medium while preserving core institutional character.
* **Voice:** The consistent editorial posture and verbal identity of Irvantri Standards across all channels and deliverables.

## 5. Requirements

### 5.1 Editorial Posture & Brand Voice
**5.1.1** All communications published by Irvantri Standards SHALL maintain an objective, matter-of-fact editorial posture grounded in verifiable facts, explicit criteria, and observable outcomes.

**5.1.2** Communications SHALL NOT contain unsubstantiated superlatives, promotional hyperbole, or vague claims of superiority (such as *world-class*, *best-in-class*, *revolutionary*, *cutting-edge*, *seamless*, or *unmatched*). Claims of superiority SHALL cite a third-party benchmark or contractual specification.

**5.1.3** Sentences SHOULD use active voice and direct verb constructions rather than passive or hedged phrasing. Passive voice MAY be used to emphasize the object of a rule.

**5.1.4** Communications SHALL maintain the tone posture assigned in Clause `5.2.1` and SHALL NOT contain slang, colloquialisms, or region-specific idioms.

### 5.2 Tone Adaptation by Context
**5.2.1** Authors SHALL align tone, grammatical person, and contraction usage to the communication context defined in the following register matrix:

| Context | Applicable Artifacts | Tone Posture | Grammatical Person | Contractions |
| :--- | :--- | :--- | :--- | :--- |
| **Normative Standards & Governance** | `A01`–`H99`, `REC-`, `Library-Index.md` | Formal, binding, impersonal | Third-person only (`SHALL` / `SHOULD` / `MAY` per `A01 §5.3.1`) | SHALL NOT be used |
| **Technical Documentation & Handbooks** | `PUB-`, specifications, architecture guides | Instructional, neutral, precise | Third-person or direct second-person (`you`) for procedures | SHOULD NOT be used |
| **Digital Interfaces & System Copy** | `D01`–`D05` interfaces, alerts, system exports | Calm, concise, action-oriented, blame-free | Second-person (`you`) or imperative verbs | MAY be used per `C03` |
| **Corporate & Client Communications** | `E04`, proposals, corporate web pages | Measured, transparent, authoritative | First-person plural (`we`, `our`) or `Irvantri Standards` (`A03 §5.2.2`) | SHOULD NOT be used in formal documents |

**5.2.2** Normative standards (`A01`–`H99`) and formal governance records (`REC-`) SHALL NOT use first-person pronouns (`I`, `we`, `our`) or second-person pronouns (`you`, `your`) inside normative clauses.

### 5.3 Plain Language & Structural Clarity
**5.3.1** Sentences inside normative clauses, procedural instructions, and executive summaries SHOULD NOT exceed `30` words. Compound statements exceeding `30` words SHOULD be split into separate sentences, numbered sub-clauses, or bulleted items.

**5.3.2** Multi-step procedures, conditional rules, and multi-attribute comparisons SHALL be presented as numbered lists, bulleted lists, or structured Markdown tables rather than prose paragraphs exceeding `5` sentences.

**5.3.3** Every non-exempt acronym or initialism SHALL be expanded on first occurrence in each standalone document or page as `Full Term (ACRONYM)` (`A03 §5.2.2`). Exempt technical initialisms are governed by `C02`.

**5.3.4** Normative clauses and formal specifications SHALL NOT contain vague qualifiers (such as *etc.*, *and/or*, *as appropriate*, *user-friendly*, *timely*, or *reasonable*) unless paired with an objective threshold (`A01 §5.3.5`).

**5.3.5** Headings and list items within a single section SHOULD maintain parallel grammatical structure (for example, all starting with imperative verbs or all phrased as noun phrases).

### 5.4 Objectivity, Precision & Attribution Integrity
**5.4.1** Technical documentation, proposals, and product descriptions SHALL distinguish explicitly between implemented capabilities, planned roadmap items, and external benchmarks.

**5.4.2** References to external standards—such as International Organization for Standardization (`ISO`) or Web Content Accessibility Guidelines (`WCAG`)—SHALL state the exact alignment level (such as *aligned with* or *conforms to*). Communications SHALL NOT imply third-party certification unless `Irvantri Standards Pte. Ltd.` holds an active certificate (`A03 §5.6.2`).

**5.4.3** System error messages, audit findings (`REC-A04`), and incident reports SHALL state observable system conditions and corrective actions objectively and SHALL NOT assign personal blame to users, clients, or staff.

### 5.5 Approved Company Descriptions
**5.5.1** Where a standardized company description is required in proposals, publications (`PUB-`), web pages (`D02`), or correspondence (`E04`), authors SHALL use one of the three approved boilerplates below. Authors SHALL NOT alter corporate names or the Endorsement Line (`A03 §5.2.1`, `A03 §5.3.2`).

* **One-Line Descriptor:**

```text
Irvantri Standards develops disciplined operating frameworks, technical standards, and structured systems that turn complex organizational requirements into clear, verifiable execution. A member of Irvantri Group.
```

* **Short Corporate Description:**

```text
Irvantri Standards (Irvantri Standards Pte. Ltd.) builds practical operating standards, governance frameworks, and structured digital and documentation systems. Focused on clarity, traceability, and repeatable execution, Irvantri Standards helps organizations replace ad-hoc work with durable, auditable baselines. A member of Irvantri Group.
```

* **Standard Institutional Boilerplate:**

```text
Irvantri Standards (Irvantri Standards Pte. Ltd.) is a standards-led operating and systems company dedicated to clarity, traceability, and disciplined execution. Through structured governance frameworks, information architectures, and digital and documentation systems, Irvantri Standards enables teams to translate complex requirements into consistent, verifiable outcomes. Operating under a unified library of normative standards, master assets, and executable templates, the company bridges strategic intent and day-to-day operational rigor. A member of Irvantri Group.
```

**5.5.2** Context-specific adaptations of the Standard Institutional Boilerplate MAY be prepared for targeted proposals or domain briefs. Adapted text SHALL preserve all authoritative corporate strings (`A03 §5.2.1`), satisfy Clause `5.1.2`, and receive Owner or Approver review before external release.

### 5.6 English Language & Mechanics
**5.6.1** The authoritative working and publication language of the Unified Operating Library SHALL be United States English (`en-US`, such as *standardize*, *organization*, *color*, and *behavior*). Statutory filings and registered legal names (`Irvantri Standards Pte. Ltd.`) are exempt where applicable law specifies otherwise.

**5.6.2** Communications SHALL use gender-neutral nouns and pronouns (such as *chairperson*, *staff*, *user*, and singular *they*) and inclusive technical terminology (such as *primary/replica* and *allowlist/denylist*).

**5.6.3** Prose across controlled documents SHALL use serial (Oxford) commas in lists of three or more items and em dashes (`—`) without surrounding spaces for parenthetical breaks. All dates SHALL follow `ISO` 8601 format (`YYYY-MM-DD`) per `C04` (`A01 §5.2.7`).

## 6. Conformance & Verification

A document, interface, publication, or corporate communication conforms to `C01` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `C01-C1` | External and internal texts contain zero unsubstantiated promotional superlatives or prohibited hype terms (`5.1.2`). | Editorial & keyword audit |
| `C01-C2` | Document tone, grammatical person, and contraction usage conform to the register matrix (`5.2.1`), with zero first- or second-person pronouns in normative clauses (`5.2.2`). | Structural & text review |
| `C01-C3` | Multi-step procedures and multi-variable comparisons use lists or tables rather than prose exceeding 5 sentences (`5.3.2`), and acronyms are expanded on first occurrence (`5.3.3`). | Document inspection |
| `C01-C4` | Normative clauses contain zero prohibited vague qualifiers (`5.3.4`), and external standard references state alignment accurately without unverified certification claims (`5.4.2`). | Clause & citation audit |
| `C01-C5` | Any corporate boilerplate reproduces the approved text (`5.5.1`) and preserves exact legal and endorsement strings (`A03 §5.2.1`, `A03 §5.3.2`). | Boilerplate comparison |
| `C01-C6` | Spelling follows `en-US` conventions (`5.6.1`), terminology is gender-neutral and inclusive (`5.6.2`), and punctuation/date mechanics conform to `5.6.3`. | Editorial & lint check |
| `C01-C7` | Communications maintain an objective posture without slang, colloquialisms, or regional idioms (`5.1.1`, `5.1.4`), distinguish implemented features from roadmap items (`5.4.1`), and keep errors and audit findings blame-free (`5.4.3`). | Editorial & incident review |
| `C01-C8` | Adapted corporate boilerplates preserve authoritative strings (`A03 §5.2.1`), satisfy Clause `5.1.2`, and record Owner or Approver review prior to external release (`5.5.2`). | Boilerplate & approval audit |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with `A04`.

## 7. Linked Artifacts

None.

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v1.1.1` | `2026-11-25` | Errata | Removed unused `A02` pointer in Section 4 and obsolete pre-approval note in Section 3, split 30+ word sentences in `5.3.3`, `5.4.2`, and `5.5.1`, and confirmed `D02 (v2.0.0)` alignment per `REC-A04-005` (`F-09`, `F-10`). | Hary Irfantri |
| `v1.1.0` | `2026-11-22` | Minor | Aligned Standard Institutional Boilerplate with locked verbatim Endorsement Line (`A03 §5.3.2`), moved mandatory boilerplates from blockquotes to fenced text blocks, removed unused `A02` reference, added `D02` and `E04` references, expanded `UX`/`ISO`/`WCAG`/`en-US`, tightened `5.1.4`, split 30+ word normative sentences, and added `C01-C7` and `C01-C8` per `REC-A04-001`. | Hary Irfantri |
| `v1.0.0` | `2026-11-22` | Major | Initial approved baseline of `C01` (Voice, Tone & Plain Language), locking editorial posture, contextual tone register matrix, plain-language thresholds, objectivity rules, approved company descriptions, and `en-US` mechanics. | Hary Irfantri |
| `v0.1.0` | `2026-11-22` | Pre-Release | Initial draft establishing editorial posture, contextual tone register matrix, plain-language structural thresholds, objectivity rules, approved company descriptions, and `en-US` language mechanics. | Hary Irfantri |
