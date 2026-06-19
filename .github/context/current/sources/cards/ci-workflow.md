# Card de fonte: GitHub Actions CI

- titulo: Workflow CI
- tipo: Automacao
- localizacao: `.github/workflows/ci.yml`
- resumo executivo: Roda CI em push e pull request para codigo, tests, docs, README, pyproject e workflow.
- conceitos-chave: Python 3.12, pip cache, install `.[dev]`, ruff, pytest.
- pontos críticos: CI cobre lint e testes, mas nao executa build de pacote nem `validate-context`.
- riscos: mudancas em `.github/context/` nao disparam o workflow atual.
- relacao com o projeto: fonte primaria para gates remotos existentes.
- modulos afetados: QA, infra, package.
- limitacoes da fonte: nao cobre validacao visual real nem empacotamento.
- como o agente deve usar esta fonte: nao assumir gates remotos alem dos declarados.
