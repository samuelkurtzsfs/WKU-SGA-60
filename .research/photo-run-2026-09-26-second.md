# Photograph run, 26 September (second pass): six more officer names closed against Talisman text, both blocked routes still shut

## Starting state

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md` and `SGA-60-AGENT-INFO.md` sections 4 and
6. `research-photos` already carried `origin/main`'s tip exactly (this morning's scheduled run had
just merged and landed #605), so no merge was needed. No pull request was open. Re-confirmed the
starting facts from this morning's run rather than trusting them: 73 leader records, 0 without a
portrait; 217 executive/senate officer records without one (counting by name, not by name-and-year,
per the note the editor left about the 216-vs-217 arithmetic).

## Two long-blocked routes, tested again, both still shut

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`, tested directly against article 10893 with the
  documented browser-navigation headers: `HTTP/2 403`, `cf-mitigated: challenge`, a Cloudflare
  interactive challenge, same as every run this week.
- Did not re-test `web.archive.org` separately; this morning's run had already logged a proxy-level
  `hostname_blocked` denial on top of the Cloudflare wall, and nothing in this container's
  environment changed between the two runs.

## A yearbook-text pass over the pre-1990 officer gap, using archive.org (not rate-limited)

Six of the 217 missing officer records fall in years archive.org holds a Talisman for (1971-1981,
1986, 1987, per `SGA-60-AGENT-INFO.md`): Vern Pulman (1974-75, Representative-at-Large), David Bass
(1977-78, Activities Vice President), David Young (1978-79, Administrative Vice President), Alice
Wicks (1978-79, Secretary), Steve Wilson (1978-79, Judicial Council Chairman) and Mark Chesnut
(1980-81, Treasurer), plus two more from 1986-87 (Chris Millay, Parliamentarian; Dwight Austin,
Sergeant-at-Arms). Downloaded the plain-text `_djvu.txt` for `talisman1975west`, `talisman1978west`,
`talisman1979west`, `talisman1981west` and `talisman1987west` (one request each, not rate-limited)
and searched all eight names directly against the OCR text plus the volume's own back-of-book name
index, rather than against a keyword search that could miss an unusual caption.

**David Bass is already handled, correctly, and needed no new work.** His only appearance in the
1978 Talisman's index is p. 34, the ASG congress-meeting candid already in `photos.json` under
`years` for 1977-78 (`1977-78-asg-meeting.jpg`) with the caption naming all four people in the
photograph — Bob Moore, Bass, Sharon May and Cathy Murphy — without singling any one of them out as
an individual crop. That is the right call: the caption gives no left-to-right order, both men in
the frame are named, and cropping a face to a name without a positional cue in the caption is
exactly the misidentification risk CLAUDE.md warns against. Confirmed the file already exists at
39 KB-plus and starts `FF D8`, and that Bass, Moore, May and Murphy's individual index entries all
point to this same p. 34 group photo and nowhere else. Nothing to add.

**The other seven are genuine dead ends, checked rather than assumed:**
- **Vern Pulman** — no occurrence of "Pulman" anywhere in `talisman1975west`'s OCR text or index,
  captioned or not.
- **Alice Wicks** — indexed once, "Wicks, Alice Elizabeth", with no page number at all. The 1979
  volume's index gives a page number only where a person has an individual photo or a captioned
  appearance (compare "Bass, David Eugene 34" above); an entry with none means she was not
  photographed for this volume.
- **David Young** — indexed once, "Young, David Paul 289." Page 289 turned out to be text, not a
  photo: it is the ASG section's continuation, and it carries the one sentence that put him in the
  organization data in the first place — "David Young, administrative vice president, said this was
  done to 'force some heads-up competition' between candidates" — with no photograph of him on that
  spread. The three photographs actually on the ASG pages (287-288) are captioned to President Steve
  Thornton and committee member Victor Jackson only.
- **Steve Wilson** — "Wilson, Steve Alan" indexed at four pages (296, 318, 320, 336), none adjacent
  to the ASG section (287-289) and none captioned with any student-government content; the word
  "judicial" does not appear anywhere in this volume's text. These four pages read as an athlete's
  or club member's appearances unconnected to the ASG judicial council seat.
- **Mark Chesnut** — indexed once, "Chesnut, Mark Cameron 234." Page 234 is nowhere near this
  volume's ASG spread (which opens at p. 282, per the section's own page marker, with the year's
  administrative vice president named as Mark Wilson, not Chesnut) and the word "treasurer" does
  not occur anywhere near an ASG context in the whole volume — every "treasurer" hit is a
  fraternity's. Whatever page 234 shows, it is not this office.
- **Chris Millay, Dwight Austin** (1986-87, parliamentarian and sergeant-at-arms) — neither surname
  is indexed under a matching first name anywhere in `talisman1987west` (the only "Millay" and
  "Austin" entries found are unrelated students), and the volume's own ASG coverage names only
  president Tim Todd and treasurer Barbara \[surname cut in OCR\] — no mention of a parliamentarian
  or sergeant-at-arms at all. Confirmed by searching "parliamentarian" and "sergeant" directly: zero
  hits in the whole text.

Also confirmed archive.org holds no Talisman volume for any of the other years still in the
217-name gap that fall outside its documented 1971-1981/1986/1987 range: `talisman1969west`
through `talisman1990west` (the years not already covered) all return `503` on the same request
that returns content for a held year, so nothing has been added to the collection since
`SGA-60-AGENT-INFO.md` was last updated on this point.

## What this closes

Seven names (Pulman, Wicks, Young, Wilson, Chesnut, Millay, Austin) can be marked checked-and-not-
found against archive.org's Talisman holdings specifically — not against every possible source, per
CLAUDE.md's rule that a miss is never grounds to write "no source found" outright, but a future run
should not re-spend a request on these same eight names against the same five volumes. The
underlying `digitalcommons.wku.edu` and `web.archive.org` routes, which might still hold a Herald
photo or a Wayback-mirrored SGA page for any of these eight, remain untested this run because both
were confirmed closed before this search began.

## Checks

`python3 scripts/build.py` and `python3 scripts/check_data.py` both ran clean. No file in `data/`
changed — this run's entire diff is this log, kept for the reason every prior one gives: stopping
the next run from repeating searches this one already made.

## For the next run

- Priorities 1 and 2 (every president and student regent) remain fully done.
- The five 2025-26/2026-27 freshman/at-large senators named in this morning's report (Miles Harvey,
  Zoe Martin, Tyreesha Morris, Nolan Rongey, Carter Smith) are still the only current-decade gap;
  re-check them after they have had another semester to appear in a headline of their own, not
  before.
- The eight pre-1990 names checked this run are closed against archive.org's Talisman text; they
  are not closed against digitalcommons or Wayback, which remain worth a fresh one-shot test each
  run before assuming either is open.
- The four-year year-photograph gap (1994-95, 1995-96, 2000-01, 2008-09) is untouched again this
  run for the same reason as this morning: both leads that would close 2000-01 and 2008-09
  (articles 9903 and 7740) sit behind the same Cloudflare wall as everything else on
  `viewcontent.cgi`.
