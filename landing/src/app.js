// Coordina Eventos — landing logic
// Hidrata categorías por caso de uso (no por tipo).
// Maneja submits del waitlist sin backend (placeholder).

const CATEGORIAS_USE_CASE = [
  'Cumpleaños',
  'Baby shower',
  'Sesión de fotos',
  'Reunión de trabajo',
  'Capacitación',
  'Yoga / clase',
  'Despedida',
  'Pop-up',
  'Grabación de video',
  'Aniversario',
  'Coworking por horas',
  'Lanzamiento de producto',
];

function hydrateChips() {
  const target = document.getElementById('cat-chips');
  if (!target) return;
  target.innerHTML = CATEGORIAS_USE_CASE
    .map((label) => `<span class="chip">${label}</span>`)
    .join('');
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
    flash(form, 'Listo. Te avisamos cuando abramos.', true);
    form.reset();
  });
}

function flash(form, msg, ok = false) {
  let node = form.querySelector('.flash');
  if (!node) {
    node = document.createElement('p');
    node.className = 'flash micro';
    node.style.marginTop = '12px';
    node.style.fontWeight = '500';
    form.appendChild(node);
  }
  node.textContent = msg;
  node.style.color = ok ? '#10B981' : '#EF4444';
}

hydrateChips();
bindWaitlist('waitlist-form', 'guest');
bindWaitlist('host-form', 'host');
