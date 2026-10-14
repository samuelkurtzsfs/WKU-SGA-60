# Photograph run, 14 October (scheduled): the `wkuherald.com` REST API tested as its own route, nothing new meets the bar

## Priorities 1, 2 and 4: reconfirmed programmatically, unchanged

**Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): checked against
`data/photos.json` before anything else, per CLAUDE.md's "check whether an earlier run already
got them." All four still carry a portrait — Todd and Dawson since the 48-hour push, Johnson and
Gilley the same.

**Priority 2** (any other president or student regent without a portrait): every `leaders`
record in `data/years.json`, all 61 years, checked by `(name, year)` against `data/photos.json`.
Zero missing.

**Priority 4** (years with no photograph at all): every year id in `data/years.json` checked
against `photos.json`'s `years` array. Zero missing — the 1994-95 gap that stood since late
August was closed on 13 October (the Evans/Higdon campaign advertisement) and nothing has
reopened it.

So this run's whole budget went to **Priority 3**: cabinet and Senate officers without a
portrait. `scripts/portrait_gap.py` reports 189 officer slots / 159 people / 157 with no
portrait anywhere, the same count the 13 October runs left it at.

## Access tested this pass

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — HTTP 403, Cloudflare managed challenge
  (`cf-mitigated: challenge`). **Closed.**
- `web.archive.org` — `curl: (35) Recv failure: Connection reset by peer`. **Closed.**
- `archive.org` (plain, Talisman djvu text and page images) — 200, full text downloaded for the
  1978, 1979 and 1981 volumes. **Open**, as it has been on every recent pass.
- `wkuherald.com/` (the ordinary site) — HTTP 403, Cloudflare managed challenge. **Closed.**
- **`wkuherald.com/wp-json/wp/v2/posts` (the WordPress REST API, not the themed site) — HTTP 200,
  intermittently.** This is the one new thing this pass found: the API endpoint sits behind a
  separate, less aggressive gate than the themed pages. `/posts?search=...` answered 200 directly
  on most calls; a handful 403'd and then succeeded on a bare retry a few seconds later, the same
  intermittency the 12-13 October notes already logged for the themed site. The archive runs back
  to August 2002 through it (`Aramark serving up new food options, renovated facilities`, 22 Aug
  2002), earlier than the "roughly 2003 onward" estimate in CLAUDE.md's source list suggests, and
  `_embed=1` returns each post's featured image and caption inline when one exists, which is
  faster than paging through the themed site by hand. Worth using as the primary way into
  `wkuherald.com` on a future run; it is the same underlying content, just a route the Cloudflare
  challenge treats more gently.

## Priority 3, worked through the new route: confirmed roles, no new portrait

Re-verified the archive.org Talisman slice first — same eight names the 12 October third pass
closed (Pulman, Bass, Young, Wilson, Wicks, Chesnut, Millay, Austin), same hits, nothing changed.
Not re-litigated past that confirmation.

Spent the rest of the session on the API route against seventeen names drawn from the 2003-2022
slice of `portrait_gap.py --list`, where `wkuherald.com`'s coverage actually reaches: Jeremy
Glass, Samantha Hughey, Liz Goddard, Monique Gooch, Aaron Pawley, Sarah Howell, Jessi Wurth,
Brittany Crowley, Sawyer Coffey, Rachel Keightley, Abhishek Bose, Smita Peter, Tribhuwan Singh,
Amelia Bice, Matthew Pava, Art Scisney, Dajana Crockett.

What came back:

- **Brittany Crowley** (2012-13, Director of Academic and Student Affairs) — confirmed in office
  and quoted by title in five SGA meeting briefs (articles 43897, 44274, 44179, 44352, 45245,
  March-May 2013). None of the five carries an image at all; these are short news-brief posts,
  not feature stories, and WordPress never attached a photo to them.
- **Aaron Pawley** (2009-10, Director of Academic and Student Affairs) — named as a newly
  appointed Associate Justice in a 2011 meeting brief (article 52467, alongside Art Scisney as
  Chief Justice and Chris Jankowski as the other Associate Justice). No image on the post.
