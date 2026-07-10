# Methodology

How this corpus is organised and governed. The governing principle is simple: **provenance and version
integrity override convenience, always.** Every authoritative text can be traced to its official source
and checked for tampering; every change is a new dated version; nothing generated is ever presented as
authoritative.

## 1. Two-layer wall

- **`authoritative/`** — primary source texts only, in their authentic language, with full provenance.
  The legal record. No machine- or human-generated interpretation, ever. **Append-only.**
- **`derived/`** — everything generated (structure, concept tags, the version timeline). Unofficial,
  labelled, and traceable to a specific authoritative version by its text hash. Regenerable.

The wall is enforced by folder location, by the schemas, and by a validator. Where a file lives tells you
what it is.

## 2. Provenance schema

Every authoritative document version carries, before it enters the corpus: `corpus_id`, `version_id`,
`title`, `jurisdiction`, `document_type`, `official_citation`, `authentic_languages` / `language`,
`source_url`, `source_publisher`, `source_is_official`, `retrieval_date`, `retrieved_by`,
`original_format`/`original_filename`, `original_sha256`, `text_sha256` / `content_hash`, `text_fidelity`,
`authoritative_status`, `legal_status`, `redistribution`, `license` / `rights_note`, `capture_history`,
supersedes/superseded_by links, and a `provenance_note`. Optional `verification` and `corrections` records
are added after checks. The machine-checkable definition is in `schema/authoritative-metadata.schema.json`.

Three distinct axes are never conflated:

| Axis | Field | Question |
|---|---|---|
| Capture accuracy | `text_fidelity` | Was the source transcribed faithfully? |
| Text authenticity | `authoritative_status` | Is this the authentic/official text? |
| Legal force | `legal_status` | Does it bind (binding), or is it guidance / soft-law? |

`jurisdiction` is a first-class dimension (ISO 3166-1 alpha-3 for national instruments; `international`
for the FATF standard) — jurisdictions are cross-referenced, never merged.

## 3. Identifiers & point-in-time versioning

A stable internal `corpus_id` (`<jurisdiction-or-authority>/<type>/<slug>-<year>`) is the key external
references depend on; the official Federal Register registration numbers (C-numbers for Acts and
compilations, F-numbers for legislative instruments) are captured as first-class provenance. `version_id`
is the date a textual state took effect. The citable spine is the **official point-in-time compilation**
captured at each in-force date; as-made instruments are captured for lineage. Every change is a new dated
version — nothing is overwritten.

## 4. Authoritative-text policy

The Federal Register of Legislation is the authority for Australian legislation (`source_is_official:
true`); `legislation.gov.uk` (The National Archives) is the authority for UK legislation; regulator copies
are secondary. Texts are reproduced faithfully, including source defects, and the fidelity flag is only
upgraded after a real check against the official source. Gaps are flagged, not filled.

**Fidelity verification (independent cross-engine extraction).** `text_fidelity` is upgraded to
`extracted_verified` only after the stored text is re-derived from the byte-exact original by a *second,
independent* engine and the two agree. Each original is re-extracted with a different tool from the one
used at ingest — DOCX via LibreOffice's converter (vs `python-docx`), PDF via poppler's `pdftotext` (vs
PyMuPDF) — and compared by order-robust multiset token coverage: `unigram_forward` (share of stored tokens
present in the independent extraction — the fabrication check), `bigram_forward` (ordered-pair agreement —
the sequence check), and `unigram_reverse` (completeness proxy). The recorded metrics and the engine used
are stored in each record's `verification` block. For the UK PDFs the reverse direction is intentionally
below 1.0 because this corpus removes per-page furniture (running headers, the repeated "Changes to
legislation" banner) that `pdftotext` retains; a token-level diff confirmed that residual is furniture, not
substantive text. Verification is by tooling, not eye; a stronger `verbatim_transcription` flag is reserved
for line-by-line human certification.

**Reproducible extraction.** Each `text.txt` is derived from its byte-exact original by committed code, not
ad-hoc steps: the toolkit's `extract.py` holds one profile per jurisdiction/format (AU DOCX; UK/US/EU/UN
PDF, with the US two-column, EU/UN letter-spacing handling, and UN furniture removal; US eCFR HTML and UN
full-document HTML) and re-derives every text on demand, comparing the result's SHA-256 to the stored hash.
It reproduces 30 of the 33 text-bearing v1 records byte-exact — including all six UN backbone records; three
early Australian records predate the module and differ only in blank-line placement (equivalent content,
retained as stored under the append-only rule). From v1.1 on, `extract.py` is the canonical extraction for
every new capture.

