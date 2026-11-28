# A01 — Document Control & Lifecycle

| Field | Value |
| :--- | :--- |
| **Code** | `A01` |
| **Version** | `v2.0.0` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-28` |
| **Next Review** | `2027-05-20` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `None` |

## 1. Purpose

This standard establishes the governance rules for authoring, structuring, approving, versioning, reviewing, publishing, and archiving controlled documents within **Standards Design**. It ensures that every standard in the library is unambiguous, objectively verifiable, traceable across revisions, and synchronized with its dependent assets, publications, and distribution mirrors.

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* All normative standards (`A01`–`H99`) registered in `Library-Index.md`.
* The lifecycle governance, version pinning, and drift controls for Master Assets (`AST-`), Executable Templates (`TPL-`), Compiled Publications (`PUB-`), and Governance Records (`REC-`).
* The maintenance and synchronization of `Library-Index.md`.
* The hybrid repository boundary between the GitHub Authoring Repository of Record and the Google Drive Distribution Mirror and Cold Archive (`5.9`).

### 2.2 Out of Scope
This standard does not govern:
* External statutory regulations, third-party standards, or client contracts (which supersede this library).
* Project specifications, client briefs, feature Product Requirement Documents (`PRD`s), or domain schemas (which consume standards without entering this register).
* Fast-changing operational runbooks, tool click-paths, or task checklists.
* Transient business records, meeting notes, invoices, or unapproved working scratchpads held outside the Authoring Repository (`5.9.4`).

## 3. Normative References

The following documents are referenced in this standard. For undated references, the latest approved edition applies.
* `Library-Index.md` — Standards Design Library Index (`v2.0.0` or later).
* `A02` — Taxonomy, Coding & File Naming.
* `A04` — Compliance, Reviews & Exceptions.
* `C01` — Voice, Tone & Plain Language.
* `C02` — Terminology & Controlled Vocabulary.
* `C04` — Data, Dates & Citation Formatting.

## 4. Terms & Definitions

For terms shared across the library, refer to `C02`. For the purposes of this standard, the following definitions apply:
* **Approver:** The designated individual holding final sign-off authority for releasing, amending, or deprecating controlled library documents.
* **Authoring Repository:** The canonical GitHub repository (`haryirfantri/irvantri-standards`, `Standards Design/` on `main`) holding every active controlled item, its Git revision history, release tags, and continuous integration (`CI`) verification tooling (`5.9.1`).
* **Breaking Change:** Any modification that alters or removes an existing `SHALL` or `SHALL NOT` requirement, renumbers normative clauses, or invalidates previously compliant work, assets, or templates.
* **Cold Archive:** The append-only `99_Archive/` directory maintained in the Google Drive Distribution Mirror to preserve browsable historical snapshots, deprecated artifacts, and retired third-party dependencies (`5.7.2`, `5.9.3`).
* **Controlled Item:** Any Normative Standard, Master Asset, Executable Template, Compiled Publication, Governance Record, or Register tracked in `Library-Index.md`.
* **Distribution Mirror:** The Google Drive folder `Standards Design` (folder ID `17-hTsw-2MIT-SzA6pRgzocpKTy1vwYin`) synced one-way from the Authoring Repository for stakeholder browsing, downloads, and cold archival (`5.9.3`).
* **Drift:** A state in which a Master Asset, Executable Template, Compiled Publication, or Distribution Mirror no longer conforms to the active version of its governing normative standard or the Authoring Repository.
* **Informative Content:** Text, notes, rationale, or examples provided to aid comprehension without imposing binding requirements.
* **Normative Content:** Clauses establishing binding requirements, recommendations, or permissions evaluated during conformance verification.
* **Owner:** The designated individual responsible for drafting, maintaining, executing errata, and initiating scheduled or event-driven reviews for a controlled item.
* **Reviewer:** An individual designated by the Owner or Approver to conduct conformance verification, peer review, or consistency audits under `A04`.

## 5. Requirements

### 5.1 Authority, Roles & Precedence
**5.1.1** Every normative standard SHALL have one assigned Owner and one assigned Approver recorded in both its metadata header and `Library-Index.md`.

**5.1.2** An Owner SHALL draft, maintain, propose revisions, execute errata, and initiate periodic reviews for their assigned standards. An Owner SHALL NOT approve Major, Minor, initial `v1.0.0`, or `Deprecated` transitions unless that individual is also the designated Approver.

**5.1.3** The Approver SHALL hold sole authority to approve initial releases (`v1.0.0`), Major revisions, Minor revisions, series activations, and deprecations across the library. Unless formally delegated in a logged governance record (`REC-`), the Approver for Irvantri Standards is Hary Irfantri.

**5.1.4** Where two controlled items conflict, precedence SHALL be resolved strictly in the following descending order:
1. Statutory, regulatory, and contractual obligations.
2. Series `A` (Governance & Traceability).
3. Normative Standards (`B`–`H`); where two standards overlap, the more specific standard prevails and the overlap SHALL be logged under `A04`.
4. Master Assets (`AST-`) and Executable Templates (`TPL-`) for physical and visual execution; any discrepancy against a governing standard SHALL be flagged `Sync Required` and reconciled.
5. Compiled Publications (`PUB-`), which are informative and SHALL NOT override their underlying normative standards.
6. Project and product specifications, which SHALL conform to applicable standards unless backed by a formal waiver logged under `A04`.

### 5.2 Mandatory Standard Anatomy
**5.2.1** Each normative standard SHALL reside in its own standalone Markdown file under `01_Standards/` named in accordance with `A02`. A single standard code SHALL NOT point to a subsection of another standard.

**5.2.2** Every normative standard SHALL open with a level-1 title (`# [CODE] — [Standard Title]`) followed immediately by a metadata table containing the following nine fields in exact order:
1. `Code`
2. `Version`
3. `Status`
4. `Effective Date`
5. `Next Review`
6. `Owner`
7. `Approver`
8. `Supersedes`
9. `Governs`

