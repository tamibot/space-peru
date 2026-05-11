#!/usr/bin/env python3
"""Genera páginas básicas de la app: cómo funciona, concierge, publicar, verificate,
ayuda, sobre, contacto, host, y legales (términos, privacidad, cookies, libro reclamaciones).

Todas siguen el branding canónico (Plus Jakarta Sans 800, radius 0, monocromo,
--verified azul solo para badge verificación).

Comparten el mismo template base (nav fixed + footer 4-col + FAB IA).

Output: app/web/*.html
"""
from __future__ import annotations
import json
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APP_DIR = ROOT / "app" / "web"
DATA = ROOT / "data" / "public" / "spaces.json"


def render_nav(active: str = "", depth: int = 0) -> str:
    """Renderiza el nav unificado.
    depth: cuántos niveles de subcarpeta. 0 = en /app/, 1 = /app/legal/, etc.
    """
    base = "./" if depth == 0 else "../" * depth
    landing = base + "../" if depth == 0 else "../" * (depth + 1)

    def cls(name: str) -> str:
        return ' class="active"' if active == name else ""

    return f"""<header class="nav" id="nav">
  <div class="nav-inner">
    <a class="brand" href="{landing}" data-spa-link>coordina<span class="brand-suffix">eventos</span></a>
    <nav class="nav-links">
      <a href="{base}buscar.html"{cls("espacios")} data-spa-link>Espacios</a>
      <a href="{base}concierge.html"{cls("concierge")} data-spa-link>Organización de eventos</a>
      <a href="{base}como-funciona.html"{cls("como-funciona")} data-spa-link>Cómo funciona</a>
      <a href="{base}publicar.html"{cls("publicar")} data-spa-link>Para hosts</a>
      <a href="{base}ayuda.html"{cls("ayuda")} data-spa-link>Ayuda</a>
      <a href="{landing}" class="nav-back" data-spa-link>← Inicio</a>
    </nav>
  </div>
</header>"""


def render_footer(depth: int = 0) -> str:
    base = "./" if depth == 0 else "../" * depth
    landing = base + "../" if depth == 0 else "../" * (depth + 1)
    legal = base + "legal/" if depth == 0 else "../" * depth + "legal/"

    return f"""<footer class="footer-app">
  <div class="container">
    <div class="footer-app-grid">
      <div class="footer-app-brand">
        <a class="brand" href="{landing}" data-spa-link>coordina<span class="brand-suffix">eventos</span></a>
        <p>Espacios por horas en Lima. Coordinas la visita por WhatsApp. Si no tienes tiempo, lo armamos contigo.</p>
        <span class="footer-app-domain">coordinaeventos.com</span>
      </div>
      <div class="footer-app-col">
        <h4>Explorar</h4>
        <a href="{base}buscar.html" data-spa-link>Espacios</a>
        <a href="{base}concierge.html" data-spa-link>Organización de eventos</a>
        <a href="{base}como-funciona.html" data-spa-link>Cómo funciona</a>
        <a href="{base}ayuda.html" data-spa-link>Centro de ayuda</a>
      </div>
      <div class="footer-app-col">
        <h4>Hosts</h4>
        <a href="{base}publicar.html" data-spa-link>Publicar mi espacio</a>
        <a href="{base}verificate.html" data-spa-link>Verificación</a>
        <a href="{base}publicar.html#cobros" data-spa-link>Cómo cobras</a>
        <a href="{base}publicar.html#empresas" data-spa-link>Para empresas</a>
      </div>
      <div class="footer-app-col">
        <h4>coordinaeventos</h4>
        <a href="{base}sobre.html" data-spa-link>Sobre nosotros</a>
        <a href="{base}contacto.html" data-spa-link>Contacto</a>
        <a href="mailto:mvelascoo@tamibot.com">mvelascoo@tamibot.com</a>
      </div>
      <div class="footer-app-col">
        <h4>Legal</h4>
        <a href="{legal}terminos.html" data-spa-link>Términos y condiciones</a>
        <a href="{legal}privacidad.html" data-spa-link>Política de privacidad</a>
        <a href="{legal}cookies.html" data-spa-link>Política de cookies</a>
        <a href="{legal}libro-reclamaciones.html" data-spa-link>Libro de reclamaciones</a>
      </div>
    </div>
    <div class="footer-app-bottom">
      <span>© 2026 coordinaeventos · Lima, Perú</span>
      <span>Imágenes de referencia: <a href="https://unsplash.com/" target="_blank" rel="noopener">Unsplash</a></span>
    </div>
  </div>
</footer>"""


def render_demo_banner(depth: int = 0) -> str:
    landing = "../" if depth == 0 else "../" * (depth + 1)
    return f"""<div class="demo-banner">
  <strong>Catálogo demo</strong> · Los primeros hosts reales se publican en junio 2026 ·
  <a href="{landing}#hosts">¿Tienes un espacio? Publica gratis →</a>
</div>"""


def render_fab() -> str:
    return """<button class="ai-fab" id="ai-fab" aria-label="Abrir asistente IA">
  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.2" aria-hidden="true">
    <path d="M12 2 C6.5 2 2 6.5 2 12 C2 14 2.5 15.8 3.4 17.4 L2 22 L6.6 20.6 C8.2 21.5 10 22 12 22 C17.5 22 22 17.5 22 12 C22 6.5 17.5 2 12 2 Z"/>
    <circle cx="8" cy="12" r="1" fill="white"/>
    <circle cx="12" cy="12" r="1" fill="white"/>
    <circle cx="16" cy="12" r="1" fill="white"/>
  </svg>
  <span class="ai-fab-label">Asistente IA</span>
</button>"""


