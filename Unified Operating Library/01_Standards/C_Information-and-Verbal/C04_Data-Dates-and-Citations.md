# C04 — Data, Dates & Citation Formatting

| Field | Value |
| :--- | :--- |
| **Code** | `C04` |
| **Version** | `v1.0.1` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-25` |
| **Next Review** | `2027-05-22` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `None` |

## 1. Purpose

This standard defines the formatting rules for calendar dates, timestamps, numeric values, currencies, units of measurement, structured tables, hierarchical numbering, and external citations across **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`). It ensures quantitative data and source references remain unambiguous, machine-parseable, and consistent across all documents and interfaces.

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* All normative standards (`A01`–`H99`), registers (`Library-Index.md`), and Governance Records (`REC-`).
* All digital interfaces, system logs, data tables, and generated exports (`D01`–`D05`).
* All formal documents, compiled publications (`PUB-`), proposals, and external correspondence (`E01`–`E04`).

### 2.2 Out of Scope
This standard does not govern:
* Internal citation syntax for controlled library standards, assets, templates, and publications (governed by `A02 §5.7`, which this standard complements).
* Semantic version identifier syntax (`vMAJOR.MINOR.ERRATA`, governed by `A01 §5.5`).
* Editorial voice, plain-language sentence limits, or United States English (`en-US`) spelling mechanics (governed by `C01`).
* Controlled glossaries, acronym exemptions, or fixed status strings (governed by `C02`).

## 3. Normative References

The following documents are referenced in this standard. For undated references, the latest approved edition applies.
* `Library-Index.md` — Irvantri Standards Unified Operating Library Index (`v1.1.2` or later).
* `A01` — Document Control & Lifecycle.
* `A02` — Taxonomy, Coding & File Naming.
* `A03` — Entity & Brand Architecture.
* `A04` — Compliance, Reviews & Exceptions.
* `C01` — Voice, Tone & Plain Language.
* `C02` — Terminology & Controlled Vocabulary.
* `C03` — Technical & User Experience (UX) Writing.
* `D01` — Design Tokens & Architecture.
* `D03` — Interface Components & Patterns.
* `D05` — Generated Outputs & Exports.
* `E01` — Formal Document Layout.

## 4. Terms & Definitions

For terms shared across the library, refer to `C02`, `A01`, `A02`, `A03`, `A04`, and `C01`. For the purposes of this standard, the following definitions apply:
* **Bibliographic Citation:** A structured reference identifying an external publication, technical specification, statute, or dataset cited as authority or evidence.
* **Currency Code:** The uppercase three-letter alphabetic code defined by International Organization for Standardization (`ISO`) 4217 to identify a monetary unit.
* **Tabular Numerals:** Monospaced digit glyphs of uniform advance width designed so numeric columns align vertically in tables and financial schedules.
* **Timestamp:** A machine-readable string recording both calendar date and time of day with an explicit time zone offset or Coordinated Universal Time (`UTC`) designator.

## 5. Requirements

### 5.1 Dates, Timestamps & Intervals
**5.1.1** Calendar dates in metadata headers, registers, data tables, and formal documents SHALL follow `ISO` 8601 extended format `YYYY-MM-DD` (`A01 §5.2.7`, `C01 §5.6.3`).

**5.1.2** Date-time timestamps in system logs, audit trails, and generated exports (`D05`) SHALL follow `ISO` 8601 format `YYYY-MM-DDTHH:MM:SSZ` in `UTC`, or include an explicit `UTC` offset (`±HH:MM`). Human-facing User Interface (`UI`) headers (`C03`) and report summaries (`E01`) MAY display minute-level `UTC` timestamps (`YYYY-MM-DDTHH:MMZ`).

**5.1.3** Date intervals SHALL separate start and end dates using a forward slash (`2026-11-01/2026-11-30`) or `through`, and SHALL NOT use slash-delimited calendar dates (`11/12/2026`).

**5.1.4** `UI` prose and localized summaries (`C03`) MAY display spelled-out month names (`November 22, 2026`) where `ISO` 8601 `YYYY-MM-DD` format is not mandated.

### 5.2 Numbers, Percentages & Currency
**5.2.1** Numbers in technical documentation, registers, and interfaces SHALL use Arabic numerals (`0`–`9`), a period (`.`) as the decimal separator, and commas (`,`) to group thousands (`1,250.50`).

**5.2.2** Sentences SHALL NOT begin with an Arabic numeral; authors SHALL either spell out the opening number or rephrase the sentence.

**5.2.3** Decimal values between `-1` and `1` SHALL include a leading zero (`0.25`, `-0.5`), and percentages SHALL use the `%` symbol without a space (`99.5%`).

**5.2.4** Monetary amounts SHALL use uppercase three-letter `ISO` 4217 currency codes followed by a single space, such as Singapore Dollars (`SGD 1,500.00`) or United States Dollars (`USD 250.00`). Bare `$` symbols SHALL NOT be used alone. Financial tables, quotes, and invoices SHALL display two decimal places. Narrative prose in external publications (`PUB-`) and executive summaries MAY display whole-unit currency amounts (`USD 50,000`).

### 5.3 Units of Measurement & Technical Quantities
**5.3.1** Physical and digital measurements SHALL use International System of Units (`SI`) symbols or standard technical unit symbols (`px`, `pt`, `mm`, `KB`, `MB`, `ms`, `s`) in accordance with `C01`.

