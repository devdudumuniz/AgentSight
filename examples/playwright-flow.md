# Playwright Flow

AgentSight exposes browser adapter primitives without making Playwright a hard dependency.

```python
from pathlib import Path

from agentsight.adapters.playwright import capture_before_after

async def run(page):
    async def action():
        await page.get_by_role("button", name="Save").click()

    return await capture_before_after(page, action, Path(".vision-runs/web"), "save-flow")
```

Install Playwright support only when needed:

```bash
python -m pip install -e ".[playwright]"
```
