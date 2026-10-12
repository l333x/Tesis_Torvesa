---
titulo: Fase 0 — Validación del proyecto de investigación (tesis Torvesa)
fecha: 2026-10-11
version: v0.1
origen: claude
tipo: propuesta
area: UPS
estado: aprobado
tags: [tesis, torvesa, fase0]
---

# Fase 0 — Validación (v0.1)

> [!warning] Punto de validación
> Nada se ha movido ni creado fuera de esta nota. La fase 1 no empieza hasta que apruebes las **decisiones D1–D7** (§0) y el plan de migración (§4).

Fuente leída completa: `00_Inbox/BORRADOR DE TESIS.pdf` (22 págs.: carta aval de la tutora + carta de Torvesa del 29-sep-2026 + *Diseño de Trabajo de Titulación* + Anexo A). Contexto: `Capitulo_IV_Diagnostico…md` y `ENCUESTA1–4.csv` (N = 30 c/u).

> [!success] Decisiones de Víctor (2026-10-11)
> - **D1** ✅ Lo que el borrador llama «piloto» = «validación del diseño en operación experimental controlada». No se usa la palabra «piloto». Nunca «implementación».
> - **D2** ✅ DSR como marco + DT en la etapa de diseño + Scrum para organizar; «mixto con predominio cuantitativo». ⏳ **Cambio pendiente de aprobar con la tutora.**
> - **D3** ✅ OVA oficiales con el mapeo de §1.4.
> - **D4** ✅ Dos censos: 30 colaboradores y 33 clientes.
> - **D5** ⏳ Víctor pregunta a la tutora. **Escenario A (peor caso, el que se planifica):** hito del 90 % el 11-dic, entrega el 15-dic. **Escenario B:** plan hasta enero y defensa en febrero.
> - **D6** ⏳ Proponer a la tutora retirar OpenTimestamps y usar hash SHA-256 + log de solo-anexión. Preparar una justificación de 1 página. **No se elimina del documento hasta que ella responda.**
> - **D7** ✅ VAN/TIR del sistema para Torvesa; el SaaS va como anexo.
> - Se ignoran `UNIVERSIDAD POLITÉCNICA.pdf` y `Formato_Entrega_Proyecto Final.docx`.
> - **Riesgos a corregir:** recalcular el 13,3 % solo con los 10 asesores · el 30 % se redacta como percepción · corregir Oldroyd («primera hora») + buscar evidencia de 2023+ sobre los 5–15 min · 30–44 min: buscar fuente + protocolo de cronometraje en campo para el jueves 15 y el viernes 16 de octubre.

---

## 0. Choques entre tu encargo y el borrador aprobado → decisiones tuyas

