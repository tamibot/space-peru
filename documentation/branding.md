# coordinaeventos — Sistema visual

> **Documento canónico vigente.** Si entra en conflicto con cualquier otro doc, **este manda**.
> Marca: `coordinaeventos` · Dominio: `coordinaeventos.com`
> Última actualización: 2026-05-06

---

## Filosofía visual

**Editorial minimalista en blanco/negro/plomo, inspirado en Peerspace + magazine spreads.**
Tipografía bold con peso editorial, fotografía documental, abundante whitespace, bordes rectos en todo, animaciones sutiles que comunican (no decoran).

**Lo que NO somos:**
- ❌ SaaS B2B genérico
- ❌ Marrón / cream cálido
- ❌ Gradientes purple-pink, glassmorphism, neumorphism
- ❌ Stock corporativo "personas señalando laptops"
- ❌ Pills excesivamente redondeados / radius mayor a 0
- ❌ Logos de empresas con captions/labels redundantes

---

## Color — Paleta canónica

### Tokens CSS (`:root` en `landing/src/styles.css`)

| Token | Hex | Uso |
|---|---|---|
| `--primary` | `#0A0A0A` | Brand mark, headings, footer, sección dark, botón primary |
| `--primary-2` | `#1F1F1F` | Hover de primary |
| `--body` | `#2B2B2B` | Body text largo |
| `--muted` | `#6B6B6B` | Captions, eyebrows, labels secundarios |
| `--muted-light` | `#C4C4C4` | Placeholders, items inactivos |
| `--bg` | `#FFFFFF` | Background base |
| `--soft` | `#F4F4F4` | Plomo claro — testimonials bg, marquee bg |
| `--soft-2` | `#ECECEC` | Plomo ligeramente más oscuro — bordes marquee |
| `--surface` | `#F8F8F8` | Hover surface, image background |
| `--line` | `#E8E8E8` | Bordes default |
| `--line-soft` | `#F0F0F0` | Separadores ultra sutiles |
| `--ok` | `#1A8754` | Status indicator (asistente IA "en línea") |
| `--verified` | `#1D9BF0` | **Excepción**: solo para badge "Espacio verificado" (check + halo). Único color funcional fuera del monocromo. |

### Reglas duras

