# E01 — Formal Document Layout

| Field | Value |
| :--- | :--- |
| **Code** | `E01` |
| **Version** | `v1.2.0` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-26` |
| **Next Review** | `2027-05-22` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `TPL-E01-01`, `TPL-E01-02`, `TPL-E01-03`, `TPL-E01-04` |

## 1. Purpose

This standard defines the cover geometry, metadata panel structure, running header and footer layout, pagination rules, corporate attribution requirements, and digital distribution `PDF` profile for formal documents across **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`). It ensures formal documents present a consistent, legible, and authoritative visual structure across print and digital distribution.

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* Formal documents, governance reports, proposals, specifications, and compiled publications (`PUB-`) produced by **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`).
* Formal document cover pages, metadata panels, running headers, running footers, pagination formatting, and digital `PDF` distribution profiles.
* Executable layout templates (`TPL-E01`) registered in `Library-Index.md` and Section 7 of this standard.

### 2.2 Out of Scope
This standard does not govern:
* Normative standard anatomy and lifecycle rules for Markdown source standards (governed by `A01`).
* Draft watermarks, revision banner styling, or release status indicator rules (governed by `E02`).
* Paper stock selection, press bleed/trim allowances, or commercial vendor proofing (governed by `E03`).
* Letters, memoranda, slide decks, or email signatures (governed by `E04`).

## 3. Normative References

The following documents are referenced in this standard. For undated references, the latest approved edition applies.
* `Library-Index.md` — Irvantri Standards Unified Operating Library Index (`v1.2.0` or later).
* `A01` — Document Control & Lifecycle.
* `A02` — Taxonomy, Coding & File Naming.
* `A03` — Entity & Brand Architecture.
* `A04` — Compliance, Reviews & Exceptions.
* `B01` — Marks & Lockups.
* `B02` — Color System.
* `B03` — Typography.
* `B04` — Grids, Spacing & Graphic Devices.
* `C01` — Voice, Tone & Plain Language.
* `C02` — Terminology & Controlled Vocabulary.
* `C04` — Data, Dates & Citation Formatting.
* `E03` — Print & Production Specifications.

## 4. Terms & Definitions

For terms shared across the library, refer to `C02`, `A01`, `B01`, `B03`, and `B04`. For the purposes of this standard, the following definitions apply:
* **Cover Page:** The front title sheet of a formal document presenting brand identification, document title, metadata summary, and signature visual geometry.
* **Digital Distribution PDF:** An electronic `PDF` deliverable formatted at exact A4 trim dimensions in Standard Red-Green-Blue (`sRGB`) color without print bleed or crop marks for screen viewing and electronic distribution.
* **Metadata Panel:** A structured summary block displaying controlled document attributes—such as identifier, version, status, owner, approver, and dates—on a formal document.
* **Running Footer:** The recurring bottom margin region displaying document title, version, attribution, and page numbering across pages.
* **Running Header:** The recurring top margin region displaying brand lockup and document or status context across pages.

## 5. Requirements

### 5.1 Cover Geometry & Metadata Panels
**5.1.1** Formal document covers SHALL place the Parent-Endorsed Lockup (`B01 §5.2.1`) in the upper region with at least `0.25×` Primary Symbol width Clear Space (`B01 §5.3.1`). Covers MAY include the `24%` **Signal Red** (`#DE0029`) and `76%` **Deep Navy** (`#092B55`) split accent bar in horizontal or `4 mm` vertical left-spine orientation (`B04 §5.3.1`).

**5.1.2** Cover titles and section headings SHALL use `Montserrat` (`B03 §5.1.1`) in United States English (`en-US`) (`C01 §5.6.1`), and SHALL NOT display internal project codenames (`A03 §5.4.2`, `C02 §5.3.3`).

**5.1.3** Cover and document metadata panels SHALL record `Version` in `vMAJOR.MINOR.ERRATA` format (`A01 §5.5.1`) and `Status` using exact `C02 §5.4.1` controlled status strings without informal synonyms (`C02 §5.4.2`). Metadata dates SHALL use International Organization for Standardization (`ISO`) 8601 format (`YYYY-MM-DD`) (`A01 §5.2.7`, `C04 §5.1.1`).

