# Branding — Coordina

> Documento canónico. Si entra en conflicto con cualquier otro doc, **este manda**.
> **Marca**: Coordina · **Marca formal**: Coordina Eventos · **Dominio**: coordinaeventos.com

---

## Posicionamiento en una frase

**Coordina es la plataforma que conecta personas con espacios para eventos en Lima**, y cuando hace falta, coordina también todo lo demás.

---

## Filosofía visual

**Profesional minimalista azul.** Inspirado en Peerspace, Stripe, Linear: navy serio + un acento azul moderno + mucho espacio en blanco. La marca debe sentirse confiable, limpia, contemporánea — sin caer en cliché tech genérico ni folclore peruano.

---

## Color

### Filosofía
Azul navy como ancla de confianza profesional. Accent azul vibrante moderno (no tech default, no Airbnb coral, no morado wallet). Mucha respiración blanca. Surface muy suave que crea ritmo de secciones.

### Tokens

| Rol | Token | Hex | Notas de uso |
|---|---|---|---|
| **Primary** | `--primary` | `#0A2540` | Wordmark, headings, footer, brand mark |
| **Primary-2** | `--primary-2` | `#1A2B4A` | Hover de buttons primary navy |
| **Body** | `--body` | `#3C4257` | Texto largo de body |
| **Muted** | `--muted` | `#697386` | Captions, labels secundarios |
| **Muted-light** | `--muted-light` | `#8792A2` | Placeholders |
| **Background** | `--bg` | `#FFFFFF` | Background base |
| **Surface** | `--surface` | `#F6F9FC` | Sections alternas, cards de fondo |
| **Surface-2** | `--surface-2` | `#F0F4F9` | Hover de surface |
| **Line** | `--line` | `#E3E8EE` | Bordes default |
| **Line-soft** | `--line-soft` | `#EDF1F6` | Separadores ultra-sutiles |
| **Accent** | `--accent` | `#3D5AFE` | CTA principal, links, énfasis |
| **Accent-strong** | `--accent-strong` | `#2841E0` | Hover de CTA accent |
| **Accent-soft** | `--accent-soft` | `#ECEFFE` | Background de iconos, hover suave |

### Funcionales
- Éxito: `#10B981`
- Alerta: `#F59E0B`
- Error: `#EF4444`

### Reglas duras
- **Accent** `#3D5AFE` aparece **máximo una vez como CTA principal** por viewport. Si aparece más, es ruido.
- **Primary navy** `#0A2540` es el color de la marca: wordmark, headings, footer, sección dark de hosts.
- **Cero gradientes purple-pink**, solo gradientes azules muy sutiles en surfaces.
- **Cero glassmorphism, neumorphism, sombras decorativas**.

---

## Tipografía

### Fuente única
**Plus Jakarta Sans** (Google Fonts, variable, libre).

> **Por qué esta fuente**: distintiva sin ser rara, geométrica moderna con proporciones sutilmente más amplias que Inter. No está sobre-usada como Inter ni Roboto. Funciona excelente en headings (700/800) y body (400/500). Variable axis para fine-tuning.

### Pesos canónicos
- **800**: hero opcional para enfatizar.
- **700**: headings, wordmark, sub-headings principales.
- **600**: CTAs, énfasis en body.
- **500**: secondary nav, labels, captions.
- **400**: body default.

### Tracking
- Headings principales: `-0.038em` a `-0.04em` (cerrado, look limpio).
- Wordmark: `-0.035em`.
- Body: `0` (neutro).
- Eyebrows (kicker): `+0.06em` con `text-transform: uppercase`.

### Escala canónica

