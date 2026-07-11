# Reproducibility

This corpus is provenance-first: the derived layer can be regenerated from the authoritative layer,
and the exact build engine that produced each release is pinned by a cryptographic fingerprint.

## The two layers

- **`authoritative/`** — the official source texts, each with its source URL, retrieval date,
  citation, and the SHA-256 of both the byte-exact original and the stored text. This layer is
  append-only; a correction or amendment is always a new dated version, never an in-place edit.
- **`derived/`** — everything generated from the authoritative layer: structure, neutral concept
  tags, the FATF crosswalk, the version timeline, the site, and the Hugging Face export. Nothing here
  is authoritative; it is all reproducible or clearly labelled as authored.

## The build engine

The derived layer is produced by the **corpus toolkit** (`aml-sanctions-corpus-toolkit`), a separate
repository holding the build scripts. The engine is hash-pinned by `scripts/MANIFEST.sha256` in that
repo; the **engine fingerprint** (the SHA-256 of that manifest) names an exact engine version and is
recorded against each release here:

| Corpus release | Engine fingerprint |
|---|---|
| v1.3.7 | `b978a9f50e0234b7cc306dd8c7469e9c27ffdef0fcde5db4f50c01c323efe78a` |
| v1.3.6 | `b9e9e35fc4e0dc83f7d888f733a78811f8f8a6b9be7618745d46523aecdd5f22` |
| v1.3.5 | `115d8b0158b3efe18003a1422c9f4fbabacdb504b7b8528865f5325cc9ca2181` |
| v1.3.4 | `42b74c8b7de0bfa1a6eb32efd6809b0be92fb9ca85ce72ff1ffe34483688e6e3` |

To reproduce this corpus, assemble a build tree (the toolkit's `scripts/` alongside this repo's
`authoritative/`, `schema/`, and `site.json`), verify the engine with `sha256sum -c
scripts/MANIFEST.sha256`, then run the build. Full procedure: `BUILD.md` in the toolkit repo.

## Authoritative text reproducibility

Every stored `text.txt` re-derives byte-for-byte from its stored original by committed code
(`scripts/extract.py`, one profile per jurisdiction/format). As of **v1.3.5 this is 68/68 byte-exact
with no exceptions** — the FATF Recommendations are the only instrument without stored text (copyright,
`restricted_withheld`). Three early AU records that were previously content-equivalent-but-not-byte-exact
were re-derived to the canonical extraction in v1.3.5 (blank-line placement only; legal content proven
identical; noted per record under `text_derivation`).

## What is reproducible

The derived layer has three provenance classes:

1. **Engine-generated (byte-reproducible)** — `structure.json`, `concepts.json`, per-record
   `derived-metadata.yaml`, `derived/concept-index.*`, and `derived/crosswalk/*`. A clean rebuild from
   the authoritative texts is byte-identical to the published files. Verified for v1.3.4 on 2026-07-11:
   the pinned engine reproduced every engine-generated file exactly.
2. **OCR step (reproducible, tool-pinned)** — the UAE `authentic-text-ar.txt` / `.meta.json`, produced
   by `ocr_arabic.py` from the hash-pinned Arabic source PDF using Tesseract 5.3.4 (`ara`). A separate,
   date-stamped step; each record records an OCR self-consistency metric.
3. **Curated (authored)** — `derived/timeline/`, a neutral synthesis of the AU Amendment Act 2024 s.2
   commencement table, carrying its own source hash and disclaimer. Not machine-regenerated.

## Validation gate

Every build must pass `validate_corpus.py` (`RESULT: OK.`), which checks the two-layer wall, the
metadata schemas, the content hashes, and the derived↔authoritative links across all records.
