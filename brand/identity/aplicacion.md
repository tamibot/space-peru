# Guía de aplicación del branding

> Cómo aplicar el sistema visual de Planea Ya en producto, redes, materiales. **Si tienes duda, este doc gana sobre cualquier interpretación**.

## Wordmark — reglas de uso

### Versiones disponibles
- `brand/logo/wordmark.svg` — color (azul + ink) sobre fondo claro.
- `brand/logo/wordmark-white.svg` — sobre fondos oscuros / azul.
- `brand/logo/icon.svg` — isotipo cuadrado (cuando no entra el wordmark completo).
- `brand/logo/favicon.svg` — favicon 32×32.
- `brand/logo/og-image.svg` — Open Graph 1200×630.

### Espacio mínimo
- Alrededor del wordmark: equivalente a la altura de la "x" en "planea ya".
- Tamaño mínimo wordmark: **80px de ancho** en web, **24mm impreso**.
- Tamaño mínimo isotipo: **24px** (favicon-grade).

### NUNCA
- Estirar, rotar o deformar el wordmark.
- Cambiar los colores fuera de la paleta oficial.
- Aplicar sombras, glow o efectos.
- Usar sobre fondos que rompan el contraste AA.
- Pegar el wordmark sobre fotografía sin contenedor (caja blanca o suficiente espacio en blanco).

---

## Paleta — cuándo usar qué

| Token | Hex | Uso correcto | Uso prohibido |
|---|---|---|---|
| `--blue-600` | `#2563EB` | CTA principal, links, brand accents, isotipo bg | Body text largos, fondos completos |
| `--blue-700` | `#1D4ED8` | Hover de CTA, headings sobre superficie clara | CTA por defecto |
| `--blue-900` | `#1E3A8A` | Headings prominentes, footer | Backgrounds grandes |
| `--blue-50` | `#EFF6FF` | Background de hero hint, hover ligero | Body text |
| `--blue-100` | `#DBEAFE` | Focus ring, separadores ligeros | CTA |
| `--ink-100` | `#0B1220` | Body text default | Fondos amplios |
| `--ink-400` | `#6B7280` | Captions, labels secundarios | Body principal |

**Regla de oro**: el azul `--blue-600` aparece **máximo 1 vez por viewport** como CTA principal. Si aparece más, es ruido.

---

## Tipografía — aplicación

### Inter es la única fuente
- Producto, landing, materiales, social.
- JetBrains Mono solo en docs técnicas, nunca en producto consumer.

### Escala canónica (Tailwind-friendly)

| Token | px | Uso |
|---|---|---|
| `text-xs`  | 12 | Disclaimers, micro-labels |
| `text-sm`  | 14 | Captions, secondary nav |
| `text-base`| 16 | Body default |
| `text-lg`  | 18 | Body amplio (lead) |
| `text-xl`  | 20 | Sub-headings menores |
| `text-2xl` | 24 | Section titles small |
| `text-3xl` | 30 | Section titles |
| `text-4xl` | 36 | Page titles mobile |
| `text-5xl` | 48 | Hero mobile / page titles desktop |
| `text-6xl` | 60 | Hero desktop |

### Reglas
- Headings: 700 con tracking `-0.02em`.
- Body: 400/500.
- Línea de base 1.55 para body, 1.05-1.15 para headings.
- Italic solo para énfasis lingüístico real (no decorativo).

---

## Botones

### Primario
```css
background: var(--blue-600);
color: white;
padding: 12px 18px;
border-radius: 12px;
font-weight: 600;
hover: var(--blue-700);
```

Solo **uno** por viewport. La acción más importante.

### Secundario
```css
background: white;
color: var(--ink-100);
border: 1px solid var(--line);
border-radius: 12px;
hover: background var(--blue-50);
```

Para acciones complementarias.

### Ghost
```css
color: var(--blue-600);
background: transparent;
hover: background var(--blue-50);
```

Para acciones terciarias / "saber más".

### Tamaños
- Default: padding 12×18, font-size 15.
- Small: padding 8×12, font-size 14.
- Large: padding 16×24, font-size 17.

