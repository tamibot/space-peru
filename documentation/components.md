# coordinaeventos — Catálogo de componentes

> Catálogo de componentes implementados con sus variantes, estados y dónde se usan.
> Última actualización: 2026-05-06
> **Lee primero**: `branding.md` (tokens) y `copy-voice.md` (textos).

---

## Botones

### Variantes

| Clase | Background | Color texto | Border | Uso |
|---|---|---|---|---|
| `.btn-primary` | `--primary` (#0A0A0A) | white | none | CTA principal (Buscar, Ingresar, Contactar concierge) |
| `.btn-light` | white | `--primary` | none | CTA sobre fondo dark (Probar el asistente, Publicar mi espacio) |
| `.btn-soft` | `--primary-soft` (#F0F0EE) | `--primary` | none | CTA secundario (Ver todas las actividades) |
| `.btn-outline` | transparent | `--primary` | 1px `--primary` | CTA secundario sobre fondo claro |
| `.btn-outline-light` | transparent | white | 1px `rgba(255,255,255,.34)` | CTA secundario sobre fondo dark |

### Tamaños

| Modificador | Padding | Font-size | Uso |
|---|---|---|---|
| `.btn-sm` | 9px 16px | 13px | Nav |
| (default) | 13px 22px | 14px | General |
| `.btn-lg` | 15px 28px | 15px | Final CTA |

### Estados

| Estado | Cambio | Notas |
|---|---|---|
| Default | base | — |
| Hover | opacity .9 / background shift | sutil |
| Active | `transform: translateY(1px)` | press feedback |
| Focus-visible | outline 2px `--primary` offset 3px | a11y obligatorio |

**Reglas**:
- Border-radius: **0** siempre.
- Solo flecha SVG inline (`→`) cuando hay acción de navegación. Nunca emojis.
- Texto en peso 700, font-size 14-15px, letter-spacing -0.005em.

---

## Eyebrow (kicker)

Etiqueta corta arriba de cada heading de sección.

```html
<span class="eyebrow">Categorías</span>
```

**Estilo base**:
- font-size: 11-12px
- font-weight: 700
- letter-spacing: 0.18em
- text-transform: uppercase
- color: `--muted`
- margin-bottom: 14-18px

### Variantes

| Variante | Diferencia | Uso |
|---|---|---|
| `.eyebrow` (base) | gris muted | secciones generales |
| `.eyebrow.light` | white | sobre fondo dark (hosts, AI section) |
| `.concierge-eyebrow` | badge sólido negro con icon | Concierge section (destacado) |

**Concierge eyebrow** (caso especial — único con background):
```html
<span class="eyebrow concierge-eyebrow">
  <svg width="14" height="14"><!-- icon --></svg>
  Servicio Concierge · Incluido
</span>
```
- background: `--primary`
- color: white
- padding: 8px 16px
- gap con icon: 8px

---

## Verified Badge

> **Excepción documentada al monocromo.** Solo aparece para indicar verificación humana del espacio.

### Token
`--verified: #1D9BF0` *(definido en branding.md como única excepción funcional)*.

### Componentes

#### Badge inline
```html
<span class="verified-badge">
  <svg viewBox="0 0 24 24">
    <circle cx="12" cy="12" r="11" fill="#1D9BF0"/>
    <path d="M7 12.5 L10.5 16 L17 9" stroke="white" stroke-width="2.5"/>
  </svg>
  Espacio verificado
</span>
```

| Variante | Uso |
|---|---|
| `.verified-badge` | Badge azul sobre fondo claro |
| `.verified-badge.dark` | Badge azul sobre fondo dark (hosts section) |
| `.verified-inline` | Inline en párrafo del FAQ (pequeño, con texto al lado) |

#### Callout block
```html
<div class="verified-callout">
  <span class="verified-badge dark">…</span>
  <strong>Destaca con el badge azul de verificación.</strong>
  <p>Envíanos un video corto del local…</p>
</div>
```
- border 1px `rgba(29,155,240,.32)` + bg `rgba(29,155,240,.06)`
- Solo en sección Hosts (donde se invita a verificarse).

**Reglas estrictas**:
- ❌ NO usar `--verified` para botones, links, headlines, CTAs decorativos.
- ✅ Solo aparece junto al texto "Espacio verificado" o explicando qué significa.

---

## Inputs (search bar)

Hero search bar — único formulario público en la landing.

```html
<form class="hero-search">
  <div class="hero-search-field">
    <label>Para qué</label>
    <input type="text" placeholder="…" />
  </div>
  …
</form>
```

| Field type | Uso |
|---|---|
| `<input type="text">` | Actividad |
| `<select>` | Distrito (dropdown nativo) |
| `<input type="date">` | Fecha (date picker nativo) |

**Estilo**:
- Background: `rgba(255,255,255,.92)` con `backdrop-filter: blur(12px)`
- Layout: grid 4 cols (3 fields + 1 button)
- Separadores verticales 1px `rgba(0,0,0,.08)` entre fields
- Border-radius: 0

**Estados**:
- Default: subtle
- Focus-within (todo el form): no shift, solo focus-visible en field
- Focus-visible field: outline 2px `--primary` offset 4px

---

## Cards

### Testimonial card

```html
<article class="testimonial">
  <p class="testimonial-quote">…</p>
  <div class="testimonial-meta">
    <strong>Camila Ríos</strong>
    <span>Baby shower · Barranco</span>
  </div>
</article>
```

- Background: white
- Border: 1px `--line`
- Padding: 36px 32px
- Width: 380px (fixed in carousel)
- Quote-mark decorativo: `\201C` serif 56px arriba del párrafo

### Why item

```html
<div class="why-item">
  <div class="why-icon"><svg>…</svg></div>
  <span class="why-num">01 — Búsqueda</span>
  <h3>…</h3>
  <p>…</p>
</div>
```

- 4 items en grid (sm: 2 cols, lg: 4 cols)
- Icon: 56×56 SVG con stroke-draw animation
- `.why-num` formato: `NN — Categoría` en uppercase, 11px, tracking 0.04em

### Concierge step

```html
<li><span>01</span><div><strong>…</strong><p>…</p></div></li>
```

- 3 items vertical
- Número: peso 800, 22px, color `--primary`
- Strong: peso 700, 17px
- Padding entre items: gap 22px

---

## Carruseles (auto-scroll infinite)

### Marquee (beneficios)
- Scroll: 42s linear infinite
- Dirección: `translateX(-50%) → translateX(0)` *(right-to-left visual)*
- Background: `--soft`
- Separadores: línea vertical 1px × 14px alto opacity .35
- Padding: 18px

### Partners (logos)
- Scroll: 75-90s linear infinite
- Dirección: `translateX(0) → translateX(-50%)`
- Background: white
- Hover: `animation-play-state: paused`
- Logos: 60×180px box, `object-fit: contain`, opacity .55 → 1 hover
- Sin captions (los logos hablan)

### Testimonials
- Scroll: 60s linear infinite
- Hover: pausa
- Cards: 380px ancho fixed
- Gradient fade en bordes (80px ::before/::after)

---

## Layout

### Hero
- Fullbleed photo `clamp(480px, 70vh, 680px)`
- Search centrada vertical
- Bloque negro debajo (no overlay) con stats

### Made-in spread
- Magazine layout — headline gigante "Hecho con [foto] coordina"
- Foto interrumpe el texto en flujo natural
- Galería 3 cols con vertical labels rotated 90°

### Categorías
- Foto arriba widescreen 21/9, vertical labels editorial
- Lista flow text inline separada por `·` middot
- Activa: peso 600 negro · Inactivas: peso 600 gris claro
- "+ más" con underline 1.5px

### Concierge (rediseño 2026-05-06)
- Header centrado dramatic + grid 2-col abajo (steps + foto)
- Eyebrow sólido negro destacado
- Headline gigante centrado max 22ch
- Lead centrado max 60ch

---

## Iconografía

### SVG line-draw (why-section)
- Stroke `--primary` width 1.5
- linecap: round, linejoin: round
- Animación: `stroke-dasharray` triggered por IntersectionObserver
- Tamaño canvas: 56×56

### SVG inline (botones, listas)
- Stroke 2.5, fill: none
- Tamaño: 14-18px
- `aria-hidden="true"` en decorativos

### Iconos canónicos
| Icono | Uso | Path d |
|---|---|---|
| Checkmark | beneficios, confirmación | `M5 13l4 4L19 7` |
| Arrow right | CTAs | `M5 12h14M13 5l7 7-7 7` |
| WhatsApp bubble | why item 02 | path con `Q` curvas |
| Star | concierge why item | `M28 12 L32 22 L43 23 L34 30 L37 41 L28 35 L19 41 L22 30 L13 23 L24 22 Z` |
| Verified check | espacio verificado | circle azul + checkmark blanco |
| Send/concierge | concierge eyebrow | `M3 11l18-8-8 18-2-8-8-2z` |

---

## Animaciones

### Inventario completo

| Animación | Trigger | Duración | Dirección |
|---|---|---|---|
| Hero badge SVG draw | onload | 1s + 600ms delay | once |
| Marquee scroll | infinite | 42s | right-to-left visual |
| Partners carousel | infinite | 75-90s | left-to-right (track shifts left) |
| Testimonials carousel | infinite | 60s + pause hover | left-to-right |
| Why icons stroke-draw | IO threshold .3 | 0.9s | once |
| AI bubbles staggered | IO threshold .25 | 200-3500ms delays | once |
| Reveal on scroll | IO threshold .12 | 0.8s | once |
| Cat photo fade | hover/focus | 0.35s | repeat |
| Arrow slide hover | :hover | 0.4s | repeat |
| Nav highlight underline | :hover/:focus-visible | 0.25s scaleX | repeat |

### Reglas

- Todas respetan `prefers-reduced-motion: reduce`.
- Solo animar `transform` y `opacity` (GPU compositor).
- Easings canónicos: `cubic-bezier(0.22, 1, 0.36, 1)` (ease-out smooth).
- Pause-on-hover en carruseles infinitos.

---

## Accesibilidad

### Required
- `:focus-visible` con outline 2px `--primary` offset 3px en TODO interactivo.
- `aria-hidden="true"` en SVGs decorativos.
- `aria-label` en botones que solo tienen icon.
- `role="button"` + `tabindex="0"` + keyboard handler en `<li>` clickeables.
- Form fields con `<label>` asociado y `name=` para submit.
- `loading="lazy"` en imágenes below-fold.
- `fetchpriority="high"` en LCP image (hero).

### Color contrast
- Texto sobre fondo dark: rgba(255,255,255,.7) mínimo *(verificar cada uso)*.
- Texto muted (`--muted #6B6B6B`) sobre `--bg` blanco: ratio 5.0:1 ✓ AA pass.

---

## Cambios mayores históricos

| Fecha | Cambio |
|---|---|
| 2026-05-02 | Brand inicial navy + accent azul |
| 2026-05-04 | Rebrand a black-forward monocromo |
| 2026-05-04 | Marrón/cream eliminado |
| 2026-05-05 | Rebrand a Peerspace-style editorial |
| 2026-05-05 | Plus Jakarta Sans 800 + radius 0 + logo coordinaeventos lowercase |
| 2026-05-06 | Sistema verified azul agregado (excepción) |
| 2026-05-06 | Concierge rediseñado: scope reducido (no armar evento, solo local + permisos + proveedores) |
