# Irvantri Standards — Third-Party Dependencies Manifest

| Field | Value |
| :--- | :--- |
| **Register** | `06_Dependencies/Dependencies-Manifest.md` *(Uncoded dependency manifest)* |
| **Entity** | Irvantri Standards (`Irvantri Standards Pte. Ltd.`) |
| **Version** | `v2.0.0` |
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

All brand typeface packages below are governed by `B03 (v2.0.0) §5.1.1`–`§5.1.3` and distributed under the **SIL Open Font License, Version 1.1 (`OFL-1.1`)**, with verbatim `OFL.txt` license text retained alongside the static font binaries inside each package folder.

| Package Path | Typeface Role | Package Contents | Upstream Version | Rights Holder / Publisher | License | Governing Standard |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `06_Dependencies/Fonts/Noto Sans Display/` | Display (`B03 §5.1.1`) | `NotoSansDisplay-Regular.ttf`, `Medium`, `SemiBold`, `Bold`, `ExtraBold`, `OFL.txt` | `2.003` | Google Inc. / Monotype Imaging Inc. (`© 2015`) | `SIL OFL-1.1` | `B03` |
| `06_Dependencies/Fonts/Noto Sans/` | Text (`B03 §5.1.1`) | `NotoSans-Regular.ttf`, `Italic`, `Medium`, `SemiBold`, `Bold`, `ExtraBold`, `OFL.txt` | `2.004` | Google LLC / Monotype Imaging Inc. (`© 2015`) | `SIL OFL-1.1` | `B03` |
| `06_Dependencies/Fonts/Noto Sans Mono/` | Monospace (`B03 §5.1.2`) | `NotoSansMono-Regular.ttf`, `Medium`, `SemiBold`, `Bold`, `OFL.txt` | `2.006` | Google LLC / Monotype Imaging Inc. (`© 2015`) | `SIL OFL-1.1` | `B03` |

### Verified Primary Template Font Checksums (Secure Hash Algorithm 256-bit (`SHA-256`))

| File Path | Size (bytes) | `SHA-256` Checksum |
| :--- | :--- | :--- |
| `06_Dependencies/Fonts/Noto Sans Display/NotoSansDisplay-Regular.ttf` | `508,388` | `3dd456595e9226472ab8adaf9408400c671b97dbba241d883d05e2ab70ceadac` |
| `06_Dependencies/Fonts/Noto Sans Display/NotoSansDisplay-Medium.ttf` | `505,504` | `0d7de6c6a264dfa9b0e93efc1338414bff20f79aaf9ff85e3a9fc901bdf9dbea` |
| `06_Dependencies/Fonts/Noto Sans Display/NotoSansDisplay-SemiBold.ttf` | `511,828` | `9fa1f6b9fc7d95e0aa49ec75a90ce858e0a4c55b839811eb64abb7798afc94fd` |
| `06_Dependencies/Fonts/Noto Sans Display/NotoSansDisplay-Bold.ttf` | `513,000` | `1640ba8acb852d9e00406e166d1fc0cedd62a4c20342fd92f1f6dbc7baa61de2` |
| `06_Dependencies/Fonts/Noto Sans Display/NotoSansDisplay-ExtraBold.ttf` | `516,168` | `21d09d821e94c676ce07e0fa6d6b9884946e8e3c0e3b9800721d58a643a83336` |
| `06_Dependencies/Fonts/Noto Sans/NotoSans-Regular.ttf` | `512,672` | `89c3c497f618fdaa0b2d1e98fef93582f28c71debd2c4a8cdf41f190ced2909d` |
| `06_Dependencies/Fonts/Noto Sans/NotoSans-Italic.ttf` | `530,120` | `5d7618dda819443fd07301c84adcee9fe8960c873ea5e5e1f0f59db384b78082` |
| `06_Dependencies/Fonts/Noto Sans/NotoSans-Medium.ttf` | `507,976` | `013ae62f5187c01e8752de78829ee7e1e0feaed6edee17db0dbf703988c99f3d` |
| `06_Dependencies/Fonts/Noto Sans/NotoSans-SemiBold.ttf` | `515,204` | `68543590a7c3185d69ad16664c46df28832beeb72621d2470e86b04099eb4efb` |
| `06_Dependencies/Fonts/Noto Sans/NotoSans-Bold.ttf` | `515,752` | `e83493c945848ecd4a9ad0f6d19164541a0d3e23a9c952304a00a46e00272ac5` |
| `06_Dependencies/Fonts/Noto Sans/NotoSans-ExtraBold.ttf` | `515,984` | `b0d459b012f378d192af7cf8fcc577d78fe96a6a8399946c44f683c860a17023` |
| `06_Dependencies/Fonts/Noto Sans Mono/NotoSansMono-Regular.ttf` | `510,612` | `6b692c4b6d15ccf59f1c1fe8d11cb8a92f51960f3e9f1f523781755a3af7e29f` |
| `06_Dependencies/Fonts/Noto Sans Mono/NotoSansMono-Medium.ttf` | `510,644` | `c6107a9c14e9d33db347299fc467fb52c473919050d1be7c661869107eeffc06` |
| `06_Dependencies/Fonts/Noto Sans Mono/NotoSansMono-SemiBold.ttf` | `517,044` | `38ab4cde310aa7c73c3c07c39527888f80c49473a4c959c68919121a6d983f67` |
| `06_Dependencies/Fonts/Noto Sans Mono/NotoSansMono-Bold.ttf` | `523,412` | `b22563d5f03b345a62115e78d8789c9ed99c2cfa8059fad6e7a5c4ced288e21e` |

> **Informative Note:** Legacy `B03 (v1.1.0)` typeface folders (`Montserrat/`, `Inter/`, `JetBrains Mono/`) were archived unmodified to `99_Archive/` on `2026-11-26` upon `B03 (v2.0.0)` approval (`A02 §5.6.2`).

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
| `v2.0.0` | `2026-11-26` | Major | Migrated `06_Dependencies/Fonts/` from retired `B03 (v1.1.0)` packages (`Montserrat`, `Inter`, `JetBrains Mono`, archived to `99_Archive/`) to the `B03 (v2.0.0)` Noto Sans superfamily (`Noto Sans Display v2.003`, `Noto Sans v2.004`, `Noto Sans Mono v2.006`) with verified `SHA-256` checksums and `SIL OFL-1.1` attribution per `A02 (v1.2.0) §5.5.4`. | Hary Irfantri |
| `v1.0.0` | `2026-11-26` | Major | Initial approved baseline registering the three complete `B03` brand typeface packages (`Montserrat`, `Inter`, `JetBrains Mono` with variable fonts, `static/` suites, `OFL.txt`, and `README.txt`) and the `ISOcoated_v2_eci.icc` (`FOGRA39`) International Color Consortium (`ICC`) profile with verified `SHA-256` checksums and rights-holder attributions per `A02 (v1.2.0) §5.5.4`. | Hary Irfantri |
