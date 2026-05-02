# Lean Canvas — Coordina Eventos

> **Producto**: Coordina Eventos — `coordinaeventos.com` (placeholder; cambiable).
> **Fecha**: 2026-05-01.
> **Owner**: info@proper.com.pe.
> **Insumo**: `analisis-mercado/06-conclusion-mercado.md`.

Una página, 9 bloques. Cualquier cambio aquí refleja en el PRD y en el plan de trabajo.

---

## 1. Problema

1. **Encontrar un espacio para alquilar por horas en Lima toma 3-7 días** de cotizaciones por DM, llamadas y WhatsApp.
2. **No hay confianza**: el guest paga 50% por adelantado a un desconocido en Yape sin garantía.
3. **El host pierde reservas** porque su único canal es Instagram y responde tarde o se le pasa el lead.
4. **El cliente que quiere "que le organicen el evento" no sabe a quién acudir** salvo wedding planners caros o agencias premium.

### Alternativas existentes (qué usa la gente hoy)

- Instagram + DMs.
- Grupos privados de Facebook ("Salones Lima", "Eventos Lima").
- Mercado Libre / OLX categoría "espacios".
- Compartir Espacios, Ineventos.pe (directorios sin transacción).
- WhatsApp del salón / recomendación de amigos.
- Wedding planners (caro, solo bodas).

---

## 2. Segmentos de cliente

### Segmento principal de la **plataforma** (tráfico orgánico)
**Guest casual**: persona NSE A/B en Lima organizando un evento social (cumpleaños, baby shower, despedida) o profesional puntual (sesión de fotos, reunión, capacitación). 25-45 años. Paga por mes 1-3 eventos al año. Usa Instagram y WhatsApp como default.

### Segmento secundario de la **plataforma** (oferta)
**Host fragmentado**: dueño de salón, loft, terraza, estudio fotográfico, estudio de yoga o cancha en Lima Moderna. PYME o emprendedor individual con un solo espacio. Usa IG y WhatsApp. No tiene web propia. Le interesa más demanda gratis.

### Segmento de monetización real (agencia)
**Cliente de agencia de eventos**: subset del guest casual que quiere "que le organicen todo" — empresa con off-site / lanzamiento, persona con boda / cumpleaños grande / quinceaños / despedida con presupuesto >S/3.000. Este segmento llega a la agencia vía la plataforma.

### Early adopters
- Productoras audiovisuales que necesitan locaciones rotativas.
- Coordinadores de RRHH de empresas medianas con eventos corporativos recurrentes.
- Wedding planners independientes que quieren un catálogo confiable de salones para sus clientes.

---

## 3. Propuesta única de valor

> **El asistente que encuentra tu espacio en Lima en minutos. Y si no, lo organizamos por ti.**

- "Coordina Eventos" = encuentra rápido o te ayudamos a organizarlo.
- Diferenciador único en Latam: **asistente conversacional conectado a inventario real + concierge humano fallback**.
- Listar es **siempre gratis**.

### Concepto de "una frase"
> "El Peerspace de Perú con concierge humano cuando no encuentras lo perfecto."

---

## 4. Solución

1. **Catálogo público** de espacios en Lima, navegable por **caso de uso** (cumpleaños, sesión de fotos, reunión, baby shower, yoga, capacitación, video shoot, pop-up).
2. **Asistente conversacional** (form inteligente v1, IA real v2) que pregunta lo necesario y devuelve 3 matches.
3. **Formulario fallback** que escala a equipo humano cuando el asistente no encuentra match.
4. **Onboarding de host gratuito** en 5 minutos. Verificación bajo demanda (cuando un guest pide visita).
5. **Coordinación host ↔ guest**: notificación al host por WhatsApp cuando alguien pide visitar; el host coordina directamente.
6. **No hay pasarela de pagos en plataforma** en MVP. La transacción ocurre offline (Yape / efectivo / como hoy).
7. **Conversión a agencia**: cualquier lead que pida "organización completa" entra al funnel de la agencia de eventos del owner.

---

## 5. Canales

### Adquisición de demanda (guests)
- **SEO orgánico** (largo plazo): páginas por distrito × caso de uso (`/lima/miraflores/cumpleanos`).
- **Instagram orgánico**: contenido de espacios destacados, casos de eventos reales.
- **Grupos de Facebook**: presencia activa en grupos clave de eventos Lima.
- **Google Ads localizados** (Fase 2 cuando haya catálogo robusto).

### Adquisición de oferta (hosts)
- **Scrape & Claim** (post-MVP, Fase 6): scrapear listings públicos de portales existentes, publicarlos como "no reclamado", y cuando llega un lead → contacto personal del owner al host: "alguien quiere alquilar tu local, recláma lo gratis".
- **Outreach B2B**: cadenas de coworking (Comunal, WeWork, Worx, Regus, Lima Coworking, Swiss Rents) y salones de hotel (Marriott, Hilton, Belmond, Casa Andina, Costa del Sol).
- **DMs a hosts en IG**: 50-100/semana.
- **Boca a boca** vía wedding planners y productoras.

