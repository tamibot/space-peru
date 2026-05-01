# Resumen Ejecutivo — Mercado de alquiler de espacios por horas en Perú (Lima)

**Fecha:** mayo 2026
**Audiencia:** equipo fundador del MVP (alternativa a Space-Pal en Perú)

## 1. Qué es este mercado

Marketplace de **alquiler de espacios por horas (no estadías):** salones de eventos, salas de reuniones, estudios fotográficos/audiovisuales, salas de yoga/clases, espacios para pop-ups, lofts, terrazas. El usuario reserva por bloques de 2-8 horas, no por noche. Es una categoría hermana de Airbnb pero con dinámica distinta: ticket más bajo, frecuencia mayor por usuario activo, supply mucho más fragmentado (una sala de reunión + un loft + un gimnasio sirven a usuarios diferentes).

Referente global: **Peerspace** (US, 40k+ espacios, comisión 20% host + fee variable guest). Referente latam que compite directamente: **SpacePal** (Argentina, fundada oct-2023, ya en Lima/Bogotá/CDMX/Santiago, 40k+ espacios listados globales, US$700k facturado en 18 meses, modelo "0% comisión host + 12% guest fee").

## 2. La oportunidad en Lima

- **Demanda fragmentada y desatendida digitalmente.** Hoy en Lima el booking se resuelve en **WhatsApp + Instagram + grupos de Facebook + Mercado Libre**, con cotización manual por DM y pago por Yape/transferencia. No existe una experiencia "buscar → ver disponibilidad → reservar y pagar en 3 minutos" para espacios por horas.
- **SpacePal Lima está flojo de inventario.** Una búsqueda directa en `space-pal.com/es/search/Lima--Peru/Espacios` arroja "no hay espacios encontrados" en el listado general (verificado). La página de "Party venues" anuncia 12 espacios. Comparado con CDMX/Buenos Aires el catálogo Lima es marginal: ventana clara para construir liderazgo local antes de que el incumbente regional invierta seriamente.
- **Coworkings ya tienen tracción.** Comunal opera 15 sedes y 100+ salas en Lima desde ~US$25/hora; WeWork en Miraflores y San Isidro; Worx en Larco. Pero su sala se reserva por su web/teléfono, no en marketplace. Hay supply listo para "agregar canal".
- **Categorías nicho con demanda real:** estudios fotográficos cobran S/45-80/hora (Compartir Espacios, Magda, Bark, NV), salas de yoga ~S/50-70/hora (Casa Ninfa), salones de baile y locales para fiestas en Miraflores/Barranco. Cada uno tiene su micro-mercado en Instagram.
- **Stack de pago local maduro:** Yape (15M+ usuarios, comisión 2.95%), Plin, Culqi (3.44%+IGV tarjetas/wallets, mismo día payout) y MercadoPago. Permite checkout completo sin fricción cultural.

## 3. Tamaño estimado (orden de magnitud, [a validar])

- **Hogares NSE A/B Lima Metropolitana:** ~600k [a validar con APEIM 2025/2026]. Consumo de eventos sociales/profesionales por hogar A/B: ~2-4 al año.
- **Empresas formales en Lima:** 800k-900k unidades activas [a validar SUNAT/INEI]. Necesidades recurrentes de salas de reuniones externas, capacitaciones, off-sites, lanzamientos.
- **Gross Bookings Value direccional para el sub-segmento direccionable:** entre **US$30M-80M anuales** combinando salones de eventos sociales, salas profesionales, estudios y espacios de fiesta [a validar — modelar bottom-up con # espacios × ocupación × ticket promedio].
- **Take-rate marketplace alcanzable:** 12-18% combinado (host + guest) → revenue potencial **US$4M-12M/año** en estado maduro Lima sola.

## 4. Posicionamiento recomendado para el MVP

**Tesis:** "Peerspace para Perú, mobile-first, con Yape/Plin nativos y verificación humana."

Tres pilares de diferenciación sobre SpacePal en Lima:

1. **Pago 100% local sin fricción.** Checkout que acepta Yape/Plin/QR + tarjeta vía Culqi, factura electrónica SUNAT automática para el guest corporativo, payout al host por CCI en 24-72h. SpacePal hoy no tiene pago local visiblemente integrado en flujo Lima.
2. **Curaduría humana + verificación física antes de listar.** Visita presencial a los primeros 100-300 espacios. Foto profesional incluida. Esto es el moat: catálogo de 200 espacios verificados > 2.000 espacios fantasma.
3. **WhatsApp-first, no email-first.** Notificaciones, confirmación de reserva y soporte por WhatsApp Business API. Es el canal default del peruano. El host responde desde su celular en 5 min, no desde un dashboard que no abre.

**Categorías de lanzamiento sugeridas (ranking detallado en `research/categorias-prioritarias.md`):**
1. Salones de eventos sociales (cumpleaños, baby showers, despedidas)
2. Estudios fotográficos / locaciones de producción audiovisual
3. Salas de reuniones / capacitación corporativa

**Cobertura geográfica MVP:** 8 distritos eje Lima Moderna (Miraflores, San Isidro, Barranco, Surco, San Borja, La Molina, Magdalena, Pueblo Libre) — concentran ~80% del NSE A/B y de la oferta premium.

## 5. Recomendación

**Sí, hay ventana.** El incumbente regional (SpacePal) llegó pero no profundizó en Perú. La demanda existe, está dispersa en canales informales y paga hoy por estos espacios; el problema es de descubrimiento y confianza, no de willingness to pay. Construir un MVP **con verificación humana, pago Yape/Plin, WhatsApp como canal de operación y enfoque vertical (lanzamos eventos sociales primero, no 10 categorías)** puede capturar liderazgo local en 12-18 meses antes de que SpacePal o Peerspace inviertan en serio en Perú.

Comisión inicial recomendada: **15% host + 5% guest = take-rate ~19%**. Detalle en `pricing/modelo-monetizacion.md`.

## Fuentes

- https://blog.emprelatam.com/2025/09/25/spacepal-startup-que-hace-el-alquiler-de-espacios-tan-facil-como-pedir-un-uber/
- https://startupslatam.com/spacepal-la-plataforma-que-revoluciona-el-alquiler-de-espacios-para-eventos/
- https://space-pal.com/support/en/articles/8583819-how-does-spacepal-make-money
- https://support.peerspace.com/en/articles/10119442-what-is-the-peerspace-service-fee
- https://comunal.co/es-PE/
- https://www.wework.com/l/meeting-rooms/lima
