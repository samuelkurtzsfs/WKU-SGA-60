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

Searched `/wp-json/wp/v2/posts?search=<name>` for eleven still-open gap names and read every
hit's content (and, for the one gallery, every photo's own caption via the method above):

- **Danny Vuleta** (First Generation Senator, 2022-23): no usable photograph, but **not** for the
  reason first written here. A search on "Danny Vuleta" returns nothing because the *Herald* prints
  him as **Daniel** Vuleta; a search on the surname returns three hits. All three were opened on
  review: 73551 ("Veterans and ROTC cadets share experiences on the Hill", 10 Nov 2023) is a
  feature carrying three photographs, but every one is captioned **William Stanley**, not Vuleta;
  73655 (9 Nov 2023) quotes him on a bill and carries no body image; 65821 is the election gallery
  above, whose eight captions are known and do not include him. The conclusion stands, the reason
  does not. **Search the surname, and search "Daniel", before recording this name as exhausted.**
  Note also that 73551 and 73655 describe a Daniel Vuleta who is the ROTC Cadet Battalion
  Commander. That he is the senator of the same name is likely but **not established**, and must
  not be treated as settled by a later pass.
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
  featured images. The most promising (68255) stayed 403 for this pass's whole remaining window;
  it answered on a cold retry during review and carries **no image in its body at all**, so the
  lead is closed, not merely unresolved. (The article, "SGA fall election results announced,
  VP Reed appointed to Council on Postsecondary Education", 21 Sept 2022, does confirm in running
  text that Patel won the Gatton Academy seat.)
- **Mallory Hardesty** (2022-23 Junior Senator): two hits, one the same Bornefeld-election gallery
  (checked photo-by-photo, not among the eight), the other a text-only trivia-night bill story.
- **Tyreesha Morris** (2025-26 First Generation Senator): four hits, all generic SGA-meeting
  featured images with no individually captioned photo of her found in the bodies checked.

## What is still open

The 189-slot gap is unchanged in count. The one lead left hanging by wkuherald's 403s (Neel Patel,
article 68255) was retried on review and is now closed: the article carries no image. Every name
checked this pass is now exhausted against wkuherald's search and, where applicable, its galleries
via the newly-confirmed media-caption method. The routes that would likely carry the pre-2011
names' photographs (`cgi/viewcontent.cgi`, `web.archive.org`) stayed closed for this session's
whole window, consistent with every pass since 13 October.

## Checks

`python3 scripts/build.py` then `python3 scripts/check_data.py`: 61 years, clean, 60 presidents,
no missing leader portrait, no year without a photograph. No file in `data/photos/` or entry in
`data/photos.json` changed this pass.

## Checked on review, 15 October

Sixteen claims in this note were opened at source before it was merged.

Holding as written: all eight gallery captions (media IDs 65823–65830, fetched individually and
matching this note word for word); article 65821's title and date; the `data-photo-ids` attribute,
which really does print those eight IDs — though only in the **rendered page HTML**, not in the
`wp-json` post object's `content.rendered`, so a future pass must fetch the article page itself to
read it; Hensley and Hardesty appearing in 65821 only in a running-text roster of elected senators
and in none of the eight captions; Padgett's 73874 and Baum's 67791 both carrying no body image;
and `portrait_gap.py`'s 189 / 159 / 157, which reproduces exactly.

Corrected above: the name count (eleven, not twelve), the Vuleta entry, and the Patel entry.

Not verified: the Tyreesha Morris search, which returned 403 on two attempts during review. The
rate-limiting this note describes is real and was hit again.

**An open question this pass turned up, for the roster rather than the photograph routine.** The
*Herald*'s election report of 20 April 2022 states that Tramaine Hawkins won the first generation
seat and Daniel Vuleta the Intercultural Student Engagement seat — the reverse of the seats the
archive records for the two, which come from SGA's own bill sheets (Bill 27-23-S names "Danny
Vuleta, First Generation Senator"; Bill 8-22-F names "Tramaine Hawkins, ISEC Senator"). Both
sources are contemporaneous and neither is obviously wrong: the bills are from inside the 2022-23
session and name each author's own seat, so the likeliest reading is that the two seats changed
hands between the April election and the session. Nothing was altered in `years.json` on the
strength of this. It is recorded so that a later pass does not flip the entries back and forth
without resolving it.
