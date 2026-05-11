// coordinaeventos app — catálogo + detalle + SPA navigation + FAB IA.

const CATEGORIAS = {
  'cumpleanos': 'Cumpleaños',
  'baby-shower': 'Baby shower',
  'sesion-fotos': 'Sesión de fotos',
  'reunion': 'Reunión de trabajo',
  'capacitacion': 'Capacitación',
  'conferencia': 'Conferencia',
  'yoga-clase': 'Yoga · clase',
  'despedida': 'Despedida',
  'pop-up': 'Pop-up',
  'aniversario': 'Aniversario',
  'coworking': 'Coworking',
  'lanzamiento': 'Lanzamiento',
  'boda': 'Boda',
  'grabacion-video': 'Grabación de video',
  'podcast': 'Podcast',
  'cena-corporativa': 'Cena corporativa',
};

// ──────────────────────────────────────────────────────────────
// Helpers
// ──────────────────────────────────────────────────────────────
function fmtPrice(n) {
  return 'S/ ' + n.toLocaleString('es-PE');
}

// Truncar dirección a algo breve: "Avenida San Martín, Barranco" → "Av. San Martín"
function briefAddress(addr) {
  if (!addr) return '';
  return addr.split(',')[0].replace(/^(Avenida|Calle|Jirón|Pasaje)\s+/i, m => {
    const map = { 'avenida': 'Av.', 'calle': 'Cl.', 'jirón': 'Jr.', 'pasaje': 'Psje.' };
    return (map[m.trim().toLowerCase()] || m.trim()) + ' ';
  }).trim();
}

function verifiedMark(size = 22) {
  return `<svg width="${size}" height="${size}" viewBox="0 0 24 24" aria-hidden="true">
    <circle cx="12" cy="12" r="11" fill="#1D9BF0"/>
    <path d="M7 12.5 L10.5 16 L17 9" stroke="white" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>`;
}

async function loadSpaces() {
  const candidates = ['./spaces.json', '../spaces.json', '/space-peru/app/web/spaces.json'];
  for (const url of candidates) {
    try {
      const r = await fetch(url, { cache: 'no-store' });
      if (r.ok) return (await r.json()).spaces;
    } catch (_) { }
  }
  console.error('No se pudo cargar spaces.json');
  return [];
}

function getQuery() { return new URLSearchParams(location.search); }

// ──────────────────────────────────────────────────────────────
// Listing card (catálogo)
// ──────────────────────────────────────────────────────────────
function spaceCard(space) {
  const verified = space.verificado
    ? `<span class="listing-card-verified" title="Espacio verificado">${verifiedMark(22)}</span>`
    : '';
  const detailHref = './espacios/' + space.slug + '.html';
  const address = briefAddress(space.direccion || space.distrito);
  return `
    <a class="listing-card" href="${detailHref}" data-spa-link>
      <div class="listing-card-photo">
        <img src="${space.fotos[0]}" alt="${space.name}" loading="lazy" />
        ${verified}
      </div>
      <div class="listing-card-body">
        <div class="listing-card-head">
          <h3>${space.name}</h3>
          <strong class="listing-card-price">Desde ${fmtPrice(space.precio_hora_pen)}<span>/h</span></strong>
        </div>
        <p class="listing-card-meta">${address} · Hasta ${space.capacidad_max} pers · ${space.tipo}</p>
      </div>
    </a>
  `;
}

