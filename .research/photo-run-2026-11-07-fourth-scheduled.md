# Photograph run, 7 November fourth scheduled pass: same three network blocks reconfirmed, the UA1C4/10 finding aid closed for good, a memento-aggregator route tried and found unreachable

## Baseline reconfirmed directly against the files

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`. Unchanged.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — 61 years, 1964 events, 60 people
  have been president, every one of the 61 years carries at least one photograph. Zero presidents
  or student regents without a portrait.
- **Priority 3** (officer/Senate gap): `python3 scripts/portrait_gap.py --any-year` reports the
  same 948 slots / 188 without a portrait for that person in that year / 158 people / 156 with no
  portrait anywhere, unchanged from the three passes earlier today.
- **Priority 4** (year photographs): the two standing gaps, 1994-95 and 2000-01, are unchanged.

## Network state retested cold, independently of the three earlier passes today

- `digitalcommons.wku.edu` item pages: HTTP 200, confirmed again (`/dlsc_ua_records/9505`).
- `digitalcommons.wku.edu/cgi/viewcontent.cgi`: still HTTP 403, Cloudflare challenge page, on two
  different fetch paths — a direct `curl` with full navigation headers, and the platform's own
  `WebFetch` tool (a separate code path entirely). Both blocked identically. Checked the item
  page's own HTML for any non-`cgi/viewcontent.cgi` download link (bepress sites sometimes expose
  a direct asset URL); there is none — `article-downloads.pack.js` routes everything through the
  same gated endpoint.
- `web.archive.org`: connection reset mid-exchange again. Checked the proxy's own status endpoint
  (`$HTTPS_PROXY/__agentproxy/status`) rather than just curl's exit code this time: it logs the
  failure itself as `ws_closed_mid_exchange` on `web.archive.org:443`, tunnel closed after 10
  seconds having sent 517 bytes and received 39 — a relay-level failure talking to that specific
  host, not a DNS or policy block (the host resolves and a tunnel opens). Same shape as the
  earlier three passes today; still intermittent, not closed for good.
- `wkuherald.com` WP-JSON: open this pass (`200`, real results). Tried it against four names from
  the officer gap that looked newest and least-searched by mention count (Emilee Bishop,
  Stefanie Sharpensteen, Shara Hammers, Michelle Woods) — all 2001-07 vintage, which is too early
  for wkuherald.com's WordPress full text; two returned no hits, two returned unrelated namesake
  articles. Confirms the standing point that this route only helps the post-2010 names, which have
  already been exhaustively tried in prior passes (see 3 October third pass).

## New angle tried this pass: a memento aggregator as a second path to archived digitalcommons PDFs

Tried `timetravel.mementoweb.org` as a route around the direct `web.archive.org` tunnel failure —
untried in any prior pass. It is not reachable at all: `getaddrinfo ENOTFOUND`, which this
session's tooling reports as a host outside the network policy's allowed domains, not a site-side
block. Ruled out for this session; not worth retrying unless the environment's allowlist changes.
Did not attempt `archive.ph` or a Google-cache URL fetch for the same reason after the first
lookup was refused by the session's own command classifier rather than by the network itself —
treat both as outside this session's reach rather than as open questions.

## The UA1C4/10 WKU Archives finding aid, closed for good

The third pass today flagged `digitalcommons.wku.edu/dlsc_ua_fin_aid/620` ("UA1C4/10 Student
Government Association Photos") as worth a future pass if its linked 174KB PDF or a fuller page
itemized folders by name or year. Opened both this pass:

- The linked PDF (`cgi/viewcontent.cgi?article=1619&context=dlsc_ua_fin_aid`) is still behind the
  same Cloudflare block as every other PDF on the site — HTTP 403, 5,984 bytes of challenge HTML,
  not a document.
- The landing page itself, read in full rather than just its abstract snippet: title, one-sentence
  abstract ("Images of Student Government Association members and activities at Western Kentucky
  University"), two disciplines tags, and a recommended citation. No box list, no folder list, no
  date range, no names anywhere on the page. There is nothing left to extract from this page short
  of the gated PDF.

**Closed for good as a photo lead until the PDF route itself reopens.** Nothing more to try here
that doesn't require `viewcontent.cgi` to answer.

## Conclusion

No file in `data/photos.json` or `data/photos/` changed; no portrait or year photograph added.
`build.py` and `check_data.py` both pass clean: 61 years, 1964 events, 60 presidents, all
portrayed. This is the fourth pass today and the state is unchanged from the third: the
`cgi/viewcontent.cgi` gate and the `web.archive.org` tunnel are the two things standing between
this routine and the 156-person officer gap and the two remaining year-photo gaps, and neither
opened this pass. The one new, closed-off idea this pass contributes is the memento-aggregator
route, which this session's network policy does not reach, so a future pass should not spend time
on it again. Landed on `research-photos`.
