# REC-A04-011 — B01 v2.1.0 Favicon & App Icon Pre-Release Gate

| Field | Value |
| :--- | :--- |
| **Code** | `REC-A04-011` |
| **Record Type** | Pre-Release Gate |
| **Date** | `2026-11-27` |
| **Status** | `Closed` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Related Standards** | `A01 (v1.2.0)`, `A02 (v1.3.0)`, `A04 (v1.2.0)`, `B01 (v2.1.0)`, `B02 (v1.3.0)`, `B05 (v1.1.0)`, `C01 (v1.1.1)`, `Library-Index.md (v1.2.21)` |
| **Expiry Date** | `None` |

## 1. Review Scope & Trigger

This Governance Record (`REC-`) documents the Pre-Release Gate (`A04 (v1.2.0) §5.1.2`, `§5.1.5`) for the items below, released together with `Library-Index.md (v1.2.21)`:

| Item | Change | Version Gated |
| :--- | :--- | :--- |
| `B01` | `MINOR`: new `5.1.4`, `5.1.5`, `5.3.4`–`5.3.6`, `5.4.4`, `5.6.2`, and `B01-C8` | `v2.1.0` |
| `AST-B01-17`, `AST-B01-18` | New Small-Format Symbol in full color (dark-mode adaptive) and Reversed White | `B01 (v2.1)` |
| `AST-B01-19` | New favicon with `16`, `32`, and `48 px` frames | `B01 (v2.1)` |
| `AST-B01-20`–`AST-B01-23` | New App Icon Tile master and its `180`, `192`, and `512 px` exports | `B01 (v2.1)` |

The trigger is the gap noted in `REC-A04-008`: no registered mark existed for `16 px` favicons. At `16 px` the Primary Symbol's strokes measure `1.23 px` (ring and diagonals) and `0.74 px` (stubs), and the zigzag no longer reads. `B01 (v2.0.1) §5.6.1` forbade redrawing the symbol or framing it, so a `MINOR` revision was needed before any small-format mark or app tile could be released.

The Approver reviewed three candidates on a rendered sheet (`16`, `32`, and `48 px` and app icon sizes, light and dark) and chose candidate C ("Hinted") on `2026-11-27`.

## 2. Method

Every result below was measured on the delivered file on branch `claude/project-thread-pgj5r3`, based on `main` at `9f17fab`.

* **Geometry:** Shapely `2.2.0` parsed the `AST-B01-17` path data into polygons and measured stroke widths, the gap between the two colors, and 180° rotational symmetry.
* **Rendering:** headless Chromium `158.0.8127.36` (Playwright `1.63.0`) rendered each `SVG` at exact pixel size with `colorScheme: light`, and again with `colorScheme: dark` for `AST-B01-17`.
* **Raster comparison:** Pillow `13.0.0` decoded every `ICO` frame and `PNG` and compared it pixel by pixel with a fresh render of its `SVG` master.
* **Contrast:** the `WCAG` 2.2 relative luminance formula, the same maths as `tools/library_checks.py`.
* **Standards text:** a script scanned every added `B01` line for prohibited keywords, first- and second-person pronouns, contractions, and vague qualifiers, and counted sentence length in words.
* **Automated check:** `tools/library_checks.py` (register sync, palette, token parity, contrast, links, `PDF` preflight, and dependencies). This release adds `.ico` to the paths its `links` check resolves.

## 3. Construction

* **Small-Format Symbol:** the Primary Symbol's anatomy (two point-symmetric halves, each a ring arc, a 45° diagonal, and a vertical stub) was rebuilt on a `16 px` grid. The ring and diagonals are `1.5 px` wide, the stubs `1.25 px`, and every gap between the colors `1.0 px`. The red half rotated 180° matches the blue half with zero area difference.
* **Dark mode:** `AST-B01-17` carries one `@media (prefers-color-scheme: dark)` rule that sets both paths to `#FFFFFF` (`B01 §5.4.4`). `AST-B01-18` is the same geometry in fixed `#FFFFFF`.
* **Favicon:** `AST-B01-19` holds three frames. The `16 px` frame is exported from `AST-B01-17`. The `32` and `48 px` frames are exported from `AST-B01-01`, because `B01 §5.3.4` reserves the Small-Format Symbol for renders below `28 px`.
* **App Icon Tile:** `AST-B01-20` is a `512 × 512` **Pure White** square. It holds the two `AST-B01-01` paths unchanged inside a uniform scale of `1.264198` and a translation of `85.333333` units on each axis.