- **NO usar marrón / cream / beige** (#F5EFE0, #EBE3D0). Reemplazado por plomo claro.
- **NO accent color decorativo**. Todo es monocromo blanco/negro/plomo.
- **Excepción: `--verified` `#1D9BF0`** se usa SOLO para el badge "Espacio verificado" (check icon + label). Es funcional, no decorativo: comunica que el host envió video y pasó verificación humana. NO usar en headlines, links, botones u otros elementos.
- **Cero gradientes decorativos**. Solo gradientes funcionales (fade en bordes de carruseles).
- **Cero sombras decorativas**. Una sombra solo aparece si comunica elevación funcional.
- Status dots de IA pueden ser circles (semánticos), todo lo demás es recto.

---

## Tipografía

### Fuente única
**Plus Jakarta Sans** (Google Fonts variable). Pesos: 400, 500, 600, 700, 800.

> Por qué Jakarta y no Manrope/Inter: Jakarta es distintiva sin ser rara, geométrica con proporciones más amables que Inter, no sobre-usada. Funciona en headings 800 sin verse Manrope-cuadrada.

### Pesos canónicos

- **800**: hero h1, section headlines, "Hecho con coordina" gigante, brand wordmark.
- **700**: brand del nav, sub-headings (h3), eyebrows, items hover/active.
- **600**: nav links, body emphasis, CTAs.
- **500**: nav placeholders, captions, marquee items.
- **400**: body default, lead paragraphs.

### Tracking (letter-spacing)

- Headings principales: `-0.035em` a `-0.04em` (cerrado, look limpio).
- Brand wordmark: `-0.04em`.
- Body: `0` (neutro).
- Eyebrows / labels: `+0.18em` con `text-transform: uppercase` (Apple-style spacing amplio).

### Escala canónica

| Token | Tamaño aprox | Peso | Uso |
|---|---|---|---|
| Hero h1 | clamp(56px, 9vw, 124px) | 800 | "Espacios para tus eventos. Por horas." |
| Section h2 | clamp(36px, 5vw, 64px) | 800 | Cuatro razones, Cinco preguntas, etc |
| Made-in spread | clamp(80px, 16vw, 240px) | 800 | "Hecho con coordina" |
| h3 | 19-22px | 700 | Cards subtitles |
| Body lead | 17px | 400 | Sub-headings, hero lead |
| Body | 14.5-16px | 400 | Párrafos |
| Eyebrow | 11-12px | 700 | Uppercase + tracking 0.18em |
| Footer micro | 10-13px | 500 | Footer y captions |

### Reglas de copy + tipografía

- **Una sola fuente** en todo el producto.
- **NUNCA italic decorativo**. Italic solo para énfasis lingüístico real.
- **NUNCA all-caps en headings**. Eyebrow sí (kicker pequeño).
- **NUNCA exclamation points en marketing copy**.

---

## Wordmark / Brand

### Construcción
**`coordinaeventos`** en lowercase, una sola palabra, sin separadores ni puntos.

```
coordinaeventos
   ↑      ↑
   700    500 (suffix gris)
```

- "coordina" → peso 700, color `--primary`
- "eventos" → peso 500, color `--muted` (suffix `--brand-suffix`)
- En nav transparente sobre foto: "eventos" → `rgba(255,255,255,.62)`
- Tracking: `-0.04em`
- Tamaño nav: 21px. Footer: 28px.

### NO usar

- ❌ `COORDINA` mayúsculas (descartado).
- ❌ `Coordina Eventos` con espacio (no usar).
- ❌ Logo separador / punto / slash entre "coordina" y "eventos".
- ❌ Versión solo "coordina" sin "eventos" en producto público.

---

## Radii — TODO RECTO ⚠️ REGLA CRÍTICA

```css
--r-sm: 0;
--r-md: 0;
--r-lg: 0;
```

**Border-radius en TODO debe ser 0**. Esto incluye:

| Elemento | Radius |
|---|---|
| Botones (todos) | **0** |
| Cards de listing | **0** |
| Search bar (hero + catálogo) | **0** |
| Search bar fields | **0** |
| Filter chips | **0** ⚠️ NUNCA pills |
| Tags / etiquetas | **0** |
| Badges (incluido verified) | **0** |
| Inputs / select / textarea | **0** |
| Image containers | **0** |
| Modals / dialogs | **0** |
| Tooltips | **0** |
| Dropdown menus | **0** |
| Avatar containers | **0** *(o 50% solo si es foto circular de persona, justificado semánticamente)* |
| Image thumbnails en cards | **0** |
| Stat blocks | **0** |
| Form fields | **0** |

### Excepciones permitidas (semánticas únicamente):

1. **Status dots** (online indicator del chat IA, badges de notificación): `border-radius: 50%` — son indicadores semánticos, no UI containers.
2. **Avatar de persona** (foto circular de host/cliente): `border-radius: 50%` — convención universal para fotos personales.
3. **Loading spinners**: pueden ser circulares.
4. **Verified check icon** (el círculo azul del SVG): es parte del ícono semántico, no del badge container.

### Lo que NUNCA tiene border-radius mayor a 0:

- ❌ Pills de búsqueda (Cumpleaños, Boda, Sesión de fotos…) — son chips RECTANGULARES
- ❌ Pills de distrito (Miraflores, San Isidro…) — RECTANGULARES
- ❌ "Tags" de amenidades — RECTANGULARES
- ❌ Botones con bordes pill (`border-radius: 999px`) — NUNCA
- ❌ Cards con esquinas redondeadas (`border-radius: 8px`, `12px`) — NUNCA
- ❌ Search bar con esquinas redondeadas — NUNCA
- ❌ Imágenes con `border-radius` — NUNCA

> Si ves un pill en cualquier mockup o implementación, es **error de branding**. Reportar y corregir.

---

## Spacing

Sistema basado en 4px. Múltiplos canónicos:
`4 · 8 · 12 · 14 · 16 · 18 · 24 · 28 · 32 · 36 · 48 · 56 · 64 · 72 · 80 · 96 · 120`

- Container max-width: `1240px`, padding horizontal `28px`.
- Container-wide max-width: `1440px`.
- Sections: padding-y `96-120px`.
- Cards: padding `28-36px`.
- Gap entre cards: `24px`.

---

## Sombras

```css
--shadow-sm: 0 1px 2px rgba(0, 0, 0, .03);
--shadow-md: 0 6px 24px rgba(0, 0, 0, .08);
```

Casi nunca usadas. Solo para elevación funcional (search bar sobre foto, modals).

---

## Componentes principales

### Nav
- `position: sticky` cuando solid, `position: absolute` cuando transparent (sobre hero photo).
- Transition: scrollY > 80 → quita clase `.transparent`.
- Padding 16-18px vertical.

### Search bar (hero)
- Fondo `rgba(255, 255, 255, .92)` con `backdrop-filter: blur(12px)`.
- Grid 4 columnas: actividad / distrito / fecha / botón.
- Separadores verticales de 1px con `rgba(0, 0, 0, .08)`.
- Botón "Buscar" sólido negro con flecha →.

### Hero
- Foto fullbleed `clamp(480px, 70vh, 680px)` con search centrada vertical.
- Bloque negro debajo (no overlay sobre foto) con headline gigante 800.
- Hero meta: 3-4 stat columns con label uppercase tracking + value bold.

### Sección dark (hosts, AI section)
- Background `var(--primary)`, texto blanco.
- Eyebrow color `rgba(255,255,255,.5)`.
- Cards internas con `rgba(255,255,255,.04)` border `rgba(255,255,255,.08)`.

### Marquee
- Background plomo `var(--soft)`, padding 18px.
- Animación 42s linear infinite, dirección `translateX(-50%) → translateX(0)` (right-to-left visual flow).
- Separadores: línea vertical 1px x 14px alto opacity .35 (no dots circulares).

### Partners carousel
- Background blanco, eyebrow uppercase "ESPACIOS DISPONIBLES EN".
- 70-90s linear infinite scroll, pausa on hover.
- Logos: PNG grayscale 200px alto procesados con PIL (cropped, mode LA).
- Display: 56px alto x 160px ancho box, `object-fit: contain`.
- Opacity .6, hover 1.
- Sin captions/labels redundantes (los logos hablan por sí mismos).

### Categorías (interactive list + photo)
- Foto arriba widescreen 21/9, vertical labels rotated.
- Lista flow text inline separada por `·` (middot).
- Activa: peso 600 negro. Inactivas: peso 600 gris claro.
- Botón "+ más" con underline 1.5px, sin background.

### Made-in spread (magazine)
- Sección dark fullbleed.
- Headline gigante "Hecho con [foto] coordina" — la foto interrumpe el texto.
- Galería 3 cols con vertical labels editorial rotated.

### Testimonials carousel
- Background `var(--soft)`.
- Cards 380px ancho fijo, 60s scroll infinito.
- Quote mark serif `\201C` 56px decorativo arriba.
- Footer divider entre quote y autor.

### Botones

| Variante | Background | Color | Border |
|---|---|---|---|
| `.btn-primary` | `--primary` | white | none |
| `.btn-light` | white | `--primary` | none |
| `.btn-soft` | `--primary-soft` | `--primary` | none |
| `.btn-outline` | transparent | `--primary` | 1px `--primary` |
| `.btn-outline-light` | transparent | white | 1px `rgba(255,255,255,.34)` |

Todos `border-radius: 0`, padding `13-15px x 22-28px`, font-weight 700.

### Eyebrows

```css
.eyebrow {
  font-size: 11-12px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--muted);
}
```

Margen-bottom 14-18px arriba del headline.

---

## Iconografía

- **SVG line-draw** custom para why-section (4 iconos).
- Stroke `--primary`, width 1.5, linecap round, linejoin round.
- Animados con `stroke-dasharray` triggered por IntersectionObserver.
- Para listas inline (host benefits): SVG checkmark 18px stroke-width 2.5.
- Decorativos: `aria-hidden="true"`.

---

## Fotografía

### Filosofía
**Editorial documental, no stock corporativo.**

- ✅ Foto real del espacio en uso (gente en el evento).
- ✅ Iluminación natural cálida, golden hour, indoor warm.
- ✅ Composición editorial (regla de tercios, foco humano).
- ❌ Stock corporativo genérico ("3 personas señalando laptop").
- ❌ Filtros VSCO / sepia heavy.
- ❌ Render 3D.
- ❌ Imágenes con marca de agua visible.

Vertical labels rotated 90° en lados de fotos editoriales (magazine pattern):
- Top right: nombre del espacio (e.g. "SALÓN NUPCIAL").
- Bottom right: ubicación (e.g. "BARRANCO, LIMA").
- Font 10-11px, uppercase, tracking 0.18em.

---

## Animaciones

### Reglas

- Todas respetan `prefers-reduced-motion: reduce`.
- Solo animar `transform` / `opacity` (GPU compositor). NO `top/left/width/padding`.
- Easings canónicos: `cubic-bezier(0.22, 1, 0.36, 1)` (ease-out smooth).

### Inventario

| Animación | Trigger | Duración |
|---|---|---|
| Hero badge SVG draw | onload | 1s |
| Marquee scroll | infinite | 42s |
| Partners carousel | infinite | 70-90s |
| Testimonials carousel | infinite | 60s |
| Why icons stroke-draw | IntersectionObserver | 0.9s |
| AI bubbles staggered fade-in | IO | 200-3500ms delays |
| Reveal on scroll | IO | 0.8s translateY 12px |
| Cat photo fade | hover/focus | 0.35s opacity |
| Arrow slide hover | :hover | 0.4s |

---

## Voz / Copy

### Reglas

- Español Perú, tuteo (no usted).
- Slang local: Yape, Plin, "coordinar", "WhatsApp con el host".
- Cortar 30-40% del copy explicativo. Beneficio antes de feature.
- Specifics > vagos: `+1,500 reservas` no "muchas reservas".
- Active voice, verb-first sentences.
- **NUNCA** usar:
  - "tecnología de punta", "innovador", "soluciones"
  - "facilitamos", "optimizamos", "agilizamos"
  - Exclamation points
  - Italic decorativo
  - "ocho categorías" / cifras internas (mejor "+ más")

### Ejemplos canónicos

| Antes | Después |
|---|---|
| Cuatro cosas que cambian la conversación | Cuatro razones, sin trampas |
| Listar tu espacio en Coordina es gratis para siempre. Sin comisión, sin contratos. | Cero comisión. Cero contratos. Cero exclusividad. |
| Nuestro equipo humano coordina catering, decoración… | ¿Nada encaja? Lo armamos contigo. |
| Genera ingresos con tu espacio | ¿Tienes un espacio? Lístalo gratis. |

---

## Stack técnico

- **HTML/CSS/JS vanilla**, no framework.
- Plus Jakarta Sans via Google Fonts (preconnect + preload).
- Imágenes Unsplash con `?w=X&q=85&auto=format&fit=crop`.
- Logos de partners: PNG grayscale 200px alto en `landing/src/brand/partners/`.
- Hero photo preload con `fetchpriority="high"`.
- Lazy loading en todas las imágenes below-fold.

---

## Componentes específicos del catálogo (`/buscar`)

### Search bar del catálogo
Misma estructura visual que el hero search bar de la landing:
- Background: white
- Border: 1px `--line`
- Border-radius: **0** ⚠️
- Padding interno: 6px
- Grid columnas: `1.6fr 1fr 1fr auto` (actividad / distrito / capacidad / botón)
- Separadores entre fields: 1px `rgba(0,0,0,.08)` border-right
- Botón "Buscar": sólido negro, radius 0, padding 16-22px

### Filter chips ⚠️ RECTOS
```css
.filter-chip {
  border: 1px solid var(--line);
  background: white;
  color: var(--primary);
  padding: 10px 18px;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: -0.005em;
  border-radius: 0; /* ⚠️ CRÍTICO */
  cursor: pointer;
  transition: background .15s ease, border-color .15s ease;
}
.filter-chip:hover { background: var(--soft); border-color: var(--primary); }
.filter-chip.active { background: var(--primary); color: white; border-color: var(--primary); }
```

- ❌ NUNCA `border-radius: 999px` ni similar.
- ❌ NUNCA fondo pill negro con texto blanco redondeado.
- ✅ Rectángulo blanco con borde gris claro → cuando activo, rectángulo negro con texto blanco.

### Listing card (resultado de búsqueda)

```html
<a class="listing-card" href="/espacio/[slug]">
  <div class="listing-card-photo">
    <img src="..." />
    <span class="verified-mark" title="Espacio verificado">
      <svg>...check azul...</svg>
    </span>
  </div>
  <div class="listing-card-body">
    <div class="listing-card-head">
      <h3>El Alto Miraflores</h3>
      <strong class="listing-card-price">S/ 220<span>/h</span></strong>
    </div>
    <p class="listing-card-meta">Miraflores · Hasta 40 personas · Salón</p>
    <p class="listing-card-amenities">WiFi · Parking · Sonido · Cocina</p>
  </div>
</a>
```

**Spec visual**:
- Border: 1px `--line`
- Border-radius: **0**
- Padding-bottom card: 18-22px
- Foto aspect ratio: **4/3** (más compacta que Peerspace que usa 16:9)
- Foto height en grid: ~200-240px
- Hover: border-color `--primary` + foto scale(1.03) en 0.3s

**Layout del header de card**:
- `display: flex; justify-content: space-between; align-items: baseline`
- Nombre a la izquierda (peso 700, 17px)
- **Precio a la DERECHA** (peso 800, 18px, negro) — esto es crítico
- `/h` en peso 500 grayed

**Verified mark**:
- Esquina superior derecha de la foto (top: 12px, right: 12px)
- Width: 22px, fondo `--verified` `#1D9BF0` con check blanco
- Tiene tooltip "Espacio verificado"

### Grid de catálogo
- `grid-template-columns: repeat(auto-fill, minmax(280px, 1fr))`
- Gap: 20-24px
- En tablet: 2 cols. En mobile: 1 col.

### Sort dropdown
- `<select>` nativo con border 1px, radius 0, padding 10px 16px.
- Etiqueta "Ordenar por" como label antes.

### Results count
- Texto pequeño: "**15** espacios encontrados"
- font-size 14px, peso 500, color `--muted`.

---

## Componentes específicos del detalle de espacio (`/espacio/[slug]`)

### Galería hero
Inspirada en Peerspace pero rectangular siempre:
- Hero photo grande (60-70% del width)
- Grid de 4 thumbnails al lado (right side) en 2x2
- En total: 5 fotos visibles arriba
- Botón "Ver todas las fotos (12)" → lightbox fullscreen
- Aspect hero: 16:10 o 4:3
- Border-radius: **0**

### Header del listing
Después de la galería:
- Eyebrow con tipo de espacio ("SALÓN · MIRAFLORES")
- H1 nombre del espacio
- Stats inline: capacidad · m² · # reviews (si hay rating)
- Badge verified azul si aplica
- CTAs principales: "Contactar por WhatsApp" + "Pedirle al concierge"

### Pricing card sticky (right column)
- Sticky a la derecha, scrollea con la página
- Background blanco, border 1px `--line`, radius **0**
- Precio prominente: "S/ 220 / hora"
- Minimum hours si aplica: "Mínimo 2 horas"
- Selectores: fecha + horas
- Botón "Contactar por WhatsApp" sólido negro
- Sub-CTA: "Pedir al concierge que lo gestione"
- Microcopy: "Coordinas directo con el host. Sin pago anticipado en plataforma."

### Sección Sobre el host
- Foto host (avatar circular 64px - excepción semántica)
- Nombre + badge verified si aplica
- "Responde en X horas" + "X eventos hospedados"
- **Otros espacios del host** (grid de 3-4 mini-cards)
- Link "Ver todos los espacios de [nombre host] →"
- Botón "Contactar al host"

### Amenidades (collapsible por categoría)
Categorías canónicas:
- **Tecnología y AV**: WiFi, proyector, pantalla, sonido, micrófonos
- **Comodidades**: Cocina, baños, AC, calefacción, accesibilidad
- **Mobiliario**: Sillas, mesas, lounge
- **Acceso**: Parking, ascensor, entrada vehicular
- **Servicios incluidos**: Limpieza, recepcionista, seguridad

### Facilidades extras (con precio)
Lista de adicionales que el host ofrece:
- Proyector premium · S/ 50
- Sonido profesional · S/ 120
- Iluminación de escenario · S/ 200
- Mobiliario extra · S/ 80
- Etc.

Mostrar precio inline, separado del nombre.

### Mapa
- Embedded Mapbox/Leaflet
- Pin aproximado (NO dirección exacta hasta post-contacto)
- Microcopy: "Dirección exacta después de contactar al host"

---

## Archivos canónicos

```
landing/src/
├── index.html              # Estructura
├── styles.css              # Sistema visual (~1500 líneas)
├── app.js                  # Carruseles dinámicos + reveal IO + smooth scroll
└── brand/partners/         # 30+ logos PNG grayscale 200px
documentation/
├── branding.md             # ESTE DOCUMENTO — sistema visual
├── copy-voice.md           # Voz, tono, glosario, frases canónicas
└── components.md           # Catálogo de componentes con variantes y estados
agents/
├── brand-keeper.md         # Vigilante: rechaza cambios fuera del sistema
├── brand-designer.md       # Creador: diseña nuevo material en el sistema
└── copy-keeper.md          # Voz: vigila y reescribe copy
```

## Cómo usar este sistema

| Necesito | Documento canónico | Agente |
|---|---|---|
| Saber qué color usar | `branding.md` | `brand-keeper` |
| Saber qué fuente / peso / tracking | `branding.md` | `brand-keeper` |
| Crear un componente nuevo | `components.md` | `brand-designer` |
| Saber qué decir / cómo decirlo | `copy-voice.md` | `copy-keeper` |
| Validar un PR antes de mergear | los 3 docs | `brand-keeper` |
| Escribir un email / social copy | `copy-voice.md` | `copy-keeper` |
| Reutilizar un patrón existente | `components.md` | `brand-designer` |

## Cómo evolucionar el sistema

1. La decisión la toma el dueño del producto (no los agentes).
2. Antes de implementar, **actualiza el doc canónico relevante** con la decisión + fecha.
3. Propaga el cambio: tokens en `styles.css`, ejemplos en componentes, copy en `copy-voice.md`.
4. Audita archivos que usan el sistema viejo y migra.
5. Comunica al equipo qué cambió.

**Regla**: cada excepción no documentada es brand-debt futuro.
