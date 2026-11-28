# C03 — Technical & User Experience (UX) Writing

| Field | Value |
| :--- | :--- |
| **Code** | `C03` |
| **Version** | `v1.0.1` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-25` |
| **Next Review** | `2027-05-22` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `None` |

## 1. Purpose

This standard defines the microcopy patterns, interface labeling conventions, error and validation message structure, confirmation dialog rules, empty state requirements, and procedural writing rules for **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`). It ensures User Interface (`UI`) text and technical documentation are clear, consistent, actionable, and blame-free.

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* All digital products, web portals, interactive controls, alerts, and system notifications (`D01`–`D05`).
* All technical guides, operational procedures, setup instructions, and product documentation (`PUB-`, `Library-Index.md`).
* All system-generated status messages, validation feedback, and export dialogs (`D05`, `E01`).

### 2.2 Out of Scope
This standard does not govern:
* Normative keyword semantics (`SHALL`, `SHOULD`, `MAY`) or standard document anatomy (governed by `A01`).
* General editorial voice, tone register matrix, sentence limits, or United States English (`en-US`) mechanics (governed by `C01`).
* Canonical glossary terms, acronym exemptions, or fixed status strings (governed by `C02`).
* Date, timestamp, numeric, unit, and bibliographic citation formatting (governed by `C04`).
* Visual layout, focus order, or Accessible Rich Internet Applications (`ARIA`) implementation details (governed by `D03` and `D04`).

## 3. Normative References

The following documents are referenced in this standard. For undated references, the latest approved edition applies.
* `A01` — Document Control & Lifecycle.
* `A02` — Taxonomy, Coding & File Naming.
* `A03` — Entity & Brand Architecture.
* `A04` — Compliance, Reviews & Exceptions.
* `C01` — Voice, Tone & Plain Language.
* `C02` — Terminology & Controlled Vocabulary.
* `C04` — Data, Dates & Citation Formatting.
* `D03` — Interface Components & Patterns.
* `D04` — Accessibility & Usability.
* `D05` — Generated Outputs & Exports.
* `E01` — Formal Document Layout.

## 4. Terms & Definitions

For terms shared across the library, refer to `C02`, `A01`, `A02`, `A03`, `A04`, and `C01`. For the purposes of this standard, the following definitions apply:
* **Confirmation Dialog:** A modal or inline prompt requiring explicit user acknowledgment before executing a significant or irreversible system action.
* **Destructive Action:** Any operation that permanently deletes data, revokes active authorization, or transitions a controlled item to an irreversible state.
* **Empty State:** An interface view displayed when a list, table, search query, or workspace contains zero items to render.
* **Microcopy:** Short, functional interface text—such as button labels, field hints, tooltips, validation messages, and status alerts—that guides user interaction.
* **Procedural Writing:** Step-by-step instructional documentation organized chronologically to guide a reader through completing a defined task.

## 5. Requirements

### 5.1 Interface Microcopy, Labels & Contraction Rules
**5.1.1** Interactive buttons, links, and action controls SHALL open with an imperative verb and object (`Save changes`, `Export CSV`). Standalone ambiguous labels (`OK`, `Yes`, `Click Here`) SHALL NOT be used.

**5.1.2** `UI` labels, helper text, tooltips, and notifications SHALL use sentence case. Title Case SHALL apply only to proper nouns, registered Offerings (`C02 §5.3`), and controlled statuses (`C02 §5.4.1`).

**5.1.3** Primary button labels SHOULD NOT exceed `3` words or `24` characters. Inline helper text and toast notifications SHOULD NOT exceed `120` characters.

**5.1.4** Common contractions (`don't`, `can't`, `isn't`) MAY appear in interactive `UI` microcopy (`C01 §5.2.1`). Contractions SHALL NOT appear in legal notices, waiver disclosures (`A04 §5.4.8`), audit logs, or formal documents (`D05`, `E01`).

**5.1.5** Standalone button labels, field labels, navigation items, and single-phrase headings SHALL NOT end with a period. Multi-sentence helper text, error messages, and dialog body copy SHALL use terminal punctuation (`C01 §5.6.3`).

### 5.2 Error Messages & Validation Feedback
**5.2.1** Every user-facing error message SHALL state three elements: what occurred, why it occurred (when safe to disclose), and how to resolve the condition.

**5.2.2** Error messages SHALL use calm, objective, blame-free phrasing (`C01 §5.4.3`). Error messages SHALL NOT blame the user (`user error`, `your mistake`, or `you entered an invalid`).

**5.2.3** Error messages SHALL NOT expose raw stack traces, internal database schemas, unformatted exception dumps, or internal project codenames (`A03 §5.4.2`, `C02 §5.3.3`). Errors MAY display a structured diagnostic reference code.

**5.2.4** Inline validation messages SHALL identify the exact field and violated constraint (for example, `Enter a date in YYYY-MM-DD format.` per `C04`) and map to component error states (`D03`).

