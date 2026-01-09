#!/bin/bash
set -euo pipefail

DUMP_DIR="/docker-entrypoint-initdb.d/dumps"

echo "Looking for dumps in ${DUMP_DIR}"

# Ensure the directory is present
if [[ ! -d "${DUMP_DIR}" ]]; then
  echo "No dump directory found at ${DUMP_DIR}; skipping restore."
  exit 0
fi

shopt -s nullglob
dump_files=("${DUMP_DIR}"/*.dump)

if [[ ${#dump_files[@]} -eq 0 ]]; then
  echo "No .dump files found; nothing to restore."
  exit 0
fi

for dump_file in "${dump_files[@]}"; do
  db_name="$(basename "${dump_file%.*}")"
  echo "Creating and restoring database: ${db_name}"

  if psql -U "${POSTGRES_USER}" -tAc "SELECT 1 FROM pg_database WHERE datname='${db_name}'" | grep -q 1; then
    echo "Database ${db_name} already exists; skipping restore."
    continue
  fi

  createdb -U "${POSTGRES_USER}" "${db_name}"
  pg_restore -U "${POSTGRES_USER}" -d "${db_name}" "${dump_file}"

  echo "Finished restoring ${db_name}"
done

echo "Database initialization complete."
