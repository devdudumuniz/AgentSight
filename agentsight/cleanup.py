from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp"}


def cleanup_runs(
    root: Path | str = ".vision-runs",
    *,
    retention_hours: int = 24,
    keep_manifest: bool = True,
) -> dict[str, Any]:
    root_path = Path(root)
    threshold = datetime.now(timezone.utc) - timedelta(hours=retention_hours)
    deleted: list[str] = []
    kept: list[str] = []

    if not root_path.exists():
        return {"root": str(root_path), "deleted_files": deleted, "kept_files": kept}

    for path in sorted(p for p in root_path.rglob("*") if p.is_file()):
        if keep_manifest and path.name == "manifest.json":
            kept.append(str(path))
            continue

        if path.suffix.lower() not in IMAGE_SUFFIXES:
            kept.append(str(path))
            continue

        modified = datetime.fromtimestamp(path.stat().st_mtime, timezone.utc)
        if modified <= threshold:
            path.unlink()
            deleted.append(str(path))
        else:
            kept.append(str(path))

    return {"root": str(root_path), "deleted_files": deleted, "kept_files": kept}
