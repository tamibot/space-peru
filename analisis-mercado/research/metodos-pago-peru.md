# Métodos de pago en Perú — qué aceptar en el MVP

## Panorama del consumidor 2025-2026

- **Yape: ~15M usuarios activos** (≈45% adultos PE). Penetración masiva NSE A/B/C.
- **Plin** (BCP/BBVA/Interbank/Scotiabank P2P) crece rápido en NSE B/C.
- **Tarjetas:** ~50% adultos tienen tarjeta de débito y ~30% de crédito [a validar — fuente BCRP/SBS 2025/2026].
- **Cash:** se reduce pero sigue ~30% de pagos minoristas. Para marketplaces digitales no aplica directamente, pero sí vía PagoEfectivo.
- **Tendencia BCRP 2025:** comisiones medias adquirentes bajaron de 2.21% → 2.17%; facilitadores de 3.15% → 2.83%.

## Stack de procesamiento — opciones

### 1. Culqi (https://culqi.com/)

- Pasarela peruana (Credicorp).
- Acepta: tarjetas Visa/MC/Amex/Diners, **Yape**, **billeteras locales**, cuotas sin interés.
- **Comisión:** 3.44% + IGV en tarjetas nacionales y wallets (Yape/Plin); 3.99% + IGV en tarjetas internacionales.
- **Payout:** mismo día (T+0) bajo ciertas condiciones.
- **Pros:** stack peruano nativo, integración Yape oficial, factura de comisión SUNAT, soporte en español.
- **Contras:** Yape vía Culqi requiere flujo "código de aprobación" (no es 1-click puro).

### 2. Niubiz (https://www.niubiz.com.pe/)

- Procesador histórico Perú (ex VisaNet).
- Acepta: tarjetas, cuotas, BIM.
- **Comisión:** 3-3.5% [a validar tarifa actual exacta].
- **Pros:** aceptación universal, marca instalada en comercio.
- **Contras:** UX más anticuada; Yape no nativo.

### 3. MercadoPago

- Plataforma regional muy fuerte en Argentina/México, también en Perú.
- Acepta: tarjetas, MercadoPago wallet, cuotas, links de pago.
- **Comisión:** ~3.5-4% + IGV.
- **Pros:** integraciones existentes, dashboard sólido.
- **Contras:** **no integra Yape/Plin nativamente** — gap crítico para Perú.

### 4. PayU / OpenPay / dLocal / Stripe Connect

- Internacionales con cobertura Perú.
- **Comisión:** 3.5-4.5%.
- **Stripe Connect:** ideal para split payments multi-host (modelo Tagvenue), pero Yape/Plin no nativo.
- **Pros:** stack moderno, split payment, escalable a otros países.
- **Contras:** sin Yape/Plin = gap UX para audiencia peruana.

### 5. Yape Negocios + Plin para comercio

- Yape Negocios permite **API de cobro online con código de aprobación**. Comisión sobre venta digital ~**2.95%**.
- Plin para comercio: integraciones vía pasarelas terceras.
- **Pros:** comisión más baja que tarjeta, alta penetración usuario.
- **Contras:** UX de "pegar código de 6 dígitos" — más fricción que tarjeta guardada; no soporta cuotas.

### 6. PagoEfectivo / SafetyPay

- Cash voucher: cliente paga en efectivo en BCP/BBVA/agentes.
- **Comisión:** ~2-3%.
- **Pros:** cubre el segmento sin bancarización digital.
- **Contras:** flujo asíncrono (paga en X horas o el booking se cae). Solo para bookings con anticipación >24h.

## Cuotas (clave en Perú)

- Cliente peruano espera **cuotas sin interés 3/6/12** en compras >S/300 con tarjeta.
- Visa/MC ofrecen "cuotas" que el comercio absorbe como costo (~3-5% extra).
- Para tickets >S/1.000 (salones eventos), ofrecer cuotas sube conversión 20-40% [benchmark e-commerce LATAM, a validar Perú].

## Recomendación de stack para MVP

**Combinación híbrida:**

| Método | Procesador | % Comisión efectivo | Prioridad |
|---|---|---|---|
| Tarjeta crédito/débito (con cuotas) | **Culqi** | 3.44% + IGV | Día 1 |
| **Yape** | **Culqi (nativo) o Yape Negocios direct** | 2.95% + IGV | Día 1 |
| Plin | Vía Culqi/pasarela | 3% [a validar] | Mes 3 |
| MercadoPago wallet | MercadoPago | 3.5-4% | Mes 6 (opcional) |
| PagoEfectivo | PagoEfectivo | 2-3% | Mes 6 (opcional, caso bookings >48h) |

**Justificación:** Culqi como ancla porque integra tarjeta + Yape + cuotas en una sola integración nativa peruana con factura SUNAT incluida. Mantenemos hooks para Stripe Connect en backend (split payment con hosts) — Stripe procesa tarjetas internacionales, Culqi procesa locales.

## Costos efectivos para el MVP (modelaje)

- Comisión promedio ponderada estimada: ~3.2% + IGV.
- En un booking de S/2.000:
  - Cobro guest: S/2.100 (incluye 5% guest fee = S/100).
  - Procesamiento (3.2% + IGV): ~S/79.
  - Comisión nuestra (15% host + 5% guest sobre S/2.000): S/400.
  - **Margen contribución por booking:** ~S/321 antes de CAC y ops.

## Payout al host

- **CCI peruano** (BCP, BBVA, Interbank, Scotiabank) vía SPID o transferencia interbancaria.
- **Yape Negocios** para hosts mini que no quieren CCI.
- **Frecuencia:** T+1 o T+3 desde la fecha del booking realizado (no la fecha de cobro). Modelo Peerspace = 7 días post-evento; nosotros podemos ser más agresivos T+1 = ventaja competitiva.

## Aspectos KYC / anti-fraude

- Captura de DNI del host al onboardear.
- Validación CCI vs RUC del host.
- Flag de bookings >S/5.000 para revisión manual.
- Política anti-chargeback con seguro vía Culqi (3D Secure obligatorio en bookings >S/500).

## Fuentes

- https://www.ecommercenews.pe/pagos-online/2025/pasarela-de-pagos-en-peru.html/
- https://culqi.com/
- https://www.yape.com.pe/preguntas-frecuentes/compras-por-internet/como-puedo-tener-la-opcion-de-compras-por-internet-codigo-de-aprobacion-yape-en-l
- https://huako.tech/blog/integracion-de-woocommerce-con-pasarelas-de-pago-locales-yape-plin-ligo-bbva-qr-mercado-pago-culqi-niubiz-y-mas/
- https://ecommerceacademy.pe/pasarelas-de-pago-en-peru-2025-comparativa-completa-de-culqi-niubiz-mercado-pago-y-payu/
- https://www.kunan.com.pe/pasarelas-de-pago-para-ecommerce-en-peru-comisiones-tiempos-de-abono-y-cual-elegir/
- https://www.rebill.com/blog/pasarelas-pago-peru
- BCRP datos pagos digitales Perú 2025 [a validar URL específica].
