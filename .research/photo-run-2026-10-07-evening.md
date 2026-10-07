# 7 October 2026, evening run (photograph routine, scheduled)

## Baseline, reconfirmed against the current file

Restarted `research-photos` from current `origin/main` rather than merging: the branch's prior
commits (through the "night report of the #696 review") are already fully contained in `main`
(`git merge-base origin/main research-photos` equals the branch tip), and every PR this routine
has opened recently (through #696) was closed unmerged on GitHub even though its content landed —
the editor appears to be folding these in by another path and closing the PR rather than using
GitHub's merge button. Starting fresh from `main` avoids re-proposing already-landed content as a
new PR.

`build.py` and `check_data.py` both ran clean before any change: 61 years, 1967 events, 60
presidents, all 73 `leaders` records carrying a portrait (Todd, Dawson, Johnson, Gilley included).
`merge_photo_finds.py` (dry run) confirmed 0 proposals pending across every staged batch file —
nothing queued and unmerged. The four standing year-photo gaps were unchanged: 1994-95, 1995-96,
2000-01, 2008-09. The officer-portrait gap was unchanged at 217 slots / 174 people.

## The access window opened this session

`cgi/viewcontent.cgi` direct: still the Cloudflare "Just a moment..." 403 challenge, as every
recent run reports. But `web.archive.org`'s `.../web/<timestamp>if_/<url>` bypass answered real
PDFs all session (confirmed by magic bytes on every fetch), the first time this routine has had a
clean, sustained window in over a day. Used it on exactly the open items this file's own "for the
next run" notes pointed at, rather than re-covering ground already closed.

## The SGA-photographs finding aid, opened for the first time

`article=1619&context=dlsc_ua_fin_aid` (`dlsc_ua_fin_aid/620`) has sat unopened since 24 August
behind the same blocked route. It is a six-page text inventory of the **physical, non-digitized**
WKU Archives print/photograph collection (UA1C4/10), not a source of images: folder-by-folder
subject lists (names, dates, scope notes) for nine folders of prints and 28 negatives, 1956 to the
collection's creation. It confirms names already in the record from its earliest folders (1962-73:
Doug Alexander, Joe Gerard, John Lyne, David Porter, Bill Straeffer among others; 1968-69: Reed
Morgan, Bill Straeffer, Paul Gerard, Charles Keown) but carries no reproducible image itself — the
prints and negatives are physical holdings, not TopSCHOLAR scans. **This closes the finding aid as
a lead for good: it is not an image source, so no future run should spend a `viewcontent.cgi`
attempt opening it again.**

## 2008-09: the Kevin Smiley story has no photograph; the Gilley frame has a usable wider crop

Opened Herald 84:46 (16 Apr 2009, `dlsc_ua_records/6747`, article 7740), "All smiles, Smiley wins
SGA election." Read the full front page: the story is pure text with an election-results box (a
checkmark graphic), no photograph of Smiley or Shelton anywhere in the issue. Ruled out.

Opened Herald 84:35 (26 Feb 2009, `dlsc_ua_records/6718`, the real `article=` parameter is **7727**,
not the TopSCHOLAR item id 6718 — confirmed from the landing page's own citation meta tag) for a
possible second frame beside Reagan Gilley's existing portrait. There is no second frame: the only
SGA photograph in the issue is the one his portrait is already cropped from (front page, "Gilley
elected student regent"). The continuation on p. 3 carries no image. But the full frame — not just
the tight single-subject crop already in `photos.json` — shows Gilley with another man clapping
beside him in the SGA office, and the original caption is usable on its own terms without
identifying the second man: "Pineville senior Reagan Gilley celebrates winning the Student
Government Association student regent election after midnight on Thursday morning. Gilley won the
election by 224 votes" (credit Ryan Stone/Herald). Extracted the full embedded image directly from
the PDF (not a re-render of the page) and added it as **2008-09's year-level photograph** —
`data/photos/2008-09-regent-election-night.jpg` — closing one of the four standing gaps. This does
not touch the existing leader portrait, which stays the tighter crop of the same source.

## 1995-96: a second, better frame from the same issue as Tara Howard's existing portrait

Herald 70:54 (20 Apr 1995, `dlsc_ua_records/7934`, article 8935), "Higdon moves up; voting down," is
the source already cited for Tara Howard's leader portrait — confirmed by re-opening it that her
existing crop is the rightmost face in a four-person embrace on the front page. The full photograph
carries its own complete caption, naming all four left to right: "After election results were
announced Tuesday, (from left) Vice President-elect Jeffrey Yan, Secretary-elect Erin Schepman,
Public Relations Director-elect Kristen Miller and President-elect Tara Higdon embrace" (credit
Craig Allen/Herald). Cropped the full group directly from the PDF page at 400 dpi and added it as
**1995-96's year-level photograph** — `data/photos/1995-96-election-embrace.jpg` — closing a second
of the four gaps. Two gaps remain: 1994-95 and 2000-01.

## 1994-95 checked again and still closed

Opened Herald 69:52 (21 Apr 1994, `dlsc_ua_records/7879`, article 8881), "Evans, Higdon ready to
lead students, SGA" — the source already cited for Robert Evans' existing leader portrait. Read the
whole issue, front page and the SGA continuation on p. 3: the only SGA photograph in it is the
small headshot already on file. No further image to add; 1994-95 stays without a separate
year-level photograph.

## 2000-01 not re-attempted

Already fully read on 3 October (all seven news pages of Herald 76:52, `dlsc_ua_records/9903`) with
no usable SGA frame found (the one strong photograph in the issue, a "Blast from the Past" concert
picture, does not clear CLAUDE.md's bar for a context photograph). Not re-opened this run since
nothing has changed about that issue; it remains the one standing year-photo gap with no identified
next lead.

## Landed

`data/photos.json`: two new `years` entries (1995-96, 2008-09). `data/photos/`: two new JPEGs,
both verified by magic bytes (`FF D8`) before committing. `build.py` and `check_data.py` both pass
clean after the change: 61 years, 1967 events, 60 presidents, 217/174 officer gap unchanged, two of
the four year-photo gaps closed (1994-95 and 2000-01 remain open).

## For the next run

- The SGA-photographs finding aid (`article=1619&context=dlsc_ua_fin_aid`) is a text-only container
  list of physical holdings, not an image source. Do not reopen it looking for a photograph.
- 1994-95 and 2000-01 are the two year-photo gaps still open, both already read in full at their
  best-known Herald leads with nothing further to find there. A new lead, not another look at
  these two issues, is what either one needs.
- `web.archive.org`'s `if_` bypass was open and stable for this entire session. Treat every prior
  "closed" report as a snapshot of that session, not a standing state — keep retrying cold.
