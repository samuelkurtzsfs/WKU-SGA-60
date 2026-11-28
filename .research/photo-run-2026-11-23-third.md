# Photograph run, 23 November (third pass)

## Baseline reconfirmed

Unchanged from this morning's two passes: all four priority-1 presidents (Nick Todd, Katie
Dawson, Jeanne Johnson, Reagan Gilley) carry a portrait; every president and student regent in
the record has one; all 61 years carry at least one `years`-level photograph. `check_data.py`
exits clean (948 officer slots, 1,111 legislation files, 61 years, 1,964 events, 60 presidents).
`scripts/portrait_gap.py --any-year` reports the same figures as every pass today and for three
weeks: 187 same-year officer/Senate-leadership gaps, 157 people, 155 of them with no portrait in
any year.

## What this pass checked

Independently, without reading the earlier passes' leads first, worked a sample of the standing
gap list through wkuherald.com's WordPress search API (free, no pacing limit) looking for a
captioned photo: Jessi Wurth, Monique Gooch, Brittany Crowley, Aaron Pawley, Rachel Keightley,
Liz Goddard, Smita Peter, Abhishek Bose, Tribhuwan Singh. Every post that mentioned one of these
by name and carried a featured image or gallery photo was opened and read for its actual caption
text (not just the alt text). None of the captions found named the officer being searched for:

- Rachel Keightley (2015-16 Director of IT): the 2 Sept 2015 "SGA welcomes new and old members"
  post has two photos; the first is captioned for then-president Jay Todd Richey, the second
  carries no caption text at all.
- Brittany Crowley (2012-13 Director of Academic and Student Affairs): ten posts mention her by
  name; only one (an unrelated yoga feature) carries a featured image, and it is not about SGA.
- Smita Peter (2017-18 Director of IT): six posts, three with featured images or galleries; the
  25 April 2018 "SGA executives share final words to Senate" photo has alt text only, no caption,
  and does not name her; the two bill-coverage photos from March 2018 are captioned for the
  meeting generally and do not name her either.
- Jessi Wurth, Monique Gooch, Aaron Pawley, Liz Goddard, Abhishek Bose, Tribhuwan Singh: no
  captioned photo turned up at all (several have no matching post, or the matching posts carry
  no image).

Also re-tried two names already recorded as closed in `data/photo-finds/_do-not-use.json` (David
Young, 1978-79 Administrative Vice President; Mark Chesnut, 1980-81 Treasurer) against the
archive.org plain-text Talisman transcripts for 1979 and 1981, to see independently whether the
closure still holds. It does: both names appear in running text (a campaign-endorsement letter
for Young; an index-only hit for Chesnut), but neither is attached to a photograph caption in
either volume. This reproduces the existing `_do-not-use.json` entries rather than adding
anything.

Tried the digitalcommons.wku.edu PDF for the 12 April 1979 *Herald* (the Young campaign-coverage
issue) once, with the required navigation headers and a 90-second wait after the first refusal.
Both attempts returned HTTP 403. Consistent with this route being intermittently closed; nothing
to act on, since the lead was already closed on paper anyway.

## No change to the record

`data/photos.json` and `data/photos/` are unchanged. Nothing to commit there. This note is the
only new file from this pass.

## Standing items, unchanged

Same two things every recent pass has flagged, repeated here only because they are still true
and still need a person:

1. `data/photo-finds/_for-the-editor.md` — 13 people, 14 photograph entries, open since
   8 September 2026 with no decision recorded. Each is a specific face already matched to a
   specific archive frame; the only open question is a yes/no identification call CLAUDE.md
   reserves for a person. No further automated research moves any of them.
2. The "SGA 60 - backlog"-style photograph trigger has fired several times a day for about three
   weeks against this same 155-person gap, now exhaustively searched through every open route.
   `update_trigger` was refused in an earlier run as "created via http_api, not by an agent" —
   only the account holder can change the schedule or stored prompt.