| # | Tu encargo dice | El borrador aprobado dice | Por qué importa | Mi recomendación |
|---|---|---|---|---|
| **D1** | **Solo diseño**: las pruebas son validación o prueba de concepto, nunca implementación | Objetivo general: «…y **validarlo mediante un piloto de dos semanas** que mida su efecto». OE3 «**Desarrollar** los componentes… mediante sprints». La carta de Torvesa autoriza la «**prueba piloto con el equipo comercial**» | Cambia el objetivo general, OE3, OE4, las metas M1–M6 y el capítulo de resultados. Si se cambia el objetivo aprobado, la tutora tiene que saberlo, y quizá el Consejo de Carrera | Mantener el piloto, pero declararlo como **«validación del diseño en operación experimental controlada»**, no como implementación. Eso respeta lo aprobado y tu regla de no presentarlo como implementado (el borrador ya dice que la adopción definitiva «no depende de este trabajo»). Si prefieres quitar el piloto, se consulta con la tutora en la Revisión 1 |
| **D2** | Enfoque **mixto, descriptivo-propositivo**, Design Thinking + Scrum | Enfoque **cuantitativo**, tipo experimental-tecnológico, **DSR** (Hevner 2004; Peffers 2007) con sprints Scrum/Kanban y diseño **cuasi-experimental pre-post de un solo grupo**. El DT solo aparece como «enfoque de empatía» en la encuesta a clientes | Son dos marcos distintos. DSR es el marco natural de un Proyecto Técnico que construye un artefacto | **DSR como marco**, DT dentro de la actividad «Diseño y desarrollo» y Scrum para organizar el trabajo. Declararlo «**mixto con predominio cuantitativo**», porque ya hay entrevistas y análisis temático. En la fase 1 busco fuentes de DSR frente a DT y de DSR + DT combinados |
| **D3** | Objetivos 4.1–4.9 | **OVA 4** (4.1, 4.2, 4.3), **OVA 5** (5.1, 5.3, 5.4) y **OVA 6** (6.1, 6.2, 6.3), mapeados a OE1–OE5 | Tu numeración no coincide con el documento oficial | Usar la oficial (tabla §1.4). Tus 4.1–4.9 equivalen uno a uno |
| **D4** | Población: «~30–33 clientes potenciales» | **Dos** poblaciones en censo: **30 colaboradores** (el diagnóstico ya hecho) y **33 clientes** (encuesta nueva) | La N = 30 del diagnóstico **no son clientes** | Mantener las dos poblaciones; la limitación de no hacer inferencia aplica a ambas |
| **D5** | Entrega 4–8 ene, defensa 1–12 feb | Cronograma: 5-oct → 29-nov, presentación en dic; «**Fecha de entrega: 15 de diciembre de 2026**». La semana 1 (5–11 oct: AS-IS, encuesta a clientes, prueba de recuperación) ya pasó | Si la carrera tomó el 15-dic como fecha, tu cronograma se pasa | Confirmar con la tutora si el 15-dic es una fecha dura. ¿Se hizo algo de la semana 1? |
| **D6** | (no lo menciona) | El **registro verificable con OpenTimestamps/Bitcoin** sigue siendo un componente (Sprint D, M5, CP4, A.10) | El 28-sep propusiste quitarlo (tu D1 de entonces) | Decidir: mantenerlo como está o reducirlo a una bitácora con hash dentro de PostgreSQL. Cualquier cambio pasa por la tutora |
| **D7** | CAPEX, OPEX, VAN y TIR de nivel pitch | Limitación (g): «la evaluación financiera del modelo SaaS es **contexto y no objeto**». Pero el OVA 6.2 exige viabilidad económica | No es una contradicción, si se separan las dos cosas | VAN/TIR **del sistema para Torvesa** (horas de [[Compras|cotización]] ahorradas + leads no perdidos), y el SaaS solo como anexo de contexto |

---

## 1. Resumen del borrador (1 página)

**Título:** Diseño de un sistema de automatización para la gestión comercial en la Constructora Torvesa. Proyecto Técnico · Período 69 (sep 2026 – feb 2027) · Tutora: Tania Alexandra Chicaiza Villalba · Autores: Diego Jhoel Bermeo Torres y Víctor Alexander Segura Heredia.

**1.1 Problema.** Torvesa tiene 30 colaboradores y una cartera de 33 clientes privados, y vende por proyecto: cada solicitud exige una cotización a medida, que toma **30–44 min**. El vendedor reparte la jornada entre la oficina y obras sin señal, así que las solicitudes esperan horas o días. El conocimiento de cada cliente vive en el teléfono y en la memoria del vendedor, y el borrador llama a eso «**amnesia institucional**». El problema se declara **tecnológico**: no existe una herramienta que conserve el conocimiento comercial y lo ponga al alcance del vendedor. La dotación de personal queda fuera porque es tema de gerencia.

**Pregunta central:** ¿cómo diseñar un sistema que permita responder en el menor tiempo, dar continuidad con el vendedor titular y conservar un historial verificable de cada cliente?

**1.2 Solución.** Sobre [[TEAMSLASH]] (landing en Vercel, API Node en Railway, PostgreSQL y Slack) se diseñan tres componentes:
- una **bóveda Obsidian** con fichas, plantillas y cotizaciones, sincronizada por Git;
- un **asistente de IA con RAG** que propone borradores de cotización;
- un **registro verificable** de eventos encadenados por hash y anclados con OpenTimestamps.

PostgreSQL guarda «quién, qué y cuándo»; la bóveda guarda «el porqué». Los controles LOPDP se detallan en el Anexo A.7.

