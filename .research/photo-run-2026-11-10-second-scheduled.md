# Photograph run, 10 November (second scheduled pass): one new portrait, William Berry, found in the 2015 Talisman's club pages using last pass's TLS-fingerprint bypass

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`, from earlier runs. Nothing to do here.
- **Priority 2**: every president and student regent carries a portrait before and after this
  pass's change. `check_data.py` exits clean.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` still reports 156 people with no
  portrait anywhere in the file, unchanged by this pass - William Berry's seat was an ordinary
  "Senator," which the script's own rule excludes from the cabinet/Senate-leadership count it
  tracks. He still had no portrait anywhere before this pass, and does now.
- **Priority 4**: every one of the 61 years carries at least one photograph. No gap.
- `research-photos` already contained every commit on `origin/main`; no merge was needed before
  starting.

## The new portrait: William Berry, 2014-15 senator

Confirmed this morning's finding from the first 10 November pass still holds: `urllib.request`
with a full browser header set reaches `digitalcommons.wku.edu/cgi/viewcontent.cgi` cleanly where
`curl` still 403s on the identical URL (tested against article 7642 again, same byte count as
logged this morning). Used it to open `data/photo-finds/_topscholar-wanted.json`'s one genuinely
open lead, record 8679 - the 2015 Talisman, *Resurgence* (viewcontent article=9665, context
dlsc_ua_records), flagged in that file since 30 September as "the full page-by-page sweep does
still appear to be outstanding" against a 23-name worklist that includes several gap-list names.

Fetched the whole PDF (585,654,199 bytes, matching the ~578 MB Wayback estimate already on file;
22.8 seconds). `pdftotext` and `pdftoppm`, both installed in this container despite
`SGA-60-AGENT-INFO.md`'s note that `pdftotext` is missing - worth a correction there, see below -
pulled a real 160-leaf text layer. Grepped it whole against the worklist's 23 names.

**William Berry is named, with a row key, in the Campus Activities Board club photograph, p. 318:**

> Row 1: Amanda Trail-Cruz, Kayla Lofton, Cadeja Hays.
> Row 2: Lakosa Shelton, Jasmine Hockaday, William Berry, Lyndsey Pener.
> Row 3: Alysha Nanouk, Megan Dunn, Kamilah Champion.

Ten people, three named rows, ten names - the key is exhaustive. Rendered the page at 300 dpi and
looked at the photograph directly rather than trusting the row arithmetic alone: of the ten people
in the frame, **he is the only man.** That makes the identification certain independent of
whether "Row 2, third" is read left-to-right or right-to-left, which is exactly the kind of
row-order ambiguity that has sunk other leads in this project. The volume's own back index -
`Berry, William 297, 318` - names only one William Berry in the whole 352-page book, at this page
and one other (p. 297, inside the student-portrait section; not reached this pass, see below), so
there is no second candidate anywhere in the source to confuse him with.

He is the 2014-15 senator confirmed in SGA's own minutes of 24 February and 5 May 2015
(`years.json`), active enough in the record to have authored four pieces of legislation that year
and run unsuccessfully for administrative vice president that spring. A Talisman club photograph
rather than an SGA-specific one is consistent with how this project has already published other
portraits - Sally Chenault's and Janice Berkshire's both come from academic-class composites, not
SGA photographs - so this is not a departure from practice, just the same identification standard
applied to a different club page.

Cropped from the rendered page, `data/photos/2014-15-william-berry.jpg` (380x520, real JPEG,
checked for the FF D8 FF E0 header). Added to `data/photos.json`'s `leaders` array with the row
key quoted and the index cross-reference recorded. `data/photo-finds/_do-not-use.json`'s existing
William Berry entry (the self-defence-class frame, closed 1 September for having no usable face)
now carries a `resolved` note pointing at this one, following the file's own convention for a
superseded refusal rather than deleting the history of why the first lead failed.

## The same volume, worked through for the rest of the worklist, and mostly exhausted

Every other name on record 8679's worklist was checked against the same text layer:

