# PUB-03 — Irvantri Standards AI Design System Context (`DESIGN.md`)

| Field | Value |
| :--- | :--- |
| **Code** | `PUB-03` |
| **Title** | Irvantri Standards AI Design System Context |
| **Deployment Filename** | `DESIGN.md` *(for external repositories, Google Stitch, Superdesign, and coding agents)* |
| **Entity** | Irvantri Standards (`Irvantri Standards Pte. Ltd.`) |
| **Affiliation** | A member of Irvantri Group |
| **Version** | `v1.0.0` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-26` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Source Standards** | `A01 (v1.2.0)`, `A02 (v1.3.0)`, `A03 (v1.1.1)`, `A04 (v1.1.1)`, `B01 (v2.0.0)`, `B02 (v1.1.1)`, `B03 (v2.0.0)`, `B04 (v1.2.0)`, `B05 (v1.1.0)`, `C01 (v1.1.1)`, `C02 (v1.1.0)`, `C04 (v1.0.1)`, `D01 (v1.0.3)`, `D02 (v2.0.1)`, `D03 (v2.0.0)`, `D04 (v1.2.1)`, `E01 (v2.1.1)`, `E02 (v1.1.0)`, `E04 (v2.1.1)` |

---

> **Precedence Notice (`A01 §5.1.4`, `§5.7.5`):** This compiled publication (`PUB-03`) is an informative Artificial Intelligence (`AI`) design and authoring context compiled on `2026-11-26` from the **Irvantri Standards Unified Operating Library** (`Library-Index.md v1.2.9`). Active normative standards (`A01`–`E04`) and `02_Assets/AST-D01-01_Design-Tokens.json` prevail in the event of any conflict between this publication and an underlying standard.

> **External Tool Deployment Note (`A02 §5.4.1`):** Inside the Unified Operating Library, this controlled publication resides at `04_Publications/PUB-03_AI-Design-System-Context.md`. When deploying into external software repositories, Google Stitch, Superdesign, or HyperText Markup Language (`HTML`) and Cascading Style Sheets (`CSS`) to Portable Document Format (`PDF`) workspaces, export or copy this file verbatim as `DESIGN.md` at the target project root.

---

## 1. Visual Theme & Aesthetic Direction

The **Irvantri Standards Design System** (`C02 §5.3.2`) follows disciplined Swiss-editorial institutional minimalism built on generous negative space, crisp typographic hierarchy, and deterministic geometric alignment.

* **Core Brand Pillars:** `Integrity` · `Precision` · `Reliability` · `Progress`
* **Proportional Color Balance (`B02 §5.4.1`, `E04 §5.2.4`):**
  * **`75%` Neutral Surfaces:** Pure White (`#FFFFFF`) primary canvas and Canvas Subtle (`#F8FAFC`) secondary washes.
  * **`20%` Institutional Blue & Navy:** Deep Navy (`#092B55`) structural headers or dark structural slides and Brand Blue (`#074C96`) primary interactive accents.
  * **`5%` Signal Red Accent:** Signal Red (`#DE0029`) strictly reserved for brand marks (`AST-B01`) and signature geometric split accent bars.
* **Minimalist Structural Discipline:**
  * Prefer open whitespace, alignment, and subtle surface washes (`#F8FAFC`, `#EFF6FF`) over heavy bordered boxes or stacked cards.
  * Keep headers, footers, and tables rule-free or horizontal-hairline-only (`#E2E8F0` / `#CBD5E1`) with zero vertical table gridlines.
  * Never place decorative rings, wave textures, gradients, drop shadows with glow, or ornamental motifs on operational work surfaces, data tables, forms, or document interiors (`B04 §5.3.2`, `§5.3.4`).
* **Default Theme (`D01 §5.2.3`):** Light mode (`#FFFFFF` / `#F8FAFC` surfaces with `#0F172A` / `#092B55` ink). Use full-bleed **Deep Navy (`#092B55`)** only for intentional high-contrast structural dividers, hero covers, or closing attribution slides.

---

## 2. Color System (`B02 v1.1.1`, `AST-D01-01`)

