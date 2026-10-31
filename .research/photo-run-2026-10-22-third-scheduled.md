# Photograph run, 22 October (third scheduled pass): Internet Archive's own outage explains the last two runs' "web.archive.org closed," Talisman confirmed absent from digitalcommons either way, no new portrait

## Priorities 1, 2 and 4, reconfirmed before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry
  a portrait in `data/photos.json`. Unchanged.
- **Priority 2**: zero presidents and zero student regents without a portrait, across all 61 years.
- **Priority 4**: every year carries at least one year-level photograph. Zero gaps.
- **Priority 3** (officer gap): `scripts/portrait_gap.py` still reports 188 officer slots / 158
  people with no portrait in any year — unchanged from this morning's two passes.

## web.archive.org is not closed; the Internet Archive itself is flaky today

Both of this morning's runs tested `web.archive.org` and recorded a flat "connection reset by
peer," concluding the route stayed closed. Retested fresh this pass, several times, with a
different result: direct fetches of `web.archive.org/web/<ts>/<url>` succeeded repeatedly (HTTP
302 to a timestamped snapshot, then 200 on the snapshot itself), including a real PDF pulled
through a cached `digitalcommons.wku.edu/cgi/viewcontent.cgi` snapshot (verified `%PDF-1.7` magic
bytes, 2.4 MB). That is new: the 16 September report traced the direct-to-digitalcommons block to
Cloudflare's challenge host being unreachable from this container's egress, which is a permanent,
environment-level wall — but fetching the **same PDF through a Wayback Machine snapshot** doesn't
touch Cloudflare at all, because it's served from archive.org's own cache. Where earlier runs saw
nothing but resets, this run got through on the first few tries.

It is not reliably open either. The CDX search index (`web.archive.org/cdx/search/cdx`) returned
`[]` or timed out on every attempt this pass, and one page request came back as an Internet
Archive status page reading **"Internet Archive: Temporarily Offline... services are temporarily
offline... we apologize for the inconvenience."** That's IA's own outage banner, not a wall this
container's egress policy puts up — the prior two runs' "closed" conclusion and this run's
"briefly open" result are both honest readings of the same intermittently-failing service, not a
contradiction to resolve by picking one.

## Why it doesn't open the pre-2003 officer gap even when it works

Confirmed again, independent of the outage: **`digitalcommons.wku.edu/talisman/` does not exist**
(plain 404) and no citation anywhere in this archive uses a digitalcommons Talisman URL. The
Talisman yearbooks live only on `archive.org` (`talisman<year>west`), a different host with its
own, separate, and currently intact access (no Cloudflare wall, no outage seen on it today). So a
working Wayback cache of `digitalcommons.wku.edu` PDFs — even on a day it's reachable — helps only
with Herald issues and SGA minutes hosted on digitalcommons, never with the Talisman gap years
(1982-85, 1988-2005) that archive.org itself doesn't hold. Those stay blocked behind whether
archive.org adds the volumes, not behind any route this run can drive around.

## Local-index check against the Herald PDF route, on the chance it was worth using today

Before spending the open window on anything else, swept `data/herald-index-full.json` (no network
cost) for 50 of the 158 gap names — spot-checking is reasonable; a full 158-name sweep has already
been run exhaustively elsewhere (16 Sept, 22 Oct first/second passes) against other corpora. Ten
names returned a hit. Read every one by hand rather than trusting the match:

- **Alice Wicks** (1978-79 Secretary) — one hit, 13 Apr 1978, "Two Win Oratorical Contests – Dennis
  Payne, Alice Wicks." A contest result, not SGA coverage, and not a photograph.
- **David Young** (1978-79 Administrative VP) — three hits, all April 1979 letters-to-the-editor
  ("Calls David Young Capable," "Endorses David Young," "Supports David Young") backing a *1979-80*
  election candidate — a year after his own term and most likely a different office or a namesake
  candidate, not his 1978-79 AVP record. Text only, no photograph regardless.
- **Connie Hoffmann** (1984-85 Secretary) — one hit, 2 Apr 1985, "Sawyer, Angie. Supports Connie
  Hoffmann" — another endorsement letter, text only.
- **Matthew Pava** (2003-04 IT Designate) — one hit, 31 Aug 2004, a letter he co-signed criticizing
  Nick Todd — his own voice, not a photograph of him.
- **Steve Wilson** (1978-79 Judicial Council Chairman) — the hits are a 1970 Young Republicans
  officer and a different "Willingham, Steve" op-ed; neither is this Wilson. (The 16 Sept report
  already separately ruled out a Talisman-indexed "Steve Wilson" as an unrelated SAE barbershop
  quartet member — a third, independent non-match for the same name.)
- **Mike McDaniel, Pat Smith, David Smith, John Holland, Jason Heflin** — each returned only
  unrelated-context hits (a 1967 item, common-surname noise, a 1998 item outside Holland's
  1983-85 term, etc.), none naming the SGA office or carrying a photograph.

None of the ten is a photograph lead. All are endorsement letters, contest results, or unrelated
namesakes — exactly the class of index hit CLAUDE.md's "a miss still proves nothing, a hit still
isn't photographic evidence" caution covers in the other direction. Nothing added to
`data/photos.json`.

## Conclusion

No new portrait landed this pass. The one genuinely new fact this run adds to the record is that
`web.archive.org`'s unreachability on 21-22 October was Internet Archive's own service outage, not
a permanent block — worth knowing so a future run doesn't file it alongside the Cloudflare/digital
commons wall as the same kind of problem, since one may lift on its own and the other won't. It
still doesn't reach the Talisman-era gap, which depends on archive.org adding volumes digitalcommons
never hosted in the first place.

`python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean; the regenerated
`site/` output (a build-date string only) was discarded rather than committed, since nothing in
`data/` changed. Landed on `research-photos`.
