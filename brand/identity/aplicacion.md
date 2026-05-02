# Guía de aplicación del branding

> Cómo aplicar el sistema visual de Coordina Eventos en producto, redes y materiales.
> Si tienes duda, **este doc gana** sobre cualquier interpretación. Tokens canónicos en `documentation/branding.md`.

---

## Wordmark — reglas de uso

### Versiones disponibles
- `brand/logo/wordmark.svg` — color sobre fondo claro (default).
- `brand/logo/wordmark-white.svg` — sobre fondos oscuros / navy.
- `brand/logo/icon.svg` — isotipo cuadrado (cuando no entra el wordmark).
- `brand/logo/favicon.svg` — favicon 32×32.
- `brand/logo/og-image.svg` — Open Graph 1200×630.

### Espacio mínimo
- Alrededor del wordmark: equivalente a la altura de la "x" en "coordina".
- Tamaño mínimo wordmark: **120px** de ancho web, **30mm** impreso.
- Tamaño mínimo isotipo: **24px** (favicon-grade).

### NUNCA
- Estirar, rotar o deformar el wordmark.
- Cambiar los colores fuera de la paleta oficial.
- Aplicar sombras, glow o efectos.
- Pegar el wordmark sobre fotografía sin contenedor (caja blanca o suficiente espacio en blanco).
- Reemplazar el "·" central por otro carácter o ícono.

---

## Paleta — cuándo usar qué

| Token | Hex | Uso correcto | Uso prohibido |
|---|---|---|---|
| `--primary` | `#0B2A5C` | Wordmark, headings, footer | Body text largos, fondos completos extensos |
| `--accent` | `#2563EB` | CTA principal, links, separador del wordmark | Aparecer >1 vez por viewport |
| `--accent-strong` | `#1D4ED8` | Hover de CTA primario | CTA por defecto |
| `--muted` | `#4B6090` | Texto secundario, "eventos" del wordmark | Texto principal |
| `--muted-light` | `#7A8AAB` | Captions, labels secundarios | Headings |
| `--surface` | `#F4F6FA` | Backgrounds de sections alternas, cards | Botones, headings |
| `--line` | `#D8DEEA` | Bordes de input, separadores | Texto |
| `--ink` | `#0B1220` | Body text default | Backgrounds |

**Regla de oro**: el `--accent` `#2563EB` aparece **máximo 1 vez por viewport** como CTA principal. Si aparece más, es ruido.

---

## Tipografía — aplicación

### Fuente única en producto
**Inter** (variable, libre). Producto, landing, materiales, social.
JetBrains Mono solo en docs técnicas, nunca en producto consumer.

### Pesos canónicos
- **600**: wordmark, headings, CTAs.
- **500**: subtítulos, énfasis.
- **400**: body default.

### Tracking
- Headings: `-0.03em`.
- Wordmark: `-0.025em`.
- Body: `0`.

### Escala (resumen — detalle en `documentation/branding.md`)

| Token | px | Uso |
|---|---|---|
| `text-xs`  | 12 | Disclaimers |
| `text-sm`  | 14 | Captions |
| `text-base`| 16 | Body default |
| `text-lg`  | 18 | Lead paragraph |
| `text-xl`  | 20 | Sub-heading |
| `text-2xl` | 24 | Section title small |
| `text-3xl` | 30 | Section title |
| `text-4xl` | 36 | Page title mobile |
| `text-5xl` | 48 | Hero mobile |
| `text-6xl` | 60 | Hero desktop |
| `text-7xl` | 76 | Hero XL / OG / statement |

---

## Botones

### Primario (CTA principal)
```css
background: var(--accent);   /* #2563EB */
color: white;
padding: 14px 22px;
border-radius: 12px;
font-weight: 600;
letter-spacing: -0.005em;
hover: background var(--accent-strong);  /* #1D4ED8 */
```
**Una sola instancia por viewport**.

### Secundario
```css
background: white;
color: var(--primary);
border: 1px solid var(--line);
border-radius: 12px;
padding: 14px 22px;
hover: background var(--surface);
```

