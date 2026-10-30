# Photograph run, 30 October (fourth scheduled pass): web.archive.org reachable
again for direct fetches, but its own image captures of the SGA department
site are missing; no new portrait

## Priorities 1, 2 and 4, checked directly against the files

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all
  four have carried a `leaders` portrait entry since the 20 August run. The
  trigger's stored brief still lists them as portraitless; it has not been
  true for over two months.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — "the archive
  checks out against its own rules" — zero presidents or student regents
  without a portrait across all 61 years.
- **Priority 4**: every year still carries at least one year-level photograph.
- **Priority 3** (officer/Senate gap): `python3 scripts/portrait_gap.py
  --any-year` reports the same figures as every pass since 28 October: 948
  officer slots, 188 without a portrait for that person in that year, held by
  158 people, 156 of whom have no portrait anywhere in the file.

## Network state, retested fresh — one real change

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`, with the navigation headers
  CLAUDE.md specifies: `HTTP 403`, unchanged since 25 August.
- `digitalcommons.wku.edu/sga/` (ordinary index page): `HTTP 200`, open as before.
- `archive.org` (plain item/download host): `HTTP 200`, open as before.
- `wkuherald.com`: `HTTP 200`, open as before; its WordPress search API has
  already been run against this gap in 23 prior reports, so it was not
  re-queried this pass.
- **`web.archive.org` now answers real page fetches over `https://`.** Every
  prior report back to late August recorded `Recv failure: Connection reset
  by peer` / `ws_closed_mid_exchange`. That is no longer true: `curl -sS -L
  https://web.archive.org/web/2020/https://wku.edu/sga/` returned `HTTP 200`
  with the real cached page (45 KB), and the same succeeded for five more
  timestamped SGA department-site snapshots fetched one at a time. Plain
  `http://` (no `s`) to `web.archive.org`, and the CDX/wildcard discovery
  endpoints (`web.archive.org/cdx/search/cdx`, `web.archive.org/web/*/…`),
  still come back `403 Blocked by egress policy` — that block is on this
  session's egress policy, not on archive.org — so snapshots have to be found
  by exact or near timestamp via `archive.org/wayback/available` (which is on
  the open `archive.org` host and still works), not by crawling the index.

### What the reopened route actually gave, for photos specifically: nothing

Using `archive.org/wayback/available`, found snapshots of
`wku.edu/Dept/Org/Student/SGA/` (or its later `wku.edu/sga/` path) at six
dates between 2000 and 2005, spanning the 2001-02 through 2004-05 officer
gaps. Fetched each page. Two of them embed a named photo — `2001_Execnew.jpg`
("2001-2002 EXECUTIVE OFFICERS") on the 2001-02 and 2002-03 captures, and
`sga_intro_011303.jpg` on the 2003-08 capture — which would have been exactly
the kind of lead this gap needs: a captioned composite of a dated executive
cabinet. Both are dead ends. `archive.org/wayback/available` returns an empty
`archived_snapshots` for each image URL, and fetching them directly at the
exact capture timestamp of the page that links them (both with and without
the `im_` modifier) returns Wayback's own 404 page, not image bytes, in both
cases. The crawler captured these pages' HTML but never fetched their
embedded images — a known gap in how old sites got crawled, not a
restriction this session can route around. The 2004-05 and 2005-02 captures
of the same page carry no `<img>` tags at all. No portrait came out of this,
but the finding that the page text itself is now reachable is worth passing
on: other routines on this project that cite Wayback-archived SGA officer
pages for names and dates (not photographs) have a route open that was
closed all last week.

### Checked the officer-gap list against the .research/ corpus before searching anything else

Pulled the current 156-name "no portrait anywhere" list and spot-checked a
further dozen names against the existing `.research/photo-run-*.md` corpus:
each already carries an independent search history of ten or more prior
passes (WebSearch, Talisman catalog, wkuherald.com's own API, Herald index).
No newly open text route surfaced this pass that would change any of those
conclusions, so none were re-searched from scratch.

## Conclusion

No new portrait landed this pass. `data/photos.json` and `data/photos/` are
unchanged from `origin/research-photos`. `python3 scripts/build.py` and
`python3 scripts/check_data.py` both exit clean; the only `site/` diff was
the build-date line, reverted before committing. The digitalcommons PDF
endpoint stays blocked, and the officer-portrait gap stands at 156 people
with no portrait anywhere, each already searched without success. The one
substantive change this pass — `web.archive.org` answering real page
fetches again — did not open a new photograph, because the two composite
cabinet photos it leads to were never captured by Wayback in the first
place; it is recorded here in case another routine on this project can use
the text access.
