# Research Notes

## Estado atual

Claude Computer Use oferece screenshot, mouse, teclado e desktop automation, mas recomenda isolamento por VM/container, allowlist de domínios e confirmação humana para ações sensíveis.

OpenAI Computer Use usa loop em que o modelo vê screenshot, retorna ações, o harness executa e devolve nova screenshot. Isso é forte, mas depende muito da qualidade do ambiente e do controle de segurança.

Playwright já resolve bem captura web: `page.screenshot`, full page, buffer e screenshot por elemento.

Skills comunitárias mostram o valor de:
- Captura antes/depois de ações.
- Anotação visual.
- Relatórios Markdown.
- Integração com Claude/Codex/Cursor.

## Nossa evolução

O salto real é construir a ferramenta como “Vision Runtime” governado:

- Escopo mínimo.
- Evidência auditável.
- Redaction local.
- Hashes.
- Retenção.
- Saída estruturada.
- Adapters por ambiente.
- Benchmarks próprios de click accuracy, privacy leak rate e visual regression detection.