## 4. Section 6 Verification — `B01 (v2.1.0)` Standard

| Check ID | Status | Measured Evidence |
| :--- | :--- | :--- |
| `A01-C2` | Pass | The header has 9 fields in order. Version `v2.1.0`, Status `Approved`, and `ISO` 8601 dates. `Governs` lists `AST-B01-01`–`AST-B01-23`, matching Section 7. |
| `A01-C3` | Pass | Level-2 sections `1`–`8` remain in order. New clauses are numbered `5.1.4`, `5.1.5`, `5.3.4`–`5.3.6`, `5.4.4`, and `5.6.2`. Both new notes use the `> **Informative Note:**` prefix. |
| `A01-C4` | Pass | Added lines contain zero `MUST`, `WILL`, or `REQUIRED`, and zero vague qualifiers. Each new `SHALL` states a measurable value: a pixel range, a stroke or gap width, a media query, a tile color, or a two-thirds width. |
| `A01-C5` | Pass | The release adds clauses and does not change the text of any existing `SHALL` or `SHALL NOT` clause, so it is `MINOR` (`A01 (v1.2.0) §5.5.4`). The Small-Format Symbol is admitted through new `5.1.5`, and the App Icon Tile through new `5.6.2`, which names it an approved frame under the unchanged `5.6.1`. |
| `A01-C6`, `A02-C6` | Pass | `99_Archive/B01_Marks-and-Lockups_v2.0.1.md` has `SHA-256` `87f1776e…73f94cd8`, equal to the outgoing file on `main` at `9f17fab`. |
| `A01-C7` | Pass | `register-sync` compares 22 standard headers with `Library-Index.md (v1.2.21)` and reports zero mismatches. |
| `A01-C8` | Pass | No `MAJOR` increment, so `AST-B01-01`–`AST-B01-16` keep their `B01 (v2.0)` pins and no item moves to `Sync Required`. |
| `C01-C2` | Pass | Zero first- or second-person pronouns and zero contractions in added lines. |
| `C01-C3` | Pass | The longest new normative sentence is `28` words (`5.3.6` and `5.4.4`), within the `30`-word limit of `C01 §5.3.1`. `ICO` is expanded as Windows Icon on first use. |
| Section 5 to 6 mapping | Pass | Every new clause is cited by the new `B01-C8`: `5.1.4`, `5.1.5`, `5.3.4`, `5.3.5`, `5.3.6`, `5.4.4`, and `5.6.2`. |
| Section 3 parity | Pass | The new text cites `B02`, `B05`, and `D02`, all already listed in Section 3. |

## 5. Section 6 Verification — Released Assets