def render_page(slug: str, title: str, meta_desc: str, body: str, active: str = "", page_data: str = "page", depth: int = 0) -> str:
    css_path = "../" * depth + "styles.css?v=2026-05-11-2"
    js_path = "../" * depth + "app.js?v=2026-05-11-2"
    favicon = "../" * (depth + 2) + "brand/logo/favicon.svg"

    return f"""<!doctype html>
<html lang="es-PE">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>{title} — coordinaeventos</title>
  <meta name="description" content="{meta_desc}" />
  <meta name="theme-color" content="#0A0A0A" />
  <link rel="icon" href="{favicon}" type="image/svg+xml" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="{css_path}" />
</head>
<body data-page="{page_data}">

{render_demo_banner(depth)}

{render_nav(active, depth)}

<main class="page-main">
  <div class="container">
{body}
  </div>
</main>

{render_fab()}

{render_footer(depth)}

<script src="{js_path}"></script>
</body>
</html>
"""


# ───────────────────────────────────────────────────────────────
# Contenido de cada página
# ───────────────────────────────────────────────────────────────

PAGES = {}

PAGES["como-funciona"] = {
    "title": "Cómo funciona",
    "meta_desc": "El proceso de coordinaeventos paso a paso. Cómo buscar, contactar al host, visitar, reservar, y cómo nos diferencia nuestro sistema de verificación.",
    "active": "como-funciona",
    "body": """
    <header class="page-header">
      <span class="eyebrow">Cómo funciona</span>
      <h1>De la búsqueda a la visita,<br>en una tarde.</h1>
      <p class="page-lead">Te contamos paso a paso cómo encontrar y reservar un espacio en coordinaeventos.</p>
    </header>

    <section class="content-section">
      <h2>Para quienes buscan un espacio</h2>
      <ol class="step-list">
        <li>
          <span class="step-num">01</span>
          <div>
            <strong>Filtra el catálogo</strong>
            <p>Usa el buscador o navega por categorías. Filtra por tipo de evento, distrito, capacidad y facilidades. Cada espacio tiene fotos reales, capacidad declarada y precio desde.</p>
          </div>
        </li>
        <li>
          <span class="step-num">02</span>
          <div>
            <strong>Elige uno y contacta al host</strong>
            <p>Cuando un espacio te interesa, abrís el detalle y haces click en "Contactar por WhatsApp". Te conectamos con el encargado del local en su chat habitual — sin formularios largos.</p>
          </div>
        </li>
        <li>
          <span class="step-num">03</span>
          <div>
            <strong>Coordina la visita</strong>
            <p>Coordinas día y hora con el host directamente. La visita es presencial o por videollamada según prefieras. La dirección exacta se comparte después del primer contacto.</p>
          </div>
        </li>
        <li>
          <span class="step-num">04</span>
          <div>
            <strong>Reserva y paga</strong>
            <p>Después de la visita, si el espacio te convence, acuerdan precio final y forma de pago. Yape, Plin, transferencia, efectivo — como prefieras. Sin pago anticipado en la plataforma.</p>
          </div>
        </li>
      </ol>
    </section>

    <section class="content-section content-section-soft">
      <h2>Sistema de verificación</h2>
      <p>Los espacios marcados con el <strong style="color:#1D9BF0;">badge azul ✓</strong> han pasado por una verificación humana. Esto significa que:</p>
      <ul class="check-list">
        <li>El host envió un video del local recorriendo ambientes, accesos y capacidad real.</li>
        <li>Nuestro equipo validó que el video coincide con lo publicado.</li>
        <li>La capacidad declarada es revisada (no solo asumida).</li>
        <li>Las amenidades listadas se ven en el video.</li>
      </ul>
      <p>Es opcional para los hosts pero da una garantía extra a quien va a alquilar. Lo que ves en la foto es lo que vas a encontrar.</p>
      <a href="./verificate.html" class="btn btn-outline" data-spa-link>Cómo verifico mi espacio →</a>
    </section>

    <section class="content-section">
      <h2>Pagos</h2>
      <p>Por ahora, los pagos se coordinan directamente entre tú y el host. Las opciones más comunes:</p>
      <div class="payment-grid">
        <div class="payment-card"><strong>Yape</strong><span>Pago instantáneo desde el celular</span></div>
        <div class="payment-card"><strong>Plin</strong><span>Igual de rápido, banca digital</span></div>
        <div class="payment-card"><strong>Transferencia</strong><span>BCP, Interbank, BBVA, Scotiabank</span></div>
        <div class="payment-card"><strong>Efectivo</strong><span>Si el host lo acepta</span></div>
      </div>
      <p class="content-note">Más adelante integraremos pago en plataforma con factura SUNAT, sin obligar a nadie a usarlo.</p>
    </section>

    <section class="content-section content-section-dark">
      <h2>¿Sin tiempo para coordinar todo?</h2>
      <p>Si organizar el evento te toma más horas de las que tienes, nuestro servicio de <strong>Organización de eventos</strong> se encarga: te buscamos el local correcto, coordinamos permisos y fechas, hablamos con los proveedores que necesites. Una sola conversación de WhatsApp.</p>
      <a href="./concierge.html" class="btn btn-light" data-spa-link>Conocer el servicio</a>
    </section>
    """
}

