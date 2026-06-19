from __future__ import annotations

import warnings

warnings.warn(
    "advanced_screenshot_agent.capture is deprecated; use agentsight.capture instead.",
    DeprecationWarning,
    stacklevel=2,
)

from agentsight.capture import *  # noqa: E402,F403