// ──────────────────────────────────────────────────────────────
// Filtro y sort
// ──────────────────────────────────────────────────────────────
function filterSpaces(spaces, q) {
  let out = spaces.slice();
  const caso = q.get('caso');
  const distrito = q.get('distrito');
  const cap = parseInt(q.get('cap'), 10);
  const extras = (q.get('extras') || '').split(',').filter(Boolean);

  if (caso) out = out.filter(s => s.casos_uso && s.casos_uso.includes(caso));
  if (distrito) out = out.filter(s => s.distrito === distrito);
  if (!isNaN(cap)) out = out.filter(s => s.capacidad_max >= cap);

  // extras filters
  for (const extra of extras) {
    if (extra === 'verificado') out = out.filter(s => s.verificado);
    else if (extra === 'con-wifi') out = out.filter(s => s.amenities?.includes('wifi'));
    else if (extra === 'con-parking') out = out.filter(s => s.amenities?.includes('estacionamiento'));
    else if (extra === 'con-cocina') out = out.filter(s => s.amenities?.includes('cocina'));
    else if (extra === 'con-sonido') out = out.filter(s => s.amenities?.includes('sonido'));
    else if (extra === 'con-proyector') out = out.filter(s => s.amenities?.includes('proyector'));
  }

  const sort = q.get('sort') || 'rating';
  if (sort === 'price-asc') out.sort((a, b) => a.precio_hora_pen - b.precio_hora_pen);
  else if (sort === 'price-desc') out.sort((a, b) => b.precio_hora_pen - a.precio_hora_pen);
  else if (sort === 'cap') out.sort((a, b) => b.capacidad_max - a.capacidad_max);
  else if (sort === 'verified') out.sort((a, b) => (b.verificado ? 1 : 0) - (a.verificado ? 1 : 0) || b.rating - a.rating);
  else out.sort((a, b) => b.rating - a.rating);
  return out;
}

async function renderHome() {
  const target = document.getElementById('grid');
  if (!target) return;
  const spaces = await loadSpaces();
  const top = spaces.slice().sort((a, b) => b.rating - a.rating).slice(0, 6);
  target.innerHTML = top.map(spaceCard).join('');
  const countEl = document.getElementById('count');
  if (countEl) countEl.innerHTML = `<strong>${spaces.length}</strong> espacios verificados en Lima`;
}

async function renderSearch() {
  const target = document.getElementById('grid');
  if (!target) return;
  const spaces = await loadSpaces();
  const q = getQuery();
  const filtered = filterSpaces(spaces, q);

  const countEl = document.getElementById('count');
  if (countEl) countEl.innerHTML = `<strong>${filtered.length}</strong> ${filtered.length === 1 ? 'espacio encontrado' : 'espacios encontrados'}`;

  if (filtered.length === 0) {
    target.innerHTML = `
      <div class="empty-state" style="grid-column: 1 / -1;">
        <h3>No encontramos espacios con esos filtros</h3>
        <p>Quita uno o pide ayuda al asistente — encontramos el que necesitas.</p>
      </div>
    `;
    return;
  }
  target.innerHTML = filtered.map(spaceCard).join('');

  // Update active chips
  document.querySelectorAll('.filter-chip').forEach(chip => {
    const filterCaso = chip.dataset.caso;
    const filterDistrito = chip.dataset.distrito;
    const filterExtra = chip.dataset.extra;
    const isActive = Boolean(
      (filterCaso && filterCaso === q.get('caso')) ||
      (filterDistrito && filterDistrito === q.get('distrito')) ||
      (filterExtra && (q.get('extras') || '').split(',').includes(filterExtra))
    );
    chip.classList.toggle('active', isActive);
  });

  // Reflect form values
  const evt = document.getElementById('q-event');
  const where = document.getElementById('q-where');
  const cap = document.getElementById('q-cap');
  if (evt) evt.value = q.get('caso') ? CATEGORIAS[q.get('caso')] || '' : '';
  if (where) where.value = q.get('distrito') || '';
  if (cap) cap.value = q.get('cap') || '';

  const sortSel = document.getElementById('sort');
  if (sortSel) sortSel.value = q.get('sort') || 'rating';
}

// ──────────────────────────────────────────────────────────────
// Search bar + filters
// ──────────────────────────────────────────────────────────────
function bindSearchBar() {
  const form = document.getElementById('search-form');
  if (!form) return;
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const evt = (document.getElementById('q-event')?.value || '').trim().toLowerCase();
    const where = (document.getElementById('q-where')?.value || '').trim();
    const cap = (document.getElementById('q-cap')?.value || '').trim();
    let caso = '';
    for (const [slug, label] of Object.entries(CATEGORIAS)) {
      if (label.toLowerCase().includes(evt) || slug.includes(evt) || evt.includes(slug.replace('-', ' '))) {
        caso = slug; break;
      }
    }
    const params = new URLSearchParams();
    if (caso) params.set('caso', caso);
    if (where) params.set('distrito', where);
    if (cap) params.set('cap', cap);
    const target = location.pathname.includes('/app/') ? './buscar.html' : './app/buscar.html';
    spaNavigate(target + '?' + params.toString());
  });
}

