#!/usr/bin/env python3
"""Genera páginas estáticas de detalle de espacio. Layout Peerspace-style.

Estructura:
- Nav con SPA navigation
- Breadcrumb
- Title + stats + verified badge inline
- Galería: hero + 4 thumbnails grid (NO una foto gigante)
- Layout 2 cols: contenido izquierda + sticky pricing card derecha
- Sobre el espacio, amenidades agrupadas, host card, reseñas, mapa, similares
- Botón flotante asistente IA
- Footer

Output: app/web/espacios/<slug>.html (sobreescribe).
"""
from __future__ import annotations

import json
import html
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "public" / "spaces.json"
OUT_DIR = ROOT / "app" / "web" / "espacios"

AMENITIES_GROUPED = {
    "Conectividad y AV": {
        "wifi": "Wi-Fi de alta velocidad",
        "tv": "Smart TV",
        "proyector": "Proyector",
        "sonido": "Sonido profesional",
        "microfonos": "Micrófonos",
        "iluminacion": "Iluminación profesional",
    },
    "Cocina y servicios": {
        "cocina": "Cocina equipada",
        "cafe": "Café incluido",
    },
    "Comodidades": {
        "aire-acondicionado": "Aire acondicionado",
        "vestidor": "Vestidor / camerino",
        "duchas": "Duchas",
        "accesible": "Acceso para movilidad reducida",
    },
    "Espacios": {
        "terraza": "Terraza",
        "ciclorama": "Ciclorama fotográfico",
        "vidriera": "Vitrina a la calle",
    },
    "Acceso": {
        "estacionamiento": "Estacionamiento",
    },
}

CATEGORIA_LABELS = {
    "cumpleanos": "Cumpleaños", "baby-shower": "Baby shower",
    "sesion-fotos": "Sesión de fotos", "reunion": "Reunión de trabajo",
    "capacitacion": "Capacitación", "conferencia": "Conferencia",
    "yoga-clase": "Yoga · clase", "despedida": "Despedida",
    "pop-up": "Pop-up", "aniversario": "Aniversario",
    "coworking": "Coworking", "lanzamiento": "Lanzamiento",
    "boda": "Boda", "grabacion-video": "Grabación de video",
    "podcast": "Podcast", "cena-corporativa": "Cena corporativa",
    "evento-corporativo": "Evento corporativo", "talleres": "Talleres",
}

MONTHS_ES = {
    1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
    5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
    9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre",
}


def fmt_date(date_str: str) -> str:
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return f"{dt.day} de {MONTHS_ES[dt.month]}, {dt.year}"
    except Exception:
        return date_str


def stars(rating: float) -> str:
    full = int(rating)
    half = rating - full >= 0.5
    s = "★" * full
    if half:
        s += "★"
        full += 1
    s += "☆" * (5 - full)
    return s


def verified_svg(size: int = 16) -> str:
    return (
        f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" aria-hidden="true" class="verified-svg">'
        '<circle cx="12" cy="12" r="11" fill="#1D9BF0"/>'
        '<path d="M7 12.5 L10.5 16 L17 9" stroke="white" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
        '</svg>'
    )


def amenities_html(amenity_slugs: list[str]) -> str:
    if not amenity_slugs:
        return ""
    rendered = []
    for group_name, items in AMENITIES_GROUPED.items():
        matched = [(slug, label) for slug, label in items.items() if slug in amenity_slugs]
        if not matched:
            continue
        items_html = "\n".join(
            f'<li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M5 13l4 4L19 7"/></svg> {label}</li>'
            for _, label in matched
        )
        rendered.append(f'<div class="amenity-group"><h4>{group_name}</h4><ul>{items_html}</ul></div>')
    return f'<div class="amenities-grid">{"".join(rendered)}</div>'


def whatsapp_link(space: dict) -> str:
    msg = (
        f"Hola, vi tu espacio *{space['name']}* en coordinaeventos "
        f"({space['distrito']}, capacidad {space['capacidad_max']} personas). "
        "Me gustaría coordinar una visita."
    )
    phone = space.get('host_phone', '+51999999999').replace('+', '').replace(' ', '')
    return f"https://wa.me/{phone}?text={quote(msg)}"


