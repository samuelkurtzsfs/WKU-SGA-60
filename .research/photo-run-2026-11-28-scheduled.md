# Photograph run, 28 November (scheduled): fresh name batch checked, no new portrait

## Baseline, reconfirmed programmatically before anything else

- The four presidents named as having no portrait at all (Nick Todd, Katie Dawson, Jeanne
  Johnson, Reagan Gilley) already carry a captioned `leaders` entry in `data/photos.json`,
  confirmed again this pass.
- Every president and student regent in `data/years.json` has a portrait.
- All 61 years carry at least one photograph.
- `scripts/portrait_gap.py` reports 187 cabinet/Senate-officer slots without a portrait, held
  by 157 people, 155 of whom have no portrait in any year — unchanged from every pass since
  22 November.

## What this pass tried that is genuinely new

Rather than re-walk names already closed out in `data/photo-finds/_do-not-use.json`, cross-
checked the current officer-gap list against that file and pulled eight names from the 2021-24
Senate that have never been searched there: Danny Vuleta, Neel Patel, Mallory Hardesty, Reed
Hensley, Connor Ferguson, Elizabeth Gannon, David Darnell, Callison Padgett.

Searched each against `wkuherald.com`'s own WP-JSON post search, then pulled the attached-media
list (`/wp-json/wp/v2/media?parent=<post id>`) for every post a name's search surfaced, to check
captions directly rather than post text:

- Danny Vuleta: zero post hits.
- Neel Patel, Elizabeth Gannon, David Darnell, Callison Padgett: several post hits each (election
  announcements, weekly-meeting roundups), none with his or her own name under a photograph.
  `wkuherald.com/72365` (Judicial Council/committee heads) carries one photo, an unlabelled room
  shot of the whole Senate meeting — no individual captioned.
- Mallory Hardesty, Reed Hensley: both named only in text (a trivia-night funding bill, a Narcan
  bill) in posts whose attached photograph captions name different people entirely — Peyton Hess
  on the trivia bill (`wkuherald.com/70844`), nobody on the Narcan piece (no media attached).
- The election-results post naming both Hardesty and Hensley's ticket-mates
  (`wkuherald.com/65821`, "Cole Bornefeld wins presidency") carries nine captioned photographs,
  but all of Bornefeld, Sam Kurtz, Garrison Reed, Alexis Courtenay and Holden Schroeder — all
  already on file — not of Hardesty or Hensley.

All eight names are the same trap CLAUDE.md names directly: appearing in running SGA-business
text is not appearing under a photograph. None is added to `_do-not-use.json` as a closed lead,
since none produced a face to rule in or out — there is simply no photograph of any of the eight
in the record searched. The gap list is otherwise unchanged from 27 November's exhaustive pass.

## Network gates, retested cold

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`: still 403 with full navigation headers.
- `web.archive.org`: still resets the connection at the egress proxy before any response.
- `wkuherald.com` WordPress API (posts and media): open, used above.

## Unchanged

`data/photos.json` and `data/photos/` are unchanged this pass; only this note was added. Build
and `check_data.py` both run clean. The editor queue is unchanged: `data/photo-finds/
_for-the-editor.md` still carries 13 people and 14 photograph entries, open since 8 September
2026, each needing a yes/no identification call no further research can make.
