---
titulo: Cronograma maestro (versión para la IA)
tipo: documento_vivo
actualizado: 2026-10-19
fuente_de_verdad: 11_Planificacion/Cronograma_Tesis.xlsx
tags: [cronograma, planificacion]
---

# Cronograma maestro — versión para la IA

> [!info] Las personas usan `Cronograma_Tesis.xlsx`. Este archivo se regenera desde el Excel (`generar_cronograma.py --md`).
> Las líneas de «Entregables» las lee `sincronizar_github.py` (formato fijo: no editar a mano).

## Entregables (= issues de GitHub)
- [ ] **S1-01** Buscar y verificar fuentes del problema (tiempo de respuesta, digitalización de la construcción, datos de Torvesa), para respaldar el capítulo 1 · @Victor · entregable: fichas en 02_Fuentes/Problema/ · hecho: afirmaciones A1–A10 con estado definido · cierre: — · #1
- [ ] **S1-02** Buscar fuentes de metodología, ley de datos (LOPDP), escala SUS en español e IA 2023–2026, para justificar el método · @Victor · entregable: fichas en 02_Fuentes/Metodologia/, 02_Fuentes/Normativa/ y 02_Fuentes/Tecnologia_IA/ · hecho: afirmaciones A39–A47 con estado · cierre: — · #2
- [x] **S1-03** Armar la matriz afirmación–fuente–estado (corte del miércoles), para decidir qué entra al capítulo 1 · @Victor · entregable: 03_Matriz_Objetivos/2026-10-14_Matriz_Afirmaciones_v0.1.xlsx · hecho: las 47 afirmaciones con estado · cierre: — · #3
- [x] **S1-04** Corregir los instrumentos de campo a la versión 0.2, para aplicarlos en Torvesa · @Victor · entregable: 04_Instrumentos/2026-10-14_*_v0.2 · hecho: aprobados por Víctor e impresos · cierre: — · #4
- [ ] **S1-05** Pedir a Torvesa el permiso de campo, la nota de respaldo y el catálogo de servicios, para trabajar con datos oficiales · @Victor · entregable: correo enviado + respuesta · hecho: respuesta recibida o plazo vencido el 14-oct · cierre: — · #5
- [ ] **S1-06** Confirmar con Torvesa a qué se dedica (vías, edificios, inmuebles), para usar las palabras correctas en encuestas y tesis · @Victor · entregable: respuesta de Torvesa · hecho: afirmaciones A1–A1d resueltas · cierre: — · #6
- [ ] **S1-07** Conversar con la tutora sobre los 5 cambios, para tener su aprobación antes de la Revisión 1 · @Victor · entregable: 08_Reuniones_Tutora/2026-10-12_Acta_Conversacion.md · hecho: acta con sus respuestas · cierre: — · #7
- [ ] **S1-08** Aplicar la encuesta, las entrevistas y la encuesta a clientes en Torvesa (si autoriza), para tener la línea base real · @Victor · entregable: 05_Datos_Campo/LineaBase_2026-10/registro_aplicacion.csv · hecho: cada aplicación en el registro de procedencia · cierre: — · #8
- [ ] **S1-09** Cronometrar cotizaciones y revisar solicitudes pasadas en Torvesa (si autoriza), para medir los tiempos reales · @Diego · entregable: 05_Datos_Campo/LineaBase_2026-10/P2A_cronometraje.csv y P2B_muestra_documental.csv · hecho: todas las cotizaciones observables registradas · cierre: — · #9
- [ ] **S1-10** Aceptar la invitación, clonar el repo y levantar el buscador RAG, para trabajar en la bóveda compartida · @Diego · entregable: commit de prueba de Diego en GitHub · hecho: rag.py consultar funciona en su PC · cierre: — · #10
- [ ] **S1-12** Tabular y anonimizar los datos de campo con el protocolo de procedencia, para que sean confiables · @Victor @Diego · entregable: 05_Datos_Campo/LineaBase_2026-10/ · hecho: auditoría de datos personales en 0 · cierre: — · #12
- [ ] **S1-13** Investigar cómo consolidar bóvedas de conocimiento y arquitecturas RAG para negocio, para diseñar la bóveda del sistema · @Diego · entregable: fichas en 02_Fuentes/Tecnologia_IA/ + resumen de 1 página · hecho: ≥10 fichas y resumen leído por Víctor · cierre: — · #54
- [ ] **S1-14** Investigar flujos de información y diseño de procesos (BPMN), para dibujar los procesos de Torvesa · @Diego · entregable: fichas en 02_Fuentes/Metodologia/ · hecho: ≥5 fichas · cierre: — · #55
- [ ] **S1-15** Investigar CRMs móviles y herramientas existentes con sus precios, para comparar opciones y calcular costos · @Diego · entregable: fichas en 02_Fuentes/Casos_Estudio/ y 02_Fuentes/Costos_Viabilidad/ · hecho: ≥6 herramientas con precio y fecha de consulta · cierre: — · #56
- [ ] **S1-16** Revisar el sprint 1 y planificar el sprint 2 · @Victor @Diego · entregable: 11_Planificacion/Bitacora_Semanal.md · hecho: sección de la semana escrita · cierre: — · #57
- [ ] **S2-01** Escribir el capítulo 1 (problema, justificación, objetivos), para tener el primer borrador · @Victor · entregable: 06_Capitulos/2026-10-20_Cap1_Problema_v0.1.docx · hecho: cada cifra con ficha verificada · cierre: — · #13
- [ ] **S2-02** Escribir el capítulo 2 (marco teórico), para sustentar el diseño · @Victor · entregable: 06_Capitulos/2026-10-22_Cap2_Marco_Teorico_v0.1.docx · hecho: solo fuentes verificadas · cierre: — · #14
- [ ] **S2-03** Escribir el capítulo 3 (metodología), para explicar cómo se investiga · @Victor · entregable: 06_Capitulos/2026-10-25_Cap3_Metodologia_v0.1.docx · hecho: coherente con las decisiones D1 y D2 · cierre: — · #15
- [ ] **S2-04** Analizar los datos de campo (tablas y gráficos), para la línea base de las metas · @Diego · entregable: 05_Datos_Campo/LineaBase_2026-10/analisis/ · hecho: línea base de M1–M4 y M6 calculada · cierre: — · #16
- [ ] **S2-05** Dibujar el proceso actual de Torvesa (AS-IS) en BPMN, para ver dónde se pierde tiempo · @Diego · entregable: 07_Flujos_Diseno/2026-10-22_AS-IS_v0.1 · hecho: validado con lo dicho en las entrevistas · cierre: — · #17
- [ ] **S2-06** Hacer el inventario de herramientas candidatas con criterios, para elegir con argumentos · @Diego · entregable: 07_Flujos_Diseno/2026-10-24_Inventario_Herramientas_v0.1.xlsx · hecho: ≥3 opciones por componente · cierre: — · #18
- [ ] **S2-07** Armar el lienzo del modelo de negocio y la propuesta de valor, para explicar cómo se vende la idea · @Victor · entregable: 06_Capitulos/Modelo_Negocio/2026-10-23_Lienzo_Modelo_Negocio_v0.1.docx · hecho: 9 bloques completos · cierre: — · #58
- [ ] **S2-08** Revisar el sprint 2 y planificar el sprint 3 · @Victor @Diego · entregable: 11_Planificacion/Bitacora_Semanal.md · hecho: sección de la semana escrita · cierre: — · #59
- [ ] **S3-01** Presentar el avance a la tutora (capítulos 1–3 y fuentes) en la Revisión 1 · @Victor · entregable: 08_Reuniones_Tutora/presentación · hecho: reunión realizada · cierre: — · #19
- [ ] **S3-02** Escribir el acta de la Revisión 1 y corregir según sus observaciones · @Victor · entregable: 08_Reuniones_Tutora/acta + capítulos v0.2 · hecho: cada observación con responsable y plazo · cierre: — · #20
- [ ] **S3-03** Preparar el proceso actual y las gráficas de datos para mostrarlos en la Revisión 1 · @Diego · entregable: 07_Flujos_Diseno/figuras · hecho: incluidas en la presentación · cierre: — · #21
- [ ] **S3-04** Escribir cómo estructuré mi bóveda 1 (patrones, no datos), para que Diego diseñe la bóveda del sistema · @Victor · entregable: 07_Flujos_Diseno/2026-10-30_Patrones_Boveda1_v0.1.docx · hecho: Diego lo leyó y anotó preguntas · cierre: — · #60
- [ ] **S3-05** Revisar el sprint 3 y explicarle a Diego los conceptos de negocio · @Victor @Diego · entregable: 11_Planificacion/Bitacora_Semanal.md · hecho: sesión hecha con Conceptos_Negocio.pdf · cierre: — · #61
- [ ] **S4-01** Dibujar los procesos con el sistema (TO-BE), para definir cómo funcionará · @Diego · entregable: 07_Flujos_Diseno/2026-11-04_TO-BE_v0.1 · hecho: cubren los 6 pasos del flujo de atención · cierre: — · #22
- [ ] **S4-02** Validar los procesos TO-BE contra los requisitos · @Victor · entregable: comentarios en 07_Flujos_Diseno/ · hecho: cada requisito ligado a un flujo · cierre: — · #23
- [ ] **S4-03** Construir la bóveda del sistema a partir de los flujos aprobados · @Diego · entregable: 07_Flujos_Diseno/Boveda_Sistema/ · hecho: estructura y plantillas funcionando · cierre: — · #24
- [ ] **S4-04** Escribir los requisitos funcionales y no funcionales · @Victor · entregable: 06_Capitulos/2026-11-03_Requisitos_v0.1.docx · hecho: cada requisito con su origen · cierre: — · #25
- [ ] **S4-05** Armar la matriz de decisión de herramientas en Excel (fórmulas vivas) · @Victor · entregable: 06_Capitulos/Modelo_Negocio/2026-11-05_Matriz_Decision_Herramientas_v0.1.xlsx · hecho: ponderaciones y sensibilidad · cierre: — · #26
- [ ] **S4-06** Calcular CAPEX (inversión) y OPEX (gasto mensual) con fuente para cada precio · @Victor · entregable: 06_Capitulos/Modelo_Negocio/2026-11-07_Modelo_Financiero_v0.1.xlsx (hoja Costos) · hecho: cada precio con enlace y fecha · cierre: — · #27
- [ ] **S4-07** Revisar el sprint 4 y planificar el sprint 5 · @Victor @Diego · entregable: 11_Planificacion/Bitacora_Semanal.md · hecho: sección escrita · cierre: — · #62
- [ ] **S5-01** Calcular beneficios, VAN, TIR y período de recuperación en 3 escenarios con sensibilidad · @Victor · entregable: 06_Capitulos/Modelo_Negocio/Modelo_Financiero (hojas Beneficios y Escenarios) · hecho: supuestos con fuente; 3 escenarios · cierre: — · #28
- [ ] **S5-02** Escribir la matriz de riesgos · @Victor · entregable: 06_Capitulos/2026-11-12_Riesgos_v0.1.xlsx · hecho: probabilidad × impacto + mitigación · cierre: — · #29
- [ ] **S5-03** Escribir el capítulo de normativa (LOPDP) · @Victor · entregable: 06_Capitulos/2026-11-13_Normativa_v0.1.docx · hecho: artículos del texto oficial · cierre: — · #30
- [ ] **S5-04** Construir la prueba de concepto (formulario → servidor → bóveda → borrador de cotización) · @Diego · entregable: repositorio de la prueba de concepto · hecho: flujo completo demostrable · cierre: — · #31
- [ ] **S5-05** Diseñar los 3 casos de prueba · @Diego · entregable: 07_Flujos_Diseno/2026-11-14_Casos_Prueba_v0.1.md · hecho: aprobados por Víctor · cierre: — · #32
- [ ] **S5-06** Escribir el pitch de 1 página para inversionista · @Victor · entregable: 06_Capitulos/Modelo_Negocio/2026-11-14_Pitch_1pagina_v0.1.docx · hecho: una página con VAN, TIR y propuesta de valor · cierre: — · #63
- [ ] **S5-07** Revisar el sprint 5 y planificar el sprint 6 · @Victor @Diego · entregable: 11_Planificacion/Bitacora_Semanal.md · hecho: sección escrita · cierre: — · #64
- [ ] **S6-01** Presentar diseño, flujos, datos y viabilidad a la tutora en la Revisión 2 · @Victor @Diego · entregable: 08_Reuniones_Tutora/presentación · hecho: reunión realizada · cierre: — · #33
- [ ] **S6-02** Escribir el acta de la Revisión 2 · @Victor · entregable: 08_Reuniones_Tutora/acta · hecho: observaciones con responsable y plazo · cierre: — · #34
- [ ] **S6-03** Revisar el sprint 6 y planificar el sprint 7 · @Victor @Diego · entregable: 11_Planificacion/Bitacora_Semanal.md · hecho: sección escrita · cierre: — · #65
- [ ] **S7-01** Incorporar las observaciones de la Revisión 2 · @Victor @Diego · entregable: versiones nuevas de capítulos y flujos · hecho: cada observación cerrada en el acta · cierre: — · #35
- [ ] **S7-02** Preparar la validación del diseño en operación experimental controlada (protocolo, capacitación, permisos) · @Victor · entregable: 04_Instrumentos/protocolo de validación · hecho: aprobado por Torvesa · cierre: — · #36
- [ ] **S7-03** Arrancar la validación del diseño en operación experimental controlada (24-nov) y monitorearla · @Diego · entregable: registro de eventos del sistema · hecho: eventos registrados sin errores · cierre: — · #37
- [ ] **S7-04** Escribir el capítulo de diagnóstico con la línea base real · @Victor · entregable: 06_Capitulos/2026-11-28_Cap4_Diagnostico_v0.1.docx · hecho: solo datos con registro de procedencia · cierre: — · #66
- [ ] **S7-05** Revisar el sprint 7 y planificar el sprint 8 · @Victor @Diego · entregable: 11_Planificacion/Bitacora_Semanal.md · hecho: sección escrita · cierre: — · #67
- [ ] **S8-01** Documentar las herramientas elegidas y descartadas, con justificación · @Diego · entregable: 07_Flujos_Diseno/Herramientas · hecho: cada decisión con criterio · cierre: — · #38
- [ ] **S8-02** Documentar el modelo de datos y el registro de eventos · @Diego · entregable: 07_Flujos_Diseno/Modelo_Datos · hecho: coincide con la prueba de concepto · cierre: — · #39
- [ ] **S8-03** Documentar las plantillas de cotización y la especificación del asistente de IA · @Diego · entregable: 07_Flujos_Diseno/Asistente_IA · hecho: revisadas por Víctor · cierre: — · #40
- [ ] **S8-04** Ejecutar los casos de prueba · @Diego · entregable: 07_Flujos_Diseno/Resultados_Casos_Prueba · hecho: resultado por caso · cierre: — · #41
- [ ] **S8-05** ✂ Escribir el manual básico de usuario · @Diego · entregable: 07_Flujos_Diseno/Manual_Usuario · hecho: un usuario de Torvesa lo puede seguir · cierre: — · #42
- [ ] **S8-06** Escribir el capítulo de diseño del sistema y viabilidad · @Victor · entregable: 06_Capitulos/2026-12-04_Cap5_Diseno_Viabilidad_v0.1.docx · hecho: integra flujos, costos y VAN/TIR · cierre: — · #68
- [ ] **S8-07** Revisar el sprint 8 y planificar el sprint 9 · @Victor @Diego · entregable: 11_Planificacion/Bitacora_Semanal.md · hecho: sección escrita · cierre: — · #69
- [ ] **S9-01** Hacer la medición «después» (7–9 dic) · @Victor @Diego · entregable: 05_Datos_Campo/ (carpeta Post) · hecho: mismos instrumentos e indicadores que la línea base · cierre: — · #43
- [ ] **S9-02** Comparar el antes y el después (análisis pre-post) y escribir resultados · @Victor · entregable: 06_Capitulos/2026-12-12_Cap6_Resultados_v0.1.docx · hecho: pruebas del borrador + tamaño del efecto · cierre: — · #44
- [ ] **S9-03** ✂ Hacer pruebas de uso y de carga simuladas con scripts · @Diego · entregable: 07_Flujos_Diseno/Pruebas_Carga · hecho: escenarios reproducibles · cierre: — · #45
- [ ] **S9-04** Revisar el sprint 9 y planificar el sprint 10 · @Victor @Diego · entregable: 11_Planificacion/Bitacora_Semanal.md · hecho: sección escrita · cierre: — · #70
- [ ] **S10-01** ✂ Ciclos con la tutora (un día revisión, un día corrección) · @Victor · entregable: 08_Reuniones_Tutora/actas · hecho: observaciones cerradas · cierre: — · #46
- [ ] **S10-02** HITO: tener la tesis al 90 % (18-dic; 11-dic en el escenario A) · @Victor @Diego · entregable: 06_Capitulos/tesis completa · hecho: todos los capítulos + bibliografía verificada · cierre: — · #47
- [ ] **S10-03** Revisar el sprint 10 y planificar la holgura · @Victor @Diego · entregable: 11_Planificacion/Bitacora_Semanal.md · hecho: sección escrita · cierre: — · #71
- [ ] **H-01** Revisar APA, citas y bibliografía en bloques cortos · @Victor · entregable: 06_Capitulos/tesis pulida · hecho: 0 citas sin ficha verificada · cierre: — · #48
- [ ] **E-01** Lograr la revisión final, la aprobación y la firma de la tutora · @Victor · entregable: tesis firmada · hecho: firmada · cierre: — · #49
- [ ] **E-02** Entregar la tesis a la carrera · @Victor @Diego · entregable: comprobante de entrega · hecho: comprobante recibido · cierre: — · #50
- [ ] **D-01** Escribir el resumen de contribuciones (quién hizo qué) · @Victor @Diego · entregable: 09_Registro_Contribuciones/ · hecho: aprobado por los dos · cierre: — · #51
- [ ] **D-02** Dividir la exposición, ensayar y armar el banco de preguntas del tribunal · @Victor @Diego · entregable: guion + banco de preguntas · hecho: ≥2 simulacros cronometrados · cierre: — · #52
- [ ] **D-03** Defender la tesis (1–12 feb) · @Victor @Diego · entregable: — · hecho: aprobada · cierre: — · #53

