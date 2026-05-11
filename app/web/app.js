// Coordina app — lógica compartida.
// 1) Carga dataset spaces.json
// 2) Render grid de resultados con filtros
// 3) Search bar con redirect a /buscar
// 4) Smooth scroll

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
  'talleres': 'Talleres',
};

const DISTRITOS = ['Miraflores', 'San Isidro', 'Barranco', 'Surco', 'San Borja', 'La Molina', 'Magdalena del Mar', 'Pueblo Libre'];

// Detect base path (works on github.io subpath and on root)
function basePath() {
  const p = location.pathname;
  // if we're inside /app/, the base is up to and including /app/
  const idx = p.indexOf('/app/');
  if (idx >= 0) return p.slice(0, idx + 5); // includes trailing /app/
  // fallback: go up to file containing dir
  return p.replace(/[^/]*$/, '');
}

async function loadSpaces() {
  const candidates = ['./spaces.json', '../spaces.json', '/space-peru/app/web/spaces.json'];
  for (const url of candidates) {
    try {
      const r = await fetch(url, { cache: 'no-store' });
      if (r.ok) return (await r.json()).spaces;
    } catch (_) { /* try next */ }
  }
  console.error('No se pudo cargar spaces.json');
  return [];
}

function getQuery() {
  return new URLSearchParams(location.search);
}

function setQuery(params) {
  const url = new URL(location.href);
  Object.entries(params).forEach(([k, v]) => {
    if (v === '' || v == null) url.searchParams.delete(k);
    else url.searchParams.set(k, v);
  });
  history.replaceState({}, '', url);
}

function fmtPrice(n) {
  return 'S/ ' + n.toLocaleString('es-PE');
}

function spaceCard(space) {
  const verifiedMark = space.verificado
    ? `<span class="listing-card-verified" title="Espacio verificado">
         <svg viewBox="0 0 24 24" aria-hidden="true">
           <circle cx="12" cy="12" r="11" fill="#1D9BF0"/>
           <path d="M7 12.5 L10.5 16 L17 9" stroke="white" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
         </svg>
       </span>`
    : '';
  const detailHref = './espacios/' + space.slug + '.html';
  // Top 3 amenities (compactas)
  const amenities = (space.amenidades || []).slice(0, 4).join(' · ');
  return `
    <a class="listing-card" href="${detailHref}">
      <div class="listing-card-photo">
        <img src="${space.fotos[0]}" alt="${space.name}" loading="lazy" />
        ${verifiedMark}
      </div>
      <div class="listing-card-body">
        <div class="listing-card-head">
          <h3>${space.name}</h3>
          <strong class="listing-card-price">${fmtPrice(space.precio_hora_pen)}<span>/h</span></strong>
        </div>
        <p class="listing-card-meta">${space.distrito} · Hasta ${space.capacidad_max} personas · ${space.tipo}</p>
        ${amenities ? `<p class="listing-card-amenities">${amenities}</p>` : ''}
      </div>
    </a>
  `;
}

function filterSpaces(spaces, q) {
  let out = spaces.slice();
  const caso = q.get('caso');
  const distrito = q.get('distrito');
  const cap = parseInt(q.get('cap'), 10);
  const max = parseInt(q.get('max'), 10);

  if (caso) out = out.filter(s => s.casos_uso && s.casos_uso.includes(caso));
  if (distrito) out = out.filter(s => s.distrito === distrito);
  if (!isNaN(cap)) out = out.filter(s => s.capacidad_max >= cap);
  if (!isNaN(max)) out = out.filter(s => s.precio_hora_pen <= max);

  // sort
  const sort = q.get('sort') || 'rating';
  if (sort === 'price-asc') out.sort((a, b) => a.precio_hora_pen - b.precio_hora_pen);
  else if (sort === 'price-desc') out.sort((a, b) => b.precio_hora_pen - a.precio_hora_pen);
  else if (sort === 'cap') out.sort((a, b) => b.capacidad_max - a.capacidad_max);
  else out.sort((a, b) => b.rating - a.rating);

  return out;
}

