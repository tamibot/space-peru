---
name: space-pricing-helper
description: Sugiere tarifa por hora para un espacio en Lima dado: distrito, categoría, capacidad, equipamiento. Usa comparables de mercado.
---

# space-pricing-helper

## Inputs requeridos
- Distrito
- Categoría (salón eventos / loft fotográfico / sala reuniones / estudio / espacio deportivo / otro)
- Capacidad (personas)
- Equipamiento clave (proyector, sonido, cocina, parking, etc.)
- Horario solicitado (turno mañana / tarde / noche / fin de semana)

## Output
- Rango sugerido (mínimo / medio / máximo) por hora en PEN
- 3-5 comparables con URL de Space-Pal, Comparto, Marketplace, etc.
- Notas sobre temporada (alta: nov-feb, dic eventos corporativos)

## Heurísticas iniciales (refinar con data real)
- Salón eventos Miraflores 50 pers: S/ 200–400/hora
- Loft fotográfico San Isidro: S/ 80–150/hora
- Sala reuniones coworking Miraflores 8 pers: S/ 40–80/hora
- Estudio de yoga Barranco: S/ 30–60/hora
- Cancha sintética Surco: S/ 80–140/hora

> Nota: estos rangos son [a validar] con scraping de Space-Pal y comparables. Refinar tras research.

## Disclaimers
- Precio sugerido, no impuesto.
- Host decide final.
- Comisión del marketplace se suma encima (a definir).
