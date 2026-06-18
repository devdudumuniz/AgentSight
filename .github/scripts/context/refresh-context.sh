#!/usr/bin/env bash
set -euo pipefail

CONTEXT="${1:-.github/context}"
VERSION="${2:-1.0.0}"
MANIFEST="$CONTEXT/manifest.json"

ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
node -e "const fs=require('fs');const p='$MANIFEST';const m=JSON.parse(fs.readFileSync(p,'utf8'));m.contextVersion='$VERSION';m.lastUpdated='$ts';m.currentPath='.github/context/current';m.integrityStatus='ACTIVE';fs.writeFileSync(p,JSON.stringify(m,null,2));"
echo "- refresh-context executado em $ts" >> "$CONTEXT/changelog.md"

