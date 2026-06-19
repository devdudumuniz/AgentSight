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


Region = tuple[int, int, int, int]


def detect_sensitive_text(text: str) -> list[RedactionHit]:
    hits: list[RedactionHit] = []
    for kind, pattern in SENSITIVE_PATTERNS.items():
        for match in pattern.finditer(text):
            hits.append(RedactionHit(kind=kind, text=match.group(0)))
    return hits


def _validate_region(region: Region, image_width: int, image_height: int) -> None:
    x, y, width, height = region
    if min(x, y, width, height) < 0 or width == 0 or height == 0:
        raise ValueError("Regiao invalida para redaction.")
    if x + width > image_width or y + height > image_height:
        raise ValueError("Regiao de redaction fora dos limites da imagem.")


def redact_image_regions(image: Image.Image, regions: list[Region] | tuple[Region, ...]) -> Image.Image:
    """Aplica blur em memoria, antes de persistir a imagem final."""
    redacted = image.convert("RGB").copy()

    for region in regions:
        _validate_region(region, redacted.width, redacted.height)
        x, y, width, height = region
        box = (x, y, x + width, y + height)
        crop = redacted.crop(box).filter(ImageFilter.GaussianBlur(radius=18))
        redacted.paste(crop, box)

    return redacted


def redact_regions(
    image_path: Path,
    regions: list[Region],
    output_path: Path | None = None,
) -> Path:
    """Aplica blur em regiões específicas da imagem.

    Coordenadas: x, y, width, height. Simples, previsível e auditável.
    """
    output_path = output_path or image_path.with_name(f"{image_path.stem}.redacted{image_path.suffix}")
    img = Image.open(image_path).convert("RGB")
    redact_image_regions(img, regions).save(output_path)
    return output_path