## 5. Licensing & the restricted posture

Commonwealth legislation is CC BY 4.0 (open) — the publishable core. FATF material is copyright-restricted:
it is represented as `authoritative_status: restricted_withheld` with `redistribution: restricted` — hash
+ citation + short attributed excerpt in the open layer, full text held privately, permission sought before
any commercial full-text use (see `restricted-sources.md`). Each source keeps its own terms; see `NOTICE`.

## 6. Scope

In scope (v1): the Australian AML/CTF core (AML/CTF Act 2006 across the reform point-in-time states; the
Amendment Act 2024; the AML/CTF Rules 2025 and Transitional Rules 2026); the FATF 40 Recommendations
(restricted); the Australian sanctions branch (Charter of the United Nations Act 1945; Autonomous
Sanctions Act 2011 + Regulations 2011); and — added by recorded decision (2026-07-09) — the **United
Kingdom** branch: the Proceeds of Crime Act 2002, the Terrorism Act 2000, the Money Laundering, Terrorist
Financing and Transfer of Funds (Information on the Payer) Regulations 2017 (SI 2017/692), the Sanctions
and Anti-Money Laundering Act 2018, and the Economic Crime (Transparency and Enforcement) Act 2022 and
Economic Crime and Corporate Transparency Act 2023 (captured as enacted, for amendment lineage); and —
added by recorded decision (2026-07-09) — the **United States** branch: the Bank Secrecy Act (31 U.S.C.
ch. 53, subch. II, §§5311–5336, incl. the Corporate Transparency Act §5336), the money-laundering
offences (18 U.S.C. §§1956–1957), the terrorist-financing offences (18 U.S.C. §§2339A–2339C), the
International Emergency Economic Powers Act (50 U.S.C. ch. 35), and 31 C.F.R. Part 1010 (FinCEN general
provisions); and — added by recorded decision (2026-07-09) — the **European Union** branch: the Fourth AML
Directive (Directive (EU) 2015/849, consolidated) and the 2024 AML package — the AML Regulation (Regulation
(EU) 2024/1624), the Sixth AML Directive (Directive (EU) 2024/1640) and the Regulation establishing the AML
Authority (Regulation (EU) 2024/1620); and — added by recorded decision (2026-07-09) — the **UN backbone**
(`jurisdiction: international`): the international treaty and Security Council root that the FATF standard
restates and that every national branch implements — the UN Convention against Illicit Traffic in Narcotic
Drugs and Psychotropic Substances (Vienna, 1988), the UN Convention against Transnational Organized Crime
(Palermo / UNTOC, 2000), the International Convention for the Suppression of the Financing of Terrorism
(1999), UN Security Council Resolutions 1267 (1999), 1373 (2001) and 1540 (2004), and the UN Convention
against Corruption (UNCAC / Mérida, 2003 — Arts. 14 and 23 extend the AML framework into the corruption
context); and — added by recorded decision (2026-07-10) — three further national branches: **Canada**
(the Proceeds of Crime (Money Laundering) and Terrorist Financing Act and Regulations, the Criminal Code
money-laundering and terrorist-financing offences, and the sanctions statutes SEMA, the United Nations Act,
the Magnitsky Act and the Freezing Assets of Corrupt Foreign Officials Act; from the Justice Laws Website,
English captured from the bilingual consolidation, free reproduction under SI/97-5), **Singapore** (the CDSA, the Terrorism (Suppression of Financing) Act,
the United Nations Act and its Anti-Terrorism Measures Regulations, and the Precious Stones and Precious
Metals Act; from Singapore Statutes Online, reproduced with AGC permission), and **Switzerland** (the
Anti-Money Laundering Act and Ordinance, the FINMA AML Ordinance, the Criminal Code money-laundering and
terrorist-financing articles, and the Embargo Act; from Fedlex, captured as the **authentic German**
consolidation — see the multilingual note below); and — added by recorded decision (2026-07-10) — three
further national branches: **Hong Kong** (the Anti-Money Laundering and Counter-Terrorist Financing
Ordinance, the OSCO and DTROP money-laundering offences, UNATMO, the UN Sanctions Ordinance, the WMD (Control
of Provision of Services) Ordinance, and the cross-boundary cash Ordinance; from e-Legislation, English is
an authentic language), **Japan** (the Criminal Proceeds Transfer Prevention Act, the Organized Crime
Punishment Act, the Terrorist Financing Punishment Act, FEFTA, and the International Terrorist Asset-Freezing
Act; from e-Gov, captured as the **authentic Japanese** under an open licence), and the **United Arab
Emirates** (Federal Decree-Law 10/2025 and the superseded 20/2018, the 2019 implementing regulation, the
2020 targeted-financial-sanctions decision, and the 2014 counter-terrorism law; captured as the **official
English translation** because the authentic Arabic does not extract to faithful text — see the note below).
All jurisdictions are
cross-referenced, never merged; UK texts are Crown copyright under the Open Government Licence v3.0, US
federal texts are public domain (17 U.S.C. §105), EU texts are © European Union reusable under Commission
Decision 2011/833/EU with attribution, and UN treaties and Security Council resolutions are UN official
documents freely reproducible with attribution — all `redistribution: open`. Out of scope (until a further
recorded decision): the sanctions *lists* /
designations of any jurisdiction (operational data, not law — the enabling Acts/Regulations are in), OFAC
program regulations (31 CFR ch. V), EU restrictive-measures regimes and EBA/technical standards, supervisory
guidance (FCA/JMLSG/AUSTRAC/FinCEN/FFIEC), national transpositions of EU directives, state money-transmitter
law, tax law, and general criminal law.

