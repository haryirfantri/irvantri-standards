# D05 — Generated Outputs & Exports

| Field | Value |
| :--- | :--- |
| **Code** | `D05` |
| **Version** | `v1.1.1` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-25` |
| **Next Review** | `2027-05-22` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `None` |

## 1. Purpose

This standard defines the formatting, metadata, timestamp, file naming, table, and attribution requirements for system-generated documents and data exports across **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`). It ensures generated outputs and exports remain traceable, machine-parseable, and aligned with governing library standards.

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* All system-generated Portable Document Format (`PDF`) documents, Comma-Separated Values (`CSV`) exports, and structured data exports produced by **Irvantri Standards** digital systems (`D01`–`D04`).
* All export audit timestamps, header/metadata fields, export filenames, and tabular structures generated for internal or external distribution.

### 2.2 Out of Scope
This standard does not govern:
* Manually authored formal document templates and print specifications (governed by `E01`–`E03`).
* Compiled human-facing publications (`PUB-`) and their source build manifests (governed by `A01 §5.7.5` and `Library-Index.md`).
* Interactive user interface controls, forms, and error dialogs prior to export generation (governed by `C03` and `D03`).

## 3. Normative References

The following documents are referenced in this standard. For undated references, the latest approved edition applies.
* `A02` — Taxonomy, Coding & File Naming.
* `A03` — Entity & Brand Architecture.
* `A04` — Compliance, Reviews & Exceptions.
* `B02` — Color System.
* `B03` — Typography.
* `C02` — Terminology & Controlled Vocabulary.
* `C04` — Data, Dates & Citation Formatting.
* `D03` — Interface Components & Patterns.
* `E02` — Versioning & Draft Marking.

## 4. Terms & Definitions

For terms shared across the library, refer to `C02`, `C04`, `B02`, and `D03`. For the purposes of this standard, the following definitions apply:
* **Audit Timestamp:** A Coordinated Universal Time (`UTC`) or offset-qualified date-time value recording when an export or generated output was produced (`C04 §5.1.2`).
* **Data Export:** A machine-readable or tabular file—such as `CSV`—extracted from system records.
* **Generated Output:** A formatted document or report—such as a `PDF`—rendered programmatically by a system or workflow.

## 5. Requirements

### 5.1 Timestamps, Numbers & Units in Exports
**5.1.1** Generated outputs and data exports SHALL record creation or audit timestamps in International Organization for Standardization (`ISO`) 8601 format (`YYYY-MM-DDTHH:MM:SSZ` in `UTC` or with an explicit `±HH:MM` offset) (`C04 §5.1.2`). Standalone calendar dates SHALL use `YYYY-MM-DD` (`C04 §5.1.1`).

**5.1.2** Numeric values, percentages, currencies, and measurement units in generated outputs and exports SHALL follow `C04 §5.2`–`§5.3`. Exports SHALL use leading zeros on decimals between `-1` and `1` and uppercase `ISO` 4217 currency codes without bare `$`. Exports SHALL also apply spaced units and explicit `MB`/`GB` versus `MiB`/`GiB` prefixes.

**5.1.3** Systems SHALL store Audit Timestamps in `UTC` (`5.1.1`). User interfaces MAY render stored timestamps in a configured local time zone when an explicit offset or zone label appears (`C04 §5.1.2`).

### 5.2 Tabular Integrity, Naming, Trigger Discipline & Attribution
**5.2.1** `CSV` and tabular exports SHALL include a header row naming each column and SHALL NOT leave data cells blank (`None` or `—` per `C04 §5.4.1`). Numeric column headers SHALL declare shared units (`C04 §5.4.2`).

**5.2.2** Generated `PDF` and tabular outputs SHALL use exact controlled status strings (`C02 §5.4.1`). Outputs SHALL NOT expose internal stack traces, raw database schemas, or internal project codenames (`D03 §5.2.3`, `A03 §5.4.2`).

**5.2.3** Controlled library deliverables generated or exported SHALL follow `A02 §5.4` filename syntax (`CODE_Title-Words.ext`). External and formal exports SHALL preserve authoritative **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`) and `A member of Irvantri Group` attribution (`A03 §5.2.1`, `§5.3.1`, `§5.6.1`).

**5.2.4** Generated `PDF` outputs SHALL apply `B02` and `B03` palette, contrast, and typography rules. Outputs SHALL carry sequential table and figure captions (`Table 1`, `Figure 1`) where tables or figures appear (`C04 §5.4.4`).

**5.2.5** Digital systems SHALL NOT automatically generate finalized formal reports or official exports on routine record save actions. Export generation SHALL require an explicit user action and confirmation for consequential outputs (`D03 §5.4.1`).

**5.2.6** Unfinalized or working exports SHALL display controlled `Draft` or `In Review` status markings (`C02 §5.4.1`, `E02 §5.2.1`) rather than informal `PROVISIONAL` labels (`C02 §5.4.2`).

## 6. Conformance & Verification

A generated output or export conforms to `D05` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `D05-C1` | Exports include `ISO` 8601 timestamps and `YYYY-MM-DD` dates (`5.1.1`), store Audit Timestamps in `UTC` with explicit local-zone offsets when displayed (`5.1.3`), and follow `C04` numeric, currency, and unit rules (`5.1.2`). | Schema & format audit |
| `D05-C2` | Tabular exports include headers, zero blank cells, and declared units (`5.2.1`), use `C02` controlled statuses without stack traces/schemas/codenames (`5.2.2`), follow `A02`/`A03` naming and attribution (`5.2.3`), meet `B02`/`B03`/`C04` `PDF` layout rules (`5.2.4`), require explicit user triggers without auto-generating on save (`5.2.5`), and mark unfinalized outputs with controlled `Draft`/`In Review` labels (`5.2.6`). | Export, workflow & layout audit |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with `A04`.

## 7. Linked Artifacts

None.

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v1.1.1` | `2026-11-25` | Errata | Split 30+ word sentence in `5.1.2` and confirmed `D03 (v2.0.0)` alignment per `REC-A04-005` (`F-10`). | Hary Irfantri |
| `v1.1.0` | `2026-11-24` | Minor | Added `UTC` storage and explicit local time-zone display rule (`5.1.3`), prohibited auto-generating formal reports on routine saves (`5.2.5`), mandated controlled `Draft`/`In Review` markings for unfinalized exports instead of informal `PROVISIONAL` labels (`5.2.6`), added `E02` reference, and updated `D05-C1` and `D05-C2`. | Hary Irfantri |
| `v1.0.1` | `2026-11-23` | Errata | Removed leaked chat citation strings across Sections 1–8, trimmed unused Section 3 references (`Library-Index.md`, `A01`, `B01`, `B04`, `B05`, `C01`, `C03`, `D01`, `D02`, `D04`), and split long Section 5 sentences per `REC-A04-004` (`F-02`, `F-04`). | Hary Irfantri |
| `v1.0.0` | `2026-11-22` | Major | Initial approved baseline of `D05` (Generated Outputs & Exports), locking `ISO` 8601 timestamps and `C04` numeric/unit rules, `CSV`/tabular completeness, `C02` status and non-exposure rules, `A02`/`A03` naming and attribution, and `B02`/`B03`/`C04` `PDF` layout rules. | Hary Irfantri |
| `v0.1.0` | `2026-11-22` | Pre-Release | Initial draft establishing `ISO` 8601 timestamps and `C04` numeric/unit rules, `CSV`/tabular completeness, `C02` status and non-exposure rules, `A02`/`A03` naming and attribution, and `B02`/`B03`/`C04` `PDF` layout rules. | Hary Irfantri |
