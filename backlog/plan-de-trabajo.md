# Plan de trabajo Coordina Eventos

> **Última revisión**: 2026-05-01.
> **Status global**: Fase 1 ✅ · Fase 2 (branding) en curso · Fase 3 (PRD) ✅ documentos base escritos · Fase 4-7 pendientes.

7 fases. Cada una tiene objetivo, entregables, agentes/skills, decisiones del owner, criterio de cierre y estimado.

---

## ✅ Fase 1 — Análisis de mercado completo

**Objetivo:** entender qué hay, cómo se resuelve hoy, qué empresas existen.

**Entregables completados**
- `analisis-mercado/01-resumen-ejecutivo.md` ✓
- `analisis-mercado/competidores/{space-pal,internacionales,otros-peru}.md` ✓
- `analisis-mercado/personas/{buyer,host}-personas.md` ✓
- `analisis-mercado/pricing/modelo-monetizacion.md` ✓
- `analisis-mercado/research/*.md` (6 docs) ✓
- `analisis-mercado/04-mapa-de-soluciones.md` ✓
- `analisis-mercado/05-empresas-listadas.md` ✓ (45 jugadores)
- `analisis-mercado/06-conclusion-mercado.md` ✓ (recomendación: vertical eventos sociales Lima)

**Conclusión accionable**: SpacePal Lima vacío. Ventana 12-18 meses. Modelo recomendado (post-pivote): plataforma gratuita lead-gen + concierge humano + agencia de eventos del owner.

---

## 🟡 Fase 2 — Branding básico

**Objetivo:** cerrar identidad visual base antes de invertir en landing.

**Entregables**
- `brand/logo/wordmark.svg` ✓ — wordmark "coordina · eventos" tipográfico simple, dos palabras, azul.
- `brand/logo/wordmark-white.svg` ✓ — versión sobre fondos oscuros.
- `brand/logo/icon.svg` ✓ — isotipo cuadrado para favicon/IG profile.
- `brand/identity/posicionamiento.md` ✓ — actualizado con modelo lead-gen + agencia.
- `brand/identity/naming.md` ✓ — Coordina Eventos con backups.
- `brand/messaging/voz.md` ✓ — voz de marca.
- `brand/messaging/taglines.md` ✓ — pendiente seleccionar final.
- `documentation/branding.md` ✓ — tokens (color, tipografía, spacing).
- `brand/identity/moodboard.md` — pendiente.
- Favicon + OG image — pendiente.

**Agentes/skills usadas**
- Skills: `brand-guidelines` (anthropics), `extract-design-system`, `web-design-guidelines`, `space-branding`, `copywriting`.

**Decisiones tomadas**
- Nombre placeholder: **Coordina Eventos** / `coordinaeventos.com`.
- Color principal: `#2563EB`.
- Wordmark tipográfico simple (Inter 700, dos palabras separadas por color).
- Sin isotipo elaborado en MVP (un cuadrado azul con la "p" inicial).

**Decisiones pendientes**
- ¿Confirmar nombre final o cambiar?
- ¿Agencia de eventos del owner ya tiene marca? Alinear o separar.
- Tagline final.

**Criterio de cierre**
- Aprobación owner de wordmark + nombre.
- Tokens documentados.
- Favicon + OG image generados.

**Estimado**: 2-3 días desde aprobación final del owner.

---

## ✅ Fase 3 — Lean Canvas + PRD MVP

**Objetivo:** convertir hallazgos en spec accionable.

**Entregables completados**
- `app/docs/lean-canvas.md` ✓
- `app/docs/prd-mvp.md` ✓ (12 secciones, MoSCoW, schema PG preliminar, riesgos, hitos)
- `documentation/scraping-policy.md` ✓ (política ética/legal para Fase 6)

**Pendientes** (no bloquean MVP)
- `app/docs/journey-maps.md` — diagramas visuales del PRD.
- `app/docs/financial-model.md` — modelo agencia.

