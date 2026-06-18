# Runbook: Troubleshooting

## Falha comum: CI com erro de caminho
- Sintoma: workflow falha por `working-directory` inexistente.
- Ação: validar e corrigir `ci.yml` para raiz atual.

## Falha comum: captura bloqueada por política
- Sintoma: `PermissionError` por fullscreen/consentimento.
- Ação: revisar parâmetros de CLI e política em `policy.py`.

## Falha comum: validação parcial
- Atualizar `reports/last-validation.md` com motivo real e classificar status.

