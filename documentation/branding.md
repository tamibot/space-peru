# Branding — Planea Ya

Documento canónico. Si entra en conflicto con `skills/space-branding.md`, este manda.

## Posicionamiento
**Marketplace minimalista de espacios por horas en Perú.** Más limpio, más intuitivo y más confiable que las alternativas.

## Color

### Paleta principal — azul
| Token | Hex | Uso |
|---|---|---|
| `--blue-50`  | `#EFF6FF` | Backgrounds suaves |
| `--blue-100` | `#DBEAFE` | Hover states muy ligeros |
| `--blue-200` | `#BFDBFE` | Bordes destacados |
| `--blue-500` | `#3B82F6` | Brand primary |
| `--blue-600` | `#2563EB` | CTA principal |
| `--blue-700` | `#1D4ED8` | CTA hover |
| `--blue-900` | `#1E3A8A` | Headings, footer |

### Neutros
| Token | Hex | Uso |
|---|---|---|
| `--ink`     | `#0B1220` | Texto principal |
| `--ink-2`   | `#1F2937` | Texto secundario |
| `--mute`    | `#6B7280` | Texto terciario, captions |
| `--line`    | `#E5E7EB` | Bordes, separadores |
| `--surface` | `#F8FAFC` | Cards, secciones alternas |
| `--bg`      | `#FFFFFF` | Background base |

### Funcionales
- Éxito: `#10B981`
- Alerta: `#F59E0B`
- Error: `#EF4444`

## Tipografía
- **Display / Headings**: Inter 700 (alternativa Geist).
- **Body**: Inter 400/500.
- **Mono**: JetBrains Mono (solo para tech / código).

### Escala
| Nombre | Tamaño | Line-height |
|---|---|---|
| `text-xs`  | 12px | 16px |
| `text-sm`  | 14px | 20px |
| `text-base`| 16px | 24px |
| `text-lg`  | 18px | 28px |
| `text-xl`  | 20px | 28px |
| `text-2xl` | 24px | 32px |
| `text-3xl` | 30px | 36px |
| `text-4xl` | 36px | 40px |
| `text-5xl` | 48px | 1.1 |
| `text-6xl` | 60px | 1.05 |

## Spacing
Sistema 4px. Múltiplos canónicos: `4, 8, 12, 16, 24, 32, 48, 64, 96, 128`.

## Radios
- Botones: `12px`
- Cards: `16px`
- Inputs: `10px`
- Pills: `9999px`

## Sombras
- `shadow-sm`: `0 1px 2px rgba(11,18,32,.05)`
- `shadow-md`: `0 4px 12px rgba(11,18,32,.06)` — solo hover/elevación clave
- Nada de sombras decorativas.

## Componentes (resumen)
- **Botón primario**: bg `--blue-600`, texto blanco, radius 12px, padding `12px 20px`, hover bg `--blue-700`.
- **Botón secundario**: borde `--line`, texto `--ink`, hover bg `--blue-50`.
- **Botón ghost**: solo texto `--blue-600`, hover bg `--blue-50`.
- **Input**: borde `--line`, focus borde `--blue-500` + ring `--blue-100`.
- **Card**: bg `--bg`, borde `--line`, radius 16px, padding 24px.

## Logo
- Wordmark "space-peru" en minúsculas, Inter 700.
- Versiones: full color (azul `--blue-600`), monocromo blanco, monocromo negro.
- Espacio mínimo alrededor: altura de la "x" del wordmark.
- [TODO] generar SVG en `landing/assets/brand/`.

## Iconografía
- Stroke 1.5px, outline, esquinas redondeadas.
- Lucide o Phosphor como librería base.

## Tono visual
- Mucho espacio en blanco.
- Fotografía real, sin stock genérico.
- Jerarquía con tipografía y espacio, no con cajas y sombras.
- Una acción primaria por pantalla. Máximo dos.

## Accesibilidad
- Contraste AA mínimo en todo. AAA en cuerpos largos.
- Focus visible siempre.
- `prefers-reduced-motion` respetado.
- Tamaño de tap mínimo 44×44px en mobile.