**Decisiones críticas tomadas**
- Vertical: horizontal multi-categoría (estilo Peerspace) en Lima.
- Geografía MVP: **solo Lima**.
- Monetización: **0% comisión, lead-gen + agencia**.
- North star: leads calificados/mes a la agencia (no bookings pagados).
- Sin pasarela de pagos en MVP.

**Estimado**: hecho.

---

## ⏳ Fase 4 — Landing v1

**Objetivo:** landing pública que captura leads del asistente desde día 1.

**Entregables**
- `landing/src/` actualizado con branding final, copy es-PE, hero con asistente form como CTA principal.
- API que recibe leads del form y los graba en Railway PG.
- Plausible analytics activado.
- OG image, favicons, sitemap, robots.txt.
- Dominio comprado y apuntando a hosting (GitHub Pages temporal, migrar a Cloudflare Pages cuando crezca).

**Agentes/skills**
- `landing-builder`, `db-migrator`, `librarian`, `reviewer`.
- Skills: `landing-page-design`, `web-design-guidelines`, `copywriting`, `space-copy-pe`, `postgresql-table-design`.

**Decisiones que tomas tú**
- Comprar `coordinaeventos.com` (~US$10/año).
- Email transaccional: Resend recomendado.
- Analítica: Plausible (US$9/mes) vs Umami self-host.

**Criterio de cierre**
- Lighthouse 95+ en perf/a11y/SEO mobile.
- Form de asistente captura leads E2E.
- 50+ visitas orgánicas semana 1.

**Estimado**: 2 semanas.

---

## ⏳ Fase 5 — App MVP

**Objetivo:** producto funcional con catálogo + asistente + onboarding host + dashboard interno.

### 5.A — Arquitectura (3-4 días)
- ADR de stack final (Astro recomendado).
- `documentation/db-schema.md` con esquema completo del PRD.
- `documentation/architecture.md` actualizado.
- ADR auth (Auth.js + Postgres).
- ADR storage imágenes (Cloudflare R2).

### 5.B — Construcción (4-5 semanas)
- Migraciones SQL aplicadas.
- Catálogo público navegable.
- Páginas SEO por distrito × caso de uso.
- Asistente conversacional scriptado (form de 5-7 preguntas, match SQL).
- Form fallback para concierge.
- Onboarding de host (registro + crear espacio en 5 min).
- Dashboard host (sus espacios, leads recibidos).
- Dashboard interno equipo (todos los leads, status, export).
- Notificaciones a host por WhatsApp (Meta Cloud API).
- Verificación bajo demanda (botón "agendar visita").

**Agentes/skills**
- `db-migrator`, `landing-builder` (extensión a app), `reviewer`.
- Skills: `engineering:architecture`, `engineering:system-design`, `postgresql-table-design`, `claude-api`.

**Decisiones que tomas tú**
- Stack frontend: Astro vs Next.js export. Recomendación: Astro.
- Auth: Auth.js vs Clerk. Recomendación: Auth.js (open source).
- WhatsApp: Meta Cloud API vs Twilio. Recomendación: Meta Cloud directo.
- Migrar Railway PG a Neon/Supabase ahora o después.

**Criterio de cierre**
- 1 lead end-to-end real: guest llena asistente → 3 matches → agenda visita → host responde por WhatsApp.

**Estimado**: 5.A: 3-4 días. 5.B: 4-5 semanas.

---

## ⏳ Fase 6 — Scrape & Claim (post-app, según ajuste owner)

**Objetivo:** poblar el catálogo con 500-2.000 espacios scrapeados de portales públicos para acelerar SEO y outreach a hosts.

**Entregables**
- `scraping/` con scrapers de Compartir Espacios, Ineventos, Roodos, Google Places API.
- Tabla `scraped_listings` separada de `spaces` en PG.
- Proceso de "reclamar listing" para hosts.
- Dashboard interno de reclamos.
- Página "esta info viene de [fuente] — recláma lo gratis" en cada listing scrapeado.

**Skills**
- `engineering:debug`, `data:write-query`, `postgresql-table-design`. Posible nueva skill: `web-scraping` (de las disponibles).

