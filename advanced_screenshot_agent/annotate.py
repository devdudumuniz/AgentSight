from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


@dataclass(frozen=True)
class Annotation:
    label: str
    kind: str
    x: int
    y: int
    width: int
    height: int


def annotate_image(
    image_path: Path,
    annotations: list[Annotation],
    output_path: Path | None = None,
) -> Path:
    output_path = output_path or image_path.with_name(f"{image_path.stem}.annotated{image_path.suffix}")
    img = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.load_default()
    except Exception:
        font = None

    for index, item in enumerate(annotations, start=1):
        box = (item.x, item.y, item.x + item.width, item.y + item.height)
        draw.rectangle(box, outline="red", width=3)
        marker = f"{index}. {item.label}"
        draw.text((item.x + 4, max(0, item.y - 14)), marker, fill="red", font=font)

    img.save(output_path)
    return output_path
