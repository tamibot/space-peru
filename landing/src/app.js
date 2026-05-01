// Hidrata categorías y maneja submits del waitlist sin backend (placeholder).
// Cuando exista API/Worker, reemplazar el handler de submit por un fetch.

// En dev (file:// o localhost desde landing/src/) sirve `../../data/public/...`
// En GitHub Pages el workflow copia data a `/data/public/...`
const CATEGORIAS_URLS = ['./data/public/categorias.json', '../../data/public/categorias.json'];

async function hydrateChips() {
  const target = document.getElementById('cat-chips');
  if (!target) return;
  let data = null;
  for (const url of CATEGORIAS_URLS) {
    try {
      const res = await fetch(url, { cache: 'no-store' });
      if (res.ok) { data = await res.json(); break; }
    } catch { /* try next */ }
  }
  try {
    if (!data) throw new Error('no-fetch');
    const data = await res.json();
    target.innerHTML = data.categorias
      .map((c) => `<span class="chip">${c.label}</span>`)
      .join('');
  } catch {
    // Fallback estático si no se sirve via http (file://)
    const fallback = [
      'Salones para eventos','Salas de reuniones','Estudios foto y video',
      'Estudios de grabación','Espacios deportivos','Estudios para clases',
      'Coworking por horas','Espacios para rodaje','Cocinas','Almacenes y lockers',
    ];
    target.innerHTML = fallback.map((l) => `<span class="chip">${l}</span>`).join('');
  }
}

function bindWaitlist(formId, kind) {
  const form = document.getElementById(formId);
  if (!form) return;
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = form.querySelector('input[type=email]')?.value?.trim();
    if (!email || !email.includes('@')) {
      flash(form, 'Necesitamos un correo válido.');
      return;
    }
    // TODO: reemplazar por POST a /api/waitlist (Cloudflare Worker → Postgres)
    const payload = Object.fromEntries(new FormData(form).entries());
    payload.kind = kind;
    payload.ts = new Date().toISOString();
    console.log('[waitlist:queued]', payload);
    flash(form, '¡Listo! Te avisamos cuando abramos.', true);
    form.reset();
  });
}

function flash(form, msg, ok = false) {
  let node = form.querySelector('.flash');
  if (!node) {
    node = document.createElement('p');
    node.className = 'flash micro';
    node.style.marginTop = '8px';
    form.appendChild(node);
  }
  node.textContent = msg;
  node.style.color = ok ? '#10B981' : '#EF4444';
}

hydrateChips();
bindWaitlist('waitlist-form', 'guest');
bindWaitlist('host-form', 'host');