- **Sawyer Coffey, Sophie Whorf, Laryn Hilderbrandt, Robert Bell** and several others on the list
  do appear in this volume, but each sits inside a large, un-rowed crowd photograph - Alpha Delta
  Pi (roughly 100 people on a lawn), CRU (similarly sized), Alpha Xi Delta - with nothing but an
  alphabetical member list beside it. No caption key ties any one name to any one face in these,
  which is the same bar that has closed every other big un-rowed composite in this project. Not
  usable, and this run found no device to make them usable; a future pass should not re-open these
  three specific photographs without a genuinely new source.
- **Abigail Potter, Allie Payne, Amber Daniels, Ben Beam, Brandon Mudd, Cameron Hubbard, Dedais
  Hudgins, Gretchen Mosby, Kasey Glasgow, Lucas Knight, Madison Keller, Nathan Cherry, Nolan
  Calhoun, Ryan Puckett, Stacey Schepers, Thomas Poole** do not appear anywhere in this volume's
  text layer by name at all (checked both full name and surname-only, to catch an OCR break
  between given name and surname).
- **Carter Jackson** is named once, with a clean position cue - "OPPOSITE Bowling Green freshman
  Caroline Davis adjusts Bowling Green sophomore Carter Jackson's hat after sledding down College
  Street" - but the photograph is a snow-day feature with no SGA content anywhere in the caption or
  the surrounding text. Declined on the same ground the September pass used to decline Jacob
  Turner's Star Wars-memorabilia feature: an identification being certain does not make a
  private-interest photograph eligible when the subject is not pictured in a student-government
  capacity. Not used.
- The **Chism-Richey presidential election** feature (pp. 184-187) was read in full - a rich,
  individually captioned three-photograph spread on the spring 2015 SGA presidential race - but
  both Brian Chism and Jay Todd Richey already carry portraits in `data/photos.json`, so nothing
  here was new. Recorded for anyone who later wants a second, better-sourced frame for either.

`_topscholar-wanted.json`'s entry for record 8679 is updated in place with this pass's findings,
superseding its 30 September "outstanding" note; treat this volume as exhausted for this worklist
unless a future pass finds a second copy with different illustrations.

## One correction to `SGA-60-AGENT-INFO.md`

Section 4 says "`pdftotext` is NOT installed here. Use PyMuPDF (`import fitz`), which is." Neither
half held in this container this pass: `pdftotext` and `pdftoppm` (poppler-utils) are both on
`PATH` and worked cleanly on a 585 MB file; `python3 -c "import fitz"` fails with
`ModuleNotFoundError` under the system Python (3.11) and PyMuPDF is not installed for it either.
Pillow has the same split: it is on `python3.13`'s site-packages only, not on the `python3`
(3.11) `dist-packages` import path, so a script that needs both PDF rendering and cropping should
plan on `pdftoppm` + `python3.13` for image work rather than assuming `fitz` is available. This
may be a container-to-container difference rather than a permanent fix; a later run should check
for itself rather than trust this note indefinitely, the same way this file already asks for every
other access claim.

## Housekeeping left undone

Page 297, the student-portrait-section reference the index also gives for William Berry, was not
located this pass - that section of the book appears to collapse many printed pages onto very few
PDF leaves (a full-bleed divider leaf sits between printed page 267 and printed page 314 with
nothing in between), and resolving the leaf-to-page mapping for it would have cost more of this
run than the lead was worth once the Campus Activities Board photograph already settled the
identification on its own. Left as a loose end for whoever next has reason to open this volume,
not as a blocker on anything.

## Conclusion

One new portrait: William Berry, 2014-15 senator, from the 2015 Talisman's Campus Activities
Board page, identified with certainty because he is the only man among ten people the caption
names in full. The volume that produced it is now worked through against its original worklist
and mostly closed out; what remains unresolved in it (page 297, three un-rowed crowd photographs)
is recorded rather than quietly dropped. `build.py` and `check_data.py` both pass clean. Landed on
`research-photos`.
