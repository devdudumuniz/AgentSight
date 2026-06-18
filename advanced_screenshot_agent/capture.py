from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from PIL import Image

from .policy import CapturePolicy


@dataclass(frozen=True)
class CaptureConfig:
    label: str
    output_dir: Path
    region: tuple[int, int, int, int] | None = None
    fullscreen: bool = False
    window_title: str | None = None
    consent: bool = False
    redact: bool = True


def _slugify(value: str) -> str:
    cleaned = "".join(ch.lower() if ch.isalnum() else "-" for ch in value)
    return "-".join(part for part in cleaned.split("-") if part)[:80] or "capture"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def capture_screen(config: CaptureConfig, policy: CapturePolicy | None = None) -> dict[str, Any]:
    """Captura tela/região e salva PNG + metadata JSON.

    Usa mss em tempo real. Em CI/headless, se mss falhar, gera uma imagem placeholder.
    Isso mantém testes honestos sem fingir que temos display disponível.
    """
    policy = policy or CapturePolicy()
    effective_fullscreen = config.fullscreen or (config.region is None and config.window_title is None)
    policy.validate_capture_request(
        fullscreen=effective_fullscreen,
        window_title=config.window_title,
        region=config.region,
        consent=config.consent,
    )

    if config.window_title and config.region is None and not config.fullscreen:
        raise NotImplementedError(
            "Captura por título de janela ainda não é suportada sem região explícita. "
            "Use --fullscreen ou informe uma região."
        )

    config.output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    basename = f"{timestamp}-{_slugify(config.label)}"
    image_path = config.output_dir / f"{basename}.png"

    capture_backend = "mss"
    capture_error: str | None = None
    try:
        import mss  # type: ignore

        with mss.mss() as sct:
            if config.region:
                x, y, width, height = config.region
                monitor = {"left": x, "top": y, "width": width, "height": height}
            else:
                monitor = sct.monitors[1]
            raw = sct.grab(monitor)
            img = Image.frombytes("RGB", raw.size, raw.rgb)
            img.save(image_path)
    except Exception as exc:
        # Sem display real. Melhor gerar placeholder explícito do que falhar silenciosamente.
        capture_backend = "placeholder"
        capture_error = str(exc)
        img = Image.new("RGB", (1280, 720), color=(245, 245, 245))
        img.save(image_path)

    metadata = {
        "label": config.label,
        "path": str(image_path),
        "sha256": _sha256(image_path),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "region": config.region,
        "fullscreen": config.fullscreen,
        "window_title": config.window_title,
        "redact_requested": config.redact,
        "capture_backend": capture_backend,
        "capture_error": capture_error,
    }
    metadata_path = config.output_dir / f"{basename}.json"
    metadata_path.write_text(json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8")
    metadata["metadata_path"] = str(metadata_path)
    return metadata
