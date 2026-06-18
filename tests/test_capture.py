import pytest

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