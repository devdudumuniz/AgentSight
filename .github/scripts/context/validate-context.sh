#!/usr/bin/env bash
set -euo pipefail

root="${1:-.}"
manifest="$root/.github/context/manifest.json"

if [[ ! -f "$manifest" ]]; then
  echo "Manifest ausente: .github/context/manifest.json" >&2
  exit 1
fi

python - "$root" <<'PY'
from __future__ import annotations

import json
import pathlib
import sys

root = pathlib.Path(sys.argv[1])
manifest_path = root / ".github/context/manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

required_files = {".github/context/manifest.json", *manifest.get("requiredFiles", [])}
missing = sorted(path for path in required_files if not (root / path).is_file())
if missing:
    raise SystemExit(f"Arquivos obrigatorios ausentes: {', '.join(missing)}")

required_dirs = set(manifest.get("requiredDirectories", []))
missing_dirs = sorted(path for path in required_dirs if not (root / path).is_dir())
if missing_dirs:
    raise SystemExit(f"Diretorios obrigatorios ausentes: {', '.join(missing_dirs)}")

agents = sorted((root / ".github").rglob("*.agent.md"))
if len(agents) != 1:
    raise SystemExit(f"Quantidade invalida de agentes *.agent.md: {len(agents)}. Esperado: 1.")

expected_agent = (root / ".github/agents/main.agent.md").resolve()
if agents[0].resolve() != expected_agent:
    raise SystemExit(f"Agente executavel inesperado: {agents[0]}")

current_path = root / manifest.get("currentPath", "")
if not current_path.is_dir():
    raise SystemExit(f"currentPath invalido no manifest: {manifest.get('currentPath')}")

if (root / ".github/context/archive/latest").exists():
    raise SystemExit("archive/latest e proibido. Use snapshots versionados.")

for hot_file in manifest.get("hotMemory", []):
    if not (root / hot_file).is_file():
        raise SystemExit(f"Hot memory ausente: {hot_file}")
PY

echo "VALIDATION_OK"
