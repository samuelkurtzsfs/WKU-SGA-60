# 4 October 2026 (photograph routine, second pass)

## Baseline reconfirmed before anything else

Nick Todd, Katie Dawson, Jeanne Johnson and Reagan Gilley all still carry a portrait in
`data/photos.json`, and all 73 top-level `leaders` records (every president and every student
regent, all 61 years) have a matching entry. The executive/Senate-officer gap and the four
year-photo gaps (1994-95, 1995-96, 2000-01, 2008-09) are unchanged from the scheduled run earlier
today. `research-photos` merged `origin/main` cleanly; `python3 scripts/build.py` and
`python3 scripts/check_data.py` both run clean.

## Both PDF routes retested cold, by two independent methods; both still closed

- `cgi/viewcontent.cgi` — `curl` with full browser navigation headers got the Cloudflare 403 again
  (confirmed against `article=1000&context=talisman` and, separately, `article=6718`). The
  platform's own `WebFetch` tool, a different fetch path, returned the same flat 403 against
  `article=6718`.
- `web.archive.org` — three spaced `curl` attempts against the CDX API all failed identically at
  the TLS handshake (`Recv failure: Connection reset by peer`). `WebFetch` against a Wayback URL
  returned "unable to fetch from web.archive.org" rather than relaying a status. Landing pages
  (`dlsc_ua_records/2464/`, `sga/`) and `archive.org/details` continue to answer normally, matching
  this morning's report — it is specifically the Wayback host and the digitalcommons PDF endpoint
  that are shut, not digitalcommons generally.
- `archive.org/advancedsearch.php` for `identifier:talisman*west` still returns exactly the same 19
  identifiers as every prior check (1943-47, 1963-65, 1971-81, 1986-87). No new Talisman year has
  been added to the archive.org mirror.

## One new, authoritative confirmation: the yearbook collection's own landing page gives the publication years directly

Fetched `digitalcommons.wku.edu/dlsc_ua_yearbooks/` (both of its two pages; the host's search page
is bot-blocked, but this is an ordinary browsable collection page and answers 200 with no
challenge). Its own front matter states plainly: "WKU *Talisman* published annually 1924-1994;
2003+." Pulled the `citation_date` meta field from the ten undated-title records sitting between
"2003 Talisman: About Face" (`dlsc_ua_records/594`) and the 1979 volumes, to check the collection's
own internal date tagging rather than trust title text alone — all ten (`dlsc_ua_records/404`
through `418`) carry `citation_date` values running 1981 through 1994, with 418 ("Against All
Odds") the last one before the jump straight to 594 (2003). This independently reproduces, by a
different method (the collection's structured metadata rather than its abstract text), the
conclusion the 3 October entries in `SGA-60-AGENT-INFO.md` already reached: no Talisman is
cataloged for any year between 1994 and 2003, and 2008-09 sits inside the separate 2003-2012
digitization gap, not the publication one. Nothing here overturns or changes that standing
conclusion; it is a second, independent confirmation of it, worth having because it was pulled from
structured metadata rather than reading an abstract.

Also checked the `/assets/md5images/<hash>.jpg` direct-asset path again, on a `stu_org` item not
previously tried (`stu_org/354`, "Phi Mu Composite, 1998") after noticing it serves a real,
full-resolution JPEG (6936x5590, confirmed `FFD8`) without going through the blocked
`viewcontent.cgi`. This reproduces, rather than overturns, the 29 September finding already on
file: the path only exposes whatever image is embedded in an item's own description text (here, a
sorority composite irrelevant to SGA), not a scan of the underlying document. It still does not
generalize to Herald issues or Talisman volumes, whose descriptions carry no embedded page images.

## Nothing added

No portrait and no year photograph were added this run. `data/photos.json` and `data/photos/` are
byte-for-byte unchanged from the merge-in of `main`; this run's only change is this note.

## For the next run

Unchanged from the scheduled run earlier today: once `viewcontent.cgi` or `web.archive.org`
reopens, the two flagged 2008-09 Herald issues (`dlsc_ua_records/6718` for a second frame beyond
Gilley's existing portrait, and `dlsc_ua_records/6747`, "All Smiles, Kevin Smiley Wins Student
Government Association Election," 16 Apr 2009) are the standing leads, and the 68 newly-surfaced
officer names from this morning's report still need a Talisman volume rather than another
wkuherald.com pass, which is already exhausted for them.
