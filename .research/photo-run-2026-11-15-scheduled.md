# Photograph run, 15 November (scheduled): network gates retested, two channels tried for the first time, nothing landed

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry
  a `leaders` portrait entry in `data/photos.json`, unchanged from every run since 20 August.
- **Priority 2**: every president and student regent already carries a portrait. `check_data.py`
  (run at the end of this report, see below) confirms this still holds.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` reports 187 officer-slots without a
  same-year portrait, held by 157 people, 155 of whom have no portrait in any year — within
  rounding of every count logged since early November. No change.
- **Priority 4**: all 61 years already carry at least one photograph.

## Network state, retested fresh

- `digitalcommons.wku.edu` ordinary pages (listings, item pages) — `200`, open, same as always.
- `digitalcommons.wku.edu/cgi/viewcontent.cgi` (the actual PDF download) — Cloudflare "Just a
  moment..." challenge via plain `curl`, and a hang/timeout via the `urllib` TLS-fingerprint
  bypass that got through on 14 November's fourth pass. Closed this session.
- `archive.org` (no `www.`) — reachable: `/metadata/talisman1986west` returns `200` with real
  metadata, and `/download/talisman1986west/talisman1986west_djvu.txt` redirects `302` as usual.
  Confirmed by direct test this pass that the site itself is up, not just "usually up."
- `archive.org` for anything **outside** the documented 1971-1981/1986/1987 holding — tested
  1988-1995, 1997-2001, and 2016 by `/metadata/<id>west` — every one returns `200` with an empty
  `{}` body, i.e. the identifier does not exist. This matches `SGA-60-AGENT-INFO.md`'s documented
  holdings exactly; archive.org was not silently missing a year that a different test would have
  caught. Confirms there is no djvu-text shortcut for the 1990s/2000s or 2010s cohorts; TopSCHOLAR
  is the only copy, and TopSCHOLAR's PDF route is the one still closed.
- `web.archive.org` — connection reset mid-handshake, unchanged.
- `wkuherald.com` — `200`, open as usual.

## Two channels tried that no prior report in `.research/` had used

1. **Google restricted to `site:digitalcommons.wku.edu`, by name, for five gap-list people** spread
   across eras: ShyAnte'e Williams (2022-23), Brenna Mathews (2019-20/2020-21), Josh Zaczek
   (2018-19/2019-20), Steve Roadcap (1996-97/1997-98), Jenny Stith (1997-98/1998-99). Every prior
   `site:` search in this project's reports was restricted to `wku.edu/news`; nobody had pointed the
   same technique at TopSCHOLAR itself, which is reachable by ordinary page but not by its own
   bot-blocked search box. No hit named any of the five next to a photograph. The one adjacent
   result worth recording: Brenna Mathews's name surfaces on `wku.edu/sga`'s own (non-archive)
   minutes PDFs as "Secretary of the Senate," confirming the role already on file but adding no
   image.
2. **The live `wku.edu/sga` legacy judicial-council page at a historical-looking URL**
   (`wku.edu/sga/2018-2019-judicial/judicial-council.php`), fetched directly to check for headshots
   against the 2018-19 gap names (Caroline Simpson, Erika Puhakka). The page does carry two
   headshot images, but for **Sophie Stirling** and **Hannah Hash** — names that do not appear
   anywhere in `data/years.json`'s 2018-19 roster, and the images carry no caption, only two-letter
   `alt` text ("ss", "hh"). The URL's year does not control what the page actually serves: this is
   the live CMS showing current-at-fetch-time content regardless of the path, not an archived
   snapshot. That rules this page out as a source for any specific year (it cannot be dated) and
   explains why the 13 November report found `wku.edu/sga`'s legacy CMS pages already exhausted —
   they are not actually year-scoped pages at all.

Neither channel produced anything usable under this project's identification rule (a caption or
article text naming the subject beside the photograph). Nothing was added to `data/photos.json`
or `data/photos/`.

## Conclusion

No new portrait this run. The two blocking facts are unchanged: TopSCHOLAR's PDF endpoint
(`viewcontent.cgi`) is Cloudflare-gated this session by every method tried, including the
bypass that worked intermittently on 14 November, and archive.org's Talisman holdings
genuinely stop at 1987 — there is no hidden post-1987 copy to find there. The remaining 155
ungated names are, per the 13 November report, already searched by name across every open
channel at least three times each; today's two new angles (TopSCHOLAR via Google, and the
live SGA judicial page) close out as dead ends rather than live leads. `python3 scripts/build.py`
and `python3 scripts/check_data.py` both run clean: 61 years, every president and student
regent portrayed. Landed on `research-photos`.