**5.2.3** Every normative standard SHALL contain the following eight level-2 sections in fixed sequential order:
1. `## 1. Purpose` *(Informative)*
2. `## 2. Scope & Applicability` *(Normative)*
3. `## 3. Normative References` *(Normative)*
4. `## 4. Terms & Definitions` *(Normative)*
5. `## 5. Requirements` *(Normative)*
6. `## 6. Conformance & Verification` *(Normative)*
7. `## 7. Linked Artifacts` *(Normative)*
8. `## 8. Revision History` *(Informative)*

**5.2.4** If a standard governs no assets or templates, Section 7 SHALL remain present and explicitly state `None.` Sections SHALL NOT be omitted or reordered.

**5.2.5** All clauses inside Section 5 SHALL be uniquely numbered (for example, `5.1.1`, `5.2.3`) to support unambiguous citation and audit traceability.

**5.2.6** Informative notes, rationale, or worked examples placed within normative sections SHALL be visually isolated inside a Markdown blockquote prefixed with `> **Informative Note:**` or `> **Example:**`. Normative verbatim copy blocks (such as approved boilerplates in `C01 §5.5.1`) SHOULD use fenced text blocks rather than blockquotes.

> **Example:** A requirement in Section 5 may be followed by `> **Informative Note:** This rule ensures deterministic sorting across operating systems.` to explain intent without altering the binding clause.

**5.2.7** All dates in metadata headers, revision histories, and registers SHALL follow International Organization for Standardization (`ISO`) 8601 format (`YYYY-MM-DD`) in accordance with `C04`.

**5.2.8** The `Governs` metadata field SHALL list all non-`Deprecated` `AST-` and `TPL-` codes registered in Section 7 of that standard. Where Section 7 lists no active items, `Governs` SHALL state `None`.

### 5.3 Normative Language & Drafting Discipline
**5.3.1** Normative clauses SHALL express requirements exclusively using the following uppercase keywords:
* `SHALL` / `SHALL NOT` — Mandatory requirement or absolute prohibition. Non-compliance is a non-conformity unless covered by a time-boxed waiver under `A04`.
* `SHOULD` / `SHOULD NOT` — Recommended default or strong discouragement. Deviation is permitted only when a documented technical or operational justification is recorded.
* `MAY` — Permissible option. Implementing or omitting the option requires no justification.

