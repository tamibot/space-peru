# Landing

Landing pública estática de Planea Ya. Deploy a GitHub Pages.

## Estructura
```
landing/
  src/         # HTML/CSS/JS (o Astro src/)
  assets/      # imágenes, logos, fonts
  content/    # copy editable separado del código
  dist/        # output del build (gitignored o publicado)
  README.md
```

## Sectores en v1
1. Hero + waitlist
2. Cómo funciona
3. Categorías
4. Por qué Planea Ya
5. Para anfitriones
6. FAQ
7. Footer

## Stack tentativo
- HTML/CSS/JS vanilla con `<script type="module">` y CSS variables.
- O **Astro** si necesitamos componentes reutilizables.
- Decisión: comenzar vanilla, migrar a Astro si crece.

## Build local
```bash
# vanilla
open landing/src/index.html
# o servidor dev simple
python3 -m http.server -d landing/src 8000
```

## Deploy
- GitHub Action en `.github/workflows/deploy-landing.yml` (a configurar).
- Push a `main` → build → publica en `gh-pages`.