function bindFilters() {
  document.body.addEventListener('click', (e) => {
    const chip = e.target.closest('.filter-chip');
    if (!chip) return;
    e.preventDefault();
    const q = getQuery();
    if (chip.dataset.caso) {
      if (q.get('caso') === chip.dataset.caso) q.delete('caso');
      else q.set('caso', chip.dataset.caso);
    }
    if (chip.dataset.distrito) {
      if (q.get('distrito') === chip.dataset.distrito) q.delete('distrito');
      else q.set('distrito', chip.dataset.distrito);
    }
    if (chip.dataset.extra) {
      const current = (q.get('extras') || '').split(',').filter(Boolean);
      const idx = current.indexOf(chip.dataset.extra);
      if (idx >= 0) current.splice(idx, 1);
      else current.push(chip.dataset.extra);
      if (current.length > 0) q.set('extras', current.join(','));
      else q.delete('extras');
    }
    const url = new URL(location.href);
    url.search = q.toString();
    spaNavigate(url.pathname + url.search);
  });

  const sortSel = document.getElementById('sort');
  if (sortSel) {
    sortSel.addEventListener('change', () => {
      const q = getQuery();
      q.set('sort', sortSel.value);
      const url = new URL(location.href);
      url.search = q.toString();
      spaNavigate(url.pathname + url.search);
    });
  }
}

// ──────────────────────────────────────────────────────────────
// SPA Navigation — History API + fetch + replace body
// Evita refresh visual cuando el usuario navega entre páginas
// ──────────────────────────────────────────────────────────────
function spaSupported() {
  return typeof window.history !== 'undefined' && typeof window.fetch !== 'undefined';
}

function showSpaLoading() {
  let bar = document.querySelector('.spa-loading');
  if (!bar) {
    bar = document.createElement('div');
    bar.className = 'spa-loading';
    document.body.appendChild(bar);
  }
}

function hideSpaLoading() {
  document.querySelectorAll('.spa-loading').forEach(el => el.remove());
}

async function spaNavigate(url) {
  if (!spaSupported()) { location.href = url; return; }

  // Si es un link externo o anchor de la misma página, navegación normal
  if (url.startsWith('http') && !url.startsWith(location.origin)) {
    location.href = url; return;
  }
  if (url.startsWith('#')) {
    location.hash = url; return;
  }

  showSpaLoading();
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error('Fetch failed');
    const text = await res.text();
    const parser = new DOMParser();
    const doc = parser.parseFromString(text, 'text/html');

    // Actualizar title + body
    document.title = doc.title;
    document.body.innerHTML = doc.body.innerHTML;
    document.body.dataset.page = doc.body.dataset.page || '';

    // Update history
    history.pushState({ url }, '', url);

    // Re-init scripts/listeners para el nuevo DOM
    initPage();
    window.scrollTo(0, 0);
  } catch (err) {
    console.error('SPA nav failed, fallback to full reload', err);
    location.href = url;
  } finally {
    hideSpaLoading();
  }
}

function bindSpaLinks() {
  document.body.addEventListener('click', (e) => {
    const link = e.target.closest('a[data-spa-link]');
    if (!link) return;
    const href = link.getAttribute('href');
    if (!href || href.startsWith('http') && !href.startsWith(location.origin)) return;
    if (link.target === '_blank') return;
    if (e.metaKey || e.ctrlKey || e.shiftKey) return; // open in new tab
    e.preventDefault();
    spaNavigate(href);
  });

  window.addEventListener('popstate', () => {
    spaNavigate(location.pathname + location.search);
  });
}