All digital Hexadecimal (`HEX`) tokens are written in uppercase with a leading `#` (`B02 §5.1.2`). Red-Green-Blue (`RGB`) values correspond to Standard Red-Green-Blue (`sRGB`) digital output.

### 2.1 Primary Brand Palette

**Table 1.** Primary Brand Palette (`B02 §5.1.1`)

| Role | Name | HEX | RGB | CSS Custom Property | Usage Guidance |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Primary Interactive & Anchor | **Brand Blue** | `#074C96` | `7, 76, 150` | `--is-color-brand-primary` | Primary buttons, links, active states, eyebrow kickers, focus rings, provenance left borders |
| Brand Accent & Split Bar | **Signal Red** | `#DE0029` | `222, 0, 41` | `--is-color-brand-accent` | Brand mark, `24%` split accent bar segment, subtle structural tick; prohibited for body, heading, or badge text (`B02 §5.3.2`) |
| Structural Dark & Headings | **Deep Navy** | `#092B55` | `9, 43, 85` | `--is-color-brand-deep` | Display headings, wordmark, `76%` split accent bar segment, dark section/closing slide canvas |
| Secondary Dark & Hover | **Royal Navy** | `#102F60` | `16, 47, 96` | `--is-color-brand-secondary` | Primary button hover state, secondary dark panels on Deep Navy slides |

### 2.2 Neutral Surface, Border & Ink Scale

**Table 2.** Neutral Surface, Border & Ink Tokens (`B02 §5.2.1`)

| Role | Name | HEX | RGB | CSS Custom Property |
| :--- | :--- | :--- | :--- | :--- |
| Primary Surface | **Pure White** | `#FFFFFF` | `255, 255, 255` | `--is-color-bg-surface` |
| Page Canvas / Subtle Wash | **Canvas Subtle** | `#F8FAFC` | `248, 250, 252` | `--is-color-bg-canvas` |
| Muted Container / Disabled | **Surface Muted** | `#F1F5F9` | `241, 245, 249` | `--is-color-bg-muted` |
| Tinted Callout / Hover Wash | **Surface Tint** | `#EFF6FF` | `239, 246, 255` | `--is-color-bg-tint` |
| Hairline Divider / Table Row | **Border Subtle** | `#E2E8F0` | `226, 232, 240` | `--is-color-border-subtle` |
| Structural Border / Input | **Border Default** | `#CBD5E1` | `203, 213, 225` | `--is-color-border-default` |
| Secondary Copy / Metadata | **Text Muted** | `#5F6C7E` | `95, 108, 126` | `--is-color-text-muted` |
| Primary Body Ink | **Text Primary** | `#0F172A` | `15, 23, 42` | `--is-color-text-primary` |
| High-Contrast Monospace Ink | **Pure Black** | `#000000` | `0, 0, 0` | `--is-color-text-mono` |

### 2.3 Five-State Semantic Status Palette (`B02 §5.3.1`, `E02 §5.2.2`)

Every semantic status indicator pairs color with an explicit `C02` text label and a non-color visual cue (such as a `6 px`–`8 px` solid square marker).

**Table 3.** Semantic Status Palette & Controlled Status Mapping (`B02 §5.3.1`, `C02 §5.4.1`, `E02 §5.2.2`)

| Semantic Role | Controlled `C02` Statuses | Foreground HEX | Surface HEX | Border HEX | CSS Foreground Var |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Informative** | `Planned`, `In Review` | `#074C96` | `#EFF6FF` | `#BFDBFE` | `--is-color-status-informative` |
| **Success** | `Approved` | `#166534` | `#F0FDF4` | `#BBF7D0` | `--is-color-status-success` |
| **Warning** | `Draft`, `Sync Required` | `#92400E` | `#FFFBEB` | `#FDE68A` | `--is-color-status-warning` |
| **Danger** | `Deprecated`, Errors | `#A42332` | `#FEF2F2` | `#FECACA` | `--is-color-status-danger` |
| **Neutral** | Archived / Inactive / Disabled | `#475569` | `#F1F5F9` | `#CBD5E1` | `--is-color-status-neutral` |

