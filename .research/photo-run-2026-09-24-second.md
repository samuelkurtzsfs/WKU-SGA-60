# Photograph run, 24 September (second scheduled run): the Wayback Machine bypass, four portraits, and a Jeanne Johnson upgrade

## Starting state

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md` and `SGA-60-AGENT-INFO.md` before
touching anything, per the brief. `research-photos` had no local divergent work; fast-forwarded
onto `origin/main` cleanly (merge commit, no conflicts). An earlier run today already closed
PR #578 on this branch; this run reopens the rolling PR.

Re-checked the four originally-named presidents (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan
Gilley) before spending time: all four already carried a portrait, confirming this morning's
report. A scripted cross-check of every `role: "president"` / `role: "regent"` leader against
`data/photos.json` found zero gaps — priorities 1 and 2 are still fully satisfied.

## The find: `web.archive.org` now bypasses the Cloudflare wall on `viewcontent.cgi`

This morning's report (`.research/photo-run-2026-09-24-scheduled.md`) recorded `web.archive.org`
as down for a third consecutive day, and TopSCHOLAR's `viewcontent.cgi` PDF endpoint as returning
Cloudflare's interstitial challenge to every plain request, closing the 32-item
`data/photo-finds/_topscholar-wanted.json` queue entirely. Both are still true individually — a
direct `curl` to `viewcontent.cgi` still gets the Cloudflare "Just a moment..." page, and
`web.archive.org` is still intermittent (several requests failed mid-exchange with
`ws_closed_mid_exchange`, matching the proxy's own failure log).

But **fetching a `digitalcommons.wku.edu` `viewcontent.cgi` URL through
`https://web.archive.org/web/<year>/<url>` works**, when a snapshot exists, and it returns the
real file — a PDF or, for the `stu_org` composite photographs, a JPEG served directly — not
Cloudflare's challenge page. This makes sense: the Wayback Machine's crawler fetched these pages
years ago and serves its own cached copy, so today's Cloudflare gate on the live site never comes
into it. The catch is `web.archive.org` itself: about half of today's requests to it succeeded
outright, and the other half reset mid-connection and needed one or two retries with a short
backoff. The CDX API (`web.archive.org/cdx/search/cdx`) is the same story — it answered directly
about half the time and timed out or reset the rest — and it is worth querying before guessing a
snapshot year, because **more than one snapshot can exist for the same URL at very different
sizes**: one `viewcontent.cgi` fetch today first landed a snapshot from 2019 that was a genuinely
truncated 1.03 MB capture (confirmed against the CDX record's own `length` field, not a proxy
problem), while a 2023 snapshot of the identical URL was the real 24 MB scanned issue. Always
check the CDX listing's `length` column and prefer the largest capture when more than one exists.

This reopens the entire 32-item TopSCHOLAR queue that this morning's report closed as
unreachable, and it does not depend on the browser-automation/TLS-trust problem that report also
ran into — this is a plain `curl` through the existing proxy, nothing more.

## What this run found and added

Worked through the queue with this method, checking each name against `data/photos.json` first
(several queue entries turned out to already be resolved by other routines since the queue was
written — noted below to save a future run from re-fetching them).

**New portraits added, all in `data/photos.json` only — `data/years.json` untouched:**

- **Eileen Forsythe** (2008-09 senator) and **Shelby Nitzken** (2013-14 senator) — WKU Archives
  UA1C11/105/35, the Phi Mu Delta Tau chapter composite for 2011-2012 (`stu_org/375`). Fetched as
  a 7.3 MB JPEG directly from a 2019 Wayback snapshot of the `context/stu_org/article/1370`
  download link. Every face on this composite carries its own printed name label under the oval
  portrait — not a positional description to be miscounted, an actual name in type — so
  identification is as certain as this kind of source gets. Cropped Forsythe (4th row, 1st from
  left) and Nitzken (7th row, 2nd from left) directly from the full-resolution composite; both
  labels read exactly as printed. The same composite also carries Brenna Duncan and Alyson
  Manley, both already portrayed from other sources, so those two were not duplicated.
- **Ben Redmon** (2005-06 senator, Campus Improvements Committee vice-chair) — *College Heights
  Herald*, "Leaving the Party at 10:30," the 1 May 2008 commencement special section, p. 6C,
  fetched via a 2023 Wayback snapshot of `dlsc_ua_records/6729`'s `viewcontent.cgi` link (the 2019
  snapshot of the same URL was the truncated capture described above). His graduating-senior
  column is captioned "Ben Redmon, President, Interfraternity Council" directly under his
  portrait — not an SGA caption, but a portrait of the named, dated individual is still a portrait
  the archive did not have. Not the same year as his SGA service, noted as such in the source.

**One upgrade — Jeanne Johnson, 2005-06/2006-07/2007-08:** the same page of that commencement
section carries a second column, captioned in as many words as it gets: **"Jeanne Johnson,
President, Student Government Association."** Her existing portrait (all three years) was a
November 2007 Homecoming Queen photograph that never captioned her SGA role at all — a weaker
identification than this one, which names the office in print. Replaced all three `leaders`
entries' `file` and `src` with the new image (`2007-08-jeanne-johnson-sga.jpg`) and removed the
now-unreferenced `2007-08-jeanne-johnson.jpg`. This is one of the four presidents this run's brief
named by name, so getting a directly-captioned source for her rather than an incidentally-dated
one is worth the upgrade even though the gap itself was already closed.

