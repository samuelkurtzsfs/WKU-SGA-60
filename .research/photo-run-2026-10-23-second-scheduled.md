# Photograph run, 23 October (second scheduled pass): the David Young IIIF lead run to ground, two more archive.org-era names checked, both blocked routes retested — no new portrait

## Priorities 1, 2 and 4, reconfirmed directly against the file before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry a
  portrait in `data/photos.json`, unchanged since August. The trigger's stored prompt still
  describes them as unfound; they are not.
- **Priority 2**: zero presidents and zero student regents without a portrait, across all 61 years.
- **Priority 4**: every year carries at least one year-level photograph.
- **Priority 3** (officer/Senate gap): `scripts/portrait_gap.py` reports 188 officer slots / 158
  people with no portrait in any year — unchanged from every pass this week.

## Network state, retested fresh

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — HTTP 403, full browser navigation headers sent.
  Still closed.
- `web.archive.org` — connection reset mid-exchange at the egress proxy. Still closed.
- `archive.org` (plain item/download host, including the IIIF image endpoint) — open and used below.
- `wkuherald.com` WP-JSON — open.

## The David Young lead from the 21 October third-scheduled-pass note, finally fetched

That note had worked out the mechanics — `talisman1979west`, index entry "Young, David Paul 289",
leaf 291 by a +2 offset — but the IIIF window closed before the fetch completed. This pass the route
was open: fetched leaves 288, 290, 291 and 292 of `talisman1979west` cleanly (HTTP 200 each, genuine
JPEGs). None is a portrait of David Young. Leaf 291 (printed p. 289) is a two-page feature on ASG
entertainment programming ("Making news about entertainment") whose body text names David Young,
administrative vice president, in a quote about the new constitution — the index page number was
pointing at a text mention, not a photograph, exactly the trap CLAUDE.md's page-image rule exists to
catch. Leaves 288 and 290 (pp. 288/288 facing) show ASG president Steve Thornton and senator Victor
Jackson individually captioned; Young appears in neither. **This closes the David Young lead as a
text-only hit, not a pending one** — the next run should not re-fetch it.

While the IIIF route was open, also worked two more archive.org-era gap names end to end:

- **Mark Chesnut** (Treasurer, 1980-81): `talisman1981west` index gives "Chesnut, Mark Cameron 234".
  Calibrated the volume's own leaf offset independently (leaf 237 = printed p. 233, so offset +4) and
  fetched leaf 238 (printed p. 234): an intramural-sports results page listing "Mark Chestnut" (note
  the extra *t* — the Talisman's own spelling, not a transcription slip here) twice among badminton
  and racquetball standings, text only, no photograph. A full-text search of the volume turns up no
  senior-portrait caption for him (only "WILLIAM G. CHESNUT, Berea" nearby in the portrait section,
  a different person by middle name). Closed as text-only, not pending.
- **Vern Pulman** (Representative-at-Large, 1974-75): searched the full text of both `talisman1974west`
  and `talisman1975west` for "Pulman" and the variants "Puhlman"/"Pullman" — zero hits in either
  volume, under any spelling. Not a fetch-window problem; the name is not in these two books at all.
  Closed as absent from the only archive.org-held Talisman years for this academic year.

Chris Millay and Dwight Austin (1986-87) were already closed as text-search misses by the 21 October
third-scheduled-pass note; not re-tried here. Alice Wicks (1978-79) was already closed there too, on
the index having no page number for her at all; not re-tried here. Steve Wilson (1978-79) was closed
on 18 October after a full page-image check; not re-tried here.

**This exhausts the archive.org-reachable portion of the current gap list.** Every gap name that
falls inside a year archive.org actually holds for Talisman (1971-1981, 1986, 1987, per the 21
October third-scheduled-pass note's `advancedsearch.php` query) has now been run to ground, by name,
through this route: a photograph, a text-only mention, or no appearance at all. The remaining 150+
names fall in years (1988-2002, 2003-2025) this host does not hold, or have already been swept
through `wkuherald.com`'s search API without result. Nothing further is reachable through either
open route under the current gap list.

## Conclusion

No new portrait landed. `python3 scripts/build.py` and `python3 scripts/check_data.py` both exit
clean against the unmodified tree (61 years, 1964 events, 60 presidents, no missing leader portrait,
no year without a photograph). Nothing in `data/` changed this run. Landed on `research-photos`.

## For the next run and for the project owner

The genuine remaining work — portraits for the 158 cabinet/Senate officers still missing one — is
now blocked on exactly two things: `digitalcommons.wku.edu/cgi/viewcontent.cgi` (the only route to
the 1988-2002 Talisman PDFs and to Herald issues past 2004) and `web.archive.org` (the only route to
the SGA website's own officer pages, ~1997-2010). Both have read as closed on every test across at
least ten consecutive scheduled passes spanning four days (20-23 October), this one included.
`archive.org`'s plain host and `wkuherald.com` stay open and are now substantively exhausted against
the current gap list — this pass closed out the last three untried archive.org-era leads (David
Young, Mark Chesnut, Vern Pulman), all negative. Until a person restores one of the two blocked
routes, or the trigger's stored prompt is corrected so it stops re-describing four already-found
portraits as the top priority, further scheduled firings will keep re-confirming this same state
without new material to work.
