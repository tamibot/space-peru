# Coordina Eventos en AWS existente

Estado verificado: 30-sep-2026. Fuente: `tamibot/space-peru`; Replit excluido por instrucción del owner.

## Infraestructura y versión

- EC2 existente: `i-0bbcdcb93c03b7895`, región `us-east-1`, IPv4 `52.205.205.232`.
- Proxy existente: `creators-caddy-1`, imagen `caddy:2-alpine`. Sin nuevas instancias, contenedores, bases ni modificación de n8n.
- Directorio dedicado del host: `/opt/creators/datos/caddy/coordina/releases/<version>/site`.
- Enlace activo: `/opt/creators/datos/caddy/coordina/current`, visto en Caddy como `/data/coordina/current`.
- Caddyfile: `/opt/creators/Caddyfile`; copia previa `/opt/creators/Caddyfile.before-coordina-20260930`. La ruta de Coordina se agregó conservando las rutas anteriores y se validó antes de una recarga sin reiniciar el servicio.
- Paquetes de versión: bucket S3 privado `coordina-eventos-backups-077296715670`, prefijo `releases/`. Cifrado, bloqueo de acceso público y versionado activos. No hay base operativa de Coordina que respaldar en esta fuente.
- Portal HTTPS: https://coordinaeventos.com y https://www.coordinaeventos.com. GoDaddy conserva el registro; el cliente instalado `gddy` confirmó acceso real y actualizó los nameservers hacia Route 53.
- Zona pública Route 53: `Z085993615VP858140ZV5`; A raíz `52.205.205.232` (TTL 600), CNAME www y registros _domainconnect/_dmarc conservados. No había MX ni DS. El registro A anterior estaba protegido por Website Builder; se revirtió el intento parcial antes de migrar autoridad. Zona adicional: US$0,50/mes más consultas (tarifa AWS), sin nueva EC2.
- Respaldo DNS previo privado fuera de Git; copias Caddy previas adicionales: `/opt/creators/Caddyfile.before-godaddy-20260930` y `/opt/creators/Caddyfile.before-coordina-https-20260930`. La dirección temporal https://coordina.52.205.205.232.sslip.io sigue disponible.

## Preparación y comprobación

```sh
sh scripts/build_static.sh /private/tmp/coordina-eventos-site
node landing/src/check.mjs
node app/scripts/check-web.cjs
```

El paquete contiene landing, app/web, brand/logo SVG y data/public. Excluye documentación, credenciales, fuentes Replit y scripts privados. No requiere dependencias instaladas, Docker local ni un build Node. Las fotos de stock y Google Fonts dependen de proveedores externos.

Transferir el tar público al bucket privado con el generador de URL firmado de AWS MCP. Por SSM: descargar a un directorio de versión nuevo, comprobar SHA256, verificar rutas del archivo comprimido y extraer sin enlaces simbólicos; cambiar el enlace activo de forma atómica. Los valores de URLs firmadas no deben guardarse en documentación o Git.

## Verificación y reversión

HTTPS comprobado para inicio, catálogo, JSON de 15 demos, ficha Casa Verde, publicar y concierge; `/buscar` conserva parámetros y redirige al catálogo. El test local valida Barranco + 30 personas = 2 opciones; conserva fecha/personas/horas en el mensaje; no usa teléfonos demo como destinatarios y no modifica History con pushState.

Reversión de contenido: apuntar `current` al directorio de la versión previa dentro de `releases/`, de forma atómica; comprobar HTTPS y JSON. No hace falta reiniciar Caddy para cambiar contenido. Reversión de la incorporación al proxy: conservar un respaldo del Caddyfile vigente, retirar sólo el bloque Coordina o restaurar la copia previa si no hay cambios posteriores; validar antes de recargar. Nunca sobrescribir cambios de otros clientes.

El workflow GitHub valida la fuente y no vuelve a desplegar en Pages ni ejecuta los generadores antiguos.

## Alcance real

Catálogo demo y contacto por correo o compartir mensaje. No reservas, pagos, cuentas, agenda real ni formularios persistidos. La organización integral se cotiza aparte. Prioridad siguiente: inventario real autorizado y captura de solicitudes con consentimiento/persistencia usando el PostgreSQL y n8n existentes, con base/rol propios y sin exponer credenciales al frontend.
