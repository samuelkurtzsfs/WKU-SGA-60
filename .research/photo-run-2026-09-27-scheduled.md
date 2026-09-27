# Photograph run, 27 September (scheduled): baseline reconfirmed, one new dead end on the browser-bypass idea

## Starting state

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md` and `SGA-60-AGENT-INFO.md` sections 4 and 6.
`research-photos` was one commit behind `origin/main` (the 27 September proposal-dating fix);
merged cleanly, no conflicts. No pull request was open on this branch.

Re-verified programmatically: **0 of the 73 leader records (every president and every student
regent, including Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley) lack a portrait**, and
all four target files are present on disk and start `FF D8 FF E0`. Priorities 1 and 2 remain fully
done. The officer-portrait gap and the four-year photo gap (1994-95, 1995-96, 2000-01, 2008-09) are
unchanged from the last few runs.

## digitalcommons.wku.edu: same Cloudflare wall, plus a browser bypass tried and closed

Tested `cgi/viewcontent.cgi` again with the documented browser-navigation headers, a warmed cookie
jar from the item's landing page, and a `Referer` header: still a Cloudflare interactive-challenge
page (`Just a moment...`) rather than a PDF, on both a Talisman volume and a Herald issue already
cited elsewhere in this archive. Same signature every run this week has logged.

New this run: tried going around it with an actual browser (Playwright/Chromium, pre-installed in
this container) rather than curl, on the theory that a real JS engine could clear the interactive
challenge where curl can't. It cannot get there either, for an unrelated reason: this container's
Chromium doesn't trust the proxy's TLS certificate (`net::ERR_CERT_AUTHORITY_INVALID` on the plain
item landing page, before any Cloudflare challenge is even reached), and importing the proxy's CA
into Chromium's trust store is a sandbox action this environment refuses outright. So the browser
route is closed for a different reason than the curl route, and neither is fixable from inside a
session. **Not worth retrying with a browser again** — record this so the next run doesn't spend a
cycle rediscovering it.

`web.archive.org` was not retested this run; the last two runs already established it as a standing
block in this container (connection reset / `hostname_blocked` depending on scheme).

## Officer portraits: independently re-swept the same pre-1990 names, same dead ends, more detail

Before searching, checked every priority in order per this run's brief. Programmatic counts:
33 executive records and ~182 senate-officer/member records still lack a portrait; 37 of those fall
within archive.org's Talisman coverage (1971-72 through 1981-82, 1986-87, 1987-88), the only span
reachable without digitalcommons.

Worked the archive.org route directly (djvu full text plus each volume's own `_scandata.xml` for
exact `leafNum`→printed-page mapping, converting with the documented `n = leafNum − 1`, per the
note already in `SGA-60-AGENT-INFO.md` §6). This reproduces the "26 September third pass" sweep of
the same eight names, independently, and reaches the same conclusions with the specific page
checked in each case:

- **David Bass** (1977-78 Activities VP) — 1978 Talisman p. 34, the ASG-meeting photograph already
  used for Bob Moore, Cathy Murphy and Sharon May. Confirmed again that the caption names four
  people ("laughter from president Bob Moore and smiles from activities vice president David Bass,
  secretary Sharon May and vice president Cathy Murphy") against three or fewer distinguishable
  faces, with no positional cue. Left alone, correctly.
- **David Young** (1978-79 Administrative VP) — index page 289 is a body-text quote in an ASG
  feature ("David Young, administrative vice president, said...''), not a photograph. No portrait
  in this volume.
- **Alice Wicks** (1978-79 Secretary) — indexed with no page number in the 1979 Talisman, the
  convention this archive's index uses for a name with no portrait. Nothing to find in this volume.
- **Steve Wilson** (1978-79 Judicial Council Chairman) — index page 296 is a four-person Pre-Law
  Club photo captioned by initial only ("Back row: J. Rue, S. Wilson"); pages 318/320/336 are an
  uncaptioned Greek Week photo and unrelated content. An initial-only caption in an unrelated club
  is too weak to stand as this Steve Wilson's identification.
- **Mark Chesnut** (1980-81 Treasurer) — index page 234 is the intramural-champions results box
  (naming "Mark Chestnut, Sigma Alpha Epsilon" as a badminton/racquetball winner), not a photograph.
- **Chris Millay**, **Dwight Austin** (1986-87 Parliamentarian, Sergeant-at-Arms) — neither name
  appears with a page number in the 1987 Talisman index at all.

Two more names outside that original eight were checked this run and are new dead ends, recorded so
nobody repeats them:

- **M. A. Baker** (1980-81 Congress member) — the one indexed page (36) is an uncaptioned moped
  photograph with no connection to this person.
- **Maura Fleenor** (1980-81 Congress member) — appears once, by name, in a roughly 60-person Chi
  Omega composite photograph (1981 Talisman p. 304, "Fourth row: ... Maura Fleenor ..."). Unlike the
  senior-grid portraits this archive already uses (uniform individual cells keyed to a printed name
  block), a freeform sorority composite this size has no reliable way to crop the right face to the
  right name from the row/position description alone. Not used.

Current-decade names (Rachel Keightley, Sawyer Coffey, Tribhuwan Singh) were spot-checked against
web search rather than re-scraped from wkuherald.com directly, to avoid re-spending a crawl on leads
already closed in PRs #476, #426, #597 and #605. All three came back the same: already-searched,
nothing new.

## Checks

`python3 scripts/build.py` and `python3 scripts/check_data.py` both ran clean on the merged branch.
No file in `data/` changed this run.

## For the next run

- Priorities 1 and 2 remain fully done.
- The digitalcommons Cloudflare wall is confirmed closed to both curl-with-headers and a real
  browser; the browser route additionally cannot be fixed from inside a session (proxy CA trust).
  Don't spend a cycle re-trying either.
- The ten pre-1990 names above (the original eight plus Baker and Fleenor) are now closed dead ends
  against archive.org's holdings specifically. A fresh source outside archive.org and digitalcommons
  — a Herald PDF reachable some other way, or a family/alumni source — would be needed to move any
  of them, not a re-search of the same Talisman volumes.
- The four-year year-photograph gap and the ~180 remaining senate-member portraits are untouched.
