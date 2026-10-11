# Photograph run, 11 October (scheduled) — both gates retested cold, a third source (wkuherald.com direct page fetch) found newly challenged mid-run, no new leads from an office-title Google search or from the one SGA Notes item the gap list pointed at

## Priorities 1, 2 and 4, reconfirmed before anything else

**Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
portrait in `data/photos.json`. Nothing to do.

**Priority 2** (any other president or student regent without a portrait): checked every
`leaders` record in `data/years.json` against `data/photos.json` by name, programmatically. Zero
missing.

**Priority 4** (years with no photograph at all): every one of the 61 years has at least one
photograph in `data/photos.json`. Zero missing.

So this pass's whole job was priority 3, same as every run since mid-September:
`scripts/portrait_gap.py` reports 189 officer slots with no portrait, held by 159 distinct
people, 157 of them with no portrait anywhere in the file. Unchanged.

## The two standing PDF gates, retested cold

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — HTTP 403 with full navigation headers
  (`Sec-Fetch-Dest: document`, `Sec-Fetch-Mode: navigate`, `Upgrade-Insecure-Requests: 1`). Same
  Cloudflare block as every pass since this gate closed. The ordinary landing pages
  (`dlsc_ua_records/<n>/`) are still open (HTTP 200) — only the PDF download itself is gated.
- `web.archive.org` — `curl: (35) Recv failure: Connection reset by peer`. Not open this session.

## A new, narrower finding: wkuherald.com's own article pages can return a Cloudflare challenge too

Prior notes (8-10 October) treated `wkuherald.com` as open, using its `/wp-json/wp/v2/` REST API
and that API stayed open this run (confirmed: `?search=SGA` returns normal JSON, HTTP 200). But a
direct fetch of one specific article's permalink (`wkuherald.com/?p=52195`) came back as a
Cloudflare "Just a moment..." challenge page, HTTP 403, with two different browser User-Agent
strings tried 5 seconds apart. This is new: no prior photo-run note records the plain article
page itself, as opposed to the PDF gates, being challenged. It did not block this run, because
the REST API's `content.rendered` field carries the same article text without touching the
challenged path, but it is worth flagging for whoever next relies on the "fetch the HTML page to
read `wp-image-` and `data-photoids` attributes" method documented in the 10 October morning
note — that method fetches the rendered page directly, not the API, and would have hit this wall
today. Whether it is a standing new gate or an intermittent flag on one request is not established
from a single hit; retest before concluding either way.

## What was actually tried this run, and why none of it produced a portrait

**Office-title-plus-year Google queries**, the specific untried method the 10 October evening
note flagged (it had only tried bare-name queries before). Ran `site:digitalcommons.wku.edu`
searches for "Chief Justice"/"Judicial Council" against Scisney and Crockett, for "Speaker of the
Senate" against Nathan Cherry, and a plain WKU-SGA query for "Director of Public Relations"
investiture photos circa 2015-16. None returned a digitalcommons.wku.edu hit naming any of the
159 gap people at all — every result was either a current (2023-2026) wku.edu/sga minutes/judicial
page naming people outside this archive's scope (Hannah Hash, Morgan Gammons, Colton Stirling,
Murphy Burke — current officers, not this project's business) or an unrelated university's SGA.

**Followed one concrete lead the search surfaced**: a wkuherald.com "SGA Chief Justice Crockett
resigns" story and its follow-up "Jessie appoints Scisney as new Chief Justice" — both are
in-scope (Dajana Crockett and Art Scisney are both on the 2009-11 gap list). Read both in full via
the REST API. Both are plain-text "SGA Notes" meeting summaries with no `<img>` tag, no
`wp-image-` class and no `data-photoids` attribute in their content — consistent with the 10
October morning finding that routine SGA meeting coverage does not photograph ordinary officers.
No portrait in either.

## Nothing landed

No file in `data/photos.json` or `data/photos/` changed; `data/years.json` is untouched.
`python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean (61 years, 60
presidents, photo overlay attachment and file-magic checks pass). This run's only output is this
note.

## For the next run

- Retry both PDF gates cold, as always.
- Retest whether the wkuherald.com article-permalink Cloudflare challenge found this run is a
  standing gate or a one-off; if it has hardened, the gallery-caption method from 10 October
  morning (which depends on fetching the rendered page, not the REST API) needs a fallback that
  reads captions a different way, since the REST API's `content.rendered` does not appear to
  carry gallery attachment IDs for the shortcode format.
- The office-title-plus-year Google strategy is now tried-and-negative for this archive; current
  wku.edu/sga pages keep surfacing in its place, which are out of scope (this project's own
  organization data, not photographs, and not this routine's business to update).
- 189 officer slots / 159 people / 157 with no portrait anywhere remains the live count.
