---
titulo: Revisión del sprint 4 y plan del sprint 5 — parte de Diego (para la bitácora)
fecha: 2026-11-02
autor: Diego Bermeo
ia: Claude (Claude Code)
tareas: [S4-T15, S4-07]
uso: Víctor la pega o la resume en 11_Planificacion/Bitacora_Semanal.md en la revisión del domingo 8 (S4-T15)
tags: [diego, revision, sprint4, sprint5]
---

# Revisión del sprint 4 · parte de Diego

> Se escribe el lunes 2-nov porque los bloques de Diego del sprint 4 se adelantaron y quedaron hechos ese día. Si el resto de la semana cambia algo, se actualiza el domingo.

## Qué se hizo (todo subido el 2-nov)
- **Lo atrasado del sprint 3:**
  - **L:** revisión técnica de la elicitación, con control de cambios. Cerró PEN-01: TEAMSLASH usa PostgreSQL y hoy no está desplegado. Propone RQ-24.
  - **N:** resumen del AS-IS.
  - **M:** casos de uso, modelo conceptual y plantilla TO-BE. Cerró PEN-11.
- **Sprint 4:**
  - **O:** TO-BE v0.1 en 3 partes.
  - **P:** bóveda del sistema v0.1.
  - **Q:** resumen de 1 página de la bóveda.
- **Cambio de plan:** el aviso de que no se recogen datos de personas (`00_Inbox/2026-11-02_aviso_sin_encuestas_ni_entrevistas.md`) y el correo nuevo a Torvesa, que solo pide documentos y datos de la empresa.

## Qué no se hizo
- **K, AS-IS v0.2:** falta saber qué observó la tutora en la Revisión 1 del 28-oct; no hay acta.
- **Campo y línea base (S4-T16, S4-T17):** sin encuestas ni observación. La línea base de M1 y M3 depende de que Torvesa mande la muestra de fechas y horas.
- **Faltan pruebas a mano:**
  - abrir la bóveda en Obsidian;
  - abrir los `.bpmn` en bpmn.io.

## Qué aprendimos
- Revisar el código real de TEAMSLASH sirvió más que los documentos: el informe y el pitch hablaban de dos versiones distintas, y el servicio ya no está desplegado.
- Quitar las encuestas y entrevistas saca a Torvesa de la ruta crítica: el diseño y las pruebas dependen de nosotros.
- Subir cada bloque al terminarlo, y no todo el domingo, funcionó.

# Plan del sprint 5 (9 al 15 de noviembre) · parte de Diego

| Día | Bloque | Tarea | Entregable | Cómo sé que terminé |
|---|---|---|---|---|
| Lun 9 | R · Base técnica | Volver a desplegar TEAMSLASH en Railway con credenciales nuevas (RIE-07); agregar la casilla de consentimiento al formulario (RQ-18) | API respondiendo en `/health`; formulario con consentimiento | Un envío de prueba llega al registro y a Slack |
| Mar 10 – Mié 11 | S · Prueba de concepto | Formulario → servidor → bóveda (nota de solicitud) → borrador de cotización con el asistente (S5-04) | Repositorio de la prueba de concepto | El flujo completo funciona con datos ficticios |
| Jue 12 | T · Registro | Hora de primer contacto (RQ-24) y registro de eventos con huella (RQ-15) | Tabla de eventos y prueba de alteración | Una alteración simulada se detecta (M5) |
| Vie 13 – Sáb 14 | U · Casos de prueba | Los 3 casos de prueba (S5-05), con las pruebas que reemplazan a las encuestas: M2 (cotización con y sin asistente, cronometrada por nosotros), M4 (recuperación con y sin bóveda) y la evaluación heurística (M6 reformulada) | `07_Flujos_Diseno/2026-11-14_Casos_Prueba_v0.1.md` | Víctor los aprueba |
| Dom 15 | V · Cierre | Revisión del sprint 5 | Sección en la bitácora | — |

**Depende de Víctor:**
- aprobar el cambio sin encuestas y cómo se reformula M6;
- RQ-24;
- la sincronización de la bóveda;
- el visto bueno al LLM (A36).
