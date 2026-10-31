# Photograph run, 25 October (second scheduled pass): baseline reconfirmed, both blocked routes still closed, one fresh lead checked and closed

## Priorities 1, 2 and 4, reconfirmed directly against the file before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry a
  portrait in `data/photos.json`, unchanged since August.
- **Priority 2**: `python3 scripts/check_data.py` reports 61 years, 1964 events, 60 presidents, no
  missing leader portrait.
- **Priority 4**: every year carries at least one year-level photograph.
- **Priority 3** (officer/Senate gap): `scripts/portrait_gap.py` reports 188 officer slots / 158
  people with no portrait in that year, 156 with no portrait in any year — unchanged from this
  morning's pass and from every pass since 20 October.

## Network state, retested fresh this run

- `web.archive.org` — still unreachable; `curl` gets a connection reset at the agent proxy on both
  a direct fetch and an `if_`-flagged Talisman snapshot request. Unchanged from this morning.
- `digitalcommons.wku.edu/talisman/` (the bare series listing) — still HTTP 404.
- `archive.org`'s advanced-search API — re-queried for every `talisman*west` identifier again:
  still exactly the same 19 (1943, 1946, 1947, 1963-65, 1971-1981, 1986, 1987). No new volume.
- `wkuherald.com` — open. Pulled its 10 most recent posts tagged SGA; nothing newer than the
  20 October "Pink Out" item already on file from the earlier pass today.

## One fresh lead run to ground: the 29 September fall-election senate swearing-in

"SGA senate complete following fall election" (wkuherald.com, 29 Sept 2026, post 97897) names six
newly sworn senators not yet checked for a portrait this cycle: Will Smith, Evan Sears, Max Fisher
(freshman), Joshua Gillespie (graduate), Bryson Baker (international), Samantha Brown (Gatton). The
article carries exactly one image (media 97901); its caption names only Dean Evelyn Thrasher
addressing the Senate, not any of the six senators, so it confirmed no portrait. The article body
has no other `<img>` tag and no other caption. None of the six is added to `data/photos.json`.
They remain unidentified and go on the standing gap list rather than being dropped from it.

## Conclusion

No new portrait landed. Both standing blocked routes (TopSCHOLAR's `talisman/` listing and
`web.archive.org`) were independently reconfirmed closed, archive.org's Talisman catalog has not
grown, and the one newly-published wkuherald.com article since this morning's pass that named
unidentified officers carried no usable photograph of them. `python3 scripts/build.py` and
`python3 scripts/check_data.py` both exit clean against the unmodified tree. Nothing in `data/`
changed this run; `site/` was rebuilt to confirm a clean run and then reverted, since it is never
committed. Landed on `research-photos`.
