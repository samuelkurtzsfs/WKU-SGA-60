# Setup — from this folder to a live website

Written assuming you have never used GitHub or Vercel. Follow it top to bottom. About 25 minutes.

---

## First: the thing you asked about that does not work

You asked to have the site auto-build "using the subscription API key." Two corrections, and the
second one is good news.

**1. A Pro or Max subscription does not come with an API key.** The Anthropic API is billed
separately through `console.anthropic.com` on its own balance. You *can* point the Claude GitHub
Action at a subscription using an OAuth token from `claude setup-token`, but those tokens currently
expire in about a day, so it breaks constantly in CI. The only reliable CI path is a paid API key,
which is money on top of what you already pay.

**2. You do not need any of that, because the build has no AI in it.** `scripts/build.py` is plain
Python. It reads a JSON file and writes HTML. It does not call a model, does not touch the network
and finishes in about a second. So "auto-build on every change" is free and always has been.

The split that actually makes sense:

| Job | Where it happens | Costs |
|---|---|---|
| **Research** — reading the archive, writing entries | You, in Claude Code, on your Max subscription | Included |
| **Build** — turning JSON into 62 HTML pages | Vercel, automatically, on every push | Free |

Research is a judgement task with a human reading sources. It should not run on a cron job at 3am
with nobody checking it. That is how a history site ends up full of confident nonsense.

---

## Step 1 — Install the two things you need

**Git** (moves files to GitHub)
- Mac: open Terminal, type `git --version`, press enter. If it asks to install developer tools, say yes.
- Windows: download from `git-scm.com`, run the installer, accept every default.

**Python 3** (runs the build locally so you can preview)
- Mac: already installed. Check with `python3 --version`.
- Windows: get it from `python.org`. **Tick "Add Python to PATH"** on the first installer screen.

You do not need Node, npm or anything else.

---

## Step 2 — Make the GitHub repository

1. Go to `github.com` and make a free account if you do not have one.
2. Click the **+** in the top right, then **New repository**.
3. Name it `sga60`. Leave it **Public** — this is a public history project and public repos get free
   everything.
4. Do **not** tick "Add a README". You already have files.
5. Click **Create repository**.
6. Leave that page open. You will need the commands on it in a moment.

---

## Step 3 — Push this folder up

Open Terminal (Mac) or Git Bash (Windows). Type `cd ` — with a space — then drag the `sga60` folder
onto the window. It fills in the path. Press enter.

Now paste these one line at a time. Replace `YOURNAME` with your GitHub username.

```bash
git init
git add .
git commit -m "SGA 60: year-keyed record of WKU student government"
git branch -M main
git remote add origin https://github.com/YOURNAME/sga60.git
git push -u origin main
```

It will ask you to sign in. Follow the browser prompt.

Refresh the GitHub page. Your files are there.

---

## Step 4 — Connect Vercel

**Do not use the drag-and-drop.** Drag-and-drop uploads a frozen copy — it has no idea your files
changed, so you would be re-dragging the folder every single time you edit one line. Connecting the
repo takes two extra minutes and then never needs touching again.

1. Go to `vercel.com`, click **Sign Up**, choose **Continue with GitHub**.
2. On your Vercel dashboard click **Add New → Project**.
3. Find `sga60` in the list, click **Import**.
4. Now the only screen that matters. Set exactly this:

   - **Framework Preset:** `Other`
   - **Build Command:** `python3 scripts/build.py`
   - **Output Directory:** `site`
   - **Install Command:** leave it empty

   Open the **Build and Output Settings** section if you do not see those fields.
5. Click **Deploy**.

Ninety seconds later you get a URL like `sga60-abc123.vercel.app`. That is the live site.

**From now on:** every time you push to GitHub, Vercel rebuilds and redeploys on its own. That is the
auto-build you wanted. No key, no token, no cost.

### If the build fails
Open the deployment, read the log. Two likely causes:
- `python3: command not found` → change the Build Command to `python scripts/build.py`
- A JSON error → you broke `data/years.json`. See Step 6.

---

## Step 5 — Point a real domain at it (optional)

In Vercel: **Settings → Domains → Add**. Type the domain. Vercel shows you two DNS records to create
at whoever sold you the domain. Add them, wait, done. HTTPS sets itself up.

If WKU will give you something like `sga60.wku.edu`, campus IT adds one CNAME record on their end.
Ask early — that request takes longer than everything else on this page.

---

## Step 6 — The daily loop

This is what you will actually do for the next few weeks.

```bash
# 1. get the latest
git pull

# 2. do research, edit data/years.json

# 3. rebuild and look at it
python3 scripts/build.py
open site/index.html          # Windows: start site\index.html

# 4. ship it
git add .
git commit -m "1974-75: added Herald election coverage"
git push
```

That last push triggers Vercel. The live site updates in about a minute.

**Edit `data/years.json` only.** Everything in `site/` is generated and gets overwritten every build.

**If you break the JSON**, the build fails and the live site keeps showing the last good version.
Nothing is lost. Check for a missing comma or a stray quote. A free JSON linter online will point at
the exact line.

---

## Step 7 — Turn Claude Code loose on the research

Install it: `npm install -g @anthropic-ai/claude-code`, then run `claude` inside the `sga60` folder
and sign in with your Max subscription.

`CLAUDE.md` in this folder tells it the rules. Give it one decade at a time, not the whole thing:

> Read CLAUDE.md and RESEARCH.md. Work on the years 1974-75 through 1979-80 only. For each year,
> verify the leader names first, then run the year sweep, then add events to data/years.json.
> Run scripts/build.py when you are done and tell me what you could not confirm.

One decade per session. Check its work before you push. It will be right most of the time and
confidently wrong occasionally, and a history project only gets one reputation.

---

## What is in this folder

```
data/years.json        the only file you edit
scripts/build.py       generator — JSON to HTML
scripts/migrate.py     one-time, already run, keep for reference
site/                  generated output. never edit by hand
CLAUDE.md              rules for Claude Code
RESEARCH.md            the research method
SETUP.md               this file
```
