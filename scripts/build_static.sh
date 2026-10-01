#!/bin/sh
# Publica únicamente los archivos web del repositorio, nunca docs ni secretos.
set -eu
cd "$(dirname "$0")/.."
destination="${1:-/private/tmp/coordina-eventos-site}"
case "$destination" in /*) ;; *) echo 'Usar un destino absoluto' >&2; exit 1 ;; esac
mkdir -p "$destination/app" "$destination/brand/logo" "$destination/data/public"
cp landing/src/index.html landing/src/styles.css landing/src/app.js "$destination/"
cp -R app/web/. "$destination/app/"
cp brand/logo/*.svg "$destination/brand/logo/"
cp -R data/public/. "$destination/data/public/"
printf 'ok\n' > "$destination/healthz.txt"
printf 'Fuente: tamibot/space-peru\n' > "$destination/version.txt"
