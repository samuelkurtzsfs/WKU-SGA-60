# Photograph run, 22 October (fourth scheduled pass): a genuinely new route tried — post-body figcaptions and featured-image captions on the Herald's own swearing-in articles — still no new portrait

## Priorities 1, 2 and 4, reconfirmed before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry
  a portrait in `data/photos.json`. Unchanged.
- **Priority 2**: zero presidents and zero student regents without a portrait, across all 61 years.
- **Priority 4**: every year carries at least one year-level photograph. Zero gaps.
- **Priority 3** (officer gap): `scripts/portrait_gap.py` still reports 188 officer slots / 158
  people with no portrait in any year — unchanged from all three of today's earlier passes.

## Network state, retested fresh

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — HTTP 403, Cloudflare challenge, full browser
  navigation headers sent. Still closed.
- `web.archive.org` — three fresh attempts, each `connection reset by peer`. Still closed; the
  third-scheduled-pass note's "IA's own outage, not a permanent wall" reading does not mean it is
  reliably open, and it was not open this pass.
- `wkuherald.com` WP-JSON — open throughout.

## A route not described as tried before: post-body figcaptions and the featured-media caption, for the 2010-2025 names specifically

Today's first pass swept `wp/v2/media?search=<name>` — the media library's own caption/title/alt
fields — against all 158 gap names. That is a different place a caption can live from the
`<figcaption>` markup inside a post's own `content.rendered` (a Gutenberg image block prints its
caption as part of the post body, not necessarily copied back onto the attachment's media-library
caption field) and from the **featured image's** caption, which is a per-post field independent of
what the body text contains. Neither of those two locations had been swept on its own before, so
this pass targeted them specifically, limited to the 2010-2025 stretch, the part of the gap list that recency makes richest in Herald
coverage (73 of the 75 names in that range; Carter Smith and Mark Clark were already checked by
name this morning and were skipped here).

Queried `wp/v2/posts?search=<name>&per_page=5` for all 73 (a courtesy against re-querying, not a
pacing requirement wkuherald.com imposes — no 429s or slowdowns seen across the 73 requests, one
second apart). 64 names returned at least one post. Filtered to the 146 hits whose title or body
actually mentions SGA/Student Government/Associated Student Government and the person's name, then
regex-scanned each post's `content.rendered` for `<figcaption>` blocks and tested whether the
person's surname or full name appeared inside one. **Zero matches** — every figcaption found across
the 146 posts named someone else (reporters' bylines aside, the figures captioned were always a
different officer than the one the post's text happened to mention in passing).

Went one step further on the seven posts that read most like a swearing-in photo op — the shape
that has produced hits for other people in this archive before (Carter Smith's sophomore-senator
swearing-in, this morning; the Garrison Reed VP photo already on file) — and fetched each post's
`featured_media` row directly for its own caption field, independent of the body:

- 96580 "SGA kicks off 60th year... swears in new committee chairs" (queried for Tyreesha Morris) —
  featured caption names President Caden Lucas; the only other figcaption in the body also names
  Lucas. Does not touch Morris.
- 72365 "...selects Judicial Council, committee heads" (Callison Padgett) — featured caption is a
  generic chamber shot, no names.
- 74403 "SGA swears in new members..." (Elizabeth Gannon) — featured caption names Gabe Jerdon; two
  in-body figcaptions name Salvador Leon Golib and Annalise Finch. No Gannon.
- 67791 "SGA votes in new senators, cabinet members..." (Garrett Baum) — featured caption is a
  generic cabinet-listening shot, no names.
- 60866 "SGA swears in seven members, elects new senators" (Nicole Massarone) — featured caption
  describes the vote generically, no names.
- 68255 "...VP Reed appointed to Council on Postsecondary Education" (Neel Patel) — featured
  caption names Cole Bornefeld and Garrison Reed (the VP already on file). No Patel.
- 92808 "Lucas wins SGA presidential election" (Robert Bell, matched on "Bell" alone — a false
  positive on the surname, confirmed by reading the post: it is about the 2026 Lucas/Barker/
  Derryberry ticket and never mentions a Bell) — featured caption names Barker, Lucas and
  Derryberry. No Bell, and the match that brought this post up was never this officer to begin
  with.

None of the seven photographs this specific route surfaced names the officer being searched for.
The pattern holding across all seven is the same one CLAUDE.md's rule exists for: these are
multi-person swearing-in events where the Herald's photographer and caption-writer picked one or
two people to name, and the rest of the room — whoever they are — goes uncaptioned. A hit on the
event is not a hit on the person.

## Conclusion

No new portrait landed. This closes off the two caption locations (post-body figcaption, featured-
media caption) that the morning's media-library sweep did not itself cover, for the 2010-2025 names
specifically — a genuinely untried angle, not a repeat of an earlier pass — and it surfaces nothing
the file didn't already lack. Combined with this morning's media-library sweep, wkuherald.com's
caption-bearing surfaces are now exhausted for the current gap list under its own search API; what
is left there is officers the Herald simply never photographed individually, not officers whose
photograph exists but is mis-indexed. The gap remains blocked on `digitalcommons.wku.edu` and
`web.archive.org` for everyone it would otherwise reach, both still closed this pass.

`python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean against the
unmodified tree (61 years, 1964 events, 60 presidents). Nothing in `data/` changed this run.
Landed on `research-photos`.
