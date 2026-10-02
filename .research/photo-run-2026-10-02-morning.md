# 2 October 2026, morning (photograph routine, scheduled, second run of the day)

## What was checked before doing anything

Same starting point as every run since 20 August, re-confirmed by reading the files directly
rather than trusting the last report: Nick Todd, Katie Dawson, Jeanne Johnson and Reagan Gilley
all still carry a portrait in `data/photos.json`. All 73 top-level `leaders` records (every
president and every student regent) have one — confirmed by cross-checking every `role: president`
or `role: regent` or `also_regent: true` leader in `data/years.json` against `data/photos.json`
programmatically, not by re-reading the prior count. 217 executive/Senate officer records still
lack a portrait, the same 217 the 02:03 UTC run of this same day counted after adding its ten new
names — nothing added to `data/years.json`'s `organization` blocks since then changed this number.
57 of 61 years have at least one year-scene photograph; the four without one are 1994-95, 1995-96,
2000-01 and 2008-09, unchanged.

`research-photos` merged cleanly onto `origin/main` (real merge base, no conflicts — the merge
pulled in 28 commits of date corrections and a duplicate-event cleanup, none touching
`data/photos.json`). `build.py` and `check_data.py` both pass clean on the merged tree before any
new work.

## Access re-tested again, nothing changed since six hours ago

- `cgi/viewcontent.cgi` still `403`, Cloudflare "Just a moment..." challenge — tested against a
  different article than the 02:03 run (10491, a Herald item), waited the full 90-second backoff
  after the first 403, and retried once as the pacing rule asks. Still 403 on retry.
- `web.archive.org` still resets at the TLS handshake (`Recv failure: Connection reset by peer`)
  on a fresh query.
- Ordinary `digitalcommons.wku.edu` landing and item pages still load fine (200/301) — the block is
  specific to `viewcontent.cgi`, not the whole domain, as every prior run has also found. Checked
  the raw HTML of a fresh item page for any non-`viewcontent.cgi` way to reach the PDF (a direct
  CDN link, a `type=native` path, an embedded preview image) — there is none; the single `href` to
  the file is the blocked `cgi/viewcontent.cgi` URL.
- `archive.org` (not `web.archive.org`) still answers normally. Re-ran its advanced search for
  everything in the Talisman collection to check for volumes added since the last count: still
  exactly nineteen identifiers (1943, 1946, 1947, 1963–65, 1971–81, 1986, 1987). No volume for any
  of the ten years this project's open officer and year-photo gaps actually need
  (1994–95 through 2008-09, plus 2016-17 and 2022-23) has ever been digitised there, and that
  remains true this run.

## Nothing to add on names, no new route found

The 02:03 run already built the officer-portrait gap list fresh and worked through every name on
it that had not been searched in an earlier pass (ten names, all unproductive, logged in
`.research/photo-run-2026-10-02.md`). Rebuilding that list again this run returns the identical
217 records — no name in it is unsearched. Running the same ten names again, or the roughly 207
behind them, against `wkuherald.com` a second time in the same day would not be new research, so
this run did not repeat it. The two routes that could still move the gap list or the four
year-photo years forward — `viewcontent.cgi` for Talisman 1988-2013/2014-2026 and pre-2002 Herald
issues, and `web.archive.org` for Wayback-era `wku.edu/sga` officer pages — are both confirmed
closed again, by direct re-test with full backoff, not by assumption.

## Nothing added

No file in `data/photos.json` or `data/photos/` changed this run. `python3 scripts/build.py` and
`python3 scripts/check_data.py` both run clean against the unmodified tree (61 years, all 73
leader portraits present, 217 officer portraits still open, the same four years without a scene
photograph).

## For the next run

Keep retrying `viewcontent.cgi` and `web.archive.org` cold on each new run — both have reopened
briefly before without warning, most recently per the 1-2 October reports. Until one of them does,
there is no further forward motion available on the officer-portrait gap or the four year-photo
gaps: every name and every alternate route this project has found is exhausted. Do not re-run the
same name-by-name `wkuherald.com` sweep again without a new source or a reopened route; treat the
217-record gap list as fully searched there as of this run.
