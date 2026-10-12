---
titulo: Glosario de la tesis
version: v1.0
fecha: 2026-10-11
tipo: referencia
tags: [glosario, referencia]
---

# Glosario de la tesis

Aquí se explica, en lenguaje simple, cada código y término que aparece en la bóveda, en GitHub y en los documentos. **Regla desde hoy:** la primera vez que un documento usa un código, lo explica entre paréntesis.

## 1. Códigos de la tesis

### A1–A47 · Afirmaciones que necesitan fuente
**Qué es:** las 47 frases del borrador aprobado que dicen un dato o una idea que hay que respaldar con una fuente verificada. Las numeré en la Fase 0 (la revisión inicial del borrador). **Ejemplo:** A4 = «una cotización toma entre 30 y 44 minutos». **Dónde aparece:** en la nota de la Fase 0 (`11_Planificacion/2026-10-11_F0_Validacion_Tesis.md`), en el cronograma y, desde el miércoles 14, en la matriz de fuentes.

| Código | Qué afirma el borrador | Estado hoy |
|---|---|---|
| A1 | Torvesa existe desde el 5-ago-2010 y su actividad registrada es construir vías | Por verificar · el giro real se confirma con Torvesa |
| A1b–A1d | Atiende sobre todo a clientes privados · vende por proyecto · ¿vende inmuebles? | Por confirmar con Torvesa |
| A2 | Tiene 30 colaboradores | Sin fuente |
| A3 | Tiene una cartera de 33 clientes | Dato de la empresa, falta documento |
| A4 | Hacer una cotización toma 30–44 minutos | Sin fuente → se medirá con cronómetro |
| A5 | La construcción es de los sectores menos digitalizados (índice de McKinsey) | Por verificar · posible fuente de segunda mano |
| A6 | La forma de trabajar por proyectos frena la tecnología en construcción | Por verificar |
| A7 | El personal reparte su día entre oficina y obra, con poca señal | Venía de datos simulados → se mide de nuevo |
| A8 | El término «amnesia institucional» | Sin fuente · ¿es término propio? |
| A9 | Responder en la primera hora multiplica las posibilidades de cerrar (Oldroyd, 2011) | Por verificar |
| A10 | La ventana ideal de respuesta es 5–15 minutos | Sospecha de cita mal atribuida |
| A11 | 13,3 % de los primeros contactos ocurre en menos de 15 minutos | ⛔ dato simulado, no se usa |
| A12 | 23,3 % de los clientes espera más de 24 horas | ⛔ dato simulado |
| A13 | 30 % del equipo cree que la mayoría se pierde antes del primer contacto | ⛔ dato simulado |
| A14 | 50 % no encuentra el historial completo de un cliente | ⛔ dato simulado |
| A15 | 43,3 % no confía en poder atender a los clientes de un compañero ausente | ⛔ dato simulado |
| A16 | 36,7 % dice que las confirmaciones desde obra «a veces nunca llegan» | ⛔ dato simulado |
| A17 | 56,7 % de lo urgente circula por canales que no dejan registro | ⛔ dato simulado |
| A18 | 53,3 % pone el «historial del cliente» como función más importante | ⛔ dato simulado |
| A19 | La primera versión del sistema sacó 53,83 puntos de usabilidad (SUS) | ⛔ dato simulado |
| A20 | 68 puntos es el umbral de «usabilidad aceptable» en la escala SUS | Por verificar |
| A21–A25 | Hallazgos de 5 estudios sobre CRM (Ohiomah, Habel, Alqershi, Rodriguez y Boyer, Gil-Gómez) | Por verificar cifras y páginas |
| A26 | Casi toda la evidencia de CRM móvil viene de empresas grandes de países ricos | Falta una revisión que lo respalde |
| A27–A29 | Tres «vacíos» de la literatura que justifican la tesis | Sin fuente · hay que buscarlos |
| A30 | «Muchas empresas no necesitan blockchain» | Sin cita · fuente candidata |
| A31–A36 | Precios y límites de Obsidian, Git, OpenTimestamps y del servicio de IA | Sin fuente · páginas oficiales |
| A37–A38 | Qué hace un RAG (búsqueda con IA) y el software «local-first» | Por verificar |
| A39–A41 | Por qué se elige DSR, el censo, las pruebas estadísticas y el «top-two-box» | Falta fuente de metodología |
| A42–A45 | Ley de Protección de Datos (LOPDP) y su reglamento | Leer el texto oficial |
| A46 | Política de la universidad sobre uso de IA | Buscarla |
| A47 | Scrum y Design Thinking | Falta fuente |

