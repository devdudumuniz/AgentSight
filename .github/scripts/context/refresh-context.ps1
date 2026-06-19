param(
  [string]$ContextPath = ".github/context",
  [string]$Version = "1.1.0"
)

$manifest = Join-Path $ContextPath "manifest.json"
$data = Get-Content $manifest -Raw | ConvertFrom-Json
$data.contextVersion = $Version
$data.lastUpdated = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
$data.currentPath = ".github/context/current"
$data.integrityStatus = "ACTIVE"

$data | ConvertTo-Json -Depth 10 | Set-Content $manifest -Encoding UTF8
Add-Content -Path (Join-Path $ContextPath "changelog.md") -Value "- refresh-context executado em $(Get-Date -Format yyyy-MM-dd)"

& ".github/scripts/context/validate-context.ps1" | Out-Null
