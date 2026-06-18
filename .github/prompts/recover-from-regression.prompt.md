# Prompt: Recover from regression

Objetivo: conter regressão sem expandir escopo.

Passos:
1. Criar incidente em `decisions/` se decisão for recorrente.
2. Consultar `reports/last-validation.md` e `changelog.md`.
3. Executar `snapshot-context` para preservar estado pré-correção.
4. Corrigir menor caminho causal.
5. Atualizar `gates/regression-gates.md` e revalidar.
6. Registrar status `REGRESSION_DETECTED`/`READY_FOR_REVIEW`.

