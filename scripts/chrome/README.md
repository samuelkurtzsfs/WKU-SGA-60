# Getting past Cloudflare on TopSCHOLAR

TopSCHOLAR serves landing pages to anything, then refuses the actual file.
`/cgi/viewcontent.cgi` returns a hard Cloudflare 403 to an address it has
decided it does not like, and once a shared address is in that state it stays
there. Backing off for eleven minutes does not clear it. Alternate bepress URL
forms do not clear it. **Headless Chrome does not clear it either**, which is
the part that wastes people's time, because headless is the obvious thing to
reach for and it fails exactly like curl does.

What works is a real windowed Chrome, parked off-screen, driven over the
DevTools protocol. It passes on the first attempt. The same trick clears
wkuherald.com's "Just a moment" interstitial.

    node scripts/chrome/chromechunk.js <outdir> <name>=<url> [<name>=<url> ...]

Two things this handles that a naive version gets wrong:

- **The bytes come back in slices.** One large base64 string hangs the CDP
  connection, and a broadsheet issue is large. It reads in 512 KB pieces.
- **Chrome renders a PDF instead of downloading it**, so
  `Browser.setDownloadBehavior` does nothing useful here. The file is fetched
  from inside the page instead.

Each process picks its own debug port from its pid. Several researchers can run
this at the same time; they could not when the port was a constant, because the
second Chrome would attach to the first one's tabs and both downloads would
come back wrong.

Found by the researcher working 2001-2005, after headless, backoff and URL
juggling had all failed.
