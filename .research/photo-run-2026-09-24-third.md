# Photograph run, 24 September (third scheduled run): the bypass window closed again, queue pruned

## Starting state

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md` and `SGA-60-AGENT-INFO.md` before touching
anything. `research-photos` had no local divergent work; fast-forwarded onto `origin/main` cleanly.
PR #581, merged earlier today (~09:26 UTC), had already landed four portraits and a Jeanne Johnson
upgrade using a `web.archive.org` bypass of `viewcontent.cgi`'s Cloudflare wall.

Re-checked the four originally-named presidents (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan
Gilley) before spending time: all four already carry a portrait. A scripted cross-check of every
`role: "president"` / `role: "regent"` leader against `data/photos.json` found zero gaps —
priorities 1 and 2 are fully satisfied. `merge_photo_finds.py` (dry run) proposes nothing new: 0
additions, 18 held FACE-PROVED-PERSON-NOT-PROVED candidates already flagged for the editor, none
of them mine to resolve.

## The bypass window closed again by evening

Tried to continue this morning's `web.archive.org` bypass against the still-open items in
`data/photo-finds/_topscholar-wanted.json`. It did not work this run, and not for lack of trying:
eight separate attempts, spaced from thirty seconds to several minutes apart, against three
different URL shapes (`/cdx/search/cdx?...`, `/web/<timestamp>/<url>`, and a bare wildcard CDX
query) all failed identically — `curl: (35) Recv failure: Connection reset by peer`, and the
agent-proxy status endpoint logs the same `ws_closed_mid_exchange` on every one, each tunnel
dying at almost exactly 10-11 seconds after connecting having sent the request and received only
39 bytes back. That is a consistent, repeatable failure, not the roughly-50/50 coin flip this
morning's report described — this evening the route is shut, full stop, for the whole session.

`digitalcommons.wku.edu/cgi/viewcontent.cgi` was retested directly too, for completeness: still
the Cloudflare "Just a moment..." 403, unchanged from every prior pass.

Plain `archive.org` (not `web.archive.org`) is a different host and stayed open throughout —
fetched `talisman1981west_djvu.txt` (1.55 MB) with no trouble. It doesn't help with this queue,
since none of the still-open items fall in a year `archive.org`'s own Talisman holdings cover, but
it's worth recording that the two hosts fail independently: a closed `web.archive.org` this
evening says nothing about whether `archive.org` is also down, and a future run shouldn't assume
one from the other.

**Lesson for the next run:** this morning's discovery is real and worth using again, but treat the
window as something that opens and closes within hours, the same as `viewcontent.cgi`'s own
Cloudflare gate has done all month. Test it fresh at the start of every run rather than assuming
either the morning's success or this evening's failure still holds.

## Housekeeping: pruned `_topscholar-wanted.json` from 32 entries to 15

This morning's report flagged this as left for a future run. Cross-checked every name in every
entry against the current `data/photos.json`: 17 entries no longer have any unresolved name left
(landed by this morning's run or by other routines since the queue was written — Eileen Forsythe,
Shelby Nitzken, Ben Redmon, and previously-portrayed people like Currie Martin, Austin Wingate,
LaDarra Starkey, Dajana Vasilijevic-Klingler, Drew Mitchell, Tyler Jury, Daniel Shaw, Katie Jeter,
Jessica Sutton). Removed those 17 so a future run's dry pass doesn't re-derive "already done" from
scratch for each one. No image or `data/photos.json` change from this step — it only edits the
worklist file itself.

**15 entries remain genuinely open**, all still blocked by the two closed routes above:

- Mallory Treece (`dlsc_ua_records/5160`)
- Lisa M. Kappler (`dlsc_ua_records/6721`)
- Corey Bewley (`dlsc_ua_records/6720`) — **already ruled out** this morning: the named article ran
  with no photograph at all. Left in the queue only because the entry's other name (Jacob Turner,
  via 6721) is unresolved; Bewley himself needs no further attempt.
- Mitchell Stevens (`dlsc_ua_records/6220`)
- Timothy Gilliam (`dlsc_ua_records/6238`) — **already ruled out** this morning: the only lead is
  four years off his recorded SGA service, too large a gap for an ordinary name to carry alone.
- Kelly Johnson, Brooke Smith, Kristin Hartley (`dlsc_ua_records/9223`, `/9224`)
- Emilee Bishop, Lucas Humble, Matt Holland, Tim Hill (`dlsc_ua_records/3695`)
- Alex Wimsatt (`dlsc_ua_records/3684`)
- Emilee England, Cacy A. Schooler, Jacob Miers (`dlsc_ua_records/6645`, `/6644`)
- Katherine Smith (`dlsc_ua_records/8633`)
- 25 names from a `talisman/` collection-wide lead, and the 2015-16 through 2019-20 senate/justice
  worklist (`_worklist-n1419.json`) referenced from the same entry
- The WKU Archives SGA-photos finding aid (`dlsc_ua_fin_aid/620`) — this morning's report says it
  was already fetched successfully and read in full (physical folders/negatives, 1961-1973 only,
  nothing digitised); kept in the queue as a pointer to that report rather than a live lead.

None of these were attempted this run beyond the routing test above — both routes that would reach
them were closed the entire session.

## The 5-year general-photograph gap

Unchanged: 1994-95, 1995-96, 2000-01, 2005-06, 2008-09. Not worked this run; the bypass that would
have been the tool for 2005-06/2008-09 was closed the whole session, and the other three have no
Talisman volume to find a photograph in at all, per the 23 September finding.

## Checks

`python3 scripts/build.py` and `python3 scripts/check_data.py` both pass clean. `data/years.json`
is untouched. The only change this run is `data/photo-finds/_topscholar-wanted.json` (32 → 15
entries); no file was added to or removed from `data/photos.json` or `data/photos/`.
