---
titulo: "Reporte de Diego: respuesta al mensaje del 16-nov (horas, Torvesa, casos de prueba, claves)"
fecha: 2026-11-15
autor: Diego Bermeo
ia: Claude (Claude Code)
responde_a: "00_Inbox/2026-11-16_Mensaje_a_Diego_BORRADOR.md"
tareas: "S6-N03 · S5-T13 · S6-T08 · S7-T01 · S5-T14"
tags: [diego, reporte, sprint6, horas, claves]
---

# Reporte del 15-nov · respuesta a tus seis puntos

## 1. Resúmenes de 1 página (S5-T14)

Recibidos los tres tuyos (exposición del negocio, Cap. 1 y requisitos y costos). Los leo antes de la revisión de sprint, para lo de «Explícame lo tuyo».

## 2. Horas del levantamiento (S6-N03)

Cómo salen los números:
- **Plan:** las horas que el cronograma (`IA_DIEGO.md` §5 y §5b) le da a cada bloque.
- **Registro:** el tiempo que estuvo abierta la sesión de trabajo con la IA ese día (inicio y fin del registro). Es un **mínimo**: no cuenta leer fuentes por fuera, revisar documentos ni configurar cosas a mano. El registro del 2-nov está incompleto.
- **Propuesta:** lo que yo reportaría. Uso el plan en los bloques que quedaron completos, porque incluye la lectura y la revisión, y el registro más el trabajo manual donde no hay plan.

| Sprint | Bloques | Qué | Fecha | Plan (h) | Registro (h) | Propuesta (h) |
|---|---|---|---|---|---|---|
| 1–2 | A y B | Arranque, repo, RAG y lectura del documento madre | 19-oct | 2,0 | 2,4 | 2,5 |
| 1–2 | C | Fuentes de bóvedas y RAG | 21-oct | 3,0 | 1,7 | 3,0 |
| 1–2 | D a H | Documentación oficial, BPMN, AS-IS v0.1, inventario de herramientas, resúmenes | 25-oct | 11,5 | 4,5 | 11,5 |
| 3 | L, M y N | Revisión de la elicitación, casos de uso y modelo conceptual, resumen AS-IS | 2-nov | 8,0 | 1,9 * | 8,0 |
| 4 | O, P y Q | TO-BE v0.1, bóveda del sistema, resumen y revisión del sprint 4 (sin análisis de campo) | 2-nov | 15,0 | (en el anterior) | 15,0 |
| 5 | R, S, T y U | Despliegue con consentimiento, prueba de concepto, registro con huellas, casos de prueba | 8-nov | — | 3,4 | 4,5 ** |
| 6 | — | Claves separadas y este reporte | 15-nov | — | 1,0 | 1,0 |
| | | **Total del trabajo técnico** | | | **≈ 14,9** | **≈ 45,5** |
| | | Reuniones con Víctor, con la tutora y gestión con Torvesa | | | — | **[Diego completa]** |

\* El registro del 2-nov solo tiene la parte final de la sesión (los commits de 11:28 a 12:10); el trabajo de esos bloques empezó antes.
\** 3,4 h de sesión más ≈ 1 h de configuración a mano: la app nueva de Slack, las variables de Railway y Vercel.

**No cuento** la sesión del 18-oct (1,4 h) del archivo de ingresos simulado: no es levantamiento y esos datos no se usan.

**Para el modelo financiero:** si se suman las reuniones, mi parte queda en unas **50 h**. Si el supuesto es de 200 h entre los dos, revisa si el resto cuadra con tus horas.

## 3. Mensaje a Torvesa

Lo revisé. Está bien y lo mando yo por el canal de siempre. Antes de enviarlo propongo tres cambios:

1. **Punto 3 (tipo de empresa).** El SRI ya dice que es **sociedad** (`Datos_Torvesa_Publicos.md`). Mejor preguntar solo qué tipo de sociedad es, y no «persona natural, sociedad o compañía», para no parecer que no revisamos.
2. **Punto 4 (formularios 101).** La frase «no se publican con el nombre de la empresa» choca con el título de la tesis, que ya nombra a Torvesa. Propongo: «Las cifras se usan solo para la tesis y no se publican sin su autorización; si lo prefieren, las presentamos sin el nombre de la empresa».
3. **Punto 1 (fechas).** Como depende de la tutora (DEC-21), propongo **mandar ya los puntos 2, 3 y 4**. Torvesa es la ruta crítica y esos datos no dependen de ella. El punto 1 iría en un segundo mensaje cuando la tutora responda.

Si estás de acuerdo, saca la v0.2 del borrador y yo la envío.

## 4. Casos de prueba (S5-T13)

- **CP-03:** **20 alteraciones al azar**, repartidas entre los tres tipos que ya probamos: contenido cambiado, huella recalculada y evento borrado del medio (7, 7 y 6). Borrar los **últimos** eventos sigue siendo la limitación conocida: va en el Cap. IV con el ancla semanal de RQ-08.
- **¿Cuatro casos?** Sí: propongo que la evaluación heurística sea el **CP-04 (M6)**. Así el Cap. I se queda con «cuatro». Si la tutora no acepta la heurística en lugar del SUS, volvemos a tres y corregimos el Cap. I.

## 5. Revisión con la tutora

Me tocan las diapositivas 4, 5 y 6. Ya tengo mi guion de ensayo: `00_Inbox/2026-11-15_Guion_Diego_Diapositivas_4a6.md`. Para el ensayo por llamada: **[Diego confirma martes o miércoles y la hora]**.

## 6. Claves del servidor (S7-T01)

**Hecho y en línea desde el 16-nov.** Hasta hoy la clave del formulario, que cualquiera ve en el navegador, también permitía listar, leer y cambiar todas las solicitudes. Ahora:

- **Clave pública** (formulario): **solo crea** solicitudes.
- **Clave privada** (prueba de concepto y equipo): lee, lista y modifica. Nunca va en el navegador.
- Las dos claves son nuevas, porque la anterior ya era visible en la página.
- Prueba nueva `test/claves.smoke.js`: la clave pública recibe 401 al listar, leer, modificar o ver el registro; la privada puede todo. Todas las pruebas de la API pasan.
- Commits: `teamslash-api` 8c6a406 (rama `rq18-consentimiento`) y `teamslash-landing` 7aade8f, ya desplegados en Railway y Vercel.
- **Comprobado en línea (16-nov):** la clave vieja ya no sirve; la pública crea solicitudes (prueba ficticia SOL-0006) pero recibe 401 al leer; la privada lee, y `sincronizar.py` funciona con ella.

Con esto, la fila del Cap. IV (Art. 37 de la LOPDP, «falta separar la clave del servidor») ya puede pasar a **cumplido**.
