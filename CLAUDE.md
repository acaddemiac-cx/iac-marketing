# iac-marketing

Repositorio de marketing de IAC Latam (sitio: https://iaclatam.com, WordPress con Elementor y Yoast SEO, detrás de Cloudflare). El sitio tiene tres versiones por país: Colombia en la raíz, México en `/mx/` y Ecuador en `/ec/`.

Responde siempre en español.

## Proyecto SEO: trabajar tarea por tarea

El plan está en `seo/TAREAS.md` y el detalle de cada tarea en el documento del equipo (enlace al inicio de ese archivo). Cuando pidan "trabaja la tarea TNN":

1. Lee la tarea en `seo/TAREAS.md` y su detalle en el documento.
2. Comprueba en el sitio que el problema sigue ahí antes de cambiar nada.
3. Si tienes acceso de edición a WordPress, haz el cambio; si no, entrega el cambio exacto (página, campo y valor nuevo) para que el equipo lo aplique.
4. Verifica el resultado en el sitio con el criterio de la tarea.
5. Marca la tarea con `[x]` en `seo/TAREAS.md`, anota la fecha y qué se hizo, y avisa para que cambien el estado en el tablero del documento.

No borres ni redirijas páginas (T19, T21, T22) sin que el equipo apruebe la lista primero.

Para repetir la auditoría (T29), usa `seo/scripts/crawl.py` con las URLs de los sitemaps y compara con `seo/datos/urls-2026-11-23.csv`.

Skills disponibles en `.claude/skills/`: `find-skills`, `seo-audit` y `ai-seo`.
