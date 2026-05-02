// Coordina — landing logic
// 1) Smooth scroll para anchors
// 2) Sección "Para cada momento": hover/click en actividad cambia la imagen
// 3) IntersectionObserver para reveal animations al entrar en viewport

(() => {
  // ── 1. Smooth scroll para anchors ──────────────────────────────
  document.querySelectorAll('a[href^="#"]').forEach((a) => {
    a.addEventListener('click', (e) => {
      const id = a.getAttribute('href');
      if (id === '#' || !id) return;
      const target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  // ── 2. Sección momento: hover cambia imagen + meta ─────────────
  const list = document.getElementById('momento-list');
  const img = document.getElementById('momento-img');
  const meta = document.getElementById('momento-meta');

  if (list && img && meta) {
    const items = list.querySelectorAll('li');

    // Preload todas las imágenes para que el hover sea instantáneo
    items.forEach((li) => {
      const url = li.dataset.img;
      if (url) { const i = new Image(); i.src = url; }
    });

    const setActive = (li) => {
      const url = li.dataset.img;
      const name = li.dataset.name;
      if (!url || !name) return;
      if (img.src === url) return;

      // fade out → cambiar src → fade in
      img.classList.add('fading');
      meta.classList.add('fading');

      setTimeout(() => {
        img.src = url;
        img.alt = name;
        meta.textContent = name;
        // wait next frame para que la opacidad cambie
        requestAnimationFrame(() => {
          img.classList.remove('fading');
          meta.classList.remove('fading');
        });
      }, 200);

      items.forEach((x) => x.classList.remove('active'));
      li.classList.add('active');
    };

    items.forEach((li) => {
      li.addEventListener('mouseenter', () => setActive(li));
      li.addEventListener('focus', () => setActive(li));
      li.addEventListener('click', () => setActive(li));
      li.tabIndex = 0;
    });
  }

  // ── 3. Reveal on scroll (para elementos fuera del hero) ────────
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('reveal-in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });

    document.querySelectorAll('.section-head, .feat, .step, .why-item, .aud-card, .space-card, .momento-text, .momento-photo')
      .forEach((el) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity .7s cubic-bezier(0.22, 1, 0.36, 1), transform .7s cubic-bezier(0.22, 1, 0.36, 1)';
        io.observe(el);
      });

    // CSS injected for reveal-in state
    const style = document.createElement('style');
    style.textContent = `
      .reveal-in {
        opacity: 1 !important;
        transform: translateY(0) !important;
      }
      @media (prefers-reduced-motion: reduce) {
        .section-head, .feat, .step, .why-item, .aud-card, .space-card, .momento-text, .momento-photo {
          opacity: 1 !important;
          transform: none !important;
        }
      }
    `;
    document.head.appendChild(style);
  }
})();
