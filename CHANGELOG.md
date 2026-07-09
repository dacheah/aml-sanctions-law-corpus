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

[Unreleased]: https://github.com/dacheah/aml-sanctions-law-corpus/compare/v1.0.1...HEAD
[1.0.1]: https://github.com/dacheah/aml-sanctions-law-corpus/releases/tag/v1.0.1
[1.0.0]: https://github.com/dacheah/aml-sanctions-law-corpus/releases/tag/v1.0.0
