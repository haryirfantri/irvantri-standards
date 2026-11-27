# A02 — Taxonomy, Coding & File Naming

| Field | Value |
| :--- | :--- |
| **Code** | `A02` |
| **Version** | `v1.3.0` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-26` |
| **Next Review** | `2027-05-20` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Supersedes** | `None` |
| **Governs** | `None` |

## 1. Purpose

This standard defines the classification taxonomy, identifier syntax, casing rules, file and folder naming conventions, repository hierarchy, third-party dependency boundaries, and citation formats for the **Irvantri Standards Unified Operating Library**. It ensures every controlled item is deterministically sortable, machine-parseable, permanently traceable, and unambiguous across internal and external references.

## 2. Scope & Applicability

### 2.1 In Scope
This standard applies to:
* All normative standards (`A01`–`H99`) registered in `Library-Index.md`.
* All Master Assets (`AST-`), Executable Templates (`TPL-`), Compiled Publications (`PUB-`), and Governance Records (`REC-`), including Cloud-Native Office Files stored in the repository.
* All directory paths within the library repository, including `06_Dependencies/` (and its uncoded `Dependencies-Manifest.md`) and archived snapshots in `99_Archive/`.
* All internal and external cross-references citing library items.

### 2.2 Out of Scope
This standard does not govern:
* Internal code identifiers, database schemas, or software package names defined by product specifications.
* Client-mandated file naming conventions imposed by external contracts.
* Unmodified vendor package subfolders and filenames of third-party binary dependencies—such as licensed font suites and International Color Consortium (`ICC`) profiles—stored inside `06_Dependencies/`.
* Legacy or third-party historical files retained unmodified inside `99_Archive/` for provenance.

## 3. Normative References

The following documents are referenced in this standard. For undated references, the latest approved edition applies.
* `Library-Index.md` — Irvantri Standards Unified Operating Library Index (`v1.2.8` or later).
* `A01` — Document Control & Lifecycle.
* `A03` — Entity & Brand Architecture.
* `A04` — Compliance, Reviews & Exceptions.
* `C02` — Terminology & Controlled Vocabulary.
* `C04` — Data, Dates & Citation Formatting.

## 4. Terms & Definitions

For terms shared across the library, refer to `C02` and `A01`. For the purposes of this standard, the following definitions apply:
* **Cloud-Native Office File:** An editable document, spreadsheet, or presentation hosted natively in a cloud productivity suite—such as Google Docs, Google Sheets, or Google Slides—whose format is defined by repository metadata rather than a filename extension.
* **Code:** The permanent, uppercase alphanumeric identifier assigned to a controlled item (for example, `A02`, `AST-B01-01`, `PUB-01`).
* **Field Separator:** A character reserved exclusively to divide structural components of a filename or folder name (`Code`, `Title`, and archived `Version`).
* **Minor Word:** An English article, coordinating conjunction, or short preposition of three or fewer letters kept in lowercase under English Title Case rules unless positioned first or last in a title.
* **Series:** A top-level domain grouping identified by a single sequential uppercase letter (`A` through `H`).
* **Third-Party Dependency:** An externally authored and licensed binary resource or package—such as a typeface suite or `ICC` color profile—retained internally inside `06_Dependencies/` for reproducible execution without transferring ownership to Irvantri Standards.
* **Title Slug:** The hyphen-delimited descriptive portion of a file or folder name following the field separator.

## 5. Requirements

### 5.1 Series & Domain Architecture
**5.1.1** The Unified Operating Library SHALL organize normative standards into sequential single-letter series from `A` through `H`:

| Series | Domain | Phase |
| :--- | :--- | :--- |
| `A` | Governance & Traceability | Active |
| `B` | Visual Foundations | Active |
| `C` | Information & Verbal Standards | Active |
| `D` | Digital Systems & Interfaces | Active |
| `E` | Formal Documents & Print | Active |
| `F` | Systems & Engineering | Reserved |
| `G` | Processes & Delivery | Reserved |
| `H` | Quality, Security & Information Integrity | Reserved |

**5.1.2** Series letters `I` through `Z` SHALL remain unallocated until formally assigned by Approver revision of this standard and `Library-Index.md`.

**5.1.3** Reserved series (`F`, `G`, `H`) SHALL NOT receive subseries standard codes until formally activated in accordance with `A01 §5.4.4`.

### 5.2 Identifier & Code Anatomy
**5.2.1** Every identifier code and artifact prefix SHALL consist exclusively of uppercase American Standard Code for Information Interchange (`ASCII`) letters (`A`–`Z`), `ASCII` digits (`0`–`9`), and hyphens (`-`) joining code segments.

**5.2.2** Normative Standard codes SHALL follow the pattern `[Series][01–99]` using a zero-padded two-digit subseries number (for example, `A01`, `B05`, `E04`). The subseries number `00` is reserved and SHALL NOT be assigned to any standard.

**5.2.3** Non-standard controlled artifacts SHALL use the following uppercase prefixes and deterministic code patterns:

| Artifact Type | Code Pattern | Example Code |
| :--- | :--- | :--- |
| Master Asset | `AST-[StandardCode]-[01–99]` | `AST-B01-01` |
| Executable Template | `TPL-[StandardCode]-[01–99]` | `TPL-E01-01` |
| Compiled Publication | `PUB-[01–99]` | `PUB-01` |
| Governance Record | `REC-[StandardCode]-[001–999]` | `REC-A04-001` |

> **Informative Note:** Including the governing standard code inside `AST-`, `TPL-`, and `REC-` identifiers establishes direct traceability from the filename alone. Compiled publications (`PUB-`) synthesize multiple standards across series and therefore carry a library-wide sequence number.

**5.2.4** The master register (`Library-Index.md`) and the third-party dependency manifest (`06_Dependencies/Dependencies-Manifest.md`) SHALL remain uncoded.

**5.2.5** Internal references within the repository SHALL use bare codes (`B02`). External references in client contracts, deliverables, or third-party audits SHOULD prepend the Irvantri Standards (`IS-`) organization namespace (`IS-B02`) without modifying the canonical internal code or filename.

### 5.3 Code Permanence & Retirement
**5.3.1** Once a code reaches `Approved` status, it SHALL remain permanently bound to its original subject.

**5.3.2** Upon deprecation of any standard or artifact, its code SHALL be permanently retired and SHALL NOT be reassigned or reused for a new item. New standards or artifacts SHALL receive the next unused sequential number in their series or prefix group.

**5.3.3** During an approved revision, a controlled file's Title Slug MAY be refined without altering its permanent code, provided `Library-Index.md` is updated on the same calendar date (`A01 §5.8.1`).

### 5.4 File & Folder Naming Conventions
**5.4.1** Active controlled filenames SHALL follow the exact pattern `CODE_Title-Words.ext` (for example, `A02_Taxonomy-and-Naming.md`, `AST-B01-01_Primary-Symbol.svg`, `PUB-01_Brand-Handbook.pdf`), except as permitted for Cloud-Native Office Files in Clause `5.4.6`.

**5.4.2** Delimiters in file and folder names SHALL observe strict role separation:
* The underscore (`_`) SHALL serve exclusively as the major field separator dividing `CODE`, `Title-Words`, and (in `99_Archive/` only) `vX.Y.Z`. Underscores SHALL NOT appear inside codes or inside title slugs.
* The hyphen (`-`) SHALL serve exclusively to join segments within compound codes (`AST-B01-01`) and separate words within title slugs (`Document-Control`).

**5.4.3** Characters in controlled folder and file names SHALL be restricted to `ASCII` letters (`A`–`Z`, `a`–`z`), digits (`0`–`9`), hyphens (`-`), underscores (`_`), and periods (`.`). Periods SHALL appear strictly before file extensions and inside archived version strings. Spaces and special characters (`+`, `%`, `~`, `@`, `#`, `&`, `$`, `!`, `;`, `(`, `)`) SHALL NOT appear in controlled paths.

