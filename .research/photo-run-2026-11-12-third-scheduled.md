# Photograph run, 12 November (third scheduled pass): the Connor Ferguson lead closes negative, no new portrait

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carried
  a `leaders` portrait entry in `data/photos.json` before this pass started.
- **Priority 2**: `python3 scripts/check_data.py` exits clean - 61 years, 1964 events, 60
  presidents, every president and student regent has a portrait.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` reports the same 187 officer-slots
  without a same-year portrait, 155 people with no portrait anywhere, that the previous two passes
  left. Unchanged this pass - see below for why.
- **Priority 4**: every one of the 61 years carries at least one photograph. No gap.
- All six names in the current 2026-27 `organization` block in `years.json` - President Caden
  Lucas, Vice President Jakob Barker, CFO Will Derryberry, Chief of Staff Gabi Pace, Chief
  Communications Officer Cayden Bailey, Speaker of the Senate Veronica Butler - already carry a
  published portrait, so there was no untried current-year officer to chase.

## Closing the one item the prior two passes left open

Post 74058, "SGA holds final meeting of semester," had stayed HTTP 403 through four retries across
the two prior passes and was the one named lead carried forward. It answered 200 cleanly on the
same plain `curl` request this pass (wkuherald.com's REST API is intermittently rate-limited in a
way that doesn't correlate with request volume, as the prior two passes' notes already record).

Its featured media (id 72374, `https://wkuherald.com/wp-content/uploads/2023/08/0829_SGA_pj004.jpg`)
is captioned only "WKU Student Government Association Senate members stand and say their oath as
they are sworn into their new committees in the SGA chambers in Bowling Green, Ky. on Aug. 29,
2023" - a group shot naming nobody - and `/wp-json/wp/v2/media?parent=74058` returns no other
attached media. Read the article body itself rather than trusting the media endpoint alone:
Connor Ferguson appears exactly once, "The authors of the bill are Sarah Vincent, junior senator,
Ethan Taylor, junior senator, Maiah Cisco, senator at large, and Connor Ferguson, Gordon Ford
College of Business Senator," with no photograph anywhere near that paragraph. He is named as a
bill co-author, not pictured - CLAUDE.md's "a bill's author is not necessarily [in the photo]"
trap, by name. Declined. Logged in `data/photo-finds/2016-2025-notes.json`.

## Checked the rest of the 2016-2020 officer-gap list against the existing register before touching the network

`portrait_gap.py --any-year` lists twenty further 2016-17 through 2019-20 names with no portrait
in any year: Amarah Reed, Hayden Skinner-Fine, John (Jack) McKinney, Lane (Caroline) Simpson, Cody
Cox, Abhishek Bose, Ian Hamilton, Helen Vickrey, Morgan Wysong, Luke Edmunds, Nathan Cherry, Chase
Coffey, Devan Richardson, Mark Clark, Smita Peter, Lucas Knight, Ryan Richardson, Erika Puhakka,
Josh Zaczek, Cassidy Townsend, Matthew Johnson, Jason Herlick, Jillian Kenney, Tribhuwan Singh.
Grepped every one against `data/photo-finds/*.json` and `*.md` before spending a single network
request: all twenty-four already carry a documented negative search, in `_officers-n1419.json` /
`n1419-notes.json`, `_officers-n2025.json` / `n2025-notes.json`, or `_do-not-use.json`. Re-running
wkuherald.com or Talisman searches against names the register already closes would have duplicated
work already on file rather than produced anything new, so none were re-checked this pass.

## Conclusion

No new portrait this pass. The Connor Ferguson lead - the one item genuinely left open by the two
prior passes - is now closed with a real answer (not a retry-and-give-up) rather than carried
forward a third time. `build.py` and `check_data.py` both pass clean: 61 years, 1964 events, 60
presidents, every one portrayed. The remaining 155 people with no portrait anywhere are, as far as
every source this project can currently reach is concerned, genuinely not in the photographic
record - the next real move for most of them is the request already on file to WKU Archives for
SGA's own 14 February 2006 meeting photographs, which no automated crawl can fulfil. Landed on
`research-photos`.
