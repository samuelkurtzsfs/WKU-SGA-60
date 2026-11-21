# Photograph run, 17 November (third scheduled pass): network gates retested with corrected params, no new portrait

## Baseline reconfirmed

- Priority 1 (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- `python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean: 61 years, 1964
  events, 60 presidents, every president and student regent portrayed. No `data/` changes this
  pass, so the `site/` rebuild (date-stamp only) was discarded rather than committed.
- `python3 scripts/portrait_gap.py --any-year` still reports the same standing gap as the two
  earlier passes today (187 officer-slots without a same-year portrait, 155 people with no
  portrait in any year).

## Network gates, retested fresh

- `cgi/viewcontent.cgi`: a first attempt with `context=talisman` returned 400 (wrong param, not a
  block); retried with the correct `context=dlsc_ua_records` against article 1418 (the 1994
  Talisman, `dlsc_ua_records/418`) and got **200, a real PDF** (`%PDF-1.7`) — open this pass,
  consistent with every recent day. Worth noting for the next run: a bare 400 here is not evidence
  the bypass closed, check the `context` value before concluding anything.
- `web.archive.org`: connection reset on the one attempt — still closed, consistent with every
  recent day.
- `wkuherald.com`'s WP-JSON: the first call (`/wp-json/wp/v2/posts?search=SGA&per_page=5&orderby=date&order=desc`)
  answered 200 with the newest post id 99339; every call after that in the same session, including
  a plain per-ID fetch of 99339 itself after a 15-second pause, came back 403. Read as the feed's
  own short burst limit rather than a sustained block — it answered once, then shut — so post
  99339's content was not read this pass. Flagging the id for whichever run gets a clean window
  next, rather than guessing at its content.

## Why no new search was attempted

Checked `.research/photo-run-2026-11-17-scheduled.md` and `-second-scheduled.md` (this morning's
two passes) before doing anything else: between them they already re-checked the freshest open
slots (the four unphotographed 2025-26 senators, against today's live WP-JSON feed) and
reconfirmed the two structural archive gaps (Talisman 1995-2002 and 2004-2011, never digitized).
The only genuinely open thread on file is the unread post 99339 above, which the feed closed
before this pass could reach it, and the standing judicial-council lead from 14 November
(`wku.edu/sga/2018-2019-judicial/judicial-council.php`, headshots for Sophie Stirling and a second
member), which stays blocked on the organization layer recording those people in `data/years.json`
first — not something this (photo-only) run can act on, since `data/photos.json` can only attach a
portrait to a name that already appears in the record.

## Conclusion

No new portrait, no change to `data/photos.json` or `data/photos/`. Landed on `research-photos`
with only this note; the open thread for the next pass is reading wkuherald post 99339 once the
feed allows more than one request per window.
