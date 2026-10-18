# Photograph run, 18 October (third scheduled pass): a candid ASG photo found and correctly left unattached, seven 1970s-80s officer names checked against archive.org's Talisman run (six ruled out, one left open), two repeat-office names checked by web search

## Priorities 1, 2 and 4: reconfirmed, unchanged

Checked against the current `data/years.json` and `data/photos.json` before touching anything:

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait.
- **Priority 2** (every other student body president or student regent): zero gaps. All 73
  `leaders` records across 61 years carry a portrait.
- **Priority 4** (years with no photograph at all): zero. Every year carries at least a leader
  portrait or a year-level photograph.

`python3 scripts/portrait_gap.py --list` still reports 189 officer slots with no portrait, held by
159 distinct people, 157 with no portrait anywhere in the file — numerically unchanged from every
pass this week.

## A candid group photo found for David Bass (1977-78 Activities Vice President), and correctly not used

The 1978 Talisman (archive.org item `talisman1978west`, covering the 1977-78 academic year) carries,
on printed page 34, a photograph captioned: "A LIGHT MOMENT IN AN
ASG MEETING brings laughter from president Bob Moore and smiles from activities vice president
David Bass, secretary Sharon May and vice president Cathy Murphy" (credited to Lewis Gardner). The
index confirms this is David Bass's only appearance in the volume (`Bass, David Eugene 34`).

Pulled the page image directly (`archive.org/download/talisman1978west/page/n37.jpg`) and cropped
and enlarged the photograph itself to check it properly rather than guess from the caption alone.
It shows three people clearly: a man standing and laughing in a tank top, a second person seated in
the foreground wearing sunglasses with a pencil and papers, and a woman smiling in the background
at a podium. The caption names four people (two men, two women). There is no way to tell which of
the two visible men — if the foreground sunglasses-wearer even is a man rather than a woman, the
hairstyle and dress are ambiguous either way — is Bass rather than Moore, or which woman is May
rather than Murphy. **Not used.** CLAUDE.md's rule is exactly for this case: a caption that names
the right people is not the same as a photograph where each face can be matched to a name, and a
misidentified face is worse than no face. The lead is now closed rather than open: a future run
does not need to re-pull this page.

## Seven more 1970s-80s names checked against archive.org's Talisman run, no photograph found for any

Checked the plain-text (`_djvu.txt`) and, where a name hit, the `_djvu.xml` word-coordinate index
for the exact leaf, for every remaining archive.org-era (1971-1981, 1986, 1987) name in the officer
gap that David Bass's year hadn't already covered:

- **Vern Pulman** (Representative-at-Large, 1974-75) — no hit anywhere in `talisman1975west`.
- **David Young** (Administrative Vice President, 1978-79) — named once in `talisman1979west`, in the
  ASG section body text on the new 24-seat congress structure (printed p. 289, leaf 290), and not next
  to a photograph: the only captioned photograph on that page is of unread ASG newsletters lying on a
  floor. The volume's index entry `Young, David Paul 289` points at that same body-text mention. The
  other `Young` hits in the volume are Rodney Young, Rita Young and a `K. Young` in a group caption,
  all different people.
- **Alice Wicks** (Secretary, 1978-79) — appears only in the alphabetical index with no page number
  at all, meaning she is not pictured anywhere in the volume.
- **Steve Wilson** (Judicial Council Chairman, 1978-79) — **still open, not ruled out.** The body-text
  search found only unrelated Wilsons (Gordon Wilson Hall, a Poland Hall resident assistant named Stu
  Wilson, Ivan Wilson Fine Arts Center), but the volume's own alphabetical index carries
  `Wilson, Steve Alan 296, 318, 320, 336`, which that search missed. Printed p. 296 is a Pre-Law Club
  group photograph whose caption ends "(Back row) J. Rue, S. Wilson", and p. 320's text names a Steve
  Wilson in a Spring Sing barbershop quartet alongside the same Jon Rue. Whether this Steve Wilson is
  the ASG Judicial Council Chairman is **not established**, and a back-row initial in a club group
  photograph would not be a confirmable portrait even if he were. The three remaining indexed pages
  have not been examined. A future run should start from the index entry, not from a body-text search.
- **Mark Chesnut** (Treasurer, 1980-81) — appears in `talisman1981west` twice outside the index: an
  intramural-champions list (unlabeled action photo, two unidentified men, cannot be matched to a
  name) and a senior-salute entry for `WILLIAM G. CHESNUT`, who is a different person (the shared
  surname is the only connection; no source here establishes any relation between them). The index
  page for Mark Chesnut's own entry (234) turned out to be the same intramural-list page, not an
  individual class photo.
