import asyncio
from pathlib import Path

from agentsight.adapters.playwright import capture_before_after, capture_locator, capture_page


class FakeTarget:
    def __init__(self):
        self.calls = []

    async def screenshot(self, path: str, **kwargs):
        self.calls.append({"path": path, **kwargs})
        Path(path).write_bytes(b"fake")


def test_capture_page_calls_screenshot(tmp_path):
    page = FakeTarget()
    path = tmp_path / "page.png"

    asyncio.run(capture_page(page, path, full_page=True))

    assert page.calls[0]["path"] == str(path)
    assert page.calls[0]["full_page"] is True


def test_capture_locator_calls_screenshot(tmp_path):
    locator = FakeTarget()
    path = tmp_path / "locator.png"

    asyncio.run(capture_locator(locator, path))

    assert locator.calls[0]["path"] == str(path)


def test_capture_before_after_calls_action(tmp_path):
    page = FakeTarget()
    called = {"value": False}

    def action():
        called["value"] = True

    result = asyncio.run(capture_before_after(page, action, tmp_path, "flow"))

    assert called["value"] is True
    assert Path(result["before"]).exists()
    assert Path(result["after"]).exists()
