# Photograph run, 20 November (fourth scheduled pass): baseline reconfirmed, no new lead

## Baseline reconfirmed before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- **Priority 2**: `python3 scripts/check_data.py` — "61 years, 1964 events, 60 people have been
  president" — every president and student regent still carries a portrait.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` — unchanged from the last three
  passes today: 187 cabinet/Senate leadership slots with no same-year portrait (157 people), 155
  of whom have no portrait anywhere in the file. No name on this list is untried; every one is
  already cross-referenced in `_officers-truly-missing-2026-09-06.json` and the dated notes files.
- **Priority 4**: all 61 years still carry at least one `years`-level photograph entry.

## What this pass checked

Pulled wkuherald.com's five most recent SGA-tagged posts directly by date: newest is still 17
November 2026 ("SGA prepares for the holidays with new bills"), the same post the first three
passes today already ruled out — its one photograph captions only a university administrator and
unnamed "student volunteers," not an SGA officer. Nothing has been published since.

Opened `digitalcommons.wku.edu/sga/` (the SGA collection landing page) fresh rather than assume it
was still the same: HTTP 200, 19,994 bytes, but it is navigation chrome (Constitution, Legislation,
RSS, author/discipline browse links), not a dated items list — there is no new-upload signal to
read off this page. Retested `web.archive.org`: connection reset mid-handshake again, consistent
with every pass since the block was isolated as a proxy-level policy block on 16 November, not a
flaky one.

## Conclusion

No new portrait, no new lead, no data change. `python3 scripts/build.py` and `python3
scripts/check_data.py` both pass clean; `site/` was rebuilt only to confirm it still builds, then
reverted (`git checkout -- site/`) rather than committing a same-content, new-date rebuild.
Landing this note only on `research-photos`.

This is the fourth identical "nothing new" result on `research-photos` today (20 November) and
the latest in a run of such results stretching back to mid-November. The standing gap — 155
cabinet/Senate officers with no portrait anywhere, and 12 years with no additional year-level
photograph beyond their one on file — is exhausted against every source this routine's
instructions name (Talisman, WKU Archives UA1C, digitalcommons Herald pages, wku.edu/news,
wkuherald.com). Clearing it further most likely needs either a source this routine cannot reach
(the Wayback Machine, still blocked at the network layer) or a human with physical-archive access.
Whoever next retunes this trigger should weigh lowering its frequency against the cost of a run
finding the same wall it found the pass before.
