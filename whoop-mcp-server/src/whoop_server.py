#!/usr/bin/env python3
"""
WHOOP MCP Server — uses existing OAuth tokens from Obsidian plugin.
Calls WHOOP Developer API v2 directly (email/password auth is unsupported).
"""

import os, json, sys, urllib.request, urllib.parse, ssl, certifi
from datetime import datetime, timedelta
from pathlib import Path
from mcp.server.fastmcp import FastMCP

SSL_CTX = ssl.create_default_context(cafile=certifi.where())

BROWSER_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

def whoop_request(url, *, data=None, token=None):
    headers = {
        "User-Agent":      BROWSER_UA,
        "Accept":          "application/json, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Origin":          "https://app.whoop.com",
        "Referer":         "https://app.whoop.com/",
    }
    if data is not None:
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, data=data, headers=headers)
    return urllib.request.urlopen(req, timeout=10, context=SSL_CTX)

VAULT = os.path.expanduser("~/Documents/MyVault")
TOKEN_FILE = os.path.join(VAULT, ".obsidian/plugins/obsidian-whoop-plugin/data.json")
TOKEN_URL  = "https://api.prod.whoop.com/oauth/oauth2/token"
API        = "https://api.prod.whoop.com/developer/v2"
CLIENT_ID     = "1637e4a7-5b98-479d-bc74-85d711110b86"
CLIENT_SECRET = "f8a24cacf97b339cd7160d7a8c3e7a1772105b976f9539df17b294cf6a1d099e"

mcp = FastMCP("WHOOP MCP Server")


# ── Token management ───────────────────────────────────────────────────────────

def get_token() -> str | None:
    if not os.path.exists(TOKEN_FILE):
        return None
    with open(TOKEN_FILE) as f:
        d = json.load(f)
    tokens = d.get("tokens", {})
    post_data = urllib.parse.urlencode({
        "grant_type":    "refresh_token",
        "refresh_token": tokens["refresh_token"],
        "client_id":     CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope":         "offline read:workout read:recovery read:sleep read:cycles",
    }).encode()
    try:
        with whoop_request(TOKEN_URL, data=post_data) as r:
            new = json.loads(r.read())
        tokens.update(new)
        d["tokens"] = tokens
        with open(TOKEN_FILE, "w") as f:
            json.dump(d, f, indent=2)
        return new["access_token"]
    except Exception as e:
        return tokens.get("access_token")

def api_get(path: str) -> dict:
    token = get_token()
    if not token:
        return {"error": "No WHOOP token available"}
    url = f"{API}{path}"
    with whoop_request(url, token=token) as r:
        return json.loads(r.read())


# ── Tools ──────────────────────────────────────────────────────────────────────

@mcp.tool()
def check_auth_status() -> dict:
    """Check if authenticated with WHOOP API."""
    try:
        token = get_token()
        if token:
            return {"authenticated": True, "message": "Connected to WHOOP API v2"}
        return {"authenticated": False, "message": "No token found"}
    except Exception as e:
        return {"authenticated": False, "message": str(e)}


@mcp.tool()
def get_latest_recovery() -> dict:
    """Get the most recent WHOOP recovery score, HRV, RHR, and SpO2."""
    try:
        data = api_get("/recovery?limit=1")
        records = data.get("records", [])
        if not records:
            return {"error": "No recovery data found"}
        r = records[0]
        s = r.get("score", {})
        return {
            "date":           r.get("created_at", "")[:10],
            "recovery_score": round(s.get("recovery_score", 0)),
            "hrv_rmssd":      round(s.get("hrv_rmssd_milli", 0), 1),
            "resting_hr":     round(s.get("resting_heart_rate", 0)),
            "spo2":           round(s.get("spo2_percentage", 0), 1),
            "skin_temp_f":    round(s.get("skin_temp_fahrenheit", 0), 1),
        }
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_recoveries(days: int = 7) -> list:
    """Get WHOOP recovery data for the past N days (default 7)."""
    try:
        data = api_get(f"/recovery?limit={days}")
        return [
            {
                "date":           r.get("created_at", "")[:10],
                "recovery_score": round(r["score"].get("recovery_score", 0)),
                "hrv_rmssd":      round(r["score"].get("hrv_rmssd_milli", 0), 1),
                "resting_hr":     round(r["score"].get("resting_heart_rate", 0)),
                "spo2":           round(r["score"].get("spo2_percentage", 0), 1),
            }
            for r in data.get("records", [])
        ]
    except Exception as e:
        return [{"error": str(e)}]


@mcp.tool()
def get_latest_cycle() -> dict:
    """Get the most recent WHOOP cycle (strain + kilojoules)."""
    try:
        data = api_get("/cycle?limit=1")
        records = data.get("records", [])
        if not records:
            return {"error": "No cycle data"}
        c = records[0]
        s = c.get("score", {})
        return {
            "date":       c.get("start", "")[:10],
            "strain":     round(s.get("strain", 0), 1),
            "kilojoule":  round(s.get("kilojoule", 0)),
            "avg_hr":     s.get("average_heart_rate", 0),
            "max_hr":     s.get("max_heart_rate", 0),
        }
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_cycles(days: int = 7) -> list:
    """Get WHOOP cycle data for the past N days."""
    try:
        data = api_get(f"/cycle?limit={days}")
        return [
            {
                "date":      c.get("start", "")[:10],
                "strain":    round(c["score"].get("strain", 0), 1),
                "kilojoule": round(c["score"].get("kilojoule", 0)),
                "avg_hr":    c["score"].get("average_heart_rate", 0),
                "max_hr":    c["score"].get("max_heart_rate", 0),
            }
            for c in data.get("records", [])
        ]
    except Exception as e:
        return [{"error": str(e)}]


@mcp.tool()
def get_workouts(limit: int = 10) -> list:
    """Get recent WHOOP workouts (runs and cycling only)."""
    try:
        data = api_get(f"/activity/workout?limit={limit}")
        results = []
        for w in data.get("records", []):
            sn = w.get("sport_name", "")
            s  = w.get("score", {})
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
            })
        return results
    except Exception as e:
        return [{"error": str(e)}]


@mcp.tool()
def get_sleeps(limit: int = 7) -> list:
    """Get recent WHOOP sleep data."""
    try:
        data = api_get(f"/activity/sleep?limit={limit}")
        return [
            {
                "date":            s.get("start", "")[:10],
                "performance_pct": round(s["score"].get("sleep_performance_percentage", 0)),
                "hours":           round(s["score"].get("stage_summary", {}).get("total_in_bed_time_milli", 0) / 3600000, 1),
                "rem_pct":         round(s["score"].get("stage_summary", {}).get("total_rem_sleep_time_milli", 0) /
                                        max(s["score"].get("stage_summary", {}).get("total_in_bed_time_milli", 1), 1) * 100),
            }
            for s in data.get("records", [])
        ]
    except Exception as e:
        return [{"error": str(e)}]


@mcp.tool()
def get_average_strain(days: int = 7) -> dict:
    """Calculate average WHOOP strain over the past N days."""
    try:
        data = api_get(f"/cycle?limit={days}")
        strains = [c["score"].get("strain", 0) for c in data.get("records", []) if c.get("score")]
        if not strains:
            return {"error": "No strain data"}
        return {
            "days":         days,
            "average_strain": round(sum(strains) / len(strains), 1),
            "max_strain":     round(max(strains), 1),
            "min_strain":     round(min(strains), 1),
        }
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_user_body_measurements() -> dict:
    """Get WHOOP user body measurements and profile."""
    try:
        return api_get("/user/measurement/body")
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    mcp.run(transport="stdio")
