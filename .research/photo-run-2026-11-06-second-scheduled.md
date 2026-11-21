# Photograph run, 6 November second scheduled pass: Issuu and the Talisman's own current site tried and closed, baseline and three standing network blocks reconfirmed unchanged, no new lead

## Priorities 1, 2 and 4, reconfirmed directly against the files

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`. Unchanged.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — "61 years, 1964 events, 60 people
  have been president," no portrait-coverage complaint. Zero presidents or student regents
  without a portrait across all 61 years.
- **Priority 4**: every year still carries at least one photograph.
- **Priority 3** (officer/Senate gap): `python3 scripts/portrait_gap.py --any-year` reports the
  same figures as the pass six hours earlier: 948 officer slots, 188 without a portrait for that
  person in that year, held by 158 people, 156 with no portrait anywhere in the file. Every one of
  the 158 already has an individual check on record; no name added or removed since.

## A genuinely new avenue tried this pass, and closed

The Talisman stopped being a print yearbook after its 2019 editions (confirmed against
`digitalcommons.wku.edu/dlsc_ua_yearbooks/`, which is reachable directly — HTTP 200, unlike the
`cgi/viewcontent.cgi` download path — and lists only two 2019 items, "2019 Talisman: Balance" and
"2019 Talisman: Paradise," nothing dated 2020 or later). That is most of why the officer/Senate
gap concentrates in 2019-2025: there is no yearbook covering those classes to search in the first
place, on TopSCHOLAR or on archive.org.

That raised a question not on record in any earlier pass: does the Talisman's post-yearbook output
survive anywhere with a names-and-faces format? Two leads, both closed negative today:

- **`issuu.com/wkutalisman`** — HTTP 404. No account at that handle. A web search for
  `issuu.com/wkutalisman` turned up nothing Issuu-hosted at all; the one WKU hit was an unrelated
  2020 Herald town-hall story. Not a route.
- **`wkutalisman.com`** — reachable (HTTP 200), but it is the current Talisman staff's own
  WordPress site, a campus lifestyle magazine (categories: Culture, Opinion, Our Hill, 270
  Chronicles, galleries of concerts and events). Skimmed its link structure: no student-government
  or SGA category or tag exists, and the "Our Hill/People" section is profiles of students and
  professors unconnected to SGA. Not a source for named SGA officers; not pursued further; this is
  not the kind of personal/social material CLAUDE.md asks this routine to stay away from either way.

Neither lead reaches any of the 158 gap names. This closes the "does the Talisman have a
post-yearbook substitute worth searching" question for good — it does not — rather than opening a
new line of individual name checks.

## Network state, retested fresh

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` (article 7642, the 2009-10 lead), full browser UA
  plus navigation headers: `HTTP 403`. Unchanged.
- `archive.org/advancedsearch.php` on `identifier:talisman*west`: still exactly 19 volumes (1943,
  1946-47, 1963-65, 1971-81, 1986-87). No coverage of the 1990s-2020s where the gap sits.
- `web.archive.org`: direct fetch still fails at the connection level (`curl: (35) Recv failure:
  Connection reset by peer`). Still closed.
- `wkuherald.com`'s WP-JSON endpoint: open, `200`. Already exhausted against the full 158-name gap
  list; no new name to search against it this pass.
- `digitalcommons.wku.edu` landing/index pages that are not `cgi/viewcontent.cgi` (e.g.
  `dlsc_ua_yearbooks/`) answer `200` normally. The block is specific to the PDF-download CGI path,
  not the whole domain — worth remembering for a future pass that only needs an item's catalogued
  title or description, not its page images.

## Conclusion

No new portrait landed. `data/photos.json` and `data/photos/` are unchanged from
`origin/research-photos`. `python3 scripts/build.py` and `python3 scripts/check_data.py` both
exit clean. Presidents and regents remain fully covered, every year has at least one photograph,
and the 156-person no-portrait-anywhere gap — almost entirely 2019-2025 senators and committee
officers, a span the Talisman never covered as a yearbook — stays blocked on the same three
closed network routes, now with the Issuu and wkutalisman.com questions also closed. No untried
name and no untried route remain on file for this gap; a future pass should keep retesting the
three standing blocks for a change in state rather than re-searching this list.
