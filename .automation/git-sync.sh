#!/bin/zsh

set -euo pipefail

REPO_DIR="/Users/sri/Documents/MyVault"
LOG_DIR="/Users/sri/.codex/automations/git-sync"
LOG_FILE="$LOG_DIR/git-sync.log"

mkdir -p "$LOG_DIR"

timestamp() {
  date "+%Y-%m-%d %H:%M:%S %Z"
}

log() {
  printf '[%s] %s\n' "$(timestamp)" "$1" | tee -a "$LOG_FILE"
}

{
  cd "$REPO_DIR"

  branch="$(git rev-parse --abbrev-ref HEAD)"
  log "Starting vault sync on branch $branch"

  if ! git remote get-url origin >/dev/null 2>&1; then
    log "Remote 'origin' is not configured"
    exit 1
  fi

  if [[ -n "$(git status --porcelain)" ]]; then
    log "Changes detected; creating sync commit"
    git add -A
    git commit -m "vault sync: $(date '+%Y-%m-%d %H:%M:%S %Z')"
  else
    log "No uncommitted changes detected"
  fi

  log "Rebasing against origin/$branch"
  git pull --rebase --autostash origin "$branch"

  log "Pushing to origin/$branch"
  git push origin "$branch"

  log "Vault sync completed successfully"
} >>"$LOG_FILE" 2>&1