def render_page(space: dict, all_spaces: list[dict]) -> str:
    name = space['name']
    slug = space['slug']
    distrito = space['distrito']
    direccion = space.get('direccion', distrito)
    tipo = space['tipo']
    capacidad = space['capacidad_max']
    precio = space['precio_hora_pen']
    fotos = space.get('fotos', [])[:5]
    rating = space.get('rating', 0)
    reviews_count = space.get('reviews_count', 0)
    verificado = space.get('verificado', False)
    lat = space.get('lat', -12.046)
    lng = space.get('lng', -77.043)
    descripcion = space.get('descripcion', '')
    highlights = space.get('highlights', [])
    bloque_min = space.get('bloque_minimo_horas', 2)
    reseñas = space.get('reseñas', [])
    casos_uso = space.get('casos_uso', [])
    listado_desde = space.get('listado_desde', '2026-01-01')

    hero_photo = fotos[0] if fotos else ''
    thumbnails = fotos[1:5] if len(fotos) > 1 else []
    casos_tags = " · ".join(CATEGORIA_LABELS.get(c, c) for c in casos_uso[:4])

    map_bbox = f"{lng-0.005},{lat-0.003},{lng+0.005},{lat+0.003}"
    map_url = f"https://www.openstreetmap.org/export/embed.html?bbox={map_bbox}&layer=mapnik&marker={lat},{lng}"

    reseñas_html = ""
    if reseñas:
        reseñas_html = '<div class="reviews-list">'
        for r in reseñas:
            author = r.get('autor', 'Cliente')
            rating_r = r.get('rating', 5)
            fecha = fmt_date(r.get('fecha', ''))
            comentario = r.get('comentario', '')
            initials = ''.join(w[0] for w in author.split()[:2]).upper()
            reseñas_html += f'<article class="review"><div class="review-head"><div class="review-avatar">{initials}</div><div class="review-meta"><strong>{html.escape(author)}</strong><span class="review-date">{fecha}</span></div><div class="review-rating" aria-label="Rating {rating_r}/5">{stars(rating_r)}</div></div><p class="review-comment">{html.escape(comentario)}</p></article>'
        reseñas_html += '</div>'

    same_district = [s for s in all_spaces if s['slug'] != slug and s['distrito'] == distrito][:3]
    if len(same_district) < 3:
        others = [s for s in all_spaces if s['slug'] != slug and s not in same_district][: 3 - len(same_district)]
        same_district = same_district + others

    host_more_html = ""
    if same_district:
        for s in same_district:
            host_more_html += f'<a class="host-more-card" href="./{s["slug"]}.html" data-spa-link><div class="host-more-photo"><img src="{s["fotos"][0]}" alt="{s["name"]}" loading="lazy" /></div><div class="host-more-body"><strong>{s["name"]}</strong><span>{s["distrito"]} · Desde S/ {s["precio_hora_pen"]}/h</span></div></a>'

    similares = sorted(
        [s for s in all_spaces if s['slug'] != slug],
        key=lambda s: abs(s.get('precio_hora_pen', 0) - precio) + abs(s.get('capacidad_max', 0) - capacidad)
    )[:4]
    similares_html = ""
    pin_svg = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-7-7-12a7 7 0 0 1 14 0c0 5-7 12-7 12z"/><circle cx="12" cy="9" r="2.4"/></svg>'
    users_svg = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="9" r="3.5"/><path d="M2 20c0-4 3.5-6 7-6s7 2 7 6"/><path d="M16 5a3.5 3.5 0 0 1 0 7M21.5 20c0-2.7-2-4.5-4.5-5"/></svg>'
    home_svg = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-8 9 8v9a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z"/></svg>'
    star_svg = '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3 7 7.5.5-5.7 4.9 1.8 7.3L12 17.8 5.4 21.7l1.8-7.3L1.5 9.5 9 9z"/></svg>'
    for s in similares:
        v_chip = f'<span class="verified-chip">{verified_svg(14)}<span>Verificado</span></span>' if s.get('verificado') else ''
        s_rating = f'<span class="listing-card-rating">{star_svg} {s.get("rating",0):.1f} <span>({s.get("reviews_count",0)})</span></span>' if s.get('rating') else ''
        s_tipo = s.get('tipo', '')
        s_dir = s.get('direccion', s.get('distrito',''))
        s_brief = s_dir.split(',')[0]
        similares_html += (
            f'<a class="listing-card" href="./{s["slug"]}.html" data-spa-link>'
            f'<div class="listing-card-photo"><img src="{s["fotos"][0]}" alt="{s["name"]}" loading="lazy" />{v_chip}</div>'
            f'<div class="listing-card-body">'
            f'<div class="listing-card-head"><h3>{s["name"]}</h3>{s_rating}</div>'
            f'<ul class="listing-card-details">'
            f'<li>{pin_svg} <span>{s_brief}<strong> · {s["distrito"]}</strong></span></li>'
            f'<li>{users_svg} <span>Hasta <strong>{s["capacidad_max"]}</strong> personas</span></li>'
            f'<li>{home_svg} <span>{s_tipo}</span></li>'
            f'</ul>'
            f'<div class="listing-card-foot">'
            f'<span class="listing-card-price"><strong>S/ {s["precio_hora_pen"]}</strong><em>por hora</em></span>'
            f'<span class="listing-card-cta">Ver detalle →</span>'
            f'</div>'
            f'</div></a>'
        )

    verified_inline = f'{verified_svg(18)}<span>Espacio verificado</span>' if verificado else ''

    thumb_html = ""
    for i, t in enumerate(thumbnails):
        thumb_html += f'<div class="gallery-thumb"><img src="{t}" alt="{name} - foto {i+2}" loading="lazy" /></div>'
    for _ in range(4 - len(thumbnails)):
        thumb_html += '<div class="gallery-thumb gallery-thumb-empty"></div>'

    highlights_html = ""
    if highlights:
        highlights_html = '<ul class="highlights">'
        for h in highlights:
            highlights_html += f'<li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M5 13l4 4L19 7"/></svg>{html.escape(h)}</li>'
        highlights_html += '</ul>'

    stat_verified = f'<span class="detail-stat-sep">·</span><span class="detail-verified">{verified_inline}</span>' if verificado else ''
    casos_section = f'<section class="detail-section"><h2>Ideal para</h2><p class="detail-tags">{casos_tags}</p></section>' if casos_tags else ''
    host_more_section = f'<div class="host-more"><h3>Más espacios en {distrito}</h3><div class="host-more-grid">{host_more_html}</div></div>' if host_more_html else ''
    reseñas_section = f'<section class="detail-section"><h2>Reseñas ({reviews_count})</h2>{reseñas_html}</section>' if reseñas_html else ''
    verified_in_host = "Verificado · " if verificado else ""

    return f'''<!doctype html>
<html lang="es-PE">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>{html.escape(name)} — coordinaeventos</title>
  <meta name="description" content="{html.escape(name)} en {distrito}. Hasta {capacidad} personas. Desde S/ {precio}/h. {html.escape(descripcion[:120])}" />
  <meta name="theme-color" content="#0A0A0A" />
  <link rel="icon" href="../../../brand/logo/favicon.svg" type="image/svg+xml" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="preconnect" href="https://images.unsplash.com" />
  <link rel="preload" as="image" href="{hero_photo}" fetchpriority="high" />
  <link rel="stylesheet" href="../styles.css?v=2026-05-11-2" />
</head>
<body data-page="detail">

<div class="demo-banner">
  <strong>Catálogo demo</strong> · Los primeros hosts reales se publican en junio 2026 ·
  <a href="../../../#hosts">¿Tienes un espacio? Publica gratis →</a>
</div>

<header class="nav" id="nav">
  <div class="nav-inner">
    <a class="brand" href="../../../" data-spa-link>coordina<span class="brand-suffix">eventos</span></a>
    <nav class="nav-links">
      <a href="../buscar.html" data-spa-link>Espacios</a>
      <a href="../concierge.html" data-spa-link>Organización de eventos</a>
      <a href="../como-funciona.html" data-spa-link>Cómo funciona</a>
      <a href="../publicar.html" data-spa-link>Para hosts</a>
      <a href="../ayuda.html" data-spa-link>Ayuda</a>
      <a href="../../../" class="nav-back" data-spa-link>← Inicio</a>
    </nav>
  </div>
</header>

<main class="detail-page">
  <div class="container">

    <nav class="breadcrumb" aria-label="Navegación">
      <a href="../buscar.html" data-spa-link>Catálogo</a>
      <span class="breadcrumb-sep">/</span>
      <a href="../buscar.html?distrito={quote(distrito)}" data-spa-link>{distrito}</a>
      <span class="breadcrumb-sep">/</span>
      <span class="breadcrumb-current">{html.escape(name)}</span>
    </nav>

    <header class="detail-header">
      <h1>{html.escape(name)}</h1>
      <div class="detail-stats">
        <span class="detail-stat"><strong>★ {rating}</strong> · {reviews_count} reseñas</span>
        <span class="detail-stat-sep">·</span>
        <span class="detail-stat">{tipo}</span>
        <span class="detail-stat-sep">·</span>
        <span class="detail-stat">Hasta {capacidad} personas</span>
        <span class="detail-stat-sep">·</span>
        <span class="detail-stat">{distrito}</span>
        {stat_verified}
      </div>
    </header>

    <section class="gallery" aria-label="Galería de fotos">
      <div class="gallery-hero">
        <img src="{hero_photo}" alt="{html.escape(name)} - foto principal" loading="eager" />
      </div>
      <div class="gallery-thumbs">
{thumb_html}
      </div>
    </section>

    <div class="detail-grid">
      <div class="detail-content">

        <section class="detail-section">
          <h2>Sobre el espacio</h2>
          <p class="detail-description">{html.escape(descripcion)}</p>
          {highlights_html}
        </section>

        {casos_section}

        <section class="detail-section">
          <h2>Lo que incluye</h2>
          {amenities_html(space.get('amenities', []))}
        </section>

        <section class="detail-section">
          <h2>Ubicación</h2>
          <p class="detail-address">{html.escape(direccion)}</p>
          <p class="detail-address-note">Dirección exacta después de coordinar la visita con el host.</p>
          <div class="detail-map">
            <iframe src="{map_url}" loading="lazy" title="Mapa de {html.escape(name)}"></iframe>
          </div>
        </section>

        <section class="detail-section">
          <h2>Sobre el host</h2>
          <div class="host-card">
            <div class="host-avatar">{slug[0].upper()}H</div>
            <div class="host-info">
              <strong>Host de {html.escape(name)}</strong>
              <span class="host-meta">{verified_in_host}Responde en 2 horas · Listado desde {fmt_date(listado_desde)}</span>
            </div>
            <a href="{whatsapp_link(space)}" class="btn btn-outline btn-sm" target="_blank" rel="noopener">Contactar</a>
          </div>
          {host_more_section}
        </section>

        {reseñas_section}

      </div>

      <aside class="pricing-card-wrap">
        <div class="pricing-card">
          <div class="pricing-card-head">
            <strong class="pricing-amount">Desde S/ {precio}<span>/hora</span></strong>
            <span class="pricing-min">Mínimo {bloque_min} horas</span>
          </div>
          <form class="pricing-form">
            <label class="pricing-field">
              <span>Fecha</span>
              <input type="date" name="fecha" />
            </label>
            <label class="pricing-field">
              <span>Personas</span>
              <input type="number" name="personas" min="1" max="{capacidad}" placeholder="Hasta {capacidad}" />
            </label>
            <label class="pricing-field">
              <span>Horas</span>
              <input type="number" name="horas" min="{bloque_min}" placeholder="Mín. {bloque_min}" />
            </label>
          </form>
          <a href="{whatsapp_link(space)}" target="_blank" rel="noopener" class="btn btn-primary btn-full">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="white" aria-hidden="true">
              <path d="M17.5 14.4c-.3-.1-1.7-.8-1.9-.9-.3-.1-.5-.1-.7.1-.2.3-.8.9-.9 1.1-.2.2-.3.2-.6.1-.9-.4-1.7-1-2.4-1.7-.6-.6-1.2-1.4-1.6-2.2-.2-.3 0-.5.1-.6.1-.1.3-.3.4-.5.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5-.1-.1-.7-1.6-.9-2.2-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5 0 1.5 1.1 2.9 1.2 3.1.2.2 2.1 3.2 5.1 4.5 1.2.5 2.1.8 2.8.7.7-.1 1.7-.7 1.9-1.4.2-.6.2-1.2.1-1.4 0-.2-.2-.2-.5-.4z M20.5 3.5C18.3 1.2 15.4 0 12.3 0 5.9 0 .7 5.2.7 11.6c0 2 .5 4 1.5 5.7L.5 24l6.9-1.8c1.7.9 3.5 1.4 5.4 1.4 6.4 0 11.6-5.2 11.6-11.6 0-3.1-1.2-6-3.4-8.2z"/>
            </svg>
            Contactar por WhatsApp
          </a>
          <p class="pricing-note">Coordinas directo con el host. Sin pago anticipado en plataforma.</p>
          <div class="pricing-divider"></div>
          <a href="../../../#concierge" class="btn btn-outline btn-full btn-sm">
            Pedir al equipo que lo gestione
          </a>
        </div>
      </aside>

    </div>

    <section class="detail-section detail-similar">
      <h2>Espacios similares</h2>
      <div class="grid grid-similares">
{similares_html}
      </div>
    </section>

  </div>
</main>

<button class="ai-fab" id="ai-fab" aria-label="Abrir asistente IA">
  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.2" aria-hidden="true">
    <path d="M12 2 C6.5 2 2 6.5 2 12 C2 14 2.5 15.8 3.4 17.4 L2 22 L6.6 20.6 C8.2 21.5 10 22 12 22 C17.5 22 22 17.5 22 12 C22 6.5 17.5 2 12 2 Z"/>
    <circle cx="8" cy="12" r="1" fill="white"/>
    <circle cx="12" cy="12" r="1" fill="white"/>
    <circle cx="16" cy="12" r="1" fill="white"/>
  </svg>
  <span class="ai-fab-label">Asistente IA</span>
</button>

<footer class="footer-app">
  <div class="container">
    <div class="footer-app-grid">
      <div class="footer-app-brand">
        <a class="brand" href="../../../" data-spa-link>coordina<span class="brand-suffix">eventos</span></a>
        <p>Espacios por horas en Lima. Coordinas la visita por WhatsApp. Si no tienes tiempo, lo armamos contigo.</p>
        <span class="footer-app-domain">coordinaeventos.com</span>
      </div>
      <div class="footer-app-col">
        <h4>Explorar</h4>
        <a href="../buscar.html" data-spa-link>Espacios</a>
        <a href="../concierge.html" data-spa-link>Organización de eventos</a>
        <a href="../como-funciona.html" data-spa-link>Cómo funciona</a>
        <a href="../ayuda.html" data-spa-link>Centro de ayuda</a>
      </div>
      <div class="footer-app-col">
        <h4>Hosts</h4>
        <a href="../publicar.html" data-spa-link>Publicar mi espacio</a>
        <a href="../verificate.html" data-spa-link>Verificación</a>
        <a href="../publicar.html#cobros" data-spa-link>Cómo cobras</a>
        <a href="../publicar.html#empresas" data-spa-link>Para empresas</a>
      </div>
      <div class="footer-app-col">
        <h4>coordinaeventos</h4>
        <a href="../sobre.html" data-spa-link>Sobre nosotros</a>
        <a href="../contacto.html" data-spa-link>Contacto</a>
        <a href="mailto:mvelascoo@tamibot.com">mvelascoo@tamibot.com</a>
      </div>
      <div class="footer-app-col">
        <h4>Legal</h4>
        <a href="../legal/terminos.html" data-spa-link>Términos y condiciones</a>
        <a href="../legal/privacidad.html" data-spa-link>Política de privacidad</a>
        <a href="../legal/cookies.html" data-spa-link>Política de cookies</a>
        <a href="../legal/libro-reclamaciones.html" data-spa-link>Libro de reclamaciones</a>
      </div>
    </div>
    <div class="footer-app-bottom">
      <span>© 2026 coordinaeventos · Lima, Perú</span>
      <span>Imágenes de referencia: <a href="https://unsplash.com/" target="_blank" rel="noopener">Unsplash</a></span>
    </div>
  </div>
</footer>

<script src="../app.js?v=2026-05-11-2"></script>
</body>
</html>
'''


def main() -> int:
    data = json.loads(DATA.read_text())
    spaces = data["spaces"]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for s in spaces:
        out_file = OUT_DIR / f"{s['slug']}.html"
        out_file.write_text(render_page(s, spaces), encoding="utf-8")
        print(f"  ✓ {out_file.relative_to(ROOT)}")
    print(f"\nGeneradas {len(spaces)} fichas en {OUT_DIR.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
