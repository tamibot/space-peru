# brand/

Carpeta canónica de **identidad de marca, narrativa y materiales estratégicos** de Planea Ya. Todo lo que un inversor, periodista, host nuevo o empleado nuevo necesita ver para entender quiénes somos y a dónde vamos.

> Si entra en conflicto con `documentation/branding.md`: **brand/ es la versión narrativa, branding.md es la versión técnica/dev**. Los tokens viven en `branding.md`. La narrativa, los manifiestos, el pitch y el storytelling viven aquí.

## Estructura

| Carpeta | Contenido |
|---|---|
| `identity/` | Misión, visión, valores, manifiesto, naming, posicionamiento |
| `logo/` | Versiones SVG/PNG, reglas de uso, espacios mínimos, sobre fondo claro/oscuro |
| `pitch-deck/` | Pitch deck del proyecto (markdown fuente → exporte a `.pptx` con `anthropic-skills:pptx`) |
| `roadmap/` | Visión de producto a 6/12/24 meses (vinculado a `backlog/roadmap.md`) |
| `messaging/` | Voz de marca, taglines, frases clave, do's & don'ts de lenguaje |
| `assets/` | Stock fotográfico, mockups, plantillas, gradientes, iconografía |

## Skills relacionadas
- `space-branding` — tokens de aplicación rápida
- `space-copy-pe` — voz y microcopy en ES-PE
- `brand-guidelines` (vendor: anthropics/skills) — best practices generales
- `extract-design-system` — analizar branding de competidores

## Workflow
1. Cualquier cambio narrativo (mensaje, valor, tagline) se propone aquí primero.
2. Una vez aprobado por owner, se propaga al copy de `landing/`, `social/` y producto.
3. Cambios en tokens visuales (color, tipografía) → editar `documentation/branding.md` primero, reflejar en `brand/identity/`.
