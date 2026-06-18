# Prompt: Check gates

Objetivo: validar criticamente readiness de uma entrega.

Checklist:
- Estrutura:
  - `context/current` é fonte ativa
  - `archive` contém apenas histórico
  - Apenas `agents/main.agent.md` existe
- Conteúdo:
  - `manifest.json`
  - `changelog.md`
  - `reports/last-validation.md`
  - `decisions/ADR*`
- Operação:
  - `.github/scripts/context/validate-context` executado com sucesso
  - links e caminhos internos resolvem

