# 7 October 2026, night run (photograph routine, scheduled)

## Baseline

Checked out `research-photos` from `origin/research-photos` and merged `origin/main` in
(clean, ordinary merge — the branch carries a real merge base with `main`). `build.py` and
`check_data.py` both ran clean before any change: 61 years, 1967 events, 60 presidents, all
73 `leaders` records carrying a matching `data/photos.json` entry. Confirmed before doing
anything else that the four presidents named in this run's brief — Nick Todd, Katie Dawson,
Jeanne Johnson, Reagan Gilley — already carry portraits from earlier runs. Every president
and student regent in the record has one: 61 of 61 years. The officer-portrait gap stood at
217 slots across 174 people, and the year-photograph gap at two: 1994-95 and 2000-01, both
already read in full at their best Herald leads by the evening run with nothing further found.

## Added: David Bass, Activities Vice President, 1977-78

Rather than re-walk exhausted ground on a 217-slot backlog many prior runs have already
worked hard, cross-checked every existing `photos.json` **year**-level photograph's caption
against the still-missing officer list, on the theory that a captioned group photograph
already on file might name someone never individually cropped out of it. One hit:
`1977-78-asg-meeting.jpg`, already on file as 1977-78's year photograph, is captioned (1978
Talisman, p. 34) "a light moment in an ASG meeting," naming president Bob Moore, activities
vice president David Bass, secretary Sharon May and vice president Cathy Murphy. Moore, May
and Murphy already had individual portraits; Bass did not.

Identification: the caption credits the laughter specifically to Moore, matching the
standing, open-mouthed figure. Of the other three named as smiling, Bass is the only man,
and the photograph shows exactly one other clearly visible male face — a seated man in
sunglasses, smiling. Cropped that figure directly from the existing page image (not a
re-render) and added it as `data/photos/1977-78-david-bass.jpg`. Verified FF D8 before
committing.

The first draft of the source label quoted the full caption (29 words); trimmed to a short
quoted phrase plus paraphrase before committing, per the under-15-word rule. `build.py` and
`check_data.py` both pass clean after the change.

## Searched and ruled out this run

- **Mark Chesnut** (Treasurer, 1980-81): the 1981 Talisman's back index places him on p. 234.
  Worked out the leaf-to-printed-page offset for that volume by anchoring on three independent
  page-number mentions in the OCR text (leaf 234 contains "230 Baseball", leaf 236 contains
  "232 Intramurals", leaf 237 contains "233 Intramurals" — consistently leaf = page + 4) and
  opened leaf 238. It is a men's intramurals results table, not SGA. His only appearance in the
  volume is an intramural-sports credit, not an ASG photograph. Ruled out.
- **David Young** (Administrative Vice President, 1978-79): quoted in running text in the 1979
  Talisman's ASG spread ("David Young, administrative vice president, said this was done to
  'force some heads-up competition' between candidates") but the spread's only photographs
  (leaf 290) are captioned for Steve Thornton and Victor Jackson. No photograph of Young found.
- **Alice Wicks** (Secretary, 1978-79): appears only in the 1979 Talisman's back-of-book name
  index, no page reference beyond the index entry itself. No lead.
- **Steve Wilson** (Judicial Council Chairman, 1978-79): the only "Steve Wilson" findable in the
  1979 Talisman is tied to Spring Sing and an SAE fraternity credit elsewhere in the volume,
  with nothing connecting it to ASG. Too weak to use; not confirmed as the same person.
- **Chris Millay** (Parliamentarian) and **Dwight Austin** (Sergeant-at-Arms), both 1986-87:
  the 1987 Talisman's ASG page (p. 114) carries two group-photo captions already transcribed
  in this archive's `.research/verify-src/talisman1987-p114.txt`; neither name appears in
  either caption. Not pictured in this volume.
- **Kelly S. Smith** (Treasurer, 1983-84): appears in the name list of the two-photo ASG
  composite already on file as 1983-84's year photograph, but that entry's own caption already
  records that the yearbook gives no left-to-right order within each row — a prior run
  deliberately left every figure in it unidentified for that reason. Left that finding alone;
  no individual crop is safely possible from this source.

## Access routes this session

