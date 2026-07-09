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
Economic Crime and Corporate Transparency Act 2023 (captured as enacted, for amendment lineage). All
jurisdictions are cross-referenced, never merged; UK texts are Crown copyright under the Open Government
Licence v3.0 (`redistribution: open`). Out of scope (until a further recorded decision): other comparative
jurisdictions (US/EU), the sanctions *lists* / designations of any jurisdiction (operational data, not
law — the enabling Acts/Regulations are in), supervisory guidance (FCA/JMLSG/AUSTRAC), tax law, and
general criminal law.

The UK primary texts are captured from `legislation.gov.uk` as the official "latest available (Revised)"
consolidations (or "as enacted" for the two amendment-lineage Acts). The revised versions carry
`authoritative_status: official_consolidation`; because they are PDFs, `text.txt` is extracted with the
per-page running headers/footers and the repeated "Changes to legislation" banner removed as
non-substantive presentation. Each UK record's `text_fidelity` is `extracted_verified`, corroborated by
independent re-extraction with poppler `pdftotext` (see §4).

## 7. Neutral concept vocabulary

The derived layer tags provisions with a neutral, construct-based vocabulary describing what a provision
is *about*, taking no position — kept jurisdiction-agnostic so later branches reuse it. Marquee provisions
are curated (human-reviewed); the remainder use a keyword fallback. See `concept-vocabulary.md` and
`derived/concept-index.md`. Tags are unofficial and never legally operative.

## 8. FATF cross-jurisdiction crosswalk

Because the concept vocabulary is shared across jurisdictions, the derived layer can align them. The
crosswalk (`derived/crosswalk/`) maps each of the 40 FATF Recommendations to the corpus's neutral concepts,
then lists the curated (human-reviewed) provisions carrying those concepts in each jurisdiction, so a reader
can see how Australia and the United Kingdom each address the same international standard. It references the
FATF Recommendation *numbers and short topics only* — identifiers, not the copyright-restricted FATF text,
consistent with the restricted posture in §5. It is **unofficial and analytical**: a navigation aid, not
legal advice, and not an assertion that any provision fully or adequately implements a Recommendation.
Recommendations whose subject falls outside v1 scope (institutional bodies, international-cooperation
instruments) are marked as such, which doubles as an honest coverage map. Every listed provision traces,
through the concept tag, to an authoritative text hash.
