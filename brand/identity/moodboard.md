# Moodboard

> Referencias visuales para el sistema de identidad. **No copiamos** — extraemos principios.

## Principio rector
**Limpio, humano, peruano sin folklor cliché.** Inspirado en marcas digitales latam contemporáneas (Yape, Belo, Cabify) y referentes globales con UX premium (Peerspace, Airbnb).

---

## Marcas que nos inspiran (por qué)

### 1. Peerspace
- **Qué tomamos**: hero con buscador centrado masivo. Cards de espacio con foto enorme dominante. Categorías por caso de uso, no por tipo. Mucho espacio en blanco.
- **Qué NO tomamos**: paleta multicolor cargada. Algunos hero patterns muy gringos.

### 2. Airbnb
- **Qué tomamos**: confianza vía reseñas con foto. Sistema "Superhost" → adaptamos a "Verificado". Iconografía outline limpia. Presentación honesta del precio.
- **Qué NO tomamos**: la marca rosada/coral. Demasiado "global lifestyle".

### 3. Yape (BCP)
- **Qué tomamos**: morado/azul plano, sin gradientes. Wordmark simple. Confianza por simplicidad. UX peruana directa.
- **Qué NO tomamos**: el morado (es de ellos). Tono "bancario serio".

### 4. Belo
- **Qué tomamos**: verde plano + tipografía gruesa. Marca confiada, no se disculpa por ser nueva. Mobile-first puro.
- **Qué NO tomamos**: el verde lima.

### 5. Linear (B2B SaaS)
- **Qué tomamos**: minimalismo radical. Una sola tipografía. Animaciones sutiles. Dark mode opcional. Hierarchy con tipografía, no con cajas.
- **Qué NO tomamos**: el feel "techie" si no encaja con audiencia consumer.

### 6. Cabify
- **Qué tomamos**: morado + blanco. Una sola acción primaria por pantalla. Promesas concretas en copy.
- **Qué NO tomamos**: el morado.

---

## Anti-referencias (lo que evitamos activamente)

| Marca/estilo | Por qué NO |
|---|---|
| Compartir Espacios | UX 2010, densidad excesiva, fonts viejos |
| Mercado Libre | Visualmente caótico, 5 colores compitiendo |
| Salones de eventos típicos en Instagram | Stock genérico, dorados pomposos, fotos sobreproducidas |
| WeWork / coworking gringo | Demasiado "cool tech bro" |
| Agencias de eventos peruanas tradicionales | Doradas, brillantitos, formal antiguo |
| Logos con guitarras / quenas / animales andinos | Folklor cliché que nos encierra a "marca artesanal" |

---

## Paleta visual extendida

### Color principal
- `--brand: #2563EB` (azul Peerspace-adyacente, profesional sin ser corporate).

### Secundario táctico
- `--accent: #93C5FD` (azul claro para destacar elementos sin gritar).

### Neutros (escala completa)
```
--ink-100: #0B1220   // texto principal
--ink-200: #1F2937
--ink-300: #4B5563
--ink-400: #6B7280   // texto secundario
--ink-500: #9CA3AF
--ink-600: #D1D5DB   // bordes
--ink-700: #E5E7EB   // separadores
--ink-800: #F3F4F6   // backgrounds suaves
--ink-900: #F8FAFC   // surface
```

### Funcionales
- Éxito: `#10B981` (verde — match exitoso, reserva confirmada).
- Alerta: `#F59E0B` (ámbar — info importante).
- Error: `#EF4444` (rojo — solo errores reales).

### Reglas
- **El azul nunca compite con foto**. En vistas con foto, el azul sólo aparece en CTA y links.
- **No usar morado, naranja, verde lima** — territorio de competencia (Yape, Cabify, Belo).
- **No usar tonos pastel** — diluyen la marca.

---

## Tipografía

### Fuente principal
**Inter** — variable, gratis, optimizada para pantalla. Usada por GitHub, Vercel, Stripe.

