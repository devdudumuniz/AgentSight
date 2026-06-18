# .github da base de contexto e operação do projeto

Este diretório é a fonte canônica de memória operacional para **este projeto**.

## Estrutura ativa

- Fonte ativa: `.github/context/current/`
- Histórico imutável: `.github/context/archive/`
- Agente principal: `.github/agents/main.agent.md`
- Skills reutilizáveis: `.github/skills/`
- Prompts recorrentes: `.github/prompts/`
- Governança: `.github/roadmap/`, `.github/gates/`, `.github/reports/`, `.github/decisions/`
- Camada de fontes (estilo NotebookLM): `.github/context/current/sources/`

## Regras curtas

- Não criar código novo apenas para organização de docs.
- Toda decisão relevante de arquitetura deve ir para ADR em `.github/decisions/` ou `.github/context/current/decisions/`.
- `archive` é histórico congelado e não deve ser lido como estado atual.
- Qualquer atualização importante de contexto deve atualizar:
  - `.github/context/changelog.md`
  - `.github/reports/last-session.md`
  - `.github/reports/last-validation.md`

