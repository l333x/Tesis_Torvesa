---
titulo: Bitácora semanal (fuente de los informes de avance)
tipo: documento_vivo
tags: [bitacora, informes, planificacion]
---

# Bitácora semanal

> [!info] Cómo se usa
> Una sección `## AAAA-MM-DD · título` por semana (la fecha es el domingo de cierre). El script `99_Scripts/gestion/generar_informe.py` toma la sección más reciente, o la que se le indique, y la cruza con `CRONOGRAMA.md` y con `git log`.
> - **Atención de Víctor:** cada viñeta se convierte en un **comentario de Word** anclado al punto del informe.
> - Se escribe **durante** la semana, no el domingo a última hora.

## 2026-10-11 · Informe 00 — Línea de partida

### Resumen
- Se abrió el proyecto de investigación sobre el **diseño aprobado** («Diseño de un sistema de automatización para la gestión comercial en la Constructora Torvesa», con aval de la tutora y autorización de Torvesa del 29-sep-2026).
- **Fase 0:** lectura completa del borrador; 47 afirmaciones que necesitan fuente; propuesta de estructura y de migración.
- **Fase 0.5:** bóveda de la tesis + repo privado en GitHub + RAG local + respaldos automáticos + lanzadores + instrumentos de campo v0.1.
- **Hallazgo crítico:** los datos del «diagnóstico N = 30» son **simulados**. No se usan. La línea base real se levanta el 15–16 de octubre.

### Decisiones
- **D1** ✅ Lo que el borrador llama «piloto» se denomina «validación del diseño en operación experimental controlada»; nunca «implementación» ni «piloto».
- **D2** ⏳ DSR como marco + Design Thinking en el diseño + Scrum para organizar; «mixto con predominio cuantitativo». **Pendiente de la tutora.**
- **D3** ✅ Se usan los OVA oficiales (4.1–4.3, 5.1/5.3/5.4, 6.1–6.3), mapeados a los objetivos de Víctor.
- **D4** ✅ Dos censos: 30 colaboradores y 33 clientes.
- **D5** ⏳ Escenario B (entrega en enero) como base; escenario A (15-dic) si la tutora lo confirma.
- **D6** ⏳ Proponer retirar OpenTimestamps y reemplazarlo por SHA-256 + log de solo-anexión; justificación de 1 página cuando haya 3 o más fuentes verificadas. **No se borra del documento hasta que la tutora responda.**
- **D7** ✅ VAN/TIR del sistema para Torvesa; el SaaS va como anexo.
- Diagnóstico simulado: **NO se usa** como dato. Se reaplican los instrumentos en campo con protocolo de procedencia.
- El repo no contiene cédulas: el PDF aprobado, las cartas y los documentos históricos quedan solo en local; el `.md` del borrador tiene las cédulas tapadas.

### Hecho
- Bóveda `F:\Obsidian\Tesis_Torvesa`: 37 archivos migrados **por copia** (log con hash); la bóveda 1 no se tocó.
- Repo privado `l333x/Tesis_Torvesa`: invitación a Diego (`PiscesLivie`, escritura); auditoría PII en 0 hallazgos antes de cada push.
- RAG local (e5-base + Chroma), incremental por hash; respuestas con ruta y referencia APA.
- Respaldos: zip diario a las 22:00 y al iniciar sesión; se conservan 30; log.
- Lanzadores en el escritorio (Bóveda 1 / Tesis) con ícono y AUMID propios; aviso si F: no está montada.
- Instrumentos v0.1: I1 colaboradores, I2 clientes, I3 entrevista, C1 consentimiento LOPDP, P1 procedencia, P2 cronometraje (esfuerzo y tiempo transcurrido).
- Cronograma maestro con 53 tareas = 53 issues en 13 milestones.