### 2.4 Contrast & Accessibility Rules (`B02 §5.5`, `D04`)
* Standard text meets **`≥ 4.5:1`** Web Content Accessibility Guidelines (`WCAG`) 2.2 Level AA contrast (`#0F172A` on `#FFFFFF` = `17.85:1`; `#5F6C7E` on `#FFFFFF` = `5.34:1`; `#092B55` on `#FFFFFF` = `14.18:1`).
* Large display headings (`≥ 24 px` regular or `≥ 18.66 px` bold) and User Interface (`UI`) component borders or icons meet **`≥ 3:1`** contrast.
* Raw **Signal Red (`#DE0029`)** is prohibited for text or badge labels; use **Danger Foreground (`#A42332`)** for error and deprecated text (`B02 §5.3.2`).

---

## 3. Typography (`B03 v2.0.0`)

Use exclusively the unified **`SIL OFL-1.1` Noto Sans superfamily** logged in `06_Dependencies/Dependencies-Manifest.md`. Never substitute decorative, serif, or unapproved fonts (`B03 §5.4.1`).

### 3.1 Google Fonts Import & Fallback Stacks
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Display:wght@400;600;700;800&family=Noto+Sans+Mono:wght@400;500;700&family=Noto+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
```

* **Display Typeface (`--is-font-family-display`):** `'Noto Sans Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Liberation Sans', Arial, sans-serif` *(keep strictly upright; do not italicize Display headings)*
* **Text Typeface (`--is-font-family-text`):** `'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Liberation Sans', Arial, sans-serif`
* **Monospace Typeface (`--is-font-family-mono`):** `'Noto Sans Mono', 'Liberation Mono', 'DejaVu Sans Mono', monospace`

### 3.2 Role-Based Type Hierarchy (`B03 §5.2.6`, `E04 §5.2.3`)

**Table 4.** Role-Based Typographic Scale Across Web, Documents & Pitch Decks

| Role | Typeface | Web / UI Size (Desktop / Mobile) | Pitch Deck (`1920 × 1080`) | Weight | Tracking | Line Height |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Cover / Hero Title** | `Noto Sans Display` | `40 px`–`48 px` / `28 px` | `56 px`–`72 px` | `800` | `-0.03em` | `1.12`–`1.18` |
| **Page / Slide Title** | `Noto Sans Display` | `32 px` / `24 px` | `36 px`–`44 px` | `700`–`800` | `-0.03em` | `1.15`–`1.20` |
| **Metric / Key Performance Indicator (`KPI`) Value** | `Noto Sans Display` | `28 px` / `24 px` | `56 px`–`72 px` | `700`–`800` | `-0.04em` | `1.05`–`1.15` |
| **Section Title** | `Noto Sans Display` | `20 px` / `18 px` | `24 px`–`28 px` | `700`–`800` | `-0.03em` | `1.20` |
| **Panel Title** | `Noto Sans Display` | `16 px` / `16 px` | `20 px`–`22 px` | `700` | `-0.02em` | `1.25` |
| **Body Copy (Docs & Decks)** | `Noto Sans` | `16 px` (`12 pt` long-form) | `≥ 22 px` (`≥ 16 pt` min) | `400`–`500` | `0` | `1.45`–`1.55` |
| **Body Copy (UI & Tables)** | `Noto Sans` | `14 px` (`10.5 pt` min) | `≥ 22 px` (`≥ 16 pt` min) | `400`–`600` | `0` | `1.40`–`1.50` |
| **Eyebrow / Overline** | `Noto Sans` | `12 px` (uppercase) | `14 px`–`16 px` (uppercase) | `700`–`800` | `+0.12em` | `1.20` |
| **Codes, Versions, Dates** | `Noto Sans Mono` | `13 px`–`14 px` | `16 px`–`22 px` | `500`–`700` | `0` | `1.40` |

### 3.3 Typographic Guardrails
* **Tabular Numerals (`B03 §5.3.1`):** Apply `font-variant-numeric: tabular-nums;` to every `KPI` readout, table column, metric card, and version register.
* **Measure (`B03 §5.2.4`):** Keep long-form prose between `50` and `85` characters per line (`max-width: 72ch` recommended).
* **Uppercase Restraint (`B03 §5.2.7`):** Restrict ALL CAPS strictly to short eyebrows, table column headers, library codes, and brand wordmarks rather than multi-sentence prose.

---

## 4. Spacing, Grids, Radii, Elevation & Graphic Devices (`B04 v1.2.0`, `D02`, `D04`)

* **Spatial Base Unit (`B04 §5.1.1`–`§5.1.2`):**
  * **Digital / Web / Slides:** `4 px` Base Unit (`4`, `8`, `12`, `16`, `20`, `24`, `32`, `44`, `48`, `64 px`).
  * **Formal A4 Documents:** `4 mm` Base Unit (`8`, `12`, `16`, `20`, `24 mm`; Safe Margins `≥ 16 mm` T/B, `20 mm` L/R).
* **Responsive Breakpoints (`D02 §5.1.1`):**
  * `Reflow Minimum:` `320 px` (zero horizontal scrolling)
  * `Compact:` `320 px` – `767 px` (tables convert to stacked cards; touch target separation `≥ 12 px`)
  * `Medium:` `768 px` – `1279 px`
  * `Expanded:` `≥ 1280 px` (`1440 px` standard content max-width)
* **Corner Radii (`B04 §5.2.1`–`§5.2.2` — Strictly Four Increments):**
  * `0 px` (`--is-radius-none`): Architectural frames, split accent bars, sharp rules
  * `4 px` (`--is-radius-sm`): Buttons, text inputs, status badges, compact tags
  * `8 px` (`--is-radius-md`): Panels, cards, callout boxes, non-approved status banners
  * `12 px` (`--is-radius-lg`): Hero feature containers
  * *Prohibited:* Pill-shaped (`9999 px`) badges/buttons or ad-hoc border radii.
* **Elevation & Focus (`B04 §5.2.3`, `D04 §5.2.4`):**
  * Card shadow (`--is-shadow-card`): `0 2px 8px rgba(15, 23, 42, 0.06)`
  * Action shadow (`--is-shadow-action`): `0 2px 6px rgba(15, 23, 42, 0.12)`
  * Focus indicator: `outline: 3px solid #074C96; outline-offset: 3px;`
  * Interactive touch targets: `min-width: 44px; min-height: 44px;`
