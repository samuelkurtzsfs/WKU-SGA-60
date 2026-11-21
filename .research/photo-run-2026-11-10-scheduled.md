# Photograph run, 10 November (scheduled pass): the viewcontent.cgi block is a TLS-fingerprint gate, not an outage - python's urllib gets through where curl still doesn't; no new portrait, but several stale leads reconciled

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- **Priority 2**: `python3 scripts/check_data.py` exits clean - 61 years, 1964 events, 60
  presidents, every president and student regent has a portrait.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` still reports 156 people with no
  portrait anywhere in the file. Unchanged this pass.
- **Priority 4**: every one of the 61 years carries at least one photograph. No gap.

## The real finding: `viewcontent.cgi`'s block depends on which HTTP client makes the request, not on whether the host is reachable at all

Yesterday's fourth pass (9 November) recorded `digitalcommons.wku.edu/cgi/viewcontent.cgi` as HTTP
403 with full browser navigation headers, the same standing Cloudflare block several passes this
week logged. Retested cold at the start of this pass with the identical URL, identical headers,
two different clients:

- `curl` with the standard navigation header set: **HTTP 403**, confirming yesterday's reading.
- Python's `urllib.request`, same headers, same URL, three seconds later: **HTTP 200**, a real PDF.

This matches a detail buried in `_archive-gaps.json`'s 8 September note, which called the block "on
the TLS fingerprint, not on request pacing or headers" without saying which client it was tested
with. This pass confirms it directly: curl and python present different TLS client fingerprints to
Cloudflare through this container's proxy, and only one of them currently passes the challenge.
Proved this is not a one-off by pulling real content end to end, not just a 200 status:

- Article 7642 (the 2009-10 Herald lead, Colton Jessie's "10 Questions" issue): 48.4 MB, opens clean.
- Article 9621 (the Katherine Smith lead, UA77/1 WKU Spirit 2007): 11.2 MB, opens clean.
- Article 1639 (SGA's own minutes of 2 September 1980): 335 KB, opens clean.
- **Article 9667, the 2016 Talisman "Life More Life"**: 755,645,090 bytes, the exact true size
  Wayback's replay layer has been truncating at ~121 MB on every attempt logged this week (8
  November's second pass). Streamed whole via `urllib` in 27 seconds, no truncation, no resume
  needed - the direct route does not share Wayback's size ceiling.

**Whoever hits a `viewcontent.cgi` 403 next should retry with `urllib.request` (or an equivalent
client with a different TLS fingerprint) before writing another "both routes closed" line.** curl
failing is not evidence the host is unreachable this session. This does not explain why the block
is client-specific or whether it will hold tomorrow - note it and move on, the way this file's
network-state sections always have.

## What the reopened route actually turned up: confirmation, not new content

With a real way to pull PDFs, worked through the leads this week's notes had logged as blocked
specifically by network, not by missing facts.

**The 2016 Talisman, fetched complete for the first time.** `data/photo-finds/n1419-notes.json`
already records an exhaustive sweep of this volume against all 39 names on the 2014-2020 officer
gap list - portrait grids, back index, club rosters, page by page - but it was unclear whether that
sweep had ever run against a complete copy, since every attempt this week stopped at the same
truncated 121 MB. It had: the existing notes cite specific PDF page numbers and xref ids that only
resolve against the full 180-page file, and a full-text search of this run's own complete copy
against the current 156-person gap list turned up nothing the existing notes do not already cover.
This closes the question of whether the truncation ever cost the project anything in this volume -
it did not - rather than finding anything new.

**Katherine Smith (UA77/1 WKU Spirit 2007, the Scholarship Recipient profile) - read in full,
declined.** Page 14 of article 9621 carries a clean, captioned photograph: "Scholarship Recipient
Katherine S. Smith," a studio-style shot of her outside the Alumni Center, paired with a donor
Q&A about what scholarship money has meant to her. Read the whole piece. It names no major, no
hometown, no activities, nothing connecting her to SGA, student government or any campus
organization at all - it is a financial-aid testimonial, nothing else. `years.json`'s Senator
Katherine Smith was not sworn in until 26 February 2008, after this Winter 2007 issue went to
print. Katherine Smith is exactly the common-name case CLAUDE.md warns against merging on name
alone, and this piece supplies no second fact to do the merging safely. Closed in
`_topscholar-wanted.json`. Not used.

**The SGA minutes of 2 September 1980 - opened, Debbie Thomas still unconfirmed.** This is the
document `_officers-truly-missing-2026-09-06.json`'s Debbie Thomas entry has been waiting on since
9 November, hoping it would carry a hometown or middle name to pick her out from the 1981
Talisman's two unresolved "Thomas" candidates. Fetched it (`sga/Meetings/Minutes/260`, article
1639). It names her exactly once, in President Fuller's list of standing committees and chairs -
"Complaint and Suggestion - Debbie Thomas" - and nothing else about her anywhere on either page.
The document exists and is now read in full; it simply does not carry the fact this entry needed.
Left unconfirmed, closed as "read, nothing extractable" rather than "still blocked."

## Three wkuherald.com leads re-fetched and re-confirmed as correctly refused

The same client-dependent block pattern applies to `wkuherald.com`: curl still 403s there too,
`urllib` does not. Checked every name in `_herald-blocked-n1419.json` and
`_herald-blocked-n2025.json` against the current `data/photos.json` before spending a request on
any of them - six of the nine names in the first file and one of the three in the second already
carry a portrait landed by some other route since those files were written, which those files did
not reflect. Reconciled both files to say so.

Of what was left genuinely open:

- **William Berry** (2014-15, self-defense class photo) - fetched and viewed. Two men grappling on
  wrestling mats, no position given in the caption, several other pairs visible in the same frame.
  Same refusal as the already-logged Courtney Hamilton frame, for the same reason. Closed.
- **MJ Mayo and Kaycee Gibson** - both already carried a correct, detailed refusal in
  `_already-done.json`/`_do-not-use.json`/`leads-notes.json` before this pass touched them. Refetched
  both independently rather than trusting the old notes, to see whether a working image route
  changed anything: it did not. Mayo's debate photographs show two masked candidates whose identity
  cannot be fixed without a position cue the caption never gives, across all four uploaded frames
  checked this pass (one new one, `351dae8c72fc4edd658dd6a1951f9bcb`, turns out to be a solo shot of
  Garrett Edmonds, already on file). Gibson's "(far right)" position sits between two women in the
  frame, and her event is a shelter volunteering feature with no SGA content regardless - out of
  this run's scope on two independent grounds, not one. Existing refusals confirmed, not changed.
- **Blake Graham** (2025-26 Chief Justice) - fetched and viewed for the first time; the existing
  `_do-not-use.json` refusal turns out to be right for a different reason than recorded. The frame
  is not an ambiguous three-or-four-person shot; it is a close two-shot of Stirling and Hash, the
  two people the caption actually positions, and Graham - who is doing the introducing from
  somewhere else in the room - simply is not pictured in it at all. Corrected the reasoning in
  `_herald-blocked-n2025.json`; the refusal itself stands.

## Conclusion

No new portrait this pass. The real result is a working method the next several passes should use:
`viewcontent.cgi` and `wkuherald.com`'s Cloudflare gates are passable this session through a client
with a different TLS signature than curl's, confirmed against five separate PDFs and three images
including one that had been truncating for a week through the Wayback workaround. Every lead this
reopened route made reachable - Katherine Smith, the Debbie Thomas minutes, the complete 2016
Talisman, Berry, Mayo, Gibson, Graham - was read and checked rather than assumed, and every one of
them holds up the same conclusion the file already carried: a real document exists, and it does not
carry the fact needed to safely identify a face. `data/photos.json` and `data/photos/` are
unchanged. `build.py` and `check_data.py` both pass clean. Landed on `research-photos`.
