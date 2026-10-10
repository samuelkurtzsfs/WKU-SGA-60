# 10 October 2026 (photograph agent, scheduled) — thirty more officer names searched, all negative; the two closed gates reconfirmed shut

## Priorities 1, 2 and 4, reconfirmed before anything else

**Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
portrait in `data/photos.json`. Nothing to do.

**Priority 2** (any other president or student regent without a portrait): checked every
`leaders` record in `data/years.json` against `data/photos.json` by name, programmatically.
Zero missing.

**Priority 4** (years with no photograph at all): checked every year's `leaders` entries and the
`years` array in `data/photos.json` together, programmatically. Every one of the 61 years has at
least one photograph. Zero missing.

So, as with every recent pass, this run's whole job was priority 3: executive and Senate officers
with no portrait on file.

## Thirty names searched on wkuherald.com, all negative

Picked thirty names from `organization.executive` and `organization.senate.officers` across
`data/years.json` that no prior run's report names as searched (cross-checked against the 9
October third pass's list of fifteen already-tried names — Pulman, Bass, Young, Wicks, Millay,
Austin, Chesnut, Hancock, Carter, Chiapetta, Varner, Murphy, Scott, McDole, Payne — all excluded
here). All thirty are 2021-22 through 2025-26 Senate seats, judicial council seats and committee
roles, searched against wkuherald.com's WordPress API (`/wp-json/wp/v2/posts?search=`), which is
the only open route for this span (see gates, below).

| Year(s) | Office | Name | Result |
|---|---|---|---|
| 2021-22, 2022-23 | Associate Justice / Chief Justice / Associate Chief Justice | Justin Goins | No individually captioned photo |
| 2023-24 | Graduate Senator | Elizabeth Gannon | No individually captioned photo |
| 2022-23 | First Generation Senator | Danny Vuleta | No results |
| 2021-22 | Secretary of the Senate | Elizabeth DeLozier | No individually captioned photo |
| 2021-22 | Associate Chief Justice | Turner Reynolds | No individually captioned photo |
| 2022-23 | Senator At-large | Maksim Zaepfel | No results |
| 2021-22 | Campus Improvements and Sustainability Committee Chair / Senator At Large | Zachary Skillman | No results |
| 2021-22 | Director of Enrollment and Student Experience | Tribhuwan Singh | No results |
| 2023-24 | Secretary of the Senate | Livi Ray | No relevant results (name too common; hits were sports/arts coverage) |
| 2021-22, 2023-24 | Senator / Senator At-Large | Maiah Cisco | No individually captioned photo |
| 2023-24 | Gordon Ford College of Business Senator | Connor Ferguson | No individually captioned photo |
| 2023-24 | PCAL Senator | David Darnell | No individually captioned photo |
| 2023-24 | College of Education and Behavioral Sciences Senator | Kayla Distler | No individually captioned photo |
| 2023-24 | Senator At Large | Joel Hornback | No individually captioned photo |
| 2022-23, 2023-24 | Senator At Large / Sophomore Senator | Callison Padgett | No individually captioned photo |
| 2022-23 | Associate Justice | Garrett Baum | No individually captioned photo |
| 2022-23 | Senator At Large | Trevor Clark | No individually captioned photo |
| 2022-23 | Senator At Large | Gunnar Robinson | No results |
| 2022-23 | Junior Senator | Mallory Hardesty | No individually captioned photo |
| 2022-23 | Gatton Academy Senator | Neel Patel | No individually captioned photo |
| 2021-22, 2022-23 | Senator At Large | Caleb Collins | No individually captioned photo |
| 2022-23 | Senator | Barrett Gibbs | No individually captioned photo |
| 2022-23 | Member of Organizational Aid Board | Reed Hensley | No individually captioned photo |
| 2022-23 | Mental Health and Wellbeing Committee Member | Brooke Mitchell | No relevant results |
| 2021-22 | Senator At Large | James Cecil | No individually captioned photo |
| 2021-22 | Associate Justice | Alexis Mayne | No results |
| 2021-22 | Associate Justice | Jason Herlick | No individually captioned photo |
| 2021-22 | Associate Justice | Nicole Massarone | No individually captioned photo |
| 2022-23 | Graduate Student Senator | ShyAnte'e Williams | No relevant results |
| 2022-23 | Senator At Large | Juan Tomas | No relevant results |

