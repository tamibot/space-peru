# Branding — Coordina Eventos

> Documento canónico. Si entra en conflicto con cualquier otro, **este manda**.
> **Marca**: Coordina Eventos · **Display corto**: coordina · **Dominio**: coordinaeventos.com

---

## Posicionamiento en una frase

**Coordina Eventos es donde el evento empieza:** la plataforma que conecta gente con espacios, y cuando hace falta, los coordinamos por ti.

---

## Color

### Filosofía
La paleta es **navy editorial**, no azul tech genérico. La intención: que el sitio se sienta confiable y profesional como una revista, no como una herramienta SaaS más. El azul vibrante aparece **sólo donde importa**: CTAs, links, accent del separador.

### Tokens

| Rol | Token | Hex | Notas de uso |
|---|---|---|---|
| **Primary** | `--primary` | `#0B2A5C` | Wordmark, headings, footer |
| **Accent** | `--accent` | `#2563EB` | CTA principal, links, separador del wordmark |
| **Accent-strong** | `--accent-strong` | `#1D4ED8` | Hover state de CTA |
| **Muted** | `--muted` | `#4B6090` | Texto secundario, segunda mitad del wordmark |
| **Muted-light** | `--muted-light` | `#7A8AAB` | Captions, labels secundarios |
| **Surface** | `--surface` | `#F4F6FA` | Backgrounds suaves, cards alternas |
| **Surface-strong** | `--surface-strong` | `#E5EAF2` | Bordes destacados, hover de surface |
| **Line** | `--line` | `#D8DEEA` | Separadores, bordes de input |
| **Background** | `--bg` | `#FFFFFF` | Background base |
| **Ink** | `--ink` | `#0B1220` | Texto largo de body |
| **Ink-2** | `--ink-2` | `#1F2937` | Texto secundario |

### Funcionales
- Éxito: `#10B981`
- Alerta: `#F59E0B`
- Error: `#EF4444`

### Reglas duras
- El **accent** `#2563EB` aparece **máximo una vez por viewport** (CTA principal). Si aparece más, es ruido.
- El **primary** `#0B2A5C` es el color de la marca: wordmark, headings, footer. Nunca decorativo.
- **Cero gradientes**, salvo el sutil `bg → surface` del hero.
- **Cero glassmorphism, cero neumorphism**.
- En texto largo, usar `--ink` (no `--primary` — fatiga la vista).

---

## Tipografía

### Fuente
**Inter** — variable, libre, optimizada para pantalla. Usada por GitHub, Stripe, Vercel.

> Razón de elección: rendimiento web óptimo, soporta todo el español sin tweaks, y a peso 600 con tracking cerrado se lee editorial, no "tech default".

### Pesos canónicos
- **600**: wordmark, headings, CTAs.
- **500**: subtítulos, énfasis en body, "eventos" del wordmark.
- **400**: body default.

### Tracking
- Headings: `-0.03em` (más cerrado de lo usual, refinado).
- Wordmark: `-0.025em`.
- Body: `0` (neutro).

### Escala canónica

| Token | Tamaño | Line-height | Uso |
|---|---|---|---|
| `text-xs`  | 12 | 16 | Disclaimers |
| `text-sm`  | 14 | 20 | Labels, captions |
| `text-base`| 16 | 24 | Body default |
| `text-lg`  | 18 | 28 | Lead paragraphs |
| `text-xl`  | 20 | 28 | Sub-headings menores |
| `text-2xl` | 24 | 32 | Section titles small |
| `text-3xl` | 30 | 36 | Section titles |
| `text-4xl` | 36 | 40 | Page titles mobile |
| `text-5xl` | 48 | 1.1 | Hero mobile |
| `text-6xl` | 60 | 1.05 | Hero desktop |
| `text-7xl` | 76 | 1.0 | Hero XL (OG, statements) |

### Reglas
- **Una sola fuente** en producto. Inter en todo.
- Headings con tracking negativo, body con tracking neutro.
- Itálica solo para énfasis lingüístico real (no decorativo).
- **Nunca** all caps salvo en labels muy puntuales (≤4 palabras, `text-xs`, tracking `+0.05em`).

---

## Wordmark

### Versiones disponibles
- `brand/logo/wordmark.svg` — color sobre fondo claro.
- `brand/logo/wordmark-white.svg` — sobre fondos oscuros / navy.
- `brand/logo/icon.svg` — isotipo cuadrado (IG profile, app icon).
- `brand/logo/favicon.svg` — favicon 32×32.
- `brand/logo/og-image.svg` — Open Graph 1200×630.

