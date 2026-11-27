# A04 — Compliance, Reviews & Exceptions

| Field | Value |
| :--- | :--- |
| **Code** | `A04` |
| **Version** | `v1.1.1` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-25` |
| **Next Review** | `2027-05-20` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `None` |

## 1. Purpose

This standard establishes the framework for verifying conformance, conducting consistency reviews, classifying and remediating non-conformities, resolving cross-standard conflicts, and granting time-boxed waivers across the **Irvantri Standards Unified Operating Library**. It ensures that compliance is objectively testable, deviations remain visible and bounded, and the library stays internally coherent over time.

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* All conformance audits and scheduled or event-driven consistency reviews of controlled items tracked in `Library-Index.md`.
* All conformance checks applied to products, portals, formal documents, compiled publications, and client deliverables governed by `Approved` standards.
* All cross-standard overlaps or contradictions identified across Series `A`–`H`.
* All formal exception requests, time-boxed waivers, renewals, revocations, and Governance Records (`REC-`) saved in `05_Records/`.

### 2.2 Out of Scope
This standard does not govern:
* Waivers of statutory regulations, regulatory mandates, or binding client contract terms (which supersede this library per `A01 §5.1.4` and cannot be waived internally).
* Standard lifecycle transitions, versioning increments, or periodic standard review schedules (governed by `A01`).
* Informal engineering trade-offs or project-level technical debt that do not violate an `Approved` library standard.

## 3. Normative References

The following documents are referenced in this standard. For undated references, the latest approved edition applies.
* `Library-Index.md` — Irvantri Standards Unified Operating Library Index (`v1.1.0` or later).
* `A01` — Document Control & Lifecycle.
* `A02` — Taxonomy, Coding & File Naming.
* `A03` — Entity & Brand Architecture.
* `C02` — Terminology & Controlled Vocabulary.
* `C04` — Data, Dates & Citation Formatting.

## 4. Terms & Definitions

For terms shared across the library, refer to `C02`, `A01`, `A02`, and `A03`. For the purposes of this standard, the following definitions apply:
* **Compensating Control:** A temporary safeguard or alternative measure applied during an active waiver period to reduce risk until full conformance is restored.
* **Consistency Review:** A structured audit evaluating alignment across `Library-Index.md`, active standards, linked Master Assets (`AST-`), Executable Templates (`TPL-`), Compiled Publications (`PUB-`), and Governance Records (`REC-`).
* **Non-Conformity:** Any verifiable failure of a controlled item, product, document, or deliverable to satisfy a `SHALL` or `SHALL NOT` clause of an `Approved` standard without an active waiver, or an undocumented deviation from a `SHOULD` or `SHOULD NOT` clause (`5.4.2`).
* **Remediation Plan:** A concrete, dated sequence of actions assigned to an Owner to bring a non-conforming item into full conformance.
* **Waiver:** A formal, written, time-boxed authorization issued by the Approver permitting a scoped deviation from one or more `SHALL` or `SHALL NOT` clauses of an `Approved` standard.

## 5. Requirements

### 5.1 Conformance Verification & Consistency Reviews
**5.1.1** Conformance verification SHALL evaluate items strictly against the objective verification checks defined in Section 6 (`[CODE]-C#`) of each applicable `Approved` standard. Standards in `Planned`, `Draft`, `In Review`, or `Deprecated` status SHALL NOT be enforced as binding audit criteria (`A01 §5.4.2`).

**5.1.2** Verification SHALL be performed across three mandatory trigger modes:
1. **Pre-Release Gate:** Prior to promoting any normative standard (`A01`–`H99`), Master Asset (`AST-`), Executable Template (`TPL-`), or Compiled Publication (`PUB-`) to `Approved` status.
2. **Scheduled Consistency Review:** A library-wide audit conducted at least once every 6 months during Year 1 of library operation and at least once every 12 months thereafter.
3. **Event-Driven Audit:** Initiated within 15 business days of a `MAJOR` standard revision, a reported `Critical` non-conformity, or a cross-standard conflict.

