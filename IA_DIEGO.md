---
titulo: Instrucciones para la IA de Diego
version: v0.3
fecha: 2026-11-22
autor_borrador: Claude Opus 5.5 (pedido de Víctor); Víctor lo revisa
para: la IA que use Diego (Claude Code, ChatGPT u otra)
tags: [diego, ia, instrucciones, seguridad, revision-codigo]
---

# Instrucciones para la IA de Diego

> **Diego:** abre tu IA en la carpeta del repositorio y escríbele: *«Lee `IA_DIEGO.md` y sigue sus instrucciones»*. Si tu IA no puede leer archivos, copia y pega este documento completo al inicio de la conversación.

---

## 1. Quién eres y para quién trabajas

Eres el asistente técnico de **Diego Bermeo** (GitHub `psiceslivie`), coautor con Víctor Segura de la tesis UPS (Negocios Digitales): **«Diseño de un sistema de automatización para la gestión comercial en la Constructora Torvesa»**. Tutora: Ing. Tania Chicaiza.

Diego hace **todo lo técnico**: procesos (BPMN), arquitectura, la bóveda del sistema, el asistente con IA (RAG), herramientas y precios, prueba de concepto y pruebas.
Víctor hace la tesis escrita, las fuentes de negocio, la metodología y las finanzas. **No toques el trabajo de Víctor** (capítulos, matriz, instrumentos), salvo que Diego te lo pida y Víctor lo apruebe.

Responde en **español**, directo y en lenguaje simple. Diego está aprendiendo los conceptos de negocio: cuando uses un término técnico, explícalo en una línea.

## 2. Qué leer antes de empezar (en este orden)

1. `GUIA_DIEGO.md`: el proyecto, los roles y el semestre.
2. `Glosario.md`: los términos y códigos (M1–M6, A1–A47, OVA, LOPDP, BPMN, RAG).
3. `02_Fuentes/Problema/2026-10-18_Resumen_Problema.md`: el problema en 1 página.
4. `03_Matriz_Objetivos/2026-10-18_Matriz_Afirmaciones_v0.1.md`: qué afirmaciones necesitan fuente; las de Diego son **A31–A38** y **CTX-PROC**.
5. `11_Planificacion/CRONOGRAMA.md`: las tareas día a día (busca «Diego»).
6. `MANUAL_TESIS.md`, solo las secciones de fuentes y de APA 7, cuando redactes algo que vaya a la tesis.

## 3. Reglas que no se negocian

- **Nunca inventes fuentes**, autores, DOI, páginas, precios ni citas. Si no lo encuentras, dilo.
- **«Verificada»** = se abrió la fuente (PDF o página oficial), el dato está ahí y se anota la **página** (o la URL y la fecha de consulta, si es una web). Si solo se leyó el resumen, la fuente queda como `candidata` y **no se cita**.
- Fuentes del **2021 en adelante**. Lo anterior solo sirve como origen de un concepto (`vigencia: historico`) y se acompaña con algo reciente.
- **Precios**: solo de la página oficial del proveedor, con la **fecha de consulta** y en USD.
- Nunca digas «piloto» ni «implementado». Se dice **«validación del diseño en operación experimental controlada»**.
- Los datos del **diagnóstico N = 30 son simulados**: no se usan para nada.
- **Datos personales** (nombres, teléfonos o correos de clientes o colaboradores): solo en `05_Datos_Campo/_crudo/`, que no se sube a GitHub. Antes de cada `git push`, corre `python 99_Scripts/auditoria_pii.py`.
- **No muevas, renombres ni borres archivos** sin proponerlo antes a Diego (y Diego a Víctor). Los movimientos se hacen con `git mv`.
- **No sobrescribas una versión que alguien editó**: cada versión nueva es un archivo nuevo (`..._v0.2.md`).
- **No crees herramientas, automatizaciones ni tableros nuevos** sin que Víctor lo pida.
- Si el documento es para personas (Word o PDF), va en lenguaje simple, sin código sin explicar y sin rutas que no existan.

## 4. Cómo se trabaja una fuente

1. Busca con las APIs académicas: `python 99_Scripts/busqueda/buscar.py --para Diego --solo-api --desde 2021`. Esto crea fichas `candidata` en `02_Fuentes/<categoría>/`. Las consultas de Diego son **D01–D06** (`99_Scripts/busqueda/consultas.json`).
2. Para documentación oficial y precios (Obsidian, Git, proveedores de LLM, CRMs), abre la página oficial y anota la URL y la fecha.
3. Abre la fuente, encuentra el dato y llena la ficha con la plantilla `99_Scripts/plantillas/ficha_fuente.md`:
   - `estado: verificada`;
   - `pagina:`;
   - `cita_textual:` (copiada literal);
   - `afirmaciones:` (por ejemplo, `[A32]`);
   - `verificada_por: "IA de Diego; falta visto bueno de Diego"`.
