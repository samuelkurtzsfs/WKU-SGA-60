# Photograph run, 16 September (second pass)

## Starting state, re-confirmed

Checked the standing brief's priority list against `data/photos.json` and
`data/years.json` before doing anything new, same as the run that preceded
this one today:

- All four presidents named in the brief — Nick Todd, Katie Dawson, Jeanne
  Johnson, Reagan Gilley — already have portraits, verified by real JPEG
  magic bytes and by an exact `name` match against `data/years.json`.
- **Every president and student regent in the archive has a portrait.**
  Cross-checked every `leaders` entry with `role: "president"` or
  `role: "regent"` against `photos.json` — zero misses. Priorities 1 and 2
  from the brief are fully satisfied.
- 12 of 61 years still lack a dedicated `years` (context) photograph
  (1993-94 through 1997-98, 2000-01, 2002-03, 2003-04, 2005-06, 2006-07,
  2008-09, 2009-10) — all of them already carry at least a leader portrait,
  so this is the thinner priority-4 gap, not a zero-image gap.

## digitalcommons.wku.edu: confirmed still blocked

Re-tested `cgi/viewcontent.cgi` directly (a Talisman article URL) rather
than trusting the prior report: HTTP 403, a Cloudflare "Just a moment..."
managed-JS-challenge page, 5,974 bytes of HTML rather than a PDF. This
matches the 13 and 16 September findings exactly — landing pages on the
same host return normal 200s, only the PDF endpoint is blocked, and it is
an egress-level block on `*.challenges.cloudflare.com`, not something a
slower pace or a different client fixes. Left this route alone rather than
re-litigate it a third time today.

## What this run did differently: a systematic sweep of priority 3

The prior run's recommendation was to search each remaining committee-chair
or Senate-officer name against wkuherald.com's *election and swearing-in*
coverage specifically, since that corpus (not in-office meeting recaps) is
where all four priority presidents' portraits came from. This run carried
that out at scale rather than spot-checking a few names.

Regenerated the candidate list (the same filter the 13 September report
used: named executive or Senate officers without a `photos.json` entry,
plain "Senator"/"Senator At Large"/"Representative" seats excluded) — 166
entries spread 1977-2024. Of those, roughly 114 had not been individually
tried by name in either of today's earlier reports or the 13 September one.
Searched essentially all of the 2003-2024 portion (wkuherald.com's
full-text era, ~80 names) plus a sample of the pre-2003 portion (which has
no wkuherald.com coverage and no archive.org Talisman text — inside the
SGA era archive.org holds only 1971-1981, 1986 and 1987; the other WKU
volumes on it, 1943, 1946, 1947 and 1963-1965, all predate the founding
of the Associated Students in May 1966, and the `Talisman1995` item there
is a German PC game, not the yearbook — so those names are unreachable
this session regardless) against the WordPress API, checking every hit's
`featured_media` for an actual caption naming the person.

**Result: zero new portraits.** The pattern already documented on 13 and 16
September held for every additional name tried. Specific near-misses worth
recording so a future run does not re-walk them:

- **Chris Jankowski / Mallory Treece**, "Four SGA members attend Rally for
  Higher Education in Frankfort" (wkuherald.com, 8 Feb 2012) — the story
  names all four attendees in the body, but the photo's own caption
  identifies only one of them, IT director **Cory Dodds** ("Cory Dodds...
  waves his red towel..."), who already has a portrait. Jankowski and
  Treece are mentioned in the article, not identified in the frame.
- **Cole McDowell**, "SGA election results" (2 Apr 2015) — the photo tied
  to this headline is captioned "Jay Todd Richey," the winning presidential
  candidate (already covered), not McDowell.
- **Tyler Scaff**, "SGA discusses ways to improve campus" (25 Sep 2014) —
  photo captioned for Executive Vice President Nolan Miles (already
  covered), not Scaff.
- **Jason Herlick / Turner Reynolds**, "SGA judicial council 'fully
  functional' following four nominations" (25 Sep 2019) — read the full
  article text, which does name both men individually in prose. The
  featured image carries no caption at all (empty caption and alt text),
  and no other image is embedded in the article body. Not usable.
- **Elizabeth DeLozier / Garrett Baum / Reed Hensley**, several 2021-22
  election and cabinet stories — checked "SGA voting opens today: Who is
  on the ballot," "SGA election results announced, Cole Bornefeld wins
  presidency" and "SGA elects committee chairs." All three photos are
  captioned for other people already on file (Sam Kurtz and Cole
  Bornefeld in the election-night photo; the other two carry a caption
  but it names nobody, describing a cabinet or a set of senators
  listening). None name DeLozier, Baum or Hensley.
- A handful of names returned hits that were plainly a different person by
  date or context and were discarded rather than misattributed: the "Mark
  Henry" hit was a WWE wrestler in a Diddle Arena story, decades off from
  the 2004-05 SGA officer; the "Jessica Williams" hits were a 2019-20
  climate activist, not the 2005-06 Academic Affairs chair; "Robert Bell"
  was a Civil War history story.
- wku.edu's news site has no working search API from this container
  (`wku.edu/wp-json/...` and `www.wku.edu/wp-json/...` both 404); reached
  a handful of individual named officers this way only via general web
  search, and none of the hits were photographs in an SGA context that
  named the person. Two 2021-22 officers turned up that way and were
  declined: one hit was a working-life page carrying no photograph of
  the person in office, the other a legislation PDF with no photograph
  at all. Neither is an archive photograph of an officer acting in their
  SGA role, and the detail that made each unusable is not recorded here
  for the same reason the Cody Cox bullet's was cut on 15 September.

The underlying pattern, now confirmed across three separate runs and well
over 90 distinct names: the Herald's SGA meeting-recap, ballot and
election-night photography almost always uses a generic "cabinet listens"
or "senators sworn in" shot, whose caption names nobody where it is
present at all, or else captions only the president. Committee chairs, Senate officers and judicial council members
are named in body text constantly but are essentially never individually
captioned in a photograph, in either the digitized Herald's index or
wkuherald.com's full text. This is not a search-technique gap; it is what
the source material contains.

## Priority 4 (year photographs) — not attempted this run

Left this alone deliberately: every avenue previously identified for it
(the SGA-photographs finding aid, individual Talisman volumes for the
12 thin years) lives behind the same blocked `cgi/viewcontent.cgi`
endpoint, and re-testing that block a third time in one day would not
learn anything the digitalcommons test above didn't already confirm.

## Recommendation for the next run

The 166-candidate priority-3 list is now exhausted for the two corpora this
container can actually reach (wkuherald.com full text, and archive.org's
limited Talisman years). Further progress on priority 3 needs one of:
digitalcommons PDF access (blocked at the container egress level, not a
technique problem), or the WKU Archives UA1C photograph finding aids,
which are themselves digitalcommons-hosted PDFs and behind the same
block. Until the egress policy changes, a photo run's marginal time is
better spent re-verifying existing entries than re-searching this list.

No data files changed this run — nothing new to commit to
`data/years.json` or `data/photos.json`. This note and the merge of
`origin/main` are the only changes on this branch.
