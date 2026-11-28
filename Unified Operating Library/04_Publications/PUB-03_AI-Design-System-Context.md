---
version: "alpha"
name: "Irvantri Standards Design System"
description: "Swiss-editorial institutional minimalism for Irvantri Standards Pte. Ltd. Built on generous pure-white negative space, disciplined 75/20/5 neutral-navy-red balance, upright Noto Sans Display and Noto Sans typography, deterministic 4px/4mm grids, restrained 0/4/8/12px radii, and horizontal-hairline-only tables."
colors:
  primary: "#074C96"
  on-primary: "#FFFFFF"
  primary-hover: "#102F60"
  secondary: "#092B55"
  on-secondary: "#FFFFFF"
  accent: "#DE0029"
  surface: "#FFFFFF"
  canvas: "#F8FAFC"
  surface-muted: "#F1F5F9"
  surface-tint: "#EFF6FF"
  border-subtle: "#E2E8F0"
  border-default: "#CBD5E1"
  border-strong: "#64748B"
  on-surface: "#0F172A"
  on-surface-muted: "#5F6C7E"
  ink-mono: "#000000"
  info: "#074C96"
  info-bg: "#EFF6FF"
  info-border: "#BFDBFE"
  success: "#166534"
  success-bg: "#F0FDF4"
  success-border: "#BBF7D0"
  warning: "#92400E"
  warning-bg: "#FFFBEB"
  warning-border: "#FDE68A"
  error: "#A42332"
  error-bg: "#FEF2F2"
  error-border: "#FECACA"
  neutral: "#475569"
  neutral-bg: "#F1F5F9"
  neutral-border: "#CBD5E1"
typography:
  slide-title:
    fontFamily: "Noto Sans Display"
    fontSize: "64px"
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: "-0.03em"
  slide-heading:
    fontFamily: "Noto Sans Display"
    fontSize: "40px"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.03em"
  headline-lg:
    fontFamily: "Noto Sans Display"
    fontSize: "32px"
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: "-0.03em"
  headline-kpi:
    fontFamily: "Noto Sans Display"
    fontSize: "28px"
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: "-0.04em"
  headline-md:
    fontFamily: "Noto Sans Display"
    fontSize: "20px"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.03em"
  headline-sm:
    fontFamily: "Noto Sans Display"
    fontSize: "16px"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  body-lg:
    fontFamily: "Noto Sans"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0em"
  body-md:
    fontFamily: "Noto Sans"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0em"
  body-slide:
    fontFamily: "Noto Sans"
    fontSize: "24px"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0em"
  label-lg:
    fontFamily: "Noto Sans"
    fontSize: "14px"
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: "0em"
  label-sm:
    fontFamily: "Noto Sans"
    fontSize: "12px"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.12em"
  code-md:
    fontFamily: "Noto Sans Mono"
    fontSize: "14px"
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: "0em"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "32px"
  touch: "44px"
  xxl: "48px"
  xxxl: "64px"
rounded:
  none: "0px"
  sm: "4px"
  md: "8px"
  lg: "12px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    height: "{spacing.touch}"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    height: "{spacing.touch}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.secondary}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    height: "{spacing.touch}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-tint}"
    textColor: "{colors.secondary}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    height: "{spacing.touch}"
  button-disabled:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.neutral}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    height: "{spacing.touch}"
  input-default:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    height: "{spacing.touch}"
  card-default:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  card-canvas:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-surface-muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  callout-provenance:
    backgroundColor: "{colors.info-bg}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
  badge-approved:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs}"
  badge-in-review:
    backgroundColor: "{colors.info-bg}"
    textColor: "{colors.info}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs}"
  badge-draft:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs}"
  badge-deprecated:
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.error}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs}"
  badge-neutral:
    backgroundColor: "{colors.neutral-bg}"
    textColor: "{colors.neutral}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs}"
  accent-bar-red:
    backgroundColor: "{colors.accent}"
    rounded: "{rounded.none}"
    height: "{spacing.sm}"
  accent-bar-navy:
    backgroundColor: "{colors.secondary}"
    rounded: "{rounded.none}"
    height: "{spacing.sm}"
  slide-dark:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.body-slide}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxxl}"
  code-inline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-mono}"
    typography: "{typography.code-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs}"
