# E03 — Print & Production Specifications

| Field | Value |
| :--- | :--- |
| **Code** | `E03` |
| **Version** | `v1.1.0` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-27` |
| **Next Review** | `2027-05-23` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `None` |

## 1. Purpose

This standard defines paper stocks, margins, bleed and trim tolerances, Cyan-Magenta-Yellow-Key (`CMYK`) color profiles, prepress packaging, and vendor proofing for **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`). It ensures physical print deliverables reproduce brand colors, typography, and layouts accurately across commercial presses.

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* All commercially offset-printed and digitally printed formal documents, reports, stationery, and compiled publications (`PUB-`) produced for **Irvantri Standards** (`Irvantri Standards Pte. Ltd.`).
* All prepress production files, color profiles, font embedding packages, and vendor proofing sign-offs supporting Series B and Series E deliverables.

### 2.2 Out of Scope
This standard does not govern:
* Cover page layout geometry, metadata panel fields, running headers, or running footers (governed by `E01`).
* Draft watermarks, status banner text, or semantic version display formatting (governed by `E02`).
* Letterhead copy structure, slide decks, or digital email signatures (governed by `E04`).
* Digital screen color tokens, web contrast rules, or system-generated export schemas (governed by `B02` and `D05`).

## 3. Normative References

The following documents are referenced in this standard. For undated references, the latest approved edition applies.
* `Library-Index.md` — Irvantri Standards Unified Operating Library Index (`v1.1.17` or later).
* `A01` — Document Control & Lifecycle.
* `A02` — Taxonomy, Coding & File Naming.
* `A03` — Entity & Brand Architecture.
* `A04` — Compliance, Reviews & Exceptions.
* `B01` — Marks & Lockups.
* `B02` — Color System.
* `B03` — Typography.
* `B04` — Grids, Spacing & Graphic Devices.
* `C02` — Terminology & Controlled Vocabulary.
* `C04` — Data, Dates & Citation Formatting.
* `E01` — Formal Document Layout.
* `E02` — Versioning & Draft Marking.

## 4. Terms & Definitions

For terms shared across the library, refer to `Library-Index.md`, `C02`, `B01`, `B02`, `B03`, `B04`, `E01`, and `E02`. For the purposes of this standard, the following definitions apply:
* **Bleed:** The printed artwork extension beyond the final trim edge that prevents unprinted white borders after mechanical cutting.
* **Color Proof:** A calibrated physical contract proof or verified digital proof used to confirm color accuracy and layout alignment prior to press production.
* **Paper Stock:** The physical sheet substrate specified by basis weight in grams per square meter (`g/m²`), opacity, and surface finish.
* **Prepress Package:** The finalized production file bundle prepared for commercial printing, including embedded fonts, color profiles, bleed geometry, and trim marks.
* **Safe Margin:** The minimum interior distance from the trim edge within which all essential text, marks, and legal attribution remain protected from cutting tolerances.

## 5. Requirements

### 5.1 Page Formats, Margins & Bleed Geometry
**5.1.1** Standard formal print deliverables and compiled publications (`PUB-`) SHALL use A4 (`210 mm × 297 mm`) trim dimensions (`C04 §5.3.2`). Non-A4 physical formats SHALL require a registered template (`TPL-`) or contractual specification (`A01 §2.2`).

**5.1.2** Print layouts SHALL align structural margins and gutters to the `4 mm` print Base Unit (`B04 §5.1.2`), maintaining at least `16 mm` outer Safe Margins (`E01 §5.2.1`).

**5.1.3** Bound publications exceeding `16` pages SHALL provide at least a `20 mm` inner binding margin (`B04 §5.1.2`, `C04 §5.3.2`).

**5.1.4** Full-bleed ink or artwork extending to the trim edge SHALL include a `3 mm` Bleed on all sides with crop marks offset by `3 mm` (`C04 §5.3.2`).

**5.1.5** Safe Margins (`5.1.2`, `E01 §5.2.1`) SHALL be measured from the trim edge to the outermost ink of any text, mark, or attribution. This includes descenders, not only text baselines or frames.

### 5.2 Paper Stocks & Surface Finishes
**5.2.1** Commercial print deliverables SHALL use uncoated or matte-coated archival-grade paper stocks meeting the minimum basis weights in the table below (`C04 §5.3.1`, `§5.4.1`):

| Print Deliverable Type | Minimum Paper Weight (`g/m²`) | Surface Finish | Permitted Application |
| :--- | :--- | :--- | :--- |
| Formal Reports & Proposals (Interior) | `100` | Uncoated or matte | Bound specifications, governance reports, and `PUB-` interiors |
| Formal Covers & Section Dividers | `250` | Matte-coated or uncoated | `E01` formal covers, executive summaries, and section tabs |
| Single-Sheet Stationery & Inserts | `120` | Uncoated | Official correspondence sheets and standalone formal inserts |

**5.2.2** High-gloss aqueous or ultraviolet (`UV`) coatings SHALL NOT be applied over text-heavy pages where surface glare degrades reading contrast (`B02 §5.5.1`).

**5.2.3** Paper stocks SHOULD carry Forest Stewardship Council (`FSC`) or Programme for the Endorsement of Forest Certification (`PEFC`) certification where available.