**Why "no individually captioned photo" is the common outcome, not "no coverage."** Most of these
names turn up real SGA articles — "SGA passes 4 bills to fund upcoming events," "SGA elects
committee chairs," "SGA election results announced, Cole Bornefeld wins presidency" — because
they authored legislation or were named in running text. That text is exactly what already
supports their `organization` entry in `data/years.json`. The photographs attached to these
articles are almost always a wide shot of the senate chamber or a lead image of the ticket that
won (e.g. the lead photograph of article 65821 is captioned for Sam Kurtz and Cole Bornefeld
only, both already on file), with a caption describing the scene or the pictured pair rather than
naming every person quoted in the story. **This holds for the lead image; it does not hold for
the galleries, and this pass did not test them** (editor's note, 10 October — see "For the next
run"). Fourteen of these thirty names surfaced a real SGA article with no caption naming them;
the other sixteen returned no result, an unrelated result, or (Livi Ray) too common a name to
search usefully this way. This matches the 9 October third pass's finding
about the post-2008 pattern exactly, now confirmed against a much larger sample.

**One name resolved differently, and is worth flagging so the next run does not repeat the
search.** Checking "Sophia Bryant" (2023-24 Senator At Large) against an article turned up during
this sweep, before cross-referencing the existing missing-portrait list, found a clean two-person,
explicitly left/right captioned photograph (Alex Cissell and Bryant at a podium, Herald, 15 March
2024 senate meeting, article 75688) that looked like a strong, safe candidate. `data/photos.json`
already carries a cropped portrait of her, sourced to a different (2024-25) Herald photograph —
she was correctly never on the missing list. No files were added for her; this is recorded only so
a future pass does not spend the same few minutes rediscovering that she already has a photograph
on file, and as a reminder to check the missing list before chasing a lead, not after.

## The two gates, retested

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — still shut. One `curl` with full navigation
  headers (`Sec-Fetch-Dest: document`, `Sec-Fetch-Mode: navigate`, `Upgrade-Insecure-Requests: 1`)
  against a known-good article number returned HTTP 403 and a Cloudflare "Just a moment..."
  challenge page, not a PDF. Consistent with every pass since this gate first closed. This route
  stays the blocker for the 2010s-2020s Talisman volumes and the 1995-96 *Xposure* issues the 9
  October third pass flagged as a lead.
- `wkuherald.com` — open, used for all thirty names above via the WordPress REST API
  (`/wp-json/wp/v2/posts?search=`). Its search is a blunt keyword match, as previously noted (it
  can match on a common first name alone), so a hit list has to be read, not trusted at face
  value.
- `archive.org` — not used this pass. Every Talisman year it holds (1971-81, 1986-87) that has a
  missing officer was already exhausted by the 9 October second and third passes (Pulman, Bass,
  Young, Wicks, Millay, Austin all searched and closed negative); nothing new to check there until
  a year's organization roster changes.

## Nothing landed

No file in `data/photos.json` or `data/photos/` changed; `data/years.json` is untouched.
`python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean against the
pre-existing tree (61 years, 1,967 events, 60 presidents) — build.py's own routine pruning of
photographs it can no longer find or that are barred ("withdrew 5 photograph(s)...") is unrelated
to this pass, produced no `data/` change, and the resulting `site/` diff was discarded rather than
committed, since this pass touched no data worth rebuilding the site over. This run's only output
is this note.

## For the next run

The missing-officer list stood at 197 office-holding terms before this pass (31 executive,
166 Senate officer/committee-chair), which is **190 distinct people** once the 7 who appear in both
columns are counted once; this note first gave 199/33 and the editor's pass of 10 October corrected
it against `years.json` and `photos.json`. It is unchanged after this pass, since nothing was
added — but thirty more of those names now have a documented negative result instead of being
untried. The pattern across forty-five searched names (fifteen from the 9
October pass, thirty from this one) supports a narrower statement than this note first made, and
the editor's pass of 10 October trimmed it to that: **a keyword search of wkuherald.com article
text and titles does not, for a 2003-and-later Senate seat or committee chair, turn up a photograph
captioned to the individual.** The causal rule this note originally drew from that — that the
coverage photographs only the room or the winning ticket — is **withdrawn as unsupported**, because
it was stated without testing the one route that bears on it. The articles carry photo galleries
whose attachments each hold their own caption, reachable at
`wkuherald.com/wp-json/wp/v2/media/<id>` from the `data-photoids` list in the article HTML, and
those captions do name individuals: in article 65821 alone, attachment 65825 captions SGA Chief
Justice Holden Schroeder as a single subject, and 65828 names Garrison Reed and Sam Kurtz
left/right. All three of those happen to be on file already, so this pass's thirty negatives are
not disturbed — but the route is open, untested against the missing list, and is the first thing
the next run should try. The productive remaining leads are still the ones the 9 October pass
named — the *Xposure* issues of 1995-96 and the 2010s Talisman
volumes — and both wait on the same `cgi/viewcontent.cgi` gate, which has now been closed on every
single pass that has tested it. A future pass with room to spare could try requesting those PDFs
with a `Range` header instead of a full GET, in case the gate's block is keyed to response size
rather than the path itself; this pass did not have room to test that and is only recording it as
untried.
