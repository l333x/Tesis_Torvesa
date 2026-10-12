---
titulo: Cronograma maestro — Tesis Torvesa
tipo: documento_vivo
actualizado: 2026-10-11
escenario_vigente: B
tags: [cronograma, planificacion]
---

# Cronograma maestro

> [!info] Cómo se usa
> - Cada tarea tiene un **ID** (`S1-03`), un responsable (`@Victor` / `@Diego`), un entregable, un criterio de **hecho** y su **issue** de GitHub (`#n`).
> - **Al cerrar:** se marca `[x]`, se pone la fecha real en `cierre:`, se cierra el issue (o el commit lleva `closes #n`) y se agrega la fila en `09_Registro_Contribuciones`.
> - **Este archivo y los issues van sincronizados.** Si cambia uno, se actualiza el otro (el informe semanal avisa si hay diferencias).
> - Formato de línea (lo lee el script de informes; no cambiar el orden):
>   `- [ ] **ID** Tarea · @Resp · entregable: … · hecho: … · cierre: — · #n`

## Escenarios

| | **B (base)** | **A (si la tutora confirma el 15-dic como fecha dura)** |
|---|---|---|
| Cierre (S9–S10) | 7–20 dic | **7–11 dic** |
| Hito del 90 % | 18 dic | **11 dic** |
| Entrega | 4–8 ene | **15 dic** |
| Holgura APA (21 dic–3 ene) | sí | se adelanta y se hace en paralelo desde S8 |
| Defensa | 1–12 feb | la que fije la carrera |

**Se recorta en el escenario A** (marcado ✂️ en las tareas):
- pruebas de carga simuladas (S9-03);
- solo 2 ciclos de revisión con la tutora en vez de alternarlos a diario (S10-01);
- el pulido APA pasa a revisión por capítulo durante S8–S9;
- el manual de usuario queda en versión básica (S8-05).

**Intocable en cualquier escenario:** el trabajo de campo de S1, las revisiones 1 y 2 con la tutora, la medición post del piloto y el hito del 90 %.

**Piloto (validación del diseño en operación experimental controlada):** del **24 nov al 5 dic** (2 semanas hábiles), con medición post del **7 al 9 dic**. Así funciona en los dos escenarios. Depende de la prueba de concepto estable (S5-04) y del permiso de Torvesa.

## Carga y contingencia

- **Carga:** entre semana, bloques de 1–2 h; fin de semana, 3–4 h. Ninguna semana pide más de unas 12 h por persona.
- **Si se pierde una semana, se recorta en este orden:**
  1. lo marcado ✂️;
  2. el inventario de herramientas pasa a una tabla corta (S2-06);
  3. 2 casos de prueba en vez de 3;
  4. la matriz de riesgos baja a 10 riesgos;
  5. se fusiona la documentación del sistema con el capítulo de resultados.
- **Nunca se recorta:** el campo, las revisiones con la tutora, la medición post, el hito del 90 % ni la verificación de fuentes de lo que se cita.

---

## S1 · 12–18 oct · Levantamiento
- [ ] **S1-01** Fase 1 de fuentes: problema, M2 y Oldroyd · @Victor · entregable: fichas en 02_Fuentes + reporte diario · hecho: A1–A10 y A4 con estado definido · cierre: — · #1
- [ ] **S1-02** Fase 1 de fuentes: metodología, LOPDP, SUS e IA 2023–2026 · @Victor · entregable: fichas + C1 v0.2 + I1 v0.2 (SUS validada) · hecho: A39–A47 con estado · cierre: — · #2
- [ ] **S1-03** Corte de la fase 1 y matriz afirmación → fuentes → estado · @Victor · entregable: 03_Matriz_Objetivos/matriz_afirmaciones · hecho: las 47 con estado; lista de qué entra al Cap. 1 · cierre: — · #3
- [ ] **S1-04** Corregir los instrumentos v0.1 → v0.2 · @Victor · entregable: 04_Instrumentos v0.2 · hecho: aprobados por Víctor e impresos · cierre: — · #4
- [ ] **S1-05** Permisos de gerencia (cronometraje, muestra documental, lista de clientes) · @Victor · entregable: autorización C1-C firmada · hecho: firmada y escaneada en _crudo · cierre: — · #5
- [ ] **S1-06** Confirmar con Torvesa el giro del negocio (vías / edificación / inmuebles) · @Victor · entregable: nota en 08 o 11 · hecho: A1–A1d resueltas y [VOCAB] reemplazado · cierre: — · #6
- [ ] **S1-07** Correo a la tutora: datos simulados, D2, D5 y D6 · @Victor · entregable: correo enviado + copia en 08 · hecho: respuesta recibida o reunión agendada · cierre: — · #7
- [ ] **S1-08** Campo: I1 colaboradores + I3 entrevistas (jue 15) · @Victor · entregable: hojas + registro P1 · hecho: registro P1 completo para cada aplicación · cierre: — · #8
- [ ] **S1-09** Campo: I2 clientes + cronometraje P2-A + muestra P2-B (jue 15–vie 16) · @Diego · entregable: P2A/P2B csv + registro P1 · hecho: todas las cotizaciones observables registradas · cierre: — · #9
- [ ] **S1-10** Aceptar la invitación, clonar y levantar el RAG · @Diego · entregable: commit de prueba de Diego · hecho: `rag.py consultar` funciona en su PC · cierre: — · #10
- [ ] **S1-11** Analizar la bóveda 1 y extraer ideas para la bóveda del sistema · @Diego · entregable: 07_Flujos_Diseno/ideas_boveda1.md · hecho: lista de patrones reutilizables y descartados · cierre: — · #11
- [ ] **S1-12** Tabulación y consolidación con el protocolo de procedencia (fin de semana) · @Victor @Diego · entregable: 05_Datos_Campo/LineaBase_2026-10 · hecho: csv anonimizados + hashes + auditoría PII en 0 · cierre: — · #12

