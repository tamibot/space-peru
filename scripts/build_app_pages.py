#!/usr/bin/env python3
"""Genera las páginas estáticas de fichas de espacio desde spaces.json.

Incluye:
- Hero con título + meta + verified badge
- Galería de fotos con lightbox CSS-only
- Descripción + casos de uso + amenities + ubicación
- Mapa OpenStreetMap embebido (sin API key)
- Reseñas
- Cotizador (fecha + personas + horas) que arma WhatsApp pre-rellenado
- Aside sticky con precio + WhatsApp directo

Output: app/web/espacios/<slug>.html
Idempotente — sobreescribe.
"""
from __future__ import annotations

import json
import html
from pathlib import Path
from urllib.parse import quote

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
    reviews_count = s["reviews_count"]
    precio = s["precio_hora_pen"]
    cap = s["capacidad_max"]
    fotos = s["fotos"]
    lat = s["lat"]
    lng = s["lng"]
    bloque_min = s["bloque_minimo_horas"]

    # Galería: pad a 4 fotos rotando si tiene menos
    while len(fotos) < 4:
        fotos = fotos + fotos
    gallery_fotos = fotos[:4]
    photo_main = fotos[0]

    amenities_html = "\n".join(
        f'        <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 13l4 4L19 7"/></svg> {html.escape(AMENITY_LABELS.get(a, a))}</li>'
        for a in s["amenities"]
    )

    casos_html = ", ".join(html.escape(CATEGORIA_LABELS.get(c, c)) for c in s["casos_uso"])

    verified_html = (
        '<span class="verified-badge"><svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M5 13l4 4L19 7"/></svg> Verificado</span>'
        if s["verificado"] else ""
    )

    # WhatsApp (cotización rápida, sin fechas)
    wa_text_quick = f"Hola, vi {s['name']} en Coordina Eventos y me interesa coordinar una visita. ¿Tienes disponibilidad?"
    wa_link_quick = f"https://wa.me/?text={quote(wa_text_quick)}"

    # Galería HTML — CSS-only lightbox usando :target
    gallery_items = []
    for i, foto in enumerate(gallery_fotos):
        gallery_items.append(
            f'      <a href="#ph-{s["id"]}-{i}" class="gal-item gal-item-{i}">'
            f'<img src="{foto}" alt="{name} foto {i+1}" loading="{"eager" if i == 0 else "lazy"}" />'
            f'</a>'
        )
    gallery_html = "\n".join(gallery_items)

    # Lightbox dialogs
    lightbox_html = "\n".join(
        f'  <div id="ph-{s["id"]}-{i}" class="lightbox"><a href="#" class="lightbox-close">×</a>'
        f'<a href="#ph-{s["id"]}-{(i - 1) % len(gallery_fotos)}" class="lightbox-prev">‹</a>'
        f'<a href="#ph-{s["id"]}-{(i + 1) % len(gallery_fotos)}" class="lightbox-next">›</a>'
        f'<img src="{foto}" alt="{name} foto {i+1}" /></div>'
        for i, foto in enumerate(gallery_fotos)
    )

    # Reseñas HTML
    reviews_html = ""
    if s.get("reseñas"):
        review_items = []
        for r in s["reseñas"]:
            stars = "★" * r["rating"] + "☆" * (5 - r["rating"])
            d = html.escape(r["date"])
            n = html.escape(r["name"])
            c = html.escape(r["comment"])
            review_items.append(
                f'        <article class="review">'
                f'<div class="review-head"><strong>{n}</strong><span class="review-stars">{stars}</span></div>'
                f'<time>{d}</time>'
                f'<p>{c}</p>'
                f'</article>'
            )
        reviews_html = "\n".join(review_items)

    # OpenStreetMap embed (sin API key)
    bbox = f"{lng-0.005},{lat-0.004},{lng+0.005},{lat+0.004}"
    map_iframe = (
        f'<iframe class="osm-map" '
        f'src="https://www.openstreetmap.org/export/embed.html?bbox={bbox}&amp;layer=mapnik&amp;marker={lat},{lng}" '
        f'title="Ubicación de {name} en {distrito}" loading="lazy"></iframe>'
        f'<a class="osm-link" href="https://www.openstreetmap.org/?mlat={lat}&amp;mlon={lng}#map=16/{lat}/{lng}" '
        f'target="_blank" rel="noopener">Ver mapa más grande →</a>'
    )

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
    <!-- HERO -->
    <section class="detail-hero">
      <div class="detail-breadcrumbs">
        <a href="../index.html">Catálogo</a>
        <span>›</span>
        <a href="../buscar.html?distrito={quote(distrito)}">{distrito}</a>
        <span>›</span>
        <span>{name}</span>
      </div>
      <h1>{name}</h1>
      <div class="detail-meta">
        <span class="star">★ {rating}</span>
        <span>{reviews_count} reseñas</span>
        <span>·</span>
        <span>{tipo}</span>
        <span>·</span>
        <span>{distrito}</span>
        {verified_html}
      </div>
    </section>

    <!-- GALERÍA con lightbox -->
    <section class="gallery-block">
{gallery_html}
    </section>

    <!-- DETALLE GRID -->
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
          <p style="margin-bottom: 16px;">{direccion}</p>
          <div class="map-wrap">
            {map_iframe}
          </div>
        </div>

        <div class="detail-section">
          <h2>Reseñas <span class="reviews-count-inline">({reviews_count} totales)</span></h2>
          <div class="reviews-grid">
{reviews_html}
          </div>
        </div>

      </div>

      <!-- ASIDE: cotizador + WhatsApp -->
      <aside class="detail-aside">
        <div class="price-block">
          <b>S/ {precio}</b>
          <span>/ hora</span>
          <span class="price-min">Mínimo {bloque_min} {'horas' if bloque_min > 1 else 'hora'}</span>
        </div>

        <form class="quote-form" data-precio="{precio}" data-bloque-min="{bloque_min}" data-cap-max="{cap}" data-name="{name}" data-distrito="{distrito}">
          <h3 class="quote-title">Cotiza tu evento</h3>

          <label class="quote-field">
            <span>Fecha</span>
            <input type="date" name="fecha" required />
          </label>

          <label class="quote-field">
            <span>Personas</span>
            <input type="number" name="personas" min="1" max="{cap}" placeholder="Hasta {cap}" required />
          </label>

          <label class="quote-field">
            <span>Duración (horas)</span>
            <input type="number" name="horas" min="{bloque_min}" max="12" value="{bloque_min}" required />
          </label>

          <div class="quote-summary">
            <div class="quote-row"><span>Subtotal</span><b id="qf-subtotal">S/ {precio * bloque_min:,}</b></div>
            <div class="quote-row quote-row-total"><span>Total estimado</span><b id="qf-total">S/ {precio * bloque_min:,}</b></div>
          </div>

          <button type="submit" class="btn btn-primary btn-block quote-submit">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413z"/></svg>
            Coordinar por WhatsApp
          </button>
        </form>

        <ul class="quick">
          <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 13l4 4L19 7"/></svg> Capacidad hasta {cap} personas</li>
          <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 13l4 4L19 7"/></svg> Coordinas directo con el encargado</li>
          <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 13l4 4L19 7"/></svg> Sin pagos por adelantado</li>
        </ul>

        <a href="../asistente.html" class="btn btn-light btn-block">¿Otras opciones? Probar asistente IA</a>
      </aside>
    </div>
  </div>
