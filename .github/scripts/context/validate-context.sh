#!/usr/bin/env bash
set -euo pipefail

required=(
  ".github/context/manifest.json"
  ".github/context/changelog.md"
  ".github/agents/main.agent.md"
  ".github/skills/README.md"
  ".github/prompts/README.md"
  ".github/context/current/sources/README.md"
  ".github/context/current/dependency-map.md"
  ".github/context/current/operations-map.md"
  ".github/context/current/project-brief.md"
  ".github/context/current/architecture-map.md"
  ".github/context/current/module-index.md"
  ".github/context/current/entrypoints.md"
)

for f in "${required[@]}"; do
  if [[ ! -f "$f" ]]; then
    echo "FALTANDO: $f" >&2
    exit 1
  fi
done

count=$(find .github -name "*.agent.md" | wc -l | tr -d ' ')
if [[ "$count" -gt 1 ]]; then
  echo "MAIS DE UM .agent.md encontrado" >&2
  exit 1
fi

echo "VALIDATION_OK"