### Construcción del wordmark

```
coordina  ·  eventos
   ↑      ↑      ↑
primary  accent  muted
 600     600     500
```

- "coordina" en `--primary`, peso 600.
- "·" en `--accent`, peso 600 (es la única chispa de azul vibrante).
- "eventos" en `--muted`, peso 500.
- Tracking `-0.025em` en todo.

### Espacio mínimo y tamaño
- Espacio de seguridad: equivalente a la altura de la "x" de "coordina".
- Tamaño mínimo: 120px ancho web, 30mm impreso.
- Versión sólo "coordina" cuando el espacio aprieta (header móvil estrecho).

### Isotipo
**Concepto**: dos cuadrados desfasados que encajan = el evento y el espacio que se coordinan.

- Cuadrado primario (blanco) representa el espacio.
- Cuadrado accent (azul vibrante) representa el evento.
- Su ligera superposición/desfase es la coordinación.

Reglas:
- Nunca girar el isotipo.
- Nunca cambiar la proporción de los cuadrados.
- En tamaños <24px usar la versión favicon (los cuadrados son más sólidos visualmente).

---

## Spacing

Sistema de 4px. Múltiplos canónicos: `4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128`.

- Padding interno de cards: 24-32.
- Gap entre cards: 16-24.
- Padding de section: 72-96 vertical, 24-72 horizontal según viewport.
- Container max-width: 1080px.

---

## Radios

- Botón: `12px`.
- Card: `16px`.
- Input: `10px`.
- Pill: `9999px`.
- Hero / hero-image: `24px`.

---

## Sombras

- `shadow-sm`: `0 1px 2px rgba(11,18,32,.04)`.
- `shadow-md`: `0 4px 16px rgba(11,42,92,.06)` — solo en hover de cards o lifted CTAs.
- **Cero sombras decorativas**. Una sombra solo aparece cuando comunica elevación funcional.

---

## Componentes (resumen)

### Botón primario
```css
background: var(--accent);
color: white;
padding: 12px 20px;
border-radius: 12px;
font-weight: 600;
letter-spacing: -0.005em;
hover: background var(--accent-strong);
```

Una sola instancia por viewport. La acción más importante.

### Botón secundario
```css
background: white;
color: var(--primary);
border: 1px solid var(--line);
border-radius: 12px;
hover: background var(--surface);
```

### Botón ghost
```css
color: var(--accent);
background: transparent;
hover: background var(--surface);
```

### Input
```css
border: 1px solid var(--line);
border-radius: 10px;
padding: 14px 16px;
font-size: 16px;
focus:
  border: 1px solid var(--accent);
  box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.12);
```

### Card
```css
background: var(--bg);
border: 1px solid var(--line);
border-radius: 16px;
padding: 24px;
hover (interactive only): shadow-md;
```

---

## Iconografía

- **Lucide Icons** (lucide.dev) — outline, stroke 1.5px.
- Color: `currentColor` salvo casos donde aplique brand color.
- Tamaños: 16, 20, 24, 32 px.

### Excepciones
- Logos de pago (Yape, Plin, Visa, Mastercard) — color oficial de cada marca.
- Logos sociales (IG, FB, X, LinkedIn) — monocromo `--muted` en footer, color en CTAs hero.

---

## Fotografía

Filosofía: **real, no stock**. Si no hay foto real, mejor texto + ilustración mínima.

✅ **Aprobada**:
- Foto real del espacio del host.
- Iluminación natural o profesional limpia.
- Personas en escena cuando el caso lo pide (un cumpleaños se ve mejor con humanos).
- Composición editorial.

❌ **Rechazada**:
- Stock corporativo ("3 personas sonriendo apuntando a un laptop").
- Filtros VSCO / vintage / sepia heavy.
- Marca de agua de competidor.
- Render 3D de salones falsos.

---

## Voz visual + escrita = una sola voz

La marca **se ve** editorial, navy, geométrica.
La marca **escribe** clara, peruana, honesta, sin clichés.

Ver `brand/messaging/voz.md` para guía de copy.

---

## Lo que NO somos visualmente

- No somos azul tech genérico (`#3B82F6` puro suelto).
- No somos morado wallet (Yape territory).
- No somos coral/rosa Airbnb.
- No somos el dorado pomposo de salones de eventos tradicionales.
- No somos folklore peruano (sin elementos andinos cliché).
- No somos un dashboard B2B SaaS gris.
