---
titulo: "Replanificación del cierre hasta la entrega del 4-ene-2027"
version: v0.1
fecha: 2026-11-27
estado: BORRADOR
autor_borrador: "Claude; Victor revisa y decide"
base: "CRONOGRAMA.md (22-nov) · Gantt v0.4 (20-nov) · Protocolo de validación v0.2 (18-nov) · Previo a la validación v0.1 (18-nov) · Bitacora_Semanal.md hasta el 23-nov · git log hasta fa414d0 (24-nov) · archivos de la bóveda al 27-nov"
no_cambia: "Cronograma_Tesis.xlsx, CRONOGRAMA.md y el Gantt v0.4 quedan iguales. Si Victor aprueba este plan, se pasan al Excel en una versión nueva."
tags: [cronograma, replan, validacion, DEC-21, cierre]
---

# Replanificación del cierre hasta el 4-ene-2027

**En una línea:** el trabajo de escritorio va adelantado, pero todo lo que depende de la tutora y de Torvesa está parado desde el 19-nov. El plan corre los casos de prueba y la redacción ya, sin esperar a nadie, y deja la validación con Torvesa como una pieza que entra solo si llega a tiempo. **Corte de decisión: viernes 4-dic. Último día para arrancar la validación con Torvesa: lunes 14-dic.**

## 0. Qué se comprobó y cómo

- Se revisaron las carpetas `06_Capitulos/`, `07_Flujos_Diseno/`, `08_Reuniones_Tutora/`, `05_Datos_Campo/`, `04_Instrumentos/`, `00_Inbox/` y `11_Planificacion/`.
- El último commit de tesis es `e72e03e` (23-nov, paquete para la tutora). El del 24-nov (`fa414d0`) es estudio de clase. **Del 24 al 27-nov no hay ningún commit de tesis.**
- No hay en la bóveda ninguna respuesta de la tutora, ninguna autorización de Torvesa ni datos de Torvesa para la línea base (`05_Datos_Campo/LineaBase_2026-10/` solo tiene el README).
- El 27-nov existen dos borradores nuevos: `00_Inbox/2026-11-27_Mensaje_Tutora_Seguimiento_BORRADOR.md` y `00_Inbox/2026-11-27_Mensaje_a_Diego_BORRADOR.md`. Ninguno está enviado.
- Marcadores pendientes en los capítulos vigentes (Cap. I v0.6, II v0.5, III v0.6, IV v0.7, V–VI v0.6): **23 `[FALTA-FUENTE]`, 55 `[FALTA-DATO]` y 9 `[DECIDIR-TUTORA]`.**

## 1. Estado real de cada tarea

Estados: **hecho**, **parcial**, **pendiente**, **bloqueada por X**, **sin evidencia** (no hay archivo ni commit que lo pruebe).

### Sprint 6 (16 a 22-nov) · Revisión 2

| Tarea | Estado | Evidencia |
|---|---|---|
| S6-01 Presentar a la tutora en la Revisión 2 | **Bloqueada por la tutora.** El material está listo | Presentación v0.4 (`08_Reuniones_Tutora/2026-11-23_Revision2_Presentacion_v0.4.pdf`). La reunión del 19-nov no se hizo y la del 25 o 27-nov tampoco |
| S6-02 Acta de la Revisión 2 | **Bloqueada por la tutora** | Solo existe `_Plantilla_Acta.md` |
| S6-03 Revisar el sprint 6 y planificar el 7 | **Parcial** | La bitácora registra el 20, 22 y 23-nov, pero no hay revisión del sprint con Diego (S6-T12 sigue «Pendiente» en el Gantt v0.4). De la reunión: sin evidencia |

### Sprint 7 (23 a 29-nov) · Arranque de la validación

