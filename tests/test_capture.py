import subprocess
import sys
from types import SimpleNamespace

import pytest
from PIL import Image

from advanced_screenshot_agent.capture import CaptureConfig, capture_screen
from advanced_screenshot_agent.policy import CapturePolicy


def test_blocks_implicit_fullscreen_capture(tmp_path):
    policy = CapturePolicy(require_user_consent=False, allow_fullscreen=False)
    config = CaptureConfig(label="implicit-full", output_dir=tmp_path, consent=True)

    with pytest.raises(PermissionError):
        capture_screen(config, policy)


def test_window_title_without_region_not_implemented(tmp_path):
    policy = CapturePolicy(require_user_consent=False, allow_window_capture=True, allow_fullscreen=True)
    config = CaptureConfig(
        label="window-only",
        output_dir=tmp_path,
        window_title="Minha Janela",
        consent=True,
    )

    with pytest.raises(NotImplementedError):
        capture_screen(config, policy)


def test_capture_applies_redaction_regions_before_save(tmp_path, monkeypatch):
    class FakeMss:
        monitors = [None, {"left": 0, "top": 0, "width": 20, "height": 20}]

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return None

        def grab(self, monitor):
            img = Image.new("RGB", (20, 20), color=(255, 255, 255))
            for x in range(10):
                for y in range(20):
                    img.putpixel((x, y), (0, 0, 0))
            return SimpleNamespace(size=img.size, rgb=img.tobytes())

    monkeypatch.setitem(sys.modules, "mss", SimpleNamespace(mss=FakeMss))

    policy = CapturePolicy(require_user_consent=False)
    config = CaptureConfig(
        label="redacted",
        output_dir=tmp_path,
        region=(0, 0, 20, 20),
        redaction_regions=((8, 0, 4, 20),),
        consent=True,
    )

    metadata = capture_screen(config, policy)
    saved = Image.open(metadata["path"]).convert("RGB")

    assert metadata["redact_applied"] is True
    assert metadata["redaction_regions_count"] == 1
    assert metadata["capture_backend"] == "mss"
    assert metadata["capture_error"] is None
    assert saved.getpixel((9, 10)) not in {(0, 0, 0), (255, 255, 255)}


def test_capture_rejects_redaction_regions_when_redaction_disabled(tmp_path):
    policy = CapturePolicy(require_user_consent=False)
    config = CaptureConfig(
        label="unsafe",
        output_dir=tmp_path,
        region=(0, 0, 10, 10),
        redaction_regions=((0, 0, 5, 5),),
        redact=False,
        consent=True,
    )

    with pytest.raises(ValueError):
        capture_screen(config, policy)


def test_cli_module_help_executes():
    result = subprocess.run(
        [sys.executable, "-m", "advanced_screenshot_agent.cli", "--help"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "usage: screenshot-agent" in result.stdout


def test_cli_capture_help_exposes_region_and_redaction_options():
    result = subprocess.run(
        [sys.executable, "-m", "advanced_screenshot_agent.cli", "capture", "--help"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "--region" in result.stdout
    assert "--redact-region" in result.stdout
    assert "--no-redact" in result.stdout
