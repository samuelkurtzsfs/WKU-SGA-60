# Photograph run, 16 October (fourth scheduled pass): the gap re-walked for names no report had tried, all of them closed

## Priorities 1, 2 and 4: reconfirmed before anything else

Checked `data/photos.json` against `data/years.json` directly, per CLAUDE.md's "check whether
an earlier run already got them," before spending any time searching:

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry
  a portrait entry.
- **Priority 2** (every other president or student regent): a direct comparison of every
  `leaders` entry in `data/years.json` against `(name, year)` pairs in `data/photos.json` found
  zero gaps — every leader in every year already has a portrait for that year.
- **Priority 4** (years with no photograph): zero years missing from `photos.json`'s `years`
  array.

Nothing to do on any of the three; both are unchanged from the three earlier passes today.

## Priority 3: found the thirteen names no report had logged, worked them, nothing survived

`python3 scripts/portrait_gap.py --list` reports the same figure as the three earlier passes
today: 189 officer slots, 159 people, 157 with no portrait anywhere. Rather than re-pick names at
random from that list and risk re-walking ground already covered, this pass wrote a short script
to diff the full 189-slot list against the text of all 90 prior `.research/photo-run-*.md`
reports and surface only the names that had never been typed into any of them. Thirteen such
names existed:

- 1994-95 Bonnie Newton (Chairperson, Student Affairs Committee)
- 1995-96 Terra Swanson (Chairperson, Academic Affairs Committee)
- 1996-97 Andy Gailor (Chairperson, Legislative Research Committee)
- 1996-97 Kip Carr (Chairperson, Technology Committee)
- 1997-98 Andy Gailor and Anne Guillory (Chairperson, Legislative Research Committee — the office
  changed hands mid-list in the data, both recorded)
- 1997-98 Anne Guillory (Chairperson, Constitutional Review Committee)
- 1998-99 Matt Bogard (Chairperson, Campus Improvements Committee)
- 1998-99 Joe Murrell (Sergeant of Arms)
- 2004-05 Blake Napper (Co-Chair, Campus Improvements Committee)
- 2004-05 Tim Howard (Co-Chair, Student Affairs Committee)
- 2007-08 Cory Gerald (Associate Justice, Judicial Council)
- 2022-23 ShyAnte'e Williams (Graduate Student Senator) — the name-matching script missed this
  one on a first pass over an apostrophe-character mismatch; the 16 October second pass had
  already logged it as open (a 403 interrupted a wkuherald.com lookup), so it is not actually new,
  and is folded into this pass's retry below rather than treated as untried.

### 1994-99 names: no open route this session

All eight of the 1994-99 names fall in the gap the Talisman yearbooks on `archive.org` do not
cover — that holding is still 1971-1981, 1986 and 1987 only, confirmed again this pass by
requesting `archive.org/metadata/talisman1994west` through `talisman1999west` directly: every one
came back with an empty `files` list. The only other route to a 1990s Talisman page image is
TopSCHOLAR's own PDF viewer, and that remains closed: `digitalcommons.wku.edu/cgi/viewcontent.cgi`
and `do/search` both returned Cloudflare's "Just a moment..." challenge page on HTTP 403 when
tested directly this session, the same block every pass has hit since 13 October. Plain item
*landing* pages on the same host are not behind that wall — `dlsc_ua_records/4686/` answered 200
directly — but a Talisman landing page carries no page-by-page index, so it gives no way to reach
a specific person's portrait without the PDF itself. wkuherald.com's archive does not reach back
this far; its earliest indexed post found in this or any prior pass is from 2013. No file was
downloaded and no entry was added for any of these eight.

### 2004-05 and 2007-08 names: checked against wkuherald.com, same result

Searched `wkuherald.com`'s `wp-json/wp/v2/posts` endpoint for Blake Napper, Tim Howard and Cory
Gerald directly. Tim Howard and Cory Gerald returned no posts earlier than 2013 — consistent with
the finding above that the site's indexed archive does not reach 2004-08 at all. Blake Napper
returned one hit, but from February 2003: "Student's not in love with Cupid," a Valentine's Day
vox-pop piece quoting a Louisville freshman named Blake Napper on why he dislikes the holiday. A
freshman in February 2003 would be entering his junior year by 2004-05, so the name is plausibly
the same person who later co-chaired Campus Improvements — but the article is unrelated to SGA,
carries no photograph (`wp-json/wp/v2/media?parent=57154` returns an empty list), and even a
confirmed identity would have no image to attach. No file was downloaded and no entry was added.

### ShyAnte'e Williams: retried, genuinely zero hits this time

The 16 October second pass left this name open rather than closed, after a `wp-json` lookup
403'd mid-check. Retried this pass with the special character stripped from the query
(`ShyAntee`) rather than the literal name, since an apostrophe can break a WordPress search term
outright: the request returned HTTP 200 with an empty result array, not a block. Genuinely zero
posts on `wkuherald.com` mention her under any spelling this pass tried. Closing this one as
checked-and-empty rather than leaving it open on an old network error.

## Network state, retested fresh this session

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` and `do/search`: both 403, Cloudflare challenge
  page, same as every pass since 13 October. Plain TopSCHOLAR item landing pages (no `cgi/` in
  the path) are not behind this wall and answered 200 directly.
- `archive.org` (not `web.archive.org`): open. Talisman holdings confirmed unchanged —
  1971-1981, 1986, 1987 — by requesting the 1994-1999 identifiers directly and getting empty
  metadata for each.
- `web.archive.org`: closed to this session outright — both a direct `curl` to its CDX API and a
  `WebFetch` call were refused before reaching the host. Earlier reports this week reached it
  successfully and warn the block is intermittent and container-dependent rather than a settled
  fact; this session's tools could not reach it at all, so the Wayback route into the old
  `wku.edu/Dept/Org/Student/SGA` officer pages was unavailable this pass regardless.
- `wkuherald.com`: open, with the same 403-then-clear-on-retry rate limiting prior passes
  describe.

## A caution for whoever reads this next

Before searching, this pass also spent time independently re-confirming four names already
logged as exhausted in `.research/photo-run-2026-10-14-*.md` (David Bass, David Young, Alice
Wicks, Mark Chesnut) using the exact same `archive.org` Talisman route those reports already
walked, down to fetching the same page images, before noticing the prior reports and the
diff script described above. That work reached the same dead ends the 13-14 October passes
already recorded and added nothing new. **Grep `.research/photo-run-*.md` for a name before
spending time on it** — with 90-plus reports now on file, a name search of the existing reports
is faster than re-deriving the same negative result, and it is the only way to find the small,
shrinking set of names, like the thirteen above, that genuinely have not been tried.

## What is still open

The 189-slot gap is unchanged in count after this pass, as it has been for several days running.
Every name checked this pass — the twelve genuinely untried ones, plus the retried ShyAnte'e
Williams — stayed open for lack of a reachable source or a captioned image, not for lack of
searching. The structural blockers are unchanged from the three earlier passes today:
`cgi/viewcontent.cgi` is still the only route into 1990s Talisman pages and it is still closed;
`web.archive.org` was additionally unreachable this specific session. Xavier Spiess's withheld
portrait (identified 15 October, needs a `years.json` roster entry this agent's scope does not
cover) is still waiting on whoever next edits that year's organization data.

## Checks

`python3 scripts/build.py` then `python3 scripts/check_data.py`: 61 years, clean, 60 presidents,
no missing leader portrait, no year without a photograph, 1,111 legislation files all present and
real PDFs. No file in `data/photos/` or entry in `data/photos.json` changed this pass. Merged
`origin/main` into `research-photos` first (clean merge, no conflict).