| Tarea | Estado | Evidencia |
|---|---|---|
| S7-01 Incorporar las observaciones de la Revisión 2 | **Bloqueada por la tutora** (no hay observaciones) | El borrador 4 v0.3 tiene cambios propios, no de la tutora |
| S7-02 Preparar la validación (protocolo, capacitación, permisos) | **Parcial; bloqueada por la DEC-21 y por la autorización de Torvesa** | Protocolo v0.2 y Previo v0.1 (`11_Planificacion/2026-11-18_*`), en md, Word y PDF. Claves separadas hechas el 16-nov (`c086e6a`). Autorización de Torvesa: sin evidencia. Material de capacitación: no existe. Envío del mensaje 1 a Torvesa por Diego: sin evidencia |
| S7-03 Arrancar la validación (24-nov) y monitorearla | **Bloqueada por la DEC-21 y por la autorización de Torvesa** | No arrancó. No hay registro de eventos de la operación |
| S7-04 Capítulo de diagnóstico con la línea base real | **Parcial; bloqueada por los datos de Torvesa** | El diagnóstico preliminar está en el Cap. IV v0.7 (sección «Línea base»). El entregable `06_Capitulos/2026-11-28_Cap4_Diagnostico_v0.1.docx` no existe. Faltan las fechas y horas de 3 meses de solicitudes |
| S7-05 Revisar el sprint 7 y planificar el 8 | **Pendiente** (el sprint cierra el domingo 29-nov) | — |

### Sprint 8 (30-nov a 6-dic) · Documentación y casos de prueba

| Tarea | Estado | Evidencia |
|---|---|---|
| S8-01 Herramientas elegidas y descartadas | **Parcial** | `07_Flujos_Diseno/2026-10-25_Inventario_Herramientas_v0.2.xlsx` y la sección «Herramientas, costos y viabilidad» del Cap. IV v0.7. La carpeta `07_Flujos_Diseno/Herramientas` no existe |
| S8-02 Modelo de datos y registro de eventos | **Parcial** | Modelo conceptual v0.1 (31-oct) y resumen de la prueba de concepto (15-nov). La carpeta `Modelo_Datos` no existe ni se comprobó que coincida con el sistema |
| S8-03 Plantillas de cotización y especificación del asistente de IA | **Parcial** | Plantillas en `07_Flujos_Diseno/Boveda_Sistema/` (2-nov) y `2026-11-17_Diseno_Agentes_v0.1.md` (sin commit). La carpeta `Asistente_IA` no existe. Revisión de Victor: sin evidencia |
| S8-04 Ejecutar los casos de prueba | **Parcial** | Casos de prueba v0.1 (14-nov). Solo hay una corrida previa de CP-03 con 3 alteraciones (8-nov); faltan las 20. CP-01 y CP-02: sin evidencia. CP-04 depende de la DEC-23. La carpeta `Resultados_Casos_Prueba` no existe |
| S8-05 ✂ Manual básico de usuario | **Pendiente** (sin evidencia) | — |
| S8-06 Capítulo de diseño y viabilidad | **Parcial, avanzado** | El contenido ya está en el Cap. IV v0.7: requisitos, casos de uso, TO-BE, componentes, LOPDP, costos, VAN y TIR con el Excel v0.3, y riesgos. El `.docx` del Cap. 5 que nombra el cronograma no existe porque la tesis cambió su estructura (el diseño quedó en el Cap. IV) |
| S8-07 Revisar el sprint 8 | **Pendiente** | — |

### Sprint 9 (7 a 13-dic) · Medir y escribir resultados

| Tarea | Estado | Evidencia |
|---|---|---|
| S9-01 Medición «después» (7 a 9-dic) | **Bloqueada por la validación** (que depende de la DEC-21 y de Torvesa) | La carpeta Post no existe |
| S9-02 Análisis antes y después y capítulo de resultados | **Parcial** | Estructura en el Cap. V–VI v0.6 (casos de prueba, validación, usabilidad, discusión y limitaciones). Faltan los datos: 19 `[FALTA-DATO]` |
| S9-03 ✂ Pruebas de uso y de carga simuladas | **Pendiente** (sin evidencia). No depende de nadie | — |
| S9-04 Revisar el sprint 9 | **Pendiente** | — |

### Sprint 10, holgura y entrega

