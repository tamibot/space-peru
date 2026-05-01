# tools.md — Inventario de herramientas e integraciones

## Infraestructura activa

| Servicio | Rol | Credencial | Estado |
|---|---|---|---|
| **Railway PostgreSQL** | DB principal | `DATABASE_URL` en `credentials.env` | Activa |
| **GitHub Pages** | Hosting estático (landing + app exportada) | Repo público | Por configurar |
| **GitHub Actions** | CI/CD, deploy a Pages | — | Por configurar |

## Pendientes de contratar / decidir

| Servicio | Rol | Decisión |
|---|---|---|
| Dominio | `space-peru.com` o similar | Por comprar |
| Email transaccional | Resend / Postmark / SES | Pendiente |
| Pagos Perú | Culqi vs MercadoPago Perú vs Niubiz | A definir tras research |
| Yape/Plin | Wallets locales | Investigar APIs |
| Mapa | Google Maps / Mapbox | Mapbox por costo |
| Storage | Cloudflare R2 / S3 | Cloudflare R2 (sin egress) |
| Auth | Clerk / Supabase Auth / Auth.js | Auth.js + Postgres |
| Analítica | Plausible / Umami | Plausible (privacidad) |
| Errores | Sentry free tier | Sentry |

## Integraciones de Claude Code disponibles

### MCPs / agentes externos
- **claude-in-chrome** — control de Chromium para web automation (preferido sobre `computer-use` para web).
- **computer-use** — control nativo de apps macOS (solo cuando no haya alternativa web).
- **n8n-mcp** — workflows automatizados (presente en sesión).
- **Notion MCP** — si se requiere docs externas.
- **Google Drive / Calendar / Gmail MCPs** — disponibles vía deferred tools.
- **GitHub plugin** — auth y operaciones de repo vía gh CLI.

### Skills útiles
- `engineering:*` — debug, code-review, system-design, deploy-checklist, architecture
- `design:*` — design-critique, accessibility-review, ux-copy, design-system, design-handoff
- `marketing:*` — draft-content, campaign-plan, seo-audit, email-sequence
- `data:*` — write-query, analyze, create-viz, build-dashboard
- `product-management:*` — write-spec, roadmap-update, brainstorm
- `anthropic-skills:docx`, `:pptx`, `:xlsx`, `:pdf` — docs ofimáticos
- `claude-api` — para integrar Claude en la app

## Herramientas locales (Bash)
- `git`, `gh` — control de repo
- `python3` — scripts utilitarios
- `node`, `npm` — frontend
- `psql` (a verificar) — para CLI a Railway

## Política de uso
- **Siempre preferir** una API/MCP dedicada antes que automatizar UI.
- **Chromium headless** > navegador del usuario.
- **Background agents** para tareas largas.
- Si una herramienta no está disponible: documentarla aquí como "Por contratar" en lugar de improvisar.
