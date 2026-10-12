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
- **D1** ✅ El piloto se llama «validación del diseño en operación experimental controlada»; nunca «implementación».
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
- El volumen de solicitudes del piloto (2 semanas, 33 clientes) puede ser bajo para las pruebas estadísticas.
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
