# Conclusión de mercado — qué hay, qué falta, dónde podemos jugar

**Fecha:** mayo 2026
**Audiencia:** equipo fundador Space-Peru — base para Fase 2 (PRD MVP)
**Insumos:** documentos `01-resumen-ejecutivo.md`, `04-mapa-de-soluciones.md`, `05-empresas-listadas.md`, archivos `competidores/`, `personas/`, `pricing/`, `research/`.

---

## A. ¿Qué existe hoy?

El mercado mundial de **alquiler de espacios por horas** está consolidado en torno a tres patrones de negocio claros: marketplace transaccional con comisión (Peerspace 20% host, Tagvenue 12.5-15%, Giggster 19%, Splacer 17%, SpacePal 0%+12%), directorio con suscripción al venue (Eventective, Compartir Espacios, Ineventos, Bodas.com.mx) y operador asset-heavy (Breather†, Comunal, WeWork). Los marketplaces asset-light dominan; los asset-heavy quebraron en COVID (Breather quemó >US$130M y se vendió por US$3M en 2021). En total el doc 05 lista **45 jugadores** entre globales (13), Latam ex-Perú (10), Perú (17) y adyacentes (5).

En **Latinoamérica** el referente único es **SpacePal** (Argentina, fundada oct-2023, 40k+ espacios globales, US$500-700k facturados en 18 meses, modelo 0% host + 12% guest). Comunica presencia en 22 países pero con catálogo desigual: tracción real CDMX/Buenos Aires; catálogo Lima esencialmente vacío (verificado mayo 2026: la búsqueda `space-pal.com/es/search/Lima--Peru/Espacios` muestra "no hay espacios encontrados"). El resto de Latam aporta jugadores adyacentes — Around (MX) con modelo "espacio dormido corporativo", Co-Work LatAm (Chile/Colombia/Uruguay) operando coworking propio, Bodas.com.mx vertical bodas — pero ninguno transacciona alquiler de espacio por horas en Perú.

En **Perú** específicamente el paisaje es: (1) ningún marketplace transaccional vertical local; (2) directorios lead-gen con SEO bueno pero UX 2010 que terminan derivando a teléfono/WhatsApp del host (Compartir Espacios, Ineventos, Roodos); (3) operadores premium B2B con su propio inventario (Comunal 15 sedes, WeWork, Worx, Regus, Swiss Rents); (4) el verdadero competidor — la **economía informal de WhatsApp + Instagram + grupos de Facebook + Yape**, que captura la mayoría del flujo NSE B/C+ y que funciona pero tarda días, no genera reputación verificada y depende del tiempo de respuesta del host.

---

## B. ¿Cómo se resuelve el problema hoy?

### Flujo dominante en Lima (detalle en `04-mapa-de-soluciones.md`)

1. **Descubrimiento:** Instagram (hashtag o publicidad pagada del host) o grupo de Facebook → Google que aterriza en directorio o sitio del propio salón.
2. **Cotización:** DM de Instagram o WhatsApp al host. El host responde con foto, precio y disponibilidad. Mediana de respuesta: ~6 horas en hábil, peor en fin de semana.
3. **Visita opcional** si el evento es grande.
4. **Cierre:** Yape de 50% como adelanto, saldo el día del evento. Sin contrato firmado, "queda hablado por WhatsApp". Garantía en efectivo opcional.
5. **Día del evento:** se completa el pago, se usa el espacio.
6. **Post-uso:** agradecimiento por WhatsApp; <5% deja reseña pública. Re-booking directo con el host la próxima vez.

**Ciclo total típico:** 2-5 días desde búsqueda hasta confirmación. Funciona, pero es manual, sin trazabilidad y no acumula memoria de mercado.

### Flujo en mercados maduros (Peerspace US, Tagvenue UK)