---

# PUB-03 — Irvantri Standards AI Design System Context (`DESIGN.md`)

| Field | Value |
| :--- | :--- |
| **Code** | `PUB-03` |
| **Title** | Irvantri Standards AI Design System Context |
| **Deployment Filename** | `DESIGN.md` *(for Superdesign, Google Stitch, external repositories, and coding agents)* |
| **Entity** | Irvantri Standards (`Irvantri Standards Pte. Ltd.`) |
| **Affiliation** | A member of Irvantri Group |
| **Version** | `v1.2.3` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-28` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Source Standards** | `A01 (v1.2.0)`, `A02 (v1.3.0)`, `A03 (v1.1.1)`, `A04 (v1.2.0)`, `B01 (v2.1.0)`, `B02 (v1.3.0)`, `B03 (v2.0.0)`, `B04 (v1.2.0)`, `B05 (v1.2.0)`, `C01 (v1.1.1)`, `C02 (v1.1.0)`, `C04 (v1.0.1)`, `D01 (v1.0.3)`, `D02 (v2.0.1)`, `D03 (v2.0.0)`, `D04 (v1.2.1)`, `E01 (v2.5.0)`, `E02 (v1.1.0)`, `E04 (v2.3.0)` |

> **Precedence Notice (`A01 §5.1.4`, `§5.7.5`):** This compiled publication (`PUB-03`) is an informative Artificial Intelligence (`AI`) design and authoring context compiled on `2026-11-28` from the **Irvantri Standards Unified Operating Library** (`Library-Index.md (v1.2.24)`). Active normative standards (`A01`–`E04`) and `02_Assets/AST-D01-01_Design-Tokens.json` prevail in the event of any conflict between this publication and an underlying standard.

---

## Overview

The **Irvantri Standards Design System** (`C02 §5.3.2`) defines a disciplined Swiss-editorial institutional minimalism grounded in generous negative space, crisp typographic hierarchy, and deterministic geometric alignment across web interfaces, concise pitch decks, and formal documents.

* **Core Brand Pillars:** `Integrity` · `Precision` · `Reliability` · `Progress`
* **Proportional Balance (`B02 §5.4.1`, `E04 §5.2.4`):** `75%` neutral surfaces (`{colors.surface}` / `{colors.canvas}`), `20%` institutional blue and navy (`{colors.secondary}` / `{colors.primary}`), and `5%` **Signal Red** (`{colors.accent}`).
* **Default Theme (`D01 §5.2.3`):** Light mode (`{colors.surface}` primary canvas, `{colors.canvas}` subtle secondary wash, `{colors.on-surface}` body ink). Reserve full-bleed **Deep Navy** (`{colors.secondary}`) strictly for structural section dividers, hero covers, or closing attribution slides.
* **Authoritative Entity & Attribution (`A03 §5.2.1`, `§5.3.3`, `§5.6.1`):**
  * Operating Entity: `Irvantri Standards Pte. Ltd.`
  * Endorsement Line (verbatim): `A member of Irvantri Group`
  * Copyright Footer: `© [YYYY] Irvantri Standards Pte. Ltd. All rights reserved.`

---

## Colors

All digital Hexadecimal (`HEX`) values are written in uppercase with a leading `#` (`B02 §5.1.2`), matching Standard Red-Green-Blue (`sRGB`) tokens in `AST-D01-01_Design-Tokens.json`.

**Table 1.** Primary Brand & Neutral Palette (`B02 §5.1.1`–`§5.2.1`)

