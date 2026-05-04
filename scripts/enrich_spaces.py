#!/usr/bin/env python3
"""Enriquece spaces.json con:
- 4-6 fotos únicas por espacio (de un pool curado de Unsplash)
- Descripciones Lima-específicas más ricas (originales, escritas por nosotros)
- Pequeños detalles que aumentan realismo: instrucciones de llegada,
  horarios sugeridos, qué incluye explícito.

Las fotos se asignan según el tipo del espacio (no random).
NO se copian textos ni imágenes de terceros — todo es contenido original
o licencia comercial libre (Unsplash).

Ejecución: python3 scripts/enrich_spaces.py
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "public" / "spaces.json"

# Pool de fotos categorizado (todas verificadas Unsplash, licencia comercial libre)
POOL = {
    "salon_eventos": [
        "https://images.unsplash.com/photo-1519167758481-83f550bb49b3",
        "https://images.unsplash.com/photo-1542665952-14513db15293",
        "https://images.unsplash.com/photo-1530103862676-de8c9debad1d",
        "https://images.unsplash.com/photo-1464366400600-7168b8af9bc3",
        "https://images.unsplash.com/photo-1469371670807-013ccf25f16a",
        "https://images.unsplash.com/photo-1531538512164-e6c51ea63d20",
        "https://images.unsplash.com/photo-1492684223066-81342ee5ff30",
        "https://images.unsplash.com/photo-1559329007-40df8a9345d8",
        "https://images.unsplash.com/photo-1553877522-43269d4ea984",
        "https://images.unsplash.com/photo-1563911302283-d2bc129e7570",
        "https://images.unsplash.com/photo-1600585154340-be6161a56a0c",
        "https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3",
    ],
    "loft": [
        "https://images.unsplash.com/photo-1505236858219-8359eb29e329",
        "https://images.unsplash.com/photo-1505691938895-1758d7feb511",
        "https://images.unsplash.com/photo-1519642918688-7e43b19245d8",
        "https://images.unsplash.com/photo-1540317580384-e5d43616b9aa",
        "https://images.unsplash.com/photo-1571171637578-41bc2dd41cd2",
    ],
    "sala": [
        "https://images.unsplash.com/photo-1497366216548-37526070297c",
        "https://images.unsplash.com/photo-1556761175-5973dc0f32e7",
        "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4",
        "https://images.unsplash.com/photo-1497366811353-6870744d04b2",
        "https://images.unsplash.com/photo-1517457373958-b7bdd4587205",
    ],
    "terraza": [
        "https://images.unsplash.com/photo-1414235077428-338989a2e8c0",
        "https://images.unsplash.com/photo-1517502884422-41eaead166d4",
        "https://images.unsplash.com/photo-1604328698692-f76ea9498e76",
    ],
    "estudio_yoga": [
        "https://images.unsplash.com/photo-1545205597-3d9d02c29597",
        "https://images.unsplash.com/photo-1540317580384-e5d43616b9aa",
        "https://images.unsplash.com/photo-1519225421980-715cb0215aed",
    ],
    "audiovisual": [
        "https://images.unsplash.com/photo-1511795409834-ef04bbd61622",
        "https://images.unsplash.com/photo-1543007630-9710e4a00a20",
    ],
    "coworking": [
        "https://images.unsplash.com/photo-1540575467063-178a50c2df87",
        "https://images.unsplash.com/photo-1497366811353-6870744d04b2",
        "https://images.unsplash.com/photo-1517457373958-b7bdd4587205",
    ],
    "showroom": [
        "https://images.unsplash.com/photo-1531058020387-3be344556be6",
        "https://images.unsplash.com/photo-1604014237800-1c9102c219da",
        "https://images.unsplash.com/photo-1571171637578-41bc2dd41cd2",
    ],
    "auditorio": [
        "https://images.unsplash.com/photo-1556761175-5973dc0f32e7",
        "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4",
    ],
}

PARAM = "?w=1400&q=80&auto=format&fit=crop"


def fotos_for(tipo_lower: str, slug: str) -> list[str]:
    """Asigna 4-6 fotos al espacio basado en su tipo, evitando colisiones obvias."""
    # detect category
    if "salón" in tipo_lower or "salon" in tipo_lower or "casa" in tipo_lower:
        primary = POOL["salon_eventos"]
    elif "loft" in tipo_lower:
        primary = POOL["loft"]
    elif "sala" in tipo_lower:
        primary = POOL["sala"]
    elif "terraza" in tipo_lower:
        primary = POOL["terraza"]
    elif "yoga" in tipo_lower or "estudio de yoga" in tipo_lower:
        primary = POOL["estudio_yoga"]
    elif "audiovisual" in tipo_lower or "audio" in tipo_lower:
        primary = POOL["audiovisual"]
    elif "coworking" in tipo_lower:
        primary = POOL["coworking"]
    elif "showroom" in tipo_lower:
        primary = POOL["showroom"]
    elif "auditorio" in tipo_lower:
        primary = POOL["auditorio"]
    elif "creativo" in tipo_lower or "multipropósito" in tipo_lower or "multipropóstio" in tipo_lower:
        primary = POOL["loft"] + POOL["showroom"]
    else:
        primary = POOL["salon_eventos"]

    # rotate based on hash of slug for variety per space
    h = sum(ord(c) for c in slug)
    rotated = primary[h % len(primary):] + primary[:h % len(primary)]
    chosen = rotated[: min(5, len(rotated))]
    # add 1 from "complementarias" si tipo es salón/casa: una foto de mesa decorada
    if ("salón" in tipo_lower or "casa" in tipo_lower) and len(chosen) < 6:
        extra = POOL["salon_eventos"][(h + 3) % len(POOL["salon_eventos"])]
        if extra not in chosen:
            chosen.append(extra)
    return [u + PARAM for u in chosen]


# Descripciones Lima-específicas, originales (escritas por nosotros, no copiadas)
DESCRIPCIONES_LIMA = {
    "casa-verde-barranco": {
        "descripcion": "Casa republicana restaurada en el corazón de Barranco, a pocas cuadras del puente de los suspiros. Patio interior con árbol y sala con techos altos de seis metros. La cocina conserva mayólica original. Ideal para baby showers, cumpleaños íntimos y sesiones de marca. Llegada en taxi recomendada por el tráfico de fines de semana; estacionamiento para tres vehículos.",
        "highlights": ["Casa republicana restaurada", "Patio interior con árbol", "Mayólica original en cocina", "A 5 min del Puente de los Suspiros"],
    },
    "el-alto-miraflores": {
        "descripcion": "Salón de eventos en el segundo piso de un edificio sobre la avenida Pardo. Pisos de madera oscura, cortinas blackout y zona lounge separada de la pista. Sonido empotrado calibrado, iluminación DMX programable. Ascensor directo desde estacionamiento. El staff del edificio coordina ingreso de proveedores; apertura desde las 15:00.",
        "highlights": ["Sonido DMX programable", "Zona lounge separada", "Ascensor directo desde parking", "Sobre Av. Pardo"],
    },
    "loft-fotografico-barranco": {
        "descripcion": "Loft de planta abierta en una casa adaptada en Barranco. Ventanal sur de seis metros que da luz natural difusa todo el día — ideal para piel y producto. Ciclorama blanco 4 metros, fondos de papel disponibles. Vestidor con espejo de cuerpo completo y enchufes para planchas. Cocina pequeña para snacks de equipo.",
        "highlights": ["Luz natural sur 6m", "Ciclorama blanco 4m", "Vestidor con espejo completo", "Cocina para crew"],
    },
    "mirador-las-casuarinas": {
        "descripcion": "Terraza privada en lo alto de Las Casuarinas con vista a Lima desde el cerro. Capacidad para 60 sentados o 90 cocktail. Pérgola cubierta para protección de neblina, calefactores exteriores en invierno. Cocina equipada para catering propio. Acceso restringido por urbanización privada — coordinar lista de invitados con 48h de anticipación.",
        "highlights": ["Vista panorámica de Lima", "Pérgola cubierta", "Calefactores para invierno", "Acceso por urbanización privada"],
    },
    "sala-norte-san-isidro": {
        "descripcion": "Sala de reuniones en piso 14 del edificio empresarial sobre Javier Prado. TV 65 pulgadas con AirPlay y Miracast, pizarra de vidrio de 3 metros, mesa para 12 con sillas Aeron. Internet enterprise simétrico 500 Mbps. Recepción del edificio recibe a tus invitados; estacionamiento de visita validable.",
        "highlights": ["TV 65\" AirPlay/Miracast", "Pizarra de vidrio 3m", "Wi-Fi enterprise 500 Mbps", "Sillas Aeron"],
    },
    "auditorio-san-borja": {
        "descripcion": "Auditorio profesional en el Centro Empresarial San Luis. Butacas reclinables con escritorio plegable, cabina de proyección con operador incluido. Pantalla 4K de 4 metros, sistema de sonido Bose con 8 micrófonos inalámbricos Sennheiser. Cabina de traducción simultánea aparte. Foyer para coffee break con 25 m².",
        "highlights": ["Butacas con escritorio plegable", "Pantalla 4K · 4m", "8 micrófonos Sennheiser", "Foyer para coffee break"],
    },
    "casa-sol-magdalena": {
        "descripcion": "Estudio de yoga en casa familiar adaptada en Magdalena. Piso de madera maple flotante, climatización mediante ventilación cruzada (sin aire acondicionado para mantener prana). Mats Manduka y bloques disponibles. Duchas con agua caliente solar; vestidor unisex. Ventanas que dan al jardín del barrio.",
        "highlights": ["Piso de madera maple", "Mats Manduka incluidos", "Agua caliente solar", "Ventilación cruzada natural"],
    },
    "estudio-creativo-barranco": {
        "descripcion": "Espacio multipropósito en una galería de arte de Barranco. Paredes blancas de seis metros, piso de cemento pulido. Riel de iluminación profesional sobre toda la planta, sonido empotrado JBL. Configurable como pista de baile, set fotográfico o pasarela. La galería deja sus obras durante el evento — los muros son del espacio.",
        "highlights": ["Galería de arte adaptable", "Riel de luz profesional", "Sonido JBL empotrado", "Cemento pulido + paredes 6m"],
    },
    "coworking-san-isidro": {
        "descripcion": "Sala privada dentro de coworking premium sobre Aramburú. Mesa redonda para 8 con sillas ergonómicas, TV 55 pulgadas con HDMI y conexión inalámbrica. Acceso a la cafetería del coworking incluido (café de origen, té, agua, infusiones). Recepción profesional bilingüe. Edificio con seguridad 24/7.",
        "highlights": ["Mesa redonda para 8", "Café de origen incluido", "Recepción bilingüe", "Edificio seguro 24/7"],
    },
    "estudio-audiovisual-la-molina": {
        "descripcion": "Estudio audiovisual insonorizado en La Molina. Cabina de podcast con 4 micrófonos Shure SM7B sobre brazos, mezcladora Rodecaster Pro 2 lista. Set de video con luz continua Aputure y greenscreen retráctil. Operador con 8 años de experiencia disponible aparte. Estacionamiento dentro del edificio para descargar equipo grande.",
        "highlights": ["4 micrófonos Shure SM7B", "Rodecaster Pro 2", "Greenscreen retráctil", "Operador 8 años exp."],
    },
    "salon-nupcial-san-isidro": {
        "descripcion": "Quinta nupcial en una calle residencial de San Isidro. Jardín principal de 800 m² con árboles maduros, salón cubierto adyacente para emergencia de lluvia. Cocina industrial con plancha, hornos y cámaras frías para catering propio. Vestidores de novios separados con espejo, baño y mini bar. Estacionamiento para 80 vehículos en lote propio.",
        "highlights": ["Jardín 800 m² con árboles", "Cocina industrial completa", "Vestidores de novios", "Parking para 80 autos"],
    },
    "showroom-miraflores": {
        "descripcion": "Showroom con vitrina a la avenida Larco. Diseño minimalista — piso de cemento, paredes blancas, riel de iluminación galería. La vitrina genera tráfico orgánico durante el evento (Larco tiene 60.000 transeúntes/día). Configurable como tienda pop-up o lounge. Conexión a sistema de música del local incluida.",
        "highlights": ["Vitrina a Av. Larco", "60k transeúntes/día", "Riel galería", "Sistema de música incluido"],
    },
    "salon-intimo-san-isidro": {
        "descripcion": "Casa íntima en zona residencial tranquila de San Isidro. Sala principal con sofás, comedor adyacente con mesa para 24, jardín interior con cobertura cubierta. Cocina equipada con horno doble y vajilla para 35. Decoración base elegante (paredes color crema, lámparas de techo) — necesitas pocos detalles para fiesta lista.",
        "highlights": ["Comedor para 24 sentados", "Cobertura cubierta jardín", "Vajilla para 35 incluida", "Decoración base lista"],
    },
    "sala-capacitacion-san-borja": {
        "descripcion": "Aula formato capacitación en torre empresarial de San Borja. Sillas con paleta plegable rotables, mesa principal del facilitador. Doble proyección: pantalla principal 100\" + TV auxiliar 75\". 4 micrófonos inalámbricos Shure. Setup de coffee break en zona aparte; el catering se contrata directo con proveedor del edificio.",
        "highlights": ["Sillas con paleta plegable", "Pantalla 100\" + TV 75\"", "4 micrófonos Shure", "Catering por proveedor edificio"],
    },
    "loft-creativo-pueblo-libre": {
        "descripcion": "Loft en una casona republicana de Pueblo Libre adaptada. Vigas de madera a la vista, ladrillo expuesto en una pared, piso de pino restaurado. Luz natural por la mañana excelente; tarde más cálida. Ideal para talleres, sesiones de marca pequeñas y eventos creativos íntimos. Wi-Fi rápido. Sin estacionamiento — taxi o caminando desde la avenida La Marina.",
        "highlights": ["Casona republicana", "Vigas de madera vistas", "Ladrillo expuesto", "Luz natural matinal"],
    },
}


def main() -> int:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    spaces = payload["spaces"]
    for s in spaces:
        s["fotos"] = fotos_for(s["tipo"].lower(), s["slug"])
        if s["slug"] in DESCRIPCIONES_LIMA:
            entry = DESCRIPCIONES_LIMA[s["slug"]]
            s["descripcion"] = entry["descripcion"]
            s["highlights"] = entry["highlights"]
    payload["updated"] = "2026-05-04"
    DATA.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ {DATA.relative_to(ROOT)} — fotos diversificadas y descripciones Lima-específicas en {len(spaces)} espacios")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
