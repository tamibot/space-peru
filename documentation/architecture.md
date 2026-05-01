# Architecture — Space-Peru

## Visión general (MVP)

```
[ Visitor / Mobile / Desktop ]
            │
            ▼
   GitHub Pages (CDN)
   ├── /            → landing/ (estático)
   └── /app/*       → app/ (SPA exportada)
            │
            ▼ (fetch JSON)
   Serverless / Railway API
            │
            ▼
   Railway PostgreSQL
```

## Componentes

### Landing (`landing/`)
- Estático puro. Sin SSR.
- Output: `landing/dist/` → push a `gh-pages` o branch dedicada.
- Captura email para waitlist → POST a una function (Cloudflare Workers / Vercel) que escribe a la PG.

### App (`app/`)
- Stack candidato: **Astro + islands** o **Next.js export estático**.
- Decisión final tras research (ver `backlog/decisiones.md`).
- Auth: Auth.js + Postgres adapter.
- API: rutas serverless.

### DB (`app/db/`)
- Railway PostgreSQL.
- Migraciones SQL puras versionadas en `app/db/migrations/`.
- Snapshot en `app/db/schema.sql`.

### Storage de imágenes
- Cloudflare R2 (sin egress fees).
- URLs firmadas para uploads de host.

## Entornos
- **dev**: local, contra una DB local o branch de Railway.
- **prod**: GitHub Pages + Railway PG.
- (Sin staging por ahora — promovemos vía PR a `main`.)

## Despliegue
- `main` → GitHub Action → build landing + app → push a `gh-pages`.
- Migraciones DB: manuales con `psql`, registradas en `app/db/migrations/`.

## Observabilidad (futuro)
- Plausible para analytics.
- Sentry free tier para errores.
- Logs de Railway para backend.

## Riesgos arquitectónicos
- **GitHub Pages tiene SSR limitado**: si SEO de listings sufre, migrar a Cloudflare Pages.
- **Railway tiene límites en plan free**: monitorear y migrar a Neon/Supabase si crece.
- **Sin colas de tareas**: si necesitamos jobs (envío de emails, notificaciones), agregar Cloudflare Queues o Trigger.dev.
