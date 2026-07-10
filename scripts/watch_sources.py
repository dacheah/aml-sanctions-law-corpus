"""
watch_sources.py -- Phase F source monitor.

Fetches each monitored source (monitoring/sources.json), reduces the page to
text, hashes it, and compares against the stored baseline. New or changed
sources are written to monitoring/last_report.md and the baseline is advanced.
Automation only WATCHES and queues; the maintainer judges (see docs/design).

Designed to run in GitHub Actions. Live fetching uses the standard library.
Run offline self-test with:  python3 watch_sources.py --selftest

Reliability (why a naive hash lies)
-----------------------------------
Several official portals are JavaScript single-page apps: a stdlib GET returns
a near-empty shell (or a generic "enable JavaScript" page), not the law. Hashing
that shell yields a STABLE hash, so the monitor would report "unchanged" forever
even as the law is amended -- false confidence, the worst failure mode for an
integrity tool. Two defences:

  * A source may declare  "render": "spa"  when its human URL is JS-rendered.
    Such a source is reported as MANUAL (a standing "check by hand" item) and is
    never given a meaningful baseline -- unless it also carries a "monitor_url"
    pointing at a server-rendered artifact (e.g. Japan's e-Gov XML API), which is
    fetched instead and treated as normal.
  * Any fetch whose stripped text is implausibly short (< CONTENT_FLOOR) is
    flagged SUSPECT and NOT baselined -- a safety net that catches a formerly
    static site silently migrating to a SPA (which is exactly how this blind spot
    would otherwise creep back in).

Note on noise: index/news pages carry a volatile 'Latest news' area, so some
flags may be cosmetic. The reviewer triages; cadence is monthly. This is a
deliberately simple monitor that can be refined (e.g., section-scoped hashing).
"""
from __future__ import annotations
import hashlib, json, os, re, sys, datetime
from urllib.request import Request, urlopen

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SOURCES = os.path.join(REPO, "monitoring", "sources.json")
REPORT = os.path.join(REPO, "monitoring", "last_report.md")
UA = "Mozilla/5.0 (compatible; provenance-corpus-monitor/1.0; +https://github.com/dacheah/aml-sanctions-law-corpus)"

# Stripped-text length (chars) below which a fetch is treated as a shell/error
# page rather than real content: too short to be a statute page or PDF.
CONTENT_FLOOR = 1000


def to_text(raw: str) -> str:
    """Reduce HTML to comparable text: drop scripts/styles/tags, collapse space."""
    raw = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    return re.sub(r"\s+", " ", raw).strip()


def content_hash(raw: str) -> str:
    return "sha256:" + hashlib.sha256(to_text(raw).encode("utf-8")).hexdigest()


def monitored_url(s: dict) -> str:
    """The URL actually fetched: a server-rendered artifact if declared, else the human URL."""
    return s.get("monitor_url") or s["url"]


def fetch(url: str) -> str:
    req = Request(url, headers={"User-Agent": UA})
    with urlopen(req, timeout=45) as r:
        return r.read().decode("utf-8", errors="replace")


def classify(sources: list, hashes: dict, lengths: dict | None = None) -> list:
    """Pure diff logic (offline-testable).

    hashes:  name -> new_hash or 'ERROR:..'
    lengths: name -> stripped-text length (for the shell/SUSPECT guard)

    States: manual (declared SPA, no server-rendered monitor_url), error,
    suspect (fetch too short = shell), baseline, changed, unchanged.
    """
    lengths = lengths or {}
    events = []
    for s in sources:
        name = s["name"]
        h = hashes.get(name)
        # A JS single-page app with no server-rendered alternative cannot be
        # hashed honestly: surface it as a standing manual-review item instead
        # of minting a meaningless "unchanged".
        if s.get("render") == "spa" and not s.get("monitor_url"):
            events.append((name, "manual", s.get("last_sha256"), h))
        elif h is None or str(h).startswith("ERROR"):
            events.append((name, "error", s.get("last_sha256"), h))
        elif lengths.get(name, CONTENT_FLOOR) < CONTENT_FLOOR:
            # Real content but implausibly short -> looks like a shell/error page.
            events.append((name, "suspect", s.get("last_sha256"), h))
        elif s.get("last_sha256") is None:
            events.append((name, "baseline", None, h))
        elif h != s["last_sha256"]:
            events.append((name, "changed", s["last_sha256"], h))
        else:
            events.append((name, "unchanged", s["last_sha256"], h))
    return events


