# Plan de tareas SEO de iaclatam.com

Auditoría del 2026-11-23. El detalle completo de cada tarea (páginas exactas, pasos y cómo verificar) está en el documento del equipo, en la pestaña "Plan de tareas":
https://claude.ai/artifact/5H31hA3FMzgFLHM5wXZ3K4

Datos de apoyo en esta carpeta:
- `datos/urls-2026-11-23.csv`: las 790 URLs revisadas, con título, descripción, H1, palabras, imágenes sin alt y problemas de cada una.
- `datos/blog-2014-2019.csv`: los 53 artículos viejos, con una columna para anotar la acción decidida (T22).
- `scripts/`: el rastreador (`crawl.py`), el resumen (`analyze.py`) y la medición de velocidad (`perf.js`) usados en la auditoría, para repetirla (T29).

Marca cada tarea con `[x]` al terminarla y anota debajo la fecha y qué se hizo.

## Fase 1

- [ ] **T01** Agregar `Sitemap: https://iaclatam.com/sitemap_index.xml` a robots.txt.
- [ ] **T02** Marcar las 96 páginas de etiquetas `/tag/` como noindex (Yoast → Categorías y etiquetas → Etiquetas).
- [ ] **T03** noindex en `/gracias-solidworks/` e `/ig/`; 301 de `/taller-ia-2/` a `/taller-ia/`.
- [ ] **T04** Arreglar los enlaces internos rotos y los que redirigen (tabla en el documento):
  - `/agentes-de-ia/` → `/productos/inteligencia-artificial/` (4 artículos)
  - `/servicios/consultoria-automatizacion-de-procesos/` y `/automatizaciones/` → `/servicios/centro-de-automatizacion/`
  - `/agente-de-ia-prediccion-de-la-demanda/` → `/productos/prediccion-de-la-demanda/`
  - `/productos/solidworks-draftsigth/` → `/productos/solidworks-draftsight/`
  - `/productos/solidworks-simulacion/` → `/productos/solidworks-simulation/`
  - `/productos/bentley-projectwise/` → `/productos/projectwise-bundle/`
  - `/productos/ptc-windchill-2/` y `/productos/ptc-thingworxs-analytics/` → quitar o enlazar a `/que-es-plm/`
  - `info@ic.com.co` sin `mailto:` en `/cuales-son-los-beneficios-de-la-automatizacion-de-procesos/`
  - Enlace a clarin.com sin `https://` en `/el-bim-en-colombia/`
  - `/mx/escaneo-3d/` → `/mx/servicios/escaneo-3d/`; `/ec/escaneo-3d/` → `/ec/servicios/escaneo-3d/`; `/ec/soporte-tecnico-ia/` → `/soporte-tecnico-ia/`
- [ ] **T05** noindex en las 8 páginas que redirigen (`/mx/`, `/ec/`, `/servicios/`, `/productos/` y sus versiones por país) para sacarlas del sitemap.
- [ ] **T06** Cambiar los destinos `/mx/Inicio` y `/ec/Inicio` por `/mx/inicio/` y `/ec/inicio/`; `/ec/` directo a `/ec/inicio/`.
- [ ] **T07** `/productos/presto-presupuestos/` debe ir a `/productos/presto-presupuestos-y-mediciones/`, no a Ecuador.
- [ ] **T08** Desactivar los archivos por fecha en Yoast; revisar el nofollow de `/curso-revit-architecture/`.
- [ ] **T09** hreflang `es-CO`, `es-MX`, `es-EC` y `x-default` en las 43 páginas con versión en los tres países (ojo con los slugs distintos, tabla en el documento).
- [ ] **T10** `lang="es-MX"` en `/mx/` y `lang="es-EC"` en `/ec/`.
- [ ] **T12** Corregir "Asisitida" (Archicad ×3), "en Ecuador" en `/mx/productos/microsoft-365/` y "creo" en `/category/creo/`.
- [ ] **T27** Comprobar que `http://`, `http://www.` y `https://www.` redirigen con un solo 301.
- [ ] **T28** Search Console y Bing Webmaster Tools; exportar Rendimiento e Indexación a `seo/datos/`.

## Fase 2

- [ ] **T11** Contenido propio de cada país en productos y servicios.
- [ ] **T13** Títulos únicos por país en 11 grupos duplicados.
- [ ] **T14** Reescribir los títulos cortos o genéricos (formato: `Licencias [Producto] en [País] | Distribuidor oficial | IAC Latam`).
- [ ] **T15** Acortar a 60 caracteres los 63 títulos largos.
- [ ] **T16** Escribir las 47 meta descripciones que faltan (21 páginas, 25 categorías y la de autor).
- [ ] **T17** Diferenciar los 41 grupos de descripciones duplicadas y acortar las 15 largas.
- [ ] **T18** H1 en 38 páginas; un solo H1 en las 2 políticas de datos.
- [ ] **T19** Decidir qué hacer con cada página de evento pasado.
- [ ] **T21** Páginas reales de Servicios y Productos (6 URLs), deshaciendo T05.

## Fase 3

- [ ] **T20** Ampliar a unas 800 palabras las 9 categorías de producto escasas.
- [ ] **T22** Limpiar los 53 artículos de 2014–2019 (ver `datos/blog-2014-2019.csv`).
- [ ] **T23** Corregir 3 URLs con errores de escritura y dejar 301.
- [ ] **T24** Texto alt en 1.043 imágenes de 308 páginas.
- [ ] **T25** Comprimir imágenes y pasarlas a WebP.
- [ ] **T26** Caché de HTML en Cloudflare.
- [ ] **T29** Repetir la auditoría al cerrar cada fase.
