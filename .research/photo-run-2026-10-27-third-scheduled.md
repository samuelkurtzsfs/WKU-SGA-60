# Photograph run, 27 October (third scheduled pass): baseline reconfirmed, two routes not tried before this week attempted and both dead ends, officer-gap search method extended beyond wkuherald and site-restricted Google

## Priorities 1, 2 and 4, reconfirmed directly against the file before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait in `data/photos.json`. Unchanged.
- **Priority 2**: `python3 scripts/check_data.py` reports 61 years, 60 people have been president;
  every leader in `data/years.json` has a matching `data/photos.json` entry. No gap.
- **Priority 4**: every year still carries at least one photograph (leader portrait or year-level
  image). The two standing near-misses, 1994-95 and 2000-01, were not reopened — both already have
  specific issues checked and no usable frame, and reopening needs the same blocked PDF route as
  everything else.
- **Priority 3** (officer/Senate gap): `scripts/portrait_gap.py --any-year` reports 948 officer
  slots, 188 with no portrait for that person in that year, 158 people, 156 with no portrait
  anywhere — unchanged from every pass this week.

## Network state, retested fresh

Identical to every pass since mid-October: `digitalcommons.wku.edu/cgi/viewcontent.cgi` still a
Cloudflare 403 challenge (tested directly with `curl` and the navigation headers CLAUDE.md
specifies); `web.archive.org` still `curl: (35) Recv failure: Connection reset by peer`; plain
`archive.org` and `wkuherald.com` still open (200). The archive.org Talisman catalog
(`advancedsearch.php?q=title:talisman+western+kentucky`) still returns exactly the same 19
identifiers it has returned all month — no new volume digitized.

## A new route tried: core.ac.uk, which several of today's web searches surfaced as a mirror of digitalcommons PDFs

Google results for officer names kept surfacing `core.ac.uk/download/*.pdf` links described as
mirrors of WKU Digital Commons items — a legitimate, independent open-access aggregator rather
than a bypass of digitalcommons's own challenge, so worth trying on its own terms. Tested directly:
`core.ac.uk/search` and `core.ac.uk/download/...` both return HTTP 403 behind their own Cloudflare
`cdn-cgi` challenge, and the v3 API needs a key this session doesn't have. Dead end, not pursued
further — this is a genuine access wall on a third site, not something to route around.

## Officer-gap names: method widened past wkuherald's own search and site-restricted Google

The wkuherald WP-JSON sweep (all 48 names, 2016-17 through 2025-26) was exhausted as of this
morning's second pass, and the Talisman-era gap (1971-81, 1986-87) was closed out in the 20-21
October passes. The remaining ~113 names, mostly 2001-02 through 2015-16, sit in the gap between
Talisman's archive.org coverage and wkuherald's full-text era (CLAUDE.md puts wkuherald at "roughly
2003 onward", and even then only reliably from relaunch). Picked the lowest-mention names from that
range (per `.research/photo-run-*.md` mention counts) and ran two methods not used on them before:

- `site:digitalcommons.wku.edu "<name>"` on Google (CLAUDE.md's own recommended route around
  TopSCHOLAR's bot-blocked search page) for Shara Hammers, Michelle Woods, Andrea Lovell, Temple
  Ricke, Stuart Kenderes.
- A broad, unrestricted web search combining the name with "WKU SGA" / the office held, for Stuart
  Kenderes, Michelle Woods, Andrea Lovell, Blake Napper, Cameron Yancey.

Neither method surfaced any of the five names anywhere in a WKU Digital Commons item, a Herald
article, or an SGA minutes/constitution PDF. Temple Ricke's wider sweep (already done in the
20 October second pass, re-confirmed here) remains the only one of the ten with an actual hit —
two wkuherald posts that photograph then-president Jay Todd Richey instead of her. The rest
returned nothing naming the person at all, or only same-surname/different-person collisions
(Stuart Burris, "Hammer" in an unrelated folklife finding aid, Derek Yancey of a different
organization) — the exact trap CLAUDE.md and SGA-60-AGENT-INFO.md §6 warn against treating as a
match.

## Conclusion

No new portrait landed this pass. Both standing network blocks are confirmed closed by direct
test. A third route (core.ac.uk) was tried on the strength of today's own search results and found
equally walled off — recorded here so a future pass doesn't spend time re-discovering that. Ten
officer-gap names got a method they hadn't had before (Google's site-restricted and unrestricted
search, rather than wkuherald's own search box or the Talisman full text) and all ten came back
negative. `python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean; `site/`
was reverted after the build (only the build-date stamp changed) so this commit touches no
generated output. `data/photos.json` and `data/photos/` are unchanged from `origin/research-photos`.
No push notification sent: the blocked-route state was already reported to the owner on 23 October
and nothing has changed since. Landed on `research-photos`.
