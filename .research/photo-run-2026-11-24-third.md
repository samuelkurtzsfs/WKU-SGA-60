# Photograph run, 24 November (third pass)

## Baseline reconfirmed, no new check performed against already-exhausted names

Re-checked at 19:55 UTC, roughly twelve hours after this morning's two passes. Before spending
any more time re-searching the standing 155-person officer-portrait gap, checked whether every
name still open had already been searched in a prior pass: ran it against every file matching
`.research/photo-run-*.md` for the eighteen names left over from the 2018-21 slice of the gap
list (Erika Puhakka, Josh Zaczek, Cassidy Townsend, Matthew Johnson, Jason Herlick, Turner
Reynolds, Brenna Mathews, Hope Wells, Jillian Kenney, Alexis Mayne, Zachary Skillman, Tribhuwan
Singh, Elizabeth DeLozier, Justin Goins, ShyAnte'e Williams, Kayla Distler, Livi Ray, Tyreesha
Morris). Every one of the eighteen already appears in at least 9 prior run notes (several past
20). Re-running an identical wkuherald.com name search against any of them would not be new
research, so none was repeated.

- Priority 1 (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): unchanged, all four
  portrayed.
- Priority 2: unchanged, every president and student regent portrayed.
- Priority 3: unchanged, 187 gaps / 157 people / 155 with no portrait anywhere, all already
  searched multiple times each.
- Priority 4: unchanged, all 61 years carry at least one `years`-level photograph.

**Network gates, retested fresh at 19:55 UTC rather than assumed from the morning:**
`digitalcommons.wku.edu/talisman/` returned HTTP 404; `web.archive.org` reset at the TLS layer
(`curl: (35) Recv failure: Connection reset by peer`); `archive.org/download/talisman1990west/...`
returned 503. All three closed, identically to both of this morning's passes. Only
`wkuherald.com`'s WP-JSON API answered normally, and its newest post matching "SGA" is still
17 November's "SGA prepares for the holidays with new bills" (post 99560) — nothing has been
published there since the second pass checked the same feed this morning.

## No change to the record

`data/photos.json` and `data/photos/` are unchanged; `scripts/check_data.py` runs clean (61
years, 1,964 events, 60 people have been president, 1,111 legislation files). This note is the
only new file.

The two items flagged in every recent pass, and already written into the open PR's body, are
unchanged and still need a person rather than a further automated run:

1. `data/photo-finds/_for-the-editor.md` — 13 people, 14 entries, open since 8 September 2026
   (now over two and a half months), each a proved photograph whose tie to the named
   officeholder needs a yes/no editorial call that CLAUDE.md's identification rule does not let
   an automated pass make.
2. The photograph trigger's cadence against a gap that has now been searched exhaustively,
   several times over, through every reachable source. `update_trigger` was refused earlier
   ("created via http_api, not by an agent"); only the account holder can change it.

Given that both items are unchanged from this morning's two passes and are already stated in
PR #835's description, this note does not repeat them there again.
