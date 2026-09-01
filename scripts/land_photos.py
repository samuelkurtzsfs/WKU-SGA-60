#!/usr/bin/env python3
"""Land whatever the portrait hunters have dropped, end to end.

    python3 scripts/land_photos.py            # show what would happen
    python3 scripts/land_photos.py --write    # merge, build, check, commit, push

Merge the findings, rebuild the site, run the archive's own checks, commit and
push, then clear the staging folder of anything now safely committed. Written
because the hunt runs overnight and this sequence gets run every time an agent
reports, and a step skipped at three in the morning is a step skipped.

Nothing is committed if the checks fail. The archive would rather publish
nothing than publish a face it cannot stand behind.
"""

import argparse
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from clear_photo_stage import live

ROOT = Path(__file__).resolve().parent.parent


def run(cmd, check=True):
    print(f"\n$ {' '.join(cmd)}")
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    if out:
        print("\n".join(out.splitlines()[-18:]))
    if check and r.returncode:
        sys.exit(f"\nstopped: {cmd[0]} exited {r.returncode}")
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    py = sys.executable
    if not args.write:
        run([py, "scripts/merge_photo_finds.py"])
        print("\nthis was a dry run. --write to land it.")
        return

    before = run(["git", "rev-parse", "HEAD"]).stdout.strip()
    run([py, "scripts/merge_photo_finds.py", "--write"])
    run([py, "scripts/build.py"])
    run([py, "scripts/check_data.py"])

    run(["git", "add", "-A", "data/photos", "data/photos.json",
         "data/photo-finds", "site"])
    staged = run(["git", "diff", "--cached", "--name-only"]).stdout.split()
    if not staged:
        print("\nnothing new to commit")
        return
    n = len([f for f in staged if f.startswith("data/photos/")])
    run(["git", "commit", "-q", "-m",
         f"Portraits: {n} more faces from the yearbooks and the Herald\n\n"
         "Each one carries the caption that identifies the person in it."])
    run(["git", "push", "-q", "origin", "main"])
    after = run(["git", "rev-parse", "HEAD"]).stdout.strip()
    print(f"\npushed {before[:8]} -> {after[:8]}")

    # A push is not a deploy. Vercel takes a minute or two to build, and the
    # cleanup only deletes what it can fetch back off the live site, so going
    # straight there would find nothing published and clear nothing, every
    # time. Wait for one of the new portraits to actually appear.
    newest = sorted(f for f in staged if f.startswith("data/photos/"))
    if newest:
        name = Path(newest[-1]).name
        print(f"\nwaiting for the deploy: {name}")
        for attempt in range(20):
            ok, why = live(name)
            if ok:
                print(f"  live after about {attempt * 20}s")
                break
            time.sleep(20)
        else:
            print(f"  still not live after ~7 minutes ({why}). Nothing will "
                  f"be deleted; the next run will pick it up.")

    # only now is it safe to throw the working files away
    run([py, "scripts/clear_photo_stage.py", "--delete"], check=False)


if __name__ == "__main__":
    main()
