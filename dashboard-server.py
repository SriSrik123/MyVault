#!/usr/bin/env python3
"""
Sri's Personal Dashboard Server
Run: python3 dashboard-server.py
Open: http://localhost:8765
"""

import http.server, json, re, os, urllib.request, urllib.parse, webbrowser, secrets, ssl, certifi
from datetime import datetime, timezone

# macOS Python doesn't use the system cert store — use certifi
SSL_CTX = ssl.create_default_context(cafile=certifi.where())

BROWSER_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

def urlopen(req, timeout=10):
    return urllib.request.urlopen(req, timeout=timeout, context=SSL_CTX)

def whoop_request(url, *, data=None, token=None):
    """Make a WHOOP API request with browser-like headers to pass Cloudflare."""
    headers = {
        "User-Agent": BROWSER_UA,
        "Accept": "application/json, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": "https://app.whoop.com",
        "Referer": "https://app.whoop.com/",
    }
    if data is not None:
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, data=data, headers=headers)
    return urlopen(req, timeout=10)

VAULT = os.path.expanduser("~/Documents/MyVault")
TODO  = os.path.join(VAULT, "second-brain/notes/TODO.md")
HTML  = os.path.join(VAULT, "personal-dashboard.html")
PORT  = 8765

# ── WHOOP ──────────────────────────────────────────────────────────────────────
WHOOP_TOKEN_FILE = os.path.join(
    VAULT, ".obsidian/plugins/obsidian-whoop-plugin/data.json"
)
WHOOP_TOKEN_URL  = "https://api.prod.whoop.com/oauth/oauth2/token"
WHOOP_API        = "https://api.prod.whoop.com/developer/v2"
WHOOP_CLIENT_ID     = "1637e4a7-5b98-479d-bc74-85d711110b86"
WHOOP_CLIENT_SECRET = "f8a24cacf97b339cd7160d7a8c3e7a1772105b976f9539df17b294cf6a1d099e"

# ── STRAVA ─────────────────────────────────────────────────────────────────────
STRAVA_CLIENT_ID     = "235717"
STRAVA_CLIENT_SECRET = "3e471ccdc5945ca837b71d79bdbe712fdb19fd79"
STRAVA_TOKEN_FILE    = os.path.join(VAULT, ".strava-tokens.json")
STRAVA_TOKEN_URL     = "https://www.strava.com/oauth/token"
STRAVA_API           = "https://www.strava.com/api/v3"
STRAVA_AUTH_URL      = (
    "https://www.strava.com/oauth/authorize"
    f"?client_id={STRAVA_CLIENT_ID}"
    "&response_type=code"
    "&redirect_uri=http://localhost:8765/auth/strava/callback"
    "&approval_prompt=force"
    "&scope=activity:read_all"
)

# ── WHOOP OAuth ────────────────────────────────────────────────────────────────
def whoop_auth_url():
    state = secrets.token_urlsafe(16)
    return (
        "https://api.prod.whoop.com/oauth/oauth2/auth"
        f"?client_id={WHOOP_CLIENT_ID}"
        "&response_type=code"
        "&redirect_uri=http://localhost:8765/auth/whoop/callback"
        "&scope=offline%20read:workout%20read:recovery%20read:sleep%20read:cycles"
        f"&state={state}"
    )


# ── TASK PARSER ────────────────────────────────────────────────────────────────

COURSE_MAP = {
    "PHYS": "phys", "CS-265": "cs265", "CS-270": "cs270",
    "SE-201": "se", "COM-270": "com", "MATH-201": "math",
    "SE-": "se", "CS-": "cs265",
}

def infer_tag(title):
    for k, v in COURSE_MAP.items():
        if k.upper() in title.upper():
            return v
    return "other"

def parse_due(line):
    m = re.search(r'due \*\*([^*]+)\*\*', line)
    if m: return m.group(1).strip()
    m = re.search(r'·\s*(\*\*[^*]+\*\*|\w+ \w+ \d+)', line)
    if m: return m.group(1).replace('*','').strip()
    return None

