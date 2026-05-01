# Modelo de monetización — comparativa y recomendación

## 1. Opciones disponibles

### A. Comisión por booking (transactional take-rate)

Modelo dominante en marketplaces de espacios. Variantes:

| Plataforma | Host fee | Guest fee | Take-rate efectivo |
|---|---|---|---|
| Peerspace | 20% | Variable (5-15% según subtotal) | ~25-28% |
| Tagvenue | 12.5% (dining) / 15% (meetings) | 0% | 12.5-15% |
| SpacePal | 0% | 12% | 12% |
| Splacer | ~15% [a validar] | ~6.5% | ~21% |
| Airbnb (referencia) | 3% (host) + 14% (guest) | 14% | ~17% |

**Pros:**
- Alineación de incentivos: ganamos cuando ellos ganan.
- Escalable, no requiere supply pague upfront.
- Estándar global, fácil de explicar.

**Contras:**
- Hosts grandes (Comunal, WeWork) renegocian o no aceptan.
- Susceptible a "leak off-platform" (cliente y host se conocen y siguiente vez se pagan directo por Yape — pierdes).

### B. Membresía / listing fee del host

Modelo Tagvenue Premium / Eventbrite Pro:
- Host paga S/X/mes para tener listing destacado, foto pro, prioridad de búsqueda.
- Sin comisión por booking, o comisión muy baja (3-5%).

**Pros:**
- Ingreso recurrente predecible (MRR).
- Mejor para hosts de alta facturación que no quieren take-rate alto.

**Contras:**
- En mercado naciente, hosts no pagan upfront por algo que aún no produce leads.
- Requiere catálogo grande primero (chicken-and-egg agudo).

### C. Lead-gen / pay-per-inquiry

Modelo Ineventos.pe / Tripadvisor:
- Plataforma cobra al host por cada lead/contacto generado.
- No transacciona, no maneja pago.

**Pros:**
- Cero fricción para construir directorio rápido.
- Bajo costo operativo.

**Contras:**
- **Es exactamente lo que queremos disrumpir.** No genera trust, no genera retención, no genera datos de booking real. Ineventos.pe lleva años así y no es marketplace, es Yellow Pages.

### D. Freemium / planes mixtos

- Listing gratis (catálogo amplio).
- Pago opcional por: (i) destacar listing (ads), (ii) foto pro, (iii) instant book privilege, (iv) badge "verificado".

**Pros:**
- Captura supply sin fricción.
- Monetización adicional sobre take-rate.

**Contras:**
- Complejidad operativa, riesgo de UX confusa.

### E. Servicios adicionales (verticalización)

- Catering, seguros, equipo AV, fotógrafo del evento.
- Markup 10-25% sobre servicio.

**Pros:**
- ARPU más alto. Diferenciación.

**Contras:**
- Operacionalmente pesado. Mejor para fase 2.

## 2. Sensibilidad cultural en Perú

- **El host peruano percibe la comisión como "te quito plata mía".** A 20% explota; a 10-12% lo acepta a regañadientes; a 0% (con guest fee) lo encuentra "raro pero conviene".
- **El guest peruano sí entiende fee de servicio** (lo paga ya en Uber, Rappi, PedidosYa, MercadoLibre). 5-10% guest fee no asusta.
- **Pago en cuotas (3-12) es estándar** en compras >S/200 con tarjeta. Plataforma debe ofrecerlo (Culqi, Niubiz lo soportan).

## 3. Recomendación inicial para el MVP

**Modelo híbrido split asimétrico, fase 1:**

- **Comisión host: 15%** (negociable a 10% para anchor tenants en fase de captación de supply).
- **Fee guest: 5%** (visible, llamado "fee de servicio").
- **Take-rate efectivo: ~19%** sobre el subtotal (similar a Splacer, mejor margen que SpacePal y Tagvenue).
- **Listing gratis. Foto profesional gratis** para los primeros 200 hosts (CAC supply).
- **Sin guest fee en bookings <S/300** para no espantar al low-ticket (clase de yoga 2 horas).

### Justificación

- 15% al host es **mejor que Peerspace (20%)** y **peor que SpacePal (0%)** — vendible como "comisión justa, no abusiva".
- 5% al guest es **mucho menor que SpacePal (12%) y Peerspace (variable)** — ventaja competitiva visible en el precio final mostrado.
- En ticket promedio de salón evento social Lima ~S/2.000/booking: nuestro revenue = ~S/400/booking. Suficiente para cubrir CAC + ops.

### Promociones lanzamiento (primeros 6 meses)

- **0% comisión host** los primeros 90 días post-listing → para vencer al "te cobro nada" de SpacePal en captación.
- **Cashback al guest** 5% en su segundo booking (retención).
- **Programa referido:** S/50 al referidor cuando el referido completa su primera reserva.

## 4. Roadmap monetización (12-18 meses)

| Mes | Movimiento |
|---|---|
| 0-3 | 0% comisión host launch promo + 5% guest fee. |
| 3-6 | 10% comisión host, mantengo guest 5%. |
| 6-12 | 15% comisión host estándar; sigue 5% guest. Foto pro paga (S/250 one-off) opcional. |
| 12-18 | Plan "Pro Host" suscripción S/49-149/mes (badge, prioridad búsqueda, ads). Servicios verticales (catering, AV) en bookings premium. Cuentas corporativas B2B con presupuesto pre-cargado. |

## 5. Métrica clave

**Take-rate %** y **GMV (gross merchandise value)** son las dos métricas norte. Margen contribución por booking debe llegar a >12% en 9 meses para ser sostenible. CAC blended < S/80 por booking en mes 12.

## Fuentes

- https://support.peerspace.com/en/articles/10119442-what-is-the-peerspace-service-fee
- https://support.tagvenue.com/hc/en-gb/articles/360018025377-What-is-the-Tagvenue-commission
- https://space-pal.com/support/en/articles/8583819-how-does-spacepal-make-money
- https://www.peerspace.com/legal/terms/fees-overview
- Marketplace business model frameworks: https://truust.io/blog/marketplace-business-models-examples-and-analysis/
- https://jordinoguera.substack.com/p/reflexionando-sobre-marketplaces
