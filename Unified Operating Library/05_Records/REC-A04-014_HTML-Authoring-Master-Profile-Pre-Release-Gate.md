# REC-A04-014 — HTML Authoring Master Profile Pre-Release Gate

| Field | Value |
| :--- | :--- |
| **Code** | `REC-A04-014` |
| **Record Type** | Pre-Release Gate |
| **Date** | `2026-11-28` |
| **Status** | `Closed` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Related Standards** | `A01 (v1.2.0)`, `A02 (v1.3.0)`, `A04 (v1.2.0)`, `C01 (v1.1.1)`, `D01 (v1.0.3)`, `D03 (v2.0.0)`, `D04 (v1.2.1)`, `E01 (v2.5.0)`, `E03 (v1.1.0)`, `E04 (v2.3.0)`, `Library-Index.md (v1.2.24)` |
| **Expiry Date** | `None` |

## 1. Review Scope & Trigger

This Governance Record (`REC-`) documents the Pre-Release Gate (`A04 (v1.2.0) §5.1.2`, `§5.1.5`) for the items below, released together with `Library-Index.md (v1.2.24)`:

| Item | Change | Version Gated |
| :--- | :--- | :--- |
| `E01` | `MINOR`: new Section `5.5` (`5.5.1`–`5.5.10`), the `HTML` Authoring Master Profile, and Check `E01-C5`; three Section 4 terms; `C03`, `D01`, `D03`, and `D04` added to Section 3 | `v2.5.0` |
| `E04` | `MINOR`: new `5.4.3`–`5.4.5` applying the profile to page templates and `HTML` slide masters and allowing native or Cloud-Native Office File companions for slides and workbooks; `E04-C4` extended; `D03` and `D04` added to Section 3 | `v2.3.0` |
| `tools/library_checks.py` | New `html-master` check measuring `E01 §5.5.3`, `§5.5.4`, and `§5.5.6`–`§5.5.9` for every registered `HTML` template | — |
| `PUB-01`, `PUB-02`, `PUB-03` | Build manifests synced to `E01 (v2.5.0)`, `E04 (v2.3.0)`, and `Library-Index.md (v1.2.24)` | `v2.0.8`, `v2.0.7`, `v1.2.3` |

**Trigger.** On `2026-11-28` the Approver asked whether `HTML` masters should become the standard template format and what that means for the people who fill them in. A proposal (`proposals/html-master-default/HTML-Master-Default-Proposal_2026-11-28.md` in the project files) set out the profile and four decisions. On `2026-11-28` the Approver approved all four:

1. `MINOR` revisions of `E01` and `E04` that apply only to templates created or revised from `2026-11-28`, so no template moves to `Sync Required`.
2. Fonts embedded in each master as byte-identical data `URI`s, with no Google Fonts request.
3. `Save filled copy` and an unsaved-changes warning as `SHALL`, and autosave as `SHOULD`.
4. Overflow blocks both exports, with no `Export anyway`.

## 2. Method

Every result below was measured on branch `claude/project-thread-bq4jbz`, based on `main` at `405d22c`.

* **Anatomy and text:** a Python script parsed the header fields and level-2 sections of `E01` and `E04`, and scanned every line the release adds under `01_Standards/` for prohibited keywords, lowercase keywords, pronouns, and contractions. It also counted words per sentence in each added Section 5 clause, counting each code span as one word.
* **Removed text:** `git diff -U0` against `main` lists every removed line in `E01` and `E04`.
* **Archive integrity:** `SHA-256` of each archived file compared with the outgoing file on `main` at `405d22c`.
* **New check:** `measure_html_master()` ran on two synthetic pages, one built to pass every measured clause and one built to fail them, and on the live `TPL-E01-03`.
* **Automated check:** `tools/library_checks.py` (register sync, palette, token parity, contrast, links, `PDF` preflight, press export, `HTML` master, and dependencies), run with the pinned `pypdf 6.1.3`.

## 3. Section 6 Verification — `E01 (v2.5.0)` and `E04 (v2.3.0)` Standards

