# Photograph run, 26 October (second scheduled pass): full 156-name local-index sweep, both blocked routes retested and still closed, no new portrait

## Priorities 1, 2 and 4, reconfirmed before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait in `data/photos.json`, checked by reading each entry directly.
- **Priority 2**: `python3 scripts/check_data.py` reports 61 years, 1964 events, 60 presidents, no
  missing leader portrait.
- **Priority 4**: every year still carries at least one photograph (leader portrait or year photo).
- **Priority 3** (officer/Senate gap): `scripts/portrait_gap.py --any-year` still reports 188
  officer slots held by 158 people with no portrait, 156 of them with no portrait anywhere in the
  file — unchanged from this morning's pass and from every pass since 20 October.

## Access, retested fresh

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — HTTP 403, Cloudflare challenge (`cf-mitigated:
  challenge`), tested directly against the SGA-photographs finding-aid PDF (article 1619,
  `context=dlsc_ua_fin_aid`). Still closed.
- `web.archive.org` — `curl: (35) Recv failure: Connection reset by peer` on a plain snapshot
  fetch. Still closed.
- `iiif.archive.org` — open, confirmed with a real JPEG fetch (`talisman1978west$38`, FF D8 FF E0
  magic bytes). The page-image route itself is fine; it just can't reach any gap name archive.org
  doesn't hold a yearbook for.
- `archive.org`'s advanced-search API for `identifier:talisman*west` — still exactly the same 19
  volumes (1943, 1946, 1947, 1963-65, 1971-1981, 1986, 1987). No new volume since every prior check.
- `wkuherald.com`'s WP-JSON search — open; the 10 most recent SGA-tagged posts are unchanged since
  the 20 October "Pink Out" item already on file.

## A full sweep of `data/herald-index-full.json` against all 156 gap names

Earlier passes (16 Sept, 2 Oct, 22 Oct) spot-checked subsets of the gap list against the local
Herald index. This pass swept the whole list at once — all 156 people, matched by first+last name
substring, restricted to issues dated within each person's officer year ±1/+2 to cut surname
noise, then flagged for a student-government keyword. Zero network cost; the file is already on
disk.

Result: no name this run's filter did not already know about. The small set of genuine
student-government hits it surfaced are the same leads already on record and still blocked behind
`viewcontent.cgi` — Lisa Kappler and Corey Bewley's February 2009 chief-justice-succession articles
(`dlsc_ua_records/6721` and `/6720`), already logged as pending on 2 October. Both landing pages
were re-fetched directly this pass on the chance either carries an embedded thumbnail: neither
does — each exposes only its full plain-text article abstract as `<meta>` description, no image
tag. The actual page image is only reachable through the PDF, which stayed 403 all pass.

One correction worth recording so a future sweep doesn't re-flag it as a lead: the date-filtered
match for "Steve Wilson" (1978-79, Judicial Council Chairman) against "Wood, Michele. Steve
Fuller, Mark Wilson, Greg Zoeller Elected to Top Associated Student Government Jobs" (Herald
55:55, 24 Apr 1980) is a false positive from the substring match — the names present are Steve
**Fuller** and Mark **Wilson**, two different people, not this Steve Wilson. No lead.

Trent Lyda's and Kip Carr's hits (`Lyda, Trent. Associated Student Government: Don't Complain, Get
Involved`, Herald 67:40, 20 Feb 1992; `Carr, Kip. Issues Must be Addressed in Student Government
Association`, Herald 73:51, 23 Apr 1998) are both letters to the editor written by the officer
himself, not news coverage — this era's letters column does not run a photograph of its writer, so
neither is treated as an open photo lead even once `viewcontent.cgi` reopens.

## Conclusion

No new portrait landed. The main value of this pass is negative but complete: every one of the 156
no-portrait people has now been checked against the free, unrated local Herald index at least
once, in one pass rather than piecemeal, and the small number of real leads it turns up are already
the ones on file waiting on `viewcontent.cgi`. Both standing blocked routes were independently
reconfirmed closed. `python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean
against the unmodified tree. Nothing in `data/` changed. Landed on `research-photos`.