### M1–M6 · Metas de validación
**Qué es:** los 6 resultados medibles que el sistema debe lograr en la validación del diseño. Vienen del borrador aprobado. **Dónde aparece:** borrador, nota F0, cronograma, instrumentos.

| Código | Meta | Cómo se mide |
|---|---|---|
| M1 | Que la mitad de los clientes reciba respuesta en menos de 15 min | Registro de horas de llegada y de respuesta |
| M2 | Que hacer una cotización con ayuda de la IA tome menos que hoy (30–44 min) | Cronómetro |
| M3 | Que se pierdan menos clientes antes del primer contacto | Registro de solicitudes |
| M4 | Que cualquier vendedor encuentre el historial de un cliente ajeno, más rápido y con más aciertos | Prueba de recuperación de información |
| M5 | Que el sistema detecte el 100 % de los cambios hechos a escondidas en su registro | Prueba de integridad |
| M6 | Que la usabilidad del sistema llegue al menos a 68 puntos SUS | Cuestionario SUS |

### D1–D7 · Decisiones de la Fase 0
**Qué es:** las 7 decisiones que tomaste el 11-oct para resolver choques entre tu encargo y el borrador aprobado. **Dónde aparece:** nota F0, Informe 00, Documento madre.

| Código | Decisión | Estado |
|---|---|---|
| D1 | Lo que el borrador llama «piloto» se llama «validación del diseño en operación experimental controlada». Nunca «implementación» | Tomada |
| D2 | Marco DSR + Design Thinking para diseñar + Scrum para organizar; enfoque «mixto con predominio cuantitativo» | Falta OK de la tutora |
| D3 | Usar los OVA oficiales de la carrera (ver OVA) | Tomada |
| D4 | Dos censos: los 30 colaboradores y los 33 clientes | Tomada |
| D5 | Entregar en enero (escenario B), salvo que la tutora diga que el 15-dic es obligatorio (escenario A) | Falta respuesta de la tutora |
| D6 | Proponer quitar OpenTimestamps (sello en Bitcoin) y usar solo una huella digital SHA-256 + registro que no se puede editar | Falta OK de la tutora |
| D7 | Evaluar VAN y TIR del sistema para Torvesa; el negocio SaaS va como anexo | Tomada |

### OVA · Objetivos Vinculados al Aprendizaje
**Qué es:** las competencias que la carrera exige demostrar en la tesis. El borrador aprobado eligió 9. **Ejemplo:** OVA 6.2 = «evaluar la viabilidad técnica y económica», que se cumple con el capítulo de costos, VAN y TIR. **Dónde aparece:** borrador, plan, matriz de fuentes.

| OVA | Qué pide | Objetivo específico de la tesis |
|---|---|---|
| 4.1 | Identificar y analizar problemas complejos | OE1 diagnóstico |
| 4.2 | Formular alternativas de solución fundamentadas | OE2 diseño |
| 4.3 | Aplicar métodos y herramientas de la profesión | OE3 desarrollo |
| 5.1 | Analizar datos de desempeño organizacional | OE1 diagnóstico |
| 5.3 | Proponer planes de implementación (recursos, cronograma, riesgos) | OE5 documentación |
| 5.4 | Evaluar el impacto con indicadores (KPI) | OE4 validación |
| 6.1 | Desarrollar soluciones digitales innovadoras | OE3 desarrollo |
| 6.2 | Evaluar viabilidad técnica y económica | OE2 diseño |
| 6.3 | Aplicar seguridad y normativa digital | OE2 diseño |

