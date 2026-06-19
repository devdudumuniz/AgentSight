from __future__ import annotations

import inspect
from pathlib import Path
from typing import Any, Callable


class PlaywrightCaptureError(RuntimeError):
    """Raised when a Playwright-like target cannot capture a screenshot."""


async def _call_screenshot(target: Any, path: Path, **kwargs: Any) -> Path:
    screenshot = getattr(target, "screenshot", None)
    if screenshot is None:
        raise PlaywrightCaptureError("Object does not expose a screenshot method.")
    path.parent.mkdir(parents=True, exist_ok=True)
    result = screenshot(path=str(path), **kwargs)
    if inspect.isawaitable(result):
        await result
    return path


async def capture_page(page: Any, path: Path, *, full_page: bool = True) -> Path:
    return await _call_screenshot(page, path, full_page=full_page)


async def capture_locator(locator: Any, path: Path) -> Path:
    return await _call_screenshot(locator, path)


async def capture_before_after(
    page: Any,
    action_callable: Callable[[], Any],
    output_dir: Path,
    label: str,
) -> dict[str, str]:
    before = output_dir / f"{label}.before.png"
    after = output_dir / f"{label}.after.png"
    await capture_page(page, before)
    result = action_callable()
    if inspect.isawaitable(result):
        await result
    await capture_page(page, after)
    return {"before": str(before), "after": str(after)}
