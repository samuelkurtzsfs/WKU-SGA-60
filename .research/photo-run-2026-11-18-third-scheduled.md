# Photograph run, 18 November (third scheduled pass): baseline reconfirmed, live Herald feed checked fresh

## Baseline reconfirmed

- Priority 1 (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`, with JPEG magic bytes confirmed on all four
  files.
- Every president and every student regent in `data/years.json` has a `data/photos.json`
  `leaders` entry (checked against the whole file).
- All 61 years carry at least one `years`-level photograph entry.
- `scripts/portrait_gap.py --any-year`: 948 officer slots in the file, 885 cabinet/Senate
  leadership, same standing gap as the two earlier passes today.
- 2026-27's current executive (Caden Lucas, Jakob Barker, Will Derryberry, Gabi Pace, Cayden
  Bailey) and Speaker Veronica Butler all already carry portraits, including the 16 November
  Herald coverage of the SGA 60th-anniversary alumni homecoming breakfast landed earlier this
  branch.

## What this pass checked that the other two today did not

The two earlier passes today worked the historical gap (1970s-80s Talisman leads, the
long-standing any-year list). This pass instead checked the one source that changes daily and
so can never be fully exhausted: wkuherald.com's live feed, via its WordPress API
(`/wp-json/wp/v2/posts?search=SGA&per_page=10&orderby=date&order=desc`).

The newest item not yet in this branch's history is "SGA prepares for the holidays with new
bills" (wkuherald.com/99560, published 17 November 2026, 11:29pm — after today's first two
passes were filed). Read the full post body. It carries one photograph, captioned:

> "Dr Leslie Noth, WKU director of the Office of Sustainability, thanking all the student
> volunteers from the WKU Food Pantry as they recieve a $2,000 grant during the SGA meeting at
> Downing Student Union on Nov. 17, 2026."

The subject is a university administrator, not an SGA officer — not usable under this
project's rule. The article quotes Parliamentarian and Senior Senator Amelia Tucker and Chief
Financial Officer Will Derryberry by name, neither pictured. Derryberry already carries a
portrait; Tucker is not currently in the any-year gap list at all (she has no `organization`
entry carrying "no portrait" status checked this pass — her office this year, Parliamentarian,
is a committee-adjacent role the gap script does track as leadership, and she was not flagged,
so she already has a photo on file or was never without one).

No other posts in the ten most recent carried an uncaptured officer photograph.

## Conclusion

No new portrait, no change to `data/photos.json` or `data/photos/`. `python3 scripts/build.py`
and `python3 scripts/check_data.py` both pass clean against the unchanged data; the `site/`
rebuild (date-stamp only) was discarded rather than committed. The historical any-year gap
remains the thoroughly worked seam described in today's two earlier reports. The live Herald
feed is now current through 17 November with nothing usable in it. Landed on `research-photos`
with only this note.