**Reglas no negociables**
- Respetar robots.txt y rate limiting (1 req / 3 seg / dominio).
- User-Agent identificable: `PlaneaYa-Crawler/1.0`.
- Solo data pública estructurada.
- Atribución visible en cada listing.
- Honor takedown requests <72h.
- Ver `documentation/scraping-policy.md` para detalles.

**Criterio de cierre**
- 500+ listings pre-poblados.
- 30%+ tasa de claim por hosts contactados.
- 0 takedown requests sin resolver.

**Estimado**: 2-3 semanas.

---

## ⏳ Fase 7 — Social, contenido, outreach

**Objetivo:** activar canales para volumen: tráfico orgánico + outreach a hosts.

**Entregables**
- `social/` con primer mes de calendario y posts redactados (LinkedIn 8, IG 16, TikTok 12, FB 4).
- Outreach kit B2B coworkings: deck + email + WhatsApp template.
- Outreach kit hoteles con salones (Marriott, Hilton, Belmond, Casa Andina, Costa del Sol).
- 3 mini casos publicados (1 host, 1 guest, 1 evento exitoso).
- SEO: páginas long-tail por distrito × caso de uso indexadas en Google.
- Programa de referidos host y guest documentado.

**Agentes/skills**
- `content-creator`, `host-onboarder`, `reviewer`.
- Skills: `marketing:draft-content`, `marketing:campaign-plan`, `marketing:seo-audit`, `marketing:email-sequence`, `copywriting`, `space-copy-pe`.

**Criterio de cierre**
- 10 hosts activos publicados.
- Primer cliente concierge cerrado vía la agencia.
- 500+ visitas únicas/semana orgánicas.

**Estimado**: continuo, intensivo primer mes.

---

## Visión global

```
✅ Fase 1: Mercado
   │
   ▼
🟡 Fase 2: Branding básico ─────┐
   │                            │
   ▼                            │
✅ Fase 3: Lean + PRD            │
   │                            │
   ▼                            │
⏳ Fase 4: Landing ──────────────┤
   │                            │
   ▼                            │
⏳ Fase 5: App (5.A → 5.B)       │
   │                            │
   ▼                            │
⏳ Fase 6: Scrape & Claim        │
                                │
              ┌─────────────────┘
              ▼
⏳ Fase 7: Social + Outreach (paralelo desde Fase 4)
```

| Fase | Estimado | Dependencia | Estado |
|---|---|---|---|
| 1. Mercado | 3-4 días | — | ✅ |
| 2. Branding | 2-3 días | 1 | 🟡 |
| 3. Lean + PRD | hecho con 1 | 1 | ✅ |
| 4. Landing | 2 sem | 2 | ⏳ |
| 5.A. Arquitectura | 3-4 días | 3 | ⏳ |
| 5.B. App | 4-5 sem | 5.A | ⏳ |
| 6. Scrape & Claim | 2-3 sem | 5 | ⏳ |
| 7. Social + Outreach | continuo | 4 | ⏳ |

**Tiempo a primer lead pagado vía agencia**: ~6 semanas desde aprobación de branding.

---

## Decisiones pendientes (urgencia descendente)

1. **Nombre final** — ¿`Coordina Eventos` o cambiar? (Hoy es placeholder.)
2. **Agencia del owner** — ¿tiene marca? ¿alineamos o separamos?
3. **Comprar dominio** — `coordinaeventos.com` (~US$10/año).
4. **Stack frontend** — Astro vs Next.js. (Recomendación: Astro.)
5. **WhatsApp API** — Meta Cloud directa vs Twilio.

---

## Estado de skills

15 skills activas (12 externas vía npx skills + find-skills + 3 locales). Top relevantes para próximas fases:

| Fase | Skills clave |
|---|---|
| 2 (branding) | `brand-guidelines`, `extract-design-system`, `space-branding` |
| 4 (landing) | `landing-page-design`, `web-design-guidelines`, `copywriting`, `space-copy-pe` |
| 5 (app) | `postgresql-table-design`, `claude-api`, `engineering:architecture` |
| 6 (scraping) | (instalar `web-scraping` cuando arranque) |
| 7 (social) | `marketing:*`, `copywriting`, `space-copy-pe` |