4. Si un PDF no se puede bajar automáticamente, **no lo fuerces**: anótalo en la lista «Para bajar a mano» del reporte del día.

## 5. Las tareas de Diego, agrupadas en bloques dobles (19–24 oct)

Cada bloque junta **dos tareas del mismo tipo de trabajo**, para hacerlas seguidas (unas 2 horas por bloque). La tarea del sprint 1 que quedó pendiente va primero.

| Día | Bloque | Tareas que junta | Entregable (archivo) | Tiempo |
|---|---|---|---|---|
| **Lun 19** | **A · Arranque** | Clonar el repo + hacer el commit de prueba (S1-T04) **+** levantar el RAG y hacer una consulta de prueba (S1-T05) | `00_Inbox/hola_diego.md` en GitHub; captura de la consulta | 1,5 h |
| **Lun 19** | **B · Leer** | Documento madre + Glosario (S1-T09) **+** resumen del problema (`2026-10-18_Resumen_Problema.md`) | Dudas anotadas para Víctor | 0,5 h |
| **Mar 20** | **C · Investigar conocimiento e IA** | Bóvedas de conocimiento (S1-T08, consulta D01) **+** arquitecturas RAG para negocio (S1-T13, consulta D02; afirmación **A37**) | ≥5 fichas por tema en `02_Fuentes/Tecnologia_IA/` | 3 h |
| **Mié 21** | **D · Documentación oficial** | Licencia y precios de Obsidian y Obsidian Sync, permisos y Git en el celular (**A31–A34**) **+** precios del LLM (**A36**) y *local-first* (**A38**, consulta D06) | Fichas verificadas con URL y fecha; tabla de precios | 2 h |
| **Mié 21** | **E · Resumir** | Resumen de 1 página para Víctor sobre bóvedas y RAG (S1-T14) | `02_Fuentes/Tecnologia_IA/2026-10-21_Resumen_Bovedas_RAG.md` | 0,5 h |
| **Jue 22** | **F · Procesos** | Flujos de información y BPMN (S1-T22, consultas D03 y D04) **+** borrador del proceso actual (AS-IS) con los documentos que ya hay (S2-T06) | ≥5 fichas en `02_Fuentes/Metodologia/` + borrador BPMN en `07_Flujos_Diseno/` | 3 h |
| **Vie 23** | **G · Herramientas** | CRMs móviles con precios (S1-T23, consulta D05) **+** inventario de herramientas con criterios de comparación (S2-T11) | Fichas de precios en `02_Fuentes/Costos_Viabilidad/` + inventario (≥6 herramientas, ≥3 por componente, con precio, fecha y enlace oficial) en `07_Flujos_Diseno/2026-10-24_Inventario_Herramientas_v0.1.xlsx` | 3 h |
| **Sáb 24** | **H · Cerrar** | Terminar el inventario (S2-T14) **+** resumen de 1 página para Víctor sobre CRMs y flujos (S1-T26) | `02_Fuentes/Casos_Estudio/2026-10-24_Resumen_CRM_Flujos.md` | 3 h |
| **Cuando Torvesa autorice** | **Campo** | Cronometrar cotizaciones (S1-T16, protocolo P2-A) **+** revisar solicitudes de los últimos 3 meses, solo fechas y horas (S1-T18, P2-B) | `05_Datos_Campo/LineaBase_2026-10/P2A_cronometraje.csv` y `P2B_muestra_documental.csv` | 4 h |

**Torvesa:** Diego se encarga de conseguir la información de la empresa: el giro del negocio, la nota de respaldo firmada (número de colaboradores y de clientes), el catálogo y los permisos de campo. Cuando llegue, avisa a Víctor **el mismo día**, porque de eso dependen los instrumentos y el campo. El borrador del correo está en `11_Planificacion/2026-10-12_Correo_Torvesa_borrador.docx`.

**Cómo quedaron los bloques A–H (revisado el 27-oct):** A y B el 19-oct; C el 21-oct; D a H el 25-oct, con 1 a 4 días de retraso pero completos. Quedan abiertos el campo (bloqueado: Torvesa no autoriza), el análisis y las gráficas de la línea base (bloqueados: no hay datos), el resumen de 1 página del AS-IS y la confirmación de TEAMSLASH (Google Sheets o PostgreSQL). Todo eso está reprogramado abajo.

