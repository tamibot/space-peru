# Oportunidades de diferenciación vs SpacePal en Perú

7 ángulos donde SpacePal en Lima hoy es flojo y donde podemos construir ventaja defendible.

---

## 1. Pago 100% local nativo: Yape + Plin + tarjeta + cuotas

**El gap:** SpacePal hoy no muestra integración visible con Yape o Plin en flujo Lima. Probablemente procesa con Stripe + MercadoPago genérico.

**Por qué importa:**
- Yape tiene **15M+ usuarios** en Perú (≈45% de la población adulta) y comisión 2.95%.
- 30-50% de transacciones de bajo ticket B2C en Perú prefieren billetera digital sobre tarjeta.
- En NSE B/C, "no acepta Yape" es señal de "no es de acá, no confío".

**Nuestra jugada:**
- Checkout con 4 métodos visibles: **Yape, Plin, tarjeta (Culqi), pago en cuotas (3-12 sin interés)**.
- Confirmación instantánea por WhatsApp tras pago Yape (Yape API admite código de aprobación).
- Pricing mostrado siempre en soles, fee separado y explícito.

---

## 2. Verificación humana del 100% de los espacios listados

**El gap:** SpacePal y la mayoría de marketplaces son self-serve — el host sube fotos, llena descripción, listo. Esto genera "espacios fantasma", fotos de Pinterest, capacidad inflada, no-shows.

**Por qué importa:**
- En Latam el guest tiene **menos confianza online** que en US/EU. La señal "verificado por equipo humano" mueve la conversión.
- El primer mal review viraliza más rápido en mercado pequeño.

**Nuestra jugada:**
- Visita presencial obligatoria primeros 200 espacios.
- Foto profesional incluida (CAC supply).
- Badge "Verificado en sitio" (sello en perfil + filtro de búsqueda).
- Encuesta post-booking al guest sobre fidelidad foto vs realidad → si baja de 4.5/5, re-verificación.

**Costo:** ~S/200-300 por espacio (transporte + fotógrafo 2 horas). Si lifetime value de un host activo > S/3.000, payback < 2 meses.

---

## 3. WhatsApp como capa de comunicación primaria

**El gap:** SpacePal usa email + chat in-app. En Perú, el host promedio **no abre el dashboard** — abre WhatsApp 80 veces al día.

**Nuestra jugada:**
- WhatsApp Business API + bot híbrido para:
  - Notificación de booking ("Llegó reserva de Camila para el sábado 15-20h, S/1.800. Confirma con SÍ").
  - Recordatorio del check-in del guest.
  - Soporte 1-on-1 directo con operador humano.
- Reportes diarios al host por WhatsApp ("hoy tienes 2 inquiries y 1 booking confirmado").
- Cliente final puede escribir a un número WhatsApp del marketplace para SOS.

---

## 4. Factura electrónica SUNAT integrada en checkout

**El gap:** ningún marketplace internacional resuelve facturación electrónica peruana out-of-the-box. Esto **descalifica** todo el segmento B2B (Camila la persona corporativa).

**Nuestra jugada:**
- Integración con proveedor SUNAT (Nubefact, Facele, Efact).
- Guest puede pegar RUC al checkout → factura electrónica emitida en 60 segundos al email/WhatsApp.
- Modelo dual host (ver `research/legal-regulacion.md`): plataforma puede facturar como agente, o el host factura desde su RUC vía nuestro sistema.

---

## 5. Curaduría editorial por categoría con tono local

**El gap:** SpacePal mezcla en un dropdown "consultorio médico", "estudio fotográfico", "salón de fiestas". UX confusa.

**Nuestra jugada:**
- Lanzar verticalizado: **3-4 categorías inicialmente** con homepages dedicadas (`/eventos`, `/audiovisual`, `/salas-corporativas`, `/wellness-clases`).
- Contenido editorial: "Top 10 lofts retro en Barranco para tu shoot de marca", "Salones para baby shower en La Molina <S/1.500".
- Voz local: usa "movida", "tonazo", "pampero", "cebichería" cuando aplica.

---

## 6. Categoría "Booking recurrente" para profesores/coaches

**El gap:** ningún marketplace global optimiza para reservas recurrentes (todos los sábados 9-11am). Andrea la profesora de yoga lo necesita y resuelve hoy con WhatsApp eterno.

**Nuestra jugada:**
- Producto "reserva recurrente": agendar 4-12 sesiones de un solo click, con precio descontado por volumen.
- Esto cierra fidelidad (Andrea no se va a otro marketplace si su agenda ya está).
- Aumenta utilización de horas muertas del host.

---

## 7. Cobertura geográfica profunda en 8 distritos vs amplia y vacía

**El gap:** SpacePal lista 12-50 espacios en toda Lima (~10M habitantes). Densidad insuficiente.

**Nuestra jugada:**
- Lanzamiento concentrado en 8 distritos (Lima Moderna): Miraflores, San Isidro, Barranco, Surco, San Borja, La Molina, Magdalena, Pueblo Libre.
- Meta: **30+ espacios verificados por distrito** en mes 6. Total ~250 espacios.
- Densidad supera la fricción de descubrimiento ("siempre hay algo cerca").

---

## Bonus: 8. Mobile-first verdad, no responsive de escritorio

- 70%+ del tráfico marketplace consumer en Latam viene de móvil [a validar Statcounter Perú 2025].
- App nativa (RN/Flutter) en mes 9-12.
- Web mobile que carga en <2s.
- Imagen comprimida con CDN.
- Fotos cargadas por el host directo desde su celular (con AI auto-crop, auto-light).

---

## Resumen visual de diferenciación

| Pilar | SpacePal Lima hoy | Nosotros |
|---|---|---|
| Yape/Plin | No visible | Nativo en checkout |
| Verificación | Self-serve | Visita humana 100% |
| WhatsApp | Email-first | WhatsApp-first |
| Factura SUNAT | No visible | Integrada |
| Curaduría categorías | Mezclada | Verticales claras |
| Booking recurrente | No | Sí |
| Cobertura | 12-50 espacios dispersos | 250+ en 8 distritos |
| Mobile UX | Web responsive | App + mobile-web |

## Fuentes

- https://www.yape.com.pe/preguntas-frecuentes/compras-por-internet/como-puedo-tener-la-opcion-de-compras-por-internet-codigo-de-aprobacion-yape-en-l
- https://culqi.com/
- https://www.ecommercenews.pe/pagos-online/2025/pasarela-de-pagos-en-peru.html/
- https://space-pal.com/es/search/Lima--Peru/Espacios
- https://space-pal.com/support/en/articles/8583819-how-does-spacepal-make-money
- https://support.peerspace.com/en/articles/10119442-what-is-the-peerspace-service-fee
- https://www.tagvenue.com/page/list-your-venue
