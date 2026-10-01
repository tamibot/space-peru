# Coordina Eventos — producto, simplificación y mejoras

30 de septiembre de 2026 · Lima. Actualizado según la decisión del usuario: **usar y desplegar el repositorio original; Replit queda fuera de esta entrega**. Este documento no acredita por sí solo un despliegue ni funciones futuras.

## Qué estamos montando

Un portal para descubrir y comparar espacios alquilables por horas en Lima. La visión comercial incluye SUM y áreas comunes de edificios, salones de hoteles y otros ambientes para eventos. El responsable del espacio decide aforo, horarios, reglas y condiciones; en edificios y hoteles debe existir autorización administrativa para ofrecer el ambiente.

Hay tres rutas: **buscar un espacio**, **pedir ayuda para un evento** y **proponer un espacio al equipo**. La organización integral se cotiza como servicio adicional. El recorrido futuro conecta búsqueda → comparación → ficha → consulta completa → respuesta del responsable. La entrega actual publica la versión estática existente con un catálogo demo, fichas y vías de contacto; no anuncia como operativas las partes que faltan.

## Fuente y alcance actual

| Material | Uso en esta entrega |
| --- | --- |
| `portal-original/landing/src` | Landing HTML/CSS/JS simplificada, menú y buscador con los parámetros que realmente admite el catálogo |
| `portal-original/app/web` | Catálogo y fichas originales, JSON demo, navegación y páginas informativas existentes |
| `revision-2026-09-30/revision.md` | Evidencia histórica del original local, portal anterior y secuencia visual del video |
| `/Users/pruebacomprador/Developer/coordina-video/src` | Dirección de producto; el video es una demostración Remotion |
| `portal/` recuperado de Replit | Excluido del despliegue por la última instrucción del usuario; conservar sin incorporarlo a esta entrega |

Se comprobó previamente el catálogo original local: 15 espacios, filtro Barranco + 30 personas con dos resultados y ficha navegable. Esta evidencia no valida disponibilidad, contactos reales, reseñas, pagos, permisos ni persistencia de solicitudes. La nueva landing se verifica con su comprobación estática y debe revisarse visualmente en el despliegue.

La revisión anterior del video utilizó fotogramas y código. No acredita escucha del audio ni fluidez en un dispositivo físico. Mapa, recorrido 360°, montaje IA, cotización guardada y entrega WhatsApp del video siguen siendo conceptos hasta implementar y probar sus versiones reales en el repositorio elegido.

## Visual y navegación aplicados en la landing

Negro editorial, fotografía protagonista, Plus Jakarta Sans y bordes rectos. **Azul en el botón principal** según la aprobación más reciente del usuario, que sustituye la antigua restricción del azul al badge «Verificado».

- Un titular claro: «Un espacio para tu próximo evento».
- Buscador nativo: evento (`caso`), distrito (`distrito`), fecha preferida (`date`) y personas (`cap`). Los nombres coinciden con el catálogo original; el parámetro anterior `actividad` no filtraba sus datos.
- La fecha se explica como preferencia; no consulta una agenda ni reserva.
- Tres entradas de navegación: Buscar espacios, Necesito ayuda y Publicar mi espacio.
- Menú móvil nativo; sin scroll horizontal ni necesidad de pasar el cursor.
- Contacto de ayuda y propuesta de espacio mediante correo, con explicación de que se abre la aplicación del usuario y el envío queda a su cargo.
- Sin cifras de tracción, logos de supuestos aliados, testimonios ficticios, promesas de plazos, comisión o publicación automática.
- Interacciones CSS de 150–250 ms y respeto por movimiento reducido. Sin autoplay, carruseles infinitos, parallax ni animaciones que escondan contenido.

Los anchors `categorias`, `por-que`, `asistente`, `concierge`, `hosts` y `preguntas` se conservan para enlaces anteriores. No se enlaza `/app/asistente.html`, que no existe en el original.

## Landing simplificada

| Bloque | Trabajo que hace | Acción real |
| --- | --- | --- |
| Hero | Explicar espacios por horas en Lima y permitir una búsqueda | GET al catálogo estático con filtros |
| Explorar opciones | Mostrar categorías con fotografía ilustrativa | Catálogo filtrado por caso de uso |
| Cómo funciona | Explicar búsqueda, comparación y consulta | Orientar; aclarar que no procesa pagos ni reservas |
| Necesito ayuda | Pedir fecha, invitados, distrito y presupuesto | Abrir correo al equipo; organización completa aparte |
| Publicar mi espacio | Explicar datos y autorización que necesita una propuesta | Abrir correo al equipo; alta manual |
| Condiciones | Resolver cuatro preguntas operativas | FAQ nativa y contacto |

El catálogo demo se señala junto al buscador y las fotografías ilustrativas junto al contenido. Las imágenes de stock no se identifican como lugares de Lima ni como eventos organizados por Coordina. La revisión comercial del inventario es un trabajo posterior, no un efecto del traslado a AWS.

## Prioridades y aceptación

### P0 — publicar el repositorio existente de forma fiable

| Trabajo | Criterio de aceptación |
| --- | --- |
| Preparación estática reproducible | Copia landing, app, JSON, logos y otros activos necesarios; arranca local sin build de Replit ni backend inventado |
| Catálogo y fichas | Carga JSON; filtro por personas excluye aforos inferiores; categoría y distrito funcionan; ficha y regreso son navegables |
| Honestidad de datos | Referencias demo visibles; sin teléfonos/reseñas/coordenadas sintéticas presentados como datos verificados; errores de carga distintos de cero coincidencias |
| Landing móvil/escritorio | Titular legible y búsqueda cercana; tres rutas claras; sin overflow; foco/etiquetas y menú usables con teclado |
| Contacto real | Ayuda y alta muestran el canal disponible; abrir correo o WhatsApp no se anuncia como envío, registro o reserva |
| AWS y dominio | Activos estáticos servidos por HTTPS; rutas `.html` y JSON accesibles; dominio final confirmado; navegación y formularios GET comprobados desde el dominio |
| Evidencia y reversibilidad | Paquete desplegado identificable y copia del anterior; posibilidad de restaurar archivos/versiones; prueba funcional sin enviar contactos comerciales |

