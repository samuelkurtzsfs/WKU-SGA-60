# Photograph run, 15 October (second scheduled pass): one identified portrait found, correctly left unattached

## Priorities 1, 2 and 4: reconfirmed, unchanged

Checked against `data/photos.json` and `data/years.json` before anything else, per CLAUDE.md's
"check whether an earlier run already got them."

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait.
- **Priority 2** (every other president or student regent): zero leader records in any of the 61
  years without a photo.
- **Priority 4** (years with no photograph at all): zero years missing from `photos.json`'s `years`
  array.

`python3 scripts/portrait_gap.py`: 189 officer slots / 159 people / 157 with no portrait in any
year — unchanged from every pass since 13 October.

## Network state this session

Both routes every report since 13 October has logged as closed were retested directly, including
one retry after a 90-second backoff on the first 403:

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`: 403 on both attempts, ~90 seconds apart. Item
  (landing) pages on the same host answer normally (200/301) — only the PDF route itself is gated.
- `web.archive.org`: connection reset outright on both attempts (`Recv failure: Connection reset
  by peer`). Closed for this session, same as every pass since 13 October.
- `archive.org` (not `web.archive.org`) and `wkuherald.com`: both open and used this pass.

## A new, correctly identified portrait — found, and correctly left unattached

Searching `wkuherald.com`'s WP-JSON API for several 2022-2025 officer-gap names (Justin Goins,
Erika Puhakka, Nathan Cherry, Danny Vuleta, Reed Hensley, Brooke Mitchell, Kayla Distler) turned
up one new, cleanly identified photograph, in the course of checking an article about a different
gap name (Justin Goins, Chief Justice 2022-23/2023-24):

**"SGA Judicial Council elects new chief justice"**
(`https://wkuherald.com/88753/news/sga-judicial-council-elects-new-chief-justice/`, published 13
November 2025, photographs by Jonah Savage) carries four individually captioned photographs from
the Judicial Council meeting of 12 November 2025, the day before. One of its captions reads:
"Associate Justice Xavier Spiess gives a speech on why he should be elected as the next Chief
Justice of the judicial council on Wednesday, Nov. 12, 2025 in the SGA Office." The photograph
(`wkuherald.com/wp-content/uploads/2025/11/SAV2655-1200x924.jpg`) is a clean, single-subject,
chest-up shot of one young man in a WKU SGA polo, named nowhere else in the frame — downloaded,
verified as a real JPEG (`FF D8` magic bytes, 1200x924), and visually a usable portrait.

Xavier Spiess is a real, sourced figure in this archive already: `data/years.json`'s 2025-26
events and profile text name him in four passages as the losing candidate in the 3-1 Judicial
Council vote that made Sophie Stirling chief justice (whose own portrait, from a different Herald photo,
is already in `photos.json`). But he does not appear in `organization.senate.officers` for
2025-26, or in any other year — the 2025-26 organization record lists only Kaden Blankenship as
Associate Justice. Adding the portrait to `photos.json` therefore fails `check_photos()` in
`scripts/check_data.py` ("photos.json names 'Xavier Spiess', who is not in the archive") and
breaks the build, exactly the Steve Wilson situation recorded on 14 October: the photograph
exists and the identification is solid, but there is nothing in the organization roster for the
overlay to attach to, and this agent's rules confine it to `data/photos.json` only — it cannot
add the missing `organization.senate.officers` entry in `years.json` itself.

Tested this directly: added the entry, ran `python3 scripts/build.py`, got exactly that one
failure, reverted both the `photos.json` entry and the downloaded file. `data/` carries no diff
from this pass.

**What the next run that touches `organization.senate.officers` for 2025-26 should do:** add an
Associate Justice (or equivalent) entry for Xavier Spiess, sourced to the events already in
`years.json` or to the Herald article above, then this portrait can be attached in the same move:

```json
{"year": "2025-26", "name": "Xavier Spiess", "file": "2025-26-xavier-spiess.jpg",
 "src": {"label": "College Heights Herald, published 13 November 2025, photographed by Jonah Savage; the caption names Associate Justice Xavier Spiess giving a speech on why he should be elected the next chief justice of the judicial council, in the SGA Office on 12 November 2025, the date of the photograph.",
         "url": "https://wkuherald.com/88753/news/sga-judicial-council-elects-new-chief-justice/"}}
```

## Other names checked, nothing usable

- **Justin Goins** (Chief Justice, 2022-23/2023-24): three wkuherald hits, none carrying a
  photograph of him specifically — one (election-results story) has only a group cabinet shot
  with no individual captions, the other two are text-only floor-business reports.
- **Erika Puhakka** (Chief Justice, 2020-21/Associate Justice, 2018-19): five hits, all text-only
  committee/legislation reports.
- **Nathan Cherry** (Speaker of the Senate, 2016-17): ten hits spanning his whole term, all
  text-only; no photograph found naming him.
- **Danny Vuleta**: the search request itself came back 403 from wkuherald's WP-JSON endpoint
  (the only 403 wkuherald gave this session, on otherwise-successful back-to-back requests) —
  not re-tried, to stay within the "others may be crawling, back off properly" guidance; open for
  a future pass.
- **Reed Hensley**: two hits, one a named-and-sourced photo gallery
  (`wkuherald.com/65821/.../gallery-sga-results-announced-cole-bornefeld-wins-presidency/`) whose
  individual images carry no caption text in the static page at all — the gallery widget appears
  to load its captions by script, which this pass has no means to render. Flagging the method gap
  rather than guessing at who is in which frame.
- **Brooke Mitchell**: both hits are a different Brooke Mitchell entirely (women's softball).
- **Kayla Distler**: seven hits, all text-only SGA floor-business and one unrelated (pink tax
  legislation, different committee).

## What is still open

The 189-slot gap moves by one correctly-withheld lead rather than by a new portrait: Xavier
Spiess waits on an `organization` entry, not on a photograph. Everyone else checked this pass
stays open for the same reason as every pass since 13 October — the routes that would likely
carry their photographs (`cgi/viewcontent.cgi` for pre-2011 names, `web.archive.org` for the old
SGA website's officer pages, and for some of the 2010s-2020s names, whatever renders wkuherald's
gallery captions) were closed or out of this pass's reach for their whole session.

## Checks

`python3 scripts/build.py` then `python3 scripts/check_data.py`: 61 years, clean, 60 presidents,
no missing leader portrait, no year without a photograph. No file in `data/photos/` or entry in
`data/photos.json` changed this pass.
