# 4 October 2026 (photograph routine, third pass)

## Baseline reconfirmed before anything else

Computed directly from the data files rather than trusted from the two reports already filed
today: all 73 top-level `leaders` records (every president and every student regent, all 61
years) have a matching entry in `data/photos.json`, Nick Todd, Katie Dawson, Jeanne Johnson and
Reagan Gilley included. Priorities 1-2 in CLAUDE.md's own order are fully clear. 217
executive/Senate-officer records still lack a portrait (119 of them from 2010-11 onward), and 4
years still lack a year-level photograph (1994-95, 1995-96, 2000-01, 2008-09) — both counts
unchanged from this morning's two passes. `research-photos` merged `origin/main` with no
conflicts; `python3 scripts/build.py` and `python3 scripts/check_data.py` both run clean (61
years, 1967 events, 60 presidents).

## Both PDF routes retested cold, by three independent methods this time

- **Plain `curl`** with full browser navigation headers against `viewcontent.cgi?article=6747`
  (the standing 2008-09 lead, Kevin Smiley): `HTTP 403`, Cloudflare `cf-mitigated: challenge`,
  the same 5,995-byte "Just a moment..." interstitial every report since late September has
  logged, byte-identical.
- **The platform's own `WebFetch` tool**, a separate fetch path from `curl`, against the same
  URL: flat `403 Forbidden`.
- **`web.archive.org`**, plain `curl` against the CDX API: TLS handshake reset
  (`Recv failure: Connection reset by peer`), matching the "blocked again" state logged
  repeatedly this month.

No new information here beyond confirming, a third time today, that neither route opened during
this session.

## One new check, which closed negative: a Herald landing page's own embedded images are generic site art, not content thumbnails

Fetched `dlsc_ua_records/6747/` directly (the record page itself, not the blocked PDF) and pulled
both images its HTML embeds under `/assets/md5images/`. Both load cleanly outside
`viewcontent.cgi` — real files, `89 50 4E 47` and `GIF89a` magic bytes confirmed — but rendering
them shows the first is TopSCHOLAR/bepress's own four-color pinwheel logo and the second is a
matching decorative strip; neither is a scan of the Herald page or any photograph of Kevin
Smiley. This reproduces, for a Herald record specifically, the same finding the 2 October and 4
October (second pass) reports already made for a `stu_org` composite item: an item's embedded
`md5images` asset only ever shows whatever is embedded in that item's own description/metadata
text, not a rendered page of the underlying PDF. Herald issue records carry no such embedded
content image, only the standard site logo. This route is closed for the Herald/Talisman
material generally, not just for this one article.

## A route not logged as tried before: plain web search against wku.edu/wkuherald.com/digitalcommons.wku.edu, rather than each site's own internal search

Every prior report searched `wkuherald.com`'s own WordPress REST API or on-site search box.
Tried a different angle this pass — an external web search restricted to `wku.edu`,
`wkuherald.com` and `digitalcommons.wku.edu` — on the theory that Google's index might surface a
page either site's own broken or limited search misses. Tested against the strongest open
year-photo lead (Kevin Smiley, 2008-09) and three 2010s Judicial Council/officer names from the
dense post-2010 gap (Dajana Crockett, and two others). Every query returned only generic SGA
department pages, unrelated people of the same name, or — in one case — a genuine SGA news
article ("Newly elected SGA members share goals for the semester," `wkuherald.com/61104/`) whose
body names the person in text but whose accompanying photo carries no caption identifying anyone
in it. This is the same pattern (name in body text, uncaptioned or unrelated photo) every prior
systematic sweep of `wkuherald.com` has already found; recording the method as tried and
negative so a future run does not treat "try Google instead of the site's own search" as an
unexplored idea. It is not a promising route and is not worth a full 217-name sweep on this
showing.

## Nothing added

No portrait and no year photograph were added or removed this run. `data/photos.json` and
`data/photos/` are byte-for-byte unchanged from the merge-in of `origin/main`.

## For the next run

Unchanged from both earlier reports today: this project's research log now documents dozens of
closed alternate routes (`core.ac.uk`, `base-search.net`, `catalog.hathitrust.org`, the
`md5images` embed path, `wkuherald.com`'s REST API and on-site search, and now plain web search)
against the two routes — `viewcontent.cgi` and `web.archive.org` — that actually carry the
content. Every lead this record holds (the 2008-09 Kevin Smiley and Gilley-adjacent Herald
issues, the 68 newly-surfaced 2010s-2020s officer names, the four year-photo gap years) is
genuinely blocked on one of those two reopening, not on anything left unsearched. A future run
should keep testing both fresh, since this file has repeatedly shown both swing open and shut
within the same week, but should not re-spend a session re-trying the mirror hosts this and
the preceding reports already closed.
