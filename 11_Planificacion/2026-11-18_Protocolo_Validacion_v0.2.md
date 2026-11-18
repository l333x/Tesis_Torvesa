---
titulo: "Protocolo de la validación del diseño en operación experimental controlada"
version: v0.2
fecha: 2026-11-18
reemplaza: "2026-11-16_Protocolo_Validacion_v0.1.md (queda igual). Cambios: fechas atadas a la autorización, CP-03 con 20 alteraciones, CP-04 condicionado a DEC-23, claves separadas hechas"
tarea: "S6-T06"
autor_borrador: "Claude (Frente B); Víctor y Diego revisan"
base: "Cap. I p2 v0.3 (metas M1–M6) · Cap. III v0.3 · Casos de prueba v0.1 de Diego (07_Flujos_Diseno, 8-nov) · Cap. IV v0.3 (requisitos) · cronograma (S7 y S8)"
estado: "propuesta; depende de DEC-21 a DEC-23 (tutora) y de la autorización de Torvesa (S6-T08)"
marcadores: "DECIDIR-TUTORA 3 · FALTA-DATO 3 · DECIDIR-VÍCTOR 2"
tags: [protocolo, validacion, M1, M6, sprint6]
---

# Protocolo de la validación del diseño en operación experimental controlada

## 1. Para qué es

Este protocolo dice **qué se hace, quién lo hace, cuándo y cómo se registra** durante las dos semanas en que el sistema funciona en condiciones reales y controladas en la Constructora Torvesa. Con eso se comparan las metas M1 a M6 contra la línea base (objetivo específico OE4).

No es una puesta en producción. Es una validación del diseño, con un alcance acotado, que se puede detener en cualquier momento a pedido de la empresa.

## 2. Fechas y fases

| Fase | Fechas | Qué se hace | Responsable | Tarea |
|---|---|---|---|---|
| 0. Autorización | hasta el 22-nov | Torvesa autoriza por escrito la validación, las fechas, quiénes participan y qué documentos entrega | Víctor y Diego | S6-T08 |
| 1. Preparación | 20 a 22-nov | Sistema estable, cuentas individuales, respaldo, claves separadas y casos de prueba corridos antes de empezar | Diego | S6-T07, S6-T09, S7-T01 |
| 2. Capacitación | 23-nov | Sesión corta con el equipo comercial: cómo llega el aviso, cómo se «toma» una solicitud, cómo se marca ganada o perdida | Ambos | S7-T02 |
| 3. Operación | 23-nov a 5-dic | El sistema recibe las solicitudes reales. Monitoreo diario y registro de incidencias | Diego | S7-T03 a S8-T15 |
| 4. Cierre | 5-dic | Se congela el registro de eventos, se respalda y se verifica su integridad | Diego | S8-T15 |
| 5. Medición y análisis | 7 a 13-dic | Medición «después», casos de prueba y comparación antes y después | Ambos | S9-T01 a S9-T06 |

Las fechas de las fases 1 a 4 son las **previstas**. La operación dura dos semanas y empieza el día hábil siguiente a la autorización de Torvesa. Si la autorización llega tarde, se corren las fases 1 a 4 y se acorta la fase 5; la entrega del 4-ene-2027 no se mueve. [DECIDIR-VÍCTOR: el Cap. I dice que la validación empieza el 23-nov; si se corre, se cambia también ahí.]

## 3. Condiciones de la operación controlada

- **Alcance:** solo las solicitudes de clientes que llegan a Torvesa durante las dos semanas, por el formulario web o registradas desde el celular (RQ-01, RQ-03).
- **Participantes:** las personas del equipo comercial que la gerencia autorice, cada una con su propia cuenta (RQ-20). [FALTA-DATO: cuántas personas y quiénes, por cargo]
- **Datos personales:**
  - El prospecto da su consentimiento en el formulario (RQ-18).
  - El registro verificable guarda solo huellas y códigos (RQ-17).
  - La IA recibe solo códigos de cliente, nunca nombres, teléfonos ni correos (RQ-21).
  - Al terminar, se eliminan o anonimizan los datos de los prospectos perdidos (RQ-19).
- **Revisión humana:** ningún borrador del asistente llega al cliente sin que una persona lo revise y lo apruebe (RQ-12).
- **Precios:** el asistente no pone precios. Los pone siempre Torvesa.
- **Detener la validación:** la gerencia puede pedirlo en cualquier momento. Si hay un incidente de seguridad, Diego apaga el sistema y avisa ese mismo día.

## 4. Qué se mide y con qué

La forma de medir sigue la **propuesta de no recoger datos de personas** (aviso del 2-nov). La decide la tutora: [DECIDIR-TUTORA: DEC-21].