**5.3.2** Numeric values SHALL be separated from unit symbols by a single space (`16 px`, `24 mm`, `500 ms`), except for degree (`90°`) and percentage (`100%`) symbols. Literal code blocks, `CSS` declarations, and design token schemas (`D01`, `D03`) MAY omit the space (`16px`, `0.25rem`) where required by syntax.

**5.3.3** Unit symbols SHALL remain singular for both singular and plural quantities (`1 mm`, `10 mm`) and SHALL NOT include trailing periods.

**5.3.4** Data storage and transfer specifications SHALL distinguish decimal prefixes (`MB`, `GB`) from binary prefixes (`MiB`, `GiB`) where precision affects system configuration (`C03`).

### 5.4 Structured Tables, Lists & Sequential Numbering
**5.4.1** Every data table SHALL include a descriptive header row naming each column and SHALL NOT leave data cells blank (use `None` or an em dash `—` per `Library-Index.md`).

**5.4.2** Numeric columns in formal documents (`E01`) and Markdown tables SHOULD align right or use tabular numerals, and SHALL state shared units in the column header (`Duration (Days)`).

**5.4.3** Multi-level hierarchical numbering in normative standards and technical specifications SHALL use dot-delimited Arabic numerals (`1`, `1.1`, `1.1.1`) without trailing periods on multi-segment numbers.

**5.4.4** Tables and figures inside compiled publications (`PUB-`), generated outputs (`D05`), and formal documents (`E01`) SHALL carry sequential labels (`Table 1`, `Figure 1`) with descriptive captions.

### 5.5 External, Statutory & Bibliographic Citations
**5.5.1** Internal citations to controlled items in the Unified Operating Library SHALL follow `A02 §5.7` (`[CODE]`, `[CODE] §[Clause]`, or `[CODE] (vMAJOR.MINOR.ERRATA)`). External contracts, client deliverables, and third-party audits SHOULD prepend the Irvantri Standards (`IS`) namespace (`IS-B02` or `IS-A02 (v1.1.0)` per `A02 §5.7.3`).

**5.5.2** Citations to external technical standards and specifications SHALL state the issuing body, identifier, edition or year, and title (`ISO 8601-1:2019`, *Date and time — Representations for information interchange*).

**5.5.3** Citations to statutes, regulations, and official filings SHALL state the jurisdiction, short title, enactment year, and section (`Singapore Companies Act 1967, Section 142`).

**5.5.4** Citations to external publications or web resources (`A03 §5.6.2`) SHALL state the author or organization, publication year (`YYYY`), title, and stable `URL` or Digital Object Identifier (`DOI`).

## 6. Conformance & Verification

A document, register, table, export, or interface conforms to `C04` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `C04-C1` | Calendar dates use `ISO` 8601 `YYYY-MM-DD` (`5.1.1`), timestamps include `UTC` or explicit offset (`5.1.2`), and intervals use `/` or `through` with zero slash-delimited dates (`5.1.3`). | Format & schema audit |
| `C04-C2` | Numbers use `.` decimals and `,` thousands grouping (`5.2.1`), sentences do not open with numerals (`5.2.2`), and decimals between `-1` and `1` carry a leading zero with unspaced `%` (`5.2.3`). | Editorial & lint check |
| `C04-C3` | Monetary amounts use uppercase `ISO` 4217 currency codes with a single space, zero bare `$` symbols, and two decimal places in tables, quotes, and invoices (`5.2.4`). | Financial & copy audit |
| `C04-C4` | Measurements use valid `SI` or technical unit symbols (`5.3.1`), single-space separation outside permitted exceptions (`5.3.2`), singular symbols without periods (`5.3.3`), and explicit decimal vs. binary prefixes (`5.3.4`). | Technical spec audit |
| `C04-C5` | Tables include header rows and zero blank cells (`5.4.1`), numeric headers declare shared units (`5.4.2`), hierarchical numbering is dot-delimited (`5.4.3`), and tables/figures carry sequential captions (`5.4.4`). | Layout & table audit |
| `C04-C6` | Internal citations follow `A02 §5.7` (`5.5.1`), and external standard, statutory, and bibliographic citations state all required attribution elements (`5.5.2`–`5.5.4`). | Citation & reference audit |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with `A04`.

## 7. Linked Artifacts

None.

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v1.0.1` | `2026-11-25` | Errata | Removed obsolete pre-approval note in Section 3, split 30+ word sentence in `5.2.4`, aligned `C04-C2` leading-zero range wording with `5.2.3`, and confirmed `D03 (v2.0.0)` alignment per `REC-A04-005` (`F-10`). | Hary Irfantri |
| `v1.0.0` | `2026-11-22` | Major | Initial approved baseline of `C04` (Data, Dates & Citation Formatting), establishing `ISO` 8601 date and `UTC` timestamp formats, numeric and `ISO` 4217 currency conventions, `SI` and digital unit spacing rules, structured table and numbering rules, and internal/external citation formats. | Hary Irfantri |
| `v0.1.0` | `2026-11-22` | Pre-Release | Initial draft establishing `ISO` 8601 date and timestamp formats, numeric and `ISO` 4217 currency conventions, `SI` and digital unit spacing rules, structured table and numbering rules, and external citation formats. | Hary Irfantri |
