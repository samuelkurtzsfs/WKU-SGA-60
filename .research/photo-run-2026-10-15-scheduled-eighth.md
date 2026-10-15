# Photograph run, 15 October (scheduled, eighth pass): a caption method unlocked, no new portrait cleared

## Priorities 1, 2 and 4: reconfirmed, unchanged

Checked `data/photos.json` against `data/years.json` before anything else.

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait, unchanged.
- **Priority 2** (every other president or student regent): zero of the 61 years' leader records
  lack a portrait.
- **Priority 4** (years with no photograph at all): zero years missing from `photos.json`'s
  `years` array.

`python3 scripts/portrait_gap.py`: 189 officer slots / 159 people / 157 with no portrait in any
year — unchanged.

## Network state this session

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`: 403. Item/landing pages on the same host answer
  normally. Closed for PDFs, same as every pass since 13 October.
- `web.archive.org`: connection reset outright. Closed, same as every pass since 13 October.
- `archive.org` (not `web.archive.org`): open, 302 on direct download (normal redirect
  behaviour), not used further this pass since no new Talisman-year lead was queued.
- `wkuherald.com`: open but rate-limiting harder than recent passes report — the WP-JSON
  `/wp/v2/posts/{id}` single-post endpoint returned 403 on roughly half of first attempts and
  200 on retry a few seconds to tens of seconds later, with no fixed backoff threshold found.
  Treated every 403 here the same way CLAUDE.md says to treat a `digitalcommons` 403: stopped
  bursting, spaced retries out, never hammered.

## A real method gap closed, even though it yielded nothing new this pass

Multiple reports since 13 October (most recently #786 and the 15 October second-pass note) flag
wkuherald.com's photo galleries — the `slideshowwrap`/`photowrap` widget used on election-result
and multi-photo stories — as unreachable because its individual captions "load by script" and
"this pass has no means to render" them. That is no longer true, and there was no need to render
anything: **`https://wkuherald.com/wp-json/wp/v2/media/{id}`, called directly with the numeric
photo ID already printed in the page's `data-photo-ids` attribute, returns that single photo's
full caption text in plain JSON (`caption.rendered`), with no JavaScript involved.**

Verified end to end on the gallery behind article 65821 ("SGA election results announced, Cole
Bornefeld wins presidency," 20 April 2022), whose `data-photo-ids` lists eight IDs
(65823–65830). Fetched all eight individually:

- 65823 (inline, no fetch needed): "Sam Kurtz (left) and Cole Bornefeld call their moms..."
- 65824: "SGA Chief Justice Holden Schroeder looks over the election results..."
- 65825: "SGA Chief Justice Holden Schroeder addresses the members of SGA..."
- 65826 / 65827: "Cole Bornefeld and Alexis Courtenay hug..."
- 65828: "Garrison Reed (left) congratulates Sam Kurtz..."
- 65829: "President Cole Bornefeld congratulates Garrison Reed..."
- 65830: "Cole Bornefeld, Sam Kurtz and Garrison Reed hug..."

Every name in that gallery (Kurtz, Bornefeld, Schroeder, Reed, Courtenay) already carries a
portrait in `data/photos.json`, so this particular gallery added nothing new — but the method
itself is the finding. **Any future pass hitting a wkuherald gallery for a still-open gap name
should pull the `data-photo-ids` list from the story's HTML and query `/wp-json/wp/v2/media/{id}`
for each one, rather than marking the lead closed as unreachable.** This reopens Reed Hensley's
gallery lead (article 65821 again, same gallery — checked this pass and he is not one of the
eight captioned photos) and any other gap name tied to a gallery story going forward.

## Names checked this pass against wkuherald.com, nothing usable

Searched `/wp-json/wp/v2/posts?search=<name>` for twelve still-open gap names and read every
hit's content (and, for the one gallery, every photo's own caption via the method above):

- **Danny Vuleta** (First Generation Senator, 2022-23): zero search hits. Fully exhausted on this
  source now; no lead remains to try here.
- **Reed Hensley** (Organizational Aid Board, 2022-23): two hits. One, the gallery above, checked
  photo-by-photo — not among the eight captioned subjects. The other is a text-only Narcan story
  with no image.
- **Kayla Distler** (2023-24 senator): seven hits, all text-only committee/legislation reports or
  unrelated stories (a different "pink tax" bill, a dorm-conditions story, a suicide-prevention
  walk) that happen to share search terms.
- **Connor Ferguson, Elizabeth Gannon, David Darnell** (2023-24 senators): featured images on
  their hits are all generic SGA-meeting stock photos or unrelated stories (an election-commission
  awareness piece, a staff-senate story, a biking story), none with a figure or caption naming
  them in the body.
- **Callison Padgett** (2023-24 senator): seven hits; the swearing-in story (73874) that should be
  the best lead carries no image at all in its body.
- **Garrett Baum** (2022-23 Associate Justice): three hits; the first-meeting story (67791,
  confirmed text-only above) names him only in running text with no accompanying photo anywhere
  in the piece.
- **Neel Patel** (2022-23 Gatton Academy Senator): three hits, all text-only or with unrelated
  featured images; the most promising (68255) stayed 403 for this pass's whole remaining window
  after two retries spaced apart, so it is unresolved rather than closed — worth a cold retry.
- **Mallory Hardesty** (2022-23 Junior Senator): two hits, one the same Bornefeld-election gallery
  (checked photo-by-photo, not among the eight), the other a text-only trivia-night bill story.
- **Tyreesha Morris** (2025-26 First Generation Senator): four hits, all generic SGA-meeting
  featured images with no individually captioned photo of her found in the bodies checked.

## What is still open

The 189-slot gap is unchanged in count. One lead (Neel Patel, article 68255) is unresolved rather
than closed, held up by wkuherald's intermittent 403s rather than by the content. Every other name
checked this pass is now exhausted against wkuherald's search and, where applicable, its galleries
via the newly-confirmed media-caption method. The routes that would likely carry the pre-2011
names' photographs (`cgi/viewcontent.cgi`, `web.archive.org`) stayed closed for this session's
whole window, consistent with every pass since 13 October.

## Checks

`python3 scripts/build.py` then `python3 scripts/check_data.py`: 61 years, clean, 60 presidents,
no missing leader portrait, no year without a photograph. No file in `data/photos/` or entry in
`data/photos.json` changed this pass.