### 5.3 Color Profiles, Ink Builds & Print Resolution
**5.3.1** Commercial offset and digital print production SHALL use the International Organization for Standardization (`ISO`) Coated v2 `CMYK` builds in `B02 §5.1.1` (`B02 §5.1.3`). Automated Red-Green-Blue (`RGB`) software conversions SHALL NOT be used.

> **Informative Note:** Fixed `ISO` Coated v2 `CMYK` builds for the neutral scale and semantic palette are defined in `B02 §5.6.1`.

**5.3.2** Single-ink monochrome print deliverables SHALL use `100%` black ink (K-only) matching **Pure Black** (`#000000`) (`B01 §5.4.1`, `B02 §5.2.1`, `C04 §5.2.3`).

**5.3.3** Print brand marks SHALL use vector masters (`SVG` or `PDF`) (`B01 §5.1.2`) and meet `B01 §5.3.2` and `B03 §5.2.5` print minimums (`12 mm` symbol; `6 pt` Endorsement Line).

**5.3.4** Embedded raster photography and continuous-tone imagery in print files SHALL maintain at least `300` pixels per inch (`ppi`) at `100%` final print scale (`C04 §5.2.3`, `§5.3.2`).

**5.3.5** Total ink coverage in `CMYK` print files SHALL NOT exceed `300%` under the `ISO` Coated v2 profile to prevent ink set-off and smudging (`C04 §5.2.3`).

### 5.4 Prepress Packaging, Font Embedding & Vendor Proofing
**5.4.1** Press-ready handoff files SHALL export as `PDF/X-4` with all licensed `B03` fonts embedded (`B03 §5.1.3`). Exports SHALL conform to `ISO 15930-7:2010`, *Graphic technology — Prepress digital data exchange using PDF* (`C04 §5.5.2`).

**5.4.2** Prepress package filenames SHALL follow `A02 §5.4` naming rules, verify `Approved` baseline status (`E02 §5.3.4`), and exclude non-approved draft banners or watermarks (`E02 §5.3.1`).

**5.4.3** Commercial print runs exceeding `50` copies or containing `E01` covers SHALL require Owner sign-off on a calibrated Color Proof before press production (`A01 §5.1.1`).

**5.4.4** Print deliverables SHALL keep `A03 §5.3.3` endorsement, `A03 §5.6.1` copyright, and active `A04 §5.4.8` waiver disclosures inside the Safe Margin without clipping (`E01 §5.2.2`, `E02 §5.3.5`).

## 6. Conformance & Verification

A print production file, prepress package, or printed deliverable conforms to `E03` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `E03-C1` | Deliverable uses A4 (`210 mm × 297 mm`) or authorized non-A4 trim (`5.1.1`), aligns to `4 mm` margins with `16 mm` outer / `20 mm` binding minimums measured to the outermost ink (`5.1.2`, `5.1.3`, `5.1.5`), and includes `3 mm` Bleed and offset crop marks (`5.1.4`). | Prepress geometry check |
| `E03-C2` | Commercial print jobs use `100 g/m²` interior, `120 g/m²` stationery, or `250 g/m²` cover uncoated/matte archival stocks (`5.2.1`) with zero high-gloss or `UV` coatings over text-heavy pages (`5.2.2`). | Vendor spec & sample audit |
| `E03-C3` | Color print uses `B02` `ISO` Coated v2 `CMYK` builds without automated `RGB` conversion (`5.3.1`), monochrome uses `100%` K-only (`5.3.2`), marks are vector meeting `B01`/`B03` print minimums (`5.3.3`), raster imagery is at least `300 ppi` (`5.3.4`), and total ink is at most `300%` (`5.3.5`). | Preflight & color audit |
| `E03-C4` | Handoff uses `PDF/X-4` (`ISO 15930-7:2010`) with embedded licensed `B03` fonts (`5.4.1`), conforms to `A02` naming with zero draft markings (`5.4.2`), holds Owner Color Proof sign-off for `> 50` copies or `E01` covers (`5.4.3`), and keeps attribution/waiver text inside Safe Margins (`5.4.4`). | Prepress & proof sign-off audit |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with `A04`.

## 7. Linked Artifacts

None.

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v1.1.0` | `2026-11-27` | Minor | Added `5.1.5` requiring Safe Margins to be measured to the outermost ink, including descenders, added an informative note pointing `5.3.1` to the `B02 §5.6.1` neutral and semantic builds, and extended `E03-C1`, per `REC-A04-009` (`U-03`, `U-01`). | Hary Irfantri |
| `v1.0.0` | `2026-11-23` | Major | Initial approved baseline of `E03` (Print & Production Specifications), locking A4 trim and `4 mm`/`16 mm`/`20 mm` margin geometry, `3 mm` Bleed rules, archival paper stock minimums (`100`–`250 g/m²`), `ISO` Coated v2 `CMYK` and `300 ppi`/`300%` ink thresholds, `PDF/X-4` prepress packaging, and Owner Color Proof gates. | Hary Irfantri |
| `v0.1.0` | `2026-11-23` | Pre-Release | Initial draft establishing A4 trim and `4 mm`/`16 mm`/`20 mm` margin geometry, `3 mm` Bleed rules, archival paper stock minimums (`100`–`250 g/m²`), `ISO` Coated v2 `CMYK` and `300 ppi`/`300%` ink thresholds, `PDF/X-4` prepress packaging, and Owner Color Proof gates. | Hary Irfantri |
