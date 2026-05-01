# Agents

Sub-agentes especializados de Claude Code para este proyecto. Cada agente vive en su propio archivo `.md` con frontmatter.

## Disponibles

| Agente | Archivo | Propósito |
|---|---|---|
| `market-researcher` | `market-researcher.md` | Research de mercado, competidores, fuentes |
| `landing-builder` | `landing-builder.md` | Construye y mantiene la landing estática |
| `content-creator` | `content-creator.md` | Genera contenido para redes (LinkedIn/IG/TikTok) |
| `db-migrator` | `db-migrator.md` | Diseña y ejecuta migraciones de la PG en Railway |
| `host-onboarder` | `host-onboarder.md` | Outreach a hosts potenciales (manual con AI assist) |

## Cómo invocar

Desde Claude Code:
```
/agent <nombre>
```

O dentro de una sesión, llamar al agente vía Task tool con `subagent_type` correspondiente.
