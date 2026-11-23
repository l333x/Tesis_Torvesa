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


## 2026-10-28 a 2026-11-04 · Sprint 3 sin Revisión 1 y sprint 4 adelantado por Diego

### Qué pasó
- **Revisión 1:** no se hizo ni el 28 ni el 29-oct. Con los feriados del 2 y 3-nov no hubo cita. Se busca para el **jueves 5 o el viernes 6-nov**.
- **29-oct (Víctor, con Claude):**
  - versión del 29-oct de la presentación, la hoja de puntos y el guion;
  - guía de puntos de la elicitación (`07_Flujos_Diseno/2026-10-29_Guia_Puntos_Elicitacion.*`).

  Se suben con el commit del 4-nov.
- **Diego (2-nov), bloques L a Q:**
  - revisión técnica de la elicitación: TEAMSLASH v2 usa PostgreSQL y **no está en línea** (RIE-07); requerimiento nuevo RQ-24 (hora del primer contacto);
  - resumen del AS-IS;
  - casos de uso y modelo conceptual;
  - TO-BE v0.1 en 3 partes;
  - bóveda del sistema v0.1;
  - resumen de la bóveda;
  - su parte de la revisión del sprint 4, con el plan del sprint 5.

  Detalle en `00_Inbox/2026-11-02_reporte_Diego.md`.
- **Cambio de método (propuesta de Diego, 2-nov):** según la directora de carrera, recoger datos de personas lleva otra autorización, más larga. Se propone medir sin encuestas, entrevistas, observación, taller ni SUS (`00_Inbox/2026-11-02_aviso_sin_encuestas_ni_entrevistas.md`).
  - **Víctor (4-nov):** se lleva a la tutora como propuesta, no como algo decidido.
  - El Cap. III se reescribe después de su respuesta.

### 4-nov (Víctor, con Claude)
- **Revisión 1, versión del 4-nov** (`08_Reuniones_Tutora/2026-11-04_*`):
  - presentación de 16 diapositivas, con 3 nuevas: la propuesta sin datos de personas, el TO-BE, y los casos de uso con la bóveda;
  - hoja de puntos con una sección nueva y 9 decisiones;
  - guion.
- **Cronograma:**
  - las tareas de Diego del 2-nov quedan como hechas;
  - la Revisión 1 y su acta pasan al 5 o 6-nov;
  - notas en S3-T16, S4-T16 y S4-T17 por el cambio de método.

### Pendiente
- **Víctor:**
  - pedir la cita a la tutora y ensayar con Diego;
  - responder las 11 dudas de Diego del 2-nov: RQ-02, RQ-24, la sincronización de la bóveda, `_Contactos` y el LLM (A36);
  - patrones de la bóveda 1 (S3-04);
  - matriz de decisión de herramientas, CAPEX y OPEX (S4-T08, T10 y T12).
- **Después de la Revisión 1:**
  - acta;
  - Cap. III v0.4;
  - elicitación v0.2;
  - AS-IS v0.2 (bloque K de Diego).

## 2026-11-07 · Primer borrador de la tesis para la tutora

### Qué pasó
- La Revisión 1 **todavía no se hizo**. Víctor decide llevarle a la tutora un **primer borrador completo** para que corrija sobre el documento.
- Torvesa sigue sin responder. El campo de Diego (S4-T16 y S4-T17) queda en espera, por decisión de Víctor.
- **Primer borrador** (`06_Capitulos/2026-11-07_Tesis_Borrador1_v0.1.docx` y `.pdf`, 55 páginas, formato UPS):
  - portada, nota para la tutora con el estado de cada capítulo, índice, resumen provisional;
  - caps. I–III v0.3 con los cambios aceptados y sin comentarios internos;
  - al inicio del Cap. III, un recuadro con la propuesta de medir sin datos de personas (DEC-21 a DEC-23);
  - **Cap. IV Desarrollo técnico v0.1** (nuevo, `2026-11-07_Cap4_Desarrollo_Tecnico_v0.1.md`): AS-IS preliminar, 5 puntos críticos, 24 requisitos, casos de uso, modelo conceptual, TO-BE en 3 partes, componentes, bóveda, protección de datos y riesgos; costos y VAN/TIR quedan para el sprint 5;
  - esquema de los caps. V y VI (`2026-11-07_Cap5_Cap6_Esquema_v0.1.md`);
  - 59 referencias unidas; marcadores: FALTA-FUENTE 16, FALTA-DATO 30, DECIDIR-TUTORA 6, DECIDIR-VÍCTOR 3, VERIFICAR-PÁG 2.
