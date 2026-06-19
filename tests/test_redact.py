import pytest
from PIL import Image

from advanced_screenshot_agent.redact import detect_sensitive_text, redact_image_regions


def test_detect_sensitive_email_and_cpf():
    hits = detect_sensitive_text("cliente teste@email.com cpf 123.456.789-10")
    kinds = {hit.kind for hit in hits}
    assert "email" in kinds
    assert "cpf" in kinds


def test_redact_image_regions_rejects_out_of_bounds_region():
    img = Image.new("RGB", (10, 10), color=(255, 255, 255))

    with pytest.raises(ValueError):
        redact_image_regions(img, [(8, 8, 4, 4)])