### OE1–OE5 · Objetivos específicos
**Qué es:** los 5 objetivos específicos del borrador aprobado: OE1 diagnosticar · OE2 diseñar · OE3 desarrollar · OE4 validar · OE5 documentar y transferir.

### PO1–PO4 · Preguntas orientadoras
**Qué es:** las 4 preguntas que guían el proyecto técnico, que en este tipo de proyecto reemplazan a las hipótesis. **Ejemplo:** PO2 = ¿qué información mínima debe tener la ficha del cliente? **Dónde aparece:** borrador aprobado.

### CP1–CP4 · Casos de prueba del borrador
**Qué es:** 4 situaciones con las que se prueba el diseño. CP1 llega un cliente y se le asigna vendedor · CP2 se hace una cotización con IA · CP3 un vendedor deja la empresa · CP4 alguien altera un registro. **Dónde aparece:** borrador (Anexo A.9). El cronograma prevé diseñar 3 casos nuevos en el sprint 5.

### I1, I2, I3 · Instrumentos de campo
**Qué es:** los cuestionarios y guías para recoger datos reales. **I1** = encuesta a los colaboradores de Torvesa · **I2** = encuesta telefónica a los clientes · **I3** = guía de entrevista a gerencia y vendedores. **Dónde aparece:** carpeta `04_Instrumentos/` (versión 0.1; la 0.2 la corriges el miércoles 14).

### C1 (A, B, C) · Consentimiento informado
**Qué es:** el permiso firmado o verbal que exige la ley de datos personales antes de recoger información. **C1-A** = hoja que firma cada colaborador · **C1-B** = autorización verbal del cliente por teléfono · **C1-C** = autorización escrita de la gerencia para revisar documentos pasados. **Dónde aparece:** `04_Instrumentos/2026-10-11_C1_Consentimiento_LOPDP_v0.1.md`.

### P1, P2 (A, B) · Protocolos
**Qué es:** instrucciones paso a paso para aplicar los instrumentos. **P1** = cómo aplicar y dejar prueba de que los datos son reales (fecha, hora, quién aplicó) · **P2-A** = cronometrar cotizaciones en vivo · **P2-B** = revisar correos y WhatsApp pasados para medir tiempos de respuesta. **Dónde aparece:** `04_Instrumentos/`.

### Códigos de participantes y registros
**Qué es:** códigos que reemplazan nombres para proteger la privacidad. `COL-07` = colaborador n.º 7 · `CLI-12` = cliente n.º 12 · `ENT-02` = entrevista n.º 2 · `COT-03` = cotización cronometrada n.º 3 · `APL-001` = aplicación n.º 1 de un instrumento · `SOL-001` = solicitud de cotización revisada. La lista que relaciona códigos con nombres vive solo en papel o en la carpeta privada `_crudo`.

### [VOCAB]
**Qué es:** marca dentro de los instrumentos donde falta ajustar palabras al negocio real de Torvesa (¿vías?, ¿edificios?, ¿inmuebles?). Se reemplaza cuando Torvesa confirme su giro.

## 2. Códigos de organización

### Sprint, S1–S10
**Qué es:** cada semana de trabajo (método Scrum). S1 = 12–18 oct, S2 = 19–25 oct… S10 = 14–20 dic. El domingo en la noche se revisa la semana y se planifica la siguiente. **Dónde aparece:** cronograma Excel (una hoja por sprint), GitHub (cada sprint es un «milestone»).

