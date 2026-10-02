# 2 October 2026, afternoon (photograph routine, scheduled)

## What was checked before doing anything

Same starting point as every run since 20 August, re-confirmed by reading the files directly:
Nick Todd, Katie Dawson, Jeanne Johnson and Reagan Gilley all still carry a portrait in
`data/photos.json`. All 73 top-level `leaders` records (every president and every student
regent) have one. 217 executive/Senate officer records still lack a portrait — the same 217
counted by both runs earlier today. 57 of 61 years have at least one year-scene photograph; the
four without one are 1994-95, 1995-96, 2000-01 and 2008-09, unchanged.

`research-photos` was already merged onto the current `origin/main` tip (`6f422942`) when this
run started; no conflict work was needed.

## Access re-tested again, nothing changed

- `cgi/viewcontent.cgi` still answers `200` on an ordinary item landing page (tested
  `dlsc_ua_records/7642`) but the PDF link itself is still the only `href` on the page and still
  resolves through the walled endpoint; a landing page carries no `og:image`, thumbnail, or any
  other image reachable without it. Checked the raw HTML specifically for an alternate image path
  this run (`/assets/md5images/*` hits are the site's own interface icons, not page scans).
- `web.archive.org` still resets mid-handshake (`ws_closed_mid_exchange` at the agent proxy).
  Tried `timetravel.mementoweb.org` as an alternate path into the same Wayback captures — its
  hostname does not resolve from this container at all, so it is not an open door either.

## New finding: the Talisman gap is a publishing gap, not an access gap

Every prior report in this file has treated the Talisman/officer-portrait hole in 1996-2011 as a
*retrieval* problem — `viewcontent.cgi` closed, `web.archive.org` closed, archive.org's own
digitised run stopping at 1986-87. This run checked whether the yearbook for those years exists
at all, independently of whether it can be fetched, and it mostly does not.

Three independent checks agree:

1. **digitalcommons.wku.edu's own OAI feed for the yearbook series**
   (`do/oai/?verb=ListRecords&metadataPrefix=document-export&set=publication:dlsc_ua_yearbooks`,
   156 records total) runs continuously 1898–1996, then nothing until a single 2003 volume, then
   nothing again until 2012, then continuously 2012–2025.
2. **This project's own local `data/herald-index-full.json`** already carries the full table of
   contents for every one of those volumes (117 `UA12/2/2`-prefixed items, no network request
   needed — this is the "search locally" rule paying off on a question nobody had put to it
   before). The same two gaps appear in it exactly: the last item before the first gap is
   `UA12/2/2 Xposure - Summer 1996` (1996-06-01, `dlsc_ua_records/424`); the only item inside the
   gap is `UA12/2/2 2003 Talisman: About Face` (2003-01-01, `dlsc_ua_records/594`); the next item
   after it is `UA12/2/2 Talisman, Vol. 83` (2012-01-01, `dlsc_ua_records/8897`).
3. **An open web search** independently confirms the Talisman "was not published" from roughly
   1995/96 to 2002, replaced for part of that span by *Xposure*, a quarterly features magazine,
   and again had a multi-year gap after the single 2003 "About Face" edition before resuming as an
   annual in 2012.

The 1995–96 replacement, *Xposure*, is itself fully indexed locally (six issues,
`dlsc_ua_records/419` through `424`) and its contents read as a general-interest features
magazine — tattoos, rave culture, dorm life, a "Portrait Gallery" of named students with no
office given — with nothing that names a student government officer or office in any issue's
table of contents. The single 2003 "About Face" Talisman's full 82-line contents (`dlsc_ua_records/594`)
likewise names no SGA officer or office; its closest institutional content is a two-page spread on
September 11 memorial events and the usual clubs/Greek-life/sports sections. Neither stand-in
publication fills the hole the missing Talismans left.

**This means the 217-record officer-portrait gap's concentration after 2003 (157 of 217, per the
1 October report) is not, for roughly fourteen of its eighteen years, waiting on `viewcontent.cgi`
to reopen.** For academic years 1996-97 through 2001-02 and 2003-04 through 2010-11, the yearbook
that would carry the portrait does not exist in this collection or, on the evidence of the gap in
its own publication history, anywhere — there was no Talisman printed for most of those years at
all. The four-year-photo gap's 2000-01 and the open half of 2008-09 both fall inside this same
hole, which is one more reason archive.org and `web.archive.org` have never produced anything for
them: the source itself is missing, not merely unreachable.

