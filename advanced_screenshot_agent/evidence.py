from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


@dataclass(frozen=True)
class EvidenceEvent:
    event_id: str
    label: str
    image_path: str
    sha256: str
    timestamp_utc: str
    action: str = "capture"


@dataclass
class EvidenceRun:
    run_id: str = field(default_factory=lambda: str(uuid4()))
    created_at_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    events: list[EvidenceEvent] = field(default_factory=list)

    def add(self, event: EvidenceEvent) -> None:
        self.events.append(event)

    def save(self, output_dir: Path) -> Path:
        output_dir.mkdir(parents=True, exist_ok=True)
        path = output_dir / "evidence-run.json"
        payload = {
            "run_id": self.run_id,
            "created_at_utc": self.created_at_utc,
            "events": [asdict(event) for event in self.events],
        }
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        return path
