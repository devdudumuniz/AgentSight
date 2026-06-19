from __future__ import annotations

import json
import hashlib
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4


def hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


@dataclass(frozen=True)
class EvidenceEvent:
    event_id: str
    label: str
    scope: str
    backend: str
    image_path: str
    redacted_image_path: str | None
    sha256: str
    timestamp_utc: str
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class EvidenceStore:
    def __init__(self, run_dir: Path, *, run_id: str | None = None) -> None:
        self.run_dir = run_dir
        self.run_id = run_id or run_dir.name or str(uuid4())
        self.events_path = self.run_dir / "events.jsonl"
        self.manifest_path = self.run_dir / "manifest.json"

    def append_event(self, event: EvidenceEvent | dict[str, Any]) -> dict[str, Any]:
        self.run_dir.mkdir(parents=True, exist_ok=True)
        payload = event.to_dict() if isinstance(event, EvidenceEvent) else event
        with self.events_path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")
        return payload

    def list_events(self) -> list[dict[str, Any]]:
        if not self.events_path.exists():
            return []
        return [
            json.loads(line)
            for line in self.events_path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

    def load_event(self, event_id: str) -> dict[str, Any]:
        for event in self.list_events():
            if event.get("event_id") == event_id:
                return event
        raise KeyError(f"Evidence event not found: {event_id}")

    def write_manifest(self) -> Path:
        self.run_dir.mkdir(parents=True, exist_ok=True)
        events = self.list_events()
        payload = {
            "schema_version": "agentsight.manifest.v1",
            "run_id": self.run_id,
            "run_dir": str(self.run_dir),
            "events_count": len(events),
            "updated_at_utc": datetime.now(timezone.utc).isoformat(),
            "events_path": str(self.events_path),
        }
        self.manifest_path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        return self.manifest_path

    def export_agent_json(self) -> dict[str, Any]:
        manifest = {}
        if self.manifest_path.exists():
            manifest = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        return {
            "schema_version": "agentsight.agent_export.v1",
            "run_id": self.run_id,
            "manifest": manifest,
            "events": self.list_events(),
        }