| Meta | Qué dice la meta (Cap. I) | Antes (línea base) | Durante y después | Instrumento |
|---|---|---|---|---|
| M1 | Mediana del tiempo de primer contacto menor a 15 minutos | Fechas y horas de 3 meses de solicitudes, sin datos de clientes (P2-B) [FALTA-DATO: documentos de Torvesa] | Hora de llegada y de primer contacto en el registro del sistema (RQ-24) | Registro del sistema |
| M2 | Menos tiempo de elaboración de una cotización con el asistente | Condición «sin asistente» del caso de prueba | Condición «con asistente» | **CP-01**, hecho por el equipo con datos ficticios |
| M3 | Fuga previa al primer contacto menor que la de la línea base | Los mismos documentos de M1 | Estados y motivos de pérdida del sistema (RQ-05, RQ-07) | Registro del sistema |
| M4 | Menos tiempo y más aciertos al recuperar el historial de un cliente ajeno | Condición «sin bóveda» | Condición «con bóveda» | **CP-02**, hecho por el equipo con datos ficticios |
| M5 | 100 % de las alteraciones simuladas detectadas | — | Copia del registro con alteraciones | **CP-03** |
| M6 | Puntaje SUS de 68 o más | — | Propuesta: evaluación heurística del equipo | **CP-04**, si la tutora acepta [DECIDIR-TUTORA: DEC-23] |

**Si la tutora no acepta la propuesta:** M2 vuelve al cronometraje de quien cotiza en la empresa (P2-A), M4 a la prueba con los vendedores y la encuesta I1, y M6 al cuestionario SUS en su versión validada en español. Esos instrumentos ya existen (C1 v0.2 e I1 v0.2) y necesitan el consentimiento de cada participante.

**Volumen:** si en dos semanas llegan pocas solicitudes, M1 y M3 se informan solo de forma descriptiva [FALTA-DATO: solicitudes por semana en Torvesa].

## 5. Los casos de prueba (resumen)

Los preparó Diego (versión 0.1, 8-nov; CP-03 y CP-04 ajustados el 15-nov). Se ejecutan en el sprint 8, con el sistema ya terminado. Los hacemos **solo nosotros dos (E1 = Diego, E2 = Víctor) y con datos ficticios**, en orden cruzado para que lo aprendido en la primera tarea no favorezca siempre a la misma condición.

| Caso | Meta | Qué compara | Criterio de aceptación |
|---|---|---|---|
| CP-01 | M2 | Tiempo para dejar lista una cotización de 4 solicitudes ficticias, con el asistente y sin él (8 mediciones) | Mediana con asistente menor; el 100 % de los borradores cita un documento; ninguno sale sin revisión; ninguno trae precio |
| CP-02 | M4 | Tiempo y aciertos (de 0 a 5) para responder 5 preguntas sobre un cliente ficticio, con la bóveda y sin ella. El material lo prepara la otra persona | Con la bóveda, menos tiempo y al menos los mismos aciertos |
| CP-03 | M5 | 20 alteraciones al azar en una copia del registro: 7 de contenido, 7 de contenido con huella recalculada y 6 de borrado de un evento del medio | 100 % detectadas y el registro original íntegro. Primera corrida, el 8-nov: 3 de 3 |
| CP-04 | M6 | Evaluación heurística del diseño hecha por el equipo con una lista reconocida de principios. Solo si la tutora acepta DEC-23; si no, se aplica el SUS | [FALTA-DATO: criterio de aceptación de la heurística, después de DEC-23] |

[DECIDIR-VÍCTOR: aprobar las 20 alteraciones de CP-03 que propone Diego.] Límite que se declara: si se borran los últimos eventos de la cadena, la verificación no lo nota. Por eso se propone publicar la última huella en el reporte de cada lunes.

## 6. Registro diario

Cada día de la operación, Diego anota:
- cuántas solicitudes entraron;
- cuántas tuvieron primer contacto antes de los 15 minutos;
- cuántos recordatorios y avisos a la gerencia hubo;
- las incidencias, con la hora, qué pasó, qué se hizo y si se perdió algún dato.

Cada lunes, el sistema genera el reporte con la mediana del tiempo de primer contacto, los estados y los motivos de pérdida (RQ-08). Ese reporte se guarda como evidencia.

## 7. Cierre y entrega de datos

1. El 5-dic se congela el registro de eventos y se respalda.
2. Se corre la verificación de integridad sobre el registro original, que debe salir íntegro.
3. Se anonimizan o eliminan los datos de los prospectos perdidos.
4. Se entregan a Torvesa sus datos y el reporte final, y se acuerda qué pasa con el sistema después de la tesis.

## 8. Limitaciones que se declaran

- Dos semanas y una sola empresa: los resultados no se generalizan.
- Los casos de prueba los hacen los autores del sistema.
- Sin el SUS, la usabilidad se mide de forma más débil (si la tutora acepta la propuesta).
- La línea base depende de que Torvesa entregue los documentos.

## 9. Lo que falta para arrancar

- [ ] Respuesta de la tutora a DEC-20, DEC-21, DEC-22 y DEC-23 [DECIDIR-TUTORA: ética y responsable del tratamiento de datos, DEC-20].
- [ ] Autorización escrita de Torvesa con fechas y participantes (S6-T08).
- [ ] Documentos de 3 meses de solicitudes, solo con fechas y horas (P2-B).
- [x] Claves del servidor separadas antes de usar datos reales: hecho y comprobado en línea el 16-nov (Diego). La clave del formulario solo crea solicitudes.
- [ ] Casos de prueba aprobados por Víctor (S5-T13), con CP-04 si la tutora acepta DEC-23.
- [ ] Consentimiento del formulario (RQ-18) unido a la rama principal del servidor (Diego).
- [ ] Cuentas individuales y respaldo listos (Diego).

La lista completa, con responsables y fechas, está en `11_Planificacion/2026-11-18_Previo_Validacion_v0.1`.
