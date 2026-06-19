from __future__ import annotations

import warnings

warnings.warn(
    "advanced_screenshot_agent.redact is deprecated; use agentsight.redact instead.",
    DeprecationWarning,
    stacklevel=2,
)

from agentsight.redact import *  # noqa: E402,F403
