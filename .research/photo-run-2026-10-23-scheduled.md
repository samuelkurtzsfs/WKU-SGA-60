# Photograph run, 23 October (scheduled): same stale trigger, same two closed routes, no new portrait — a new route tried and ruled out

## Priorities 1, 2, 4 reconfirmed, as every pass since August has found

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry a
  portrait in `data/photos.json`, unchanged since August. This run's stored instructions still name
  them as if unfound.
- **Priority 2**: zero presidents and zero student regents lack a portrait, across all 61 years.
- **Priority 4**: every year carries at least one year-level photograph.
- **Priority 3** (officer/senate gap): `scripts/portrait_gap.py` reports 188 officer slots / 158
  people with no portrait in any year, 156 of them with no portrait anywhere in the file — the same
  figures every pass has reported all week.

## Network state, retested fresh rather than trusted from yesterday's notes

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` (the actual PDF/file endpoint) — HTTP 403, full
  browser navigation headers sent. Still closed.
- `digitalcommons.wku.edu` landing pages (`/dlsc_ua_records/<id>`, not `viewcontent.cgi`) — HTTP 200,
  open. This is not new; prior runs have used landing pages for titles and captions while the PDF
  endpoint stayed shut.
- `web.archive.org` — connection reset by peer. Still closed.
- `archive.org` plain item/download host (including the IIIF image endpoint) — open.
- `wkuherald.com` WP-JSON — open.

## One route not described as tried before, now ruled out

A digitalcommons landing page embeds an inline image at `/assets/md5images/<hash>.png` — checked
whether this could be a per-article thumbnail that bypasses `viewcontent.cgi` entirely. Fetched one
directly (`dlsc_ua_records/6630`, a 2009-10 Herald issue already on the gap list's lead sheet): HTTP
200, a genuine 155×160 PNG, but it is bepress/Digital Commons's own generic platform logo, identical
on every item page regardless of content, not a cover or content thumbnail. Dead end; not a route
around the block.

## Conclusion

No new portrait landed. This is the fifth scheduled firing in roughly 24 hours (four on 22 October,
this one on 23 October) and, per `.research/photo-run-2026-10-22-second-scheduled.md`, at least the
second to explicitly flag that the situation itself — not the photo gap — is what now needs a
person's attention. `python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean
against the unmodified tree (61 years, 1964 events, 60 presidents). Nothing in `data/` changed this
run. Landed on `research-photos`.

**For the project owner, restated plainly because it has not changed:** this trigger fires every
few hours with a stored prompt describing four presidents' portraits as missing; they have not been
missing since August. The genuine remaining work — portraits for 158 cabinet/Senate officers — is
blocked on two routes (`digitalcommons.wku.edu`'s PDF endpoint and `web.archive.org`) that have now
read as closed on every test across at least nine consecutive scheduled passes over three days,
including this one. `archive.org`'s plain host and `wkuherald.com` stay open and have been swept
repeatedly; nothing further is reachable there under the current gap list. No agent session can
repoint or disable the trigger (permission wall recorded in `SGA-60-AGENT-INFO.md` §8: it was
created via `http_api`, not by an agent). Until a person either lowers the firing cadence or one of
the two blocked routes reopens, further firings will keep re-confirming the same state.
