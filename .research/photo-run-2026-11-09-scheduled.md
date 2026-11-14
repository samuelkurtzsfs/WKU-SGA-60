# Photograph run, 9 November (scheduled pass): both standing routes closed again, the last open lead tried and left unresolved, no new portrait

## Baseline

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`, checked directly against the file rather than
  trusted from the last note. No work needed.
- **Priority 2**: `python3 scripts/check_data.py` exits clean - 61 years, 1964 events, 60
  presidents, every president and student regent has a portrait.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` reports the same 156-person gap
  (948 slots, 188 without a same-year portrait, 156 of those with no portrait in any year) this
  file's recent passes have recorded. Cross-checked every one of the 157 unique names on that list
  against the full text of every file in `data/photo-finds/`: all 157 are already mentioned by
  full name or surname somewhere in the tracking files. There is no name in the current gap that a
  previous pass has not already touched at least once.

## Network state this pass

Probed cold at the start of this pass, before touching any lead:

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`: HTTP 403 (Cloudflare), with the standard browser
  navigation headers sent.
- `web.archive.org`, both the `/web/` replay layer and a `/cdx/search/cdx` query: connection reset
  by the agent proxy's tunnel to egress on every attempt (`ws_closed_mid_exchange`) - the same
  standing block this file has recorded on roughly half of this week's passes.
- `archive.org`'s own catalogue API (`advancedsearch.php`, a different host from the Wayback
  replay layer) and `wkuherald.com`'s WordPress API both answered normally.

Both of the two routes that have produced this project's only new portrait content since late
October were closed again this pass.

## The one live, untried lead: closed out for today

`data/photo-finds/_topscholar-wanted.json`'s "Katherine Smith" entry (item 12, UA77/1 WKU Spirit
2007, `dlsc_ua_records/8633`) was the only item in that file still carrying no status note, i.e.
the one genuinely untried lead left anywhere in the tracking files. Tried it:

- The landing page opens directly (HTTP 200, no viewcontent redirect needed for the metadata
  itself). Its contents list confirms the magazine really does carry a profile headed "Scholarship
  Recipient Katherine Smith," but the metadata gives nothing past that headline - no detail there
  ties this Katherine Smith to the Katherine Smith who sat in the 2007-08 senate, which the note
  already flagged as the condition for this lead being usable at all.
- The article itself is viewcontent id `article=9621`. That route answered HTTP 403 this pass.
  The web.archive.org id_ bypass that has opened other viewcontent PDFs this month (see the 8
  November second-pass note) was also closed this pass, on both a replay fetch and a CDX lookup.

Neither route reached the actual page, so the lead is recorded as **unresolved**, not closed: the
question of whether the profile ties this Katherine Smith to the senator is still open, and worth
retrying once either route is next reachable, but not worth re-opening the landing page again -
that part is now read and adds nothing further.

## Conclusion

No new portrait. Both of the two routes that have produced this project's only new content since
late October were closed this pass, same as roughly half of this week's passes. The 156-person gap
is unchanged, and every name on it is already recorded as checked at least once somewhere in
`data/photo-finds/`; there is no backlog of untouched names left to work through on the open
routes (`archive.org`'s catalogue, `wkuherald.com`) alone. The one lead left with no status note
has now been tried and left honestly unresolved rather than silently skipped. `build.py` and
`check_data.py` both pass clean. Landed on `research-photos`.