**1.3 Objetivos.**
- **OG:** diseñar el sistema y validarlo en 2 semanas de validación del diseño en operación experimental controlada (el borrador dice «piloto»).
- **OE1:** diagnóstico AS-IS y línea base.
- **OE2:** arquitectura TO-BE, requisitos, viabilidad técnica y económica, LOPDP.
- **OE3:** desarrollo en sprints A–D.
- **OE4:** 4 casos de prueba + validación del diseño en operación experimental controlada.
- **OE5:** manual, gobierno de la información y transferencia.

**1.4 Mapa de OVA (D3).**

| Tu código | OVA oficial | Objetivo específico |
|---|---|---|
| 4.1 Diagnosticar problemas | **4.1** | OE1 |
| 4.2 Analizar datos de desempeño | **5.1** | OE1 |
| 4.3 Formular alternativas | **4.2** | OE2 |
| 4.4 Viabilidad técnica y económica | **6.2** | OE2 |
| 4.5 Seguridad y normativa | **6.3** | OE2 |
| 4.6 Métodos de la profesión | **4.3** | OE3 |
| 4.7 Soluciones innovadoras | **6.1** | OE3 |
| 4.8 Impacto con KPI | **5.4** | OE4 |
| 4.9 Plan de implementación | **5.3** | OE5 |

**1.5 Metodología declarada.** Enfoque cuantitativo, tipo experimental-tecnológico, **DSR** en las 6 actividades de Peffers y diseño cuasi-experimental pre-post de un solo grupo. Censo de 30 colaboradores y de 33 clientes. La unidad de análisis son las solicitudes de la validación del diseño en operación experimental controlada.

**Instrumentos nuevos:**
- BPMN AS-IS/TO-BE, con entrevistas y una jornada de observación;
- encuesta a clientes con enfoque de empatía (DT);
- prueba de recuperación (5 datos de un cliente ajeno, midiendo tiempo y aciertos);
- 4 casos de prueba;
- prueba de integridad;
- logs `lead_events`, historial de Git y anclajes OTS.

**Instrumentos que se reaplican:** los 4 cuestionarios del diagnóstico (con SUS y α de Cronbach) y una entrevista de cierre a 3–5 personas.

**Análisis:** Python y Jamovi; Wilcoxon, McNemar, Mann-Whitney y z/χ², con α = 0,05 y tamaño del efecto; análisis temático para las entrevistas.

**1.6 Cifras citadas.** Oldroyd: «7×» en la primera hora y «60×» frente a 24 h. Del diagnóstico: 13,3 % de contactos en ≤15 min · 23,3 % esperan >24 h · 30,0 % de fuga modal antes del primer contacto · 50,0 % no encuentra el historial · 43,3 % no confía en retomar una cartera ajena · 36,7 % dice que las confirmaciones «nunca llegan» · 56,7 % usa canales no trazables · 53,3 % pone el historial como prioridad n.º 1 · SUS 53,83 frente al umbral de 68. De las fuentes: Ohiomah (108 profesionales, 55 % de varianza), Habel (0–23 pp), Alqershi (284 pymes).

**1.7 Metas M1–M6.**
- M1: mediana del speed-to-lead <15 min.
- M2: menos tiempo de cotización.
- M3: fuga menor al 30 %.
- M4: mejor recuperación de información (bajar el 50 % y el 43,3 %).
- M5: 100 % de las alteraciones detectadas.
- M6: SUS ≥ 68.

**1.8 Cronograma original.** S1 5–11 oct línea base · S2 requisitos/TO-BE · S3 sprints A+B · S4 sprints C+D · S5 casos de prueba · S6–7 validación del diseño en operación experimental controlada (9–22 nov) · S8 análisis e informe (23–29 nov) · diciembre revisión y presentación · entrega 15-dic-2026.

**1.9 Limitaciones declaradas.** Caso único sin grupo de control · línea base en parte autorreportada · N pequeña, por eso pruebas no paramétricas · efecto Hawthorne · Obsidian sin permisos por usuario · el registro prueba que no hubo alteración, no que lo registrado sea cierto · el SaaS es contexto.

