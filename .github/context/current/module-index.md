# Módulos principais

## Pacote `agentsight`
- `cli.py` — entrypoint de comando
- `capture.py` — fluxo principal de captura
- `policy.py` — validações de segurança
- `evidence.py` — registro de eventos
- `report.py` — relatorio Markdown
- `cleanup.py` — retencao/limpeza de imagens
- `annotate.py` — anotação de regiões/labels
- `redact.py` — redaction por região
- `crypto.py` — cifragem básica de arquivos
- `adapters/mss_capture.py` — captura real por mss
- `adapters/playwright.py` — integração com Playwright
- `advanced_screenshot_agent/` — shim legado sem logica duplicada

## Testes
- `tests/test_capture.py`
- `tests/test_policy.py`
- `tests/test_evidence.py`
- `tests/test_redact.py`
- `tests/test_annotate.py`
- `tests/test_playwright.py`
