from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from pathlib import Path

from PIL import Image, ImageFilter

Region = tuple[int, int, int, int]

SENSITIVE_PATTERNS = {
    "email": re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+"),
    "cpf": re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b|\b\d{11}\b"),
    "card_like": re.compile(r"\b(?:\d[ -]*?){13,19}\b"),
    "token_like": re.compile(r"(?i)\b(?:sk-[a-z0-9_-]+|api[_-]?key|token|secret|password|senha)\b"),
}


@dataclass(frozen=True)
class RedactionHit:
    kind: str
    masked: str


@dataclass(frozen=True)
class RedactionReport:
    image_path: str
    output_path: str
    regions_count: int
    hits: list[RedactionHit] = field(default_factory=list)

    def to_dict(self) -> dict[str, object]:
        return {
            "image_path": self.image_path,
            "output_path": self.output_path,
            "regions_count": self.regions_count,
            "hits": [asdict(hit) for hit in self.hits],
        }


def detect_sensitive_text(text: str) -> list[RedactionHit]:
    hits: list[RedactionHit] = []
    for kind, pattern in SENSITIVE_PATTERNS.items():
        for match in pattern.finditer(text):
            hits.append(RedactionHit(kind=kind, masked=mask_value(match.group(0))))
    return hits


def mask_value(value: str) -> str:
    if "@" in value:
        local, _, domain = value.partition("@")
        prefix = local[:1] if local else "*"
        return f"{prefix}***@{domain}"

    digits = re.sub(r"\D", "", value)
    if len(digits) == 11:
        return "***.***.***-**"

    normalized = value.strip()
    if normalized.lower().startswith("sk-") and len(normalized) > 7:
        return f"sk-...{normalized[-4:]}"

    if len(normalized) <= 4:
        return "***"

    return f"{normalized[:2]}...{normalized[-4:]}"


def validate_regions(regions: list[Region] | tuple[Region, ...], image_size: tuple[int, int]) -> None:
    image_width, image_height = image_size
    for region in regions:
        x, y, width, height = region
        if min(x, y, width, height) < 0 or width <= 0 or height <= 0:
            raise ValueError("Invalid redaction region.")
        if x + width > image_width or y + height > image_height:
            raise ValueError("Redaction region is outside image bounds.")


def redact_image_regions(image: Image.Image, regions: list[Region] | tuple[Region, ...]) -> Image.Image:
    redacted = image.convert("RGB").copy()
    validate_regions(regions, redacted.size)

    for x, y, width, height in regions:
        box = (x, y, x + width, y + height)
        crop = redacted.crop(box).filter(ImageFilter.GaussianBlur(radius=18))
        redacted.paste(crop, box)

    return redacted


def redact_regions(
    image_path: Path,
    regions: list[Region] | tuple[Region, ...],
    output_path: Path | None = None,
) -> RedactionReport:
    output_path = output_path or image_path.with_name(f"{image_path.stem}.redacted{image_path.suffix}")
    img = Image.open(image_path).convert("RGB")
    redacted = redact_image_regions(img, regions)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    redacted.save(output_path)

    return RedactionReport(
        image_path=str(image_path),
        output_path=str(output_path),
        regions_count=len(regions),
    )
