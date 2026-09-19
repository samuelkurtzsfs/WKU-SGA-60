# Photograph run, 19 September (scheduled) — nothing added, three negative searches worth recording

## Starting state, re-confirmed

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md` and `SGA-60-AGENT-INFO.md` §4 and §6
before touching anything. `research-photos` had one unmerged `origin/main` commit (the 19
September night report); merged it cleanly with the required commit identity
(`SGA 60 <kurtztoddsam2@gmail.com>`).

Checked the four standing priorities fresh against current `data/years.json` and `data/photos.json`:

- **Priorities 1 and 2 (presidents and regents): fully satisfied**, independently reconfirmed.
  All four named presidents (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley) and every
  other `leaders` entry with `role: "president"` or `role: "regent"` across all 61 years has a
  portrait, and the four named files all check out as real JPEGs (`ffd8ffe0`).
- **Priority 4 (a photo for every year): satisfied at the minimum bar.** All 61 years carry at
  least one photograph.
- **Priority 3 (cabinet/Senate officers): the open queue**, unchanged in scale from the last
  several reports — 34 executive-cabinet names and roughly 183 Senate-officer/committee-chair/
  senator names still carry no portrait.

## Read `.research/` for same-cluster reports before spending time — as instructed, and it paid off

`photo-run-2026-09-17-officer-search.md`, `-wayback-pdfs.md` and `-2026-09-18-morning.md` had
already exhaustively checked David Bass, Alice Wicks, Mark Chesnut, David Young, Chris Millay,
Vern Pulman, Dwight Austin, Kelly S. Smith, John Holland and Connie Hoffmann against every
Talisman year archive.org or the Wayback-PDF route can reach for 1974-1987. This run did not
repeat any of that — see "Left for the next run" in those files for what remains genuinely open
on those specific names (the 1984 class-portrait grids for Smith/Holland, still an unread,
low-OCR page-by-page job; the 1985 Chi Omega composite for Hoffmann, deliberately left unused).

## Three new negative checks, done properly rather than skipped

**Mickie Hennig (Secretary, 1988-89) — checked against the 1989 Talisman's own back-of-book name
index, not just its group photographs.** Downloaded `talisman1989.pdf` via the Wayback capture
described in the 17 September report (`web.archive.org/web/20240908065242id_/...article/1413/...`,
189 pages, downloaded whole — no truncation this time). The volume's index runs pp. 178-186 of the
PDF (spreads); read the full "He-" through "Hu-" run on p. 180 by eye (Hedrick, Heflin, Helfenbein,
Hensley, Helm, Helton, Hendon, Hendricks, Hendley... straight through to Hubbard) and there is no
"Hennig" entry at all — not a blank page number, an absent name. This is stronger evidence than
the earlier check (which only ruled her out of one already-known group photo): a name absent from
a working alphabetical index across the whole book strongly suggests no individual portrait or
group-photo caption exists in this specific volume. Left without a portrait; the 1988 Talisman
(one year earlier, when she may have been photographed as an incoming officer) is still unread.

**David Smith (Chair, Academic Affairs, 1992-93) and Trent Lyda (City Council Representative,
1992-93) — checked against the 1993 Talisman's index, a volume neither this cluster of reports nor
any earlier one had opened.** This is a new year pulled from the Wayback-PDF technique's own
documented gap list (`article/1417`, `talisman1993.pdf`, 144 spread pages, confirmed against the
live TopSCHOLAR yearbooks listing first — `digitalcommons.wku.edu/dlsc_ua_yearbooks/`, entry
"UA12/2/2 Talisman: A New Shade of Red" — before trusting the Wayback capture's filename). Its
index (pp. 137-140) has good OCR quality (real words, not the near-garbage of the 1984/1993-era
scans described in earlier reports) and runs the full alphabet cleanly. Read the complete "L"
section (p. 139: Ladas through Lynn, including Logsdon, Lohr, Lomax — no Lyda) and the complete
"S" section (p. 140: Saab through Suddath, including a long run of nine other Smiths — Beth,
Brian, Carla, Chris, Crystal, Deborah, Denise, Derrick, Donald, Frances, Gary, Heather, Janice,
Matthew, Melissa, Michael, Michelle, Nathan, Orbin(?), Robyn, Shaun, Thomas, Tim, Traci, Travis —
but no David). Neither name appears anywhere in this volume's index. Left without a portrait.

**Mapped how the TopSCHOLAR Talisman collection is actually organized, which the next run can use
directly instead of re-deriving it.** `digitalcommons.wku.edu/talisman/` (a guess at a collection
slug) 404s — the real listing is `digitalcommons.wku.edu/dlsc_ua_yearbooks/`, reachable live and
not Cloudflare-gated (only `/cgi/viewcontent.cgi`, the file server, is gated). A `viewcontent.cgi`
`article=N` number and the item's public landing-page URL `dlsc_ua_records/<N-1000>` are the same
item, offset by exactly 1000 (confirmed: article 1408 / landing `/408/` = 1984 "The Touch of Red";
article 1417 / landing `/417/` = 1993 "A New Shade of Red"). **The Talisman itself has a real
publishing gap: nothing in the collection between the 1996 volume and a 2003 volume
("About Face," article 1594, landing `/594/`)** — the collection listing runs 1972 through 1996
consecutively by descending article ID (404-422ish) and then jumps straight to 594 for 2003, with
no 1997-2002 entry of any kind in between. This explains why the Wayback-PDF CDX query (`filter=
original:.*talisman.*`) that works cleanly for 1980-1995 turns up nothing for those years: **there
is nothing to find, not a search failure.** The six missing exec/Senate names that fall in this
1996-97 through 2002-03 window (Steve Roadcap, Ryan Faught, Jamie Fite, Amanda Cole, Mitchell
Bailey, and the whole 1997-98/1998-99 Senate list) have no Talisman-derived path to a portrait at
all — Herald indexing (`data/herald-index-full.json`, `data/herald-photos.json`) or Wayback
captures of `wku.edu`'s own SGA officer pages are the only routes left for that specific window,
and this run did not have time to try either against this particular name list.

The 2003 "About Face" volume itself was not opened this run — it covers the 2002-03 academic
year, one year before the earliest missing name in that stretch (Matthew Pava, 2003-04), so it was
not an obvious match and was left for whichever future run reaches 2003-04 specifically.

## Fresh cross-check: 41 missing 2018-2026 Senate/committee names against wkuherald.com's live search API directly

The 18 September report's index-based cross-check used a locally cached snapshot of captioned
`wkuherald.com` photographs (`data/herald-photos.json`). This run queried the live
`wkuherald.com/wp-json/wp/v2/posts` search endpoint directly, one name at a time (1.5s apart,
well under any rate limit trouble so far observed on this host), and for every returned post
pulled its embedded featured-media caption via `_embed`, checking for both the first and last
name together in the caption text — the same standard the 18 September report used to accept
Jackson Smith. Tried: Zachary Skillman, Justin Goins, Elizabeth DeLozier, Brenna Mathews, Erika
Puhakka, Turner Reynolds, Alexis Mayne, Jesse Banales, Maksim Zaepfel, Danny Vuleta, Neel Patel,
ShyAnte'e Williams, Gunnar Robinson, Mallory Hardesty, Callison Padgett, David Darnell, Elizabeth
Gannon, Jillian Kenney, Hope Wells, Josh Zaczek, Jason Herlick, Nicole Massarone, Garrett Baum,
Caleb Collins, Trevor Clark, Juan Tomas, Barrett Gibbs, Reed Hensley, Brooke Mitchell, Livi Ray,
Maiah Cisco, Connor Ferguson, Joel Hornback, Miles Harvey, Zoe Martin, Tyreesha Morris, Nolan
Rongey, James Cecil, Abi Canter, Caroline Simpson, Cassidy Townsend, Tribhuwan Singh.

Zero caption hits. Five of the 41 (Skillman, Zaepfel, Vuleta, Gunnar Robinson, Singh) return zero
Herald search results at all — not just no photo, no article mentioning them by name anything the
Herald's own search can find. Spot-checked one incidental lead this turned up anyway: a WKU-news
search result described Zachary Skillman in a February 2022 feature about attending college
alongside his brother — unconnected to his SGA committee-chair role, so per the same privacy
reasoning the 18 September report applied to Cody Cox and Mark Clark, this would not be usable
even if pulled up directly. Did not chase it further.

## Nothing added

`data/photos.json` and `data/photos/` are unchanged this run. `python3 scripts/build.py` and
`scripts/check_data.py` both pass clean on the unmodified data (`site/` was regenerated, diffed
against the committed copy to confirm no content changed, and reverted with `git checkout --
site/` rather than committed — nothing in this run touched `data/`, so there was nothing for a
rebuild to reflect). No commit was needed for the data side; this report is the only new file.

## Left for the next run

- The 1996-97 through 2002-03 Talisman gap (Roadcap, Faught, Fite, Cole, Bailey, and the 1997-99
  Senate lists) has no Talisman path at all. Worth trying `wku.edu`'s own SGA officer pages via
  Wayback (`web.archive.org/web/*/wku.edu/Dept/Org/Student/SGA*`, per `SGA-60-AGENT-INFO.md` §4)
  for this specific stretch, which no report so far has pointed at this exact gap.
  `dlsc_ua_yearbooks/` is a genuine collection-browse page and unblocked live — use it, not a
  guessed slug, to confirm any Talisman year's existence and article ID before assuming a Wayback
  miss means a search failure.
- The 1984 Talisman class-portrait grids (Kelly S. Smith, John Holland) are still unread — same
  status as every report this week, flagged again rather than reattempted at real cost for a
  fourth time.
- 39 more 1990s-2020s cabinet/Senate names remain entirely unchecked against the Talisman-gap-era
  or newer-era sources; this run's 41-name Herald sweep and two Talisman-index checks did not
  overlap with most of the 34+183 total, so the backlog's true size is closer to 170+ after
  today's negatives are subtracted out as "checked, not just missing."
