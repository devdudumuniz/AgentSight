from __future__ import annotations

import warnings

warnings.warn(
    "advanced_screenshot_agent.adapters.playwright is deprecated; "
    "use agentsight.adapters.playwright instead.",
    DeprecationWarning,
    stacklevel=2,
)

from agentsight.adapters.playwright import *  # noqa: E402,F403
