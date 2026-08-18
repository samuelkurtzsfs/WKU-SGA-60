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

`gh` is **not installed** in these containers, so do not start with
`gh auth setup-git` and do not waste minutes downloading the binary. Git is
already credentialed. Test it without changing anything:

```bash
git push --dry-run origin HEAD:refs/heads/access-probe
```

A line reading `* [new branch] HEAD -> access-probe` means you have write
access. Then push for real:

```bash
git push -u origin <your-branch>
```

For pull requests, use the GitHub MCP tools rather than `gh`. Load them with
`ToolSearch` for `mcp__github__list_pull_requests`,
`mcp__github__pull_request_read`, `mcp__github__add_issue_comment`,
`mcp__github__create_pull_request` and `mcp__github__merge_pull_request`.

Confirm the branch really is on origin with `git ls-remote --heads origin`
before you believe it.

## Beware: main is an orphan history

`main` and the older `research-*` branches from 4 August have **different root
commits and no merge base**. Those branches are snapshots of a superseded
repository, not forks of main. Merging one deletes `herald-index-full.json`,
`legislation-authors.json`, `name-aliases.json`, the contributor layer and the
validators.

Never merge a branch into main without checking `git merge-base origin/main
<branch>` first. If there is no merge base, compare file contents
(`git diff origin/main <branch> -- ':!site'`), take only what main genuinely
lacks, and apply it as a fresh commit on a branch cut from current main.

Branches you create yourself from current `origin/main` are ordinary branches
and merge normally. This warning is about the 4 August ones.

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
