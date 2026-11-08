---
titulo: Reporte de Diego — sprint 5 adelantado (bloques R, S, T y U)
fecha: 2026-11-08
autor: Diego Bermeo
ia: Claude (Claude Code)
tags: [diego, reporte, sprint5, prueba-de-concepto, casos-de-prueba]
---

# Reporte del 8-nov · sprint 5 adelantado

Los bloques R, S y T de la prueba de concepto quedaron funcionando, y el bloque U, los casos de prueba, queda para que lo apruebes. Todo es con **datos ficticios**.

## Qué se hizo

- **R · Base técnica (RIE-07 cerrado, RQ-18):**
  - TEAMSLASH vuelve a estar en línea:
    - la API en Railway, con PostgreSQL: `https://teamslash-api-production-772d.up.railway.app`;
    - el formulario en Vercel: `https://teamslash-torvesa.vercel.app`.
  - Credenciales nuevas: una app de Slack nueva y una API key nueva. Las del Apps Script quedaron descartadas.
  - Casilla de consentimiento obligatoria en el formulario, con un aviso de privacidad v0.1 en borrador. Lo que solo puede dar Torvesa (RUC, correo y plazo de conservación) queda marcado por completar. Sin la casilla, la API rechaza la solicitud.
  - Las fotos del sitio ahora son de Wikimedia Commons, con licencia libre y créditos. El pie aclara que no son obras de Torvesa.
- **S · Prueba de concepto (S5-T02, S5-T04, S5-T06):** repo privado `psiceslivie/teamslash-poc`.
  - `sincronizar.py` lleva las solicitudes de la API a la bóveda: solicitud, ficha del cliente sin datos personales, y el contacto solo en `_Contactos`. Quita teléfonos y correos del texto libre.
  - `borrador.py` arma el borrador de cotización con el asistente (Claude Sonnet 5.5):
    - usa la plantilla del tipo de obra, no pone precios y cita los documentos que usó;
    - el borrador queda como «Borrador» hasta que una persona lo revisa;
    - antes de llamar al asistente, revisa que no vayan datos personales.
  - Primera prueba: un borrador de cocina en 15 s, con 11 preguntas útiles para completar la cotización.
- **T · Registro (RQ-24, RQ-15, RQ-16, RQ-17):**
  - Hora del primer contacto guardada en el servidor.
  - Tabla de eventos de solo agregar, con huellas SHA-256 encadenadas.
  - Verificación en `/api/eventos/verificar`.
  - Prueba de alteración: **3 de 3 alteraciones detectadas (M5).**
- **U · Casos de prueba (S5-05):** `07_Flujos_Diseno/2026-11-14_Casos_Prueba_v0.1.md`.
  - Tres casos, uno por meta: **CP-01** M2, **CP-02** M4 y **CP-03** M5, como en el esquema del Cap. V.
  - **Anexo A:** la evaluación heurística propuesta para M6.
  - **Anexo B:** lo ya comprobado de cada requisito en la prueba de concepto.

## Para revisar (Víctor)

1. **Aprobar los casos de prueba.** Es el criterio de cierre del bloque U.
2. **¿Tres o cuatro casos?** El Cap. I, el Cap. III y la presentación dicen «cuatro»; el cronograma y el Cap. V dicen tres. Si la evaluación heurística cuenta como el cuarto, se puede dejar «cuatro».
3. **RQ-24:** propuse que el primer contacto cuente cuando alguien pulsa «Tomar» (o cierra la solicitud), no cuando la archiva. ¿Lo apruebas?
4. **Estados:** TEAMSLASH tiene 4 y RQ-05 pide 5. Hoy la bóveda trata «Cerrado» como ganada y «Archivado» como perdida, y «Cotizada» no existe en el servidor.
5. **Límite del registro:** borrar los **últimos** eventos no se detecta. Propongo publicar cada lunes la última huella en el reporte semanal (RQ-08), como ancla. Va también como limitación en el Cap. IV.
6. **CP-03:** ¿cuántas alteraciones al azar en S8-04? Propongo 20.
7. **Sigue pendiente:** el modelo de IA (A36), la sincronización de la bóveda y `_Contactos` (de las 11 dudas del 2-nov).

## Para el Cap. IV

- La tabla 3 («ya existe en TEAMSLASH / es nuevo») ya se puede actualizar. Ya funcionan:
  - la hora del primer contacto;
  - la casilla de consentimiento;
  - el registro verificable;
  - la bóveda con el asistente, en versión de prueba de concepto.
- El riesgo «la versión publicada no está en línea» quedó cerrado el 8-nov.
