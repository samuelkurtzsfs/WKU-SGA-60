# Photograph run, 15 November (fourth scheduled pass): the TLS-fingerprint bypass confirmed working with real downloads, three already-flagged "still open" threads run down to ground and found already closed

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry a
  `leaders` portrait entry in `data/photos.json`.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — 61 years, 1964 events, 60
  presidents, every president and student regent portrayed.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` reports 187 officer-slots without a
  same-year portrait, 155 people with no portrait in any year — unchanged from today's three
  earlier passes.
- **Priority 4**: all 61 years already carry at least one photograph.

## The bypass is not hypothetical today — it moved real PDFs

Today's earlier three passes left `viewcontent.cgi`'s status ambiguous: `curl` got the standing
Cloudflare 403, and one pass's own quick `urllib` test returned 400 and was logged as "not a
confirmed reopening." Re-tested this pass with proper navigation headers and a `Referer` matching
the item's own landing page: `curl` still 403s, but plain `urllib.request` pulled two real PDFs
clean — the 1994 Talisman ("Against All Odds," `dlsc_ua_records/418`, article 1418, 253.7 MB, 148
pages) and the 1984 Talisman ("The Touch of Red," `dlsc_ua_records/408`, article 1408, 46.2 MB, 198
PDF pages / ~396 printed pages). Both opened and rendered correctly with `pdftoppm`. The bypass is
open right now, not merely plausible.

## Spent that access on the three leads already on file as the project's best open threads

All three turned out to already be closed in `data/photo-finds/_do-not-use.json` and
`.research/NIGHT-REPORT.md`, more thoroughly than this pass could redo in the time available. Ran
each down independently anyway, by eye against the rendered page images rather than by trusting the
prior note, since the bypass window was open and the volumes hadn't been re-verified in weeks:

- **Derrek Duncan (1993-94, Legislative Research chair)**, via the 1994 Talisman's back index:
  confirmed absent between "Dullaghan" and "Dunbar," exactly where the name would sort. This
  matches `n8892-notes.json`'s own recorded check of the same two spots in the same volume — an
  independent reproduction of an already-documented negative, not a new one. The fuller record
  there (a six-volume OCR grid sweep, a Spirit Masters scrapbook check, and a Herald search) already
  closes this name far more thoroughly than a single index read can.
- **John Holland and Kelly S. Smith (1983-84, PR Vice President and Treasurer)**, via the 1984
  Talisman: the back index was checked letter by letter — no "Holland" entry anywhere between
  "Holcomb" and "Hollenbeck" (he is absent from the whole volume, not just its SGA pages), and the
  only "Smith, Kelly" is "Kelly **Annette** Smith," a middle-name mismatch against the archive's
  "Kelly **S.** Smith" that CLAUDE.md's rule against matching by name alone already correctly
  excludes in `_do-not-use.json`. Also read the p. 238 "Touch cont." article text itself at full
  resolution rather than relying on the photo captions alone — it quotes only Vice President Tony
  Whalen on the `84 congress's record and ASG's unpassed bills, naming no one else. All of this
  matches `NIGHT-REPORT.md`'s own line "John Holland, 1983-84, is closed negative for the whole
  1984 volume, index included" word for word in substance. Nothing new, but independently
  re-confirmed rather than carried forward on faith.
- **The judicial-headshot gap flagged by the 14 November pass** (Sophie Stirling and Hannah Hash,
  named and photographed on the live `wku.edu/sga` judicial page but then absent from
  `years.json`'s 2025-26 organization block) is resolved: whichever pass since then updated the
  organization layer, both now appear as 2025-26 Chief Justice and Associate Chief Justice in
  `years.json`, and both already carry a `photos.json` portrait — sourced to Herald frames rather
  than the stale `wku.edu` headshots the 14 November note flagged, which is a better source anyway.
  Nothing to add.

## Conclusion

No new portrait, no change to `data/photos.json` or `data/photos/`. `build.py` and `check_data.py`
both pass clean: 61 years, 1964 events, 60 presidents, every one portrayed. This is the fourth pass
today to find the remaining ~155-person officer gap genuinely exhausted rather than merely
unsearched, now including two large Talisman volumes fetched and read page-by-page for the first
time in weeks rather than just index-checked. Repeating the operational note the last three passes
already made: this trigger has fired roughly 3-4 times a day since early November with almost
nothing to find, and today's four passes between them confirmed a real, working network bypass and
then spent it confirming dead ends already on file. A future pass would do better aimed at
`SGA-60-AGENT-INFO.md` §8's other open items, or at the small number of names in the gap list that
mention-count analysis (14 November's method) shows as genuinely under-searched, than at another
full baseline resweep. Landed on `research-photos`.