**5.4.4** Casing across all controlled folder and file names SHALL follow two rules:
* **Codes & Prefixes:** Every series letter, standard code, and artifact prefix SHALL be in UPPERCASE (`A02`, `AST-B01-01`, `A_Governance`).
* **Title Slugs:** Every descriptive title in both folder names and file names SHALL follow English Title Case:
  1. Capitalize the first word and the last word of the title slug unconditionally.
  2. Capitalize all principal words: nouns, pronouns, verbs, adjectives, adverbs, and subordinating conjunctions (for example, `After`, `Because`, `Before`, `Since`, `Until`, `When`, `While`).
  3. Lowercase minor words unless appearing as the first or last word:
     * **Articles:** `a`, `an`, `the`
     * **Coordinating conjunctions:** `and`, `but`, `for`, `nor`, `or`, `so`, `yet`
     * **Short prepositions (three letters or fewer):** `as`, `at`, `by`, `for`, `in`, `of`, `off`, `on`, `out`, `per`, `to`, `up`, `via`
  4. Capitalize prepositions of four or more letters (for example, `With`, `From`, `Into`, `Over`, `Under`).
  5. Preserve established uppercase acronyms and initialisms in UPPERCASE. Examples include User Interface (`UI`), User Experience (`UX`), Application Programming Interface (`API`), International Organization for Standardization (`ISO`), Web Content Accessibility Guidelines (`WCAG`), and Cyan-Magenta-Yellow-Key (`CMYK`).

