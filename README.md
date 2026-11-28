# Irvantri Standards

**Standards Design**

The authoritative repository for the governance, visual, verbal, digital, and documentation standards used by [Irvantri Standards Pte. Ltd.](https://irvantri.com).

[Library index](#library-index) · [Repository structure](#repository-structure) · [Hybrid workflow](#hybrid-github--google-drive-workflow) · [Authority and precedence](#authority-and-precedence)

---

> **Status:** Approved · **Register:** `v2.0.0` · **Last updated:** 2026-11-28

## Purpose

**Standards Design** turns institutional requirements into consistent, verifiable outputs. It provides normative standards, controlled master assets, executable templates, compiled publications, governance records, and tracked third-party dependencies.

The repository currently contains:

| Resource | Count | Purpose |
| --- | ---: | --- |
| Normative standards | 23 | Binding rules across active Series A–E (`A01`–`E05`) |
| Master assets | 27 | Canonical marks, favicons/app icons, design tokens (`JSON` + `CSS`), component kit, and gallery |
| Executable templates | 4 active | Single-file `HTML` authoring masters (`TPL-E01-03`, `TPL-E01-06`) and official letterheads (`TPL-E04-01`/`03`); `TPL-E04-02` `Planned` |
| Compiled publications | 3 | Human-facing and AI-facing reference documents (`PUB-01`–`PUB-03`) |
| Governance records | 16 | Reviews, audits, and measured Pre-Release Gates (`REC-A04-001`–`016`) |

## Library index

The [Library Index](Standards%20Design/Library-Index.md) is the authoritative register for every controlled item in the repository.

Start with the index when you need to:

- Find the active version and status of a standard or artifact.
- Identify the governing standard for a master asset or template.
- Trace dependencies and compiled publications.
- Review active, reserved, or deprecated library items.

For a concise institutional overview, read [PUB-02 — Company Overview](Standards%20Design/04_Publications/PUB-02_Company-Overview.md).

## Series

| Series | Domain | Standards |
| --- | --- | --- |
| **A** | Governance and traceability | [Document control](Standards%20Design/01_Standards/A_Governance/A01_Document-Control.md), taxonomy, entity architecture, compliance |
| **B** | Visual foundations | Marks, color, typography, grids, iconography |
| **C** | Information and verbal | Voice, terminology, UX writing, dates and citations |
| **D** | Digital systems | Design tokens, navigation, components, accessibility, exports |
| **E** | Documents and print | Formal layouts, versioning, production, correspondence, document body elements |
| **F–H** | Future activation | Systems and engineering, delivery, quality and security |

Series F–H remain reserved until activated through the governance process.

## Repository structure

```text
Standards Design/
├── 01_Standards/       Binding normative standards (A01–E05)
├── 02_Assets/          Master marks, tokens (JSON/CSS), component kit & gallery
├── 03_Templates/       Approved HTML authoring masters and print/digital letterheads
├── 04_Publications/    Compiled institutional and AI publications (PUB-01–PUB-03)
├── 05_Records/         Immutable governance reviews and Pre-Release Gates
├── 06_Dependencies/    Third-party fonts, script libraries, and ICC color profile
└── Library-Index.md    Authoritative master register

tools/                  Automated CI checks, token/template builders, and Drive publisher
.github/workflows/      Continuous integration (`library-checks.yml`) and Drive publish
```

## Hybrid GitHub + Google Drive workflow

Per [A01 §5.9](Standards%20Design/01_Standards/A_Governance/A01_Document-Control.md), **Standards Design** separates authoring from stakeholder distribution:

1. **GitHub (`haryirfantri/irvantri-standards`) — Authoring Repository of Record:**
   - All changes to `Standards Design/` are authored on feature branches and reviewed via Pull Requests running `.github/workflows/library-checks.yml`.
   - Git commit history and annotated release tags preserve every historical revision natively.
2. **Google Drive (`Standards Design/`) — Read-Only Distribution Mirror & Cold Archive:**
   - Active controlled folders (`01_Standards/`–`06_Dependencies/` and `Library-Index.md`) are published strictly one-way from GitHub `main` via `tools/publish_drive.py` or `.github/workflows/publish-drive.yml`.
   - `99_Archive/` resides exclusively on Google Drive as an append-only Cold Archive preserving outgoing `MAJOR`/`MINOR`/`Deprecated` snapshots and retired vendor packages.

### Run checks locally

```sh
pip install -r tools/requirements.txt
python3 tools/library_checks.py --report-dir check-report
python3 tools/build_tokens_css.py --check
python3 tools/build_document_master.py --check
```

## Key publications and artifacts

- [Brand and Design System Guide](Standards%20Design/04_Publications/PUB-01_Brand-and-Design-System-Guide.html)
- [AI Design System Context (`DESIGN.md`)](Standards%20Design/04_Publications/PUB-03_AI-Design-System-Context.md)
- [Design Tokens (`JSON`)](Standards%20Design/02_Assets/AST-D01-01_Design-Tokens.json) & [Design Tokens (`CSS`)](Standards%20Design/02_Assets/AST-D01-02_Design-Tokens.css)
- [Component Kit (`CSS`)](Standards%20Design/02_Assets/AST-D03-01_Component-Kit.css) & [Component Gallery (`HTML`)](Standards%20Design/02_Assets/AST-D03-02_Component-Gallery.html)
- [Formal Document Master (`TPL-E01-06`)](Standards%20Design/03_Templates/TPL-E01-06_Formal-Document-Master.html)
- [Digital Formal Cover Template (`TPL-E01-03`)](Standards%20Design/03_Templates/TPL-E01-03_Formal-Cover-Digital.html)
- [Dependencies Manifest](Standards%20Design/06_Dependencies/Dependencies-Manifest.md)

## Authority and precedence

Conflict resolution follows `A01 §5.1.4`:

1. Statutory, regulatory, and contractual obligations
2. Series A governance and traceability
3. Active normative standards
4. Master assets and executable templates
5. Compiled publications
6. Project and product specifications

A compiled publication is informative and does not override its underlying normative standards. Active standards in GitHub `main` prevail in case of conflict.

## Entity

**Irvantri Standards**  
`Irvantri Standards Pte. Ltd.`  
A member of Irvantri Group

---

Maintained by the Irvantri Standards Approver and Owner. Canonical changes are recorded in `Library-Index.md` and Git history.