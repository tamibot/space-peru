# Branding — Coordina

> Documento canónico. Si entra en conflicto con cualquier otro doc, **este manda**.
> **Marca**: Coordina · **Marca formal**: Coordina Eventos · **Dominio**: coordinaeventos.com

---

## Posicionamiento en una frase

**Coordina es donde el evento empieza:** la plataforma editorial que conecta gente con espacios en Lima, y cuando hace falta, los coordinamos por ti.

---

## Filosofía visual

**Editorial peruvian sunset.**
La marca se siente como una revista de domingo, no como otro SaaS. La paleta evoca atardecer limeño sin caer en folclore. La tipografía mezcla un serif italic expresivo con un sans geométrico moderno. El resultado: cálido, premium, distintivo, y **claramente no hecho por IA**.

---

## Color

### Filosofía
Cream sobre carbon, con terracotta como acento puntual. Nada de azul tech genérico. Nada de morado wallet. Nada de verde tropical. **Peruvian sunset editorial**.

### Tokens

| Rol | Token | Hex | Notas de uso |
|---|---|---|---|
| **Ink** | `--ink` | `#0F0F0F` | Texto principal, headings, wordmark |
| **Ink-2** | `--ink-2` | `#2A2A2A` | Texto secundario denso |
| **Muted** | `--muted` | `#5C5C5C` | Captions, leads, párrafos secundarios |
| **Muted-light** | `--muted-light` | `#8A8A8A` | Placeholders, labels micro |
| **Background** | `--bg` | `#FFFFFF` | Background base |
| **Cream** | `--cream` | `#FAF8F5` | Surface cálido — sections alternas, cards |
| **Cream-2** | `--cream-2` | `#F4EFE6` | Borders cálidos, hover de cream |
| **Peach** | `--peach` | `#FFF1E5` | Acento muy suave (hover sutil) |
| **Line** | `--line` | `#E8E2D8` | Bordes default |
| **Line-soft** | `--line-soft` | `#F2EDE5` | Separadores ultra-sutiles |
| **Terracotta** | `--terracotta` | `#B8451C` | Accent principal — CTA, links destacados, italics |
| **Terracotta-strong** | `--terracotta-strong` | `#9A3815` | Hover de CTA terracotta |
| **Terracotta-soft** | `--terracotta-soft` | `#F4B488` | Sobre fondos oscuros, gradients |

### Funcionales
- Éxito: `#047857` (verde profundo, no neón).
- Alerta: `#B45309` (ámbar tostado).
- Error: `#B91C1C` (rojo profundo).

### Reglas duras
- **Terracotta** `#B8451C` aparece **máximo 2 veces por viewport** (CTA principal + acento decorativo). Si aparece más, es ruido.
- **Cream** es el fondo natural de secciones alternas. Crea ritmo editorial.
- **Carbon** es para texto y la sección host (dark contrast).
- **Cero gradients tech** (purple→pink) — solo gradientes orgánicos peruvian sunset (cream→terracotta→carbon).
- **Cero glassmorphism, cero neumorphism**.

---

## Tipografía

### Stack dual
- **Display**: `Fraunces` (Google Fonts, variable, gratis). Serif italic con personalidad. Optical sizing `opsz: 144` para títulos grandes.
- **Sans**: `Geist` (Vercel, gratis vía Google Fonts). Geométrica precisa. UI, body, micro-copy.

### Por qué este stack
- **Fraunces** es lo opuesto de Inter genérico. Tiene carácter editorial italic, optical sizing real, y un peso 700 que se siente luxury sin ser pomposo.
- **Geist** es la respuesta de Vercel a Inter. Más nueva, geométrica precisa, sin estar todavía sobre-usada.
- La combinación serif italic + sans geométrica dice "revista cuidadosamente diseñada", no "dashboard SaaS más".

### Pesos canónicos
- Display heading: **700 italic** con `opsz: 144`.
- Display sub: **600** o **500 italic** según contexto.
- Sans body: **400**.
- Sans énfasis: **500** o **600**.

### Tracking
- Display headings: `-0.04em` a `-0.045em` (muy cerrado, look editorial).
- Display body: `-0.025em` a `-0.03em`.
- Sans UI: `-0.005em` a `0`.

### Escala canónica

| Token | px | Display típico | Uso |
|---|---|---|---|
| `text-xs` | 12 | sans 500 | Eyebrow, labels micro |
| `text-sm` | 13–14 | sans 400/500 | Captions, footer |
| `text-base` | 15–16 | sans 400 | Body default |
| `text-lg` | 18 | sans 400 | Lead paragraphs |
| `text-xl` | 22 | display 600 | Sub-titles |
| `text-2xl` | 28 | display 700 | Section titles small |
| `text-3xl` | 36–44 | display 700 | Section titles |
| `text-4xl` | 48–60 | display 700 | Page titles mobile |
| `text-5xl` | 64–80 | display 700 | Hero mobile / dark sections |
| `text-6xl` | 96–104 | display 700 italic | Hero desktop |

### Reglas
- **Display** se usa sólo en headings, wordmark, statements. No en body.
- **Italics terracota** marcan el énfasis emocional del título — solo una palabra clave.
- **Eyebrows** (kicker antes del heading): sans 500, uppercase, `letter-spacing: 0.12em`. Pequeño, elegante, editorial.
- **Cero all-caps en headings**. La italics + tracking ya da personalidad.

---

## Wordmark

### Concepto
**"coordina"** en Fraunces italic 700. Una sola palabra, un punto terracotta como acento. La marca formal completa es "Coordina Eventos" pero la identidad visible es **coordina** — más memorable, más distintiva, más Peerspace-style (single mark).