> **Example:** Compliant names include `C03_Technical-and-UX-Writing.md`, `C_Information-and-Verbal/`, `E01_Formal-Document-Layout.md`, and `01_Standards/`. Non-compliant names include `C03_Technical-And-Ux-Writing.md` and `01_standards/c_information-and-verbal/`.

**5.4.5** Active controlled files in `01_Standards/`, `02_Assets/`, `03_Templates/`, `04_Publications/`, and `05_Records/` SHALL NOT include version numbers in their filenames (`A01 §5.7.1`).

**5.4.6** Active Cloud-Native Office Files in `03_Templates/` MAY omit file extensions and follow the exact pattern `CODE_Title-Words` (for example, `TPL-E01-05_Formal-Document`). Their native format (such as Google Docs, Google Sheets, or Google Slides) SHALL be declared explicitly in `Library-Index.md` and Section 7 of the governing standard.

### 5.5 Repository Directory Structure
**5.5.1** The library repository SHALL maintain the following directory layout using numbered prefixes and English Title Case folder names:

```text
Library-Index.md
01_Standards/
├── A_Governance/
├── B_Visual-Foundations/
├── C_Information-and-Verbal/
├── D_Digital-Systems/
├── E_Documents-and-Print/
├── F_Systems-and-Engineering/ (created upon series activation)
├── G_Processes-and-Delivery/ (created upon series activation)
└── H_Quality-Security-and-Integrity/ (created upon series activation)
02_Assets/
03_Templates/
04_Publications/
05_Records/
06_Dependencies/
├── Color-Profiles/
├── Fonts/
└── Dependencies-Manifest.md
99_Archive/
```

**5.5.2** Every controlled file SHALL reside in the directory corresponding to its artifact layer and, for normative standards, its assigned series folder.

**5.5.3** Folders for reserved series (`F`, `G`, `H`) SHALL NOT be created in the repository until the corresponding series is formally activated.

**5.5.4** Third-party licensed packages and binaries required by controlled templates (`TPL-`) or deliverables SHALL reside unmodified inside `06_Dependencies/` rather than `02_Assets/`. Every package or standalone binary in `06_Dependencies/` SHALL be logged in `Dependencies-Manifest.md` with its path, upstream version, license, rights holder, and governing standard (`A03 §5.6.2`). Unmodified vendor subfolders and filenames inside `06_Dependencies/` are exempt from Clauses `5.4.1`–`5.4.5` to preserve upstream provenance.

### 5.6 Archive Naming & Immutability
**5.6.1** Outgoing approved snapshots copied to `99_Archive/` per `A01 §5.7.2` SHALL append `_vMAJOR.MINOR.ERRATA` immediately before the file extension. For example, an archived snapshot uses `99_Archive/A01_Document-Control_v1.0.0.md`.

**5.6.2** Legacy or pre-library files transferred into `99_Archive/` for historical provenance SHALL retain their original filenames unmodified and SHALL NOT be renamed to match active conventions.

**5.6.3** Archived Cloud-Native Office Files moved to `99_Archive/` SHALL append `_vMAJOR.MINOR.ERRATA` to the title (for example, `99_Archive/TPL-E01-05_Formal-Document_v1.0.0`) without adding a synthetic extension. Archived native files SHALL remain unmodified after placement (`5.6.2`).

### 5.7 Cross-Reference Citation Syntax
**5.7.1** Undated citations pointing to the latest approved edition SHALL use the format `[CODE]` or `[CODE] §[Clause]` (for example, `A01` or `A01 §5.7.2`).

**5.7.2** Version-pinned citations SHALL append the version in parentheses: `[CODE] (vMAJOR.MINOR.ERRATA)` or `[CODE] (vMAJOR.MINOR.ERRATA) §[Clause]` for audits, waivers, and contracts (for example, `A01 (v1.1.0) §5.7.2`). Errata-tolerant pinning for `AST-` and `TPL-` registers (`A01 §5.7.4`) SHALL use `[CODE] (vMAJOR.MINOR)` (for example, `B01 (v1.0)`).

**5.7.3** External version-pinned citations SHOULD combine the `IS-` namespace with the pinned format (for example, `IS-A02 (v1.1.0)`).

**5.7.4** Clause `5.7` governs citations to controlled items within the Irvantri Standards Unified Operating Library. External bibliographic, statutory, and data citations SHALL follow `C04`.

## 6. Conformance & Verification

A controlled file, folder, or citation conforms to `A02` if and only if all of the following objective checks pass:

