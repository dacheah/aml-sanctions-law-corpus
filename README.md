# AML/CTF & Financial-Sanctions Legal Corpus (Australia, United Kingdom & United States, v1)

[![Validate corpus](https://github.com/dacheah/aml-sanctions-law-corpus/actions/workflows/validate.yml/badge.svg)](https://github.com/dacheah/aml-sanctions-law-corpus/actions/workflows/validate.yml)

A neutral, provenance-tracked, machine-readable record of the **law** of anti-money-laundering /
counter-terrorism-financing (AML/CTF) and financial sanctions, on the FATF standard as backbone. Version 1
covers **Australia**, the **United Kingdom** and the **United States** as separate, cross-referenced
jurisdiction branches — never merged; each instrument is recorded from its own official source.

> **An independent, non-commercial reference project. Not affiliated with or endorsed by any employer or
> government body. Not legal or compliance advice.** This corpus records what each instrument says, as at
> a date, from the official source, and takes no position on any matter, institution, or investigation.

## What's inside

- **`authoritative/`** — official source texts only, in their authentic language, each with a byte-exact
  captured original and full provenance (`metadata.yaml`). **Append-only**: every amendment or new
  compilation is a new dated version; nothing is ever overwritten.
- **`derived/`** — everything generated from the authoritative texts: structure extraction, neutral
  concept tags, a commencement/version timeline, and a **FATF cross-jurisdiction crosswalk**
  (`derived/crosswalk/`) mapping each FATF Recommendation to the Australian and UK provisions that address
  it. **Unofficial**, labelled, and traceable to a specific authoritative version by its text hash. Freely
  regenerable.
- **`schema/`** — the JSON Schemas every record must satisfy.
- **`site/`** — a static, dependency-free browsable site (`site/index.html`): each instrument beside its
  provenance, a browse-by-concept index, and a browse-by-FATF-Recommendation crosswalk.
- **`docs/`** — the methodology, concept vocabulary, restricted-source notes, and monitoring policy.

The wall between `authoritative/` and `derived/` is absolute: official texts never mix with anything
generated. See [`docs/methodology.md`](docs/methodology.md).

## Provenance & independent verification

Every authoritative text records its source URL, retrieval date, official citation, issuing body,
jurisdiction, legal status, redistribution posture, and a SHA-256 hash of both the captured original and
the stored text. Anyone can verify integrity with a standard tool — no special software:

```
sha256sum authoritative/<id>/<version>/text.txt      # compare to text_sha256 in metadata.yaml
```

## Coverage (v1)

| Instrument | Jurisdiction | Status |
|---|---|---|
| Anti-Money Laundering and Counter-Terrorism Financing Act 2006 (Cth) | AUS | ingested — 3 point-in-time states (Comp. 59 / 31 Mar 2025 pre-reform, Comp. 60 / 31 Mar 2026, Comp. 61 / 4 Jun 2026) |
| AML/CTF Amendment Act 2024 (as made) | AUS | ingested |
| AML/CTF Rules 2025 (Comp. 1) + Transitional Rules 2026 (Comp. 1) | AUS | ingested |
| FATF 40 Recommendations + Interpretive Notes | international | ingested — restricted posture (hash + citation + excerpt; full text withheld, see [`docs/restricted-sources.md`](docs/restricted-sources.md)) |
| Charter of the United Nations Act 1945 (Comp. 15); Autonomous Sanctions Act 2011 (Comp. 4) + Regulations 2011 (Comp. 18) | AUS | ingested — sanctions branch, cross-referenced |
| Proceeds of Crime Act 2002 (c. 29); Terrorism Act 2000 (c. 11); Sanctions and Anti-Money Laundering Act 2018 (c. 13) | GBR | ingested — official revised (in-force) consolidations from legislation.gov.uk |
| Money Laundering, Terrorist Financing and Transfer of Funds (Information on the Payer) Regulations 2017 (SI 2017/692) | GBR | ingested — revised, in force to 3 Jul 2026 (incl. SI 2026/621) |
| Economic Crime (Transparency and Enforcement) Act 2022 (c. 10); Economic Crime and Corporate Transparency Act 2023 (c. 56) | GBR | ingested — as enacted (amendment lineage) |
| Bank Secrecy Act — 31 U.S.C. §§5311–5336 (incl. Corporate Transparency Act §5336) | USA | ingested — U.S. Code 2024 edition (govinfo) |
| Money-laundering offences 18 U.S.C. §§1956–1957; terrorist-financing offences 18 U.S.C. §§2339A–2339C | USA | ingested — U.S. Code 2024 edition (govinfo) |
| International Emergency Economic Powers Act — 50 U.S.C. ch. 35 (§§1701–1708) | USA | ingested — U.S. Code 2024 edition (govinfo) |
| 31 C.F.R. Part 1010 — FinCEN general provisions (CDD, beneficial ownership) | USA | ingested — eCFR, current as of 7 Jul 2026 |

The 1 July 2026 compilation of the AML/CTF Act will be added when the Federal Register publishes it;
official sources (AU and UK) are monitored for change (`docs/monitoring.md`). UK legislation is Crown
copyright under the Open Government Licence v3.0.

## Also available as a dataset

A machine-readable export — one row per instrument version (full text + provenance) and one row per
provision (with neutral concept tags) — is published as a Hugging Face dataset:
**[huggingface.co/datasets/dacheah/aml-sanctions-law-corpus](https://huggingface.co/datasets/dacheah/aml-sanctions-law-corpus)**.
It is generated from this repository's open layers; the FATF material stays withheld there too.

## Licensing

See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).

- **This corpus's own contributions** (the derived layer, schemas, docs, and site) are released under
  **CC BY 4.0**.
- **Commonwealth legislation** (the Australian statutes and instruments) is © Commonwealth of Australia,
  licensed **CC BY 4.0** via the Federal Register of Legislation (excludes the Commonwealth Coat of Arms
  and any third-party material) — redistributable with attribution.
- **FATF material** is FATF/OECD copyright and is handled under a restricted posture (link + citation +
  hash + short attributed excerpt; full text not redistributed).
- Each source text keeps its own terms, recorded per record in `metadata.yaml`.

Attribution for the Australian legislation: *Federal Register of Legislation
(https://www.legislation.gov.au), © Commonwealth of Australia, licensed CC BY 4.0.*
