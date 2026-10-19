# Photograph run of 19 October (scheduled): baseline reconfirmed, two new 2026-27 officer gaps checked and closed negative, both TopSCHOLAR routes retested and still closed

## Priorities 1, 2 and 4: reconfirmed, unchanged

Checked against the current `data/years.json` and `data/photos.json` before touching anything:

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait. Done well before this run, and done again every run since.
- **Priority 2** (every other student body president or student regent): zero gaps. All 73
  `leaders` records across 61 years carry a portrait.
- **Priority 4** (years with no photograph at all): zero. Every year carries at least a leader
  portrait or a year-level photograph.

`python3 scripts/portrait_gap.py --list` reports the same 189 officer slots with no portrait as
the 18 October runs, held by 159 distinct people, 157 with no portrait anywhere in the file.
Cross-checked every one of those 157 names against this file's own `.research/*.md` history: all
157 have already been searched at least once in an earlier run (Herald index, wkuherald.com,
general web search, or a Talisman volume read page by page), most more than once. This run did
not re-run those searches; it checked the two names new to the record since the last photograph
run instead (below).

## Network state, retested fresh

- `cgi/viewcontent.cgi`: HTTP 403, Cloudflare "Just a moment..." challenge. Still closed.
- `web.archive.org`'s `if_` bypass: `curl: (35) Recv failure: Connection reset by peer`, confirmed
  at the agent proxy as a `ws_closed_mid_exchange` tunnel failure, not just a client-side error.
  Still closed.
- `archive.org` (the plain item/download host, not `web.archive.org`): open, confirmed with a real
  `_djvu.txt` pull and an `advancedsearch.php` metadata query this run.

**Re-confirmed directly rather than assumed: `archive.org` holds no Talisman identifier for 1982
through 1985, and none for any year after 1987 until an advanced search turns up nothing at all
for `talisman20*west` or any 1990s `talisman19*west` beyond 1986-87.** This matches the standing
note in `SGA-60-AGENT-INFO.md` §4 exactly (archive.org holds 1971-1981, 1986, 1987, and not
1982-1985) and extends it: the gap runs all the way from 1988 to the present on this host. Every
remaining officer-gap name from the 1990s through the 2020s depends on either `viewcontent.cgi`
(for the pre-2003 Herald and the 1988-2003/2012+ Talisman volumes TopSCHOLAR holds) or
`wkuherald.com` (for roughly 2003 onward), never on `archive.org`.

## Two names new to the record since the last photograph run: Elizabeth Allen and Tyreesha Morris

`data/years.json`'s 2026-27 entry records a 25 August 2026 Senate meeting swearing in nine
committee chairs (Herald, "SGA kicks off 60th year on campus, swears in new committee chairs").
Seven of the nine already carry a portrait from an earlier year (Jade Ismail, Amelia Tucker,
Landon Terry, Jackson Smith, Ethan Vietze, Gabi Pace, Molly Ricke/Ricky). Two do not and are new
to this archive's record: **Elizabeth Allen** (Chair, Campus Safety and Security) and **Tyreesha
Morris** (Chair, Mental Health and Well-Being).

- **The swearing-in photoshoot itself has no individual caption to use.** The article's three
  frames from that night (`wp-json/wp/v2/media` ids 96582, 96583, 96584, filenames
  `082526_SGA_BH-5-1`, `082526_SGA_BH-3`, `082526_SGA_BH-6`) all caption as a group - "nominees
  for speaker of the Senate and committee chairs... are sworn in" - or name only President Caden
  Lucas. No frame's caption picks out Allen or Morris by name, so neither can be identified from
  it even though both are almost certainly somewhere in the group photograph.
- **Tyreesha Morris**: searched `wkuherald.com`'s post and media search for "Tyreesha" (0 media
  hits, 5 post hits) and read every image caption on the four SGA-adjacent posts that aren't the
  swearing-in story itself (presidential election, the restaurant-group Q&A, the SNAP-cuts
  response, the Domestic Violence Awareness piece) - none names her. A general web search turned
  up nothing beyond a third-party Instagram mirror listing her name in an unlabeled roster of
  about nineteen people with no role given, which is not a usable identification. Not found.
- **Elizabeth Allen**: searched the same way. `wkuherald.com` media search for "Elizabeth Allen"
  returns one real hit, media id 98160, 15 October 2026: "Elizabeth Allen, left, president of the
  pre law student association tables during the PCAL Fall Festival at the Colonnades... 'Our goal
  is to help students to connect to PCAL as a whole not just to law students,' Allen said." This
  is a clean, individually captioned, direct-quote identification of an Elizabeth Allen at WKU in
  the same semester as the SGA chair of that name - but the caption describes her **pre-law club
  presidency, not any SGA role**, and nothing in the article or caption connects the two offices.
  **Declined rather than used.** This run's brief is explicit that a portrait should show someone
  acting in their student government role, not any photograph of the same name found on a
  university news page; a tabling photo for an unrelated student organization does not clear that
  bar even where the identification itself would otherwise be sound, and the risk of a same-name
  mismatch (common first and last names, no SGA context to cross-check against) is exactly the
  kind of identification CLAUDE.md's portrait rule exists to guard against. Left as a lead for a
  later run if an SGA-context photograph of her ever surfaces, not used now.

Neither name is added to `data/photos.json`. Both remain open.

## No file changed in `data/photos.json` or `data/photos/`

This run's only output is this note. `python3 scripts/build.py` then `python3 scripts/check_data.py`:
both pass clean - 61 years, 60 presidents, no missing leader portrait, no year without a
photograph. Working tree is `origin/research-photos` plus `origin/main`'s commits since the last
merge, plus this file. Landed on `research-photos`.