def parse_todo():
    if not os.path.exists(TODO):
        return {"active": [], "done": []}

    with open(TODO, encoding="utf-8") as f:
        content = f.read()

    active, done = [], []
    current_section = ""

    for line in content.splitlines():
        if line.startswith("## "):
            current_section = line[3:].strip()

        m = re.match(r'\s*- \[([ x])\] \*\*(.*?)\*\*(.*)', line)
        if not m:
            continue

        checked = m.group(1) == "x"
        title   = m.group(2).strip()
        rest    = m.group(3)
        due     = parse_due(rest) or parse_due(line)
        tag     = infer_tag(title)

        task = {"title": title, "due": due, "tag": tag, "section": current_section}

        if checked or "Done" in current_section or "Archive" in current_section:
            done.append(task)
        else:
            active.append(task)

    return {"active": active, "done": done, "updated": datetime.now().isoformat()}


# ── WHOOP HELPERS ──────────────────────────────────────────────────────────────

def whoop_token():
    if not os.path.exists(WHOOP_TOKEN_FILE):
        return None
    with open(WHOOP_TOKEN_FILE) as f:
        d = json.load(f)
    tokens = d.get("tokens", {})

    data = urllib.parse.urlencode({
        "grant_type":    "refresh_token",
        "refresh_token": tokens["refresh_token"],
        "client_id":     WHOOP_CLIENT_ID,
        "client_secret": WHOOP_CLIENT_SECRET,
        "scope":         "offline read:workout read:recovery read:sleep read:cycles",
    }).encode()
    try:
        with whoop_request(WHOOP_TOKEN_URL, data=data) as r:
            new = json.loads(r.read())
        tokens.update(new)
        d["tokens"] = tokens
        with open(WHOOP_TOKEN_FILE, "w") as f:
            json.dump(d, f, indent=2)
        return new["access_token"]
    except Exception as e:
        print(f"WHOOP token refresh failed: {e}")
        return tokens.get("access_token")


