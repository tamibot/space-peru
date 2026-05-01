# CLAUDE.md — Contexto persistente para este repo

## Qué es esto
Marketplace de **espacios alquilables por horas en Perú** (eventos, coworking, lockers, salones, estudios, etc.). Inspirado en https://space-pal.com pero con **branding minimalista, azul, y UX más intuitiva**. Foco inicial: Lima.

## Owner
`info@proper.com.pe`

## Decisiones arquitectónicas vigentes
- **Hosting MVP**: GitHub Pages (estático). Cualquier API se hace serverless o se hostea aparte (Railway / Vercel functions).
- **DB**: PostgreSQL en Railway. Connection string en `credentials.env` → `DATABASE_URL`.
- **Stack landing**: HTML/CSS/JS vanilla o framework liviano (Astro / 11ty). Sin build pesado.
- **Stack app**: a definir tras el análisis de mercado. Candidatos: Next.js (export estático) + API serverless, o Astro + Cloudflare Workers.
- **Branding**: azul como color principal, paleta y tokens en `documentation/branding.md` (a crear).

## Reglas de trabajo (resumen — detalle en `rules.md`)
1. **Background-first**: tareas largas en agentes background, no en el hilo principal.
2. **No usar el navegador del usuario**: para web automation usar Chromium headless / Chrome MCP.
3. **No pedir confirmaciones de automatización**: el usuario ya autorizó proceder.
4. **Secretos siempre en `credentials.env`** (gitignored). Nunca hardcodear.
5. **Carpeta por dominio**: cada iniciativa nueva vive en su propia subcarpeta.

## Flujo de trabajo del proyecto
1. `analisis-mercado/` — research primero
2. `landing/` — captar interés / waitlist
3. `app/` — producto completo
4. `social/` — contenido en paralelo desde el momento que haya landing

## Convenciones
- Idioma del producto: **español (Perú)**.
- Idioma del código y nombres de archivo: **inglés**.
- Idioma de docs internas (esto): **español**.
- Commits: conventional commits (`feat:`, `fix:`, `docs:`, `chore:`).

## Memoria operativa
Ver carpeta `agents/` y `skills/` para sub-agentes definidos. Memoria persistente del CLI vive en `~/.claude/projects/-Users-pruebacomprador-Desktop-space-peru/memory/`.