PAGES["concierge"] = {
    "title": "Organización de eventos",
    "meta_desc": "Servicio de organización completa: buscamos el local, coordinamos permisos y fechas, hablamos con los proveedores. Una sola conversación de WhatsApp.",
    "active": "concierge",
    "body": """
    <header class="page-header">
      <span class="eyebrow">Servicio de organización</span>
      <h1>Tú nos cuentas el evento.<br>Nosotros nos encargamos del resto.</h1>
      <p class="page-lead">Buscar el local correcto, hablar con varios hosts, coordinar permisos y fechas, conseguir proveedores — eso toma horas que no tienes. Nuestro equipo lo hace por ti, en una sola conversación.</p>
    </header>

    <section class="content-section">
      <h2>Qué hacemos por ti</h2>
      <ol class="step-list">
        <li>
          <span class="step-num">01</span>
          <div>
            <strong>Buscamos el local ideal para tu evento</strong>
            <p>Nos cuentas qué necesitas — tipo de evento, fecha, cuánta gente, distrito, presupuesto. Filtramos el catálogo y te traemos las opciones que realmente encajan en menos de dos horas.</p>
          </div>
        </li>
        <li>
          <span class="step-num">02</span>
          <div>
            <strong>Coordinamos permisos, fechas y reservas</strong>
            <p>Nos comunicamos con el host para fijar día y hora, revisar las condiciones del local y gestionar los permisos que apliquen. Tú no tienes que perseguir a nadie por WhatsApp.</p>
          </div>
        </li>
        <li>
          <span class="step-num">03</span>
          <div>
            <strong>Hablamos con los proveedores que necesites</strong>
            <p>Si tu evento requiere proveedores externos, los contactamos por ti y consolidamos la información. Una propuesta clara, en una sola conversación.</p>
          </div>
        </li>
      </ol>
    </section>

    <section class="content-section content-section-soft">
      <h2>Cuándo conviene pedírnoslo</h2>
      <div class="reasons-grid">
        <div class="reason">
          <strong>No tienes tiempo</strong>
          <p>Tu evento es la próxima semana y no quieres pasar horas en Instagram buscando opciones.</p>
        </div>
        <div class="reason">
          <strong>Es tu primera vez</strong>
          <p>Nunca organizaste algo así. Te guiamos en qué tipo de espacio buscar y qué preguntar al host.</p>
        </div>
        <div class="reason">
          <strong>Es corporativo</strong>
          <p>Necesitas formalidad: cotización clara, factura, comunicación profesional. Nos encargamos.</p>
        </div>
        <div class="reason">
          <strong>Quieres comparar opciones</strong>
          <p>Te conseguimos 3 espacios serios que encajan en tu presupuesto, no 30 al azar.</p>
        </div>
      </div>
    </section>

    <section class="content-section content-section-dark">
      <h2>Contacta con nuestro equipo</h2>
      <p>Respondemos en menos de dos horas por WhatsApp. La primera consulta es gratis y sin compromiso.</p>
      <a href="mailto:mvelascoo@tamibot.com?subject=Quiero contactar al concierge" class="btn btn-light">Escribir al equipo</a>
    </section>
    """
}

PAGES["publicar"] = {
    "title": "Publica tu espacio",
    "meta_desc": "Lista tu espacio en coordinaeventos. Cero comisión, sin contratos, sin exclusividad. Cobras directo. Asistente IA para ayudarte a publicar en cinco minutos.",
    "active": "publicar",
    "body": """
    <header class="page-header">
      <span class="eyebrow">Para hosts</span>
      <h1>¿Tienes un espacio?<br>Lístalo gratis.</h1>
      <p class="page-lead">Cero comisión. Cero contratos. Cero exclusividad. Te lleva cinco minutos publicarlo y los leads te llegan filtrados por WhatsApp.</p>
    </header>

    <section class="content-section">
      <h2>Cómo es publicar</h2>
      <ol class="step-list">
        <li>
          <span class="step-num">01</span>
          <div>
            <strong>El asistente te guía paso a paso</strong>
            <p>Nuestro asistente con IA te hace cinco preguntas básicas: cómo se llama tu espacio, qué tipo es, dónde queda, qué amenidades tiene, qué tipo de eventos aceptas. La descripción la genera contigo en base a tus inputs.</p>
          </div>
        </li>
        <li>
          <span class="step-num">02</span>
          <div>
            <strong>Sube tus fotos</strong>
            <p>Arrastra y suelta las fotos del espacio. La IA evalúa la calidad y sugiere las 5-8 mejores. Si necesitas guía sobre qué fotos tomar, te damos checklist.</p>
          </div>
        </li>
        <li>
          <span class="step-num">03</span>
          <div>
            <strong>Tarifario y extras</strong>
            <p>Defines tu precio por hora y mínimo de horas. Agregas extras que ofreces (proyector, sonido, decoración, mobiliario) con precio individual. Editas cuando quieras.</p>
          </div>
        </li>
        <li>
          <span class="step-num">04</span>
          <div>
            <strong>Publicas y recibes leads</strong>
            <p>Tu espacio queda en el catálogo. Cuando alguien te contacta por WhatsApp, ya viene con la info básica del evento. Coordinas la visita y cierras la reserva.</p>
          </div>
        </li>
      </ol>

      <div class="cta-row">
        <a href="mailto:mvelascoo@tamibot.com?subject=Quiero publicar mi espacio" class="btn btn-primary">Publicar mi espacio</a>
        <a href="./como-funciona.html" class="btn btn-outline" data-spa-link>Conocer el proceso</a>
      </div>
    </section>

    <section class="content-section content-section-soft" id="cobros">
      <h2>Cómo cobras</h2>
      <p>Tú cobras directo al cliente, sin que pase por nuestra plataforma. Esto significa:</p>
      <ul class="check-list">
        <li><strong>Cero comisión.</strong> El precio que negocias con el cliente es lo que recibes.</li>
        <li><strong>Yape, Plin, transferencia, efectivo.</strong> Como prefieras.</li>
        <li><strong>Sin tiempos de retención.</strong> No esperas que nosotros te transfiramos nada.</li>
        <li><strong>Factura tú.</strong> Si el cliente la necesita, emites desde tu RUC o tu CCI personal.</li>
      </ul>
      <p>Ganamos como agencia cuando alguien quiere que armemos el evento completo, no por publicar tu local.</p>
    </section>

    <section class="content-section">
      <h2>Verificación de tu espacio</h2>
      <p>Después de publicar, puedes verificarte. Es opcional pero recomendado: los espacios verificados aparecen marcados con el <strong style="color:#1D9BF0;">badge azul ✓</strong> y se posicionan mejor en el catálogo.</p>
      <a href="./verificate.html" class="btn btn-outline" data-spa-link>Conocer el proceso de verificación →</a>
    </section>

    <section class="content-section content-section-soft" id="empresas">
      <h2>Para empresas con múltiples espacios</h2>
      <p>Si tienes hotel, cadena de oficinas, coworking con varios locales o cualquier operación con más de un espacio: te ayudamos a configurar tu perfil de host con todos tus ambientes y gestionar leads de forma centralizada.</p>
      <a href="mailto:mvelascoo@tamibot.com?subject=Soy empresa con múltiples espacios" class="btn btn-primary">Hablar con el equipo</a>
    </section>
    """
}

