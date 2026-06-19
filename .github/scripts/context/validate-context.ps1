param(
  [string]$Root = "."
)

$ErrorActionPreference = "Stop"

$manifestPath = Join-Path $Root ".github/context/manifest.json"
if (!(Test-Path -LiteralPath $manifestPath -PathType Leaf)) {
  Write-Error "Manifest ausente: .github/context/manifest.json"
  exit 1
}

$manifest = Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json

$missing = New-Object System.Collections.Generic.List[string]
$requiredFiles = @(".github/context/manifest.json") + @($manifest.requiredFiles)
foreach ($file in ($requiredFiles | Sort-Object -Unique)) {
  $path = Join-Path $Root $file
  if (!(Test-Path -LiteralPath $path -PathType Leaf)) {
    $missing.Add($file)
  }
}

$missingDirs = New-Object System.Collections.Generic.List[string]
foreach ($dir in @($manifest.requiredDirectories)) {
  $path = Join-Path $Root $dir
  if (!(Test-Path -LiteralPath $path -PathType Container)) {
    $missingDirs.Add($dir)
  }
}

if ($missing.Count -gt 0) {
  Write-Error "Arquivos obrigatorios ausentes: $($missing -join ', ')"
  exit 1
}

if ($missingDirs.Count -gt 0) {
  Write-Error "Diretorios obrigatorios ausentes: $($missingDirs -join ', ')"
  exit 1
}

$agentRoot = Join-Path $Root ".github"
$agentFiles = @(Get-ChildItem -LiteralPath $agentRoot -Filter "*.agent.md" -Recurse -File)
if ($agentFiles.Count -ne 1) {
  Write-Error "Quantidade invalida de agentes *.agent.md: $($agentFiles.Count). Esperado: 1."
  exit 1
}

$expectedAgent = (Resolve-Path -LiteralPath (Join-Path $Root ".github/agents/main.agent.md")).Path
if ($agentFiles[0].FullName -ne $expectedAgent) {
  Write-Error "Agente executavel inesperado: $($agentFiles[0].FullName)"
  exit 1
}

$currentPath = Join-Path $Root $manifest.currentPath
if (!(Test-Path -LiteralPath $currentPath -PathType Container)) {
  Write-Error "currentPath invalido no manifest: $($manifest.currentPath)"
  exit 1
}

if (Test-Path -LiteralPath (Join-Path $Root ".github/context/archive/latest")) {
  Write-Error "archive/latest e proibido. Use snapshots versionados."
  exit 1
}

foreach ($hotFile in @($manifest.hotMemory)) {
  if (!(Test-Path -LiteralPath (Join-Path $Root $hotFile) -PathType Leaf)) {
    Write-Error "Hot memory ausente: $hotFile"
    exit 1
  }
}

Write-Output "VALIDATION_OK"
exit 0
