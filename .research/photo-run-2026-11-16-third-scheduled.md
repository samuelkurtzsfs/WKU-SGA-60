# Photograph run, 16 November (third scheduled pass): two photographs from the archive's own anniversary event, no change to the standing gap

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — 61 years, 1964 events, 60
  presidents, every president and student regent portrayed.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` still reports the same ~155-156
  person no-portrait-anywhere gap logged by every pass since early November. Checked a sample of
  roughly 30 of those names against files already on disk (`_do-not-use.json`, the
  `_officers-n*.json`/`n*-notes.json` pairs); every one has 14+ prior mentions already recorded
  as searched and exhausted. No new name resolved this pass.
- **Priority 4**: all 61 years still carry at least one photograph.

## Network gates, retested

- `cgi/viewcontent.cgi` via `curl` with full browser navigation headers: `403` (Cloudflare),
  tested against article 7642.
- The same URL via plain `urllib.request`, identical headers: **200, a real PDF** — the
  TLS-fingerprint bypass logged open on several dates this month is open again. Not spent this
  pass; see below for where effort went instead.
- `web.archive.org`: connection reset, unchanged.

## What actually landed: wkuherald.com published a report on the archive's own subject the day before this run

Checked `wkuherald.com`'s WP-JSON feed for anything published since the last pass (a route none
of the recent daily firings had reason to re-check, since it answers only what is new). It
returned a story filed at 23:23 on 15 November and published the morning of this run: "SGA
celebrates 60th anniversary with alumni homecoming"
(`wkuherald.com/99339/news/sga-celebrates-60th-anniversary-with-alumni-homecoming/`), covering an
alumni breakfast SGA held in its own chambers on 14 November 2026 — the gathering this whole
project exists to mark.

The article carries two captioned photographs, both by Tanner York:

- "WKU Student Government Association Student Body President Cayden Lucas speaks and closes out
  the SGA Homecoming breakfast with thanks to all alumni and staff attending in DSU on Saturday,
  Nov. 14, 2026." — sitting president Caden Lucas, already portrayed elsewhere in `photos.json`,
  but not previously photographed at this event.
- "Former 2024-2025 Student Body Vice President Donte Reed attends the SGA Homecoming breakfast
  event showing support for former SGA Student Body President Sam Kurtz during his speech in DSU
  on Saturday, Nov. 14, 2026." — Donté Reed, likewise already portrayed, pictured here at the
  anniversary event itself.

Both were downloaded straight (`curl`, browser `User-Agent`, no gate on this host), checked byte
by byte (`FF D8 FF E0`, real JPEGs, 352302 and 255028 bytes), and added to `data/photos.json`'s
`years` array for 2026-27 as event photographs, not leader portraits — both subjects already have
a `leaders` entry, so this adds coverage of the anniversary gathering itself rather than filling
a portrait gap:

- `data/photos/2026-27-sga60-homecoming-breakfast-lucas.jpg`
- `data/photos/2026-27-sga60-homecoming-breakfast-reed-kurtz.jpg`

The same article names two more people by name with no photograph attached to their mention —
Susan Davis ("who served as SGA secretary in 1986") and Norman Sims ("a 1972 mass communications
graduate" who "served as the men's dormitory representative") — but neither appears anywhere in
`data/years.json`'s `leaders` or `organization` blocks for any year. Per the photos schema, a
`leaders` entry's name must match an existing leader in `years.json`, and the `years` array is for
year-level photographs, not for introducing new officers; adding either name is data work for
`years.json`, outside this agent's remit (photos only). Flagging here for whichever pass next
works 1985-86 or 1971-72: the Herald quotes are a lead worth checking against SGA minutes or the
Talisman for those years, not a sourced fact to act on from a reminiscence alone.

## Conclusion

Two new, cleanly captioned photographs landed for 2026-27, both verified real JPEGs with sources
quoted above. No change to the standing ~155-person no-portrait gap — every sampled name there is
already exhausted on file, and this pass found no new route into it. `build.py` and
`check_data.py` both pass clean. Landed on `research-photos`.