PAGES["verificate"] = {
    "title": "Verificación de espacio",
    "meta_desc": "Obtén el badge azul de verificación. Envíanos un video corto del local y validamos que coincide con tu publicación. Genera confianza y mejora tu posicionamiento.",
    "active": "verificate",
    "body": """
    <header class="page-header">
      <span class="eyebrow">
        <svg width="14" height="14" viewBox="0 0 24 24" style="vertical-align:-2px;margin-right:4px;">
          <circle cx="12" cy="12" r="11" fill="#1D9BF0"/>
          <path d="M7 12.5 L10.5 16 L17 9" stroke="white" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        Verificación
      </span>
      <h1>Destaca con el badge azul<br>de verificación.</h1>
      <p class="page-lead">Envíanos un video corto de tu local y validamos que coincide con la publicación. Es la forma más rápida de generar confianza con quien va a alquilar.</p>
    </header>

    <section class="content-section">
      <h2>Por qué verificarte</h2>
      <div class="reasons-grid">
        <div class="reason">
          <strong>Más exposición en el catálogo</strong>
          <p>Los verificados aparecen primero cuando alguien filtra por "Verificados" — más del 60% de clientes lo activan.</p>
        </div>
        <div class="reason">
          <strong>Más confianza para el cliente</strong>
          <p>Saber que lo que ven en la foto es lo que van a encontrar reduce mucha fricción en el contacto.</p>
        </div>
        <div class="reason">
          <strong>Mejor conversión a reserva</strong>
          <p>Los hosts verificados reportan que el cliente acepta visitar más rápido y reserva con menos preguntas.</p>
        </div>
        <div class="reason">
          <strong>Es gratis y rápido</strong>
          <p>No cuesta nada y lo procesamos en menos de 24 horas.</p>
        </div>
      </div>
    </section>

    <section class="content-section content-section-soft">
      <h2>Cómo te verificas</h2>
      <ol class="step-list">
        <li>
          <span class="step-num">01</span>
          <div>
            <strong>Graba un video corto (1-3 minutos)</strong>
            <p>Recorre el local con el celular en horizontal. Muestra los ambientes principales, accesos, capacidad real, y las amenidades que aparecen en tu publicación.</p>
          </div>
        </li>
        <li>
          <span class="step-num">02</span>
          <div>
            <strong>Envíalo por WhatsApp o subes el archivo</strong>
            <p>Cualquier resolución funciona. No necesitas edición, transiciones, ni música. Lo importante es que se vea el espacio real.</p>
          </div>
        </li>
        <li>
          <span class="step-num">03</span>
          <div>
            <strong>Nuestro equipo lo valida</strong>
            <p>Confirmamos que el video coincide con la publicación. Si algo no encaja, te pedimos aclaración (no rechazamos sin avisar).</p>
          </div>
        </li>
        <li>
          <span class="step-num">04</span>
          <div>
            <strong>Recibes el badge azul</strong>
            <p>En menos de 24 horas tu espacio aparece marcado en el catálogo. Te enviamos confirmación por WhatsApp.</p>
          </div>
        </li>
      </ol>
    </section>

    <section class="content-section">
      <h2>Qué mostrar en el video</h2>
      <ul class="check-list">
        <li>Entrada del local + acceso (escalera, ascensor, rampa)</li>
        <li>Cada ambiente principal con plano general</li>
        <li>Capacidad real — toma la sala vacía para que se vea el m²</li>
        <li>Amenidades que aparecen en tu publicación (cocina, baños, sonido, etc.)</li>
        <li>Vista del exterior si aplica (terraza, jardín, estacionamiento)</li>
      </ul>

      <div class="cta-row">
        <a href="mailto:mvelascoo@tamibot.com?subject=Quiero verificar mi espacio" class="btn btn-primary">Empezar verificación</a>
      </div>
    </section>
    """
}

