# Source monitoring

This corpus watches the official source of each in-scope instrument for change — a new
compilation, a remake, a new amending instrument, or a revised standard. Monitoring only
**detects and queues** change; a maintainer reviews every flag and decides what to ingest.
**Nothing is ingested automatically.**

## Watched sources

See `monitoring/sources.json`. Each entry is an official source page; a change in its
content hash raises a flag for maintainer review.

## Fetch reliability (why a hash can lie)

The monitor fetches with the Python standard library, which does not run JavaScript. Several
official portals are JavaScript single-page apps: a stdlib GET returns a near-empty shell — or a
generic "enable JavaScript" page — rather than the law. Hashing that shell yields a *stable* hash,
so a naive monitor would report the instrument "unchanged" indefinitely even as it is amended. This
false green is the worst failure mode for an integrity tool, so the monitor guards against it two ways:

- A source whose human URL is JS-rendered carries `"render": "spa"`. It is reported as **MANUAL** —
  a standing "check this by hand each cycle" item — and is never given a meaningful baseline, *unless*
  it also carries a `"monitor_url"` pointing at a server-rendered artifact (fetched instead of the
  human URL). Japan's five instruments use the e-Gov **XML API** (`laws.e-gov.go.jp/api/1/lawdata/<id>`),
  which returns the full statute server-side, so they are monitored normally.
- Any fetch whose stripped text is implausibly short (below `CONTENT_FLOOR`, currently 1000 chars) is
  flagged **SUSPECT** and not baselined — a safety net that catches a previously static site silently
  migrating to a SPA.

The report (`monitoring/last_report.md`) groups sources by state (CHANGED / SUSPECT / MANUAL / error /
baseline / unchanged) so the manual-review set is visible on every run rather than hidden behind a green tick.

As of this writing the manual-review set is 17 sources with no stdlib-reachable text artifact: Hong Kong
e-Legislation (7), the UAE legislation portal (5), and Swiss Fedlex (5). Restoring any of these to
automatic monitoring means finding a server-rendered URL (an XML/print/API endpoint, like Japan's) and
adding it as that source's `monitor_url`.

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
