# Photograph run, 7 November second scheduled pass: digitalcommons HTML reachable again, PDF route still closed, no new lead

## Priorities 1, 2 and 4, reconfirmed directly against the files

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`, unchanged from the last pass.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — 61 years, 1964 events, 60 people
  have been president. Zero presidents or student regents without a portrait across all 61 years.
- **Priority 4**: every one of the 61 academic years still carries at least one photograph.
- **Priority 3** (officer/Senate gap): `python3 scripts/portrait_gap.py --any-year` reports the
  same figures as every pass since 4 November: 948 officer slots, 189 without a portrait for that
  person in that year, held by 159 people, 157 with no portrait anywhere in the file.

## digitalcommons.wku.edu: partial reopening worth recording precisely

This pass is the first in several days to find digitalcommons answering with real content rather
than a Cloudflare challenge, so the distinction matters:

- A plain item page (`https://digitalcommons.wku.edu/dlsc_ua_records/9505`, full browser headers,
  current desktop Chrome UA, one request, no burst) returned **HTTP 200 with the real page**, title
  tag, `og:title` and abstract text intact. No "Just a moment..." challenge body. Repeated against
  a second, unrelated item (`/dlsc_ua_records/8690`) with the same result.
- The series browse page (`/talisman/`) returned a genuine 404 (not a disguised challenge) — wrong
  path, not a block; the Talisman yearbooks are filed as individual items inside
  `dlsc_ua_records`, not under a dedicated `/talisman/` series path.
- **The PDF route is still closed.** `cgi/viewcontent.cgi?article=9678&context=dlsc_ua_records`,
  the actual download for the item above, still returns **HTTP 403**, 5,984 bytes, a Cloudflare
  block page, with the same navigation headers that made the item page work. So this run can read
  an item's catalogue description and abstract, but still cannot pull the scanned page or
  photograph itself off digitalcommons. That is why this does not translate into a new portrait
  yet: a caption confirms a photograph exists, but the image stays behind the 403.
- `core.ac.uk`, which mirrors some digitalcommons PDFs outside WKU's own Cloudflare, was tried as a
  possible way around this (`core.ac.uk/download/212145698.pdf`) — also 403, an HTML block page
  under a `.pdf` name, not a working alternate route.
- `web.archive.org` — direct fetch still resets the connection mid-exchange, unchanged from every
  prior pass.

So: one of three standing blocks (digitalcommons, in its HTML-only form) has partly lifted; the
PDF/image layer underneath it, and `web.archive.org`, have not.

## New method tried this pass: cross-referencing wkuherald.com photo captions against the gap list

Earlier passes searched wkuherald.com's WP-JSON endpoint by name and read article text. This pass
added a check of the **inline images and photo-gallery captions** on the matching articles, since
several recent SGA stories carry WordPress photo galleries with full identifying captions (officer,
role, date) rather than plain prose.

- Took the 75 names in the officer/Senate gap whose year is 2010-11 or later (wkuherald.com's full
  text coverage starts well before that but its photo galleries are a 2020s feature).
- Searched each by name against `wp-json/wp/v2/posts`, then pulled full content for every post
  returned in a bounded set (37 names with 1-5 hits checked in full; the top 3 hits for each of the
  29 names with more than 5 hits, mostly common first/last names landing false positives on
  unrelated articles).
- Fetched the `wp/v2/media` caption for every embedded image or gallery photo ID found (dozens of
  posts, several hundred photo IDs) and read what each caption actually names.
- **Confirmed the method works**: it reliably turns up real, specifically-captioned people — Jade
  Ismail, Julie Mischuck (spelled `Mishchuk` in `years.json`), Amelia Tucker, Caden Lucas, Rush
  Robinson, Salvador Leon Golib, Annalise Finch, Miles VanRude, Jacob Thomas and others all came up
  this way with named, dated captions. Checked every one against `data/photos.json` — **every
  single name it surfaced already carries a portrait.** None was a match for anyone still on the
  157-person gap list.
- No caption, across the whole batch, named any of the 75 gap names checked.

This is a genuine negative result rather than a method failure: the search is comprehensive enough
to keep rediscovering people this archive has already photographed, which is exactly what should
happen if the gap is real.

## Conclusion

Nothing added to `data/photos.json` or `data/photos/`. The headline change this pass is that
digitalcommons' HTML item pages are reachable again after days of being fully blocked, which the
next pass should keep testing and should try to extend to the PDF layer (`viewcontent.cgi`) where
the actual Talisman and Herald page images live — that is the route that would open new portraits,
and it is still closed. wkuherald.com's photo captions, checked systematically for the first time
this pass rather than just its article text, confirm the 157-person officer/Senate gap rather than
narrowing it.
