# PRD MVP — Coordina Eventos

> **Producto**: Coordina Eventos (working name).
> **Dominio**: coordinaeventos.com (placeholder).
> **Owner**: info@proper.com.pe.
> **Estado**: borrador para revisión.
> **Fecha**: 2026-05-01.
> **Insumos**: `lean-canvas.md`, `analisis-mercado/06-conclusion-mercado.md`.

---

## 1. Resumen ejecutivo

**Coordina Eventos es el marketplace de espacios alquilables por horas en Lima** que combina (a) catálogo gratuito navegable por caso de uso, (b) asistente conversacional que matchea al guest con 3 opciones reales en segundos, y (c) concierge humano fallback que escala los casos no resueltos hacia la agencia de eventos del owner.

El MVP **no procesa pagos**. La transacción ocurre offline (Yape, transferencia, efectivo) entre host y guest. La plataforma monetiza indirectamente: los leads premium (organización completa, eventos grandes) van a la agencia donde el ticket promedio es S/3.000-8.000 con margen 15-25%.

Tiempo a primer lead pagado vía agencia: **4-6 semanas**.

---

## 2. Personas

### Persona 1 — Lucía, guest casual (segmento principal)

- **Edad**: 32 años. NSE B+. Lima Moderna (Surco).
- **Rol**: gerenta de marketing en empresa mediana.
- **Contexto**: organiza un baby shower para una amiga en 5 semanas. Capacidad 25 personas, sábado tarde, presupuesto S/1.500-3.000 incluido espacio y decoración.
- **Job to be done**: "Encontrar un espacio bonito en Miraflores o Barranco que se pueda decorar, que tenga sillas y mesas, y que el dueño responda rápido."
- **Dolor actual**: 3 días buscando en Instagram, pidió cotización a 6 cuentas, recibió respuesta de 2, ninguna le convenció totalmente, considera contratar wedding planner por desespero.
- **Por qué eligiría Coordina Eventos**: en 5 minutos ve 5 opciones reales con foto y precio. Pide visita directo. Si no le convencen, "ayúdenme a organizarlo".

### Persona 2 — Mario, host fragmentado (segmento secundario)

- **Edad**: 48 años. Dueño de salón de eventos en Pueblo Libre, capacidad 60 personas, S/200/h.
- **Rol**: emprendedor. Su negocio principal es el salón.
- **Contexto**: tiene cuenta de Instagram (3.500 seguidores) y un grupo de WhatsApp con clientes recurrentes. No tiene web propia. Pierde leads cuando no responde DM en 6h.
- **Job to be done**: "Recibir más clientes nuevos sin perder tiempo en publicidad ni mantener web."
- **Dolor actual**: las publicaciones en IG ya no funcionan como antes. Los grupos de Facebook traen clientes que regatean.
- **Por qué se uniría**: gratis, tarda 5 minutos publicar, le notifican leads por WhatsApp.

### Persona 3 — Sandra, cliente de la agencia (segmento de monetización)

- **Edad**: 38 años. NSE A. Casada, 2 hijos. Vive en La Molina.
- **Rol**: directora de RRHH en multinacional.
- **Contexto**: organiza el aniversario de la empresa (120 invitados) y el cumpleaños de su hija (40 niños) en el mismo trimestre. Presupuesto combinado S/15.000.
- **Job to be done**: "Que alguien me organice esto sin que tenga que coordinar a 8 proveedores."
- **Dolor actual**: el wedding planner que conoce está saturado. No quiere meterse a coordinar DJ + catering + decoración + mozos.
- **Por qué se convierte a la agencia**: entra a Coordina Eventos buscando espacio, ve "Te organizamos todo" como CTA, pide cotización. La agencia responde en <2h con propuesta full.

---

## 3. Job stories

> Formato: "Cuando ___, quiero ___, para que ___."

1. **Cuando estoy organizando un evento social (cumpleaños, baby shower, despedida)**, quiero ver opciones reales filtradas por mi distrito y presupuesto en menos de 5 minutos, para que no tenga que perseguir 10 cuentas de Instagram.
2. **Cuando una opción me gusta**, quiero pedir una visita y que el host me confirme rápido, para que no se me pase la fecha.
3. **Cuando ninguna opción me convence**, quiero que alguien me ayude a buscarlo y/o organizar el evento, para no abandonar el proceso frustrada.
4. **Cuando soy host de un espacio**, quiero publicar mi local gratis en 5 minutos, para que más gente lo encuentre sin que tenga que hacer marketing.
5. **Cuando recibo un lead**, quiero que me llegue por WhatsApp con todos los datos del guest, para responder desde el celular sin abrir un dashboard.