## S2 · 19–25 oct · Redacción por capítulos
- [ ] **S2-01** Capítulo 1 (lun–mar) · @Victor · entregable: 06_Capitulos/Cap1_v0.1 · hecho: cada cifra con ficha verificada · cierre: — · #13
- [ ] **S2-02** Capítulo 2 (mié–jue) · @Victor · entregable: Cap2_v0.1 · hecho: marco teórico con fuentes verificadas · cierre: — · #14
- [ ] **S2-03** Capítulo 3 (sáb–dom) · @Victor · entregable: Cap3_v0.1 · hecho: metodología coherente con D1/D2 · cierre: — · #15
- [ ] **S2-04** Análisis de los datos de campo (descriptivo) · @Diego · entregable: 05_Datos_Campo/analisis + script · hecho: línea base M1–M4 y M6 calculada y reproducible · cierre: — · #16
- [ ] **S2-05** Mapa del proceso AS-IS (BPMN) · @Diego · entregable: 07_Flujos_Diseno/AS-IS · hecho: validado contra las entrevistas I3 · cierre: — · #17
- [ ] **S2-06** Inventario de herramientas candidatas con criterios · @Diego · entregable: 07_Flujos_Diseno/inventario_herramientas · hecho: ≥ 3 opciones por componente con criterios · cierre: — · #18

## S3 · 26–30 oct · Revisión 1 con la tutora
- [ ] **S3-01** Presentar el avance (Cap. 1–3 + respaldo bibliográfico) · @Victor · entregable: presentación · hecho: reunión realizada · cierre: — · #19
- [ ] **S3-02** Acta de la Revisión 1 · @Victor · entregable: 08_Reuniones_Tutora/acta · hecho: observaciones con responsable y plazo · cierre: — · #20
- [ ] **S3-03** AS-IS y datos listos para mostrar · @Diego · entregable: figuras exportadas · hecho: incluidas en la presentación · cierre: — · #21

## S4 · 2–8 nov · Diseño
- [ ] **S4-01** Flujogramas TO-BE (2–4 nov) · @Diego · entregable: 07_Flujos_Diseno/TO-BE · hecho: cubren los 6 pasos del Anexo A.5 · cierre: — · #22
- [ ] **S4-02** Validar el TO-BE contra los requisitos · @Victor · entregable: comentarios en los flujos · hecho: cada requisito trazado a un flujo · cierre: — · #23
- [ ] **S4-03** Levantar la bóveda del sistema desde los flujos aprobados (5–8 nov) · @Diego · entregable: repo o carpeta de la bóveda del sistema · hecho: estructura A.3 + plantillas A.4 funcionando · cierre: — · #24
- [ ] **S4-04** Requisitos funcionales y no funcionales · @Victor · entregable: documento de requisitos · hecho: cada requisito con origen (hallazgo o norma) · cierre: — · #25
- [ ] **S4-05** Matriz de decisión de herramientas (Excel con fórmulas vivas) · @Victor · entregable: .xlsx · hecho: ponderaciones y sensibilidad · cierre: — · #26
- [ ] **S4-06** CAPEX / OPEX · @Victor · entregable: hoja de costos · hecho: cada precio con fuente y fecha · cierre: — · #27