def selftest() -> int:
    sources = [
        {"name": "a", "url": "x", "last_sha256": "sha256:aaa"},
        {"name": "b", "url": "y", "last_sha256": None},
        {"name": "c", "url": "z", "last_sha256": "sha256:ccc"},
        {"name": "d", "url": "w", "last_sha256": "sha256:ddd"},
        # e: declared SPA with no server-rendered URL -> always MANUAL.
        {"name": "e", "url": "spa", "render": "spa", "last_sha256": "sha256:eee"},
        # f: declared SPA but repointed at a server-rendered API -> treated normally.
        {"name": "f", "url": "spa", "render": "spa", "monitor_url": "api", "last_sha256": "sha256:fff"},
        # g: fetch succeeded but content is a tiny shell -> SUSPECT, not baselined.
        {"name": "g", "url": "v", "last_sha256": None},
    ]
    hashes = {"a": "sha256:aaa", "b": "sha256:bbb", "c": "sha256:CHANGED", "d": "ERROR:timeout",
              "e": "sha256:eee", "f": "sha256:fff", "g": "sha256:short"}
    lengths = {"a": 5000, "b": 5000, "c": 5000, "d": 0, "e": 40, "f": 5000, "g": 12}
    got = {n: st for n, st, _, _ in classify(sources, hashes, lengths)}
    expected = {"a": "unchanged", "b": "baseline", "c": "changed", "d": "error",
                "e": "manual", "f": "unchanged", "g": "suspect"}
    assert got == expected, f"selftest FAILED: {got}"
    assert content_hash("<p>hi</p>") == content_hash("<p>  hi  </p>"), "hash normalisation failed"
    # A SPA source must never be silently baselined even on a first run.
    fresh = [{"name": "z", "url": "spa", "render": "spa", "last_sha256": None}]
    assert classify(fresh, {"z": "sha256:zz"}, {"z": 30})[0][1] == "manual", "SPA baseline leak"
    print("watch_sources selftest: OK")
    return 0


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    data = json.load(open(SOURCES, encoding="utf-8"))
    sources = data["sources"]
    now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    hashes, lengths = {}, {}
    for s in sources:
        # Declared SPA with no server-rendered fallback: don't even pretend to fetch it.
        if s.get("render") == "spa" and not s.get("monitor_url"):
            hashes[s["name"]] = None
            continue
        try:
            raw = fetch(monitored_url(s))
            lengths[s["name"]] = len(to_text(raw))
            hashes[s["name"]] = content_hash(raw)
        except Exception as e:
            hashes[s["name"]] = f"ERROR:{type(e).__name__}"
    events = classify(sources, hashes, lengths)

    st_of = {name: state for name, state, _, _ in events}
    order = ["changed", "suspect", "manual", "error", "baseline", "unchanged"]
    mark = {"changed": "🔶 CHANGED", "suspect": "🟥 SUSPECT — content too short (shell/error?)",
            "manual": "🟠 MANUAL — JS-rendered source, auto-monitor cannot see the law",
            "error": "⚠️ fetch error", "baseline": "🟦 baseline set", "unchanged": "✅ unchanged"}
    lines = [f"# Source monitor report — {now}", "",
             f"{sum(1 for e in events if e[1]=='changed')} changed · "
             f"{sum(1 for e in events if e[1]=='suspect')} suspect · "
             f"{sum(1 for e in events if e[1]=='manual')} manual-review · "
             f"{sum(1 for e in events if e[1]=='error')} error · "
             f"{len(sources)} total", ""]
    by_state = {k: [] for k in order}
    for name, state, old, new in events:
        by_state[state].append((name, old, new))
    for state in order:
        rows = by_state[state]
        if not rows:
            continue
        lines.append(f"## {mark[state]} ({len(rows)})")
        for name, old, new in rows:
            lines.append(f"- **{name}**")
            if state == "changed":
                lines.append(f"    - was `{old}`")
                lines.append(f"    - now `{new}`")
        lines.append("")
    lines += ["_Automation only watches and queues. A change may be a genuinely new/amended "
              "instrument OR a cosmetic page update (e.g. news sidebar). **MANUAL** sources are "
              "JavaScript single-page apps whose law text a stdlib fetch cannot see — a maintainer "
              "must check these by hand each cycle. **SUSPECT** means the fetch returned too little "
              "text to trust (possible shell/error, or a site that has migrated to a SPA). Nothing "
              "is ingested automatically._"]
    open(REPORT, "w", encoding="utf-8").write("\n".join(lines) + "\n")

    # Advance the baseline ONLY for fetches we can trust: never baseline a shell
    # (suspect), a manual SPA, or an error.
    trustworthy = {"baseline", "unchanged", "changed"}
    for s in sources:
        h = hashes[s["name"]]
        if st_of[s["name"]] in trustworthy and not str(h).startswith("ERROR"):
            s["last_sha256"] = h
        s["last_checked"] = now
    json.dump(data, open(SOURCES, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    # Flag genuine changes AND newly-suspect sources (both warrant a human look).
    flag = any(st in ("changed", "suspect") for _, st, _, _ in events)
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a") as f:
            f.write(f"changes={'true' if flag else 'false'}\n")
    print(f"Checked {len(sources)} sources; "
          f"{sum(1 for _,st,_,_ in events if st=='changed')} changed, "
          f"{sum(1 for _,st,_,_ in events if st=='suspect')} suspect, "
          f"{sum(1 for _,st,_,_ in events if st=='manual')} manual, "
          f"{sum(1 for _,st,_,_ in events if st=='error')} errors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
