# Photograph run, 16 November (scheduled): baseline reconfirmed, no new portrait, cadence flagged again

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — 61 years, 1964 events, 60
  presidents, every president and student regent portrayed.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` still reports the same ~155-156
  person no-portrait-anywhere gap as every pass since early November. No new name resolved.
- **Priority 4**: all 61 years still carry at least one photograph.

Also reconfirmed the 15 November finding that Sophie Stirling and Hannah Hash (2025-26 Judicial
Council) are properly in both `years.json`'s organization block and `data/photos.json` — the
gap the 14 November pass flagged is in fact closed, not just reported closed.

## Network gates, retested

- `cgi/viewcontent.cgi` — `403` via `curl` (Cloudflare challenge), tested against article 7642.
  Did not re-test the plain-`urllib` TLS-fingerprint bypass that moved two real PDFs on 15
  November; see note below on why.
- `web.archive.org` — connection reset mid-handshake, same as every recent pass.

## The two lowest-coverage names are still closed, not just unsearched

Anne Guillory (1996-97) and Tim Hatton (1998-99) were the floor of the 14 November mention-count
analysis. Re-checked what's on file rather than re-running the searches themselves:

- **Anne Guillory** — already found and already rejected in `data/photo-finds/_do-not-use.json`:
  a Herald photograph (71:59, 2 May 1996, p. 2) identifies her by caption but the frame is
  unusably dark, 85% of the face below tone 40 in the scan, nothing recoverable with a level
  stretch. This is a found-and-discarded case, not an open lead.
- **Tim Hatton** — seven Herald appearances across 1997-98, all text-only, confirmed again in
  `data/photo-finds/n9701-notes.json`. His year (1998-99) has no Talisman on archive.org (both
  `talisman1998west` and `talisman1999west` 404 there, confirmed again this pass), and the
  viewcontent.cgi route to TopSCHOLAR's own copy is the only other way to one if it exists —
  gated by the same 403 above.

## Conclusion

No new portrait, no change to `data/photos.json` or `data/photos/`. `build.py` and
`check_data.py` both pass clean. This is now the better part of two weeks of multiple daily
firings against the same exhausted ~155-person gap, with the two lowest-coverage names on file
as found-and-rejected or fully text-only rather than unsearched. Repeating the standing note from
the 14th and 15th: a prior run already tried to fix the trigger's stale stored prompt and cadence
directly and was refused — `update_trigger` on `trig_01LjXLD8nYoNr8M2RehpHZMu` ("SGA 60 -
backlog") answered "this routine was created via http_api, not by an agent." This run's own
trigger ("SGA 60 - portraits", `trig_01YPsfcHzQEhQH6n1RPVRje1`) is a separate one but likely has
the same origin and the same restriction; no attempt was made to edit it this pass for the same
reason. Only the account holder can retime or repoint it from wherever they manage Routines.
Landed on `research-photos`.
