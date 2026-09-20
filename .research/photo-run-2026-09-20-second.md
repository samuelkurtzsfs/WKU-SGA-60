# Photograph run, 20 September (second scheduled firing): the Wayback window opened, four year-photographs landed

## Starting state

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md` and `SGA-60-AGENT-INFO.md` §4 and §6, then
found this session's own scheduled trigger had already fired once today: `.research/photo-run-
2026-09-20-scheduled.md`, merged into `main` a few hours earlier, found priorities 1 and 2
(president and regent portraits) fully satisfied, priority 4 (year photographs) short eleven
years, and both `digitalcommons.wku.edu/cgi/viewcontent.cgi` and `web.archive.org` blocked for
that entire run. Re-checked both routes fresh rather than trust that report's "blocked" finding as
still true, per this file's own standing advice that access varies run to run.

`digitalcommons.wku.edu/cgi/viewcontent.cgi` was still behind a Cloudflare challenge on a direct
request. `web.archive.org`'s CDX API and its raw-capture endpoint, however, were reachable this
run — intermittently (several individual requests came back "Recv failure: Connection reset by
peer," one hit `archive.org`'s own "Temporarily Offline" page, one hit a `504 Gateway Time-out`),
but a plain retry after a few seconds' pacing cleared each of those every time. Confirms the
standing note that this route is worth testing fresh every run rather than assumed closed from one
failure.

## Method used this run

For a given Herald or Talisman item already known from `dlsc_ua_records/<item>/`, its landing page
(not gated) was fetched to read the real `article=` number directly from its download link, then
`web.archive.org/cdx/search/cdx?url=digitalcommons.wku.edu%2Fcgi%2Fviewcontent.cgi%3Farticle%3D
<N>%26context%3Ddlsc_ua_records&output=json&filter=statuscode:200` was queried for a clean capture
timestamp, then the PDF was pulled from the `if_` raw endpoint at that timestamp. `pymupdf` (not
preinstalled; `pip3 install pymupdf pillow` pulled it clean) rendered pages to images for reading
since several of these older issues carry no text layer, or one too poor to keyword-search.

## Four year-photographs added, all newly identified and captioned

Went after the eleven general-year-photograph gaps the morning report re-confirmed (1994-95,
1995-96, 1996-97, 1997-98, 2000-01, 2002-03, 2003-04, 2005-06, 2006-07, 2008-09, 2009-10), working
from candidate Herald issues already logged in `data/herald-index-full.json` for each academic
year (spring elections filed to the year the winner serves, per the dating law, but a general year
photograph is dated by when the picture was actually taken — an election-night photo from a spring
issue belongs to the academic year the paper was printed in, not the year the winners go on to
serve).

- **2002-03** — `2002-03-election-night-2003.jpg`. Herald
  78:49, 8 Apr 2003, p. 1, photo by Justin Fowler: "Paducah junior John Bradley congratulates
  Marion junior Patti Johnson after the election while Henderson sophomore Nick Todd congratulates
  Abby Lovan, a junior from Jeffersonville, Ind." All four named in the printed caption.
- **2003-04** — `2003-04-election-night-2004.jpg`. Herald 78:47, 18 Mar 2004, p. 1, photo by James
  Branaman: "Student Government Association President-elect Nick Todd hugs Administrative Vice
  President-elect Evelina Petkova after the final results were announced shortly after midnight,"
  with defeated candidate Josh Collins named at right. This is the front-page lead photo of the
  issue, not a small inset.
- **1997-98** — `1997-98-sga-campaigning.jpg`. Herald 73:53, 30 Apr 1998, p. 8, photo by Catherine
  Cull: "While campaigning for Tuesday's SGA elections, Central City junior Brad Sweatt greets his
  friend, Louisville freshman Jackie Ayers, in front of the Downing University Center." The print
  is dark and both figures are substantially silhouetted — noted plainly in the caption added to
  `photos.json` — but the printed caption identifies both by name, which is the bar CLAUDE.md sets,
  not image clarity.
- **2008-09** — `2008-09-kevin-smiley-10-questions.jpg`. Herald 84:52, 7 May 2009, p. 7B, the
  Diversions section's "10 Questions with SGA President Kevin Smiley, a Danville junior" feature.
  Smiley already has a leader portrait from a different source (a November 2008 Daily News piece);
  this is a second, independently sourced and captioned photograph, used here for the year rather
  than duplicating his leader entry.

All four verified as real JPEGs (`ffd8ffe0`) before being added. `python3 scripts/build.py`,
`check_data.py` and `check_duplicates.py` all pass clean; the four known duplicate-event pairs are
unchanged and untouched (this run only touched `photos.json` and `data/photos/`).

## Leads chased and closed negative

- **The 2013–2019 "magazine-style" Talisman years, flagged by the 19 September report as an
  untried Wayback target for the dense 2016-17/2017-18 officer-portrait gap, are a dead end.**
  Pulled both the 2016 (*Identity*, article 9666, 99 MB) and 2017 (*Well Being*, article 9670, 98
  MB) volumes via Wayback captures neither prior run had used. Neither contains the word "Senate,"
  "SGA," "Student Government" or "Associated Student" anywhere close to a captioned photograph, and
  neither carries a single name from the ~30-person 2016-17/2017-18 missing-officer list. The 2017
  volume mentions "SGA" exactly twice, both in unrelated stories (a farmers'-market funding
  mention, and Sustainability Committee chair Savannah Molyneaux quoted in a sustainability
  feature with no photograph of her). This closes the whole 2013-2019 Talisman avenue for the
  officer-portrait backlog — it is not merely unsearched, as the 19 September report treated it,
  but structurally without the alphabetical club section or composite photographs the older
  Talismans have.
- **The 1996-04-25 Herald swearing-in article** (`dlsc_ua_records/2986`, article 3986), left open
  by the very first 20 September report as "still an open, promising lead" for the 1995-96/1996-97
  gap, was pulled and read. It is a text-only story with no accompanying photograph of any officer
  — Kristen Miller, Carlene and Darlene Lodmell, Steve Roadcap and Shawna Whartenby are all named
  in running prose only. Closed negative; the 1995-96/1996-97 gap remains open and this specific
  lead should not be retried.
- **"Johnson elected new speaker of the senate"** (Herald 81:24, 8 Dec 2005, p. 5A, article 4674),
  chased for 2005-06, is also text-only — no photograph of Jeanne Johnson runs with it, only an
  unrelated Kwanzaa photo elsewhere on the same page. Closed negative.
- **The 23 April 2010 "10 Questions with SGA president-elect Colton Jessie"** (article 7642, long
  logged as the "strongest 2009-10 lead" every prior run had failed to reach) was finally pulled
  via Wayback and read in full. It is real and well-captioned, but it belongs to **2010-11**, not
  2009-10 — the article says outright Jessie "will serve as president for the 2010-2011 school
  year," consistent with the dating law. Both Jessie (leader portrait) and 2010-11 (a different
  year photograph, the DUC resolution vote) are already on file, so this closes the lead without
  adding anything: **2009-10 is still without a year photograph**, and this was the strongest
  candidate on record for it.
- **The 15 March 2001 "Four winners and more than 15,000 losers"** (article 10081, chased for
  2000-01) is an opinion-page editorial cartoon — a hand-drawn mock ballot — not a photograph of
  any person. Closed negative, confirming the 28 August report's conclusion that 2000-01 needs a
  different source.

## Left for the next run

Seven year-photograph gaps remain: **1994-95, 1995-96, 1996-97, 2000-01, 2005-06, 2006-07,
2009-10.** 1996-97 and 2005-06 both have a leader portrait on file (Kristen Miller; the Speaker
search above) but no distinct year-level photograph — a different image would be needed, not a
re-use of the leader's own portrait. The 2013-2019 Talisman route is now confirmed closed for the
officer-portrait backlog specifically (see above); it was not re-tested against the year-photograph
gaps, which is a narrower and different question (a campus-life or election photo rather than a
named officer), and could still be worth a look for 2005-06 or 2006-07 specifically if a future run
has time.

The Cloudflare block on `viewcontent.cgi` itself did not lift once this run; every download here
came through `web.archive.org`'s raw-capture mirror, and that route is worth trying first, before
assuming it is closed, on the next run — it cleared on retry every single time it failed here.
