#!/usr/bin/env python3
"""
Harvest the SGA legislation archive from wku.edu into the repo.

Reads  https://www.wku.edu/sga/legislative/legislation.php          (archive, 2011-2025)
       https://www.wku.edu/sga/legislative/legislative_archive_2.php (current session)
Writes data/legislation/<session>/<file>.pdf   the actual documents
       data/legislation.json                    metadata: session, type, title, source

Idempotent: files already downloaded are skipped, titles are refreshed.
Rerun each semester to pick up new bills. Older legislation (pre-2011) lives on
TopSCHOLAR and is added by the research agents, not this script.
"""
import json, re, html, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "legislation"
META = ROOT / "data" / "legislation.json"

PAGES = [
    "https://www.wku.edu/sga/legislative/legislation.php",
    "https://www.wku.edu/sga/legislative/legislative_archive_2.php",
]

GOVERNING = ("constitution", "bylaws", "election_codes", "jc_general", "governingdocuments")

# Sessions read off the face of the document where the URL carries no date.
SESSION_OVERRIDES = {
    "sgatutionfreeze.pdf": "2015-16",  # header: First Reading 16 Feb 2016, Resolution 2-16-S
    "presidentialqualificationsresolution.pdf": "2015-16",  # header: Res 2-16-S
    "ea1-12.pdf": "2012-13",  # Executive Action 1 of 2012, signed by Cory Dodds, president 2012-13
}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "SGA60-archive/1.0"})
    return urllib.request.urlopen(req, timeout=60).read()


def session_for(url):
    """Work out the academic session a document belongs to from its URL."""
    low = url.lower()
    base = low.rsplit("/", 1)[-1]
    if base in SESSION_OVERRIDES:
        return SESSION_OVERRIDES[base]
    if any(g in low for g in GOVERNING):
        return "governing"
    m = re.search(r"/sga/[^/]*?(\d{4})[_-](\d{4})", low) or re.search(r"legislation-(\d{4})-(\d{4})", low)
    if m:
        return f"{m.group(1)}-{m.group(2)[2:]}"
    m = re.search(r"/sga/legislative/(\d{4})_(\d{2})_legislation", low)
    if m:
        return f"{m.group(1)}-{m.group(2)}"
    # bare filenames end in ...-17-s / _21_f: s = spring of that year, f = fall of that year
    m = re.search(r"[_-](\d{2})[_-]([fs])\.pdf$", low)
    if m:
        yy, sem = int(m.group(1)), m.group(2)
        start = 2000 + (yy - 1 if sem == "s" else yy)
        return f"{start}-{str(start + 1)[2:]}"
    m = re.search(r"(?:ea|b|r)\w*?(\d{2})\.pdf$", low)  # uploads/bills/ea1-12.pdf
    if m:
        start = 2000 + int(m.group(1))
        return f"{start}-{str(start + 1)[2:]}"
    return "undated"


def type_for(url):
    base = url.rsplit("/", 1)[-1].lower()
    if "res" in base or base.startswith("r"):
        return "resolution"
    if "ea" in base[:3]:
        return "executive action"
    return "bill"


def main():
    links = {}  # url -> [title fragments in order]
    for page in PAGES:
        try:
            text = fetch(page).decode("utf-8", "replace")
        except Exception as e:
            print(f"could not fetch {page}: {e}", file=sys.stderr)
            continue
        for u, t in re.findall(r'<a[^>]+href="([^"]+\.pdf)"[^>]*>(.*?)</a>', text, re.S | re.I):
            if u.startswith("/"):
                u = "https://www.wku.edu" + u
            if "wku.edu" not in u:
                continue
            title = html.unescape(re.sub(r"<[^>]+>", "", t)).strip()
            title = re.sub(r"\s+", " ", title)
            frags = links.setdefault(u, [])
            if title and title not in frags:
                frags.append(title)

    entries, failed = [], []
    for url in sorted(links):
        session = session_for(url)
        sdir = OUT / session
        sdir.mkdir(parents=True, exist_ok=True)
        name = url.rsplit("/", 1)[-1]
        dest = sdir / name
        if not dest.exists():
            try:
                blob = fetch(url)
                if not blob.startswith(b"%PDF"):
                    raise ValueError("not a PDF")
                dest.write_bytes(blob)
            except Exception as e:
                failed.append(f"{url}: {e}")
                continue
        entries.append({
            "session": session,
            "type": type_for(url),
            "title": " ".join(links[url]) or name,
            "file": f"{session}/{name}",
            "source_url": url,
        })

    META.write_text(json.dumps({"entries": entries}, ensure_ascii=False, indent=1) + "\n")
    total = sum(f.stat().st_size for f in OUT.rglob("*.pdf"))
    print(f"{len(entries)} documents in {META.name}, {total // 1_000_000} MB on disk")
    if failed:
        print(f"{len(failed)} failed:", *failed[:20], sep="\n  ", file=sys.stderr)


if __name__ == "__main__":
    main()
