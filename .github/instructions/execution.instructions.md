# Instrucoes de execucao

## Antes de alterar

- Verificar `git status --short --branch`.
- Identificar stack, scripts, testes e CI.
- Ler os arquivos de contexto relevantes.
- Definir risco e rollback.

## Durante a execucao

- Fazer a menor mudanca segura.
- Preservar contratos existentes.
- Nao criar mock ou stub para fingir funcionamento real.
- Nao tocar arquivos nao relacionados.

## Depois

- Rodar gates aplicaveis.
- Atualizar changelog e reports.
- Revisar diff antes de commit.
