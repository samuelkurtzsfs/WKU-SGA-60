#!/usr/bin/env python3
"""Checks the contributor layer's rules without touching GitHub.

Signing, who may edit what, and the validation that stands between a
contributor and the archive. Exit 1 on any failure, so it can gate a deploy
the same way check_data.py does.

    python3 scripts/check_contrib.py
"""
import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("SESSION_SECRET", "test-only-secret")
os.environ.setdefault("GITHUB_TOKEN", "test-only-token")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "api"))
import index as A  # noqa: E402

FAILED = []


def check(name, cond):
    if not cond:
        FAILED.append(name)
    print(f'  {"ok  " if cond else "FAIL"}  {name}')


def main():
    print("signing")
    tok = A.sign({"t": "session", "email": "a@b.c", "exp": time.time() + 60})
    check("a token round trips", A.unsign(tok)["email"] == "a@b.c")
    check("a tampered token is refused", A.unsign("x" + tok) is None)
    check("a forged signature is refused", A.unsign(tok.split(".")[0] + ".AAAA") is None)
    check("an expired token is refused",
          A.unsign(A.sign({"t": "session", "exp": time.time() - 1})) is None)
    check("nonsense is refused", A.unsign("nonsense") is None)

    print("who may edit what")
    check("the editor may edit any year", A.may_edit({"admin": True, "years": []}, "1994-95"))
    check("a star means every year", A.may_edit({"years": ["*"]}, "1994-95"))
    check("a contributor may edit their own year", A.may_edit({"years": ["1994-95"]}, "1994-95"))
    check("and no other year", not A.may_edit({"years": ["1994-95"]}, "1995-96"))
    check("nobody with no years may edit", not A.may_edit({"years": []}, "1994-95"))

    print("what the archive refuses")
    old = {"id": "1994-95", "leaders": [{"name": "Jane Doe", "role": "president"}],
           "events": []}
    good = {"id": "1994-95", "leaders": [{"name": "Jane Doe", "role": "president"}],
            "events": [{"date": "1994-09-01", "title": "T", "body": "B",
                        "src": {"label": "Herald", "url": "https://x.test/a"}}]}

    def probs(mut):
        y = json.loads(json.dumps(good))
        mut(y)
        return A.validate_year(y, old)

    check("a sound year is accepted", A.validate_year(json.loads(json.dumps(good)), old) == [])
    y = json.loads(json.dumps(good))
    A.validate_year(y, old)
    check("status is set from the entry count", y["status"] == "partial")
    check("an entry with no source is refused",
          any("No source" in p for p in probs(lambda y: y["events"][0].pop("src"))))
    check("a source that is not a link is refused",
          any("http link" in p for p in
              probs(lambda y: y["events"][0]["src"].update(url="javascript:alert(1)"))))
    check("a date that is not YYYY-MM-DD is refused",
          any("YYYY-MM-DD" in p for p in probs(lambda y: y["events"][0].update(date="Sept 94"))))
    check("an entry with no title is refused",
          any("needs a title" in p for p in probs(lambda y: y["events"][0].update(title=" "))))
    check("an entry with no body is refused",
          any("needs a body" in p for p in probs(lambda y: y["events"][0].update(body=" "))))
    check("removing a person from a year is refused",
          any("cannot remove a leader" in p for p in probs(lambda y: y["leaders"].clear())))
    check("an invented role is refused",
          any("must be president" in p for p in probs(lambda y: y["leaders"][0].update(role="king"))))
    check("changing a year's id is refused",
          any("id cannot be changed" in p for p in probs(lambda y: y.update(id="1899-00"))))
    check("adding a person is allowed",
          probs(lambda y: y["leaders"].append({"name": "New Person", "role": "regent"})) == [])

    print("the research drop box can only reach research branches")
    def refuses(name):
        try:
            A.safe_branch(name)
            return False
        except A.Res:
            return True
    check("a research branch is allowed", A.safe_branch("research-profiles") == "research-profiles")
    check("main is refused", refuses("main"))
    check("a sneaky main is refused", refuses("research-x/../main"))
    check("an empty branch is refused", refuses(""))
    check("someone else's branch is refused", refuses("feature-x"))
    check("a ref path is refused", refuses("refs/heads/main"))

    print("the commit it writes")
    msg = A.commit_message({"name": "Jane Doe", "email": "j@x.test",
                            "role": "President, 1994-95"},
                           "1994-95, as Jane Doe recorded it", "fixed a date")
    check("names the contributor", "Contributed-By: Jane Doe <j@x.test>" in msg)
    check("carries no tool attribution",
          not any(s in msg.lower() for s in ("co-authored", "generated with", "claude")))

    print()
    if FAILED:
        print(f"{len(FAILED)} check(s) failed:")
        for f in FAILED:
            print(f"  - {f}")
        return 1
    print("the contributor layer checks out against its own rules")
    return 0


if __name__ == "__main__":
    sys.exit(main())
