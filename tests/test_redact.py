from pathlib import Path

from PIL import Image

from agentsight.redact import detect_sensitive_text, mask_value, redact_regions


def test_detect_sensitive_email_cpf_and_token():
    hits = detect_sensitive_text("email dudu@example.com cpf 123.456.789-10 token sk-liveabcd")
    kinds = {hit.kind for hit in hits}

    assert "email" in kinds
    assert "cpf" in kinds
    assert "token_like" in kinds


def test_mask_value_does_not_leak_complete_secret():
    assert mask_value("dudu@example.com") == "d***@example.com"
    assert mask_value("123.456.789-10") == "***.***.***-**"
    assert mask_value("sk-testabcd") == "sk-...abcd"


def test_redact_regions_generates_different_image(tmp_path):
    source = tmp_path / "source.png"
    output = tmp_path / "redacted.png"
    img = Image.new("RGB", (40, 20), color=(255, 255, 255))
    for x in range(20):
        for y in range(20):
            img.putpixel((x, y), (0, 0, 0))
    img.save(source)

    report = redact_regions(source, [(16, 0, 8, 20)], output)

    assert Path(report.output_path).exists()
    assert output.read_bytes() != source.read_bytes()
