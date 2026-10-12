# Photograph run, 12 October: priorities 1-2 and 4 reconfirmed at their standing state, both PDF routes closed all session, the full untried 2016-2026 officer-gap slice swept on wkuherald.com with nothing usable, and a new-looking lead on wku.edu/sga turned out to be fully redundant

## Priorities 1 and 2: reconfirmed, nothing to do

**Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): checked directly against
`data/photos.json` before anything else. All four still carry a portrait.

**Priority 2** (any other president or student regent without a portrait): every `leaders` record
in `data/years.json` checked programmatically against `data/photos.json` by name. Zero missing —
all 73 leader records, across all 61 years, carry a portrait.

## Priority 4: unchanged

Checked programmatically which years in `data/years.json` have no entry in `photos.json`'s
`years` array: only **1994-95**. (2000-01, the other standing gap as of 8-11 October, was closed
by the 11 October later-scheduled run's election-night debate photograph — confirmed by this
check, not re-researched.) 1994-95 is the Talisman/Xposure publication gap documented repeatedly
since 15 September: no Talisman was published for that year, Xposure (its magazine-era
replacement) carries no SGA content, and five separate Herald issues have been read with no
usable frame. Nothing new to try on it this session — both routes that could reach a sixth Herald
PDF (`cgi/viewcontent.cgi`, the `web.archive.org` bypass) were closed throughout, tested below.

## Access this session: both PDF routes closed throughout, retried at the start and again at the end

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — Cloudflare 403 challenge (5,995 bytes) on every
  attempt, with full browser navigation headers, against article 8989 (the 1994-95 lead the
  11 October later-scheduled run left as the specific next step). Tested at the start of the
  session, after a 15-second pause, and again after the wkuherald sweep (roughly 20 minutes
  later): 403 every time.
- `web.archive.org` — unreachable all session. `curl: (35) Recv failure: Connection reset by
  peer` on a plain fetch of the homepage, and the agent proxy's own status line confirms
  `ws_closed_mid_exchange` on the same host — the tunnel itself closing, not a WKU-side block.
  Same failure mode as the 11 September (second scheduled) run logged for this route.

Per the standing advice in this file (11 September, second scheduled pass) not to conclude a
route is shut from one failed request, both were retried rather than taken on a single timeout;
the result held across three separate attempts spread over the session.

## Priority 3: the full untried 2016-2026 officer-gap slice from the 11 October note, swept on wkuherald.com

`portrait_gap.py` still reports 189 officer slots / 159 people / 157 with no portrait in any
year — unchanged. The 11 October (second scheduled) report left a specific list of untried names
from the 2016-2025 slice; this run worked through every one of them, plus the two 2025-26 names
`portrait_gap.py --list` now shows (Tyreesha Morris, Carter Smith), none of which were on that
list because they postdate it:

- **Matthew Johnson, Hope Wells, Jillian Kenney, Tribhuwan Singh, Alexis Mayne, Danny Vuleta,
  ShyAnte'e Williams, Brooke Mitchell** — zero or near-zero `wkuherald.com` search hits, and none
  of the hits that did come back carry any photograph at all.
- **Jesse Banales, Garrett Baum, Neel Patel, Mallory Hardesty, Reed Hensley, Kayla Distler,
  Connor Ferguson, David Darnell, Livi Ray, Callison Padgett** — each returns hits with the name
  in the body text, and a few of those stories carry one image, but every image checked is either
  an uncaptioned featured thumbnail or a caption naming someone else (a TopNet voting screenshot
  with no caption at all, for three of these names sharing the same story).
- **Elizabeth Gannon** — article 74403 ("SGA swears in new members, opens spring scholarships")
  mentions her in the body and carries two captioned photographs, but both captions name other
  officers (Administrative Vice President Salvador Leon Golib, Executive Vice President Annalise
  Finch) — neither photograph is of Gannon.
- **Tyreesha Morris** — the strongest-looking hits (90387, six images; 88370, four images) are
  both from Senate floor-business stories whose photographs are fully captioned for other named
  people (WKU Restaurant Group staff, Sen. Miles VanRude, Sen. Jacob Thomas, SGA President Rush
  Robinson, Senator At-Large Amelia Tucker) — Morris is named in the running text, not in any
  caption. No usable frame.
