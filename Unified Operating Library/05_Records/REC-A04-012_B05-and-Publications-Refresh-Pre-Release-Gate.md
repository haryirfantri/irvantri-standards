# REC-A04-012 — B05 v1.2.0 & Publications Refresh Pre-Release Gate

| Field | Value |
| :--- | :--- |
| **Code** | `REC-A04-012` |
| **Record Type** | Pre-Release Gate |
| **Date** | `2026-11-27` |
| **Status** | `Closed` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Related Standards** | `A01 (v1.2.0)`, `A02 (v1.3.0)`, `A04 (v1.2.0)`, `B01 (v2.1.0)`, `B05 (v1.2.0)`, `C01 (v1.1.1)`, `Library-Index.md (v1.2.22)` |
| **Expiry Date** | `None` |

## 1. Review Scope & Trigger

This Governance Record (`REC-`) documents the Pre-Release Gate (`A04 (v1.2.0) §5.1.2`, `§5.1.5`) for the items below, released together with `Library-Index.md (v1.2.22)`:

| Item | Change | Version Gated |
| :--- | :--- | :--- |
| `B05` | `MINOR`: new `5.1.4` requiring the `B01` Small-Format Symbol for brand symbols from `16 px` to below `28 px`; `B05-C1` extended | `v1.2.0` |
| `PUB-01` | Small-Format Symbol, favicon, and App Icon Tile cards; two Table 1 rows; page favicon; build manifest refreshed | `v2.0.6` |
| `PUB-02` | Section 4.3 marks summary extended; governing standards and build manifest refreshed | `v2.0.5` |
| `PUB-03` | Favicon and app icon guidance added; source standards and build manifest refreshed | `v1.2.1` |

The trigger is the follow-up named in `REC-A04-011` Section 7: the publications still cited `B01 (v2.0.0)`, and `B05 §5.1.3` described small-format derivatives without naming the registered asset. The Approver asked for both follow-ups on `2026-11-27`.

## 2. Method

Every result below was measured on the delivered file on branch `claude/project-thread-pgj5r3`, based on `main` at `6640da7`.

* **Embedded assets:** a script decoded every `SVG` data `URI` in `PUB-01` and compared its `SHA-256` with the `02_Assets/` master.
* **Render:** headless Chromium `158.0.8127.36` (Playwright `1.63.0`) loaded `PUB-01` at `1280 px` and `390 px` widths, listed console errors, checked that every image in Section 02 decoded, and read the page favicon link.
* **Standards text:** a script scanned every added line for prohibited keywords, first- and second-person pronouns, contractions, and vague qualifiers, and counted sentence length in words.
* **Automated check:** `tools/library_checks.py` (register sync, palette, token parity, contrast, links, `PDF` preflight, and dependencies).

## 3. Section 6 Verification — `B05 (v1.2.0)` Standard

| Check ID | Status | Measured Evidence |
| :--- | :--- | :--- |
| `A01-C2` | Pass | The header has 9 fields in order. Version `v1.2.0`, Effective Date `2026-11-27`, and `ISO` 8601 dates. `Governs` stays `None`, matching an empty Section 7. |
| `A01-C3` | Pass | Level-2 sections `1`–`8` remain in order. The new clause is numbered `5.1.4`, and its note uses the `> **Informative Note:**` prefix. |
| `A01-C4` | Pass | Added lines contain zero `MUST`, `WILL`, or `REQUIRED`, and zero vague qualifiers. The new `SHALL` states a pixel range and two asset codes. |
| `A01-C5` | Pass | The release adds `5.1.4` and changes no existing `SHALL` or `SHALL NOT` text, so it is `MINOR` (`A01 (v1.2.0) §5.5.4`). |
| `A01-C6`, `A02-C6` | Pass | `99_Archive/B05_Iconography-and-Visuals_v1.1.0.md` has `SHA-256` `fe7db68c…5e06166d`, equal to the outgoing file on `main` at `6640da7`. |
| `A01-C7` | Pass | `register-sync` compares 22 standard headers with `Library-Index.md (v1.2.22)` and reports zero mismatches. |
| `C01-C2`, `C01-C3` | Pass | Zero pronouns and zero contractions in added lines. The longest new sentence in `5.1.4` is `24` words (each code span counted as one word), within the `30`-word limit. |
| Section 5 to 6 mapping | Pass | `5.1.4` is cited by the extended `B05-C1`. |
| Section 3 parity | Pass | The new clause cites `B01`, which is already listed in Section 3. |

## 4. Section 6 Verification — Publications

| Item | Check ID | Status | Measured Evidence |
| :--- | :--- | :--- | :--- |
| `PUB-01 (v2.0.6)` | `B01-C1` | Pass | The page embeds 5 new `SVG` data `URI`s. Each decodes to bytes identical to its master: `AST-B01-17` (3: page favicon, `16 px`, and `24 px` previews), `AST-B01-18` (1), and `AST-B01-20` (1). |
| `PUB-01 (v2.0.6)` | `B01-C8` | Pass | The Small-Format Symbol previews render at `16` and `24 px`, inside the `16`–`27 px` range of `B01 §5.3.4`. The page favicon is `AST-B01-17`, linked as `image/svg+xml`. The App Icon Tile preview shows `AST-B01-20` unaltered. |
| `PUB-01 (v2.0.6)` | `D04` render | Pass | All 8 images in Section 02 decode. There are zero console errors other than the external font host. Page width equals the viewport at `1280 px` and at `390 px`, so there is no horizontal scroll. |
| `PUB-01 (v2.0.6)`, `PUB-02 (v2.0.5)`, `PUB-03 (v1.2.1)` | `A01-C10` | Pass | Each build manifest cites `B01 (v2.1.0)`, `B05 (v1.2.0)`, `Library-Index.md (v1.2.22)`, and a compile date of `2026-11-27`, and keeps its precedence notice. `PUB-02` cites `PUB-01 (v2.0.6)`. |
| `PUB-01`–`PUB-03` | `B02-C1` | Pass | `palette` reports zero off-palette values across all three files. |
| `PUB-02`, `PUB-03` | `C01-C2` | Pass | Zero pronouns and zero contractions in added lines. The longest new sentence is `27` words (`PUB-02` Section 4.3). |

## 5. Non-Conformity Register (`A04 (v1.2.0) §5.2.2`)

None. Zero non-conformities were found.

## 6. Closure Verification (`A04 (v1.2.0) §5.2.3`, `§5.1.7`)

* **Gate Verdict:** `Pass`. The items in Section 1 are released as listed.
* **Automated Check:** `python3 tools/library_checks.py` gives `PASS` with zero failing findings and zero known issues on this branch.
* **Approver Sign-Off:** The Approver requested both follow-ups on `2026-11-27`. Merging the release pull request records sign-off and puts the release into effect.
* **Approver:** Hary Irfantri
