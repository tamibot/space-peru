// Ejecutar: node landing/src/check.mjs. Sin dependencias.
import assert from 'node:assert/strict';
import { readFileSync, existsSync } from 'node:fs';
import { runInNewContext } from 'node:vm';

const html = readFileSync(new URL('./index.html', import.meta.url), 'utf8');
const ids = new Set([...html.matchAll(/\bid="([^"]+)"/g)].map(match => match[1]));
for (const [, href] of html.matchAll(/\bhref="([^"]+)"/g)) {
  if (href.startsWith('#')) assert(ids.has(href.slice(1)), `Ancla ausente: ${href}`);
  if (href.startsWith('./app/')) {
    const path = href.split('?')[0].replace('./app/', '../../app/web/');
    assert(existsSync(new URL(path, import.meta.url)), `Página ausente: ${href}`);
  }
}
const form = html.match(/<form\b[\s\S]*?<\/form>/)[0];
assert(form.includes('action="./app/buscar.html"'));
for (const name of ['caso', 'distrito', 'date', 'cap']) assert(form.includes(`name="${name}"`), `Filtro ausente: ${name}`);
assert(!form.includes('name="actividad"'), 'El catálogo no filtra por actividad');
assert(!html.includes('app/asistente.html'), 'El original no tiene esa página');
assert(html.includes('Catálogo demo.'));

const details = { open: true };
let onClick;
runInNewContext(readFileSync(new URL('./app.js', import.meta.url), 'utf8'), {
  document: { querySelectorAll: () => [{ addEventListener: (event, handler) => { assert.equal(event, 'click'); onClick = handler; }, closest: () => details }] },
});
onClick();
assert.equal(details.open, false, 'El menú debe cerrarse al navegar');
console.log('OK: rutas, anclas, filtros y cierre del menú.');