AWS debe alojar lo que existe. Un portal estático no necesita base de datos, servidor de aplicaciones ni migración de Replit. Las decisiones específicas de servicios y DNS corresponden al inventario de la cuenta y al despliegue verificado.

### P1 — completar la utilidad comercial con inventario y operación reales

| Mejora | Criterio de aceptación |
| --- | --- |
| Inventario autorizado | Cada espacio comercial tiene responsable localizable, consentimiento de publicación, fotos coherentes y condiciones; edificios/hoteles con autorización registrada |
| Solicitud estructurada | Recoge espacio, evento, fecha/horario, invitados, presupuesto y contacto; valida datos; persiste registro con identificador antes de confirmar |
| Seguimiento del equipo | Cada solicitud tiene estado y siguiente acción; entrega externa comprobada si se ofrece, fallos visibles y datos preservados |
| Precio entendible | Tarifa × horas, mínimo de contratación y extras desglosados; total referencial y garantía separados; organización aparte; fee solo con política comercial confirmada |
| Publicación de anfitriones | Fotos cargables, vista previa y estado de revisión; propuesta no pasa a publicada automáticamente sin controles requeridos |
| Navegación persistente | Abrir ficha/volver conserva filtros y posición; ayuda puede reutilizar datos; enlaces directos funcionan |
| Revisión de copy del resto del original | Quitar fechas antiguas, gratuidad/plazos no aprobados y afirmaciones de visitas/verificación sin evidencia en páginas informativas y fichas |

Las solicitudes requieren una decisión técnica posterior: el original es estático y no guarda formularios en un backend. Evitar anunciar «solicitud recibida» hasta que exista persistencia o entrega comprobable.

### P2 — llevar la diferenciación del video al producto

| Mejora | Dependencia | Criterio de aceptación |
| --- | --- | --- |
| Mapa | Ubicaciones verificadas y oferta útil | Lista/Mapa conservan filtros; aproximación declarada; lista disponible ante fallo |
| Recorrido por ambientes | Fotografías del mismo inmueble y nombres de ambientes | Galería controlable; «360°» solo con panoramas reales |
| Antes/después | Permisos de imágenes y una misma escena | Propuesta IA identificada y comparador accesible; no garantiza aforo/costo/factibilidad |
| Generación IA | Demanda, costo por generación y contador compartido | Estados reales, resultado recuperable y costo controlado; no repetir trabajo tras timeout sin revisar estado |
| Disponibilidad | Calendario mantenido por responsables | Horarios comprobados y conflictos evitados; no simular fechas ocupadas como reales |
| Comparación lado a lado | Dificultad observada al comparar varias fichas | Mismos campos y selección recuperable; antes, cards consistentes y favoritos cubren comparación básica |

## Métricas que conviene medir

No hay resultados actuales ni porcentajes de éxito acreditados. Medir una línea base antes de fijar objetivos y distinguir lo que puede conocerse en un sitio estático de lo que necesita seguimiento comercial.

| Métrica | Definición |
| --- | --- |
| Fallo de catálogo | Cargas de JSON fallidas / cargas intentadas, separado de búsquedas válidas sin coincidencias |
| Oferta útil | Espacios autorizados con fotos/condiciones completas y responsable confirmado, separados de demos y pausados |
| Uso de búsqueda | Sesiones que buscan y abren una ficha, con filtros más usados; sin datos personales en analítica |
| Inicio de contacto | Clics en correo o enlace WhatsApp; no equivalen a mensajes enviados ni solicitudes recibidas |
| Solicitud útil, cuando exista backend | Registros persistidos con datos suficientes para cotizar; dato faltante y resultado por cohorte |
| Respuesta operativa | Mediana y percentil 90 desde recepción real hasta primera respuesta humana |
| Resultado comercial | Confirmadas, perdidas y pendientes; separar alquiler de organización; motivo de pérdida |

Verificar que el catálogo siga cargando requiere revisar sus datos y resultado, no solo HTTP 200. En canales externos futuros, respetar el contador compartido y fallo cerrado de las instrucciones globales. No generar contactos comerciales de prueba a anfitriones reales.

## Qué omitir ahora

Reescritura en React, backend especulativo, base de datos vacía para servir HTML, microservicios, nuevas librerías de animación, app móvil, checkout, chat IA, SEO masivo, dashboards sin operación real y métricas/testimonios inventados. Incorporar cada capacidad cuando exista una necesidad observada y sea posible demostrar su resultado.

## Secuencia

1. Preparar y verificar el repositorio original en local.
2. Revisar copy y datos demo, simplificar landing y navegación manteniendo rutas reales.
3. Desplegar el paquete estático en AWS, conectar dominio/HTTPS y comprobar catálogo, ficha, filtros y contacto.
4. Conseguir inventario autorizado y acordar política comercial y operación.
5. Implementar solicitudes persistidas y publicación revisada; después, diferenciación del video.

Mensaje para comunicar: «Coordina Eventos te ayuda a explorar espacios por horas en Lima y comparar opciones para tu evento. Puedes consultar ayuda o proponer un espacio al equipo. La versión actual muestra un catálogo demo; la organización completa se cotiza aparte.»
