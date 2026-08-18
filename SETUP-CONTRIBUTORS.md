# Turning on the contributor system

Written for Sam, 17 August 2026. No coding required. Everything below is
copying values into boxes on two websites.

The code is already live. Until the keys below are set, the sign-in page loads
and then says the system is not configured yet. Nothing is broken in the
meantime, and the rest of the site is unaffected.

---

## Part 1, urgent: the research bots cannot save anything

This is separate from the contributor system and it is costing you real work
right now.

The five research routines run fine. They read the archive, do the research,
fact-check it with a second agent, and rebuild the site. Then they try to push
to GitHub and get this back:

> GitHub access is not enabled for this session. An org admin must connect the
> Claude GitHub App for this organization.

Every route is blocked: plain `git push`, the `gh` command, and the GitHub
tools. So each run finishes its work and then dies with its container. Twelve
hours of research has already gone this way, including ten finished and
fact-checked officer profiles for the early 1970s.

**The fix, and it is one command.** In a Claude Code terminal session, type:

```
/web-setup
```

That takes the GitHub token your terminal is already signed in with, which is
`samuelkurtzsfs` with the `repo` scope, and syncs it to your Claude account.
Cloud sessions then reach GitHub with the same access you have.

There is a second way, authorizing the Claude GitHub App at
<https://github.com/apps/claude>. Either one works on its own; you do not need
both.

Two things that are easy to get wrong here:

- **Installing the App on the repository is not what grants session access.**
  It only turns on pull request webhooks. If the App is already installed and
  the routines still fail, installing it again changes nothing. Run
  `/web-setup`.
- The GitHub option inside a Claude chat, for adding repository files to a
  conversation, is a different feature and does not affect cloud sessions.

Afterwards, re-run one routine from <https://claude.ai/code/routines> and check
that a `research-*` branch appears on GitHub. That is the proof it worked.

**If that does not work**, the site now has a way around it, described in Part
3 below. Either path fixes the problem. The GitHub connection is the cleaner
one because the routines are already written for it.

---

## Part 2: the keys the contributor system needs

These go on Vercel, which is where the site is hosted.

1. Go to <https://vercel.com>, open the SGA 60 project.
2. Settings, then Environment Variables.
3. Add each of the following, for all three environments (Production, Preview,
   Development).

| Name | What to put in it |
|---|---|
| `GITHUB_TOKEN` | A GitHub token so the site can save people's edits. How to make one is below. |
| `SESSION_SECRET` | A long random string. Make one by running `python3 -c "import secrets; print(secrets.token_urlsafe(48))"` in Terminal. Never share it. |
| `SITE_URL` | The site's address, with no slash on the end. For example `https://wku-sga-60.vercel.app`. |
| `MAIL_FROM` | The address sign-in emails come from. If you use the Gmail option below, use your own Gmail address. |
| `RESEARCH_TOKEN` | Another long random string, made the same way as `SESSION_SECRET`. Only needed for Part 3. |

Then **one** of these two ways of sending email:

**Gmail (simplest, good for a handful of people)**

| Name | Value |
|---|---|
| `SMTP_HOST` | `smtp.gmail.com` |
| `SMTP_PORT` | `587` |
| `SMTP_USER` | your Gmail address |
| `SMTP_PASS` | a Google app password, not your normal password |

To get an app password: Google Account, Security, turn on 2-Step Verification
if it is not already on, then App passwords, and make one called "SGA 60".
Google shows you sixteen letters. That is the value.

**Resend (better if this grows)**

Sign up at <https://resend.com>, verify a domain you own, make an API key, and
set `RESEND_API_KEY`. Without a verified domain Resend will only deliver to
your own address, which is why Gmail is the better starting point.

### Making the GitHub token

1. Go to <https://github.com/settings/personal-access-tokens/new>.
2. Token name: `SGA 60 site`.
3. Expiration: a year.
4. Repository access: Only select repositories, and pick `WKU-SGA-60`.
5. Permissions: under Repository permissions set **Contents** to
   **Read and write**, and **Pull requests** to **Read and write**. Leave
   everything else alone.
6. Generate, copy the token, and paste it into Vercel as `GITHUB_TOKEN`. You
   cannot see it again after you leave the page.

After adding all of them, go to Deployments and redeploy the latest one, so
the new settings are picked up.

---

## Part 3: the way around the blocked bots

If Part 1 does not work, the site can take finished research straight from the
bots and put it on a branch itself, without going through the platform's
GitHub. It can only write to branches whose names begin with `research-`, it
cannot touch the live site, and it cannot merge anything. Publishing stays a
decision the editor routine makes.

The routines are already written to try this whenever a push is refused. It
needs four values, in two places.

**On Vercel** (same screen as Part 2): `GITHUB_TOKEN` and `RESEARCH_TOKEN`.

**On the Claude cloud environment**, which is where the bots run. Go to
<https://claude.ai/code/environments>, open "Scholarfi Cloud", and add:

| Name | Value |
|---|---|
| `SGA60_SITE` | the same address you used for `SITE_URL`, no slash on the end |
| `SGA60_RESEARCH_TOKEN` | exactly the same string you used for `RESEARCH_TOKEN` on Vercel |

The two `RESEARCH_TOKEN` values must match: that is the whole of the security.
Treat it like a password. If it ever leaks, generate a new one and change it in
both places.

Once those are set, a bot that gets refused by GitHub will post its work to the
site instead and open its pull request that way. If neither route works it
falls back to writing everything into its run report, so research is never
silently lost.

---

## How it works once it is on

**Someone who served goes to `/contribute.html`**, puts in their email, and
says who they were. If they are already approved, a sign-in link arrives. If
not, the request lands on your desk. The page gives the same answer either way,
so nobody can use it to work out who has an account.

**You approve them at `/admin.html`**, which only you can open. You set their
name, their title, and which years they may edit. They get an email.

**They edit at `/edit.html`.** They can fix notes, write profiles, and add,
change or remove entries in their year. They can also write a first-hand piece
that appears under "in their own words" on their year and on `/voices.html`.

**Every save is a commit in their name.** The site rebuilds and the change is
public in about a minute. Your admin page lists every change any contributor
has made, with an Undo button that puts the files back the way they were.

### What contributors cannot do

- Remove a person from a year. That needs a source, not a memory, so it stays
  with you.
- Add a dated entry with no citation. The same rule the build enforces is
  enforced at the door, and they get told which entry failed and why.
- Touch a year that is not theirs.
- Change the design, the other pages, or anyone else's writing.

### If you need to take someone's access away

Edit `data/contributors.json` in the repository and remove their block, or
change `"status"` to anything other than `"approved"`. It takes effect on their
next request, without a rebuild.

---

## Checking it still works

```bash
python3 scripts/check_contrib.py   # the rules the contributor layer enforces
python3 scripts/check_data.py      # the rules the archive enforces
python3 scripts/build.py           # rebuild the site
```

The first of those runs entirely offline and touches nothing.
