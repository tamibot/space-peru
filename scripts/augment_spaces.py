#!/usr/bin/env python3
"""Expande spaces.json con reseñas, coordenadas, host_phone y bloque mínimo.

Usa los IDs y datos existentes y agrega:
- lat, lng (aprox por distrito Lima)
- host_phone (placeholder)
- bloque_minimo_horas (según tipo)
- reseñas[] (3 sintéticas plausibles cada uno)

Ejecución: python3 scripts/augment_spaces.py
Sobreescribe data/public/spaces.json.
"""
from __future__ import annotations

import json
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(42)

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "public" / "spaces.json"

DISTRITO_COORDS = {
    "Miraflores":          (-12.1213, -77.0297),
    "San Isidro":          (-12.0978, -77.0365),
    "Barranco":            (-12.1465, -77.0220),
    "Surco":               (-12.1449, -76.9947),
    "San Borja":           (-12.1080, -76.9985),
    "La Molina":           (-12.0867, -76.9511),
    "Magdalena del Mar":   (-12.0907, -77.0717),
    "Pueblo Libre":        (-12.0762, -77.0631),
}

NAMES = [
    "Andrea M.", "Rodrigo V.", "Camila S.", "Diego R.", "Valeria T.",
    "Sebastián L.", "Lucía P.", "Mariana C.", "José Luis A.", "Patricia G.",
    "Luis Fernando R.", "Adriana B.", "Renato M.", "Claudia H.", "Alejandro V.",
    "Daniela O.", "Joaquín N.", "Carolina G.", "Andrés P.", "Pamela R.",
    "Sergio E.", "Brenda M.", "Eduardo L.", "Sofía A.", "Manuel D.",
    "Gianella P.", "Gonzalo F.", "Vanessa C.", "Iván R.", "Stephanie K.",
]

# Comentarios por tipo de espacio (key = palabra del tipo, value = lista comments)
COMMENTS_BY_KIND = {
    "salón": [
        "El espacio es perfecto. Las fotos no le hacen justicia, en persona se ve aún mejor.",
        "Hicimos el cumpleaños de mi hija acá y todos los invitados quedaron encantados. Limpio y bien iluminado.",
        "El encargado respondió rapidísimo por WhatsApp. Coordinamos la visita el mismo día.",
        "Excelente ubicación. Estacionamiento amplio. Recomendado para eventos medianos.",
        "El precio es justo para todo lo que incluye. Sonido y luces ya armados, eso ahorra mucho.",
    ],
    "loft": [
        "El loft tiene una luz natural increíble. Hicimos sesión de producto y las fotos quedaron espectaculares.",
        "Espacio amplio y bien decorado. El ciclorama es de buena calidad.",
        "La dueña fue súper atenta. Nos dejó todo el equipo de luz disponible sin costo extra.",
        "Para sesiones creativas, perfecto. Buena ventilación, vestidor cómodo.",
    ],
    "terraza": [
        "Vista impresionante al atardecer. Hicimos el aniversario y fue una experiencia inolvidable.",
        "Buen espacio para cocktail. La cocina equipada es un plus importante.",
        "El anfitrión muy amable, nos dio recomendaciones de catering local.",
        "Muy recomendado para eventos al aire libre. Cuidado con el viento en algunas tardes.",
    ],
    "sala": [
        "Sala muy profesional. La pizarra magnética y el TV grande funcionaron sin problemas.",
        "Wi-Fi rápido y silencio absoluto. Ideal para reuniones serias.",
        "Edificio con seguridad y estacionamiento. Llegaron todos los participantes a tiempo.",
        "Buena relación calidad-precio para reuniones de hasta 12 personas.",
    ],
    "auditorio": [
        "Todo el equipo audiovisual funcionó perfecto. Los micrófonos inalámbricos sin fallas.",
        "Capacidad real para 120 personas, todos cómodos. Acústica muy buena.",
        "El operador del sistema fue clave, ayudó con la presentación todo el rato.",
        "Recomendable para conferencias serias. Accesible para personas con movilidad reducida.",
    ],
    "estudio": [
        "Excelente para clases de yoga. El piso de madera es perfecto y los mats están en buen estado.",
        "Espacio limpio, con duchas funcionales. Los talleres salen redondos.",
        "Luz natural espectacular en la mañana. Recomendado para sesiones tempranas.",
        "Equipo de sonido suficiente para clases dinámicas. Sin eco molesto.",
    ],
    "showroom": [
        "Vitrina a la calle generó tráfico extra durante el lanzamiento. Súper recomendado.",
        "Diseño minimalista. Quedó perfecto para nuestra marca.",
        "El equipo nos ayudó a montar el escaparate. Buena atención.",
    ],
    "casa": [
        "Casa hermosa y muy bien cuidada. Hicimos el baby shower y fue inolvidable.",
        "El jardín interior es un lujo. Los invitados no querían irse.",
        "La cocina equipada nos ahorró contratar catering completo.",
        "Decoración elegante por defecto. Apenas necesitamos agregar detalles.",
    ],
    "coworking": [
        "Wi-Fi enterprise, café incluido y recepción profesional. La sala se ve mejor que en las fotos.",
        "Reunión de trabajo perfecta. El ambiente del coworking suma seriedad.",
        "Por hora es muy razonable. Lo usamos varias veces ya.",
    ],
    "audiovisual": [
        "Cabina insonorizada de verdad. Grabamos el podcast sin un solo ruido externo.",
        "El operador conoce el equipo perfecto. Ahorra horas de set-up.",
        "Calidad profesional a precio razonable. Repetiremos.",
    ],
}


