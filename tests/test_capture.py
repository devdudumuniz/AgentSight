import json
import importlib
import subprocess
import sys

import pytest

from agentsight.adapters.mss_capture import CaptureBackendError
from agentsight.capture import CaptureConfig, capture
from agentsight.policy import CapturePolicy, PolicyViolation


def test_mock_capture_generates_png_and_metadata(tmp_path):
    result = capture(
        CaptureConfig(
            label="demo",
            output_dir=tmp_path,
            scope="region",
            region=(0, 0, 100, 100),
            consent=True,
            mock=True,
        )
    )

    assert result["schema_version"] == "agentsight.capture.v1"
    assert result["backend"] == "mock"
    assert result["image_path"].endswith(".png")
    assert (tmp_path / "events.jsonl").exists()
    assert (tmp_path / "manifest.json").exists()


def test_real_capture_backend_error_does_not_create_placeholder(tmp_path, monkeypatch):
    def fail_capture(region, output_path):
        raise CaptureBackendError("no display")

    capture_module = importlib.import_module("agentsight.capture")
    monkeypatch.setattr(capture_module, "capture_region", fail_capture)

    with pytest.raises(CaptureBackendError):
        capture(
            CaptureConfig(
                label="real",
                output_dir=tmp_path,
                scope="region",
                region=(0, 0, 100, 100),
                consent=True,
                mock=False,
            )
        )

    assert not list(tmp_path.glob("*.png"))


def test_fullscreen_without_allow_fullscreen_fails(tmp_path):
    with pytest.raises(PolicyViolation):
        capture(
            CaptureConfig(
                label="full",
                output_dir=tmp_path,
                scope="fullscreen",
                consent=True,
                mock=True,
            ),
            CapturePolicy(allow_fullscreen=False),
        )


def test_mock_capture_with_redaction_regions_sets_redacted_path(tmp_path):
    result = capture(
        CaptureConfig(
            label="redacted",
            output_dir=tmp_path,
            scope="region",
            region=(0, 0, 200, 120),
            redaction_regions=((10, 10, 50, 40),),
            consent=True,
            mock=True,
        )
    )

    assert result["redacted_image_path"] is not None
    assert result["image_path"] == result["redacted_image_path"]
    assert result["sha256"]


def test_cli_module_help_executes():
    result = subprocess.run(
        [sys.executable, "-m", "agentsight.cli", "--help"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "usage: agentsight" in result.stdout


def test_cli_capture_mock_report_and_cleanup(tmp_path):
    run_dir = tmp_path / "run"
    capture_result = subprocess.run(
        [
            sys.executable,
            "-m",
            "agentsight.cli",
            "capture",
            "--mock",
            "--label",
            "demo",
            "--scope",
            "region",
            "--region",
            "0,0,100,100",
            "--consent",
            "--output",
            str(run_dir),
            "--json",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert capture_result.returncode == 0
    payload = json.loads(capture_result.stdout)
    assert payload["backend"] == "mock"

    report_result = subprocess.run(
        [sys.executable, "-m", "agentsight.cli", "report", "--run", str(run_dir)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert report_result.returncode == 0
    assert "AgentSight Visual Evidence Report" in report_result.stdout

    cleanup_result = subprocess.run(
        [
            sys.executable,
            "-m",
            "agentsight.cli",
            "cleanup",
            "--root",
            str(tmp_path),
            "--retention-hours",
            "0",
            "--keep-manifest",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert cleanup_result.returncode == 0
    assert "deleted_files" in cleanup_result.stdout