### 5.2 Running Headers, Footers & Pagination
**5.2.1** Running headers and footers SHALL align to the `4 mm` print Base Unit grid (`B04 §5.1.2`, `C04 §5.3.2`) and maintain `B02 §5.5.1` contrast and `B03 §5.2.2` legibility rules.

**5.2.2** Formal documents SHALL display the verbatim Endorsement Line `A member of Irvantri Group` (`A03 §5.2.1`, `§5.3.3`). Documents SHALL also display `© [YYYY] Irvantri Standards Pte. Ltd. All rights reserved.` (`A03 §5.6.1`) on the cover, colophon, or running header or footer.

**5.2.3** Running footers or page margins SHALL display sequential page numbering (`Page X of Y` or `X / Y`) (`C04 §5.2.1`, `§5.4.3`). Required header and footer metadata fields SHALL NOT be left blank (`C04 §5.4.1`).

### 5.3 Executable Layout Templates (`TPL-E01`)
**5.3.1** Formal document layout templates SHALL be registered as `TPL-E01` Executable Templates in `Library-Index.md` and Section 7, pinned to `E01 (vMAJOR.MINOR)` (`A01 §5.7.4`, `A02 §5.7.2`).

**5.3.2** Page-based `TPL-E01` templates deployed across print and electronic channels SHALL maintain paired Print (`E03`) and Digital (`5.4`) editions derived from identical layout geometry.

### 5.4 Digital Distribution PDF Profile
**5.4.1** Formal documents and compiled publications (`PUB-`) distributed digitally as `PDF` files SHALL use exact A4 (`210 mm × 297 mm`) trim dimensions (`C04 §5.3.2`). Digital `PDF` files SHALL omit print bleed extensions, slug areas, and crop marks.

**5.4.2** Digital distribution `PDF` files SHALL use `sRGB` color matching exact `B02 §5.1.1`–`§5.3.1` Hexadecimal (`HEX`) and Red-Green-Blue (`RGB`) values (`B02 §5.5.1`).

**5.4.3** Digital distribution `PDF` files SHALL embed all licensed `B03` fonts (`B03 §5.1.3`), preserve selectable live text, and retain vector brand marks sourced from `AST-B01` masters (`B01 §5.1.2`).

## 6. Conformance & Verification

A formal document or layout template conforms to `E01` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `E01-C1` | Cover applies `B01` lockup and Clear Space rules, optional horizontal or `4 mm` vertical spine `24%` / `76%` accent bar (`5.1.1`), `Montserrat` and `en-US` text without codenames (`5.1.2`), and `vMAJOR.MINOR.ERRATA`, `C02` status, and `YYYY-MM-DD` metadata (`5.1.3`). | Cover & metadata audit |
| `E01-C2` | Running headers and footers align to `4 mm` increments and meet contrast and size rules (`5.2.1`), preserve `A member of Irvantri Group` and `© [YYYY] Irvantri Standards Pte. Ltd. All rights reserved.` (`5.2.2`), and include page numbers without blank fields (`5.2.3`). | Header, footer & pagination check |
| `E01-C3` | Formal layout templates are registered as `TPL-E01` in `Library-Index.md` and Section 7 pinned to `E01 (vMAJOR.MINOR)` (`5.3.1`), with paired Print and Digital editions for dual-channel templates (`5.3.2`). | Template & register audit |
| `E01-C4` | Digital distribution `PDF` files use exact A4 trim without bleed or crop marks (`5.4.1`), apply exact `B02` `sRGB` palette values (`5.4.2`), and embed licensed `B03` fonts, selectable text, and vector `AST-B01` marks (`5.4.3`). | Digital `PDF` preflight audit |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with `A04`.

## 7. Linked Artifacts

