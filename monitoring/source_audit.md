# Source URL audit — 2026-07-22T06:15:04Z

37 ok · 2 need review · 4 broken · 17 manual (declared unfetchable)

Advisory only — nothing was changed. A REDIRECT is not automatically wrong (sites move pages legitimately) but must be confirmed to still be the intended target. A title mismatch means the page may not be what the source claims to watch.

**A clean audit means no broken plumbing — not that every source watches the right page.** A URL resolving cleanly to a real but wrong page passes this tool UNLESS the source declares an `expect_contains` anchor (a stable string the right page must carry). Without an anchor, only a human reading the page catches a wrong-page.

**Anchor coverage: 0/60 sources declare an `expect_contains` anchor.** The remaining 60 are checked for plumbing only (HTTP status, redirects, title) and would NOT be caught resolving to a wrong page. Adding anchors to those is the durable fix for the resolving-but-wrong-page class (see the source-verification task).

## ⛔ BROKEN (4)

- **FATF 40 Recommendations (standard)**
    - `https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html`
    - could not be fetched — HTTPError: HTTP Error 403: Forbidden
- **US Bank Secrecy Act — 31 U.S.C. ch. 53 subch. II (current)**
    - `https://uscode.house.gov/view.xhtml?path=/prelim@title31/subtitle4/chapter53/subchapter2&edition=prelim`
    - could not be fetched — URLError: <urlopen error [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond>
- **US IEEPA — 50 U.S.C. ch. 35 (current)**
    - `https://uscode.house.gov/view.xhtml?path=/prelim@title50/chapter35&edition=prelim`
    - could not be fetched — URLError: <urlopen error [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond>
- **Canada — Criminal Code (R.S.C. 1985, c. C-46)**
    - `https://laws-lois.justice.gc.ca/eng/acts/C-46/`
    - could not be fetched — ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host

## 🔶 REVIEW (2)

- **Canada — PCMLTFA (S.C. 2000, c. 17)**
    - `https://laws-lois.justice.gc.ca/eng/acts/P-24.501/`
    - page title 'Proceeds of Crime (Money Laundering) and Terrorist Financing Act' does not resemble the source name
- **Canada — PCMLTFR (SOR/2002-184)**
    - `https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-184/`
    - page title 'Proceeds of Crime (Money Laundering) and Terrorist Financing Regulations' does not resemble the source name

## 🟠 MANUAL (declared unfetchable — checked by hand) (17)

- **Switzerland — AMLA / GwG (SR 955.0)**
    - `https://www.fedlex.admin.ch/eli/cc/1998/892_892_892/de`
    - declared manual (render:spa or monitor:manual) — checked by hand, not auto-fetched
- **Switzerland — AMLO / GwV (SR 955.01)**
    - `https://www.fedlex.admin.ch/eli/cc/2015/791/de`
    - declared manual (render:spa or monitor:manual) — checked by hand, not auto-fetched
- **Switzerland — AMLO-FINMA / GwV-FINMA (SR 955.033.0)**
    - `https://www.fedlex.admin.ch/eli/cc/2015/390/de`
    - declared manual (render:spa or monitor:manual) — checked by hand, not auto-fetched
- **Switzerland — Criminal Code (SR 311.0)**
    - `https://www.fedlex.admin.ch/eli/cc/54/757_781_799/de`
    - declared manual (render:spa or monitor:manual) — checked by hand, not auto-fetched
- **Switzerland — Embargo Act / EmbG (SR 946.231)**
    - `https://www.fedlex.admin.ch/eli/cc/2002/564/de`
    - declared manual (render:spa or monitor:manual) — checked by hand, not auto-fetched
- **Hong Kong — AMLO (Cap. 615)**
    - `https://www.elegislation.gov.hk/hk/cap615`
    - declared manual (render:spa or monitor:manual) — checked by hand, not auto-fetched
- **Hong Kong — OSCO (Cap. 455)**
    - `https://www.elegislation.gov.hk/hk/cap455`
    - declared manual (render:spa or monitor:manual) — checked by hand, not auto-fetched
- **Hong Kong — DTROP (Cap. 405)**
    - `https://www.elegislation.gov.hk/hk/cap405`
    - declared manual (render:spa or monitor:manual) — checked by hand, not auto-fetched
- **Hong Kong — UNATMO (Cap. 575)**
    - `https://www.elegislation.gov.hk/hk/cap575`
    - declared manual (render:spa or monitor:manual) — checked by hand, not auto-fetched
- **Hong Kong — UN Sanctions Ordinance (Cap. 537)**
    - `https://www.elegislation.gov.hk/hk/cap537`
    - declared manual (render:spa or monitor:manual) — checked by hand, not auto-fetched
- **Hong Kong — WMD(CPS)O (Cap. 526)**
    - `https://www.elegislation.gov.hk/hk/cap526`
    - declared manual (render:spa or monitor:manual) — checked by hand, not auto-fetched
- **Hong Kong — Cross-boundary Currency & BNI Ordinance (Cap. 629)**
    - `https://www.elegislation.gov.hk/hk/cap629`
    - declared manual (render:spa or monitor:manual) — checked by hand, not auto-fetched
- **UAE — Federal Decree-Law 10/2025 (AML/CTF/PF)**
    - `https://uaelegislation.gov.ae/en/legislations/3314`
    - declared manual (render:spa or monitor:manual) — checked by hand, not auto-fetched
- **UAE — Federal Decree-Law 20/2018 (superseded)**
    - `https://uaelegislation.gov.ae/en/legislations/1016`
    - declared manual (render:spa or monitor:manual) — checked by hand, not auto-fetched
- **UAE — Implementing Regulation (Cabinet Decision 10/2019)**
    - `https://uaelegislation.gov.ae/en/legislations/1015`
    - declared manual (render:spa or monitor:manual) — checked by hand, not auto-fetched
- **UAE — TFS mechanism (Cabinet Decision 74/2020)**
    - `https://uaelegislation.gov.ae/en/legislations/2198`
    - declared manual (render:spa or monitor:manual) — checked by hand, not auto-fetched
- **UAE — Combating Terrorism Crimes Law (7/2014)**
    - `https://uaelegislation.gov.ae/en/legislations/1018`
    - declared manual (render:spa or monitor:manual) — checked by hand, not auto-fetched

## ✅ OK (37)

- **AML/CTF Act 2006 — compilations (C2006A00169)**
    - `https://api.prod.legislation.gov.au/v1/Versions?%24filter=titleId%20eq%20%27C2006A00169%27&%24orderby=start%20desc&%24top=10&%24select=titleId%2CcompilationNumber%2Cstart%2Cend%2CregisteredAt`
    - ''
- **AML/CTF Amendment Act 2024 (C2024A00110)**
    - `https://api.prod.legislation.gov.au/v1/Versions?%24filter=titleId%20eq%20%27C2024A00110%27&%24orderby=start%20desc&%24top=10&%24select=titleId%2CcompilationNumber%2Cstart%2Cend%2CregisteredAt`
    - ''
- **AML/CTF Transitional Rules 2026 (F2026L00393)**
    - `https://api.prod.legislation.gov.au/v1/Versions?%24filter=titleId%20eq%20%27F2026L00393%27&%24orderby=start%20desc&%24top=10&%24select=titleId%2CcompilationNumber%2Cstart%2Cend%2CregisteredAt`
    - ''
- **Charter of the United Nations Act 1945 (C1945A00032)**
    - `https://api.prod.legislation.gov.au/v1/Versions?%24filter=titleId%20eq%20%27C1945A00032%27&%24orderby=start%20desc&%24top=10&%24select=titleId%2CcompilationNumber%2Cstart%2Cend%2CregisteredAt`
    - ''
- **Autonomous Sanctions Act 2011 (C2011A00038)**
    - `https://api.prod.legislation.gov.au/v1/Versions?%24filter=titleId%20eq%20%27C2011A00038%27&%24orderby=start%20desc&%24top=10&%24select=titleId%2CcompilationNumber%2Cstart%2Cend%2CregisteredAt`
    - ''
- **Autonomous Sanctions Regulations 2011 (F2011L02673)**
    - `https://api.prod.legislation.gov.au/v1/Versions?%24filter=titleId%20eq%20%27F2011L02673%27&%24orderby=start%20desc&%24top=10&%24select=titleId%2CcompilationNumber%2Cstart%2Cend%2CregisteredAt`
    - ''
- **AML/CTF Rules 2025 — principal rules (F2025L01026, compilation F2026C00274)**
    - `https://api.prod.legislation.gov.au/v1/Versions?%24filter=titleId%20eq%20%27F2025L01026%27&%24orderby=start%20desc&%24top=10&%24select=titleId%2CcompilationNumber%2Cstart%2Cend%2CregisteredAt`
    - ''
- **UK Proceeds of Crime Act 2002 (c. 29) — revised**
    - `https://www.legislation.gov.uk/ukpga/2002/29/contents`
    - 'Proceeds of Crime Act 2002'
- **UK Terrorism Act 2000 (c. 11) — revised**
    - `https://www.legislation.gov.uk/ukpga/2000/11/contents`
    - 'Terrorism Act 2000'
- **UK Money Laundering Regulations 2017 (SI 2017/692) — revised**
    - `https://www.legislation.gov.uk/uksi/2017/692/contents`
    - 'The Money Laundering, Terrorist Financing and Transfer of Funds (Information on the Payer) Regulations 2017'
- **UK Sanctions and Anti-Money Laundering Act 2018 (c. 13) — revised**
    - `https://www.legislation.gov.uk/ukpga/2018/13/contents`
    - 'Sanctions and Anti-Money Laundering Act 2018'
- **US 31 C.F.R. Part 1010 — FinCEN general provisions (eCFR)**
    - `https://www.ecfr.gov/api/versioner/v1/versions/title-31.json?part=1010`
    - ''
- **EU 4AMLD — Directive (EU) 2015/849 (consolidated, EUR-Lex)**
    - `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02015L0849-20241230`
    - ''
- **EU AML Regulation 2024/1624 (AMLR, EUR-Lex)**
    - `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1624`
    - ''
- **EU 6AMLD — Directive (EU) 2024/1640 (EUR-Lex)**
    - `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024L1640`
    - ''
- **EU AMLA Regulation 2024/1620 (EUR-Lex)**
    - `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1620`
    - ''
- **UN Vienna Convention 1988 (UNODC)**
    - `https://www.unodc.org/pdf/convention_1988_en.pdf`
    - ''
- **UN Convention against Transnational Organized Crime (Palermo/UNTOC 2000, UNODC)**
    - `https://www.unodc.org/unodc/en/organized-crime/intro/UNTOC.html`
    - 'United Nations Convention against Transnational Organized Crime'
- **UN International Convention for the Suppression of the Financing of Terrorism (1999, UNODC)**
    - `https://www.unodc.org/documents/treaties/Special/1999%20International%20Convention%20for%20the%20Suppression%20of%20the%20Financing%20of%20Terrorism.pdf`
    - ''
- **UN Security Council Resolution 1267 (1999)**
    - `https://docs.un.org/S/RES/1267(1999)`
    - 'Select a language for S/RES/1267(1999)'
- **UN Security Council Resolution 1373 (2001)**
    - `https://docs.un.org/S/RES/1373(2001)`
    - 'Select a language for S/RES/1373(2001)'
- **UN Security Council Resolution 1540 (2004)**
    - `https://docs.un.org/S/RES/1540(2004)`
    - 'Select a language for S/RES/1540(2004)'
- **UN Convention against Corruption (UNCAC/Mérida 2003, UNODC)**
    - `https://www.unodc.org/documents/treaties/UNCAC/Publications/Convention/08-50026_E.pdf`
    - ''
- **Canada — Special Economic Measures Act (S.C. 1992, c. 17)**
    - `https://laws-lois.justice.gc.ca/eng/acts/S-14.5/`
    - 'Special Economic Measures Act'
- **Canada — United Nations Act (R.S.C. 1985, c. U-2)**
    - `https://laws-lois.justice.gc.ca/eng/acts/U-2/`
    - 'United Nations Act'
- **Canada — JVCFOA / Magnitsky (S.C. 2017, c. 21)**
    - `https://laws-lois.justice.gc.ca/eng/acts/J-2.3/`
    - 'Justice for Victims of Corrupt Foreign Officials Act (Sergei Magnitsky Law)'
- **Singapore — CDSA (Act 29 of 1992)**
    - `https://sso.agc.gov.sg/Act/CDTOSCCBA1992`
    - 'Corruption, Drug Trafficking and Other Serious Crimes (Confiscation of Benefits) Act 1992'
- **Singapore — TSOFA (Act 16 of 2002)**
    - `https://sso.agc.gov.sg/Act/TSFA2002`
    - 'Terrorism (Suppression of Financing) Act 2002'
- **Singapore — United Nations Act 2001 (Act 44 of 2001)**
    - `https://sso.agc.gov.sg/Act/UNA2001`
    - 'United Nations Act 2001'
- **Singapore — UN (Anti-Terrorism Measures) Regs (Rg 1)**
    - `https://sso.agc.gov.sg/SL/UNA2001-RG1`
    - 'United Nations (Anti-terrorism Measures) Regulations'
- **Singapore — Precious Stones and Precious Metals Act 2019 (Act 7 of 2019)**
    - `https://sso.agc.gov.sg/Act/PSPMPMLTFPFA2019`
    - 'Precious Stones and Precious Metals (Prevention of Money Laundering, Terrorism Financing and Proliferation Financing) Act 2019'
- **Canada — Freezing Assets of Corrupt Foreign Officials Act (S.C. 2011, c. 10)**
    - `https://laws-lois.justice.gc.ca/eng/acts/F-31.6/`
    - 'Freezing Assets of Corrupt Foreign Officials Act'
- **Japan — Criminal Proceeds Transfer Prevention Act (Act 22/2007)**
    - `https://laws.e-gov.go.jp/api/1/lawdata/419AC0000000022`
    - ''
- **Japan — Organized Crime Punishment Act (Act 136/1999)**
    - `https://laws.e-gov.go.jp/api/1/lawdata/411AC0000000136`
    - ''
- **Japan — Terrorist Financing Punishment Act (Act 67/2002)**
    - `https://laws.e-gov.go.jp/api/1/lawdata/414AC0000000067`
    - ''
- **Japan — FEFTA (Act 228/1949)**
    - `https://laws.e-gov.go.jp/api/1/lawdata/324AC0000000228`
    - ''
- **Japan — International Terrorist Asset-Freezing Act (Act 124/2014)**
    - `https://laws.e-gov.go.jp/api/1/lawdata/426AC0000000124`
    - ''