### 5.3 Confirmations, Destructive Actions & System Feedback
**5.3.1** Confirmation dialogs for destructive or irreversible actions (such as deleting records, revoking waivers, or deprecating controlled items) SHALL state the target item and permanent consequence.

**5.3.2** Primary buttons in destructive confirmation dialogs SHALL name the specific action and target object (`Delete source`, `Revoke waiver`). Generic labels (`OK`, `Confirm`, `Yes`) SHALL NOT be used.

**5.3.3** Success notifications SHALL state the completed action and affected object (`Library-Index.md saved.`). Success messages SHALL NOT contain exclamation marks (`!`) or promotional hyperbole (`C01 §5.1.2`).

**5.3.4** Progress and loading indicators SHOULD name the active operation using a present participle (`Validating metadata...`, `Syncing sources...`) rather than generic text (`Loading...` or `Please wait...`).

### 5.4 Empty States & Onboarding Prompts
**5.4.1** Every empty state in a table, list, search view, or workspace SHALL explain why no items appear (such as initial setup versus zero matching filter results).

**5.4.2** Actionable empty states SHALL provide a direct primary call to action or recovery step (such as creating an item or clearing filters) conforming to Clause `5.1.1`.

### 5.5 Procedural & Technical Writing
**5.5.1** Task-oriented technical guides and operational procedures SHALL present multi-step workflows as numbered lists (`1.`, `2.`, `3.`) in strict chronological execution order (`C01 §5.3.2`).

**5.5.2** Each procedural step SHALL state one primary action, open with an imperative verb, and specify the expected system outcome where verification is required.

**5.5.3** Prerequisites, required permissions, and destructive-action warnings SHALL appear immediately before the step to which they apply.

**5.5.4** Technical documentation SHALL reproduce exact `UI` labels (`C02 §5.1.1`), format file paths and identifiers in inline monospace (`A02 §5.4`), and preserve accessible control names (`D04`).

**5.5.5** Normative keywords (`SHALL`, `SHALL NOT`, `SHOULD`, `SHOULD NOT`, `MAY`) remain governed by `A01 §5.3` and SHALL NOT appear in `UI` microcopy or end-user tutorials.

## 6. Conformance & Verification

A digital interface, microcopy string, or technical guide conforms to `C03` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `C03-C1` | Interactive controls open with imperative verb-object labels (`5.1.1`), use sentence case (`5.1.2`), follow contraction boundaries (`5.1.4`), and observe terminal punctuation rules (`5.1.5`). | `UI` string & copy audit |
| `C03-C2` | User-facing error messages state what occurred, why, and how to recover (`5.2.1`) using objective, blame-free language (`5.2.2`). | Error catalog review |
| `C03-C3` | Error payloads expose zero stack traces, internal schemas, or codenames (`5.2.3`), and inline validation identifies exact fields and constraints (`5.2.4`). | Application & form testing |
| `C03-C4` | Destructive confirmations state the target item and consequence (`5.3.1`) with specific verb-object primary buttons (`5.3.2`). | Modal & workflow review |
| `C03-C5` | Success notifications state the completed action and object without exclamation marks or hyperbole (`5.3.3`). | Notification string audit |
| `C03-C6` | Empty states explain why no items appear (`5.4.1`) and provide a valid primary recovery action where actionable (`5.4.2`). | Empty state inspection |
| `C03-C7` | Multi-step procedures use numbered chronological steps (`5.5.1`), single imperative actions (`5.5.2`), and pre-step prerequisites or warnings (`5.5.3`). | Documentation review |
| `C03-C8` | Technical guides reproduce exact `UI` labels and format file paths and identifiers in inline monospace (`5.5.4`), and `UI` microcopy or tutorials contain zero normative keywords (`5.5.5`). | Editorial & lint check |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with `A04`.

## 7. Linked Artifacts

None.

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v1.0.1` | `2026-11-25` | Errata | Aligned `UI` button examples in `5.1.1` (`Save changes`) and `5.3.2` (`Delete source`, `Revoke waiver`) to sentence case (`5.1.2`), removed unused `Library-Index.md` and obsolete pre-approval note in Section 3, aligned `C03-C8` monospace scope wording with `5.5.4`, and confirmed `D03 (v2.0.0)` alignment per `REC-A04-005` (`F-06`, `F-09`, `F-10`). | Hary Irfantri |
| `v1.0.0` | `2026-11-22` | Major | Initial approved baseline of `C03` (Technical & User Experience (`UX`) Writing), establishing `UI` microcopy labeling, sentence-case and contraction boundaries, three-part blame-free error messaging, destructive confirmation rules, empty state requirements, and chronological procedural writing rules. | Hary Irfantri |
| `v0.1.0` | `2026-11-22` | Pre-Release | Initial draft establishing `UI` microcopy labeling, sentence-case and contraction boundaries, three-part blame-free error messaging, destructive confirmation rules, empty state requirements, and chronological procedural writing rules. | Hary Irfantri |