**5.3.2** Keywords carry normative force only when written in ALL CAPS. Lowercase occurrences (`shall`, `should`, `may`) SHALL NOT be used to express normative rules.

**5.3.3** Authors SHALL NOT use `MUST`, `WILL`, or `REQUIRED` as synonyms for `SHALL` inside normative clauses.

**5.3.4** Informative statements describing facts, capabilities, or consequences SHALL use lowercase ordinary verbs (such as `is`, `can`, `applies`).

**5.3.5** Every `SHALL` and `SHALL NOT` clause SHALL be objectively verifiable on a pass/fail basis. Subjective adjectives (such as *clean*, *appropriate*, *reasonable*, or *timely*) SHALL NOT appear inside a `SHALL` clause unless paired with a measurable threshold or defined reference.

### 5.4 Lifecycle Statuses & State Transitions
**5.4.1** Every normative standard SHALL hold exactly one of the following five controlled status values in both its metadata header and `Library-Index.md`:
* `Planned` — Code allocated in `Library-Index.md`; file does not yet exist.
* `Draft` — File created (`v0.Y.0`) and under active authoring; non-binding.
* `In Review` — Content frozen for formal verification and Approver sign-off; non-binding.
* `Approved` — Active, binding standard (`v1.0.0` or higher).
* `Deprecated` — Retired or superseded; non-binding; code permanently locked against reuse per `A02`.

**5.4.2** Only standards in `Approved` status SHALL be enforced in conformance audits or cited as binding requirements in deliverables.

**5.4.3** Every Master Asset (`AST-`) and Executable Template (`TPL-`) in `Library-Index.md` SHALL hold exactly one of four controlled status values: `Planned`, `Approved`, `Sync Required`, or `Deprecated`.

**5.4.4** A reserved series (`F`, `G`, or `H`) SHALL remain inactive until activated by the Approver. Activation SHOULD occur only when a recurring operational risk, repeat client requirement, or cross-project failure justifies formal company-wide rules.

**5.4.5** Every Compiled Publication (`PUB-`) in `Library-Index.md` SHALL hold exactly one of four controlled status values: `Planned`, `Approved`, `Sync Required`, or `Deprecated`.

**5.4.6** Every Governance Record (`REC-`) in `Library-Index.md` SHALL hold exactly one of six controlled status values: `Open`, `Approved`, `Rejected`, `Expired`, `Revoked`, or `Closed` (`A04 §5.2.2`, `§5.4.5`).

### 5.5 Versioning (`vMAJOR.MINOR.ERRATA`)
**5.5.1** Every normative standard and `Library-Index.md` SHALL use a strict three-part numeric version formatted as `vMAJOR.MINOR.ERRATA` (for example, `v1.2.0`). Trailing prose labels (such as `errata 4` or `rev B`) SHALL NOT be used in version identifiers.

**5.5.2** Pre-release drafts SHALL use `MAJOR = 0` (starting at `v0.1.0` and incrementing `MINOR` for subsequent draft iterations). Upon initial formal approval, the version SHALL advance to `v1.0.0`.

**5.5.3** `MAJOR` (`vX.0.0`) SHALL increment for any breaking change. Breaking changes include altering or removing a `SHALL` or `SHALL NOT` clause, renumbering clauses, or invalidating compliant outputs, assets, or templates. Incrementing `MAJOR` SHALL:
* Reset `MINOR` and `ERRATA` to `0`.
* Require full review and explicit Approver sign-off.
* Trigger archival of the outgoing approved snapshot per Clause `5.7.2`.
* Transition all dependent `AST-` and `TPL-` files pinned to the prior `MAJOR` version to `Sync Required` status until verified or updated.

**5.5.4** `MINOR` (`vX.Y.0`) SHALL increment for non-breaking substantive changes, including adding new clauses, expanding scope, or clarifying guidance without invalidating previously compliant work. Incrementing `MINOR` SHALL:
* Reset `ERRATA` to `0`.
* Require Approver sign-off.
* Trigger archival of the outgoing approved snapshot per Clause `5.7.2`.