> [!danger] Riesgos de fondo que veo (no tocar el texto aún; para la Revisión 1)
> 1. **Validez del dato de speed-to-lead:** el 13,3 % y el 23,3 % salen de la Encuesta 3, que respondieron **los 30 colaboradores**, incluido personal de obra y administrativo. Solo 10 de los 30 se declaran asesores comerciales. Es percepción, no registro, y se comparará contra un post medido en el sistema: esa asimetría la va a ver el tribunal.
> 2. **M3:** el 30,0 % es la *etapa modal* donde «se pierde la mayoría» (opinión), no una tasa de fuga medida. No se puede comparar contra una tasa real de la validación del diseño en operación experimental controlada.
> 3. **Composición inestable:** «Director/Gerencia» son 7 en la E1 y 11 en la E3. Con 30 colaboradores, entre 7 y 11 directivos es raro: o la autodeclaración es libre o no fueron las mismas personas. Hay que explicarlo.
> 4. **Volumen durante la validación del diseño en operación experimental controlada:** con 33 clientes en cartera, ¿cuántos leads nuevos entran en 2 semanas? Si son menos de 10, M1 y la U de Mann-Whitney quedan sin potencia.
> 5. **Probable error de atribución:** la «ventana de 5 a 15 minutos» se atribuye a Oldroyd et al. (2011), pero ese artículo habla de **la primera hora**. El dato de 5 minutos viene del *Lead Response Management Study* (Elkington y MIT, 2007). Hay que verificarlo en la fase 1.

---

## 2. Afirmaciones que necesitan fuente

Estado: 🔎 citada en el borrador, falta verificar · ❌ sin fuente · 🏠 dato propio, falta trazarlo a los datos crudos · ⚠️ sospecha de error.

### 2.1 Contexto y problema

> [!warning] ⏳ Giro del negocio PENDIENTE (Víctor lo confirma con Torvesa, 2026-10-11)
> Hasta tener la confirmación, queda pendiente toda afirmación sobre qué vende Torvesa y a quién:
> - **A1:** actividad SRI = construcción de carreteras y vías + obras de ingeniería civil.
> - **A1b:** «atiende principalmente a clientes privados —empresas, inmobiliarias, promotores de proyectos habitacionales y personas naturales—».
> - **A1c:** «su oferta se vende por proyecto; cada solicitud exige una cotización a medida».
> - **A1d:** ¿vende inmuebles (departamentos, casas, locales)? El instrumento simulado lo daba por hecho y el SRI no lo registra.
> - El ejemplo del Anexo A.3/A.4 («PRY-0001 Edificio Cumbayá», «COT-0001 Adoquinado de vía») mezcla edificación y vialidad.
> - El alcance excluye la contratación pública (SNCP). Si el giro principal son vías, hay que confirmar qué parte de la cartera es privada.
>
> Lo que responda Torvesa define el vocabulario de los instrumentos del jueves y el viernes.

| # | Afirmación | Fuente actual | Estado | Acción |
|---|---|---|---|---|
| A1 | Torvesa inició el 5-ago-2010; su actividad es la construcción de vías | SRI (2026) | 🔎 ⏳ giro pendiente | Captura de la consulta de RUC con fecha |
| A2 | 30 colaboradores | ninguna | ❌ | Documento de la empresa (nómina/IESS) o declaración de gerencia |
| A3 | Cartera de 33 clientes | «registros de la empresa» | 🏠 | Extracto anonimizado del CRM |
| A4 | Una cotización toma 30–44 min | «registros de la empresa» | 🏠 ❌ | **Crítica (base de M2)**: ¿de dónde sale? Necesita una medición documentada |
| A5 | La construcción es el penúltimo sector del índice de digitalización del MGI | Agarwal et al. (2016) | 🔎 ⚠️ | El índice original es del MGI (Manyika et al., 2015, *Digital America*); Agarwal lo cita. Buscar el original y evidencia de 2023+ |
| A6 | La lógica B2B, la fragmentación y la organización por proyectos frenan la adopción | Samuelson y Stehn (2023); Nyqvist et al. (2024) | 🔎 | Verificar páginas |
| A7 | El personal reparte la jornada entre oficina y obra con conectividad limitada | Bermeo y Segura (2026) | ⛔ datos simulados | Medirlo en la reaplicación (pregunta sobre conectividad en obra) |
| A8 | «Amnesia institucional» | diagnóstico | ❌ | ¿Término propio o de la literatura? Si es propio, declararlo y anclarlo en Walsh y Ungson |

