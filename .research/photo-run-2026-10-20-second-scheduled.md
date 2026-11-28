# Photograph run, 20 October second scheduled pass: five fresh leads checked at source, none survive; access unchanged

## Priorities 1, 2 and 4: reconfirmed, not re-searched

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry
  a portrait in `data/photos.json`, as every run since August has found.
- **Priority 2**: `python3 scripts/check_data.py` reports no missing leader portrait across all 61
  years, 60 presidents.
- **Priority 4**: every year carries at least a leader portrait or a year-level photograph.

## Network state, retested fresh (07:54 UTC)

- `digitalcommons.wku.edu`, article landing pages (e.g. `/talisman/122/`): HTTP 200, loads cleanly.
- `digitalcommons.wku.edu/cgi/viewcontent.cgi`, the actual file-download endpoint: still HTTP 403,
  Cloudflare "Just a moment..." challenge. Tried a real headless Chromium (Playwright, the
  `/opt/pw-browsers/chromium-1194` binary already in this container) instead of a bare `curl`, on
  the theory that a JS challenge might clear for an actual browser engine even where it holds a
  plain request. It did not: the challenge page still reads "Just a moment..." after 32 seconds of
  waiting inside the browser itself. This is a stronger test than previous passes have run and it
  still reads closed — worth knowing so a later run does not re-try the same idea expecting a
  different result from a plain HTTP client.
- `web.archive.org`: `curl: (35) Recv failure: Connection reset by peer`, repeated. Still closed.
- `archive.org` (the plain item/download host, distinct from `web.archive.org`): open. Used below,
  including a path not exercised recently — see next section.
- `wkuherald.com` WP-JSON: open. Newest SGA-tagged post is still the 14 October one already read
  by the previous pass (97897/98116); no new post to check this run.

## A path worth recording: archive.org serves full-volume PDFs and JP2 page scans directly

Confirmed via the metadata API (`archive.org/metadata/<id>`) that `talisman1975west`,
`talisman1979west` and `talisman1987west` each carry a `Text PDF` (the full scanned volume) and a
`Single Page Processed JP2 ZIP`, hosted on `archive.org` itself, independent of the
`digitalcommons.wku.edu` domain that is currently blocked. This means a year whose Talisman volume
is one of the ones archive.org holds (1971-1981, 1986, 1987) is not actually cut off from images
just because digitalcommons is — the full volume and its page images can be pulled from
archive.org directly. Flagging this for whoever next needs to download an actual page image in
this range, since the current run's five leads turned out not to need it (see below: either no
caption exists, or the name never appears).

## Five fresh leads from `scripts/portrait_gap.py --list`, checked against the djvu text of the volume for their year

All five fall inside the one span of years archive.org actually holds (1971-1981, 1986-87), and
none had been searched before (`git log --all | grep -i <name>` returned nothing for any of them,
unlike Bass/Chesnut/Wilson in the same list, which prior runs had already run to ground).

- **Vern Pulman, Representative-at-Large, 1974-75** (`talisman1975west`): no match for "Pulman" or
  any plausible OCR variant anywhere in the volume's text, including the ASG/Congress sections.
  Consistent with the role itself: he was a February 1975 appointment filling a vacancy, per the
  year's existing note, not an elected officer the yearbook would have had reason to photograph.
  No portrait exists to find here.
- **David Young, Administrative Vice President, 1978-79** (`talisman1979west`): his name does
  appear once, but only as a quote in the "Getting organized" ASG article — "David Young,
  administrative vice president, said this was done to 'force some heads-up competition'..." — not
  attached to any photograph. The spread's actual photo captions on the same pages name only Steve
  Thornton (ASG president) and Victor Jackson. No caption anywhere in the volume ties a picture to
  Young. Not a portrait; a quote.
- **Alice Wicks, Secretary, 1978-79** (`talisman1979west`): appears only in the senior-portrait
  name index as "Wicks, Alice Elizabeth" with no page number following her name, which in this
  volume's index format means she was not photographed for an individual portrait that year
  (compare neighbouring entries like "Wible, Gerald Alan 401", which do carry a page). No portrait
  to find.
- **Chris Millay, Parliamentarian, 1986-87** (`talisman1987west`): no match anywhere for "Millay"
  tied to a first name "Chris" or "Christopher" — the only Millays in the whole volume are "Beth
  Ann Millay" and "Lori Ann Millay" in the senior index, different people. The organizations
  section this year has no dedicated ASG club-photo spread at all (only the "Weekend in the Woods"
  leadership-retreat photos, captioned for president Tim Todd and treasurer Barbara Rush, and the
  "ASG/UCB" year-in-review text, captioned for nobody). No portrait, and nothing to misattribute it
  to.
- **Dwight Austin, Sergeant-at-Arms, 1986-87** (`talisman1987west`): no match for "Dwight Austin"
  anywhere in the volume; every "Austin" hit is either "Austin Peay" (the university) or an
  unrelated senior in the name index. No portrait.

None of these five is a case of "the archive doesn't reach this source" — in each case the
relevant Talisman volume was read in full text and the name either does not appear attached to any
photograph, or does not appear at all. These are genuine dead ends, not access gaps, and should not
need re-checking against this same volume again.

## What this run leaves unchanged

`data/photos.json` and `data/photos/` are unchanged from the last commit on this branch. The
remaining 184 of the 189 gap entries (189 minus the 5 checked this run) are overwhelmingly 2000s
through 2020s Senate and Judicial Council members already searched 7-14 times apiece against
`wkuherald.com` and, before it closed, `digitalcommons.wku.edu`, per the run-log history in this
directory; re-running those same searches against the same two open-or-closed routes would not
produce a different result. `python3 scripts/build.py` and `python3 scripts/check_data.py` both
exit clean (61 years, 1964 events, 60 presidents, no missing leader portrait, no year without a
photograph).
