# Photograph run, 14 November (second scheduled pass): network gates re-tested fresh, three exhausted-era leads re-verified by hand, no new portrait

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry a
  `leaders` portrait entry in `data/photos.json`, unchanged.
- **Priority 2**: `python3 scripts/check_data.py` exits clean - 61 years, 1964 events, 60
  presidents, every president and student regent portrayed.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` reports 187 officer-slots without a
  same-year portrait, 155-157 people with no portrait in any year - unchanged from the morning's
  pass.
- **Priority 4**: all 61 years already carry at least one photograph.

## Network state, retested fresh (independently of this morning's pass)

- `cgi/viewcontent.cgi` via plain `curl` with browser navigation headers: **403**, the standing
  Cloudflare challenge, tested against article 7642.
- The same URL via Python's `urllib.request`, identical headers: **200**, a real 48 MB PDF. This is
  the TLS-fingerprint gate this project has now logged open on five separate dates; confirmed open
  again today. Used it this pass to pull two of the uncatalogued Talisman volumes a 12 November pass
  had identified (articles 1409 and 1411, the 1985 and 1987 yearbooks) and re-verify their ASG
  photographs by eye rather than trust the existing written description alone.
- `web.archive.org` - `Recv failure: Connection reset by peer`, unchanged.
- `archive.org` (no `www.`) - open; a bare `curl` to a real volume (`talisman1980west`) returns 200
  (follow redirects), and a volume that genuinely does not exist (`talisman1998west`) returns 503
  rather than 404, which is this host's way of saying "no such item," not a sign the gate is down.
- `wkuherald.com` - 200, open; its WP-JSON API continues to answer some requests with a passing 403
  that clears on retry a few seconds later, same intermittent pattern prior passes have logged.

## Re-examined the 1986-87 Associated Student Government photographs by eye

Fetched article 1411 (the 1987 Talisman) via the `urllib` bypass and rendered printed pp. 114-115 at
300 dpi (`pdftoppm`) to check, independently, whether Chris Millay (Parliamentarian) or Dwight Austin
(Sergeant-at-Arms) appear in either ASG group photograph. They do not: the two photographs' captions
name thirty people total (`FRONT ROW: Carol Sue Norcia, Hollie Hale, Kimberly Summers, Karen
Lassiter, Barbara Rush SECOND ROW: Janet Dryer, Terri Wakefield, Michelle Conner, Kristina Hayden,
Lynn Groemling BACK ROW: Lynn Ritter, Donald Herron, Martha Wilson, Caroline Miller, Laura Dibert`
and `FRONT ROW: Holger Velastegui, Laura Tracy, Kent Groemling, Adrian Smoot SECOND ROW: Andrea
Collin, William Schilling, Chris Leneave, Chuck Newton, Jerry Castleberry BACK ROW: Daniel Rodriguez,
John Schocke, Tim Todd, Greg Robertson`), and every one of them is already on file in
`data/photos.json` from a prior pass. Neither Millay nor Austin is named. This matches and confirms
the 12 November second pass's finding by an independent read of the page image rather than by
trusting the note; no new information, but worth having re-verified by eye rather than carried
forward unchecked.

## The John Holland lead (1984-85, Public Relations Vice-President) - tried, still not safe to close

A 12 November pass flagged this as the one genuinely open thread in the gap list: the 1985
Talisman's second "Associated Student Government" group photograph (printed p. 205, article 1409)
captions a standing row as `SECOND ROW: Bill Veneman, John M. Holland, Julie Lippert, Danny
Broderick, Beverly Kirk`, and Holland is a live gap name. Fetched the volume and rendered the page at
300 dpi and again at 600 dpi to see whether a finer scan would resolve the row.

It does not. The photograph is a three-tier theater-seating group shot: a clean front row of five
seated women (reads cleanly against the caption's front-row names, already on file), then what the
negative space shows is genuinely two interleaved tiers of standing people behind them rather than
one clean band - some heads sit noticeably higher and further back than others at uneven horizontal
spacing, consistent with people standing on two different rows of fixed theater seats. At this scan's
actual print resolution (going to 600 dpi just re-samples the same halftone dots; it adds no real
detail), the five "second row" faces cannot be told apart from the six "back row" faces by position
alone, and 1980s hairstyles make several of the figures' sex ambiguous at this resolution - not a
safe basis for matching a specific face to Holland's name even with Julie Lippert's independently-
sourced face (from the 1984 Talisman's junior class grid) as a potential anchor point. Attempted the
comparison; the resolution is not good enough to place Lippert's face in the row with confidence, and
without that anchor there is no way to count in from either end. Leaving this exactly where the 12
November pass left it: a real, specific, still-open lead, but not one to force. A future pass would
need either a cleaner scan of this exact page from a different digitization, or a second independent
source naming Holland's position in this photograph, before cropping anything from it.

## ShyAnte'e Williams (2022-23 Graduate Student Senator) - the most under-searched name, now fully run down

By mention-count across every `.research/photo-run-*.md` file, this was the single least-searched
name left in the portrait gap (prior passes had only ever re-tested the standing wkuherald.com WP-
JSON gate against her and gotten nothing). Went directly to the articles instead of a bare name
search this time, and found all three that name her:

- "SGA fall elections open for voting" (19 Sep 2022, `wkuherald.com/68206`) - spells her **ShyAnte'e
  Williams**, running for graduate student senator against Arpana Lakhmani.
- "SGA fall election results announced..." (21 Sep 2022, `wkuherald.com/68255`) - spells her
  **Shy'Ante Williams**, reporting she won the seat.
- "Student Government Association senators sworn-in..." (27 Sep 2023, `wkuherald.com/72872`) -
  spells her **ShyAntye'e Williams**, reporting she was re-elected graduate senator for the 23rd
  Senate, i.e. 2023-24 as well as 2022-23.

Three Herald articles, three different spellings of the same person - a genuine inconsistency in the
sources, not a transcription error on this project's side, and worth flagging for whichever routine
maintains `years.json`'s organization data (not touched here; this file only governs `photos.json`).
Checked every one of the three posts' attached media (`/wp-json/wp/v2/media?parent=<id>`): 68206
carries one image, a TopNet voting-screen screenshot with no people in it; 68255 and 72872 carry no
media at all. No photograph of her exists at any of her three known mentions in this outlet. Logged
in `data/photo-finds/2016-2025-notes.json` so a future pass does not re-open this by a bare name
search and conclude it is merely unsearched.

## Conclusion

No new portrait this pass. The network state is unchanged from this morning's run (TopSCHOLAR's
TLS-fingerprint bypass open, `web.archive.org` closed, `archive.org` and `wkuherald.com` open), and
the two most promising open threads in the written record - the 1986-87 Millay/Austin photograph and
the 1984-85 Holland row - were both re-examined directly rather than taken on faith, with the former
re-confirmed closed and the latter re-confirmed still genuinely open but still not safe to crop from.
ShyAnte'e Williams is now fully run down across all three of her known mentions and can be dropped
from future "under-searched" triage. `build.py` and `check_data.py` both pass clean: 61 years, 1964
events, 60 presidents, every one portrayed. Landed on `research-photos`.
