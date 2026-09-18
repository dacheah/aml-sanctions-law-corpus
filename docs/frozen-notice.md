# Frozen notice — AML/CTF & financial-sanctions corpus

**Status:** FROZEN · **Frozen as at:** 2026-08-04 · **Last automated sweep:** 2026-08-03

## Dates, precisely

The decision to freeze was taken on 26 July 2026, but monitoring did not stop then: the weekly workflow
continued to run and completed sweeps on **27 July** and **3 August 2026**, both committed by
`github-actions[bot]`. The freeze takes effect on **4 August 2026**, the date the workflow was actually
disabled.

An earlier draft of this notice recorded the freeze as 26 July. That was the date of the decision, not
of the last monitoring — and in a corpus whose entire premise is that recorded dates mean what they say,
a freeze date predating two real sweeps is exactly the kind of small inaccuracy the method exists to
prevent. Corrected here rather than left to stand.

## What "frozen" means here

Source monitoring is **deliberately switched off**. This is a decision, not neglect — the distinction
matters, because an unmaintained corpus that still looks maintained is worse than one that says plainly
it has stopped.

- The records are unchanged, byte-exact and hash-verifiable. Nothing has been withdrawn or altered.
- Each record remains accurate **as at its own `retrieval_date`**, which is recorded per record.
- No new compilations, amendments or instruments will be ingested.
- The scheduled monitoring workflow is disabled rather than left to fail quietly.

## Why it was frozen

Two reasons, recorded honestly.

**Maintenance economics.** This corpus watched ~60 official sources across ten jurisdictions — roughly a
third of the whole portfolio's monitoring burden. A deep prior-art check on 26 July 2026 found that
every comparable independent project died of exactly this: not a bad thesis, but the cost of keeping
government portals from rotting. The `open-source-legislation` project archived in November 2025 with
the post-mortem *"unsustainable maintenance burden… this is a full-time job disguised as a side
project."* Freezing here is a deliberate choice to spend that capacity where it is not duplicated.

**Duplication.** AML/CTF and sanctions law is the most commercially saturated legal domain in this
portfolio — World-Check, Dow Jones Risk, ComplyAdvantage, Moody's, and the RegTech incumbents (CUBE,
Corlytics, Regology/Bloomberg) all cover it with staff. It is also the domain with the *highest*
completeness expectation: a compliance-grade AML source that is 95% complete is not 95% useful, because
the missing 5% is the liability. An independent single-maintainer corpus cannot honestly make that
claim, and this project does not make claims it cannot support.

## What could never be machine-checked

The corpus's own source audit (`monitoring/source_audit.md`, 2026-07-22) belongs with this notice, because
it is the honest edge of the monitoring claim above. Of the 60 monitored sources:

- **17 declared manual** (`render:spa` or `monitor:manual`) — SPA-rendered or otherwise fetch-opaque
  portals (Switzerland's fedlex, Hong Kong's e-legislation and others). They were checked by hand, and
  they are why a green monitor run must never be read as "every source was checked".
- **4 broken** at the last audit: FATF's recommendations page returning `403`; the two
  `uscode.house.gov` `view.xhtml` endpoints timing out; Canada's Criminal Code page resetting the
  connection. Each needs a browser or a replacement URL rather than a retry loop — the portfolio's
  standing rule is escalate, never bypass.
- **2 for review**: Canada's PCMLTFA and PCMLTFR, whose page titles do not resemble the source names and
  may therefore be the wrong pages.
- **0 of 60 sources declared an `expect_contains` anchor**, so the plumbing check could not have caught a
  source that resolves cleanly to a *wrong* page. That is the durable fix this corpus never got to, and
  it is recorded rather than implied away.

The four source-monitor issues open at the freeze (#1–#4, July–August 2026) are closed against this
notice. Two of them recorded **real** content changes (the UK Proceeds of Crime Act 2002 and Terrorism
Act 2000 on-as-amended pages, 20 July 2026); those were **not** ingested, because the freeze is a
deliberate stop. Every record speaks only as at its own `retrieval_date`.

## Do not use this for compliance

Superseded law is indistinguishable from current law at a glance. Every record here carries its
`source_url`, `official_citation` and `retrieval_date` so that going back to the issuing authority is
always possible — do that for anything operative.

## What this corpus is still good for

- A **point-in-time record**: what these instruments said, as at the dates recorded, from official
  sources, with byte-exact originals and verifiable hashes.
- A **methodology reference**: the two-layer authoritative/derived separation, the FATF crosswalk
  linking each Recommendation to its UN treaty and Security Council basis and then to national
  implementations, the dual-engine fidelity verification, and the Arabic OCR reconciliation are all
  intact and documented.
- A **citable dataset**: the Zenodo DOI remains valid and resolves to the frozen state.

## Tooling

The build engine lives in a separate private repository and is **not** frozen. The generic parts —
ingest, validation, the reproducibility gate, the set-aware engine manifest verifier, the source monitor
— continue to be maintained and used by the other corpora. The AML-specific parts (the FATF crosswalk
builder, the Arabic OCR profile, the cross-engine fidelity checker) are retained there as domain modules
rather than being discarded with this corpus.

## Reversal

Freezing is reversible. Restarting means: re-enabling the monitoring workflow, running a full source
audit (expect rot across ten jurisdictions after any long gap), re-baselining, and removing this notice
along with the README banner. Nothing about the frozen state prevents that.
