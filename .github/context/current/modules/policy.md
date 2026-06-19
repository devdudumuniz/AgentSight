# Módulo: policy

## O que faz
Valida se uma solicitação de captura é permitida.

## Entrada principal
- `CapturePolicy.validate_capture_request`

## Regras codificadas
- Consentimento explícito obrigatório.
- Bloqueio fullscreen por padrão.
- Bloqueio de palavras sensíveis no título de janela.
- Validação básica de região.

## Pontos a evoluir
- Persistência de política por perfil/workspace.
- Allowlist de processo/domínio operacional mais granular.
