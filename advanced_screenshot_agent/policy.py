from __future__ import annotations

import warnings

warnings.warn(
    "advanced_screenshot_agent.policy is deprecated; use agentsight.policy instead.",
    DeprecationWarning,
    stacklevel=2,
)

from agentsight.policy import *  # noqa: E402,F403
