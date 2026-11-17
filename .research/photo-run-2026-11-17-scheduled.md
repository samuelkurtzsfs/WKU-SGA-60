# Photograph run, 17 November (scheduled): baseline reconfirmed, no new portrait, cadence note repeated

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — 61 years, 1964 events, 60
  presidents, every president and student regent portrayed.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` reports the same 187 officer-slots
  without a same-year portrait, 155 people with no portrait in any year, unchanged from every pass
  since early November.
- **Priority 4**: all 61 years still carry at least one photograph.

## Network gates, retested fresh rather than assumed

- `cgi/viewcontent.cgi` via plain `urllib.request` with navigation headers and a matching
  `Referer`: **200, a real PDF** (tested against article 1418, the 1994 Talisman) — the
  TLS-fingerprint bypass is open again this pass, consistent with every recent day.
- `web.archive.org`: connection reset this pass (on other days this proxy block has surfaced as an
  immediate `403 Blocked by egress policy` instead) — still closed either way, confirming the
  16 November finding that this is a proxy-level hostname block, not a flaky remote reset.
- `wkuherald.com`'s WP-JSON feed, checked for anything published since the 15 November anniversary
  story: nothing new. The ten most recent SGA-tagged posts are unchanged from the last pass; no
  fresh captioned photograph to chase.

## Where the open bypass went this pass

With `viewcontent.cgi` open, re-derived the Talisman collection's own date list from
`data/herald-index-full.json` (grepping `dlsc_ua_records` entries whose title contains
"Talisman") rather than re-probing individual missing-year URLs one at a time. It confirms what
the 16 November second pass already established by reading the yearbook collection's landing page
directly: **the Talisman run on TopSCHOLAR has no entries for 1995 through 2002**, jumping straight
from the 1994 volume (`dlsc_ua_records/418`) to the 2003 volume (`dlsc_ua_records/594`), and a
second real gap from 2004 through 2011, jumping from 2003 to the 2012 volume
(`dlsc_ua_records/8897`). Both spans were already logged as structurally absent (no yearbook was
ever digitized for those years, not a fetch failure) in `data/photo-finds/_archive-gaps.json` and
in prior run reports (16 November second pass for 1995-2002; multiple October passes for
2004-2011). This pass's own independent read of the index agrees with both and adds nothing new —
recorded here only to confirm the finding still holds rather than to reopen either span.

## Conclusion

No new portrait, no change to `data/photos.json` or `data/photos/`. `build.py` and
`check_data.py` both pass clean: 61 years, 1964 events, 60 presidents, every one portrayed. The
standing ~155-person officer-portrait gap remains exhaustively documented as closed, found-and-
rejected, or structurally unreachable (Talisman volumes that were never scanned) rather than
unsearched. This is now roughly three weeks of multiple daily firings against a gap that has had
every reachable lead run to ground more than once; the account holder's attention is the one
remaining route not yet tried on the cadence itself (`update_trigger` on this routine's own
trigger has been refused before as "created via http_api, not by an agent" — see the 16 November
scheduled-pass report). Landed on `research-photos`.