---

## 4. User stories priorizadas (MoSCoW)

### Must (MVP — Fase 5)

#### Catálogo y búsqueda
- M1. Como guest, puedo navegar el catálogo de espacios filtrando por distrito y caso de uso.
- M2. Como guest, puedo ver la ficha de un espacio con fotos, capacidad, equipamiento, precio referencial.
- M3. Como guest, puedo iniciar el asistente conversacional desde el hero o desde una ficha.

#### Asistente
- M4. El asistente me hace 5-7 preguntas (caso de uso, fecha, distrito, capacidad, presupuesto, equipamiento clave, preferencia de ambiente) y devuelve 3 opciones reales del catálogo o me deriva al formulario humano.
- M5. Cuando el asistente no encuentra match, captura mis datos (nombre, WhatsApp, descripción del evento) y los manda al equipo concierge.

#### Coordinación
- M6. Como guest, puedo solicitar una visita al espacio. Esto dispara una notificación al host por WhatsApp con mis datos.
- M7. Como host, recibo la notificación con WhatsApp del guest pre-poblado para responder en 1 click.

#### Onboarding host
- M8. Como host, puedo crear mi cuenta con email + WhatsApp. Sin pago.
- M9. Como host, publico un espacio en formulario de 5 minutos: nombre, distrito, dirección, capacidad, fotos, equipamiento, precio referencial, casos de uso. Estado inicial: "publicado, pendiente de verificación".
- M10. Como host, puedo editar/pausar/despublicar mi espacio.

#### Dashboard interno (sólo equipo)
- M11. Como equipo Coordina Eventos, veo todos los leads del concierge en una pantalla con estado (nuevo / contactado / cotizado / cerrado / perdido).
- M12. Como equipo, puedo marcar un lead como "calificado para agencia" y exportar sus datos.

### Should (post-MVP cercano)
- S1. Sistema de "reclamar listing" para hosts cuyos espacios fueron pre-poblados por scrape (Fase 6).
- S2. Reseñas de guest post-evento.
- S3. Verificación humana de espacios (visita presencial), sello "Verificado".
- S4. Asistente IA real (Claude API + RAG sobre catálogo) en lugar del form scriptado.
- S5. Sincronización de calendario del host con Google Calendar.
- S6. Página por distrito × caso de uso con SEO local agresivo.

### Could (visión 6-12 meses)
- C1. Pago en plataforma (Culqi + Yape).
- C2. Marketplace de proveedores (DJ, catering, decoración, fotografía).
- C3. Cuentas corporativas pre-pagadas B2B.
- C4. Programa de referidos host y guest.
- C5. Expansión a Cusco, Arequipa, Trujillo.

### Won't (explícitamente fuera del MVP)
- W1. App móvil nativa (iOS/Android). El producto es web responsive.
- W2. Pasarela de pagos en plataforma.
- W3. Verificación masiva de catálogo entero. Se hace bajo demanda.
- W4. Geografía fuera de Lima Metropolitana.
- W5. Integraciones con Google/IG Calendar en MVP.

---

## 5. Métricas de éxito

### North star
**Leads calificados/mes a la agencia** (definición: formulario fallback completo + descripción de evento + presupuesto >S/2.000 o explícito "quiero que me organicen todo").

### KPIs guard rails

| KPI | Mes 3 | Mes 6 | Mes 12 |
|---|---|---|---|
| Espacios publicados | 200 | 500 | 1.200 |
| Visitas únicas/mes | 1.000 | 5.000 | 20.000 |
| % visitas que inician asistente | 20% | 25% | 30% |
| % asistente con match exitoso | 50% | 60% | 70% |
| Leads concierge/mes | 10 | 50 | 200 |
| Conversión lead → cliente agencia | — | 15% | 25% |
| Hosts activos (lead en últimos 30d) | 30 | 80 | 200 |

### Métricas anti-vanity (lo que NO importa)
- Total de signups (importa "hosts activos").
- Pageviews crudas (importa "asistente iniciado").
- Total de espacios listados sin filtro (importa "espacios con foto y datos completos").

---

## 6. Diseño funcional

