# Data

Datasets, fixtures, exports.

## Estructura
```
data/
  public/        # commiteable: categorías, distritos, fixtures de ejemplo
  raw/           # scrapings, exports — NO commitear (gitignored)
  private/       # data sensible — NO commitear (gitignored)
  hosts-prospects/  # briefs por host (gitignored si tiene PII)
```

## Inicial
- `public/categorias.json` — categorías oficiales del marketplace
- `public/distritos-lima.json` — distritos prioritarios con metadata
- `public/equipamiento.json` — diccionario de amenities
