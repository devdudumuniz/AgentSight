from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from PIL import Image

from agentsight.policy import Region


class CaptureBackendError(RuntimeError):
    """Raised when a real capture backend cannot capture the requested image."""


def _save_grab(raw: Any, output_path: Path) -> tuple[int, int]:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    img = Image.frombytes("RGB", raw.size, raw.rgb)
    img.save(output_path)
    return img.width, img.height


def capture_region(region: Region, output_path: Path, *, monitor_index: int = 1) -> dict[str, Any]:
    try:
        import mss  # type: ignore
    except Exception as exc:  # pragma: no cover - environment dependent
        raise CaptureBackendError("mss is not installed. Install agentsight[capture].") from exc

    x, y, width, height = region
    monitor = {"left": x, "top": y, "width": width, "height": height}

    try:
        with mss.mss() as sct:
            raw = sct.grab(monitor)
            image_width, image_height = _save_grab(raw, output_path)
    except Exception as exc:
        raise CaptureBackendError(f"mss region capture failed: {exc}") from exc

    return {
        "backend": "mss",
        "width": image_width,
        "height": image_height,
        "monitor_index": monitor_index,
        "path": str(output_path),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    }


def capture_fullscreen(output_path: Path, *, monitor_index: int = 1) -> dict[str, Any]:
    try:
        import mss  # type: ignore
    except Exception as exc:  # pragma: no cover - environment dependent
        raise CaptureBackendError("mss is not installed. Install agentsight[capture].") from exc

    try:
        with mss.mss() as sct:
            if len(sct.monitors) <= monitor_index:
                raise CaptureBackendError(f"mss monitor index unavailable: {monitor_index}")
            raw = sct.grab(sct.monitors[monitor_index])
            image_width, image_height = _save_grab(raw, output_path)
    except CaptureBackendError:
        raise
    except Exception as exc:
        raise CaptureBackendError(f"mss fullscreen capture failed: {exc}") from exc

    return {
        "backend": "mss",
        "width": image_width,
        "height": image_height,
        "monitor_index": monitor_index,
        "path": str(output_path),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    }
