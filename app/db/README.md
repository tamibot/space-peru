# DB — Railway PostgreSQL

## Conexión

```bash
set -a && source ../../credentials.env && set +a
psql "$DATABASE_URL"
```

## Migraciones
- Cada cambio de schema → archivo nuevo en `migrations/` con prefijo numérico (`0001_init.sql`, `0002_add_spaces.sql`).
- Forward-only.
- Aplicar con: `psql "$DATABASE_URL" -f migrations/<file>.sql`.

## Snapshot
```bash
pg_dump --schema-only "$DATABASE_URL" > schema.sql
```

## Seeds
- `seed/categorias.sql` — desde `data/public/categorias.json`
- `seed/distritos.sql` — desde `data/public/distritos-lima.json`
- `seed/equipamiento.sql` — desde `data/public/equipamiento.json`

## Reglas
- Confirmar con owner antes de cualquier `DROP` en producción.
- Backups antes de cambios destructivos.
- Probar contra DB local antes de aplicar a Railway.
