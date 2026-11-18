---
titulo: "Lo que falta antes de la validación del diseño"
version: v0.1
fecha: 2026-11-18
tarea: "S6-T06 (protocolo) · S6-T08 (autorización) · S6-T07, S6-T09, S7-T01 (preparación) · S5-T13 (casos de prueba)"
base: "Protocolo de la validación v0.1 (16-nov), §2 y §9 · reporte de Diego del 15-nov · decisiones DEC-18 a DEC-23 · Cap. IV v0.4 (huecos RQ-08, RQ-16 y RQ-19)"
estado: "propuesta; se actualiza después de la Revisión 2 (19-nov)"
tags: [validacion, pendientes, ruta-critica, sprint6]
---

# Lo que falta antes de la validación del diseño

La validación del diseño en operación experimental controlada dura dos semanas en Torvesa. Estaba prevista del 23-nov al 5-dic. Para que arranque tienen que cumplirse cuatro condiciones, en este orden:

1. **La tutora aprueba la forma de medir** (DEC-21) y dice quién es el responsable del tratamiento de datos (DEC-20).
2. **Torvesa autoriza por escrito**, con las fechas y las personas que participan.
3. **El sistema queda listo** para recibir solicitudes reales.
4. **El equipo de Torvesa recibe la capacitación**.

Cada condición depende de la anterior. La que más riesgo tiene es la segunda: Torvesa no responde desde octubre.

## 1. La ruta, paso a paso

| Orden | Paso | Quién | Dónde se hace | Fecha objetivo | Depende de | Estado |
|---|---|---|---|---|---|---|
| 1 | Ensayar la Revisión 2 | Víctor y Diego | Llamada | 18-nov | — | Pendiente |
| 2 | Enviar el mensaje 1 a Torvesa (datos de la empresa) | Víctor aprueba, Diego envía | Canal de Diego con Torvesa | 18 o 19-nov | — | Borrador v0.2 listo |
| 3 | Revisión 2: respuestas a DEC-18 a DEC-23 | Tutora | Reunión en la UPS | 19-nov | — | Pendiente |
| 4 | Pedir a la tutora la carta de respaldo para Torvesa | Víctor | Reunión en la UPS | 19-nov | — | Pendiente |
| 5 | Acta de la Revisión 2 y decisiones en la app | Claude, con las notas de Víctor | Bóveda y app Bitácora Torvesa | 19-nov | Paso 3 | Plantilla lista |
| 6 | Protocolo v0.3 con lo que diga la tutora | Claude; Víctor revisa | Bóveda (`11_Planificacion/`) | 20-nov | Paso 3 | v0.2 lista |
| 7 | Enviar el mensaje 2 a Torvesa (fechas y protocolo) | Diego | Canal de Diego con Torvesa | 20-nov | Pasos 3 y 6 | Borrador v0.2 listo |
| 8 | **Autorización escrita de Torvesa** | Gerencia de Torvesa | Correo o carta | 20 a 22-nov | Paso 7 | **Ruta crítica** |
| 9 | Preparar el sistema: estable, cuentas individuales y respaldo | Diego | Servidor y página en línea | 20 a 22-nov | — | Por confirmar con Diego |
| 10 | Aprobar los casos de prueba (CP-03 con 20 alteraciones; CP-04 si la tutora acepta) | Víctor | Bóveda (`07_Flujos_Diseno/`) | 20-nov | Paso 3 | Pendiente |
| 11 | Capacitar al equipo comercial | Víctor y Diego | Oficina de Torvesa, Quito | Día 1 de la validación | Pasos 8 y 9 | Material aún no existe; se prepara la semana del 16-nov |
| 12 | Arranque de la validación | Diego monitorea | Torvesa | Día siguiente a la autorización | Pasos 8 a 11 | — |

**Si Torvesa no autoriza hasta el 22-nov:** se escala como ya estaba previsto (tarea DEC-TOR-24 de la app). Víctor llama al Ing. Torres o se envía la carta de respaldo de la tutora. Cada semana de retraso se descuenta de la medición (7 a 13-dic), no de la entrega del 4-ene-2027.

## 2. Lo que tiene que dar Torvesa

| Qué | Para qué | ¿Frena el arranque? | Estado |
|---|---|---|---|
| Autorización escrita con fechas | Poder usar el sistema con solicitudes reales | **Sí** | Sin respuesta |
| Quiénes participan, por cargo | Crear una cuenta por persona (RQ-20) | **Sí** | Sin respuesta |
| Fechas y horas de 3 meses de solicitudes, sin datos de clientes | Línea base de M1 y M3 | No frena el arranque, pero sin ellas no hay comparación antes y después | Se pide en el mensaje 1 |
| Cuántas solicitudes llegan por semana | Saber si dos semanas alcanzan para M1 y M3 | No | Se puede preguntar con la autorización |
| Actividad (vías o edificaciones) y tipo de sociedad | Describir bien a la empresa en el Cap. I | No | Se pide en el mensaje 1 |
| Formularios 101 de 2023 a 2025 | Cifras reales en el estudio de costos | No | Se pide en el mensaje 1 |

## 3. Lo que tiene que decidir la tutora

| Decisión | Qué cambia si dice que sí | Qué cambia si dice que no |
|---|---|---|
| DEC-20 · Ética y responsable del tratamiento de datos | Se escribe en el protocolo y en el formulario de consentimiento | Si hace falta un comité de ética, la validación espera su aprobación |
| DEC-21 · Medir sin datos de personas | Se mantiene el protocolo: documentos, registro del sistema y casos de prueba | Vuelven el cronometraje, la encuesta I1 y el SUS, con consentimiento de cada participante (instrumentos C1 v0.2 e I1 v0.2, ya hechos) |
| DEC-22 · Enfoque cuantitativo | Cambia el nombre del enfoque en el Cap. III | Se mantiene «mixto con predominio cuantitativo» y hace falta una parte cualitativa |
| DEC-23 · Heurística en lugar del SUS (M6) | Hay cuatro casos de prueba (CP-04) y el Cap. I queda igual | Quedan tres casos, se corrige el Cap. I y se aplica el SUS |
| DEC-18 y DEC-19 · Redacción de OE3 y nombre del diseño | Solo cambian palabras en los Caps. I y III | No frenan la validación |

## 4. Lo que tiene que dejar listo Diego

| Qué | Requisito | Estado al 18-nov |
|---|---|---|
| Claves del servidor separadas (la del formulario solo crea solicitudes) | Art. 37 de la LOPDP | **Hecho y comprobado en línea el 16-nov** |
| Consentimiento en el formulario | RQ-18 | Programado y en línea, en la rama `rq18-consentimiento`; falta unirlo a la rama principal |
| Cuentas individuales | RQ-20 | Por confirmar con Diego |
| Respaldo del registro y del servidor | Protocolo, fase 1 | Por confirmar con Diego |
| Reporte de cada lunes con la última huella como ancla | RQ-08 | Hueco abierto en el Cap. IV |
| Verificación del registro | RQ-16 | Hueco abierto en el Cap. IV (CP-03 la prueba) |
| Eliminar o anonimizar a los prospectos perdidos al cierre | RQ-19 | Hueco abierto en el Cap. IV; se necesita el 5-dic, no al arranque |

## 5. Qué se hace con esta lista

- **Mañana, en la reunión:** se usa la sección 3 para anotar las respuestas de la tutora.
- **El 19-nov por la tarde:** se marca cada fila en la app Bitácora Torvesa y se saca la v0.2 de esta lista.
- **Diego:** confirma las filas «por confirmar» de la sección 4.
