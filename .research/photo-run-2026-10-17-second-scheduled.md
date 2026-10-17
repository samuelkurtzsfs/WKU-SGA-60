# Photograph run, 17 October (second scheduled pass): the wkuherald.com route checked exhaustively against the whole officer-portrait gap, and closed

## Priorities 1, 2 and 4: reconfirmed, unchanged

Checked against the current `data/years.json` and `data/photos.json` before searching anything:

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait. Unchanged.
- **Priority 2** (every other president or student regent): zero gaps. All 60 presidents and every
  student regent carry a leader-level portrait.
- **Priority 4** (years with no photograph at all): zero. All 61 years carry at least one.

`python3 scripts/portrait_gap.py --list` still reports 948 officer slots, 189 with no portrait,
held by 159 distinct people, 157 with no portrait anywhere in the file — the same count the
morning run of today reported, and the same count most passes this week have reported.

## Network state, retested fresh

Same as this morning, re-tested rather than assumed:

- `cgi/viewcontent.cgi`: HTTP 403, the Cloudflare "Just a moment..." challenge page, 5,984 bytes.
  Tested again directly against article id 6164 (2014 Talisman, already on the morning run's
  target list). Still closed.
- `web.archive.org`: `curl: (35) Recv failure: Connection reset by peer` at the TLS layer. Still
  closed.
- `digitalcommons.wku.edu` item landing pages (not the PDF route): open, HTTP 200. Checked whether
  a landing page carries a cover thumbnail that might stand in for the blocked PDF — it does not;
  the only images on a `dlsc_ua_records` item page are the site's own logos.
- `wkuherald.com`: open, including its WordPress REST API (`/wp-json/wp/v2/posts`), which reaches
  back to August 2002.

## What this run tried that the morning pass had not: every name in the gap, searched by surname against Herald captions, not just a sample

Earlier passes have searched individual names from the 189-gap list a few at a time. This run took
the full list of 113 distinct people named in the 2001-02-through-2025-26 slice of the gap (the
part Talisman can't help with is pre-2002, where TopSCHOLAR is still the only possible source and
is still blocked; the rest is in wkuherald.com's covered range) and queried each one's full name
against the Herald's search API, reading back every returned post's embedded featured-image caption
rather than just the headline.

A caption was only counted as an identification if the person's own surname actually appears inside
it — not just inside the article text, and not just inside the search-matched headline. That bar
matters: a first pass at this caught several false positives from common surnames (a `Howard` match
pulling in an unrelated `Kat Howard`, a `Henry` match pulling in an unrelated Staff Senate photo)
before the check was tightened to require the literal surname string inside the caption text
itself.

**Result: one genuine identification, and it was already in the file.** Carter Smith, 2026-27
sophomore senator, is named directly in the caption of a Natasha Gomez photograph ("WKU Student
Government Association Sophomore Senator Carter Smith gets sworn in...", Herald, 23 Sep 2026) — and
`data/photos.json` already carries exactly this photograph under exactly this citation
(`2026-27-carter-smith.jpg`). No other name in the 113 returned a caption that named them. Several
searches returned Herald photographs of SGA meetings and election nights from the right years, but
every caption in them named only the people already on record with a portrait — presidents, vice
presidents, the CFO — never the committee chairs, judicial council members or individual senators
this gap is made of. That is consistent with what the organization layer itself shows: the
Herald's photo desk covers the executive table and the cabinet, not the committee rosters.

This closes wkuherald.com as a source for the current 189-gap, not provisionally but on an actual
full pass of the names rather than a sample. The bottleneck remains what every pass since the
Talisman-collection discovery has reported: the 13 recent-decade Talisman volumes TopSCHOLAR holds
for 2012-2025 (mapped with their `viewcontent.cgi` article ids in this morning's report) are the
real next source for 2014-15, 2016-17, 2021-22 and 2022-23, and the PDF route to them is still
Cloudflare-blocked.

## No portrait found or added this run

No file in `data/photos.json` or `data/photos/` changed. The 189-slot gap is numerically unchanged.
This run's contribution is ruling out wkuherald.com as a source for the gap as it currently stands,
confirmed by name rather than assumed, and reconfirming the network state.

## Checks

`python3 scripts/build.py` then `python3 scripts/check_data.py`: clean. 61 years, 60 presidents, no
missing leader portrait, no year without a photograph. Merged `origin/main` into `research-photos`
first (one conflict, in `.research/NIGHT-REPORT.md` itself — an append-only file where both sides
had appended a new section; resolved by keeping both).
