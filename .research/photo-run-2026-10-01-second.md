# 1 October 2026 (photograph routine, second scheduled run)

## What was checked before doing anything

Same starting point as every run since 20 August: the four named priority portraits — Nick Todd,
Katie Dawson, Jeanne Johnson, Reagan Gilley — already carry a portrait in `data/photos.json`. All 73
top-level `leaders` records (every president and every student regent) have a portrait. 57 of 61
years have at least one year-scene photograph; the four without one are 1994-95, 1995-96, 2000-01
and 2008-09, unchanged. 217 executive/Senate officer records still lack a portrait.

## Access re-tested, nothing changed

- `cgi/viewcontent.cgi` still `403`, Cloudflare challenge. Item landing pages (`dlsc_ua_records/*`)
  still a clean `200` — only the PDF endpoint is walled.
- `web.archive.org` still resets at the TLS handshake.
- `wkuherald.com`'s WordPress REST API answers normally (`200`).

## wkuherald.com: the bulk-pull variant the last run proposed, carried out

The 1 October (scheduled) report's own suggestion — pull every SGA-tagged post's `content.rendered`
in bulk and scan for in-body `<img>`/`<figcaption>` pairs, instead of one `search=` query per missing
name — was tried this run. The `sga` tag (id 3300) carries 122 posts, 2010-10-06 to 2026-09-29,
fetched in two pages with `_fields=id,date,link,title,content`. Scanning every `<figure>...</figure>`
block's caption and image-alt text against the full list of officers without a portrait produced 126
name/caption matches across 50 posts with images.

Cross-checked against `data/photos.json` by (year, name) pair rather than by name alone — matching
by name alone is wrong here, since a returning officer's photo entry is filed against one specific
year and does not cover every year they served (`apply_photo_overlay` in `build.py` only attaches a
portrait to the year named in the overlay entry). Of the 126 hits, every single one was already on
file: the images and their exact captions match existing `data/photos.json` entries byte for byte.
This bulk pull is the right method, as the prior report judged, but it turns out the project's recent
decade has already been swept this way — the 217 open slots are not hiding in this tag's postings.

The only names in the post-2024 window genuinely still open are five 2025-26 senators who appear in
body text (an election-results roundup, a committee-swearing-in story) but never inside a captioned
`<figure>`: Miles Harvey, Zoe Martin, Tyreesha Morris, Nolan Rongey, Carter Smith. No image in any
post mentioning them is captioned with their name, so none is usable under the "never use a photo
whose subject you cannot confirm" rule.

## A new route into the archive.org Talisman years — tried, and it works, but found nothing new

Archive.org's book reader exposes two endpoints beyond the `_djvu.txt` full text already in use:

- `https://{server}/fulltext/inside.php?item_id=...&doc=...&path=...&q="phrase"` — the search-inside
  API, which returns the matching leaf number and the bounding box of the hit on that page image.
- `https://{server}/BookReader/BookReaderImages.php?zip=.../{id}_jp2.zip&file={id}_jp2/{id}_NNNN.jp2&id={id}&scale=2` —
  pulls a single page as a real JPEG straight out of the multi-hundred-megabyte `_jp2.zip`, without
  downloading the zip itself.

Both answered cleanly and are not rate-limited the way TopSCHOLAR is — tested against
`talisman1978west` and `talisman1979west`, one request each, no 403. This means the 1971-1981,
1986-87 Talisman window archive.org already holds is not limited to full-text search the way prior
reports treated it: an actual page image can be pulled for any confirmed caption, for every volume
in that window, without touching TopSCHOLAR at all. Worth keeping on record for the next run working
that decade, since it was not mentioned in the chain of reports leading up to this one.

Used it against the eight remaining officer gaps that fall inside this window (1974-75 Vern Pulman;
1977-78 David Bass; 1978-79 David Young, Alice Wicks, Steve Wilson; 1980-81 Mark Chesnut; 1986-87
Chris Millay, Dwight Austin). Result: nothing addable.

- **David Bass** (1977-78 activities vice president) is named in a photo caption on p. 34 of the 1978
  *Talisman* (leaf 38 via search-inside) — but the caption names four people in one group shot
  ("laughter from president Bob Moore and smiles from activities vice president David Bass, secretary
  Sharon May and vice president Cathy Murphy") with no left-to-right or other positional key, and the
  photo shows three or four indistinguishable faces. This is already in `data/photos.json` as the
  1977-78 year photo `1977-78-asg-meeting.jpg`, captioned with the same quote — a prior run already
  found and correctly filed it as a group photo rather than a mis-attributed individual portrait.
  Confirms that decision rather than adding anything.
- **David Young** (1978-79 administrative vice president) appears only in running text on p. 289
  ("David Young, administrative vice president, said this was done to 'force some heads-up
  competition'...") on a page with two unrelated photos (faculty evaluation forms, discarded ASG
  newsletters) — no picture of him exists on the page.
- **Vern Pulman**, **Alice Wicks**, **Steve Wilson**, **Mark Chesnut**, **Chris Millay**, **Dwight
  Austin** — zero hits in their respective volumes beyond the alphabetical senior/student index
  (surname only, no office, no photo). A `"Judicial Council"` search against the 1978-79 volume (for
  Wilson's office) returns no matches at all; that body of the yearbook simply does not cover ASG's
  judicial council that year.

## Nothing added

No file in `data/photos.json` or `data/photos/` changed this run. `python3 scripts/build.py` and
`python3 scripts/check_data.py` both run clean against the unmodified tree (61 years, all 73 leader
portraits present, 217 officer portraits still open, the same four years without a scene photograph).

## For the next run

The bulk wkuherald pull is now done for the full `sga` tag archive and found nothing new — don't
repeat it verbatim. If wkuherald.com is tried again, the open thread is the untagged pre-2010
articles: `search=SGA` against the plain post endpoint (no tag filter) reaches as far back as 2002,
but a direct date-ranged query against 2008-09 (the one year-photo gap inside that article range)
returned zero posts of any kind — that window was never migrated into this WordPress install, tagged
or not, so it is a dead end, not an unswept one. 1994-95 and 1995-96 predate wkuherald.com entirely.
2000-01 is untested this way and is the one remaining thread: a `search=` query restricted to
2000-2001 dates, if the install holds anything that far back, hasn't been tried.

The archive.org search-inside + BookReaderImages.php route is now proven and costs nothing against
TopSCHOLAR's pacing limits; it is worth using directly (rather than djvu.txt plus a manual leaf guess)
whenever a future run works 1971-1981, 1986 or 1987 material, but it cannot produce more than
`_djvu.txt` already told this run existed — the gap in those five years is the yearbook's own
coverage, not the retrieval method.
