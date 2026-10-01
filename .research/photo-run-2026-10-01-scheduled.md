# 1 October 2026 (photograph routine, scheduled run)

## What was checked before doing anything

The four named priority portraits — Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley — all
already carry a portrait in `data/photos.json`, as every run since 20 August has confirmed. More
broadly, all 73 top-level `leaders` records (every president and every student regent) have a
portrait, and 57 of 61 years have at least one year-scene photograph; the four without one are
1994-95, 1995-96, 2000-01 and 2008-09, unchanged since 30 September. No student body president or
student regent is missing a portrait. The only open gap is executive and Senate officer portraits:
217 officer/senate-officer records across the archive still lack one, concentrated in 1996-2023 and
worst from 2003 onward (157 of the 217).

## Access re-tested, nothing changed

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` still answers a bare request with `403` and
  `cf-mitigated: challenge` — a Cloudflare bot challenge, not the empty-202 session problem the
  browser-navigation headers fix. The item landing pages (`dlsc_ua_records/*`) still return a clean
  200; only the PDF endpoint is walled. No TopSCHOLAR path for the Talisman yearbooks exists at all —
  `digitalcommons.wku.edu/talisman/` is a plain 404, confirmed again, and no photo citation in this
  archive uses that path.
- `web.archive.org` still resets at the TLS handshake from this container.
- Re-checked whether archive.org might have added Talisman volumes outside its known 1971-1981,
  1986-87 window: `archive.org/metadata/talisman<year>west` returns HTTP 200 for every year tried
  (1982-2020), but with an empty `files` list and no title — archive.org's metadata endpoint returns
  200 for identifiers that don't exist, not 404, so this is a false signal, not a new find. The
  confirmed Talisman window on archive.org has not changed.
- `wku.edu/news` has no SGA tag or category page (`/news/tag/sga/` is a 404), so the browse-by-date
  route suggested at the end of the 30 September afternoon report does not exist either; its search
  parameter still ignores the query, as already documented.

## wkuherald.com, extended past the five names already tried

The 30 September run tried five of the most senior missing officer titles against the WordPress
search API and found real but unusable coverage (no individually captioned photograph). This run
tried six more, drawn from the same post-2003 gap, picked for lower-ranked offices (Judicial Council,
committee officers) to see whether a different tier of coverage existed: Matt Holland (Chief Justice,
2006-07), David Spalding (Chief Justice, 2011-12), Jacob Miers (Secretary of the Senate, 2007-08),
Liz Goddard (Director of Public Relations, 2007-08), Cacy Schooler (Secretary of the Senate, 2007-08),
Monique Gooch (Director of Public Relations, 2008-09).

Three returned no results at all. The other three returned real articles, none closer to a usable
portrait than the pattern already on record: two "Matt Holland" hits are a different, later Matt
Holland (a 2022 WKU dean of students story, a 2020 debate recap) with no connection to the SGA
officer; "David Spalding" turns up genuine SGA senate-removal coverage from 2011-12 with
`featured_media: 0` on the relevant posts, i.e. no image at all; "Cacy Schooler" matches a 2025
financial-aid story, an unrelated person despite the exact name. Nothing usable. This confirms,
rather than overturns, the 30 September finding: the WordPress-era Herald does not carry
individually captioned photographs for officers below the president/regent level in the searchable
window, at either end of the title hierarchy tried so far.

## Nothing added

No file in `data/photos.json` or `data/photos/` changed this run. `python3 scripts/build.py` and
`python3 scripts/check_data.py` both run clean against the unmodified tree (61 years, all 73 leader
portraits present, 217 officer portraits still open).

## For the next run

The three live routes (digitalcommons PDFs, web.archive.org, TopSCHOLAR Talisman) remain closed for
the reasons documented across the last several reports, and this run adds nothing to reopen any of
them. The one source actually open — wkuherald.com — has now had eleven of the 217 missing names
tried against its search API across two runs, spread across both ends of the title hierarchy, with
no individual portrait recovered either time. Trying more names one at a time against the same
endpoint is unlikely to behave differently without a change of method; a bulk pull of all SGA-tagged
posts' `content.rendered` (rather than one `search=` query per name) to check for in-body `<img>`
tags with captions naming officers directly, instead of relying on `featured_media`, is the untried
variant worth a future run's time.
