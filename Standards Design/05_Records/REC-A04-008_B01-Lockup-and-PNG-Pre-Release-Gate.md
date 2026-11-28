# REC-A04-008 — B01 Primary Master Lockup & PNG Derivatives Pre-Release Gate

| Field | Value |
| :--- | :--- |
| **Code** | `REC-A04-008` |
| **Record Type** | Pre-Release Gate |
| **Date** | `2026-11-27` |
| **Status** | `Closed` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Related Standards** | `A01 (v1.2.0)`, `A02 (v1.3.0)`, `A04 (v1.1.1)`, `B01 (v2.0.1)`, `B02 (v1.2.0)`, `B03 (v2.0.0)`, `E01 (v2.2.0)`, `E04 (v2.1.1)`, `Library-Index.md (v1.2.16)` |
| **Expiry Date** | `None` |

## 1. Review Scope & Trigger

This Governance Record (`REC-`) documents the Pre-Release Gate (`A04 (v1.1.1) §5.1.2`) for twelve new Master Assets before promotion to `Approved`:

* `AST-B01-05`–`AST-B01-07`: Primary Master Lockup (`B01 (v2.0.1) §5.1.1`) in the Full-Color Primary, Reversed White, and Monochrome Black colorways (`§5.4.1`).
* `AST-B01-08`: Monochrome Black Symbol (`§5.4.1`).
* `AST-B01-09`–`AST-B01-16`: lossless Portable Network Graphics (`PNG`) derivatives of every `AST-B01` Scalable Vector Graphics (`SVG`) master (`§5.1.2`, `E01 (v2.2.0) §5.4.4`, `E04 (v2.1.1) §5.3.3`).

The trigger is a gap found in the library evaluation of `2026-11-27`. `B01 §5.2.1` and `D02 §5.2.1` require the Primary Master Lockup in navigation bars and product headers, and `§5.4.1` authorizes a Monochrome Black colorway. Neither existed as a registered master, and `§5.6.1` forbids redrawing marks.

Every result below is measured on the delivered files, not inferred from other documents.

## 2. Construction Method

* **Symbol:** The two symbol paths in `AST-B01-05`–`AST-B01-08` are byte-identical to `AST-B01-01`. The symbol group uses the same transform as `AST-B01-03`, so it fills `0`–`160` units in height.
* **Wordmark:** The `IRVANTRI` and `STANDARDS` outlines are the curve-outlined `Noto Sans Display` ExtraBold paths from `AST-B01-03`. They are set on one line with a `14.48` unit word space and scaled uniformly by `1.05048` (no stretching). This gives a `39.00` unit cap height, centered on the symbol.
* **Divider:** It has the same `4 × 152` geometry as `AST-B01-03`. It uses `#CBD5E1` in full color, `#FFFFFF` at `40%` in reversed white, and solid `#000000` in black.
* **Black symbol:** `AST-B01-08` is `AST-B01-02` with its fill changed from `#FFFFFF` to `#000000`. It has no other change.
* **PNG derivatives:** Each `PNG` is rendered directly from its `SVG` master at `4×` scale with an `RGBA` transparent background. It is saved losslessly with `300` dots per inch (`DPI`) metadata.

## 3. Section 6 Verification (`B01 (v2.0.1)`)

| Check ID | Status | Measured Evidence |
| :--- | :--- | :--- |
| `B01-C1` | Pass | All twelve files are in `02_Assets/` and registered in `B01` Section 7 and `Library-Index.md` Section 5, pinned to `B01 (v2.0)`. Each `PNG` decodes to pixels identical to a fresh render of its `SVG` master (`8/8` lossless matches). |
| `B01-C2` | Pass | The Primary Master Lockup has no Endorsement Line, as `§5.2.1` requires for navigation and product headers. No `Tier 0` or `Tier 3` marks are introduced. |
| `B01-C3` | Pass | The lockup canvas ends exactly at the artwork bounds: the symbol spans `x 0`–`160` and the wordmark spans `x 229.66`–`800.00`. The required `40` unit Clear Space (`0.25 × 160`) is therefore applied outside the file and is not reduced by internal padding. |
| `B01-C4` | Pass | The lockup is `800 × 160` (`5:1`). At the `140 px` minimum, the symbol renders at `28.0 px` and the wordmark cap height at `6.83 px`, which matches `§5.3.2`. The `PNG` sizes at `300 DPI` are: symbols `1080 px` (`91.4 mm`); Parent-Endorsed Lockup `2656 px` (`224.9 mm`); Primary Master Lockup `3200 px` (`270.9 mm`). Each exceeds its print minimum. |
| `B01-C5` | Pass | Every hex value in the new `SVG` files belongs to the `B02` palette: `#DE0029`, `#074C96`, `#092B55`, `#CBD5E1`, `#FFFFFF`, and `#000000`, with zero values outside the palette. Mark fills measure against white at `14.11:1` (Deep Navy), `8.46:1` (Brand Blue), `5.07:1` (Signal Red), and `21.00:1` (Pure Black). Reversed White measures `14.11:1` on Deep Navy. All exceed `4.5:1`. |
| `B01-C6` | N/A | No `Tier 4` co-branded lockup is introduced. |
| `B01-C7` | Pass | The symbol paths are byte-identical to `AST-B01-01`. The wordmark outlines are reused from `AST-B01-03` with a uniform scale and translation only. No rotation, skew, effects, or new letterforms are introduced. |

## 4. Library Control Checks

| Control Area | Governing Clause | Status | Evidence & Notes |
| :--- | :--- | :--- | :--- |
| **File Naming** | `A02 (v1.3.0) §5.4.1`, `§5.4.3`, `§5.4.5` | Pass | All twelve files follow `CODE_Title-Words.ext` in `ASCII` characters, without version numbers. |
| **Governs Header** | `A01 (v1.2.0) §5.2.8` | Pass | `B01 (v2.0.1)` `Governs` lists `AST-B01-01`–`AST-B01-16`, matching Section 7. |
| **Versioning** | `A01 (v1.2.0) §5.5.6`, `§5.5.7` | Pass | `B01` changes only Section 7 and its header (`ERRATA`, `v2.0.1`, no archive snapshot). `Library-Index.md` is a routine registration (`ERRATA`, `v1.2.16`). |
| **Register Sync** | `A01 (v1.2.0) §5.8.1`, `A04 (v1.1.1) §5.5.2` | Pass | `B01`, `AST-B01-05`–`AST-B01-16`, and `REC-A04-008` were synced in `Library-Index.md (v1.2.16)` on `2026-11-27`. |

## 5. Non-Conformity Register (`A04 (v1.1.1) §5.2.2`)

None. Zero non-conformities were found.

> **Informative Note:** These items remain outside this gate and are tracked for later work. First, the `B01` informative note and `B05 §5.1.3` call for a simplified `16 px` favicon derivative, which needs new design work. Second, `PUB-01`–`PUB-03` still list only `AST-B01-01`–`AST-B01-04`. An `ERRATA` revision of `B01` does not require them to be resynced (`A01 §5.5.5`).

## 6. Closure Verification (`A04 (v1.1.1) §5.2.3`)

* **Approver Sign-Off Date:** `2026-11-27`
* **Approver:** Hary Irfantri
* **Objective Closure Evidence:** The Approver reviewed and approved the rendered design sheet for `AST-B01-05`–`AST-B01-08` on `2026-11-27`. All applicable `B01` Section 6 checks pass with the measured evidence above. This record is transitioned to immutable terminal `Closed` status per `A04 (v1.1.1) §5.5.3`.
