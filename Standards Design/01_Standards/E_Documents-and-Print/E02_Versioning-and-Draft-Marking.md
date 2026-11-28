# E02 — Versioning & Draft Marking

| Field | Value |
| :--- | :--- |
| **Code** | `E02` |
| **Version** | `v1.1.1` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-28` |
| **Next Review** | `2027-05-23` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `None` |

## 1. Purpose

This standard defines semantic version display rules, release status indicator styling, non-approved status banners, watermark thresholds, and active exception waiver disclosures for **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`). It ensures readers can immediately distinguish working drafts, documents under review, approved baselines, and deprecated records.

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* All formal documents, governance reports, proposals, specifications, and compiled publications (`PUB-`) tracked in `Library-Index.md`.
* All cover metadata panels, running headers, running footers, status badges, and revision history tables across formal documents (`E01`).
* All archived snapshots stored in `99_Archive/` and formal deliverables operating under active `A04` exception waivers.

### 2.2 Out of Scope
This standard does not govern:
* Semantic version increment triggers (`MAJOR`, `MINOR`, `ERRATA`) or lifecycle state transition authority (governed by `A01`).
* Cover page layout geometry, running header/footer dimensions, or pagination rules (governed by `E01`).
* Paper stock selection, press bleed/trim allowances, or commercial vendor proofing (governed by `E03`).
* Letters, memoranda, slide decks, or email signatures (governed by `E04`).

## 3. Normative References

The following documents are referenced in this standard. For undated references, the latest approved edition applies.
* `Library-Index.md` — Standards Design Library Index (`v2.0.0` or later).
* `A01` — Document Control & Lifecycle.
* `A02` — Taxonomy, Coding & File Naming.
* `A04` — Compliance, Reviews & Exceptions.
* `B02` — Color System.
* `B03` — Typography.
* `B04` — Grids, Spacing & Graphic Devices.
* `C02` — Terminology & Controlled Vocabulary.
* `C04` — Data, Dates & Citation Formatting.
* `E01` — Formal Document Layout.

## 4. Terms & Definitions

For terms shared across the library, refer to `Library-Index.md`, `C02`, `A01`, `B02`, `B03`, `B04`, `C04`, and `E01`. For the purposes of this standard, the following definitions apply:
* **Draft Watermark:** A low-opacity diagonal text overlay rendered behind body content to mark non-approved working documents during review.
* **Release Status Indicator:** A visual badge or pill displaying the controlled lifecycle status of a document in a header, cover, or metadata panel.
* **Status Banner:** A full-width callout strip displayed on non-approved formal documents to prevent premature operational reliance.

## 5. Requirements

### 5.1 Version Identifier Display & Revision Logs
**5.1.1** Formal documents and compiled publications (`PUB-`) SHALL display `vMAJOR.MINOR.ERRATA` (`A01 §5.5.1`) on the Cover Page metadata panel and Running Footer (`E01 §5.1.3`).

**5.1.2** Displayed version strings SHALL use an approved monospace font (`B03 §5.1.2`) and SHALL NOT use two-part version numbers or trailing prose labels (`A01 §5.5.1`).

**5.1.3** Formal documents and compiled publications (`PUB-`) SHALL include a reverse-chronological Revision History table recording `Version`, `Date`, `Type`, `Summary of Changes`, and `Approver` (`A01 §5.2.3`, `C04 §5.4.1`).

**5.1.4** Pre-release working drafts SHALL display `v0.Y.0` version strings (`A01 §5.5.2`), and initial formally approved releases SHALL display `v1.0.0`.

### 5.2 Release Status Indicators & Semantic Styling
**5.2.1** Release status indicators in running headers, cover badges, and metadata panels (`E01 §5.1.3`) SHALL display exact `C02 §5.4.1` controlled status strings without informal synonyms (`C02 §5.4.2`).

**5.2.2** Status indicators SHALL pair the `B02 §5.3.1` semantic Hexadecimal (`HEX`) color tokens in the table below with an explicit text label (`B02 §5.5.2`) and `4 px` corner radius (`B04 §5.2.1`):

| Controlled Status (`C02`) | Semantic Role (`B02`) | Foreground HEX | Surface HEX | Border HEX |
| :--- | :--- | :--- | :--- | :--- |
| `Planned` | Informative | `#074C96` | `#EFF6FF` | `#BFDBFE` |
| `Draft` | Warning | `#92400E` | `#FFFBEB` | `#FDE68A` |
| `In Review` | Informative | `#074C96` | `#EFF6FF` | `#BFDBFE` |
| `Approved` | Success | `#166534` | `#F0FDF4` | `#BBF7D0` |
| `Sync Required` | Warning | `#92400E` | `#FFFBEB` | `#FDE68A` |
| `Deprecated` | Danger | `#A42332` | `#FEF2F2` | `#FECACA` |

**5.2.3** Status indicators SHALL meet Web Content Accessibility Guidelines (`WCAG`) 2.2 Level AA contrast (`B02 §5.5.1`) and SHALL NOT use raw **Signal Red** (`#DE0029`) for badge text (`B02 §5.3.2`).