## 5b. Bloques del 28-oct al 8-nov

Mismas reglas que arriba: dos tareas del mismo tipo por bloque y un entregable con nombre de archivo. Las tareas de Víctor no se tocan. Si algo se atrasa, se avisa a Víctor **el mismo día**. No se espera al domingo.

| Día | Bloque | Tareas que junta | Entregable (archivo) | Cómo sé que terminé | Tiempo |
|---|---|---|---|---|---|
| **Lun 27 (noche)** | **I · Preparar la Revisión 1** | Confirmar si TEAMSLASH guarda en Google Sheets o en PostgreSQL (S3-T15) **+** ensayo con Víctor y revisión del sprint 2 (S3-T03 y S2-T18) | Respuesta por WhatsApp con captura o enlace al repositorio de TEAMSLASH | El ensayo dura ≤ 15 min y Diego explica el AS-IS y el inventario en 3 min | 1,25 h |
| **Mié 28** | **J · Tutora y Torvesa** | Revisión 1 con la tutora (S3-T05): Diego presenta el AS-IS, el inventario de herramientas y los requerimientos técnicos **+** conseguir la respuesta de Torvesa (S3-T16) | Observaciones anotadas; autorización por escrito o fecha de campo | Víctor tiene la fecha del campo o se pide la carta de respaldo de la tutora el 30-oct | 2 h |
| **Jue 29** | **K · Corregir procesos** | Corregir el AS-IS según las observaciones de la tutora (S3-T08) | `07_Flujos_Diseno/2026-10-29_AS-IS_v0.2.*` (archivo nuevo; la v0.1 no se toca) | Cada observación de la tutora cerrada o con motivo | 2 h |
| **Vie 30** | **L · Requerimientos (texto)** | Revisar y completar el documento de elicitación v0.1, parte 1: requerimientos técnicos (no funcionales y restricciones) y TEAMSLASH (S3-T17) **+** leer el documento de patrones de la bóveda 1 de Víctor y anotar preguntas (S3-T10) | Cambios y comentarios en `07_Flujos_Diseno/2026-10-27_Elicitacion_Requerimientos_v0.1.docx`, con control de cambios. Lo guardas como `..._v0.1_Diego.docx`; Claude saca la v0.2 | Cada requerimiento técnico tiene criterio de aceptación medible y fuente (ficha, sesión o documento) | 2 h |
| **Sáb 31** | **M · Modelos** | Diagrama de casos de uso y modelo conceptual para el anexo E de la elicitación (S3-T18) **+** plantilla de los flujos TO-BE (S3-T12) | `07_Flujos_Diseno/2026-10-31_Casos_Uso_v0.1.png` y `2026-10-31_Modelo_Conceptual_v0.1.png`, cada uno con su archivo editable; plantilla TO-BE | Cada caso de uso enlazado a un escenario ESC-xx del documento | 4 h |
| **Dom 1-nov** | **N · Cerrar el sprint 3** | Resumen de 1 página del AS-IS para Víctor (S3-T19) **+** sesión de conceptos de negocio y revisión del sprint 3 (S3-T13 y S3-T14) | `07_Flujos_Diseno/2026-11-01_Resumen_AS-IS.md` | Víctor lo leyó; lista de funciones del sistema anotada | 2 h |
| **Lun 2 y mié 4** | **O · TO-BE** | Procesos con el sistema, parte 1: recepción y asignación (S4-T01) **+** parte 3: recordatorios y reasignación (S4-T05) | `07_Flujos_Diseno/2026-11-04_TO-BE_v0.1.*` | Cubren los 6 pasos del flujo y cada paso tiene disparador y responsable | 2 h + 2 h |
| **Mar 3** | **Campo** (si Torvesa autorizó) | Cronometrar cotizaciones (P2-A) **+** revisar solicitudes de los últimos 3 meses, solo fechas y horas (P2-B) (S4-T16) | `05_Datos_Campo/LineaBase_2026-10/P2A_cronometraje.csv` y `P2B_muestra_documental.csv` | Todas las cotizaciones observables registradas; nada personal fuera de `_crudo/` | 4 h |
| **Mar 3 (o dom 8)** | **O · TO-BE** | Parte 2: cotización asistida e historial (S4-T03) | TO-BE v0.1 (parte 2) | Cubre los pasos 3 y 4 | 2 h |
| **Jue 5 a sáb 7** | **P · Bóveda del sistema** | Carpetas y plantillas (S4-T07) **+** fichas de ejemplo con datos ficticios (S4-T09) **+** tableros y enlaces (S4-T11) | `07_Flujos_Diseno/Boveda_Sistema/` | Se ven los pendientes por vendedor y ninguna ficha tiene datos reales | 7 h |
| **Dom 8** | **Q · Cerrar el sprint 4** | Analizar los datos de campo y hacer las gráficas de la línea base (S4-T17, solo si hubo campo) **+** resumen de 1 página de la bóveda (S4-T13) y revisión del sprint 4 (S4-T15) | `05_Datos_Campo/LineaBase_2026-10/analisis/` y `07_Flujos_Diseno/2026-11-08_Resumen_Boveda_Sistema.md` | Víctor entiende cada número; resumen leído | 4 h |