### Ghost (links de texto / acciones terciarias)
```css
color: var(--accent);
background: transparent;
hover: background var(--surface);
```

### Tap target
- Mínimo **44×44px** en mobile (incluido padding).

---

## Cards de espacio

```
┌────────────────────────────┐
│                            │
│      FOTO 60% del card     │
│                            │
├────────────────────────────┤
│ Nombre del espacio    ★4.9 │
│ Distrito · Capacidad XX    │
│                            │
│ S/ 200/h          [Ver más] │
└────────────────────────────┘
```

- Foto dominante (4:3 o 3:2).
- Border `1px solid var(--line)` o nada.
- Radius **16px** card, **12px** foto interior.
- Sin sombra por defecto. `shadow-md` solo en hover de cards interactivas.

---

## Inputs

```css
border: 1px solid var(--line);
border-radius: 10px;
padding: 14px 16px;
font-size: 16px;            /* mínimo, evita zoom iOS */
font-family: inherit;

focus:
  border: 1px solid var(--accent);
  box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.12);
```

Labels arriba del input, no dentro. Placeholder no es label.

---

## Iconografía

- Librería: **Lucide Icons** (`lucide.dev`). Outline, **stroke 1.5px**.
- Color: hereda de `currentColor` salvo cuando aplique brand color.
- Tamaños canónicos: 16, 20, 24, 32 px.

### Excepciones
- Logos de pago (Yape, Plin, Visa, Mastercard) — color oficial de cada marca.
- Logos sociales (IG, FB, X, LinkedIn) — monocromo `--muted` en footer, color en hero.

---

## Fotografía

✅ **Aprobada**:
- Foto real del espacio del host.
- Iluminación natural o profesional limpia.
- Personas en escena cuando aplique al caso de uso.
- Composición editorial, foco en el espacio.
- Resolución mínima 1200px de ancho.

❌ **Rechazada**:
- Stock corporativo genérico.
- Filtros VSCO / vintage / sepia heavy.
- Marca de agua de competidor o fotógrafo externo.
- Texto encima del cuadro (lo agregamos nosotros si aplica).
- Render 3D de salones falsos.

---

## Aplicación a redes

### Instagram post
- Cuadrado 1080×1080.
- Wordmark abajo a la derecha en versión mini.
- Una idea por post. **Cero "8 razones por las que…"**.

### IG Story / Reel
- 1080×1920.
- Texto sobre safe area (excluir top 250px y bottom 250px).
- Wordmark arriba a la izquierda.

### LinkedIn post (imagen)
- 1200×627.
- Texto + wordmark sobre fondo `--surface`.

### Carrusel IG
- 5-8 slides máximo.
- Cada slide tiene **una sola idea**.
- Slide 1 = hook. Slide final = CTA.

---

## Email transaccional

- Header con wordmark color.
- Body con tipografía sistema (sans-serif fallback) si Inter no carga.
- CTA único por email, color `--accent`.
- Footer: dirección física (CAN-SPAM / GDPR), unsubscribe, links sociales.

---

## Voz visual + voz escrita = una sola voz

La marca **se ve** editorial, navy, geométrica.
La marca **escribe** clara, peruana, honesta, sin clichés.

Si una pieza visual es minimalista pero el copy es marketing-bullshit, **falla la marca**.

Ver `brand/messaging/voz.md` y `brand/messaging/taglines.md`.

---

## Checklist final antes de publicar cualquier pieza

- [ ] ¿Wordmark en versión correcta (color/blanco/icono)?
- [ ] ¿Una sola fuente (Inter)?
- [ ] ¿Accent `#2563EB` aparece máximo 1 vez como CTA?
- [ ] ¿Foto real, no stock?
- [ ] ¿Contraste AA en todo texto?
- [ ] ¿Funciona a 375px (mobile)?
- [ ] ¿Tap target ≥44×44px en interactivos?
- [ ] ¿Sin gradientes / sombras decorativas?
- [ ] ¿El copy pasa el filtro de `voz.md` y `taglines.md`?
- [ ] ¿Tagline correcto según la página? (Ver mapeo en `taglines.md`.)