| Tarea | Estado | Evidencia |
|---|---|---|
| S10-01 ✂ Ciclos con la tutora | **Bloqueada por la tutora** (no responde desde el 23-nov) | Correo del 23-nov enviado, según Victor; seguimiento del 27-nov en borrador |
| S10-02 Hito: tesis al 90 % | **Pendiente** | La base es el borrador 4 v0.3 (84 páginas), con los marcadores de la sección 0 |
| S10-03 Revisar el sprint 10 | **Pendiente** | — |
| H-01 APA, citas y bibliografía | **Parcial** | Hay fichas en `02_Fuentes/`, pero quedan 23 `[FALTA-FUENTE]` en los capítulos vigentes. El criterio «0 citas sin ficha verificada» no se cumple |
| E-01 Revisión final, aprobación y firma de la tutora | **Pendiente; depende de la tutora** | — |

## 2. Lo atrasado y por qué

| Qué | Debía estar | Atraso al 27-nov | Por qué |
|---|---|---|---|
| Revisión 2 y su acta (S6-01, S6-02) | 19-nov | 8 días | La tutora movió la reunión y no responde al correo del 23-nov |
| DEC-18 a DEC-23 y DEC-25 | 19-nov | 8 días | Mismo motivo. La DEC-21 frena todo lo de Torvesa |
| Autorización y datos de Torvesa (S6-T08, S7-02) | 22-nov | 5 días | El mensaje 2 espera la DEC-21. Del mensaje 1 no hay evidencia de envío |
| Arranque de la validación (S7-03) | 24-nov (luego 30-nov) | 3 días y contando | Depende de la DEC-21 y de la autorización |
| Línea base real (S7-04) | 28-nov | Casi seguro | Sin las fechas y horas de Torvesa no hay línea base de M1 y M3 |
| Sistema listo: cuentas individuales, respaldo y rama RQ-18 (S7-T01) | 22-nov | 5 días | Sin evidencia de Diego. Además, claves antiguas en el historial de la landing sin confirmar (bitácora del 23-nov) |
| Revisiones de sprint 6 y 7 | 22 y 29-nov | 5 días | Dos semanas sin trabajo en la tesis |

## 3. Plan semana a semana (30-nov a 4-ene)

### Reglas del plan

- **Lo común a los tres escenarios se hace ya.** Casos de prueba, documentación técnica, capítulos y citas no dependen de la tutora ni de Torvesa.
- **Días de baja carga:** jueves 24 y viernes 25-dic, jueves 31-dic y viernes 1-ene. Esos días solo se lee o no se trabaja.
- **Límite duro de operación:** ningún día de validación con Torvesa después del **martes 22-dic**. Después de esa fecha no queda tiempo para medir, analizar y escribir antes del 4-ene.
- **Fechas límite para arrancar la validación con Torvesa:**
  - **miércoles 9-dic** para hacer las dos semanas completas del protocolo (9 al 22-dic);
  - **lunes 14-dic** para una versión corta de una semana (14 al 18-dic, con el 21 y 22 de margen). Esa versión se declara como limitación.
  - **Después del 14-dic la validación con Torvesa ya no cabe.** Se pasa al escenario C.
- **La DEC-21 no es lo único que falta.** Aunque la tutora acepte, sin la autorización escrita de Torvesa no se arranca. Por eso Diego pide la autorización la semana 1, con las fechas sujetas a la respuesta de la tutora (lo decide Victor).
- **Si la tutora dice que no a la DEC-21:** vuelven el cronometraje, la encuesta I1 y el SUS, con el consentimiento de cada persona (C1 v0.2 e I1 v0.2 ya existen). Suma unos 2 días de preparación, pero las fechas límite no cambian.

### Semana 1 · 30-nov a 6-dic (común a los tres escenarios)