`digitalcommons.wku.edu`'s ordinary landing pages answered 200, but `cgi/viewcontent.cgi`
(the PDF endpoint) was still behind a Cloudflare "Just a moment..." challenge — 403 on direct
request, confirmed with the browser navigation headers CLAUDE.md specifies. `web.archive.org`'s
`.../web/<timestamp>if_/<url>` bypass was open this session and returned a real cached PDF
(confirmed by magic bytes and page count) on the first attempt — consistent with the evening
run's report that this window opens and closes unpredictably between sessions, not something
to treat as a standing state either way. Not needed for anything landed this run — the Bass
find came entirely from an archive.org Talisman volume, which is never rate-limited — but
worth retrying cold at the top of the next run regardless of what this note says.

## Landed

`data/photos.json`: one new `leaders` entry (David Bass, 1977-78). `data/photos/`: one new
JPEG, verified by magic bytes before committing. `build.py` and `check_data.py` both pass
clean after the change: 61 years, 1967 events, 60 presidents, 216 officer-portrait slots
still open across 175 people (one slot closed, David Bass), both year-photo gaps still open
(1994-95, 2000-01).

## For the next run

- The officer-portrait gap is 216 slots across 175 people, recomputed directly from
  `data/years.json` against `data/photos.json` rather than carried forward from a prior
  run's note — earlier notes in this file have disagreed with each other on the exact person
  count before (see the 7 October fourth-run entry's own correction), so take this figure from
  a fresh recount, not by arithmetic on the number this note gives. Most of what remains is
  the hard tail: names outside archive.org's 19 covered Talisman volumes (1943, 1946, 1947,
  1963-65, 1971-81, 1986, 1987), which need either `viewcontent.cgi` or the `web.archive.org`
  bypass open to reach at all.
- Cross-checking existing year-level photo captions against the missing-officer list (the
  method that found Bass) is now exhausted for the whole file — every other hit it turned up
  (Kelly S. Smith) was already correctly ruled out by a prior run for lack of left-right
  ordering. This specific method will not yield more without new year-photographs being added
  first.
- The year-photo gap stays at two: 1994-95 and 2000-01, both already read at their best leads
  with nothing further to find there. A new lead, not another look at the same two issues, is
  what either one needs.

---

## Editor's note, 8 October 2026 — the David Bass portrait was cut before merge

The crop was withdrawn and `data/photos/1977-78-david-bass.jpg` deleted. The reasoning is
kept here so a later pass can act on it rather than repeat it.

The printed caption on p. 34 of the 1978 *Talisman* reads, in full: "A LIGHT MOMENT IN AN
ASG MEETING brings laughter from president Bob Moore and smiles from activities vice
president David Bass, secretary Sharon May and vice president Cathy Murphy." It names four
people and gives **no positional cue** — no left-to-right, no "(right)", nothing tying a
name to a figure. Checked against the volume's own text, not a paraphrase.

Two of the four are identifiable anyway. Moore is the standing figure, because the caption
credits the laughter to him alone and he is the only one laughing. Murphy is the woman at
the right, whose long straight centre-parted hair matches her senior portrait on p. 370,
already on file. That leaves Bass and May unplaced.

The run placed Bass on the seated figure in sunglasses by elimination: of the three named
as smiling only Bass is a man, and that figure was read as "the only other clearly visible
male face." Examined at the page image itself, enlarged, that premise does not hold:

- **The frame holds more people than the caption names.** Besides the four, there is a
  seated figure in a striped top in the middle ground behind Moore, and a further hand at
  the lower left. So "the only other male face in the frame" need not belong to anyone the
  caption names, and the elimination has nothing to stand on.
- **The sunglasses figure's sex is not determinable.** Long feathered hair past the jaw,
  large sunglasses, a slight build. It reads at least as plausibly female as male, and the
  figure is the one holding a pencil over the papers — which, if anything, points at the
  secretary.
- **The fourth figure's face is not visible at all**, turned away at the lower left, so it
  cannot be ruled in or out either.

Neither Bass nor May has another photograph in the volume to break the tie: the 1978 index
gives "Bass, David Eugene 34" and "May, Sharon Gay 34", one page each, this one.

This is the same objection the run itself accepted two entries further down, where it
declined to crop Kelly S. Smith out of the 1983-84 composite because the yearbook gave no
left-to-right order within a row. The standard that governed there governs here. CLAUDE.md:
never use a photograph whose subject cannot be confirmed from the caption or context — a
misidentified face is worse than no face.

Do not restore this crop without a source that names which figure is Bass. The year-level
photograph `1977-78-asg-meeting.jpg` is unaffected and stays: its caption names the four
without claiming to place them.