1. **Descubrimiento:** búsqueda dentro de Peerspace por **caso de uso** ("wedding photo shoot", "team off-site", "podcast recording") + filtros estructurados (capacidad, layout, amenities, precio/hora).
2. **Selección:** detalle del espacio con foto de calidad cinematográfica, calendario de disponibilidad real-time, reseñas con foto del evento, SLA visible del host ("responde en 1 hora").
3. **Reserva:** "instant book" o "request to book" → mensajería integrada → host confirma → checkout con tarjeta → seguro de daños incluido.
4. **Post-booking:** reseña bidireccional (host califica al guest, guest al host), booking history queda en cuenta del usuario.

**Ciclo total típico:** 15 minutos desde búsqueda hasta confirmación con instant book.

### Brecha entre los dos mundos

El usuario peruano de NSE A/B+ que ya viajó y usó Airbnb/Peerspace en el extranjero **espera el flujo maduro pero recibe el flujo informal en su propia ciudad**. Esa frustración es el wedge psicológico de Space-Peru.

---

## C. ¿Qué falta / dónde está el gap?

### Gap 1 — Ningún marketplace transacciona end-to-end en Perú
De los 45 jugadores listados, **cero** combinan: (a) catálogo multi-host, (b) calendario de disponibilidad real-time, (c) booking instantáneo, (d) pago integrado, (e) confirmación automática, (f) reseña post-booking. Compartir Espacios e Ineventos son directorios; Comunal/WeWork son operadores propios; Mercado Libre tiene UX inadecuada para horas; SpacePal tiene la UX pero no el inventario Lima; los grupos FB son informales. **Evidencia:** doc 05 columna "Modelo".

### Gap 2 — Space-Pal Lima está vacío y eso le abre la ventana
SpacePal es el único marketplace regional con el producto correcto pero su catálogo Lima es marginal: empty state en búsqueda general (verificado mayo 2026), 12 espacios en categoría Party. Los fundadores son argentinos sin equipo en Lima. **Implicancia:** ventana de 12-18 meses para construir liderazgo local antes de que SpacePal invierta seriamente o que Peerspace decida entrar.

### Gap 3 — Cero plataformas con Yape/Plin nativo en checkout
Yape tiene 15M+ usuarios y comisión 2.95%; Plin compite; Culqi soporta ambos en checkout integrado. Ningún marketplace de espacios en Perú integra esto en flujo en plataforma. SpacePal usa pasarela genérica regional (probable Stripe/MercadoPago); Compartir Espacios no procesa pago; los coworkings premium aceptan tarjeta pero no Yape. **Esto descalifica a 50%+ del NSE B/C** que prefiere Yape como default.

### Gap 4 — Cero verificación humana de espacios en Lima
SpacePal es self-serve: el host sube fotos y publica. Compartir Espacios igual. Los grupos FB son tierra de nadie. No existe "este espacio fue verificado físicamente por nuestro equipo" como sello de confianza. En un mercado pequeño donde una mala experiencia se viraliza en grupos de WhatsApp en 24h, **la curaduría es moat**.

### Gap 5 — Cero plataformas con WhatsApp como canal nativo del producto
Peerspace y SpacePal usan email + dashboard. En Perú el dueño del salón no abre el dashboard pero responde WhatsApp en 5 minutos. Ningún jugador en Latam (verificado en doc 05) tiene WhatsApp Business API integrado para confirmaciones, recordatorios, soporte y mensajería host-guest. **Es ventaja cultural defendible.**

### Gap 6 — Cero plataformas con factura SUNAT automática para guest corporativo
El guest B2B (sala de reuniones para empresa, capacitación, off-site) necesita factura electrónica con IGV. Comunal/WeWork lo tienen en flujo propio porque son operadores. Ningún marketplace lo emite automatic en checkout. Resultado: el corporativo va a Comunal directo y no usa marketplace. **Gap de US$4M-12M anuales en revenue B2B no servido vía marketplace.**

### Gap 7 — Cero plataformas que estructuren el descubrimiento por **caso de uso** en Lima
Los directorios peruanos categorizan por tipo de espacio ("salón de eventos", "estudio fotográfico"). Peerspace y Splacer categorizan por intención del guest ("baby shower", "podcast recording", "team off-site"). El usuario peruano busca con la misma intención pero no encuentra UI que la respete. **Implicancia producto:** taxonomía dual (tipo + caso de uso) como diferenciador de búsqueda.

