# Skill: context-audit

Use para auditar se `.github/` continua aderente ao contrato de contexto do projeto.

## Fluxo

1. Conferir existencia de um unico `.github/agents/main.agent.md`.
2. Validar hot, warm, cold memory e evidence layer.
3. Confirmar que `archive/` nao e fonte ativa.
4. Comparar `manifest.json` com a estrutura real.
5. Rodar validadores PowerShell e Bash quando possivel.

## Saida

- Lista de inconsistencias.
- Correcoes aplicadas ou plano de correcao.
- Evidencia dos gates.