The EU texts are captured from **EUR-Lex** as the English authentic version (every EU official-language
version is equally authentic; English is one of them, recorded in provenance). The Fourth Directive is the
EUR-Lex consolidated version (`official_consolidation`); the 2024 package is captured as adopted
(`authentic_text`) — adopted law that mostly *applies from 10 July 2027*, with the application dates noted in
each record. Single-column PDFs are extracted with the OJ/CELEX running header removed, de-hyphenated,
letter-spaced headings re-joined, and EUR-Lex consolidation markers (▼B/▼M) stripped; each EU record is
`extracted_verified` against `pdftotext` (see §4).

The UK primary texts are captured from `legislation.gov.uk` as the official "latest available (Revised)"
consolidations (or "as enacted" for the two amendment-lineage Acts). The revised versions carry
`authoritative_status: official_consolidation`; because they are PDFs, `text.txt` is extracted with the
per-page running headers/footers and the repeated "Changes to legislation" banner removed as
non-substantive presentation. Each UK record's `text_fidelity` is `extracted_verified`, corroborated by
independent re-extraction with poppler `pdftotext` (see §4).

The US statutes are captured from **govinfo.gov** (GPO) as the official U.S. Code 2024 annual-edition PDFs;
the regulation (31 C.F.R. Part 1010) from the **eCFR** (Office of the Federal Register), the current
authoritative-but-unofficial edition. The two-column USC print is extracted column-aware and de-hyphenated,
with per-page running headers removed and each single-section PDF trimmed to its own section (adjacent
sections spilling onto a shared page are dropped); the eCFR original is the saved HTML (its PDF export
exceeded the site limit) and `text.txt` is taken from the Part content container with site chrome removed.
US records carry `authoritative_status: official_consolidation` and are `extracted_verified` — the USC
against `pdftotext` and the eCFR HTML against an independent parse (see §4). US federal works are public
domain (17 U.S.C. §105).