PAGES["ayuda"] = {
    "title": "Centro de ayuda",
    "meta_desc": "Preguntas frecuentes sobre coordinaeventos. Respuestas para clientes, hosts y todo lo relacionado a publicación, búsqueda, verificación y pagos.",
    "active": "ayuda",
    "body": """
    <header class="page-header">
      <span class="eyebrow">Centro de ayuda</span>
      <h1>Lo que más nos preguntan.</h1>
      <p class="page-lead">Si tu pregunta no está aquí, escribe a <a href="mailto:mvelascoo@tamibot.com" style="color:var(--primary);font-weight:700;">mvelascoo@tamibot.com</a> y te respondemos.</p>
    </header>

    <section class="content-section">
      <h2>Para clientes</h2>
      <div class="faq-page">
        <details>
          <summary>¿Cómo busco un espacio?</summary>
          <p>Abre el <a href="./buscar.html" data-spa-link>catálogo</a> y usa los filtros: tipo de evento, distrito, capacidad y características. También puedes pasar el cursor por el listado del Inicio para ver lo más popular por categoría.</p>
        </details>
        <details>
          <summary>¿Cómo contacto al host?</summary>
          <p>En el detalle de cualquier espacio, haz click en "Contactar por WhatsApp". Te conectamos con el encargado del local en su chat habitual. La conversación es directa, sin formularios.</p>
        </details>
        <details>
          <summary>¿Qué significa que un espacio sea "verificado"?</summary>
          <p>Los espacios con el badge azul ✓ pasaron por verificación humana: el host envió un video del local y nuestro equipo validó que coincide con la publicación. Es opcional para los hosts.</p>
        </details>
        <details>
          <summary>¿Cuándo pago el espacio?</summary>
          <p>Después de coordinar con el host y aceptar precio final. Yape, Plin, transferencia o efectivo — el host te dice qué acepta. No hay pago anticipado en la plataforma.</p>
        </details>
        <details>
          <summary>¿Qué incluye el servicio de Organización de eventos?</summary>
          <p>Te buscamos el local ideal, coordinamos visita y reservas, hablamos con los proveedores que necesites. Nosotros gestionamos la coordinación; tú llegas al evento sin haber perseguido a nadie. Conoce más en <a href="./concierge.html" data-spa-link>Organización de eventos</a>.</p>
        </details>
      </div>
    </section>

    <section class="content-section content-section-soft">
      <h2>Para hosts</h2>
      <div class="faq-page">
        <details>
          <summary>¿Cobran comisión a los hosts?</summary>
          <p>No. Listar es gratis para siempre. Cero comisión por reserva. Cero comisión por listing. Ganamos como agencia cuando alguien quiere que organicemos el evento completo, eso es opcional y separado.</p>
        </details>
        <details>
          <summary>¿Cómo me verifico como host?</summary>
          <p>Después de publicar, envías un video corto (1-3 min) recorriendo tu local. Validamos que coincide con la publicación y agregamos el badge azul. Toma menos de 24 horas y es gratis. Más detalle en <a href="./verificate.html" data-spa-link>Verificación</a>.</p>
        </details>
        <details>
          <summary>¿Cómo cobro de las reservas?</summary>
          <p>Directamente al cliente, sin pasar por la plataforma. Yape, Plin, transferencia o efectivo — como prefieras. Si necesitas factura, la emites tú desde tu RUC o CCI.</p>
        </details>
        <details>
          <summary>¿Necesito firmar un contrato con coordinaeventos?</summary>
          <p>No. Sin contratos, sin exclusividad, sin permanencia. Si quieres pausar tu listing, lo pausas. Si quieres bajarlo, lo bajas. Te respondemos por WhatsApp.</p>
        </details>
        <details>
          <summary>¿Cómo configuro tarifario y extras?</summary>
          <p>En el wizard de publicación defines tu precio base por hora y los extras opcionales (proyector, sonido, decoración, mobiliario adicional) con su precio individual. Lo editas cuando quieras.</p>
        </details>
      </div>
    </section>

    <section class="content-section">
      <h2>Sobre la plataforma</h2>
      <div class="faq-page">
        <details>
          <summary>¿Cuándo lanzan?</summary>
          <p>El catálogo actual es demo. Lanzamos oficialmente en junio 2026 con los primeros 50 espacios verificados en Lima Moderna. Si te registras hoy, te avisamos cuando abramos.</p>
        </details>
        <details>
          <summary>¿Solo Lima?</summary>
          <p>Sí, empezamos por Lima Moderna (Miraflores, San Isidro, Barranco, Surco, San Borja, La Molina, Magdalena, Pueblo Libre). Otras ciudades cuando Lima esté maduro.</p>
        </details>
        <details>
          <summary>¿Van a sumar otros proveedores además de espacios?</summary>
          <p>Sí, la visión a 12-24 meses es ser el ecosistema completo: catering, decoración, DJs, fotógrafos, mozos. Por ahora solo espacios.</p>
        </details>
      </div>
    </section>
    """
}

PAGES["sobre"] = {
    "title": "Sobre nosotros",
    "meta_desc": "coordinaeventos es un marketplace de espacios por horas en Lima, hecho por gente que organizó muchos eventos y se cansó de buscar en Instagram.",
    "active": "",
    "body": """
    <header class="page-header">
      <span class="eyebrow">Sobre nosotros</span>
      <h1>Nos cansamos de buscar<br>locales por Instagram.</h1>
      <p class="page-lead">coordinaeventos es un marketplace de espacios por horas en Lima, pensado para personas y empresas que necesitan resolver el "dónde" sin pasar horas chateando con cinco contactos.</p>
    </header>

    <section class="content-section">
      <h2>Lo que estamos construyendo</h2>
      <p>Un catálogo de espacios para eventos en Lima que funciona como debería: filtras por lo que necesitas, hablas directo con el host por WhatsApp, coordinas la visita y cierras la reserva. Sin formularios largos, sin pagos anticipados a desconocidos, sin comisión a hosts.</p>
      <p>Cuando alguien no tiene tiempo de coordinar todo solo, nuestro equipo se encarga: buscamos el local, hablamos con el host, gestionamos los permisos, coordinamos con los proveedores que se necesiten. Una sola conversación.</p>
    </section>

    <section class="content-section content-section-soft">
      <h2>Quiénes somos</h2>
      <p>Somos un equipo pequeño en Lima. Venimos de eventos, hospitalidad y producto. Estamos construyendo esto porque vimos el problema desde los dos lados — quien busca y quien ofrece.</p>
      <p>Si quieres contactarnos, escribe a <a href="mailto:mvelascoo@tamibot.com" style="color:var(--primary);font-weight:700;">mvelascoo@tamibot.com</a>.</p>
    </section>

    <section class="content-section content-section-dark">
      <h2>Qué buscamos cambiar</h2>
      <div class="reasons-grid">
        <div class="reason">
          <strong>Hosts que cobran lo que es</strong>
          <p>Cero comisión a hosts. Cobran directo, sin retenciones, sin sorpresas.</p>
        </div>
        <div class="reason">
          <strong>Clientes que llegan informados</strong>
          <p>Fotos reales, capacidad declarada, badge de verificación, host que responde.</p>
        </div>
        <div class="reason">
          <strong>Sin Instagram DM</strong>
          <p>Búsqueda profesional para algo que la gente todavía resuelve por DM.</p>
        </div>
        <div class="reason">
          <strong>Local primero</strong>
          <p>Lima Moderna a fondo antes de pensar en escalar a otras ciudades.</p>
        </div>
      </div>
    </section>
    """
}