* **Signature Split Accent Bar (`B04 §5.3.1`):**
  * Exact **`24%` Signal Red (`#DE0029`)** and **`76%` Deep Navy (`#092B55`)**.
  * **Horizontal top bar:** `2 mm` (A4 `PDF`) or `4 px`–`8 px` (web/slides) full-width across the top edge (`24%` red left, `76%` navy right).
  * **Vertical left-spine bar (formal covers):** `4 mm` (A4 `PDF`) or `12 px`–`16 px` (slides) along the left edge (`76%` Deep Navy upper, `24%` Signal Red lower).

---

## 5. Brand Marks & Legal Attribution (`B01 v2.0.0`, `A03 v1.1.1`)

Always source brand artwork verbatim from the approved `02_Assets/` Scalable Vector Graphics (`SVG`) masters—never redraw or re-typeset the lockup (`B01 §5.1.2`).

**Table 5.** Approved Brand Mark Masters & Minimum Dimensions (`B01 §5.3.2`)

| Asset Code | Variant | Surface | Aspect Ratio | Minimum Size (Digital / Print) |
| :--- | :--- | :--- | :--- | :--- |
| `AST-B01-01` | Primary Symbol (`#074C96` & `#DE0029`) | Light (`#FFFFFF`, `#F8FAFC`) | `1:1` | `28 px` / `12 mm` |
| `AST-B01-02` | White Symbol (`#FFFFFF`) | Dark (`#092B55`, `#102F60`) | `1:1` | `28 px` / `12 mm` |
| `AST-B01-03` | Parent-Endorsed Lockup (Full Color, Curve-Outlined) | Light (`#FFFFFF`, `#F8FAFC`) | `4.15:1` (`664 × 160`) | `260 px` / `64 mm` |
| `AST-B01-04` | Parent-Endorsed Lockup (Reversed White, Curve-Outlined) | Dark (`#092B55`, `#102F60`) | `4.15:1` (`664 × 160`) | `260 px` / `64 mm` |

