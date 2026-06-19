import pytest

from agentsight.policy import CapturePolicy, PolicyViolation


def test_blocks_fullscreen_without_permission():
    policy = CapturePolicy(allow_fullscreen=False, require_user_consent=False)

    with pytest.raises(PolicyViolation):
        policy.validate_capture_request(scope="fullscreen", consent=True)


def test_requires_consent():
    policy = CapturePolicy(require_user_consent=True)

    with pytest.raises(PolicyViolation):
        policy.validate_capture_request(scope="region", region=(0, 0, 10, 10), consent=False)


def test_blocks_sensitive_window_title():
    policy = CapturePolicy(require_user_consent=False)

    with pytest.raises(PolicyViolation):
        policy.validate_capture_request(
            scope="window",
            window_title="My Password Manager",
            consent=True,
        )


def test_blocks_invalid_region():
    policy = CapturePolicy(require_user_consent=False)

    with pytest.raises(PolicyViolation):
        policy.validate_capture_request(scope="region", region=(0, 0, 0, 10), consent=True)


def test_allows_valid_region_with_consent():
    policy = CapturePolicy()

    decision = policy.validate_capture_request(scope="region", region=(0, 0, 100, 100), consent=True)

    assert decision.allowed is True
    assert decision.scope == "region"
