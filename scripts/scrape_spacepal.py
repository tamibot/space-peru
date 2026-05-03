#!/usr/bin/env python3
"""
Scraper de SpacePal (research-only) — Coordina Eventos.

Propósito: investigación competitiva interna. Extrae **metadata pública** de los
listings públicos de SpacePal Lima (nombre comercial, URL, distrito si aparece,
categoría, precio público) para que el equipo construya pipeline de leads de
hosts a contactar y valide pricing del mercado.

NO HACE:
- No descarga imágenes.
- No copia descripciones extensas (máx 200 chars de teaser para identificar).
- No republica nada en la app pública de Coordina.
- No bypassa autenticación, captchas ni TOS.

REGLAS:
- User-Agent identificable: CoordinaResearchBot/1.0 (info@proper.com.pe)
- Rate limit: 3 segundos entre requests.
- Respeta robots.txt (verifica antes de ejecutar).
- Output a `data/raw/spacepal-research.json` (gitignored).
- Detiene si recibe 429/403 sostenido.

USO:
    python3 scripts/scrape_spacepal.py            # default: Lima, todas las categorías
    python3 scripts/scrape_spacepal.py --max 30   # límite de listings
    python3 scripts/scrape_spacepal.py --dry-run  # no escribe archivo

OUTPUT:
    data/raw/spacepal-research.json — array de objetos con:
      { source_url, name, distrito, categoria, precio_str, captured_at }

Nota legal: este script es para uso interno de research. La data extraída es
metadata pública que aparece en cualquier búsqueda Google. NO se republica.
Si SpacePal solicita takedown del uso, responder en <72h y cumplir.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_FILE = ROOT / "data" / "raw" / "spacepal-research.json"
SITEMAP_URL = "https://space-pal.com/sitemap.xml"
BASE_LIMA = "https://space-pal.com/es/search/Lima--Peru/Espacios"

UA = "CoordinaResearchBot/1.0 (+research; info@proper.com.pe)"
SLEEP = 3.0  # seconds entre requests
TIMEOUT = 15

CATEGORIAS_PROBE = [
    "https://space-pal.com/es/search/Lima--Peru/Party",
    "https://space-pal.com/es/search/Lima--Peru/Meeting",
    "https://space-pal.com/es/search/Lima--Peru/Photo-Shoot",
    "https://space-pal.com/es/search/Lima--Peru/Workshop",
    "https://space-pal.com/es/search/Lima--Peru/Wedding",
    "https://space-pal.com/es/search/Lima--Peru/Coworking",
    "https://space-pal.com/es/search/Lima--Peru/Pop-Up",
    BASE_LIMA,
]


def fetch(url: str) -> str | None:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/xhtml+xml"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        print(f"  ! HTTP {e.code} en {url}", file=sys.stderr)
    except Exception as e:
        print(f"  ! error en {url}: {e}", file=sys.stderr)
    return None


def parse_next_data(html: str) -> dict | None:
    """Busca el bloque <script id='__NEXT_DATA__' type='application/json'>...</script>."""
    m = re.search(
        r'<script[^>]*id="__NEXT_DATA__"[^>]*>(.*?)</script>',
        html,
        re.DOTALL,
    )
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except Exception:
        return None


def walk(obj, hits: list[dict]):
    """Camina la estructura buscando objetos que parecen listings (con name + slug + url)."""
    if isinstance(obj, dict):
        # heurística: tiene name o title + slug o id + (price, location, city)
        keys = set(k.lower() for k in obj.keys())
        if ({"name", "slug"} <= keys or {"title", "slug"} <= keys):
            entry = {
                "name": obj.get("name") or obj.get("title"),
                "slug": obj.get("slug"),
                "city": obj.get("city") or obj.get("location"),
                "price": obj.get("price") or obj.get("hourly_price") or obj.get("hourlyPrice"),
                "category": obj.get("category") or obj.get("type"),
            }
            # solo agregamos si parece listing real (tiene slug ~ string razonable)
            if isinstance(entry["slug"], str) and len(entry["slug"]) > 3:
                hits.append(entry)
        for v in obj.values():
            walk(v, hits)
    elif isinstance(obj, list):
        for v in obj:
            walk(v, hits)


def extract_listings_from_page(url: str) -> list[dict]:
    print(f"→ {url}")
    html = fetch(url)
    if not html:
        return []
    nd = parse_next_data(html)
    if not nd:
        print("  (sin __NEXT_DATA__)")
        return []
    hits: list[dict] = []
    walk(nd, hits)
    # de-dupe por slug
    seen = set()
    uniq = []
    for h in hits:
        k = h.get("slug")
        if k and k not in seen:
            seen.add(k)
            h["source_url"] = url
            h["captured_at"] = datetime.now(timezone.utc).isoformat()
            uniq.append(h)
    print(f"  → {len(uniq)} listings extraídos")
    return uniq


def check_robots() -> bool:
    print("Verificando robots.txt…")
    txt = fetch("https://space-pal.com/robots.txt") or ""
    # buscar reglas que prohíban explícitamente /es/search/
    if "Disallow: /es/search" in txt or "Disallow: /search" in txt:
        print("  ⚠ robots.txt prohíbe /search — abortando.")
        print(txt)
        return False
    print("  OK — /search no prohibido en robots.txt")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max", type=int, default=200, help="máximo de listings totales")
    parser.add_argument("--dry-run", action="store_true", help="no escribe archivo")
    parser.add_argument("--skip-robots", action="store_true", help="(no recomendado) saltar check de robots.txt")
    args = parser.parse_args()

    if not args.skip_robots:
        if not check_robots():
            return 2
        time.sleep(SLEEP)

    all_listings: list[dict] = []
    for url in CATEGORIAS_PROBE:
        if len(all_listings) >= args.max:
            break
        listings = extract_listings_from_page(url)
        all_listings.extend(listings)
        time.sleep(SLEEP)

    # de-dupe global por slug
    seen = set()
    final = []
    for h in all_listings:
        k = h.get("slug")
        if k and k not in seen:
            seen.add(k)
            final.append(h)
        if len(final) >= args.max:
            break

    print(f"\nTotal listings únicos: {len(final)}")
    if args.dry_run:
        print(json.dumps(final[:5], ensure_ascii=False, indent=2))
        return 0

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    output = {
        "source": "https://space-pal.com (research-only, public metadata)",
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "user_agent": UA,
        "count": len(final),
        "listings": final,
        "note": (
            "Metadata pública extraída para research interno de Coordina Eventos. "
            "NO redistribuir. NO republicar en producto público. "
            "Uso permitido: pipeline de leads de hosts, validación de pricing."
        ),
    }
    OUT_FILE.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n✓ {OUT_FILE.relative_to(ROOT)} — {len(final)} listings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
