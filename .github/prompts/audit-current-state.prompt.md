# Prompt: Auditar estado atual

Objetivo: validar a saúde da base sem tomar ações destrutivas.

Use este prompt quando:
- houver dúvida do estado de entrada,
- início de sessão de diagnóstico,
- antes de grande refactor.

Passos:
1. Ler `manifest.json`.
2. Executar `git status --short --branch`.
3. Revisar `.github/context/changelog.md` e `last-session.md`.
4. Rodar `.github/scripts/context/validate-context.ps1` (ou `.sh`).
5. Reportar divergências e status com evidência objetiva.