* **Clear Space (`B01 §5.3.1`):** Keep at least `0.25×` Primary Symbol width completely unobstructed on all four sides around every mark or lockup.
* **Mandatory Legal Strings (`A03 §5.2.1`, `§5.3.3`, `§5.6.1`):**
  * Operating Entity: `Irvantri Standards Pte. Ltd.`
  * Endorsement Line (verbatim): `A member of Irvantri Group`
  * Copyright Footer: `© [YYYY] Irvantri Standards Pte. Ltd. All rights reserved.`

---

## 6. Component Patterns (`D03 v2.0.0`, `B05 v1.1.0`, `E02 v1.1.0`)

* **Primary Button:** Background `#074C96` (hover `#102F60`), text `#FFFFFF` (`Noto Sans` `600`, `14 px`), radius `4 px`, min-height `44 px`, horizontal padding `16 px`–`20 px`.
* **Secondary Button:** Background `#FFFFFF` (hover `#EFF6FF`), border `1px solid #CBD5E1`, text `#092B55`, radius `4 px`, min-height `44 px`.
* **Status Badge (`E02 §5.2.2`):** Radius `4 px`, `1px` semantic border, semantic tint fill, `6 px` solid square cue (`border-radius: 0`), exact Title Case `C02` string (`Approved`, `In Review`, `Draft`, `Planned`, `Sync Required`, `Deprecated`) in `Noto Sans Bold`.
* **Provenance / Governance Callout (`D03 §5.4.3`):** Background `#EFF6FF`, `4 px` left border `#074C96`, optional `1px` outer border `#BFDBFE` or borderless wash, radius `8 px`, padding `16 px 20 px`.
* **Minimalist Data Table:** Zero vertical gridlines, zero outer box borders; header row `#F8FAFC` with `#092B55` bold text and `2px solid #092B55` bottom border; body rows `#FFFFFF` with `1px solid #E2E8F0` bottom hairline; tabular numerals on numeric columns; never leave cells blank (`None` or `—`).
* **Icons (`B05 §5.1`):** Simple geometric line icons on a `24 px` grid (`16 px` / `20 px` / `24 px` sizes), `1.5 px` or `2 px` uniform stroke width, zero multi-color fills; motion transitions `≤ 300 ms` with `prefers-reduced-motion` support.

---

## 7. Verbal Tone, Data Formatting & Approved Boilerplates (`C01`, `C04`)

* **Language & Posture (`C01 §5.1`–`§5.6`):** United States English (`en-US`), objective, verifiable, zero slang, zero promotional superlatives (`world-class`, `best-in-class`, `revolutionary`, `cutting-edge`, `seamless`, `unmatched` are prohibited). Avoid contractions in formal documents, letters, and pitch decks.
* **Dates & Units (`C04`):** International Organization for Standardization (`ISO`) 8601 calendar dates (`YYYY-MM-DD`), uppercase `ISO` 4217 currency codes (`SGD 1,200`, never bare `$`), spaced units (`20 mm`, `16 px`, `300 DPI`), and explicit `None` or `—` for empty values.
* **Verbatim Approved Boilerplates (`C01 §5.5.1`):**

```text
One-Line Descriptor:
Irvantri Standards develops disciplined operating frameworks, technical standards, and structured systems that turn complex organizational requirements into clear, verifiable execution. A member of Irvantri Group.
```

```text
Short Corporate Description:
Irvantri Standards (Irvantri Standards Pte. Ltd.) builds practical operating standards, governance frameworks, and structured digital and documentation systems. Focused on clarity, traceability, and repeatable execution, Irvantri Standards helps organizations replace ad-hoc work with durable, auditable baselines. A member of Irvantri Group.
```

---

## 8. HTML/CSS-to-PDF Print & Pitch Deck Shells (`E01 §5.4`, `E04 §5.2`)

When moving `HTML` exported from **Google Stitch** or **Superdesign** into `PDF` production (via headless Chromium / Playwright or WeasyPrint), wrap the markup in the matching `@page` shell below.

