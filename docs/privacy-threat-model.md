# Privacy Threat Model

## Ameaças

1. Captura acidental de dados sensíveis.
2. OCR persistindo segredo em memória textual.
3. Prompt injection visual dentro da screenshot.
4. Acesso de outro processo aos arquivos locais.
5. Agente realizando ação destrutiva após interpretar errado a UI.
6. Vazamento por relatório Markdown enviado ao PR.

## Controles

- Consentimento obrigatório.
- Fullscreen bloqueado por padrão.
- Redaction local antes de persistência.
- Criptografia opcional.
- TTL de retenção.
- Hash de evidência.
- Human approval para ações irreversíveis.
- Allowlist de janelas/domínios no roadmap.

## Política recomendada para empresas

- Captura apenas de janela/região autorizada.
- Proibição de tela de banco, senha, token, chat privado e documentos sensíveis.
- Logs sem imagem bruta por padrão.
- Relatórios com thumbnails redigidas.
- Storage local criptografado.
