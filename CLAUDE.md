# Working notes for Claude — aml-sanctions-law-corpus

## Session preamble (ALWAYS)

Every block of shell commands for this repo must begin with these two lines. No exceptions —
omitting them has already caused commands to run against the wrong repo.

```
cd "C:\Users\dache\Claude\Projects\Project Origin\aml-sanctions-law-corpus"
git branch --show-current
```

**Project Origin holds TWO git repos** with overlapping script names:

| Folder | Remote | What it is |
|---|---|---|
| `aml-sanctions-law-corpus` | `dacheah/aml-sanctions-law-corpus` | the corpus (this repo) |
| `aml-sanctions-corpus-toolkit` | `dacheah/aml-sanctions-corpus-toolkit` | the private toolkit |

Both contain `scripts/watch_sources.py`. Getting the `cd` wrong stages the wrong repo, so the branch
check is part of the preamble, not optional.

**When the Crawl4AI layer is lifted into this repo** (`scripts/crawl/`, currently only in
deep-seabed-mining-law-corpus), the preamble gains a third line and the venv becomes mandatory:

```
& "$env:USERPROFILE\.venvs\crawl4ai\Scripts\Activate.ps1"
```

Without it the monitor **silently** degrades to whole-page mode for every source — it does not error,
so a missing venv looks like a successful run that quietly did less.

## Repo facts

- Remote: `https://github.com/dacheah/aml-sanctions-law-corpus.git` — **public dev repo**.
- Default branch: `main`.
- No `scripts/requirements.txt` in this repo; the toolkit repo carries the dependency list
  (`PyYAML`, `jsonschema`).

## Repo workflow

- **Write locally, the user pushes.** Never `git commit`, `git push`, or change git config from the
  agent sandbox.
- Stage **only** files explicitly created or changed, **each named individually**. Never `git add .`
  or `git add -A`.
- Name the target branch explicitly in the push command.
- Commit messages: `type: short imperative summary`, double-quoted, no `$`, backticks or nested
  quotes.

## Traps that have bitten before

- **The monitor auto-commits to the remote**, so local can sit behind without you touching anything —
  a push then fails as non-fast-forward. Precede pushes with:

  ```
  git pull --ff-only origin main
  ```

- **CRLF breaks the hash gate.** Six Australian `text.txt` files were once CRLF locally while the
  recorded hashes were LF, failing verification on files nobody had edited. `.gitattributes` pins
  `original.* binary` and `text.txt text eol=lf`. If verification fails on untouched files, check
  line endings before anything else.
- **Metadata-only migrations must not change content hashes** (all 206 records were byte-identical on
  the last migration).

## Layer boundary (non-negotiable)

`authoritative/` stores official files byte-for-byte. Nothing generated — no crawler output, no model
output — is ever written into it as `text.txt`; `scripts/extract.py` is the sole version-pinned
extractor, so reproducibility checks stay valid.
