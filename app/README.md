# App

Producto principal de Planea Ya.

## Estructura
```
app/
  frontend/    # SPA / Astro / Next export
  backend/     # serverless functions / API
  db/          # migraciones, schema, seeds
  docs/        # docs específicas del producto
  README.md
```

## Stack (decidir tras research)
- **Frontend candidato**: Astro + islands (estático) o Next.js export.
- **Backend candidato**: Cloudflare Workers o Vercel functions o pequeño servicio Node en Railway.
- **DB**: PostgreSQL en Railway (`DATABASE_URL`).
- **Auth**: Auth.js + Postgres adapter.
- **Storage**: Cloudflare R2.

## Modelo de datos (preliminar)
- `users` (host y guest unificados, role en columna)
- `spaces` (un host puede tener N espacios)
- `space_photos`
- `space_amenities` (M:N con `equipamiento.json`)
- `availability_rules` (días/horas que el host habilita)
- `bookings`
- `reviews` (1:1 con bookings completados)
- `payments`
- `payouts` (al host)

## Variables de entorno
Ver `credentials.env` raíz. La app lee desde ahí en local; en producción se inyectan en el host (Railway/Vercel/Cloudflare).
