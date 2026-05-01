# Log de decisiones (ADR ligero)

Una entrada por decisión. Formato: fecha, contexto, decisión, alternativas, consecuencias.

---

### 2026-05-01 — Hosting MVP en GitHub Pages
- **Contexto**: necesitamos publicar landing y app sin infra costosa.
- **Decisión**: GitHub Pages para todo lo estático. APIs irán en serverless o Railway.
- **Alternativas**: Vercel, Cloudflare Pages, Netlify.
- **Consecuencias**: SSR limitado; necesitamos export estático o SPA. Bueno para landing, restrictivo para app real → revisitar antes de Fase 2.

### 2026-05-01 — DB en Railway (PostgreSQL)
- **Contexto**: el owner ya tiene una instancia activa.
- **Decisión**: usar la PG de Railway como DB principal del MVP.
- **Alternativas**: Supabase, Neon, PlanetScale.
- **Consecuencias**: vendor lock-in bajo (es Postgres puro). Migración a Supabase/Neon trivial si crece.

### 2026-05-01 — Branding azul minimalista
- **Contexto**: diferenciarse de Space-Pal (que tiene branding más cargado).
- **Decisión**: paleta dominantemente azul, alto contraste, mucho espacio en blanco.
- **Alternativas**: verde (cercano a Airbnb), naranja (energía).
- **Consecuencias**: tokens y guía visual a definir en `documentation/branding.md`.

### 2026-05-01 — Idioma producto: español Perú
- **Contexto**: foco inicial Lima.
- **Decisión**: ES-PE en producto, EN en código.
- **Consecuencias**: contenido y copy localizados desde día 1. i18n se considera post-MVP.

### 2026-05-01 — No automatizaciones sin pedirlo explícitamente
- **Contexto**: instrucción del owner.
- **Decisión**: Claude no propone /schedule, /loop, ni hooks proactivamente.
- **Consecuencias**: workflows recurrentes solo si el owner los solicita.
