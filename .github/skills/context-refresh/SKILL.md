# Skill: context-refresh

Use quando houver mudanca relevante de codigo, docs, gates ou roadmap que precise atualizar a memoria ativa.

## Entradas

- Objetivo da sessao.
- Arquivos alterados.
- Validacoes executadas.

## Fluxo

1. Ler hot memory.
2. Comparar contexto com estado real do repositorio.
3. Atualizar somente arquivos afetados em `.github/context/current/`.
4. Atualizar `.github/context/changelog.md`.
5. Atualizar `.github/reports/last-session.md`.
6. Rodar `.github/scripts/context/validate-context.ps1`.

## Saida

- Contexto ativo coerente com o codigo.
- Lacunas marcadas como `PARTIAL` ou `BLOCKED_BY_ENVIRONMENT` quando necessario.
