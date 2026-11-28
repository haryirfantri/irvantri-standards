# Library checks

`library_checks.py` measures the real files in `Unified Operating Library/` and writes a report that governance records can cite as evidence for the Section 6 checks listed below. It reads its rules from the live library where they are written as data: the palette from `B02` Section 5, versions and statuses from `Library-Index.md`, and checksums from `06_Dependencies/Dependencies-Manifest.md`.

## Run it

```sh
pip install -r tools/requirements.txt
python3 tools/library_checks.py --report-dir check-report
```

It writes `check-report/check-report.json` (every measurement) and `check-report/check-report.md` (summary), and exits with status `1` if any finding fails and is not listed in `known-issues.json`.

The GitHub Actions workflow `.github/workflows/library-checks.yml` runs the same command on every pull request and every push to `main`, shows the summary on the run page, and keeps the report as an artifact named `library-check-report-<commit>` for 400 days.

## What it checks

| Check | What is measured | Evidence for |
| :--- | :--- | :--- |
| `register-sync` | Version, status and next-review date in each standard's header against `Library-Index.md`; every registered path exists (except `Planned`); every file in `02_`–`05_` is registered | `A01` header metadata, `A02-C3`, `A02-C5`, `A02-C9` |
| `palette` | Every `#RRGGBB` and `rgb()` value in active `.md`, `.svg`, `.html`, `.json` files is a `B02` value and uppercase (`99_Archive/` skipped) | `B02-C1`, `B02-C2`, `D01-C2` |
| `token-parity` | `AST-D01-01` colours, `RGB` and `CMYK` against `B02`; every reference resolves; JSON embedded in HTML equals the master; `--is-` custom properties equal their token values | `D01-C2`, `D01-C3`, `B02-C1` |
| `contrast` | WCAG 2.2 ratios for the pairings in `contrast-pairs.json`, plus ratios quoted in library text checked against the maths | `B02-C5`, `D01-C2`, `D04-C1`, `D04-C2` |
| `links` | Relative links in Markdown, HTML and SVG, and backticked library paths in the register and manifest (revision history skipped) | `A02-C5`, `A02-C7`, `E01-C3` |
| `pdf-preflight` | Print: `PDF/X-4` in Info and XMP, one `FOGRA39` CMYK OutputIntent, A4 trim, 3 mm bleed, embedded fonts, CMYK-only operators on `B02` builds, total ink ≤ 300%, no undefined font resources. Digital: exact A4, no bleed, embedded fonts, `sRGB` values on the `B02` palette | `E03-C1`, `E03-C3`, `E03-C4`, `E01-C4` |
| `press-export` | Runs `press_export.py` on each `fixtures/*press-layout.pdf` sample and preflights the `PDF/X-4` result: A4 trim, 3 mm bleed, `FOGRA39`, only `B02` CMYK builds, total ink ≤ 300%, embedded fonts | `E01-C3`, `E03-C1`, `E03-C3`, `E03-C4` |
| `html-master` | For every registered `HTML` template: literal colours in style rules, free-text fields without a declared character limit, `Save filled copy` and unsaved-changes warning, `Press preview` beside a press export, remote requests, fonts and script libraries embedded byte-identical to `06_Dependencies/` (SHA-256), an `ARIA` Live Region, and that `TPL-E01-06` equals a fresh build from `tools/document-master/`. Enforced only for templates pinned to `E01 (v2.5)` / `E04 (v2.3)` or later; earlier pins are measured but never fail (`E01 §5.5.1`) | `E01-C5`, `E04-C4`, `D04-C3` |
| `dependencies` | SHA-256 and byte size of every font, ICC profile and script library against the manifest; no unlisted binaries or scripts; each font folder carries the full OFL-1.1 text and each script folder its MIT `LICENSE`, with a copyright line | `B03-C2`, `A02-C10`, `E03-C4` |

The PDF check is a structural preflight. It is not a certified `PDF/X` validation, so a press proof or a commercial preflight tool remains the final word for print (`E03 §5.4.3`).

Checks that need a person (layout, tone, visual misuse) are not covered and still need review against each standard's Section 6.

## Press export (`E01 §5.3.4`)

An `HTML` authoring master such as `TPL-E01-03` makes press files in two steps:

1. Fill in the cover, set it to `Approved`, and press **Export press PDF**. Save the result as a PDF from the browser print dialog with margins set to none. You get a `230 × 317 mm` sheet in sRGB with the A4 trim, a 3 mm bleed, and crop marks.
2. Run the converter on that file:

```sh
pip install -r tools/requirements.txt
python3 tools/press_export.py cover-press.pdf --title "Document title"
```

It writes `cover-press_PDFX4.pdf`. Each sRGB colour is swapped for its fixed `B02 §5.1.1` or `§5.6.1` CMYK build from a lookup table, never an ICC conversion. The tool sets the trim and bleed boxes, attaches the ISO Coated v2 / `FOGRA39` output intent from `06_Dependencies/Color-Profiles/`, writes `PDF/X-4` metadata, and runs the same preflight as `pdf-preflight`. It stops with an error on any colour that has no fixed build, on raster images, and on a page that is not the press sheet. An Owner colour proof is still needed before any press run (`E03 §5.4.3`).

The samples in `fixtures/` are press layouts saved by Chromium: a blank `TPL-E01-03` cover and the `TPL-E01-06` sample document. If you change either layout, save a fresh sample so the `press-export` check keeps measuring the current layout.

`press_export.py` reads the document title and Owner from a `TPL-E01-06` cover for the PDF metadata; `--title` and `--author` override them.

## Formal Document Master (`TPL-E01-06`)

`03_Templates/TPL-E01-06_Formal-Document-Master.html` is generated. Edit the sources in `tools/document-master/` (`master.src.html`, `app.js`, `authoring-flow.svg`) and rebuild:

```sh
python3 tools/build_document_master.py          # writes the template
python3 tools/build_document_master.py --check  # exit 1 if the committed file is stale
```

The build embeds the fonts from `06_Dependencies/Fonts/` and the script libraries from `06_Dependencies/Scripts/` byte-identical, so the `html-master` check can compare them with the manifest.

After **Export A4 PDF**, finish the digital file so every browser's output carries the same properties (`E05 §5.9.2`):

```sh
python3 tools/pdf_finish.py "REF-001 Title v1.0.0.pdf"
```

It sets the title and author from the cover title and Owner, sets the language to `en-US`, and keeps the browser's bookmarks, or rebuilds them from the Contents page when the browser wrote none.

## Changing the rules

- **Contrast pairings** live in `contrast-pairs.json`, each with the clause it comes from. `pairs` must pass their minimum; `informative` pairs are measured but never fail; `stated_ratios` fail if the quoted text disappears or the maths disagrees.
- **Known issues** live in `known-issues.json`. Each entry names a finding `id` from `check-report.json`, a `reason`, a `reference` (record, waiver or pull request) and a `review_by` date. After that date the entry stops suppressing the finding. An entry that no longer matches anything is listed in the report so it can be removed.

## Citing a run in a record

Cite the commit, the run URL and the check ID, for example: "`contrast` passed, 39 pairings, minimum 4.52:1 (library checks run `<url>`, commit `<sha>`)". The JSON report holds every measured number.