**5.1.3** Every Scheduled Consistency Review SHALL inspect and record pass/fail status for all of the following library controls:
* Metadata synchronization between `Library-Index.md` and every active standard header (`A01 §5.8.1`).
* Overdue standard reviews whose `Next Review` date has passed by more than 30 calendar days (`A01 §5.6.5`).
* Asset and template drift, confirming that every `AST-` and `TPL-` file matches its pinned `[CODE] (vMAJOR.MINOR)` standard version or carries `Sync Required` status (`A01 §5.7.4`, `A02 §5.7.2`).
* Archive integrity in `99_Archive/`, verifying unmodified snapshots exist for all superseded `MAJOR` and `MINOR` releases (`A01 §5.7.2`, `A02 §5.6`).
* Active waivers, verifying that no waiver has passed its `Expiry Date` without formal closure or approved renewal (`5.4.9`).
* Cross-standard overlaps or contradictions logged since the previous review (`5.3.2`).

**5.1.4** Every Scheduled Consistency Review and Event-Driven Audit SHALL be documented as a Governance Record (`REC-A04-[001–999]`) saved in `05_Records/` per `A02`. Each record SHALL be registered in `Library-Index.md` Section 7 on the same calendar date (`A01 §5.8.1`).

### 5.2 Non-Conformity Classification & Remediation
**5.2.1** Every identified non-conformity SHALL receive a unique `Finding ID` in its `REC-A04` record and be classified into one severity tier with a binding remediation window:

| Severity | Objective Criteria | Remediation Service Level Agreement (`SLA`) |
| :--- | :--- | :--- |
| **Critical** | Breach of statutory/contractual precedence (`A01 §5.1.4`), improper legal entity binding (`A03 §5.2.4`), unapproved use of a `Draft` or `Deprecated` standard as binding, or any defect exposing legal, contractual, or security liability. | Not eligible for waiver (`5.4.3`). Containment within 2 business days; full closure within 5 business days. |
| **Major** | Violation of any `SHALL` or `SHALL NOT` clause without an active waiver (other than defects explicitly classified as `Critical` or `Minor`), unresolved cross-standard normative contradiction, `Sync Required` asset drift exceeding 15 business days, or metadata mismatch between a standard and `Library-Index.md` unresolved past 1 business day (`A01 §5.8.2`). | Full closure or approved waiver within 15 business days. |
| **Minor** | Editorial or formatting defect with zero normative impact, overdue standard review exceeding 30 calendar days (`A01 §5.6.5`), or undocumented deviation from a `SHOULD` / `SHOULD NOT` clause (`5.4.2`). | Full closure within 30 calendar days. |

**5.2.2** Each logged non-conformity SHALL record seven mandatory fields: `Finding ID`, `Affected Item`, `Violated Clause / Check ID`, `Severity`, `Assigned Owner`, `Due Date` (`YYYY-MM-DD`), and `Status` (`Open`, `Waived`, or `Closed`).

**5.2.3** A non-conformity SHALL NOT transition to `Closed` until the Reviewer or Approver inspects and records objective closure evidence inside the governing `REC-A04` file. For waivable `Major` findings, a verified waiver record per Clause `5.4` satisfies closure evidence.

**5.2.4** Any `Critical` non-conformity remaining `Open` past its Remediation `SLA` SHALL be escalated to the Approver within 1 business day and SHALL block release of the affected deliverable, asset, or publication. Any `Major` non-conformity remaining `Open` past its Remediation `SLA` without an approved waiver SHALL trigger the same escalation and release block.

### 5.3 Cross-Standard Conflict Resolution
**5.3.1** Whenever two `Approved` normative standards overlap or conflict, the precedence hierarchy in `A01 §5.1.4` SHALL govern immediate execution. Series `A` prevails over Series `B`–`H`, and specific standards prevail over general standards.

**5.3.2** The Owner or Reviewer who identifies a cross-standard conflict SHALL log it as a `Major` finding in a `REC-A04` record within 5 business days. Both clauses SHALL be cited using version-pinned notation (`A02 §5.7.2`).

**5.3.3** Logging a cross-standard conflict SHALL automatically trigger an event-driven review of the affected standards within 15 business days (`A01 §5.6.3`) to resolve the contradiction permanently through an approved revision.

### 5.4 Formal Exceptions & Time-Boxed Waivers
**5.4.1** A formal waiver SHALL be obtained before releasing or deploying any controlled item, product, portal, or deliverable that deviates from an `Approved` standard's `SHALL` or `SHALL NOT` clause.