### Riesgos y bloqueos
- **El diseño firmado por la tutora presenta datos simulados como diagnóstico real.** Si no se aclara antes de la Revisión 1, es un riesgo de integridad académica.
- Las metas **M1, M3, M4 y M6** quedan sin línea base hasta el campo del 15–16 oct. **M2** (30–44 min) no tiene fuente: se mide con cronómetro.
- **Giro del negocio sin confirmar:** el SRI dice vías; el instrumento simulado hablaba de inmuebles. Afecta el vocabulario de los instrumentos.
- El campo depende de permisos de gerencia (cronometraje, muestra documental, lista de clientes) que todavía no están.
- El volumen de solicitudes durante la validación del diseño en operación experimental controlada (2 semanas, 33 clientes) puede ser bajo para las pruebas estadísticas.
- El tablero (Project) de GitHub falta: requiere `gh auth refresh -s project`.

### Atención de Víctor
- Escribir a la tutora **antes** de la Revisión 1: datos simulados, D2, D5 (¿el 15-dic es fecha dura?) y D6.
- Conseguir de gerencia, antes del jueves 15: autorización C1-C, permiso de cronometraje y lista de los 33 clientes (solo a `_crudo/`).
- Confirmar con Torvesa el giro real del negocio y si vende inmuebles.
- Corregir los instrumentos v0.1 → v0.2 el miércoles 14 (cada cambio en un archivo nuevo).
- Ejecutar `gh auth refresh -s project` para crear el tablero kanban.
- Aprobar o ajustar la propuesta de reorganización del repo (renombrados con `git mv`).

