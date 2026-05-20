#!/usr/bin/env python3
"""
scan_todos.py — Second Brain TODO Scanner
Scans the repo for assignments, labs, projects, and todo items,
then writes an updated notes/TODO.md.

Run this locally or via GitHub Actions.
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

# ── Config ─────────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).parent.parent
TODO_FILE = REPO_ROOT / "notes" / "TODO.md"

# Folder/file names that signal a task item
TASK_PATTERNS = re.compile(
    r"(assign|homework|hw|lab|project|proj|exercise|problem.?set|pset|exam|quiz|midterm|final|worksheet|report|essay|presentation)",
    re.IGNORECASE,
)

# Markers that signal a task is DONE
DONE_MARKERS = re.compile(
    r"(done|complete|completed|submitted|submit|turned.?in|finished|graded|pass)",
    re.IGNORECASE,
)

# Due date patterns in file content
DUE_PATTERN = re.compile(
    r"(?:due|deadline)[:\s]+(.{1,40})",
    re.IGNORECASE,
)

# Ignore these folders
IGNORE_DIRS = {".git", ".github", "node_modules", "__pycache__", ".venv", "venv"}


# ── Helpers ─────────────────────────────────────────────────────────────────

def is_task_path(path: Path) -> bool:
    """Return True if the path name matches a task pattern."""
    return bool(TASK_PATTERNS.search(path.name))


def is_done(path: Path) -> bool:
    """Heuristic: decide if a task folder/file looks completed."""
    name_lower = path.name.lower()
    # Name itself signals completion
    if DONE_MARKERS.search(name_lower):
        return True
    # Parent folder signals completion
    if DONE_MARKERS.search(path.parent.name.lower()):
        return True
    # For directories: look for a "done" or "submitted" marker file inside
    if path.is_dir():
        for marker in ["done", "completed", "submitted", "DONE", "SUBMITTED"]:
            if (path / marker).exists() or (path / f"{marker}.md").exists():
                return True
        # Check if any immediate child has a done-like name
        try:
            for child in path.iterdir():
                if DONE_MARKERS.search(child.name.lower()):
                    return True
        except PermissionError:
            pass
    return False


def extract_due_date(path: Path) -> str | None:
    """Try to find a due date in a markdown file."""
    if path.suffix not in (".md", ".txt"):
        return None
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
        m = DUE_PATTERN.search(text)
        if m:
            return m.group(1).strip().rstrip(".,;")
    except Exception:
        pass
    return None


def extract_checkboxes(path: Path) -> list[dict]:
    """Extract markdown checkbox items from a file."""
    items = []
    if path.suffix != ".md":
        return items
    try:
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        for line in lines:
            m = re.match(r"\s*-\s+\[([ xX])\]\s+(.+)", line)
            if m:
                done = m.group(1).lower() == "x"
                text = m.group(2).strip()
                items.append({"text": text, "done": done, "source": str(path.relative_to(REPO_ROOT))})
    except Exception:
        pass
    return items


def scan_repo() -> dict:
    """Walk the repo and collect task items."""
    open_tasks = []
    done_tasks = []
    checkbox_open = []
    checkbox_done = []

    for root, dirs, files in os.walk(REPO_ROOT):
        # Prune ignored dirs
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        root_path = Path(root)

        # Check directories
        for d in list(dirs):
            dir_path = root_path / d
            if is_task_path(dir_path):
                rel = str(dir_path.relative_to(REPO_ROOT))
                due = None
                # Look for a README or description file inside
                for candidate in ["README.md", "readme.md", "description.md", f"{d}.md"]:
                    candidate_path = dir_path / candidate
                    if candidate_path.exists():
                        due = extract_due_date(candidate_path)
                        break

                entry = {"name": d, "path": rel, "due": due}
                if is_done(dir_path):
                    done_tasks.append(entry)
                else:
                    open_tasks.append(entry)

        # Check files
        for f in files:
            file_path = root_path / f
            if is_task_path(file_path) and file_path.suffix in (".md", ".txt", ".pdf", ".ipynb"):
                rel = str(file_path.relative_to(REPO_ROOT))
                due = extract_due_date(file_path)
                entry = {"name": f, "path": rel, "due": due}
                if is_done(file_path):
                    done_tasks.append(entry)
                else:
                    open_tasks.append(entry)

            # Always extract checkboxes from all markdown files
            if file_path.suffix == ".md" and file_path.name != "TODO.md":
                for cb in extract_checkboxes(file_path):
                    if cb["done"]:
                        checkbox_done.append(cb)
                    else:
                        checkbox_open.append(cb)

    return {
        "open": open_tasks,
        "done": done_tasks,
        "checkbox_open": checkbox_open,
        "checkbox_done": checkbox_done,
    }


def format_entry(entry: dict) -> str:
    due_str = f" *(due: {entry['due']})*" if entry.get("due") else ""
    return f"- [ ] **{entry['name']}** — `{entry['path']}`{due_str}"


def format_done_entry(entry: dict) -> str:
    return f"- [x] ~~{entry['name']}~~ — `{entry['path']}`"


def build_todo_md(data: dict) -> str:
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# 📋 TODO — Second Brain",
        "",
        f"> *Auto-generated on {now}. Edit this file to manually mark items done — changes are preserved on the next sync.*",
        "",
    ]

    # ── Open tasks from file/folder scan ──
    if data["open"]:
        lines += ["## 🔴 Open Tasks", ""]
        for entry in data["open"]:
            lines.append(format_entry(entry))
        lines.append("")

    # ── Open checkbox items from notes ──
    if data["checkbox_open"]:
        lines += ["## 📝 Open Checklist Items (from notes)", ""]
        for cb in data["checkbox_open"]:
            lines.append(f"- [ ] {cb['text']} *(in `{cb['source']}`)*")
        lines.append("")

    # ── Done tasks ──
    if data["done"] or data["checkbox_done"]:
        lines += ["## ✅ Completed", ""]
        for entry in data["done"]:
            lines.append(format_done_entry(entry))
        for cb in data["checkbox_done"]:
            lines.append(f"- [x] ~~{cb['text']}~~ *(in `{cb['source']}`)*")
        lines.append("")

    if not data["open"] and not data["checkbox_open"]:
        lines += ["## ✅ All caught up!", "", "No open tasks found in the repo.", ""]

    return "\n".join(lines)


def preserve_manual_completions(new_md: str, existing_md: str) -> str:
    """
    If the user manually checked off a box in TODO.md (changed `- [ ]` to `- [x]`),
    keep that item as done even if the scanner would re-open it.
    """
    manually_done = set()
    for line in existing_md.splitlines():
        m = re.match(r"-\s+\[x\]\s+\*\*(.+?)\*\*", line, re.IGNORECASE)
        if m:
            manually_done.add(m.group(1))

    if not manually_done:
        return new_md

    result_lines = []
    for line in new_md.splitlines():
        m = re.match(r"-\s+\[\s+\]\s+\*\*(.+?)\*\*", line)
        if m and m.group(1) in manually_done:
            # User already checked this off — keep it done
            line = line.replace("- [ ]", "- [x]", 1)
            line = re.sub(r"\*\*(.+?)\*\*", r"~~\1~~", line)
        result_lines.append(line)
    return "\n".join(result_lines)


def main():
    # If TODO.md is in manual mode, skip auto-generation entirely
    if TODO_FILE.exists() and "<!-- manual -->" in TODO_FILE.read_text(encoding="utf-8"):
        print("📌 TODO.md is in manual mode — skipping auto-generation.")
        return

    print("🔍 Scanning repo for tasks...")
    data = scan_repo()
    print(f"  Found {len(data['open'])} open tasks, {len(data['done'])} done tasks")
    print(f"  Found {len(data['checkbox_open'])} open checkboxes, {len(data['checkbox_done'])} done checkboxes")

    new_md = build_todo_md(data)

    # Preserve any manual completions the user marked
    existing_md = ""
    if TODO_FILE.exists():
        existing_md = TODO_FILE.read_text(encoding="utf-8")

    final_md = preserve_manual_completions(new_md, existing_md)

    # Write the file
    TODO_FILE.parent.mkdir(parents=True, exist_ok=True)
    TODO_FILE.write_text(final_md, encoding="utf-8")
    print(f"✅ Updated {TODO_FILE}")


if __name__ == "__main__":
    main()
