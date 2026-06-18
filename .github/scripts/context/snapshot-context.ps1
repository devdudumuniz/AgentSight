param(
  [string]$Timestamp = (Get-Date -Format "yyyyMMddTHHmmssZ"),
  [string]$SourcePath = ".github/context/current",
  [string]$ArchiveRoot = ".github/context/archive/snapshots"
)

$target = Join-Path $ArchiveRoot $Timestamp
New-Item -ItemType Directory -Force $target | Out-Null

Copy-Item -Path $SourcePath -Destination (Join-Path $target "current") -Recurse -Force
Copy-Item -Path ".github/context/manifest.json" -Destination $target -Force
Write-Output "SNAPSHOT_CREATED $target"

