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

### 2026-05-01 — Tesis MVP: "Peerspace para Perú, mobile-first, Yape/Plin nativos, verificación humana"
- **Contexto**: research completo en `analisis-mercado/`. Space-Pal Lima tiene catálogo prácticamente vacío; competencia real es informal (IG + grupos FB + WhatsApp + Yape).
- **Decisión**: 3 pilares de diferenciación → (1) pago 100% local (Yape/Plin/Culqi + factura SUNAT), (2) curaduría humana con visita presencial, (3) WhatsApp-first para notificaciones y soporte.
- **Categorías de lanzamiento**: salones eventos sociales → estudios foto/video → salas reuniones corporativas (en ese orden).
- **Cobertura geográfica MVP**: 8 distritos de Lima Moderna (Miraflores, San Isidro, Barranco, Surco, San Borja, La Molina, Magdalena, Pueblo Libre).
- **Take-rate inicial**: 15% host + 5% guest = ~19% combinado (a validar con piloto).

### 2026-05-01 — Estrategia de supply: priorizar coworkings con horas muertas
- **Contexto**: hallazgo crítico del research — Comunal (100+ salas, 15 sedes), WeWork, Worx, Regus, Lima Coworking, Swiss Rents tienen inventario operativo vacío lun-jue AM.
- **Decisión**: outreach inicial a gerentes de coworking con KPI de ocupación, no a dueños de salones individuales (que es más lento y fragmentado).
- **Consecuencias**: cohorte cero podría llegar a 100+ salas en semanas, no meses. Ajustar `agents/host-onboarder.md` con plantilla específica para B2B coworking.
