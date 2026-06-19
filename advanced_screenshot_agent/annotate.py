from __future__ import annotations

import warnings

warnings.warn(
    "advanced_screenshot_agent.annotate is deprecated; use agentsight.annotate instead.",
    DeprecationWarning,
    stacklevel=2,
)

from agentsight.annotate import *  # noqa: E402,F403
