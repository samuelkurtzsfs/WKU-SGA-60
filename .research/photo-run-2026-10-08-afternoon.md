# Photograph run, 8 October (afternoon)

Baseline reconfirmed first, by script against the current file rather than by note: all 73
`leaders` records carry a portrait, the four named presidents this routine's brief still points
at (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley) are among them, and
`scripts/portrait_gap.py` reports the cabinet/Senate officer gap at 189 slots across 159 people,
157 of them with no portrait in any year — the same figure, on the same counting rule, as every
recent run. The two standing year-photo gaps, 1994-95 and 2000-01, are unchanged.

`research-photos` had fallen three commits behind `main` (a closed-PR merge and a Lodmell/Mollozzi
style fix, none of it photograph work); fast-forwarded to `main` rather than merged, so the branch
carries nothing stale. PR #6 is closed and no open PR exists for this branch; a new one will be
opened when this run lands.

## The access picture this session

`cgi/viewcontent.cgi` answered the Cloudflare "Just a moment..." 403 challenge directly all
session, as it has for weeks. The `web.archive.org` `if_`-bypass was **open for a sustained
window** — real, magic-byte-verified PDFs on the first or second attempt throughout, after one
cold `Recv failure` reset at the very start of the session (consistent with the intermittency this
file has logged for weeks; retrying once cleared it). Used the window to reach four pre-2003
*Talisman*/Herald items this routine had not individually pulled before:

- **1984 *Talisman* ("The Touch of Red", article 1408)**, 198 pages — fetched to check the two
  standing 1983-84 gaps, Public Relations Vice President John Holland and Treasurer Kelly S. Smith.
  The OCR text layer on this volume is badly garbled (character-substitution noise throughout, not
  a parsing fault — `pdftotext` returns prose but it is not reliably searchable), so this run
  located the Organizations section by rendering contact sheets and reading them directly rather
  than by text search. Found book pp. 238-239, two captioned "Associated Student Government" group
  photographs with full rosters by row. **This is not a new find** — it is already in
  `data/photos.json` as `1983-84-asg-congress-photo.jpg`, landed by an earlier run with the same
  caveat already recorded there: the yearbook gives rows, not left-to-right order within a row, so
  no individual face in either photograph is identified. Neither John Holland nor Kelly S. Smith
  appears in either roster. Cross-checked against `data/photo-finds/n8087-notes.json` and
  `_archive-gaps.json` afterward: both names have already been read off this exact volume's index
  (Holland does not appear in it at all — the index runs Holcomb to Hollenbeck with no Holland
  between them, p. 373 of the printed book) and off the 1985 volume too, by a prior run, with the
  same negative result. Confirms rather than extends the existing dead end.
- **Herald 70:42, 28 Feb 1995 ("Cleanup draws nearly 150 workers", article 8920)** — a strong-looking
  lead for the 1994-95 year-photo gap, a well-attended, well-quoted campus clean-up story. Opened
  the full issue (22 pages, rendered and read, not just text-searched, since this volume's OCR is
  also unreliable): the story runs sixteen column-inches of text and a pull quote, no photograph
  anywhere on the page or the facing page.
- **Herald 70:12, 4 Oct 1994 ("SGA helps students avoid bookstore blues", article 8903)** — same
  1994-95 gap, same result: text only, no photograph.
- **Herald 70:9, 22 Sep 1994 ("SGA to enter queen candidate", article 8889)** — same gap, same
  result: a short item with no accompanying photograph.

So the 1994-95 gap is now checked at five separate issues across the academic year (the three
above, plus the two already on file — the Evans portrait source at 69:52 and the 70:54 election
issue, both already read by prior runs) with no usable frame at any of them. That does not close
the gap — this file's own standing rule is that a miss is never proof of absence, and the Herald
index for Aug 1994-Jun 1995 still has 46 SGA-related issues nobody has opened as a PDF — but it
raises the number of specifically-read misses rather than leaving the gap merely unattempted.

**For the next run, if the Wayback window is open again:** the unopened remainder of the 1994-95
list (46 of 50 SGA-related issues in `data/herald-index-full.json` for this range) is the
honest next step before concluding anything further about this year. None of the four items
opened this run were picked for any reason stronger than "sounds visual" — there is no
narrower, ranked list to hand off.

No file in `data/photos.json` or `data/photos/` changed. `build.py` and `check_data.py` both pass
clean. This run's only change is this note and the corresponding entry in
`SGA-60-AGENT-INFO.md`. Landed on `research-photos`.
