#!/bin/zsh

set -euo pipefail

PLIST_SOURCE="/Users/sri/Documents/MyVault/.automation/com.sri.myvault.git-sync.plist"
PLIST_TARGET="$HOME/Library/LaunchAgents/com.sri.myvault.git-sync.plist"
LABEL="com.sri.myvault.git-sync"
UID_VALUE="$(id -u)"

mkdir -p "$HOME/Library/LaunchAgents"
cp "$PLIST_SOURCE" "$PLIST_TARGET"

launchctl bootout "gui/$UID_VALUE/$LABEL" >/dev/null 2>&1 || true
launchctl bootstrap "gui/$UID_VALUE" "$PLIST_TARGET"
launchctl enable "gui/$UID_VALUE/$LABEL"

echo "Installed $LABEL from $PLIST_TARGET"