async function renderHome() {
  const target = document.getElementById('grid');
  if (!target) return;
  const spaces = await loadSpaces();
  // home: featured = top 6 by rating
  const top = spaces.slice().sort((a, b) => b.rating - a.rating).slice(0, 6);
  target.innerHTML = top.map(spaceCard).join('');

  const countEl = document.getElementById('count');
  if (countEl) countEl.textContent = spaces.length + ' espacios verificados en Lima';
}

async function renderSearch() {
  const target = document.getElementById('grid');
  if (!target) return;
  const spaces = await loadSpaces();
  const q = getQuery();
  const filtered = filterSpaces(spaces, q);

  const countEl = document.getElementById('count');
  if (countEl) countEl.textContent = `${filtered.length} ${filtered.length === 1 ? 'espacio encontrado' : 'espacios encontrados'}`;

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

  // Update active filter chips — coerce a boolean para que toggle(force=false) realmente remueva
  document.querySelectorAll('.filter-chip').forEach(chip => {
    const filterCaso = chip.dataset.caso;
    const filterDistrito = chip.dataset.distrito;
    const filterExtra = chip.dataset.extra;
    const isActive = Boolean(
      (filterCaso && filterCaso === q.get('caso')) ||
      (filterDistrito && filterDistrito === q.get('distrito')) ||
      (filterExtra && q.get('extras')?.split(',').includes(filterExtra))
    );
    chip.classList.toggle('active', isActive);
  });

  // Reflect form values from query
  const evt = document.getElementById('q-event');
  const where = document.getElementById('q-where');
  const cap = document.getElementById('q-cap');
  if (evt) evt.value = q.get('caso') ? CATEGORIAS[q.get('caso')] || '' : '';
  if (where) where.value = q.get('distrito') || '';
  if (cap) cap.value = q.get('cap') || '';

  const sortSel = document.getElementById('sort');
  if (sortSel) sortSel.value = q.get('sort') || 'rating';
}

// search bar handler — convierte texto a slug de caso si match
function bindSearchBar() {
  const form = document.getElementById('search-form');
  if (!form) return;
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const evt = (document.getElementById('q-event')?.value || '').trim().toLowerCase();
    const where = (document.getElementById('q-where')?.value || '').trim();
    const cap = (document.getElementById('q-cap')?.value || '').trim();

    // best-match a slug de caso
    let caso = '';
    for (const [slug, label] of Object.entries(CATEGORIAS)) {
      if (label.toLowerCase().includes(evt) || slug.includes(evt) || evt.includes(slug.replace('-', ' '))) {
        caso = slug;
        break;
      }
    }

    const params = new URLSearchParams();
    if (caso) params.set('caso', caso);
    if (where) params.set('distrito', where);
    if (cap) params.set('cap', cap);

    // siempre vamos a buscar.html
    const target = location.pathname.includes('/app/') ? './buscar.html' : './app/buscar.html';
    location.href = target + '?' + params.toString();
  });
}

function bindFilters() {
  document.querySelectorAll('.filter-chip').forEach(chip => {
    chip.addEventListener('click', (e) => {
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
      location.href = url.pathname + url.search;
    });
  });

  const sortSel = document.getElementById('sort');
  if (sortSel) {
    sortSel.addEventListener('change', () => {
      const q = getQuery();
      q.set('sort', sortSel.value);
      const url = new URL(location.href);
      url.search = q.toString();
      location.href = url.pathname + url.search;
    });
  }
}

// initialize based on page
document.addEventListener('DOMContentLoaded', () => {
  bindSearchBar();
  bindFilters();
  if (document.body.dataset.page === 'home') renderHome();
  else if (document.body.dataset.page === 'search') renderSearch();
});
