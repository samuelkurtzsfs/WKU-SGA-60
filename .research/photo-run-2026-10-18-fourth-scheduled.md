# Photograph run, 18 October (fourth scheduled pass): the Steve Wilson lead run to ground and closed, three more names spot-checked by web search

## Priorities 1, 2 and 4: reconfirmed, unchanged

Checked against the current `data/years.json` and `data/photos.json` before touching anything:

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait.
- **Priority 2** (every other student body president or student regent): zero gaps. All 73
  `leaders` records across 61 years carry a portrait.
- **Priority 4** (years with no photograph at all): zero. Every year carries at least a leader
  portrait or a year-level photograph.

`python3 scripts/portrait_gap.py --list` still reports 189 officer slots with no portrait, held by
159 distinct people, 157 with no portrait anywhere in the file — numerically unchanged.

## Network state, retested fresh

- `cgi/viewcontent.cgi`: HTTP 403, 5,664-byte Cloudflare challenge page. Still closed.
- `web.archive.org`: `curl: (35) Recv failure: Connection reset by peer`. Still closed.
- `archive.org` (item/download host): open, confirmed with a real PDF-text and two real page-image
  pulls this run.

## Steve Wilson (Judicial Council Chairman, 1978-79), left open by the previous pass, run to ground

The prior pass today found the alphabetical index of `talisman1979west` carrying
`Wilson, Steve Alan 296, 318, 320, 336` and left the lead open rather than ruling it out from a
body-text search alone, per the method `SGA-60-AGENT-INFO.md` recommends. Pulled the plain text and
the word-coordinate XML and checked all four index pages properly:

- **p. 296** — a Young Democrats club photograph, caption ending "(Back row) J. Rue, S. Wilson."
- **pp. 318-320** — the Greek Week feature. Body text: "Steve Wilson, who coordinated Spring Sing
  for the SAEs, said the brothers practiced for 2½ weeks," and a photo caption naming a barbershop
  quartet of "Scott Neel, Jon Rue, Kreis McGuire and Steve Wilson."
- **p. 337** (indexed as 336, off by one in the OCR's own page-number line) — the **Sigma Alpha
  Epsilon** fraternity composite photograph. Pulled the actual leaf image
  (`archive.org/download/talisman1979west/page/n338.jpg`) to check it, not just the caption text.
  It is a single unlabeled group shot of roughly 40 men in five rows in front of the fraternity
  house, captioned "(Front row) D. Pelino, C. Warren, J. Rue, B. Johnson, L. Heffington,
  G. Hernandez, T. Elwert, B. Thompson, B. Moore, T. Briske, S. Robertson, S. Wilson. (Second row)
  ... (Third row) R. Carey, R. Poling, **S. Thornton**, M. Murphy ..." — Steve Thornton, the 1978-79
  ASG president, is a brother in the same chapter and the same photograph, two rows back from
  Wilson. There is no independent evidence anywhere in the volume connecting the ASG Judicial
  Council to SAE or to this specific Steve Wilson — "ASG" and "Judicial" never co-occur in the
  book's text at all, so the Talisman does not appear to have photographed that office in 1978-79
  by any route. And even granting that this Steve Wilson is the same man as the officer, a name
  list against an unlabeled 40-person group photograph gives no way to point at his specific face —
  exactly the David Bass problem the previous pass correctly ruled on, at a larger scale. **Not
  used, and now genuinely closed rather than left open**: every one of the four indexed pages has
  been read, and none is an individually captioned photograph of Steve Wilson.

## Three more names spot-checked by web search

`Cindy Chiapetta` (Chairperson, Public Relations Committee, 1995-96), `Terra Swanson`
(Chairperson, Academic Affairs Committee, 1995-96) and `Trent Lyda` (City Council Representative,
1992-93) — all three distinctive enough names to search without a flood of false positives, and
none previously recorded as checked in this file. No result named any of the three in connection
with WKU or its student government; hits were unrelated SGA pages (constitutions, minutes,
candidate packets from other years) and unrelated people sharing a first name. Closed as leads for
this run; none is ruled out for all time, since a site:-restricted search on `wkuherald.com` would
need the Herald's own search API rather than general web search to be exhaustive for the 1990s.

## No portrait found or added this run

No file in `data/photos.json` or `data/photos/` changed. The 189-slot gap is numerically
unchanged. This run's contribution is properly closing the one lead left open from earlier today
(Steve Wilson — read, checked against the page image, correctly not used) and three fresh negative
checks, so a future run starts from a smaller, better-documented open list rather than re-opening
Wilson from the same half-finished state.

## Checks

`python3 scripts/build.py` then `python3 scripts/check_data.py`: clean. 61 years, 60 presidents, no
missing leader portrait, no year without a photograph. Working tree was already even with
`origin/research-photos` (no new commits on `main` to merge this pass).