### 2.2 Evidencia cuantitativa
| # | Afirmación | Fuente actual | Estado | Acción |
|---|---|---|---|---|
| A9 | Responder en ≤1 h → ~7× más probabilidad de calificar; >60× frente a 24 h | Oldroyd et al. (2011) | 🔎 | Confirmar cifras y página; buscar evidencia de 2023+ (seminal) |
| A10 | La ventana de referencia es de 5–15 min | Oldroyd et al. (2011) | ⚠️ | Ver el riesgo 5 (§1) |
| A11–A19 | 13,3 % · 23,3 % · 30,0 % · 50,0 % · 43,3 % · 36,7 % · 56,7 % · 53,3 % · SUS 53,83 | Bermeo y Segura (2026) | ⛔ datos simulados | **No se usan.** Se reemplazan con la reaplicación del 15–16 oct (`05_Datos_Campo/Diagnostico_2026_SIMULADO_no_usar/LEEME_Procedencia.md`) |
| A20 | El umbral normativo de la SUS es 68 | Sauro (2011); Lewis (2018); Bangor et al. (2008) | 🔎 | Verificar |
| A21 | Ohiomah et al.: 108 profesionales, PLS-SEM, 55 % de varianza | Ohiomah et al. (2019) | 🔎 | Verificar el número y la página |
| A22 | La automatización del seguimiento sube la conversión entre 0 y 23 pp | Habel et al. (2025) | 🔎 | Verificar (artículo reciente, posible *online first*) |
| A23 | Solo las dimensiones tecnológica y organizativa del CRM afectan el desempeño (284 pymes) | Alqershi et al. (2020) | 🔎 | Verificar |
| A24 | El CRM móvil solo eleva el desempeño con proceso y colaboración | Rodriguez y Boyer (2020) | 🔎 | Verificar |
| A25 | El CRM se vincula con la innovación del modelo de negocio | Gil-Gómez et al. (2020) | 🔎 | Verificar |

### 2.3 Afirmaciones sobre la literatura (vacíos)
| # | Afirmación | Estado | Acción |
|---|---|---|---|
| A26 | La evidencia de CRM móvil viene de empresas grandes y economías desarrolladas, y es autorreportada | 🔎 (3 citas) | Respaldar con una revisión sistemática reciente |
| A27 | Vacío (a): casi no se miden tiempos reales registrados | ❌ | Revisión de la literatura |
| A28 | Vacío (b): no hay evidencia en pymes constructoras latinoamericanas sin conectividad | ❌ | Búsqueda en SciELO/Redalyc/DSpace (o confirmar la ausencia) |
| A29 | Vacío (c): no se ha estudiado el uso de repositorios consultados con IA para cotizar en pymes | ❌ | Búsqueda en 2023–2026 |
| A30 | «La literatura advierte que muchas implementaciones empresariales no necesitan blockchain» | ❌ **sin cita** | Candidata: Wüst y Gervais (2018), *Do you need a blockchain?* (falta verificar) |

### 2.4 Tecnología y costos
| # | Afirmación | Estado | Acción |
|---|---|---|---|
| A31 | Obsidian es gratuito para uso comercial | ❌ | Página oficial de licencias (cambió en 2025; verificar) |
| A32 | Obsidian Sync cuesta USD 4–5 por usuario al mes | ❌ | Precio oficial con fecha de consulta |
| A33 | Obsidian no tiene permisos por usuario | ❌ | Documentación oficial |
| A34 | Git puede ser lento en Android/iOS | ❌ | Documentación del plugin o issues |
| A35 | OpenTimestamps es gratuito y no requiere criptomonedas | 🔎 Todd (2016) | Verificar |
| A36 | El costo del LLM por consumo es acotado | ❌ | Precios oficiales del [[Proveedores|proveedor]] elegido (CAPEX/OPEX) |
| A37 | RAG ancla las respuestas y reduce errores | 🔎 Lewis et al. (2020) | Seminal; buscar evidencia de 2023+ sobre alucinación con RAG |
| A38 | Local-first permite trabajar sin conexión | 🔎 Kleppmann et al. (2019) | Verificar |