- **Presentación y guion, versión del 7-nov** (`08_Reuniones_Tutora/2026-11-07_*`): portada, diapositiva 2 y cronograma con el borrador; el guion pide entregar el borrador impreso y acordar cómo devuelve las observaciones.

### Para revisar (Víctor)
- Incoherencias que el borrador deja a la vista:
  - el Cap. I dice «cuatro casos de prueba» y el cronograma dice 3;
  - la validación aparece del 23-nov al 5-dic en el Cap. I y del 24-nov al 5-dic en la presentación.
- ¿El censo de 5 personas del Informe Final fue real o era parte de lo simulado? (marcador en el Cap. IV).
- Pedir la cita a la tutora (SOL-09, actualizado en la app).

### Pendiente
- **Víctor:** sprint 4 (requisitos, matriz de herramientas, CAPEX y OPEX), que alimentan la sección de viabilidad del Cap. IV.
- **Después de la Revisión 1:** acta, Cap. III v0.4 y borrador v0.2 con las observaciones.

## 2026-11-10 · Borrador 2, finanzas, FODA y prototipo revisado

### Qué pasó (Víctor, con Claude)
- **Repos del prototipo:** acceso con `l333x` a `teamslash-landing` y `teamslash-api`; `teamslash-poc` da «no encontrado» (falta la invitación de Diego). Servidor y página en línea.
- **Hallazgos del código:** la clave de la API está en la página pública y también permite leer y modificar solicitudes; RQ-05 a RQ-08 ya están programados en la rama `rq18-consentimiento`, sin unir a `main`.
- **Respuestas a las 7 preguntas de Diego:** propuesta en `00_Inbox/2026-11-10_respuestas_Victor_a_Diego_PROPUESTA.md`. **Víctor aún no las aprueba.**
- **Finanzas y herramientas** (`06_Capitulos/Modelo_Negocio/2026-11-10_*`): matriz de 11 alternativas (gana el stack del prototipo, 4,14 de 5) y modelo financiero con supuestos: VAN −10.282 / 11.557 / 66.526 USD (pesimista / base / optimista). El caso depende de recuperar unas 3 obras al año; todos los montos de Torvesa son supuestos.
- **Necesidad, FODA, proceso estrella, guía de negociación y pitch** v0.1 (`06_Capitulos/` y `Modelo_Negocio/`). 18 fichas nuevas en `02_Fuentes/`.
- **Figuras** (`06_Capitulos/Figuras/2026-11-10_*`) y tablero privado de Miro: https://miro.com/app/board/uXjVEP28Oyg=/ (falta revisar a ojo que nada se salga de su marco).
- **Borrador 2 de la tesis** (`06_Capitulos/2026-11-10_Tesis_Borrador2_v0.2.docx` y `.pdf`): Cap. IV v0.2 y Caps. V–VI v0.2; caps. I–III sin cambios. Marcadores: FALTA-FUENTE 19, FALTA-DATO 35, DECIDIR-TUTORA 9, DECIDIR-VÍCTOR 7, VERIFICAR-PÁG 3.

### Pendiente
- **Víctor:** enviar SOL-09 a la tutora; mensaje a Diego (invitación, claves, rama publicada); aprobar o cambiar las respuestas a Diego; revisar el borrador 2.
- **Sin verificar:** IVA 15 % (decreto), aporte IESS, normas ISO, A9 (Oldroyd), uso de WhatsApp en Ecuador, precio de Odoo.
- **Claude:** cronograma (tareas de Diego del sprint 5 como hechas), registro de contribuciones, auditoría PII, commit y push al cerrar el día.

