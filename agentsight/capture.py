from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4

from PIL import Image, ImageDraw

from .adapters.mss_capture import CaptureBackendError, capture_fullscreen, capture_region
from .evidence import EvidenceStore, hash_file
from .policy import CapturePolicy, CaptureScope, Region
from .redact import redact_regions


def _slugify(value: str) -> str:
    cleaned = "".join(ch.lower() if ch.isalnum() else "-" for ch in value)
    return "-".join(part for part in cleaned.split("-") if part)[:80] or "capture"


def _timestamp_slug() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


@dataclass(frozen=True)
class CaptureConfig:
    label: str
    output_dir: Path | None = None
    scope: CaptureScope | str = CaptureScope.REGION
    region: Region | None = None
    redaction_regions: tuple[Region, ...] = ()
    fullscreen: bool = False
    window_title: str | None = None
    consent: bool = False
    allow_fullscreen: bool = False
    mock: bool = False
    redact: bool = True


@dataclass(frozen=True)
class CaptureResult:
    schema_version: str
    event_id: str
    label: str
    scope: str
    backend: str
    image_path: str
    redacted_image_path: str | None
    sha256: str
    timestamp_utc: str
    policy: dict[str, Any]
    warnings: list[str] = field(default_factory=list)
    manifest_path: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _default_output_dir(label: str) -> Path:
    return Path(".vision-runs") / f"{_timestamp_slug()}-{_slugify(label)}"


def _mock_capture(path: Path, *, scope: str, region: Region | None) -> dict[str, Any]:
    path.parent.mkdir(parents=True, exist_ok=True)
    width = region[2] if region else 800
    height = region[3] if region else 480
    img = Image.new("RGB", (width, height), color=(238, 241, 245))
    draw = ImageDraw.Draw(img)
    draw.rectangle((8, 8, width - 8, height - 8), outline=(60, 80, 120), width=2)
    draw.text((20, 20), "AgentSight explicit mock capture", fill=(30, 30, 30))
    img.save(path)
    return {
        "backend": "mock",
        "width": width,
        "height": height,
        "monitor_index": None,
        "path": str(path),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "scope": scope,
    }


def capture(config: CaptureConfig, policy: CapturePolicy | None = None) -> dict[str, Any]:
    scope = CaptureScope.FULLSCREEN if config.fullscreen else CaptureScope(config.scope)
    policy = policy or CapturePolicy(allow_fullscreen=config.allow_fullscreen)
    decision = policy.validate_capture_request(
        scope=scope,
        consent=config.consent,
        region=config.region,
        window_title=config.window_title,
    )

    if config.redaction_regions and not config.redact:
        raise ValueError("Redaction regions were provided, but redaction is disabled.")

    output_dir = config.output_dir or _default_output_dir(config.label)
    output_dir.mkdir(parents=True, exist_ok=True)
    basename = f"{_timestamp_slug()}-{_slugify(config.label)}"
    raw_path = output_dir / f"{basename}.png"
    final_path = raw_path
    redacted_image_path: str | None = None
    warnings = list(decision.warnings)

    if config.mock:
        metadata = _mock_capture(raw_path, scope=scope.value, region=config.region)
        warnings.append("mock_capture")
    else:
        if scope == CaptureScope.REGION:
            if config.region is None:
                raise ValueError("Region capture requires --region.")
            metadata = capture_region(config.region, raw_path)
        elif scope == CaptureScope.FULLSCREEN:
            metadata = capture_fullscreen(raw_path)
        else:
            raise CaptureBackendError(f"Real capture for scope {scope.value!r} is not available via CLI.")

    if config.redact and config.redaction_regions:
        redacted_path = output_dir / f"{basename}.redacted.png"
        report = redact_regions(raw_path, config.redaction_regions, redacted_path)
        raw_path.unlink(missing_ok=True)
        final_path = redacted_path
        redacted_image_path = report.output_path

    sha256 = hash_file(final_path)
    event_id = str(uuid4())
    result = CaptureResult(
        schema_version="agentsight.capture.v1",
        event_id=event_id,
        label=config.label,
        scope=scope.value,
        backend=str(metadata["backend"]),
        image_path=str(final_path),
        redacted_image_path=redacted_image_path,
        sha256=sha256,
        timestamp_utc=datetime.now(timezone.utc).isoformat(),
        policy={
            "consent_required": policy.require_user_consent,
            "fullscreen_allowed": policy.allow_fullscreen,
        },
        warnings=warnings,
    )

    store = EvidenceStore(output_dir)
    payload = result.to_dict()
    store.append_event(payload)
    manifest_path = store.write_manifest()
    payload["manifest_path"] = str(manifest_path)
    metadata_path = output_dir / f"{basename}.json"
    metadata_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return payload


def capture_screen(config: CaptureConfig, policy: CapturePolicy | None = None) -> dict[str, Any]:
    return capture(config, policy)
