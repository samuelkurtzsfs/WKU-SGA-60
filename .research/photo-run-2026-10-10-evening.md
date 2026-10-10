# Photograph run, 10 October (evening) — Google site-search tried against the digitalcommons collection as a bypass for the closed PDF gate; unproductive, and recorded as a different kind of negative than the usual gate-closed one

## Priorities 1, 2 and 4, reconfirmed before anything else

**Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
portrait in `data/photos.json`. Nothing to do.

**Priority 2** (any other president or student regent without a portrait): checked every
`leaders` record in `data/years.json` against `data/photos.json` by name, programmatically. Zero
missing.

**Priority 4** (years with no photograph at all): every one of the 61 years has at least one
photograph in `data/photos.json`. Zero missing. The two standing gaps (1994-95, 2000-01) are
unchanged; both still wait on the same closed PDF gates as everything below.

`scripts/portrait_gap.py` reports the same figures as every pass since 9-10 October: 189 officer
slots with no portrait, held by 159 distinct people, 157 of them with no portrait anywhere in the
file.

## The two PDF gates, retested cold

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — `curl` with full navigation headers
  (`Sec-Fetch-Dest: document`, `Sec-Fetch-Mode: navigate`, `Upgrade-Insecure-Requests: 1`) against
  a known-good article number returned HTTP 403, Cloudflare `cf-mitigated: challenge`, "Just a
  moment..." page. Same as every pass since this gate closed.
- `web.archive.org` — `curl: (35) Recv failure: Connection reset by peer` on an `if_` bypass
  request. Not open this session.
- `archive.org` (plain) — root page answers HTTP 200. Not pursued further: every Talisman year it
  holds (1971-81, 1986-87) with a missing officer was already exhausted in the 9 October and
  10 October afternoon passes.

## A genuinely new method tried: Google `site:digitalcommons.wku.edu` search

No prior photo-run report in `.research/` uses this; CLAUDE.md names it only as a workaround for
TopSCHOLAR's own blocked search page, not as something the photograph agent had tried. The idea:
if Google has indexed a Talisman or Herald landing page's abstract text, a name search could
surface a hit without ever touching the Cloudflare-gated `cgi/viewcontent.cgi` endpoint — since,
per this afternoon's finding, ordinary `dlsc_ua_records`/`dlsc_ua_yearbooks` landing pages are not
behind that gate, only the PDF download is.

Ran it against eight names from the "no portrait in any year" list, chosen from years `archive.org`
does not hold (pre-1987 names already exhausted there) and spread across decades: Vern Pulman
(1974-75), David Bass (1977-78), Alice Wicks (1978-79), John Holland (1983-84/1984-85), Trent Lyda
(1992-93), Derrek/Derek Duncan (1993-94/1994-95), Mickie Hennig (1988-89), Chris Gaddis (1988-89).

**Zero usable hits.** Every query either returned no WKU Digital Commons result naming the person
at all, or returned digitalcommons.wku.edu pages that mention a *different* person of a similar or
unrelated name (George Pulman, Vernon Sheeley, David Payne, Alice Gatewood Waddel, Alice Dunham
Green, Alice Z. Upshaw, John Pulman) with no connection to WKU student government. One result
(the 1984 Herald issue carrying a "Holland, John" byline on an unrelated piece, "Write Legislators")
came closest to a name match, but it is a byline on the issue's own author list, not a caption
identifying a Student Government Association officer in a photograph, so it is not a lead.

**Why this is a different negative than the usual one, and worth recording as its own finding
rather than folding into "gates still shut."** Every other method this project's recent passes
have exhausted failed because a specific door was closed (Cloudflare on `cgi/viewcontent.cgi`,
intermittent resets on `web.archive.org`) or because a specific index genuinely does not carry the
content (the magazine-era Talisman abstracts not indexing a group photo page, per this afternoon).
This one fails for a third reason: Google's crawl of `digitalcommons.wku.edu` does not appear to
reach deep enough into this collection's per-item abstract text to make a name search useful for
obscure 1970s-90s student officers — the results it does return for this domain skew toward
finding-aid pages, cartoon collections and other "herstory"/exhibit content that happens to rank
on the query terms, not the Herald/Talisman items this project actually needs. That is a limit of
Google's index, not of the archive or of this project's access to it, so it does not change
anything about the two real gates above, and it is not a route worth spending more of a future
run's budget on without a different query strategy (e.g. searching for the office title and year
instead of the person's name, which was not tried this run).

## Nothing landed

No file in `data/photos.json` or `data/photos/` changed; `data/years.json` is untouched.
`python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean against the
unchanged tree (61 years, 1,967 events, 60 presidents); the `site/` rebuild this produced was
discarded (`git checkout -- site/`) since nothing in `data/` changed. This run's only output is
this note.

## For the next run

- Retry both PDF gates cold, as always.
- Google site-search is now tried-and-negative for a person-name query against this collection;
  if it is tried again, use an office-title-plus-year query instead of a bare name, which this run
  did not test.
- Everything else named in the 10 October morning and afternoon notes (gallery captions on
  wkuherald.com, magazine-era Talisman abstracts, the pre-1987 `archive.org` Talisman texts) stays
  exhausted until a gate reopens or a new source surfaces.
- 189 officer slots / 159 people / 157 with no portrait anywhere remains the live count.