The UN backbone is captured from **UNODC** (the convention PDFs) and the **UN documents system** (the
Security Council resolution PDFs). UN treaties and Security Council resolutions are `authentic_text`
(`legal_status: binding`) and are static — a treaty is amended only by protocol and a resolution is fixed as
adopted — so each `version_id` is simply the adoption date, with no consolidation cycle. UN instruments are
equally authentic in the six UN languages (Arabic, Chinese, English, French, Russian, Spanish); the English
authentic version is captured and every language version is recorded as equally authentic (as with the EU
branch). The single-column PDFs are extracted with running headers/footers dropped by position,
de-hyphenated and with letter-spaced headings re-joined; each UN record is `extracted_verified` against an
independent engine (see §4). The Terrorist Financing Convention 1999 is the one exception to PDF capture:
the available UNODC PDF was a scanned image with no text layer, so the authentic text was captured from the
UNODC HTML of the same instrument (recorded in that record's provenance). UN official documents may be
freely reproduced with attribution (`redistribution: open`), so — unlike FATF — the full authentic text is
published. The Palermo record's stored original is the UNODC ebook, which bundles the Convention with its
three Protocols; the derived structure layer disambiguates the repeated article numbering per protocol
section, and the FATF crosswalk's UN-treaty-basis mapping cites the Convention articles directly.

The **Canadian** texts are captured from the Justice Laws Website as the official consolidations
(`official_consolidation`). Justice Laws PDFs are bilingual side-by-side (English left, French right); the
English authentic column is extracted word-by-word by horizontal position (both languages are equally
authentic, the English is captured, and each record's "current to" date is the `version_id`). The Criminal
Code money-laundering (s. 462.31) and terrorist-financing (ss. 83.02–83.04) offences are stored as a
section extract sliced from the consolidated Code by committed anchors. Reproduction is under the
Reproduction of Federal Law Order (SI/97-5): free, with the record noting it is not the official version.
The **Singapore** texts are from Singapore Statutes Online (`official_consolidation` — SSO states the online
text is an informal consolidation; the authoritative version is the printed 2020 Revised Edition), single
column, reproduced with the Attorney-General's Chambers' permission. The **Swiss** texts are from Fedlex as
the **authentic German** consolidation (`authentic_text`, `language: de`): Switzerland's authentic languages
are German, French and Italian, and Fedlex's English is an expressly non-authentic translation (its URL is
recorded in provenance), so — to keep the corpus's authentic-text discipline — the German is captured and
the English linked. Swiss federal law is not copyright-protected (CopA Art. 5), so the full text is
published. Two Swiss records sit marginally below the 0.995 forward-coverage gate (0.9946–0.9948) because
German long compound words tokenise differently between the two comparison engines; a manual diff confirmed
every residual token is a real compound in the source, so they are recorded as `extracted_verified` with the
metrics and reason in their `verification` block. The Swiss Criminal Code articles (Art. 305bis, 305ter,
260quinquies, 260ter) are a section extract; note that where a flattened superscript footnote digit attaches
to a plain Fedlex article number the derived structure layer may carry that footnote in the unit number (a
best-effort limitation of PDF capture — the authentic text itself is unaffected).

The **Hong Kong** texts are captured from e-Legislation as the "Verified Copy" English PDFs
(`official_consolidation`; the verified copy is the legally authoritative version under Cap. 614). English
and Chinese are both authentic (Cap. 5), so the English is an authentic version; each record's `version_id`
is the "verified copy as at" date. The **Japanese** texts are captured from e-Gov as the **authentic
Japanese** consolidation (`authentic_text`, `language: ja`) under the Government of Japan Standard Terms of
Use v2.0 (CC BY-compatible, so the full text is published, `redistribution: open`); this is the corpus's
first CJK branch, extracted verbatim (no whitespace collapse) and segmented by 第N条 with kanji numerals
converted to Arabic, and it verifies at full token *and character* coverage. Only the Japanese is authentic;
the Ministry of Justice's English translations are unofficial and lag, so a JLT English URL is recorded in
provenance where one exists.

The **United Arab Emirates** posed a script problem that is worth recording. Arabic is the sole authentic
legal language (the English on the portal is an official but non-binding translation), so the intent was to
capture the authentic Arabic. But the portal's Arabic PDFs store glyphs in *visual* order, and no available
PDF text engine recovers faithful logical-order text from them: PyMuPDF badly garbles the Arabic, and even
poppler `pdftotext` — the best of them — transposes the letters of the article marker (المادة → املادة) and
reverses parenthesised numbers. A deep-dive established that **Tesseract OCR with the Arabic language pack**
*does* read the rendered page into correctly-ordered Unicode (with minor OCR-level character noise), and is
the route to faithful Arabic text in future. For now, to keep the corpus's fidelity standard, each UAE
record stores the **official English translation** (a new `authoritative_status: official_translation`,
`language: en`, `authentic_languages: [ar]`), which extracts cleanly and passes cross-engine verification —
here run as poppler-vs-PyMuPDF, both of which read the Latin-script English faithfully. The **authentic
Arabic PDF is preserved byte-exact inside each record** (`authentic-source-ar.pdf`, recorded in an
`authentic_source` metadata block with its own SHA-256), so the prevailing legal text is retained. A
**derived OCR Arabic text layer** has since been produced from those preserved PDFs with Tesseract (`ara`)
and sits on the derived side of the wall (`derived/<id>/<version>/authentic-text-ar.txt`, registered as an
`ocr_authentic_text` artifact): it is readable and correctly ordered, but UNOFFICIAL and unverified — OCR
carries minor character-level noise and there is no independent second engine for Arabic, so instead of a
cross-engine gate each record records an OCR *self-consistency* metric (character agreement between a
300-dpi and a 400-dpi pass, ≈ 0.995–0.998). The verified stored text remains the official English
translation; the OCR Arabic is a reading aid, surfaced on the site under an "OCR · unofficial · unverified"
label. UAE material is `redistribution: restricted` (government source, all rights
reserved): the source link, citation and hash are always publishable, and the translation is captured for a
neutral reference corpus. Federal Decree-Law 20/2018 is retained as a `superseded` record (replaced by
10/2025).

## 7. Neutral concept vocabulary

The derived layer tags provisions with a neutral, construct-based vocabulary describing what a provision
is *about*, taking no position — kept jurisdiction-agnostic so later branches reuse it. The vocabulary grows
as scope grows: it now carries 25 concepts, including **`proliferation_financing`** (FATF R.7 / UNSCR 1540)
and **`cash_couriers`** (FATF R.32 — cross-border movement of currency and bearer-negotiable instruments),
added once instruments addressing them were in the corpus. Marquee provisions are curated (human-reviewed);
the remainder use a keyword fallback. See `concept-vocabulary.md` and `derived/concept-index.md`. Tags are
unofficial and never legally operative.

## 8. FATF cross-jurisdiction crosswalk

Because the concept vocabulary is shared across jurisdictions, the derived layer can align them. The
crosswalk (`derived/crosswalk/`) maps each of the 40 FATF Recommendations to the corpus's neutral concepts,
then lists the curated (human-reviewed) provisions carrying those concepts in each jurisdiction, so a reader
can see how Australia, the United Kingdom, the United States and the European Union each address the same
international standard. It references the FATF Recommendation *numbers and short topics only* — identifiers,
not the copyright-restricted FATF text, consistent with the restricted posture in §5. It is **unofficial and
analytical**: a navigation aid, not legal advice, and not an assertion that any provision fully or adequately
implements a Recommendation. Recommendations whose subject falls outside v1 national scope (institutional
bodies, international-cooperation instruments) are marked as such, which doubles as an honest coverage map.
Every listed national provision traces, through the concept tag, to an authoritative text hash.

Above the national columns, each Recommendation also shows its **UN treaty / Security Council basis** — the
root international instrument the Recommendation restates — making the crosswalk *vertical*: UN instrument →
FATF Recommendation → national provision. This UN-basis mapping is a **fixed, human-curated** table
(`scripts/build_crosswalk.py`, `UN_BASIS`) held separate from the concept-tag resolution used for the
national columns, so the specific article/paragraph citations stay exact (and to avoid the Palermo
protocol-numbering collisions). It restores the international-cooperation Recommendations (R.36–40), which
have no captured national instrument in v1, to visible coverage through their treaty root. Like the rest of
the crosswalk it is unofficial and analytical — a claim of lineage, **not** a claim of legal equivalence
between the UN instrument and any national provision.