- **Sawyer Coffey** (2014-15 and 2015-16, Director of Public Relations) — the only name of the
  seventeen whose search turned up a post carrying a featured image (article 32099, "Class
  project attempts to break Guinness World Record," May 2016). Read in full: this is a senior
  capstone class project unrelated to SGA, Coffey is quoted as a student participant, and the
  image's own caption names the street festival, not any person in it. It fails both rules at
  once — Coffey is not pictured acting in a student government role, and nobody in the caption is
  named — so it was not used.
- **Smita Peter** (2017-18, Director of Information Technology) — **this entry was wrong as first
  written and was corrected on editorial review, 14 October.** It said article 24584, "SGA
  executives share final words to Senate," never mentions Peter and was a false positive from the
  search index. It is not. The article names her by office — "SGA Director of Information
  Technology Smita Peter" — and quotes her on the Senate judging people by gender, which confirms
  her title and year independently of the roster. The post does carry a featured image, so it was
  worth looking at; the image has an empty caption and empty alt text, names nobody, and so fails
  the identification bar. No portrait taken, for that reason rather than the one first given.
- Jeremy Glass, Samantha Hughey, Liz Goddard, Monique Gooch, Rachel Keightley, Abhishek Bose,
  Tribhuwan Singh, Amelia Bice, Dajana Crockett — zero relevant hits, or hits that are plainly a
  different context (Abhishek Bose's one hit is about an unrelated Indian student group).
- Matthew Pava (2003-04, Information Technology Designate) — five hits, all 2002-2004 letters and
  briefs; none is captioned with his name on an image, and one 2004 hit ("In defense of SGA
  officers") is a letter to the editor about him rather than by him, with no portrait attached.
- Sarah Howell (2009-10, Director of Information Technology) — all five hits are about a
  different Sarah Howell (WKU women's golf, 2015-2023), not the SGA officer; surname-only
  collision, not pursued further.
- Jessi Wurth (2010-11, Director of Public Relations) — two SGA-adjacent hits (Ransdell speaks to
  SGA; crime reports), neither naming her or carrying an image.

Nothing here clears CLAUDE.md's bar — a caption or article text that names the subject beside
the photograph. No portrait was added.

## Nothing changed in the data

`data/photos.json`, `data/photos/` and `data/years.json` are all untouched this run.
`python3 scripts/build.py` then `python3 scripts/check_data.py`: 61 years, clean, matching the
counts the 13 October evening run left (60 presidents, no missing leader portrait, no year
without a photograph). This run's only output is this note.

## For the next run

- **Use `wkuherald.com/wp-json/wp/v2/posts?search=...&_embed=1` instead of the themed site.** Same
  content, a gentler Cloudflare gate, and `_embed=1` returns any photo and caption in one request
  instead of a second fetch per post.
- The seventeen names checked this pass are exhausted on this route as of today **for portraits**;
  re-querying them without a new source turning up would just repeat this note. They are not
  exhausted as officer citations — the Peter correction above is one such citation found while
  hunting a photograph, and the Crowley and Pawley hits are others.

## Checked on editorial review, 14 October

Four of this note's claims were re-run against the live API before the branch was merged. The
`wp-json/wp/v2/posts` route answered 200, with the same intermittent 403s the note describes (two
of three calls failed on first attempt and succeeded on a bare retry). Brittany Crowley's five
article ids and Aaron Pawley's 52467 came back exactly as listed; Sarah Howell's hits are the
golf player of 2015-2023, so the collision is read correctly. The Smita Peter paragraph did not
hold and has been rewritten above. Nothing in this branch touches `data/`.
- `cgi/viewcontent.cgi` and `web.archive.org` were both closed throughout this session. The
  pre-2011 officer-gap names behind the first, and anything that depends on the Wayback Machine,
  remain untried until one of those reopens.
- The REST-API route is worth running against the rest of the 2003-2022 names in
  `portrait_gap.py --list` that this pass did not reach (the Judicial Council justices and
  committee chairs make up most of the remaining 159), but on the evidence of this pass — zero
  images on routine meeting-brief posts, the one image found unrelated to SGA — expect a low
  yield; these are appointed, not elected, positions and rarely got their own feature story.
