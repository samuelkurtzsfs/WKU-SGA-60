# Photograph run, 27 November (third scheduled pass)

Baseline reconfirmed programmatically against the live data before anything else: all four
priority presidents (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley) carry a portrait,
every president and student regent carries a portrait, and all 61 years carry at least one
photograph. No new portrait this pass either.

This pass's own angle: retest the two gates this branch has logged as closed, cold, rather than
trust the last pass's reading, and check whether anything genuinely new has appeared on the one
source that updates with time (wkuherald.com), rather than re-walk the officer-gap list a third
time today — the second pass already established, by counting mentions across every
`.research/*.md` and `data/photo-finds/*.json` file, that none of the 157 names on
`portrait_gap.py --list` is untried.

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — still a flat 403 with full browser navigation
  headers set (`Sec-Fetch-Dest: document`, `Sec-Fetch-Mode: navigate`,
  `Upgrade-Insecure-Requests: 1`, a real Chrome user agent). Unchanged.
- `web.archive.org` — still resets the TLS connection at the egress proxy before any response.
  Unchanged.
- `archive.org` (Talisman djvu text and full page-image PDF) and `wkuherald.com`'s WP-JSON API —
  both still open and answering normally.
- wkuherald.com's ten newest posts tagged SGA, pulled fresh (`orderby=date&order=desc`): the
  newest is still "SGA prepares for the holidays with new bills" (post 99560, 17 November), the
  same post every pass since 23 November has already read in full and ruled out. Nothing has
  been published since. No new post to search for a photograph.

Nothing in `data/photos.json` or `data/photos/` changed. Only this note was added. Build and
`check_data.py` both run clean.

The one open item that needs a person rather than another automated pass is unchanged:
`data/photo-finds/_for-the-editor.md` carries 13 people and 14 photograph entries, open since
8 September 2026, each needing a yes/no identification call no further research can make.
