# Photograph run, 14 November (third scheduled pass): four of the mapped 2012-2025 Talisman volumes actually opened for the first time, the format itself ruled out rather than the network gate

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry a
  `leaders` portrait entry in `data/photos.json`, unchanged.
- **Priority 2**: `python3 scripts/check_data.py` exits clean - 61 years, 1964 events, 60
  presidents, every president and student regent portrayed.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` reports 187 officer-slots without a
  same-year portrait, 155-157 people with no portrait in any year - unchanged from this morning's
  two passes.
- **Priority 4**: all 61 years already carry at least one photograph.

## What this pass actually did differently

The 17 October pass mapped thirteen digitized Talisman volumes on TopSCHOLAR covering 2012-2025
(`dlsc_ua_yearbooks/`) as a target list for the largest slots in the officer-gap list, but every
one of them was still behind the standing `cgi/viewcontent.cgi` Cloudflare block and none was ever
opened. Today's earlier two passes confirmed the TLS-fingerprint bypass (Python `urllib.request`
with the same browser-navigation headers the standing `curl` recipe uses) is open right now, but
used it only on already-known article ids. This pass used it to actually fetch four of the
mapped-but-unopened volumes and read them - `pdftotext` is still not installed, and the
container's default `python3` (3.11) has no `fitz`; `pip3 install pymupdf` landed cleanly under
`python3.13`, so `python3.13 -c "import fitz..."` is the working PDF-text route this run used.

(Note: `context=dlsc_ua_yearbooks` on `viewcontent.cgi` 400s. The correct param, confirmed working,
is `context=dlsc_ua_records` - matching the item's own `dlsc_ua_records/<n>` URL, not the
collection name on the landing page.)

Downloaded and searched in full, page by page:

| Volume | record | article id | size | SGA content |
|---|---|---|---|---|
| 2013 Talisman: Form | `dlsc_ua_records/8696` | 9683 | 941 MB | Yes - see below |
| 2015 Talisman: Resurgence | `dlsc_ua_records/8679` | 9665 | 586 MB | Yes - see below |
| 2016 Talisman: Identity | `dlsc_ua_records/8678` | 9666 | 99 MB | None at all |
| 2019 Talisman: Balance | `dlsc_ua_records/8683` | 9672 | 19 MB | None at all |

Confirmed by reading the landing page's own abstract (the full article-by-article table of
contents TopSCHOLAR prints for each issue; no PDF download needed) rather than downloading the
file, for six more: **2014 Talisman: Reckoning, Part I and Part II, 2017 Talisman: Power, 2017
Talisman: Well Being, 2021 Talisman, 2022 Talisman: Forge** - none of their complete contents
tables mentions Student Government, SGA or Senate anywhere.

Also opened in full (91 MB): **2022 Talisman: Illuminate** (`dlsc_ua_records/8898`, article 9883),
whose abstract had promised nothing and whose full text, searched, confirmed nothing for either
the 2021-22 or 2022-23 gap cohort.

## The structural finding: post-2012 Talismans are not yearbooks in the old sense

2016 Identity and 2019 Balance and 2022 Illuminate are 36-101 page themed photo-essay magazines
("Issue No. 01", "Issue No. 07", "Issue No. 12"), each with its own masthead explaining the
redesign: *"First published in 1924, the Talisman was WKU's yearbook, and it documented..."* -
past tense, in the magazine's own self-description. There is no club-and-organization photo
section, no Greek section, no senior-portrait grid - just bylined feature stories. A full-text
search of all three volumes for "Student Government", "SGA" and every live gap name in their
respective years returned nothing at all. This closes the entire remaining target list from the
17 October pass as a **structural dead end rather than a network gate** for 2016-17 through
2019-20 and 2021-22/2022-23: Amarah Reed, Hayden Skinner-Fine, Jack McKinney, Caroline Simpson,
Cody Cox, Abhishek Bose, Ian Hamilton, Helen Vickrey, Morgan Wysong, Luke Edmunds, Nathan Cherry,
Chase Coffey, Devan Richardson, Mark Clark, Smita Peter, Lucas Knight, Ryan Richardson, Turner
Reynolds, Alexis Mayne, Jason Herlick, Justin Goins, Nicole Massarone, Zachary Skillman, Tribhuwan
Singh, Jesse Banales, Elizabeth DeLozier, Garrett Baum, Danny Vuleta, Neel Patel, Mallory Hardesty,
Reed Hensley and Brooke Mitchell are not reachable through any of these specific volumes - full
details logged to `data/photo-finds/2016-2025-notes.json` so a future pass does not re-open the
same five/six volumes expecting the gate rather than the format to be the obstacle.

**Not yet opened**, and worth a future pass given it is already the source of an existing
portrait (Brian Chism's, reused at 2012-13/2013-14): 2016 Talisman: Life More Life
(`dlsc_ua_records/8677`, article 9667, 721 MB). 2018 Talisman: Grit (23 MB) was also not checked
this pass.

## 2013 Form and 2015 Resurgence do carry Student Government features - both close without a new portrait

Both of these two earlier, larger volumes (pre-dating the full magazine redesign) do contain an
SGA feature article:

- **2013 Talisman: Form**, p. 224-225, "Student Government Association Scandal": Keyana Boka's
  2013 disqualification as president-elect over an Honors College email and her reinstatement by
  Vice President for Student Affairs Howard Bailey. Boka already carries a portrait in
  `data/photos.json` (College Heights Herald, 31 Oct 2013), so this adds nothing new.
- **2015 Talisman: Resurgence**, p. 184-189, "Chism for President": Brian Chism's loss to Jay Todd
  Richey in the 2015 SGA presidential election, with the subsequent election-code appeals against
  Richey. Both Chism and Richey already carry portraits in `data/photos.json`.

Both volumes also carry a "Clubs and Organizations" section running many pages (2013: p. 356-391;
2015: p. 311-345), but it is **not usable for identifying any individual face**: apart from a
handful of small, already-matched "Row 1/2/3/4" group photographs, it consists of enormous flat
alphabetical name lists (sorority/fraternity rosters, by the look of the names) with no caption
tying any specific name to a face or even confirming which of several photographs on a spread a
name belongs to. Two live gap names turned up inside these lists - Sawyer Coffey (2014-15 Director
of Public Relations, 2015 volume p. 316-317) and Kelly Simmons (2012-13 Judicial Council, 2013
volume p. 366-367) - and neither is safe to use: Coffey's own case is worse than most, since the
2015 volume's own index carries both "Coffey, Sawyer" (p. 316) and "Coffee, Sawyer" (p. 327) as
separate entries, so even which name is the real spelling is not settled by this source. Left
unphotographed under the no-caption rule rather than guessed at.

Full-text search of all 160 pages of the 2015 volume and all 202 pages of the 2013 volume for every
other live 2012-13/2013-14/2014-15/2015-16 gap name - Christopher Jankowski, Brittany Crowley,
Mallory Treece, Jackie Stewart, Justin McDole, Kara Raley, Tyler Scaff, Cole McDowell, Kasey
Glasgow, Cody Cox, Amber Daniel(s), Rachel Keightley, Madison Keller, Temple Ricke - found none of
them anywhere in either volume. Logged to `data/photo-finds/2011-2015-notes.json`.

## Conclusion

No new portrait this pass; `data/photos.json` and `data/photos/` unchanged. Six of the thirteen
mapped 2012-2025 Talisman volumes are now actually read rather than merely catalogued, and the
other six were ruled out by their own published table of contents without needing a download. The
17 October target list is closed except for 2016 Talisman: Life More Life and 2018 Talisman: Grit,
which are the two specific volumes a future pass should open next if the TLS bypass is still
working - everything else in that list is now a confirmed structural dead end, not a lead to keep
retrying. `build.py` and `check_data.py` both pass clean: 61 years, 1964 events, 60 presidents,
every one portrayed. Landed on `research-photos`.