### Arquitectura informacional

```
/                       → home + asistente hero
/buscar                 → catálogo con filtros
/buscar/[distrito]      → SEO landing por distrito
/buscar/[caso-uso]      → SEO landing por caso (ej. /buscar/baby-shower)
/buscar/[distrito]/[caso-uso]  → combinación SEO

/espacios/[slug]        → ficha de espacio individual
/asistente              → flujo conversacional standalone
/concierge              → form fallback "te ayudamos"

/host                   → landing host (publica gratis)
/host/registro          → onboarding host
/host/dashboard         → panel del host (sus espacios, leads)
/host/espacios/nuevo    → crear espacio
/host/espacios/[id]/editar

/admin                  → dashboard interno equipo (leads, listings)
```

### Flujo principal del guest

```
Home
  │
  ▼
"¿Qué evento estás planeando?" + chips de casos de uso
  │
  ├──→ Click chip "Baby shower"
  │      │
  │      ▼
  │    /buscar/baby-shower (lista filtrada)
  │
  └──→ Click "Te ayudamos a encontrarlo"
         │
         ▼
       Asistente conversacional (5-7 preguntas)
         │
         ├──→ Match exitoso (3 opciones)
         │      │
         │      ▼
         │    Click "Pedir visita" → notificación WhatsApp al host
         │
         └──→ Sin match
                │
                ▼
              Form concierge → equipo humano responde por WhatsApp
                │
                ▼
              Si calificado: enrutado a agencia
```

### Asistente — preguntas fijas (v1, scriptado)

1. ¿Qué tipo de evento estás organizando? *(chip selector: cumpleaños, baby shower, sesión de fotos, reunión, capacitación, video shoot, yoga, pop-up, otro)*
2. ¿Cuándo? *(date picker — hoy / mañana / esta semana / este mes / fecha específica)*
3. ¿Cuántas personas? *(input numérico)*
4. ¿En qué distrito te conviene? *(multi-select de los 8 distritos de Lima Moderna + "cualquiera")*
5. ¿Cuál es tu presupuesto aproximado? *(rangos: <S/500, S/500-1.500, S/1.500-3.000, >S/3.000)*
6. ¿Necesitas algo en particular? *(checkboxes: estacionamiento, cocina, terraza, sonido, proyector, accesibilidad, mascotas)*
7. *(Opcional)* ¿Algo más que debamos saber? *(textarea libre)*

→ Backend hace match SQL → devuelve top 3 ordenados por relevancia + disponibilidad.
→ Si <3 matches o `confidence_score < 0.6` → directo a form concierge.

### Schema de datos (preliminar)

```sql
-- Hosts (cuentas)
hosts (
  id uuid PK,
  email text unique,
  whatsapp text,
  display_name text,
  created_at timestamptz,
  status text  -- active / paused / banned
)

-- Espacios
spaces (
  id uuid PK,
  host_id uuid FK → hosts,
  slug text unique,
  name text,
  distrito text,
  direccion text,
  lat numeric, lng numeric,
  capacidad_min int, capacidad_max int,
  precio_hora_pen numeric,
  precio_evento_pen numeric,  -- alternativa a precio/hora
  descripcion text,
  fotos jsonb,  -- array de URLs
  equipamiento text[],  -- amenities slugs
  casos_uso text[],
  status text,  -- draft / published / paused / verified / claimed_pending
  created_at, updated_at, verified_at
)

-- Leads del asistente / concierge
leads (
  id uuid PK,
  source text,  -- assistant_match / assistant_no_match / concierge_form / direct
  nombre text,
  email text, whatsapp text,
  caso_uso text,
  fecha_evento date,
  capacidad int,
  distrito_preferido text[],
  presupuesto_rango text,
  requisitos text[],
  notas text,
  matched_space_ids uuid[],  -- si hubo matches
  status text,  -- new / contacted / quoted / closed_won / closed_lost
  agency_eligible bool,
  created_at, updated_at
)

-- Solicitudes de visita (host ↔ guest)
visit_requests (
  id uuid PK,
  space_id uuid FK,
  lead_id uuid FK,
  guest_whatsapp text,
  status text,  -- pending / contacted / scheduled / done / cancelled
  created_at, updated_at
)

-- Reseñas (post-MVP — Should)
-- Verificaciones (post-MVP — Should)
-- Reclamación de listings (post-MVP — Fase 6 scrape)
```

