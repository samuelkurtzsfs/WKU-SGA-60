# Photograph run, 27 November (scheduled): baseline reconfirmed, no new portrait

## Priority order, checked programmatically against the live data

- The four presidents named as having no portrait at all (Nick Todd, Katie Dawson, Jeanne
  Johnson, Reagan Gilley) already carry a captioned `leaders` entry in `data/photos.json`.
- Every president and student regent in `data/years.json` has a portrait: zero missing of either
  role, checked against the whole file.
- All 61 years carry at least one photograph (a `years` or a `leaders` entry).
- 40 years still have executive-cabinet or Senate-officer gaps, concentrated 1997-2026.

## What this pass tried that was genuinely checked fresh

**The 2025-26 Senate's four still-unphotographed names** (Miles Harvey, Zoe Martin, Tyreesha
Morris, Nolan Rongey — Senators at Large bar Morris, First Generation Senator) were searched
directly against `wkuherald.com`'s own media library (`/wp-json/wp/v2/media?search=`), not just
its post text, on the theory that a name absent from an article's words could still be present in
a photo caption the search-by-post-text method would miss. All four returned zero media results.
The spring-election-results article that names all three Senate recruits together (Martin,
Harvey, Rongey, `wkuherald.com/83881`) carries exactly one captioned photograph, of Mahurin Honors
College Senator-elect Chin Lun, who already has a portrait; the rest of the piece is a bare name
list. The autumn committee-chairs article naming Tyreesha Morris as the new Mental Health and
Well-Being Committee chair (`wkuherald.com/96580`) likewise carries one captioned photograph, of
President Caden Lucas, already on file. Both confirm the pattern CLAUDE.md warns about: a name in
running text is not a name under a photograph.

**Re-derived the archive.org Talisman page-image route independently, then cross-checked it
against this branch's own record.** Without first reading `.research/` or `data/photo-finds/`,
tested network access cold and found `archive.org/download/<id>/<id>.pdf` (the full scanned
volume, not just the djvu text) serves at 200 for every Talisman year it holds (1971-1981, 1986,
1987), where `digitalcommons.wku.edu/cgi/viewcontent.cgi` is still a flat 403 and
`web.archive.org` still resets the connection at the egress proxy. Used this to look at the actual
pages behind the back-index page numbers for seven names still on the officer-gap list: Vern
Pulman (1974-75), David Young, Alice Wicks, Steve Wilson (1978-79), Mark Chesnut (1980-81), and
Chris Millay, Dwight Austin (1986-87). None turned up a photograph captioned with the right name
and office. Reading `data/photo-finds/_do-not-use.json` afterward, all seven are already recorded
there with the identical conclusion (Chesnut's "page 234" is the men's intramural champions list,
misspelled "Chestnut"; Young is quoted in the 1979 ASG spread's body text but not pictured; and so
on) — independent corroboration of an already-closed lead, not a new one. The route itself is
already documented as open in `.research/photo-run-2026-10-29-scheduled.md` and used to the same
effect on 18 November; this pass adds nothing to that finding beyond reconfirming it still holds.

## Network gates, retested cold

- `digitalcommons.wku.edu` landing pages: open (200/301).
- `cgi/viewcontent.cgi` (PDF download route): closed (403), with full navigation headers sent.
- `archive.org/download/.../<id>_djvu.txt` and `.../<id>.pdf`: open (200). The djvu text times out
  on the largest volumes under a 30s client timeout but completes at 90s; the full PDF is ~100MB
  and needs a long timeout or a background fetch.
- `web.archive.org`: closed, TLS reset at the egress proxy.
- `wkuherald.com` WordPress API (posts and media): open.
- `wku.edu/sga/executive/index.php`: open, but shows only the *current* cabinet (now 2026-27);
  it had already rotated past 2025-26 by the time of this check, and nothing on it was new —
  Caden Lucas, Jakob Barker, Will Derryberry, Gabi Pace and Cayden Bailey are all already on file.
- `www.wku.edu/news/articles/?s=` does not actually filter by query on this CMS; it returns the
  same recent-articles list regardless of the search term. Not a usable route.

## Unchanged

`data/photos.json` and `data/photos/` are unchanged this pass; only this note was added. Build
and `check_data.py` both run clean.

Two items already on record still need a person rather than another automated run:
`data/photo-finds/_for-the-editor.md` carries 13 people and 14 photograph entries, open since
8 September 2026, each needing a yes/no identification call that no further research can make.