### Código de tarea (S1-03) e issue (#3)
**Qué es:** `S1-03` = tarea 3 del sprint 1. Cada tarea tiene una **ficha en GitHub** llamada *issue*, con un número (`#3`), donde se comenta su avance. **Ejemplo:** «S1-04 · Corregir los instrumentos (#4)».

### Criterio de «hecho»
**Qué es:** cómo sabemos que una tarea está terminada, dicho de forma que no se pueda discutir. **Ejemplo:** para «corregir los instrumentos», el criterio es «aprobados por Víctor e impresos».

### Escenario A / Escenario B
**Qué es:** dos calendarios posibles. **B (el que usamos):** entrega en enero y defensa en febrero. **A:** si la tutora confirma que el 15-dic es fecha obligatoria; entonces se comprime diciembre y se recortan las tareas marcadas con ✂.

### ✂ Recortable
**Qué es:** tarea que se elimina primero si falta tiempo (por ejemplo, las pruebas de carga simuladas).

### Hito del 90 %
**Qué es:** la fecha en que la tesis debe estar casi completa: 18-dic (escenario B) u 11-dic (escenario A).

### Fase 0, Fase 0.5, Fase 1
**Qué es:** las etapas del trabajo de investigación. **Fase 0** = revisión del borrador (11-oct) · **Fase 0.5** = montar la bóveda, GitHub y los respaldos (11-oct) · **Fase 1** = buscar y verificar fuentes (12–14 oct).

### Corte
**Qué es:** el cierre de una fase en el que se hace inventario de lo logrado y se decide qué sigue. El corte de la Fase 1 es el miércoles 14-oct en la noche.

### E1–E7 · Propuesta de reorganización
**Qué es:** los 7 cambios de carpetas que propuse el 11-oct. Aprobaste E1 (marcar los datos simulados), E2 (fecha en el nombre de los instrumentos) y E6 (sacar del repo versiones repetidas).

## 3. Términos de la investigación

| Término | Qué es (simple) | Ejemplo | Dónde aparece |
|---|---|---|---|
| **DSR** (Design Science Research, investigación en ciencia del diseño) | Método de investigación para proyectos que **construyen** algo (un sistema) y lo prueban. Tiene 6 pasos: problema → objetivos → diseño → demostración → evaluación → comunicación | El borrador sigue los 6 pasos de Peffers (2007) | Borrador, metodología, D2 |
| **Design Thinking** (pensamiento de diseño) | Forma de diseñar partiendo de entender a las personas que usarán la solución (empatía) | La encuesta a clientes (I2) busca entender qué les molesta | D2, I2 |
| **Scrum** | Forma de organizar el trabajo en ciclos cortos (sprints) con revisión al final de cada uno | Cada domingo se revisa la semana | Cronograma |
| **Kanban** | Tablero con columnas (Por hacer → En curso → Hecho) para ver el avance | El tablero de GitHub (pendiente de crear) | GitHub |
| **AS-IS / TO-BE** | AS-IS = cómo funciona el proceso **hoy**; TO-BE = cómo funcionará **con el sistema** | AS-IS: el vendedor busca cotizaciones viejas en su correo | Tareas de Diego |
| **BPMN** | Notación estándar para dibujar procesos (cajas, flechas, decisiones) | Diagrama del proceso de cotización | Carpeta `07_Flujos_Diseno/` |
| **Línea base** | La medición del «antes», para comparar con el «después» | Tiempo de respuesta medido el 15–16 oct | Instrumentos, metas |
| **Medición post / pre-post** | Medir lo mismo **después** de la validación y comparar con el antes | SUS antes y después | Cronograma S9 |
| **Validación del diseño en operación experimental controlada** | Probar el diseño durante unos días con el equipo real, de forma controlada y medida. No es instalarlo definitivamente | 24-nov → 5-dic (propuesta corta: 23-nov → 2-dic) | Cronograma, plan |
| **PoC** (Proof of Concept, prueba de concepto) | Prototipo mínimo que demuestra que la idea funciona técnicamente | Formulario → base de datos → bóveda → borrador de cotización | Sprint 5 (Diego) |
| **Censo** | Encuestar a **todos**, no a una muestra | Los 30 colaboradores | Metodología (D4) |
| **SUS** (System Usability Scale) | Cuestionario de 10 preguntas que da un puntaje de usabilidad de 0 a 100; 68 se considera aceptable | «El sistema es fácil de usar» | I1 bloque D, M6 |
| **α de Cronbach** | Número que indica si las preguntas de una escala miden lo mismo de forma consistente | α = 0,80 sería bueno | Metodología |
| **Wilcoxon, McNemar, Mann-Whitney** | Pruebas estadísticas para comparar antes y después cuando hay pocos datos | ¿Mejoró el SUS? | Borrador, análisis |
| **Top-two-box** | Contar como «de acuerdo» las respuestas 4 y 5 de una escala de 1 a 5 | 18 de 30 marcaron 4 o 5 | Cap. IV antiguo (A41) |
| **Efecto Hawthorne** | La gente trabaja distinto cuando sabe que la observan | El vendedor cotiza más rápido con cronómetro | Protocolo P2 |
| **Tiempo de esfuerzo / tiempo transcurrido** | Esfuerzo = minutos de trabajo real · Transcurrido = horas o días de calendario hasta que el cliente recibe algo | 35 min de trabajo, pero entregada 2 días después | P2, M1, M2 |
| **Muestra documental** | Revisar documentos pasados (correos, WhatsApp) para sacar datos | Hora de cada solicitud y de cada respuesta | P2-B |
| **APA 7** | Norma de citas y referencias bibliográficas que exige la UPS | Oldroyd et al. (2011) | Todas las fuentes |
| **Fuente seminal** | Estudio antiguo pero fundador de una idea; se acepta si se acompaña de evidencia reciente | Nonaka y Takeuchi (1995) | Fase 1 |
| **Ficha de fuente** | Nota con los datos de una fuente: referencia APA, qué respalda, cita textual, página, estado | `oldroyd_2011.md` | `02_Fuentes/` |
| **Citekey** | Nombre corto de una fuente: apellido + año | `nonaka_1995` | Fichas |
| **Candidata / verificada / descartada** | Candidata = encontrada pero no revisada · Verificada = la abrí y el dato está ahí, con página · Descartada = no sirve | Solo se cita lo verificado | Fichas, matriz |
| **Solo resumen** | Fuente de la que solo se pudo leer el resumen; **no cuenta** como verificada | Artículo de pago | Fichas |
| **Matriz afirmación–fuente–estado** | Tabla que cruza cada afirmación (A1–A47) con sus fuentes y su estado; sirve para decidir qué entra al capítulo 1 | A9 → oldroyd_2011 (verificada) | Se crea el 14-oct en `03_Matriz_Objetivos/` |
| **Datos simulados** | Datos inventados para practicar, que no vienen de personas reales | Las 4 encuestas del proyecto integrador | `05_Datos_Campo/Diagnostico_2026_SIMULADO_no_usar/` |

## 4. Términos de negocio

| Término | Qué es (simple) | Ejemplo |
|---|---|---|
| **Lead / prospecto** | Persona o empresa que pidió información o cotización y todavía no es cliente | Una inmobiliaria pide precio de adoquinado |
| **Speed-to-lead (tiempo de primera respuesta)** | Cuánto tarda la empresa en contestar por primera vez a un prospecto | 2 horas |
| **Embudo comercial** | Etapas que recorre un prospecto: solicitud → contacto → cotización → negociación → cierre | De 10 solicitudes se cierran 2 |
| **Fuga** | Prospectos que se pierden en una etapa | 3 nunca recibieron respuesta |
| **CRM / CRM móvil** | Sistema para registrar y dar seguimiento a clientes; el móvil se usa desde el celular | TEAMSLASH |
| **TEAMSLASH** | El CRM que Víctor y Diego construyeron en el proyecto integrador; la tesis lo amplía | Landing + API + base de datos + Slack |
| **SaaS** | Software que se alquila por suscripción en internet | TEAMSLASH como producto futuro |
| **CAPEX / OPEX** | CAPEX = inversión inicial (se paga una vez) · OPEX = gasto de operación (se paga cada mes) | CAPEX: configurar el sistema · OPEX: servidor mensual |
| **VAN** (Valor Actual Neto) | Cuánto gana el proyecto, en dinero de hoy, después de pagar la inversión. Si es mayor que 0, conviene | VAN = USD 2.000 |
| **TIR** (Tasa Interna de Retorno) | La rentabilidad anual del proyecto; se compara con lo que costaría el dinero | TIR 35 % |
| **Período de recuperación (payback)** | En cuánto tiempo se recupera la inversión | 8 meses |
| **Lienzo de modelo de negocio** | Hoja de 9 bloques que resume a quién se le vende, qué valor recibe, cómo se gana dinero y qué cuesta | Se arma después del sprint 1 |
| **Propuesta de valor** | Por qué el cliente elegiría la solución | «Responder en minutos con el historial a la mano» |
| **KPI** | Indicador clave para medir el desempeño | % de solicitudes respondidas en 15 min |

## 5. Términos de tecnología

| Término | Qué es (simple) | Ejemplo |
|---|---|---|
| **Bóveda (Obsidian)** | Carpeta de notas enlazadas entre sí que se abre con el programa Obsidian | La bóveda de la tesis |
| **Bóveda 1** | Tu bóveda personal del Segundo Cerebro (Compras CRISFE). **Diego no tiene acceso** | `F:\Obsidian\Mejor elemento de compras` |
| **Bóveda 2** | La bóveda de la tesis, compartida con Diego por GitHub | `F:\Obsidian\Tesis_Torvesa` |
| **Bóveda del sistema** | La que Diego diseñará para Torvesa (fichas de clientes, cotizaciones). Se construye después, no esta semana | Sprint 4 en adelante |
| **RAG** | Búsqueda con IA: el programa busca en tus notas los fragmentos más parecidos a tu pregunta y te dice de qué archivo salieron | «¿Qué dice la tesis sobre cotizaciones?» → 3 fragmentos con su ruta |
| **Embeddings** | La forma en que la IA convierte un texto en números para comparar significados | — |
| **LLM** | Modelo de lenguaje (como Claude o ChatGPT) | El asistente que propondrá cotizaciones |
| **Local-first** | Programas que guardan los datos primero en tu equipo y funcionan sin internet | Obsidian en obra sin señal |
| **Hash SHA-256 / log de solo-anexión** | Hash = «huella digital» de un texto: si cambia una letra, cambia la huella. Log de solo-anexión = registro en el que solo se puede agregar, nunca editar | Base de la propuesta D6 |
| **OpenTimestamps** | Servicio que sella esa huella en la red de Bitcoin para probar la fecha. D6 propone quitarlo | — |
| **GitHub, repo** | Sitio donde se guarda la bóveda compartida con su historial. «Repo» = repositorio | `github.com/l333x/Tesis_Torvesa` |
| **Commit / push / pull** | Commit = guardar un cambio con un mensaje · Push = subirlo a GitHub · Pull = bajar lo que subió el otro | — |
| **Issue / milestone / Project** | Issue = ficha de una tarea · Milestone = grupo de tareas de un sprint · Project = tablero Kanban | Issue #4 en el milestone S1 |
| **_crudo** | Carpeta privada para datos con nombres o teléfonos. **Nunca se sube a GitHub** | Lista de los 33 clientes |
| **PII / auditoría PII** | PII = datos personales (nombre, cédula, teléfono, correo). La auditoría es un programa que los busca antes de subir algo | «0 hallazgos» = se puede subir |
| **LOPDP** | Ley Orgánica de Protección de Datos Personales del Ecuador (2021) | Exige consentimiento informado |
| **RO** | Registro Oficial: publicación donde salen las leyes del Ecuador | RO 459 |
| **Frontmatter** | El bloque de datos al inicio de una nota (`titulo:`, `estado:`…) que leen los programas | `estado: verificada` |
| **Lanzador** | Ícono del escritorio que abre Claude en la bóveda correcta | «Claude Tesis Torvesa» |