---

## 7. Stack y arquitectura tentativa

| Capa | Decisión | Justificación |
|---|---|---|
| Frontend | **Astro** + islands (Solid o Preact para interactividad) | Estático, rápido, SEO-friendly, deployable a GitHub Pages / Cloudflare Pages |
| API | **Cloudflare Workers** o serverless functions de Vercel | Sin servidor que mantener, cold-start mínimo |
| DB | **Railway PostgreSQL** (ya activa) | Decisión vigente. Migrar a Neon/Supabase si crece |
| Storage imágenes | **Cloudflare R2** | Sin egress fees, S3-compatible |
| Auth host | **Auth.js** + Postgres adapter | Open source, sin lock-in |
| Email transaccional | **Resend** | API limpia, free tier 100 emails/día |
| Notificaciones host | **WhatsApp Business API (Meta Cloud)** | Default cultural en Perú |
| Analytics | **Plausible** | Privacy-first, sin cookie banner |
| Dominio | `coordinaeventos.com` (placeholder) | A confirmar |

---

## 8. Lo que NO entra en MVP (refresh de Won't)

- Pagos en plataforma.
- App móvil nativa.
- Geografía fuera de Lima.
- Verificación masiva.
- Asistente IA real (es scriptado en MVP).
- Sistema de reclaim de listings scrapeados (Fase 6).
- Reseñas verificadas.
- Marketplace de proveedores complementarios.
- Cuentas B2B corporativas.

---

## 9. Riesgos y mitigaciones

| # | Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|---|
| R1 | El asistente devuelve matches malos por catálogo escaso → frustración | Alta | Alto | Cohorte cero curada manualmente. Catálogo pre-cargado con scraping (Fase 6). Form fallback siempre disponible. |
| R2 | Hosts no responden a leads en <24h → ranking de plataforma se cae | Media | Alto | Tracking de tiempo de respuesta. Penalización en ranking. Recordatorio por WhatsApp si no responde. |
| R3 | Agencia no convierte leads (volumen no compensa esfuerzo) | Media | Crítico | Medir conversión desde día 1. Pivote rápido a fee fijo si la agencia no convierte. |
| R4 | SpacePal pone equipo en Lima | Baja-Media | Crítico | Construir foso operativo (concierge + Yape + WhatsApp + agencia propia) — no replicable en 90 días. |
| R5 | Sin pagos en plataforma → no podemos demostrar tracción a inversores | Media | Medio | Documentar leads/mes de agencia como tracción equivalente. |
| R6 | Scraping (Fase 6) genera takedown requests masivos | Media | Medio | Política de scraping clara (`documentation/scraping-policy.md`), respetar robots.txt, responder rápido a requests. |
| R7 | Costo operativo agencia + plataforma supera revenue temprano | Alta | Alto | Equipo MVP mínimo (2-3 part-time). Crecer solo cuando revenue justifique. |

---

## 10. Hitos del MVP

| Semana | Hito | Entregable |
|---|---|---|
| 1 | Branding cerrado | Logo + tokens + dominio comprado |
| 2 | Landing v1 live | Hero + asistente form + onboarding host capturando emails |
| 3 | Catálogo público + 50 espacios curados | Búsqueda funcional |
| 4 | Asistente scriptado completo | 7 preguntas + match SQL + form fallback |
| 5 | Dashboard host + dashboard interno | Hosts pueden gestionar espacios; equipo ve leads |
| 6 | Primer lead pagado vía agencia | Validación del modelo |

---

## 11. Lo que el owner debe decidir antes de Fase 5 (app)

1. **Stack frontend**: Astro vs Next.js export. *Recomendación: Astro.*
2. **Dominio final**: confirmar `coordinaeventos.com` o cambiar.
3. **Email transaccional**: Resend vs SES. *Recomendación: Resend.*
4. **WhatsApp API provider**: Meta Cloud directa vs Twilio. *Recomendación: Meta Cloud.*
5. **Estructura legal de la agencia**: ¿quién factura los servicios concierge? ¿el RUC de Proper o uno nuevo "Coordina Eventos"?

---

## 12. Aprobación

- [ ] Owner — info@proper.com.pe — fecha: _____
- [ ] Reviewer interno (`reviewer` agent) — fecha: _____

> Cualquier cambio post-aprobación se documenta como ADR en `backlog/decisiones.md`.
