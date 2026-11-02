---
titulo: Resumen para Víctor — proceso actual (AS-IS) y funciones del sistema
version: v0.1
fecha: 2026-11-01
autor: Diego Bermeo
ia: Claude (Claude Code)
tarea: S3-T19 (bloque N)
base: 07_Flujos_Diseno/2026-10-25_AS-IS_v0.1.md
estado: borrador sin validar en campo
tags: [diego, resumen, as-is, procesos, sprint3]
---

# El proceso actual de Torvesa en 1 página

> [!summary] En tres frases
> 1. El cliente escribe al **WhatsApp personal** de un socio o ingeniero, que casi siempre está en obra y lo lee cuando puede.
> 2. Si no puede atenderlo, lo **reenvía** a otra persona, que **arma la cotización casi desde cero**.
> 3. **Nada queda registrado**: el seguimiento depende de la memoria y, si alguien se va, el historial del cliente se va con su celular.

> [!warning] Es un borrador
> Sale del Informe Final del 22-jul (antecedente vigente) y del Cap. 2. **No se ha observado ni entrevistado a nadie en Torvesa.** Dos pasos son supuestos (el reenvío por WhatsApp y cómo se envía la cotización). Se valida en campo con la guía I3. Diagrama completo: `2026-10-25_AS-IS_v0.1.png`.

## Los 8 pasos de hoy

Cliente escribe → quien recibe lo lee cuando puede → ¿puede atender? (si no, lo reenvía) → primer contacto → cotización desde cero → envío → seguimiento si se acuerda → el cliente acepta o se va sin que quede el motivo.

## Dónde se pierde tiempo y qué función del sistema lo ataca

| Punto | Qué pasa hoy | Función que necesita el sistema | Requerimientos | Meta |
|---|---|---|---|---|
| ❶ Espera | Nadie ve el mensaje hasta revisar el celular | Registrar la solicitud y **avisar al instante** al celular | RQ-01, RQ-02, RQ-03 | M1, M3 |
| ❷ Asignación informal | El reenvío no deja rastro ni responsable | **Asignar un responsable** y registrar cada cambio de estado; recordar a los 15 min | RQ-04, RQ-05, RQ-06, RQ-24 | M1, M3 |
| ❸ Cotización desde cero | Las cotizaciones viejas están en celulares y cuadernos | **Plantillas** y **borrador con IA** a partir de la bóveda, revisado por una persona | RQ-10, RQ-11, RQ-12 | M2 |
| ❹ Seguimiento de memoria | Sin recordatorios, el cliente «se enfría» | **Fecha de seguimiento** con recordatorio | NEC-11 (en análisis) | Ninguna |
| ❺ Historial en celulares | Si alguien se va, se pierde lo que sabía | **Ficha por cliente** en la bóveda, que cualquiera autorizado puede buscar | RQ-09, RQ-13, RQ-14 | M4 |

Además, en todos los pasos: **registro verificable** de cada evento (RQ-15, RQ-16; M5) y **protección de datos** (RQ-17 a RQ-21).

## Qué ya existe y qué es nuevo (revisé el código de TEAMSLASH el 2-nov)

- **Ya existe en el MVP (versión 2, 23-jul-2026):**
  - formulario web que registra la solicitud con código `CLI-0001` en una base de datos PostgreSQL;
  - aviso a Slack (y, si se configuran, a Telegram, Discord o Teams) con botones de estado: «Tomar» deja como responsable a quien lo pulsa;
  - notas con autor y fecha, y una fecha de seguimiento que crea un evento en Google Calendar: **el punto ❹ ya tiene una solución simple**.
- **Falta (trabajo nuevo):**
  - la hora del primer contacto (sin ella no se mide M1; propuse RQ-24);
  - el historial de cambios de estado y el registro verificable;
  - los cinco estados de RQ-05 (hoy son cuatro: Nuevo, En proceso, Cerrado, Archivado);
  - la casilla de consentimiento del formulario;
  - la bóveda, las plantillas y el asistente de IA.
- **Atención:** hoy el MVP **no está desplegado**: Railway responde «Application not found». Hay que volver a ponerlo en marcha antes de la prueba de concepto (RIE-07).

## Qué hay que confirmar en campo (guía I3)

1. ¿Por dónde llegan las solicitudes y en qué proporción?
2. ¿Quién decide quién atiende?
3. ¿Hay visita a la obra antes de cotizar?
4. ¿Quién cotiza y con qué herramienta?
5. ¿Alguien aprueba la cotización antes de enviarla?
6. ¿Cómo se envía y cómo se sigue?
7. ¿Se anota por qué se pierde un cliente?