// ──────────────────────────────────────────────────────────────
// FAB Asistente IA
// ──────────────────────────────────────────────────────────────
function bindAIFab() {
  const fab = document.getElementById('ai-fab');
  if (!fab) {
    // Si no existe el FAB, lo creamos dinámicamente (para landing/buscar)
    if (document.body.dataset.page) {
      const btn = document.createElement('button');
      btn.id = 'ai-fab';
      btn.className = 'ai-fab';
      btn.setAttribute('aria-label', 'Abrir asistente IA');
      btn.innerHTML = `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.2" aria-hidden="true">
        <path d="M12 2 C6.5 2 2 6.5 2 12 C2 14 2.5 15.8 3.4 17.4 L2 22 L6.6 20.6 C8.2 21.5 10 22 12 22 C17.5 22 22 17.5 22 12 C22 6.5 17.5 2 12 2 Z"/>
        <circle cx="8" cy="12" r="1" fill="white"/>
        <circle cx="12" cy="12" r="1" fill="white"/>
        <circle cx="16" cy="12" r="1" fill="white"/>
      </svg><span class="ai-fab-label">Asistente IA</span>`;
      document.body.appendChild(btn);
    }
  }

  const fabBtn = document.getElementById('ai-fab');
  if (!fabBtn) return;

  fabBtn.addEventListener('click', () => {
    let panel = document.getElementById('ai-panel');
    if (!panel) {
      panel = document.createElement('div');
      panel.id = 'ai-panel';
      panel.className = 'ai-panel';
      panel.innerHTML = `
        <div class="ai-panel-header">
          <strong>Asistente IA</strong>
          <button class="ai-panel-close" aria-label="Cerrar">×</button>
        </div>
        <div class="ai-panel-body">
          <p>Cuéntame qué estás buscando y te traigo los espacios que encajan.</p>
          <span class="ai-suggestion" data-q="Cumpleaños para 30 personas">Cumpleaños para 30 personas</span>
          <span class="ai-suggestion" data-q="Sala de reuniones en San Isidro">Sala de reuniones en San Isidro</span>
          <span class="ai-suggestion" data-q="Cena corporativa de fin de año">Cena corporativa de fin de año</span>
          <span class="ai-suggestion" data-q="Sesión de fotos con luz natural">Sesión de fotos con luz natural</span>
          <p style="margin-top:14px;font-size:12px;color:var(--muted);">El asistente completo está en desarrollo. Por ahora estos shortcuts filtran el catálogo.</p>
        </div>
      `;
      document.body.appendChild(panel);

      panel.querySelector('.ai-panel-close').addEventListener('click', () => panel.classList.remove('open'));
      panel.querySelectorAll('.ai-suggestion').forEach(s => {
        s.addEventListener('click', () => {
          const q = s.dataset.q;
          const params = new URLSearchParams();
          // Detectar slug y distrito básicos
          for (const [slug, label] of Object.entries(CATEGORIAS)) {
            if (q.toLowerCase().includes(label.toLowerCase())) { params.set('caso', slug); break; }
          }
          const distritos = ['Miraflores', 'San Isidro', 'Barranco', 'Surco', 'San Borja', 'La Molina', 'Magdalena del Mar', 'Pueblo Libre'];
          for (const d of distritos) {
            if (q.toLowerCase().includes(d.toLowerCase().split(' ')[0])) { params.set('distrito', d); break; }
          }
          const target = location.pathname.includes('/app/') ? './buscar.html' : '/app/buscar.html';
          panel.classList.remove('open');
          spaNavigate(target + '?' + params.toString());
        });
      });
    }
    panel.classList.toggle('open');
  });
}

// ──────────────────────────────────────────────────────────────
// Init
// ──────────────────────────────────────────────────────────────
function initPage() {
  const page = document.body.dataset.page;
  if (page === 'home') renderHome();
  else if (page === 'search') {
    renderSearch();
    bindSearchBar();
    bindFilters();
  }
  bindAIFab();
}

if (!window.__spaInit) {
  window.__spaInit = true;
  bindSpaLinks();
}
initPage();
