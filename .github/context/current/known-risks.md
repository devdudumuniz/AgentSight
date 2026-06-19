# Riscos conhecidos

## Produto e seguranca

- Captura visual pode expor dados sensiveis se usada fora das politicas de consentimento, janela/regiao e redaction.
- Redaction automatica ainda nao esta acoplada ao fluxo principal de `capture`.
- OCR e classificacao visual sensivel ainda sao opcionais/futuros.
- Retencao/cleanup ainda nao esta implementada como comando operacional do CLI.

## Runtime

- `capture.py` usa fallback explicito `placeholder` quando nao ha display real. Isso evita falha silenciosa em ambiente headless, mas a evidencia nao deve ser tratada como captura real.
- Captura por `window_title` sem regiao explicita ainda levanta `NotImplementedError`.
- Adapter Playwright atual e experimental/minimo.

## Governanca

- Contexto pode ficar defasado se alteracoes de codigo nao atualizarem `manifest.json`, `changelog.md` e relatorios.
- Snapshots devem permanecer historicos; qualquer uso como fonte ativa e regressao de governanca.
