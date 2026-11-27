# Irvantri Standards

**Unified Operating Library**

The authoritative repository for the governance, visual, verbal, digital, and documentation standards used by [Irvantri Standards Pte. Ltd.](https://irvantri.com).

[Library index](#library-index) · [Repository structure](#repository-structure) · [Working with the library](#working-with-the-library) · [Authority and precedence](#authority-and-precedence)

---

> **Status:** Approved · **Register:** `v1.2.14` · **Last updated:** 2026-11-27

## Purpose

The Unified Operating Library turns institutional requirements into consistent, verifiable outputs. It provides normative standards, controlled master assets, executable templates, compiled publications, governance records, and tracked third-party dependencies.

The repository currently contains:

| Resource | Count | Purpose |
| --- | ---: | --- |
| Normative standards | 22 | Binding rules across active Series A–E |
| Master assets | 5 | Canonical marks and design-system exports |
| Executable templates | 6 | Print and digital production masters |
| Compiled publications | 3 | Human-facing reference and overview documents |
| Governance records | 7 | Reviews, audits, and conformance evidence |

## Library index

The [Library Index](Unified%20Operating%20Library/Library-Index.md) is the authoritative register for every controlled item in the repository.

Start with the index when you need to:

- Find the active version and status of a standard or artifact.
- Identify the governing standard for a master asset or template.
- Trace dependencies and compiled publications.
- Review active, reserved, or deprecated library items.

For a concise institutional overview, read [PUB-02 — Company Overview](Unified%20Operating%20Library/04_Publications/PUB-02_Company-Overview.md).

## Series

| Series | Domain | Standards |
| --- | --- | --- |
| **A** | Governance and traceability | [Document control](Unified%20Operating%20Library/01_Standards/A_Governance/A01_Document-Control.md), taxonomy, entity architecture, compliance |
| **B** | Visual foundations | Marks, color, typography, grids, iconography |
| **C** | Information and verbal | Voice, terminology, UX writing, dates and citations |
| **D** | Digital systems | Design tokens, navigation, components, accessibility, exports |
| **E** | Documents and print | Formal layouts, versioning, production, correspondence |
| **F–H** | Future activation | Systems and engineering, delivery, quality and security |

Series F–H remain reserved until activated through the governance process.

## Repository structure

```text
Unified Operating Library/
├── 01_Standards/       Binding normative standards
├── 02_Assets/          Master symbols and design-system assets
├── 03_Templates/       Approved print and digital templates
├── 04_Publications/    Compiled institutional publications
├── 05_Records/         Governance reviews and audit records
├── 06_Dependencies/    Third-party fonts and color profiles
├── 99_Archive/         Immutable historical snapshots
└── Library-Index.md    Authoritative master register
```

## Working with the library

### Find the right document

1. Consult [Library-Index.md](Unified%20Operating%20Library/Library-Index.md) for the canonical code, path, version, and status.
2. Open the relevant normative standard under `01_Standards/`.
3. Use that standard's linked artifacts to locate governed assets, templates, and publications.
4. Check `06_Dependencies/Dependencies-Manifest.md` before changing fonts or print color profiles.

### Use a standard

Controlled requirements are written with uppercase normative keywords:

- `SHALL` / `SHALL NOT` — mandatory requirement or prohibition
- `SHOULD` / `SHOULD NOT` — recommended default or strong discouragement
- `MAY` — permitted option

All dates use ISO 8601 format (`YYYY-MM-DD`). File and identifier names follow `A02 — Taxonomy, Coding & File Naming`.

### Change a controlled item

Library revisions are governed by [A01 — Document Control & Lifecycle](Unified%20Operating%20Library/01_Standards/A_Governance/A01_Document-Control.md) and [A02 — Taxonomy, Coding & File Naming](Unified%20Operating%20Library/01_Standards/A_Governance/A02_Taxonomy-and-Naming.md).

- Preserve permanent artifact codes.
- Archive outgoing approved snapshots for revisions that require it.
- Update the master index and dependent artifacts on the same change date.
- Obtain written Approver confirmation before releasing a controlled update.
- Record exceptions and compliance reviews through `A04`.

## Key publications and artifacts

- [Brand and Design System Guide](Unified%20Operating%20Library/04_Publications/PUB-01_Brand-and-Design-System-Guide.html)
- [AI Design System Context](Unified%20Operating%20Library/04_Publications/PUB-03_AI-Design-System-Context.md)
- [Design Tokens](Unified%20Operating%20Library/02_Assets/AST-D01-01_Design-Tokens.json)
- [Primary Symbol](Unified%20Operating%20Library/02_Assets/AST-B01-01_Primary-Symbol.svg)
- [Digital Formal Cover Template](Unified%20Operating%20Library/03_Templates/TPL-E01-03_Formal-Cover-Digital.html)
- [Dependencies Manifest](Unified%20Operating%20Library/06_Dependencies/Dependencies-Manifest.md)

## Authority and precedence

Conflict resolution follows A01 and the registered hierarchy:

1. Statutory, regulatory, and contractual obligations
2. Series A governance and traceability
3. Active normative standards
4. Master assets and executable templates
5. Compiled publications
6. Project and product specifications

A compiled publication is informative and does not override its underlying normative standards. Active standards and the Library Index prevail in case of conflict.

## Entity

**Irvantri Standards**  
`Irvantri Standards Pte. Ltd.`  
A member of Irvantri Group

---

Maintained by the Irvantri Standards Approver and Owner. Canonical changes are recorded in the Library Index and the applicable revision history.