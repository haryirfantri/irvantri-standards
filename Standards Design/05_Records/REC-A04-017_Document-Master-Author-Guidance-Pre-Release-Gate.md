# REC-A04-017 — Document Master Author Guidance Pre-Release Gate

| Field | Value |
| :--- | :--- |
| **Code** | `REC-A04-017` |
| **Record Type** | Pre-Release Gate |
| **Date** | `2026-11-28` |
| **Status** | `Closed` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Related Standards** | `A01 (v2.0.0)`, `A02 (v2.0.0)`, `A04 (v1.2.1)`, `B02 (v2.0.0)`, `C01 (v1.1.2)`, `C03 (v1.0.1)`, `D04 (v1.2.1)`, `E01 (v2.6.1)`, `E02 (v1.1.1)`, `E05 (v2.0.0)`, `Library-Index.md (v2.0.1)` |
| **Expiry Date** | `None` |

## 1. Review Scope & Trigger

This Governance Record (`REC-`) documents the Pre-Release Gate (`A04 (v1.2.1) §5.1.2`, `§5.1.5`) for the items below, released together with `Library-Index.md (v2.0.1)`:

| Item | Change | Version Gated |
| :--- | :--- | :--- |
| `TPL-E01-06` | Revised in place: opens as a blank `Draft` at `v0.1.0` dated the current day; **How to use this template** panel (six numbered steps) with **Start blank document** and **Load sample document** and an inline replace confirmation; **Markdown cheat sheet** (20 elements); Export checks count; **Go to** selects the affected body text; next-step messages after each export. Pin unchanged. | `E01 (v2.6)` |
| `PUB-04` | New compiled publication: Formal Document Master Quick-Start (six-step workflow and the five most common Export Blocks) | `v1.0.0` |
| `tools/` | `contrast-pairs.json` gains the confirmation panel pairing; `README.md` describes the guide, the sample, and `PUB-04` | — |

**Trigger.** On `2026-11-28` the Approver asked whether a new author needs a guide to the Formal Document Master and approved two layers: guidance built into the template, and a one-page quick-start in the library. A preview (screenshots and a `PUB-04` draft in the project files) was reviewed. The Approver approved:

1. The quick-start as `PUB-04`, a Markdown compiled publication synthesized from `C03`, `C04`, `E01`, `E02`, `E03`, and `E05`. Click-level detail stays in the template, because `A01 §2.2` places tool click-paths outside the library.
2. The template opens as a blank `Draft`, with the sample one click away.
3. `TPL-E01-06` revised in place with its `E01 (v2.6)` pin, no archive copy (as for the in-place `TPL-E01-03` fixes in `REC-A04-009`), `Library-Index.md` `ERRATA` `v2.0.1`, and no standard text changed.
4. The five most common Export Blocks named in `PUB-04` Section 3 (an estimate from the block catalogue, not a usage measurement).

## 2. Method

Initial browser and export measurements were taken on branch `claude/project-thread-jfg5u7` at commit `846a5b9` (prior to the `REC-A04-016` unification), then rebased onto `main` (`4c91b2d`, `Standards Design/`, `Library-Index.md v2.0.0`), rebuilt from `tools/document-master/`, and re-verified with `python3 tools/library_checks.py` and `CI`.

* **Subject:** `03_Templates/TPL-E01-06_Formal-Document-Master.html`, `7,667,238` bytes, `SHA-256` `c74be66a…cf75c646`.
* **Behaviour:** a scripted Chromium (Playwright) run opened the file from disk with `window.print` captured: opening state, keyboard order, replace confirmation, sample load, both exports, Press Preview, overflow, Export Blocks and **Go to**, Filled Copy save and reopen, `beforeunload`, guide state, and network requests.
* **Exports:** the sample document was saved as `PDF` with `preferCSSPageSize` in print media after **Export A4 PDF** and **Export press PDF**. `tools/pdf_finish.py` finished the digital file; `tools/press_export.py` converted the press file. Both were measured with the `pdf-preflight` functions of `tools/library_checks.py` and `pypdf 6.1.3`.
* **Text:** `PUB-04` and the new interface strings were scanned for normative keywords, pronouns, and contractions.
* **Automated check:** `python3 tools/library_checks.py`.

## 3. Section 6 Verification — `TPL-E01-06`

