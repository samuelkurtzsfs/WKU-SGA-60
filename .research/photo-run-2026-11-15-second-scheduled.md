# Photograph run, 15 November (second scheduled pass): same two gates retested and still closed, no new search spent on an already-exhausted list

## Baseline, reconfirmed by script rather than by reading an earlier report

- Priority 1 (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry a
  `leaders` portrait in `data/photos.json`.
- Priority 2: `check_data.py` confirms every president and student regent still has one.
- Priority 3: `python3 scripts/portrait_gap.py --any-year` reports the same 187 officer-slots /
  157 people / 155-with-no-portrait-anywhere figure as this morning's run. No change.
- Priority 4: all 61 years carry at least one photograph.

## Network, retested fresh rather than trusted from the morning's report

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — `curl` against a live article (1408) returns
  `403` (Cloudflare), matching this morning's result exactly.
- `web.archive.org` — connection reset mid-handshake, matching this morning's result exactly.
- `archive.org` (no `www.`) — up; `/metadata/talisman1986west` returns real metadata, confirming
  the 1971-1981/1986/1987 holding is reachable and nothing wider.

Both blocking gates are unchanged from the run six hours earlier. Rather than re-running the same
name-by-name search this list has already had (per `_do-not-use.json` and `_archive-gaps.json`,
every name in the archive.org-reachable year range — Pulman 1974-75, Young/Wicks/Wilson 1978-79,
Chesnut 1980-81, Millay/Austin 1986-87 — is already a documented dead end, most checked three or
more times by independent methods), this run spent its time differently: see the note added to
`SGA-60-AGENT-INFO.md` §8 about this trigger's firing rate against its actual yield.

No change to `data/photos.json` or `data/photos/`. `build.py` and `check_data.py` both run clean.
Landed on `research-photos`.
