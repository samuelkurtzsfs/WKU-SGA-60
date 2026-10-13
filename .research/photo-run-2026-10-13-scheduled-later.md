# Photograph run, 13 October (later scheduled pass): priorities 1, 2 and 4 reconfirmed at zero; wkuherald.com open and worked through 33 names in the officer gap, none usable

## Priorities 1, 2 and 4: reconfirmed against the current file

**Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): checked against
`data/photos.json` before anything else. All four still carry a portrait.

**Priority 2** (any other president or student regent without a portrait): zero missing,
reconfirmed.

**Priority 4** (years with no photograph at all): still only **1994-95**, blocked by the
same closed route as every pass since late September (see below).

## Access this session

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — HTTP 403 against article 8989 (the standing
  1994-95 lead), with the full navigation-header set. Still closed.
- `web.archive.org` — connection reset at the TLS layer (`ws_closed_mid_exchange`ish, a plain
  `Recv failure: Connection reset by peer`). Still closed.
- `archive.org` (plain, Talisman djvu route) — open: 302/200 on 1979, confirmed 503 on 1982 and
  1996, which is the volume range CLAUDE.md already records archive.org as not holding, not a
  new access problem.
- `wkuherald.com` — **open** both on the WP-JSON search API and on individual post/media fetches,
  with occasional single 403s that cleared on a short retry, matching every recent note's
  description of this host's intermittency. This was the one open route worth spending the
  session on.

## Priority 3: 33 names searched on wkuherald.com, none produced a usable portrait

Picked up where the 13 October scheduled note left off — the standing list of untried
post-2011 officer-gap names, plus a check of several 2011-2021 names that a `grep` across all
66 `.research/photo-run-*.md` files showed had never actually been searched (the standing
gap list is long enough that earlier passes had not worked all the way through it).

