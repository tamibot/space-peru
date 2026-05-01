# tools.md — Inventario de herramientas e integraciones

## Infraestructura activa

| Servicio | Rol | Credencial | Estado |
|---|---|---|---|
| **Railway PostgreSQL** | DB principal | `DATABASE_URL` | ✅ activa, verificada (PG 18.3) |
| **GitHub** | Repo + Pages | `gh` CLI autenticado como `tamibot` | ✅ auth OK |
| **GitHub Pages** | Hosting estático | — | ⏳ por publicar |
| **GitHub Actions** | CI/CD deploy | `.github/workflows/deploy-landing.yml` | ✅ definido |

## Skills CLI activo

| Tool | Versión | Comando |
|---|---|---|
| `npx skills` | latest | `npx -y skills <cmd>` |

Skills instaladas: ver `skills/README.md`.

## Pendientes de contratar / decidir

| Servicio | Rol | Decisión |
|---|---|---|
| Dominio `space-peru.com` | Marca | Por comprar |
| Email transaccional | Resend / Postmark | Resend probable |
| Pagos Perú tarjeta | Culqi vs Niubiz vs MercadoPago | Culqi probable (research/metodos-pago-peru.md) |
| Yape/Plin | Wallets locales | Investigar APIs (research) |
| Mapas | Mapbox vs Google | Mapbox por costo |
| Storage imágenes | Cloudflare R2 / S3 | Cloudflare R2 (sin egress) |
| Auth | Auth.js + Postgres adapter | Auth.js |
| Analítica | Plausible / Umami | Plausible (privacidad) |
| Errores | Sentry free tier | Sentry |
| WhatsApp Business API | Notificaciones / soporte | Meta Cloud API o Twilio |

## Integraciones de Claude Code disponibles

### MCPs / agentes externos vivos en esta sesión
- **claude-in-chrome** — Chromium control para web automation (preferido sobre `computer-use` para web).
- **computer-use** — control nativo de apps macOS (solo cuando no haya alternativa web).
- **n8n-mcp** — workflows automatizados (presente).
- **GitHub plugin** — auth y operaciones vía `gh` CLI.
- **MCPs deferred**: Google (Drive/Calendar/Gmail), Notion, Atlassian, Linear, Asana, Slack, Stripe (vía plugin), Supabase, Neon, etc. Cargables vía `ToolSearch` cuando hagan falta.

### Skills oficiales de stock siempre disponibles
- `engineering:*` — debug, code-review, system-design, deploy-checklist, architecture
- `design:*` — design-critique, accessibility-review, ux-copy, design-system, design-handoff
- `marketing:*` — draft-content, campaign-plan, seo-audit, email-sequence
- `data:*` — write-query, analyze, create-viz, build-dashboard
- `product-management:*` — write-spec, roadmap-update, brainstorm
- `anthropic-skills:docx`, `:pptx`, `:xlsx`, `:pdf` — docs ofimáticos (usar `:pptx` para exportar pitch deck)
- `claude-api` — para integrar Claude en la app

### Skills locales propias del proyecto
Ver `skills/README.md`.

## Herramientas locales (Bash)
- `git`, `gh` — control de repo
- `python3` + `.venv` — scripts utilitarios (`scripts/test_db.py`, etc.)
- `node`, `npm`, `npx` — para Skills CLI y futuros frontend builds
- `psql` (vía Bash) — CLI a Railway

## Política de uso (durísima)
- **Siempre preferir** una API/MCP/skill dedicada antes que automatizar UI.
- **Chromium headless** > navegador del owner (regla de `rules.md`).
- **Background agents** para tareas largas.
- **Antes de implementar** algo común, llamar `find-skills` (regla de `skills/README.md`).
- **Si una herramienta no está disponible**: documentarla aquí como "Por contratar" en lugar de improvisar.
