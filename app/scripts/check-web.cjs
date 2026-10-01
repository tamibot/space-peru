// Run: node app/scripts/check-web.cjs
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const web = path.join(__dirname, '../web');
const source = fs.readFileSync(path.join(web, 'app.js'), 'utf8');
const fields = { fecha: {value: ''}, personas: {value: ''}, horas: {value: '', min: '4'} };
const events = {};
const form = { elements: { namedItem: name => fields[name] }, addEventListener: (name, fn) => events[name] = fn, reportValidity: () => true };
const link = { href: 'https://wa.me/?text=demo', addEventListener: () => {} };
const context = {
  URL, URLSearchParams, console,
  location: { search: '?date=2026-10-15&cap=30&hours=5', pathname: '/app/espacios/casa-verde-barranco.html', assign: url => context.destination = url },
  history: { replaceState: (_state, _title, url) => context.replaced = url },
  document: {
    body: { dataset: {} }, getElementById: () => null,
    querySelector: selector => selector.includes('script') ? {src: 'https://coordina.test/app/app.js'} : null,
    querySelectorAll: () => [],
  },
};
context.window = context;
vm.createContext(context);
vm.runInContext(source, context);
const spaces = JSON.parse(fs.readFileSync(path.join(web, 'spaces.json'))).spaces;
assert.equal(context.filterSpaces(spaces, new URLSearchParams('distrito=Barranco&cap=30')).length, 2);
assert.match(context.spaceCard(spaces[0]), /date=2026-10-15&amp;cap=30&amp;hours=5/);
assert.doesNotMatch(context.spaceCard(spaces[0]), /verified-chip|listing-card-rating/);
context.document.querySelector = selector => selector === '.pricing-form' ? form : selector.includes('h1') ? {textContent: 'Casa Verde'} : null;
context.document.querySelectorAll = selector => selector.includes('wa.me') ? [link] : [];
context.bindDetail();
assert.equal(fields.fecha.value, '2026-10-15');
assert.equal(fields.personas.value, '30');
assert.equal(fields.horas.value, '5');
fields.horas.value = '6';
events.input();
const message = new URL(link.href).searchParams.get('text');
assert.match(message, /Fecha: 2026-10-15/);
assert.match(message, /Personas: 30/);
assert.match(message, /Horas: 6/);
assert.equal(new URL(link.href).pathname, '/');
assert.match(context.replaced, /hours=6/);
context.spaNavigate('/app/buscar.html?cap=30');
assert.equal(context.destination, '/app/buscar.html?cap=30');
assert.doesNotMatch(source, /history\.pushState|addEventListener\('popstate'/);
context.malicious = '<img onerror="x">';
assert.equal(vm.runInContext('escapeHtml(malicious)', context), '&lt;img onerror=&quot;x&quot;&gt;');
for (const file of fs.readdirSync(path.join(web, 'espacios'))) {
  assert.doesNotMatch(fs.readFileSync(path.join(web, 'espacios', file), 'utf8'), /https:\/\/wa\.me\/\d/);
}

const generated = require('node:child_process').execFileSync('python3', ['-c', `import json, runpy
from pathlib import Path
g = runpy.run_path('scripts/build_app_pages.py')
d = json.loads(Path('data/public/spaces.json').read_text())
print(g['render_page'](d['spaces'][0], d['spaces']))`], { cwd: path.join(__dirname, '../..'), encoding: 'utf8' });
assert.doesNotMatch(generated, /https:\/\/wa\.me\/\d|junio 2026|Responde en 2 horas|listing-card-rating|Espacio verificado|reseñas/);
assert.match(generated, /class="catalog-demo"/);
assert.match(generated, /<link rel="icon" href="\/brand\/logo\/favicon\.svg"/);
const favicon = path.join(__dirname, '../../brand/logo/favicon.svg');
assert.ok(fs.statSync(favicon).isFile(), 'The published favicon source must exist.');
for (const file of fs.readdirSync(web, { recursive: true }).filter(file => file.endsWith('.html'))) {
  assert.match(fs.readFileSync(path.join(web, file), 'utf8'), /<link rel="icon" href="\/brand\/logo\/favicon\.svg"/, `Broken favicon route: ${file}`);
}

console.log('OK: filters, state, WhatsApp demo, native history, escaped query and favicon routes.');
