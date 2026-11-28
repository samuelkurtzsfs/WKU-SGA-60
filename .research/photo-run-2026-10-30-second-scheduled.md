# Photograph run, 30 October (second scheduled pass): baseline reconfirmed, both
standing network blocks retested unchanged, a WebSearch pass against 15 further
officer-gap names comes back negative

## Priorities 1, 2 and 4, checked directly against the files

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four
  still carry a `leaders` entry in `data/photos.json`, matched against
  `data/years.json` by name and year, not assumed from an earlier log. Each file
  was also re-checked for its magic bytes this pass (`ffd8ffe0`, a real JPEG, for
  all four: `2004-05-nick-todd.jpg`, `2005-06-katie-dawson.jpg`,
  `2007-08-jeanne-johnson-sga.jpg`, `2008-09-reagan-gilley.jpg`). This trigger's
  stored brief still names them as portraitless; it has not been true since the
  20 August run.
- **Priority 2**: every `leaders` record in `data/years.json` whose `role` is
  `president` or `regent`, or whose `also_regent` is true, has a matching
  `(year, name)` pair in `data/photos.json`'s `leaders` array — 0 gaps, checked
  by script.
- **Priority 4**: all 61 years in `data/years.json` carry at least one entry in
  `data/photos.json`'s `years` array. No gap.
- **Priority 3** (officer/Senate gap): `python3 scripts/portrait_gap.py --any-year`
  reports 948 officer slots, 188 without a portrait for that person in that year,
  held by 158 people, 156 of whom have no portrait anywhere in the file — the
  same figures as every pass since 28 October.

## Network state, retested fresh

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`, with the navigation headers
  CLAUDE.md specifies: `HTTP 403`, unchanged since 25 August.
- `digitalcommons.wku.edu/sga/` (ordinary index page): `HTTP 200`, open as before.
- `web.archive.org`: `curl: (35) Recv failure: Connection reset by peer`, unchanged.

Neither block has moved. Nothing attempted this pass depended on either route.

## New this pass: WebSearch against 15 more officer-gap names

The 30 October first pass opened WebSearch as a new method against 8 names and
closed all 8 negative. This pass ran it against 15 more, chosen from the
executive-officer slice of the 158-person gap (`portrait_gap.py --any-year
--list`) for having distinctive enough spellings to avoid the surname trap,
queries restricted to `wku.edu`, `wkuherald.com`, `digitalcommons.wku.edu` and
`bgdailynews.com`:

Matthew Pava (2003-04), Jeremy Glass (2007-08), Samantha Hughey (2007-08),
Monique Gooch (2008-09), Aaron Pawley (2009-10), Sarah Howell (2009-10),
Jessi Wurth (2010-11), Brittany Crowley (2012-13), Sawyer Coffey (2014-15/15-16),
Rachel Keightley (2015-16), Abhishek Bose (2016-17), Smita Peter (2017-18),
Tribhuwan Singh (2021-22), Amelia Bice (2004-05), Liz Goddard (2007-08).

Several queries confirmed the office and term already on record in
`data/years.json` from SGA Senate minutes or legislation text — Samantha Hughey
(Director of IT, Senate minutes 2 Oct 2007), Aaron Pawley (Director of Academic
and Student Affairs, minutes 20 Oct 2009), Abhishek Bose and Smita Peter
(Director of IT, 2016-17 and 2017-18 executive cabinet pages), Tribhuwan Singh
(Director of Enrollment and Student Experience, *Herald* report of his election,
Sep 2021) — but none of those sources carries a photograph of the person, only
a name on a roster, a minutes line, or running text. Liz Goddard surfaced a real
photograph lead — a 2008 Daily News piece on the SGA awards banquet naming her
as the Mary Angela Norcia Award recipient — but the article text alone does not
establish it ran with her picture, and nothing in the search result shows one;
it is not pursued further without opening the actual page. Matthew Pava,
Monique Gooch, Sarah Howell (the WKU IT-staff Sarah Howell is a namesake, not
the 2009-10 SGA officer — the ITS staff page is nine years too recent and names
a different title), Jessi Wurth, Brittany Crowley, Sawyer Coffey, Rachel
Keightley, and Amelia Bice came back with no SGA-linked result at all, or only
unrelated namesakes (a Bowling Green property deed, a birth announcement, an
ITS staff listing).

Zero of the 15 produced a captioned photograph. This closes off 15 more names
from this method; 150 - 15 = 135 of the 158-person gap have now had either an
archive sweep, a wkuherald WP-JSON search, or a WebSearch pass, or some
combination, all negative. It is not proposed as proof the remaining people
have no photograph on record anywhere, only that the open, reachable sources
this method checks do not surface one.

## Conclusion

No new portrait landed this pass. Both standing network blocks are unchanged.
`python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean;
the only `site/` diff was the build-date line, reverted before committing.
`data/photos.json` and `data/photos/` are unchanged from `origin/research-photos`.
No push notification: nothing actionable surfaced for the owner beyond what has
already been reported on every pass since late August — the digitalcommons PDF
endpoint and web.archive.org remain blocked from this container, and the
officer-portrait gap stands at 156 people with no portrait anywhere in the file.
