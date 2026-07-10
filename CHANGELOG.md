# Changelog

All notable changes to this corpus are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning is
[Semantic Versioning](https://semver.org/) adapted for a legal corpus:

- **major** — a new jurisdiction, or a breaking change to the schema, layout, or the two-layer wall;
- **minor** — new instruments, new dated versions of existing instruments, or new derived features;
- **patch** — fidelity corrections, provenance fixes, and non-substantive tooling changes.

The `authoritative/` layer is append-only: a correction or amendment is always a **new dated version**,
never an in-place edit.

## [Unreleased]

_Nothing yet._

## [1.3.2] — 2026-07-10

Implements the UAE **authentic-Arabic OCR pass** scoped in 1.3.0. No authoritative texts change.

### Added

- A **derived OCR Arabic text layer** for the three UAE records that preserve an authentic Arabic source
  (`derived/<id>/<version>/authentic-text-ar.txt`, registered as an `ocr_authentic_text` artifact with a
  sidecar of metrics). Produced with Tesseract (`ara`) from the preserved `authentic-source-ar.pdf` — the
  route the 1.3.0 deep-dive identified, since glyph extraction corrupts Arabic. It is readable and correctly
  ordered but **unofficial and unverified**; in place of a cross-engine gate (unavailable for Arabic) each
  record records an OCR **self-consistency** metric (300-dpi vs 400-dpi character agreement, ≈ 0.995–0.998).
- The authentic Arabic is now rendered on the UAE site pages (right-to-left, under an "OCR · unofficial ·
  unverified" label) and included in the Hugging Face export as an `authentic_text_ar` field.
- New toolkit module `scripts/ocr_arabic.py`; the derived-metadata schema gains the `ocr_authentic_text`
  type, an `ocr` generation method, and a `source_authentic_sha256` field.

## [1.3.1] — 2026-07-10

Derived-layer refresh: the concept vocabulary and FATF crosswalk now reflect the corpus's broadened scope.
No authoritative texts change.

### Added

- Two neutral concepts — **`proliferation_financing`** (FATF R.7 / UNSCR 1540) and **`cash_couriers`**
  (FATF R.32) — with curated tags on the relevant provisions (UNSCR 1540, Hong Kong WMD(CPS)O and Japan
  FEFTA export controls for proliferation; the Australian AML/CTF Act cross-border-movement Part and Hong
  Kong's Cross-boundary Currency Ordinance (Cap. 629) for cash couriers).

### Changed

- The FATF crosswalk now shows **R.7 (proliferation-related TFS)** against the actual WMD/proliferation
  instruments and **R.32 (cash couriers)** as *in scope* — previously R.32 read as "outside v1 scope"
  despite the instruments being present. Out-of-scope Recommendations drop from 12 to 11 (the remainder —
  institutional bodies, NPOs, secrecy laws, and the R.36–40 cooperation set already shown via their UN
  treaty basis — are correctly not captured as national instruments).

## [1.3.0] — 2026-07-10

Adds three more national branches — **Hong Kong, Japan and the United Arab Emirates** — taking the corpus to
ten cross-referenced jurisdictions, and extends the FATF crosswalk to ten national columns. Introduces the
corpus's first CJK branch (Japan) and its first non-Latin-script handling (UAE).

### Added

- **Hong Kong branch** (`HKG`, 7 records) — the Anti-Money Laundering and Counter-Terrorist Financing
  Ordinance (Cap. 615), OSCO (Cap. 455, incl. the s.25 ML offence and s.25A STR), DTROP (Cap. 405), UNATMO
  (Cap. 575), the UN Sanctions Ordinance (Cap. 537), the WMD (Control of Provision of Services) Ordinance
  (Cap. 526) and the Cross-boundary Currency and BNI Ordinance (Cap. 629). English "Verified Copy" texts
  from e-Legislation; English is authentic.
- **Japan branch** (`JPN`, 5 records) — the Criminal Proceeds Transfer Prevention Act, the Organized Crime
  Punishment Act (ML offences), the Terrorist Financing Punishment Act, FEFTA (sanctions) and the
  International Terrorist Asset-Freezing Act. Captured as the **authentic Japanese** from e-Gov under an open
  (CC BY-compatible) licence. New CJK extraction profile and a 第N条 segmenter with kanji-numeral conversion;
  every record verifies at full token and character coverage.
- **United Arab Emirates branch** (`ARE`, 5 records) — Federal Decree-Law 10/2025 (and the superseded
  20/2018), the 2019 Implementing Regulation, the 2020 targeted-financial-sanctions Cabinet Decision, and the
  2014 Combating Terrorism Crimes Law. Captured as the **official English translation** (see below), with the
  authentic Arabic preserved per record.
- New extraction profiles in `extract.py` (Hong Kong e-Legislation; Japan CJK; UAE English via poppler) and
  new segmenters. Reproducibility is now **65 of 68** text-bearing records byte-exact.
- Curated concept tags on the marquee provisions of all three branches; the **FATF crosswalk extended to ten
  national columns**.
- **Schema:** a new `authoritative_status: official_translation`, and an `authentic_source` block that
  records a preserved authentic-language source file (its bytes and hash) when the stored text is a
  translation.

### Notes

- **Arabic extraction (UAE).** The UAE's authentic Arabic PDFs store glyphs in visual order and do not
  extract to faithful logical-order text with any available PDF text engine (PyMuPDF garbles them; even
  poppler transposes the article marker and reverses numbers). A deep-dive found that **Tesseract OCR with
  the Arabic pack** does produce correctly-ordered text (with minor OCR noise) — the route to authentic
  Arabic text in future. For now the corpus stores the official English translation (cleanly verifiable) and
  **preserves the authentic Arabic PDF byte-exact inside each record** (`authentic_source`) for that future
  OCR pass. Arabic cannot be cross-engine verified (only one engine reads it at all), so the Arabic is
  preserved-but-not-text-verified; the stored English is fully verified.

## [1.2.1] — 2026-07-10

Completes the Canada branch and corrects the Swiss article numbering.

### Added

- **Canada — Freezing Assets of Corrupt Foreign Officials Act** (S.C. 2011, c. 10; `ca/act/facfoa`), the
  remaining sanctions statute (freezing politically-exposed foreign persons' assets at a foreign state's
  request), `extracted_verified`. Canada is now seven records.

### Fixed

- **Swiss article numbering.** Fedlex PDFs flatten superscript footnote digits onto plain article numbers,
  so the derived structure previously mis-numbered some Swiss articles (e.g. AMLA Art. 1 as "15"). The Swiss
  structure layer now relabels articles positionally against the authentic Fedlex **Akoma-Ntoso XML** order,
  giving clean numbers (1, 2, 2a, 2b, 3, 4, 5, 6, …). The authoritative texts and hashes are unchanged —
  this affects only the derived structure layer.

### Changed

- Swiss curated concept tags enriched now that article numbering is reliable: the crosswalk's Switzerland
  column covers customer due diligence, beneficial ownership, record-keeping, the AML programme, suspicious-
  transaction reporting and asset-freezing (AMLA Arts. 3–12), not only the Criminal Code offences.

## [1.2.0] — 2026-07-10

Adds three national branches — **Canada, Singapore and Switzerland** — taking the corpus to seven
cross-referenced jurisdictions over the UN + FATF international backbone, and extends the FATF crosswalk to
seven columns.

### Added

- **Canada branch** (`CAN`, 6 records) — the Proceeds of Crime (Money Laundering) and Terrorist Financing
  Act and its Regulations, the Criminal Code money-laundering (s. 462.31) and terrorist-financing
  (ss. 83.02–83.04) offences, the Special Economic Measures Act, the United Nations Act, and the Justice for
  Victims of Corrupt Foreign Officials Act (Magnitsky). English captured from the bilingual Justice Laws
  consolidations by word-level column separation.
- **Singapore branch** (`SGP`, 5 records) — the Corruption, Drug Trafficking and Other Serious Crimes
  (Confiscation of Benefits) Act, the Terrorism (Suppression of Financing) Act, the United Nations Act and
  its Anti-Terrorism Measures Regulations, and the Precious Stones and Precious Metals Act. From Singapore
  Statutes Online.
- **Switzerland branch** (`CHE`, 5 records) — the Anti-Money Laundering Act (GwG) and Ordinance (GwV), the
  FINMA AML Ordinance, the Criminal Code AML/CTF articles (305bis/305ter/260quinquies/260ter), and the
  Embargo Act (EmbG). Captured as the **authentic German** consolidation from Fedlex (English on Fedlex is
  non-authentic); Swiss federal law is not copyright-protected.
- New extraction profiles in `extract.py` (Canada bilingual English-column word-level; Singapore SSO
  single-column; Switzerland Fedlex German single-column) and committed Criminal-Code section slices for the
  Canadian and Swiss offence extracts. Reproducibility is now **47 of 50** text-bearing records byte-exact.
- Curated concept tags on the marquee provisions of all three branches, and the **FATF crosswalk extended to
  seven national columns** (AU · UK · US · EU · CA · SG · CH) beneath the UN treaty basis.

### Changed

- `docs/methodology.md` §6 records the Canada/Singapore/Switzerland scope decision (dated) with the
  bilingual-capture, informal-consolidation and authentic-German notes; the browsable site lists the three
  new branches and the crosswalk renders seven columns.
- `monitoring/sources.json` extended with the Canadian, Singaporean and Swiss source pages.

### Notes

- Two Swiss records verify at 0.9946–0.9948 forward coverage — marginally below the 0.995 English-calibrated
  gate — because German long compounds tokenise differently between the comparison engines; a manual diff
  confirms the residual is real source text (no fabrication), recorded in each `verification` block.

## [1.1.0] — 2026-07-09

Adds the **UN backbone** — the international treaty and Security Council root beneath the FATF standard —
and makes the FATF crosswalk *vertical* (UN instrument → FATF Recommendation → national provision).

### Added

- **UN backbone branch** (`jurisdiction: international`) — seven authoritative records (authentic text,
  open — UN official documents are freely reproducible with attribution): the UN Convention against Illicit
  Traffic in Narcotic Drugs and Psychotropic Substances (Vienna, 1988), the UN Convention against
  Transnational Organized Crime (Palermo / UNTOC, 2000), the International Convention for the Suppression of
  the Financing of Terrorism (1999), UN Security Council Resolutions 1267 (1999), 1373 (2001) and 1540
  (2004), and the UN Convention against Corruption (UNCAC / Mérida, 2003). All seven are `extracted_verified`
  by independent cross-engine re-extraction and reproduced byte-exact by `extract.py`.
- **Vertical "UN treaty basis" dimension** in the FATF crosswalk — each Recommendation now shows the root UN
  instrument(s) it restates *above* the AU/UK/US/EU columns (fixed human-curated mapping), making the chain
  visible root-to-implementation and restoring the international-cooperation Recommendations (R.36–40) to
  coverage through their treaty root.
- Curated concept tags on the marquee UN provisions (Vienna Art. 3/5; Palermo Art. 6/7/12; TF Convention
  Art. 2/8/18; UNCAC Art. 14/23/31/52; the key operative paragraphs of UNSCR 1267/1373/1540).
- UN extraction profiles in `extract.py` (single-column UN PDF + full-document UN HTML); reproducibility is
  now **31 of 34** text-bearing records byte-exact (all seven UN records included).

### Changed

- `docs/methodology.md` — §6 records the UN backbone scope decision (dated) with the multilingual and
  free-reproduction notes; §8 documents the UN-treaty-basis crosswalk dimension.
- The browsable site now groups the landing page **by jurisdiction** (the international UN + FATF backbone,
  then the Australia, UK, US and EU branches) rather than by document type — mirroring the corpus's
  never-merged-branches principle — and the crosswalk page renders the UN treaty basis per Recommendation.
- `monitoring/sources.json` extended with the seven UN source pages (22 sources total).

### Fixed

- The UN treaty structure segmenter now recovers article headings that the source PDFs rendered without
  their "Article N" prefix, by anchoring to the table-of-contents sequence: the Vienna Convention now
  segments into 33 of 34 articles (was 28) and the Palermo Convention captures its bundled Protocols without
  article-number collisions. The authoritative texts are unchanged (append-only); this affects only the
  derived structure layer.

## [1.0.1] — 2026-07-09

Maintenance release: a citable DOI and reproducible extraction. The authoritative texts and their hashes
are **unchanged** from 1.0.0 (append-only) — this release is tooling, metadata, and documentation only.

### Added

- `.zenodo.json` — deposit metadata so each GitHub release auto-archives to Zenodo and mints a DOI.
- `CHANGELOG.md` — this changelog (Keep a Changelog format).
- **Reproducible extraction** — the toolkit's `extract.py` re-derives every `text.txt` from its byte-exact
  original using committed per-jurisdiction profiles (AU DOCX; UK/US/EU PDF, incl. the US two-column and EU
  letter-spacing handling; US eCFR HTML), and checks each result's SHA-256 against the stored hash. It
  reproduces **24 of the 27** text-bearing records byte-exact; three early Australian records predate the
  module and differ only in blank-line placement (equivalent content, retained as stored).

### Changed

- `docs/methodology.md` §4 now documents the reproducible-extraction method and its 24/27 result.

## [1.0.0] — 2026-07-09

Initial public release. A neutral, provenance-first, machine-readable record of anti-money-laundering /
counter-terrorism-financing (AML/CTF) and financial-sanctions **law**, on the FATF standard as backbone,
covering four fidelity-verified jurisdictions as separate, cross-referenced branches — never merged.

### Added

**Jurisdictions & coverage (28 authoritative records)**

- **Australia** — Anti-Money Laundering and Counter-Terrorism Financing Act 2006 (three point-in-time
  states), the Amendment Act 2024, the AML/CTF Rules 2025 and Transitional Rules 2026, and the sanctions
  branch (Charter of the United Nations Act 1945; Autonomous Sanctions Act 2011 + Regulations 2011).
- **United Kingdom** — Proceeds of Crime Act 2002, Terrorism Act 2000, the Money Laundering Regulations
  2017, the Sanctions and Anti-Money Laundering Act 2018, and the Economic Crime Acts 2022 and 2023.
- **United States** — the Bank Secrecy Act (31 U.S.C. §§5311–5336, incl. the Corporate Transparency Act),
  the money-laundering offences (18 U.S.C. §§1956–1957), the terrorist-financing offences (18 U.S.C.
  §§2339A–2339C), IEEPA (50 U.S.C. ch. 35), and 31 C.F.R. Part 1010 (FinCEN general provisions).
- **European Union** — the Fourth AML Directive (Directive (EU) 2015/849, consolidated) and the 2024 AML
  package: the AML Regulation (2024/1624), the Sixth Directive (2024/1640), and the AMLA Regulation
  (2024/1620).
- **International** — the FATF 40 Recommendations, under a restricted posture (citation + hash + short
  attributed excerpt; full text withheld).

**Provenance & integrity**

- Full provenance on every authoritative text: source URL, retrieval date, official citation, issuing body,
  jurisdiction, legal status, redistribution posture, and SHA-256 of both the byte-exact original and the
  stored text.
- A strict wall between `authoritative/` (official texts) and `derived/` (everything generated), enforced by
  folder, schema, and validator. Append-only dated versions.
- **Every text `extracted_verified`** by independent cross-engine re-extraction (LibreOffice vs python-docx
  for DOCX; poppler `pdftotext` vs PyMuPDF for PDF; an independent parse for HTML), with the agreement
  metrics recorded in each record's `verification` block.

**Derived layer**

- Deterministic structure extraction, a neutral concept vocabulary (curated on marquee provisions, keyword
  fallback elsewhere), a commencement/version timeline for the Australian reform, and a **four-way FATF
  crosswalk** mapping each Recommendation to the AU/UK/US/EU provisions that address it.

**Distribution & automation**

- A dependency-free browsable static site (GitHub Pages), including a browse-by-concept index and the
  browse-by-Recommendation crosswalk.
- A Hugging Face dataset export of the open layers (documents + provisions).
- GitHub Actions: schema/wall/hash validation on every push, and a weekly monitor watching 15 official
  source pages across all four jurisdictions.
- JSON Schemas, methodology, concept-vocabulary, restricted-source and monitoring documentation, a
  contributing/maintainer guide, and per-source licensing (`LICENSE` / `NOTICE`).

### Notes

- The private construction toolkit (ingestion, build, and verification scripts) is kept out of this
  repository by design; the corpus remains independently verifiable from the published originals, texts,
  hashes, and open schemas.
- This is a reference record of the law — **not legal or compliance advice** — and takes no position on any
  matter, institution, or investigation.

[Unreleased]: https://github.com/dacheah/aml-sanctions-law-corpus/compare/v1.3.2...HEAD
[1.3.2]: https://github.com/dacheah/aml-sanctions-law-corpus/releases/tag/v1.3.2
[1.3.1]: https://github.com/dacheah/aml-sanctions-law-corpus/releases/tag/v1.3.1
[1.3.0]: https://github.com/dacheah/aml-sanctions-law-corpus/releases/tag/v1.3.0
[1.2.1]: https://github.com/dacheah/aml-sanctions-law-corpus/releases/tag/v1.2.1
[1.2.0]: https://github.com/dacheah/aml-sanctions-law-corpus/releases/tag/v1.2.0
[1.1.0]: https://github.com/dacheah/aml-sanctions-law-corpus/releases/tag/v1.1.0
[1.0.1]: https://github.com/dacheah/aml-sanctions-law-corpus/releases/tag/v1.0.1
[1.0.0]: https://github.com/dacheah/aml-sanctions-law-corpus/releases/tag/v1.0.0