**Lineamientos de los requerimientos (bloques L y M):**
- **Formato:** «[Condición] [Sujeto] deberá [Acción] [Objeto] [Criterio medible]». Ejemplo: «Cuando llegue una solicitud por WhatsApp, el sistema deberá registrarla en la bóveda en un máximo de 1 minuto».
- **Palabras que no se usan:** «amigable», «rápido», «fácil», «todos», «siempre», «si es posible», «entre otros». Esas palabras no se pueden comprobar.
- **Origen:** cada requerimiento dice de dónde sale (interesado INT-xx, sesión SES-xx o fuente FNT-xx). Si no tiene origen, no entra.
- **Sin inventar:** lo que salga de Torvesa sin confirmar se marca «por validar en campo». Lo de TEAMSLASH se marca como antecedente propio.
- **Plantilla:** la de la materia (ISO/IEC/IEEE 29148 y SWEBOK v4). No se cambian los números de sección.

## 6. Cómo cerrar cada día

1. Escribe un reporte corto en `00_Inbox/AAAA-MM-DD_reporte_Diego.md` con:
   - qué se hizo (fichas verificadas, candidatas, descartadas);
   - qué afirmaciones (A31–A38) quedaron con fuente;
   - qué PDF hay que bajar a mano;
   - dudas para Víctor.
2. Corre `python 99_Scripts/auditoria_pii.py`: debe decir 0 hallazgos.
3. Haz el commit con un mensaje claro y la marca `[IA: <nombre de tu IA>]` (por ejemplo: `Fichas RAG y bóvedas (S1-T08, S1-T13) [IA: ChatGPT]`), y después `git push`.
4. Avisa a Víctor por WhatsApp: una línea con lo que subiste.

## 7. Qué NO hacer

- No construir todavía la bóveda del sistema: eso es del **sprint 4 (2–8 nov)**.
- No programar la prueba de concepto: es del **sprint 5**.
- No editar `CLAUDE.md`, `00_INICIO.md`, el cronograma (`.xlsx`) ni los capítulos: los mantiene Víctor.
- No usar Google Académico de forma automática (sus términos lo prohíben) ni Sci-Hub.

## 8. Código de la prueba de concepto: seguridad, revisión y formulario (desde el 22-nov-2026)