| Check ID | Status | Measured Evidence |
| :--- | :--- | :--- |
| `E01-C3`, `E01-C4` | Pass | Digital: 18 pages at `209.89 × 297.01 mm` (inside `±0.5 mm`, `E01 §5.4.5`), 7 embedded fonts, `sRGB` values all on `B02 (v2.0.0)`, zero preflight findings. Press: 18 pages, TrimBox `210 × 297 mm`, BleedBox `3 mm` each side, `FOGRA39` OutputIntent, fixed `B02 (v2.0.0)` `CMYK` builds, maximum total ink `250%`, preflight passed. Identical page count and document stylesheet to `REC-A04-016`. |
| `E01-C5` | Pass | `html-master`: zero literal colors, 14 fields all limited (no new fields), `Save filled copy`, `beforeunload`, `Press preview` beside `Export press PDF`, zero remote references, 9 fonts and 4 scripts byte-identical to `06_Dependencies/`, 6 Live Regions, and the file equals a fresh build (`build_document_master.py --check`). Browser: zero network requests and zero page errors across the run. A 90-character title raised "The title is too long for the running footer" and the export stayed stopped. A Filled Copy reopened with the title, Identifier, body and status restored. An unsaved edit fired the `beforeunload` warning. Press preview set `aria-pressed="true"` and showed 18 sheets. |
| `E02-C1` | Pass | The blank document opens at `v0.1.0`, `Draft`, with a one-row Revision History (`v0.1.0`, current date, `Pre-Release`), so a new document starts on the `E02 §5.1.4` draft range and passes the newest-row check. |
| `E05-C1`, `E05-C9` | Pass | The cheat sheet lists 20 Table 1 elements and none of the `E05 §5.1.3` exclusions, which it names as unavailable. The sample loads with one click as 18 pages with zero Export checks. A body with a missing footnote, a misnumbered appendix, and an unknown cross-reference raised 7 Export Blocks; the assertive Live Region announced "Export stopped. 7 items need fixing; see Export checks." and the heading showed "7 to fix". **Go to** selected `[^2]`, `Appendix B — Extra`, and `(#tbl-fees` in the body. |
| `D04-C3` | Pass | Tab order after the skip link: guide summary, **Start blank document**, **Load sample document**, Cover and metadata summary, then the fields in visual order. The confirmation region is labelled by its text; it takes focus on **Keep current document**, and Enter there keeps the content and returns focus to **Start blank document**. Status changes are announced through the existing Live Regions. |
| `C03-C1`, `C03-C4` | Pass | New controls use verb-object sentence-case labels: **Start blank document**, **Load sample document**, **Replace current document**, **Keep current document**. The confirmation states the target and the loss: "This replaces every field, the body and the images with the sample document. Unsaved changes are lost. Save filled copy first to keep them." It appears only when there are unsaved changes. |
| `C03-C7`, `C03-C8` | Pass | The guide panel and `PUB-04` Section 2 use six numbered steps in order, each opening with an imperative verb, and reproduce exact control labels. Zero normative keywords in the guide, cheat sheet, export messages, or `PUB-04` (the cheat sheet clause example reads "Clause text."). |
| `B02-C5`, `D04-C1` | Pass | New pairing Text Primary `#0F172A` on Status Warning Background `#FFFBEB` measures `17.22:1` (minimum `4.5`), added to `contrast-pairs.json`. |

## 4. Section 6 Verification — `PUB-04` & Register

| Item | Check ID | Status | Measured Evidence |
| :--- | :--- | :--- | :--- |
| `PUB-04 (v1.0.0)` | `A01-C10` | Pass | Header, precedence notice, and Section 5 build manifest cite `C03 (v1.0.1)`, `C04 (v1.0.2)`, `E01 (v2.6.1)`, `E02 (v1.1.1)`, `E03 (v1.1.1)`, `E05 (v2.0.0)`, `TPL-E01-06 (E01 (v2.6))`, and `Library-Index.md (v2.0.1)`, compiled `2026-11-28`. |
| `PUB-04 (v1.0.0)` | `A02-C3`, `A02-C5` | Pass | `04_Publications/PUB-04_Document-Master-Quick-Start.md` follows `CODE_Title-Words.ext` with no version suffix; `PUB-04` is the next unused code. |
| `PUB-04 (v1.0.0)` | `C01-C2` | Pass | Zero first- or second-person pronouns and zero contractions. |
| `Library-Index.md (v2.0.1)` | `A01-C7`, `A04-C7` | Pass | `register-sync` compares 23 standard headers with zero mismatches; `PUB-04` and `REC-A04-017` are registered on the release date; the `TPL-E01-06` pin stays `E01 (v2.6)`. |
| `PUB-01`–`PUB-03` | `A01-C10` | Pass | No source they cite changed version; their manifests remain accurate and are not refreshed in this release. |

## 5. Non-Conformity Register (`A04 (v1.2.1) §5.2.2`)

None. One defect found during the build was fixed before this record: the cheat sheet's clause example used `SHALL`, which `C03 §5.5.5` keeps out of interface copy.

## 6. Observations (Upstream, Not Baseline)

* **`U-01` (`E05 (v2.0.0) §5.9.2`):** a digital `PDF` needs `tools/pdf_finish.py`, a Python step, before distribution when the browser omits title, author, or language. Authors without Python depend on the Owner for every digital release. Logged for a future proposal; no change in this release.

## 7. Closure Verification (`A04 (v1.2.1) §5.2.3`, `§5.1.7`)

* **Gate Verdict:** `Pass`. The items in Section 1 are released as listed.
* **Automated Check:** `python3 tools/library_checks.py` gives `PASS` with zero failing findings and zero known issues on the release branch. The continuous integration (`CI`) `library-checks` run [`46138887184`](https://github.com/haryirfantri/irvantri-standards/actions/runs/46138887184) on commit `3b51f42` of the release pull request completed with `success` (`A04 §5.1.7`).
* **Approver Sign-Off:** The Approver approved the plan, preview, and rebase onto `Standards Design` (`Library-Index.md v2.0.1`) on `2026-11-28`. Merging the release pull request records sign-off and puts the release into effect.
* **Approver:** Hary Irfantri