- **Carter Smith** — same pattern: hits with images (97612, 87022) caption a guest speaker and
  President Caden Lucas/Rush Robinson, never Smith.

No name checked this run produced a caption meeting CLAUDE.md's bar — a photograph whose subject
is named, alone or clearly, in the caption or the text immediately beside it. This exhausts every
name the 11 October note flagged as untried in the 2016-2026 range; the remaining 150-odd people
in the gap are the pre-2011 names that `archive.org`/Talisman cannot currently reach (route closed
this session, see above) and names already individually checked and closed in earlier runs.

## A lead that looked new and was not: `wku.edu/sga/executive/index.php`'s live headshot directory

Found by following the current SGA site's own navigation rather than a Herald search — a page
not named in any earlier photograph-run note in this file. It carries real headshot photographs
of the 2026-27 executive cabinet, each in its own card with the officer's name as a visible
heading, their title, and their university email directly beside the photo:

- Caden Lucas, Student Body President — `caden.jpg`
- Jakob Barker, Student Body Vice President — `jakobbarker.jpg`
- Will Derryberry, Chief Financial Officer — `will.jpg`
- Gabi Pace, Chief of Staff — `gabipace2.jpg`
- Cayden Bailey, Chief Communications Officer — `caydenbayley.jpg`

One oddity worth recording so a future run does not trip on it: the `alt` attribute on Lucas's
`<img>` reads "A headshot image of Student Body President **Rush Robinson**," not Lucas — a
stale attribute left over from the 2025-26 page (Robinson was 2025-26's president), while the
visible card heading, title and filename all correctly read Caden Lucas. The visible card text is
the real identification here, not the `alt` text, and it is unambiguous.

Checked `data/photos.json` before downloading anything: **all five already carry a portrait**,
each sourced from a *College Heights Herald* caption (the 15 April 2026 election-night photo for
Lucas/Barker/Derryberry, the 25 November 2025 committee-report frame for Bailey, the 2 April 2026
bill-presentation frame for Pace), which are stronger identifications than this directory page
gives (a named photo caption beside the SGA cabinet's own business, versus a staff-directory
headshot). Nothing to add. Also checked `wku.edu/sga/legislative/senate_committees.php` for the
two outstanding 2025-26 senator names (Tyreesha Morris, Carter Smith) on the theory that a
committee-roster page might carry photos where the Herald sweep above did not: it names both,
but the page is a text-only roster with no images at all.

## Nothing changed

`data/photos.json`, `data/photos/` and `data/years.json` are all untouched this run. No new file
to verify. `python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean (61
years, 1968 events, 60 presidents; "the archive checks out against its own rules"). The `site/`
rebuild this produced was discarded (`git checkout -- site/`) since nothing in `data/` changed.
This run's only output is this note.

## For the next run

- Both PDF routes (`cgi/viewcontent.cgi`, `web.archive.org`) were closed for this entire session,
  tested three times each, spread out rather than back to back. Test fresh rather than trusting
  this note for more than a few hours — the intermittency recorded throughout late September and
  October is real.
- The 1994-95 year-photo gap's specific next step is unchanged from 11 October: re-fetch
  `article=8989` (Herald 69:51) and read printed pages 6-9, and finish the unread tail (printed
  pp. 8-29) of `article=8933` (Herald 70:56), the moment either PDF route opens.
- Priority 3's untried-name list from 11 October is now fully exhausted, including the two
  2025-26 names it didn't yet cover (Tyreesha Morris, Carter Smith). What's left in the 159-person
  gap is almost entirely pre-2011 names behind the closed `archive.org`/Talisman route, plus names
  already individually closed in earlier runs — there is no fresh, untried slice to work through
  on `wkuherald.com` right now. A future run should check whether new officer announcements have
  landed since 12 October before re-walking old ground.
- `wku.edu/sga/executive/index.php` is a live, well-identified headshot directory worth checking
  again after each election, since it should update to the newest cabinet before the Herald
  covers them — but note its `alt` attributes are not reliable (see Lucas/Robinson above); use the
  visible name/title card text next to each photo instead.
