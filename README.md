# Space Peru

Marketplace de espacios alquilables por horas en Perú — alternativa local a Space-Pal, con un branding minimalista, limpio y predominantemente azul.

## Estado
MVP en construcción. Hospedaje sobre **GitHub Pages**, base de datos en **Railway (PostgreSQL)**.

## Estructura del repo

| Carpeta | Propósito |
|---|---|
| `analisis-mercado/` | Research de competidores, perfil de usuario, pricing, oportunidades |
| `landing/` | Landing pública (estática, sirve por GitHub Pages) |
| `app/` | Producto principal (frontend + backend + DB) |
| `social/` | Contenido para LinkedIn / IG / TikTok / FB / X |
| `agents/` | Sub-agentes de Claude especializados |
| `skills/` | Skills reutilizables |
| `data/` | Datasets de research, exports, fixtures |
| `documentation/` | Docs técnica y de producto |
| `backlog/` | Tareas pendientes, ideas, roadmap |
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

- Color principal: azul (paleta a definir en `documentation/branding.md`)
- Estética: minimalista, limpio, alto contraste, mucho espacio en blanco
- Diferenciación vs Space-Pal: más intuitivo, menos densidad, foco en la experiencia móvil

## Contacto

`info@proper.com.pe`
