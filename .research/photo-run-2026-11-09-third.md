# Photograph run, 9 November (third scheduled pass): the Debbie Thomas lead opened and closed unconfirmed, no new portrait

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`. Checked directly against the file rather than
  trusted from the day's earlier notes.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — 61 years, 1964 events, 60
  presidents, every president and student regent has a portrait.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` reports the same gap this file has
  carried all week. Unchanged by this pass — see below.
- **Priority 4**: every one of the 61 years carries at least one photograph. No gap.

## Network state this pass

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`: HTTP 403, standard browser navigation headers
  sent. Same standing Cloudflare block every pass today has recorded.
- `web.archive.org`: connection reset by the agent proxy's tunnel (`ws_closed_mid_exchange`),
  same as this morning's two passes.
- `archive.org`'s own download and catalogue hosts (not the Wayback replay layer) were reachable
  all pass, including the page-image route (`archive.org/download/<item>/page/n<leaf>_w<width>.jpg`
  via `scripts/talisman.py`) and the item-metadata/scandata API.

## The one open lead this morning's second pass left behind: Debbie Thomas, 1980-81

The 9 November second pass logged sixteen committee chairs searched for the first time, closing
fifteen and leaving one open: Debbie Thomas, chair of the Complaint and Suggestion committee
(named in SGA's minutes of 2 September 1980, per `years.json`), for whom the 1981 Talisman's own
index gives "Thomas, Deborah Lynn 356" — a real page reference the earlier pass didn't have time
to open.

Opened it this pass. `scripts/talisman.py`'s leaf numbers for `talisman1981west` run one ahead of
the volume's own printed page numbers in this range — leaf n360 prints as page 357, leaf n359
prints as page 356 — confirmed against the volume's own `_scandata.xml` (`<pageNumber>356</pageNumber>`
on `leafNum="360"`, one-indexed against this script's zero-indexed `--page`). Page 356 is a Juniors
class-directory grid (`site/talisman1981west`, "Juniors / Shriver-Wheeler"). The block of names set
beside the matching nine-photo row reads, top to bottom: DEBORAH L. THOMAS (Glasgow), GREGORY S.
THOMAS (Columbia), JAMES A. THOMASON (Morgantown), AMY THOMPSON (Owensboro), DANIEL THOMPSON
(Northbrook, Ill.), GEORGE A. THOMPSON (Morganfield), LYNETTE THOMPSON (Owensboro), MARY THOMPSON
(Elizabethtown), ROXANNE THOMPSON (Sebree) — nine names against nine thumbnails, Deborah L. Thomas
first and leftmost in the row.

**Not added to `data/photos.json`.** The same Talisman index also lists a second, separate
"Thomas, Debra Ann" with no page number at all, so the given name alone does not pick between two
real candidates. `years.json`'s note on the committee chair carries nothing past "Debbie Thomas" —
no hometown, class standing or middle name — so there is nothing in this archive's own record to
confirm the Glasgow junior pictured on page 356 is the SGA committee chair rather than the
unlocated Debra Ann Thomas. Matching on first-and-last name alone, with no third fact to anchor
it, is exactly the error CLAUDE.md's rules warn against (trap 4: never match by surname alone;
here it is given-name-plus-surname alone, the same risk one step removed). Logged the finding and
the reason it was declined in `data/photo-finds/_officers-truly-missing-2026-09-06.json` so the
next pass does not reopen the same page without a new fact to settle it — specifically, a
hometown, major, or middle initial recovered from the SGA minutes of 2 September 1980 or nearby
would close this cleanly either way.

## Conclusion

No new portrait this pass — the one open lead left by this morning's work was real and reachable,
but resolved to an unconfirmable name match rather than a usable photograph, which this project
treats the same as no photograph at all. `data/photos.json` and `data/photos/` are unchanged.
`build.py` and `check_data.py` both pass clean. Landed on `research-photos`.
