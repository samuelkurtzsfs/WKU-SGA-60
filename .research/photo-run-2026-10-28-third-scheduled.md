# Photograph run, 28 October (third scheduled pass): both blocked routes retested through a second, independent fetch path and confirmed closed there too; the archive.org Talisman full-text method from this morning's pass is now exhausted for every gap name within its coverage years

## Priorities 1, 2 and 4, reconfirmed against the file before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait in `data/photos.json`. Unchanged — this trigger's stored brief still names them as
  portraitless, and it still isn't true; see every run since 20 August.
- **Priority 2**: `python3 scripts/check_data.py` reports 61 years, 60 people have been president;
  every leader in `data/years.json` has a matching `data/photos.json` entry. No gap.
- **Priority 4**: every year still carries at least one photograph. The standing near-misses
  (1994-95, 2000-01) were not reopened this pass.
- **Priority 3** (officer/Senate gap): `python3 scripts/portrait_gap.py --any-year` reports 948
  officer slots, 188 with no portrait for that person in that year, 158 people, 156 with no
  portrait anywhere — unchanged from both earlier passes today.

## Network state, retested through a second fetch path this time

Both standing blocks were retested today through `curl` from this container (same result as
every prior pass) and, new this pass, through the session's own `WebFetch` tool, which reaches
the web through different infrastructure than this container's egress:

- `digitalcommons.wku.edu/cgi/viewcontent.cgi?article=8989&context=dlsc_ua_records` —
  `WebFetch` returned a plain `HTTP 403 Forbidden`, no body. Same outcome as the Cloudflare
  challenge `curl` has hit since 25 August, by a route that does not share this container's
  IP or headers.
- `web.archive.org` — `WebFetch` refused outright ("Claude Code is unable to fetch from
  web.archive.org") rather than returning a connection-level error, but the practical result is
  the same as `curl`'s `Recv failure: Connection reset by peer`: no access, by either path.

This rules out the theory that the block is specific to this container's crawling pattern or
reputation — a second, independently-operated fetcher gets refused the same way, so neither
route is likely to open from trying harder or waiting out a single session's rate limit. Worth
re-testing again after more time has passed, not worth spending another pass hammering either
one today.

## The archive.org Talisman full-text route, checked against the whole gap list, is now exhausted

This morning's two passes used `archive.org/metadata/<id>` + `fulltext/inside.php` to search
specific Talisman volumes for four names (David Young, Mark Chesnut, Chris Millay, Dwight
Austin) plus Vern Pulman and the already-barred Steve Wilson/Alice Wicks. That method only
works for the nineteen years archive.org actually holds Talisman OCR text for: 1971-1981, 1986,
1987 (CLAUDE.md, §4 of this file's table). Cross-checked the full 158-person gap list from
`portrait_gap.py --any-year` against those nineteen years rather than assuming coverage: the
only gap names that fall inside an archive.org Talisman year are exactly the ones already
checked this morning — Vern Pulman (1974-75), David Young/Steve Wilson/Alice Wicks (1978-79),
Mark Chesnut (1980-81), Chris Millay/Dwight Austin (1986-87). Every other gap name sits in a
year archive.org does not hold (1982-85, 1988-2002) or post-dates the Talisman era entirely
(2016-26, where wkuherald.com's WP-JSON search is the applicable tool and has already been run
against all of them per the prior pass's name-by-name confirmation).

So, as of today, there is no gap name left that has an untried source available to this
session: the officer/Senate gap is blocked on `viewcontent.cgi` or `web.archive.org` for the
1982-2002 names, and has already returned negative results from wkuherald.com's WP-JSON search
for the 2016-26 names. Nothing changes this until one of the two blocked routes reopens, a new
Talisman year is digitised on archive.org, or new Herald content is posted naming one of the
158 people.

## Conclusion

No new portrait landed this pass. Both standing network blocks were confirmed closed through a
second, independently-operated fetch path (`WebFetch`), not just this container's own `curl` —
a genuinely new test, and a stronger negative than repeating the same route a third time would
have been. The archive.org Talisman full-text method introduced this morning has now been run
against every gap name it can reach; nothing is left untried in that lane either.
`python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean; the
build-date-only diff in `site/` was reverted. `data/photos.json` and `data/photos/` are
unchanged from `origin/research-photos`. No push notification: nothing actionable surfaced, and
the blocked-route state was already reported to the owner on 23 October. Landed on
`research-photos`.
