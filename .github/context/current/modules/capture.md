# Módulo: capture

## O que faz
Captura imagem, aplica redaction regional quando informada e gera metadados (`label`, `sha256`, `timestamp`, `path`, backend usado, redaction aplicada).

## Entrada principal
- `advanced_screenshot_agent.capture.capture_screen`

## Dependências
- `PIL`, `mss`

## Regras e riscos
- Validação via `CapturePolicy` antes de capturar.
- Em ambiente sem display, usa placeholder para manter robustez de execução.
- Redaction por regiões é aplicada em memória antes de salvar quando `redaction_regions` é informado.
- OCR/redaction automática por conteúdo ainda não faz parte do fluxo padrão.
