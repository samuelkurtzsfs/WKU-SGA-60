# Photograph run, 27 October (second scheduled pass): a wider wkuherald per-name sweep on names the first pass today hadn't covered, a near-miss caught before it became a duplicate, a wku.edu/news search route tried and found to be client-rendered

## Priorities 1, 2 and 4, reconfirmed directly against the file before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait in `data/photos.json`. Unchanged.
- **Priority 2**: `python3 scripts/check_data.py` reports 61 years, 60 people have been president,
  archive checks out against its own rules. No missing leader portrait.
- **Priority 4**: unchanged; every year still carries at least one photograph. The two standing
  year-photo near-misses (1994-95, 2000-01) were not reopened this pass.
- **Priority 3** (officer/Senate gap): `scripts/portrait_gap.py --any-year` reports 948 officer
  slots, 188 with no portrait for that person in that year, 158 people, 156 with no portrait
  anywhere. Unchanged from this morning's first pass.

## Network state, retested fresh

Identical to this morning's first pass: `cgi/viewcontent.cgi` still a Cloudflare 403 challenge;
`web.archive.org` still `curl: (35) Recv failure: Connection reset by peer`; plain `archive.org`
still open (200 after redirect, same 19 `talisman*west` identifiers, nothing new); `wkuherald.com`
still open.

## A near-miss: Carter Smith looked like a new find, was already on file, caught before it became a duplicate

Read `scripts/portrait_gap.py`'s own doc string this time before trusting its list by eye: a name
printed **without** the `(no portrait in any year)` suffix has a portrait somewhere, just not in
the year printed. The list's last line, "2025-26 Freshman Senator: Carter Smith", has no such
suffix - a difference this pass almost missed reading quickly, the exact mistake the 3 October
note about Keith Coffman warns against. Went looking anyway (see below), found a clean portrait,
and only discovered via `check_data.py` flagging a hard duplicate (same name, same year, two
entries) that `data/photos.json` already carries him, added 15 October from the identical Herald
article: `data/photos/2026-27-carter-smith.jpg`, captioned "WKU Student Government Association
Sophomore Senator Carter Smith gets sworn in to be a sophomore senator... Tuesday, Sept. 22, 2026,"
sourced to `wkuherald.com/97612/...bus-tracking-resolution/`. Reverted cleanly: removed the
duplicate `leaders` entry, restored `site/` and the (already-identical) image file with `git
checkout`, confirmed `git status` and `git diff --stat` both empty against `origin/research-photos`
before doing anything else. **No net change from this episode** - logged here so the next pass
reads the `--any-year` suffix correctly and doesn't repeat it a third time.

## A wkuherald.com per-name sweep extended to names the first pass today hadn't covered

The first pass today (see the note above this one) swept 20 names from the 2016-17 through
2021-22 slice of the gap list by querying wkuherald's WP-JSON search per name with `_embed=1`,
checking each hit's embedded featured-media caption and in-content `<figcaption>`/`<img alt>` text
for the person's own name. This pass ran the same method on the 27 names from that gap list the
first pass had not touched, spanning 2016-17 through 2025-26: Hayden Skinner-Fine, Jack McKinney,
Caroline Simpson, Abhishek Bose, Helen Vickrey, Luke Edmunds, Chase Coffey, Mark Clark, Smita
Peter, Lucas Knight, Matthew Johnson, Hope Wells, Jillian Kenney, Nicole Massarone, Tribhuwan
Singh, Jesse Banales, Danny Vuleta, Neel Patel, ShyAnte'e Williams, Reed Hensley, Brooke Mitchell,
Kayla Distler, Connor Ferguson, Elizabeth Gannon, David Darnell, Callison Padgett, Tyreesha Morris
(Carter Smith, the 28th name on the list, is the near-miss above and was not a real gap).

Several names returned posts whose text happened to contain the surname as a substring of someone
else's name or a place name ("Clark" inside "Clarksville," "Johnson" as part of a football
player's name, "Smith" as part of someone else's name) or an image that is not a photograph of a
person at all (Kayla Distler's hit is a screenshot of a petition document, not a picture of her).
Every hit was opened and read against its actual content, not trusted on the substring match
alone; none held a captioned photograph of the named person. Zero of the 27 produced a usable
portrait. Consistent with every per-name sweep this gap has had since September: these
committee-chair- and senator-level roles are covered by wkuherald in running text, not by
captioned photographs, far more often than not.

## wku.edu's live news search tried directly, and found to be the same kind of dead end as the SGA CMS pages

CLAUDE.md's source list names `wku.edu/news` as a route for recent decades, alongside
`wkuherald.com`, so tried it directly rather than assuming the 27 October (first pass) finding
about `wku.edu/sga`'s stale CMS pages extends to it. `https://www.wku.edu/news/?s=SGA` redirects
(301) to `https://www.wku.edu/news/articles/?s=SGA`, which returns a clean `200` - but the saved
HTML carries zero occurrences of "sga" anywhere in the document, only the site's standard
navigation chrome. The search results are rendered client-side (JavaScript), so a plain fetch
never sees them. This is the same shape of dead end the first pass found on the `wku.edu/sga`
legacy pages, just reached a different way: not a route this archive's tools (`curl`, `WebFetch`)
can use without a real browser. Nothing to add; ruling this out is the finding.

## Conclusion

No new portrait landed this pass, and the one photograph this pass's own search turned up
(Carter Smith) was already on file - caught and reverted cleanly rather than duplicated. Both
standing network blocks are confirmed still closed. The wkuherald per-name method has now swept
all 48 names in the 2016-17 through 2025-26 slice of the officer gap list across this pass and the
one before it today, with zero portraits found in total; a future pass working this gap should
look to a different source (the Talisman, where TopSCHOLAR's own landing pages carry no digitized
volume past 2003 per the 3 October catalog-mapping note, or whatever opens on `viewcontent.cgi` or
`web.archive.org` next) rather than re-running this same WP-JSON search a third time. `python3
scripts/build.py` and `python3 scripts/check_data.py` both exit clean; `data/photos.json` and
`data/photos/` are unchanged from `origin/research-photos`. This run's only output is this note.
Landed on `research-photos`.
