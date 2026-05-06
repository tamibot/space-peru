// Coordina — landing logic.

(() => {
  // Partners carousel — populate logos dinámicamente
  const partnersTrack = document.getElementById('partners-track');
  if (partnersTrack) {
    // Solo venues alquilables (no bancos / retail). Intercalado por categoría.
    const logos = [
      ['wework', 'WeWork'],
      ['marriott', 'Marriott International'],
      ['larcomar', 'Larcomar'],
      ['maido', 'Maido'],
      ['pucp', 'PUCP'],
      ['casa-andina', 'Casa Andina'],
      ['icpna', 'ICPNA'],
      ['hilton', 'Hilton'],
      ['comunal', 'Comunal Coworking'],
      ['ulima', 'Universidad de Lima'],
      ['regatas', 'Club Regatas Lima'],
      ['westin', 'The Westin'],
      ['holiday-inn', 'Holiday Inn'],
      ['mall-plaza', 'Mall Plaza'],
      ['belmond', 'Belmond'],
      ['upc', 'UPC'],
      ['sheraton', 'Sheraton'],
      ['hotel-b', 'Hotel B'],
      ['four-seasons', 'Four Seasons'],
      ['hilton-garden', 'Hilton Garden Inn'],
      ['usil', 'USIL'],
      ['hyatt', 'Hyatt'],
      ['upacifico', 'Universidad del Pacífico'],
      ['aloft', 'Aloft'],
      ['wyndham', 'Wyndham'],
      ['esan', 'ESAN'],
      ['ihg', 'IHG Hotels'],
      ['utec', 'UTEC'],
      ['accor', 'Accor'],
      ['choice', 'Choice Hotels'],
      ['best-western', 'Best Western'],
      ['upn', 'UPN'],
      ['san-marcos', 'UNMSM'],
    ];
    const makeImg = (slug, alt, hidden = false) => {
      const img = document.createElement('img');
      img.className = 'partner-logo';
      img.src = `./brand/partners/${slug}.png`;
      img.alt = hidden ? '' : alt;
      if (hidden) img.setAttribute('aria-hidden', 'true');
      img.loading = 'lazy';
      return img;
    };
    logos.forEach(([slug, alt]) => partnersTrack.appendChild(makeImg(slug, alt)));
    // duplicar para loop infinito
    logos.forEach(([slug, alt]) => partnersTrack.appendChild(makeImg(slug, alt, true)));
  }

  // Smooth scroll
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

  // Categorías hover/click — cambia foto + label vertical + locación
  const list = document.getElementById('cat-list');
  const img = document.getElementById('cat-img');
  const frame = document.getElementById('cat-frame');
  const loc = document.getElementById('cat-loc');

  if (list && img && frame && loc) {
    const items = list.querySelectorAll('li');

    items.forEach((li) => {
      const url = li.dataset.img;
      if (url) { const i = new Image(); i.src = url; }
    });

    const setActive = (li) => {
      const url = li.dataset.img;
      const name = li.dataset.name;
      const place = li.dataset.loc || '';
      if (!url || !name) return;
      if (img.src === url) return;

      img.classList.add('fading');
      setTimeout(() => {
        img.src = url;
        img.alt = `${name} en ${place}`;
        frame.setAttribute('data-label', name);
        loc.textContent = place;
        requestAnimationFrame(() => img.classList.remove('fading'));
      }, 200);

      items.forEach((x) => x.classList.remove('active'));
      li.classList.add('active');
    };

    items.forEach((li) => {
      li.addEventListener('mouseenter', () => setActive(li));
      li.addEventListener('focus', () => setActive(li));
      li.addEventListener('click', () => setActive(li));
      li.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          setActive(li);
        }
      });
    });
  }

  // Nav transparente sobre hero photo, sólido al scrollear
  const nav = document.getElementById('nav');
  if (nav) {
    const onScroll = () => {
      if (window.scrollY > 80) nav.classList.remove('transparent');
      else nav.classList.add('transparent');
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // Reveal en viewport — generic
  if ('IntersectionObserver' in window) {
    const targets = document.querySelectorAll('.section-head, .made-cell, .ai-grid, .host-cta, .future-grid, .final-inner, .made-in-headline, .categories-head, .partners-grid, .testimonial');
    targets.forEach((el) => el.classList.add('reveal'));

    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    targets.forEach((el) => io.observe(el));

    // Why-items: trigger SVG line-draw cuando entra
    const whyIO = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          whyIO.unobserve(entry.target);
        }
      });
    }, { threshold: 0.3 });
    document.querySelectorAll('.why-item').forEach((el) => whyIO.observe(el));

    // AI section: trigger chat sequence cuando entra
    const aiSection = document.querySelector('.ai-section');
    if (aiSection) {
      const aiIO = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('in');
            aiIO.unobserve(entry.target);
          }
        });
      }, { threshold: 0.25 });
      aiIO.observe(aiSection);
    }
  }
})();
