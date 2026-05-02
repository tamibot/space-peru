#!/usr/bin/env python3
"""Genera las páginas estáticas de fichas de espacio desde spaces.json.

Output: app/web/espacios/<slug>.html (una por espacio).
Lee plantilla embebida abajo. Idempotente — sobrescribe.

Uso:
    python3 scripts/build_app_pages.py
"""
from __future__ import annotations

import json
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "public" / "spaces.json"
OUT_DIR = ROOT / "app" / "web" / "espacios"

AMENITY_LABELS = {
    "wifi": "Wi-Fi",
    "estacionamiento": "Estacionamiento",
    "cocina": "Cocina equipada",
    "terraza": "Terraza",
    "sonido": "Sonido profesional",
    "iluminacion": "Iluminación",
    "aire-acondicionado": "Aire acondicionado",
    "tv": "Smart TV",
    "proyector": "Proyector",
    "microfonos": "Micrófonos",
    "ciclorama": "Ciclorama",
    "vestidor": "Vestidor / camerino",
    "duchas": "Duchas",
    "cafe": "Café incluido",
    "accesible": "Accesible",
    "vidriera": "Vitrina a la calle",
}

CATEGORIA_LABELS = {
    "cumpleanos": "Cumpleaños",
    "baby-shower": "Baby shower",
    "sesion-fotos": "Sesión de fotos",
    "reunion": "Reunión de trabajo",
    "capacitacion": "Capacitación",
    "conferencia": "Conferencia",
    "yoga-clase": "Yoga · clase",
    "despedida": "Despedida",
    "pop-up": "Pop-up",
    "aniversario": "Aniversario",
    "coworking": "Coworking",
    "lanzamiento": "Lanzamiento",
    "boda": "Boda",
    "grabacion-video": "Grabación de video",
    "podcast": "Podcast",
    "talleres": "Talleres",
}


def render_page(s: dict) -> str:
    name = html.escape(s["name"])
    tipo = html.escape(s["tipo"])
    distrito = html.escape(s["distrito"])
    direccion = html.escape(s["direccion"])
    descripcion = html.escape(s["descripcion"])
    rating = s["rating"]
    reviews = s["reviews_count"]
    precio = s["precio_hora_pen"]
    cap = s["capacidad_max"]
    fotos = s["fotos"]
    photo1 = fotos[0]
    photo2 = fotos[1] if len(fotos) > 1 else fotos[0]
    photo3 = fotos[2] if len(fotos) > 2 else (fotos[1] if len(fotos) > 1 else fotos[0])

    amenities_html = "\n".join(
        f'        <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 13l4 4L19 7"/></svg> {html.escape(AMENITY_LABELS.get(a, a))}</li>'
        for a in s["amenities"]
    )

    casos_html = ", ".join(html.escape(CATEGORIA_LABELS.get(c, c)) for c in s["casos_uso"])

    verified_html = (
        '<span class="verified-badge"><svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M5 13l4 4L19 7"/></svg> Verificado</span>'
        if s["verificado"] else ""
    )

    wa_text = f"Hola, vi {name} en Coordina Eventos y me interesa coordinar una visita. ¿Tienes disponibilidad?"
    wa_link = f"https://wa.me/?text={wa_text.replace(' ', '%20').replace(',', '%2C').replace('?', '%3F').replace('¿', '%C2%BF')}"

    return f"""<!doctype html>
<html lang="es-PE">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>{name} — {tipo} en {distrito} · Coordina Eventos</title>
  <meta name="description" content="{descripcion[:155]}" />
  <meta name="theme-color" content="#0A2540" />
  <link rel="icon" href="../../../brand/logo/favicon.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="../styles.css" />
</head>
<body>

<header class="nav">
  <div class="nav-inner">
    <a class="brand" href="../index.html">coordina<span class="brand-suffix">eventos</span></a>
    <nav class="nav-links">
      <a href="../buscar.html">← Volver al catálogo</a>
      <a href="../asistente.html">Asistente IA</a>
      <a href="../../../" class="nav-back">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
        Landing
      </a>
    </nav>
  </div>
</header>

<main>
  <div class="container">
    <section class="detail-hero">
      <h1>{name}</h1>
      <div class="detail-meta">
        <span class="star">★ {rating}</span>
        <span>{reviews} reseñas</span>
        <span>·</span>
        <span>{tipo}</span>
        <span>·</span>
        <span>{distrito}</span>
        {verified_html}
      </div>
    </section>

    <div class="detail-photos">
      <div class="ph"><img src="{photo1}" alt="{name}" loading="eager" /></div>
      <div class="ph"><img src="{photo2}" alt="{name}" loading="lazy" /></div>
      <div class="ph"><img src="{photo3}" alt="{name}" loading="lazy" /></div>
    </div>

    <div class="detail-grid">
      <div class="detail-main">
        <div class="detail-section">
          <h2>Sobre el espacio</h2>
          <p>{descripcion}</p>
        </div>

        <div class="detail-section">
          <h2>Para qué sirve</h2>
          <p>{casos_html}</p>
        </div>

        <div class="detail-section">
          <h2>Equipamiento</h2>
          <ul class="amenities">
{amenities_html}
          </ul>
        </div>

        <div class="detail-section">
          <h2>Ubicación</h2>
          <p>{direccion}</p>
        </div>
      </div>

      <aside class="detail-aside">
        <div class="price-block">
          <b>S/ {precio}</b>
          <span>/ hora</span>
        </div>
        <a href="{wa_link}" class="btn btn-primary btn-block" target="_blank" rel="noopener">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413z"/></svg>
          Coordinar por WhatsApp
        </a>
        <ul class="quick">
          <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 13l4 4L19 7"/></svg> Capacidad hasta {cap} personas</li>
          <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 13l4 4L19 7"/></svg> Coordinas directo con el encargado</li>
          <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 13l4 4L19 7"/></svg> Sin pagos por adelantado</li>
        </ul>
        <a href="../asistente.html" class="btn btn-light btn-block">¿Necesitas ayuda? Probar asistente IA</a>
      </aside>
    </div>
  </div>
</main>

<footer class="footer">
  <div class="container footer-content">
    <span>© 2026 Coordina Eventos · Lima, Perú</span>
    <a href="../buscar.html">← Ver todos los espacios</a>
  </div>
</footer>

</body>
</html>
"""


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    data = json.loads(DATA.read_text(encoding="utf-8"))
    spaces = data["spaces"]
    for s in spaces:
        out_file = OUT_DIR / f"{s['slug']}.html"
        out_file.write_text(render_page(s), encoding="utf-8")
        print(f"  ✓ {out_file.relative_to(ROOT)}")
    print(f"\nGeneradas {len(spaces)} fichas en {OUT_DIR.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
