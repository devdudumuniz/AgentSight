from __future__ import annotations

import warnings

warnings.warn(
    "advanced_screenshot_agent.cli is deprecated; use agentsight.cli instead.",
    DeprecationWarning,
    stacklevel=2,
)

from agentsight.cli import *  # noqa: E402,F403

if __name__ == "__main__":
    from agentsight.cli import main

    main()
