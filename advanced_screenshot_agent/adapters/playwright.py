from __future__ import annotations

from pathlib import Path


async def capture_page(page, path: Path, *, full_page: bool = True) -> Path:
    """Adapter mínimo para Playwright.

    Mantém a ferramenta compatível com o padrão oficial de page.screenshot().
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    await page.screenshot(path=str(path), full_page=full_page)
    return path
