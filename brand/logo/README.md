# Logo

Archivos de marca visual.

> ⚠️ **Nombre placeholder**: el wordmark dice "coordina · eventos". Cuando se confirme nombre final, regenerar SVG con find/replace + actualizar este README.

## Archivos disponibles

| Archivo | Tamaño | Uso |
|---|---|---|
| `wordmark.svg` | 360×80 | Sobre fondos claros (default) |
| `wordmark-white.svg` | 360×80 | Sobre fondos oscuros / azul |
| `icon.svg` | 64×64 | Isotipo cuadrado (IG profile, app icon) |
| `favicon.svg` | 32×32 | Favicon del sitio |
| `og-image.svg` | 1200×630 | Open Graph (compartir en redes / WhatsApp) |

## Pendientes de generar (cuando se cierre el nombre)
- `apple-touch-icon.png` (180×180) — convertir desde `icon.svg`.
- `favicon.ico` multi-size (16/32/48) — herramienta: realfavicongenerator.net.
- `og-image.png` (1200×630 PNG) — convertir desde `og-image.svg` para mejor compatibilidad social.
- Variante negra `wordmark-black.svg` para impreso.

## Reglas de uso
- **Espacio mínimo alrededor del wordmark**: altura de la "x" del wordmark.
- **Tamaño mínimo**: 80px de ancho web, 24mm impreso.
- **Fondo claro**: usa wordmark `--blue-600` o negro.
- **Fondo oscuro / foto**: usa versión blanca.
- **NUNCA**: estirar, rotar, cambiar color fuera de la paleta, agregar efectos.

## Siguientes pasos
1. Iterar concepto wordmark en Figma o herramienta similar.
2. Exportar SVG optimizado (sin metadata).
3. Generar favicons con `realfavicongenerator.net` o equivalente.
4. Diseñar OG image con tagline.
