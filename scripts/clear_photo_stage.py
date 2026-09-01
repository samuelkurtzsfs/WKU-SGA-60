#!/usr/bin/env python3
"""Delete the working files once the photograph is live on the site.

    python3 scripts/clear_photo_stage.py             # what is safe to delete
    python3 scripts/clear_photo_stage.py --delete    # delete it
    python3 scripts/clear_photo_stage.py --delete --pages   # sweep page scans too
    python3 scripts/clear_photo_stage.py --delete --all     # the hunt is over

The hunt pulls down yearbook pages at three thousand pixels a side and throws
most of them away. The owner wants them off the machine, and wants that to
happen once the photograph is actually published, not merely committed.

So the test here is the real one: fetch the file from sga60.vercel.app and
check it is byte for byte the file on disk. A commit that never deployed, a
build that dropped the image, a push that raced another push, all of them fail
that test and all of them would pass a test that only asked git. Nothing is
deleted on the strength of an intention.

What each kind of staged file is, and when it is spent:

  a crop, <year>-<slug>.jpg   the portrait itself, or a candidate for it.
                              Spent once that portrait is verified live.
  a page, <year>-n<leaf>.jpg  a whole yearbook page, working material that
                              several people may still be cut from. Re-fetchable
                              at any time with talisman.py, so --pages sweeps
                              them once the researchers have finished.
  anything in _rejected/      confirmed to be the wrong person. Never going to
                              be published, so it goes with --delete.
"""

import argparse
import hashlib
import json
import re
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAGE = Path.home() / "Desktop" / "SGA60 photo hunt"
PHOTOS = ROOT / "data" / "photos"
OVERLAY = ROOT / "data" / "photos.json"
SITE = "https://sga60.vercel.app/photos/"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

# Working material: a scanned leaf, or a whole volume pulled down in one go.
# Researchers on the rate-limited years fetch the entire yearbook rather than
# spend a paced request per page, which is the right call and also what fills
# the disk: one volume runs to a hundred megabytes. Both kinds are re-fetchable
# and neither is ever published, so they are swept together.
PAGE = re.compile(r"^\d{4}-n\d+\.jpg$", re.I)
VOLUME = re.compile(r"\.(pdf|zip|djvu|txt)$", re.I)


def working_material(p):
    return bool(PAGE.match(p.name) or VOLUME.search(p.name))


def sha(b):
    return hashlib.sha256(b).hexdigest()


def live(name):
    """Is this exact file being served by the site right now?"""
    req = urllib.request.Request(SITE + name, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            if r.status != 200:
                return False, f"HTTP {r.status}"
            body = r.read()
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}"
    except (urllib.error.URLError, TimeoutError) as e:
        return False, f"unreachable ({e})"
    if body[:2] != b"\xff\xd8" and body[:4] != b"\x89PNG":
        return False, "served something that is not an image"
    local = PHOTOS / name
    if not local.is_file():
        return False, "not in data/photos any more"
    if sha(body) != sha(local.read_bytes()):
        return False, "live copy differs from the local one"
    return True, "live"



def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--delete", action="store_true")
    ap.add_argument("--pages", action="store_true",
                    help="also sweep whole-page scans, which are re-fetchable")
    ap.add_argument("--all", action="store_true",
                    help="the hunt is finished: clear the folder entirely")
    args = ap.parse_args()

    if not STAGE.is_dir():
        print(f"{STAGE} does not exist, nothing staged")
        return
    files = [p for p in STAGE.rglob("*")
             if p.is_file() and p.name not in ("README.txt", ".DS_Store")]
    if not files:
        print("staging folder is already empty")
        return
    print(f"{len(files)} files staged, "
          f"{sum(p.stat().st_size for p in files) / 1e6:.0f} MB")

    if args.all:
        doomed, kept = files, []
        print("\n--all: the hunt is over, clearing everything")
    else:
        published = {p["file"] for p in
                     json.loads(OVERLAY.read_text()).get("leaders", [])}
        verified, failed = set(), {}
        for name in sorted(published):
            if not any(p.name == name for p in files):
                continue          # nothing staged for it, no need to ask
            ok, why = live(name)
            (verified.add(name) if ok else failed.setdefault(name, why))
        print(f"\n{len(verified)} portraits verified live on the site")
        for name, why in sorted(failed.items()):
            print(f"  NOT deleting {name}: {why}")

        doomed = [p for p in files if p.name in verified]
        doomed += [p for p in files if p.parent.name == "_rejected"]
        if args.pages:
            doomed += [p for p in files if working_material(p)]
        doomed = sorted(set(doomed))
        kept = [p for p in files if p not in set(doomed)]
        work = [p for p in kept if working_material(p)]
        print(f"\n{len(doomed)} spent, {len(kept)} kept")
        if work and not args.pages:
            mb = sum(p.stat().st_size for p in work) / 1e6
            print(f"  {len(work)} of those kept are yearbook pages and whole "
                  f"volumes, {mb:.0f} MB.\n  They are working material several "
                  f"people may still be cut from, and re-fetchable;\n  sweep "
                  f"them with --pages once the researchers have finished.")

    if not doomed:
        print("\nnothing safe to delete yet")
        return
    freed = sum(p.stat().st_size for p in doomed)
    if not args.delete:
        print(f"\nthis was a dry run. --delete frees {freed / 1e6:.0f} MB.")
        return
    for p in doomed:
        p.unlink()
    for d in sorted(STAGE.rglob("*"), reverse=True):
        if d.is_dir() and not any(d.iterdir()):
            d.rmdir()
    print(f"\ndeleted {len(doomed)} files, freed {freed / 1e6:.0f} MB")


if __name__ == "__main__":
    main()
