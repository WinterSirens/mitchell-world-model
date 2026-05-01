#!/usr/bin/env python3
"""
LinkedIn OAuth helper.

Walks through the OAuth 2.0 authorization-code flow, captures the access token
and refresh token, fetches the author URN, and writes everything to .env.

Run once after creating your LinkedIn Developer App. Run again to refresh the
token when it expires (LinkedIn access tokens last ~60 days).

Usage:
    python3 auth.py            # full OAuth flow (first time)
    python3 auth.py --refresh  # use refresh token to get new access token
"""

import http.server
import json
import os
import secrets
import socketserver
import sys
import threading
import urllib.parse
import urllib.request
import webbrowser
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
ENV_PATH = SCRIPT_DIR / ".env"

AUTH_URL = "https://www.linkedin.com/oauth/v2/authorization"
TOKEN_URL = "https://www.linkedin.com/oauth/v2/accessToken"
USERINFO_URL = "https://api.linkedin.com/v2/userinfo"
SCOPES = "openid profile w_member_social"


def load_env() -> dict:
    if not ENV_PATH.exists():
        sys.exit(f"Missing {ENV_PATH}. Copy .env.example to .env and fill in client credentials.")
    env = {}
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()
    return env


def write_env(env: dict) -> None:
    lines = ["# LinkedIn API credentials — gitignored\n"]
    for key in [
        "LINKEDIN_CLIENT_ID",
        "LINKEDIN_CLIENT_SECRET",
        "LINKEDIN_REDIRECT_URI",
        "LINKEDIN_ACCESS_TOKEN",
        "LINKEDIN_REFRESH_TOKEN",
        "LINKEDIN_TOKEN_EXPIRES_AT",
        "LINKEDIN_AUTHOR_URN",
    ]:
        lines.append(f"{key}={env.get(key, '')}\n")
    ENV_PATH.write_text("".join(lines))
    os.chmod(ENV_PATH, 0o600)


def post_form(url: str, data: dict) -> dict:
    body = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def get_userinfo(access_token: str) -> dict:
    req = urllib.request.Request(USERINFO_URL)
    req.add_header("Authorization", f"Bearer {access_token}")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def run_oauth_flow(env: dict) -> dict:
    client_id = env.get("LINKEDIN_CLIENT_ID")
    client_secret = env.get("LINKEDIN_CLIENT_SECRET")
    redirect_uri = env.get("LINKEDIN_REDIRECT_URI", "http://localhost:8000/callback")
    if not client_id or not client_secret:
        sys.exit("LINKEDIN_CLIENT_ID and LINKEDIN_CLIENT_SECRET must be set in .env first.")

    state = secrets.token_urlsafe(16)
    auth_params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": SCOPES,
        "state": state,
    }
    auth_link = f"{AUTH_URL}?{urllib.parse.urlencode(auth_params)}"

    parsed = urllib.parse.urlparse(redirect_uri)
    port = parsed.port or 8000
    received = {}

    class Handler(http.server.BaseHTTPRequestHandler):
        def log_message(self, *args, **kwargs):
            pass

        def do_GET(self):
            qs = urllib.parse.urlparse(self.path).query
            params = dict(urllib.parse.parse_qsl(qs))
            received.update(params)
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            msg = "Authorization received. You can close this tab and return to the terminal."
            if "error" in params:
                msg = f"Error: {params.get('error_description', params.get('error'))}"
            self.wfile.write(f"<html><body><h2>{msg}</h2></body></html>".encode())

    server = socketserver.TCPServer(("localhost", port), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    print(f"Opening browser for LinkedIn authorization...")
    print(f"If it doesn't open automatically, paste this URL:\n  {auth_link}\n")
    webbrowser.open(auth_link)

    while "code" not in received and "error" not in received:
        threading.Event().wait(0.5)
    server.shutdown()

    if "error" in received:
        sys.exit(f"Authorization failed: {received.get('error_description', received['error'])}")
    if received.get("state") != state:
        sys.exit("State mismatch — possible CSRF. Aborting.")

    print("Exchanging authorization code for access token...")
    token_resp = post_form(
        TOKEN_URL,
        {
            "grant_type": "authorization_code",
            "code": received["code"],
            "redirect_uri": redirect_uri,
            "client_id": client_id,
            "client_secret": client_secret,
        },
    )
    return token_resp


def run_refresh(env: dict) -> dict:
    refresh_token = env.get("LINKEDIN_REFRESH_TOKEN")
    if not refresh_token:
        sys.exit("No refresh token in .env. Run `python3 auth.py` for the full OAuth flow.")
    print("Refreshing access token...")
    return post_form(
        TOKEN_URL,
        {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": env["LINKEDIN_CLIENT_ID"],
            "client_secret": env["LINKEDIN_CLIENT_SECRET"],
        },
    )


def main() -> None:
    env = load_env()
    if "--refresh" in sys.argv:
        token_resp = run_refresh(env)
    else:
        token_resp = run_oauth_flow(env)

    access_token = token_resp["access_token"]
    expires_in = token_resp.get("expires_in", 0)
    import time
    expires_at = int(time.time()) + int(expires_in)

    env["LINKEDIN_ACCESS_TOKEN"] = access_token
    env["LINKEDIN_TOKEN_EXPIRES_AT"] = str(expires_at)
    if "refresh_token" in token_resp:
        env["LINKEDIN_REFRESH_TOKEN"] = token_resp["refresh_token"]

    print("Fetching author URN from /v2/userinfo...")
    userinfo = get_userinfo(access_token)
    sub = userinfo["sub"]
    env["LINKEDIN_AUTHOR_URN"] = f"urn:li:person:{sub}"

    write_env(env)
    print(f"\nDone. Access token saved to {ENV_PATH}")
    print(f"Author URN: {env['LINKEDIN_AUTHOR_URN']}")
    print(f"Token expires in: {expires_in} seconds (~{expires_in // 86400} days)")


if __name__ == "__main__":
    main()
