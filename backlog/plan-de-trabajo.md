# Plan de trabajo Space-Peru

> **Estado**: aprobado por owner el 2026-05-01.
> **Ajuste vigente**: Fase 1 NO incluye entrevistas ni validación SUNAT. Foco: análisis de mercado completo (qué existe, cómo se resuelve hoy, listado de empresas locales e internacionales).

6 fases secuenciales con dependencias. Cada una tiene objetivo, entregables, agentes/skills, decisiones del owner, criterio de cierre y estimado.

---

## Fase 1 — Análisis de mercado completo

**Objetivo:** entender en general qué hay actualmente en el mercado, cómo se resuelve hoy el problema, qué empresas existen (locales + internacionales) y qué oportunidad real queda. Salir con una **foto clara del estado del arte**, no con investigación de campo.

**Lo que NO entra en esta fase** (por decisión explícita del owner):
- ❌ Entrevistas a hosts/buyers
- ❌ Validación SUNAT / empresas activas
- ❌ Scraping intensivo de contactos
- ❌ Profundizar en willingness to pay con data primaria

**Entregables**
- `analisis-mercado/01-resumen-ejecutivo.md` — ya existe, validar y refrescar.
- `analisis-mercado/competidores/space-pal.md` — análisis profundo (referente de origen de la idea). Ya existe; complementar con scraping ético del catálogo público.
- `analisis-mercado/competidores/internacionales.md` — Peerspace, Splacer, Tagvenue, Storefront, ShareDesk, Breather, This Open Space. Ya existe; revisar y completar.
- `analisis-mercado/competidores/otros-peru.md` — Comparto Espacios, Ineventos, marketplaces de coworking (Comunal, WeWork, Worx, Regus, Lima Coworking, Swiss Rents), Mercado Libre, grupos Facebook activos. Ya existe; refresco.
- `analisis-mercado/04-mapa-de-soluciones.md` — **NUEVO**: mapa visual de cómo se resuelve hoy el problema. 4 columnas: (1) descubrimiento, (2) reserva, (3) pago, (4) post-uso. Por cada columna: qué herramienta usa la gente hoy.
- `analisis-mercado/05-empresas-listadas.md` — **NUEVO**: tabla maestra única con todas las empresas/plataformas que tocan el problema. Columnas: nombre, país, modelo, categorías, fortalezas, debilidades, URL.
- `analisis-mercado/06-conclusion-mercado.md` — **NUEVO**: 1–2 páginas que respondan "¿qué hay, qué falta, dónde podemos jugar?" — base para Fase 2.

**Agentes/skills**
- `orchestrator` (coordina), `market-researcher` (background), `reviewer` (cierra)
- Skills: `customer-research` (21K), `extract-design-system` (analizar branding de Space-Pal y referentes), `find-skills` (si surge necesidad nueva)
- Tools: WebFetch, WebSearch, Chrome MCP si se necesita scraping autenticado

**Decisiones que tomas tú**
- Aprobar el listado final de empresas a analizar (mi propuesta inicial, tú agregas/quitas).
- Confirmar que el alcance "general" es suficiente o si quieres profundizar en alguna empresa específica.

**Criterio de cierre**
- 6 documentos aprobados por `reviewer`.
- Tabla maestra con ≥20 empresas listadas (locales + internacionales).
- Mapa de soluciones cubre 4 columnas con ≥3 herramientas cada una.
- 0 marcadores `[a validar]` en los 3 documentos NUEVOS (los anteriores pueden quedar con flags).

**Estimado:** 3–4 días.

---

## Fase 2 — Definir oferta, público y scope del MVP

**Objetivo:** convertir hallazgos de Fase 1 en un PRD del MVP con scope estrecho y métricas de éxito.

**Entregables**
- `app/docs/lean-canvas.md` — Lean Canvas completo (problema, segmentos, propuesta única, solución, canales, ingresos, costos, métricas, ventaja).
- `app/docs/prd-mvp.md` — Product Requirements Document:
  - Vertical único del MVP (recomendación tentativa: salones eventos sociales en Lima Moderna).
  - 2 personas focales (1 host, 1 buyer) detalladas.
  - User stories priorizadas (MoSCoW).
  - Out-of-scope explícito.
  - Métricas de éxito (north star + 3 KPIs).
