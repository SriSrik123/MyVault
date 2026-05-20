#!/usr/bin/env python3
"""
Upload today's morning briefing to NotebookLM and generate an audio overview.

Usage:
    python3 notebooklm_upload.py <briefing_file_path>
    python3 notebooklm_upload.py  # auto-finds today's briefing

Run `notebooklm login` once before first use.
"""

import asyncio
import sys
import os
from datetime import date
from pathlib import Path

VAULT = Path("/home/user/MyVault")
BRIEFING_DIR = VAULT / "second-brain" / "morning-briefing"
AUDIO_DIR = BRIEFING_DIR / "audio"
NOTEBOOK_TITLE = "Sri's Daily Morning Briefing"


async def run(briefing_path: Path) -> None:
    from notebooklm import NotebookLMClient

    today = date.today().isoformat()
    content = briefing_path.read_text(encoding="utf-8")
    source_title = f"Morning Briefing — {today}"

    print(f"[notebooklm] Connecting...")
    async with NotebookLMClient.from_storage() as client:
        # Find or create the notebook
        notebooks = await client.notebooks.list()
        notebook = next((n for n in notebooks if n.title == NOTEBOOK_TITLE), None)

        if notebook is None:
            print(f"[notebooklm] Creating notebook: '{NOTEBOOK_TITLE}'")
            notebook = await client.notebooks.create(NOTEBOOK_TITLE)
        else:
            print(f"[notebooklm] Found existing notebook: '{NOTEBOOK_TITLE}'")

        notebook_id = notebook.id

        # Remove all existing sources so audio is based only on today's briefing
        existing_sources = await client.sources.list(notebook_id)
        for src in existing_sources:
            print(f"[notebooklm] Removing old source: {src.title}")
            await client.sources.delete(notebook_id, src.id)

        # Add today's briefing as text source
        print(f"[notebooklm] Uploading briefing as source...")
        source = await client.sources.add_text(
            notebook_id,
            title=source_title,
            content=content,
            wait=True,
            wait_timeout=120.0,
        )
        print(f"[notebooklm] Source ready: {source.title}")

        # Trigger audio overview generation
        print(f"[notebooklm] Generating audio overview (this takes ~2-3 min)...")
        status = await client.artifacts.generate_audio(notebook_id)

        # Wait for audio to finish
        final_status = await client.artifacts.wait_for_completion(
            notebook_id,
            status.task_id,
            timeout=300.0,
        )

        if final_status.is_complete:
            AUDIO_DIR.mkdir(parents=True, exist_ok=True)
            audio_path = AUDIO_DIR / f"{today}.mp3"
            downloaded = await client.artifacts.download_audio(
                notebook_id,
                output_path=str(audio_path),
            )
            print(f"[notebooklm] Audio saved: {downloaded}")
        else:
            print(f"[notebooklm] Audio generation incomplete: {final_status}")


def main() -> None:
    if len(sys.argv) > 1:
        briefing_path = Path(sys.argv[1]).expanduser()
    else:
        today = date.today().isoformat()
        briefing_path = BRIEFING_DIR / f"{today}.md"

    if not briefing_path.exists():
        print(f"[notebooklm] ERROR: briefing file not found: {briefing_path}")
        sys.exit(1)

    asyncio.run(run(briefing_path))


if __name__ == "__main__":
    main()
