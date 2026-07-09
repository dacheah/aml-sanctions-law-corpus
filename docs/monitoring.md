# Source monitoring

This corpus watches the official source of each in-scope instrument for change — a new
compilation, a remake, a new amending instrument, or a revised standard. Monitoring only
**detects and queues** change; a maintainer reviews every flag and decides what to ingest.
**Nothing is ingested automatically.**

## Watched sources

See `monitoring/sources.json`. Each entry is an official source page; a change in its
content hash raises a flag for maintainer review.

## Network requirements

Automated monitoring and byte-exact capture require outbound access to the official sources:

- **`legislation.gov.au`** (and subdomains) — the Federal Register of Legislation (the authority
  for Australian statutes and legislative instruments).
- **`fatf-gafi.org`** (and subdomains) — FATF standards.

Change-detection can read these pages through a managed fetch service, but **byte-exact capture of
the official files** (the authoritative artifacts) requires either (a) the build environment's
network access to allow those domains, or (b) an official human download stored byte-for-byte
(itself a provenance upgrade).

## Cadence

- **Active phase** (Tranche 2 roll-out, 2026–2027): closer-than-monthly — weekly recommended.
- **Steady phase**: monthly, with event-driven checks around FATF plenaries and known commencement dates.

## Pending additions

Add to `monitoring/sources.json` once the official Federal Register identifiers are confirmed at
ingestion: AML/CTF Rules 2025; Charter of the United Nations Act 1945; Autonomous Sanctions Act 2011
+ Regulations 2011; AUSTRAC sector/regulatory guidance pages.
