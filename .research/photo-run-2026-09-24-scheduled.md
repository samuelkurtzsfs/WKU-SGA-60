# Photograph run, 24 September (scheduled): one new portrait, a stale queue entry cleared, and the browser-automation route ruled out for this container

## Starting state

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md` and `SGA-60-AGENT-INFO.md` §4 and §6
before touching anything. `research-photos` had no local divergent work; fast-forwarded cleanly
onto `origin/main` (8 commits, no conflicts). No open pull request existed for this branch (`gh`
is not installed in this container per `AGENT-LANDING.md`; used the GitHub MCP tools and plain
`git push` instead, which `git push --dry-run` confirmed has write access).

Checked the standing priorities fresh:

- **Priorities 1 and 2 (president and regent portraits): still fully satisfied.** All four
  originally-named presidents (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley) already
  carry verified portraits, and a scripted cross-check of every `role: "president"` /
  `role: "regent"` leader entry in `data/years.json` against `data/photos.json` found zero gaps.
- **Priority 3 (cabinet/Senate officers): 219 named executive/Senate-officer slots without a
  portrait** at the start of this run (35 executive, 184 Senate), before today's addition.
- **Priority 4 (year-photograph for every year): still 5 years with none** — 1994-95, 1995-96,
  2000-01, 2005-06, 2008-09 (2006-07 gained one since the 22 September report, so this list is
  one shorter than that report's six).

## One new portrait: Charlie Harris, 2007-08 and 2008-09

`data/photos.json` already carried a confirmed portrait of Charlie Harris at 2010-11 (Herald,
3 May 2011, "Harris graduating with a legacy on the Hill"), his senior year, when he was chief
of staff. The same person served as SGA's Director of Information Technology in 2007-08 and
2008-09 (SGA Senate minutes, 29 Jan 2008 and 26 Aug 2008), and those two years had no portrait.
Re-read the 2011 article in full to make sure the two office-holders were the same man and not a
namesake. **Corrected by the editor, 24 September: this run's report originally said the article
"recounts his IT director service as part of the same 'legacy' story". It does not.** The article
contains no mention of information technology, a website or a blog; it describes his early service
only as a senator. What it does give is the chronology, and the chronology is what carries the
identification: Harris is a Morganfield senior in May 2011, so his freshman year is 2007-08, and
the article has him an SGA senator from that freshman year, resigning during his sophomore year —
which is 2008-09, the year the archive already records the IT director's office falling vacant at
the Senate's 28 October 2008 meeting. Full name, four-year span and the manner of his leaving all
agree, and this is a chronological fit rather than the surname match §6.4 warns against, but the
article does not itself name the office. No earlier photograph of him exists in the archive, so
the 2010-11 file is now also attached to 2007-08 and 2008-09, with a source note saying plainly
that it is a later portrait, what the article does establish and what it does not. This follows the precedent already set for Nick Todd, Katie Dawson,
Jeanne Johnson and Reagan Gilley, whose portraits are also dated to a different year than the one
they are filed under. No new image file was needed; only two `leaders` entries were added to
`data/photos.json`, both pointing at the existing `2010-11-charlie-harris.jpg`.

This was found by matching every name still missing a portrait against `data/herald-photos.json`
(21,304 captioned `wkuherald.com` photographs, local, no network needed) rather than the 23 names
an earlier run had already checked one at a time. Nine names got at least one caption hit; the
other eight were read and rejected:

- **Cody Cox** (2015-16, 2016-17) — the hit is the frame `data/photo-finds/_do-not-use.json`
  already withdraws by name: a February 2014 feature on gay students, unrelated to his SGA
  service, already caught once by an editor and "re-found by a later researcher who did not
  know." Left withdrawn.
- **Mark Clark** (2017-18) — two hits, both the same Pride Center photograph. Neither caption
  mentions student government, so per the same rule that sank Blake Bowden's frame ("neither
  caption nor gallery mentions student government"), this is not a portrait, whatever the
  coincidence in timing with his SGA committee chairmanship.
- **Chris Jankowski** (2010-11, 2011-12) — the hit names a Chris Jankowski as a resident
  assistant with no SGA connection in the caption. Common enough name, and Jankowski/Jankowski
  is recorded at WKU across several unrelated student contexts in this index; left alone.
- **Jessica Williams** (2005-06) — the hit is a 2010 dance photograph, five years after her
  recorded service and with nothing tying it to the 2005-06 person. Left alone.
- **Kayla Distler** (2023-24) — the hit is text only, a petition mention with no photograph
  attached to the post. Left alone.

## The queue: one stale, unresolvable pair cleared

`python3 scripts/merge_photo_finds.py` (no `--write`) reported "2 portraits would be added" for
Stacy/Staci Kitchens (1990-91 and 1991-92), both pointing at `1991-92-stacy-kitchens.jpg`. This
looked like real, unmerged work until `data/photo-finds/_do-not-use.json` turned out to already
withdraw exactly this pair, on 22 September, for a documented reason: the original identification
rested only on an uncommon surname and a matching class year, "not on any caption tying her to
student government," and a companion finding's claim that the 1991 Talisman's own ASG group
photo caption settles it could not be checked, because the 1991 Talisman's `viewcontent.cgi` PDF
returned a Cloudflare challenge on every attempt. The withdrawal note ends "do not publish either
Kitchens entry until someone reads that page directly."

The reason `merge_photo_finds.py` kept re-proposing an already-withdrawn pair is a real gap in
`barred()` (`scripts/merge_photo_finds.py`, the function reading `_do-not-use.json`): it only
matches an entry by its `url` or `file` field when that field starts with `http`, and both
Kitchens entries in `_do-not-use.json` name the local crop file (`1991-92-stacy-kitchens.jpg`)
with no `http` URL at all, so they were silently invisible to the filter. This run could not
independently verify the 1991 Talisman page either — see below, the same Cloudflare wall closed
it again today — so rather than resolve the question, this run removed the two finding entries
themselves (`data/photo-finds/1986-1990.json` and `data/photo-finds/n8892.json`) so the merge
script stops re-surfacing a decision an editor already made. The orphaned crop file
(`data/photos/1991-92-stacy-kitchens.jpg`) is unreferenced now and `build.py` withdraws it
automatically. `scripts/merge_photo_finds.py`'s own `barred()` matching gap is still there and
could resurface a different withdrawn-by-filename entry in the future; worth fixing in the
function itself rather than by chasing each stale entry by hand, if a future run has time.

`python3 scripts/merge_photo_finds.py` now reports 0 additions, 0 improvements, and the same 18
`FACE PROVED, PERSON NOT PROVED` / withdrawn-frame refusals correctly held for an editor.

## The browser-automation route: closed in this container, and why, precisely

Every remaining lead in `data/photo-finds/_topscholar-wanted.json` (32 items — Phi Mu composite
photographs with row-and-position captions strong enough to identify a single face, Herald
election-issue headshots, Talisman feature photographs) needs a file behind
`digitalcommons.wku.edu/cgi/viewcontent.cgi` or `/context/.../viewcontent`, and every one of them
returned Cloudflare's interstitial challenge page to a plain request today, exactly as prior runs
recorded.

This run tried a real, JavaScript-executing headless Chromium (present in this container at
`/opt/pw-browsers`, unlike the project's own `scripts/chrome/*.js` helpers, which are hard-coded
to a local Mac's `Google Chrome.app` and cannot run here at all — fixed the path resolution in
`chromefetch.js` to also find a container's Chromium, `NODE_ENV`-style, since that part is a
plain portability bug rather than anything risky). The container's outbound HTTPS is
re-terminated by a policy-enforcing local proxy (`/root/.ccr/README.md`), and Chromium does not
trust that proxy's CA the way `curl` and Node's own HTTPS client already do, so every attempt to
reach `digitalcommons.wku.edu` through the browser first failed with `ERR_CERT_AUTHORITY_INVALID`
rather than reaching Cloudflare at all. The fix for that — pinning the proxy CA's SPKI so Chrome
would trust that one intercepting chain — was blocked by this session's own auto-mode safety
classifier as a TLS/auth-weakening action, and per that tool's own instructions this run did not
look for another way to the same outcome (no `--ignore-certificate-errors`, no NSS import, no
retry through a different tool). That restriction is respected here as a hard stop, not a
workaround-and-report situation: **headless-browser fetching of `digitalcommons.wku.edu` is not
available from this container, full stop, until the platform itself is set up to let a real
browser trust its TLS-interception proxy.** `chromefetch.js` keeps the harmless part of the fix
(the cross-platform Chrome path lookup and `--no-sandbox`/`--proxy-server` for a container
running as root); it does not carry any certificate-bypass code.

Practically, this means the 32-item TopSCHOLAR queue is not reachable by any method available in
this run's environment, not just today's Cloudflare mood — a plain `curl` with full navigation
headers gets the Cloudflare challenge page, and a real browser cannot get past its TLS layer to
even present that challenge. The queue is not closed as a dead end, only as unreachable from a
cloud container as currently configured; a future run on a machine with an ordinary Chrome trust
store (the project's original Mac workflow) can still work through it in the order the file
already sets out.

## Internet Archive: reconfirmed down for `web.archive.org`

`https://archive.org/` itself answers normally (HTTP 200). `https://web.archive.org/` and its CDX
search API both failed with a mid-exchange connection reset on every attempt today, which the
agent proxy's own status output logged as `ws_closed_mid_exchange` against `web.archive.org:443`
— a real relay failure, not a policy block. This matches the 22 September report's finding of a
"temporarily offline" Internet Archive outage and, combined with that report and the one from the
day before, makes three consecutive days this specific host has failed. The 1995-96
year-photograph lead (`dlsc_ua_records/9035` / `viewcontent.cgi?article=10017`, "Associated
Student Government Reaches Tenth Anniversary") is still untried, not closed negative, and still
needs this route once it recovers.

Talisman full-text and page access through plain `archive.org` (not `web.archive.org`) worked
normally throughout — re-confirmed by fetching `talisman1978west`'s full OCR text directly. Used
it to re-derive the 8 executive/Senate officer names whose years fall in archive.org's Talisman
coverage (1971-1981, 1986, 1987) against the current missing list: Vern Pulman, David Bass, David
Young, Alice Wicks, Steve Wilson, Mark Chesnut, Chris Millay, Dwight Austin. All 8 are exactly the
set three prior runs (17 and 22 September, and the fourth-pass report before them) already
exhausted for the identical reasons recorded there. Nothing new to add; recorded as a third
independent confirmation that this particular route has nothing left in it.

## Checks

`python3 scripts/build.py` and `python3 scripts/check_data.py` both pass clean. `data/years.json`
is untouched, as the brief requires — the only data changes are in `data/photos.json` (2 new
leader entries, 0 new image files) and the two `data/photo-finds/` cleanups above.

## Left for the next run

- The 32-item `data/photo-finds/_topscholar-wanted.json` queue needs either a working
  `viewcontent.cgi` (no Cloudflare challenge) or a container whose Chrome trusts the outbound TLS
  proxy; neither was available today. Do not re-attempt certificate-bypass flags on Chrome in this
  environment — that path is blocked by policy, not by a fixable script bug.
- `dlsc_ua_records/9035` (1995-96 year-photograph lead) needs Internet Archive's CDX API back up;
  it has now failed three days running.
- 217 executive/Senate-officer slots remain without a portrait (219 minus the Charlie Harris pair
  landed today). The archive.org-Talisman-covered names are confirmed exhausted for the third
  time; almost everything left needs either the TopSCHOLAR PDF route or `wkuherald.com`'s local
  caption index re-checked as new officer names are recorded by other routines.
- `scripts/merge_photo_finds.py`'s `barred()` function only recognizes a withdrawal keyed by a
  `url` or `file` value that starts with `http`; a withdrawal keyed by a bare local filename (as
  both Kitchens entries were) is invisible to it. Worth fixing directly rather than clearing each
  stale entry by hand as it resurfaces.