### 2.5 Metodología y normativa
| # | Afirmación | Estado | Acción |
|---|---|---|---|
| A39 | DSR es el marco propio de los proyectos que construyen artefactos | 🔎 Hevner; Peffers | Más 2–3 fuentes recientes y comparación con DT y la investigación-acción (D2) |
| A40 | Censo cuando N es pequeña; no paramétricas; α de Cronbach | ❌ | Hernández-Sampieri y Mendoza (2018) u otro texto de métodos |
| A41 | Top-two-box como práctica convencional (Cap. IV) | ❌ | Fuente de investigación de mercados |
| A42 | LOPDP (2021), RO 459 | 🔎 | Verificar el número del RO |
| A43 | Reglamento General de la LOPDP (2023) | ❌ **falta en las referencias** | Agregar con el número de RO |
| A44 | Ley de Comercio Electrónico (2002), RO 557 | 🔎 | Verificar |
| A45 | Archivar a los 12 meses las fichas de leads perdidos | ❌ | Justificar con el principio de conservación de la LOPDP (artículo exacto) |
| A46 | Política de uso de IA de la UPS | ❌ | Buscarla y confirmarla en la fase 1 (es obligatoria) |
| A47 | Scrum / Design Thinking | ❌ no están en las referencias | Scrum Guide 2020 + textos base de DT + evidencia reciente |

**Resumen:** 47 afirmaciones · 19 citadas por verificar · 14 sin fuente · 11 datos propios por trazar · 3 con sospecha de error.

---

## 3. Estructura propuesta para la bóveda de investigación

### 3.1 Dónde: **bóveda separada**, `F:\Obsidian\Tesis_Torvesa\` (recomendado)
- **Se comparte con Diego** por Git sin exponer [[CRISFE]] ni tus notas personales. La bóveda actual mezcla compras, finanzas y diario.
- **El ingestor y el enlazador no la tocan.** Hoy mueven a `00_Inbox` todo lo que cae en Downloads y le ponen tags como `compras` (al Cap. IV le puso `[teamslash, compras]`).
- **Su RAG queda limpio:** solo fuentes de la tesis, sin que las compras compitan en la búsqueda.
- Alternativa: una subcarpeta `04_Proyectos/Tesis_Torvesa/` dentro de la bóveda actual. Es más simple, pero no se puede compartir.

### 3.2 Carpetas (tu base, con 3 ajustes)
```
Tesis_Torvesa/
├── 00_Inbox/
├── 01_Borrador_Aprobado/        solo lectura: PDF 29-sep + texto .md + _historico/
├── 02_Fuentes/                  una ficha .md por fuente (carpeta = categoría principal)
│   ├── Problema/ Contexto/ Metodologia/ Evidencia_Datos/
│   ├── Tecnologia_IA/ Casos_Estudio/ Normativa/ Costos_Viabilidad/
│   └── _Textos/                 PDF de acceso abierto, nombrados por citekey (autor_año)
├── 03_Matriz_Objetivos/         OVA oficiales ↔ OE ↔ fuentes ↔ capítulos
├── 04_Instrumentos/             encuestas, guías de entrevista, consentimientos (LOPDP)
├── 05_Datos_Campo/              SOLO anonimizado
│   └── Diagnostico_2026_SIMULADO_no_usar/        ENCUESTA1–4.csv + script de recálculo
├── 06_Capitulos/                Cap_X_vN.md / .docx  (nunca se sobrescribe una versión tuya)
├── 07_Flujos_Diseno/            BPMN, Mermaid, Miro (Diego)
├── 08_Reuniones_Tutora/
├── 09_Registro_Contribuciones/
├── 10_Antecedentes_Propios/     ← NUEVO
├── 11_Planificacion/            ← NUEVO
└── 99_Scripts/                  + datos/fuentes.sqlite, fuentes.csv
```

**Por qué los ajustes:**
- **10_Antecedentes_Propios:** el informe final, el proyecto integrador, el pitch y el Cap. IV son *trabajo propio previo*. Si se reusa texto de ahí sin citar, es **autoplagio**. Separarlos obliga a citarlos como «Bermeo y Segura (2026)» y no como fuente externa.
- **11_Planificacion:** el Plan v0.1 (.docx), la Fase 0 y los análisis no son capítulos ni fuentes; sin esta carpeta acabarían en el Inbox.
- **02_Fuentes/_Textos:** las fichas apuntan al PDF. Así «abrí la fuente y confirmé el dato» queda verificable.

---

## 4. Plan de migración (todo es **COPIA**; la bóveda actual no se toca)