**Checked, no usable portrait (name not next to a photograph with a caption identifying them):**
Matthew Johnson, Hope Wells, Alexis Mayne, Tribhuwan Singh, Garrett Baum, Danny Vuleta (also
tried as "Daniel Vuleta," the SGA election story's own spelling), Neel Patel, ShyAnte'e
Williams, Mallory Hardesty, Reed Hensley, Brooke Mitchell, Elizabeth Gannon, David Darnell,
Livi Ray, Callison Padgett, Tyreesha Morris, Erika Puhakka, Josh Zaczek, Cassidy Townsend,
Brenna Mathews, Turner Reynolds, Justin Goins, Nicole Massarone, Zachary Skillman, Elizabeth
DeLozier, Connor Ferguson, Jillian Kenney, Temple Ricke, Chase Coffey, Lucas Knight (the last
three genuinely new to this file's search history, per the grep check above).

Two near-misses, checked in detail and ruled out:

- **Kayla Distler** — article 65656 ("McLean Hall students demand compensation for dorm
  conditions") has a featured image whose caption names her directly: "A petition regarding
  conditions in McLean Hall was started by WKU sophmore Kayla Distler." But the file itself
  (`Screen-Shot-2022-04-13-at-2.10.08-PM.png`) is a screenshot of the petition page, not a
  photograph of her — the filename alone says so, and the CDN refused the download anyway
  (HTTP 403, retried once). Not a portrait candidate even if the download had worked.
- **Carter Smith** — found via a search before checking `photos.json` first: article 97612's
  featured image (97546) is captioned "WKU Student Government Association Sophomore Senator
  Carter Smith gets sworn in..." This is already in the archive, added by an earlier run
  today: `data/photos.json` carries it for 2026-27, file `2026-27-carter-smith.jpg` verified
  present and a real JPEG (FF D8 FF E0). Confirms the file is current; nothing to add.
- **John (Jack) McKinney** — zero hits on an exact-name search.

One gallery fully worked through for completeness: article 65821 ("SGA election results
announced, Cole Bornefeld wins presidency") links an 8-photo gallery (media 65823-65830).
Fetched each media record's own caption rather than relying on the one embedded in the post.
All eight resolve, though not on one pass: 65826 and 65828 each returned a single 403 on
their own media endpoint and answered on a short retry, so a 403 here means try again rather
than that the record is closed. None of the eight names Mallory Hardesty, Reed Hensley or
Daniel/Danny Vuleta, all three of whom the same article's body text lists among the new
senators. The faces the captions do identify are Sam Kurtz, Cole Bornefeld, Alexis Courtenay,
Chief Justice Holden Schroeder, and — in 65828, 65829 and 65830 — Garrison Reed. Schroeder and
Reed both already carry a portrait in `data/photos.json` (Reed under 2022-23, reused for
2023-24), so the gallery adds no face the archive lacks.

Also checked figure-by-figure (not just the featured image) on three multi-photo articles that
the body-text search flagged as mentioning a gap name: 90387 (6 figures, Tyreesha Morris named
in body only), 96580 (1 figure, Caden Lucas only), 88370 (4 figures, Amelia Tucker and Rush
Robinson only, despite Tyreesha Morris being named in the same article as newly sworn in).

`portrait_gap.py` still reports 189 slots / 159 people / 157 with no portrait in any year,
unchanged — the Carter Smith slot it lists lacks the "(no portrait in any year)" tag precisely
because he already has one for a different year, which checked out.

## Nothing changed

`data/photos.json`, `data/photos/` and `data/years.json` are all untouched this run.
`python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean: 61 years, 1968
events, 60 presidents, "the archive checks out against its own rules." `site/` was reverted
(`git checkout -- site/`) since build output is not committed to this branch.

## For the next run

- `cgi/viewcontent.cgi` and `web.archive.org` remain the two closed routes; test them again
  before assuming either way, per this file's own standing advice.
- wkuherald.com's WP-JSON API (`/wp-json/wp/v2/posts?search=...&_embed=1` and
  `/wp-json/wp/v2/media/{id}`) is the one open route, and this pass worked through essentially
  the whole standing post-2011 gap list without a hit — the hit rate really is close to zero
  now, not just in this run's small sample. The names from 2011-2021 that a cross-check of
  all 66 prior `.research/photo-run-*.md` files showed as never searched are three, not four:
  Temple Ricke, Chase Coffey and Lucas Knight, now checked, with the same result. John "Jack"
  McKinney does **not** belong on that list — `photo-run-2026-10-02.md` had already searched
  him on this same host and recorded the outcome (one wkuherald.com hit and one general-web
  hit, both about a later Judicial Council cohort rather than the 2016-17 officer this record
  wants). The grep that produced the never-searched list missed him.
- A featured image's filename alone (`Screen-Shot-...png`) is a useful tell that it is not a
  face photograph even before spending a download attempt on it — Kayla Distler's case is the
  worked example.
- When a post links a photo gallery (`data-photo-ids` on a `.sfiphotowrap` div, several ids
  past the featured one), fetch each gallery image's own `/wp-json/wp/v2/media/{id}` record
  rather than trusting the post's single embedded caption — captions differ photo to photo, as
  65821's gallery of 8 shows.
- The remaining untried slots in the officer gap are now almost entirely the 2011-2020 names
  this pass worked through once and the pre-2011 names tied to the still-closed TopSCHOLAR and
  web.archive.org routes. There is very little low-hanging fruit left on the open route; the
  next real gain is more likely to come from one of the two closed routes opening than from
  further wkuherald.com name-by-name search.

## Corrected on editorial review, 13 October

Three claims in this note as first written did not survive a check against the repository and
against the cited pages. The corrections are in the text above; what they were is recorded here
so a later pass can see the reasoning rather than just the result.

- **The name count was 36 and is 33.** The list of names checked without a usable portrait holds
  30; the three near-misses set out separately (Kayla Distler, Carter Smith, John "Jack"
  McKinney) bring it to 33. "Daniel Vuleta" is the election story's spelling of Danny Vuleta and
  is one name, not two; Mallory Hardesty, Reed Hensley and Vuleta appear again in the gallery
  paragraph but were already counted in the 30.
- **John "Jack" McKinney had been searched before.** He was listed among four names a grep of the
  66 prior run notes was said to show as never searched. `photo-run-2026-10-02.md` searched him
  on wkuherald.com and wrote the result down. The other three on that list are genuinely new.
- **The 65821 gallery identifies a fifth person.** Garrison Reed is named in the captions of
  65828, 65829 and 65830; the note said the photographs covered only four people. No portrait
  was lost to the error — Reed already has one — but the sentence was wrong. Both images the note
  reported as refused answered on a retry, so all eight captions are readable.

Verified unchanged in the same pass: all four priority-1 portraits present; zero presidents or
student regents without a portrait for their own year; 1994-95 still the only year with no
scene photograph; `portrait_gap.py` at 189 slots / 159 people / 157 people with no portrait in
any year; the Kayla Distler and Carter Smith captions word for word against their media records;
`cgi/viewcontent.cgi` still 403 on article 8989 and `web.archive.org` still resetting, with
plain `archive.org` answering 200.
