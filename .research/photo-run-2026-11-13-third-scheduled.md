# Photograph run, 13 November (third scheduled pass): network state unchanged, one new search channel tried and ruled out

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry
  a `leaders` portrait entry in `data/photos.json`, unchanged.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — 61 years, 1964 events, 60
  presidents, every president and student regent has a portrait by exact name match.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` reports the same 187 officer-slots
  without a same-year portrait, 157 people with no portrait in any year — unchanged from the
  morning and second passes today.
- **Priority 4**: all 61 years already carry at least one photograph.

Before repeating any search, checked how many times the names on the current 157-person gap list
already appear across `.research/photo-run-*.md` (160+ files). The lowest count found was 3 (Jack
McKinney); every other name clears that. This is not an untouched backlog — every remaining name
has been searched by full name at least three times, most considerably more, across the Talisman
djvu texts, the Talisman PDF route, `wkuherald.com`'s WP-JSON search, the WKU Archives UA1C finding
aid and photo album, and `wku.edu/sga`'s legacy CMS pages.

## Network state, retested fresh

- `cgi/viewcontent.cgi` — `403`, Cloudflare challenge page. Tested once against article 7642
  (2009-10 lead), same gate this project has logged on and off for weeks.
- `web.archive.org` — `curl: (35) Recv failure: Connection reset by peer`, same as every recent run.
- `archive.org` (no `www.`) — `302` redirect, open as usual.
- `wkuherald.com` — `200`, open as usual.

No change from the second pass earlier today.

## One genuinely new channel tried: Google search restricted to `wku.edu/news`

Nothing in this project's 160+ prior reports had tried routing *around* `wku.edu/news`'s
client-side search rendering (confirmed dead since 27 October) via a search engine's own index
instead of a direct fetch. Tried `site:wku.edu/news SGA senator 2022` and a direct name query
(`"Temple Ricke" WKU SGA`) through this session's web search tool.

Neither surfaced a single `wku.edu/news` article — Google's index for that query returns only
`wkuherald.com` posts, SGA's own `.docx`/`.pdf` minutes and bylaws, and one unrelated student-paper
site (`thenortherner.com`, Northern Kentucky University, not WKU). `wku.edu/news` appears to carry
little to no SGA-specific coverage in the first place, not merely coverage that is hard to reach —
so there is no article page hiding behind the client-rendered search box for this archive to go
after. The name query turned up only text mentions of Temple Ricke in senate-minutes rolls and
election-results text, no `<figure>` or captioned image anywhere in the returned pages, consistent
with the 8 November `wkuherald.com` sweep's conclusion for the rest of this cohort.

This closes `wku.edu/news` as a route for the 2016-2026 gap cohort more firmly than the 27 October
note did: it is not just unreachable by direct fetch, it does not appear to hold the material.

## Conclusion

No new portrait this pass, and no change to `data/photos.json`. `build.py` and `check_data.py`
both pass clean: 61 years, 1964 events, 60 presidents, every one portrayed. The remaining 157
officer/Senate names are, as far as every source this project can currently reach is concerned,
genuinely unphotographed in the record, barred by the no-caption rule, or behind a Talisman window
this archive does not hold (2017-18 onward: no yearbook) or a `viewcontent.cgi` gate that is closed
again this session. A future pass should keep retrying `viewcontent.cgi` at different hours rather
than re-sweeping `wkuherald.com` or `wku.edu/news` a further time for this cohort — both are now
confirmed exhausted, not merely difficult. Landed on `research-photos`.
