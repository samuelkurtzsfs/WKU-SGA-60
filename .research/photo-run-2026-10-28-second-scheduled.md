# Photograph run, 28 October (second scheduled pass): both blocked routes retested unchanged, the Steve Wilson senior-portrait lead re-found and re-confirmed as already barred, and the officer gap confirmed to hold no untried name

## Priorities 1, 2 and 4, reconfirmed against the file before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait in `data/photos.json`. Unchanged.
- **Priority 2**: `python3 scripts/check_data.py` reports 61 years, 60 people have been president;
  every leader has a matching `data/photos.json` entry. No gap.
- **Priority 4**: every year still carries at least one photograph. The standing near-misses
  (1994-95, 2000-01) were not reopened this pass.
- **Priority 3** (officer/Senate gap): `python3 scripts/portrait_gap.py --any-year` reports 948
  officer slots, 188 with no portrait for that person in that year, 158 people, 156 with no
  portrait anywhere — unchanged from the first pass today.

## Network state, retested fresh

`digitalcommons.wku.edu/cgi/viewcontent.cgi`: Cloudflare 403 challenge, tested directly with the
navigation headers CLAUDE.md specifies. `web.archive.org`: `curl: (35) Recv failure: Connection
reset by peer` on a plain request. `archive.org` itself: open (HTTP 200 on `/metadata/...`).
All three unchanged from this morning's pass and from every pass this month.

## A near-duplicate of a mistake caught before it was made

Picked two names from the 1978-79 gap not touched by this morning's pass: Steve Wilson (Judicial
Council Chairman) and Alice Wicks (Secretary). Used `archive.org/metadata/talisman1979west` to get
the item's `server`/`dir`, then `fulltext/inside.php` to search the volume's OCR text directly
rather than downloading the whole `_djvu.txt` — the method logged in this morning's report.

Full-text search for "Steve Wilson" turned up a senior class portrait caption, "STEVE WILSON,
agriculture, Tompkinsville," at printed p. 379 (leaf 381, `talisman1979west$381`). Pulled the page
image, cropped the matching face, and before touching `data/photos.json` checked what the
back-of-book index says about him — the step that has caught every false surname-match on this
project. The index carries exactly one "Wilson, Steve Alan," at pp. 296, 318, 320, 336, with no
page in common with 379; a second volunteer senior on the same page, James Wimberley, confirms the
index does credit seniors with their portrait page (his entry reads "258, 379"), so the omission is
real and not a quirk of how the index is built. That is exactly the shape of evidence this project
has already weighed and rejected: `data/photo-finds/_do-not-use.json` (entries 87 and 99) already
bars this identical "Steve Wilson" senior-portrait finding, for the identical reason, twice —
including a 3 October 2026 withdrawal of this exact photograph after it briefly reached the site.
No file was added. The crop made this pass was discarded rather than committed.

Alice Wicks: the index carries "Wicks, Alice Elizabeth" with no page number, meaning no photograph
to turn to. Already recorded the same way in `data/photo-finds/_do-not-use.json`.

Both re-finds matched the barred reasoning independently rather than being read off the bar file
first, which is some confirmation the bar is sound rather than wasted caution.

## The officer gap has no untried name left in it

Built a script-driven check rather than relying on memory: pulled every name currently in
`portrait_gap.py --any-year`'s output (158 people), and grepped `.research/*.md` and
`data/photo-finds/_do-not-use.json` for each one. 156 of 158 matched a prior mention on a direct
string search; the 2 that did not (John (Jack) McKinney, Lane (Caroline) Simpson, both 2016-17/
2018-19 Associate Justices) turned out to be covered too, under "McKinney" and "Caroline Simpson"
respectively, once the parenthetical nicknames were dropped from the query. So: as of today, every
single name on the open officer-gap list has at least one prior, logged search attempt somewhere in
this project's history. This is worth recording explicitly so a future run does not spend a pass
rediscovering that fact — the honest next step for this list is re-trying an already-searched name
once a blocked route reopens (`viewcontent.cgi`, `web.archive.org`) or once enough time has passed
that a newly digitised source might answer differently, not hunting for a name nobody has tried.

## Conclusion

No new portrait landed. Both standing network blocks are unchanged. The one lead that looked new
(Steve Wilson's senior portrait) was independently re-derived and is in fact the project's own
best-documented false positive, caught before republication. `python3 scripts/build.py` and
`python3 scripts/check_data.py` both exit clean; the build-date-only diff in `site/` was reverted.
`data/photos.json` and `data/photos/` are unchanged from `origin/research-photos`. No push
notification: nothing actionable surfaced, and the blocked-route state was already reported to the
owner on 23 October. Landed on `research-photos`.
