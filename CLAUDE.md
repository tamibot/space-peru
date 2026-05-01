# CLAUDE.md — Contexto persistente para este repo

## Qué es esto
Marketplace de **espacios alquilables por horas en Perú** (eventos, coworking, lockers, salones, estudios, etc.). Inspirado en https://space-pal.com pero con **branding minimalista, azul, y UX más intuitiva**. Foco inicial: Lima.

## Owner
`info@proper.com.pe` — GitHub: `tamibot`.

## Cómo arrancar una sesión nueva
**Llamar primero al agente `orchestrator`** (`agents/orchestrator.md`). Lee el contexto vivo, diagnostica y enruta. No saltearlo.

## Decisiones arquitectónicas vigentes
- **Hosting MVP**: GitHub Pages (estático).
- **DB**: PostgreSQL en Railway (`DATABASE_URL` en `credentials.env`).
- **Stack landing**: HTML/CSS/JS vanilla, mobile-first.
- **Stack app**: a definir tras Fase 0/1. Candidatos: Astro o Next.js (export estático).
- **Branding**: azul como color principal. Tokens en `documentation/branding.md`. Narrativa en `brand/`.
- **Idioma producto**: español Perú. **Idioma código**: inglés.

## Tesis del producto (post-research)
"**Peerspace para Perú**, mobile-first, Yape/Plin nativos, verificación humana."

3 pilares de diferenciación:
1. Pago 100% local (Yape/Plin/Culqi + factura SUNAT)
2. Curaduría humana con visita presencial
3. WhatsApp-first para notificaciones y soporte

Categorías de lanzamiento (orden): salones eventos sociales → estudios foto/video → salas reuniones corporativas.

Geografía MVP: 8 distritos Lima Moderna (Miraflores, San Isidro, Barranco, Surco, San Borja, La Molina, Magdalena, Pueblo Libre).

Take-rate inicial: 15% host + 5% guest (~19% combinado), 0% host primeros 6 meses.

## Reglas de trabajo (resumen — detalle en `rules.md`)
1. **Background-first**: tareas largas → sub-agentes background.
2. **No usar el navegador del owner**: Chromium headless / Chrome MCP siempre.
3. **No proponer automatizaciones** (instrucción del owner). Solo si las pide.
4. **Secretos siempre en `credentials.env`** (gitignored). Agente `librarian` los gestiona.
5. **Antes de implementar algo común, llamar `find-skills`** para ver si ya existe la skill.
6. **Antes de cerrar entregable, pasar por `reviewer`**.

## Mapa del repo
| Carpeta | Qué hay |
|---|---|
| `analisis-mercado/` | Research de mercado (12 docs) |
| `brand/` | Identidad, manifiesto, posicionamiento, taglines, pitch deck, roadmap narrativo |
| `landing/` | Landing estática mobile-first |
| `app/` | Producto (frontend, backend, db) |
| `social/` | Contenido por plataforma + calendar |
| `agents/` | 8 sub-agentes especializados (incluye orchestrator, librarian, reviewer) |
| `skills/` | Skills locales + `.claude/skills/` con find-skills + 5 skills externas |
| `data/public/` | Categorías, distritos, equipamiento (consumido por landing) |
| `documentation/` | Branding técnico, arquitectura, glosario, **variables.md**, incidents |
| `backlog/` | roadmap, tasks, ideas, decisiones (ADR) |
| `scripts/` | Utilitarios (`test_db.py`) |

## Flujo de trabajo del proyecto
1. ✅ `analisis-mercado/` — research (Fase 0)
2. ⏳ `landing/` + `brand/` — captar interés / waitlist (Fase 1)
3. ⏳ `app/` — producto completo (Fase 2-3)
4. ⏳ `social/` — contenido en paralelo desde Fase 1

## Convenciones
- Idioma del producto: **español (Perú)**.
- Idioma del código y nombres de archivo: **inglés**.
- Idioma de docs internas: **español**.
- Commits: conventional commits (`feat:`, `fix:`, `docs:`, `chore:`).
- Branch base: `main`.

## Memoria operativa
Ver `agents/` y `skills/` para definiciones. Memoria persistente del CLI vive en `~/.claude/projects/-Users-pruebacomprador-Desktop-space-peru/memory/`.
