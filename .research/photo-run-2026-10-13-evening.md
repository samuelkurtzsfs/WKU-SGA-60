# Photograph run, 13 October (evening): the 1994-95 year-photo gap closed, both gated routes retested live

## Priorities 1, 2: reconfirmed against the current file before anything else

**Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
portrait in `data/photos.json`, checked by reading each entry directly.

**Priority 2** (any other president or student regent without a portrait): zero, computed by
walking every `leaders` entry in `data/years.json` against `data/photos.json`'s leader list.

## Both gated routes retested live, not assumed

`digitalcommons.wku.edu/cgi/viewcontent.cgi` answered **403, Cloudflare "Just a moment..."
interstitial** against article 8989 (the standing 1994-95 lead), full browser navigation-header
set. Still closed, consistent with every pass since late September.

`web.archive.org` answered inconsistently across four different URLs and nine attempts this
session: three plain connection resets at the TLS layer, one open 302 on a throwaway
`wku.edu/sga` snapshot, three HTTP 403 "Blocked by egress policy" responses (the agent proxy's
own block on an `http://` request to that host, not the server), and **two full 200 responses
with a real PDF body** against the exact standing lead,
`https://web.archive.org/web/20240906210952/https://digitalcommons.wku.edu/cgi/viewcontent.cgi?article=8989&context=dlsc_ua_records`
— a 27,977,595-byte file beginning `%PDF-1.7`, confirmed by `file` as a genuine 21-page PDF, not
a bot-check page saved under the wrong name. Four attempts against that same URL timed out
mid-download before completing; one of the two successes was itself a retry after a timeout. The
pattern: the route is not simply "open" or "closed" this session, it drops the connection more
often than it completes one, but it completes often enough that repeated retries, spaced a few
seconds apart, get through. Worth remembering for the next run that finds it refusing on the
first one or two tries.

## The 1994-95 year-photo gap, closed

The standing lead was Herald 69:51 [52], 19 April 1994 (`dlsc_ua_records/7984`, article 8989 —
the same issue already cited for Robert Evans's own 1994-95 portrait, drawn from its page 1).
With the PDF in hand for the first time since this gap was opened, every page was read, not just
the pp. 6-9 range earlier notes had flagged as the target: the front page's own SGA election
story carries no photograph of its own (the accompanying photo is an unrelated "clean sweep"
campus-maintenance picture), pp. 6-9 hold a judicial-council story, a Banshee rugby-party photo
feature, storm-damage coverage and a women's-studies appointment, none of them SGA's business
with a usable photograph. Page 11 does: a full-column paid campaign advertisement, "ELECT Rob
Evans President / Tara Higdon Vice-President," carries a photograph of both candidates together,
captioned by the ad copy itself rather than a Herald caption — their names and the offices they
were seeking are printed directly beside the photograph, which is the same identification bar
the archive has used for other candidate photographs (e.g. the 1990-91 "Meet the Candidates"
box). This is the actual ticket that won the election that issue covers; Evans took office as
1994-95 president and Higdon as his administrative vice president, confirmed already in
`years.json`.

Cropped to the photograph itself (both faces, cutting the ad copy and the candidates' names
printed beside it, which run on in the source and are not part of the image) and saved as
`data/photos/1994-95-evans-higdon-campaign-ad.jpg`. Verified `FF D8 FF E0` before and after
copying into the repository. Added to `data/photos.json`'s `years` array — not `leaders`, since
both Evans and Higdon already carry individual leader portraits from other sources and this is
general documentation of the year, specifically an election-season artifact rather than a news
photograph. The caption says plainly that it is a paid advertisement, not Herald photojournalism,
so a reader is not misled about what kind of document it is.

This was the only year left without a year-level photograph; `portrait_gap.py`'s separate officer
tally is unaffected (189 slots / 159 people / 157 with no portrait anywhere, unchanged — nothing
in this run touched the cabinet/Senate officer gap, only the standing year-photo lead).

## Priority 3: not attempted this run

The pre-2016 officer-gap slice was reported fully exhausted on every open route as of this
afternoon's run (`photo-run-2026-10-13-afternoon.md`), with the only remaining path being the
2012-13 through 2016-17 Talisman volumes behind `cgi/viewcontent.cgi`. That route answered 403
again this session (see above). Spent the open `web.archive.org` window on the standing,
already-identified 1994-95 lead instead of a fresh name search, since a known, specific target
was more likely to pay off in a narrow, unreliable window than starting a new search cold.

## Build and validation

`python3 scripts/build.py` then `python3 scripts/check_data.py`: 61 years, 1,968 events, 60
presidents, clean. `site/` rebuilt and committed alongside the data and image files, matching
the precedent set by the last photograph that was actually added (#739, the 2000-01 debate
photograph) — a photograph commit lands its own site rebuild rather than leaving `site/` stale
on this branch.

## For the next run

- `web.archive.org` is worth retrying directly against any standing lead before assuming it is
  closed from a single attempt — it dropped more connections than it completed this session, but
  completed enough, on retry, to deliver a full 28MB PDF twice.
- The 1994-95 gap that stood since late August is now closed. No year-level photograph gap
  remains open in the file as of this run (reconfirmed: all years from the Priority 4
  description now carry at least a leader portrait, and this was the last without a year
  photograph).
- The pre-2016 officer-gap Talisman slice (Priority 3) is still the only work item this routine
  has open, and it is still entirely behind `cgi/viewcontent.cgi`, which did not reopen this
  session.
