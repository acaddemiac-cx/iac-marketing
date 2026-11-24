# Plan de tareas SEO de iaclatam.com

Auditoría del 2026-11-23. El detalle completo de cada tarea (páginas exactas, pasos y cómo verificar) está en el documento del equipo, en la pestaña "Plan de tareas":
https://claude.ai/artifact/5H31hA3FMzgFLHM5wXZ3K4

Datos de apoyo en esta carpeta:
- `datos/urls-2026-11-23.csv`: las 790 URLs revisadas, con título, descripción, H1, palabras, imágenes sin alt y problemas de cada una.
- `datos/urls-control.csv`: las mismas URLs en la auditoría de control, con hreflang y lang.
- `datos/blog-2014-2019.csv`: los 53 artículos viejos, con una columna para anotar la acción decidida (T22).
- `scripts/`: el rastreador (`crawl.py`), el resumen (`analyze.py`), la comparación tarea por tarea (`compare.py`) y la medición de velocidad (`perf.js`), para repetir la auditoría (T29).

Marca cada tarea con `[x]` al terminarla y anota debajo la fecha y qué se hizo.

## Fase 1

- [x] **T01** Agregar `Sitemap: https://iaclatam.com/sitemap_index.xml` a robots.txt.
  - Verificado 2026-11-23 (auditoría de control): robots.txt ya incluye la línea Sitemap.
- [x] **T02** Marcar las 96 páginas de etiquetas `/tag/` como noindex (Yoast → Categorías y etiquetas → Etiquetas).
  - Verificado 2026-11-23 (auditoría de control): 0 etiquetas indexables; post_tag-sitemap.xml ya no existe.
- [x] **T03** noindex en `/gracias-solidworks/` e `/ig/`; 301 de `/taller-ia-2/` a `/taller-ia/`.
  - Verificado 2026-11-23 (auditoría de control): /gracias-solidworks/ e /ig/ con noindex; /taller-ia-2/ redirige a /taller-ia/.
- [x] **T04** Arreglar los enlaces internos rotos y los que redirigen (tabla en el documento):
  - Verificado 2026-11-23 (auditoría de control): 0 enlaces internos a 404. Quedan 2 enlaces que redirigen, ver T31.
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
- [x] **T05** noindex en las 8 páginas que redirigen (`/mx/`, `/ec/`, `/servicios/`, `/productos/` y sus versiones por país) para sacarlas del sitemap.
  - Verificado 2026-11-23 (auditoría de control): Ninguna de las 8 URLs sigue en el sitemap.
- [x] **T06** Cambiar los destinos `/mx/Inicio` y `/ec/Inicio` por `/mx/inicio/` y `/ec/inicio/`; `/ec/` directo a `/ec/inicio/`.
  - Verificado 2026-11-23 (auditoría de control): Todas llegan en un solo salto.
- [x] **T07** `/productos/presto-presupuestos/` debe ir a `/productos/presto-presupuestos-y-mediciones/`, no a Ecuador.
  - Verificado 2026-11-23 (auditoría de control): Redirige a /productos/presto-presupuestos-y-mediciones/.
- [x] **T08** Desactivar los archivos por fecha en Yoast; revisar el nofollow de `/curso-revit-architecture/`.
  - Verificado 2026-11-23 (auditoría de control): Los archivos por fecha redirigen a la portada; ya no hay nofollow.
- [x] **T09** hreflang `es-CO`, `es-MX`, `es-EC` y `x-default` en las 43 páginas con versión en los tres países (ojo con los slugs distintos, tabla en el documento).
  - Verificado 2026-11-23 (auditoría de control): 152 páginas con hreflang es-CO/es-MX/es-EC/x-default, todas con autorreferencia, retorno y destinos 200.
- [x] **T10** `lang="es-MX"` en `/mx/` y `lang="es-EC"` en `/ec/`.
  - Verificado 2026-11-23 (auditoría de control): /mx/ declara es-MX y /ec/ declara es-EC.
- [x] **T12** Corregir "Asisitida" (Archicad ×3), "en Ecuador" en `/mx/productos/microsoft-365/` y "creo" en `/category/creo/`.
  - Verificado 2026-11-23 (auditoría de control): Sin "Asisitida"; /mx/productos/microsoft-365/ ya dice México.
- [ ] **T27** Comprobar que `http://`, `http://www.` y `https://www.` redirigen con un solo 301.
- [ ] **T28** Search Console y Bing Webmaster Tools; exportar Rendimiento e Indexación a `seo/datos/`.
  - Control 2026-11-24: Google Search Console listo según el equipo; Bing Webmaster Tools en espera (unos 2 días). Pendiente: subir los CSV de Rendimiento e Indexación a seo/datos/.

## Fase 2

- [ ] **T11** Contenido propio de cada país en productos y servicios.
- [x] **T13** Títulos únicos por país en 11 grupos duplicados.
  - Verificado 2026-11-23 (auditoría de control): 0 títulos duplicados entre páginas indexables.
- [x] **T14** Reescribir los títulos cortos o genéricos (formato: `Licencias [Producto] en [País] | Distribuidor oficial | IAC Latam`).
  - En curso, auditoría de control 2026-11-23: Quedan 26 (categorías, eventos y artículos viejos).
  - Verificado 2026-11-24: 0 títulos de menos de 30 caracteres; categorías con la plantilla "Artículos sobre … | Blog IAC Latam".
