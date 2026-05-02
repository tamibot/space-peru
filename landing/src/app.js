// Coordina — landing logic
// 1) Smooth scroll
// 2) Sección "Para cada momento": hover/click cambia imagen
// 3) IntersectionObserver: reveal animations on scroll
// 4) Disparar animaciones del chat (asistente IA) y SVG steps al entrar viewport

(() => {
  // ── 1. Smooth scroll ────────────────────────────────────────────
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

  // ── 2. Sección momento ──────────────────────────────────────────
  const list = document.getElementById('momento-list');
  const img = document.getElementById('momento-img');
  const meta = document.getElementById('momento-meta');

  if (list && img && meta) {
    const items = list.querySelectorAll('li');
    items.forEach((li) => {
      const url = li.dataset.img;
      if (url) { const i = new Image(); i.src = url; }
    });

    const setActive = (li) => {
      const url = li.dataset.img;
      const name = li.dataset.name;
      if (!url || !name) return;
      if (img.src === url) return;

      img.classList.add('fading');
      meta.classList.add('fading');

      setTimeout(() => {
        img.src = url;
        img.alt = name;
        meta.textContent = name;
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

  // ── 3. IntersectionObserver: reveal on scroll ──────────────────
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('reveal-in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });

    document.querySelectorAll('.section-head, .feat, .step, .why-item, .aud-card, .space-card, .momento-text, .momento-photo, .ai-text, .ai-features li, .chip-static')
      .forEach((el) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity .7s cubic-bezier(0.22, 1, 0.36, 1), transform .7s cubic-bezier(0.22, 1, 0.36, 1)';
        io.observe(el);
      });

    const style = document.createElement('style');
    style.textContent = `
      .reveal-in { opacity: 1 !important; transform: translateY(0) !important; }
      @media (prefers-reduced-motion: reduce) {
        .section-head, .feat, .step, .why-item, .aud-card, .space-card,
        .momento-text, .momento-photo, .ai-text, .ai-features li, .chip-static {
          opacity: 1 !important; transform: none !important;
        }
      }
    `;
    document.head.appendChild(style);

    // ── 4a. Chat mock animation ────────────────────────────────
    const chatBody = document.getElementById('chat-body');
    if (chatBody) {
      const chatIO = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            chatBody.querySelectorAll('.anim').forEach((el) => el.classList.add('play'));
            chatIO.unobserve(entry.target);
          }
        });
      }, { threshold: 0.3 });
      chatIO.observe(chatBody);
    }

    // ── 4b. SVG steps animations ───────────────────────────────
    const stepIO = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('play');
          stepIO.unobserve(entry.target);
        }
      });
    }, { threshold: 0.4 });
    document.querySelectorAll('.step-svg').forEach((el) => stepIO.observe(el));

    // ── 4c. Benefits SVG animations (path-draw + dots) ─────────
    const benIO = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
          benIO.unobserve(entry.target);
        }
      });
    }, { threshold: 0.3 });
    document.querySelectorAll('.benefit').forEach((el) => benIO.observe(el));

    // ── 4d. Soon cards SVG animations ──────────────────────────
    const soonIO = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
          soonIO.unobserve(entry.target);
        }
      });
    }, { threshold: 0.2 });
    document.querySelectorAll('.soon-card').forEach((el) => soonIO.observe(el));
  }
})();