| Code | Artifact | File | Pinned Version | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `TPL-E01-01` | Header & Footer Layout Template (Print) | `03_Templates/TPL-E01-01_Header-and-Footer-Print.pdf` | `E01 (v1.2)` | `Planned` | Press-ready A4 running header and footer template (`E03` `PDF/X-4`, `vMAJOR.MINOR.ERRATA` version display and `C02` status badge) |
| `TPL-E01-02` | Formal Document Cover Template (Print) | `03_Templates/TPL-E01-02_Formal-Cover-Print.pdf` | `E01 (v1.2)` | `Approved` | Press-ready A4 cover template (`E03` `PDF/X-4`, `ISO` Coated v2, `3 mm` bleed/crop marks, `AST-B01-03` lockup, `4 mm` `24%` / `76%` vertical spine bar; Title Slug refined `2026-11-26` per `A02 §5.3.3`) |
| `TPL-E01-03` | Formal Document Cover Template (Digital) | `03_Templates/TPL-E01-03_Formal-Cover-Digital.pdf` | `E01 (v1.2)` | `Approved` | Digital A4 cover template (`5.4` `sRGB`, zero bleed/crop marks, embedded `B03` fonts, `AST-B01-03` lockup, `4 mm` `24%` / `76%` vertical spine bar; Approved `2026-11-26`) |
| `TPL-E01-04` | Header & Footer Layout Template (Digital) | `03_Templates/TPL-E01-04_Header-and-Footer-Digital.pdf` | `E01 (v1.2)` | `Planned` | Digital A4 running header and footer template (`5.4` `sRGB`, zero bleed/crop marks, `vMAJOR.MINOR.ERRATA` version display and `C02` status badge) |

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v1.2.0` | `2026-11-26` | Minor | Added Digital Distribution `PDF` Profile (`5.4.1`–`5.4.3`, `E01-C4`), mandated paired Print and Digital editions for dual-channel `TPL-E01` templates (`5.3.2`, `E01-C3`), added `E03` to Section 3, refined `TPL-E01-01`/`02` Title Slugs (`-Print`) per `A02 §5.3.3`, registered `TPL-E01-03` (`Approved`) and `TPL-E01-04` (`Planned`), and re-pinned `TPL-E01-01`–`04` to `E01 (v1.2)`. | Hary Irfantri |
| `v1.1.1` | `2026-11-26` | Errata | Promoted `TPL-E01-02` (`03_Templates/TPL-E01-02_Formal-Cover.pdf`) from `Planned` to `Approved` in Section 7 and updated the `Library-Index.md` reference floor (`v1.1.28`) in Section 3 per `A01 §5.5.7`. | Hary Irfantri |
| `v1.1.0` | `2026-11-25` | Minor | Expanded `5.1.1` and `E01-C1` to permit either horizontal or `4 mm` vertical left-spine orientation for the `24%` **Signal Red** / `76%` **Deep Navy** cover accent bar per `B04 (v1.2.0) §5.3.1`, updated `Library-Index.md` reference floor in Section 3, and re-pinned `TPL-E01-01` and `TPL-E01-02` to `E01 (v1.1)` in Section 7. | Hary Irfantri |
| `v1.0.2` | `2026-11-25` | Errata | Populated `Governs` header (`TPL-E01-01`, `TPL-E01-02`) to match active Section 7 artifacts per `A01 (v1.2.0) §5.2.8` and `REC-A04-005` (`F-07`). | Hary Irfantri |
| `v1.0.1` | `2026-11-23` | Errata | Trimmed unused Section 3 references (`D02`, `D05`, `E02`, `E03`, `E04`), removed misdirected `C04 §5.4.1` citation in `5.2.2`, and split long Section 5 sentences (`5.1.1`, `5.1.3`, `5.2.2`, `5.2.3`) per `REC-A04-004` (`F-04`). | Hary Irfantri |
| `v1.0.0` | `2026-11-22` | Major | Initial approved baseline of `E01` (Formal Document Layout), locking cover lockup and accent bar geometry, `vMAJOR.MINOR.ERRATA` and `C02` status metadata rules, `4 mm` running header/footer and pagination rules, corporate attribution placement, and `TPL-E01` template registration. | Hary Irfantri |
| `v0.1.0` | `2026-11-22` | Pre-Release | Initial draft establishing cover lockup and accent bar geometry, `vMAJOR.MINOR.ERRATA` and `C02` status metadata rules, `4 mm` running header/footer and pagination rules, corporate attribution placement, and `TPL-E01` template registration. | Hary Irfantri |