- `app/docs/journey-maps.md` — flujo guest (descubrir → reservar → pagar → usar → reseñar) y host (postular → verificar → publicar → recibir → cobrar).
- `app/docs/financial-model.md` — modelo financiero MVP (unit economics, take-rate, costos fijos/variables, runway 12 meses).
- `backlog/decisiones.md` actualizado con ADRs: vertical de lanzamiento, scope MVP, take-rate confirmado.

**Agentes/skills**
- `orchestrator` (lidera), `reviewer` (audita PRD)
- Skills: `lean-canvas`, `business-model`, `startup-metrics-framework`, `startup-financial-modeling`, `product-management:write-spec`, `product-management:product-brainstorming`

**Decisiones que tomas tú** (críticas)
- **Vertical único de lanzamiento** (recomendación: salones eventos sociales).
- **Take-rate final** (recomendado: 15% host + 5% guest, 0% host primeros 6 meses).
- **Cohorte cero**: coworkings vs hosts individuales (research sugiere coworkings).
- **Métrica principal del MVP**: reservas pagadas/mes vs GMV vs # hosts activos.

**Criterio de cierre**
- PRD aprobado y firmado por owner.
- Lean Canvas en 1 página.
- Backlog dividido en P0 (MVP) y P1+ (post-MVP) con ETA.

**Estimado:** 3–4 días.

---

## Fase 3 — Concepto de marca e identidad

**Objetivo:** cerrar la marca antes de invertir en landing y producto.

**Entregables**
- `brand/identity/posicionamiento.md` validado.
- `brand/messaging/taglines.md` — tagline final elegida.
- `brand/logo/` — wordmark + isotipo + favicons + OG image (SVG/PNG).
- `documentation/branding.md` — tokens validados (hex, tipos, spacing finales).
- `brand/identity/moodboard.md` — estética visual de referencia.
- `brand/assets/templates/` — plantillas IG carrusel, LinkedIn, OG.

**Agentes/skills**
- Skills: `brand-guidelines`, `extract-design-system`, `web-design-guidelines`, `space-branding`.
- Externos: si el wordmark se hace en Figma, el owner o un diseñador. Yo entrego specs y mockups en SVG código.