| Origen (bóveda actual) | Destino | Nota |
|---|---|---|
| `00_Inbox/BORRADOR DE TESIS.pdf` | `01_Borrador_Aprobado/2026-09-29_Diseno_Titulacion_APROBADO.pdf` + `.md` con el texto | Versión oficial |
| `00_Inbox/Carta_Aval_Docente_Tutor….docx`, `Carta_Autorizacion_Constructora_Torvesa.docx` | `01_Borrador_Aprobado/cartas/` | Editables (en el PDF están sin firma ni cédula de la tutora) |
| `00_Inbox/Diseno_Titulacion_TEAMSLASH_…_final.docx` (28-sep, «Implementación») · `01_Raw/UPS/Tesis_TeamSlash/2026-09-27_BORRADOR DE TESIS.docx` | `01_Borrador_Aprobado/_historico/` | Superadas, se guardan como trazabilidad |
| `01_Raw/UPS/Tesis_TeamSlash/`: informe final + v4, proyecto integrador 12-05 y Sprint 5, pitch deck, master brief, propuesta concurso, manual de usuario, `teamslash.pdf`, `proyecto.pdf` | `10_Antecedentes_Propios/` | Las 4 copias del pitch → **1** (la más reciente; te muestro los hashes antes) |
| `00_Inbox/TEAMSLASH_Tablas_Comparativas_Herramientas.pdf` | `10_Antecedentes_Propios/` | Base para «herramientas elegidas/descartadas» |
| `00_Inbox/Capitulo_IV_Diagnostico_y_Analisis_de_Resultados.md` | `10_Antecedentes_Propios/` | Quitar el tag `compras` en la copia |
| `00_Inbox/ENCUESTA1–4.csv` | `05_Datos_Campo/Diagnostico_2026_SIMULADO_no_usar/` | Revisé las cabeceras: rol, antigüedad y respuestas, **sin nombres**. Confirmo celda por celda antes de copiar |
| `03_Out/UPS/2026-09-27_Analisis_Borrador_Tesis.md`, `Tesis_Plan/*` | `11_Planificacion/_historico/` | `busquedas.json` sirve de semilla para el script de la fase 1 |
| esta nota (F0) | `11_Planificacion/` | |
| `02_Wiki/UPS/Tesis_TeamSlash.md` | **se queda** | Solo le agrego un enlace a la bóveda nueva |

**No se migra:** Materias (calidad de software, Tyche, GP U1/U4), Administrativo (récord, pagos, CV), el cuadernillo y el plan de acompañamiento (personales), `Carta-CF-28732188.pdf`, `solicitud_1723515.pdf`. **Por identificar:** `UNIVERSIDAD POLITÉCNICA.pdf` (1 pág. escaneada de mayo, sin texto) y `Materias/Formato_Entrega_Proyecto Final.docx`. ¿Alguno es el formato oficial?

**Regla operativa:** como el ingestor sigue moviendo Downloads a la bóveda de compras, lo de la tesis deberías guardarlo directo en `Tesis_Torvesa/00_Inbox`. O agrego una regla al ingestor para que lo desvíe (requiere tu OK).

---

## 5. Notas para la fase 1 (sin ejecutar)
- **APIs:** OpenAlex, Crossref y arXiv no piden clave. **Semantic Scholar** funciona sin clave pero con poca tasa. **CORE** exige una clave gratuita (te la pediré). SciELO y Redalyc se consultan por OAI-PMH. DSpace (UPS, EPN, PUCE, USFQ) por OAI-PMH donde esté expuesto.
- **Informes de industria** (McKinsey, Gartner, Salesforce, HubSpot): no tienen API; se curan a mano con su URL oficial. Gartner suele estar detrás de pago, y cuando no haya acceso legal lo marco como no disponible.
- Ninguna fuente pasa a «verificada» sin haber abierto el texto y anotado la página.

## Registro
- 2026-10-11 · v0.1 · Claude (Opus 5.5) · lectura del borrador aprobado, inventario de solo lectura de la bóveda, este documento.
- 2026-10-11 · v0.1 · Víctor · decisiones D1–D7 aprobadas (D2, D5 y D6 pendientes de la tutora). Pasa a la fase 0.5 (infraestructura).