### Tap target
- Mínimo 44×44px en mobile (incluido padding).

---

## Cards de espacio (preview)

Estructura canónica:
```
┌────────────────────────────┐
│                            │
│      FOTO 60% del card     │
│                            │
├────────────────────────────┤
│ Nombre del espacio    ★4.9 │
│ Distrito · Capacidad XX    │
│                            │
│ S/ 200/h        [Ver más] │
└────────────────────────────┘
```

- Foto dominante (aspect ratio 4:3 o 3:2).
- Sin bordes pesados — solo `1px solid var(--line)` o nada.
- Radius 16px en card, 12px en foto interior.
- Sin sombra por defecto. Sombra ligera solo en hover.

---

## Inputs

```css
border: 1px solid var(--line);
border-radius: 10px;
padding: 12px 14px;
font-size: 16px;  /* mínimo, evita zoom iOS */

focus:
  border: 1px solid var(--blue-500);
  box-shadow: 0 0 0 4px var(--blue-100);
```

Labels arriba del input, no dentro (placeholder no es label).

---

## Iconografía

- Librería: **Lucide Icons** (`lucide.dev`). Outline, 1.5px stroke.
- Tamaños canónicos: 16, 20, 24, 32 px.
- Color hereda de `currentColor` salvo cuando aplique color de marca.

### Casos especiales
- Logos de pago (Yape, Plin, Visa) usan color oficial de la marca, no monocromo.
- Logos sociales (IG, FB, X) monocromo en footer, color en CTAs.

---

## Fotografía — qué pasa el filtro

✅ **Aprobada**:
- Foto real del espacio del host.
- Iluminación natural o profesional limpia.
- Personas en escena cuando aplique al caso de uso (un cumpleaños se ve mejor con humanos).
- Composición simple, foco en el espacio.

❌ **Rechazada**:
- Stock genérico ("tres personas sonriendo en oficina").
- Filtro VSCO / vintage / sepia heavy.
- Marca de agua de competidor o fotógrafo externo.
- Texto encima del cuadro (lo agregamos nosotros si aplica).
- Render 3D de salones falsos.
- Resolución <1200px de ancho.

---

## Aplicación a redes (preview)

### Instagram post
- Cuadrado 1080×1080.
- Wordmark abajo a la derecha en versión mini.
- Una idea por post. Cero "8 razones por las que Planea Ya es la mejor plataforma".

### IG Story / Reel
- 1080×1920.
- Texto sobre safe area (excluyendo top 250px y bottom 250px).
- Wordmark arriba a la izquierda.

### LinkedIn post (imagen)
- 1200×627.
- Texto + wordmark, fondo `--surface` o `--blue-50`.

### Carrusel IG
- 5-8 slides máximo.
- Cada slide tiene una sola idea.
- Slide 1 = hook. Slide final = CTA.

---

## Email transaccional

- Header con wordmark en `--blue-600`.
- Body con tipografía sistema (sans-serif fallback) si Inter no carga.
- CTA en botón único, color brand.
- Footer con dirección física (requisito CAN-SPAM / GDPR), unsubscribe, links sociales.

---

## Voz visual + voz escrita = una sola voz

- La marca **se ve** limpia, simple, peruana, confiada.
- La marca **escribe** clara, peruana, honesta, sin clichés.

Si una pieza visual es minimalista pero el copy es marketing-bullshit, **falla la marca**.

Ver `brand/messaging/voz.md` para guía de copy.

---

## Checklist final antes de publicar cualquier pieza

- [ ] ¿Wordmark en versión correcta (color/blanco/icono)?
- [ ] ¿Una sola fuente (Inter)?
- [ ] ¿Azul `--blue-600` aparece 1 vez como CTA?
- [ ] ¿Foto real, no stock?
- [ ] ¿Contraste AA en todo texto?
- [ ] ¿Funciona a 375px (mobile)?
- [ ] ¿Tap target ≥44×44px en interactivos?
- [ ] ¿Sin gradientes / sombras decorativas?
- [ ] ¿El copy pasa el filtro de `voz.md`?
- [ ] ¿Tagline si aplica viene de `taglines.md`?