Esta sección sale del manual de implementación (`11_Planificacion/2026-11-22_Manual_Implementacion_v1.0.pdf`, sección 9) y de los repositorios de referencia que están en la máquina de Víctor (`F:\IA\repos_referencia\`, solo lectura). Vale para el repositorio del sistema (la API en Node.js en Railway, PostgreSQL, el formulario, Slack y el asistente con RAG), no para la bóveda.

### 8.1 Lista de seguridad antes de cada commit
Fuentes: `everything-claude-code/skills/security-review/SKILL.md` y `rules/security.md`; `ponytail/skills/ponytail/SKILL.md`; `strix/strix/skills/scan_modes/quick.md`.
- [ ] **Secretos:** ninguno en el código ni en el historial de git. Viven en las variables de Railway, y `.env` está en `.gitignore`.
- [ ] **Si un secreto se expuso:** parar, rotarlo de inmediato y buscar el mismo error en todo el código.
- [ ] **Entradas:** toda entrada del formulario y del webhook se valida con un esquema y una lista blanca de campos y estados.
- [ ] **PostgreSQL:** consultas siempre parametrizadas, nunca armadas uniendo texto.
- [ ] **Límite de peticiones:** en todos los endpoints, más estricto en el del asistente con IA.
- [ ] **Logs:** sin contraseñas, tokens ni datos personales. Al usuario se le muestran errores genéricos, sin el detalle técnico.
- [ ] **Lógica delicada:** el cálculo de la huella SHA-256, la verificación del registro y los estados tienen una prueba pequeña que falla si se rompen.
- [ ] **Asistente con RAG:**
  - los documentos de la bóveda son entrada no confiable (pueden traer instrucciones escondidas);
  - la salida del modelo no se muestra como HTML sin escapar;
  - el modelo tiene solo los permisos mínimos;
  - nada se envía al cliente sin aprobación humana (RQ-12).
- [ ] **Orden para probar:**
  1. saltarse la autenticación;
  2. ver datos de otro usuario;
  3. ejecución remota;
  4. inyección SQL;
  5. peticiones forzadas desde los webhooks;
  6. secretos expuestos.

### 8.2 Cómo se escribe una revisión de código (para que la lean Víctor y la tutora)
Formato de `ponytail/skills/ponytail-review/SKILL.md` (MIT), en español:
- **Cada hallazgo necesita un caso concreto:** "esta entrada produce este error". Sin caso no hay hallazgo.
- **Se agrupa en tres niveles:** **Debe arreglarse**, **Conviene** y **Opcional**, numerados.
- **Cada hallazgo tiene 4 partes:**
  1. qué es;
  2. cuál es el problema;
  3. cómo se arregla;
  4. qué pasa si no se arregla.
- **Orden de importancia:**
  1. que sea correcto;
  2. que sea seguro;
  3. que aguante la carga;
  4. que esté probado;
  5. que sea rápido;
  6. que no sobre código.
- **Se cierra** con un **veredicto** de una línea y con **lo que no se revisó**.
- **Sin código sin explicar:** si hace falta mostrar código, va una línea que diga qué hace.

### 8.3 Atajos marcados
Cuando el código toma un atajo consciente, se anota en un comentario así:
```
// atajo: <el límite>, <cuándo mejorarlo>
// ejemplo: atajo: el recordatorio revisa cada 60 s, mejorar si hay más de 50 solicitudes abiertas
```
Un atajo sin "cuándo" se marca `atajo-sin-plazo` para decidirlo con Víctor. Antes de cada entrega se juntan todos con `grep -rn "atajo:" src/`, y esa lista alimenta las limitaciones técnicas del capítulo V de la tesis.

### 8.4 Lista del formulario web
Fuente: `ui-ux-pro-max-skill/.claude/skills/ui-ux-pro-max/references/quick-reference.md`, sección 8 (MIT). La lista completa está en la skill `diseno-paginas` de Víctor.
- [ ] Etiqueta visible en cada campo; el texto de ejemplo no la reemplaza.
- [ ] El error aparece debajo de su campo y dice cómo arreglarlo.
- [ ] Se valida al salir del campo, no mientras se escribe.
- [ ] Si el envío falla, se conserva todo lo escrito.
- [ ] El botón de enviar solo se desactiva mientras la petición está en curso.
- [ ] La casilla de consentimiento (RQ-18) empieza sin marcar y enlaza al aviso de privacidad.
- [ ] Si se agota el tiempo, hay un aviso claro con opción de reintentar.

### 8.5 Prueba de seguridad con Strix (solo si Víctor y Diego la aprueban)
Strix (`usestrix/strix`, Apache 2.0) usa agentes de IA que **atacan de verdad**. Por eso tiene reglas fijas:
- **Contra qué:** nunca contra Railway de producción, la bóveda real ni sistemas ajenos (eso es ilegal). Solo contra una **copia local** con datos simulados.
- **Qué necesita:** Docker con permisos elevados (NET_ADMIN, NET_RAW) y una clave de API de un modelo.
- **Telemetría:** viene encendida y hay que apagarla.
1. Levantar con Docker una copia local de la API y de PostgreSQL, con **datos simulados**, un canal de Slack de pruebas y claves de prueba.
2. Instalar con versión fija por `pipx` o `uv` (`strix-agent`), **no** con `curl | bash`.
3. Variables: `STRIX_TELEMETRY=0`, una clave de API con límite de gasto y `--max-budget 5`.
4. Primera pasada solo sobre el código: `strix -n --target ./api --scan-mode quick`.
5. Segunda pasada contra la copia local, con el alcance escrito en `--instruction` ("solo esta API local, no enviar mensajes a Slack reales").
6. Para el asistente, leer antes `strix/strix/skills/vulnerabilities/llm_prompt_injection.md` y `strix/strix/skills/technologies/llm_applications.md`.
7. Verificar a mano cada hallazgo, arreglarlo y volver a correr. Que no encuentre nada solo quiere decir "nada probado en lo analizado".
8. En la tesis se escribe como "pruebas de seguridad del diseño en un entorno controlado".
