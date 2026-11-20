# Landing Rocketbot por IAC: marcadores pendientes

Abre la página con `?revision` al final de la URL (por ejemplo `index.html?revision`) para ver resaltado en rojo cada elemento pendiente. En el código, cada uno lleva un comentario `<!-- [MARCADOR] -->` y el atributo `data-tbc`.

## Logos y activos de marca

| Marcador | Dónde | Qué falta |
|---|---|---|
| `[LOGO IAC SVG]` | Menú y footer | Hoy es un logotipo tipográfico provisional (IAC + triángulo ámbar). |
| `[LOGO ROCKETBOT]` | Menú | Hoy es texto. Usar el logo en monocromo blanco. |
| `[LOGO OFICIAL]` Protección | Casos de éxito | Cambiar el nombre por `<img>`. Requiere autorización del cliente. |
| `[LOGO OFICIAL]` Aciturri | Casos de éxito | Ídem. |
| `[LOGO OFICIAL]` Hospital Pablo Tobón Uribe | Casos de éxito | Ídem. |
| Clientes no nombrados | Casos de éxito | Conciliación bancaria, retail y e-commerce llevan un ícono de sector y el rótulo "Cliente confidencial", porque Rocketbot no publica sus nombres. |
| `[SI APLICAN]` sellos de certificación | Footer (oculto) | |

## [CONFIRMAR]

| Marcador | Dónde | Qué falta |
|---|---|---|
| `[CONFIRMAR CON ROCKETBOT]` | Preguntas · "¿Es seguro?" | Hosting, cifrado, opción on-premise y certificaciones. |
| `[CONFIRMAR CON EL EQUIPO TÉCNICO]` | Preguntas · "¿Cuánto tarda el primer robot?" | Rango de plazo. |
| `[CONFIRMAR ALCANCE]` | Preguntas · UiPath, Automation Anywhere y Power Automate | Que el Orchestrator coordine procesos de esas plataformas. |
| `[CONFIRMAR CONDICIONES]` | Preguntas · Empresa mediana | Planes para la mediana empresa. |
| `[CONFIRMAR]` URL canónica | `<head>` | `https://iaclatam.com/servicios/rocketbot/` |
| `[CONFIRMAR]` política de datos | Formulario | URL de la política de tratamiento de datos (Ley 1581 de 2012). |
| "Modelo operativo AAO" | Metodología · Estrategia | Texto entregado por IAC. Confirmar que la sigla se entiende o explicarla. |

## [VERIFICAR VIGENCIA]

- Franja de cifras: 4,7/5 en Gartner Peer Insights (137 reseñas, oct. 2025).
- Casos de éxito: Aciturri, 17.000 h/año (Forbes Perú, 2022).

## [PENDIENTE]

| Marcador | Dónde | Qué falta |
|---|---|---|
| Endpoint del formulario / CRM | `<form id="lead" data-endpoint="">` | Sin endpoint, el envío abre un correo prellenado a info@iaclatam.com. |
| ID de GA4 | `<head>`, snippet comentado | Eventos ya conectados: `cta_hero_click`, `industria_tab`, `calculadora_uso`, `form_start`, `form_submit`, `whatsapp_click`, `scroll_75`, `demo_repetir`. |
| ID del píxel de Meta | `<head>`, snippet comentado | Eventos `ViewContent` y `Lead` ya conectados. |
| og:image | `<head>` | Imagen 1200×630 con marca IAC. |

## Datos ilustrativos (rotulados en la página)

- Hero: tareas de los robots y "1.284 horas devueltas" ("Simulación" / "Dato ilustrativo").
- Bloque 1: simulación de 40 facturas: a mano termina hacia las 12:00 y con un robot a las 08:20 ("Ejemplo ilustrativo").
- Bloque 3: visuales de cada capacidad ("Visuales ilustrativos").
- Bloque 4: escenas y tareas por industria ("Simulación").
- Calculadora: valores iniciales (COP 35.000 · USD 9 · MXN 170 por hora, 48 semanas).

## Escala tipográfica

Plus Jakarta Sans para todo el texto y JetBrains Mono para los datos.

| Elemento | Tamaño |
|---|---|
| Título de bloque (H3) | 33 px (26 px en móvil) |
| Frase SEO sobre el título (H2) | 13 px |
| Títulos secundarios (H4) | 17 px |
| Texto interno | 14 px |
| H1 del hero | 46 px (3 líneas en escritorio) |
