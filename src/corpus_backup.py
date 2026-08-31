"""Reference implementation of a consistent append-only corpus backup."""
from pathlib import Path
import sqlite3


def backup(source: Path, destination: Path) -> None:
    """Back up a live SQLite database and verify the resulting snapshot."""
    source_connection = sqlite3.connect(f"file:{source}?mode=ro", uri=True)
    destination_connection = sqlite3.connect(destination)
    try:
        source_connection.backup(destination_connection, pages=1000)
        result = destination_connection.execute("PRAGMA integrity_check").fetchone()[0]
        if result != "ok":
            raise RuntimeError(f"backup integrity check failed: {result}")
    finally:
        destination_connection.close()
        source_connection.close()