- Display / Headings: **Inter 700** con `letter-spacing: -0.02em`.
- Body: **Inter 400/500**.
- Mono: **JetBrains Mono** (solo para código en docs técnicas, no producto).

### Alternativa para pruebas
**Geist** (Vercel) — si Inter se siente saturada. Misma vibe, ligeramente más distinto.

### Reglas
- **Una sola fuente**. Inter en todo. Mono solo en docs.
- Headings con tracking negativo (`-0.01em` a `-0.02em`).
- Body normal tracking.
- Nada de itálicas decorativas. Itálica solo cuando hay énfasis lingüístico real.

---

## Fotografía e ilustración

### Fotografía
- **Real, no stock**. Cuando un host se publique, foto real del espacio (incluso amateur > stock genérico).
- **Personas en escena cuando aplique** — un cumpleaños se ve mejor con humanos, no con sillas vacías.
- **Sin filtros vintage / sepia / VSCO heavy**.
- **WebP optimizado**, hero <250KB, cards <80KB.

### Ilustración
- **Mínima**. Solo cuando la foto no funciona (estados vacíos, errores, onboarding).
- **Estilo**: trazo limpio, 2 colores máximo (azul + ink). Sin sombras decorativas.
- Librería sugerida: **Lucide Icons** (outline, 1.5px stroke). Ilustraciones a medida para hero/empty states.

### Lo que NO hacemos
- Stock corporativo (3 personas sonriendo apuntando a una pantalla).
- Render 3D de salones genéricos.
- Fondos con texturas marmoleadas / doradas / "elegante de quinceañero".
- Memes / gifs en producto (en redes sí, en producto no).

---

## Iconografía

- **Lucide Icons** como base (https://lucide.dev).
- Stroke 1.5px, outline, esquinas redondeadas.
- Color: hereda del texto.
- Tamaños canónicos: 16, 20, 24, 32 px.

### Excepciones
- Logo de método de pago (Yape, Plin, Visa) usa color oficial de la marca.
- Logo de redes sociales (IG, FB, etc.) usa monocromo en footer, color en CTAs.

---

## Layouts

- Mobile-first **siempre**. Diseñar a 375px y escalar.
- Container máximo: **1080px** centrado en desktop.
- Spacing system: múltiplos de 4 (4, 8, 12, 16, 24, 32, 48, 64, 96, 128).
- Una acción primaria por pantalla. Máximo dos.
- Hierarchy con tipografía y espacio en blanco, no con cajas y sombras.
- **NO glassmorphism, NO neumorphism, NO gradientes ruidosos**.

---

## Animación

- **Sutil**. Transiciones 150-300ms, easing `ease-out`.
- Hover state en interactivos.
- `prefers-reduced-motion` respetado siempre.
- Sin scroll-jacking, sin parallax, sin motion library cargada al cargar.

---

## Voz visual de la marca en una frase

> **"Peerspace si fuera peruano y supiera cuándo callarse."**

---

## Aplicación a producto (preview mental)

- Home: hero blanco con buscador centrado, foto de fondo opcional muy sutil.
- Cards: foto dominante 60%, info abajo en 40%, sin bordes pesados.
- Botones primarios: azul `#2563EB`, padding generoso, radius 12px.
- FAQ: details/summary nativos, sin acordeones decorados.
- Footer: pocos links, mucho aire, color de fondo `surface`.

---

## Checklist de aplicación

Cada vez que se diseñe algo, revisar:
- [ ] ¿Usa Inter como fuente única?
- [ ] ¿El azul aparece máximo 1 vez por viewport (CTA principal)?
- [ ] ¿Hay una sola acción primaria visible?
- [ ] ¿La foto es real, no stock?
- [ ] ¿Funciona a 375px?
- [ ] ¿Pasa contraste AA en todo texto?
- [ ] ¿Tap target mínimo 44×44px en interactivos?
- [ ] ¿Sin gradientes / sombras decorativas?
