"""The contributor layer for SGA 60.

Everything a signed-in contributor does ends up as a commit on main, made in
their own name. There is no database: the roster, the access requests, the
posts and the archive itself are all files in this repository, so the edit
history is the git history and a revert is a real revert.

One function serves every /api/* route. vercel.json rewrites them all here.

Environment it needs:
  GITHUB_TOKEN    fine-grained token, contents read+write on this repo
  GITHUB_REPO     owner/name, defaults to samuelkurtzsfs/WKU-SGA-60
  SESSION_SECRET  any long random string; signs the sign-in links and cookies
  SITE_URL        https://... , used to build the sign-in link
  MAIL_FROM       the From: address on sign-in mail
  and either
  RESEND_API_KEY  to send through Resend
  or
  SMTP_HOST / SMTP_PORT / SMTP_USER / SMTP_PASS   to send through any mailbox
"""

import base64
import hashlib
import hmac
import json
import os
import re
import smtplib
import time
import urllib.error
import urllib.parse
import urllib.request
from email.message import EmailMessage
from http.server import BaseHTTPRequestHandler

REPO = os.environ.get("GITHUB_REPO", "samuelkurtzsfs/WKU-SGA-60")
BRANCH = os.environ.get("GITHUB_BRANCH", "main")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
SECRET = os.environ.get("SESSION_SECRET", "")
SITE_URL = os.environ.get("SITE_URL", "").rstrip("/")
MAIL_FROM = os.environ.get("MAIL_FROM", "")

ROSTER = "data/contributors.json"
REQUESTS = "data/access-requests.json"
YEARS = "data/years.json"
POSTS = "data/posts"

LOGIN_TTL = 30 * 60           # a sign-in link is good for half an hour
SESSION_TTL = 30 * 24 * 3600  # a session lasts a month
API = "https://api.github.com"


# ---------------------------------------------------------------- signing
# Tokens are HMAC-signed JSON. Nothing is stored server side, so there is no
# session table to keep and no state to lose.

def b64e(raw):
    return base64.urlsafe_b64encode(raw).decode().rstrip("=")


def b64d(s):
    return base64.urlsafe_b64decode(s + "=" * (-len(s) % 4))


def sign(payload):
    body = b64e(json.dumps(payload, separators=(",", ":"), sort_keys=True).encode())
    mac = hmac.new(SECRET.encode(), body.encode(), hashlib.sha256).digest()
    return f"{body}.{b64e(mac)}"


def unsign(token):
    """Return the payload, or None if the signature or the expiry fails."""
    try:
        body, mac = token.split(".", 1)
        want = hmac.new(SECRET.encode(), body.encode(), hashlib.sha256).digest()
        if not hmac.compare_digest(b64d(mac), want):
            return None
        payload = json.loads(b64d(body))
    except Exception:
        return None
    if payload.get("exp", 0) < time.time():
        return None
    return payload


# ---------------------------------------------------------------- github
def gh(method, path, body=None):
    """One call to the GitHub API. Returns (status, parsed body)."""
    req = urllib.request.Request(
        API + path, method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"Authorization": f"Bearer {TOKEN}",
                 "Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28",
                 "Content-Type": "application/json",
                 "User-Agent": "sga60-contrib"})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            return r.status, json.loads(r.read() or b"null")
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            return e.code, json.loads(raw or b"null")
        except Exception:
            return e.code, {"message": raw.decode("utf-8", "replace")[:400]}


def get_file(path, ref=None):
    """Return (text, sha). Missing file gives (None, None)."""
    q = f"?ref={urllib.parse.quote(ref or BRANCH)}"
    st, data = gh("GET", f"/repos/{REPO}/contents/{urllib.parse.quote(path)}{q}")
    if st != 200 or not isinstance(data, dict) or "content" not in data:
        return None, None
    return base64.b64decode(data["content"]).decode("utf-8"), data["sha"]


