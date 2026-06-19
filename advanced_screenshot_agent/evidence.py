from __future__ import annotations

import warnings

warnings.warn(
    "advanced_screenshot_agent.evidence is deprecated; use agentsight.evidence instead.",
    DeprecationWarning,
    stacklevel=2,
)

from agentsight.evidence import *  # noqa: E402,F403