| Tarea | Responsable | Dónde se hace | Entregable |
|---|---|---|---|
| Enviar el seguimiento a la tutora: WhatsApp el lunes 30; si el martes 1-dic no hay respuesta, responder al correo del 23-nov con Diego en copia | Victor | WhatsApp y Outlook de la UPS | Mensaje enviado (`00_Inbox/2026-11-27_Mensaje_Tutora_Seguimiento_BORRADOR.md`) |
| Enviar el mensaje a Diego y hacer la revisión de los sprints 6 y 7 (domingo 29-nov o lunes 30) | Victor y Diego | Llamada | Sección nueva en `Bitacora_Semanal.md` |
| Confirmar el envío del mensaje 1 a Torvesa; enviar el pedido de datos (fechas y horas de 3 meses, sin nombres) y la consulta de autorización con fechas sujetas a la tutora | Diego (Victor aprueba el texto) | Canal de Diego con Torvesa | Respuesta de Torvesa o plazo vencido el 4-dic |
| Confirmar o rotar las claves antiguas; cuentas individuales, respaldo y rama RQ-18 unida | Diego | Repositorio y servidor de Diego | Lista de verificación cerrada en el Previo |
| Correr CP-03 con las 20 alteraciones y CP-01 y CP-02 en orden cruzado (E1 Diego, E2 Victor) | Diego y Victor | Copia local con datos ficticios | `07_Flujos_Diseno/Resultados_Casos_Prueba/` (aún no existe; se crea esta semana) |
| Aprobar las 20 alteraciones de CP-03 | Victor | Bóveda, `07_Flujos_Diseno/2026-11-14_Casos_Prueba_v0.1.md` | Visto bueno anotado |
| Capítulo III v0.7 con la medición sin datos de personas, marcado como propuesta en espera de la DEC-21 | Claude; Victor revisa | Bóveda, `06_Capitulos/` | `Cap3_Metodologia_v0.7.md` |
| Documentar herramientas, modelo de datos y asistente de IA (S8-01 a S8-03) | Diego | Bóveda, `07_Flujos_Diseno/` | Tres notas nuevas, una por tarea |
| **Viernes 4-dic: corte de decisión** (ver la sección 4) | Victor, con Claude | Bóveda y app Bitácora Torvesa | Escenario elegido, anotado en la bitácora y en la app |

### Escenario A · la tutora acepta la DEC-21 hasta el viernes 4-dic

**Fecha límite para la validación completa: arrancar el miércoles 9-dic.**

| Semana | Tareas | Responsable | Dónde | Entregable |
|---|---|---|---|---|
| 2 · 7 a 13-dic | Acta de la reunión y DEC-21 en la app. Autorización escrita de Torvesa hasta el martes 8. Capacitación corta el miércoles 9 y arranque de la operación el mismo día. Monitoreo diario. CP-04 si se acepta la DEC-23. Capítulo III final según el acta | Claude (acta), Diego (Torvesa y monitoreo), Victor y Diego (capacitación), Victor (Cap. III) | Bóveda; oficina de Torvesa; servidor de Diego | Acta en `08_Reuniones_Tutora/`; autorización; registro diario de la operación |
| 3 · 14 a 20-dic | Sigue la operación y el monitoreo. Pruebas de carga simuladas (S9-03). Victor cierra el Cap. IV con la línea base, si Torvesa entregó los datos. **Viernes 18-dic: borrador 5 a la tutora** (todo menos los resultados de la validación) | Diego (operación y pruebas), Victor (Cap. IV), Claude (armado del borrador 5) | Servidor de Diego; bóveda; correo UPS | Borrador 5 en Word y PDF |
| 4 · 21 a 27-dic | Lunes 21 y martes 22: últimos días de operación. Martes 22: congelar y respaldar el registro y verificar la integridad. Miércoles 23: medición «después» con el registro y los casos de prueba. 24 y 25: baja carga | Diego (cierre del registro), Victor y Diego (medición) | Servidor de Diego; bóveda | Registro congelado; carpeta Post en `05_Datos_Campo/` (aún no existe; se crea el 22-dic) |
| 5 · 28-dic a 3-ene | Análisis antes y después, Cap. V–VI con resultados, citas y APA (H-01). 31-dic y 1-ene: baja carga. Sábado 2 y domingo 3: lectura completa | Victor (análisis y capítulos), Claude (tablas, figuras y revisión de citas), Diego (anexos técnicos) | Bóveda | Tesis completa |
| Lunes 4-ene | Enviar la tesis completa a la tutora (D5) | Victor | Correo UPS | Correo enviado |

