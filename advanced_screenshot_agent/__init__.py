from __future__ import annotations

import warnings

warnings.warn(
    "advanced_screenshot_agent is deprecated; use agentsight instead.",
    DeprecationWarning,
    stacklevel=2,
)

from agentsight import *  # noqa: E402,F403