### 5.3 Status Banners, Watermarks & Active Waiver Disclosures
**5.3.1** Every non-Approved formal document (`Planned`, `Draft`, `In Review`, `Sync Required`, or `Deprecated`) SHALL display a status banner on the Cover Page (`E01 §5.1.1`) and Running Header (`E01 §5.2.1`).

**5.3.2** Status banners SHALL align to the `4 mm` print Base Unit (`B04 §5.1.2`), use an `8 px` corner radius (`B04 §5.2.1`), and display the verbatim notice below:

```text
[STATUS] — [Version] | Non-Binding Working Copy. Do not distribute as an Approved baseline.
```

> **Example:** A working draft displays: `Draft — v0.2.0 | Non-Binding Working Copy. Do not distribute as an Approved baseline.`

**5.3.3** Non-Approved formal documents distributed for review MAY include a diagonal watermark in the Display Typeface (`B03 §5.1.1`) using **Border Default** (`#CBD5E1`) (`B02 §5.2.1`) at `10%` to `15%` opacity (`C04 §5.2.3`).

**5.3.4** Watermarks SHALL NOT reduce body text contrast below the `4.5:1` `WCAG` 2.2 Level AA minimum (`B02 §5.5.1`) and SHALL be removed before `Approved` release (`A01 §5.4.1`).

**5.3.5** Deliverables released under an active `A04` waiver SHALL visibly disclose `Waiver ID` (`REC-A04-[001–999]`) and `Expiry Date` (`YYYY-MM-DD`) on the Cover Page or Metadata Panel (`A04 §5.4.8`).

### 5.4 Archived & Superseded Document Marking
**5.4.1** Outgoing snapshots stored in `99_Archive/` for `MAJOR`, `MINOR`, or `Deprecated` transitions SHALL append `_vMAJOR.MINOR.ERRATA` before the file extension (`A01 §5.7.2`, `A02 §5.6.1`) and SHALL remain unmodified (`A02 §5.6.2`).

**5.4.2** Superseded or `Deprecated` documents retained for reference SHALL display `Deprecated` status (`C02 §5.4.1`) and state the superseding document code (`A01 §5.2.2`, `§5.7.3`) in the Metadata Panel (`E01 §5.1.3`).

## 6. Conformance & Verification

A formal document, compiled publication, or archived file conforms to `E02` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `E02-C1` | Cover and footer display `vMAJOR.MINOR.ERRATA` in approved monospace without two-part numbers or prose suffixes (`5.1.1`, `5.1.2`), pre-release drafts use `v0.Y.0` (`5.1.4`), and a reverse-chronological Revision History table is present (`5.1.3`). | Version & history audit |
| `E02-C2` | Release status indicators use exact `C02` status strings (`5.2.1`), pair `B02` semantic palette tokens with text labels and `4 px` radius (`5.2.2`), and meet `WCAG` 2.2 Level AA contrast without `#DE0029` text (`5.2.3`). | Badge & contrast inspection |
| `E02-C3` | Non-Approved documents display the `4 mm` / `8 px` status banner with exact notice text (`5.3.1`, `5.3.2`), and any watermark preserves `4.5:1` text contrast and is removed before `Approved` release (`5.3.4`). | Visual & pre-release check |
| `E02-C4` | Deliverables operating under an active `A04` waiver visibly disclose `Waiver ID` (`REC-A04-[001–999]`) and `Expiry Date` (`YYYY-MM-DD`) on the Cover Page or Metadata Panel (`5.3.5`). | Waiver disclosure audit |
| `E02-C5` | Archived snapshots in `99_Archive/` carry unmodified `_vMAJOR.MINOR.ERRATA` filenames (`5.4.1`), and retained `Deprecated` documents display `Deprecated` status and their superseding code (`5.4.2`). | Archive & metadata check |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with `A04`.

## 7. Linked Artifacts

None.

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v1.1.1` | `2026-11-28` | Errata | Renamed library references to `Standards Design` and raised the `Library-Index.md` reference floor to `v2.0.0` per `A01 §5.5.5`, `§5.5.7`, and `REC-A04-016`. | Hary Irfantri |
| `v1.1.0` | `2026-11-26` | Minor | Decoupled optional diagonal review watermark (`5.3.3`) from the retired hardcoded `Montserrat` typeface name to reference the Display Typeface (`B03 §5.1.1`) in alignment with `B03 (v2.0.0)`, and updated `Library-Index.md` reference floor (`v1.2.1`). | Hary Irfantri |
| `v1.0.0` | `2026-11-23` | Major | Initial approved baseline of `E02` (Versioning & Draft Marking), locking `vMAJOR.MINOR.ERRATA` monospace display and Revision History rules, `B02` semantic status badge mappings, mandatory non-approved status banners, `10%`–`15%` watermark thresholds, `A04` waiver disclosures, and `Deprecated` archival markings. | Hary Irfantri |
| `v0.1.0` | `2026-11-23` | Pre-Release | Initial draft establishing `vMAJOR.MINOR.ERRATA` monospace display and Revision History rules, `B02` semantic status badge mappings, mandatory non-approved status banners, `10%`–`15%` watermark thresholds, `A04` waiver disclosures, and `Deprecated` archival markings. | Hary Irfantri |
