# Photograph run, 17 November (second scheduled pass): current-term senator gap checked fresh, no new portrait

## Baseline reconfirmed

- Priority 1 (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- `python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean: 61 years, 1964
  events, 60 presidents, every president and student regent portrayed. No `data/` changes this
  pass, so the `site/` rebuild (date-stamp only) was discarded rather than committed.
- `python3 scripts/portrait_gap.py --any-year` still reports the same 187 officer-slots without a
  same-year portrait, 155 people with no portrait in any year.

## Network gates, retested fresh

- `cgi/viewcontent.cgi` via plain `urllib.request` with navigation headers and a matching
  `Referer`: 200, a real PDF (tested against article 1418, the 1994 Talisman) — open this pass.
- `web.archive.org`: connection reset — still closed, consistent with every recent day.
- `wkuherald.com`'s WP-JSON (`/wp-json/wp/v2/posts` and `/wp-json/wp/v2/media`): open, fast,
  unthrottled.

## New ground actually covered this pass

Rather than re-walk the exhaustively searched pre-2003 officer list again, checked the live
`organization.executive`/`organization.senate.officers` layer in `data/years.json` for 2025-26
and 2026-27 against `data/photos.json` by hand (name+year pairs, not just file count), since this
is the one part of the gap that grows every week rather than being fixed. All of 2026-27's
executive and Speaker already carry portraits. Four 2025-26 senators remain unphotographed:
**Miles Harvey, Zoe Martin, Tyreesha Morris, Nolan Rongey**.

Searched `wkuherald.com`'s WP-JSON for each by name:
- Miles Harvey: 6 posts (Bike4Alz coverage, the April 2025 and April 2026 election-result
  stories, one 2018 article about an unrelated Miles Harvey). No captioned photograph of him.
- Zoe Martin: 1 post, the 16 April 2025 election-results story. Named in a list of newly elected
  senators in the body text; the story's only photograph (693a9960) is captioned to Ciin Lun
  alone.
- Tyreesha Morris: 4 posts, including the 25 August 2026 "kicks off 60th year... swears in new
  committee chairs" story and the SNAP-cuts story (88370). Read the figure captions in every one;
  none names her. 96580's single photograph is captioned to Caden Lucas only; 88370's four
  photographs are captioned to Amelia Tucker, a committee group, and Rush Robinson.
- Nolan Rongey: 1 post, the same 16 April 2025 election-results story as Zoe Martin, same result.

Also opened the full 12-photo gallery at `wkuherald.com/92840` (the 15 April 2026 election-night
photo essay already mined for Jakob Barker and Will Derryberry's portraits) and read every
caption by hand: Jaden Marshall, Caden Lucas, Veronica Butler, Susan and Jeffery Lucas (family),
Jakob Barker, Will Derryberry, Rush Robinson and Dr. Charley Pride are named; none of the four
target senators appear.

Checked `.research/` and `data/photo-finds/` before writing this up: all four names already
recur across roughly a dozen prior run reports and `_officers-truly-missing-2026-09-06.json`, so
this pass's result — no accessible photograph — agrees with, rather than discovers, the standing
finding. Recorded here mainly so the "freshest" open slots in the gap (this year's own senators,
as opposed to the 1966-2002 backlog) are confirmed re-checked against today's live WP-JSON feed
rather than assumed stale.

## Conclusion

No new portrait, no change to `data/photos.json` or `data/photos/`. The standing gap is unchanged:
every president and student regent photographed, 155 officers with no portrait in any year, all
exhaustively searched and documented as closed or structurally unreachable. Landed on
`research-photos`.