PAGES["contacto"] = {
    "title": "Contacto",
    "meta_desc": "Escríbenos. Para clientes, hosts, prensa o partners. Respondemos por WhatsApp o email en menos de 24 horas.",
    "active": "",
    "body": """
    <header class="page-header">
      <span class="eyebrow">Contacto</span>
      <h1>Escríbenos.</h1>
      <p class="page-lead">Cualquier consulta, sugerencia, partnership o reclamo: te respondemos en menos de 24 horas hábiles.</p>
    </header>

    <section class="content-section">
      <h2>Email principal</h2>
      <p style="font-size:18px;"><a href="mailto:mvelascoo@tamibot.com" style="color:var(--primary);font-weight:700;">mvelascoo@tamibot.com</a></p>
    </section>

    <section class="content-section content-section-soft">
      <h2>Por tipo de consulta</h2>
      <div class="contact-grid">
        <div class="contact-card">
          <strong>Busco un espacio</strong>
          <p>Si necesitas ayuda para encontrar el local correcto, escribe al servicio de Organización de eventos.</p>
          <a href="./concierge.html" class="btn btn-outline btn-sm" data-spa-link>Ir a Organización →</a>
        </div>
        <div class="contact-card">
          <strong>Tengo un espacio</strong>
          <p>Para publicar tu local o gestionar tu listing actual.</p>
          <a href="mailto:mvelascoo@tamibot.com?subject=Quiero publicar mi espacio" class="btn btn-outline btn-sm">Email hosts</a>
        </div>
        <div class="contact-card">
          <strong>Prensa y partners</strong>
          <p>Para medios, entrevistas, partnerships estratégicos o coberturas.</p>
          <a href="mailto:mvelascoo@tamibot.com?subject=Prensa / Partners" class="btn btn-outline btn-sm">Email prensa</a>
        </div>
        <div class="contact-card">
          <strong>Reclamos formales</strong>
          <p>Si tienes un reclamo formal, regístralo en nuestro libro de reclamaciones (INDECOPI).</p>
          <a href="./legal/libro-reclamaciones.html" class="btn btn-outline btn-sm" data-spa-link>Libro de reclamaciones</a>
        </div>
      </div>
    </section>

    <section class="content-section">
      <h2>Datos generales</h2>
      <ul class="info-list">
        <li><strong>Operación:</strong> Lima, Perú</li>
        <li><strong>Cobertura:</strong> Lima Moderna (Miraflores, San Isidro, Barranco, Surco, San Borja, La Molina, Magdalena, Pueblo Libre)</li>
        <li><strong>Horario de atención:</strong> Lunes a sábado, 9am a 8pm</li>
      </ul>
    </section>
    """
}

# ───────────────────────────────────────────────────────────────
# Páginas legales
# ───────────────────────────────────────────────────────────────

