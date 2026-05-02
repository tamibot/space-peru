# Coordina Eventos

> Working name. Dominio placeholder: `coordinaeventos.com`. El nombre del repo (`space-peru`) es legacy.

Marketplace de **espacios alquilables por horas en Lima**, con catálogo gratuito + asistente conversacional + concierge humano que enruta leads premium a la **agencia de eventos del owner**.

## Estado
MVP en construcción. Hospedaje temporal en **GitHub Pages**; migrará a hosting propio cuando se compre el dominio. Base de datos en **Railway (PostgreSQL)**.

## Estructura del repo

| Carpeta | Propósito |
|---|---|
| `analisis-mercado/` | Research de competidores, perfil de usuario, pricing, oportunidades |
| `brand/` | Identidad, manifiesto, posicionamiento, pitch deck, taglines |
| `landing/` | Landing pública (estática, sirve por GitHub Pages) |
| `app/` | Producto principal (frontend + backend + DB) |
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

```bash
# Clonar y entrar
git clone <repo> space-peru && cd space-peru

# Cargar credenciales
cp .env.example credentials.env
# editar credentials.env con tus valores

# Probar conexión a la DB
python3 scripts/test_db.py
```

## Branding (resumen)

- Nombre: **Coordina Eventos** (working name).
- Color principal: azul `#2563EB`.
- Estética: minimalista, limpio, alto contraste, mucho espacio en blanco.
- Wordmark: ver `brand/logo/wordmark.svg`.
- Diferenciación vs Peerspace/SpacePal: asistente IA conectado a inventario real + concierge humano + agencia de eventos propia como vehículo de monetización.

## Contacto

`info@proper.com.pe`
