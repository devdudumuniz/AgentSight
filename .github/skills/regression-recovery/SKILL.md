# Skill: regression-recovery

Use quando uma regressao real ou suspeita aparecer em codigo, contexto, docs ou gates.

## Fluxo

1. Identificar comportamento esperado e comportamento atual.
2. Localizar primeira fonte confiavel do contrato.
3. Corrigir a menor superficie possivel.
4. Adicionar ou atualizar teste/gate quando aplicavel.
5. Registrar em `.github/context/current/regression-watchlist.md`.
6. Atualizar `last-validation.md`.

## Criterio de saida

- Regressao corrigida ou marcada como `FAILED_VALIDATION`, `REGRESSION_DETECTED` ou `BLOCKED_BY_ENVIRONMENT`.