| Token | px | Display típico | Uso |
|---|---|---|---|
| `text-xs`  | 12-13 | 600 | Eyebrows, labels micro |
| `text-sm`  | 13-14 | 500 | Captions, footer |
| `text-base`| 15-16 | 400 | Body default |
| `text-lg`  | 17-19 | 400 | Lead paragraphs |
| `text-xl`  | 20-22 | 700 | Sub-headings |
| `text-2xl` | 28-30 | 700 | Section titles small / feat headings |
| `text-3xl` | 32-44 | 700 | Section titles |
| `text-4xl` | 48-56 | 700 | Page titles, host CTA |
| `text-5xl` | 60-68 | 700 | Hero |

### Reglas
- **Una sola fuente** en todo el producto.
- Headings con tracking negativo (`-0.03em` a `-0.04em`).
- Body con tracking neutro.
- Eyebrows con tracking expandido + uppercase.
- **Nunca** italic decorativo. Italic solo para énfasis lingüístico real.
- **Nunca** all caps en headings. Eyebrow sí (kicker pequeño con tracking expandido).

---

## Wordmark

### Concepto
**"coordina"** en Plus Jakarta Sans peso 700, sólido, sin elementos decorativos. Mark sólido tipográfico — Peerspace-style.

La marca formal completa es "Coordina Eventos" pero el display visible es **coordina** — más memorable, más distintivo.

### Versiones disponibles
- `brand/logo/wordmark.svg` — color sobre fondo claro (default).
- `brand/logo/wordmark-white.svg` — sobre fondos oscuros / navy.
- `brand/logo/icon.svg` — isotipo cuadrado (navy con "c" blanca).
- `brand/logo/favicon.svg` — favicon 32×32.
- `brand/logo/og-image.svg` — Open Graph 1200×630.

### Construcción
```
coordina
   ↑
primary 700
sólido, sin punto, sin separador
```

- Plus Jakarta Sans peso 700.
- Tracking `-0.035em`.
- Color: `--primary` `#0A2540`.

### Espacio mínimo y tamaño
- Espacio de seguridad: equivalente a la altura de la "x" de "coordina".
- Tamaño mínimo wordmark: **120px** ancho web, **30mm** impreso.
- Tamaño mínimo isotipo: **24px** (favicon-grade).

### Isotipo
Navy `#0A2540` con la letra "c" en Plus Jakarta peso 700 en blanco. Limpio, geométrico, funcional.

---

## Spacing

Sistema basado en 4px. Múltiplos canónicos: `4 · 8 · 12 · 16 · 24 · 32 · 48 · 56 · 64 · 72 · 80 · 96 · 120`.

- Padding interno cards: 32-48.
- Gap entre cards: 24-32.
- Padding section vertical: 96-120.
- Container max-width: 1140px.

---

## Radios

- Botón: `10px` (rectangular suave, no totalmente redondeado).
- Botón pill (en chip listas): `999px`.
- Card: `16-20px`.
- Input: `10px`.
- Hero visual: `24px`.
- Icon container small: `10-12px`.
- Final CTA banner: `24px`.

---

## Sombras

- `shadow-sm`: `0 1px 2px rgba(10, 37, 64, .04)` — cards default.
- `shadow-md`: `0 4px 16px rgba(10, 37, 64, .06)` — hover, elevated.
- `shadow-lg`: `0 12px 32px rgba(10, 37, 64, .08)` — final CTA, hero raised.
- **Cero sombras decorativas**. Una sombra solo aparece cuando comunica elevación funcional.

---

## Componentes principales

### Botones
- **Primary** (CTA principal): bg `--accent` `#3D5AFE`, color blanco, radius 10px, font 600. Hover: `--accent-strong`.
- **Dark** (CTA secundario alto contraste): bg `--primary` navy, color blanco, radius 10px.
- **Outline**: border `--primary`, color `--primary`, transparent. Hover: bg `--primary` color blanco.
- **Outline-light** (sobre fondos oscuros): border blanco semi, color blanco.
- **Light**: bg blanco, color `--primary`, border `--line`.