### 8.1 Formal A4 Digital Distribution PDF (`E01 §5.4`)
```css
@page {
  size: 210mm 297mm; /* Exact A4 trim; zero bleed/crops for digital sRGB PDF */
  margin: 16mm 20mm 16mm 20mm; /* 4 mm Base Unit Safe Margins */
}
@page :first {
  margin: 16mm 20mm 16mm 24mm; /* 24 mm inner spine margin for formal covers */
}
html, body {
  margin: 0;
  padding: 0;
  background: #FFFFFF;
  color: #0F172A;
  font-family: var(--is-font-family-text);
  font-size: 10.5pt;
  line-height: 1.5;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
table, figure, .callout { break-inside: avoid; }
h1, h2, h3 { font-family: var(--is-font-family-display); color: #092B55; break-after: avoid; }
```

### 8.2 Concise `16:9` Pitch Deck PDF (`E04 §5.2`)
```css
@page {
  size: 1920px 1080px; /* Exact 16:9 widescreen, 4 px Base Unit */
  margin: 0;
}
.slide {
  position: relative;
  width: 1920px;
  height: 1080px;
  overflow: hidden;
  break-after: page;
  page-break-after: always;
  background: #FFFFFF;
  color: #0F172A;
  font-family: var(--is-font-family-text);
  font-size: 22px; /* >= 16 pt minimum body copy (E04 §5.2.3) */
}
.slide--dark {
  background: #092B55;
  color: #FFFFFF;
}
```

---

## 9. Copy-Paste `:root` CSS Token Sheet (`AST-D01-01`)

Derived verbatim from the single-source JavaScript Object Notation (`JSON`) schema `02_Assets/AST-D01-01_Design-Tokens.json` (`D01 §5.3.1`).

```css
:root {
  /* Brand & Structural Colors */
  --is-color-brand-primary: #074C96;
  --is-color-brand-accent: #DE0029;
  --is-color-brand-deep: #092B55;
  --is-color-brand-secondary: #102F60;

  /* Neutral Surfaces, Borders & Ink */
  --is-color-bg-surface: #FFFFFF;
  --is-color-bg-canvas: #F8FAFC;
  --is-color-bg-muted: #F1F5F9;
  --is-color-bg-tint: #EFF6FF;
  --is-color-border-subtle: #E2E8F0;
  --is-color-border-default: #CBD5E1;
  --is-color-text-primary: #0F172A;
  --is-color-text-muted: #5F6C7E;
  --is-color-text-inverse: #FFFFFF;
  --is-color-text-mono: #000000;

  /* Semantic Status Tokens */
  --is-color-status-informative: #074C96;
  --is-color-status-informative-bg: #EFF6FF;
  --is-color-status-informative-border: #BFDBFE;
  --is-color-status-success: #166534;
  --is-color-status-success-bg: #F0FDF4;
  --is-color-status-success-border: #BBF7D0;
  --is-color-status-warning: #92400E;
  --is-color-status-warning-bg: #FFFBEB;
  --is-color-status-warning-border: #FDE68A;
  --is-color-status-danger: #A42332;
  --is-color-status-danger-bg: #FEF2F2;
  --is-color-status-danger-border: #FECACA;
  --is-color-status-neutral: #475569;
  --is-color-status-neutral-bg: #F1F5F9;
  --is-color-status-neutral-border: #CBD5E1;

  /* Typography */
  --is-font-family-display: 'Noto Sans Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Liberation Sans', Arial, sans-serif;
  --is-font-family-text: 'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Liberation Sans', Arial, sans-serif;
  --is-font-family-mono: 'Noto Sans Mono', 'Liberation Mono', 'DejaVu Sans Mono', monospace;
  --is-font-size-eyebrow: 12px;
  --is-font-size-body-ui: 14px;
  --is-font-size-body-doc: 16px;
  --is-font-size-panel-title: 16px;
  --is-font-size-section-title: 20px;
  --is-font-size-page-title: 32px;
  --is-font-line-height-heading: 1.2;
  --is-font-line-height-body: 1.5;

  /* Spacing (4 px Base Unit) */
  --is-space-1: 4px;
  --is-space-2: 8px;
  --is-space-3: 12px;
  --is-space-4: 16px;
  --is-space-5: 20px;
  --is-space-6: 24px;
  --is-space-8: 32px;
  --is-space-11: 44px;
  --is-space-12: 48px;
  --is-space-16: 64px;

  /* Radii, Shadows & Focus */
  --is-radius-none: 0px;
  --is-radius-sm: 4px;
  --is-radius-md: 8px;
  --is-radius-lg: 12px;
  --is-shadow-card: 0 2px 8px rgba(15, 23, 42, 0.06);
  --is-shadow-action: 0 2px 6px rgba(15, 23, 42, 0.12);
  --is-focus-ring-width: 3px;
  --is-focus-ring-offset: 3px;
  --is-focus-ring-color: #074C96;
}
```

