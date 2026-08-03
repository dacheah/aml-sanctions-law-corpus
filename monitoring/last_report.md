# Source monitor report — 2026-08-03T21:30:40Z

_monitor v3.8 · schema mode off (whole-page fallback)_

10 changed · 3 suspect · 0 schema-suspect · 18 manual-review · 1 error · 60 total

## Schema-mode sources

- **AML/CTF Act 2006 — compilations (C2006A00169)** — ✅ unchanged (10 records)
- **AML/CTF Amendment Act 2024 (C2024A00110)** — ✅ unchanged (1 records)
- **AML/CTF Transitional Rules 2026 (F2026L00393)** — ✅ unchanged (3 records)
- **Charter of the United Nations Act 1945 (C1945A00032)** — ✅ unchanged (10 records)
- **Autonomous Sanctions Act 2011 (C2011A00038)** — ⚠️ TimeoutError: The read operation timed out
- **Autonomous Sanctions Regulations 2011 (F2011L02673)** — ✅ unchanged (10 records)
- **AML/CTF Rules 2025 — principal rules (F2025L01026, compilation F2026C00274)** — ✅ unchanged (2 records)
- **US 31 C.F.R. Part 1010 — FinCEN general provisions (eCFR)** — ✅ unchanged (157 records)

## 🔶 CHANGED (10)
- **UK Terrorism Act 2000 (c. 11) — revised**
    - was `sha256:20b7fff02ccd339ee4f0204a06d562c02a42b553b13541ecccba130118e6d7b5`
    - now `sha256:2587731b3978bec6511714a71c987cb59b47afa06de7786160ffd8e34432c478`
- **UN Convention against Transnational Organized Crime (Palermo/UNTOC 2000, UNODC)**
    - was `sha256:33b9d56fb358c37d6b543f80dfbca98f7c03698d1cd574d84ea3ad729b0bc60a`
    - now `sha256:8e9c9e305806111a720cc0c33b3c075a60fe21b00039ffff6e66fc9237ffa30c`
- **Canada — PCMLTFA (S.C. 2000, c. 17)**
    - was `sha256:2d59431c7d8c5683464a54b0a4a7459666238fd7d89c253d9684f9cd09642610`
    - now `sha256:8afa4beae069ac94a6b8e7ab951dea6c044ceb3a4d92d84f21b98004298ef62a`
- **Canada — PCMLTFR (SOR/2002-184)**
    - was `sha256:88da139f2fdfa2657c8202f0f28d1ce7055845d7d66cc27cb5dae40f3bb45422`
    - now `sha256:8a6fc3e5dea1255319e36e61f045b45f3d3ef51e75b7d885db54e544cd6033a3`
- **Canada — Criminal Code (R.S.C. 1985, c. C-46)**
    - was `sha256:f821200c8156c7a1830486fccbc5cf42c56f7e01e5a61991839f85ddc9aec72d`
    - now `sha256:9d6528752be4f22edf76a7d70df11fe452a6a0d8cfda7ec1ea03e6ce4a9e8336`
- **Canada — Special Economic Measures Act (S.C. 1992, c. 17)**
    - was `sha256:2e593128a1d611c62173dbf443090379865ece8e710e5f7b264b17475a186dab`
    - now `sha256:f08971b110995a686b8a2c1d34cb920d41a87cd850d92f50b2f276c38db21abb`
- **Canada — United Nations Act (R.S.C. 1985, c. U-2)**
    - was `sha256:12cdb67f2c245193c2c5c9ecac15d91165b674b85047bfa93e3b2fff6ab4cf00`
    - now `sha256:9c6ab9e83347a2d0d5326eb01d571deb8f1c1871325c7bd09f88e47184113dbe`
- **Canada — JVCFOA / Magnitsky (S.C. 2017, c. 21)**
    - was `sha256:727e7ee229adc321de27ef6e2fe99a8ec10297d66f1bd12361840d6427d756d4`
    - now `sha256:2c2188ccab9186995c185185acf8d97b88339ef4a5c9ae7427b5ef4ea4e11a06`