### Gap 8 — Sub-categorías nicho con demanda real y cero plataforma
Pop-up retail temporal (Storefront en US, ningún equivalente Latam), salas de yoga/clases con disponibilidad por hora (Casa Ninfa cobra S/50-70/h en Instagram, sin plataforma), espacios para grabación de podcast/contenido creator (mercado emergente Lima sin oferta agregada). Cada uno es vertical de v2.

### Gap 9 — Cero programa de cuentas corporativas B2B con presupuesto pre-pagado
ShareDesk (US) lo tiene: empresa pre-paga US$X mensual, sus empleados reservan salas contra ese saldo. En Lima ningún jugador lo ofrece. ARPU corporativo es 5-10x el del guest individual y la retención es mucho mayor.

---

## D. ¿Dónde podemos jugar?

Tres opciones de posicionamiento ranqueadas con tradeoffs.

### Opción 1 — Marketplace vertical "salones de eventos sociales en Lima Moderna" (RECOMENDADA)

**Tesis:** "Peerspace para Perú, mobile-first, Yape/Plin nativos, verificación humana, WhatsApp como canal de operación. Lanzamos en una sola vertical (eventos sociales: cumpleaños, baby showers, despedidas) en 8 distritos."

- **Pro:** scope estrecho, mercado direccionable claro, demand visible en grupos FB e Instagram, supply concentrado en Miraflores/Barranco/Surco/Magdalena, ticket promedio S/300-1.500 por evento, frecuencia repetida (un usuario hace 2-4 eventos/año).
- **Pro 2:** llegamos primero antes de SpacePal y los gaps 1-7 se atacan en paralelo.
- **Contra:** TAM Lima vertical eventos sociales ~US$15-30M anuales (subset del total US$30-80M); revenue 12-18% take rate ⇒ techo realista US$2-5M/año en estado maduro Lima sola.
- **Riesgo:** SpacePal despierta a los 12 meses y ataca con 0% comisión host como precio de guerra.
- **Mitigación:** moat es curaduría + pago local + relación humana, no take rate.

### Opción 2 — Marketplace B2B horizontal "salas de reunión + capacitación corporativa"

**Tesis:** "ShareDesk para Perú. Cuentas corporativas pre-pagadas. Inventario agregado de Comunal + WeWork + Worx + Regus + Swiss Rents + ~50 salas independientes."

- **Pro:** ARPU 5-10x mayor, retención corporativa alta, factura SUNAT default, ciclo de venta B2B conocido.
- **Pro 2:** los operadores premium ya quieren canal adicional para llenar fines de semana / horarios muertos — partner natural.
- **Contra:** los operadores también pueden no querer entregar la relación con el cliente (mismo problema de OTAs en hotel).
- **Contra 2:** mercado más chico y maduro; competimos contra el "ya llamo a Comunal directo".
- **Riesgo:** WeWork/Comunal lanzan su propio marketplace ofertando inventario propio + de terceros.

### Opción 3 — Marketplace horizontal multi-categoría desde día 1 (estilo SpacePal/Peerspace)

**Tesis:** "El SpacePal de Perú, hecho desde Lima. 6 categorías desde día 1 (eventos sociales + corporate + foto + yoga + producción + pop-up)."

- **Pro:** cobertura amplia de demand y supply, captura cualquier intención.
- **Contra:** scope demasiado ancho para MVP, equipo se distrae, ninguna vertical alcanza liquidez crítica, riesgo de quedar como SpacePal Lima (todo y nada).
- **Riesgo:** quemamos runway sin alcanzar marketplace liquidity en ninguna vertical.

### Recomendación final

**Opción 1.** La aritmética startup dice que la vertical estrecha con liquidez supera al horizontal raquítico. Cuando tengamos 200 espacios verificados de eventos sociales en 8 distritos y 500 bookings pagados/mes, agregamos vertical 2 (corporate B2B) y vertical 3 (foto/producción) — no antes.