- [x] **T15** Acortar a 60 caracteres los 63 títulos largos.
  - En curso, auditoría de control 2026-11-23: Quedan 51 de 63.
  - Verificado 2026-11-24: solo quedan 3 títulos largos y son páginas 2+ de categorías (normal).
- [x] **T16** Escribir las 47 meta descripciones que faltan (21 páginas, 25 categorías y la de autor).
  - En curso, auditoría de control 2026-11-23: Quedan 4: /compra-una-licencia-de-creo-y-obten-una-segunda-a-mitad-de-precio/, /curso-revit-architecture-basico/, /estaremos-presentes-en-la-feria-de-expoconstruccion-y-diseno-2019/, /innovation-day-bentley/.
  - Control 2026-11-24: quedan 2: /innovation-day-bentley/ y /estaremos-presentes-en-la-feria-de-expoconstruccion-y-diseno-2019/.
  - Verificado 2026-11-24: todas las páginas indexables tienen meta descripción.
- [x] **T17** Diferenciar los 41 grupos de descripciones duplicadas y acortar las 15 largas.
  - En curso, auditoría de control 2026-11-23: 0 duplicadas entre páginas distintas (las 9 que quedan son páginas 2+ de categorías, es normal). Queda 1 larga: /power-bi-2026-copilot-ia-actualizaciones-guia/.
  - Verificado 2026-11-24: sin descripciones duplicadas entre páginas distintas ni descripciones largas; solo se repiten en páginas 2+ de categorías (normal).
- [ ] **T18** H1 en 38 páginas; un solo H1 en las 2 políticas de datos.
  - En curso, auditoría de control 2026-11-23: Quedan 13 sin H1: /contacto/, /ec/contacto/, /blogs/ y 10 páginas de eventos. Ya no hay páginas con dos H1.
  - Control 2026-11-24: quedan 5 sin H1: /blogs/, /congreso-inteligencia-artificial/, /cata-de-vinos-solidworks-2026/, /live-projectwise-bundle/, /live-synchro-y-primavera/. En /live-conversatorio/ el H1 dice "LIVE BIM" aunque el evento es de OpenFlows.
  - Control 2026-11-24: solo queda /blogs/: la página no tiene ningún encabezado visible (solo el listado de artículos); hay que añadir un widget de encabezado H1.
  - Control 2026-11-24: /blogs/ sigue sin H1 en el sitio (2026-11-24): el texto "Blog de IAC Latam" está solo en el título SEO y la descripción, no como encabezado visible.
- [ ] **T19** Decidir qué hacer con cada página de evento pasado.
- [ ] **T21** Páginas reales de Servicios y Productos (6 URLs), deshaciendo T05.

## Fase 3

- [ ] **T20** Ampliar a unas 800 palabras las 9 categorías de producto escasas.
- [x] **T22** Limpiar los 53 artículos de 2014–2019 (ver `datos/blog-2014-2019.csv`).
  - Verificado 2026-11-24: los 53 artículos redirigen con 301 a /blogs/.
- [x] **T23** Corregir 3 URLs con errores de escritura y dejar 301.
  - Verificado 2026-11-24: las 3 URLs nuevas responden 200, las viejas redirigen con 301 y no quedan enlaces internos a las viejas.
- [x] **T24** Texto alt en 1.043 imágenes de 308 páginas.
  - En curso, auditoría de control 2026-11-23: Quedan 961 imágenes sin alt (antes 1.043).
  - Control 2026-11-24: quedan 115 imágenes distintas sin alt (antes 334): 56 son íconos decorativos (correcto dejarlas vacías) y 59 son imágenes dentro de artículos del blog que guardan su propio alt en el artículo, más 2 de /innovation-day-bentley/.
  - Verificado 2026-11-24: 0 imágenes de contenido sin alt; quedan vacías solo 56 íconos decorativos (correcto).
- [ ] **T25** Comprimir imágenes y pasarlas a WebP.
- [ ] **T26** Caché de HTML en Cloudflare.
- [ ] **T29** Repetir la auditoría al cerrar cada fase.

## Hallazgos de la auditoría de control (2026-11-23)

- [x] **T30** Tres artículos tienen la etiqueta canónica apuntando al dominio antiguo `iac.com.co`, así que Google no los indexa como de iaclatam.com: `/conozca-lo-nuevo-de-la-suscripcion-autocad/`, `/iac-presente-en-el-congreso-mundial-de-iot/` y `/quieres-adquirir-3-asientos-de-creo-essentials-por-el-pecio-de-2/`. Tampoco están en el sitemap. Decidir junto con T22: corregir la canónica en Yoast (campo "URL canónica") o redirigirlos.
  - Verificado 2026-11-24: los 3 artículos redirigen con 301 a la portada.
- [x] **T31** Dos enlaces internos todavía pasan por una redirección: `/inteligencia-artificial/` (en 3 artículos de agentes de IA; cambiar por `/productos/inteligencia-artificial/`) y `/author/iac/` (lo pone el tema en las categorías; quitar el enlace al autor o apuntarlo a `/nosotros/`).
  - Verificado 2026-11-24: los enlaces apuntan a /productos/inteligencia-artificial/ y las categorías ya no enlazan al autor.
