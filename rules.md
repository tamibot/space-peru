# rules.md — Reglas operativas del proyecto

Estas reglas las sigue Claude Code en cada sesión. Cualquier desviación requiere instrucción explícita del owner.

## 1. Background-first
- Tareas que tomen >1 minuto se delegan a sub-agentes en **background**.
- El hilo principal no debe quedarse esperando builds, scrapings ni research largo.

## 2. No tocar el navegador del usuario
- Para web automation usar **Chromium headless**, **Chrome MCP** o **WebFetch / WebSearch**.
- Nunca abrir ventanas en el Chrome/Safari del usuario para tareas automatizadas.

## 3. Recursos locales mínimos
- Preferir integraciones (APIs, MCPs, servicios cloud) antes que procesar local.
- DB en Railway, hosting en GitHub Pages, no levantar servidores locales salvo desarrollo activo.

## 4. Secretos y credenciales
- TODO secreto vive en `credentials.env` (gitignored).
- `.env.example` se mantiene actualizado con las claves vacías.
- Nunca pegar secretos en commits, issues, PRs, ni docs.
- Si un secreto se filtra: rotar inmediatamente y documentar en `documentation/incidents.md`.

## 5. Estructura por dominio
- Cada iniciativa nueva (research, landing, app, social, etc.) tiene su carpeta dedicada.
- Dentro de cada carpeta, un `README.md` que explique qué hay y cómo se usa.

## 6. Idiomas
- Producto y copy: **español Perú**.
- Código y nombres de archivo: **inglés**.
- Documentación interna: **español**.
- Commits: inglés, conventional commits.

## 7. Branding (no negociable salvo cambio explícito)
- Color principal: **azul**.
- Estilo: **minimalista, limpio, alto contraste, mucho espacio en blanco**.
- Mobile-first siempre.
- Diferenciación vs Space-Pal: más intuitivo, menos densidad visual.

## 8. Git
- Branch base: `main`.
- Conventional commits.
- Commits atómicos y frecuentes.
- Nunca `git push --force` a `main`.

## 9. Datos y privacidad
- No exponer información personal de usuarios en logs ni en el repo.
- Datasets sensibles → `data/private/` (gitignored).
- Datasets públicos / fixtures → `data/public/`.

## 10. Decisiones reversibles vs no reversibles
- Reversibles (editar archivos, refactor, cambiar copy): proceder.
- No reversibles (eliminar tablas, cambiar permisos GitHub, publicar contenido en redes, deploy a producción que afecte usuarios): **confirmar con owner antes**.

## 11. Tono de Claude en este repo
- Respuestas cortas, accionables, sin relleno.
- No ofrecer scheduling de automatizaciones (instrucción explícita del owner).
- Reportar lo hecho, lo siguiente, y los bloqueos. Nada más.
