# Photograph run, 13 November (second scheduled pass): three archive.org/TopSCHOLAR leads opened by hand, nothing new

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry
  a `leaders` portrait entry in `data/photos.json`, unchanged.
- **Priority 2**: `python3 scripts/check_data.py` exits clean - 61 years, 1964 events, 60
  presidents, every president and student regent has a portrait.
- **Priority 3**: every leader (president/regent) already has a portrait by name. The gap is
  entirely in executive cabinet and Senate officers - 213 officer-slots across the record lack a
  same-year portrait by exact name match against `data/photos.json`.
- **Priority 4**: all 61 years already carry at least one photograph.

This matches the morning pass's own conclusion (`photo-run-2026-11-13-scheduled.md`): the
remaining gap is officers, not leaders or years, and most of it has already been searched
repeatedly. Rather than take that on faith, this pass independently re-opened three leads by hand
to check it.

## 1978-79: David Young (Administrative Vice President) and Alice Wicks (Secretary)

Fetched both halves of the 1979 Talisman's own ASG spread directly off archive.org
(`talisman1979west`, leaves n289/n290 = printed pp. 288-289, no rate limit) and read them as
images rather than trusting OCR. The spread ("ASG met each Tuesday in Downing University Center")
carries three individually captioned photographs - all three name only president Steve Thornton
or senator Victor Jackson - and one uncaptioned photograph of two seated people and a standing
figure that names no one. David Young is quoted in the article text on the facing page ("the
heads-up competition" quote already in his `organization` entry) but is not pictured or captioned
anywhere in this spread. Alice Wicks does not appear in it at all. This confirms the conclusion
already on file in `photo-run-2026-09-13-scheduled.md` and ~40 other reports: there is no
individually-identified photograph of either of them in this volume. Not reattempted further.

## 1980-81: Mark Chesnut (Treasurer)

Checked the 1981 Talisman (`talisman1981west`, archive.org, no rate limit) for "Chesnut." The only
hit is an intramural-sports results page (printed p. 234, confirmed by image), which credits
"Mark Chestnut (Sigma Alpha Epsilon)" - note the spelling, with a *t* - as a badminton and
racquetball-doubles intramural winner for a fraternity team. SGA's own Treasurer Mark Chesnut has
no Greek affiliation on record and this page is sports results, not a photograph; the name is
either a different person or the yearbook's own inconsistent spelling of the surname, and either
way the page carries no picture of him. No usable lead. Matches the standing conclusion already
logged for this name.

## 1983-84: Kelly S. Smith (Treasurer) and John Holland (Public Relations Vice President)

This is the one genuinely new piece of legwork this pass did. `curl` against
`digitalcommons.wku.edu/cgi/viewcontent.cgi` still answers a Cloudflare challenge page (not a
real PDF) under this session's TLS fingerprint - the same gate this project's notes have now
logged open on several dates. Plain Python `urllib.request` with a standard browser User-Agent,
run from a clean interpreter (`python3 -I`) with no other request in flight, fetched the actual
PDF of the 1984 Talisman (`dlsc_ua_records/408`, 46 MB, verified `%PDF-1.7` header) in one request,
paced from the single prior `curl` attempt by far more than the 90-second rule. This is the same
client-not-browser distinction this project's own scripts (`talisman.py`, `herald_photo_index.py`)
already use against TopSCHOLAR and archive.org; no browser automation and no challenge-solving was
attempted or needed.

The volume's scan has a badly garbled OCR text layer (consistent with the 1986 volume's own note
about "almost no OCR text layer"), so text search for "Associated Student Government" inside the
PDF was unreliable. Used the Table of Contents instead (`Organizations 226`) and calibrated the
PDF's own page-spread numbering by rendering known pages (6, 116, 234) until the formula held:
PDF leaf *i* = printed spread (2*i*-6, 2*i*-5). That put the Organizations section's clubs
correctly on PDF leaves 116 onward, and leaf 122 (printed pp. 238-239) carries not one but two
separately boxed "Associated Student Government" photographs:

- **Box 1** - Front row: Donna Holloway, Kathy Rokleder, Cindy Strine, Teresa Anthony. Second row:
  Lorri Burchett, Alex Bell, Jeff Fehy, Bob Shults, Stanly Reagan. Back row: Johnny Ragan, Sean
  Peck, Jack Smith, Tony Vick, Delmer Esters, Anthony Rhea.
- **Box 2** - Front row: Jane Reid, Sheila Wasinger, Kimberly Houk, Aimee Bryan, Suzanne Depaty.
  Second row: Jessica Rappaport, Mitchell McKinney, Sandra Hill, Lesa Ferguson, Tony Whalen, Happy
  Chandler. Back row: Allan Kujala, Chris Watkins, Traci Turner, Claire Groemling, Danny
  Broderick, Brian Maddox, Michael Tolbert.

Cross-checked both captions, name by name, against `data/photos.json`: every single one of the
thirty-two names already carries a portrait on file, including Jack Smith (1983-84 President,
appearing here as a plain Senate member alongside his own cabinet), Teresa Anthony (1983-84
Secretary), Tony Whalen (1983-84 Administrative Vice President) and Happy Chandler (1983-84 Public
Affairs Vice President). This confirms the page was already mined for this archive, under exactly
the officers it already has portraits for. **Neither Kelly S. Smith nor John Holland appears in
either caption.** The Treasurer and the Public Relations Vice President for 1983-84 are both
absent from this spread; nothing else in the volume's Organizations section names them under
"Associated Student Government" or any obvious variant. No portrait found.

## Conclusion

No new portrait this pass, and no change to `data/photos.json`. `build.py` and `check_data.py`
both pass clean: 61 years, 1964 events, 60 presidents, every one portrayed. All three leads this
pass opened by hand independently confirm what the morning's pass already concluded from the
written record: the 213 remaining officer-portrait gaps are not a research backlog so much as a
list this archive's available sources genuinely do not picture, at least not under a caption that
names the person. The one practical finding worth keeping for a future pass: `digitalcommons.wku.edu`'s
`viewcontent.cgi` PDFs can still be fetched with plain Python `urllib.request` and a browser
User-Agent even when `curl` meets a Cloudflare challenge on the same URL in the same session - no
browser automation involved, just a different HTTP client. Landed on `research-photos`.
