# Irvantri Standards — Third-Party Dependencies Manifest

| Field | Value |
| :--- | :--- |
| **Register** | `06_Dependencies/Dependencies-Manifest.md` *(Uncoded dependency manifest)* |
| **Entity** | Irvantri Standards (`Irvantri Standards Pte. Ltd.`) |
| **Version** | `v1.0.0` |
| **Status** | `Approved` |
| **Effective Date** | `2026-11-26` |
| **Last Updated** | `2026-11-26` |
| **Owner** | Hary Irfantri |
| **Approver** | Hary Irfantri |
| **Governing Rules** | `A02 §5.5.4` (Third-Party Dependencies), `A03 §5.6.2` (Third-Party Attribution), `B03 §5.1.3` (Font Licensing), `E03 §5.3.1` (Print Color Profiles) |

---

## 1. Purpose & Ownership Boundary

This manifest records every unmodified third-party licensed package and binary resource stored inside `06_Dependencies/` to support reproducible rendering of controlled templates (`TPL-`), publications (`PUB-`), and prepress outputs across the **Irvantri Standards Unified Operating Library**.

> **Third-Party Attribution Notice (`A03 §5.6.2`):** All files listed in this manifest are owned by their respective external authors and rights holders. Storing these unmodified packages inside this internal repository ensures deterministic typography and color reproduction and does not claim Irvantri Standards ownership, authorship, or endorsement by any rights holder. Unmodified vendor subfolders and filenames are preserved under `A02 §5.5.4`.

---

## 2. Licensed Typeface Packages (`06_Dependencies/Fonts/`)

All brand typeface packages below are governed by `B03 §5.1.1`–`§5.1.3` and distributed under the **SIL Open Font License, Version 1.1 (`OFL-1.1`)**, with verbatim `OFL.txt` license texts retained alongside the variable and `static/` font files inside each package folder.

| Package Path | Typeface Role | Package Contents | Upstream Version | Rights Holder / Publisher | License | Governing Standard |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `06_Dependencies/Fonts/Montserrat/` | Display (`B03 §5.1.1`) | `Montserrat-VariableFont_wght.ttf`, `Montserrat-Italic-VariableFont_wght.ttf`, `static/` (18 static weights), `OFL.txt`, `README.txt` | `9.000` | The Montserrat Project Authors (Julieta Ulanovsky) | `SIL OFL-1.1` | `B03` |
| `06_Dependencies/Fonts/Inter/` | Text (`B03 §5.1.1`) | `Inter-VariableFont_opsz,wght.ttf`, `Inter-Italic-VariableFont_opsz,wght.ttf`, `static/` (54 optical-size static weights), `OFL.txt`, `README.txt` | `4.001` | The Inter Project Authors (Rasmus Andersson) | `SIL OFL-1.1` | `B03` |
| `06_Dependencies/Fonts/JetBrains Mono/` | Monospace (`B03 §5.1.2`) | `JetBrainsMono-VariableFont_wght.ttf`, `JetBrainsMono-Italic-VariableFont_wght.ttf`, `static/` (16 static weights), `OFL.txt`, `README.txt` | `2.211` | The JetBrains Mono Project Authors (JetBrains) | `SIL OFL-1.1` | `B03` |

### Verified Primary Template Font Checksums (Secure Hash Algorithm 256-bit (`SHA-256`))

| File Path | Size (bytes) | `SHA-256` Checksum |
| :--- | :--- | :--- |
| `06_Dependencies/Fonts/Montserrat/static/Montserrat-ExtraBold.ttf` | `344,052` | `5cf0a23133ccce35f9e115b8dbbf90434201827bc2465d12f9d91bbf02cf9466` |
| `06_Dependencies/Fonts/Montserrat/static/Montserrat-ExtraBoldItalic.ttf` | `348,532` | `45ce93da96fbcff5547cf081bc979cd525c3567bd732f830febde8f29f2bffd2` |
| `06_Dependencies/Fonts/Inter/Inter-VariableFont_opsz,wght.ttf` | `874,708` | `0be2399ea925f1f83ff974764761da9860ec50742ed29a5d4c1ffd0c5c7ac3a8` |
| `06_Dependencies/Fonts/Inter/Inter-Italic-VariableFont_opsz,wght.ttf` | `904,532` | `6136f73372fedc37b80fd1a8ec3e21734073ff17376f3672718f186779672e7a` |
| `06_Dependencies/Fonts/JetBrains Mono/static/JetBrainsMono-Medium.ttf` | `114,920` | `23d57b8a635d023c3717a9c7ac1721199d0f8c6fe4b06d4d5ba3af2170fcbaa2` |
| `06_Dependencies/Fonts/JetBrains Mono/static/JetBrainsMono-MediumItalic.ttf` | `118,044` | `c11300f0b569bf3b830230b1335d4dd82a5a936be1c1692e1e269a865ecf7ca2` |

> **Informative Note:** Automated `PDF/X-4` (`E03 §5.4.1`) and Digital Distribution `PDF` (`E01 §5.4.3`) pipelines may embed either the bundled `static/` files or deterministic static weight subsets (`Regular 400`, `Medium 500`, `SemiBold 600`, `Bold 700` at `opsz 14`) instantiated from `Inter-VariableFont_opsz,wght.ttf`.

---

## 3. Print Color Profiles (`06_Dependencies/Color-Profiles/`)

Color profiles below are governed by `B02 §5.1.3` and `E03 §5.3.1` for International Organization for Standardization (`ISO`) Coated v2 Cyan-Magenta-Yellow-Key (`CMYK`) commercial offset and digital press production.

| File Path | Profile Name & Characterization | Upstream Version | Rights Holder / Publisher | Usage & Distribution Scope | Governing Standards | Size (bytes) | `SHA-256` Checksum |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `06_Dependencies/Color-Profiles/ISOcoated_v2_eci.icc` | `ISO Coated v2 (ECI)` (`FOGRA39` OutputIntent) | `PrintOpen 5.2.0` | European Color Initiative (`ECI`) / Heidelberger Druckmaschinen AG (`© 2000–2006`) | Internal prepress use and `PDF/X-4` OutputIntent embedding only; SHALL NOT be republished publicly as a standalone mirror | `B02`, `E03` | `1,829,077` | `128dc02f7246cc3807af0323695379f64151a8f27a587736acc59f8b6ce894b8` |

---

## 4. Revision History

| Version | Date | Type | Summary of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| `v1.0.0` | `2026-11-26` | Major | Initial approved baseline registering the three complete `B03` brand typeface packages (`Montserrat`, `Inter`, `JetBrains Mono` with variable fonts, `static/` suites, `OFL.txt`, and `README.txt`) and the `ISOcoated_v2_eci.icc` (`FOGRA39`) International Color Consortium (`ICC`) profile with verified `SHA-256` checksums and rights-holder attributions per `A02 (v1.2.0) §5.5.4`. | Hary Irfantri |