| YAML Token | Name | HEX | Red-Green-Blue (`RGB`) | CSS Custom Property | Role |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `{colors.primary}` | **Brand Blue** | `#074C96` | `7, 76, 150` | `--is-color-brand-primary` | Primary buttons, links, active states, eyebrow kickers, focus rings, callout borders |
| `{colors.accent}` | **Signal Red** | `#DE0029` | `222, 0, 41` | `--is-color-brand-accent` | Brand mark and `24%` split accent bar segment; prohibited for text (`B02 §5.3.2`) |
| `{colors.secondary}` | **Deep Navy** | `#092B55` | `9, 43, 85` | `--is-color-brand-deep` | Display headings, wordmark, `76%` split accent bar, dark structural slides |
| `{colors.primary-hover}` | **Royal Navy** | `#102F60` | `16, 47, 96` | `--is-color-brand-secondary` | Primary hover state, secondary dark panels on Deep Navy slides |
| `{colors.surface}` | **Pure White** | `#FFFFFF` | `255, 255, 255` | `--is-color-bg-surface` | Primary page and card surface |
| `{colors.canvas}` | **Canvas Subtle** | `#F8FAFC` | `248, 250, 252` | `--is-color-bg-canvas` | Page canvas, subtle washes, table headers |
| `{colors.surface-muted}` | **Surface Muted** | `#F1F5F9` | `241, 245, 249` | `--is-color-bg-muted` | Disabled controls, neutral containers |
| `{colors.surface-tint}` | **Surface Tint** | `#EFF6FF` | `239, 246, 255` | `--is-color-bg-tint` | Provenance callout wash, secondary button hover |
| `{colors.border-subtle}` | **Border Subtle** | `#E2E8F0` | `226, 232, 240` | `--is-color-border-subtle` | Hairline dividers and table row separators |
| `{colors.border-default}` | **Border Default** | `#CBD5E1` | `203, 213, 225` | `--is-color-border-default` | Decorative card borders and table grids |
| `{colors.border-strong}` | **Border Strong** | `#64748B` | `100, 116, 139` | `--is-color-border-strong` | Input borders and interactive control outlines (`4.76:1` on white) |
| `{colors.on-surface-muted}` | **Text Muted** | `#5F6C7E` | `95, 108, 126` | `--is-color-text-muted` | Secondary copy, captions, metadata labels (`5.34:1` on white) |
| `{colors.on-surface}` | **Text Primary** | `#0F172A` | `15, 23, 42` | `--is-color-text-primary` | Primary body ink (`17.85:1` on white) |
| `{colors.ink-mono}` | **Pure Black** | `#000000` | `0, 0, 0` | `--is-color-text-mono` | High-contrast monospace identifiers and code |

**Table 2.** Five-State Semantic Status Palette (`B02 §5.3.1`, `C02 §5.4.1`, `E02 §5.2.2`)

| Semantic Role | Controlled `C02` Statuses | Foreground | Surface | Border |
| :--- | :--- | :--- | :--- | :--- |
| **Informative** | `Planned`, `In Review` | `{colors.info}` (`#074C96`) | `{colors.info-bg}` (`#EFF6FF`) | `{colors.info-border}` (`#BFDBFE`) |
| **Success** | `Approved` | `{colors.success}` (`#166534`) | `{colors.success-bg}` (`#F0FDF4`) | `{colors.success-border}` (`#BBF7D0`) |
| **Warning** | `Draft`, `Sync Required` | `{colors.warning}` (`#92400E`) | `{colors.warning-bg}` (`#FFFBEB`) | `{colors.warning-border}` (`#FDE68A`) |
| **Danger** | `Deprecated`, Errors | `{colors.error}` (`#A42332`) | `{colors.error-bg}` (`#FEF2F2`) | `{colors.error-border}` (`#FECACA`) |
| **Neutral** | Archived / Inactive / Disabled | `{colors.neutral}` (`#475569`) | `{colors.neutral-bg}` (`#F1F5F9`) | `{colors.neutral-border}` (`#CBD5E1`) |

