# Photograph run, 14 October (fourth scheduled pass): a new route into the archive, no new portrait cleared

## Priorities 1, 2 and 4: reconfirmed, unchanged

Per CLAUDE.md's "check whether an earlier run already got them," checked against `data/photos.json`
and `data/years.json` before anything else.

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait in `data/photos.json`.
- **Priority 2** (every other president or student regent): all 61 years' `leaders` records carry
  a photo. Zero missing, confirmed by direct query of `years.json` against `photos.json`.
- **Priority 4** (years with no photograph at all): zero years missing from `photos.json`'s `years`
  array.

`python3 scripts/portrait_gap.py`: 189 officer slots / 159 people / 157 with no portrait in any
year — unchanged from every pass since 13 October. Nothing moved this pass either, but the method
below is new and worth carrying forward.

## A route around the network block that prior passes didn't have

Every photo-run report since 13 October has recorded the same two blockers: `digitalcommons.wku.edu/
cgi/viewcontent.cgi` (the PDF route) refused with a Cloudflare challenge at this container's egress,
and `web.archive.org` resetting the connection outright. Both re-confirmed exactly that, fresh, this
pass. But `archive.org` itself (not `web.archive.org`) is open, and prior passes used only one of its
routes: the plain-text `_djvu.txt` OCR dump, for a name-match check. **archive.org also serves the
scanned page images directly**, for every Talisman it holds (1971-1981, 1986, 1987), through the
Internet Archive's own page-image service, which needs no special headers and isn't
Cloudflare-gated. **Corrected on review, 14 October:** this note first gave the route as
`BookReaderImages.php`, which is retired — it answers 404 from both of an item's nodes and returns
Internet Archive's generic "Page Not Found" page, so any routine that copied it would have read a
dead endpoint as a dead archive. The two routes that do serve the images are:

```
https://archive.org/download/{id}/page/n{leaf}.jpg
https://iiif.archive.org/iiif/{id}%24{leaf}/full/800,/0/default.jpg
```

Both answer 302 first, so a fetch that does not follow redirects records a failure where there is
none; follow them (`curl -sSL`) and both return a real JPEG, verified by its `FF D8` magic bytes.
The first serves the full-resolution page (about 1.8 MB for a Talisman leaf), the second a width-
capped rendering (about 200 KB) that is enough to read a caption and cheaper to fetch.

The leaf number for a given printed page comes from `{id}_page_numbers.json` in the same item (maps
`pageNumber` to `leafNum`; there is a front-matter offset, typically 3-4 leaves, that a page-number
search alone will not catch). This returns a real JPEG of the actual printed page — not OCR text,
the page itself — which means a caption an OCR pass mis-set, split across a column break, or
rendered illegibly can now be read directly. It costs one request per page and nothing rate-limits
it the way digitalcommons does.

This matters beyond photographs: every other research routine on this project has been treating the
Talisman years archive.org holds as "text-search only, images unreachable." They are not. Worth
flagging to whichever routine reads `.research/` next, not just this one.

## Applied to five years still carrying gap names, nothing cleared the bar

- **1974-75, Vern Pulman** (Representative-at-Large): the index-listed ASG pages are 108-109, 334,
  384, 394, 406 (`talisman1975west`, leaves 112-113, 338, ...). Viewed 108, 109 and 334 as actual
  page images. Page 108 ("ASG....Let's take roll") names and photographs Jeff Consolo, and captions
  a "Secretary Cindy Kirkpatrick" photo already in the archive; page 334 is the Talisman staff's own
  section, unrelated. No photograph or caption anywhere names Pulman. Consistent with the OCR-only
  conclusion from 13-14 October, now checked against the actual page rather than its text layer.
- **1977-78, David Bass** (Activities Vice President): found what OCR-only search had not surfaced
  cleanly — p. 34's caption, "A LIGHT MOMENT IN AN ASG MEETING brings laughter from president Bob
  Moore and smiles from activities vice president David Bass, secretary Sharon May and vice
  president Cathy Murphy," over a photograph with three clearly distinguishable people (a standing
  man laughing, a seated woman in sunglasses, a seated woman behind). Checked whether the other three
  named people could be eliminated by their own already-confirmed portraits (Robert Moore, Sharon
  May, Cathy Murphy all already carry sourced photos elsewhere in `photos.json`, from senior/
  sophomore class portrait pages, independent of this group shot) and leave Bass as the remainder by
  elimination. **Did not do this.** Four names over three clearly-countable faces, with no
  left-to-right or positional language in the caption, means elimination is a guess dressed as
  identification — exactly what CLAUDE.md's "a misidentified face is worse than no face" rule is
  for. Recording the page and the reasoning so a future pass does not re-walk it and does not take
  the elimination shortcut either.