def get_json(path, default=None):
    text, sha = get_file(path)
    if text is None:
        return (default if default is not None else None), None
    try:
        return json.loads(text), sha
    except json.JSONDecodeError:
        return (default if default is not None else None), sha


def put_file(path, text, sha, message, author=None):
    """Write a file. Returns (ok, response). 409 means someone else moved first."""
    body = {"message": message, "branch": BRANCH,
            "content": base64.b64encode(text.encode()).decode()}
    if sha:
        body["sha"] = sha
    if author:
        body["author"] = author
        body["committer"] = {"name": "SGA 60", "email": author["email"]}
    st, data = gh("PUT", f"/repos/{REPO}/contents/{urllib.parse.quote(path)}", body)
    return st in (200, 201), data


def commit_message(who, summary, detail=""):
    """Plain editorial voice, plus a trailer the admin page can filter on."""
    lines = [summary, ""]
    if detail:
        lines += [detail.strip(), ""]
    lines.append(f"Contributed-By: {who['name']} <{who['email']}>")
    if who.get("role"):
        lines.append(f"Contributor-Role: {who['role']}")
    return "\n".join(lines)


# ---------------------------------------------------------------- mail
def send_mail(to, subject, text):
    if os.environ.get("RESEND_API_KEY"):
        req = urllib.request.Request(
            "https://api.resend.com/emails", method="POST",
            data=json.dumps({"from": MAIL_FROM, "to": [to],
                             "subject": subject, "text": text}).encode(),
            headers={"Authorization": f"Bearer {os.environ['RESEND_API_KEY']}",
                     "Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status < 300
    host = os.environ.get("SMTP_HOST")
    if not host:
        raise RuntimeError("no mail transport configured")
    msg = EmailMessage()
    msg["From"] = MAIL_FROM
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(text)
    port = int(os.environ.get("SMTP_PORT", "587"))
    with smtplib.SMTP(host, port, timeout=20) as s:
        s.starttls()
        if os.environ.get("SMTP_USER"):
            s.login(os.environ["SMTP_USER"], os.environ.get("SMTP_PASS", ""))
        s.send_message(msg)
    return True


# ---------------------------------------------------------------- roster
def norm_email(e):
    return (e or "").strip().lower()


def load_roster():
    data, sha = get_json(ROSTER, {"contributors": []})
    return data.get("contributors", []), sha


def find_contributor(email):
    email = norm_email(email)
    for c in load_roster()[0]:
        if norm_email(c.get("email")) == email and c.get("status") == "approved":
            return c
    return None


def may_edit(who, year_id):
    if who.get("admin"):
        return True
    years = who.get("years") or []
    return "*" in years or year_id in years


# ---------------------------------------------------------------- validation
# A contributor is trusted with their own year, not with the rules. These are
# the invariants check_data.py enforces at build time, applied here so a bad
# edit is refused at the door rather than breaking the deploy.

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
URL_RE = re.compile(r"^https?://", re.I)


def validate_year(new, old):
    """Return a list of problems. Empty list means it can be committed."""
    bad = []
    if not isinstance(new, dict):
        return ["The year must be an object."]
    if new.get("id") != old.get("id"):
        bad.append("The year's id cannot be changed.")

    for i, e in enumerate(new.get("events") or []):
        where = f'Event {i + 1} ("{str(e.get("title", ""))[:40]}")'
        if not isinstance(e, dict):
            bad.append(f"Event {i + 1} is not an object.")
            continue
        if not DATE_RE.match(str(e.get("date", ""))):
            bad.append(f"{where} needs a date as YYYY-MM-DD. "
                       "Use 01 for the day if you only know the month.")
        if not str(e.get("title", "")).strip():
            bad.append(f"{where} needs a title.")
        if not str(e.get("body", "")).strip():
            bad.append(f"{where} needs a body.")
        src = e.get("src")
        if not isinstance(src, dict) or not URL_RE.match(str(src.get("url", ""))):
            bad.append(f"{where} needs a source with a working http link. "
                       "No source, no entry.")
        elif not str(src.get("label", "")).strip():
            bad.append(f"{where} needs a label on its source saying what it is.")

    old_names = {l.get("name") for l in (old.get("leaders") or [])}
    new_names = {l.get("name") for l in (new.get("leaders") or [])}
    gone = old_names - new_names
    if gone:
        bad.append("You cannot remove a leader from a year through the editor: "
                   + ", ".join(sorted(str(g) for g in gone))
                   + ". Send a correction to the editor instead, with the source.")

    for l in new.get("leaders") or []:
        if l.get("role") not in (None, "president", "regent", "unresolved"):
            bad.append(f'{l.get("name")} has a role of "{l.get("role")}". '
                       "It must be president, regent or unresolved.")
        for p in l.get("profile") or []:
            if not str(p).strip():
                bad.append(f'{l.get("name")} has an empty profile paragraph.')

    n = len(new.get("events") or [])
    want = "researched" if n >= 3 else ("partial" if n else "empty")
    if new.get("status") != want:
        new["status"] = want
    return bad


# ---------------------------------------------------------------- responses
class Res(Exception):
    def __init__(self, status, payload, headers=None):
        self.status, self.payload, self.headers = status, payload, headers or []


def need_session(handler):
    cookie = handler.headers.get("Cookie", "")
    raw = ""
    for part in cookie.split(";"):
        k, _, v = part.strip().partition("=")
        if k == "sga60":
            raw = v
    payload = unsign(raw) if raw else None
    if not payload or payload.get("t") != "session":
        raise Res(401, {"error": "Not signed in."})
    who = find_contributor(payload["email"])
    if not who:
        raise Res(403, {"error": "That account is no longer approved."})
    return who


def need_admin(handler):
    who = need_session(handler)
    if not who.get("admin"):
        raise Res(403, {"error": "That is for the editor only."})
    return who


# ---------------------------------------------------------------- routes
def r_auth_request(handler, body):
    """Either send a sign-in link, or lodge a request for access."""
    email = norm_email(body.get("email"))
    if "@" not in email or len(email) > 200:
        raise Res(400, {"error": "That does not look like an email address."})

    who = find_contributor(email)
    if who:
        token = sign({"t": "login", "email": email, "exp": time.time() + LOGIN_TTL})
        link = f"{SITE_URL}/api/auth/callback?token={urllib.parse.quote(token)}"
        send_mail(email, "Your sign-in link for SGA 60",
                  f"Hello {who.get('name', '').split(' ')[0]},\n\n"
                  f"Here is your sign-in link for the SGA 60 archive. It works once "
                  f"and it expires in thirty minutes.\n\n{link}\n\n"
                  f"If you did not ask for this, you can ignore it. Nobody can sign "
                  f"in as you without this link.\n")
        return {"ok": True, "state": "sent"}

    # Not on the roster. Record the ask so the editor sees it, and say the same
    # thing either way so the form cannot be used to test who has an account.
    pending, sha = get_json(REQUESTS, {"requests": []})
    rows = pending.get("requests", [])
    if not any(norm_email(r.get("email")) == email and r.get("status") == "pending"
               for r in rows):
        rows.append({"email": email,
                     "name": str(body.get("name", ""))[:120],
                     "served": str(body.get("served", ""))[:200],
                     "note": str(body.get("note", ""))[:1000],
                     "asked": time.strftime("%Y-%m-%d"),
                     "status": "pending"})
        pending["requests"] = rows
        put_file(REQUESTS, json.dumps(pending, indent=1) + "\n", sha,
                 f"Someone asked for access to the archive: {email}")
    return {"ok": True, "state": "requested"}


def r_auth_callback(handler, query):
    payload = unsign(query.get("token", [""])[0])
    if not payload or payload.get("t") != "login":
        raise Res(303, None, [("Location", "/contribute.html?err=expired")])
    who = find_contributor(payload["email"])
    if not who:
        raise Res(303, None, [("Location", "/contribute.html?err=notapproved")])
    session = sign({"t": "session", "email": norm_email(who["email"]),
                    "exp": time.time() + SESSION_TTL})
    cookie = (f"sga60={session}; Path=/; HttpOnly; Secure; SameSite=Lax; "
              f"Max-Age={SESSION_TTL}")
    raise Res(303, None, [("Location", "/edit.html"), ("Set-Cookie", cookie)])


def r_auth_logout(handler):
    raise Res(303, None, [("Location", "/contribute.html"),
                          ("Set-Cookie", "sga60=; Path=/; HttpOnly; Secure; "
                                         "SameSite=Lax; Max-Age=0")])


def r_me(handler):
    who = need_session(handler)
    return {"name": who.get("name"), "email": who.get("email"),
            "role": who.get("role", ""), "admin": bool(who.get("admin")),
            "years": who.get("years") or []}


def r_year_get(handler, query):
    who = need_session(handler)
    yid = query.get("id", [""])[0]
    if not may_edit(who, yid):
        raise Res(403, {"error": f"You are not down as able to edit {yid}."})
    doc, _ = get_json(YEARS)
    if not doc:
        raise Res(500, {"error": "Could not read the archive."})
    for y in doc["years"]:
        if y.get("id") == yid:
            return {"year": y}
    raise Res(404, {"error": f"There is no year {yid} in the archive."})


def r_year_put(handler, body):
    who = need_session(handler)
    yid = str(body.get("id", ""))
    if not may_edit(who, yid):
        raise Res(403, {"error": f"You are not down as able to edit {yid}."})
    incoming = body.get("year")

    # Re-read, re-apply and retry: the research routines commit to main too, so
    # the file can move under us between the read and the write.
    for attempt in range(4):
        text, sha = get_file(YEARS)
        if text is None:
            raise Res(500, {"error": "Could not read the archive."})
        doc = json.loads(text)
        idx = next((i for i, y in enumerate(doc["years"]) if y.get("id") == yid), None)
        if idx is None:
            raise Res(404, {"error": f"There is no year {yid} in the archive."})

        problems = validate_year(incoming, doc["years"][idx])
        if problems:
            raise Res(400, {"error": "That edit was not saved.", "problems": problems})

        stamp = incoming.setdefault("contributions", [])
        stamp.append({"by": who.get("name"), "role": who.get("role", ""),
                      "on": time.strftime("%Y-%m-%d"),
                      "note": str(body.get("message", ""))[:300]})
        doc["years"][idx] = incoming

        ok, resp = put_file(
            YEARS, json.dumps(doc, indent=1, ensure_ascii=False) + "\n", sha,
            commit_message(who, f"{yid}, as {who.get('name')} recorded it",
                           str(body.get("message", ""))),
            author={"name": who.get("name") or "SGA 60 contributor",
                    "email": who["email"]})
        if ok:
            return {"ok": True, "commit": (resp.get("commit") or {}).get("sha", "")}
        if resp and "409" not in str(resp) and attempt == 3:
            raise Res(502, {"error": "GitHub refused the change.",
                            "detail": str(resp.get("message", ""))[:300]})
        time.sleep(0.6 * (attempt + 1))
    raise Res(409, {"error": "The archive was being written to by something else. "
                             "Try again in a moment."})


def r_post_put(handler, body):
    """Create or replace one contributor's written piece."""
    who = need_session(handler)
    title = str(body.get("title", "")).strip()
    paras = [str(p).strip() for p in (body.get("body") or []) if str(p).strip()]
    yid = str(body.get("year", "")).strip()
    if not title:
        raise Res(400, {"error": "The piece needs a title."})
    if not paras:
        raise Res(400, {"error": "The piece is empty."})
    if yid and not may_edit(who, yid):
        raise Res(403, {"error": f"You are not down as connected to {yid}."})

    base = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:60] or "untitled"
    name = str(body.get("slug", "")).strip() or f"{yid + '-' if yid else ''}{base}"
    path = f"{POSTS}/{name}.json"
    _, sha = get_file(path)

    post = {"slug": name, "title": title, "year": yid,
            "author": who.get("name"), "author_role": who.get("role", ""),
            "author_email": who["email"],
            "date": time.strftime("%Y-%m-%d"), "body": paras}
    ok, resp = put_file(path, json.dumps(post, indent=1, ensure_ascii=False) + "\n", sha,
                        commit_message(who, f'"{title}", in their own words'),
                        author={"name": who.get("name") or "SGA 60 contributor",
                                "email": who["email"]})
    if not ok:
        raise Res(502, {"error": "GitHub refused the change.",
                        "detail": str((resp or {}).get("message", ""))[:300]})
    return {"ok": True, "slug": name}


def r_admin_queue(handler):
    need_admin(handler)
    pending, _ = get_json(REQUESTS, {"requests": []})
    roster, _ = load_roster()
    return {"requests": [r for r in pending.get("requests", [])
                         if r.get("status") == "pending"],
            "contributors": roster}


def r_admin_decide(handler, body):
    """Approve someone onto the roster, or turn the request down."""
    need_admin(handler)
    email = norm_email(body.get("email"))
    decision = body.get("decision")
    if decision not in ("approve", "deny"):
        raise Res(400, {"error": "Decision must be approve or deny."})

    pending, psha = get_json(REQUESTS, {"requests": []})
    rows = pending.get("requests", [])
    row = next((r for r in rows if norm_email(r.get("email")) == email
                and r.get("status") == "pending"), None)
    if not row:
        raise Res(404, {"error": "No pending request for that address."})
    row["status"] = "approved" if decision == "approve" else "denied"
    row["decided"] = time.strftime("%Y-%m-%d")

    if decision == "approve":
        data, rsha = get_json(ROSTER, {"contributors": []})
        years = [str(y).strip() for y in (body.get("years") or []) if str(y).strip()]
        data.setdefault("contributors", []).append({
            "email": email,
            "name": str(body.get("name") or row.get("name") or email)[:120],
            "role": str(body.get("role") or row.get("served") or "")[:120],
            "years": years, "admin": False, "status": "approved",
            "added": time.strftime("%Y-%m-%d")})
        put_file(ROSTER, json.dumps(data, indent=1, ensure_ascii=False) + "\n", rsha,
                 f"{data['contributors'][-1]['name']} can edit "
                 f"{', '.join(years) or 'nothing yet'}")
        try:
            send_mail(email, "You can now edit the SGA 60 archive",
                      f"Your request to contribute to the SGA 60 archive has been "
                      f"approved.\n\nGo to {SITE_URL}/contribute.html, enter this "
                      f"address, and a sign-in link will come back to you.\n\n"
                      f"You can edit: {', '.join(years) or 'nothing yet, ask the editor'}\n")
        except Exception:
            pass

    pending["requests"] = rows
    put_file(REQUESTS, json.dumps(pending, indent=1) + "\n", psha,
             f"Access request from {email} {row['status']}")
    return {"ok": True}


def r_admin_history(handler, query):
    """Every commit a contributor made, newest first."""
    need_admin(handler)
    st, commits = gh("GET", f"/repos/{REPO}/commits?sha={BRANCH}&per_page=60")
    if st != 200 or not isinstance(commits, list):
        raise Res(502, {"error": "Could not read the history."})
    out = []
    for c in commits:
        msg = ((c.get("commit") or {}).get("message") or "")
        if "Contributed-By:" not in msg:
            continue
        who = ""
        for line in msg.splitlines():
            if line.startswith("Contributed-By:"):
                who = line.split(":", 1)[1].strip()
        out.append({"sha": c.get("sha", ""),
                    "summary": msg.splitlines()[0],
                    "by": who,
                    "when": ((c.get("commit") or {}).get("author") or {}).get("date", "")})
    return {"commits": out}


def r_admin_revert(handler, body):
    """Put every file this commit touched back the way its parent had it."""
    who = need_admin(handler)
    sha = str(body.get("sha", ""))
    if not re.fullmatch(r"[0-9a-f]{7,40}", sha):
        raise Res(400, {"error": "That is not a commit id."})
    st, commit = gh("GET", f"/repos/{REPO}/commits/{sha}")
    if st != 200:
        raise Res(404, {"error": "No such commit."})
    parents = commit.get("parents") or []
    if not parents:
        raise Res(400, {"error": "That commit has no parent to go back to."})
    parent = parents[0]["sha"]

    undone = []
    for f in commit.get("files") or []:
        path = f.get("filename", "")
        if not path.startswith("data/"):
            continue
        was, _ = get_file(path, ref=parent)
        _, now_sha = get_file(path)
        if was is None:
            continue
        ok, _ = put_file(path, was, now_sha,
                         commit_message(who, f"Undo {sha[:7]}: {path} back as it was"),
                         author={"name": who.get("name") or "SGA 60",
                                 "email": who["email"]})
        if ok:
            undone.append(path)
    if not undone:
        raise Res(400, {"error": "Nothing in that commit could be put back."})
    return {"ok": True, "reverted": undone}


ROUTES = {
    ("POST", "/api/auth/request"): lambda h, b, q: r_auth_request(h, b),
    ("GET", "/api/auth/callback"): lambda h, b, q: r_auth_callback(h, q),
    ("GET", "/api/auth/logout"): lambda h, b, q: r_auth_logout(h),
    ("GET", "/api/me"): lambda h, b, q: r_me(h),
    ("GET", "/api/year"): lambda h, b, q: r_year_get(h, q),
    ("POST", "/api/year"): lambda h, b, q: r_year_put(h, b),
    ("POST", "/api/post"): lambda h, b, q: r_post_put(h, b),
    ("GET", "/api/admin/queue"): lambda h, b, q: r_admin_queue(h),
    ("POST", "/api/admin/decide"): lambda h, b, q: r_admin_decide(h, b),
    ("GET", "/api/admin/history"): lambda h, b, q: r_admin_history(h, q),
    ("POST", "/api/admin/revert"): lambda h, b, q: r_admin_revert(h, b),
}


class handler(BaseHTTPRequestHandler):
    def _go(self, method):
        parsed = urllib.parse.urlparse(self.path)
        route = ROUTES.get((method, parsed.path.rstrip("/") or "/"))
        try:
            if not SECRET or not TOKEN:
                raise Res(503, {"error": "The contributor system is not configured "
                                         "yet. The editor needs to set its keys."})
            if not route:
                raise Res(404, {"error": "No such endpoint."})
            body = {}
            if method == "POST":
                n = int(self.headers.get("Content-Length") or 0)
                if n > 4_000_000:
                    raise Res(413, {"error": "That is too big to save."})
                raw = self.rfile.read(n) if n else b"{}"
                try:
                    body = json.loads(raw or b"{}")
                except json.JSONDecodeError:
                    raise Res(400, {"error": "The browser sent something unreadable."})
            self._send(200, route(self, body, urllib.parse.parse_qs(parsed.query)))
        except Res as r:
            self._send(r.status, r.payload, r.headers)
        except Exception as e:  # never leak a stack trace to the page
            self._send(500, {"error": "Something went wrong saving that.",
                             "detail": str(e)[:200]})

    def _send(self, status, payload, headers=()):
        self.send_response(status)
        for k, v in headers:
            self.send_header(k, v)
        if payload is None:
            self.end_headers()
            return
        raw = json.dumps(payload).encode()
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self):
        self._go("GET")

    def do_POST(self):
        self._go("POST")

    def log_message(self, *a):
        pass
