from advanced_screenshot_agent.redact import detect_sensitive_text


def test_detect_sensitive_email_and_cpf():
    hits = detect_sensitive_text("cliente teste@email.com cpf 123.456.789-10")
    kinds = {hit.kind for hit in hits}
    assert "email" in kinds
    assert "cpf" in kinds