**Decisiones que tomas tú**
- Tagline final (favorita actual: "Reserva claro. Llega tranquilo.").
- Wordmark: tipográfico puro o con isotipo.
- Paleta: confirmar `--blue-600` (#2563EB) o variante.
- Tono fotográfico: real vs ilustrado.

**Criterio de cierre**
- Logo en 5 versiones commiteado.
- Tokens aplicados en mockups (landing + slide pitch).
- Aprobación owner firmada.

**Estimado:** 1 semana (depende de iteración de diseño).

---

## Fase 4 — Landing page v1

**Objetivo:** landing pública en GitHub Pages con waitlist real, captura a Postgres, analytics privacy-first.

**Entregables**
- `landing/src/` — landing v1 con branding final, copy es-PE, 7 secciones.
- `app/db/migrations/0001_init.sql` — schema mínimo waitlist.
- `app/backend/api-waitlist.ts` — Cloudflare Worker o Vercel Function que graba en PG.
- Plausible analytics activado.
- Dominio `space-peru.com` apuntando a GitHub Pages.
- `social/calendar.md` — primeros 5 posts pre-anuncio listos.

**Agentes/skills**
- `landing-builder`, `db-migrator`, `librarian`, `reviewer`.
- Skills: `landing-page-design`, `web-design-guidelines`, `space-copy-pe`, `postgresql-table-design`.

**Decisiones que tomas tú**
- Dominio: comprar `space-peru.com` (~US$10/año) y `.pe` opcional.
- Email transaccional: Resend (recomendado) vs Postmark vs SES.
- Analítica: Plausible (US$9/mes) vs Umami self-host vs nada.
- CTA principal hero.

**Criterio de cierre**
- Lighthouse 95+ en perf/a11y/SEO en mobile.
- Waitlist funcional E2E.
- 50+ signups orgánicos en primera semana de soft-launch.

**Estimado:** 2 semanas.

---

## Fase 5 — Arquitectura técnica + app v1

### 5.A — Arquitectura (1 semana)
**Entregables**
- `documentation/architecture.md` con stack final.
- `documentation/db-schema.md` — schema completo MVP.
- ADRs: stack frontend, auth, storage imágenes, pagos.

### 5.B — App MVP (4–6 semanas)
**Entregables**
- Schema migrado a Railway.
- Listado público de espacios (sin booking).
- Onboarding de host.
- Búsqueda por distrito y categoría.
- Backoffice mínimo para aprobar.
- Booking real con Culqi + Yape manual.
- Confirmación email + WhatsApp Business API.
- Reseñas post-booking.

**Agentes/skills**
- `db-migrator`, `landing-builder`, `reviewer`.
- Skills: `engineering:architecture`, `engineering:system-design`, `postgresql-table-design`, `claude-api`, `data:sql-queries`.
- MCPs: Supabase / Neon (si migramos), Stripe / Culqi.

**Decisiones que tomas tú**
- Stack frontend (Astro vs Next.js export vs Cloudflare full SSR).
- Auth (Auth.js vs Clerk vs Supabase Auth).
- Migrar DB de Railway a Supabase/Neon ahora o después.
- Pagos (Culqi recomendado vs Niubiz vs MercadoPago).
- WhatsApp (Meta Cloud API vs Twilio).

**Criterio de cierre**
- 5.A: 5 ADRs aprobados, schema completo.
- 5.B: 1 booking real end-to-end (host real → guest real → pago → reseña).

**Estimado:** A: 1 semana. B: 4–6 semanas.

---

## Fase 6 — Comunicación, contenido y crecimiento

**Objetivo:** activar canales para volumen de waitlist → conversión a primeros usuarios.

**Entregables**
- `social/` — primer mes de calendario con posts redactados.
- `brand/pitch-deck/` — 3 versiones .pptx (host pitch, investor, press kit).
- Outreach kit B2B coworking.
- `social/casos/` — 3 mini casos.
- SEO: páginas por distrito × categoría.
- Programa de referidos host y guest.

**Agentes/skills**
- `content-creator`, `host-onboarder`, `reviewer`.
- Skills: `marketing:draft-content`, `marketing:campaign-plan`, `marketing:seo-audit`, `marketing:email-sequence`, `space-copy-pe`.

**Decisiones que tomas tú**
- Si pagas ads desde Fase 6 o solo orgánico.
- Presupuesto outreach.
- Vocero público.

**Criterio de cierre**
- 10 hosts activos publicados.
- Primera reserva pagada externa al círculo cercano.
- 500+ signups o follower base.

**Estimado:** continuo, primeros 30 días intensivos en paralelo a Fase 5.B.

---

## Visión global

```
Fase 1 ─→ Fase 2 ─→ Fase 3 ─→ Fase 4 ──┬──→ Fase 5.A ─→ Fase 5.B
mercado    PRD MVP    marca    landing │
                                       └──→ Fase 6 (paralelo desde Fase 4)
                                              contenido + outreach
```

| Fase | Estimado | Dependencia | Bloquea |
|---|---|---|---|
| 1. Mercado | 3–4 días | — | 2, 3 |
| 2. PRD MVP | 3–4 días | 1 | 3, 4, 5 |
| 3. Marca | 1 sem | 1, 2 | 4 |
| 4. Landing | 2 sem | 3 | 6 (parcial) |
| 5.A. Arquitectura | 1 sem | 2 | 5.B |
| 5.B. App | 4–6 sem | 5.A | producción |
| 6. Contenido | continuo | 3, 4 | crecimiento |

**Total a "primer booking real":** ~9–11 semanas en serie, ~7–8 semanas con paralelización 5↔6.

---

## Decisiones críticas (ordenadas por urgencia)

1. **Vertical único del MVP** (Fase 2) — todo cuelga de esto.
2. **Tagline y wordmark final** (Fase 3).
3. **Dominio + analítica + email** (Fase 4).
4. **Stack frontend + auth + pagos** (Fase 5.A).
5. **Vocero / presencia pública** (Fase 6).

---

## Estado actual
- ✅ Fase 0 completada (estructura repo, DB Railway, agentes, skills, brand inicial).
- ⏳ Fase 1 — lista para arrancar.
- ⏳ Fases 2–6 — pendientes.

## Skills disponibles para el plan
14 skills activas (10 externas + find-skills + 3 locales). Ver `skills/README.md`.

Skills clave por fase:
- **Fase 1**: `customer-research`, `extract-design-system`, `find-skills`
- **Fase 2**: `lean-canvas`, `business-model`, `startup-metrics-framework`, `startup-financial-modeling`
- **Fase 3**: `brand-guidelines`, `space-branding`, `extract-design-system`
- **Fase 4**: `landing-page-design`, `web-design-guidelines`, `space-copy-pe`, `postgresql-table-design`
- **Fase 5**: `postgresql-table-design`, `claude-api`, `engineering:*` (oficiales)
- **Fase 6**: `marketing:*` (oficiales), `space-copy-pe`
