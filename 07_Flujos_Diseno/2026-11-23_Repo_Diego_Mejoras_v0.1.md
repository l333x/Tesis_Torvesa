---
titulo: Mejoras de bajo riesgo en el repositorio de Diego (teamslash-api) y tareas pendientes
version: v0.1
fecha: 2026-11-22
autor: Claude (Claude Code), a pedido de Víctor
ia: Claude (Claude Code)
estado: Pull Request en borrador; lo revisa y decide Diego
base: "psiceslivie/teamslash-api, rama rq18-consentimiento (8c6a406) · teamslash-landing main (7aade8f) · [[2026-11-17_Revision_Codigo_Limpio_v0.1]] · IA_DIEGO §8"
pr: https://github.com/psiceslivie/teamslash-api/pull/1
tags: [diego, codigo-limpio, seguridad, prueba-de-concepto, pull-request]
---

# Mejoras de bajo riesgo en el repositorio de Diego

> [!summary] En tres frases
> 1. Se abrió el **Pull Request en borrador #1** (https://github.com/psiceslivie/teamslash-api/pull/1) desde la rama `mejoras-revision-22nov` hacia `rq18-consentimiento`. Tiene 4 commits: DT-01, DT-03, atajos marcados y documentos para la IA de Diego.
> 2. Pruebas: **5 de 5 suites** pasaban antes; **6 de 6** pasan después. La suite nueva (`aviso`) demuestra que el formulario responde en unos 60 ms aunque Slack no conteste. Con el código anterior la misma prueba tardaba 4.068 ms y fallaba.
> 3. No hay secretos reales en el historial de la API. Sí hay **claves antiguas de la API en el historial de la landing** (hay que confirmar en Railway que la privada actual es otra), y hay **4 problemas de seguridad comprobados con un caso**: sin límite de peticiones, sin esquema ni largo máximo, texto del cliente sin escapar en Slack y Telegram abierto por defecto.

## 1. Estado del repositorio (22-nov)

| Repo | Ramas | Situación |
|---|---|---|
| `teamslash-api` | `main` (c3ca2b9, 23-jul), `rq18-consentimiento` (8c6a406, 15-nov) y ahora `mejoras-revision-22nov` | `rq18-consentimiento` está **5 commits por delante** de `main`, y `main` no tiene nada propio. Por eso la rama nueva sale de `rq18-consentimiento` y el PR va hacia ella. No había PR abiertos. El código está en la subcarpeta `teamslash-api/` (Node.js ≥ 18, Express, `pg`, `pg-mem` para pruebas). No hay carpeta `.github` (sin CI). |
| `teamslash-landing` | `main` (7aade8f, 15-nov) y `rq18-consentimiento` (7a948a6, atrás de `main`) | HTML/CSS/JS estático en `landing torvesa/`. No se cambió nada. |