**5.5.5** `ERRATA` (`vX.Y.Z`) SHALL increment solely for editorial corrections—such as spelling fixes, broken links, or formatting repairs—that produce zero change to normative meaning. An `ERRATA` update:
* SHALL be logged in Section 8 by the Owner.
* SHALL receive written Approver confirmation (such as an approval note, commit review, or logged message) before release.
* SHALL NOT trigger re-audits or transition linked assets to `Sync Required`.

**5.5.6** Routine metadata synchronizations in `Library-Index.md` SHALL increment `ERRATA` (`vX.Y.Z`) with Owner execution and written Approver confirmation, and SHALL NOT require Cold Archive snapshots in Google Drive `99_Archive/`. Routine synchronizations record lifecycle changes, artifact registrations, or `REC-` entries without altering register schema or Sections 1 through 3. Schema or governance-section changes to `Library-Index.md` SHALL increment `MINOR` or `MAJOR` and trigger archival per Clause `5.7.2`.

**5.5.7** Routine Section 7 artifact status updates and Section 3 `Library-Index.md` reference-floor updates SHALL increment `ERRATA` (`vX.Y.Z`) when Sections 2 through 6 remain unchanged. These updates SHALL follow Clause `5.5.5` and SHALL NOT require Cold Archive snapshots in Google Drive `99_Archive/`.

### 5.6 Review Cadence & Maintenance
**5.6.1** Every `Approved` normative standard SHALL carry an explicit `Next Review` date in its metadata header and `Library-Index.md`.

**5.6.2** Scheduled periodic reviews SHALL follow this cadence unless an individual standard specifies a shorter interval:
* **Year 1 after initial approval (`v1.0.0`):** Every 6 months.
* **Subsequent years:** Every 12 months.

**5.6.3** An event-driven review SHALL be initiated within 15 business days whenever any of the following occurs:
* A statutory, regulatory, or contractual obligation changes in a way that affects the standard.
* A compliance audit (`REC-A04`) identifies a structural ambiguity or conflict with another standard.
* An upstream normative reference undergoes a `MAJOR` revision.

**5.6.4** If a review confirms no changes are needed, the Owner SHALL update the `Next Review` date in the metadata header and `Library-Index.md` and log a review confirmation note without incrementing the standard version.

**5.6.5** Any standard whose `Next Review` date has passed by more than 30 calendar days SHALL be flagged as overdue in the next consistency review (`REC-A04`).

### 5.7 Archival & Drift Control
**5.7.1** Active controlled files in `01_Standards/`, `02_Assets/`, `03_Templates/`, `04_Publications/`, and `05_Records/` SHALL NOT include version numbers in their filenames.

**5.7.2** Git commit history and annotated release tags in the Authoring Repository (`5.9.1`) SHALL serve as the canonical historical record for all revisions. Prior to overwriting any `MAJOR` or `MINOR` revision in the Distribution Mirror (`5.9.3`), the publish workflow SHALL copy the outgoing approved file unmodified into the Google Drive Cold Archive (`99_Archive/`) with its archive suffix appended per `A02 §5.6.1`.

**5.7.3** Upon transitioning a controlled item to `Deprecated`, the Owner SHALL archive its final snapshot to the Google Drive Cold Archive (`99_Archive/`) per `A02 §5.6.1`, remove the active file from the Authoring Repository working tree, and update `Library-Index.md` with its `Deprecated` status, superseding code, and Cold Archive path. Terminal Governance Records (`REC-`) retained permanently in `05_Records/` per `A04 §5.5.3` are exempt. Files in `99_Archive/` SHALL NOT be modified, duplicated, or deleted after archival.

**5.7.4** Every `AST-` and `TPL-` entry in `Library-Index.md` and in Section 7 of its governing standard SHALL pin the exact `MAJOR.MINOR` standard version against which it was verified using parenthetical notation (for example, `B01 (v2.1)` per `A02 §5.7.2`).