* **Web Content Accessibility Guidelines (`WCAG`) 2.2 Level AA Contrast (`B02 §5.5.1`, `D04`):** Standard text meets `≥ 4.5:1`; large headings and User Interface (`UI`) borders meet `≥ 3:1`. Every semantic status pairs color with an exact `C02` text label and a `6 px`–`8 px` solid square visual cue.

---

## Typography

Use exclusively the unified **`SIL OFL-1.1` Noto Sans superfamily** (`06_Dependencies/Fonts/`): upright `Noto Sans Display` for display headings, `Noto Sans` for body copy and interfaces, and `Noto Sans Mono` for codes, versions, and International Organization for Standardization (`ISO`) 8601 dates (`B03 v2.0.0`).

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Display:wght@400;600;700;800&family=Noto+Sans+Mono:wght@400;500;700&family=Noto+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
```

**Table 3.** Role-Based Typographic Scale, generated from `AST-D01-01` (`B03 §5.2.6`, `E04 §5.2.6`)

| YAML Token | Role | Typeface | Size | Weight | Tracking | Line Height | Source Token |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `{typography.slide-title}` | Slide Title (`1920 × 1080`) | `Noto Sans Display` | `64px` | `800` | `-0.03em` | `1.2` | `primitive.font.size.slide-title` |
| `{typography.slide-heading}` | Slide Heading (`1920 × 1080`) | `Noto Sans Display` | `40px` | `700` | `-0.03em` | `1.2` | `primitive.font.size.slide-heading` |
| `{typography.body-slide}` | Slide Body & Captions (`1920 × 1080`) | `Noto Sans` | `24px` (minimum) | `400` | `0em` | `1.5` | `primitive.font.size.slide-body` |
| `{typography.headline-lg}` | Page Title | `Noto Sans Display` | `32px` | `800` | `-0.03em` | `1.2` | `primitive.font.size.page-title-desktop` |
| `{typography.headline-kpi}` | Metric / Key Performance Indicator (`KPI`) | `Noto Sans Display` | `28px` | `800` | `-0.04em` | `1.2` | `primitive.font.size.kpi-desktop` |
| `{typography.headline-md}` | Section Title | `Noto Sans Display` | `20px` | `700` | `-0.03em` | `1.2` | `primitive.font.size.section-title-desktop` |
| `{typography.headline-sm}` | Panel Title | `Noto Sans Display` | `16px` | `700` | `-0.02em` | `1.2` | `primitive.font.size.panel-title` |
| `{typography.body-lg}` | Long-Form Documentation | `Noto Sans` | `16px` (`12 pt`) | `400` | `0em` | `1.5` | `primitive.font.size.body-doc` |
| `{typography.body-md}` | Standard UI & Tables | `Noto Sans` | `14px` (`10.5 pt`) | `400` | `0em` | `1.5` | `primitive.font.size.body-ui` |
| `{typography.label-lg}` | Button & Field Labels | `Noto Sans` | `14px` | `600` | `0em` | `1.5` | `primitive.font.size.body-ui` |
| `{typography.label-sm}` | Eyebrow / Overline (Uppercase) | `Noto Sans` | `12px` | `700` | `0.12em` | `1.2` | `primitive.font.size.eyebrow` |
| `{typography.code-md}` | Codes, Versions, Dates | `Noto Sans Mono` | `14px` | `500` | `0em` | `1.5` | `primitive.font.size.body-ui` |

* **Slide Text (`E04 §5.2.6`):** On `1920 × 1080` slides, use only `{typography.slide-title}`, `{typography.slide-heading}`, and `{typography.body-slide}`. Never set slide text below `24px`.
* **Fallback Stacks (`B03 §5.1.4`):** `'Noto Sans Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Liberation Sans', Arial, sans-serif`; `'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Liberation Sans', Arial, sans-serif`; `'Noto Sans Mono', 'Liberation Mono', 'DejaVu Sans Mono', monospace`.
* **Tabular Numerals & Measure (`B03 §5.2.4`, `§5.3.1`):** Enforce `font-variant-numeric: tabular-nums;` on every table, metric readout, and register. Keep prose columns between `50` and `85` characters per line (`max-width: 72ch`). Restrict ALL CAPS to eyebrows, table headers, codes, and wordmarks (`B03 §5.2.7`).

---

## Layout

* **Spatial Base Unit (`B04 §5.1.1`–`§5.1.2`):** Align all digital screens and `1920 × 1080` slides to the `4px` Base Unit (`{spacing.xs}` through `{spacing.xxxl}`). Align A4 (`210 mm × 297 mm`) formal documents to the `4 mm` Base Unit with `20 mm` L/R and `16 mm` T/B Safe Margins (`24 mm` inner spine margin on covers).
* **Responsive Breakpoints (`D02 §5.1.1`):**
  * `Reflow Minimum:` `320px` (zero horizontal scrolling)
  * `Compact:` `320px`–`767px` (tables convert to stacked cards; touch target gap `≥ 12px`)
  * `Medium:` `768px`–`1279px`
  * `Expanded:` `≥ 1280px` (`1440px` standard content max-width)
* **Minimalist Framing:** Prefer open whitespace, left alignment, and subtle `{colors.canvas}` / `{colors.surface-tint}` surface washes over heavy card borders. Keep running headers and footers rule-free.

---

## Elevation & Depth

Depth is communicated primarily through surface tone contrast (`{colors.surface}` over `{colors.canvas}`) and hairline borders (`1px solid {colors.border-subtle}` or `{colors.border-default}`) rather than heavy drop shadows (`B04 §5.2.3`).

* **Card Elevation (`--is-shadow-card`):** `0 2px 8px rgba(15, 23, 42, 0.06)`
* **Action Elevation (`--is-shadow-action`):** `0 2px 6px rgba(15, 23, 42, 0.12)`
* **Focus Indicator (`D04 §5.2.4`):** `outline: 3px solid #074C96; outline-offset: 3px;`
* **Motion (`B05 §5.4`):** Keep state transitions `≤ 300ms` with `prefers-reduced-motion` support; prohibit flashing or erratic decorative motion.