- **Chris Millay** and **Dwight Austin** (Parliamentarian and Sergeant-at-Arms, 1986-87) — neither
  person appears in `talisman1986west` or `talisman1987west`, checked both volumes since the
  academic year could plausibly be covered by either. Stated precisely, because the loose version
  of this sentence is what produces a false negative: both surnames *do* occur in those volumes,
  and every occurrence is someone else. `Millay` is Beth Ann Millay (a runner, indexed 1986 at
  132, 185, 346 and 1987 at 240) and Lori Ann Millay (1987, 52); the only `Dwight` in either book
  is Dwight Scott of Nortonville, indexed 1987 at 329. No `Austin` entry in either index carries
  the forename Dwight. There is no Chris Millay and no Dwight Austin in either volume's index.

Confirmed in passing that the archive.org page-image route itself still works cleanly
(`archive.org/download/<item>/page/n<N>.jpg` against the item's own leaf numbering, cross-checked
against the `_djvu.xml` `PARAM name="PAGE"` value to convert a word hit to a leaf, then against the
printed folio visible in the image to convert a leaf to a page number) — this is a usable method for
a future run with a specific lead, just not one that turned up anything usable today.

## Two repeat-office names checked by web search, no hit

`data/photos.json` carries no portrait anywhere for either; both hold the same office across
multiple years, so either would have closed more than one slot at once. Tried `WebSearch` (not
restricted to a domain, since neither is a current enough name to expect a live WKU page):

- **Steve Roadcap** (Chairperson/Campus Improvements 1995-96, Treasurer 1996-97, Judicial Foreman
  1997-98 — Legislative Research in 1996-97 was Andy Gailor's committee, not his) — no result naming him in connection with WKU SGA at
  all.
- **Andy Gailor** (Chairperson/Legislative Research, 1996-97 and 1997-98) — no result.

Both searches returned only generic WKU SGA constitution/minutes pages and unrelated people. This
is a two-name spot check, not a sweep of the 1990s slice of the gap; it closes these two leads
without closing the decade.

## No portrait found or added this run

No file in `data/photos.json` or `data/photos/` changed. The 189-slot gap is numerically unchanged.
This run's contribution is closing the David Bass lead properly (found, checked carefully, correctly
rejected rather than guessed at) and ruling out six more archive.org-era names and two repeat-office
names so a future run does not re-spend time on them. The seventh, Steve Wilson, is left open with a
specific next step rather than ruled out.

## Checks

`python3 scripts/build.py` then `python3 scripts/check_data.py`: clean. 61 years, 60 presidents, no
missing leader portrait, no year without a photograph. Merged `origin/main` into `research-photos`
first (clean fast-forward, no conflicts).

## Editorial check, 18 October

This log was checked against the sources before it was merged. Everything it reports about the
David Bass candid stands: the 1978 Talisman caption is verbatim as quoted, the index entry
`Bass, David Eugene 34` is his only appearance in the volume, and all four people the caption
names are the 1977-78 executive in `data/years.json` (Robert Moore president, Bass activities
vice president, Sharon May secretary, Cathy Murphy administrative vice president). Leaving the
photograph unattached was right. Vern Pulman's absence from `talisman1975west`, Alice Wicks's
index entry carrying no page number, and the absence of Chris Millay and Dwight Austin from both
the 1986 and 1987 volumes were each reconfirmed independently.

Four claims did not survive the check and have been corrected above:

- **Steve Wilson was reported as ruled out and is not.** The volume's index carries
  `Wilson, Steve Alan 296, 318, 320, 336`, which a body-text search for "Steve Wilson" cannot
  see. The lead is reopened with the index entry as its starting point. This is the same method
  the run used correctly for Alice Wicks and David Bass, and not using it here would have cost a
  future run a real lead on the strength of a false negative.
- **David Young was named once, not three times.** The other `Young` hits in the volume are
  other people. The run's conclusion — body text, no photograph — is correct and unchanged.
- **The name count was inconsistent** (six in the title, five in the heading and conclusion,
  seven in the list). It is seven: six ruled out, one left open.
- **A family relationship was asserted from a shared surname** between Mark Chesnut and
  William G. Chesnut. Nothing in the sources here establishes one, so the claim is gone.

No file in `data/` changed in this branch and nothing here reaches the published site; the
corrections are to the research record, which is what tells the next run which leads are closed.
