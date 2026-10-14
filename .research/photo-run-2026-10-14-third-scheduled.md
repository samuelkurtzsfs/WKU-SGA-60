# Photograph run, 14 October (third scheduled pass): gap unchanged, network blockers re-confirmed, five more names checked and cleared

## Priorities 1, 2 and 4: reconfirmed, unchanged

Checked against `data/photos.json` and `data/years.json` before anything else, per CLAUDE.md's
"check whether an earlier run already got them."

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait, each file still a real JPEG (`FF D8` header) at its path in `data/photos/`.
- **Priority 2** (every other president or student regent): all 61 years' `leaders` records carry
  a photo in `data/photos.json`. Zero missing.
- **Priority 4** (years with no photograph at all): zero years missing from `photos.json`'s
  `years` array.

`python3 scripts/portrait_gap.py`: **189 officer slots / 159 people / 157 with no portrait in any
year** — unchanged from every pass since 13 October.

## Network routes probed fresh, not assumed

Per AGENT-LANDING's "probe rather than assume," re-tested rather than trusting the prior passes'
notes:

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — still HTTP 403, still a "Just a moment..."
  Cloudflare challenge page saved under the requested name (the trap-7 pattern). This container's
  egress proxy is the block, not WKU's server, as the 14 October second pass established; nothing
  about that has changed.
- `digitalcommons.wku.edu/talisman/` — still 404; the collection is catalogued under
  `dlsc_ua_records` (UA12/2/2), not a `talisman/` path, as already closed this afternoon.
- `web.archive.org` — connection reset by the egress proxy before any response, same as prior
  passes.
- `wkuherald.com/wp-json/...` — a multi-term query (`Mark Henry SGA`) returned a Cloudflare 403
  this pass where single- and two-term queries have answered cleanly in recent passes. Worth a
  note for whoever next uses this route: keep queries to a name only, not name-plus-keyword.
- `archive.org/download/talisman<year>west/..._djvu.txt` (plain text, not Cloudflare-gated) — still
  open and fast. Confirmed again that 1967, 1968 both return 503: archive.org does not hold those
  years, matching the established holdings note that it holds only 1971-1981, 1986 and 1987.
  That note is in SGA-60-AGENT-INFO.md section 4 (the source table), not in CLAUDE.md; an
  earlier draft of this note cited it to the wrong file.

## Five more gap names checked against archive.org's Talisman text and cleared

None of these turned up a usable portrait; recording them so a future pass does not repeat the
search.

- **Vern Pulman**, Representative-at-Large, 1974-75 — no match anywhere in
  `talisman1975west_djvu.txt`. Not a spelling-OCR miss either; tried `Pullman` and `Puhlman`
  variants, nothing.
- **Steve Wilson**, Judicial Council Chairman, 1978-79 — appears three times in
  `talisman1979west_djvu.txt`: a Spring Sing credit, a senior-portraits-section line
  ("STEVE WILSON, agriculture"), and a second Spring Sing credit as one of four men in an SAE
  barbershop quartet. (An earlier draft of this note called that third item "the surname index."
  It is not: the index entry reads "Wilson, Steve Alan 296, 318, 320, 336" and so does not match
  a search for the name as written. Corrected on editorial review, 14 October.) The conclusion is
  unchanged and now better supported: the index puts his four appearances on pages 296 to 336,
  nowhere near the Associated Student Government pages (indexed to page 53), the phrase "Judicial
  Council" does not occur anywhere in the volume, and the senior-portrait line carries no SGA
  role, so it fails CLAUDE.md's identification bar even though a face exists on that page.
- **Mark Chesnut**, Treasurer, 1980-81 — `talisman1981west_djvu.txt` has only
  "Chesnut, Mark Cameron 234" in the back-of-book name index, no portrait credit or caption text
  recovered from the OCR near page 234's content.
- **Chris Millay** (Parliamentarian) and **Dwight Austin** (Sergeant-at-Arms), both 1986-87 —
  checked both `talisman1986west` and `talisman1987west`. Neither volume names Chris Millay.
  The 1986 volume's only Millay is Beth Ann Millay, a track athlete, and the 1987 volume carries
  both her and a second, "Millay, Lori Ann 52" in its index. (An earlier draft said Beth Ann was
  the only Millay in either volume. That was wrong — Lori Ann is indexed in 1987. Neither is
  Chris Millay, so the name stays cleared. Corrected on editorial review, 14 October.) Dwight
  Austin does not appear in either volume at all: the Austin index entries are Alan Earl, Robin
  Renae and Samantha Andora in 1986, Lee Ann and Sherian Salome in 1987.

These five joined the already-exhausted list from the 13-14 October passes (David Bass, David
Young, Alice Wicks, and the seventeen 2003-2022 names tried against wkuherald.com). Nothing in
`data/photos.json` changed as a result.

## What is still open

- **184 of the 189 officer portrait slots were not tried this pass.** The five names above
  account for five slots. (An earlier draft wrote 185, counting the five names as four and
  subtracting a count of people from a count of slots; the 189 slots are held by 159 people, so
  the two figures do not subtract cleanly in any case.) Most of the
  portrait gap (per the 13-14 October notes) falls in 1995-2002 and 2004-2011, the span the local
  Talisman index shows as absent from TopSCHOLAR's own holdings, compounded by the digitalcommons
  PDF route being closed at this container's network layer rather than by WKU's rate limiting. No
  pacing or retry fixes that; it needs the egress policy changed, which is outside a research
  pass's reach.
- 1966-67, 1967-68 and 1969-70 names (Carla Dotson, Patricia Lanning, Pat Smith, Mike McDaniel,
  Paul Gerard) are in the one other archive.org gap: those years are not mirrored there either
  (1967, 1968 confirmed 503 this pass), so they are reachable only through the blocked
  digitalcommons PDF route.
- The wkuherald.com WordPress route is intact but should be queried by name alone, not
  name-plus-keyword, after this pass's one observed multi-term 403.

## Checks

`data/photos.json`, `data/photos/` and `data/years.json` are all untouched this run — nothing
cleared the identification bar. `python3 scripts/build.py` then `python3 scripts/check_data.py`:
61 years, clean, 60 presidents, no missing leader portrait, no year without a photograph, same as
every recent pass.