### 10-nov, segunda ronda (tarde)
- **Estudio de costos v0.2** (`06_Capitulos/Modelo_Negocio/2026-11-10_Estudio_Costos_v0.2.*`): TEAMSLASH como negocio (punto de equilibrio: 27, 51 y 126 clientes según el tamaño), Torvesa como cliente (VAN base USD 12.388 por su cuenta y USD 15.832 como servicio), y bóveda, asistente y AWS. Los precios de venta y los sueldos son supuestos.
- **Gantt** (`11_Planificacion/2026-11-10_Gantt_Tesis_v0.1.xlsx`), **revisión del cronograma** con 29 cambios propuestos (sin aplicar) y tablero privado de Trello: https://trello.com/b/VdkwofqC. Avance real: 36 %.
- **Flujos revisados** (`07_Flujos_Diseno/2026-11-10_Revision_Flujos.md`): 6 figuras nuevas con tiempos; `99_Scripts/figuras/Generar_Figuras.bat` las regenera (herramienta nueva, pedida por Víctor).
- **Por qué nosotros** v0.1, **documento maestro para IA** (`11_Planificacion/2026-11-10_Documento_Maestro_Para_IA.*`) y **borrador 2 v0.3** (66 páginas; solo cambia la figura del proceso central; el Cap. IV sigue con las cifras del modelo v0.1).
- Copia de todo en el Escritorio: `REVISION TRAS FABLE` (copias; la bóveda es la fuente).
- **Pendiente de Víctor:** decidir si el Cap. IV pasa a las cifras v0.2, cuál tablero de Trello se queda y los 29 cambios del cronograma.

### 2026-11-15 (domingo) · Modelo de negocio con un solo cliente, datos reales
- **Pedido de Víctor:** partir de una sola empresa (Torvesa), vender primero la idea (necesidad y oportunidad) y después la viabilidad; dos planes (Estándar y Premium, el Premium cubre lo que el Estándar no); cobrar el trabajo de los fundadores; 80 % real; Excel que la directora de carrera (Contabilidad y Auditoría) entienda sin explicación; escalamiento al final con techo de 20 empresas.
- **Modelo financiero v0.2** (`06_Capitulos/Modelo_Negocio/2026-11-15_Modelo_Financiero_v0.2.xlsx`): estructura de estudio financiero (inversión → costos → precio → ingresos → estado de resultados → flujo → evaluación), panel con listas desplegables, 63 supuestos con tipo y fuente, nombres en las fórmulas, glosario y 30 fuentes. Escenario base: Estándar USD 175/mes (VAN negativo: no devuelve el levantamiento); **Premium USD 275/mes + USD 311, VAN USD 427, TIR 26 %, B/C 1,03**; Torvesa VAN USD 13.618, se paga con 1,9 obras al año; el sistema costaría el 56 % de la utilidad de una constructora pequeña típica. Real: 71 % de lo que depende de nosotros; 6 % de lo de Torvesa.
- **Análisis financiero v0.2**, **caso de negocio v0.1**, **Por qué nosotros v0.2**, **exposición de 1 página** (.md/.docx/.pdf) y **matriz de herramientas v0.2** (portada + hoja «Por qué nosotros»). Estudio de costos v0.3 (techo de 20 y precio por tipo de empresa) queda para el escalamiento.
- **Fuentes:** +24 fichas verificadas (sueldos TI, IESS, Código del Trabajo, IR y RIMPE, retenciones, GEM Ecuador 2025, BLS, CB Insights, INEC REEM 2025, Damodaran, Superintendencia de Compañías, SRI, Kommo, Leadsales, Callbell). Tablas: `2026-11-15_Datos_Reales_Frente_A1.md` y `2026-11-15_Datos_Torvesa_Publicos.md`.
- **Hallazgos que contradicen el borrador:** TMAR 12 % no se sostiene (prima de riesgo de Ecuador 17,18 %); margen neto del sector 1,9 %, no 10 %; aporte patronal 12,15 %; Torvesa no está en la Superintendencia de Compañías y el SRI la registra como constructora de **vías** (F4210).
- **Pendiente de Víctor:** confirmar con Diego la actividad y el tipo de sociedad de Torvesa; pedir formularios 101 de 2023–2025; horas reales del levantamiento; decidir independientes o SAS, margen, plazo de recuperación y precios por tipo de empresa.