- **Despliegue:** no se pudo ver desde el código qué rama despliega Railway. Como producción ya tiene las claves separadas del 15-nov, lo más probable es que sea `rq18-consentimiento`. En ese caso, el merge del PR hace deploy. Diego lo confirma.
- **Clones de trabajo** (temporales): `C:\Users\vasha\AppData\Local\Temp\claude\9c980eed3ad3d1c7\1557e702-6bd9-4a4d-a59c-5a4af61db2f7\scratchpad\repos_diego\`.

## 2. Pruebas antes y después

| Momento | Orden | Resultado |
|---|---|---|
| Antes (8c6a406) | `npm ci` + `npm test`, con un entorno vacío, sin `.env` ni credenciales | **5 de 5** en verde: `smoke`, `claves`, `telegram`, `eventos` (M5: 3 de 3 alteraciones detectadas) y `funciones` (RQ-05 a RQ-08) |
| Prueba nueva con el `leads.js` anterior | `node test/aviso.smoke.js` | **Falla**: la respuesta tardó 4.068 ms. Esperaba al aviso, y sin el límite nuevo habría esperado sin fin. |
| Después (d436fc8) | `npm test` | **6 de 6** en verde. La nueva `aviso` responde en unos 60 ms, el aviso se corta a los 4.000 ms y el log no lleva datos personales. |

- Única advertencia, que ya existía: `pg-mem` no tiene `plpgsql`, así que en las pruebas la tabla de eventos queda modificable a propósito.
- No se usó ninguna credencial real ni se llamó a Railway, Slack o Telegram. El Slack de la prueba es un servidor falso en `127.0.0.1`.

## 3. Qué se implementó (commits en `mejoras-revision-22nov`)

| Commit | Qué hace | Cambia el comportamiento |
|---|---|---|
| `d990b63` DT-01 | `POST /api/leads` responde 201 apenas se guarda la solicitud y manda los avisos después, sin `await`. El módulo nuevo `src/services/limite.js` aplica `AbortSignal.timeout(4000)` a **todos** los `fetch` externos (Slack, Discord, Telegram, Teams). El log dice el código y «sin respuesta en 4000 ms». Se corrigió el comentario engañoso, se agregó `test/aviso.smoke.js` a `npm test` y una nota en el README. | Sí: la respuesta ya no espera los avisos (RQ-01/RQ-02). |
| `3ae69d4` DT-03 | Quita `escapeHtml` de `notify.js`, que no se usaba. | No. |
| `5e3c42c` Atajos | 12 comentarios `// atajo:` (con el de `limite.js` son 13): intervalo de 60 s, cola en memoria, recordatorio de 24 h, UTC-5 fijo, lista de estados copiada, `/leads` con 15, Telegram abierto sin lista o sin secreto, clave privada como respaldo, SSL sin `DATABASE_CA`, `listarLeads` sin paginar y motivos provisionales. | No (solo comentarios). |
| `d436fc8` Documentos | `AGENTS.md` (contexto, cómo probar, 10 reglas, §8.1, §8.2, §8.3 y Strix §8.5 solo en local, con `STRIX_TELEMETRY=0`, `--max-budget 5` y versión fija por `pipx`), `CLAUDE.md` («Lee AGENTS.md») y `docs/TAREAS_DIEGO.md`. | No. |

- **Pull Request:** https://github.com/psiceslivie/teamslash-api/pull/1 (borrador, base `rq18-consentimiento`). Sin merge, sin borrar ramas y sin force push.
- **Efecto a vigilar:** `enviarTexto` (recordatorio y reporte de los lunes) también se corta a los 4 s. Si Slack tardara más pero igual publicara, el reporte podría repetirse al minuto siguiente. Quedó anotado en el PR.
- **Lo que no se hizo, por indicación:** RF-01/RF-02 (migran datos), dependencias, variables, despliegue, CI y la landing.

## 4. Hallazgos de seguridad (sin valores de secretos)

Formato de IA_DIEGO §8.2. El detalle de cada uno, con las 4 partes, está en `docs/TAREAS_DIEGO.md` del repositorio.

**Debe arreglarse**
1. **Claves antiguas en el historial de `teamslash-landing`.** En `landing torvesa/js/main.js` de los commits `4dc05a2` y `d31227b` (julio) y `7a948a6` (8-nov) quedaron claves anteriores de la API. Hasta el 15-nov esas claves podían leer y cambiar solicitudes. Hay que confirmar en Railway que `TEAMSLASH_API_KEY` (la privada) es nueva y distinta de todas; si no, **rotarla**. La clave pública actual está en el navegador a propósito y solo crea solicitudes.
2. **Sin límite de peticiones.** Con la clave pública, que se ve en el navegador, se puede inundar la base y el canal de Slack.
3. **Sin esquema ni largo máximo.** Caso comprobado: con `servicio: "cualquier-cosa-inventada"` y una descripción de 50.000 caracteres, la validación no devuelve ningún error. Slack rechaza secciones de más de 3.000 caracteres, así que esa tarjeta no llega.
4. **Texto del cliente sin escapar en la tarjeta de Slack (`mrkdwn`).** Caso comprobado: con la descripción `<!channel> <https://malo.example|Ver ficha>` se avisa a todo el canal y aparece un enlace disfrazado.
5. **Telegram abierto por defecto.** Sin `TELEGRAM_WEBHOOK_SECRET` el webhook acepta cualquier petición, y sin lista de chats cualquier chat opera el CRM. Además, el secreto se compara con `!==`.

