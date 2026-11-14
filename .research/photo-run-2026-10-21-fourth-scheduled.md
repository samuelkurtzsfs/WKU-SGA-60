# Photograph run, 21 October fourth scheduled pass: David Bass identified by elimination, iiif.archive.org confirmed open again, six more archive.org-coverable gap names checked and closed

## Priorities 1, 2 and 4, reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry
  a portrait in `data/photos.json`, confirmed before doing anything else.
- **Priority 2**: zero presidents and zero student regents without a portrait.
- **Priority 4**: every year carries at least one year-level photograph.

## Network state, retested fresh at the start of this run

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`: still HTTP 403, Cloudflare "Just a moment..."
  challenge, tested with the full browser-navigation header set. Still closed.
- `web.archive.org`: still a connection reset mid-exchange. Still closed.
- `archive.org` (plain item host): open.
- `wkuherald.com`: open, WordPress API reachable.
- **`iiif.archive.org`: open, and stayed open through roughly a dozen fetches across three
  different Talisman volumes this pass.** The 21 October third-scheduled-pass note on this same
  branch left it closed mid-session with the David Young lead unfetched. It is not closed now.

## A new portrait: David Bass, 1977-78 Activities Vice President

Picked up the lead the third-scheduled-pass note left open and went one step past it. The 1978
Talisman's own index gives `Bass, David Eugene 34`, and p. 34 is the same ASG meeting page
`data/photos.json` already uses for a *year*-level photograph (`1977-78-asg-meeting.jpg`, added by
an earlier run) — its caption, by Lewis Gardner: "A Light Moment in an ASG Meeting... laughter from
president Bob Moore and smiles from activities vice president David Bass, secretary Sharon May and
vice president Cathy Murphy."

Fetched the leaf at full resolution via `iiif.archive.org/iiif/talisman1978west$38/...` (volume
offset confirmed directly this pass: leaf 36 prints page 32, so leaf = printed page + 4 for this
volume, not the +2 that holds for `talisman1979west` — the front matter differs book to book, as
the earlier note already warned). The photograph shows three faces clearly: a standing man laughing
with his mouth wide open, a seated man in sunglasses smiling, and a woman at a podium smiling. Bob
Moore and Cathy Murphy already have portraits on file from other sources (Herald headshot and a
1978 Talisman senior portrait respectively), and Sharon May has one too (1977 Talisman sophomore
portrait) — all three confirmed female except Moore. That leaves exactly one unidentified face that
can be male: the seated man in sunglasses is David Bass by elimination, since Sharon May and Cathy
Murphy are both women already pictured elsewhere in the file, the standing laughing man matches the
caption's own "laughter from president Bob Moore," and Bass is the only other person the caption
names. Cropped his face alone (not the whole scene, which was already on file) and added it to
`data/photos.json` under `leaders`, `1977-78-david-bass.jpg`. Verified the JPEG header (`FF D8`)
before committing.

This is an elimination identification, not a caption printed directly under his face, and the
record says so explicitly in the `src` label so a later pass can judge it on its own terms rather
than trusting a bare citation.

## Six more archive.org-coverable gap names, checked and closed with nothing added

Cross-referenced `scripts/portrait_gap.py --list --any-year` against archive.org's actual Talisman
holdings (1971-1981, 1986, 1987, confirmed by the third-scheduled-pass note) to find which
"no portrait in any year" names fall inside a volume that is actually fetchable right now:

- **Vern Pulman** (1974-75, Representative-at-Large): not in `talisman1975west`'s directory at all
  — no "Pulman" of any spelling. He was a February 1975 appointee filling a vacant seat, which may
  explain his absence from a volume largely assembled before that appointment. No portrait.
- **Steve Wilson** (1978-79, Judicial Council Chairman): the 1979 directory carries two entries,
  "Wilson, Stephen Alan" (no page) and "Wilson, Steve Alan 296, 318, 320, 336" — already ambiguous
  as to whether these are one person or two. Checked all three fetchable pages. P. 296 is a Pre-Law
  Club group photo captioned only "S. Wilson," no first name, no SGA context. P. 318 is a Greek Week
  section divider with no caption at all. P. 320 names a "Steve Wilson" as one quarter of a
  barbershop quartet in a Spring Sing photo, but does not say which of the four singers he is. None
  of these ties a confirmable face to the Judicial Council Chairman, and the fraternity/Greek-Week
  context of every hit raises real doubt this is even the same Steve Wilson rather than a different
  student who shares the name — exactly the trap CLAUDE.md warns against. No portrait added.
- **Alice Wicks** (1978-79, Secretary): confirmed again, no page number in the 1979 directory at
  all (every neighbouring entry that has a senior portrait carries one). No portrait.
- **David Young** (1978-79, Administrative Vice President): followed up the leaf-291 lead directly.
  It is real but is not a portrait — p. 289 is a text page, "Making news about entertainment," that
  quotes him by name on the new student constitution, with unrelated photography (an ASG newsletter
  stack, two students studying) credited to a different photographer. The directory page number
  points at a text mention, not a senior portrait. No portrait.
- **Mark Chesnut** (1980-81, Treasurer): the 1981 directory's `Chesnut, Mark Cameron 234` points at
  an intramural-sports results page listing "Mark Chestnut (Sigma Alpha Epsilon)" as a badminton and
  racquetball-doubles winner — text only, and spelled with a 't' where the organization data spells
  it without one. The page's one photograph is two unrelated football players. No portrait.
- Confirmed again rather than re-run: **Chris Millay** and **Dwight Austin** (1986-87) were checked
  against `talisman1987west`'s full text in the 21 October third-scheduled-pass run with nothing
  found; not repeated here.

## What this run leaves changed

`data/photos.json` gained one `leaders` entry (David Bass, 1977-78) and `data/photos/` gained
`1977-78-david-bass.jpg`. `scripts/portrait_gap.py` now reports 188 officer slots (158 people)
without a portrait, down from 189 (159), `--any-year`. `python3 scripts/build.py` and
`python3 scripts/check_data.py` both exit clean. Landed on `research-photos`.

## For the next run

`iiif.archive.org` is open and was stable for this whole pass — do not assume it is closed without
testing fresh. Every "no portrait in any year" name that falls inside archive.org's actual Talisman
coverage (1971-1981, 1986-87) has now been checked at least once through this route; the David Bass
find was the only one of seven tried this pass that panned out. The 1988-2002 stretch remains wholly
dependent on the blocked `digitalcommons.wku.edu` route (the only place those yearbooks exist), and
2003-2025 names keep surfacing only in SGA's own text minutes or in `wkuherald.com` recap articles
that do not carry individual photographs of junior officers — tried five more names this pass
(Elizabeth DeLozier, Livi Ray, Elizabeth Gannon, Connor Ferguson, Kayla Distler) through
`wkuherald.com`'s own search API with nothing but meeting-recap mentions, no new lead worth writing
up in detail.
