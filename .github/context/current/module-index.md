# Módulos principais

## Pacote `advanced_screenshot_agent`
- `cli.py` — entrypoint de comando
- `capture.py` — fluxo principal de captura
- `policy.py` — validações de segurança
- `evidence.py` — registro de eventos
- `annotate.py` — anotação de regiões/labels
- `redact.py` — redaction por região
- `crypto.py` — cifragem básica de arquivos
- `adapters/playwright.py` — integração com Playwright

## Testes
- `tests/test_capture.py`
- `tests/test_policy.py`
- `tests/test_evidence.py`
- `tests/test_redact.py`

