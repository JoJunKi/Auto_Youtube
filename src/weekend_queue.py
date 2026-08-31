"""Public reference implementation of the translated-video inventory gate."""
from __future__ import annotations

import json
from pathlib import Path


def ready_episodes(root: Path) -> list[Path]:
    """Return publishable episodes oldest-first; test builds are excluded."""
    queue: list[tuple[str, Path]] = []
    for status_file in root.glob("*/status.json"):
        status = json.loads(status_file.read_text(encoding="utf-8-sig"))
        if status.get("state") != "ready" or status.get("publish") is not True:
            continue
        if status.get("upload_blocked") is True:
            continue
        queue.append((status.get("ready_at", ""), status_file.parent))
    return [path for _, path in sorted(queue)]


def assert_complete(episode: Path) -> None:
    """Fail closed unless the long form and all six short forms exist."""
    status = json.loads((episode / "status.json").read_text(encoding="utf-8-sig"))
    required = [
        Path(status["final_video"]),
        Path(status["thumbnail"]),
        Path(status["description_file"]),
        episode / "shorts" / "batch_manifest.json",
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise RuntimeError(f"incomplete episode: {missing}")
    manifest = json.loads(required[-1].read_text(encoding="utf-8"))
    if len(manifest.get("clips", [])) != 6:
        raise RuntimeError("exactly six short-form videos are required")

