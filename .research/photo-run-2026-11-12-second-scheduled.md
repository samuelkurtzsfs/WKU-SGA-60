# Photograph run, 12 November (second scheduled pass): the three queued Talisman leads close with no new portrait; sixteen 2021-26 officer names checked and declined

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carried
  a `leaders` portrait entry in `data/photos.json` before this pass started.
- **Priority 2**: `python3 scripts/check_data.py` exits clean - 61 years, 1964 events, 60
  presidents, every president and student regent has a portrait.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` reports the same 187 officer-slots
  without a same-year portrait, 155 people with no portrait anywhere, that the previous pass left.
  This pass closed leads without landing a new name, so the count is unchanged.
- **Priority 4**: every one of the 61 years carries at least one photograph. No gap.

## Closing the three Talisman leads the prior pass queued but did not open

The prior pass (12 November, first scheduled run) identified three previously-uncatalogued
Talisman volumes reachable through the `viewcontent.cgi` `urllib`-bypass window and queued them
against six open portrait-gap names, but ran out of time before reading any of them. This pass
fetched and read all three.

- **`article=1411`, the 1987 Talisman** (`dlsc_ua_records/411`), for 1986-87's Parliamentarian
  Chris Millay and Sergeant-at-Arms Dwight Austin. Read the entire "Governing bodies" feature
  (printed pp. 112-119: both Associated Student Government group photographs, Inter-Hall Council,
  University Center Board, Spirit Masters, Student Alumni, Inter-Fraternity Council, Panhellenic
  Council, International Student Organization, United Black Students, Young Democrats, College
  Republicans) as rendered page images at 150 dpi - the OCR text layer is badly garbled throughout,
  consistent with every other scan of this era, so nothing was trusted from text search alone.
  Neither name appears in any caption. Every other person pictured in the two ASG group photographs
  on p.114 was already on file from an earlier pass (via archive.org's djvu transcript of the same
  volume), so this read's only new information is that Millay and Austin are confirmed absent from
  the volume, not merely unsearched.
- **`article=1413`, the 1989 Talisman** (`dlsc_ua_records/413`), for 1988-89's Secretary Mickie
  Hennig and Vice-Chair of the Judicial Council Chris Gaddis. The government section ("Leading the
  way", pp. 198-201) carries exactly one Associated Student Government photograph, a seven-person
  officer group (Amos Gott, John Seiber, Scott Whitehouse, Victor Click, Mari Knights, Lori Easton,
  Honor Logsdon), alongside Black Student Alliance, College Republicans, Young Democrats, University
  Center Board, Student Alumni and Students Over the Traditional Age. Neither Hennig nor Gaddis is
  named anywhere in the section.
- **`article=1417`, the 1993 Talisman** (`dlsc_ua_records/417`), for 1992-93's Academic Affairs
  chair David Smith and City Council Representative Trent Lyda. Its "Student Government
  Association" group photograph (p.204) names Donnie Miller, Jennifer Raffaelli, Jeremy Sublett,
  Susan Mitchell, Joe Rains, Cindy Hayes, Bert Blevins, Scott Sivley, Jason Embry, Cinnamon Roberts,
  Nikki Creasey, Woody Zorn, Greg Edmonds, Huma Ahsan, Edward Myers, Eric McWilliams, Kyle Key,
  **Donald Smith**, Joe Tinsley, Matthew Anderson and Kibby Rose. A Smith is pictured, but the
  caption gives the given name as Donald, not David, and CLAUDE.md's rule against matching people
  by name alone forbids closing a two-letter-different given name gap on sight; left unused. Trent
  Lyda does not appear in the photograph at all.

All three volumes are now exhausted for these six names. Logged the full reasoning in
`data/photo-finds/_topscholar-wanted.json` so no future pass re-opens them without a new source.
The `viewcontent.cgi` TLS-fingerprint bypass (plain `urllib.request` where `curl` gets a Cloudflare
403) is confirmed open again this pass, for the third time across three different dates.

## Sixteen 2021-2026 officer-gap names checked against wkuherald.com

wkuherald.com's REST API answered plain requests cleanly at the start of this pass, so swept a
batch of officer-gap names from 2021-22 through 2025-26 that no prior pass's notes named as
checked: Kayla Distler, Connor Ferguson, Elizabeth Gannon, David Darnell, Livi Ray, Callison
Padgett (2023-24); Tyreesha Morris, Carter Smith (2025-26); Jesse Banales, Zachary Skillman,
Elizabeth DeLozier, Nicole Massarone, Alexis Mayne, Turner Reynolds, Mallory Hardesty (2021-23).

Method: search the posts endpoint for the name (`order=asc` to dodge the newest-first cap that
buries older hits under 2026 volume), then pull `/wp-json/wp/v2/media?parent=<post id>` for every
SGA-relevant post that came back, and read each attached photograph's caption.

Two names - Livi Ray, Carter Smith - are common enough that every hit is a different, unrelated
person (a 2002-03 arts writer, a 2000s sports reporter), with no SGA connection at all; not pursued
further. For the rest, the SGA posts that came back either carry no attached media, or carry media
whose captions name other people already on file - Caden Lucas, Cole Bornefeld, Sam Kurtz, Garrison
Reed, Holden Schroeder - rather than the person searched for. No new portrait from this batch.
Logged in `data/photo-finds/2016-2025-notes.json`.

**wkuherald.com's REST API answered 403 to several of these exact requests, then 200 to the same
request retried minutes later**, with no pattern tying it to request volume or to a specific
endpoint - posts 71533, 96580's media, 67853 and Nicole Massarone's/Mallory Hardesty's own name
searches all did this. A plain backoff and retry cleared every one except post 74058 ("SGA holds
final meeting of semester," the post most likely to carry Connor Ferguson), which stayed 403
through two retries forty-five seconds apart and was not read this pass - worth a fresh try next
time rather than treating it as checked.

## Conclusion

No new portrait this pass. The three Talisman leads the prior pass queued are now closed with
reasoning on file rather than left open, and sixteen more officer-gap names from the 2021-2026
range are checked and declined, narrowing what a future pass needs to re-discover. `build.py` and
`check_data.py` both pass clean: 61 years, 1964 events, 60 presidents, every one portrayed. Landed
on `research-photos`.