**5.7.5** Every Compiled Publication (`PUB-`) SHALL include a visible build manifest stating its compile date, the exact `vMAJOR.MINOR.ERRATA` versions of all source standards used to generate it, and a notice stating that active normative standards prevail in the event of a conflict.

### 5.8 Register Synchronization
**5.8.1** Every status change, version increment, archival action, or new controlled item registration SHALL be reflected in `Library-Index.md` on the same calendar date as the change.

**5.8.2** Where metadata in a standard's header differs from `Library-Index.md`, the Owner SHALL resolve the discrepancy within 1 business day of discovery. Any discrepancy remaining unresolved past 1 business day SHALL be logged as a `Major` non-conformity under `A04 §5.2.1`.

### 5.9 Hybrid Repository Architecture
**5.9.1** The Authoring Repository of Record SHALL be the GitHub repository `haryirfantri/irvantri-standards` (`Standards Design/` directory on the `main` branch). Only controlled items committed to `main` inside `Standards Design/` SHALL count as active binding editions of this library.

**5.9.2** Unapproved `Draft` and `In Review` revisions SHALL be authored on Git feature branches and verified through Pull Requests running the automated `CI` checks (`A04 §5.1.7`) prior to Approver merge to `main`. A `98_Drafts/` folder SHALL NOT be maintained inside the controlled library tree.

**5.9.3** The Google Drive folder `Standards Design` (folder ID `17-hTsw-2MIT-SzA6pRgzocpKTy1vwYin`) SHALL operate as the read-only Distribution Mirror for active controlled files (`Library-Index.md` and `01_Standards/` through `06_Dependencies/`) and as the append-only Cold Archive (`99_Archive/`). Synchronization from the Authoring Repository to the Distribution Mirror SHALL be strictly one-way (`GitHub → Google Drive`). Controlled files inside the Distribution Mirror SHALL NOT be edited manually; where the Distribution Mirror differs from GitHub `main`, GitHub `main` SHALL prevail.

**5.9.4** Non-controlled working notes, stakeholder briefs, or vendor proofs stored outside `Standards Design/` on Google Drive SHALL NOT be registered in `Library-Index.md`, cited as binding requirements (`5.4.2`), or synced automatically. Content adopted from outside the Authoring Repository SHALL enter through a reviewed Pull Request under Clause `5.9.2`.

## 6. Conformance & Verification

A standard or controlled update conforms to `A01` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `A01-C1` | File exists as a standalone Markdown file under `01_Standards/` (and controlled files in `02_Assets/`, `03_Templates/`, `04_Publications/`, and `05_Records/`) with no version suffix in its active filename (`5.2.1`, `5.7.1`). | Repository inspection |
| `A01-C2` | Metadata header contains all 9 required fields in exact order (`5.2.2`), uses `ISO` 8601 dates (`5.2.7`), and populates `Governs` with all non-`Deprecated` Section 7 codes or `None` (`5.2.8`). | Header inspection |
| `A01-C3` | Document contains all 8 fixed level-2 sections in exact order (`5.2.3`) with Section 7 explicitly populated or marked `None.` (`5.2.4`), numbered clauses in Section 5 (`5.2.5`), and prefixed blockquotes for informative notes/examples (`5.2.6`). | Structural inspection |
| `A01-C4` | Normative clauses use only uppercase `SHALL`, `SHALL NOT`, `SHOULD`, `SHOULD NOT`, and `MAY`, with zero prohibited synonyms (`MUST`, `WILL`, `REQUIRED`), and all `SHALL` / `SHALL NOT` clauses are objectively testable without unmeasured subjective adjectives (`5.3.1`–`5.3.5`). | Text / regex audit |
| `A01-C5` | Version string matches `vMAJOR.MINOR.ERRATA` (`5.5.1`) and matches the severity of changes logged in Section 8 (`5.5.2`–`5.5.7`). | Diff & changelog review |
| `A01-C6` | Canonical Git commit history preserves every release, and outgoing snapshots for published `MAJOR`, `MINOR`, and `Deprecated` releases exist unmodified in the Google Drive Cold Archive (`99_Archive/`) with unique archive suffixes (`5.7.2`, `5.7.3`). | Git & Drive archive inspection |
| `A01-C7` | `Library-Index.md` matches the document's `Version`, `Status`, `Owner`, and `Next Review` date on the date of release (`5.8.1`). | Register cross-check (`library_checks.py`) |
| `A01-C8` | Dependent `AST-`/`TPL-` files are marked `Sync Required` whenever their governing standard increments `MAJOR` (`5.5.3`). | Register cross-check |
| `A01-C9` | Owner/Approver separation (`5.1.1`–`5.1.3`), precedence and overlap logging (`5.1.4`), controlled status validity across all artifact layers (`5.4.1`–`5.4.6`), and periodic/event-driven review triggers (`5.6.1`–`5.6.5`) are upheld. | Register & role audit |
| `A01-C10` | `Deprecated` items are archived per `5.7.3`, `AST-`/`TPL-` files carry `MAJOR.MINOR` pins (`5.7.4`), `PUB-` files include build manifests (`5.7.5`), and metadata defects resolve within 1 business day (`5.8.2`). | Repository & artifact audit |
| `A01-C11` | Active controlled files live in GitHub `main` (`Standards Design/`) with zero `98_Drafts/` folder inside the controlled tree (`5.9.1`, `5.9.2`), Google Drive mirrors active files strictly one-way from `main` without manual drift (`5.9.3`), and external working files are never cited as binding (`5.9.4`). | GitHub & Drive mirror audit |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with `A04`.

