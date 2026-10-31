# Photograph run of 19 October (third scheduled pass): same baseline, same closed access, two targeted retries added nothing

Reconfirmed before anything else, independently rather than on this morning's word: all four named
presidents (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley), all 73 `leaders` records and
all 61 years still carry a portrait or year-level photograph. `portrait_gap.py` still reports 189
officer slots / 159 people / 157 with no portrait anywhere, unchanged from the first two passes
today.

Retested access fresh: `cgi/viewcontent.cgi` still 403 (Cloudflare challenge); `web.archive.org`
still resets mid-exchange at the agent proxy (`ws_closed_mid_exchange`), on two separate attempts
six seconds apart. TopSCHOLAR landing pages, `archive.org`'s Talisman text/download host, and
`wkuherald.com` all still answer normally — the block is specific to the two PDF/archive routes
that hold the bulk of the unexploited pre-2003 leads, not the open web.

Spent the open routes on two specific retries rather than re-running the whole gap list a third
time today:

- **Daniel/Danny Vuleta** (First Generation Senator, 2022-23): the 403 noted on 15 October against
  wkuherald's WP-JSON search cleared on retry. Both matching articles were read in full. Article
  73551 ("Veterans and ROTC cadets share experiences on the Hill," 10 Nov 2023) quotes him
  extensively as ROTC Battalion Commander but its one photograph is captioned "William Stanley...
  (Kayden Mu)," not Vuleta. Article 73655 ("SGA approves four bills at weekly meeting," 9 Nov 2023)
  quotes him on a veterans' bill but carries no photograph of him — its featured image is a generic
  SGA Senate-meeting shot with no caption naming anyone. Ruled out again, on a cleared search this
  time rather than a blocked one; nothing to add.
- **`web.archive.org`'s `if_` bypass**, the route that closed two of the four year-photo gaps on 7
  October: closed this pass, consistently, not intermittently open as on some other days.

No file in `data/photos.json` or `data/photos/` changed. `python3 scripts/build.py` and
`python3 scripts/check_data.py` both exit clean (61 years, 60 presidents, no missing leader
portrait, no year without a photograph). This run's only output is this note.

## For whoever owns this trigger

The "SGA 60 - portraits" trigger has fired on a 6-hour cycle since 17 August with no change to its
stored prompt. Every officer name in the standing 157-person gap has now been searched, by this
file's own count, at least seven times apiece across every route that is actually reachable from
this container (`wkuherald.com`, `archive.org`'s Talisman full texts for 1971-1981/1986/1987, and
general web search). `data/photos.json` has not gained an entry since 15 October — four calendar
days and roughly a dozen runs producing nothing new, this one included. What remains of the gap
sits almost entirely behind two routes this container cannot reach: `digitalcommons.wku.edu`'s
`cgi/viewcontent.cgi` (a Cloudflare challenge, confirmed from a second independent fetch path on
27 September) and `web.archive.org` (proxy resets, open on some days and closed on others with no
pattern this file has found). Neither is a credential problem; nothing in this container can open
either route on demand. Until one does, a run every six hours mostly reconfirms the same closed
doors. A slower cycle, or one that pauses until a person confirms TopSCHOLAR is reachable again,
would spend less of the project's budget re-checking the same access than finding new portraits.
