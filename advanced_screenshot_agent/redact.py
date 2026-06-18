from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageFilter


SENSITIVE_PATTERNS = {
    "email": re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+"),
    "cpf": re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b|\b\d{11}\b"),
    "card_like": re.compile(r"\b(?:\d[ -]*?){13,19}\b"),
    "token_like": re.compile(r"(?i)\b(api[_-]?key|token|secret|password|senha)\b"),
}


@dataclass(frozen=True)
class RedactionHit:
    kind: str
    text: str


def detect_sensitive_text(text: str) -> list[RedactionHit]:
    hits: list[RedactionHit] = []
    for kind, pattern in SENSITIVE_PATTERNS.items():
        for match in pattern.finditer(text):
            hits.append(RedactionHit(kind=kind, text=match.group(0)))
    return hits


def redact_regions(
    image_path: Path,
    regions: list[tuple[int, int, int, int]],
    output_path: Path | None = None,
) -> Path:
    """Aplica blur em regiões específicas da imagem.

    Coordenadas: x, y, width, height. Simples, previsível e auditável.
    """
    output_path = output_path or image_path.with_name(f"{image_path.stem}.redacted{image_path.suffix}")
    img = Image.open(image_path).convert("RGB")

    for x, y, width, height in regions:
        box = (x, y, x + width, y + height)
        crop = img.crop(box).filter(ImageFilter.GaussianBlur(radius=18))
        img.paste(crop, box)

    img.save(output_path)
    return output_path