| Check ID | Verification Criterion | Method |
| :--- | :--- | :--- |
| `A02-C1` | Code uses strictly uppercase `ASCII` letters/digits and matches the assigned pattern in `5.2.2` or `5.2.3` (no `00` standard code). | Regex / register audit |
| `A02-C2` | No newly assigned code duplicates any active or `Deprecated` code recorded in `Library-Index.md` (`5.3.2`). | Register history check |
| `A02-C3` | Filename follows `CODE_Title-Words.ext` (active), `CODE_Title-Words` (active Cloud-Native Office Files with format declared per `5.4.6`), or `CODE_Title-Words_vX.Y.Z.ext` (archived) with zero spaces or prohibited characters (`5.4.1`–`5.4.3`, `5.4.6`). | Path lint / regex audit |
| `A02-C4` | Every folder and file title slug conforms to English Title Case rules and preserves uppercase acronyms (`5.4.4`). | Path inspection |
| `A02-C5` | Active files carry no version suffix (`5.4.5`) and reside in the exact folder defined in `5.5.1`–`5.5.2`. | Repository tree check |
| `A02-C6` | Archived snapshots in `99_Archive/` follow `_vX.Y.Z` naming (`5.6.1`, `5.6.3`) and remain unmodified after archival (`5.6.2`). | Archive inspection |
| `A02-C7` | Cross-references match `[CODE] §[Clause]`, `[CODE] (vX.Y.Z) §[Clause]`, or `[CODE] (vX.Y)` syntax (`5.7.1`–`5.7.2`), and external bibliographic citations follow `C04` (`5.7.4`). | Document review |
| `A02-C8` | Series `A`–`H` boundaries are preserved, `I`–`Z` remain unallocated, no reserved `F`/`G`/`H` folders exist prior to activation, `Library-Index.md` and `Dependencies-Manifest.md` remain uncoded, and internal references use bare codes (`5.1`, `5.2.4`–`5.2.5`, `5.5.3`). | Repository & register audit |
| `A02-C9` | Approved codes remain bound to their original subjects, and Title Slug edits sync in `Library-Index.md` on the same calendar date (`5.3.1`, `5.3.3`). | Register history check |
| `A02-C10` | Third-party licensed packages and binaries reside unmodified in `06_Dependencies/` rather than `02_Assets/`, and `Dependencies-Manifest.md` logs path, upstream version, license, rights holder, and governing standard (`5.5.4`). | Dependency & manifest audit |

Exceptions to any requirement in this standard require a formal, time-boxed waiver approved and logged in accordance with `A04`.

## 7. Linked Artifacts

None.

## 8. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v1.3.0` | `2026-11-26` | Minor | Defined Cloud-Native Office File in Section 4, updated Section 2.1 scope, added `5.4.6` and `5.6.3` permitting extensionless active and `_vX.Y.Z` archived Google Workspace templates with explicit format declarations in `Library-Index.md` and Section 7, aligned `5.4.1`, `A02-C3`, and `A02-C6`, and updated the `Library-Index.md` reference floor (`v1.2.8`). | Hary Irfantri |
| `v1.2.0` | `2026-11-26` | Minor | Added `06_Dependencies/` (`Color-Profiles/`, `Fonts/`, and uncoded `Dependencies-Manifest.md`) to `5.5.1` and `5.2.4`, added third-party package and binary provenance rules (`5.5.4`) with `A03` reference and `A02-C10`, defined Third-Party Dependency in Section 4, and exempted unmodified vendor subfolders and filenames in `06_Dependencies/` from `5.4.1`–`5.4.5`. | Hary Irfantri |
| `v1.1.1` | `2026-11-25` | Errata | Removed obsolete pre-approval note in Section 3 and tightened or split 30+ word sentences in `5.3.3`, `5.4.3`, `5.4.4`, and `5.6.1` per `REC-A04-005` (`F-10`). | Hary Irfantri |
| `v1.1.0` | `2026-11-22` | Minor | Harmonized parenthetical `MAJOR.MINOR` asset pinning (`5.7.2`), clarified `A02` vs. `C04` citation boundary (`5.7.4`), added `05_Records/` to active no-version rule (`5.4.5`), expanded `ASCII`, `IS-`, and example acronyms on first occurrence, and added `A02-C8` and `A02-C9` per `REC-A04-001`. | Hary Irfantri |
| `v1.0.0` | `2026-11-20` | Major | Initial approved baseline of `A02` (Taxonomy, Coding & File Naming), confirming Series `A`–`H`, zero-padded codes, artifact prefixes (`AST-`, `TPL-`, `PUB-`, `REC-`), English Title Case naming, repository structure, and citation syntax. | Hary Irfantri |
| `v0.1.0` | `2026-11-20` | Pre-Release | Initial draft establishing Series `A`–`H` taxonomy, zero-padded codes, artifact prefixes, `CODE_Title-Words.ext` syntax, English Title Case rules, Title Case repository directories, and citation formats. | Hary Irfantri |