---

## Shapes

* **Corner Radii (`B04 §5.2.1` — Strictly Four Increments):**
  * `{rounded.none}` (`0px`): Split accent bars, architectural frames, square badge cues, sharp hairlines
  * `{rounded.sm}` (`4px`): Buttons, inputs, status badges, inline code tags
  * `{rounded.md}` (`8px`): Cards, panels, provenance callouts, status banners
  * `{rounded.lg}` (`12px`): Hero feature containers
* **Signature Split Accent Bar (`B04 §5.3.1`):** Exact **`24%` Signal Red (`{colors.accent}`)** and **`76%` Deep Navy (`{colors.secondary}`)** — either a full-width top edge bar (`2 mm` in A4 `PDF`; `4px`–`8px` on web/slides, red left / navy right) or a vertical left-spine cover bar (`4 mm` in A4 `PDF`; `12px`–`16px` on slides, navy upper / red lower).
* **Icons (`B05 §5.1`):** Geometric line icons on a `24px` grid (`16px` / `20px` / `24px` sizes), uniform `1.5px` or `2px` stroke width, zero multi-color fills.

---

## Components

* **Buttons (`D03`):** `44px` minimum height (`{spacing.touch}`), `{rounded.sm}` (`4px`) radius, `16px`–`20px` horizontal padding. Primary uses `{colors.primary}` background with `{colors.on-primary}` text (hover `{colors.primary-hover}`); Secondary uses `{colors.surface}` with `1px solid {colors.border-strong}` border and `{colors.secondary}` text (hover `{colors.surface-tint}`).
* **Status Badges (`E02 §5.2.2`):** `{rounded.sm}` (`4px`), `1px` semantic border, semantic background tint, `6px` solid square marker (`border-radius: 0`), and exact Title Case `C02` text (`Approved`, `In Review`, `Draft`, `Planned`, `Sync Required`, `Deprecated`).
* **Provenance Callout (`D03 §5.4.3`):** `{colors.info-bg}` fill (`#EFF6FF`), `4px` left border `{colors.primary}` (`#074C96`), `{rounded.md}` (`8px`) radius, `16px 20px` padding.
* **Minimalist Data Tables (`C04 §5.4`):** Zero vertical gridlines and zero outer box borders. Header row uses `{colors.canvas}` fill, `{colors.secondary}` bold text, and `2px solid {colors.secondary}` bottom border; body rows use `{colors.surface}` fill and `1px solid {colors.border-subtle}` bottom hairline. Never leave cells blank (populate `None` or `—`).
* **Brand Mark Assets (`B01 v2.1.0`):** Source all logos verbatim from approved `02_Assets/` Scalable Vector Graphics (`SVG`) masters (`AST-B01-01` Primary Symbol `≥ 28px`/`12 mm`; `AST-B01-02` White Symbol `≥ 28px`/`12 mm`; `AST-B01-03` Full-Color Parent-Endorsed Lockup `4.15:1` `≥ 260px`/`64 mm`; `AST-B01-04` White Parent-Endorsed Lockup `4.15:1` `≥ 260px`/`64 mm`) with at least `0.25×` Primary Symbol width unobstructed Clear Space on all four sides.
* **Favicons & App Icons (`B01 v2.1.0 §5.3.4`, `§5.4.4`, `§5.6.2`; `B05 §5.1.4`):** Below `28px`, never shrink the Primary Symbol; use `AST-B01-17_Small-Format-Symbol.svg` (`16px`–`27px`, switches to white under `prefers-color-scheme: dark`) or `AST-B01-18_White-Small-Format-Symbol.svg` on dark surfaces. Web pages link `AST-B01-17` as `<link rel="icon" type="image/svg+xml">`, `AST-B01-19_Favicon.ico` as the fallback, and `AST-B01-21_Apple-Touch-Icon.png` as `apple-touch-icon`; web app manifests list `AST-B01-22_App-Icon-192.png` and `AST-B01-23_App-Icon-512.png`. Never redraw the symbol as a `UI` icon or place it in any frame other than the Pure White App Icon Tile.

