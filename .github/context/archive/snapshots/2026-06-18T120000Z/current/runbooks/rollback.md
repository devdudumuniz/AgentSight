# Runbook: Rollback

## Quando usar
- Falha funcional em validação crítica.
- Regresso detectado por decisão de produto/segurança.

## Procedimento
1. Marcar status em `reports/last-validation.md` como `REGRESSION_DETECTED`.
2. Reapontar para snapshot anterior em `.github/context/archive/snapshots/<timestamp>/`.
3. Reaplicar mudanças apenas após validação revisada.