### 15-nov, segunda ronda · Presentación de 1 minuto, Trello y Gantt
- **Presentación de 1 minuto** (`06_Capitulos/Modelo_Negocio/2026-11-15_Presentacion_1min_v0.1.pptx/.pdf/.md`): 5 diapositivas (necesidad → oportunidad → planes → viabilidad → cierre y pedido), guion en las notas. Cubre S5-T11 y sirve de base para S6-T01.
- **Gantt v0.2** (`11_Planificacion/2026-11-15_Gantt_Tesis_v0.2.xlsx`; la v0.1 queda igual): estado al 15-nov, S4-T08/T10/T12 y S5-T01/T03/T05 apuntan a la v0.2, S5-T11 y S5-T14 por aprobar, y 6 filas NUEVA que salen del modelo de negocio (1 hecha, 5 pendientes). `Cronograma_Tesis.xlsx` no se tocó.
- **Trello** (https://trello.com/b/VdkwofqC, ahora «(15-nov)»): 8 tarjetas actualizadas y 6 nuevas (1 en Hecho y 5 en «Pendiente esta semana»). Nadie lo había tocado desde el 10-nov.

### 15-nov, tercera ronda · Puesta al día: borrador 3, Revisión 2 y paquete para la profe
- **Pedido de Víctor:** terminar lo atrasado, dejar lista la semana siguiente, una carpeta del estudio de costos para presentarle a la profe esta semana y un borrador 3 bien estructurado para la tutora. Se trabajó en 2 frentes en paralelo. Los archivos nuevos van fechados 16-nov, inicio de la semana de presentación.
- **Frente A · Borrador 3** (`06_Capitulos/2026-11-16_Tesis_Borrador3_v0.1.docx/.pdf`, 76 páginas, 78 referencias, 9 anexos), con nota para la tutora (DEC-18 a DEC-23):
  - Cap. I v0.4: 3 casos de prueba; Torvesa con marcador por F4210.
  - Cap. III v0.4.
  - Cap. IV v0.4: cifras del modelo v0.2, LOPDP con 10 obligaciones, trazabilidad (19 requisitos cubiertos, 3 huecos: RQ-08, 16 y 19) y riesgos.
  - Caps. V y VI v0.3 con criterios y conclusiones provisionales.
  - Matriz de riesgos v0.1 en Excel: 18 riesgos.
  - Marcadores: FALTA-FUENTE 21, FALTA-DATO 53, DECIDIR-TUTORA 9, DECIDIR-VÍCTOR 7, VERIFICAR-PÁG 3. Cambios en `06_Capitulos/2026-11-16_Cambios_Borrador3.md`.
- **Frente B:**
  - carpeta del Escritorio `PARA LA PROFE - Estudio de costos` (16 archivos) con guía de lectura (`Modelo_Negocio/2026-11-16_Guia_Lectura_Profe.*`);
  - presentación de la Revisión 2 (10 diapositivas) y guion con 10 preguntas probables (`08_Reuniones_Tutora/2026-11-16_Revision2_*`);
  - protocolo de la validación v0.1 (`11_Planificacion/2026-11-16_Protocolo_Validacion_v0.1.*`);
  - resúmenes de 1 página para Diego (Cap. I y requisitos y costos);
  - agenda de la revisión de sprint S5 y plantilla del acta de la Revisión 2;
  - 3 mensajes **en borrador, sin enviar** (`00_Inbox/2026-11-16_*_BORRADOR.md`): tutora (SOL-09), Torvesa vía Diego y Diego.
- **Carpeta** `PARA LA TUTORA - Borrador 3 y Revision 2` en el Escritorio.
- **Gantt v0.3** (`11_Planificacion/2026-11-15_Gantt_Tesis_v0.3.xlsx`): avance ponderado 43 % frente a 40 % del tiempo, si Víctor aprueba lo entregado (21 tareas por aprobar). Quedan 6 atrasadas: S3-T04 y S3-T09 (bóveda 1, solo Víctor), S3-T10 y S5-T10 (Diego), S3-T13 (sesión de negocio) y S3-T14 (revisión de sprint; su agenda ya está, falta la reunión). Trello: 12 tarjetas actualizadas y 2 nuevas.
- **Pendiente de Víctor:** revisar el borrador 3 y la carpeta de la profe; enviar los 3 mensajes; ensayar la Revisión 2; aprobar los casos de prueba; decidir RQ-25, el margen y el plazo; leer el Reglamento de la LOPDP (Decreto 904).

## 2026-11-18 · Preparación de la Revisión 2 (reunión con la tutora el jueves 19-nov)

### Qué pasó (Víctor, con Claude)
- **Lo que trajo Diego (15 y 16-nov):** horas del levantamiento (≈ 50,5 h con reuniones), claves del servidor separadas y comprobadas en línea (S7-T01), CP-03 con 20 alteraciones al azar, propuesta de que la evaluación heurística sea el CP-04, tres cambios al mensaje a Torvesa y su guion de las diapositivas 4 a 6. Ensayo por llamada previsto para hoy.
- **Presentación v0.2** (`08_Reuniones_Tutora/2026-11-18_Revision2_Presentacion_v0.2.pptx/.pdf`; la v0.1 queda igual):
  - diapositiva 2: «tres casos de prueba listos y un cuarto si acepta la heurística»;
  - diapositiva 6: cuatro tarjetas (CP-04 · M6, condicionado a DEC-23) y CP-03 con 20 alteraciones;
  - diapositiva 9: la validación empieza con la autorización de Torvesa (prevista del 23-nov al 5-dic); avance de 37 a 43 % con el 45 % del tiempo; claves separadas como avance;
  - notas del orador de las diapositivas 5, 6 y 9.
- **Guion v0.2** (`2026-11-18_Revision2_Guion_v0.2.md/.docx/.pdf`): preguntas 4 y 10 al día y pregunta nueva 11 (¿se llega si Torvesa no autoriza?).
- **Mensaje a Torvesa v0.2** (`00_Inbox/2026-11-18_Mensaje_Torvesa_via_Diego_v0.2_BORRADOR.md`): mensaje 1 con los datos de la empresa, listo para enviar; mensaje 2 con las fechas, después de DEC-21.
- Carpeta del Escritorio `PARA LA TUTORA - Borrador 3 y Revision 2` con la presentación y el guion v0.2.

### Pendiente
- **Víctor:** ensayar con Diego hoy; aprobar el mensaje 1 a Torvesa para que Diego lo envíe; en la reunión, anotar DEC-18 a DEC-23 en la plantilla del acta.
- **Después de la reunión:** acta de la Revisión 2, respuestas a la app, Cap. IV (fila del Art. 37 de la LOPDP a cumplido) y borrador 4 con las observaciones.

### 18-nov, segunda ronda · Lo previo a la validación, en Word y PDF
- **Pedido de Víctor:** lo pendiente antes de que arranque la validación y los documentos para la reunión, en Word y PDF.
- **Lista de lo previo** (`11_Planificacion/2026-11-18_Previo_Validacion_v0.1.md/.docx/.pdf`): ruta de 12 pasos con responsable, lugar, fecha y dependencia; lo que da Torvesa, lo que decide la tutora y lo que deja listo Diego. Figura en `11_Planificacion/Informes/_figuras/2026-11-18_Ruta_Previo_Validacion.png`.
- **Resumen para la tutora** (`08_Reuniones_Tutora/2026-11-18_Resumen_Tutora_Revision2_v0.1.*`): qué se trae, lo principal en cuatro líneas, las seis decisiones con nuestra propuesta y dos pedidos.
- **Protocolo v0.2** (`11_Planificacion/2026-11-18_Protocolo_Validacion_v0.2.*`; la v0.1 queda igual): fechas atadas a la autorización, CP-03 con 20 alteraciones, CP-04 condicionado a DEC-23, claves separadas hechas.
- **Mensajes a Torvesa v0.2** en Word y PDF; el adjunto apunta al protocolo v0.2.
- Todo copiado a la carpeta del Escritorio (00, 04, 07 y 08).
- **Por confirmar con Diego:** cuentas individuales, respaldo y unión de la rama `rq18-consentimiento` a la principal.

## 2026-11-20 (viernes) · La Revisión 2 se movió, decisiones de Víctor y trabajo de clase

### Qué pasó (Víctor, con Claude)
- **Revisión 2:** no se hizo el 19-nov. Falta la fecha nueva.
  - Mensaje a la tutora en borrador: `00_Inbox/2026-11-20_Mensaje_Tutora_Reprogramar_Revision2_BORRADOR.md`. Pide fecha desde el lunes 23-nov y pone primero la DEC-21.
  - Quedan bloqueadas el acta (S6-T05) y las observaciones (S6-T10 y S6-T11).
  - DEC-18 a DEC-23 siguen abiertas.
- **Decisiones de Víctor:**
  - aprobó el **mensaje 1 a Torvesa** (datos de la empresa), que envía Diego; el mensaje 2 (fechas) espera la DEC-21;
  - **DEC-24 (S6-N02):** independientes al inicio, margen de 20 % y 36 meses para recuperar el levantamiento, como ya usa el modelo v0.2.
- **Mensaje a Diego** en borrador: `00_Inbox/2026-11-20_Mensaje_a_Diego_BORRADOR.md`. Lleva el envío del mensaje 1, la Revisión 2 movida, lo previo del sistema (RQ-20, respaldo, rama RQ-18, casos de prueba) y sus horas al día.
- **Gantt v0.4** (`11_Planificacion/2026-11-20_Gantt_Tesis_v0.4.xlsx`; la v0.3 queda igual). Cambian 9 filas: S6-N02 hecha; S6-T04, T05, T10 y T11 bloqueadas; S6-T08, N01, N03 y N04 en curso. `Cronograma_Tesis.xlsx` no se tocó.
- **Trabajo de clase, fuera de la tesis:** proyecto final de Procesos para Negocios Digitales (prof. Caiza).
  - Son 14 diapositivas en PDF, en estilo McKinsey, con el proceso estrella, las horas, el costo, la rentabilidad, el Gantt y la captura real del Trello.
  - Está en `Documents\Proyecto_Final_Procesos_Torvesa` y tiene una copia en el Escritorio.
  - El método quedó guardado como skill `diapositivas-pdf`.

### Riesgo
- **La validación del 23-nov ya no es segura.** Depende de la DEC-21 (tutora) y de la autorización de Torvesa. Si la tutora responde la semana del 23, la validación se corre a la semana del 30-nov y se come parte de la holgura del 21-dic. Se decide cuando haya fecha.

### Pendiente hasta el domingo 22-nov
- **Víctor:**
  - enviar el mensaje a la tutora y el mensaje a Diego;
  - anotar sus horas del levantamiento (S6-N03);
  - revisión del sprint 6 con Diego el domingo (S6-T12).
- **Diego:**
  - enviar el mensaje 1 a Torvesa;
  - RQ-20, respaldo y rama RQ-18 (REV2-04);
  - los 3 casos de prueba (S6-T09);
  - sus horas al día.
- **Claude, cuando haya fecha o respuesta:** acta de la Revisión 2, Gantt, app y presentación. El domingo, el informe y el documento madre (tarea automática).

## 2026-11-22 (domingo) · Deberes de Requerimientos, borrador 4 y envío a la tutora

### Qué pasó (Víctor, con Claude)
- **Encuesta Kano (Deber 1 de IR, clase):**
  - el PDF que mandó Diego en la mañana era una **simulación**: tenía fechas del 25 y el 26-nov y una página que decía "simulación", así que no se usó;
  - se armó un Google Forms con un script de Apps Script y respondieron **7 personas reales, ninguna de Torvesa**;
  - resultado: 6 de 10 Indiferente; RF-01 y RF-03 De rendimiento; RF-04 De deleite; RF-06 Básico.
- **Deber 1 entregado** por Víctor en el AVAC. Ese día se hicieron cuatro cambios:
  - MoSCoW con solo 4 Must (23 %);
  - prioridad final de 4 altas, 5 medias y 1 baja;
  - todo el documento en vertical;
  - sin fechas de las respuestas.
- **Skill nueva `voz-victor`:** reglas de la forma de escribir de Víctor, medida en sus libros, más el revisor `revisar_voz.py`.
- **Deber 2, parte de Víctor:** se pasó a Diego para la verificación cruzada, la validación con un stakeholder y sus propias historias. Cierra hoy a las 23:59. Si el recorrido con Torvesa no alcanza por el feriado, se pide una prórroga al profe.
- **Borrador 4 de la tesis** (`06_Capitulos/2026-11-22_Tesis_Borrador4_v0.1`, 77 páginas):
  - redacción revisada;
  - priorización y backlog en el Cap. IV;
  - DEC-24 tomada;
  - validación prevista desde el 30-nov.
  - Detalle en `06_Capitulos/2026-11-22_Cambios_Borrador4.md`.
- **Presentación de la Revisión 2 v0.3** (`08_Reuniones_Tutora/2026-11-22_Revision2_Presentacion_v0.3.pdf`, 13 diapositivas, estilo de la skill `diapositivas-pdf`):
  - resumen ejecutivo al inicio;
  - priorización y backlog;
  - cronograma nuevo;
  - 7 decisiones.
- **Correo a la tutora** en borrador (`00_Inbox/2026-11-22_Correo_Tutora_Avances_BORRADOR.md`):
  - pide reunirse el **lunes 23 y el miércoles 25** y que revise el borrador **hasta el miércoles 25**;
  - lleva un cuadro con 9 dudas (DEC-18 a DEC-23, DEC-25 nueva, carta de respaldo y forma de devolver las observaciones).
- **Mensaje a Diego** en borrador (`00_Inbox/2026-11-22_Mensaje_a_Diego_BORRADOR.md`): el Deber 2, el reenvío del correo y lo que hay que pedirle a Torvesa.
- **Carpeta en el Escritorio** `TESIS - ENVIO TUTORA 23-nov`: borrador 4 (PDF y Word), presentación, correo (txt y html) y nota para Diego.

### Decisión nueva para la tutora
- **DEC-25:** si se cita el Kano exploratorio (7 personas fuera de Torvesa) como antecedente o se deja fuera por la DEC-21.

### Pendiente
- **Víctor:**
  - enviar el correo a la tutora y el mensaje a Diego;
  - verificar las historias de Diego;
  - unir los dos informes del Deber 2 y subirlos.
- **Diego:**
  - verificar las historias de Víctor;
  - hacer el recorrido con una persona de Torvesa;
  - pedirle a Torvesa los datos y la autorización.
- **Claude, cuando haya respuesta de la tutora:** acta, capítulo III según la DEC-21 y Gantt.

### 22-nov, noche: claridad de la tesis, Excel, repositorios y manual
- **Borrador 4 v0.2 (83 páginas):**
  - cada sigla, código y término se explica en su primer uso;
  - al inicio van el control de versiones, la lista de 37 siglas y códigos y el glosario de 17 términos;
  - en la bóveda queda `06_Capitulos/CONTROL_VERSIONES_TESIS.md`.
- **Excel:** la revisión está en `06_Capitulos/Modelo_Negocio/2026-11-22_Revision_Excel_y_Tablero_v0.1.md`. Ningún libro tiene errores de cálculo, pero hay incoherencias:
  - el estudio de costos v0.3 contradice al modelo v0.2;
  - **el "6 % de datos reales de Torvesa" es en realidad 0 datos de Torvesa** (el único "dato" es un promedio del sector);
  - el precio Premium se lleva el 30,8 % del beneficio de Torvesa, sobre el límite del 25 %;
  - la firma electrónica se cuenta dos veces.
  - **Tablero nuevo:** `2026-11-22_Tablero_Costos_v0.1.xlsx` (plan × escenario, 12 tarjetas, 4 gráficos, Datos con origen celda por celda).
- **Repositorios:** se analizaron 9 (solo lectura). El informe está en `11_Planificacion/2026-11-22_Informe_Repositorios_v0.1.md`, con 12 propuestas y 60 reglas.
  - **Se recomienda no adoptar agent-reach** (sin fuentes académicas, copia cookies) **ni los hooks de everything-claude-code** (bloquean los .md).
- **Manual de implementación v1.0** (`11_Planificacion/2026-11-22_Manual_Implementacion_v1.0.pdf`, 23 páginas): 13 secciones, plan de 12 mejoras y anexos.
- **Ninguna propuesta se aplicó:** la infraestructura sigue congelada hasta que Víctor elija.

### 22-nov, cierre: manual aplicado
- Víctor aprobó aplicar el manual y 10 de las 12 mejoras quedaron hechas. El detalle está en `11_Planificacion/2026-11-22_Implementacion_Manual.md`.
- **Skills nuevas:** `diseno-paginas` (con el DESIGN.md único) y `tablero-excel`.
- **Skills ampliadas:** `voz-victor`, con los rasgos de 2.ª generación y el revisor nuevo, y `diapositivas-pdf`, con las reglas de gráficos.
- **IA_DIEGO.md §8:** seguridad, revisión de código, atajos, formulario y el plan de Strix, que está preparado pero no se ejecutó.
- **Documentos actualizados:** `MANUAL_TESIS.md` (regla de claridad) y `CLAUDE.md` (sección "Skills y método de trabajo").
- **Repositorios de referencia:** quedaron en `F:\IA\repos_referencia\`, solo para leer.
- **Manual v1.1:** lleva la columna Estado.

## 2026-11-23 (lunes, madrugada) · Diego, Excel v0.3 y repo
- **Deber 1 de Diego:** comparado con el de Víctor en `07_Flujos_Diseno/2026-11-23_Comparacion_Deber1_Victor_Diego.md`.
  - Coinciden los datos de Kano.
  - Diego tiene 4 errores: APA 2026a/b/c, fechas viejas, códigos OBJ/NEC/CON sin explicar y "23 requisitos".
  - Diferencias para decidir: Must 4 contra 6, 130 h contra 108 h y dos listas de 12 puntos distintas.
- **Mensaje a Diego** en `00_Inbox/2026-11-23_Mensaje_a_Diego_BORRADOR.md`: correcciones, guía del Deber 2, PR, Strix y Torvesa.
- **Excel v0.3:** precio Premium 270, VAN 380, TIR 24,6 % y 4,5 % de datos propios de Torvesa (el censo).
- **Repo de Diego:**
  - PR #1 en borrador hacia `rq18-consentimiento`;
  - **hay claves antiguas en el historial de la landing:** Diego tiene que confirmar o rotar;
  - la seguridad tiene 5 fallas comprobadas, todas en `docs/TAREAS_DIEGO.md`.
- **Skill `investigacion-web`** creada.

### 23-nov, mañana: paquete final para la tutora
- **Borrador 4 v0.3** (`06_Capitulos/2026-11-23_Tesis_Borrador4_v0.3`, 84 páginas):
  - capítulo IV v0.7 y capítulos V–VI v0.6 con las cifras del Excel v0.3 (Premium 270, VAN 380, TIR 25 %, B/C 1,02, VAN Torvesa 13.755, inversión 2.235, matriz con la hora a 9,26);
  - dice que solo 1 de 22 datos es propio de Torvesa y que el Premium se lleva el 30,3 % del beneficio, sobre el límite de 25 %.
- **Presentación v0.4** (`08_Reuniones_Tutora/2026-11-23_Revision2_Presentacion_v0.4.pdf`): mismas cifras y fechas nuevas.
- **Correo** (`00_Inbox/2026-11-23_Correo_Tutora_Avances_BORRADOR.md`), que reemplaza al del 22-nov:
  - reunión el miércoles 25 o el viernes 27 (el lunes 23 ya pasó);
  - DEC-21 en esa reunión y revisión completa hasta el lunes 30;
  - párrafo sobre los mapas AS-IS y TO-BE y el cuadro de 9 dudas en lenguaje simple.
- **Escritorio:** `TESIS\01_Correo_tutora_23-nov (listo para enviar)`, con los 3 adjuntos y el correo en HTML y TXT.
- **Pendiente de Victor:** enviar el correo desde el Outlook de la UPS, con Diego en copia, y borrar el borrador viejo del 22-nov.

### 23-nov, tarde: material para presentar y Escritorio ordenado
- **Tablero para presentar v1.0** (`06_Capitulos/Modelo_Negocio/2026-11-23_Tablero_Presentacion_v1.0.xlsx`, 48 KB, y su PDF de 11 páginas):
  - 7 hojas: Inicio, Finanzas, Metricas, Herramientas, Avance, Datos y origen, y Glosario;
  - solo valores copiados del modelo v0.3, de la matriz v0.3 y de los capítulos, con origen celda por celda;
  - la nota para la IA es `2026-11-23_Tablero_Presentacion_v1.0_nota.md`.
- **Flujo de aprendizaje v0.1** (`08_Reuniones_Tutora/2026-11-23_Flujo_Aprendizaje_Avance_v0.1.pdf`): 11 diapositivas en 6 pasos, con un guion de 1 página.
- **Presentación v0.4 corregida** (sin cambiar de versión, porque no se había enviado): la diapositiva 13 y el cronograma ya dicen las fechas nuevas, y la portada dice "Victor" sin tilde.
- **Escritorio:**
  - quedaron solo `TESIS` y `COMPRAS - CRISFE`;
  - la lista de movimientos está en `Escritorio\TESIS\LEEME_movimientos_23-nov.md`;
  - la carpeta para presentar es `TESIS\00_PARA PRESENTAR - directora y tutora`, y su copia para la laptop está en `OneDrive\TESIS - para presentar 23-nov`.
- **Queda como FALTA:**
  - las líneas base de M1 y M3, que dependen de las fechas y horas que entregue Torvesa;
  - el estado de las tareas en `Cronograma_Tesis.xlsx`, sin actualizar desde el sprint 3.