---

## Do's and Don'ts

### Do
* Use strictly upright `Noto Sans Display`, `Noto Sans`, and `Noto Sans Mono` across every interface, deck, and document.
* Keep `75%` of layouts neutral white/slate space so `{colors.secondary}` headings and `{colors.primary}` actions anchor visual hierarchy.
* Apply `tabular-nums` to all numeric columns, `KPI` cards, and registers, and use `ISO` 8601 dates (`YYYY-MM-DD`), uppercase `ISO` 4217 currency codes (`SGD 1,200`), and spaced units (`20 mm`, `16px`).
* Write in objective United States English (`en-US`) without contractions in formal documents and pitch decks, and reproduce `C01 §5.5.1` boilerplates verbatim when describing Irvantri Standards.

### Don't
* Never use serif, script, or retired fonts (`Montserrat`, `Inter`, `JetBrains Mono`, `Calibri`, `Arial` as primary).
* Never use **Signal Red (`#DE0029`)** for body copy, links, headings, or error text (use `{colors.error}` `#A42332` for errors and deprecated labels).
* Never use pill-shaped (`9999px`) badges/buttons, neon glows, glassmorphism, multi-stop gradients, or decorative rings/waves on operational work surfaces or tables.
* Never leave table cells blank, invent informal status strings (*WIP*, *Final*, *Done*), display internal project codenames externally, use promotional superlatives (*world-class*, *best-in-class*, *revolutionary*, *cutting-edge*, *seamless*, *unmatched*), or bind `Irvantri Group Pte. Ltd.` in place of `Irvantri Standards Pte. Ltd.`.

