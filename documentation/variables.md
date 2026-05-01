# Variables y credenciales — catálogo

> **Mantenido por**: agente `librarian`.
> **Valores reales**: `credentials.env` (gitignored).
> **Plantilla pública**: `.env.example`.

Cada variable tiene una entrada acá. Si una variable existe en `credentials.env` pero no acá, falló el flujo de `librarian` y debe arreglarse.

---

## Activas

### `DATABASE_URL`
- **Servicio**: Railway PostgreSQL
- **Tipo**: connection string (postgres URL)
- **Quién lo usa**: `scripts/test_db.py`, futuras migraciones en `app/db/migrations/`, backend serverless
- **Cómo se rota**: Dashboard Railway → Database → Settings → "Reset password". Nueva URL se actualiza acá y en cualquier deployment.
- **Última rotación**: 2026-05-01 (inicial)
- **Dueño**: owner

### `PGHOST`, `PGPORT`, `PGUSER`, `PGPASSWORD`, `PGDATABASE`
- **Servicio**: Railway PostgreSQL
- **Tipo**: componentes individuales del DSN
- **Quién lo usa**: clientes que no aceptan URL completa (psql, pg_dump)
- **Cómo se rota**: misma rotación que `DATABASE_URL` — derivar de la nueva URL.
- **Dueño**: owner

### `OWNER_EMAIL`
- **Servicio**: contacto público
- **Tipo**: email
- **Valor**: `info@proper.com.pe`
- **Quién lo usa**: footer landing, mailto en docs, sender de futuros emails transaccionales
- **Cómo se rota**: cambiar en `credentials.env` y propagar.
- **Dueño**: owner

---

## Reservadas (placeholder, sin valor aún)

### `GH_USER`
- **Servicio**: GitHub
- **Tipo**: username
- **Pendiente**: confirmar usuario para crear el repo. (Detectado vía `gh auth status`: `tamibot`. Confirmar con owner.)

### `GH_REPO`
- **Servicio**: GitHub
- **Valor por defecto**: `space-peru`
- **Quién lo usa**: scripts de deploy, GitHub Action.

### `GH_PAGES_URL`
- **Servicio**: GitHub Pages
- **Pendiente**: rellenar tras primer deploy.

### `ANTHROPIC_API_KEY`
- **Servicio**: Anthropic Claude API
- **Tipo**: API key
- **Cuándo se necesita**: si se integra Claude en producto (recomendaciones, soporte AI).
- **Cómo se obtiene**: console.anthropic.com → Keys.

### `GOOGLE_MAPS_API_KEY` / `MAPBOX_TOKEN`
- **Servicio**: mapas en producto
- **Decisión pendiente**: Mapbox por costo (`backlog/decisiones.md`).
- **Cómo se obtiene**: account.mapbox.com.

### `RESEND_API_KEY`
- **Servicio**: emails transaccionales
- **Cuándo se necesita**: Fase 1+ (waitlist, confirmaciones).
- **Cómo se obtiene**: resend.com/api-keys.

### `STRIPE_SECRET_KEY`
- **Servicio**: pagos internacionales (probable que NO se use, dejado como opción).

### `CULQI_PRIVATE_KEY`
- **Servicio**: pagos Perú (tarjetas)
- **Cuándo se necesita**: Fase 3 (booking real).
- **Cómo se obtiene**: panel.culqi.com.

### `MERCADOPAGO_ACCESS_TOKEN`
- **Servicio**: pagos Perú alternativo
- **Cuándo se necesita**: Fase 3.
- **Cómo se obtiene**: developers.mercadopago.com.

---

## DEPRECATED

(ninguna por ahora)

---

## Checklist al agregar una variable nueva

- [ ] Valor real → `credentials.env`
- [ ] Placeholder → `.env.example`
- [ ] Documentar acá (servicio, tipo, uso, rotación, dueño)
- [ ] Verificar que `credentials.env` siga gitignored: `git check-ignore credentials.env`
- [ ] Correr escaneo pre-commit del agente `librarian`
