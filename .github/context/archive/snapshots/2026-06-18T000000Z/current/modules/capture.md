# Módulo: capture

## O que faz
Captura imagem e gera metadados (`label`, `sha256`, `timestamp`, `path`, backend usado).

## Entrada principal
- `advanced_screenshot_agent.capture.capture_screen`

## Dependências
- `PIL`, `mss`

## Regras e riscos
- Validação via `CapturePolicy` antes de capturar.
- Em ambiente sem display, usa placeholder para manter robustez de execução.
- Falta de redaction automática no fluxo atual por padrão (`capture` apenas gera imagem + metadata).

