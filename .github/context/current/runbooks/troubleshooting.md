# Runbook: Troubleshooting

## Falha comum: CI falhando
- Sintoma: workflow falha em lint, testes, build ou smoke do CLI.
- Acao: validar `.github/workflows/ci.yml`, matriz Python e instalacao `.[dev,capture]`.

## Falha comum: captura bloqueada por politica
- Sintoma: `PermissionError` por fullscreen/consentimento.
- Acao: revisar parametros de CLI e politica em `agentsight/policy.py`.

## Falha comum: validação parcial
- Atualizar `reports/last-validation.md` com motivo real e classificar status.
