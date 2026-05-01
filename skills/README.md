# Skills

Skills locales del proyecto + skills externas instaladas vía `npx skills`.

## Skills locales (`skills/`)

| Skill | Cuándo |
|---|---|
| `space-branding` | Aplicar tokens de branding |
| `space-copy-pe` | Generar copy en español Perú con voz de marca |
| `space-pricing-helper` | Sugerir tarifa por hora |

## Skills instaladas vía CLI (`.claude/skills/` y `.agents/skills/`)

| Skill | Fuente | Installs | Cuándo |
|---|---|---|---|
| `find-skills` | vercel-labs/skills | — | **Skill maestra**: descubre e instala más skills. Úsala antes de improvisar. |
| `web-design-guidelines` | vercel-labs/agent-skills | — | Auditar UI / accesibilidad / a11y |
| `brand-guidelines` | anthropics/skills | 34K | Aplicar best practices de branding |
| `extract-design-system` | arvindrk/extract-design-system | 79K | Extraer design system de un sitio (útil para benchmarks de Space-Pal) |
| `landing-page-design` | infsh-skills/skills | 14K | Diseño de landing pages |
| `postgresql-table-design` | wshobson/agents | 15K | Diseñar schemas/tablas en PG |
| `customer-research` | coreyhaines31/marketingskills | 21K | Plan y ejecución de research de clientes (Fase 1) |
| `startup-financial-modeling` | wshobson/agents | 6.3K | Modelo financiero MVP, unit economics, runway |
| `startup-metrics-framework` | wshobson/agents | 5.8K | North star + KPIs, framework para Fase 2 |
| `lean-canvas` | phuryn/pm-skills | 571 | Lean Canvas (Fase 2 — definir oferta y MVP) |
| `business-model` | phuryn/pm-skills | 652 | Business Model Canvas |

## Cómo invocar
```
/skill <nombre>
```
o referenciar dentro de un agente.

## Skills oficiales de Anthropic siempre disponibles
La sesión de Claude Code carga muchas skills de stock (productivity, engineering, design, marketing, data, sales, etc.). El agente `orchestrator` decide cuál usar caso por caso. Ver lista en system reminders.

## Política de skills
1. **Antes de implementar** algo desde cero, llamar a `find-skills` para verificar si existe una skill que cubra el caso.
2. **Solo instalar** skills con install count >1K o de fuentes oficiales (anthropics/, vercel-labs/, microsoft/, supabase/).
3. **Cada skill instalada** se documenta en este archivo con su install count y caso de uso.
4. **Antes de remover** una skill, verificar que ningún agente la referencie.

## Comandos `npx skills` útiles
```bash
npx skills list                                  # listar skills instaladas
npx skills find <query>                          # buscar skills
npx skills add <owner/repo> -s <name> -y         # instalar skill específica
npx skills add <owner/repo> -l                   # listar skills disponibles del repo
npx skills update                                # actualizar todas
npx skills remove <name>                         # remover
```
