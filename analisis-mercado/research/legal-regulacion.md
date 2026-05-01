# Mapa de riesgos legales y regulatorios

> **Disclaimer:** este documento NO constituye asesoría legal. Es un mapa de riesgos para identificar dónde necesitamos contratar abogado especializado peruano (recomendado: estudio con experiencia marketplaces + tributario, ej. Rebaza/Payet/Estudio Olaechea/Garrigues PE).

## 1. Régimen tributario — IGV y facturación electrónica

### IGV
- **Tasa general:** 18% (16% IGV + 2% IPM).
- **Régimen MYPE 2026:** restaurantes y hoteles MYPE tienen tasa reducida 8% temporal — **no aplica al alquiler de espacios** salvo el host se constituya como hotel.
- Operaciones gravadas con IGV >S/700 pueden activar régimen de retención del 3% si una de las partes es agente designado por SUNAT.

### Facturación electrónica
- **Obligatoria para emisores con ingresos anuales >150 UIT** (~S/772.500 en 2026, UIT 2026 = S/5.150) [a validar UIT vigente y umbral 2026].
- Marketplace que cobra en nombre propio = obligación de emitir factura/boleta electrónica al cliente final.
- **Modelos posibles:**
  - **Modelo "principal":** marketplace cobra al guest, emite factura propia, paga al host con boleta del host como gasto.
  - **Modelo "agente / mandatario":** marketplace solo intermedia el cobro, host emite la factura directamente al guest. Más amigable tributariamente al host pequeño.
- **Recomendación:** modelo dual en MVP. Default agente; opción principal para hosts que no quieran lidiar con facturación.
- Proveedores de facturación electrónica certificados SUNAT (OSE/PSE): Nubefact, Facele, Efact, Mifact.

### Riesgo clave
- Si marketplace factura como principal, asume responsabilidad SUNAT total (declarar mensualmente, fiscalizable). Si actúa como agente y un host evade, riesgo solidario [a validar con asesor].

## 2. Licencias municipales para eventos

### ITSE (Inspección Técnica de Seguridad en Edificaciones)
- Obligatoria para todo establecimiento abierto al público.
- **Riesgo bajo, medio o alto** según aforo y giro.
- **Vigencia:** 2 años.
- Es **responsabilidad del host** tenerla, no del marketplace. Pero marketplace debe **verificar al onboardear** que el host la tiene vigente — si no, riesgo reputacional masivo en caso de accidente.

### ECSE (Evaluación de Condiciones de Seguridad para Eventos)
- Obligatoria para eventos públicos:
  - **Hasta 3.000 personas** → Municipalidad distrital (donde se realiza).
  - **>3.000 personas** → Municipalidad Metropolitana de Lima.
- Requiere: plan de seguridad, plan de evacuación, certificado GLP si aplica, descriptivo de instalaciones eléctricas.
- **Implicancia para marketplace:** la mayoría de bookings serán privados (cumpleaños familiares <100 personas) y NO requieren ECSE específico — basta licencia funcionamiento del local. Pero si ofrecemos categoría "eventos masivos", responsabilidad del organizador del evento, no del marketplace.

### Licencia de funcionamiento municipal
- Cada distrito de Lima tiene su propio TUPA. Costos S/100-S/2.000 según giro y tamaño.
- El host debe tenerla. Si no, riesgo de clausura y multa al evento.

## 3. Responsabilidad por daños

- **Daño al espacio por el guest:** marketplace puede actuar como mediador con depósito de garantía / hold en tarjeta. Modelo Peerspace cobra deposit y libera 24h post-evento.
- **Daño al guest dentro del espacio (accidente, lesión):** responsabilidad civil del host. Recomendación: requerir póliza de RC del host (Pacífico/Rímac/Mapfre ofrecen pólizas comerciales desde ~S/100/mes).
- **Cancelaciones / no-show:** definir política contractual clara en T&C — refund tiers (estricta/moderada/flexible). Modelo Airbnb/Peerspace.
- **Marketplace como facilitador:** la cláusula "somos un marketplace, no propietario, no operamos los espacios" es estándar. Limita pero no elimina responsabilidad — el Indecopi puede sancionar por falta de información clara al consumidor.

## 4. Indecopi y protección al consumidor

