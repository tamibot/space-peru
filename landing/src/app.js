// Coordina — landing logic.

(() => {
  // Hero search — typeahead/autocomplete para "Para qué"
  const actInput = document.getElementById('hs-act');
  const actList = document.getElementById('hs-act-list');
  if (actInput && actList) {
    const suggestions = [
      'Aniversario', 'Animación infantil', 'Asamblea', 'Auditorio',
      'Baby shower', 'Bautizo', 'Boda', 'Boda civil',
      'Brunch', 'Capacitación corporativa',
      'Casa íntima', 'Catación', 'Cena corporativa', 'Cena privada',
      'Charla', 'Clase grupal', 'Cocktail', 'Conferencia',
      'Conversatorio', 'Coworking por horas', 'Cumpleaños',
      'Demo de producto', 'Despedida', 'Estudio fotográfico',
      'Estudio para video', 'Evento corporativo', 'Exposición',
      'Fiesta privada', 'Filmación', 'Graduación',
      'Junta directiva', 'Lanzamiento de producto', 'Meet and greet',
      'Networking', 'Pop-up store', 'Presentación',
      'Quinceañera', 'Reunión de empresa', 'Sala de reuniones',
      'Seminario', 'Sesión de fotos', 'Showroom', 'Taller',
      'Team building', 'Terraza con vista', 'Workshop', 'Yoga'
    ];

    let activeIndex = -1;
    let currentMatches = [];

    const closeList = () => {
      actList.hidden = true;
      actInput.setAttribute('aria-expanded', 'false');
      activeIndex = -1;
    };

    const renderList = (matches) => {
      currentMatches = matches;
      if (matches.length === 0) { closeList(); return; }
      actList.innerHTML = matches.map((m, i) =>
        `<li role="option" data-i="${i}" class="${i === activeIndex ? 'active' : ''}">${m}</li>`
      ).join('');
      actList.hidden = false;
      actInput.setAttribute('aria-expanded', 'true');
    };

    const filter = (q) => {
      const norm = (s) => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
      const nq = norm(q.trim());
      if (!nq) return suggestions.slice(0, 8); // top 8 al focus
      // priorizar matches al inicio del string
      const starts = [], contains = [];
      suggestions.forEach((s) => {
        const ns = norm(s);
        if (ns.startsWith(nq)) starts.push(s);
        else if (ns.includes(nq)) contains.push(s);
      });
      return [...starts, ...contains].slice(0, 8);
    };

    actInput.addEventListener('focus', () => {
      activeIndex = -1;
      renderList(filter(actInput.value));
    });

    actInput.addEventListener('input', () => {
      activeIndex = -1;
      renderList(filter(actInput.value));
    });

    actInput.addEventListener('keydown', (e) => {
      if (actList.hidden && (e.key === 'ArrowDown' || e.key === 'ArrowUp')) {
        renderList(filter(actInput.value));
        return;
      }
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        activeIndex = Math.min(activeIndex + 1, currentMatches.length - 1);
        renderList(currentMatches);
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        activeIndex = Math.max(activeIndex - 1, 0);
        renderList(currentMatches);
      } else if (e.key === 'Enter') {
        if (activeIndex >= 0 && currentMatches[activeIndex]) {
          e.preventDefault();
          actInput.value = currentMatches[activeIndex];
          closeList();
        }
      } else if (e.key === 'Escape') {
        closeList();
      }
    });

    actList.addEventListener('mousedown', (e) => {
      const li = e.target.closest('li');
      if (!li) return;
      e.preventDefault();
      actInput.value = li.textContent;
      closeList();
      actInput.focus();
    });

    actInput.addEventListener('blur', () => {
      // delay para permitir mousedown en option
      setTimeout(closeList, 120);
    });
  }

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