**Conviene**
6. **Errores con detalle técnico.** Caso comprobado: el cuerpo `{mal`, incluso sin clave, devuelve 400 con el mensaje interno del parser de JSON.
7. **PD-01 sigue igual.** Slack, Telegram, Discord, Teams y **Google Calendar** reciben nombre, teléfono y correo. [DECIDIR-VÍCTOR]
8. **La firma de Slack no tiene prueba automática** (el código existe).

**Opcional**
9. **Chatbot de la landing.** Pone el texto del usuario con `innerHTML`. Es *self-XSS*: solo afecta a quien lo escribe.

**Lo que cumple:**
- en `teamslash-api` no hay secretos reales en ningún commit (solo valores de ejemplo en `env.example`) y `.gitignore` excluye `.env`;
- todo el SQL está parametrizado;
- los logs llevan códigos, no datos personales;
- la huella, la verificación y los estados tienen pruebas.

**Veredicto:** el PR es seguro de revisar y mejora RQ-01/RQ-02. Antes de recibir datos reales de Torvesa hay que cerrar los puntos 1 a 4.

**Lo que no se revisó:**
- `teamslash-poc` (sincronización, bóveda y asistente con RAG);
- la configuración de Railway y Vercel;
- la rotación real de los tokens del antiguo Apps Script;
- dependencias con avisos (`npm audit` no se corrió).

## 5. Formulario (`teamslash-landing`) contra la lista §8.4

| Punto | Estado |
|---|---|
| Etiqueta visible en cada campo | Cumple. El ejemplo del teléfono tiene formato de otro país. |
| Error debajo del campo y cómo arreglarlo | A medias. Sin `aria-*` ni `aria-live`; los `detalles` del 400 no se muestran por campo. |
| Validar al salir del campo | No cumple. Se valida al enviar y luego tecla a tecla. |
| Conservar lo escrito si falla | Cumple. |
| Botón desactivado solo durante el envío | Cumple. |
| Consentimiento sin marcar y con enlace al aviso | Cumple. |
| Aviso de tiempo agotado con «Reintentar» | No cumple. El `fetch` no tiene límite de tiempo. |

## 6. Tareas para Diego (orden de `docs/TAREAS_DIEGO.md`)

| Orden | Tarea | Tipo |
|---|---|---|
| 0 | Revisar y decidir el merge del PR #1 (confirmar antes qué rama despliega Railway) | Revisión |
| A1 | RF-01 + RF-02: `src/estados.js` con los nombres de RQ-05 y migración de los datos | Debe, riesgo medio |
| A2 | Límite de peticiones (con `trust proxy` para Railway) | Debe |
| A3 | Esquema con lista blanca y largo máximo (formulario y `PATCH`) | Debe |
| A4 | Escapar `&`, `<` y `>` en los bloques `mrkdwn` de Slack | Debe |
| A5 | Confirmar o rotar la clave privada en Railway; después, quitar el respaldo de transición en `auth.js` | Debe (lo hace Diego, no la IA) |
| A6 | Telegram que niegue por defecto y compare en tiempo constante | Debe si se usa Telegram |
| B1 | PD-01 según lo que decida Víctor | Conviene |
| B2 | DT-02: SQL de `recordatorios.js` y `reporte.js` dentro de `db.js` | Conviene |
| B3 | Errores 400 sin mensajes internos | Conviene |
| B4 | Tabla de atajos para el Cap. V | Conviene |
| D | Formulario: validación al salir del campo, `aria-*`, límite de 10 s con «Reintentar», `detalles` por campo y `textContent` en el chatbot | Conviene, en `teamslash-landing` |
| E | Strix solo contra una copia local con datos simulados (si Víctor y Diego lo aprueban) | Opcional |

Cada tarea del archivo del repositorio trae su línea para pedírsela a la IA. Por ejemplo: «Lee AGENTS.md y docs/TAREAS_DIEGO.md tarea A1; …; al terminar corre npm test.»

## 7. Para la tesis

- **Cap. V, evidencia:**
  - el límite de 5 s (RQ-01/RQ-02) ahora tiene una prueba automática que mide la respuesta con un canal caído;
  - las suites pasan de 5 a 6.
- **Cap. V, limitaciones técnicas:** la lista de atajos sale de `grep -rn "atajo:" teamslash-api/src` (13 hoy).
- **Cap. IV, protección de datos:** PD-01 ahora incluye Google Calendar como posible encargado.
