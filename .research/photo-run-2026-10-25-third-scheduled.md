# Photograph run, 25 October (third scheduled pass): baseline reconfirmed, both blocked routes still closed, a systematic alt-text sweep of wkuherald.com tried and abandoned as noise

## Priorities 1, 2 and 4, reconfirmed directly against the file before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry a
  portrait in `data/photos.json`, unchanged since August. Checked by reading each entry directly.
- **Priority 2**: `python3 scripts/check_data.py` reports 61 years, 60 presidents, no missing
  leader portrait.
- **Priority 4**: every year still carries at least one year-level photograph.
- **Priority 3** (officer/Senate gap): `scripts/portrait_gap.py` reports 188 officer slots / 158
  people with no portrait for that person in that year, 156 with no portrait in any year —
  unchanged from both earlier passes today and from every pass since 20 October.

## Access, retested fresh this run

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — HTTP 403, Cloudflare challenge. Tested against a
  live article and against the SGA-photographs finding-aid PDF (article 1619,
  `context=dlsc_ua_fin_aid`). Still closed.
- `digitalcommons.wku.edu/do/search/` — also HTTP 403 this pass. The gate is not limited to the
  PDF endpoint.
- Plain digitalcommons item landing pages (e.g. `/dlsc_ua_records/382/`) — HTTP 200, open, as
  always; inspected one for an embedded cover-thumbnail image that might bypass `viewcontent.cgi`
  the way a bepress platform badge does. There is none: the only `<img>` tags on a landing page
  are the DC Network icon and the TopSCHOLAR banner, both generic site assets, not per-item
  content. Confirms again that landing pages cannot stand in for the blocked download endpoint.
- `web.archive.org` — connection reset mid-exchange at the agent proxy. Still closed.
- `archive.org`'s plain item/metadata host, including `advancedsearch.php` — open. Re-queried for
  every `talisman*west` identifier again: still exactly the same 19 volumes (1943, 1946, 1947,
  1963-1965, 1971-1981, 1986, 1987). No new volume.
- `iiif.archive.org`'s page-image endpoint
  (`https://iiif.archive.org/iiif/<identifier>$<leaf>/full/<size>,/0/default.jpg`) — **open this
  pass**, confirmed by fetching a real JPEG (`talisman1979west` leaf 0, correct magic bytes). This
  window opens and closes independently of the other two; worth checking fresh each pass rather
  than assuming it shares their state. Not used to add anything this time, because every
  Talisman-era (1971-81/86-87) gap name already has a closed, specific disposition from the
  20-21 October passes (Pulman, Young, Wicks, Wilson, Millay, Austin, Chesnut, Bass) and none of
  today's remaining gap names fall in archive.org's covered years.
- `wkuherald.com` WP-JSON — open.

## One new technique tried, and abandoned partway for a documented reason

Every prior pass that used `wkuherald.com` searched a handful of names per run and read the
matching posts by hand. This pass tried to go wider: wrote a script
(`/tmp/.../wkuherald_scan.py`, scratch only, not committed) to run all 56 of the 2016-2025 gap
names through the WP-JSON search API, then grep every matching post's `alt` and `<figcaption>`
text for the person's surname, to surface any photo caption a manual pass might have skipped.

It was stopped after only 2 of 56 names, because the two completed runs showed the method
produces mostly noise rather than signal on this gap list, exactly as the "never match by surname
alone" rule in `CLAUDE.md` and `SGA-60-AGENT-INFO.md` §6 warns:

- "John McKinney" (Associate Justice, 2016-17) matched only "Sheldon Mckinney," an unrelated
  person in a 2016 Board of Regents story.
- "Ian Hamilton" (Senator, 2016-17/2017-18) matched three unrelated Hamiltons across sports,
  arts, and alumni-profile posts — none connected to SGA.

Common surnames in this gap list (Hamilton, Smith, Reed, Reynolds, Baker, and others) would have
produced the same ratio of noise across the remaining 54 names for a large time cost, and the
great majority of this list has already been searched by full name through `wkuherald.com`'s own
search across the many passes logged on this branch since mid-September — the technique was not
finding anything those earlier, more targeted passes had missed. Recorded here so a future run
does not re-invent the same wide sweep without first checking this note.

## Conclusion

No new portrait landed. Both standing blocked routes are unchanged and were independently
reconfirmed closed fresh this pass; the one newly-confirmed-open window (`iiif.archive.org`) has
no unresolved Talisman-era lead left to spend it on. `python3 scripts/build.py` and
`python3 scripts/check_data.py` both exit clean against the unmodified tree. Nothing in `data/`
changed this run. The project owner was already notified of the stuck-trigger/blocked-routes
state on 23 October; nothing has changed since, so this pass does not repeat that notification.
Landed on `research-photos`.