</main>

<!-- LIGHTBOXES (CSS-only) -->
{lightbox_html}

<footer class="footer">
  <div class="container footer-content">
    <span>© 2026 Coordina Eventos · Lima, Perú</span>
    <a href="../buscar.html">← Ver todos los espacios</a>
  </div>
</footer>

<script>
// Cotizador inline
(() => {{
  const form = document.querySelector('.quote-form');
  if (!form) return;
  const precio = parseFloat(form.dataset.precio);
  const bloqueMin = parseInt(form.dataset.bloqueMin, 10);
  const capMax = parseInt(form.dataset.capMax, 10);
  const name = form.dataset.name;
  const distrito = form.dataset.distrito;

  const fmt = (n) => 'S/ ' + Math.round(n).toLocaleString('es-PE');

  function update() {{
    const horas = parseInt(form.querySelector('[name=horas]').value, 10) || bloqueMin;
    const personas = parseInt(form.querySelector('[name=personas]').value, 10) || 0;
    const fecha = form.querySelector('[name=fecha]').value;
    const total = precio * horas;
    document.getElementById('qf-subtotal').textContent = fmt(total);
    document.getElementById('qf-total').textContent = fmt(total);
    return {{ horas, personas, fecha, total }};
  }}

  form.querySelectorAll('input').forEach(inp => inp.addEventListener('input', update));

  form.addEventListener('submit', (e) => {{
    e.preventDefault();
    const {{ horas, personas, fecha, total }} = update();
    if (!fecha || !personas) {{
      alert('Completa fecha y cantidad de personas para cotizar.');
      return;
    }}
    if (personas > capMax) {{
      alert(`Capacidad máxima de este espacio: ${{capMax}} personas.`);
      return;
    }}
    const text = `Hola, vi ${{name}} (${{distrito}}) en Coordina Eventos y quiero cotizar:\\n\\n` +
      `📅 Fecha: ${{fecha}}\\n` +
      `👥 Personas: ${{personas}}\\n` +
      `⏱  Duración: ${{horas}} h\\n` +
      `💰 Estimado: S/ ${{total.toLocaleString('es-PE')}}\\n\\n` +
      `¿Tienes disponibilidad?`;
    window.open('https://wa.me/?text=' + encodeURIComponent(text), '_blank', 'noopener');
  }});

  update();
}})();
</script>

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
