from PIL import Image

from agentsight.annotate import Annotation, annotate_image


def test_annotate_image_returns_metadata(tmp_path):
    image = tmp_path / "source.png"
    Image.new("RGB", (100, 100), color=(255, 255, 255)).save(image)

    result = annotate_image(
        image,
        [Annotation(label="button", kind="ui", x=10, y=10, width=20, height=20)],
        tmp_path / "annotated.png",
    )

    assert result["annotations_count"] == 1
    assert (tmp_path / "annotated.png").exists()