- **1978-79, David Young / Alice Wicks / Steve Wilson**: re-viewed the actual ASG spread images
  (pp. 288-289, confirmed via `talisman1979west`'s own index entry "Associated Student Government
  53, 73, 82, 119, 262, 288-9") as pictures, not text. Page 288 photographs and names only Steve
  Thornton (president) and Victor Jackson (a committee member, not a gap name). Page 289's article
  text names David Young, who is indexed at that page and no other, saying the change was meant to
  force heads-up competition; the page's only photograph is an uncaptioned-by-name shot of two
  unidentified people at a desk plus a pile of newsletters. Alice Wicks is in the volume's index as
  "Wicks, Alice Elizabeth" but carries no page number at all, where the entries either side of her
  do, so there is nothing to turn to.
  **Corrected on review, 14 October.** This note first said no photograph anywhere in the volume
  names any of the three. That is wrong as to Wilson, and the correction leaves the decision
  unchanged while replacing the reason. Page 379, a class-portrait page, carries a caption reading
  "STEVE WILSON, agriculture" with Tompkinsville beneath it. It cannot be tied to the ASG officer:
  the volume indexes three separate men here — Wilson, Stephen Alan (no page); Wilson, Steve Alan
  (296, 318, 320, 336); Wilson, Stevie Joe (379) — and every other name in that portrait run
  (Willoughby, Kevin Wilson, Patricia Wilson, Wimberley, Witten) is indexed at 379 too, which fixes
  the p. 379 portrait as Stevie Joe Wilson. None of the three is indexed to any of the ASG pages.
  So the portrait exists and is not usable, which is a different and more useful thing to record
  than its absence: what a later pass has to settle is which of these three men held the office,
  not whether the volume photographed anybody.
- **1980-81, Mark Chesnut** (Treasurer): the volume's ASG group photograph (p. "Associated Student
  Government — Front row: ... Back row: ...", a full named roster, on the spread ending at p. 284)
  does not include his name among its 28 captioned figures (6 front, 7 second, 8 third, 7 back —
  this note first said eighteen, corrected on review against the caption itself). The back-of-book index gives only "Chesnut, Mark Cameron 234" with
  no photo credit recoverable there. A second check, for any other "treasurer" caption in the volume
  that might name him outside the ASG section, found only fraternity treasurers (Sigma Alpha Epsilon,
  Sigma Chi, Alpha Gamma Rho), none of them Chesnut.
- **1986-87, Chris Millay / Dwight Austin**: re-confirmed via `talisman1987west`'s full text that
  neither name appears anywhere in the volume (Millay: two index entries, both a different person,
  Beth Ann and Lori Ann Millay; Austin: all index entries are other people). No ASG feature spread
  with a named photo caption exists in this volume to check as an image — the ASG mentions in this
  year's Talisman are confined to a few paragraphs of running text about president Tim Todd, with no
  accompanying photograph of the office-holders below him.

## What is still open

The 189-slot gap is unchanged. The method above reaches the Talisman years archive.org holds
(1971-1981, 1986, 1987) at the level of the actual page image, and the five years above are worked
out by it, with one live lead left rather than none: the p. 379 Steve Wilson portrait in the 1979
volume waits on establishing which of three men of that name held the 1978-79 office, which is a
question for the Herald and the ASG minutes, not for the yearbook. Holdings re-checked item by item
on review: 1971 through 1981, 1986 and 1987 return metadata, and 1982, 1983, 1984, 1985 and 1988
return an empty object, so the boundaries above are the archive's and not an artefact of guessing at
identifiers. It cannot reach 1982-1985, 1988 onward (not held by archive.org; blocked at
digitalcommons) or the pre-1971 years (not held by archive.org either, and the 1966-70 names in the
gap — Carla Dotson, Patricia Lanning, Pat Smith, Mike McDaniel, Paul Gerard — stay reachable only
through the still-blocked digitalcommons PDF route). The bulk of the gap, per the 13-14 October
notes, falls in 1992-2011, also outside archive.org's holdings.

## Checks

No file in `data/photos/` or entry in `data/photos.json` changed this pass; nothing cleared the
identification bar. `python3 scripts/build.py` then `python3 scripts/check_data.py`: 61 years, clean,
60 presidents, no missing leader portrait, no year without a photograph.
