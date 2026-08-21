# Senate rolls: the years with no members, checked 20 August 2026

`organization.senate.members` is empty on 18 academic years. This note records what
this run actually checked, so the next run does not repeat dead ends. It added no
names to `data/years.json` — everything below is a negative result, held to the
same sourcing bar as a positive one.

## The minutes collection does not reach six of these years

`digitalcommons.wku.edu/sga/Meetings/Minutes/` was pulled live and in full (one
request, no pagination needed — 843 item links, of which 830 carry a date, from
1969-02-13 to 2008-12-02). Mapped to academic year, six gap years have **zero**
minutes items on TopSCHOLAR, confirmed against the complete listing rather than
`.research/minutes-index.json` (which independently agrees — it has 0 entries for
the same six years):

- **1966-67, 1967-68** — before the collection starts. The earliest digitised
  minutes item is 13 February 1969, mid-way through 1968-69.
- **1969-70, 1971-72** — inside the collection's date range, but so is almost
  nothing else from those years. The whole of the late sixties and early
  seventies is one dated item: 13 February 1969. Nothing else is dated before
  1975-76, so 1968-69 (1 item), 1969-70, 1970-71, 1971-72, 1972-73, 1973-74 and
  1974-75 (0 each) are all effectively unrepresented, not two absences inside a
  covered run. The thirteen undated item links cannot be assigned to a year
  either way.
- **1999-00, 2004-05** — genuinely interior gaps. Both sit between years the
  collection does cover (1998-99 has 43 items and 2000-01 has 13; 2003-04 has 26
  and 2005-06 has 48), and the collection itself stops in December 2008.

`1979-80` was already investigated (see `SGA-60-AGENT-INFO.md` §8.3 item 1): the
only two items dated inside that term (250, 261) turn out to swear in *1980-81's*
officers, not 1979-80's. Re-confirmed against the same live listing; nothing new.

## Talisman does not substitute, where it was checked

Of the six, only 1971-72 has a yearbook on `archive.org` (`talisman1972west`,
1971–1981/1986/1987 is the site's coverage; the others fall outside it). Its full
text was pulled and searched. The "Associated Students Officers" section (pp.
56-57, 272) yields only the four officers already on record (Linda Jones, Reginald
Glass, Joe Glasser, Nancy Pape) plus two names — Beverly June Bryant and Christina
Jo Moore — that share the page-272 index reference without any caption text
identifying their role. Not added: the archive's own rule is not to guess at a
role from a bare index cross-reference. No composite "Congress" roster photo with
named individuals was found anywhere in the volume — the 1972 book profiles
officers, not the body.

1966-67, 1967-68 and 1969-70 have no Talisman on `archive.org` at all (the site's
holdings start at 1971), and no alternate host was found.

## Herald coverage exists for 1999-00 but does not print a roster

Unlike minutes, the digitised and wkuherald.com Herald cover 1999-2000 (and
2004-05) heavily — dozens of SGA stories that academic year. None of them is a
post-election roster: the September/October 1999 issues checked in full (not
just the local truncated index) carry SGA budget, elections-code and platform
coverage but no "N students elected to Congress" list. Herald appears to name
rank-and-file senators only when one does something individually newsworthy
(sponsors a bill, resigns, is quoted), which is exactly the kind of piecemeal,
hard-to-verify source the project's own rules already warn about (a bill's
author is not necessarily a member). Building a roster this way was judged not
safe to attempt in one pass; it wants its own careful run with adversarial
verification per name, not a byproduct of this one. 2004-05 was not read
issue-by-issue for the same reason time did not allow both.

## Net effect

No changes to `data/years.json` this run. `.research/senators-unverified.json`
was already empty (reconciled by an earlier pass) — step 1 of the standing
instructions was a no-op, confirmed rather than assumed.