- Ley de Protección al Consumidor (Ley 29571) aplica plenamente al marketplace.
- Obligaciones clave:
  - **Información clara antes de la compra:** precio total con IGV y fees, condiciones, política de cancelación.
  - **Garantía de información veraz:** si la foto del espacio no corresponde a la realidad, Indecopi sanciona al marketplace (no solo al host) en ciertos casos. Por eso la verificación humana es además mitigación legal.
  - **Libro de reclamaciones electrónico** obligatorio.
  - **Atención de reclamos en plazos máximos** (15-30 días según tipo).

## 5. Datos personales — Ley 29733

- Registro de banco de datos personales ante ANPDP (Autoridad Nacional de Protección de Datos Personales).
- Consentimiento explícito para uso de datos del guest y host.
- Si transferimos datos al exterior (host en Stripe US, p. ej.) → declaración de transferencia internacional.

## 6. Pagos digitales — SBS / BCR

- Marketplace que **mantiene saldos de usuarios** podría caer bajo regulación de Empresa Emisora de Dinero Electrónico (EEDE) — riesgo regulatorio mayor.
- **Mitigación:** no mantener saldos. Cobrar al guest, transferir al host inmediatamente (T+1 a T+3), nunca acumular wallet del host sin payout. Modelo "passthrough payments" usando Culqi/Stripe Connect.

## 7. Laboral

- Si verificadores y fotógrafos son colaboradores recurrentes → riesgo de reclamación de relación laboral.
- **Mitigación:** locación de servicios formal con RUC propio del freelancer + RxH; o contratar bajo régimen MYPE como dependientes.

## 8. Antilavado / GAFI

- Marketplaces con tickets >US$1.500/transacción pueden caer en obligaciones de UIF (Unidad de Inteligencia Financiera).
- **Mitigación:** umbrales de KYC reforzado en bookings >S/5.000.

## Resumen de riesgos top 5

| # | Riesgo | Probabilidad | Severidad | Mitigación |
|---|---|---|---|---|
| 1 | No verificar ITSE de host → accidente en evento | Media | Alta | Verificar al onboardear, exigir copia, badge "ITSE vigente" |
| 2 | Facturación SUNAT mal estructurada | Alta | Alta | Asesor tributario antes de cobrar primer booking; modelo agente claro |
| 3 | Indecopi por foto/info falsa | Media | Media | Verificación humana + foto pro propia |
| 4 | Operar como EEDE sin licencia SBS | Baja | Muy alta | Stripe Connect / Culqi como passthrough, no wallet |
| 5 | Datos personales sin registro ANPDP | Media | Media | Registrar banco de datos pre-launch |

## Acciones requeridas pre-launch (checklist)

- [ ] Constituir SAC con objeto social claro: "intermediación digital en alquiler temporal de espacios y servicios conexos".
- [ ] RUC + facturación electrónica habilitada.
- [ ] T&C con cláusula de marketplace + política de cancelación.
- [ ] Política de privacidad + registro ANPDP.
- [ ] Libro de reclamaciones electrónico.
- [ ] Asesor tributario confirma modelo agente vs principal.
- [ ] Decisión de seguro RC para hosts (incluido / opcional).

## Fuentes

- https://emprender.sunat.gob.pe/principales-impuestos/impuesto-general-las-ventas-igv/impuesto-general-las-ventas
- https://emprender.sunat.gob.pe/principales-impuestos/impuesto-general-las-ventas-igv/regimen-retencion-igv
- https://www.gob.pe/20961-obtener-certificado-de-inspeccion-tecnica-de-seguridad-en-edificaciones-de-riesgo-bajo-o-medio
- https://www.munlima.gob.pe/tramites-y-servicios/certificado-de-inspecciones-tecnicas-de-seguridad-en-edificaciones-itse/
- https://portal.indeci.gob.pe/minisites/preguntas-frecuentes/
- https://www.munisanmiguel.gob.pe/general/sglc/0201_AUTO_TEMP_PP.pdf
- https://img.lpderecho.pe/wp-content/uploads/2020/07/reglamento-de-inspecciones-tecnicas-de-seguridad-en-edificaciones-Ley-27157-LP.pdf
- https://www.nubefact.com/blog/actualizaciones-sunat/nueva-tasa-de-igv-e-ipm-2026-para-mypes-de-restaurantes-y-hoteles-en-peru
- https://facele.pe/retenciones-del-igv-en-peru-y-cambios-sunat/
- Ley 29571 — Código de Protección y Defensa del Consumidor (Indecopi).
- Ley 29733 — Ley de Protección de Datos Personales (ANPDP).
- [a validar UIT 2026, umbral facturación electrónica 2026].
