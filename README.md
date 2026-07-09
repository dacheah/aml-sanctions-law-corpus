# AML/CTF & Financial-Sanctions Legal Corpus (Australia, v1)

A neutral, provenance-tracked, machine-readable record of the **law** of anti-money-laundering /
counter-terrorism-financing (AML/CTF) and financial sanctions. Version 1 is anchored on Australia, on
the FATF standard as backbone.

> **An independent, non-commercial reference project. Not affiliated with or endorsed by any employer or
> government body. Not legal or compliance advice.** This corpus records what each instrument says, as at
> a date, from the official source, and takes no position on any matter, institution, or investigation.

## What's inside

- **`authoritative/`** — official source texts only, in their authentic language, each with a byte-exact
  captured original and full provenance (`metadata.yaml`). **Append-only**: every amendment or new
  compilation is a new dated version; nothing is ever overwritten.
- **`derived/`** — everything generated from the authoritative texts: structure extraction, neutral
  concept tags, and a commencement/version timeline. **Unofficial**, labelled, and traceable to a specific
  authoritative version by its text hash. Freely regenerable.
- **`schema/`** — the JSON Schemas every record must satisfy.
- **`site/`** — a static, dependency-free browsable site (`site/index.html`): each instrument beside its
  provenance, plus a browse-by-concept index.
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

The 1 July 2026 compilation of the AML/CTF Act will be added when the Federal Register publishes it;
official sources are monitored for change (`docs/monitoring.md`).

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