LEGAL_PAGES = {
    "terminos": {
        "title": "Términos y condiciones",
        "meta_desc": "Términos y condiciones de uso de coordinaeventos.",
        "body": """
    <header class="page-header">
      <span class="eyebrow">Legal</span>
      <h1>Términos y condiciones</h1>
      <p class="page-lead">Última actualización: 11 de mayo de 2026.</p>
    </header>

    <section class="legal-content">
      <h2>1. Aceptación de los términos</h2>
      <p>Al usar coordinaeventos.com aceptas estos términos. Si no estás de acuerdo, no uses la plataforma.</p>

      <h2>2. Qué somos</h2>
      <p>coordinaeventos es un marketplace que conecta personas que buscan espacios para eventos con hosts que los ofrecen. No somos dueños ni operadores directos de los espacios listados.</p>

      <h2>3. Tu cuenta</h2>
      <p>Eres responsable de la información que provees y de las interacciones con los hosts. Debes ser mayor de edad y proveer información veraz.</p>

      <h2>4. Reservas y pagos</h2>
      <p>Las reservas y pagos se coordinan directamente entre cliente y host. coordinaeventos no intermedia el pago. Las condiciones de cancelación las define cada host.</p>

      <h2>5. Verificación</h2>
      <p>El badge "Espacio verificado" indica que nuestro equipo validó que el espacio coincide con lo publicado mediante video. No es una garantía absoluta de calidad o disponibilidad.</p>

      <h2>6. Conducta prohibida</h2>
      <p>No uses la plataforma para actividades ilegales, spam, suplantación de identidad o uso indebido de datos de hosts/clientes.</p>

      <h2>7. Propiedad intelectual</h2>
      <p>El contenido de la plataforma (marca, diseño, código) es propiedad de coordinaeventos. Las fotos y descripciones de espacios son de sus respectivos hosts.</p>

      <h2>8. Limitación de responsabilidad</h2>
      <p>coordinaeventos no se hace responsable por la calidad, seguridad o disponibilidad de los espacios. Tampoco por desacuerdos entre clientes y hosts.</p>

      <h2>9. Modificaciones</h2>
      <p>Podemos modificar estos términos. Te avisaremos por email o en la plataforma. El uso continuado implica aceptación.</p>

      <h2>10. Ley aplicable</h2>
      <p>Estos términos se rigen por la legislación peruana. Cualquier disputa se resolverá en Lima, Perú.</p>

      <h2>11. Contacto</h2>
      <p>Para consultas legales: <a href="mailto:mvelascoo@tamibot.com">mvelascoo@tamibot.com</a></p>
    </section>
    """
    },
    "privacidad": {
        "title": "Política de privacidad",
        "meta_desc": "Cómo manejamos tus datos personales en coordinaeventos.",
        "body": """
    <header class="page-header">
      <span class="eyebrow">Legal</span>
      <h1>Política de privacidad</h1>
      <p class="page-lead">Última actualización: 11 de mayo de 2026.</p>
    </header>

    <section class="legal-content">
      <h2>1. Qué datos recopilamos</h2>
      <ul>
        <li><strong>De clientes:</strong> nombre, email, WhatsApp, tipo de evento, fecha tentativa, distrito de interés.</li>
        <li><strong>De hosts:</strong> nombre comercial, dirección, WhatsApp, datos del espacio, fotos, RUC (opcional).</li>
        <li><strong>De navegación:</strong> cookies técnicas, páginas visitadas, dispositivo, IP (anonimizada).</li>
      </ul>

      <h2>2. Para qué los usamos</h2>
      <ul>
        <li>Conectarte con hosts/clientes a través de WhatsApp.</li>
        <li>Mostrar el catálogo personalizado a tus búsquedas.</li>
        <li>Mejorar la plataforma (analítica agregada y anonimizada).</li>
        <li>Comunicarte novedades del producto si te suscribiste.</li>
      </ul>

      <h2>3. Con quién compartimos</h2>
      <p>Solo compartimos los datos mínimos necesarios para que coordines con el host correspondiente. No vendemos datos a terceros. No compartimos información de clientes con otros clientes ni con hosts no relacionados a tu consulta.</p>

      <h2>4. Cookies</h2>
      <p>Usamos cookies técnicas para que la plataforma funcione (preferencias, sesión). Para más detalle ver <a href="./cookies.html" data-spa-link>Política de cookies</a>.</p>

      <h2>5. Tus derechos</h2>
      <p>Puedes pedir acceso, rectificación, supresión o portabilidad de tus datos en cualquier momento escribiendo a <a href="mailto:mvelascoo@tamibot.com">mvelascoo@tamibot.com</a>.</p>

      <h2>6. Seguridad</h2>
      <p>Los datos viajan cifrados (HTTPS) y se almacenan con medidas razonables de seguridad. Ningún sistema es 100% invulnerable, pero hacemos lo posible.</p>

      <h2>7. Retención</h2>
      <p>Conservamos los datos mientras tu cuenta esté activa o sean necesarios para cumplir con obligaciones legales (5 años para contabilidad).</p>

      <h2>8. Marco legal</h2>
      <p>Cumplimos con la Ley N° 29733 de Protección de Datos Personales de Perú.</p>

      <h2>9. Contacto</h2>
      <p>Dudas sobre privacidad: <a href="mailto:mvelascoo@tamibot.com">mvelascoo@tamibot.com</a></p>
    </section>
    """
    },
    "cookies": {
        "title": "Política de cookies",
        "meta_desc": "Cookies que usa coordinaeventos y cómo gestionarlas.",
        "body": """
    <header class="page-header">
      <span class="eyebrow">Legal</span>
      <h1>Política de cookies</h1>
      <p class="page-lead">Última actualización: 11 de mayo de 2026.</p>
    </header>

    <section class="legal-content">
      <h2>1. Qué es una cookie</h2>
      <p>Una cookie es un archivo pequeño que se guarda en tu navegador cuando visitas un sitio. Sirve para que el sitio "te recuerde" entre visitas.</p>

      <h2>2. Qué cookies usamos</h2>
      <h3>Técnicas (necesarias)</h3>
      <ul>
        <li><strong>Sesión:</strong> mantiene tu estado de navegación.</li>
        <li><strong>Preferencias:</strong> guarda filtros de búsqueda recientes y distrito preferido.</li>
      </ul>
      <h3>Analíticas (anonimizadas)</h3>
      <ul>
        <li><strong>Páginas vistas:</strong> nos ayuda a entender qué secciones son útiles.</li>
        <li><strong>Tiempo en página:</strong> agregado, sin identificarte personalmente.</li>
      </ul>

      <h2>3. Qué cookies NO usamos</h2>
      <p>No usamos cookies de publicidad, retargeting ni rastreo entre sitios.</p>

      <h2>4. Cómo gestionarlas</h2>
      <p>Puedes desactivar las cookies desde la configuración de tu navegador. Si desactivas las técnicas, algunas funciones de la plataforma pueden no funcionar correctamente.</p>

      <h2>5. Cambios en esta política</h2>
      <p>Si actualizamos cómo usamos cookies, te lo informaremos por la plataforma o por email.</p>

      <h2>6. Contacto</h2>
      <p>Dudas: <a href="mailto:mvelascoo@tamibot.com">mvelascoo@tamibot.com</a></p>
    </section>
    """
    },
    "libro-reclamaciones": {
        "title": "Libro de reclamaciones",
        "meta_desc": "Libro de reclamaciones de coordinaeventos según INDECOPI.",
        "body": """
    <header class="page-header">
      <span class="eyebrow">Legal · INDECOPI</span>
      <h1>Libro de reclamaciones</h1>
      <p class="page-lead">Conforme al Decreto Supremo N° 011-2011-PCM, contamos con un libro de reclamaciones virtual a disposición de nuestros usuarios.</p>
    </header>

    <section class="legal-content">
      <h2>Información del proveedor</h2>
      <ul class="info-list">
        <li><strong>Razón social:</strong> coordinaeventos S.A.C. (en constitución)</li>
        <li><strong>RUC:</strong> Pendiente de inscripción</li>
        <li><strong>Domicilio:</strong> Lima, Perú</li>
        <li><strong>Email:</strong> <a href="mailto:mvelascoo@tamibot.com">mvelascoo@tamibot.com</a></li>
      </ul>

      <h2>Tipos de comunicación</h2>
      <ul>
        <li><strong>Reclamo:</strong> disconformidad relacionada con el servicio prestado.</li>
        <li><strong>Queja:</strong> disconformidad ajena al servicio (atención al cliente).</li>
      </ul>

      <h2>Cómo registrar</h2>
      <p>Para registrar un reclamo o queja formal, envíanos por email a <a href="mailto:mvelascoo@tamibot.com?subject=Libro de reclamaciones - Reclamo formal">mvelascoo@tamibot.com</a> con asunto "Libro de reclamaciones — Reclamo formal" e incluye:</p>
      <ul>
        <li>Nombre completo y DNI</li>
        <li>Dirección y teléfono de contacto</li>
        <li>Email para respuesta</li>
        <li>Detalle del reclamo: fecha, espacio involucrado, host, monto si aplica</li>
        <li>Lo que pides como solución</li>
      </ul>

      <h2>Plazo de respuesta</h2>
      <p>Te responderemos en un plazo máximo de <strong>30 días calendario</strong> según lo establecido por INDECOPI.</p>

      <h2>Sobre INDECOPI</h2>
      <p>Si no estás conforme con nuestra respuesta, puedes acudir a INDECOPI:</p>
      <ul>
        <li>Web: <a href="https://www.gob.pe/indecopi" target="_blank" rel="noopener">www.gob.pe/indecopi</a></li>
        <li>Teléfono: 224-7777 (Lima)</li>
        <li>Sede central: Calle de la Prosa 104, San Borja</li>
      </ul>
    </section>
    """
    }
}


