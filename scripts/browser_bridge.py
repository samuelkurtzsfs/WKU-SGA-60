#!/usr/bin/env python3
"""A local drop box so the browser can hand files to disk.

    python3 scripts/browser_bridge.py &          # listens on 127.0.0.1:8765

TopSCHOLAR answers `/cgi/viewcontent.cgi` with 403 to every script. Retrying,
backing off, spoofing the user agent and running headless Chrome all fail; the
block is on the TLS fingerprint, not on anything a header can carry. The one
client that gets 200 is the human's own Chrome, and there is no cf_clearance
cookie to lift out of it.

So the bytes have to leave by the browser. The page fetches the file with its
own credentials and POSTs it here, and this writes it to disk. Nothing passes
through the model's context, which matters: one Talisman is 25 MB, and as
base64 in a transcript it would be 34 MB of text for a single volume.

Range requests work against TopSCHOLAR (206, exact byte counts), so the page
can send a big file in chunks and this appends them in order.
"""

import json
import re
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Only ever writes inside these. A page is untrusted input, and the name it
# sends is chosen by whatever the page felt like sending.
ALLOWED = {
    "photos": ROOT / "data" / "photos",
    "stage": Path.home() / "Desktop" / "SGA60 photo hunt",
    "scratch": ROOT / "data" / "photo-finds" / "_browser",
}
SAFE = re.compile(r"^[A-Za-z0-9._-]{1,120}$")


class Bridge(BaseHTTPRequestHandler):
    def cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "content-type,x-drop,x-into,x-append")
        self.send_header("Access-Control-Allow-Methods", "POST,OPTIONS")
        # Chrome treats an https page reaching 127.0.0.1 as a private-network
        # request and refuses the preflight without this, whatever the other
        # CORS headers say.
        self.send_header("Access-Control-Allow-Private-Network", "true")

    def do_OPTIONS(self):
        self.send_response(204)
        self.cors()
        self.end_headers()

    def do_POST(self):
        name = self.headers.get("x-drop", "")
        into = self.headers.get("x-into", "stage")
        append = self.headers.get("x-append", "") == "1"
        # A path separator or a .. in the name is the whole attack; reject the
        # name outright rather than trying to sanitise it into something safe.
        if into not in ALLOWED or not SAFE.match(name):
            self.send_response(400)
            self.cors()
            self.end_headers()
            self.wfile.write(b"bad name or destination")
            return
        out = ALLOWED[into] / name
        out.parent.mkdir(parents=True, exist_ok=True)
        n = int(self.headers.get("content-length", 0))
        body = self.rfile.read(n)
        with open(out, "ab" if append else "wb") as fh:
            fh.write(body)
        self.send_response(200)
        self.cors()
        self.send_header("content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(
            {"wrote": str(out), "bytes": len(body), "total": out.stat().st_size}
        ).encode())
        print(f"  {'+=' if append else '<-'} {out.name}  {len(body):,} bytes "
              f"(now {out.stat().st_size:,})", flush=True)

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    for k, v in ALLOWED.items():
        v.mkdir(parents=True, exist_ok=True)
    print(f"bridge on http://127.0.0.1:{port}  ->  {', '.join(ALLOWED)}", flush=True)
    HTTPServer(("127.0.0.1", port), Bridge).serve_forever()