### Próxima semana
- **Lun–mié:** fase 1 de fuentes (problema y M2 → metodología → LOPDP → SUS → IA 2023–2026); corte el miércoles en la noche con la matriz afirmación → fuentes → estado.
- **Mié:** instrumentos v0.2 impresos.
- **Jue–vie:** campo (I1, I2, I3, P2-A, P2-B) con el registro de procedencia P1.
- **Fin de semana:** tabulación, anonimización, hashes y auditoría PII.
- **Diego:** aceptar la invitación, clonar, levantar el RAG y hacer el commit de prueba (#10).

## 2026-10-11 · Cambio de enfoque: documentos para personas

### Resumen
- Desde hoy hay dos tipos de documentos: los **.md** son para la IA y los **Word/PDF** son para Víctor y Diego, en lenguaje simple, con diagramas y sin códigos sin explicar.
- Nuevos: **Documento madre** (este, se actualiza cada domingo), **Glosario**, **Auditoría de la bóveda**, **cronograma día a día en Excel** (166 tareas en sprints semanales), **guía de conceptos de negocio**, **scripts de búsqueda de fuentes con Chrome** y su guía de 1 página.
- **Roles corregidos:** Víctor = tesis, fuentes, método, modelo de negocio y finanzas · Diego = todo lo técnico. Diego **no** tendrá acceso a la bóveda 1; esta semana investiga con fuentes (bóvedas, RAG, flujos, CRMs).
- Mañana, lunes 12, conversación con la tutora en la UPS y correo a Torvesa.

### Decisiones
- ✅ Se usa siempre «validación del diseño en operación experimental controlada», nunca «piloto».
- ✅ Reorganización aprobada y hecha: datos simulados marcados «NO USAR», fecha en el nombre de los instrumentos, versiones repetidas fuera del repositorio.
- ✅ Se canceló la copia de la bóveda 1 para Diego (tarea #11 cerrada).
- ✅ La infraestructura queda congelada (la única excepción fueron los scripts de búsqueda).
- ✅ El tablero de GitHub se descarta: el avance se sigue en el Excel del cronograma.
- ✅ «Subasta suiza» queda fuera de la guía de conceptos.
- ✅ Se borró el contenido de la copia cancelada de la bóveda 1 (`F:\Compartir_Diego_PENDIENTE`) y los duplicados se movieron a `_historico`.

### Riesgos y bloqueos
- **El diseño que firmó la tutora presenta datos simulados como si fueran reales.** Hay que contárselo mañana, antes de la primera revisión formal.
- Las metas que dependen de la línea base (la medición del «antes») quedan sin dato hasta que Torvesa autorice el campo: responder en menos de 15 minutos, perder menos clientes antes del primer contacto, encontrar el historial de un cliente ajeno y la usabilidad del sistema.
- El dato «30–44 minutos por cotización» no tiene fuente: se medirá con cronómetro si Torvesa lo permite.
- No sabemos con certeza a qué se dedica Torvesa (en el SRI figura la construcción de vías; las encuestas simuladas hablaban de inmuebles).

### Atención de Víctor
- Mañana: conversar con la tutora usando la hoja de 5 puntos (`08_Reuniones_Tutora/2026-10-12_Puntos_Tutora.pdf`) y escribir el acta ese mismo día.
- Mañana: enviar el correo a Torvesa (borrador en `11_Planificacion/2026-10-12_Correo_Torvesa_borrador.docx`), con respuesta hasta el miércoles 14.
- Borrar la carpeta vacía `F:\Compartir_Diego_PENDIENTE` (la herramienta no me deja borrar carpetas en la raíz de F:).
- Elegir cuál es el Informe Final y cuál es el pitch deck vigentes (hay varias versiones en `10_Antecedentes_Propios`).
- Avisar a Diego que acepte la invitación de GitHub (vence el 18-oct).

### Próxima semana
- Lunes a miércoles: buscar y verificar fuentes (tiempo de respuesta, digitalización de la construcción, metodología, ley de datos, escala de usabilidad en español).
- Miércoles 14: instrumentos corregidos (versión 0.2) y matriz de fuentes.
- Jueves 15 y viernes 16: campo en Torvesa **solo si lo autoriza**; si no, más fuentes.
- Diego: investigar bóvedas de conocimiento, RAG, flujos y CRMs, con un resumen de 1 página para Víctor.
- Domingo 18: revisión de la semana con «explícame lo tuyo».


## 2026-10-18 · Revisión del sprint 1 (12–18 oct)

### Resumen
- **Qué se hizo:**
  - lunes 12: 22 fuentes verificadas, base de fuentes, manual de redacción y app;
  - martes 13: formatos oficiales UPS y MANUAL_TESIS v0.2;
  - domingo 18: corte de la fase 1, con 8 verificadas más (30 en total), matriz afirmación–fuente–estado, C1 v0.2 (LOPDP), I1 v0.2 (SUS validada en español), resumen del problema para Diego e instrucciones para la IA de Diego (`IA_DIEGO.md`).
- **Qué no se hizo:**
  - del martes 13 al mediodía al sábado 17 no hubo trabajo (dos días de retraso, según Víctor);
  - el campo en Torvesa no se hizo;
  - Diego no empezó su parte.
- **Qué aprendimos:**
  - la evidencia no respalda la ventana de 5–15 min (A10), que pasa a ser una decisión de diseño;
  - la ley no fija los 12 meses de archivo (A45): es un plazo que fija la tesis;
  - las editoriales grandes bloquean la descarga automática, así que hace falta un rato de descarga a mano.

### Decisiones
- ✅ Tutora: Víctor conversó con ella el 12-oct y no hubo objeciones a los 5 puntos. El acta se hará más adelante (decisión de Víctor).
- ✅ Antecedentes vigentes: **Informe Final del 22-jul** y **pitch decks del 22-jul b y c** (una mezcla de los dos). Los demás pasaron a `_versiones/`; `2026-07-16_teamslash.pdf` se queda.
- ✅ Diego se encarga de conseguir la información y los permisos de Torvesa.
- ✅ Las tareas de Diego se organizan en bloques dobles del 19 al 24 oct, guiadas por su IA con `IA_DIEGO.md`.
- ✅ La carpeta vacía `F:\Compartir_Diego_PENDIENTE` ya se borró (lo hizo Víctor).

### Riesgos y bloqueos
- **El campo depende de Torvesa:** sin línea base no hay análisis de datos (S2-T02, S2-T04) ni proceso AS-IS completo.
- 19 de 42 filas de la matriz siguen sin fuente; el capítulo 2 (CRM, A21–A27) es lo más urgente para Víctor.
- La fecha de entrega (D5: 15-dic o enero) sigue sin confirmar.

### Atención de Víctor
- Bajar a mano los PDF de la lista de `F1_reporte_2026-10-18.md`.
- Revisar la matriz, C1 v0.2, I1 v0.2, el resumen del problema y `IA_DIEGO.md`.
- Confirmar con la tutora la fecha de entrega (D5).
- Llamada de 20 min con Diego: «explícame lo tuyo».

### Próxima semana (sprint 2, 19–25 oct)
- **Víctor (bloques dobles):**
  - lun: cap. 1 parte 1 + PDF a mano;
  - mar: cap. 1 parte 2 + fuentes de CRM A21–A27;
  - mié: cap. 2 parte 1 + censo y métodos (biblioteca);
  - jue: cap. 2 parte 2 + A44 y A30;
  - vie: fuentes de IA + lienzo del modelo de negocio;
  - sáb: cap. 3 parte 1 + resumen para Diego;
  - dom: cap. 3 parte 2 + revisión del sprint.
- **Diego:** bloques A–H de `IA_DIEGO.md` (arranque, bóvedas y RAG, documentación oficial y precios, BPMN, herramientas) y el campo cuando Torvesa autorice.

### Decisiones (18-oct, noche)
- ✅ **D5 — Escenario B:** la fecha límite es el **lunes 4-ene-2027**, con el documento final completo y listo para la revisión de la tutora. El cronograma ya estaba armado así (Entrega-T01), así que no se comprime nada.
- ✅ `ejemploInformeTesis.docx` y `ejemploInformeTesisArticulo.docx` (cédulas de terceros) salen del repositorio y quedan solo en local (`.gitignore`).

### Análisis de avance y metas del sprint 2 (18-oct, noche)
- **Avance:** 7 de 166 tareas (4 %); faltan 11 semanas para el 4-ene-2027.
  - Fuentes: 30 verificadas de 60–100.
  - Matriz: 16 de 42 con algo verificado; lo más débil es el cap. 2 (CRM, A21–A27).
  - Instrumentos: C1 e I1 en v0.2.
  - Capítulos: ninguno empezado.
- **Ruta crítica:** caps. 1–3 → Revisión 1 (26–30 oct); campo → línea base → diseño (2–8 nov) → prueba de concepto (9–15 nov) → validación del diseño en operación experimental controlada (23 nov–6 dic) → medición posterior (7–13 dic) → tesis al 90 % (18 dic) → 4 de enero.
- **Riesgo principal:** la autorización de Torvesa. El campo debería hacerse a más tardar la semana del 2-nov.
  - Si Torvesa no responde hasta el **viernes 24-oct**, se escala: llamada de Víctor al Ing. Torres o carta de respaldo de la tutora. Se decide ese día.
- **Metas al 25-oct:**
  - caps. 1, 2 y 3 en v0.1, editados por Víctor;
  - unas 55 fuentes verificadas;
  - menos de 10 afirmaciones sin fuente;
  - lienzo del modelo de negocio en borrador.
- **Seguimiento a Diego:** el mensaje con su tabla se envió por WhatsApp el 18-oct. Si el martes 20 no ha hecho el bloque A (repo clonado), hay que hablar con él.

## 2026-10-19 · Sprint 2, día 1 (lunes)

### Resumen
- **Qué se hizo (Víctor pidió adelantar la semana):**
  - cap. I v0.1 en dos partes (contexto, empresa, problema, evidencias, delimitación, pregunta; justificación, objetivos, preguntas, metas y alcance), con control de cambios frente al diseño aprobado;
  - cap. II v0.1 (marco teórico) con lo verificado y cap. III v0.1 completo (metodología);
  - lienzo del modelo de negocio v0.1 (propuesta de valor para Torvesa + TEAMSLASH como anexo, D7);
  - resumen del cap. I para Diego;
  - 7 fuentes verificadas (37 en total) y matriz v0.2 (15 afirmaciones sin fuente; A30 y A35 salen por D6).
- **Correcciones al diseño aprobado:** fuera los datos simulados, los «30–44 min», el «60 veces» y la ventana de «5–15 min» atribuida a Oldroyd; índice de digitalización atribuido a Manyika et al. (2015).
- Detalle en `11_Planificacion/F1_reporte_2026-10-19.md`.

### Atención de Víctor
- Revisar en Word los caps. I, II y III y el lienzo (control de cambios activado).
- Bajar los PDF de la lista del reporte del 19-oct (ya no hace falta Lewis y Sauro).
- Decidir: plan de precios de la bóveda y la IA; TEAMSLASH como antecedente propio.

## 2026-10-20 · Sprint 2, día 2 (martes)

### Resumen
- **Víctor aprobó en el chat:** las v0.1 de los caps. I, II y III y del lienzo; las frases nuevas de A28 y A29; DEC-16 (bóveda en el plan Estándar, asistente de IA solo en el Premium); y DEC-17 (TEAMSLASH como antecedente propio, sin cifras).
- **Salió la v0.2** de los capítulos y del lienzo. Solo lo de hoy va marcado con control de cambios.
- **NotebookLM:** cuaderno con 29 fuentes, resumen de audio, mapa mental y resumen en video para Diego. Reglas en `11_Planificacion/NotebookLM_Flujo.md`.
- **Fuentes:** 40 verificadas (norma SHA-256, Peña-Ramírez 2024, Bakiyalakshmi 2026). Búsqueda documentada de A28 y A29. Matriz v0.3.
- Detalle en `11_Planificacion/F1_reporte_2026-10-20.md`.

### Atención
- **Diego:** confirmar si TEAMSLASH guarda los datos en Google Sheets (lo que dice el Informe Final) o en PostgreSQL (lo que dice el pitch).
- **Víctor:** bajar a mano los PDF de la lista del 19-oct y la revisión de *Infrastructures* (2025).

## 2026-10-21 · Sprint 2, día 3 (miércoles)

### Resumen
- **Gemini Deep Research no sirvió:** falló otra vez y ya no aparece en el menú. Claude buscó con las APIs y Consensus.
- **Fuentes:** 49 verificadas (+9). Ahora tienen respaldo RAG (Lewis, 2020), *local-first* (Kleppmann, 2019), Obsidian (licencia, precios y permisos), el plugin de Git en el móvil, la Ley de Comercio Electrónico, y el CRM en pymes (AlQershi, 2020; Gil-Gomez, 2020).
- **Matriz v0.4:** 7 afirmaciones sin fuente (antes 15) y 17 respaldadas (antes 10).
- **NotebookLM:** 37 fuentes.
- Detalle en `11_Planificacion/F1_reporte_2026-10-21.md`.

### Atención
- **Contradicción en A23:** AlQershi et al. (2020) no dice que «solo» las dimensiones tecnológica y organizativa afecten el desempeño. Hay que reformular (frase propuesta en el reporte).
- **A25:** Gil-Gomez et al. (2020) es una propuesta conceptual; no prueba nada.
- **Víctor:** bajar Agag (2023), de Haan (2015) y Gil-Gomez (2020), que son abiertos pero con CAPTCHA; y pedir a la biblioteca UPS Ohiomah (2019), Habel (2025) y Rodriguez y Boyer (2020).

## 2026-10-22 a 2026-10-27 · Cierre del sprint 2 y arranque del sprint 3

### Qué pasó del 22 al 27
- **Víctor:** del 22 al 26 no hubo sesiones de trabajo, así que no hay bitácora ni reportes F1 de esos días. Los capítulos siguen en la v0.2 del 20-oct y la v0.3 espera su revisión.
- **Diego (25-oct, domingo):** subió los bloques C a H de una vez, en 5 commits. Detalle en `00_Inbox/2026-10-25_reporte_Diego.md`.
  - Unió la base de fuentes con la del 21-oct. Hay **93 verificadas**, contando las suyas.
  - Tabla de precios de 3 proveedores de LLM; propone **Claude Sonnet 5.5** para A36, pero falta el visto bueno de Víctor.
  - 6 fichas de BPMN, entre ellas la especificación oficial de la OMG, con lo que **CTX-PROC queda propuesta como respaldada**.
  - **AS-IS v0.1** (`07_Flujos_Diseno/2026-10-25_AS-IS_v0.1.*`): borrador hecho con el Informe Final del 22-jul y sin validar en campo; marca 5 puntos donde se pierde tiempo.
  - **Inventario de herramientas v0.1 y v0.2:** 13 herramientas, criterios C1–C8 con pesos y puntuación.
  - Resúmenes de 1 página: bóvedas y RAG, y CRM y flujos.
- **Torvesa:** sigue sin autorizar el campo. El escalamiento previsto para el 24-oct no quedó registrado.

### Revisión del sprint 2 (19–25 oct), que quedó pendiente
- **Qué se hizo:**
  - **Víctor (con Claude):** caps. I, II y III y el lienzo en v0.2 (adelantados al 19 y 20-oct); 49 fuentes verificadas hasta el 21-oct; matriz v0.4 con 7 afirmaciones sin fuente.
  - **Diego:** bloques A a H completos, con retraso, más el AS-IS v0.1 y el inventario v0.2.
- **Qué no se hizo:**
  - **campo y línea base:** S2-T02, T04 y T17 están bloqueadas porque Torvesa no autorizó;
  - el resumen de 1 página del AS-IS (S2-T15);
  - la confirmación de TEAMSLASH (Google Sheets o PostgreSQL);
  - la llamada de revisión (S2-T18);
  - la v0.3 de los capítulos, que espera a que Víctor revise la v0.2;
  - las respuestas a las dudas 1 a 10 de Diego.
- **Qué aprendimos:**
  - Diego rinde mejor con bloques largos. El trabajo de una semana lo subió en un solo día, el domingo. Desde ahora el retraso se avisa el mismo día y se sube al cerrar cada bloque, sin esperar al domingo.
  - El campo es la ruta crítica y depende de una sola persona en Torvesa. Hace falta un plan B: carta de respaldo de la tutora.
  - Cuando el cronograma y `IA_DIEGO.md` dicen cosas distintas, Diego pierde tiempo preguntando (duda 1 del 19-oct). Desde el 27-oct manda `IA_DIEGO.md` §5b, que ya coincide con el Excel.

### Replanificación (27-oct)
- **En el cronograma:**
  - las tareas de Diego hechas se marcaron con su fecha real;
  - las bloqueadas quedan como «Movido», con una copia en el día nuevo (nota «reprogramada 27-oct»);
  - tareas nuevas: S3-T15 a S3-T19 y S4-T16 y S4-T17.
- **Fechas de Diego:**
  - TEAMSLASH hoy;
  - respuesta de Torvesa el 28-oct;
  - elicitación de requerimientos el 30 y 31-oct;
  - resumen del AS-IS el 1-nov;
  - campo el 3-nov (si Torvesa autoriza);
  - análisis de la línea base el 8-nov.
- **Carga:** el 3-nov se pasa del límite (campo de 4 h más el TO-BE parte 2). Si hay campo, el TO-BE parte 2 se termina el 8-nov.
- **Detalle por bloques:** `IA_DIEGO.md` §5b.