This does **not** close the other two live routes. `viewcontent.cgi` and `web.archive.org` are
still worth retrying cold on each future run for everything *outside* this hole — pre-1997
Talismans (1971-81 and 1986-87 already reachable via archive.org; 1898-1970 and 1987-96 reachable
only through `viewcontent.cgi`), the single 2003 and 2012-2025 volumes, and all pre-2002 Herald
issues for officers not pictured in any yearbook. It only means a future run should stop spending
time looking for a Talisman portrait specifically inside 1996-97 through 2001-02 or 2003-04
through 2010-11: for those years, *wkuherald.com* (where it reaches, 2002 on) and `wku.edu/news`
are the only possible photographic sources left, and both have already been swept hard by the
last several reports in this file.

## A full local cross-check of the 217 names, against the whole index rather than just Herald headlines

Built the 217-record officer-portrait gap list fresh from `data/years.json` against
`data/photos.json` (same 217 both runs today already found) and grepped every name, in full,
against all 141,079 lines of `data/herald-index-full.json` — not only the `UA12/2/1` Herald
items the routine normally searches, but every `UA12/2/2` Talisman/Xposure entry and everything
else in the archive, in one pass, to catch a hit this routine's narrower Herald-only searches
might have missed.

Nineteen names returned a hit. All nineteen were read in context, not taken on the strength of
the grep alone, because this index holds *headlines*, not captions — a name in it proves an
article exists, never that a photograph does. None of the nineteen is usable:

- Several are a different person of the same name (Pat Smith in a 1934 feature; John Holland
  matching "John Hollander" the poet; David Smith matching a football player; Mark Clark matching
  a football coach; Jason Heflin matching a 2015 brewery story) — the surname-and-first-name match
  still needs the office or year to line up, and for these it does not.
- Several are the officer themselves but the hit is a plain news headline with no indication of
  an accompanying photograph, in an issue this project cannot currently open to check (Paul Gerard,
  David Bass, David Young, Alice Wicks, Steve Wilson, Connie Hoffmann, Matthew Pava, Lisa Kappler,
  Corey Bewley, Cody Cox) — David Bass's is already on file as the confirmed 1977-78 group photo,
  per the 1 October report; the rest point at a specific Herald issue worth opening once
  `viewcontent.cgi` reopens, but none can be confirmed today.
- Three (Jenna Haugen, Jessica Williams, Mallory Treece) hit an issue already inside
  `wkuherald.com`'s reach or the 2013-14 Talisman; none of the three headlines is a captioned
  photograph of the person — Haugen's and Treece's were re-checked directly against
  `wkuherald.com` and the archive's own record of the Talisman hit respectively, and Treece's is a
  single name in a group byline list ("Stories to Tell"), not a caption naming her in a photograph.
- Mike McDaniel's hit is a byline, not a photograph of him.

Nothing added. This confirms the local index has already been searched as thoroughly as it can be
for this gap list without becoming a fishing expedition on bare-surname matches, which the
project's own traps section (`SGA-60-AGENT-INFO.md` §6.4) warns against by name.

## Nothing added

No file in `data/photos.json` or `data/photos/` changed this run. `python3 scripts/build.py` and
`python3 scripts/check_data.py` both run clean against the unmodified tree (61 years, all 73
leader portraits present, 217 officer portraits still open, the same four years without a scene
photograph).

## For the next run

Stop re-trying the Talisman route specifically for 1996-97 through 2001-02 and 2003-04 through
2010-11 — the yearbook was not published for most of those years, confirmed three independent
ways above, so no amount of `viewcontent.cgi` or `web.archive.org` access will ever produce one
for them. Keep retrying both routes cold for every year outside that hole, and for pre-2002
Herald issues generally, since they have reopened briefly before without warning. The 217-name
gap list is now exhausted against both `wkuherald.com` (as of 2 October morning) and the complete
local index (this run); a future run with a reopened `viewcontent.cgi` should go straight to
fetching known leads (the ten-plus specific Herald issue numbers named above and in the 1 October
reports) rather than re-searching for new ones.