---

## 10. Strict Prohibitions ("Never Do" Rules for AI Agents)

1. **Never use unapproved fonts** (no serif, script, or retired fonts); lock strictly to `Noto Sans Display` (upright), `Noto Sans`, and `Noto Sans Mono`.
2. **Never use `#DE0029` (Signal Red) for text, links, or badge copy**; use `#A42332` for error or danger text and reserve `#DE0029` for brand marks and split accent bars (`≤ 5%` of area).
3. **Never use rounded pill badges (`border-radius: 9999px`)**, neon glows, glassmorphism, or multi-stop gradients.
4. **Never leave table cells blank** (use `None` or `—`) or omit `tabular-nums` on multi-row numeric columns.
5. **Never distort, recolor, or crowd `AST-B01` marks** below their minimum sizes (`260 px`/`64 mm` lockup, `28 px`/`12 mm` symbol) or inside `0.25×` Clear Space.
6. **Never invent informal status labels** (such as *WIP*, *Final*, *Done*, or *Archived* instead of exact `C02` strings) or display internal project codenames on external screens or decks.
7. **Never use promotional hyperbole or contractions** in formal documents or pitch decks, and never bind `Irvantri Group Pte. Ltd.` in place of `Irvantri Standards Pte. Ltd.`.

---

## 11. Publication Build Manifest & Revision History (`A01 §5.7.5`, `E02 §5.1.3`)

### 11.1 Source Manifest (`A01 §5.7.5`)

**Table 6.** Publication Build Manifest — `PUB-03` (Compiled `2026-11-26`)

| Series / Layer | Source Items and Exact Versions | Status |
| :--- | :--- | :--- |
| **Master Registers & Assets** | `Library-Index.md (v1.2.9)`, `Dependencies-Manifest.md (v2.0.0)`, `AST-B01-01`–`AST-B01-04` (`B01 (v2.0)`), `AST-D01-01` (`D01 (v1.0)`) | `Approved` |
| **Series A — Governance** | `A01 (v1.2.0)`, `A02 (v1.3.0)`, `A03 (v1.1.1)`, `A04 (v1.1.1)` | `Approved` |
| **Series B — Visual Foundations** | `B01 (v2.0.0)`, `B02 (v1.1.1)`, `B03 (v2.0.0)`, `B04 (v1.2.0)`, `B05 (v1.1.0)` | `Approved` |
| **Series C — Verbal Standards** | `C01 (v1.1.1)`, `C02 (v1.1.0)`, `C04 (v1.0.1)` | `Approved` |
| **Series D — Digital Systems** | `D01 (v1.0.3)`, `D02 (v2.0.1)`, `D03 (v2.0.0)`, `D04 (v1.2.1)` | `Approved` |
| **Series E — Documents & Print** | `E01 (v2.1.1)`, `E02 (v1.1.0)`, `E04 (v2.1.1)` | `Approved` |

### 11.2 Revision History (`E02 §5.1.3`)

**Table 7.** Revision History — `PUB-03`

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v1.0.0` | `2026-11-26` | Major | Initial approved baseline of `PUB-03` (Irvantri Standards AI Design System Context, external deployment filename `DESIGN.md`), synthesizing live `Approved` Series `A`–`E` standards and `AST-D01-01` tokens for Google Stitch, Superdesign, HTML/CSS-to-PDF pipelines, and coding agents. | Hary Irfantri |

---

© 2026 Irvantri Standards Pte. Ltd. All rights reserved. | A member of Irvantri Group
