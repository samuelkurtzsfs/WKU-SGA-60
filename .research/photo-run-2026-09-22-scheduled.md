# Photograph run, 22 September (scheduled): baseline reconfirmed, archive.org's CDX API down again today

## Starting state

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md` and `SGA-60-AGENT-INFO.md` §4 and §6
before touching anything. `research-photos` had no local divergent work; fast-forwarded cleanly
onto `origin/main` (5 commits, all already-merged prior research, no conflicts).

Checked the standing priorities fresh rather than trust yesterday's reports as still current:

- **Priorities 1 and 2 (president and regent portraits): still fully satisfied.** All four
  originally-named presidents (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley) carry
  verified portraits with real JPEG magic bytes (`ffd8ffe0`), and a scripted cross-check of
  every `role: "president"` / `role: "regent"` leader entry in `data/years.json` against
  `data/photos.json` found zero gaps.
- **Priority 4 (year-photograph for every year): the same six gaps as every run since 20
  September** — 1994-95, 1995-96, 2000-01, 2005-06, 2006-07, 2008-09.
- **Priority 3 (cabinet/Senate officers): 208 named executive/Senate-officer slots still
  without a portrait**, or 226 counting committee chairs as well. The figure carried in earlier
  reports, 216, is not reachable from `data/years.json` by any counting basis tried here, and a
  previous editorial pass recorded the same failure (NIGHT-REPORT, "216 is not reachable by any
  method I tried"). Stating it as an exact match to the fourth-pass entry was wrong; the count
  moves as officers are added, so it should be re-derived each run rather than carried forward.

## Executive officers: independently re-derived the same eight declines

Before reading that section, this run separately searched `talisman1978west`, `talisman1979west`,
`talisman1981west` and `talisman1987west` (via `scripts/talisman.py`, the archive.org OCR-leaf
route) for the eight named officers who fall in an archive.org-covered year: Vern Pulman
(1974-75), David Bass (1977-78), David Young/Alice Wicks/Steve Wilson (1978-79), Mark Chesnut
(1980-81), Chris Millay/Dwight Austin (1986-87). Only then read SGA-60-AGENT-INFO.md's fourth-pass
write-up from the previous evening and found it reached the identical conclusion on all eight,
for the identical reasons: Bass is in a four-person group photo with no left-right order given in
the caption; Young, Pulman, Wicks, Millay and Austin have no accompanying photograph or no hit at
all; Wilson's only hit is an unrelated agriculture major with nothing tying him to student
government; Chesnut/Chestnut's only hit is an intramural results list, no photo. Nothing new to
add here — recorded as independent confirmation that the backlog against this route really is
exhausted, not re-litigated in full since SGA-60-AGENT-INFO.md already has the page-by-page
detail.

## The Wayback-PDF route: closed for today by a real Internet Archive outage, not a block

Tried a fresh, previously-untried lead for the 1995-96 year-photograph gap: `dlsc_ua_records/9035`,
"Associated Student Government Reaches Tenth Anniversary" (Herald, 12 Oct 1995), a retrospective
piece that seemed more likely than a routine headline to carry a historical photograph. The
landing page loads fine (article number 10017). Querying `web.archive.org`'s CDX API for a capture
of the underlying `viewcontent.cgi?article=10017` PDF failed repeatedly — not the Cloudflare
403 this project has logged against the live `digitalcommons.wku.edu` front door, but connection
resets, then confirmed directly: `https://web.archive.org/` itself returned an HTML page titled
**"Internet Archive: Temporarily Offline"** ("Internet Archive services are temporarily offline
... check our official accounts ... for the latest information"), HTTP 503, on two separate
attempts a few minutes apart, with a plain timeout on a third. This matches the fourth-pass
report's note from the previous evening that the CDX API was already reporting the same outage
then — so this is a real, ongoing service-side outage at Internet Archive, not a proxy or
container-specific block, and not something a different header or retry count fixes. The lead
on `dlsc_ua_records/9035` is untried, not closed negative; worth another attempt once Internet
Archive's own status accounts confirm service is back.

`archive.org`'s **download/iiif endpoints for the 19 already-covered Talisman years** (used above
for the officer search) were unaffected by this outage and worked normally throughout — confirming
SGA-60-AGENT-INFO.md's fourth-pass note that these are a separate, independently-hosted service
from `web.archive.org`'s CDX search, not one route with one uptime.

## Nothing landed this run

No new portrait could be confirmed against the "misidentified face is worse than no face" bar,
and the one fresh lead for a year-photograph gap is blocked by an outage outside this project's
control rather than closed. `data/photos.json` and `data/photos/` are unchanged. `git push
--dry-run` confirmed direct write access; pushed the fast-forward merge from `origin/main`
straight to `research-photos`.

## Validation

`python3 scripts/build.py` and `scripts/check_data.py` both pass clean on the unmodified data
tree.

## Left for the next run

- Retry `dlsc_ua_records/9035` (1995-96) once Internet Archive's CDX API is reachable again.
  Editorial check at 03:0x UTC on 22 September: `https://web.archive.org/` is serving again
  (HTTP 200, "Wayback Machine"), but the CDX search endpoint still times out with no bytes
  received, so the partial-recovery pattern this report describes still holds and the lead is
  still untried rather than closed. The `dlsc_ua_records/9035` landing page itself was confirmed
  reachable and is the Herald issue of 12 October 1995 (`article=10017`), whose index carries
  Alfina Mami's "Associated Student Government Reaches Tenth Anniversary".
- The other five year-photograph gaps (1994-95, 2000-01, 2005-06, 2006-07, 2008-09) are
  otherwise as the 20 September third-pass report left them: the local Herald index's
  SGA-tagged headlines are exhausted for the obvious leads, and the image-only mid-1990s/2000s
  issues without an OCR text layer will need a photo-credit-first or visual-scan approach rather
  than keyword search.
- 208 executive/Senate-officer slots remain without a portrait (226 including committee
  chairs), counted fresh this run; the archive.org-covered years
  (1971-1981, 1986, 1987) are now confirmed exhausted twice over. The pre-1988 gap years and
  1988-1995 stretch still depend on the Wayback-PDF route documented in the 17 September report,
  which needs Internet Archive's CDX API back up to use.