### Conversión a agencia
- CTA "Te ayudamos a organizarlo" en cada paso del funnel.
- Formulario de "no encontramos exacto" → equipo humano por WhatsApp.
- Email + WhatsApp post-evento ofreciendo organización para próximo evento.

---

## 6. Flujos de ingreso

**La plataforma genera CERO revenue directo en MVP.** Es un imán de leads para la agencia de eventos del owner.

| Fuente | Cuándo | Estimado mes 6 | Estimado mes 12 |
|---|---|---|---|
| Eventos organizados por la agencia (margen) | Día 1 | S/ 5.000-10.000/mes | S/ 15.000-30.000/mes |
| Comisión de proveedores referidos (DJ, catering, etc.) | Mes 6+ | S/ 0 | S/ 2.000-5.000/mes |
| Listing premium / destacado para hosts | Mes 9+ | S/ 0 | S/ 1.000-3.000/mes |
| Publicidad para servicios complementarios | Mes 12+ | S/ 0 | S/ 0 |

**North star**: leads calificados/mes que llegan a la agencia.
**Métrica de salud de la plataforma**: visitas únicas/mes, espacios listados, tasa de match exitoso del asistente.

---

## 7. Estructura de costos

### Infraestructura (mensual)
- Dominio `.com`: ~US$1/mes (US$12/año).
- Hosting (GitHub Pages → Cloudflare Pages cuando crezca): US$0-20/mes.
- DB Railway PG: US$5-20/mes (incluido en plan free / Hobby).
- Anthropic API (asistente IA v2): US$30-150/mes según volumen.
- Email transaccional (Resend): US$0-20/mes.
- Plausible analytics: US$9/mes.
- Cloudflare R2 (imágenes): US$1-10/mes.

**Total infra estimada**: **US$50-230/mes** según fase.

### Equipo operativo (mensual)
- Owner (tú) — 0 hasta primera agencia revenue.
- Community manager part-time: S/ 1.500-2.500/mes (Fase 2+).
- Sales / host onboarding part-time: S/ 1.500-3.000/mes (Fase 3+).
- Customer success / concierge humano: S/ 2.000-4.000/mes (Fase 4+).

**Total equipo estimado a mes 6**: S/ 5.000-10.000/mes.

### Marketing
- Ads Google + Meta: US$0 hasta tener catálogo (Fase 4+), luego US$200-1.000/mes según crecimiento.

---

## 8. Métricas clave

### North star (mensual)
**Leads calificados a la agencia/mes** = formularios completados + concierge requests + emails con presupuesto >S/2.000.

### KPIs de plataforma
1. **Espacios listados** (objetivo mes 3: 200; mes 6: 500; mes 12: 1.200).
2. **Visitas únicas/mes** (mes 3: 1.000; mes 6: 5.000; mes 12: 20.000).
3. **Conversión visita → asistente iniciado** (objetivo: 25%).
4. **Tasa de match exitoso del asistente** (objetivo: 60% el asistente devuelve ≥1 opción que el guest considera).
5. **Hosts activos** = que han recibido al menos 1 lead en últimos 30 días.

### KPIs de agencia (lo que monetiza)
1. **Leads calificados/mes** (mes 3: 10; mes 6: 50; mes 12: 200).
2. **Conversión lead → cliente agencia** (objetivo: 15-25%).
3. **Ticket promedio agencia** (estimado: S/ 3.000-8.000 por evento).
4. **Margen por evento agencia** (estimado: 15-25%).

---

## 9. Ventaja injusta (lo que es difícil de copiar)

1. **Agencia de eventos propia ya operando** (del owner) — los competidores son solo plataforma, nosotros somos plataforma + servicio. Doble play.
2. **Asistente IA conectado a inventario real con disponibilidad** — Peerspace y SpacePal no lo tienen en español/Latam. Costo y tiempo de réplica: 6+ meses.
3. **Pago Yape/Plin nativo + SUNAT** (cuando se active la transacción on-platform en post-MVP) — un competidor regional tarda 3-6 meses en levantar la integración.
4. **Conocimiento del mercado local** — el owner conoce hosts, proveedores, distritos, dinámicas de eventos peruanos. SpacePal está en Buenos Aires.
5. **Scrape & Claim** (Fase 6) — al momento de activarlo, ya tendremos brand + tráfico, así que cada host contactado convierte mejor que un cold call de competidor nuevo.

---

## Resumen ejecutivo del Canvas

- **Negocio**: lead-gen marketplace + agencia de eventos.
- **MVP scope**: catálogo Lima + asistente form + onboarding host gratis + dashboard interno de leads.
- **Sin pagos en plataforma** (MVP).
- **Geografía MVP**: solo Lima.
- **North star**: leads calificados/mes a la agencia.
- **Riesgo principal**: el modelo no escala con código sino con personas operando la agencia.
- **Tiempo a primer lead pagado**: 4-6 semanas.
