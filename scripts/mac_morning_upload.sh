#!/bin/bash
# Runs on Mac each morning: pulls latest vault, uploads today's briefing to NotebookLM.
# Scheduled via launchd — see scripts/com.sri.morning-briefing.plist

set -e

VAULT="$HOME/Documents/MyVault"
TODAY=$(date +%Y-%m-%d)
BRIEFING="$VAULT/second-brain/morning-briefing/$TODAY.md"

# Pull latest from GitHub
cd "$VAULT"
git pull --ff-only origin main 2>/dev/null || git pull --ff-only origin claude/morning-briefing-audio-M2WGq 2>/dev/null || true

# Wait up to 5 minutes for today's briefing to appear (Claude may still be generating it)
WAITED=0
while [[ ! -f "$BRIEFING" && $WAITED -lt 300 ]]; do
    sleep 15
    git pull --ff-only 2>/dev/null || true
    WAITED=$((WAITED + 15))
done

if [[ ! -f "$BRIEFING" ]]; then
    echo "$(date): No briefing found for $TODAY, skipping." >> "$VAULT/scripts/upload.log"
    exit 0
fi

echo "$(date): Uploading $BRIEFING to NotebookLM..." >> "$VAULT/scripts/upload.log"
python3 "$VAULT/scripts/notebooklm_upload.py" "$BRIEFING" >> "$VAULT/scripts/upload.log" 2>&1
echo "$(date): Done." >> "$VAULT/scripts/upload.log"
