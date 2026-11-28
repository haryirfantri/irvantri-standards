#!/usr/bin/env python3
"""Mint the OAuth 2.0 refresh token that lets GitHub Actions publish to Google Drive.

Run this once on your own computer (it opens a browser), signed in as the
Google account that owns the Standards Design folder. Standard library only.

    python3 tools/drive_oauth_token.py --client-id XXX.apps.googleusercontent.com --client-secret YYY

Prerequisites (Google Cloud Console, once):
  1. Create a project and enable the Google Drive API.
  2. OAuth consent screen: External, add your account as a test user, then press
     "Publish app" so the status is "In production". Tokens of apps left in
     "Testing" expire after 7 days.
  3. Credentials -> Create credentials -> OAuth client ID -> Desktop app.

Then store three repository secrets (Settings -> Secrets and variables -> Actions):
  GDRIVE_OAUTH_CLIENT_ID, GDRIVE_OAUTH_CLIENT_SECRET, GDRIVE_OAUTH_REFRESH_TOKEN

The refresh token grants full Drive access to your account. Keep it only in
GitHub Secrets; never commit it or paste it into chat.
"""
from __future__ import annotations

import argparse
import hashlib
import base64
import http.server
import json
import secrets
import threading
import urllib.parse
import urllib.request
import webbrowser

AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"
SCOPE = "https://www.googleapis.com/auth/drive"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--client-id", required=True)
    ap.add_argument("--client-secret", required=True)
    ap.add_argument("--port", type=int, default=8765, help="local loopback port for the redirect (default 8765)")
    args = ap.parse_args()

    redirect = f"http://127.0.0.1:{args.port}/"
    state = secrets.token_urlsafe(16)
    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b"=").decode()
    result: dict[str, str] = {}

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):  # noqa: N802
            q = dict(urllib.parse.parse_qsl(urllib.parse.urlparse(self.path).query))
            result.update(q)
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Done. You can close this tab and return to the terminal.")

        def log_message(self, *a):
            pass

    server = http.server.HTTPServer(("127.0.0.1", args.port), Handler)
    thread = threading.Thread(target=server.handle_request, daemon=True)
    thread.start()

    url = AUTH_URL + "?" + urllib.parse.urlencode({
        "client_id": args.client_id,
        "redirect_uri": redirect,
        "response_type": "code",
        "scope": SCOPE,
        "access_type": "offline",
        "prompt": "consent",
        "state": state,
        "code_challenge": challenge,
        "code_challenge_method": "S256",
    })
    print("Opening your browser. If it does not open, visit:\n\n" + url + "\n")
    webbrowser.open(url)
    thread.join(timeout=300)
    server.server_close()

    if result.get("state") != state or "code" not in result:
        raise SystemExit(f"Authorization failed: {result.get('error', 'no code received')}")

    body = urllib.parse.urlencode({
        "code": result["code"],
        "client_id": args.client_id,
        "client_secret": args.client_secret,
        "redirect_uri": redirect,
        "grant_type": "authorization_code",
        "code_verifier": verifier,
    }).encode()
    with urllib.request.urlopen(urllib.request.Request(TOKEN_URL, data=body, method="POST")) as resp:
        data = json.loads(resp.read())
    if "refresh_token" not in data:
        raise SystemExit("No refresh token returned. Revoke the app at https://myaccount.google.com/permissions and retry.")

    print("Store this value as the repository secret GDRIVE_OAUTH_REFRESH_TOKEN:\n")
    print(data["refresh_token"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
