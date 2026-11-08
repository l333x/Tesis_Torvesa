---
titulo: Resumen para Víctor — la prueba de concepto en 1 página
version: v0.1
fecha: 2026-11-08
autor: Diego Bermeo
ia: Claude (Claude Code)
tarea: S5-T14 (intercambio de resúmenes, 15-nov)
base: "repos teamslash-api, teamslash-landing y teamslash-poc · 07_Flujos_Diseno/2026-11-14_Casos_Prueba_v0.1.md (anexo B)"
tags: [diego, resumen, prueba-de-concepto, sprint5]
---

# La prueba de concepto en 1 página

> [!summary] En tres frases
> 1. El camino completo del sistema **ya funciona en internet**, con datos ficticios: el cliente llena el formulario, el equipo recibe el aviso en Slack, la solicitud aparece en la bóveda y el asistente propone un borrador de cotización.
> 2. El borrador del asistente **no pone precios ni se envía solo**. Queda marcado como «Borrador» hasta que una persona lo revisa, y al asistente nunca le llegan nombres, teléfonos ni correos.
> 3. Cada cambio de una solicitud queda en un **registro con huellas** que delata si alguien lo altera: la prueba detectó **3 de 3 alteraciones** (M5).

> [!warning] Todo es de prueba
> Las solicitudes, los clientes y las cotizaciones son **ficticios**. Torvesa todavía no usa el sistema.

## El recorrido de una solicitud

| Paso | Qué pasa | Dónde | Meta o requisito |
|---|---|---|---|
| 1 | El cliente llena el formulario y **marca la casilla de consentimiento**; sin ella no se envía | Página web (Vercel) | RQ-01, RQ-18 |
| 2 | La solicitud se guarda con su hora de llegada y el equipo recibe una tarjeta en **Slack** | Servidor TEAMSLASH (Railway) | M1, RQ-02 |
| 3 | Alguien pulsa **«Tomar»**: queda como responsable y se guarda la **hora del primer contacto** | Slack → servidor | M1, RQ-04, RQ-24 |
| 4 | La solicitud y la ficha del cliente aparecen en la **bóveda de Obsidian**; los datos personales van aparte | Bóveda | M4, RQ-09 |
| 5 | El asistente arma un **borrador de cotización** con la plantilla del tipo de obra, sin precios y diciendo qué documentos usó | Bóveda + Claude Sonnet 5.5 | M2, RQ-11 |
| 6 | Una persona **revisa** y completa el borrador antes de enviarlo | Bóveda | RQ-12 |
| — | Cada paso queda en el **registro con huellas**, sin datos personales | Servidor | M5, RQ-15 a RQ-17 |

**Primera prueba (8-nov):** una solicitud ficticia de una cocina de 12 m². El asistente tardó **15 segundos**. Dejó los precios vacíos, propuso los 12 m² de piso como cantidad estimada e hizo 11 preguntas para completar la cotización. El teléfono que el «cliente» había escrito en la descripción no llegó al asistente.

## Qué falta antes de la validación (23–24 de noviembre)

- **Funciones** (sprint 6):
  - el recordatorio a los 15 minutos sin contacto, con aviso a la gerencia (RQ-06);
  - el motivo de pérdida obligatorio (RQ-07);
  - el estado «Cotizada» (RQ-05);
  - el reporte de cada lunes (RQ-08).
- **Datos de Torvesa** para el aviso de privacidad: RUC, correo de contacto y plazo de conservación.
- **Que Torvesa autorice** que su equipo use el sistema durante las dos semanas de validación. Sin eso no hay validación ni línea base. **Es la ruta crítica.**

## Lo que esto le da a tu parte (finanzas y viabilidad)

- **Servicios que usa hoy:**
  - Railway (servidor y base de datos);
  - Vercel (página web);
  - Slack (avisos);
  - Obsidian (bóveda);
  - Claude (asistente).

  Para el CAPEX y el OPEX hay que sacar sus precios de las páginas oficiales, con fecha de consulta. Aquí no van cifras.
- **Para estimar beneficios**, el tiempo que ahorra el asistente sale de CP-01. Hasta que se ejecute (S8-04) es un supuesto, no un dato.

## Enlaces para verlo

| Qué | Enlace | Quién puede entrar |
|---|---|---|
| Página web con el formulario | https://teamslash-torvesa.vercel.app | Cualquiera |
| Aviso de privacidad (borrador v0.1) | https://teamslash-torvesa.vercel.app/aviso-privacidad.html | Cualquiera |
| Estado del servidor (debe decir `"status":"ok"`) | https://teamslash-api-production-772d.up.railway.app/health | Cualquiera |
| Código del servidor | https://github.com/psiceslivie/teamslash-api (rama `rq18-consentimiento`) | Repo privado: Diego da acceso |
| Código de la página web | https://github.com/psiceslivie/teamslash-landing | Repo privado: Diego da acceso |
| Prueba de concepto (sincronización, bóveda y asistente) | https://github.com/psiceslivie/teamslash-poc | Repo privado: Diego da acceso |
| Avisos, botones y reporte de los lunes | Canal de Slack del espacio «Constructora Torvesa» | Por invitación al espacio |

- **Para probarlo:** se llena el formulario con datos inventados y se marca la casilla. A los segundos llega la tarjeta al canal de Slack.
- **Lo que no se abre en el navegador:** el listado de solicitudes, el registro de eventos y el reporte semanal piden la clave de la API, que no va en este repositorio. Para verlos, se le piden a Diego o se miran en Slack.
