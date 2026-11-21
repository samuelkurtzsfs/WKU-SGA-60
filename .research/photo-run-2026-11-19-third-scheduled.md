# Photograph run, 19 November (third scheduled pass): the WKU Archives SGA finding aid opened — uncaptioned, no usable faces

## Baseline reconfirmed before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- **Priority 2**: checked programmatically against the whole file — every president and every
  student regent in `data/years.json` has a portrait. Zero missing.
- **Priority 4**: all 61 years carry at least one `years`-level photograph entry.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` is unchanged from this morning's two
  passes — 187 cabinet/Senate leadership slots with no same-year portrait, 155 people with no
  portrait anywhere in the file. Every name has a documented dead end in `data/photo-finds/`.

## What this pass opened that no prior pass had

`data/photo-finds/_topscholar-wanted.json` item 15 — the WKU Archives' own dedicated SGA
photograph finding aid, `dlsc_ua_fin_aid/620` ("UA1C4/10 Student Government Association
Photos") — has sat as an open, never-fetched lead since 24 August. `viewcontent.cgi` answered
the urllib cookie-jar bypass (visit the landing page to set a session cookie, then request
`viewcontent.cgi?article=1619&context=dlsc_ua_fin_aid` with a `Referer` pointing back at the
landing page) directly this pass: 200, a genuine five-page PDF (confirmed by the `%PDF-` magic
bytes before trusting it).

It is a container-list inventory, not a photo gallery: nine physical folders (PC F334, F247,
F320, F322, F323, F4167 through F4170) each list the names and subjects the folder's prints and
negatives cover, with no scanned images and no links — except three folders (F4167-F4169) noted
as "Images removed from photo album D7390," with that album's own digitized URL,
`digitalcommons.wku.edu/sga/Documents/Reports/164`.

Followed that link. It is "Student Government Association: Photo Album," described on its own
landing page as "events sponsored by the Student Government Association over the 1967-1968
school year... concerts, dances, lectures and the Miss Western pageant" — viewcontent article
2817, context `sga`. Fetched the whole thing (71 pages, 25.0 MB) through the same bypass.
Rendered the first 20 pages at 100 dpi and read them directly rather than trust a text layer: there
isn't one, on any of the 71 pages, confirmed with PyMuPDF's `get_text()` across the entire PDF.
The pages are loose scrapbook snapshots — a crowd dancing, a band in silhouette, a trumpet player
— with no printed caption, name or label anywhere. This matches the finding aid's own subject
list for these folders (dance parties, musicians, bands, Miss Western pageant) exactly: it is
party photography, not officer portraiture, and CLAUDE.md's rule against identifying anyone
without a caption rules every face in it out on sight, with no need to render the remaining 51
pages to know that.

Checked this against the open 1966-67/1967-68 gaps it might have closed — Carla Dotson, Patricia
Lanning, Pat Smith (Campus Wide Representative At Large, Panhellenic Representative,
Representative of Women's Residence Halls, 1966-67) and Mike McDaniel (Campus Representative At
Large, 1967-68). All four are already closed dead ends as of 10 November
(`1966-1970-notes.json`), checked against the 1967 and 1968 Talisman group photographs and every
committee photograph on their facing pages; nothing in this uncaptioned party album could have
reopened them even if it had happened to show the right year, since there is nothing in it to
read a name from. 1967-68 also already carries a `years`-level photograph
(`1967-68-associated-students.jpg`, 1968 Talisman p. 153), so this was not needed there either.

Recorded the resolution directly in `_topscholar-wanted.json` item 15 so no future pass re-opens
either the finding aid or the photo album expecting new ground.

## Also checked

`digitalcommons.wku.edu` answered plain requests without a 403 for the whole window this pass
(no backoff needed). Re-ran `python3 scripts/portrait_gap.py --any-year` against the current
tree before and after the above to confirm the gap count genuinely didn't move.

## Conclusion

No new portrait. One long-open lead (the WKU Archives' own SGA photograph finding aid, and the
1967-68 photo album it pointed to) is now closed with a documented reason rather than sitting
open indefinitely. `python3 scripts/build.py` and `python3 scripts/check_data.py` both pass
clean. Landed on `research-photos`.
