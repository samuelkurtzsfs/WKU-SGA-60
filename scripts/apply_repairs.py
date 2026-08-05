#!/usr/bin/env python3
"""
Apply an editor's repair pass to programme entries that failed fact-checking.

Each repair file holds one decision per rejected entry: `rewrite`, with a body
in which every clause is supported by the cited source, or `drop`. Rewrites are
handed to the ordinary programme merge, which enforces the dating law and the
no-source-no-entry rule; drops are recorded so the decision is not lost.

Usage: python3 scripts/apply_repairs.py .research/repaired-*.json
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main(paths):
    rewrites, drops = [], []
    for p in paths:
        for r in json.loads(Path(p).read_text()):
            (rewrites if r.get("action") == "rewrite" else drops).append(r)

    out = ROOT / ".research" / "programs-repaired.json"
    out.write_text(json.dumps(rewrites, ensure_ascii=False, indent=1) + "\n")
    log = ROOT / ".research" / "programs-dropped.json"
    log.write_text(json.dumps(drops, ensure_ascii=False, indent=1) + "\n")

    print(f"{len(rewrites)} rewritten, {len(drops)} dropped")
    for d in drops:
        print(f"  dropped {d.get('year')}: {d.get('title', '')[:64]}")
        print(f"    {d.get('why', '')[:150]}")
    print(f"\nwrote {out.relative_to(ROOT)} - merge it with:")
    print(f"  python3 scripts/merge_programs.py {out.relative_to(ROOT)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: apply_repairs.py FILE [FILE ...]")
    main(sys.argv[1:])
