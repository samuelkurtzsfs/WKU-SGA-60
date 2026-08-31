#!/usr/bin/env python3
"""Clear the photo-hunt staging folder of anything already published.

    python3 scripts/clear_photo_stage.py            # show what would go
    python3 scripts/clear_photo_stage.py --delete   # delete it

The hunt downloads full yearbook pages at three thousand pixels a side and
throws most of them away. They pile up on the Desktop, which is where the owner
wants them while the work is going on, and nowhere at all once it is finished.

A staged file is safe to delete when the portrait cut from it is in
data/photos.json AND committed. Not merely present on disk: a portrait that
has not been committed could still be lost, and then the page it came from
would be the only copy left. Anything the archive has no record of is kept and
listed, because that is either work still in progress or a mistake worth
seeing.
"""

import argparse
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAGE = Path.home() / "Desktop" / "SGA60 photo hunt"
PHOTOS = ROOT / "data" / "photos"
OVERLAY = ROOT / "data" / "photos.json"


def committed():
    """Portrait files git has, so losing the staged original costs nothing."""
    out = subprocess.run(["git", "ls-files", "data/photos"], cwd=ROOT,
                         capture_output=True, text=True)
    return {Path(p).name for p in out.stdout.split() if p}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--delete", action="store_true")
    ap.add_argument("--all", action="store_true",
                    help="the hunt is over: clear the folder entirely")
    args = ap.parse_args()

    if not STAGE.is_dir():
        print(f"{STAGE} does not exist, nothing staged")
        return

    files = [p for p in STAGE.rglob("*")
             if p.is_file() and p.name not in ("README.txt", ".DS_Store")]
    if not files:
        print("staging folder is already empty")
        return
    size = sum(p.stat().st_size for p in files)
    print(f"{len(files)} files staged, {size / 1e6:.0f} MB")

    if args.all:
        doomed = files
        print("\n--all: clearing everything, the hunt is finished")
    else:
        published = {p["file"] for p in json.loads(OVERLAY.read_text())
                     .get("leaders", [])}
        safe = published & committed()
        print(f"{len(published)} portraits in the archive, "
              f"{len(safe)} of them committed")
        # a staged page is spent once every portrait naming it is committed,
        # and a staged file that IS a portrait goes once its copy is committed
        doomed = [p for p in files if p.name in safe]
        keep = [p for p in files if p not in doomed]
        print(f"\n{len(doomed)} staged files are published and committed")
        print(f"{len(keep)} are not, and are kept:")
        for p in sorted(keep)[:25]:
            print(f"   {p.relative_to(STAGE)}")
        if len(keep) > 25:
            print(f"   ... and {len(keep) - 25} more")

    if not doomed:
        print("\nnothing to delete yet")
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
