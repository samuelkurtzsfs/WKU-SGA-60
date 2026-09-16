# Photograph run, 16 September (third pass)

## Starting state, re-confirmed

Checked the standing brief's priorities against `data/photos.json` and `data/years.json`
before doing anything new, same as both earlier passes today:

- All four presidents named in the brief — Nick Todd, Katie Dawson, Jeanne Johnson, Reagan
  Gilley — already have portraits.
- Every `leaders` entry with `role: "president"` or `role: "regent"` across all 61 years
  has a portrait. Priorities 1 and 2 are fully satisfied.
- 12 of 61 years still lack a `years` (context) photograph: 1993-94 through 1997-98,
  2000-01, 2002-03, 2003-04, 2005-06, 2006-07, 2008-09, 2009-10.
- `build.py` and `check_data.py` both pass clean on the merged tree (61 years, 1963
  events, 60 people have been president).

## A full name-integrity check of `data/photos.json`, run for the first time this way

Rather than search for more portraits — the 13 and 16 September reports both already
exhausted the reachable corpora for priority 3 — this run did something not on record
before: checked, programmatically, that every one of the 1,388 `leaders` entries in
`data/photos.json` has a `name` that exactly matches a name appearing somewhere in that
same year in `data/years.json` (leaders, executive, Senate officers, committee chairs, or
Senate members), as CLAUDE.md's Pictures section requires.

A naive first pass (checking only the `leaders` array) flagged ten apparent mismatches —
Tim Irons (1979-80), Marsha Sanner (1980-81), Natalie Croney (2003-04), Benjamin
Lineweaver and Brittany-Ann Wick (2008-09), Currie Martin and Dave Vickery (2009-10),
Lillian Nellans (2017-18), and Amanda Harder and Matt Barr (2018-19) — because those ten
are committee chairs or organization-block names, not `leaders` entries. Extending the
check to the full `organization` block (executive, Senate officers, committee chairs,
Senate members) found an exact match for all ten, and for all 1,388 entries overall:
**zero real name mismatches.** All 1,388 files also still open with valid JPEG or PNG
magic bytes and all 1,388 referenced files exist on disk. This is a clean bill of health,
not a finding to act on, but it had not been checked this exhaustively before and is worth
having on record.

## Routes re-tested fresh rather than trusted from the two earlier reports today

- **`digitalcommons.wku.edu/cgi/viewcontent.cgi`** — still HTTP 403, Cloudflare
  "Just a moment..." challenge, with the documented navigation headers. No change.
- **`web.archive.org`** — intermittent, as documented repeatedly since 16 September:
  a CDX query against `wku.edu/sga*` returned a clean HTTP 200 on the third attempt;
  the same endpoint against `digitalcommons.wku.edu` (both a wildcard `viewcontent.cgi*`
  query and a bare-domain query) returned HTTP 503 "Internet Archive: Temporarily
  Offline" or a connection reset on five further attempts spread over about a minute.
  Recorded as inconclusive, not closed — a future run should retry the
  digitalcommons-domain CDX query specifically, since it was never confirmed either way
  today.

## One genuinely new, untried idea, tested and left half-open

**Checking whether the Wayback Machine holds its own captures of
`digitalcommons.wku.edu` — which would sidestep the live Cloudflare block entirely — has
not been tried by any earlier run in this file.** This run tried it (the CDX queries
above) but could not get a clean answer either way before `web.archive.org` itself
started refusing the specific queries needed. This is worth a future run picking up
first, before re-running the exhausted wkuherald.com/archive.org searches again: if
TopSCHOLAR was ever crawled by the Wayback Machine, its PDFs might be retrievable from
`web.archive.org/web/<timestamp>/https://digitalcommons.wku.edu/cgi/viewcontent.cgi?...`
even while the live site is not.

## Priority 4 (year photographs): one new negative result

The two earlier reports today left priority 4 alone because every identified route for it
sits behind the blocked `viewcontent.cgi`. This run tried one route that does not:
`wkuherald.com`'s WordPress full-text search, for the five priority-4 gap years that fall
inside its coverage window (2003-04, 2005-06, 2006-07, 2008-09, 2009-10), searching
"Student Government Association" with `after`/`before` date bounds rather than by name.

The site's full text does reach back this far — 98 posts came back for 2003-04 alone,
confirming wkuherald.com's WordPress backend holds content from as early as 2002, not
only from ~2011-12 as an earlier report's phrasing implied (that report's "2012 or later"
finding was about specific *names* returning no relevant hits, not about the corpus's
date range). But **none of the posts returned for any of the five years carries a
`featured_media` image** — 0 of 98 for 2003-04, and either 0 or 1 total post for the
other four years, none with an image. This appears to be a migration gap rather than a
search-technique gap: the older College Publisher-era content came across as text only.
**wkuherald.com is now confirmed closed for priority 4 as well as priority 3, for these
five years; do not re-run this search without a new source.** The other seven gap years
(1993-94 through 1997-98, 2000-01, 2002-03) predate wkuherald.com's coverage entirely and
were never in scope for this test.

## Nothing added

No photograph was added or removed this run; `data/photos.json` and `data/photos/` are
unchanged. `build.py` and `check_data.py` both pass clean on the merged tree. The next
run's most promising unexhausted thread is the Wayback-capture-of-digitalcommons idea
above; everything else reachable from this container for priorities 3 and 4 has now been
tried and closed at least once today.
