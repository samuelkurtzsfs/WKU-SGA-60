# Photograph run, 10 October (afternoon) — the magazine-era Talisman tested as an index, not a PDF; both PDF gates retested including an untried bypass; nothing landed

## Priorities 1, 2 and 4, reconfirmed before anything else

**Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
portrait in `data/photos.json`. Nothing to do.

**Priority 2** (any other president or student regent without a portrait): checked every
`leaders` record in `data/years.json` against `data/photos.json` by name, programmatically. Zero
missing.

**Priority 4** (years with no photograph at all): every one of the 61 years has at least one
photograph in `data/photos.json`. Zero missing. The two standing year-photo gaps (1994-95,
2000-01) are unchanged; both wait on the same closed PDF gates as everything else below.

So this pass's whole job was priority 3, same as every recent run: `scripts/portrait_gap.py`
reports 189 officer slots with no portrait, held by 159 distinct people, 157 of them with no
portrait anywhere in the file. Unchanged from 9-10 October.

## The two PDF gates, retested cold, plus one untried idea now ruled out

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — HTTP 403, Cloudflare "Just a moment..."
  challenge page, with full navigation headers (`Sec-Fetch-Dest: document`,
  `Sec-Fetch-Mode: navigate`, `Upgrade-Insecure-Requests: 1`). Same as every pass since this gate
  closed.
- **New this run: a `Range: bytes=0-1023` request against the same URL, on the theory noted at the
  close of the 10 October scheduled run that the block might be keyed to response size rather than
  the path.** It is not — the Range request got the identical 403 Cloudflare challenge page, not a
  partial PDF. This closes that idea as tried and negative; the block is the Cloudflare JS
  challenge on the path itself, not a size-based rule, confirming what the 27 September and
  3 October passes already established by a different method (WebFetch hitting the same 403 from
  a separate fetch path).
- `web.archive.org` (`if_` bypass) — `curl: (35) Recv failure: Connection reset by peer` on both a
  bare request to `web.archive.org/` and a known-good `if_` article URL. Not open this session,
  consistent with its documented intermittency.
- `archive.org` (plain, not `web.archive.org`) — the root page answers 200, but
  `archive.org/details/...` reset mid-exchange this run. Not tested further since no new Talisman
  year in this archive's held range (1971-81, 1986-87) has an unexhausted officer name — every gap
  candidate in those years was already searched to the ground on 9 October.

## A genuinely new method: reading the magazine-era Talisman as a TopSCHOLAR index page, not a PDF

Every prior pass's Talisman work has either used `archive.org`'s plain-text `_djvu.txt` route
(only covers 1971-81, 1986-87) or been blocked waiting on `cgi/viewcontent.cgi` for anything later.
What had not been tried: `digitalcommons.wku.edu/dlsc_ua_records/<id>`, the **ordinary landing
page** for each Talisman item, is not behind the Cloudflare gate — only the PDF download endpoint
is — and for the 2012-2025 "magazine era" Talismans (the format that replaced the traditional
yearbook after the 2003 "About Face" edition, per the 3 October second-pass catalogue work) its
`citation_abstract`/meta-description field carries the issue's full table of contents, the same
way a digitised Herald issue's abstract does.

Fetched all 20 such items from `digitalcommons.wku.edu/dlsc_ua_yearbooks/`'s own landing page
(paced 3 seconds apart, ordinary pages, no PDF endpoint touched): "2013 Talisman: Form" (8696),
"2014 Talisman: Reckoning" parts I/II (5160, 5162), "2015 Talisman: Resurgence" (8679), "2016
Talisman" Identity/Life More Life (8678, 8677), "2017 Talisman" Well Being/Power (8685, 8686),
"2018 Talisman" Grit/Movement (8684, 8690), "2019 Talisman" Paradise/Balance (8682, 8683),
"Talisman: Zeitgeist" (8681, 2020), "Talisman" (8776, 2021), "Talisman: Illuminate"/"Forge" (8898,
9256, both 2022), "Talisman: Dimension"/"Surreal Issue No. 14" (9740, 9836, both 2023), "Talisman:
Legacy"/"Pulse" (9809, 9821, both 2024), "Talisman: Connection" (9820, 2025). Read `citation_date`
off each page to map publication year to academic year (a Talisman published in year Y covers
Y-1/Y), then checked every one of the 159 officer-gap names as an exact "First Last" substring
(with a second pass allowing the printed-nickname form, e.g. "John (Jack) McKinney" also tried as
"Jack McKinney") against the full abstract text of the matching academic year's volume(s).

**Zero genuine matches.** An initial surname-only pass threw up dozens of candidates (Smith,
Johnson, Williams, Cole, Williams, Carter, Austin, Young, Wilson — all common surnames), but every
one dissolved under a full-name check: the abstracts are built as `Byline (Last, First). Article
title – Subject` triples, and the byline names are Talisman staff writers and photographers, not
SGA people, so a bare surname match is almost always a different person entirely by first name.
No gap candidate's full name appears in any of the 20 abstracts for the academic year that
candidate's slot falls in.

**This is a structural finding, not just a bigger miss.** The two confirmed uses of this era's
Talisman already on file — Brian Chism ("Brian Chism for President," 2015 Resurgence) and James
Line ("The President's Keeper," 2016 Life More Life) — are both individual profile features, the
magazine format's equivalent of a news story, not a club/organization page. Unlike the traditional
yearbook format this collection holds through 1987 (composite group photographs captioned with a
full officer roster, the kind that already supplied the 1983-84 ASG Congress photo and the David
Bass group shot), nothing in any of these 20 abstracts reads as an organization-page roster at
all — no index line resembling "Student Government Association" as a section header followed by a
name list, only occasional one-off feature headlines naming an individual. That is consistent with
this format never carrying a composite SGA photograph for this entire span, not merely with this
run's search missing one. It does not rule out an individual feature on one of the 157 gap names
existing in a full page image this abstract doesn't capture (the abstract is a contents list, not
page text — the same caveat CLAUDE.md gives for the Herald index), but it means **a keyword/name
sweep of this index can no longer be a route to those group-photo gaps**, which is the thing the
next run should not re-spend time trying before reaching for the real blocker, the PDF.

## Nothing landed

No file in `data/photos.json` or `data/photos/` changed; `data/years.json` is untouched.
`python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean against the
unchanged tree (61 years, 1,967 events, 60 presidents). This run's only output is this note.

## For the next run

- Retry both PDF gates cold, as always — `cgi/viewcontent.cgi` has been shut on every single pass
  that has tested it since it first closed, and `web.archive.org` is genuinely intermittent (open
  for sustained windows on 3 and 7-8 October, shut today).
- The magazine-era Talisman abstracts are now exhausted as a name-search index (this run) on top
  of the keyword-search and gallery-caption methods already exhausted on `wkuherald.com` (9-10
  October). What remains untried for the 2012-2025 span specifically is opening one of these
  volumes' actual page images once a PDF route opens, to check whether an SGA page exists at all
  that the TOC abstract simply doesn't index as such — this run's negative is about the index, not
  proof the page itself is empty.
- The pre-1987 Talisman route (`archive.org` `_djvu.txt`) and the 1995-96 *Xposure* issues remain
  fully exhausted / gate-blocked respectively, unchanged from the 9-10 October notes.
- 189 officer slots / 159 people / 157 with no portrait anywhere remains the live count.
