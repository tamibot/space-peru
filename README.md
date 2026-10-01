# Coordina Eventos

> Dominio activo: `coordinaeventos.com`. El nombre del repo (`space-peru`) es legacy.

Visión de producto: marketplace de **espacios alquilables por horas en Lima**, con asistente conversacional y concierge humano que conecta solicitudes con la **agencia de eventos del owner**. La entrega actual es el portal estático demo descrito abajo.

## Estado
Versión estática desplegada en el Caddy existente de AWS Creators Latam: https://coordinaeventos.com. El catálogo de 15 espacios es demostrativo. Ayuda y propuestas de publicación se coordinan por correo; esta fuente no incluye un backend operativo, reservas ni pagos. Replit queda excluido por decisión del owner. GoDaddy mantiene el registro; Route 53 sirve la zona con los registros auxiliares conservados y HTTPS activo para raíz y www. Ver `documentation/aws-deployment.md`.

## Estructura del repo

| Carpeta | Propósito |
|---|---|
| `analisis-mercado/` | Research de competidores, perfil de usuario, pricing, oportunidades |
| `brand/` | Identidad, manifiesto, posicionamiento, pitch deck, taglines |
| `landing/` | Landing pública estática, alojada en AWS existente |
| `app/` | Frontend estático del catálogo, fichas y páginas informativas |
| `social/` | Contenido para LinkedIn / IG / TikTok / FB / X |
| `agents/` | Sub-agentes de Claude (orchestrator, librarian, reviewer + 5 ejecutores) |
| `skills/` | Skills locales + `.claude/skills/` con `find-skills` y otras instaladas |
| `data/` | Datasets de research, exports, fixtures |
| `documentation/` | Docs técnica, branding tokens, variables, incidents |
| `backlog/` | Tareas pendientes, ideas, roadmap, decisiones (ADR) |
| `scripts/` | Utilitarios (test DB, deploy, scrapers) |

## Archivos raíz

- `README.md` — este archivo
- `CLAUDE.md` — contexto persistente para Claude Code
- `rules.md` — reglas de trabajo y guardarraíles
- `tools.md` — inventario de herramientas/integraciones disponibles
- `credentials.env` — secretos (NO commitear, en `.gitignore`)
- `.env.example` — plantilla pública

## Quickstart

```sh
sh scripts/build_static.sh /private/tmp/coordina-eventos-site
python3 -m http.server 4178 --bind 127.0.0.1 --directory /private/tmp/coordina-eventos-site
```

Abrir `http://127.0.0.1:4178`. Esta entrega no requiere credenciales, base de datos ni instalación de dependencias. Comprobaciones: `node landing/src/check.mjs` y `node app/scripts/check-web.cjs`.

## Branding (resumen)

- Nombre: **Coordina Eventos** (working name).
- Base editorial negro/blanco/plomo y CTA principal azul `#2563EB`, aprobados por el owner. `documentation/branding.md` es la referencia vigente.
- Estética: minimalista, limpio, alto contraste, mucho espacio en blanco.
- Wordmark: ver `brand/logo/wordmark.svg`.
- Diferenciación vs Peerspace/SpacePal: asistente IA conectado a inventario real + concierge humano + agencia de eventos propia como vehículo de monetización.

## Contacto

`info@proper.com.pe`