| Item | Check ID | Status | Measured Evidence |
| :--- | :--- | :--- | :--- |
| `AST-B01-17`–`AST-B01-23` | `B01-C1` | Pass | All seven files are in `02_Assets/` and registered in `B01` Section 7 and `Library-Index.md` Section 5, pinned to `B01 (v2.1)`. `register-sync` and `links` resolve every path. |
| `AST-B01-17` | `B01-C8` (`5.3.5`) | Pass | Ring width measured radially at ten angles: `1.471`–`1.516 px`. Diagonal width measured across its parallel edges: `1.500 px`. Stub width between its vertical edges (`x 8.600` and `9.850`): `1.250 px`. Minimum distance between the red and blue shapes: `1.000 px`. |
| `AST-B01-17` | `B01-C5`, `B01-C8` (`5.4.4`) | Pass | Light render: every opaque pixel is `#DE0029` or `#074C96`. Dark render: every opaque pixel is `#FFFFFF`. |
| `AST-B01-19` | `B01-C8` (`5.1.4`, `5.3.4`) | Pass | The file holds exactly `16`, `32`, and `48 px` frames. Each decodes to pixels identical to a fresh render of its master: `16 px` from `AST-B01-17`, `32` and `48 px` from `AST-B01-01` (`3/3` lossless matches). |
| `AST-B01-20` | `B01-C7`, `B01-C8` (`5.6.2`) | Pass | Its two path `d` attributes are byte-identical to `AST-B01-01`, under a uniform scale only. In the `512 px` render the ink spans `x 85`–`425` and `y 85`–`425` (`341 px`, `0.666` of the tile), with margins of `85`–`86 px` against the required `85.25 px` (`0.25 × 341`). All four corner pixels are `#FFFFFF`. |
| `AST-B01-21`–`AST-B01-23` | `B01-C1`, `B01-C8` | Pass | Sizes `180 × 180`, `192 × 192`, and `512 × 512`, each opaque (minimum alpha `255`) and pixel-identical to a fresh render of `AST-B01-20` (`3/3`). The farthest ink is `171.6 px` from the centre of the `512 px` icon, inside the `204.8 px` maskable safe zone. |
| `AST-B01-17`–`AST-B01-23` | `B01-C5` | Pass | Hex values used: `#DE0029`, `#074C96`, and `#FFFFFF`, all on the `B02` palette (`palette` check: zero off-palette values). On the white tile, Brand Blue measures `8.46:1` and Signal Red `5.07:1`. The dark-mode white mark measures `16.10:1` and `12.07:1` on the two dark tab colors of Chromium browsers (`RGB` `32, 33, 36` and `53, 54, 58`). |
| `AST-B01-19` | `B01-C5` (`5.4.4`) | Pass | The `ICO` fallback stays full color as `5.4.4` requires. On the dark `RGB` `53, 54, 58` tab, Brand Blue measures `1.43:1`, which is why `5.4.4` exempts `ICO` fallbacks from `5.4.2` and moves dark-mode support to the `SVG` favicon. |
| All | `B01-C2`, `B01-C4`, `B01-C6` | N/A | No lockup, Endorsement Line, print use, or co-branding is introduced. The `32 px` and larger renders use the Primary Symbol above its `28 px` minimum. |

## 6. Library Control Checks

| Control Area | Governing Clause | Status | Evidence & Notes |
| :--- | :--- | :--- | :--- |
| **File Naming** | `A02 (v1.3.0) §5.4.1`, `§5.4.3`, `§5.4.5` | Pass | All seven files follow `CODE_Title-Words.ext` in `ASCII` characters, without version numbers. |
| **Register Sync** | `A01 (v1.2.0) §5.8.1`, `A04 (v1.2.0) §5.5.2` | Pass | `B01`, `AST-B01-17`–`AST-B01-23`, and `REC-A04-011` were synced in `Library-Index.md (v1.2.21)` on `2026-11-27`. |
| **File Checksums** | `A04 (v1.2.0) §5.1.6` | Pass | `SHA-256` of each released file (first and last 8 hex digits): `AST-B01-17` `7b957d3d…16a16235`; `AST-B01-18` `ea139a65…5319128a`; `AST-B01-19` `d3ab0b4d…420c1440`; `AST-B01-20` `f268132f…c7670f02`; `AST-B01-21` `4ce7e06a…defc652a`; `AST-B01-22` `5d8c60bc…608922f0`; `AST-B01-23` `73872c7d…75befeeb`. |

## 7. Non-Conformity Register (`A04 (v1.2.0) §5.2.2`)

None. Zero non-conformities were found.

> **Informative Note:** These items are outside this gate. First, `PUB-01`–`PUB-03` still cite `B01 (v2.0.0)` in their build manifests. That remains accurate for their compile date, and a `MINOR` revision does not require a resync (`A01 §5.5.4`). The next publication refresh can add the favicon set. Second, no live website uses these files yet. Web pages that adopt them should link `AST-B01-17` as the `SVG` icon, `AST-B01-19` as the fallback, and `AST-B01-21` as the Apple touch icon, and list `AST-B01-22` and `AST-B01-23` in the web app manifest.

## 8. Closure Verification (`A04 (v1.2.0) §5.2.3`, `§5.1.7`)

* **Gate Verdict:** `Pass`. The items in Section 1 are released as listed.
* **Automated Check:** `python3 tools/library_checks.py` gives `PASS` with zero failing findings and zero known issues. Continuous integration (`CI`) run `46058481522` measured commit `a8b8d5a`, which holds every gated change, and passed.
* **Approver Sign-Off:** The Approver chose design C and approved the `B01 (v2.1.0)` revision on `2026-11-27`. Merging the release pull request records sign-off and puts the release into effect.
* **Approver:** Hary Irfantri
