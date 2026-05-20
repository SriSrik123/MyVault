#!/usr/bin/env python3
"""
One-time Whoop OAuth setup.
Run this once from your terminal: python3 whoop_auth.py
It will open your browser, you authorize, and tokens are saved to ~/.whoop_config.json
"""

import http.server
import urllib.parse
import webbrowser
import requests
import json
import os
import secrets
from pathlib import Path

CLIENT_ID     = "1637e4a7-5b98-479d-bc74-85d711110b86"
CLIENT_SECRET = "f8a24cacf97b339cd7160d7a8c3e7a1772105b976f9539df17b294cf6a1d099e"
REDIRECT_URI  = "http://localhost:8080/callback"
AUTH_URL      = "https://api.prod.whoop.com/oauth/oauth2/auth"
TOKEN_URL     = "https://api.prod.whoop.com/oauth/oauth2/token"
SCRIPT_DIR    = Path(__file__).resolve().parent
CONFIG_FILE   = SCRIPT_DIR / ".whoop_tokens.json"

SCOPES = "offline read:recovery read:sleep read:workout read:body_measurement read:cycles"

STATE = secrets.token_hex(16)  # random 32-char state for CSRF protection
auth_code = None

class CallbackHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        if "code" in params:
            auth_code = params["code"][0]
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h2 style='font-family:sans-serif;margin:40px'>Whoop authorized! You can close this tab.</h2>")
        else:
            self.send_response(400)
            self.end_headers()

    def log_message(self, format, *args):
        pass  # suppress server logs


# Build authorization URL manually — keep colons unencoded in scope, use %20 for spaces
scope_param    = SCOPES.replace(" ", "%20")
redirect_param = urllib.parse.quote(REDIRECT_URI, safe="")
full_url = (
    f"{AUTH_URL}"
    f"?client_id={CLIENT_ID}"
    f"&redirect_uri={redirect_param}"
    f"&response_type=code"
    f"&scope={scope_param}"
    f"&state={STATE}"
)

print("\n=== Whoop Auth Setup ===")
print("Opening browser for authorization...")
print(f"\nIf browser doesn't open, paste this URL manually:\n{full_url}\n")
webbrowser.open(full_url)

# Wait for callback
print("Waiting for authorization (timeout: 120s)...")
server = http.server.HTTPServer(("localhost", 8080), CallbackHandler)
server.timeout = 120
server.handle_request()

if not auth_code:
    print("\nNo authorization code received. Try again.")
    exit(1)

print("Authorization code received. Exchanging for tokens...")

# Exchange code for tokens
resp = requests.post(TOKEN_URL, data={
    "grant_type":    "authorization_code",
    "code":          auth_code,
    "client_id":     CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "redirect_uri":  REDIRECT_URI,
})

if not resp.ok:
    print(f"Token exchange failed: {resp.status_code} {resp.text}")
    exit(1)

tokens = resp.json()
tokens["client_id"]     = CLIENT_ID
tokens["client_secret"] = CLIENT_SECRET

with open(CONFIG_FILE, "w") as f:
    json.dump(tokens, f, indent=2)
os.chmod(CONFIG_FILE, 0o600)

print(f"\nTokens saved to {CONFIG_FILE}")
print("Setup complete! The daily sync will run automatically each morning.")
