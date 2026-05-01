# Política de scraping — Planea Ya

> **Estado**: borrador. Implementación post-MVP (Fase 6 del plan de trabajo).
> **Owner**: info@proper.com.pe.
> **Mantenido por**: agente `librarian`.

Este documento define **qué scrapeamos, cómo, y bajo qué reglas legales/éticas**, para nutrir el catálogo inicial de Planea Ya.

---

## Objetivo

Pre-poblar el catálogo público con 500-2.000 espacios visibles públicamente en otros portales y redes, para acelerar **SEO**, **descubrimiento orgánico** y **outreach a hosts** ("alguien busca tu local en planea ya").

---

## Fuentes objetivo

| # | Fuente | Tipo | Volumen estimado | Prioridad |
|---|---|---|---|---|
| 1 | Compartir Espacios (compartirespacios.com) | Directorio público | ~500-1.500 listings Perú | Alta |
| 2 | Ineventos.pe | Directorio público | ~200-500 | Alta |
| 3 | Roodos.com | Directorio público | ~200-400 | Media |
| 4 | Mercado Libre (categoría "Servicios > Eventos > Salones") | Marketplace | ~300-700 | Media |
| 5 | OLX Perú (categoría espacios) | Marketplace | ~100-300 | Media |
| 6 | Google Maps (categoría "venue/event venue Lima") | Mapa | ~500-1.000 (con duplicados) | Baja |
| 7 | Instagram (cuentas públicas con bio "salón eventos Lima") | Red social | indefinido | Baja |

---

## Reglas (no negociables)

### Legales
1. **Solo data pública**. Nunca contenido detrás de login, paywall o protegido por scraping detection.
2. **Respetar robots.txt** de cada sitio. Si prohíbe `/listings/*`, no scrapeamos esa ruta.
3. **No copiar texto descriptivo extenso** del listing original. Solo metadata estructurada (nombre, distrito, capacidad, fotos públicas, precio público, contacto público). Las descripciones se reescriben o se piden al host cuando reclama.
4. **Atribución obligatoria**: cada listing scrapeado tiene un campo `source` con URL al original y badge visual "Datos de [fuente]".
5. **Honor takedown requests** en <72h. Email de contacto en `legal@planearya.com` (a configurar).

### Éticas
6. **Rate limiting** estricto: máximo 1 request cada 3 segundos por dominio. Sin excepciones.
7. **User-Agent identificable**: `PlaneaYa-Crawler/1.0 (+https://planearya.com/bot)` con página explicando qué hacemos y cómo opt-out.
8. **No scraping** de fotos protegidas (con marca de agua, bajo copyright explícito). Si la foto tiene marca de agua, mostramos foto placeholder y pedimos al host original que suba sus propias.
9. **No scraping de datos personales** del host más allá de lo público (nombre comercial sí, número de DNI no, dirección particular del dueño no si no está pública).

### Técnicas
10. **Almacenamiento**: tabla `scraped_listings` separada de `spaces`. Nunca se mezclan hasta que el host reclama y verifica.
11. **Estado de claim**:
    - `unclaimed_active`: visible en el portal con disclaimer "no reclamado aún".
    - `unclaimed_paused`: oculto si llegan quejas.
    - `claimed_pending`: host inició proceso de reclamo.
    - `claimed_verified`: host validado, listing activo full.
    - `removed`: takedown request o decisión interna.
12. **Re-scrape**: máximo 1 vez por mes por listing. Cambios menores se sobreescriben; cambios mayores (precio, fotos) requieren confirmación del host (si está en proceso de claim) o aviso al equipo.

---

## Flujo "Scrape & Claim"

```
[Scraper] ──→ [DB.scraped_listings (unclaimed)]
                       │
                       ▼
              Página pública con disclaimer
              "Esta información viene de [fuente]. ¿Eres dueño? Reclámalo gratis."
                       │
                       ▼
              Llega lead de un guest interesado
                       │
                       ▼
              Equipo Planea Ya contacta al host por WhatsApp:
              "Hola, alguien busca tu local. Lo tenemos publicado en
               planearya.com. Recláma lo gratis y recibe más leads."
                       │
                       ▼
              Host se registra → reclama → verifica → status: claimed_verified
                       │
                       ▼
              Listing pasa a tabla principal `spaces`
              Datos enriquecidos con info que solo el host conoce.
```

---

## Compliance

### Ley peruana
- **Ley 29733** (Protección de Datos Personales): no almacenamos datos personales identificables de no-clientes sin consentimiento. Nombres comerciales y teléfonos publicados públicamente como "contacto del salón" son data comercial, no personal.
- **Decreto Legislativo 1044** (Represión Competencia Desleal): no presentamos data de competidores de forma engañosa. Atribución clara siempre.
- **DCM SUNAT**: no aplica hasta que haya transacción.

### Internacional
- **GDPR / equivalente UE**: si un usuario europeo accede al portal, derecho a olvido aplica. Endpoint para borrar tracking.
- **CCPA (California)**: igual.

### Plataformas terceras
- **Mercado Libre / OLX**: TOS prohíben scraping comercial. Solución: usar como fuente de descubrimiento manual ("voy a registrar a este salón yo mismo"), no scraping automatizado masivo.
- **Instagram / Meta**: TOS prohíben scraping. Solución: solo descubrimiento manual + contacto directo al host.

> **Decisión**: el scraper automatizado se enfoca en directorios web (Compartir Espacios, Ineventos, Roodos, Google Maps Places API legítima). Mercado Libre, OLX e Instagram se trabajan manualmente como pipeline de outreach, no scraping masivo.

---

## Stack técnico (cuando se implemente)

- **Lenguaje**: Python 3.12 + `httpx` + `selectolax` (HTML parsing rápido).
- **Cola**: simple Postgres queue inicialmente. RabbitMQ si crece.
- **Storage**: tabla `scraped_listings` en Railway PG.
- **Imágenes**: descarga + reupload a Cloudflare R2 con compresión WebP. Fotos originales nunca se sirven hot-link.
- **Logs**: cada request logueado con timestamp, URL, status, content-hash.
- **Cron**: 1 vez al día overnight, throttled.

---

## Roles humanos

- **Owner / equipo Planea Ya**: revisa listings nuevos, contacta hosts, gestiona reclamos.
- **Librarian agent (Claude)**: monitorea logs, alerta si rate-limit cae bajo, audita compliance mensual.
- **Reviewer agent (Claude)**: audita esta política trimestral.

---

## Métricas

- Listings scrapeados/mes.
- % listings reclamados por hosts (objetivo: 30% en 6 meses).
- Takedown requests recibidos (objetivo: <2/mes).
- Tiempo de respuesta a takedown (objetivo: <72h, idealmente <24h).
- Costo operativo del scraper (objetivo: <US$30/mes).

---

## Lo que NO hacemos

- ❌ Scraping de Instagram bot-style (anti-bot detection nos baneará).
- ❌ Republicar fotos sin re-encoder.
- ❌ Mostrar listings scrapeados sin disclaimer "no reclamado".
- ❌ Vender o compartir la base scraped con terceros.
- ❌ Usar fotos con marca de agua del competidor.
- ❌ Bypassing de captchas.
- ❌ Scraping desde IPs residenciales / proxies dudosos. Solo IP propia con UA identificable.

---

## Aprobación

- [ ] Owner — info@proper.com.pe
- [ ] Reviewer agent
- [ ] Asesor legal (cuando se contrate)
