#!/usr/bin/env python3
"""
One-time setup: installs WHOOP + Strava MCP servers into Claude's config.
Run with: python3 ~/Documents/MyVault/setup-mcps.py
"""

import json, os, subprocess, sys

CONFIG_PATH = os.path.expanduser(
    "~/Library/Application Support/Claude/claude_desktop_config.json"
)
VAULT = os.path.expanduser("~/Documents/MyVault")

# ── Install Python deps for WHOOP MCP ─────────────────────────────────────────
print("📦  Installing WHOOP MCP dependencies...")
subprocess.run([
    sys.executable, "-m", "pip", "install",
    "mcp", "whoop", "fastapi", "uvicorn",
    "requests", "python-dotenv", "pydantic", "--quiet"
], check=True)
print("    ✓ Done")

# ── Read existing config ───────────────────────────────────────────────────────
os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
if os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH) as f:
        config = json.load(f)
    print(f"\n📄  Existing config loaded ({len(config.get('mcpServers', {}))} servers found)")
else:
    config = {}
    print("\n📄  Creating new claude_desktop_config.json")

if "mcpServers" not in config:
    config["mcpServers"] = {}

# ── Add WHOOP MCP ──────────────────────────────────────────────────────────────
config["mcpServers"]["whoop"] = {
    "command": sys.executable,
    "args": [f"{VAULT}/whoop-mcp-server/src/whoop_server.py"],
    "env": {
        "WHOOP_EMAIL":    "hellosri2006@gmail.com",
        "WHOOP_PASSWORD": "h@&.CjOTT3cn=(fzqZ]?"
    }
}
print("✅  WHOOP MCP configured")

# ── Add Strava MCP ─────────────────────────────────────────────────────────────
config["mcpServers"]["strava"] = {
    "command": "npx",
    "args": ["-y", "@r-huijts/strava-mcp-server"],
    "env": {
        "STRAVA_CLIENT_ID":     "235717",
        "STRAVA_CLIENT_SECRET": "3e471ccdc5945ca837b71d79bdbe712fdb19fd79"
    }
}
print("✅  Strava MCP configured")

# ── Write config ───────────────────────────────────────────────────────────────
with open(CONFIG_PATH, "w") as f:
    json.dump(config, f, indent=2)

print(f"\n✅  Saved to: {CONFIG_PATH}")
print("\nAll MCP servers now configured:")
for name in config["mcpServers"]:
    marker = "←  new" if name in ("whoop", "strava") else ""
    print(f"    • {name} {marker}")

print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Next steps:
  1. Quit Claude completely  (Cmd+Q)
  2. Reopen Claude
  3. In a new Cowork session, say:
       "Connect my Strava account"
     to complete the Strava OAuth flow
     (needed once to get activity:read scope)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