### Escenario B · la tutora responde entre el 7 y el 11-dic

**Fecha límite: arrancar el lunes 14-dic con la versión corta de una semana.** Si la respuesta llega después del miércoles 9-dic, ya no caben las dos semanas.

| Semana | Tareas | Responsable | Dónde | Entregable |
|---|---|---|---|---|
| 2 · 7 a 13-dic | Se sigue como en C (casos de prueba, documentación y capítulos). Al llegar la respuesta: acta, pedido de autorización con fecha fija al 14-dic y material de capacitación | Claude (acta), Diego (Torvesa), Victor y Claude (capacitación) | Bóveda; canal de Diego con Torvesa | Acta; autorización hasta el viernes 11-dic |
| 3 · 14 a 20-dic | Capacitación y arranque el lunes 14. Operación del 14 al 18 (y el 21 y 22 si hace falta). **Viernes 18-dic: borrador 5 a la tutora** | Diego (operación), Victor y Diego (capacitación), Claude (borrador 5) | Oficina de Torvesa; servidor de Diego; correo UPS | Registro de la operación; borrador 5 |
| 4 · 21 a 27-dic | Martes 22: cierre del registro. Miércoles 23: medición «después». 24 y 25: baja carga. Resultados descriptivos (con una semana, M1 y M3 se informan solo de forma descriptiva) | Diego (cierre), Victor y Diego (medición) | Servidor de Diego; bóveda | Carpeta Post en `05_Datos_Campo/` |
| 5 · 28-dic a 3-ene | Igual que en A, más la limitación de la semana corta en la discusión | Victor, Claude, Diego | Bóveda | Tesis completa |
| Lunes 4-ene | Enviar la tesis completa | Victor | Correo UPS | Correo enviado |

**Si la autorización de Torvesa no llega hasta el lunes 14-dic, se pasa a C aunque la tutora haya respondido.**

### Escenario C · la tutora no responde hasta el viernes 11-dic (o Torvesa no autoriza hasta el 14-dic)

No hay validación con solicitudes reales. **La tesis valida el diseño con los casos de prueba, las pruebas simuladas y los documentos de Torvesa que lleguen, y lo declara como limitación.** Se apoya en el aviso de la directora de carrera del 2-nov (no recoger datos de personas), que ya está en la bóveda.

| Semana | Tareas | Responsable | Dónde | Entregable |
|---|---|---|---|---|
| 2 · 7 a 13-dic | Terminar los casos de prueba CP-01 a CP-03 y CP-04 como evaluación heurística (marcada `[DECIDIR-TUTORA: DEC-23]`). Pruebas de carga y de uso simuladas (S9-03). Línea base de M1 y M3 solo con los documentos de Torvesa, si llegan. Si el viernes 4-dic no hubo respuesta: Victor escribe a la dirección de carrera pidiendo orientación | Diego (pruebas), Victor (casos cruzados y correo a la dirección), Claude (borrador del correo y tablas de resultados) | Copia local con datos ficticios; bóveda; correo UPS | Resultados por caso en `07_Flujos_Diseno/Resultados_Casos_Prueba/` |
| 3 · 14 a 20-dic | Cap. V con los resultados de los casos de prueba y las pruebas simuladas. Cap. III y Cap. I ajustados: M1 y M3 quedan como «diseño listo para medirse» y se explica cómo se medirían. Manual básico de usuario (S8-05). **Viernes 18-dic: borrador 5 a la tutora**, completo | Victor (capítulos), Claude (redacción de apoyo y armado), Diego (manual y anexos) | Bóveda; correo UPS | Borrador 5 en Word y PDF |
| 4 · 21 a 27-dic | Discusión y limitaciones, conclusiones (Cap. VI), citas y APA (H-01). 24 y 25: baja carga | Victor, Claude | Bóveda | Cap. V–VI completos |
| 5 · 28-dic a 3-ene | Integración, coherencia entre capítulos, figuras y anexos. 31-dic y 1-ene: baja carga. 2 y 3-ene: lectura completa | Victor, Diego, Claude | Bóveda | Tesis completa |
| Lunes 4-ene | Enviar la tesis completa, con una nota que diga qué quedó sin el visto bueno de la tutora | Victor | Correo UPS | Correo enviado |