def comments_for(tipo: str) -> list[str]:
    t = tipo.lower()
    for key, lst in COMMENTS_BY_KIND.items():
        if key in t:
            return lst
    return COMMENTS_BY_KIND["salón"]


def gen_reviews(tipo: str, total: int) -> list[dict]:
    pool = comments_for(tipo)
    used_names = random.sample(NAMES, total)
    reviews = []
    for i in range(total):
        days_ago = random.randint(7, 240)
        d = date.today() - timedelta(days=days_ago)
        rating = random.choices([4, 5], weights=[1, 4])[0]
        comment = random.choice(pool)
        reviews.append({
            "name": used_names[i],
            "rating": rating,
            "date": d.isoformat(),
            "comment": comment,
        })
    # most recent first
    reviews.sort(key=lambda r: r["date"], reverse=True)
    return reviews


def block_min_for(tipo: str, casos: list[str]) -> int:
    t = tipo.lower()
    if "auditorio" in t or "salón" in t or "salon" in t or "casa" in t:
        return 4
    if "estudio" in t or "loft" in t:
        return 2
    if "coworking" in t or "sala" in t:
        return 1
    return 2


def host_phone() -> str:
    return f"+51 9{random.randint(10, 99)} {random.randint(100, 999)} {random.randint(100, 999)}"


def jitter(coord: tuple[float, float]) -> tuple[float, float]:
    """Small jitter para que no todos los espacios del mismo distrito caigan en el mismo punto."""
    lat, lng = coord
    return (
        round(lat + random.uniform(-0.008, 0.008), 6),
        round(lng + random.uniform(-0.008, 0.008), 6),
    )


def main() -> int:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    spaces = payload["spaces"]
    for s in spaces:
        coord = DISTRITO_COORDS.get(s["distrito"], (-12.0464, -77.0428))  # default Lima centro
        lat, lng = jitter(coord)
        s["lat"] = lat
        s["lng"] = lng
        s["host_phone"] = host_phone()
        s["bloque_minimo_horas"] = block_min_for(s["tipo"], s.get("casos_uso", []))
        s["reseñas"] = gen_reviews(s["tipo"], 3)
    payload["updated"] = "2026-05-02"
    payload["note"] = (
        "Dataset de demostración — 15 espacios reales referenciados con datos plausibles "
        "construidos a partir del research de mercado. Coordenadas, reseñas, teléfonos y "
        "bloques mínimos son sintéticos. Imágenes vía Unsplash (licencia comercial libre). "
        "Cuando se publiquen hosts reales, este dataset se reemplaza con sus datos verificados."
    )
    DATA.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ {DATA.relative_to(ROOT)} — {len(spaces)} espacios augmentados con coords, host_phone, bloque_min, 3 reseñas c/u")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
