# Photograph run, 25 September (second pass): a landing-page-number trap, and a year-scene photograph for 2005-06

## Starting state

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md` (note: the stored trigger prompt for this
task still says to try `gh auth setup-git` first; `AGENT-LANDING.md` itself, the more recent and
more authoritative source, says `gh` is not installed in these containers and not to waste time on
it — followed the file, not the stale prompt), and `SGA-60-AGENT-INFO.md` sections 4 and 6.
`research-photos` had no local divergent work; fast-forwarded onto `origin/main` cleanly (11
commits, no conflicts). No pull request was open on this branch — the prior rolling PR had already
been merged.

Re-checked the four originally-named presidents (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan
Gilley) before doing anything else: all four already carry a portrait, as `.research/photo-run-2026-09-25-scheduled.md`
(the same day's earlier run) had already confirmed a few hours before this one started. Read that
report in full before proceeding rather than repeating its checks; picked up its two recommendations
instead: retry articles 7666, 7667 and 6164 (all three had come back truncated that morning), and
leave the four 1978-81 Talisman names and Nathan Cherry alone as independently closed dead ends.

## Retried the three truncated articles

The `web.archive.org/web/<ts>id_/<viewcontent.cgi URL>` bypass, fetched with `curl -L` and browser
navigation headers, worked cleanly this time for two of the three:

- **Article 7666** (`dlsc_ua_records/6645`, Herald 82:44, 5 April 2007) — 20.9 MB, opens with real
  text on all 17 pages. Read in full. The SGA story on this front page is the presidential-election
  result ("Johnson keeps presidency"), not a senate-candidate mugshot grid: it carries a captioned
  photo of Jeanne Johnson (already has a portrait) relaxing with her roommate after the results, and
  a second captioned photo of losing candidate Kendrick Bryan. None of the six names this entry was
  chasing — Brian Fisher, Drew Eclov, Emilee England, Jessica VanWinkle, Cacy A. Schooler, Jacob
  Miers — appear anywhere in the issue by name. Closed.
- **Article 7667** (`dlsc_ua_records/6644`, Herald 82:44, 10 April 2007) — 23.3 MB (curl reported an
  HTTP/2 stream warning but the full byte count arrived and the file opens; a few internal objects
  throw "not a stream" errors that did not block text extraction elsewhere). Covers a bookstore
  textbook-deadline resolution and a mock gubernatorial election with Secretary of State Trey
  Grayson — no senate-election result story, and none of Fisher, Eclov, England or VanWinkle appear
  as a photographed subject. Closed.
- **Article 6164** (`dlsc_ua_records/5160`, 2014 Talisman, wanted for Mallory Treece) — still will
  not land. Its only near-normal-size capture (`20230528170903`) downloads every time as exactly
  1,048,576 bytes and will not open (`code=7: Invalid number of pages`); the CDX list's only larger
  alternative is 356 MB, well beyond what is practical to pull through this container in one
  request. Left open, not closed — the capture exists, it just has not landed whole.

## A trap worth writing down: the landing-page number is not the viewcontent article number

Tried to apply the same recipe directly to two more `_topscholar-wanted.json` entries, 3684 and
3695, by assuming the trailing number in their `want` landing-page URL (`dlsc_ua_records/3684`)
was also the `article=` parameter `viewcontent.cgi` needs. It is not, and this assumption produced
a wrong but entirely valid-looking result: fetching `article=3684` returned a clean, complete,
correctly-formed PDF — and it turned out to be *All About Us*, a 1977 WKU library-services
newsletter, sharing nothing with the wanted 2006 Herald issue except the coincidental article
number. Caught only by opening the file and reading page 1, not by the byte count or magic bytes,
both of which looked completely normal.

This should have been obvious from the two successful fetches already on file: `dlsc_ua_records/6645`
is `article=7666`, `dlsc_ua_records/6721` is `article=7724` — different numbering systems, already
demonstrated twice before this run made the same mistake a third time. Re-derived the real number
by fetching the landing page itself, `https://digitalcommons.wku.edu/dlsc_ua_records/3684`, directly
over plain HTTPS with browser navigation headers — it answered 200 on the very first try, no Wayback
bypass needed for a landing page — and reading its own embedded `viewcontent.cgi` link: the true
article id is **4689**. **Anyone continuing this queue: never assume the landing-page slug equals
the viewcontent article id. Resolve it from the landing page's own link, or from a mapping a prior
run already confirmed, before spending a fetch on the guess.**

