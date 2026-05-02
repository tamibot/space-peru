// Coordina — landing logic.
// Landing explicativa, sin formularios funcionales por ahora.
// Los CTAs principales abren mailto: directos.
// Cuando exista el backend, reemplazar mailto por POST a la API.

// Smooth scroll mejorado para anchors (algunos browsers lo necesitan)
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
