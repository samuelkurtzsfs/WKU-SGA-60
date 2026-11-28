# Photograph run, 21 October scheduled: baseline reconfirmed, both routes retested fresh, ten more under-searched names run to ground with nothing new

## Priorities 1, 2 and 4, checked directly rather than assumed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry
  a portrait in `data/photos.json`, confirmed again by reading the file directly.
- **Priority 2**: `python3 scripts/check_data.py` reports no missing leader portrait. Independently
  cross-checked every `leaders` entry in `data/years.json` against `data/photos.json`: zero
  presidents and zero student regents without a portrait, 61 years, 60 people.
- **Priority 4**: every one of the 61 years in `data/years.json` carries at least a year-level
  photograph or a leader portrait, per the same cross-check prior passes have been running.

## Network state, retested fresh rather than carried over

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` (the file-download endpoint): HTTP 403, Cloudflare
  "Just a moment..." challenge, tested with the full navigation header set
  (`Sec-Fetch-Dest: document`, `Sec-Fetch-Mode: navigate`, `Upgrade-Insecure-Requests: 1`). Still
  closed, same as every pass since this blocker first appeared.
- `digitalcommons.wku.edu` ordinary item/landing pages: HTTP 200, loads cleanly (checked
  `/dlsc_ua_records/4686/`). Only the download endpoint is blocked.
- `web.archive.org`: `curl: (35) Recv failure: Connection reset by peer`. Still closed.
- `archive.org` (the plain item/download host, distinct from `web.archive.org`): open, confirmed
  against `talisman1975west`'s djvu text.
- `wkuherald.com` WP-JSON (`/wp-json/wp/v2/posts` and `/media`): open. Newest SGA-tagged post is
  still 14 October's "SGA funds new Preston Center area..."; nothing newer to check.

## Priority 3: ten names from the standing gap, picked for the fewest prior mentions

Ranked every name on `scripts/portrait_gap.py --list`'s 160-name gap by how many
`.research/photo-run-*.md` files already mention it, and picked from the bottom of that ranking,
all of them 2003 or later so `wkuherald.com`'s WP-JSON search actually reaches them (the pre-2003
names at the bottom of the ranking — Patricia Lanning 1966-67, Michelle Woods 2001-02/2002-03,
Andrea Lovell 2001-02 — fall before both open routes' coverage and were not re-tried, consistent
with every prior pass's finding that no route reaches that span right now):

Andy Vandiver (Associate Justice, 2006-07), Blake Napper (Co-Chair, Campus Improvements, 2004-05),
Cameron Yancey (Sergeant At Arms, 2003-04), Chris/Christopher Jankowski (Associate Justice
2010-11/2011-12, Chief Justice 2012-13), Hunter Sprowles (Chair, Public Relations, 2005-06),
John (Jack) McKinney (Associate Justice, 2016-17), Kasey Glasgow (Student Affairs Chair, 2014-15),
Stefanie Sharpensteen (Co-Chair, Public Relations, 2004-05), Corbin Snardon (Justice, Judicial
Council, 2009-10), ShyAnte'e Williams (Graduate Student Senator, 2022-23), and, picked up alongside
Jankowski from the same era, Madison Keller (Public Relations Committee Head, 2015-16) and Gretchen
Light (Judicial Council, 2003-04/2004-05).

- **Vandiver, Napper, Yancey, Sprowles, McKinney, Glasgow, Sharpensteen, Snardon, ShyAnte'e
  Williams, Madison Keller**: searched by full name and by bare surname against the WP-JSON API.
  Every hit returned is an unrelated person or story sharing the surname (a 2025 Black History
  Month piece, football postseason honors, a Diddle Arena funeral, a Valentine's Day feature, and
  so on — none naming an SGA officer, several from years decades away from the officer's actual
  term). No lead for any of the ten.
- **Chris Jankowski** was the one name this pass that is genuinely in the SGA record on
  `wkuherald.com`, not merely a surname collision: he is named in the body text of three 2011-12
  articles — the 29 March 2011 "SGA Notes" piece reporting his appointment as Associate Justice
  alongside Aaron Pawley (also ungoverned by a portrait) when Art Scisney moved up to Chief Justice
  on Dajana Crockett's resignation; the 15 November 2011 senator-review story, where he is quoted
  twice as the sitting Justice explaining the attendance rule; and the 8 February 2012 Frankfort
  rally story, which names him as one of four attendees. None of the three carries a usable image:
  the first two have no attached media at all (`featured_media: 0`), and the rally story's one
  captioned photograph (`wkuherald.com` media id 48760) identifies only Cory Dodds, not Jankowski —
  Dodds already has a portrait on file (`2012-13-cory-dodds.jpg`). A second, uncaptioned image on
  that same post (media id 48761) cannot be used under this project's rule against a photo whose
  subject cannot be confirmed from its caption. No portrait for Jankowski.
- **Mallory Treece**, also named in that rally story and likewise without a portrait, turned up in
  six further 2011-12 SGA articles while checking Jankowski's hits, all with `featured_media: 0`.
  No image anywhere ties to her.
- **Gretchen Light**: all five hits are unrelated people sharing the surname across a 23-year
  span (2002 birth-control feature, 2003 rally story, a 2014 fashion retrospective, two 2025-26
  campus stories); none from 2003-05, her actual years. No lead.

## What this run leaves unchanged

`data/photos.json` and `data/photos/` are unchanged from the last commit on this branch. 189
officer slots (157 people) remain without a portrait, per `scripts/portrait_gap.py` — the same
count the last several passes have recorded, since nothing found this run clears the bar this
project sets for attaching a face to a name. `python3 scripts/build.py` and
`python3 scripts/check_data.py` both exit clean (61 years, 1964 events, 60 presidents, no missing
leader portrait, no year without a photograph). Landed on `research-photos`.