## S5 · 9–15 nov · Mejora continua
- [ ] **S5-01** VAN / TIR del sistema para Torvesa · @Victor · entregable: modelo financiero · hecho: supuestos con fuente + sensibilidad · cierre: — · #28
- [ ] **S5-02** Matriz de riesgos · @Victor · entregable: matriz · hecho: probabilidad × impacto + mitigación · cierre: — · #29
- [ ] **S5-03** Capítulo de normativa (LOPDP) · @Victor · entregable: sección · hecho: artículos del texto oficial · cierre: — · #30
- [ ] **S5-04** Prueba de concepto: front conversacional → back → bóveda · @Diego · entregable: PoC funcionando · hecho: flujo de punta a punta demostrable · cierre: — · #31
- [ ] **S5-05** Diseño de los 3 casos de prueba · @Diego · entregable: casos con criterios de aceptación · hecho: aprobados por Víctor · cierre: — · #32

## S6 · 16–22 nov · Revisión 2 con la tutora
- [ ] **S6-01** Presentar diseño, flujos, datos y viabilidad · @Victor @Diego · entregable: presentación · hecho: reunión realizada · cierre: — · #33
- [ ] **S6-02** Acta de la Revisión 2 · @Victor · entregable: acta en 08 · hecho: observaciones con responsable y plazo · cierre: — · #34

## S7 · 23–29 nov · Feedback + arranque del piloto
- [ ] **S7-01** Incorporar las observaciones de la Revisión 2 · @Victor @Diego · entregable: versiones nuevas · hecho: cada observación cerrada en el acta · cierre: — · #35
- [ ] **S7-02** Preparar la validación controlada (protocolo, capacitación, permisos) · @Victor · entregable: protocolo del piloto · hecho: aprobado por Torvesa · cierre: — · #36
- [ ] **S7-03** Arrancar el piloto (24-nov) y monitorear · @Diego · entregable: registro de eventos activo · hecho: primeros eventos registrados sin errores · cierre: — · #37

## S8 · 30 nov–6 dic · Documentación del sistema (el piloto sigue hasta el 5-dic)
- [ ] **S8-01** Herramientas elegidas y descartadas, con justificación · @Diego · entregable: documento · hecho: cada decisión con criterio · cierre: — · #38
- [ ] **S8-02** Modelo de datos y registro de eventos · @Diego · entregable: diagrama + diccionario · hecho: coincide con la PoC · cierre: — · #39
- [ ] **S8-03** Plantillas de cotización y especificación del asistente de IA · @Diego · entregable: documentos · hecho: revisados por Víctor · cierre: — · #40
- [ ] **S8-04** Ejecutar los casos de prueba · @Diego · entregable: resultados · hecho: tasa de aprobación por caso · cierre: — · #41
- [ ] **S8-05** ✂️ Manual básico de usuario · @Diego · entregable: manual · hecho: un usuario de Torvesa lo puede seguir · cierre: — · #42

## S9–S10 · 7–20 dic · Cierre (escenario A: 7–11 dic)
- [ ] **S9-01** Medición post (7–9 dic) · @Victor @Diego · entregable: datos post con registro P1 · hecho: los mismos instrumentos e indicadores que la línea base · cierre: — · #43
- [ ] **S9-02** Análisis pre-post · @Victor · entregable: capítulo de resultados · hecho: pruebas según el borrador + tamaño del efecto · cierre: — · #44
- [ ] **S9-03** ✂️ Pruebas de uso y de carga simuladas con scripts · @Diego · entregable: reporte · hecho: escenarios documentados y reproducibles · cierre: — · #45
- [ ] **S10-01** ✂️ Ciclos con la tutora (un día revisión, un día corrección) · @Victor · entregable: actas · hecho: observaciones cerradas · cierre: — · #46
- [ ] **S10-02** HITO: tesis al 90 % (B: 18-dic · A: 11-dic) · @Victor @Diego · entregable: documento completo · hecho: todos los capítulos + bibliografía verificada · cierre: — · #47

## Holgura · 21 dic–3 ene
- [ ] **H-01** Revisión APA, citas y bibliografía (bloques cortos) · @Victor · entregable: tesis pulida · hecho: 0 citas sin ficha verificada · cierre: — · #48

## Entrega · 4–8 ene (escenario A: 15-dic)
- [ ] **E-01** Revisión final, aprobación y firma de la tutora · @Victor · entregable: tesis firmada · hecho: firmada · cierre: — · #49
- [ ] **E-02** Entrega a la carrera · @Victor @Diego · entregable: comprobante · hecho: comprobante de entrega · cierre: — · #50

## Defensa · 11 ene–12 feb
- [ ] **D-01** Resumen de contribuciones (quién hizo qué) · @Victor @Diego · entregable: documento desde 09 · hecho: aprobado por los dos · cierre: — · #51
- [ ] **D-02** División de la exposición + simulacros + banco de preguntas del tribunal · @Victor @Diego · entregable: guion + banco · hecho: ≥ 2 simulacros cronometrados · cierre: — · #52
- [ ] **D-03** Defensa (1–12 feb) · @Victor @Diego · entregable: — · hecho: aprobada · cierre: — · #53