def build_host_pages(spaces: list) -> None:
    """Genera /app/host/[slug].html para cada host único (basado en distrito + slug)."""
    host_dir = APP_DIR / "host"
    host_dir.mkdir(parents=True, exist_ok=True)

    # Agrupamos espacios por distrito como proxy de host (en MVP no hay host real)
    for space in spaces:
        host_slug = space['slug']  # un "host" por espacio en el MVP
        host_name = f"Host de {space['name']}"
        verified = space.get('verificado', False)
        listado_desde = space.get('listado_desde', '2026-01-01')
        space_count = 1

        # Otros espacios del mismo distrito como proxy del portfolio
        same_district = [s for s in spaces if s['distrito'] == space['distrito']]
        if len(same_district) > 1:
            space_count = len(same_district)

        verified_badge = '''<span class="host-page-verified">
            <svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true">
              <circle cx="12" cy="12" r="11" fill="#1D9BF0"/>
              <path d="M7 12.5 L10.5 16 L17 9" stroke="white" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span>Host verificado</span>
          </span>''' if verified else ''

        cards = ""
        for s in same_district:
            v_mark = '''<span class="listing-card-verified"><svg width="20" height="20" viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="#1D9BF0"/><path d="M7 12.5 L10.5 16 L17 9" stroke="white" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></span>''' if s.get('verificado') else ''
            cards += f'''<a class="listing-card" href="../espacios/{s["slug"]}.html" data-spa-link>
              <div class="listing-card-photo">
                <img src="{s["fotos"][0]}" alt="{s["name"]}" loading="lazy" />
                {v_mark}
              </div>
              <div class="listing-card-body">
                <div class="listing-card-head">
                  <h3>{s["name"]}</h3>
                  <strong class="listing-card-price">Desde S/ {s["precio_hora_pen"]}<span>/h</span></strong>
                </div>
                <p class="listing-card-meta">{s["distrito"]} · Hasta {s["capacidad_max"]} pers · {s["tipo"]}</p>
              </div>
            </a>'''

        body = f"""
    <header class="page-header host-page-header">
      <span class="eyebrow">Host · {space['distrito']}</span>
      <div class="host-page-info">
        <div class="host-page-avatar">{space['slug'][0].upper()}H</div>
        <div>
          <h1>{html.escape(host_name)}</h1>
          <div class="host-page-meta">
            {verified_badge}
            <span>Listado desde 2025</span>
            <span>·</span>
            <span>{space_count} {"espacio" if space_count == 1 else "espacios"}</span>
            <span>·</span>
            <span>Responde en 2 horas</span>
          </div>
        </div>
      </div>
    </header>

    <section class="content-section">
      <h2>Espacios de este host</h2>
      <div class="grid grid-similares">
        {cards}
      </div>
    </section>

    <section class="content-section content-section-soft">
      <h2>Contactar al host</h2>
      <p>Coordina la visita o pide info adicional por WhatsApp.</p>
      <a href="mailto:mvelascoo@tamibot.com" class="btn btn-primary">Escribir al host</a>
    </section>
        """

        page = render_page(
            slug=host_slug,
            title=f"{host_name}",
            meta_desc=f"Espacios del host en {space['distrito']}. {space_count} espacios para alquilar por horas en Lima.",
            body=body,
            active="",
            page_data="host",
            depth=1
        )
        out = host_dir / f"{host_slug}.html"
        out.write_text(page)


def main() -> int:
    APP_DIR.mkdir(parents=True, exist_ok=True)
    (APP_DIR / "legal").mkdir(parents=True, exist_ok=True)

    # Páginas principales
    for slug, info in PAGES.items():
        page = render_page(
            slug=slug,
            title=info["title"],
            meta_desc=info["meta_desc"],
            body=info["body"],
            active=info.get("active", ""),
            page_data=slug,
            depth=0
        )
        out = APP_DIR / f"{slug}.html"
        out.write_text(page)
        print(f"  ✓ {out.relative_to(ROOT)}")

    # Legales
    for slug, info in LEGAL_PAGES.items():
        page = render_page(
            slug=slug,
            title=info["title"],
            meta_desc=info["meta_desc"],
            body=info["body"],
            active="",
            page_data="legal",
            depth=1
        )
        out = APP_DIR / "legal" / f"{slug}.html"
        out.write_text(page)
        print(f"  ✓ {out.relative_to(ROOT)}")

    # Páginas de host
    spaces = json.loads(DATA.read_text())["spaces"]
    build_host_pages(spaces)
    print(f"  ✓ Generadas {len(spaces)} páginas de host")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