### Cards (audience cards)
- Padding 48×40, radius 20px, border 1px `--line`.
- Hover: border accent + shadow-md.
- Variante `primary`: bg navy, color blanco, accent texts en `#93B4FF`.

### Steps numerados
- Círculo navy 44×44 con número blanco peso 700, radius 50%.
- Heading 20px peso 700.
- Párrafo body 15px.

### Eyebrows
- Font-size 13px, peso 600, uppercase, letter-spacing `+0.06em`, color `--accent`.
- Margin-bottom 16-24px arriba del heading.

### Hero visual
- Aspect 1/1.05, bg gradient azul muy suave.
- 3 cards apiladas con icono + texto, mostrando los 3 pasos del producto.
- No es funcional — es ilustración del producto.

### Sección dark (hosts)
- Bg `--primary` navy, texto blanco, accent `#93B4FF`.
- Card glassmorphism interno: `rgba(255,255,255,0.04)` + border `rgba(255,255,255,0.12)` + backdrop-filter blur.

---

## Iconografía

- **Lucide Icons** estilo (lucide.dev) — outline, stroke 2px, color hereda de currentColor.
- Tamaños canónicos: 16, 18, 20, 22, 24 px.
- Para feature icons (que llevan bg colored): icon 22px, container 48px.
- Para inline icons en listas: 18px, color `--accent` o `#93B4FF` en dark.

### Excepciones
- Logos de pago (Yape, Plin, Visa, Mastercard) — color oficial de cada marca cuando aplique.
- Logos sociales — monocromo en footer, color en CTAs hero.

---

## Fotografía

Filosofía: **real, no stock**. En MVP / landing no usamos fotos de espacios reales aún (no tenemos catálogo). Por eso la landing es **explicativa, no demo de producto**: visuales con icons y cards, no fotos.

Cuando lleguen fotos reales:
- ✅ Foto real del espacio del host.
- ✅ Iluminación natural o profesional.
- ✅ Composición editorial.
- ❌ Stock corporativo genérico.
- ❌ Filtros VSCO / sepia heavy.
- ❌ Render 3D.

---

## Voz visual + voz escrita

Visual: limpio, profesional, navy/azul, mucho aire blanco.
Escrita: clara, peruana, honesta, sin clichés de marketing.

Ver `brand/messaging/voz.md` y `brand/messaging/taglines.md`.

---

## Lo que NO somos visualmente

- ❌ Tech default Inter + azul `#3B82F6` puro.
- ❌ Editorial Fraunces italic + terracotta (era el approach previo, descartado).
- ❌ Morado wallet (Yape territory).
- ❌ Coral Airbnb (`#FF385C`).
- ❌ Naranja chillón (`#F97316`).
- ❌ Dorado pomposo de salones tradicionales.
- ❌ Folklore peruano (sin elementos andinos cliché).
- ❌ Dashboard B2B SaaS gris.
- ❌ Stock corporativo "3 personas señalando un laptop".
- ❌ Glassmorphism / neumorphism / shadows decorativas.

---

## Estructura canónica de la landing

La landing **NO es un demo de la app**. Es una página explicativa que vende el concepto:

1. **Hero** — qué somos en una frase + 2 CTAs (guests / hosts) + visual ilustrativo.
2. **Qué hacemos** — 3 features explicando el modelo.
3. **Para quién** — 2 audience cards segmentadas (guest / host).
4. **Cómo funciona** — 3 pasos numerados.
5. **Categorías** — chips ejemplo (estáticos, no buscador).
6. **Por qué Coordina** — 4 diferenciadores con icons.
7. **Hosts CTA** — sección dark dedicada.
8. **FAQ** — preguntas honestas.
9. **Final CTA** — banner navy con dos opciones.
10. **Footer** — multi-columna.

**Lo que NO va en landing**:
- ❌ Search bar funcional (eso es la app).
- ❌ Galería de espacios reales con prices (eso es la app).
- ❌ Filtros, mapa, results.
