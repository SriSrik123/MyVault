#!/usr/bin/env python3
"""
Polls WHOOP API until today's recovery score is available.
Writes data to $WHOOP_DATA_FILE and outputs the new refresh token
to $GITHUB_OUTPUT so the workflow can rotate the stored secret.

Usage: python3 fetch_whoop.py
  Env: WHOOP_REFRESH_TOKEN  — current refresh token
       WHOOP_DATA_FILE       — where to write the JSON (default: /tmp/whoop_today.json)
       GITHUB_OUTPUT         — set automatically by GitHub Actions
"""

import json
import os
import ssl
import sys
import time
import urllib.parse
import urllib.request
from datetime import date, datetime

import certifi

SSL_CTX   = ssl.create_default_context(cafile=certifi.where())
TOKEN_URL = "https://api.prod.whoop.com/oauth/oauth2/token"
API       = "https://api.prod.whoop.com/developer/v2"
CLIENT_ID     = "1637e4a7-5b98-479d-bc74-85d711110b86"
CLIENT_SECRET = "f8a24cacf97b339cd7160d7a8c3e7a1772105b976f9539df17b294cf6a1d099e"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"


def token_refresh(refresh_tok: str) -> dict:
    body = urllib.parse.urlencode({
        "grant_type":    "refresh_token",
        "refresh_token": refresh_tok,
        "client_id":     CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope":         "offline read:workout read:recovery read:sleep read:cycles",
    }).encode()
    req = urllib.request.Request(TOKEN_URL, data=body, headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent":   UA,
    })
    with urllib.request.urlopen(req, timeout=15, context=SSL_CTX) as r:
        return json.loads(r.read())


def api_get(path: str, access_token: str) -> dict:
    req = urllib.request.Request(f"{API}{path}", headers={
        "Authorization": f"Bearer {access_token}",
        "User-Agent":    UA,
        "Accept":        "application/json",
    })
    with urllib.request.urlopen(req, timeout=15, context=SSL_CTX) as r:
        return json.loads(r.read())


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def main() -> None:
    refresh_tok = os.environ.get("WHOOP_REFRESH_TOKEN", "").strip()
    if not refresh_tok:
        log("ERROR: WHOOP_REFRESH_TOKEN env var not set")
        sys.exit(1)

    output_file   = os.environ.get("WHOOP_DATA_FILE", "/tmp/whoop_today.json")
    github_output = os.environ.get("GITHUB_OUTPUT", "")
    today         = date.today().isoformat()
    max_attempts  = 36  # 5 min × 36 = 3 hours

    for attempt in range(max_attempts):
        try:
            tokens      = token_refresh(refresh_tok)
            access_tok  = tokens["access_token"]
            refresh_tok = tokens.get("refresh_token", refresh_tok)

            rec_resp = api_get("/recovery?limit=1", access_tok)
            records  = rec_resp.get("records", [])

            if records:
                rec            = records[0]
                created        = rec.get("created_at", "")[:10]
                recovery_score = rec.get("score", {}).get("recovery_score")

                if created >= today and recovery_score is not None:
                    sleep_resp = api_get("/activity/sleep?limit=1", access_tok)
                    sleep_rec  = (sleep_resp.get("records") or [{}])[0]

                    with open(output_file, "w") as f:
                        json.dump({
                            "recovery":   rec,
                            "sleep":      sleep_rec,
                            "fetched_at": datetime.utcnow().isoformat() + "Z",
                        }, f, indent=2)

                    log(f"Recovery ready: {recovery_score}% — data written to {output_file}")

                    # Write new refresh token to GitHub Actions output
                    if github_output:
                        with open(github_output, "a") as f:
                            f.write(f"new_refresh_token={refresh_tok}\n")
                            f.write(f"data_file={output_file}\n")

                    sys.exit(0)

        except Exception as e:
            log(f"Attempt {attempt + 1}: {e}")

        if attempt < max_attempts - 1:
            log(f"Recovery not ready yet (attempt {attempt + 1}/{max_attempts}), waiting 5 min…")
            time.sleep(300)

    log("ERROR: WHOOP recovery data not available after 3 hours")
    sys.exit(1)


if __name__ == "__main__":
    main()