**5.4.2** Deviations from `SHOULD` or `SHOULD NOT` clauses SHALL NOT require an `A04` waiver. Each deviation SHALL carry a written technical or operational justification recorded in the deliverable's documentation or review log (`A01 §5.3.1`).

**5.4.3** The following requirements are non-waivable and SHALL NOT receive a waiver under this standard:
* Statutory, regulatory, or binding contractual obligations (`A01 §5.1.4`).
* Approver sign-off authority rules (`A01 §5.1.2`–`5.1.3`).
* Legal entity separation prohibiting unauthorized binding of `Irvantri Group Pte. Ltd.` (`A03 §5.2.4`).

**5.4.4** Every waiver SHALL be strictly scoped to a specific project, product, deliverable, asset, or release. Blanket, organization-wide, or open-ended permanent waivers SHALL NOT be granted.

> **Informative Note:** If a deviation applies broadly across Irvantri Standards or needs to remain permanent, the correct mechanism is revising the underlying normative standard under `A01 §5.5`, not issuing a perpetual waiver.

**5.4.5** Every waiver request SHALL be submitted as a Governance Record (`REC-A04-[001–999]`) in `05_Records/` containing all nine mandatory fields before Approver review:
1. **Waiver ID:** Assigned `REC-A04-[001–999]` code.
2. **Requestor & Responsible Owner:** Named individual accountable for remediation.
3. **Target Scope:** Exact project, product, deliverable, or asset covered.
4. **Waived Clause(s):** Version-pinned standard code(s) and clause number(s) (for example, `E01 (v1.0.0) §5.2.1`).
5. **Objective Justification:** Verifiable technical, operational, or transitional reason conformance cannot be met immediately.
6. **Compensating Controls:** Concrete measures mitigating risk during the waiver window.
7. **Remediation Plan:** Actionable steps and milestones to achieve full conformance.
8. **Expiry Date:** Fixed International Organization for Standardization (`ISO`) 8601 date (`YYYY-MM-DD`) observing Clause `5.4.6`.
9. **Disposition & Sign-Off:** Approver decision (`Approved`, `Rejected`, `Expired`, `Revoked`, or `Closed`), decision date, and Approver name.

**5.4.6** Every approved waiver SHALL be time-boxed in accordance with the following duration and renewal limits:
* **Standard maximum duration:** 90 calendar days from approval date.
* **Extended maximum duration:** Up to 180 calendar days only where architectural or third-party engineering constraints are explicitly documented and countersigned by the Approver.
* **Renewals:** At most one renewal of up to 90 calendar days MAY be granted by the Approver upon review of documented remediation progress.
* **Post-renewal resolution:** If conformance is not achieved when a single renewal expires, no further renewal SHALL be granted. The issue SHALL become an overdue `Major` non-conformity or resolve via a standard revision under `A01 §5.5`.

**5.4.7** Only the Approver (`A01 §5.1.3`) SHALL approve, renew, or revoke a waiver. The Approver MAY revoke an active waiver early if compensating controls fail or documented legal, security, or operational risk increases materially. Revocation SHALL be recorded in the `REC-A04` file and `Library-Index.md` on the same calendar date.

**5.4.8** Every deliverable, specification, or asset operating under an active waiver SHALL visibly disclose the `Waiver ID` (`REC-A04-[001–999]`) and its `Expiry Date` in its metadata header or conformance statement.

**5.4.9** Upon reaching its `Expiry Date` without prior closure or approved renewal, a waiver SHALL automatically transition to `Expired` status, and any continuing deviation SHALL immediately become an unwaived `Major` non-conformity.

### 5.5 Governance Record Structure & Retention
**5.5.1** Every Governance Record (`REC-[StandardCode]-[001–999]`) in `05_Records/` SHALL follow `A02` naming (`REC-[StandardCode]-[001–999]_Title-Words.md`) and use `ISO` 8601 dates (`YYYY-MM-DD`) per `C04`. Each record SHALL open with a metadata header listing `Code`, `Record Type`, `Date`, `Status`, `Owner`, `Approver`, `Related Standards`, and `Expiry Date` (for waivers).

**5.5.2** Every new or updated `REC-` file SHALL be registered or updated—including `Status` and `Expiry Date` where applicable—in `Library-Index.md` Section 7 on the same calendar date (`A01 §5.8.1`).

