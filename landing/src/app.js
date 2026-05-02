// Coordina — landing logic.
// Captura del search form (placeholder hasta tener API).
// Captura del host form.

function bindForm(formId, kind) {
  const form = document.getElementById(formId);
  if (!form) return;
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const payload = Object.fromEntries(new FormData(form).entries());
    payload.kind = kind;
    payload.ts = new Date().toISOString();

    if (kind === 'search') {
      console.log('[search:queued]', payload);
      flash(form, 'Listo. Estamos preparando los primeros espacios — te avisamos cuando abramos.', true);
      form.reset();
      return;
    }

    const email = payload.email?.toString().trim();
    if (!email || !email.includes('@')) {
      flash(form, 'Necesitamos un correo válido.');
      return;
    }
    console.log('[host:queued]', payload);
    flash(form, 'Recibido. Te contactamos por WhatsApp en menos de 24 h.', true);
    form.reset();
  });
}

function flash(form, msg, ok = false) {
  let node = form.parentElement.querySelector('.flash');
  if (!node) {
    node = document.createElement('p');
    node.className = 'flash';
    node.style.cssText = `
      margin-top: 14px;
      font-size: 13px;
      font-weight: 500;
      letter-spacing: -0.005em;
      max-width: 60ch;
    `;
    form.parentElement.appendChild(node);
  }
  node.textContent = msg;
  node.style.color = ok ? '#047857' : '#B91C1C';
}

bindForm('search-form', 'search');
bindForm('host-form', 'host');
