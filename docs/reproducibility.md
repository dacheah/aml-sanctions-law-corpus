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
| v1.3.4 | `42b74c8b7de0bfa1a6eb32efd6809b0be92fb9ca85ce72ff1ffe34483688e6e3` |

To reproduce this corpus, assemble a build tree (the toolkit's `scripts/` alongside this repo's
`authoritative/`, `schema/`, and `site.json`), verify the engine with `sha256sum -c
scripts/MANIFEST.sha256`, then run the build. Full procedure: `BUILD.md` in the toolkit repo.

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
