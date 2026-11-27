# REC-A04-007 — B03 v2.0.0 Typography Migration Event-Driven Audit

| Field | Value |
| :--- | :--- |
| **Code** | `REC-A04-007` |
| **Record Type** | Event-Driven Audit |
| **Date** | `2026-11-26` |
| **Status** | `Closed` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Related Standards** | `A01 (v1.2.0)`, `A02 (v1.2.0)`, `A03 (v1.1.1)`, `A04 (v1.1.1)`, `B01 (v2.0.0)`, `B03 (v2.0.0)`, `D01 (v1.0.3)`, `E01 (v2.0.2)`, `E02 (v1.1.0)`, `E03 (v1.0.0)`, `E04 (v2.0.0)`, `Library-Index.md (v1.2.5)` |
| **Expiry Date** | `None` |

## 1. Review Scope & Trigger

This Governance Record (`REC-`) documents the Event-Driven Audit triggered by the `MAJOR` revision of `B03 (v2.0.0)` and paired decoupling releases of `E01 (v2.0.0)`, `E02 (v1.1.0)`, and `E04 (v2.0.0)` on `2026-11-26` (`A01 (v1.2.0) §5.5.3`, `§5.6.3`; `A04 (v1.1.1) §5.1.2`). The migration replaces `Montserrat`, `Inter`, and `JetBrains Mono` with the `SIL OFL-1.1` Noto Sans superfamily (`Noto Sans Display`, `Noto Sans`, `Noto Sans Mono`).

## 2. Mandatory Library Control Inspection (`A04 (v1.1.1) §5.1.3`)

| Control Area | Governing Clause | Status | Evidence & Notes |
| :--- | :--- | :--- | :--- |
| **Metadata Synchronization** | `A01 (v1.2.0) §5.8.1` | Pass | `B03 (v2.0.0)`, `E01 (v2.0.2)`, `E02 (v1.1.0)`, `E04 (v2.0.0)`, `Dependencies-Manifest.md (v2.0.0)`, `AST-B01-03`/`04` (`Approved`), `AST-D01-01` (`Approved`), `TPL-E01-01`–`04` (`Approved`), `PUB-01 (v2.0.0)` (`Approved`), `PUB-02 (v2.0.0)` (`Approved`), and `REC-A04-007` (`Closed`) synced in `Library-Index.md (v1.2.5)` on `2026-11-26`. |
| **Overdue Standard Reviews** | `A01 (v1.2.0) §5.6.5` | Pass | Zero standards exceed scheduled `Next Review` dates (`2027-05-20` earliest). |
| **Asset & Template Drift** | `A01 (v1.2.0) §5.5.3`, `§5.7.4` | Pass | Zero `Sync Required` items remain across the Unified Operating Library: `AST-D01-01`, `AST-B01-03`/`04` (`F-01`), `TPL-E01-01`–`04` (`F-02`), and `PUB-01`/`PUB-02` (`F-03`) are all synced to `B03 (v2.0.0)` and `Approved`. |
| **Archive Integrity** | `A01 (v1.2.0) §5.7.2`, `A02 (v1.2.0) §5.6` | Pass | Outgoing snapshots preserved unmodified in `99_Archive/`: `B03_Typography_v1.1.0.md`, `E01_Formal-Document-Layout_v1.2.0.md`, `E02_Versioning-and-Draft-Marking_v1.0.0.md`, `E04_Correspondence-and-Presentations_v1.1.0.md`, `Dependencies-Manifest_v1.0.0.md`, `AST-D01-01_Design-Tokens_v1.0.0.json`, `AST-B01-03_Parent-Lockup_v1.0.0.svg`, `AST-B01-04_Parent-Lockup-White_v1.0.0.svg`, `TPL-E01-02_Formal-Cover-Print_v1.0.0.pdf`, `TPL-E01-03_Formal-Cover-Digital_v1.0.0.pdf`, `PUB-01_Brand-and-Design-System-Guide_v1.0.0.html`, `PUB-02_Company-Overview_v1.0.0.md`, `Library-Index_v1.2.0.md`, and legacy font packages (`Montserrat/`, `Inter/`, `JetBrains Mono/`). |
| **Active Waivers** | `A04 (v1.1.1) §5.4.9` | Pass | Zero active or expired waivers exist; `REC-A04-001` through `REC-A04-007` remain immutable in terminal `Closed` status. |
| **Cross-Standard Conflicts** | `A04 (v1.1.1) §5.3.2` | Pass | `E01`, `E02`, and `E04` decoupled to reference `B03 §5.1.1` Display/Text roles; `B01 (v2.0.0)` `664 × 160` (`260 px` / `64 mm`) lockup minimums verified mathematically compatible with curve-outlined `Noto Sans` (`9.26 px` / `6.46 pt` Endorsement Line cap height). |

## 3. Non-Conformity & Drift Remediation Register (`A04 (v1.1.1) §5.2.2`)

All Service Level Agreement (`SLA`) due dates are calculated from `2026-11-26` per `A04 (v1.1.1) §5.2.1`: `Major` findings carry a 15-business-day closure window (`2026-12-17`).

| Finding ID | Affected Item | Violated Clause / Check ID | Severity | Assigned Owner | Due Date | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `F-01` | `AST-B01-03`, `AST-B01-04` | `B03 (v2.0.0) §5.1.1` (`B03-C1`); `A01 (v1.2.0) §5.5.3` | `Major` | Hary Irfantri | `2026-12-17` | `Closed` |
| `F-02` | `TPL-E01-02`, `TPL-E01-03` | `B03 (v2.0.0) §5.1.1`–`§5.1.2` (`B03-C1`); `E01 (v2.0.0) §5.1.2` (`E01-C1`) | `Major` | Hary Irfantri | `2026-12-17` | `Closed` |
| `F-03` | `PUB-01`, `PUB-02` | `A01 (v1.2.0) §5.1.4`, `§5.7.5` (`A01-C10`); `B03 (v2.0.0) §5.1.1`–`§5.1.2` (`B03-C1`) | `Major` | Hary Irfantri | `2026-12-17` | `Closed` |

