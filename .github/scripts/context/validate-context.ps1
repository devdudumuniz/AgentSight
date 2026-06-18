param(
  [string]$Root = "."
)

$requiredFiles = @(
  ".github/context/manifest.json",
  ".github/context/changelog.md",
  ".github/agents/main.agent.md",
  ".github/skills/README.md",
  ".github/prompts/README.md",
  ".github/context/current/sources/README.md",
  ".github/context/current/dependency-map.md",
  ".github/context/current/operations-map.md",
  ".github/context/current/project-brief.md",
  ".github/context/current/architecture-map.md",
  ".github/context/current/module-index.md",
  ".github/context/current/entrypoints.md"
)

$missing = @()
foreach ($f in $requiredFiles) {
  if (!(Test-Path (Join-Path $Root $f))) { $missing += $f }
}

if ($missing.Count -gt 0) {
  Write-Error "Arquivos obrigatórios ausentes: $($missing -join ', ')"
  exit 1
}

$agentFiles = Get-ChildItem -Path $Root\.github -Filter "*.agent.md" -Recurse
if ($agentFiles.Count -gt 1) {
  Write-Error "Mais de um agente *.agent.md encontrado."
  exit 1
}

Write-Output "VALIDATION_OK"
exit 0

