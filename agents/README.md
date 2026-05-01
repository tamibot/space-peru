# Agents

Sub-agentes especializados de Claude Code para Planea Ya. Cada agente vive en su propio archivo `.md` con frontmatter.

## Mapa de agentes

### Capa de control
| Agente | Archivo | Propósito |
|---|---|---|
| `orchestrator` | `orchestrator.md` | **Director de operaciones**. Coordina, decide tooling, reporta estado. **Empezar siempre por aquí en sesiones nuevas.** |
| `librarian` | `librarian.md` | Documentador y guardián de credenciales/variables. Escanea pre-commit. |
| `reviewer` | `reviewer.md` | QA crítico de entregables. Aprueba o bloquea con criterios fijos. |

### Capa de ejecución
| Agente | Archivo | Propósito |
|---|---|---|
| `market-researcher` | `market-researcher.md` | Research de mercado, competidores, fuentes |
| `landing-builder` | `landing-builder.md` | Construye y mantiene la landing estática |
| `content-creator` | `content-creator.md` | Genera contenido para redes |
| `db-migrator` | `db-migrator.md` | Diseña y ejecuta migraciones del PG en Railway |
| `host-onboarder` | `host-onboarder.md` | Outreach a hosts potenciales (manual con AI assist) |

## Flujo recomendado

```
sesión nueva
    │
    ▼
orchestrator (lee CLAUDE.md, rules.md, backlog, decisiones)
    │
    ├──→ market-researcher (background)
    ├──→ landing-builder
    ├──→ content-creator
    ├──→ db-migrator
    ├──→ host-onboarder
    │
    ▼
reviewer (audita cada entregable antes de cerrar ticket)
    │
    ▼
librarian (al final, antes de commit, valida secretos y variables)
    │
    ▼
commit
```

## Cómo invocar
Desde Claude Code:
```
/agent <nombre>
```
O dentro de una sesión, llamar al agente vía Task tool con el `subagent_type` correspondiente.

## Reglas comunes
- Cada agente respeta `rules.md`.
- Los agentes nunca commiten — siempre dejan los cambios listos y reportan.
- Tareas largas → siempre background.
- Web automation → Chromium / Chrome MCP, nunca el navegador del owner.
