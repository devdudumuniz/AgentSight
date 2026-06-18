#!/usr/bin/env bash
set -euo pipefail

TIMESTAMP="${1:-$(date -u +%Y%m%dT%H%M%SZ)}"
SRC="${2:-.github/context/current}"
ARCHIVE="${3:-.github/context/archive/snapshots}"
TARGET="$ARCHIVE/$TIMESTAMP"

mkdir -p "$TARGET"
cp -r "$SRC" "$TARGET/current"
cp .github/context/manifest.json "$TARGET/"
echo "SNAPSHOT_CREATED $TARGET"

