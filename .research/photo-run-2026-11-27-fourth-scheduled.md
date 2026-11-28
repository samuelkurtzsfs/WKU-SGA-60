# Photograph run, 27 November (fourth scheduled pass): a search-engine angle tried, still no new portrait

Baseline reconfirmed programmatically before anything else, same as the first three passes
today: all four priority presidents (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley)
carry a portrait, every president and student regent carries a portrait, all 61 years carry at
least one photograph, and `portrait_gap.py` still reports 187 cabinet/Senate-officer slots
without a portrait, held by 157 people — unchanged from every pass today.

## What this pass tried that the first three did not

The last two passes established, by direct count, that every name on the 157-person officer-gap
list has already been searched on every open route this project uses directly (local Herald
index, `wkuherald.com`'s own WP-JSON text search, `archive.org`'s Talisman holdings). None of
those routes is a general web search engine. This pass ran one, as a genuinely different method
rather than a re-walk of the same sources by hand:

- `site:digitalcommons.wku.edu` searches for officer-gap names (tried against Vern Pulman,
  1974-75) returned no page mentioning the name at all. Google does not appear to index the text
  inside these PDFs, only the landing-page metadata — so this route adds nothing over the direct
  local-index and landing-page checks already on record, and is not worth repeating for the rest
  of the list.
- A domain-restricted search (`wkuherald.com` and `wku.edu`) for a more recent name (Livi Ray,
  2023-24 Secretary of the Senate) surfaced several real text mentions — an election listing, a
  swearing-in report, a bill sponsorship, an award citation — none with a photograph or caption.
  This is the same trap CLAUDE.md names directly: a name in running text is not a name under a
  photograph. It also does not go beyond what the WP-JSON text search already covers, since both
  methods are searching the same underlying post text.
- Checked `wku.edu/sga/senate/index.php` directly on the chance the live site publishes a
  photographed senate roster: 404, that page does not exist. (The executive roster at
  `wku.edu/sga/executive/index.php`, already on file from the morning pass, is the only live SGA
  roster page found so far, and it shows headshot-free text only in any case.)

## Network gates, retested cold a third time this session

- `digitalcommons.wku.edu` landing pages: open (200), confirmed again against
  `dlsc_ua_records/412`. Inspected the landing page's own download link and social-share image
  tags on the chance of an unprotected thumbnail route: the only content link is the same
  `cgi/viewcontent.cgi` URL, and the only embedded images are the site's stock logo/icon assets,
  not a cover thumbnail. No alternate download path exists on the page itself.
- `cgi/viewcontent.cgi`: still 403 with full navigation headers and a referer set. Unchanged.
- `web.archive.org`: still resets the TLS connection at the egress proxy before any response.
  Unchanged.

## Unchanged

`data/photos.json` and `data/photos/` are unchanged this pass; only this note was added. Build
and `check_data.py` both run clean. The one open item that needs a person rather than another
automated pass is unchanged: `data/photo-finds/_for-the-editor.md` carries 13 people and 14
photograph entries, open since 8 September 2026, each needing a yes/no identification call no
further research can make. A fifth pass today should not repeat the search-engine angle tried
here against more names on the officer-gap list — it is now confirmed to surface text mentions
at best, never a caption — and should instead wait for either gate to reopen, or for a person to
clear the editor queue.