## What article 4689 actually holds

Herald 81:36, 14 March 2006, "Three Candidates Run for President" — fetched whole (3.9 MB, 17
pages). Its text layer is heavily garbled OCR, consistent with the standing note elsewhere in
`_archive-gaps.json` that mid-2000s Herald scans are close to unreadable as text; pages were
rendered as images and read visually rather than trusted to a text search, after a first blind
search of the extracted text came back empty even for names later confirmed present in a caption
by eye.

- **Page 1** (front page): names the three primary candidates — Berea junior Kara Ratliff, Bardstown
  sophomore Josh McCubbins, Bowling Green senior Robert Watkins — running to succeed the "current
  president," Radcliffe senior Katie Dawson. No photograph of any candidate on this page.
- **Page 9** ("SGA: Elections held in April," continuing the front-page story): carries three
  individually captioned headshots, one per candidate, the name printed directly under each face —
  Josh McCubbins, Kara Ratliff, Robert Watkins, in that order. As firm an identification as this
  project accepts. The same page's running text also names Taylorsville junior Lindsey Lilly and
  Goodlettsville, Tenn. junior Amanda Allen as candidates for administrative vice president, and
  Marion sophomore Jeanne Johnson (then Speaker of the Senate) as the sole candidate for executive
  vice president — none of the three has an accompanying photograph on this page. Alex Wimsatt,
  the third name `_topscholar-wanted.json` listed for this article, does not appear anywhere in the
  issue.

**No new officer coverage.** All three photographed candidates already carry a portrait in
`data/photos.json`: Robert Watkins from a 2006 WKU Board of Regents page (he won this election,
served as SGA president for 2006-07, and resigned that November — the Board seat photo is the one
already on file), and McCubbins/Ratliff from a Herald election special the existing entries date to
"15 March 2005" — a full year before this article. That earlier date was not re-investigated this
run; flagging it here in case it is a transcription slip (2005 for 2006) worth a future run
rechecking, though it does not block anything since both people are already covered either way.

**Landed instead as a year-scene photograph.** Cropped the three-headshot block from page 9 and
added it as `data/photos/2005-06-sga-presidential-primary-candidates.jpg`, attached to `photos.json`
under `years` for **2005-06** — one of the five years with no year-scene photograph at all
(Priority 4). This is SGA's own presidential primary, not campus context, and the caption states
plainly that all three faces are already covered as individuals; the entry exists to document the
election itself. This closes one of the five open Priority-4 years; **four remain: 1994-95, 1995-96,
2000-01, 2008-09.**

## Housekeeping

Added `note` fields to the `_topscholar-wanted.json` entries for 3684, 6645 and 6644 recording what
each issue actually contains, so a future run does not re-fetch any of the three expecting a
different result. Appended today's findings — the article-number trap and the 6164 truncation
detail — to `_archive-gaps.json`.

## Checks

`python3 scripts/build.py` and `python3 scripts/check_data.py` both ran clean with the one new
photograph added: "the archive checks out against its own rules." The build's routine "withdrew 1
photograph(s) the archive no longer holds or has barred" line is the pre-existing `_do-not-use.json`
housekeeping noted as unrelated in the morning's report, not anything from this run.

## Searched and not found this run

- Cacy A. Schooler, Jacob Miers, Brian Fisher, Drew Eclov, Emilee England (2007-08 senate cohort) —
  not in either Herald issue that was supposed to carry their result coverage.
- Mallory Treece (2014 Talisman feature) — capture still will not land whole; not a dead end, just
  still blocked.
- Alex Wimsatt (spring 2006 presidential field) — does not appear in the one issue that should have
  covered him most directly.
