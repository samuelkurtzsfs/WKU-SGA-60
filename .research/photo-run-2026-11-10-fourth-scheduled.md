# Photograph run, 10 November (fourth scheduled pass): the 1968 Talisman's whole Associated Students spread read page by page, and its own officer roster document opened in full - Mike McDaniel confirmed absent from both, no new portrait

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- **Priority 2**: `python3 scripts/check_data.py` exits clean - 61 years, 60 presidents, every
  president and student regent has a portrait.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` still reports 156 people with no
  portrait anywhere in the file. Unchanged this pass.
- **Priority 4**: every one of the 61 years carries at least one photograph. No gap.
- Today's earlier passes already established `viewcontent.cgi` is passable this session through
  `urllib.request` (curl still 403s on the identical URL). Reconfirmed at the start of this pass
  by pulling two fresh PDFs end to end (see below) before relying on it further.

## What this pass chased: Mike McDaniel's own officer document, and the whole 1968 Talisman Associated Students section

Of the three oldest names on the portrait gap list, this week's earlier passes closed Carla
Dotson and Pat Smith negative and Patricia Lanning unusable (1967 Talisman, p. 136, logged 10
November). The fourth-oldest open name, Mike McDaniel (1967-68, Campus Representative at Large),
had so far only been checked against Herald bylines - never against either document his own
`years.json` entry or the project's usual portrait source actually cites.

**`dlsc_ua_records/508` (UA3/3/1, "Associated Student Government Officers 1967-68") - his own
cited source, opened for the first time.** Landing page gives viewcontent article=1508. Fetched
via the `urllib` bypass (528 KB, 3 pages, opens clean) and rendered each page at 3x. It is a
typed roster of the 1967-68 officers and Congress by name, office, address and phone number -
McDaniel's own line reads "Mike McDaniel / Campus Representative at Large / 1351 College Street /
842-9861." No photograph anywhere in the three pages. This was the archive's own citation for him
and it simply never carried an image.

**The 1968 Talisman's Associated Students section (`dlsc_ua_records/384`, article=1384, pp.
152-155) - fetched whole and read as rendered page images rather than through its badly garbled
OCR layer (names like "Wonald D. Deck" for "Ronald D. Beck").** This is the volume covering his
exact year and the source nearly every other 1967-68 officer's portrait in this file already
comes from. Read all four pages:

- **P. 153**: the Associated Students group photograph, 20 people on the chapel steps, captioned
  by row: *Fourth Row:* Tom Evans, Steve Stephens, Bill Straeffer, Skip Gaines, Terry Gilpin, Earl
  Edmonds. *Third Row:* Michael Klein, Steve Reeves, Frank Genzianelli, Carmen Willoughby.
  *Second Row:* Susan Streible, Randi Jensen, Johnny Graham, Bonnie Jo Cheron, Becky Cooper,
  Margaret Brockman. *First Row:* Ron Beck, William Menser, Claudia Fowler, Larry Heishman. Also
  four individual officer portraits captioned William Earl Menser (President), Ronald D. Beck
  (Vice President), Claudia L. Fowler (Secretary), Larry S. Heishman (Treasurer).
- **Pp. 154-155**: six further committee photographs, each individually captioned - Executive
  Committee (Heishman, Straeffer, Fowler, Streible, Evans, Menser, Beck), Publicity Committee
  (Jensen, Seitz, Sullivan, Sandifer, Simon, Coughlan, Bush, Priddy, Vertner, Myers, Genzianelli,
  McDonald), Rules and Elections Committee (Gerard, Garrison, Adams), Student Activities
  Committee (Bass, Beck, Jaffe, Lee), Judicial Council (Skillern, Dalrymple, Matthews, Ashby,
  Leeper, Glowacki), Finance Committee (Loyal, Morgan, Heishman, Townsend).

Mike McDaniel is named in none of these eight captions, and neither is Keith Petrie, the other
1967-68 Campus Representative at Large - both of the year's two at-large seats are absent from
every photograph in the section, not just McDaniel's. (The Publicity Committee caption's "Arthur
McDonald" is a different surname, checked directly against the rendered image rather than assumed
from the OCR layer, which elsewhere in this project has a known habit of reading names loosely.)

## Conclusion

No new portrait this pass. Both of the two most promising documentary leads for Mike McDaniel -
his own cited officer roster and the Talisman's full organizational section for his exact year -
are now read in full rather than partially cited, and neither carries an image of him or of the
seat's other holder. This does not close the search (a photograph could still exist in a class
portrait grid if his year of enrollment were known, which it is not from any source on file), but
it rules out the two sources most likely to have settled it cheaply. Logged in
`data/photo-finds/1966-1970-notes.json`. `data/photos.json` and `data/photos/` are unchanged.
`build.py` and `check_data.py` both pass clean. Landed on `research-photos`.