---

## Appendix A — Verbatim Corporate Boilerplates (`C01 §5.5.1`)

```text
One-Line Descriptor:
Irvantri Standards develops disciplined operating frameworks, technical standards, and structured systems that turn complex organizational requirements into clear, verifiable execution. A member of Irvantri Group.
```

```text
Short Corporate Description:
Irvantri Standards (Irvantri Standards Pte. Ltd.) builds practical operating standards, governance frameworks, and structured digital and documentation systems. Focused on clarity, traceability, and repeatable execution, Irvantri Standards helps organizations replace ad-hoc work with durable, auditable baselines. A member of Irvantri Group.
```

---

## Appendix B — HTML/CSS-to-PDF Print Shells & `:root` Tokens (`E01 §5.4`, `E04 §5.2`, `AST-D01-01`)

When compiling HyperText Markup Language (`HTML`) and Cascading Style Sheets (`CSS`) exported from **Superdesign** or **Google Stitch** to Portable Document Format (`PDF`) via headless Chromium / Playwright or WeasyPrint, apply the `@page` rules and `:root` custom properties below (derived verbatim from `02_Assets/AST-D01-01_Design-Tokens.json`).

```css
/* Formal A4 Digital Distribution PDF (E01 §5.4) */
@page { size: 210mm 297mm; margin: 16mm 20mm 16mm 20mm; }
@page :first { margin: 16mm 20mm 16mm 24mm; }

/* Concise 16:9 Pitch Deck PDF (E04 §5.2) — use in deck stylesheets instead of A4 */
/* @page { size: 1920px 1080px; margin: 0; } */
/* .slide { width: 1920px; height: 1080px; overflow: hidden; break-after: page; } */

:root {
  --is-color-brand-primary: #074C96;
  --is-color-brand-accent: #DE0029;
  --is-color-brand-deep: #092B55;
  --is-color-brand-secondary: #102F60;
  --is-color-bg-surface: #FFFFFF;
  --is-color-bg-canvas: #F8FAFC;
  --is-color-bg-muted: #F1F5F9;
  --is-color-bg-tint: #EFF6FF;
  --is-color-border-subtle: #E2E8F0;
  --is-color-border-default: #CBD5E1;
  --is-color-border-strong: #64748B;
  --is-color-text-primary: #0F172A;
  --is-color-text-muted: #5F6C7E;
  --is-color-text-inverse: #FFFFFF;
  --is-color-text-mono: #000000;
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
  --is-font-family-display: 'Noto Sans Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Liberation Sans', Arial, sans-serif;
  --is-font-family-text: 'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Liberation Sans', Arial, sans-serif;
  --is-font-family-mono: 'Noto Sans Mono', 'Liberation Mono', 'DejaVu Sans Mono', monospace;
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

## Appendix C — Publication Build Manifest & Revision History (`A01 §5.7.5`, `E02 §5.1.3`)

**Table 4.** Publication Build Manifest — `PUB-03` (Compiled `2026-11-28`)

| Series / Layer | Source Items and Exact Versions | Status |
| :--- | :--- | :--- |
| **Master Registers & Assets** | `Library-Index.md (v1.2.24)`, `Dependencies-Manifest.md (v2.0.0)`, `AST-B01-01`–`AST-B01-04` (`B01 (v2.0)`), `AST-B01-17`–`AST-B01-23` (`B01 (v2.1)`), `AST-D01-01` (`D01 (v1.0)`) | `Approved` |
| **Series A — Governance** | `A01 (v1.2.0)`, `A02 (v1.3.0)`, `A03 (v1.1.1)`, `A04 (v1.2.0)` | `Approved` |
| **Series B — Visual Foundations** | `B01 (v2.1.0)`, `B02 (v1.3.0)`, `B03 (v2.0.0)`, `B04 (v1.2.0)`, `B05 (v1.2.0)` | `Approved` |
| **Series C — Verbal Standards** | `C01 (v1.1.1)`, `C02 (v1.1.0)`, `C04 (v1.0.1)` | `Approved` |
| **Series D — Digital Systems** | `D01 (v1.0.3)`, `D02 (v2.0.1)`, `D03 (v2.0.0)`, `D04 (v1.2.1)` | `Approved` |
| **Series E — Documents & Print** | `E01 (v2.5.0)`, `E02 (v1.1.0)`, `E04 (v2.3.0)` | `Approved` |

**Table 5.** Revision History — `PUB-03`

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v1.2.3` | `2026-11-28` | Errata | Synchronized the source standards and Table 4 to `E01 (v2.5.0)`, `E04 (v2.3.0)`, and `Library-Index.md (v1.2.24)` (`REC-A04-014`). | Hary Irfantri |
| `v1.2.2` | `2026-11-27` | Errata | Synchronized the source standards and Table 4 to `E01 (v2.4.0)` and `Library-Index.md (v1.2.23)` (`REC-A04-013`). | Hary Irfantri |
| `v1.2.1` | `2026-11-27` | Errata | Synchronized the source standards and Table 4 to `B01 (v2.1.0)`, `B05 (v1.2.0)`, and `Library-Index.md (v1.2.22)`, and added favicon and app icon guidance for `AST-B01-17`–`AST-B01-23` (`REC-A04-012`). | Hary Irfantri |
| `v1.2.0` | `2026-11-27` | Minor | Regenerated the front-matter typography and Table 3 from `AST-D01-01`: replaced the unsourced `48px` `headline-display` with `slide-title` (`64px`), added `slide-heading` (`40px`), raised `body-slide` from `22px` to `24px` (`E04 (v2.2.0) §5.2.6`), snapped all line heights to the `1.2` / `1.5` tokens, and removed deck sizes below `24px` (`REC-A04-009` `F-02`); refreshed the source standards and Table 4 to `A04 (v1.2.0)`, `B02 (v1.3.0)`, `E01 (v2.3.0)`, `E04 (v2.2.0)`, and `Library-Index.md (v1.2.20)`. | Hary Irfantri |
| `v1.1.3` | `2026-11-27` | Errata | Moved the secondary button border guidance from `{colors.border-default}` to `{colors.border-strong}` per `B02 (v1.2.0) §5.2.2` (`REC-A04-009` `F-01`), and refreshed Table 4 to `Library-Index.md (v1.2.18)`. | Hary Irfantri |
| `v1.1.2` | `2026-11-27` | Errata | Synchronized to `B02 (v1.2.0)`: added the `border-strong` color token (`#64748B`) for input and control borders, limited `border-default` to decorative uses, and refreshed Table 4 to `Library-Index.md (v1.2.15)` with the compile date corrected to `2026-11-27`. | Hary Irfantri |
| `v1.1.1` | `2026-11-27` | Errata | Refreshed the source standards and Table 4 register references to E01 (v2.2.0), E04 (v2.1.1), and Library-Index.md (v1.2.14). | Hary Irfantri |
| `v1.1.0` | `2026-11-26` | Minor | Added `@google/design.md` / Superdesign-compliant YAML frontmatter (`version`, `name`, `description`, `colors`, `typography`, `spacing`, `rounded`, `components`) starting on line 1, reordered prose into the canonical 8-section `DESIGN.md` structure (`Overview` through `Do's and Don'ts`), and verified WCAG 2.2 Level AA contrast (`≥ 4.5:1`) on every component token pair. | Hary Irfantri |
| `v1.0.0` | `2026-11-26` | Major | Initial approved baseline of `PUB-03` (Irvantri Standards AI Design System Context, external deployment filename `DESIGN.md`), synthesizing live `Approved` Series `A`–`E` standards and `AST-D01-01` tokens. | Hary Irfantri |

---

© 2026 Irvantri Standards Pte. Ltd. All rights reserved. | A member of Irvantri Group
