#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${CODEX_SKILLS_DIR:-$HOME/.codex/skills}"
TARGET="$TARGET_DIR/family-os"

mkdir -p "$TARGET_DIR"

if [ -e "$TARGET" ] || [ -L "$TARGET" ]; then
  echo "family-os already exists at $TARGET"
  echo "Remove it first or set CODEX_SKILLS_DIR to another directory."
  exit 1
fi

ln -s "$SCRIPT_DIR/skill" "$TARGET"
echo "Installed family-os skill at $TARGET"