**Qué se pierde en C:** no hay datos de operación real para M1 y M3; la tesis muestra que el diseño cumple en pruebas controladas, no en la empresa. **Qué no se pierde:** M2, M4 y M5 se miden igual con los casos de prueba, y el diseño, la viabilidad y el cumplimiento de la LOPDP no cambian.

## 4. Fecha de corte recomendada: viernes 4-dic

Ese día, Victor (con Claude) revisa tres cosas y anota el resultado en la bitácora y en la app:

1. **¿Respondió la tutora a la DEC-21?** Si sí y acepta → escenario A. Si dice que no → escenario A con los instrumentos de personas (C1, I1 y SUS) y consentimiento.
2. **¿Torvesa autorizó por escrito o dio una fecha?** Si no hay respuesta, Diego insiste ese día y se fija el lunes 14-dic como último plazo.
3. **¿Llegaron los datos de Torvesa para la línea base?** Si no, M1 y M3 quedan como descriptivos o sin medir, en cualquier escenario.

**Qué hacer según lo que haya:**
- **Tutora sí y Torvesa sí:** escenario A. Diego confirma la capacitación para el miércoles 9-dic.
- **Tutora sí y Torvesa no:** se espera a Torvesa hasta el 14-dic (versión corta, escenario B).
- **Tutora no responde:** se queda en espera activa hasta el viernes 11-dic, trabajando en lo de C. Victor escribe ese mismo 4-dic a la dirección de carrera. **El viernes 11-dic es el segundo y último corte:** sin respuesta, se cierra en C.

## 5. Lo que Claude puede adelantar sin la tutora

1. **Capítulo III v0.7** con la medición sin datos de personas, marcado como propuesta en espera de la DEC-21, y la variante con instrumentos de personas lista por si dice que no.
2. **Las dos versiones de la parte de validación del Cap. V:** con validación en Torvesa (A o B) y solo con casos de prueba (C), con la limitación ya redactada.
3. **Plantillas de resultados** por caso de prueba (CP-01 a CP-04) en `07_Flujos_Diseno/Resultados_Casos_Prueba/`, para que Diego y Victor solo llenen las cifras.
4. **Revisión de citas (H-01):** cruzar las 23 `[FALTA-FUENTE]` con las fichas de `02_Fuentes/` y decir cuáles se cierran, cuáles se quitan y cuáles hay que buscar.
5. **Lista de los 55 `[FALTA-DATO]`** separada por quién los puede cerrar: Torvesa, Diego, Victor o nadie (y entonces se reescribe la frase).
6. **Material de capacitación** de una página para el equipo comercial de Torvesa, para tenerlo listo si se va a A o B.
7. **Borrador del correo a la dirección de carrera** para el 4-dic, por si la tutora no responde.
8. **Acta de la Revisión 2** en cuanto haya reunión, y la actualización de la app Bitácora Torvesa.
9. **Coherencia entre capítulos:** cifras del Excel v0.3 (Premium 270, VAN 380, TIR 24,6 %, censo 1 de 22) en todos los capítulos, y la estructura del cronograma alineada con la de la tesis (el diseño está en el Cap. IV, no en un Cap. 5 aparte).
10. **Borrador 5** en Word y PDF para el 18-dic, armado con `estilo_docx.py`.

Claude **no** puede adelantar: los casos de prueba (los ejecutan Diego y Victor), la autorización ni los datos de Torvesa, ni ninguna decisión DEC.

---

*No se revisó:* la app Bitácora Torvesa (ArtifactData), `Cronograma_Tesis.xlsx` por dentro ni el repositorio de Diego; si allí hay avances de Diego o una respuesta de Torvesa, cambian los estados de S7-02, S8-01 a S8-04 y la fecha de A.
