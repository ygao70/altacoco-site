#!/bin/bash
# Resizes every .jpg/.jpeg/.png in this folder to max 2000px on the long edge and
# re-saves JPEGs at quality 82. macOS only (uses the built-in `sips`). Originals are overwritten.
cd "$(dirname "$0")"
for f in *.jpg *.jpeg *.png; do
  [ -e "$f" ] || continue
  sips -Z 2000 "$f" >/dev/null
  case "$f" in *.jpg|*.jpeg) sips -s format jpeg -s formatOptions 82 "$f" --out "$f" >/dev/null ;; esac
  echo "optimized $f"
done
