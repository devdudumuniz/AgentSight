# Regression watchlist

## Regras que nao podem regredir

- Nao permitir fullscreen por padrao.
- Nao capturar sem consentimento quando `require_user_consent=True`.
- Nao criar placeholder automatico quando captura real falhar.
- Nao permitir mock sem flag explicita `--mock`.
- Nao remover metadata com `sha256` e `timestamp_utc`.
- Nao remover schema `agentsight.capture.v1`.
- Nao criar mais de um `*.agent.md` executavel.
- Nao usar `.github/context/archive/` como fonte ativa.
- Nao deixar `validate-context` passar com hot memory incompleta.

## Gates associados

- `.github/scripts/context/validate-context.ps1`
- `.github/scripts/context/validate-context.sh`
- `ruff check .`
- `python -m pytest`
- `python -m build`
- `python -m agentsight.cli --help`
- `agentsight --help`
- `agentsight doctor`