## Leads checked and found already resolved (no action needed)

Cross-checking the rest of the queue against the current `data/photos.json` before spending a
Wayback fetch on each showed several names already carry a portrait from other sources, landed by
routines since `_topscholar-wanted.json` was written:

- **Currie Martin** (William Currie Martin) — already portrayed 2008-09/2009-10 from a Herald
  sports feature. Fetched the queue's own lead anyway (23 March 2010, SGA executive VP race) as a
  first test of the method: it is a clean single-candidate headshot captioned "CURRIE MARTIN," so
  the method is confirmed sound even though this particular portrait was not needed.
- **Austin Wingate** — already portrayed 2008-09/2010-11; not recorded as an officer in
  `data/years.json` for the 2011-12 presidential-candidacy year the queue's lead was for, so nothing
  to attach a new portrait to.
- **LaDarra Starkey** and **Dajana Vasilijevic-Klingler** — both already portrayed from the exact
  Phi Mu composites the queue named (2007-2008 and 2006-2007 respectively). Re-fetched the 2008
  composite to double-check and confirmed the existing crop and caption are correct.
- **Jacob Turner, Tyler Jury, Daniel Shaw, Drew Mitchell, Amanda B. Allen** — all already
  portrayed. Amanda Allen's queue lead (a 4 April 2006 debate photo, "Amanda Allen (center)")
  was fetched and is a clean, positionally-captioned group photo, but she already has a portrait,
  so it was not added a second time.

## Leads checked and ruled out

- **Corey Bewley** (2008-09 Chief Justice successor) — the named article, "SGA approves new chief
  justice" (Herald, 19 Feb 2009, p. 3), ran with no photograph at all. Confirmed by rendering the
  page directly. No portrait exists in this source.
- **Timothy Gilliam** — the queue's lead is a 17 November 2009 feature on students who work for
  politicians, but the archive's only recorded Timothy Gilliam served as a senator in **2013-14**,
  four years later. Too large a gap for a name this ordinary to stand on alone (the archive's own
  rule against surname-only or coincidental-name matches applies just as much to a four-year date
  mismatch as to a spelling coincidence); left alone rather than guessed at.

## What this leaves for the next run

- **The Wayback bypass is real and worth using systematically**, not just on this run's sample.
  Roughly two-thirds of the remaining `_topscholar-wanted.json` queue (the Herald single-subject
  and small-group items, items 6-28 in the file as it stood this morning) has not been attempted
  yet: Mallory Treece, Lisa Kappler, Katherine Smith, and the large multi-name election-issue
  leads (items 22-27, up to 46 names in one 2006 cohort with no portrait at all) are all still
  open. Budget retries: expect roughly one `web.archive.org` request in three to need a second or
  third attempt with a short backoff, and check the CDX `length` field before trusting a single
  snapshot.
- The `_topscholar-wanted.json` queue itself should be pruned of the entries this run confirmed
  already resolved (Martin, Wingate, Starkey, Vasilijevic-Klingler, Turner, Jury, Shaw, Mitchell,
  Allen) so a future run does not re-derive the same "already done" conclusion from scratch.
- The finding aid for **UA1C4/10 Student Government Association Photos** (WKU Archives' own SGA
  photograph collection) was successfully fetched this way for the first time
  (`dlsc_ua_fin_aid/620`, via `context/dlsc_ua_fin_aid/article/1619/viewcontent/auto_convert.pdf`).
  It lists physical folders and negatives by name for 1961-1973 (Doug Alexander, Bill Straeffer,
  Reed Morgan, and dozens more), but these are undigitized prints and negatives, not files
  reachable online — useful as a name/date index for what the physical archive holds, not as a
  source of images. Worth reading in full by a future run for cross-checking names and dates
  against 1960s-70s election-year composites, but it does not shortcut to any single portrait on
  its own.
- The 5-year general-photograph gap (1994-95, 1995-96, 2000-01, 2005-06, 2008-09) is unchanged.
  The 1995-96 lead this run had on file (`dlsc_ua_records/9035`, "Associated Student Government
  Reaches Tenth Anniversary") was fetched successfully via this same Wayback method — the CDX
  outage blocking it this morning has cleared — but it turned out to be a Homecoming retrospective
  special section looking back at SGA's first decade from October 1995, not a photograph of
  1995-96 itself; its one photograph (a 1956 Homecoming bonfire) predates the year by four decades
  and does not represent it. Confirmed no usable general photograph in this particular document;
  the gap is still open for a future run.

## Checks

`python3 scripts/build.py` and `python3 scripts/check_data.py` both pass clean. `data/years.json`
is untouched. Changes are confined to `data/photos.json` (4 leader entries added/changed across
Forsythe, Nitzken, Redmon and the three Jeanne Johnson years) and `data/photos/` (three new image
files; one superseded file removed).