- **Canada — Freezing Assets of Corrupt Foreign Officials Act (S.C. 2011, c. 10)**
    - was `sha256:452a7868d78631a828de8b54cc01c958628f251e06e915ce9a26f58228cc86d6`
    - now `sha256:55c83be63aac7b4840b6103227effcf3a8d58f36a25551ec8a195386167b9433`
- **Japan — Criminal Proceeds Transfer Prevention Act (Act 22/2007)**
    - was `sha256:63bef3bcf9e429228fe8bc088bcc8315c1f5025dff5ec64db26634ae8c3abc6e`
    - now `sha256:34da2aebf142e1a38772db76c2be678c70636216d31e2a6d51e70ecc4ac37c97`

## 🟥 SUSPECT — content too short (shell/error?) (3)
- **UN Security Council Resolution 1267 (1999)**
- **UN Security Council Resolution 1373 (2001)**
- **UN Security Council Resolution 1540 (2004)**

## 🟠 MANUAL — JS-rendered source, auto-monitor cannot see the law (18)
- **FATF 40 Recommendations (standard)**
- **Switzerland — AMLA / GwG (SR 955.0)**
- **Switzerland — AMLO / GwV (SR 955.01)**
- **Switzerland — AMLO-FINMA / GwV-FINMA (SR 955.033.0)**
- **Switzerland — Criminal Code (SR 311.0)**
- **Switzerland — Embargo Act / EmbG (SR 946.231)**
- **Hong Kong — AMLO (Cap. 615)**
- **Hong Kong — OSCO (Cap. 455)**
- **Hong Kong — DTROP (Cap. 405)**
- **Hong Kong — UNATMO (Cap. 575)**
- **Hong Kong — UN Sanctions Ordinance (Cap. 537)**
- **Hong Kong — WMD(CPS)O (Cap. 526)**
- **Hong Kong — Cross-boundary Currency & BNI Ordinance (Cap. 629)**
- **UAE — Federal Decree-Law 10/2025 (AML/CTF/PF)**
- **UAE — Federal Decree-Law 20/2018 (superseded)**
- **UAE — Implementing Regulation (Cabinet Decision 10/2019)**
- **UAE — TFS mechanism (Cabinet Decision 74/2020)**
- **UAE — Combating Terrorism Crimes Law (7/2014)**

## ✅ unchanged (21)
- **UK Proceeds of Crime Act 2002 (c. 29) — revised**
- **UK Money Laundering Regulations 2017 (SI 2017/692) — revised**
- **UK Sanctions and Anti-Money Laundering Act 2018 (c. 13) — revised**
- **US Bank Secrecy Act — 31 U.S.C. ch. 53 subch. II (current)**
- **US IEEPA — 50 U.S.C. ch. 35 (current)**
- **EU 4AMLD — Directive (EU) 2015/849 (consolidated, EUR-Lex)**
- **EU AML Regulation 2024/1624 (AMLR, EUR-Lex)**
- **EU 6AMLD — Directive (EU) 2024/1640 (EUR-Lex)**
- **EU AMLA Regulation 2024/1620 (EUR-Lex)**
- **UN Vienna Convention 1988 (UNODC)**
- **UN International Convention for the Suppression of the Financing of Terrorism (1999, UNODC)**
- **UN Convention against Corruption (UNCAC/Mérida 2003, UNODC)**
- **Singapore — CDSA (Act 29 of 1992)**
- **Singapore — TSOFA (Act 16 of 2002)**
- **Singapore — United Nations Act 2001 (Act 44 of 2001)**
- **Singapore — UN (Anti-Terrorism Measures) Regs (Rg 1)**
- **Singapore — Precious Stones and Precious Metals Act 2019 (Act 7 of 2019)**
- **Japan — Organized Crime Punishment Act (Act 136/1999)**
- **Japan — Terrorist Financing Punishment Act (Act 67/2002)**
- **Japan — FEFTA (Act 228/1949)**
- **Japan — International Terrorist Asset-Freezing Act (Act 124/2014)**

_Automation only watches and queues. A flag may be a genuinely new or amended instrument OR a cosmetic page update — the maintainer triages. **MANUAL** sources are JavaScript apps a stdlib fetch cannot see. **SUSPECT** means too little text to trust. **SCHEMA SUSPECT** means selectors probably broke. Nothing is ingested automatically._
