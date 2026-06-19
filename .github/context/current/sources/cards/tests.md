# Card de fonte: tests

- titulo: Testes automatizados
- tipo: Testes
- localizacao: `tests/`
- resumo executivo: Testes unitarios cobrem policy gate, capture, evidence e redaction.
- conceitos-chave: bloqueio de fullscreen, consentimento, janela sensivel, metadata, hash, blur/redaction.
- pontos críticos: testes passam com `python -m pytest`.
- riscos: nao substituem validacao visual em desktop real.
- relacao com o projeto: fonte primaria para regressões ja protegidas.
- modulos afetados: capture, policy, redaction, evidence.
- limitacoes da fonte: nao cobre Playwright completo, OCR ou cleanup de retencao.
- como o agente deve usar esta fonte: conferir testes existentes antes de criar novos gates.
