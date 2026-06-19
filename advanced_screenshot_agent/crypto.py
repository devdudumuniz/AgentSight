from __future__ import annotations

import warnings

warnings.warn(
    "advanced_screenshot_agent.crypto is deprecated; use agentsight.crypto instead.",
    DeprecationWarning,
    stacklevel=2,
)

from agentsight.crypto import *  # noqa: E402,F403
