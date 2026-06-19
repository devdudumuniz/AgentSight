from __future__ import annotations

from dataclasses import asdict, dataclass
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


def _validate_annotation(annotation: Annotation, image_size: tuple[int, int]) -> None:
    image_width, image_height = image_size
    if min(annotation.x, annotation.y, annotation.width, annotation.height) < 0:
        raise ValueError("Invalid annotation coordinates.")
    if annotation.width <= 0 or annotation.height <= 0:
        raise ValueError("Invalid annotation size.")
    if annotation.x + annotation.width > image_width or annotation.y + annotation.height > image_height:
        raise ValueError("Annotation is outside image bounds.")


def annotate_image(
    image_path: Path,
    annotations: list[Annotation],
    output_path: Path | None = None,
) -> dict[str, object]:
    output_path = output_path or image_path.with_name(f"{image_path.stem}.annotated{image_path.suffix}")
    img = Image.open(image_path).convert("RGB")
    for item in annotations:
        _validate_annotation(item, img.size)

    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.load_default()
    except Exception:  # pragma: no cover - Pillow fallback
        font = None

    for index, item in enumerate(annotations, start=1):
        box = (item.x, item.y, item.x + item.width, item.y + item.height)
        draw.rectangle(box, outline="red", width=3)
        marker = f"{index}. {item.label}"
        draw.text((item.x + 4, max(0, item.y - 14)), marker, fill="red", font=font)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(output_path)
    return {
        "image_path": str(image_path),
        "annotated_image_path": str(output_path),
        "annotations_count": len(annotations),
        "annotations": [asdict(item) for item in annotations],
    }
