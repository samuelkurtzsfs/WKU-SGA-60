# How to land your work

Read this before you finish a run. Getting research into the repository has
failed silently on this project more than once, and a run that researches for
half an hour and then loses everything is worse than a run that never started.

## The problem this exists for

Cloud runs are refused GitHub access at the platform level:

```
GitHub access is not enabled for this session.
An org admin must connect the Claude GitHub App for this organization.
HTTP 403
```

`git push`, `gh`, and the GitHub tools all return this. It is not a credential
you can fix and it is not something to raise as needing the owner's attention.
On 17 August 2026 it destroyed twelve hours of finished, fact-checked research
across five routines. Assume it may still be happening and plan for it.

## Route one: push, the normal way

```bash
gh auth setup-git
git push -u origin <your-branch>
gh pr create --title "..." --body "..."   # or comment on the open PR
```

If that works you are done. Confirm the branch is actually on origin with
`git ls-remote --heads origin` before you believe it.

## Route two: the site's research drop box

If route one is refused, the site can commit for you under its own
credentials. It needs `SGA60_SITE` and `SGA60_RESEARCH_TOKEN` in your
environment.

```bash
# one request per file. data/ and .research/ paths only.
B64=$(base64 -w0 data/years.json)
curl -sS -X POST "$SGA60_SITE/api/research/file" \
  -H "Authorization: Bearer $SGA60_RESEARCH_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"branch\":\"$BRANCH\",\"path\":\"data/years.json\",\"content_b64\":\"$B64\",\"message\":\"what changed\"}"
```

Then open or update the pull request, with your run report as the body:

```bash
curl -sS -X POST "$SGA60_SITE/api/research/pr" \
  -H "Authorization: Bearer $SGA60_RESEARCH_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"branch\":\"$BRANCH\",\"title\":\"Research: ...\",\"body\":\"...\"}"
```

Rules of the drop box:

- **Never send `site/`.** It is regenerated at deploy. Sending it wastes
  minutes and megabytes for nothing.
- Send only `data/` and `.research/` paths. Anything else is refused.
- It can only write to branches named `research-*`. It cannot touch `main` and
  it cannot merge. That is deliberate.
- JSON files are parsed before they are committed, so a broken file is refused
  rather than published.
- **Read the response.** Success is `{"ok": true, ...}`. Anything else means it
  did not save, whatever the exit code says. A script that reports success
  while producing nothing has happened four times on this project.

## Route three: the report

Only if both routes fail. Put every finding, with its source URL, into your
final run output. Describe it as "findings preserved in report for the editor."
Do not phrase it as a problem needing anyone's attention: it is a known
platform gate and the next run lands the work automatically.

Never abandon verified research because a push was refused, and never push to
`main`.
