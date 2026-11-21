# Photograph run, 18 November (fourth scheduled pass): a genuinely new local-index lead opened and closed, network gates re-tested

## Baseline reconfirmed

- Priority 1 (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- Every president and every student regent in `data/years.json` has a `data/photos.json`
  `leaders` entry (checked against the whole file).
- All 61 years carry at least one `years`-level photograph entry.
- 28 executive-cabinet slots and 185 Senate-officer slots remain without a same-year portrait.
  Cross-checked every name in the executive list against `.research/*` and `data/photo-finds/*`:
  every one of the 28 already has a documented dead end from a prior pass (10-27 hits apiece),
  confirming this is not an unexamined backlog.

## Live Herald feed re-checked

`wkuherald.com`'s WordPress API (`/wp-json/wp/v2/posts?search=SGA&per_page=5&orderby=date&order=desc`)
still returns "SGA prepares for the holidays with new bills" (id 99560, 17 November 2026 23:29) as
its newest item — the same one the third pass today already read and ruled out (photo subject is
a university sustainability officer, not an SGA officer). Nothing new has posted since.

`wku.edu/news`'s own search endpoint (`index.php?search=SGA`) does not return search results at
all — it serves the plain news-category navigation page regardless of the query string — so it is
not a usable route for finding dated articles and was not pursued further.

## One lead neither this branch's history nor today's earlier passes had opened

Searched `data/herald-index-full.json` directly (not `.research/`) for every executive-officer
surname in the any-year gap, to find an index hit nobody had opened yet rather than re-reading
hits already logged. Three of the four matches (Fite 1935, Chesnut 1962, Hennig 2012) are
different people by date alone. The fourth was new: **"Roadcap, Steve. Herald is One-sided,"**
*Herald* 71:40, 20 February 1996 (`dlsc_ua_records/2957`) — not previously referenced anywhere in
`.research/` or `data/photo-finds/`.

Opened the item page (reachable, HTTP 200) to read the full article list: it is a letter to the
editor criticizing Herald coverage, listed among ordinary People Poll/Campus Line/opinion content
with no photograph indicated for any opinion contributor in this issue, and no indication the
letter-writer is the same Steve Roadcap who was SGA treasurer the following year (1996-97) rather
than any other student of that name. Not pursued further — a letters-page byline is not a
captioned photograph under this project's rule, and the identity itself is unconfirmed. Closed as
a dead end; worth recording only so no future pass re-opens the same index hit expecting new
ground.

## Network gates

`digitalcommons.wku.edu` landing pages answered cleanly (HTTP 200, full content) on every request
this pass — a better state than many recent passes have found. `cgi/viewcontent.cgi` (the actual
PDF/page-image path) did not share that: 403 on the first attempt with full browser navigation
headers and a same-session `Referer`, and still 403 on a second attempt after the full 90-second
backoff the pacing rule calls for. So the landing-page/PDF split persists exactly as prior reports
describe it — browsing the index works, reading the actual scanned pages does not — and this
remains the operative constraint on the entire pre-2003 officer-portrait cohort, not something
this pass's better-than-usual landing-page access changed.

## Conclusion

No new portrait, no change to `data/photos.json` or `data/photos/`. `python3 scripts/build.py`
and `python3 scripts/check_data.py` both pass clean against the unchanged data; the `site/`
rebuild (date-stamp only) was discarded rather than committed. Landed on `research-photos` with
only this note, so the next pass knows the Roadcap/2957 index hit has been opened and ruled out.