## Tareas día a día

| Sprint | ID | Día | Resp. | Tarea | Dónde | Resultado | Estado | Fecha real |
|---|---|---|---|---|---|---|---|---|
| S1 | S1-T01 | 2026-10-12 | Víctor | Conversar con la tutora sobre los 5 cambios, para tener su aprobación | UPS Quito, en persona · llevar 08_Reuniones_Tutora/2026-10-12_Puntos_Tutora.pdf | Respuestas de la tutora anotadas | Hecho | 2026-10-12 |
| S1 | S1-T02 | 2026-10-12 | Víctor | Escribir el acta de la conversación, para que quede por escrito lo que decidió | 08_Reuniones_Tutora/ | 08_Reuniones_Tutora/2026-10-12_Acta_Conversacion.md | Movido |  |
| S1 | S1-T03 | 2026-10-12 | Víctor | Enviar el correo a Torvesa (giro, nota de respaldo, catálogo, permisos), para trabajar con datos oficiales | Correo electrónico · borrador en 11_Planificacion/2026-10-12_Correo_Torvesa_borrador.docx | Correo enviado con el catálogo adjunto | Movido |  |
| S1 | S1-T04 | 2026-10-12 | Diego | Aceptar la invitación de GitHub y clonar el repo, para trabajar en la bóveda compartida | PC de Diego · pasos en GUIA_DIEGO.pdf (raíz) | Repo clonado + 00_Inbox/hola_diego.md | En curso |  |
| S1 | S1-T05 | 2026-10-12 | Diego | Levantar el buscador RAG en su PC, para consultar la bóveda | PC de Diego · pasos en RAG_README.md (raíz) | Consulta de prueba con resultados | Movido |  |
| S1 | S1-T06 | 2026-10-13 | Víctor | Buscar y verificar fuentes sobre el tiempo de respuesta a clientes (Oldroyd y estudios 2023+), para respaldar el problema (A9, A10) | 02_Fuentes/Problema/ · con 99_Scripts/busqueda/ | ≥5 fichas, ≥2 verificadas con página | En curso |  |
| S1 | S1-T07 | 2026-10-13 | Víctor | Buscar fuentes sobre la digitalización de la construcción, para respaldar el contexto (A5, A6) | 02_Fuentes/Problema/ | ≥4 fichas | Hecho | 2026-10-12 |
| S1 | S1-T08 | 2026-10-13 | Diego | Investigar cómo consolidar bóvedas de conocimiento, para diseñar la bóveda del sistema | 02_Fuentes/Tecnologia_IA/ · con 99_Scripts/busqueda/ | ≥5 fichas | Movido |  |
| S1 | S1-T09 | 2026-10-13 | Diego | Leer el Documento madre y el Glosario, para entender el proyecto completo | 00_DOCUMENTO_MADRE.pdf y Glosario.pdf (raíz) | Dudas anotadas en el issue #10 | Movido |  |
| S1 | S1-T10 | 2026-10-14 | Víctor | Revisar la respuesta de Torvesa y ajustar el campo del jueves y viernes, para saber qué se puede aplicar | Correo · 11_Planificacion/Cronograma_Tesis.xlsx | Campo confirmado o reprogramado | Movido |  |
| S1 | S1-T11 | 2026-10-14 | Víctor | Corregir los instrumentos a la versión 0.2, para aplicarlos en Torvesa | 04_Instrumentos/ | 04_Instrumentos/2026-10-14_*_v0.2 (.md + Word) | Hecho | 2026-10-18 |
| S1 | S1-T12 | 2026-10-14 | Víctor | Hacer el corte de fuentes: armar la matriz afirmación–fuente–estado, para decidir qué entra al capítulo 1 | 03_Matriz_Objetivos/ | 03_Matriz_Objetivos/2026-10-14_Matriz_Afirmaciones_v0.1.xlsx | Hecho | 2026-10-18 |
| S1 | S1-T13 | 2026-10-14 | Diego | Investigar arquitecturas RAG para negocio, para proponer cómo el asistente consultará la bóveda | 02_Fuentes/Tecnologia_IA/ | ≥5 fichas | Movido |  |
| S1 | S1-T14 | 2026-10-14 | Diego | Escribir un resumen de 1 página para Víctor sobre bóvedas y RAG, para compartir lo aprendido | 02_Fuentes/Tecnologia_IA/ | 02_Fuentes/Tecnologia_IA/2026-10-14_Resumen_Bovedas_RAG.md | Movido |  |
| S1 | S1-T15 | 2026-10-15 | Víctor | Aplicar la encuesta a colaboradores y 2 entrevistas en Torvesa (si autorizó), para la línea base real | Torvesa (oficina, Quito) · registro en 05_Datos_Campo/LineaBase_2026-10/ | Hojas firmadas + 05_Datos_Campo/LineaBase_2026-10/registro_aplicacion.csv | Movido |  |
| S1 | S1-T16 | 2026-10-15 | Diego | Cronometrar las cotizaciones del día en Torvesa (si autorizó), para medir el tiempo real (meta M2) | Torvesa (oficina, Quito) | 05_Datos_Campo/LineaBase_2026-10/P2A_cronometraje.csv | Movido |  |
| S1 | S1-T17 | 2026-10-16 | Víctor | Llamar a los clientes para la encuesta corta (si autorizó), para conocer su experiencia | Teléfono · lista solo en 05_Datos_Campo/_crudo/ (privada) | Respuestas codificadas CLI-xx | Movido |  |
| S1 | S1-T18 | 2026-10-16 | Diego | Revisar solicitudes y cotizaciones de los últimos 3 meses (solo fechas y horas), para medir el tiempo de respuesta (meta M1) | Torvesa (oficina, Quito) | 05_Datos_Campo/LineaBase_2026-10/P2B_muestra_documental.csv | Movido |  |
| S1 | S1-T19 | 2026-10-17 | Víctor | Buscar el texto oficial de la ley de datos (LOPDP) y agregar sus artículos al consentimiento, para cumplir la ley | 02_Fuentes/Normativa/ y 04_Instrumentos/ | Ficha LOPDP + consentimiento v0.2 con artículos | Hecho | 2026-10-18 |
| S1 | S1-T20 | 2026-10-17 | Víctor | Buscar la versión validada en español de la escala SUS, para medir la usabilidad correctamente | 02_Fuentes/Metodologia/ | Ficha verificada + encuesta I1 v0.2 con la traducción | Hecho | 2026-10-18 |
| S1 | S1-T21 | 2026-10-17 | Víctor | Buscar fuentes de metodología (DSR, Design Thinking, Scrum, censo), para justificar el método | 02_Fuentes/Metodologia/ | ≥6 fichas | En curso |  |
| S1 | S1-T22 | 2026-10-17 | Diego | Investigar flujos de información y diseño de procesos (BPMN), para dibujar el proceso de Torvesa | 02_Fuentes/Metodologia/ | ≥5 fichas | Movido |  |
| S1 | S1-T23 | 2026-10-17 | Diego | Investigar CRMs móviles y herramientas existentes con sus precios, para comparar y calcular costos | 02_Fuentes/Casos_Estudio/ y 02_Fuentes/Costos_Viabilidad/ | Tabla de ≥6 herramientas con precio y fecha | Movido |  |
| S1 | S1-T24 | 2026-10-18 | Ambos | Tabular y anonimizar los datos de campo, para que estén listos y sean confiables | 05_Datos_Campo/LineaBase_2026-10/ | CSV anonimizados + hashes + auditoría | Movido |  |
| S1 | S1-T25 | 2026-10-18 | Víctor | Escribir un resumen de 1 página para Diego sobre el problema y sus fuentes | 02_Fuentes/Problema/ | 02_Fuentes/Problema/2026-10-18_Resumen_Problema.md | Hecho | 2026-10-18 |
| S1 | S1-T26 | 2026-10-18 | Diego | Escribir un resumen de 1 página para Víctor sobre CRMs y flujos | 02_Fuentes/Casos_Estudio/ | 02_Fuentes/Casos_Estudio/2026-10-18_Resumen_CRM_Flujos.md | Movido |  |
| S1 | S1-T27 | 2026-10-18 | Ambos | Revisar el sprint (qué hicimos, qué no, qué aprendimos), hacer 20 min de «explícame lo tuyo» y planificar el siguiente | Llamada Víctor–Diego · 11_Planificacion/Bitacora_Semanal.md y 11_Planificacion/Cronograma_Tesis.xlsx | Sección de la semana en la bitácora + hoja del sprint siguiente ajustada | En curso |  |
| S2 | S2-T01 | 2026-10-19 | Víctor | Escribir el capítulo 1, parte 1 (problema y evidencias), para tener el primer borrador | 06_Capitulos/ | Cap1 v0.1 (primera mitad) | En curso |  |
| S2 | S2-T02 | 2026-10-19 | Diego | Analizar los datos de campo (tablas y gráficos simples), para calcular la línea base | 05_Datos_Campo/LineaBase_2026-10/ | 05_Datos_Campo/LineaBase_2026-10/analisis/ (tablas y script) | Pendiente |  |
| S2 | S2-T03 | 2026-10-20 | Víctor | Escribir el capítulo 1, parte 2 (justificación y objetivos) | 06_Capitulos/ | 06_Capitulos/2026-10-20_Cap1_Problema_v0.1.docx | En curso |  |
| S2 | S2-T04 | 2026-10-20 | Diego | Terminar el análisis de datos y escribir lo que muestran, en lenguaje simple | 05_Datos_Campo/LineaBase_2026-10/ | 05_Datos_Campo/LineaBase_2026-10/analisis/2026-10-20_Resultados_LineaBase_v0.1.md | Pendiente |  |
| S2 | S2-T05 | 2026-10-21 | Víctor | Escribir el capítulo 2, parte 1 (CRM, tiempo de respuesta, gestión del conocimiento) | 06_Capitulos/ | Cap2 v0.1 (primera mitad) | En curso |  |
| S2 | S2-T06 | 2026-10-21 | Diego | Dibujar el proceso actual (AS-IS) en BPMN con lo dicho en las entrevistas | 07_Flujos_Diseno/ | AS-IS v0.1 (borrador) | Pendiente |  |
| S2 | S2-T07 | 2026-10-22 | Víctor | Escribir el capítulo 2, parte 2 (IA, RAG, normativa) | 06_Capitulos/ | 06_Capitulos/2026-10-22_Cap2_Marco_Teorico_v0.1.docx | En curso |  |
| S2 | S2-T08 | 2026-10-22 | Diego | Terminar el proceso actual (AS-IS) y marcar dónde se pierde tiempo | 07_Flujos_Diseno/ | 07_Flujos_Diseno/2026-10-22_AS-IS_v0.1 | Pendiente |  |
| S2 | S2-T09 | 2026-10-23 | Víctor | Buscar fuentes de adopción de IA y automatización comercial 2023–2026, para el marco teórico | 02_Fuentes/Tecnologia_IA/ | ≥5 fichas | Hecho | 2026-10-19 |
| S2 | S2-T10 | 2026-10-23 | Víctor | Armar el lienzo del modelo de negocio y la propuesta de valor (primer borrador) | 06_Capitulos/Modelo_Negocio/ | 06_Capitulos/Modelo_Negocio/2026-10-23_Lienzo_Modelo_Negocio_v0.1.docx | En curso |  |
| S2 | S2-T11 | 2026-10-23 | Diego | Hacer el inventario de herramientas candidatas, con criterios de comparación | 07_Flujos_Diseno/ | Inventario v0.1 (borrador) | Pendiente |  |
| S2 | S2-T12 | 2026-10-24 | Víctor | Escribir el capítulo 3, parte 1 (enfoque, DSR y población) | 06_Capitulos/ | Cap3 v0.1 (primera mitad) | En curso |  |
| S2 | S2-T13 | 2026-10-24 | Víctor | Escribir un resumen de 1 página para Diego del capítulo 1 | 06_Capitulos/ | 06_Capitulos/2026-10-24_Resumen_Cap1.md | En curso |  |
| S2 | S2-T14 | 2026-10-24 | Diego | Terminar el inventario de herramientas con precios y criterios | 07_Flujos_Diseno/ | 07_Flujos_Diseno/2026-10-24_Inventario_Herramientas_v0.1.xlsx | Pendiente |  |
| S2 | S2-T15 | 2026-10-24 | Diego | Escribir un resumen de 1 página para Víctor del proceso actual | 07_Flujos_Diseno/ | 07_Flujos_Diseno/2026-10-24_Resumen_AS-IS.md | Pendiente |  |
| S2 | S2-T16 | 2026-10-25 | Víctor | Escribir el capítulo 3, parte 2 (instrumentos, análisis y ética) | 06_Capitulos/ | 06_Capitulos/2026-10-25_Cap3_Metodologia_v0.1.docx | En curso |  |
| S2 | S2-T17 | 2026-10-25 | Diego | Preparar las gráficas de datos para la Revisión 1 | 05_Datos_Campo/LineaBase_2026-10/ | 05_Datos_Campo/LineaBase_2026-10/analisis/figuras/ | Pendiente |  |
| S2 | S2-T18 | 2026-10-25 | Ambos | Revisar el sprint (qué hicimos, qué no, qué aprendimos), hacer 20 min de «explícame lo tuyo» y planificar el siguiente | Llamada Víctor–Diego · 11_Planificacion/Bitacora_Semanal.md y 11_Planificacion/Cronograma_Tesis.xlsx | Sección de la semana en la bitácora + hoja del sprint siguiente ajustada | Pendiente |  |
| S3 | S3-T01 | 2026-10-26 | Víctor | Preparar la presentación de avance (capítulos 1–3 y fuentes), para la Revisión 1 | 08_Reuniones_Tutora/ | 08_Reuniones_Tutora/2026-10-27_Presentacion_Revision1.pptx | Pendiente |  |
| S3 | S3-T02 | 2026-10-26 | Diego | Exportar el proceso actual y las gráficas para la presentación | 07_Flujos_Diseno/ | Imágenes en la presentación | Pendiente |  |
| S3 | S3-T03 | 2026-10-27 | Ambos | Ensayar la presentación de la Revisión 1 | Llamada Víctor–Diego | Ensayo cronometrado | Pendiente |  |
| S3 | S3-T04 | 2026-10-27 | Víctor | Escribir cómo estructuré mi bóveda 1 (patrones, no datos), parte 1 | 07_Flujos_Diseno/ | Patrones v0.1 (primera mitad) | Pendiente |  |
| S3 | S3-T05 | 2026-10-28 | Ambos | Asistir a la Revisión 1 con la tutora (fecha a confirmar) | UPS Quito, en persona | Observaciones anotadas | Pendiente |  |
| S3 | S3-T06 | 2026-10-28 | Víctor | Escribir el acta de la Revisión 1 | 08_Reuniones_Tutora/ | 08_Reuniones_Tutora/2026-10-28_Acta_Revision1.md | Pendiente |  |
| S3 | S3-T07 | 2026-10-29 | Víctor | Corregir los capítulos según las observaciones, parte 1 | 06_Capitulos/ | Capítulos v0.2 | Pendiente |  |
| S3 | S3-T08 | 2026-10-29 | Diego | Corregir el proceso actual y las gráficas según las observaciones | 07_Flujos_Diseno/ | AS-IS v0.2 | Pendiente |  |
| S3 | S3-T09 | 2026-10-30 | Víctor | Escribir cómo estructuré mi bóveda 1, parte 2 | 07_Flujos_Diseno/ | 07_Flujos_Diseno/2026-10-30_Patrones_Boveda1_v0.1.docx | Pendiente |  |
| S3 | S3-T10 | 2026-10-30 | Diego | Leer el documento de patrones de la bóveda 1 y anotar preguntas | 07_Flujos_Diseno/ | Preguntas en el issue de S3-04 | Pendiente |  |
| S3 | S3-T11 | 2026-10-31 | Víctor | Corregir los capítulos según las observaciones, parte 2 | 06_Capitulos/ | Capítulos v0.2 completos | Pendiente |  |
| S3 | S3-T12 | 2026-10-31 | Diego | Preparar la plantilla de los flujos TO-BE (Mermaid o Miro) | 07_Flujos_Diseno/ | Plantilla de flujos | Pendiente |  |
| S3 | S3-T13 | 2026-11-01 | Ambos | Sesión: Víctor explica a Diego los conceptos de negocio (embudo, tiempo de respuesta, propuesta de valor) | Llamada Víctor–Diego · Conceptos_Negocio.pdf (raíz) | Diego traduce cada concepto a una función del sistema | Pendiente |  |
| S3 | S3-T14 | 2026-11-01 | Ambos | Revisar el sprint (qué hicimos, qué no, qué aprendimos), hacer 20 min de «explícame lo tuyo» y planificar el siguiente | Llamada Víctor–Diego · 11_Planificacion/Bitacora_Semanal.md y 11_Planificacion/Cronograma_Tesis.xlsx | Sección de la semana en la bitácora + hoja del sprint siguiente ajustada | Pendiente |  |
| S4 | S4-T01 | 2026-11-02 | Diego | Dibujar los procesos con el sistema (TO-BE), parte 1: recepción y asignación | 07_Flujos_Diseno/ | TO-BE v0.1 (parte 1) | Pendiente |  |
| S4 | S4-T02 | 2026-11-02 | Víctor | Escribir los requisitos funcionales (qué debe hacer el sistema) | 06_Capitulos/ | Requisitos v0.1 (funcionales) | Pendiente |  |
| S4 | S4-T03 | 2026-11-03 | Diego | Dibujar los procesos TO-BE, parte 2: cotización asistida e historial | 07_Flujos_Diseno/ | TO-BE v0.1 (parte 2) | Pendiente |  |
| S4 | S4-T04 | 2026-11-03 | Víctor | Escribir los requisitos no funcionales (seguridad, sin conexión, ley de datos) | 06_Capitulos/ | 06_Capitulos/2026-11-03_Requisitos_v0.1.docx | Pendiente |  |
| S4 | S4-T05 | 2026-11-04 | Diego | Dibujar los procesos TO-BE, parte 3: recordatorios y reasignación | 07_Flujos_Diseno/ | 07_Flujos_Diseno/2026-11-04_TO-BE_v0.1 | Pendiente |  |
| S4 | S4-T06 | 2026-11-04 | Víctor | Validar los flujos TO-BE contra los requisitos | 07_Flujos_Diseno/ | Comentarios en los flujos | Pendiente |  |
| S4 | S4-T07 | 2026-11-05 | Diego | Construir la bóveda del sistema: carpetas y plantillas | 07_Flujos_Diseno/ | 07_Flujos_Diseno/Boveda_Sistema/ | Pendiente |  |
| S4 | S4-T08 | 2026-11-05 | Víctor | Armar la matriz de decisión de herramientas en Excel (fórmulas vivas) | 06_Capitulos/Modelo_Negocio/ | 06_Capitulos/Modelo_Negocio/2026-11-05_Matriz_Decision_Herramientas_v0.1.xlsx | Pendiente |  |
| S4 | S4-T09 | 2026-11-06 | Diego | Construir la bóveda del sistema: fichas de ejemplo con datos ficticios | 07_Flujos_Diseno/ | Fichas CLI-0001… | Pendiente |  |
| S4 | S4-T10 | 2026-11-06 | Víctor | Calcular CAPEX (inversión inicial) con fuente para cada precio | 06_Capitulos/Modelo_Negocio/ | Hoja Costos del modelo financiero | Pendiente |  |
| S4 | S4-T11 | 2026-11-07 | Diego | Construir la bóveda del sistema: tableros y enlaces | 07_Flujos_Diseno/ | Tableros de pendientes | Pendiente |  |
| S4 | S4-T12 | 2026-11-07 | Víctor | Calcular OPEX (gasto mensual) con fuente para cada precio | 06_Capitulos/Modelo_Negocio/ | 06_Capitulos/Modelo_Negocio/2026-11-07_Modelo_Financiero_v0.1.xlsx | Pendiente |  |
| S4 | S4-T13 | 2026-11-08 | Diego | Escribir un resumen de 1 página para Víctor de la bóveda del sistema | 07_Flujos_Diseno/ | 07_Flujos_Diseno/2026-11-08_Resumen_Boveda_Sistema.md | Pendiente |  |
| S4 | S4-T14 | 2026-11-08 | Víctor | Escribir un resumen de 1 página para Diego de requisitos y costos | 06_Capitulos/Modelo_Negocio/ | 06_Capitulos/Modelo_Negocio/2026-11-08_Resumen_Costos.md | Pendiente |  |
| S4 | S4-T15 | 2026-11-08 | Ambos | Revisar el sprint (qué hicimos, qué no, qué aprendimos), hacer 20 min de «explícame lo tuyo» y planificar el siguiente | Llamada Víctor–Diego · 11_Planificacion/Bitacora_Semanal.md y 11_Planificacion/Cronograma_Tesis.xlsx | Sección de la semana en la bitácora + hoja del sprint siguiente ajustada | Pendiente |  |
| S5 | S5-T01 | 2026-11-09 | Víctor | Estimar los beneficios con supuestos explícitos (horas ahorradas, clientes no perdidos) | 06_Capitulos/Modelo_Negocio/ | Hoja Beneficios | Pendiente |  |
| S5 | S5-T02 | 2026-11-09 | Diego | Construir la prueba de concepto, parte 1: formulario → servidor | Repositorio de la prueba de concepto | Formulario guarda en la base de datos | Pendiente |  |
| S5 | S5-T03 | 2026-11-10 | Víctor | Calcular VAN, TIR y período de recuperación en 3 escenarios | 06_Capitulos/Modelo_Negocio/ | Hoja Escenarios | Pendiente |  |
| S5 | S5-T04 | 2026-11-10 | Diego | Construir la prueba de concepto, parte 2: servidor → bóveda | Repositorio de la prueba de concepto | La ficha del cliente aparece en la bóveda | Pendiente |  |
| S5 | S5-T05 | 2026-11-11 | Víctor | Hacer el análisis de sensibilidad (qué pasa si cambian los supuestos) | 06_Capitulos/Modelo_Negocio/ | Hoja Sensibilidad | Pendiente |  |
| S5 | S5-T06 | 2026-11-11 | Diego | Construir la prueba de concepto, parte 3: borrador de cotización con IA | Repositorio de la prueba de concepto | Borrador generado desde la bóveda | Pendiente |  |
| S5 | S5-T07 | 2026-11-12 | Víctor | Escribir la matriz de riesgos | 06_Capitulos/ | 06_Capitulos/2026-11-12_Riesgos_v0.1.xlsx | Pendiente |  |
| S5 | S5-T08 | 2026-11-12 | Diego | Construir la prueba de concepto, parte 4: alertas y registro de eventos | Repositorio de la prueba de concepto | Eventos registrados | Pendiente |  |
| S5 | S5-T09 | 2026-11-13 | Víctor | Escribir el capítulo de normativa (LOPDP) | 06_Capitulos/ | 06_Capitulos/2026-11-13_Normativa_v0.1.docx | Pendiente |  |
| S5 | S5-T10 | 2026-11-13 | Diego | Probar la prueba de concepto completa y corregir errores | Repositorio de la prueba de concepto | Flujo completo sin errores | Pendiente |  |
| S5 | S5-T11 | 2026-11-14 | Víctor | Escribir el pitch de 1 página para inversionista | 06_Capitulos/Modelo_Negocio/ | 06_Capitulos/Modelo_Negocio/2026-11-14_Pitch_1pagina_v0.1.docx | Pendiente |  |
| S5 | S5-T12 | 2026-11-14 | Víctor | Terminar el capítulo de normativa | 06_Capitulos/ | Normativa v0.1 completa | Pendiente |  |
| S5 | S5-T13 | 2026-11-14 | Diego | Diseñar los 3 casos de prueba | 07_Flujos_Diseno/ | 07_Flujos_Diseno/2026-11-14_Casos_Prueba_v0.1.md | Pendiente |  |
| S5 | S5-T14 | 2026-11-15 | Ambos | Intercambiar resúmenes de 1 página (finanzas ↔ prueba de concepto) | 06_Capitulos/Modelo_Negocio/ y 07_Flujos_Diseno/ | 2 resúmenes | Pendiente |  |
| S5 | S5-T15 | 2026-11-15 | Ambos | Revisar el sprint (qué hicimos, qué no, qué aprendimos), hacer 20 min de «explícame lo tuyo» y planificar el siguiente | Llamada Víctor–Diego · 11_Planificacion/Bitacora_Semanal.md y 11_Planificacion/Cronograma_Tesis.xlsx | Sección de la semana en la bitácora + hoja del sprint siguiente ajustada | Pendiente |  |
| S6 | S6-T01 | 2026-11-16 | Ambos | Preparar la presentación de la Revisión 2 (diseño, flujos, datos y viabilidad) | 08_Reuniones_Tutora/ | 08_Reuniones_Tutora/2026-11-17_Presentacion_Revision2.pptx | Pendiente |  |
| S6 | S6-T02 | 2026-11-17 | Ambos | Ensayar la presentación de la Revisión 2 | Llamada Víctor–Diego | Ensayo cronometrado | Pendiente |  |
| S6 | S6-T03 | 2026-11-17 | Diego | Estabilizar la prueba de concepto para la demostración | Repositorio de la prueba de concepto | Demo sin fallas | Pendiente |  |
| S6 | S6-T04 | 2026-11-18 | Ambos | Asistir a la Revisión 2 con la tutora (fecha a confirmar) | UPS Quito, en persona | Observaciones anotadas | Pendiente |  |
| S6 | S6-T05 | 2026-11-18 | Víctor | Escribir el acta de la Revisión 2 | 08_Reuniones_Tutora/ | 08_Reuniones_Tutora/2026-11-18_Acta_Revision2.md | Pendiente |  |
| S6 | S6-T06 | 2026-11-19 | Víctor | Preparar el protocolo de la validación del diseño en operación experimental controlada | 04_Instrumentos/ | 04_Instrumentos/2026-11-19_Protocolo_Validacion_v0.1.md | Pendiente |  |
| S6 | S6-T07 | 2026-11-19 | Diego | Dejar estable la prueba de concepto para la validación | Repositorio de la prueba de concepto | Versión congelada | Pendiente |  |
| S6 | S6-T08 | 2026-11-20 | Víctor | Pedir a Torvesa la autorización y las fechas de la validación | Correo electrónico | Autorización escrita | Pendiente |  |
| S6 | S6-T09 | 2026-11-20 | Diego | Probar la prueba de concepto con los 3 casos de prueba antes de la validación | 07_Flujos_Diseno/ | Resultados preliminares | Pendiente |  |
| S6 | S6-T10 | 2026-11-21 | Víctor | Incorporar las observaciones de la Revisión 2 (documento) | 06_Capitulos/ | Versiones nuevas | Pendiente |  |
| S6 | S6-T11 | 2026-11-21 | Diego | Incorporar las observaciones de la Revisión 2 (técnicas) | 07_Flujos_Diseno/ | Versiones nuevas | Pendiente |  |
| S6 | S6-T12 | 2026-11-22 | Ambos | Revisar el sprint (qué hicimos, qué no, qué aprendimos), hacer 20 min de «explícame lo tuyo» y planificar el siguiente | Llamada Víctor–Diego · 11_Planificacion/Bitacora_Semanal.md y 11_Planificacion/Cronograma_Tesis.xlsx | Sección de la semana en la bitácora + hoja del sprint siguiente ajustada | Pendiente |  |
| S7 | S7-T01 | 2026-11-22 | Diego | Preparar el sistema para la validación (accesos, respaldo) | Repositorio de la prueba de concepto | Accesos listos | Pendiente |  |
| S7 | S7-T02 | 2026-11-23 | Ambos | Capacitar al equipo de Torvesa para la validación | Torvesa (oficina, Quito) | Equipo capacitado | Pendiente |  |
| S7 | S7-T03 | 2026-11-24 | Diego | Arrancar la validación del diseño en operación experimental controlada | Torvesa (oficina, Quito) | Primeros eventos registrados | Pendiente |  |
| S7 | S7-T04 | 2026-11-24 | Víctor | Escribir el capítulo de diagnóstico, parte 1 (línea base real) | 06_Capitulos/ | Cap4 v0.1 (primera mitad) | Pendiente |  |
| S7 | S7-T05 | 2026-11-25 | Diego | Monitorear la validación y anotar incidencias | Registro de eventos del sistema | Bitácora de incidencias | Pendiente |  |
| S7 | S7-T06 | 2026-11-25 | Diego | Incorporar observaciones técnicas pendientes | 07_Flujos_Diseno/ | Versiones nuevas | Pendiente |  |
| S7 | S7-T07 | 2026-11-25 | Víctor | Escribir el capítulo de diagnóstico, parte 2 | 06_Capitulos/ | Cap4 v0.1 | Pendiente |  |
| S7 | S7-T08 | 2026-11-26 | Diego | Monitorear la validación y anotar incidencias | Registro de eventos del sistema | Bitácora de incidencias | Pendiente |  |
| S7 | S7-T09 | 2026-11-26 | Víctor | Incorporar observaciones pendientes del documento | 06_Capitulos/ | Versiones nuevas | Pendiente |  |
| S7 | S7-T10 | 2026-11-27 | Diego | Monitorear la validación y anotar incidencias | Registro de eventos del sistema | Bitácora de incidencias | Pendiente |  |
| S7 | S7-T11 | 2026-11-27 | Víctor | Revisar el capítulo de diagnóstico | 06_Capitulos/ | 06_Capitulos/2026-11-28_Cap4_Diagnostico_v0.1.docx | Pendiente |  |
| S7 | S7-T12 | 2026-11-28 | Diego | Monitorear la validación y empezar a documentar las herramientas | Registro de eventos · 07_Flujos_Diseno/ | Bitácora + borrador de herramientas | Pendiente |  |
| S7 | S7-T13 | 2026-11-28 | Víctor | Escribir un resumen de 1 página para Diego del diagnóstico | 06_Capitulos/ | 06_Capitulos/2026-11-28_Resumen_Cap4.md | Pendiente |  |
| S7 | S7-T14 | 2026-11-29 | Ambos | Revisar el sprint (qué hicimos, qué no, qué aprendimos), hacer 20 min de «explícame lo tuyo» y planificar el siguiente | Llamada Víctor–Diego · 11_Planificacion/Bitacora_Semanal.md y 11_Planificacion/Cronograma_Tesis.xlsx | Sección de la semana en la bitácora + hoja del sprint siguiente ajustada | Pendiente |  |
| S8 | S8-T01 | 2026-11-30 | Diego | Documentar las herramientas elegidas y descartadas, con justificación | 07_Flujos_Diseno/ | 07_Flujos_Diseno/Herramientas | Pendiente |  |
| S8 | S8-T02 | 2026-11-30 | Diego | Monitorear la validación | Registro de eventos del sistema | Bitácora | Pendiente |  |
| S8 | S8-T03 | 2026-11-30 | Víctor | Escribir el capítulo de diseño y viabilidad, parte 1 (arquitectura y flujos) | 06_Capitulos/ | Cap5 v0.1 (parte 1) | Pendiente |  |
| S8 | S8-T04 | 2026-12-01 | Diego | Documentar el modelo de datos y el registro de eventos | 07_Flujos_Diseno/ | 07_Flujos_Diseno/Modelo_Datos | Pendiente |  |
| S8 | S8-T05 | 2026-12-01 | Diego | Monitorear la validación | Registro de eventos del sistema | Bitácora | Pendiente |  |
| S8 | S8-T06 | 2026-12-01 | Víctor | Escribir el capítulo de diseño y viabilidad, parte 2 (costos y VAN/TIR) | 06_Capitulos/ | Cap5 v0.1 (parte 2) | Pendiente |  |
| S8 | S8-T07 | 2026-12-02 | Diego | Documentar las plantillas de cotización y el asistente de IA | 07_Flujos_Diseno/ | 07_Flujos_Diseno/Asistente_IA | Pendiente |  |
| S8 | S8-T08 | 2026-12-02 | Diego | Monitorear la validación | Registro de eventos del sistema | Bitácora | Pendiente |  |
| S8 | S8-T09 | 2026-12-02 | Víctor | Escribir el capítulo de diseño y viabilidad, parte 3 (normativa y riesgos) | 06_Capitulos/ | Cap5 v0.1 (parte 3) | Pendiente |  |
| S8 | S8-T10 | 2026-12-03 | Diego | Ejecutar los casos de prueba | 07_Flujos_Diseno/ | 07_Flujos_Diseno/Resultados_Casos_Prueba | Pendiente |  |
| S8 | S8-T11 | 2026-12-03 | Diego | Monitorear la validación | Registro de eventos del sistema | Bitácora | Pendiente |  |
| S8 | S8-T12 | 2026-12-03 | Víctor | Revisar los documentos técnicos de Diego | 07_Flujos_Diseno/ | Comentarios | Pendiente |  |
| S8 | S8-T13 | 2026-12-04 | Diego | ✂ Escribir el manual básico de usuario | 07_Flujos_Diseno/ | 07_Flujos_Diseno/Manual_Usuario | Pendiente |  |
| S8 | S8-T14 | 2026-12-04 | Víctor | Terminar el capítulo de diseño y viabilidad | 06_Capitulos/ | 06_Capitulos/2026-12-04_Cap5_Diseno_Viabilidad_v0.1.docx | Pendiente |  |
| S8 | S8-T15 | 2026-12-05 | Diego | Cerrar la validación: congelar el registro y respaldar los datos | Registro de eventos · 05_Datos_Campo/LineaBase_2026-10/ | Respaldo con hash | Pendiente |  |
| S8 | S8-T16 | 2026-12-05 | Víctor | Preparar los instrumentos de la medición «después» | 04_Instrumentos/ | Instrumentos post impresos | Pendiente |  |
| S8 | S8-T17 | 2026-12-06 | Ambos | Intercambiar resúmenes de 1 página (capítulo 5 ↔ documentación técnica) | 06_Capitulos/ y 07_Flujos_Diseno/ | 2 resúmenes | Pendiente |  |
| S8 | S8-T18 | 2026-12-06 | Ambos | Revisar el sprint (qué hicimos, qué no, qué aprendimos), hacer 20 min de «explícame lo tuyo» y planificar el siguiente | Llamada Víctor–Diego · 11_Planificacion/Bitacora_Semanal.md y 11_Planificacion/Cronograma_Tesis.xlsx | Sección de la semana en la bitácora + hoja del sprint siguiente ajustada | Pendiente |  |
| S9 | S9-T01 | 2026-12-07 | Ambos | Hacer la medición «después», día 1 (encuesta a colaboradores y SUS) | Torvesa (oficina, Quito) | Datos post + registro de procedencia | Pendiente |  |
| S9 | S9-T02 | 2026-12-08 | Ambos | Hacer la medición «después», día 2 (prueba de recuperación) | Torvesa (oficina, Quito) | Datos post | Pendiente |  |
| S9 | S9-T03 | 2026-12-09 | Ambos | Hacer la medición «después», día 3 (clientes y entrevistas de cierre) | Torvesa (oficina, Quito) | Datos post | Pendiente |  |
| S9 | S9-T04 | 2026-12-10 | Víctor | Comparar el antes y el después (análisis pre-post) | 05_Datos_Campo/LineaBase_2026-10/ | Tablas pre-post | Pendiente |  |
| S9 | S9-T05 | 2026-12-10 | Diego | ✂ Hacer pruebas de carga simuladas con scripts | 07_Flujos_Diseno/ | 07_Flujos_Diseno/Pruebas_Carga | Pendiente |  |
| S9 | S9-T06 | 2026-12-11 | Víctor | Terminar el análisis pre-post | 05_Datos_Campo/LineaBase_2026-10/ | Resultados listos | Pendiente |  |
| S9 | S9-T07 | 2026-12-11 | Diego | Hacer pruebas de uso y preparar las gráficas de resultados | 07_Flujos_Diseno/ | Gráficas | Pendiente |  |
| S9 | S9-T08 | 2026-12-12 | Víctor | Escribir el capítulo de resultados | 06_Capitulos/ | 06_Capitulos/2026-12-12_Cap6_Resultados_v0.1.docx | Pendiente |  |
| S9 | S9-T09 | 2026-12-12 | Diego | Revisar el capítulo de resultados (parte técnica) | 06_Capitulos/ | Comentarios | Pendiente |  |
| S9 | S9-T10 | 2026-12-13 | Ambos | Revisar el sprint (qué hicimos, qué no, qué aprendimos), hacer 20 min de «explícame lo tuyo» y planificar el siguiente | Llamada Víctor–Diego · 11_Planificacion/Bitacora_Semanal.md y 11_Planificacion/Cronograma_Tesis.xlsx | Sección de la semana en la bitácora + hoja del sprint siguiente ajustada | Pendiente |  |
| S10 | S10-T01 | 2026-12-14 | Víctor | Enviar a la tutora la tesis completa para revisión | Correo electrónico | Tesis enviada | Pendiente |  |
| S10 | S10-T02 | 2026-12-14 | Diego | Revisar anexos técnicos y figuras | 06_Capitulos/ | Anexos revisados | Pendiente |  |
| S10 | S10-T03 | 2026-12-15 | Víctor | ✂ Ciclo con la tutora: recibir observaciones | 08_Reuniones_Tutora/ | Observaciones | Pendiente |  |
| S10 | S10-T04 | 2026-12-16 | Ambos | Corregir según las observaciones | 06_Capitulos/ | Versión corregida | Pendiente |  |
| S10 | S10-T05 | 2026-12-17 | Víctor | ✂ Ciclo con la tutora: segunda revisión | 08_Reuniones_Tutora/ | Observaciones | Pendiente |  |
| S10 | S10-T06 | 2026-12-18 | Ambos | HITO: dejar la tesis al 90 % | 06_Capitulos/ | Tesis completa | Pendiente |  |
| S10 | S10-T07 | 2026-12-19 | Ambos | Integrar todo y revisar coherencia entre capítulos | 06_Capitulos/ | Versión integrada | Pendiente |  |
| S10 | S10-T08 | 2026-12-20 | Ambos | Revisar el sprint (qué hicimos, qué no, qué aprendimos), hacer 20 min de «explícame lo tuyo» y planificar el siguiente | Llamada Víctor–Diego · 11_Planificacion/Bitacora_Semanal.md y 11_Planificacion/Cronograma_Tesis.xlsx | Sección de la semana en la bitácora + hoja del sprint siguiente ajustada | Pendiente |  |
| Holgura | Holgura-T01 | 2026-12-22 | Víctor | Revisar las citas del capítulo 1 y 2 contra sus fichas | 06_Capitulos/ | Citas verificadas | Pendiente |  |
| Holgura | Holgura-T02 | 2026-12-23 | Diego | Revisar los anexos técnicos y su numeración | 06_Capitulos/ | Anexos ordenados | Pendiente |  |
| Holgura | Holgura-T03 | 2026-12-26 | Víctor | Revisar las citas de los capítulos 3–6 | 06_Capitulos/ | Citas verificadas | Pendiente |  |
| Holgura | Holgura-T04 | 2026-12-29 | Víctor | Revisar la bibliografía en APA 7 | 06_Capitulos/ | Bibliografía final | Pendiente |  |
| Holgura | Holgura-T05 | 2026-12-30 | Diego | Revisar figuras, tablas y diagramas | 06_Capitulos/ | Figuras finales | Pendiente |  |
| Holgura | Holgura-T06 | 2027-01-02 | Ambos | Leer la tesis completa una vez más | 06_Capitulos/ | Lista de últimos cambios | Pendiente |  |
| Entrega | Entrega-T01 | 2027-01-04 | Víctor | Enviar la versión final a la tutora | Correo electrónico | Versión final enviada | Pendiente |  |
| Entrega | Entrega-T02 | 2027-01-06 | Ambos | Hacer las últimas correcciones | 06_Capitulos/ | Versión final corregida | Pendiente |  |
| Entrega | Entrega-T03 | 2027-01-07 | Víctor | Conseguir la firma de la tutora | UPS Quito, en persona | Tesis firmada | Pendiente |  |
| Entrega | Entrega-T04 | 2027-01-08 | Ambos | Entregar la tesis a la carrera | Sistema de la UPS | Comprobante | Pendiente |  |
| Defensa | Defensa-T01 | 2027-01-12 | Ambos | Escribir el resumen de contribuciones (quién hizo qué) | 09_Registro_Contribuciones/ | Resumen de contribuciones | Pendiente |  |
| Defensa | Defensa-T02 | 2027-01-23 | Ambos | Dividir la exposición y armar las diapositivas | Llamada Víctor–Diego | Guion + diapositivas | Pendiente |  |
| Defensa | Defensa-T03 | 2027-01-30 | Ambos | Armar el banco de preguntas del tribunal y hacer el simulacro 1 | Llamada Víctor–Diego | Banco de preguntas + simulacro | Pendiente |  |
| Defensa | Defensa-T04 | 2027-02-06 | Ambos | Hacer el simulacro 2 con preguntas cruzadas (cada uno responde lo del otro) | Llamada Víctor–Diego | Simulacro 2 | Pendiente |  |
| Defensa | Defensa-T05 | 2027-02-09 | Ambos | Defender la tesis (fecha a confirmar por la carrera) | UPS Quito, en persona | Defensa | Pendiente |  |