def whoop_workouts(token, limit=15):
    url = f"{WHOOP_API}/activity/workout?limit={limit}"
    try:
        with whoop_request(url, token=token) as r:
            data = json.loads(r.read())
        results = []
        for w in data.get("records", []):
            sn = w.get("sport_name", "")
            if sn not in ("running", "cycling"):
                continue
            s = w.get("score", {})
            start = datetime.fromisoformat(w["start"].replace("Z", "+00:00"))
            end   = datetime.fromisoformat(w["end"].replace("Z", "+00:00"))
            dur   = int((end - start).total_seconds() // 60)
            results.append({
                "date":     w["start"][:10],
                "sport":    sn,
                "duration": dur,
                "strain":   round(s.get("strain", 0), 1),
                "avg_hr":   s.get("average_heart_rate", 0),
                "max_hr":   s.get("max_heart_rate", 0),
                "kj":       round(s.get("kilojoule", 0)),
                "source":   "whoop",
            })
        return results
    except Exception as e:
        print(f"WHOOP workout fetch failed: {e}")
        return []


def whoop_recovery(token):
    url = f"{WHOOP_API}/recovery?limit=7"
    try:
        with whoop_request(url, token=token) as r:
            data = json.loads(r.read())
        return [
            {
                "score": round(r["score"]["recovery_score"]),
                "hrv":   round(r["score"]["hrv_rmssd_milli"], 1),
                "rhr":   round(r["score"]["resting_heart_rate"]),
                "spo2":  round(r["score"]["spo2_percentage"], 1),
            }
            for r in data.get("records", [])
        ]
    except Exception as e:
        print(f"WHOOP recovery fetch failed: {e}")
        return []


# ── STRAVA HELPERS ─────────────────────────────────────────────────────────────

def strava_load_tokens():
    if not os.path.exists(STRAVA_TOKEN_FILE):
        return None
    with open(STRAVA_TOKEN_FILE) as f:
        return json.load(f)

def strava_save_tokens(d):
    with open(STRAVA_TOKEN_FILE, "w") as f:
        json.dump(d, f, indent=2)

def strava_has_activity_scope(d):
    return "activity:read" in d.get("scope", "")

def strava_refresh(d):
    data = (
        f"client_id={STRAVA_CLIENT_ID}"
        f"&client_secret={STRAVA_CLIENT_SECRET}"
        f"&refresh_token={d['refresh_token']}"
        f"&grant_type=refresh_token"
    ).encode()
    req = urllib.request.Request(STRAVA_TOKEN_URL, data=data,
                                 headers={"Content-Type": "application/x-www-form-urlencoded"})
    try:
        with urlopen(req, timeout=8) as r:
            new = json.loads(r.read())
        d.update(new)
        strava_save_tokens(d)
        return d
    except Exception as e:
        print(f"Strava token refresh failed: {e}")
        return None

def strava_token():
    """Returns (access_token, needs_auth). needs_auth=True means visit /auth/strava."""
    d = strava_load_tokens()
    if not d:
        return None, True
    if not strava_has_activity_scope(d):
        return None, True   # tokens exist but wrong scope — need re-auth
    d2 = strava_refresh(d)
    if not d2:
        return d.get("access_token"), False  # stale token as fallback
    return d2["access_token"], False

def strava_exchange_code(code):
    data = (
        f"client_id={STRAVA_CLIENT_ID}"
        f"&client_secret={STRAVA_CLIENT_SECRET}"
        f"&code={code}"
        f"&grant_type=authorization_code"
    ).encode()
    req = urllib.request.Request(STRAVA_TOKEN_URL, data=data,
                                 headers={"Content-Type": "application/x-www-form-urlencoded"})
    with urlopen(req, timeout=8) as r:
        tokens = json.loads(r.read())
    strava_save_tokens(tokens)
    return tokens

def strava_activities(token, limit=20):
    url = f"{STRAVA_API}/athlete/activities?per_page={limit}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    try:
        with urlopen(req, timeout=10) as r:
            acts = json.loads(r.read())
        results = []
        for a in acts:
            t = a.get("type", "")
            if t not in ("Run", "Ride"):
                continue
            dist_m   = a.get("distance", 0)
            dist_mi  = round(dist_m / 1609.34, 2)
            move_s   = a.get("moving_time", 0)
            move_min = move_s / 60
            if t == "Run" and dist_mi > 0:
                ppm  = move_min / dist_mi
                pace = f"{int(ppm)}:{int((ppm % 1) * 60):02d}/mi"
            elif t == "Ride" and move_s > 0:
                mph  = dist_mi / (move_s / 3600)
                pace = f"{mph:.1f} mph"
            else:
                pace = ""
            results.append({
                "date":         a["start_date_local"][:10],
                "sport":        "running" if t == "Run" else "cycling",
                "name":         a.get("name", t),
                "distance_mi":  dist_mi,
                "duration":     int(move_min),
                "pace":         pace,
                "avg_hr":       round(a.get("average_heartrate") or 0),
                "max_hr":       round(a.get("max_heartrate") or 0),
                "elevation_ft": round((a.get("total_elevation_gain") or 0) * 3.281),
                "source":       "strava",
            })
        return results
    except Exception as e:
        print(f"Strava activities fetch failed: {e}")
        return []


# ── HTTP HANDLER ───────────────────────────────────────────────────────────────

class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass

    def send_json(self, obj, status=200):
        body = json.dumps(obj).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)

    def send_html(self, html, status=200):
        body = html.encode()
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)

    def send_file(self, path, ctype="text/html"):
        with open(path, "rb") as f:
            body = f.read()
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)

    def redirect(self, url):
        self.send_response(302)
        self.send_header("Location", url)
        self.end_headers()

    def do_GET(self):
        p = self.path.split("?")[0]

        if p == "/" or p == "/index.html":
            self.send_file(HTML)

        elif p == "/api/tasks":
            self.send_json(parse_todo())

        elif p == "/api/workouts":
            token = whoop_token()
            if token:
                workouts = whoop_workouts(token)
                recovery = whoop_recovery(token)
                self.send_json({"workouts": workouts, "recovery": recovery})
            else:
                self.send_json({"workouts": [], "recovery": [], "error": "No WHOOP token"})

        elif p == "/api/strava":
            token, needs_auth = strava_token()
            if needs_auth:
                self.send_json({"activities": [], "needs_auth": True, "auth_url": "/auth/strava"})
            else:
                activities = strava_activities(token) if token else []
                self.send_json({"activities": activities, "needs_auth": False})

        elif p == "/auth/strava":
            self.redirect(STRAVA_AUTH_URL)

        elif p == "/auth/strava/callback":
            qs = {}
            if "?" in self.path:
                for pair in self.path.split("?", 1)[1].split("&"):
                    if "=" in pair:
                        k, v = pair.split("=", 1)
                        qs[k] = urllib.parse.unquote(v)

            if "error" in qs:
                self.send_html(f"<h2>Strava auth cancelled: {qs.get('error')}</h2>")
                return

            try:
                tokens  = strava_exchange_code(qs.get("code", ""))
                scope   = tokens.get("scope", "")
                athlete = tokens.get("athlete", {})
                name    = f"{athlete.get('firstname','')} {athlete.get('lastname','')}".strip()
                self.send_html(f"""<!DOCTYPE html>
<html><body style="font-family:sans-serif;padding:40px;background:#09090f;color:#e4e6f0;text-align:center">
<h1 style="color:#34d399">&#10003; Strava Connected!</h1>
<p>Logged in as <strong>{name or 'athlete'}</strong></p>
<p style="color:#8b90a8;font-size:13px">Scope: {scope}</p>
<p style="color:#8b90a8">You can close this tab. Activities will appear in the dashboard within 30 seconds.</p>
<script>setTimeout(()=>window.close(),3000)</script>
</body></html>""")
                print(f"✅  Strava connected — {name}, scope: {scope}")
            except Exception as e:
                self.send_html(f"<h2 style='color:#f87171'>Error: {e}</h2>")

        elif p == "/auth/whoop":
            self.redirect(whoop_auth_url())

        elif p == "/auth/whoop/callback":
            # Use proper query string parsing
            qs = urllib.parse.parse_qs(self.path.split("?", 1)[1] if "?" in self.path else "")
            # parse_qs returns lists — flatten
            qs = {k: v[0] for k, v in qs.items()}

            if "error" in qs:
                self.send_html(f"<h2>WHOOP auth error: {qs.get('error')}<br><small>{qs.get('error_description','')}</small></h2>")
                return

            try:
                code = qs.get("code", "")
                # Use urlencode so all values are properly encoded in the POST body
                post_data = urllib.parse.urlencode({
                    "grant_type":    "authorization_code",
                    "code":          code,
                    "client_id":     WHOOP_CLIENT_ID,
                    "client_secret": WHOOP_CLIENT_SECRET,
                    "redirect_uri":  "http://localhost:8765/auth/whoop/callback",
                }).encode()
                with whoop_request(WHOOP_TOKEN_URL, data=post_data) as r:
                    tokens = json.loads(r.read())

                # Save fresh tokens to the plugin file
                if os.path.exists(WHOOP_TOKEN_FILE):
                    with open(WHOOP_TOKEN_FILE) as f:
                        d = json.load(f)
                else:
                    d = {}
                d["tokens"] = tokens
                with open(WHOOP_TOKEN_FILE, "w") as f:
                    json.dump(d, f, indent=2)

                self.send_html("""<!DOCTYPE html>
<html><body style="font-family:sans-serif;padding:40px;background:#09090f;color:#e4e6f0;text-align:center">
<h1 style="color:#34d399">&#10003; WHOOP Connected!</h1>
<p style="color:#8b90a8">Fresh tokens saved. You can close this tab.</p>
<script>setTimeout(()=>window.close(),3000)</script>
</body></html>""")
                print("✅  WHOOP re-authenticated successfully")
            except urllib.error.HTTPError as e:
                body = e.read().decode()
                self.send_html(f"<h2 style='color:#f87171'>HTTP {e.code}: {e.reason}</h2><pre>{body}</pre>")
                print(f"WHOOP auth HTTP error {e.code}: {body}")
            except Exception as e:
                self.send_html(f"<h2 style='color:#f87171'>Error: {e}</h2>")
                print(f"WHOOP auth error: {e}")

        elif p == "/api/refresh":
            wt = whoop_token()
            tasks    = parse_todo()
            workouts = whoop_workouts(wt) if wt else []
            recovery = whoop_recovery(wt) if wt else []
            st, needs_auth = strava_token()
            strava   = strava_activities(st) if (st and not needs_auth) else []
            self.send_json({
                "tasks":    tasks,
                "workouts": workouts,
                "recovery": recovery,
                "strava":   {"activities": strava, "needs_auth": needs_auth},
            })

        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.end_headers()


if __name__ == "__main__":
    server = http.server.HTTPServer(("localhost", PORT), Handler)
    url = f"http://localhost:{PORT}"
    print(f"\n✅  Dashboard running at {url}")
    print(f"    Tasks: {TODO}")
    d = strava_load_tokens()
    if not d or not strava_has_activity_scope(d):
        print(f"\n⚡  Strava needs one-time authorization.")
        print(f"    → Open this in your browser: {url}/auth/strava\n")
    else:
        print(f"    Strava: connected ✓")
    print(f"    Press Ctrl+C to stop.\n")
    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
