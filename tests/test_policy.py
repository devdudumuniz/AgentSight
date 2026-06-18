import pytest

from advanced_screenshot_agent.policy import CapturePolicy


def test_blocks_fullscreen_without_permission():
    policy = CapturePolicy(allow_fullscreen=False, require_user_consent=False)
    with pytest.raises(PermissionError):
        policy.validate_capture_request(fullscreen=True, window_title=None, region=None, consent=True)


def test_requires_consent():
    policy = CapturePolicy(require_user_consent=True)
    with pytest.raises(PermissionError):
        policy.validate_capture_request(fullscreen=False, window_title=None, region=(0, 0, 10, 10), consent=False)


def test_blocks_sensitive_window_title():
    policy = CapturePolicy(require_user_consent=False)
    with pytest.raises(PermissionError):
        policy.validate_capture_request(
            fullscreen=False,
            window_title="My Password Manager",
            region=None,
            consent=True,
        )


def test_blocks_window_capture_when_disabled():
    policy = CapturePolicy(require_user_consent=False, allow_window_capture=False)
    with pytest.raises(PermissionError):
        policy.validate_capture_request(
            fullscreen=False,
            window_title="Dashboard",
            region=None,
            consent=True,
        )


def test_blocks_region_capture_when_disabled():
    policy = CapturePolicy(require_user_consent=False, allow_region_capture=False)
    with pytest.raises(PermissionError):
        policy.validate_capture_request(
            fullscreen=False,
            window_title=None,
            region=(0, 0, 100, 100),
            consent=True,
        )
