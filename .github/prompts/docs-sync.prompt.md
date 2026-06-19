# Docs Sync Prompt

Use para sincronizar documentacao, contexto e relatorios com o estado real do repositorio.

## Entrada

- Objetivo da sincronizacao.
- Arquivos ou modulos alterados.
- Validacoes executadas.

## Processo

1. Leia hot memory.
2. Compare README, docs, codigo, testes e workflow.
3. Identifique afirmacoes obsoletas ou sem evidencia.
4. Atualize `.github/context/current/`, `docs/` e reports somente onde houver fato confirmado.
5. Rode `validate-context`.

## Saida

- Arquivos atualizados.
- Fontes consultadas.
- Gates executados.
- Pendencias com status oficial.