### Versiones disponibles
- `brand/logo/wordmark.svg` — color sobre fondo claro (default).
- `brand/logo/wordmark-white.svg` — sobre fondos oscuros / carbon.
- `brand/logo/icon.svg` — isotipo cuadrado (carbon con "c" + punto).
- `brand/logo/favicon.svg` — favicon 32×32.
- `brand/logo/og-image.svg` — Open Graph 1200×630.

### Construcción
```
coordina.
   ↑     ↑
ink/700  terracotta dot
italic
```

- Fraunces italic peso 700, `opsz: 144`.
- Tracking `-0.03em`.
- Color: `--ink` `#0F0F0F`.
- Punto decorativo: círculo de 5px en `--terracotta`, alineado al baseline-ish (vertical-align top + margin).

### Espacio mínimo y tamaño
- Espacio de seguridad: equivalente a la altura de la "x" de "coordina".
- Tamaño mínimo wordmark: **120px** ancho web, **30mm** impreso.
- Tamaño mínimo isotipo: **24px** (favicon-grade).

### Isotipo
Carbon `#0F0F0F` con la letra "c" en Fraunces italic en cream + punto terracotta. La "c" italic tiene personalidad propia y funciona como mark independiente.

---

## Spacing

Sistema basado en 4px. Múltiplos canónicos: `4 · 8 · 12 · 16 · 24 · 32 · 48 · 56 · 64 · 80 · 96 · 128`.

- Padding interno cards: 16-32.
- Gap entre cards: 16-24.
- Padding section vertical: 80-96.
- Container max-width: 1080-1200px (más amplio que el típico 720 — look editorial revista).

---

## Radios

- Botón pill: `999px` (totalmente redondeado — Peerspace-style).
- Botón rectangular: `12px` (uso secundario).
- Card: `16-20px`.
- Input dentro de search-bar: `999px`.
- Hero / hero-image: `24px`.

---

## Sombras

- `shadow-sm`: `0 1px 2px rgba(15,15,15,.04)`.
- `shadow-md`: `0 6px 24px rgba(15,15,15,.06)` — solo en hover de cards o en search bar elevada.
- **Cero sombras decorativas**. La sombra solo aparece cuando comunica elevación funcional.

---

## Componentes principales

### Search bar (hero)
Caja blanca redondeada (`999px`) con 3 campos divididos por línea + botón terracotta. Inspirada directamente en Peerspace pero adaptada al contexto Lima (campos: qué evento, dónde, cuándo).

### Cards de espacio
Foto/gradient placeholder dominante (aspect 4:3) con tag flotante abajo a la izquierda. Meta abajo (nombre serif 600, distrito sans, precio serif 600).

### Pillares numerados
Número grande Fraunces italic terracotta a la izquierda (32px). Texto a la derecha con strong serif 600 + parrafo sans 400.

### Sección oscura (hosts)
Fondo carbon `#0F0F0F`, texto cream, terracotta-soft para italics e iconografía. Contraste editorial fuerte.

### CTA dual
Dos cards lado a lado al final. Una clara (cream + terracotta) para guests, una oscura (carbon + terracotta-soft) para hosts. Visualmente comunican los dos públicos.

---

## Iconografía

- **Lucide Icons** (lucide.dev) — outline, stroke 1.5-2px.
- Color: hereda de `currentColor` salvo cuando aplique brand color.
- Tamaños canónicos: 16, 18, 20, 24 px.

### Excepciones
- Logos de pago (Yape, Plin, Visa, Mastercard) — color oficial de cada marca.
- Logos sociales (IG, FB, X, LinkedIn) — monocromo en footer, color en CTAs hero.

---

## Fotografía

Filosofía: **real, no stock**. En MVP usamos **gradients sofisticados** como placeholder (peruvian sunset) hasta tener fotos reales de los hosts. Esto se siente premium y evita el "stock corporativo IA-look".

✅ **Aprobada (cuando llegue)**:
- Foto real del espacio del host.
- Iluminación natural o profesional.
- Personas en escena cuando aplique al caso de uso.
- Composición editorial.

❌ **Rechazada**:
- Stock corporativo genérico.
- Filtros VSCO / vintage / sepia heavy.
- Marca de agua de competidor.
- Render 3D de salones falsos.

### Placeholder gradients
Hasta tener fotos reales, usar 6 gradient backgrounds peruvian sunset (`bg-1` a `bg-6` en CSS). Cada uno con tag textual de qué espacio representaría. Esto es **mejor que stock**, no peor.

---

## Voz visual + voz escrita = una sola voz

La marca **se ve** editorial peruvian sunset.
La marca **escribe** clara, peruana, honesta, sin clichés.

Si una pieza visual es minimalista pero el copy es marketing-bullshit, **falla la marca**.

Ver `brand/messaging/voz.md` y `brand/messaging/taglines.md`.

---

## Lo que NO somos visualmente

- ❌ Azul tech default (`#3B82F6` / `#2563EB`) puro.
- ❌ Morado wallet (Yape territory).
- ❌ Coral Airbnb (`#FF385C`).
- ❌ Naranja chillón (`#F97316`) tipo Substack.
- ❌ Dorado pomposo de salones de eventos tradicionales.
- ❌ Folklore peruano (sin elementos andinos cliché — pampas, llamas, flautas).
- ❌ Dashboard B2B SaaS gris.
- ❌ Inter peso 700 default.
- ❌ Stock corporativo "3 personas señalando un laptop".