| Check ID | Status | Measured Evidence |
| :--- | :--- | :--- |
| `A01-C2` | Pass | Both headers have 9 fields in order. `E01` shows Version `v2.5.0` and `E04` shows `v2.3.0`, both with Effective Date `2026-11-28`. `Governs` is unchanged: `TPL-E01-01`, `TPL-E01-03`, and `TPL-E01-04` for `E01`, and `TPL-E04-01`–`TPL-E04-03` for `E04`, matching each Section 7. |
| `A01-C3` | Pass | Both files keep level-2 sections `1`–`8` in order. New clauses are numbered `5.5.1`–`5.5.10` (`E01`) and `5.4.3`–`5.4.5` (`E04`). Both new notes use the `> **Informative Note:**` prefix. |
| `A01-C4` | Pass | Added lines contain zero `MUST`, `WILL`, or `REQUIRED`, and zero lowercase `shall`, `should`, or `may`. The 37 new `SHALL` keywords each name a measurable value, a named control, or a referenced clause. |
| `A01-C5` | Pass | The removed lines are only the old Version and Effective Date fields, the Section 1 sentence, the `Library-Index.md` reference floors, the Section 4 lead-in, and the `E04-C4` text that the extended check repeats in full. No `SHALL` or `SHALL NOT` clause changes and no clause is renumbered, so both releases are `MINOR` (`A01 (v1.2.0) §5.5.4`). Every template keeps its pin. |
| `A01-C6`, `A02-C6` | Pass | `99_Archive/E01_Formal-Document-Layout_v2.4.0.md` has `SHA-256` `34d01b6a…ae4f641c`, and `99_Archive/E04_Correspondence-and-Presentations_v2.2.0.md` has `07e96830…4909a7b9`. Both equal the outgoing files on `main`. |
| `C01-C2` | Pass | Added lines contain zero first- or second-person pronouns and zero contractions. |
| `C01-C3` | Pass | The longest new Section 5 sentence is `29` words. `URI` and `ARIA` are expanded at first use in `E01`. |
| Section 5 to 6 mapping | Pass | `E01 §5.5.1`–`§5.5.10` are each cited by the new `E01-C5`. `E04 §5.4.3`–`§5.4.5` are cited by the extended `E04-C4`. |
| Section 3 parity | Pass | New clauses cite `A02`, `A04`, `B01`, `B02`, `B03`, `D01`, `D03`, and `D04`. Each is in Section 3 of the citing standard. Both floors are `Library-Index.md` `v1.2.24`. |

`E01 §5.5.10` and the `E01-C5` behaviour checks apply to the release of an `HTML` Authoring Master. This release adds no master, so no export evidence is due here.

## 4. Section 6 Verification — `html-master` Check

| Test | Status | Measured Evidence |
| :--- | :--- | :--- |
| Passing synthetic page | Pass | Zero literal colors, 2 fields both limited, `Save filled copy` and `beforeunload` found, `Press preview` found beside `Export press PDF`, zero remote requests, one embedded font whose `SHA-256` matches the Dependencies Manifest, one Live Region. |
| Failing synthetic page | Pass | It reported the literal `color: #074C96`, one field without a limit, no `Save filled copy`, no unsaved-changes warning, no `Press preview`, one remote `<link>`, and zero Live Regions. |
| Live `TPL-E01-03` | Measured, not enforced | It is pinned to `E01 (v2.4)`, before the profile (`E01 §5.5.1`), so the check records the results without failing. It shows one literal color (`rgba(15, 23, 42, 0.45)` dialog backdrop), 2 field templates without a limit, no `Save filled copy` label (its control reads `Save HTML`), no `Press preview`, 2 remote Google Fonts `<link>` elements, 11 fonts by relative path, and one Live Region. |

The `TPL-E01-03` results are the work list for its next revision. They are not findings against this release.

## 5. Section 6 Verification — Register & Publications

| Item | Check ID | Status | Measured Evidence |
| :--- | :--- | :--- | :--- |
| `Library-Index.md (v1.2.24)` | `A01-C7` | Pass | `register-sync` compares 22 standard headers with zero mismatches. The `E01` and `E04` rows show `v2.5.0` and `v2.3.0` with Next Review `2027-05-26`. |
| `PUB-01 (v2.0.8)`, `PUB-02 (v2.0.7)`, `PUB-03 (v1.2.3)` | `A01-C10` | Pass | Each build manifest cites `E01 (v2.5.0)`, `E04 (v2.3.0)`, `Library-Index.md (v1.2.24)`, and a compile date of `2026-11-28`, and keeps its precedence notice. `PUB-02` cites `PUB-01 (v2.0.8)`. The `PUB-02` closing colophon showed `v2.0.5` against a header of `v2.0.6`; it now shows `v2.0.7`. |
| `PUB-01`–`PUB-03` | `B02-C1` | Pass | `palette` reports zero off-palette values. |

## 6. Non-Conformity Register (`A04 (v1.2.0) §5.2.2`)

None. Zero non-conformities were found. The stale `PUB-02` colophon version was corrected in this release and is recorded in Section 5.

## 7. Closure Verification (`A04 (v1.2.0) §5.2.3`, `§5.1.7`)

* **Gate Verdict:** `Pass`. The items in Section 1 are released as listed.
* **Automated Check:** `python3 tools/library_checks.py` gives `PASS` with zero failing findings and zero known issues on the release branch. The continuous integration (`CI`) run for the release commit is cited in the pull request.
* **Follow-Up:** The header and footer (`TPL-E01-01`, `TPL-E01-04`) and the letterheads (`TPL-E04-01`, `TPL-E04-03`) move to `HTML` Authoring Masters in later releases, each with its own gate under `E01 §5.5.10`. `TPL-E01-03` meets the profile when it is next revised (Section 4).
* **Approver Sign-Off:** The Approver approved the proposal on `2026-11-28`. Merging the release pull request records sign-off and puts the release into effect.
* **Approver:** Hary Irfantri