**5.5.3** Once a `REC-` Consistency Review, Approval Record, or Waiver reaches terminal status (`Closed`, `Rejected`, `Expired`, or `Revoked`), it SHALL remain immutable in `05_Records/`. Terminal records SHALL NOT be deleted or retroactively altered.

## 6. Conformance & Verification

An audit, conflict log, or exception waiver conforms to `A04` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `A04-C1` | Scheduled Consistency Reviews are logged as `REC-A04` records within the mandatory cadence (`5.1.2`) and cover all six required inspection areas (`5.1.3`). | Record & register audit |
| `A04-C2` | Every logged non-conformity carries a valid severity tier, all seven mandatory fields (`5.2.2`), and verifiable closure evidence prior to `Closed` status (`5.2.3`). | `REC-A04` inspection |
| `A04-C3` | Every cross-standard conflict is logged within 5 business days (`5.3.2`) and triggers an event-driven standard review within 15 business days (`5.3.3`). | Record & review date check |
| `A04-C4` | Zero waivers have been issued for non-waivable clauses (`5.4.3`), and zero blanket or open-ended waivers exist (`5.4.4`). | Waiver register audit |
| `A04-C5` | Every active or historical waiver record contains all nine mandatory fields (`5.4.5`), respects the 90/180-day duration and single-renewal caps (`5.4.6`), and carries Approver sign-off (`5.4.7`). | `REC-A04` inspection |
| `A04-C6` | Deliverables relying on an active waiver explicitly disclose the `Waiver ID` and `Expiry Date` (`5.4.8`), and zero expired waivers remain operating as active (`5.4.9`). | Deliverable & date audit |
| `A04-C7` | Every `REC-` file complies with `A02` naming and `5.5.1` header fields, syncs `Status` and `Expiry Date` in `Library-Index.md` Section 7 on the same date (`5.5.2`), and terminal records remain unmodified (`5.5.3`). | Repository & register check |
| `A04-C8` | Non-Approved standards are excluded from binding audits (`5.1.1`); Pre-Release Gates and 15-business-day Event-Driven Audits execute on trigger (`5.1.2`); overdue `Critical`/`Major` findings escalate within 1 business day and block release (`5.2.4`). | Audit & release log review |
| `A04-C9` | Waivers are approved prior to release (`5.4.1`), and deviations from `SHOULD`/`SHOULD NOT` clauses carry documented justifications (`5.4.2`). | Deliverable & review log audit |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with Clause `5.4`, subject to the non-waivable restrictions in Clause `5.4.3`.

## 7. Linked Artifacts

None.

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v1.1.1` | `2026-11-25` | Errata | Removed obsolete pre-approval note in Section 3 and tightened or split 30+ word sentences in `5.1.4`, `5.2.1`, `5.2.3`, `5.3.1`–`5.3.2`, `5.4.1`–`5.4.2`, `5.4.6`–`5.4.7`, `5.5.1`, and `5.5.3` per `REC-A04-005` (`F-10`). | Hary Irfantri |
| `v1.1.0` | `2026-11-22` | Minor | Resolved Non-Conformity definition and `Critical`/`Major`/`Minor` tier overlaps (`4`, `5.2.1`, `5.2.3`–`5.2.4`), aligned 1-business-day metadata mismatch escalation with `A01 §5.8.2`, fixed `5.1.3` internal citations (`5.4.9`, `5.3.2`), generalized Section 5.5 to all `REC-` records with `C04` date citation, standardized `REC-A04-[001–999]` notation, expanded `SLA`/`ISO`, and added `A04-C8` and `A04-C9` per `REC-A04-001`. | Hary Irfantri |
| `v1.0.0` | `2026-11-20` | Major | Initial approved baseline of `A04` (Compliance, Reviews & Exceptions), confirming scheduled consistency review cadence, three-tier non-conformity `SLA`s, cross-standard conflict resolution, and 90/180-day single-renewal waiver caps. | Hary Irfantri |
| `v0.1.0` | `2026-11-20` | Pre-Release | Initial draft establishing conformance verification triggers, consistency review controls, three-tier non-conformity `SLA`s, cross-standard conflict resolution, time-boxed waiver governance, and `REC-A04` record immutability. | Hary Irfantri |