## 4. Detailed Finding Descriptions & Remediation Summary

* **`F-01` (`Major` — Parent-Endorsed Lockup SVG Typography Drift — `Closed` `2026-11-26`):** `02_Assets/AST-B01-03_Parent-Lockup.svg` and `02_Assets/AST-B01-04_Parent-Lockup-White.svg` previously rendered wordmark and Endorsement Line typography from retired `B03 (v1.1.0)` fonts (`Montserrat` / `Inter`). **Closure Evidence (`A04 §5.2.3`):** Archived outgoing masters unmodified as `99_Archive/AST-B01-03_Parent-Lockup_v1.0.0.svg` and `99_Archive/AST-B01-04_Parent-Lockup-White_v1.0.0.svg`. Rebuilt both `664 × 160` (`4.15:1`) vector masters using verbatim `AST-B01-01`/`02` symbol paths and curve-outlined `NotoSansDisplay-ExtraBold.ttf` (`v2.003`) + `NotoSans-Regular.ttf` (`v2.004`) paths with GPOS kerning (`33 px` Endorsement Line, divider at `x = 192`, text at `x = 228`), passing all `B01-C1`–`C5`/`C7`, `B02-C1`–`C5`, and `B03-C1`–`C5` Pre-Release Gate checks (`9.26 px` digital / `6.46 pt` print `'A'` cap height at `260 px` / `64 mm` minimums; canonical uppercase `#RRGGBB` fills). Promoted both files to `Approved` in `02_Assets/` with explicit Approver sign-off (Hary Irfantri) and synced `Library-Index.md (v1.2.3)` on `2026-11-26`.
* **`F-02` (`Major` — Formal Cover Template Typography Drift — `Closed` `2026-11-26`):** `03_Templates/TPL-E01-02_Formal-Cover-Print.pdf` and `03_Templates/TPL-E01-03_Formal-Cover-Digital.pdf` previously embedded retired `B03 (v1.1.0)` fonts and remained pinned to `E01 (v1.2)`. **Closure Evidence (`A04 §5.2.3`):** Archived outgoing covers unmodified as `99_Archive/TPL-E01-02_Formal-Cover-Print_v1.0.0.pdf` and `99_Archive/TPL-E01-03_Formal-Cover-Digital_v1.0.0.pdf`. Recompiled both paired covers from identical A4 geometry using verbatim `AST-B01-03` vector paths (`80 mm × 19.28 mm`), `4 mm` vertical left-spine `76%` / `24%` accent bar, `24 mm` inner / `20 mm` outer Safe Margins, and 5 embedded `SIL OFL-1.1` Noto font subsets with zero substitute fonts. Preflight verified `TPL-E01-02` (`PDF/X-4`, `FOGRA39` OutputIntent, `3 mm` Bleed + `100%` K crop marks, zero RGB operators, max ink `266% < 300%`) and `TPL-E01-03` (exact A4 `sRGB IEC61966-2.1`, zero bleed/crop marks, live selectable text) passing all `E01-C1`/`C3`/`C4`, `E02-C1`/`C2`, `E03-C1`/`C3`/`C4`, and `B01`–`B04` checks. Promoted both to `Approved` pinned to `E01 (v2.0)` with explicit Approver sign-off (Hary Irfantri), updated `E01 (v2.0.2)`, and synced `Library-Index.md (v1.2.4)` on `2026-11-26`.
* **`F-03` (`Major` — Compiled Publication Typography & Manifest Drift — `Closed` `2026-11-26`):** `PUB-01` (`Sync Required`, also tracked under `REC-A04-006` `F-02`) and `PUB-02` (`§4.3` hardcoded retired font names) previously reflected `B03 (v1.1.0)` and `B01 (v1.0.1)`. **Closure Evidence (`A04 §5.2.3`):** Archived outgoing publications unmodified as `99_Archive/PUB-01_Brand-and-Design-System-Guide_v1.0.0.html` and `99_Archive/PUB-02_Company-Overview_v1.0.0.md`. Recompiled both publications to `v2.0.0` (`2026-11-26`): `PUB-01 (v2.0.0)` regenerated all `91` `--is-*` CSS tokens from `AST-D01-01`, embedded curve-outlined `AST-B01-03`/`04`, updated Table 1 (`260 px` / `64 mm`) and Section 04 / Table 4 (Noto Sans superfamily), and synced Table 6 across all 22 live `Approved` standards (`Library-Index.md (v1.2.4)`); `PUB-02 (v2.0.0)` updated `§3.1`–`§3.2`, `§4.3`, and Table 6 with zero occurrences of retired font names or contractions. Passed all Pre-Release Gate checks, received explicit Approver sign-off (Hary Irfantri), promoted both to `Approved` in `04_Publications/`, and synced `Library-Index.md (v1.2.5)` on `2026-11-26`.

## 5. Closure Verification (`A04 (v1.1.1) §5.2.3`)

* **Approver Sign-Off Date:** `2026-11-26`
* **Approver:** Hary Irfantri
* **Objective Closure Evidence:** All three drift findings (`F-01`, `F-02`, `F-03`) are verified `Closed` with zero remaining `Sync Required` artifacts across Series `A`–`E`, all outgoing superseded files are archived unmodified in `99_Archive/`, and `Library-Index.md (v1.2.5)` is synchronized. This record is transitioned to immutable terminal `Closed` status per `A04 (v1.1.1) §5.5.3`.