**Justificación:**
- Vertical eventos sociales tiene la demand más visible (grupos FB con decenas de miles de miembros, búsquedas Google long-tail), supply más fragmentado (ergo más valor de agregación) y ticket suficiente para take rate sano.
- Vertical corporate (Opción 2) es mejor revenue per booking pero la relación con los 5-6 operadores premium es política — esperamos a tener flywheel para ofrecerles "agreguen su inventario muerto" desde posición de fuerza.
- Horizontal (Opción 3) muere por dilución — la lección Breather y la lección SpacePal Lima.

**Take rate inicial recomendado** (consistente con `pricing/modelo-monetizacion.md`):
- Mes 1-6: **0% host + 12% guest** (replicar SpacePal para captar supply rápido).
- Mes 7-12: **5% host + 12% guest** = take rate 17%.
- Mes 13+: **15% host + 5% guest** = take rate 20% (paridad Peerspace cuando flywheel esté probado).

**Cobertura geográfica MVP:** 8 distritos Lima Moderna (Miraflores, San Isidro, Barranco, Surco, San Borja, La Molina, Magdalena, Pueblo Libre). Concentran ~80% del NSE A/B y de la oferta premium.

**Métricas de cierre Fase 2 (PRD):**
- North star: bookings pagados/mes.
- KPIs: # espacios verificados, % bookings con Yape, NPS guest, time-to-booking (mediana de minutos desde discovery hasta confirmación).

---

## Hallazgos sorprendentes (vs research previo)

1. **LiquidSpace cobra 50% al guest en su primera booking** (luego 25%, luego 10%) — modelo tiered raro pero potencialmente innovador para enganchar primer booking sin sacrificar margen long-term.
2. **Storefront fue adquirida por PopUp Immo en 2023** — el pop-up retail vertical se consolidó vía M&A, no quebró; señal de que el mercado vertical genera salida líquida.
3. **VenueScanner UK declara "0% comisión" pero levantó £800k** — modelo monetización opaco, probable revenue share oculto al venue. Lección: "0% comisión" es marketing, no modelo sostenible.
4. **Around (MX) descubrió un canal de supply nuevo:** empresas alquilan su excedente de oficina a otras empresas. Es supply asset-light que ningún competidor en Lima toca.

## `[a validar]` críticos antes de Fase 2

- Take rate exacto post-adquisición de Storefront (PopUp Immo).
- Comisión real de Around (MX) y modelo de revenue share con la empresa anfitriona.
- Cuántos espacios SpacePal lista hoy en Lima por categoría (conteo manual visitando cada categoría — pendiente).
- Modelo monetización real de VenueScanner UK (las £800k de levantamiento sugieren que cobran al venue de alguna forma).
- Tamaño exacto de los grupos Facebook clave de eventos Lima (miembros activos).

## Fuentes

- `analisis-mercado/01-resumen-ejecutivo.md`
- `analisis-mercado/04-mapa-de-soluciones.md`
- `analisis-mercado/05-empresas-listadas.md`
- `analisis-mercado/competidores/space-pal.md`
- `analisis-mercado/competidores/internacionales.md`
- `analisis-mercado/competidores/otros-peru.md`
- `analisis-mercado/pricing/modelo-monetizacion.md`
- `analisis-mercado/research/oportunidades-diferenciacion.md`
- https://space-pal.com/es/search/Lima--Peru/Espacios (verificado mayo 2026)
- https://thelogic.co/news/the-big-read/out-of-breath-inside-breathers-rise-and-fall/
- https://liquidspace.com/how-it-works
- https://splacer.zendesk.com/hc/en-us/articles/207909669-Does-Splacer-charge-a-commission-How-is-it-calculated-
- https://www.eventective.com/how-it-works/
- https://www.venuescanner.com/list-your-venue
- https://startupslatam.com/spacepal-la-plataforma-que-revoluciona-el-alquiler-de-espacios-para-eventos/
- https://www.elespanol.com/invertia/disruptores-innovadores/america-tech/mexico/20210629/around-oficina-flexible-america-latina-empresas-espacio/592441071_0.amp.html