## 7. Linked Artifacts

None.

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v2.0.0` | `2026-11-28` | Major | Renamed the library to `Standards Design`; added Section `5.9` establishing GitHub (`haryirfantri/irvantri-standards`) as the Authoring Repository of Record (`5.9.1`–`5.9.2`) and Google Drive (`Standards Design`) as the one-way Distribution Mirror and append-only Cold Archive (`5.9.3`–`5.9.4`), retiring `98_Drafts/` inside the controlled tree; updated `5.7.2`–`5.7.3`, `A01-C6`, and added `A01-C11` so Git history/tags serve as canonical version history while Drive hosts `99_Archive/` per `REC-A04-016`. | Hary Irfantri |
| `v1.2.0` | `2026-11-25` | Minor | Defined `Governs` header population rules (`5.2.8`), classified routine Section 7 status syncs and Section 3 reference-floor updates as `ERRATA` (`5.5.7`), mapped `5.1.4`, `5.2.6`, `5.2.8`, and `5.5.7` in Section 6, removed obsolete pre-approval note in Section 3, and split 30+ word sentences in `5.5.3`, `5.5.6`, and `5.7.3` per `REC-A04-005` (`F-07`, `F-10`). | Hary Irfantri |
| `v1.1.0` | `2026-11-22` | Minor | Defined Reviewer role, `PUB-`/`REC-` controlled statuses (`5.4.5`–`5.4.6`), `Library-Index.md` sync increment rule (`5.5.6`), 1-business-day metadata defect threshold (`5.8.2`), `05_Records/` active naming and retention alignment (`5.7.1`, `5.7.3`), parenthetical `MAJOR.MINOR` pinning (`5.7.4`), written confirmation definition (`5.5.5`), expanded `PRD`/`ISO`, and added `A01-C9` and `A01-C10` per `REC-A04-001`. | Hary Irfantri |
| `v1.0.1` | `2026-11-20` | Errata | Updated repository folder path references (`01_Standards/`, `02_Assets/`, `03_Templates/`, `04_Publications/`, `99_Archive/`) to English Title Case per `A02` naming convention. | Hary Irfantri |
| `v1.0.0` | `2026-11-20` | Major | Initial approved baseline of `A01` (Document Control & Lifecycle), confirming Year-1/subsequent review cadence and lightweight Approver confirmation for errata. | Hary Irfantri |
| `v0.1.0` | `2026-11-20` | Pre-Release | Initial draft establishing document anatomy, normative language, lifecycle statuses, `vMAJOR.MINOR.ERRATA` versioning, review cadence, archival, and drift controls. | Hary Irfantri |
