---
titulo: "Capítulo III · Metodología (partes 1 y 2)"
version: "0.1"
fecha: 2026-10-19
autor_borrador: "Claude Opus 5.5 (Víctor edita)"
tarea: "S2-T12 y S2-T16 (#15), adelantadas del 24 y 25-oct"
base: "Diseño aprobado (Metodología 1–7) + decisiones D1, D2, D4 y D6 + instrumentos v0.2 (04_Instrumentos/) + fichas verificadas de 02_Fuentes/Metodologia y Normativa"
word: "2026-10-19_Cap3_Metodologia_v0.1.docx"
marcadores: "FALTA-FUENTE 5 · FALTA-DATO 4 · DECIDIR-TUTORA 3 · DECIDIR-VÍCTOR 1 · VERIFICAR-PÁG 1"
tags: [capitulo3, metodologia, borrador]
---

<!--
Versión para la IA. La de Víctor es el Word del mismo nombre.
Este capítulo cambia mucho frente al diseño aprobado (enfoque, instrumentos, registro), así que se redacta
como texto nuevo, sin tachados: los cambios frente al diseño aprobado se explican en comentarios.
Notación: {>>comentario<<} *cursiva*.
-->

# CAPÍTULO III{>>Capítulo III completo en v0.1 (adelanta S2-T12 y S2-T16). Como cambia mucho frente al diseño aprobado, va como texto limpio, y cada diferencia con el diseño aprobado se explica en un comentario. El control de cambios está activado para tus ediciones.<<}

# METODOLOGÍA

Este capítulo describe cómo se desarrolla el trabajo: el enfoque y el tipo de investigación, el marco de diseño que organiza las actividades, la población, las técnicas e instrumentos de recolección, el procedimiento, el análisis de los datos y los resguardos éticos y legales.

## Enfoque de la investigación

El trabajo adopta un enfoque mixto con predominio cuantitativo. En un diseño mixto, el investigador decide qué prioridad da a cada componente, y puede dar más peso a la recolección y al análisis de datos cuantitativos (Dawadi et al., 2021, p. 28). Aquí el componente cuantitativo es el principal: se miden tiempos de respuesta y de elaboración de cotizaciones, proporciones, aciertos en la recuperación de información, puntajes de usabilidad y resultados de pruebas antes y después de la validación. El componente cualitativo, formado por las entrevistas y las preguntas abiertas de las encuestas, sirve para reconstruir el proceso actual, explicar las causas de las demoras y orientar el diseño desde la experiencia de los colaboradores y de los clientes.{>>Decisión D2 (tutora sin objeciones, 12-oct). El diseño aprobado decía «cuantitativo» y usaba las entrevistas solo como apoyo. Falta un libro de base del método mixto: Creswell y Plano Clark (2018), en la biblioteca UPS.<<} [FALTA-FUENTE: texto de base del método mixto — Creswell y Plano Clark (2018) o Hernández-Sampieri y Mendoza (2018), biblioteca UPS]

Los dos componentes se integran en tres momentos: en el diagnóstico, los tiempos medidos se contrastan con lo que relatan los colaboradores y los clientes; en el diseño, cada requisito del sistema se vincula a un hallazgo del diagnóstico; y en la evaluación, las cifras antes y después se leen junto con las opiniones recogidas al cierre. La integración se presenta en tablas que ponen frente a frente la cifra y la cita del participante.

## Tipo de investigación

Es una investigación aplicada y de desarrollo tecnológico: produce un artefacto —el diseño del sistema y un prototipo funcional de sus componentes— y lo somete a prueba en la organización mediante cuatro casos de prueba y una validación del diseño en operación experimental controlada de dos semanas. Por su alcance, combina un nivel descriptivo, en el diagnóstico de la situación actual, con una comparación antes y después en un solo grupo, en la validación.{>>El diseño aprobado decía «experimental y tecnológica». Con un solo grupo y sin grupo de control no es un experimento en sentido estricto; «comparación antes y después en un solo grupo» es más preciso y evita objeciones del tribunal. [DECIDIR-TUTORA: confirmar si prefiere el término «preexperimental» o «cuasiexperimental de un solo grupo»]<<}

## Marco metodológico: investigación en ciencia del diseño

El trabajo se organiza con la investigación en ciencia del diseño (*Design Science Research*, DSR). La DSR genera conocimiento a partir del diseño y la evaluación de artefactos innovadores que resuelven problemas reales (Tuunanen et al., 2024) [VERIFICAR-PÁG: Tuunanen et al. 2024 — la página de la versión publicada]. Es, por eso, el marco propio de un proyecto técnico que diseña un sistema de información para una empresa. Además, la DSR admite dividir un proyecto en partes más pequeñas que se diseñan y evalúan por separado (Tuunanen et al., 2024), lo que encaja con el trabajo por ciclos cortos que se describe más adelante.

Las seis actividades del proceso de la DSR [FALTA-FUENTE: Peffers et al. (2007), las seis actividades — PDF por conseguir] se cumplen así en este trabajo:

- Identificación del problema: diagnóstico de la atención comercial actual (AS-IS) y levantamiento de la línea base con datos reales de la empresa (capítulo IV).

- Definición de los objetivos de la solución: requisitos funcionales y metas de validación M1 a M6 (capítulo I).

- Diseño y desarrollo: arquitectura, procesos objetivo (TO-BE) y prototipo funcional de los componentes, construido en ciclos cortos (capítulo IV).

- Demostración: ejecución de los cuatro casos de prueba con el equipo comercial.

- Evaluación: validación del diseño en operación experimental controlada durante dos semanas y comparación con la línea base (capítulo V).

- Comunicación: el presente documento, el manual de operación y la defensa.{>>El diseño aprobado usaba el diagnóstico simulado (N = 30) para la primera actividad. Ahora la primera actividad es el diagnóstico con datos reales.<<}

### Design Thinking para diseñar con el usuario

Dentro de la actividad de diseño se usa el *Design Thinking*, una metodología centrada en las personas que se apoya en la empatía, la generación de ideas y la experimentación (Cuadrado Torres, 2023, p. 44). Su aporte es metodológico: las encuestas y entrevistas del diagnóstico recogen lo que viven los colaboradores y los clientes (empatía), esos hallazgos definen los requisitos (definición), las alternativas de diseño se comparan antes de elegir una (ideación) y el prototipo se prueba con el equipo comercial (prototipo y prueba). El caso de Cuadrado Torres (2023), en microempresas de Manta, muestra que el *Design Thinking* se combina con métodos ágiles en empresas pequeñas del Ecuador.{>>Ojo con esta fuente: el PDF dice «Vol 23 No 38» y el DOI dice «v23i39». Se confirma en la web de la revista antes de la versión final. Falta un texto teórico base de DT: Auernhammer y Roth (2021), en tu lista de PDF a mano.<<} [FALTA-FUENTE: texto teórico base de Design Thinking — Auernhammer y Roth (2021), PDF a mano]

### Scrum para organizar el trabajo

El trabajo de diseño y desarrollo se organiza con Scrum, un marco de trabajo liviano basado en el empirismo que ayuda a los equipos a generar valor mediante soluciones adaptativas para problemas complejos (Schwaber y Sutherland, 2020, p. 3). Scrum organiza el trabajo en ciclos de duración fija llamados *sprints*, de un mes o menos (Schwaber y Sutherland, 2020, p. 7). En este proyecto, cada sprint dura una semana y cierra con una revisión de lo hecho y la planificación del siguiente. Una revisión sistemática reciente confirma que Scrum es un marco flexible y adaptable que se aplica también fuera del desarrollo de software (Sassa et al., 2023, p. 173).{>>Decisión D2: DSR para el marco, Design Thinking para diseñar y Scrum para organizar. El diseño aprobado mencionaba «Scrum y tablero Kanban»; el tablero de GitHub se descartó, así que no se menciona Kanban.<<}

## Población

La población tiene dos grupos y en ambos se trabaja por censo, sin calcular una muestra, porque son pequeños y accesibles [FALTA-FUENTE: A40 — justificación del censo en poblaciones pequeñas, Hernández-Sampieri y Mendoza (2018), biblioteca UPS]:

- Colaboradores: las 30 personas que trabajan en Torvesa [FALTA-DATO: A2 — nota de respaldo de la gerencia]. Todas responden la encuesta; los indicadores de atención al cliente se analizan solo con quienes atienden clientes o preparan cotizaciones.

- Clientes: los 33 clientes de la cartera actual [FALTA-DATO: A3 — nota de respaldo de la gerencia]. Se encuesta a la totalidad, porque son quienes mejor conocen los tiempos de respuesta y las fallas de la atención.{>>Decisión D4: dos censos. Con poblaciones de este tamaño, cada persona pesa 3,3 puntos porcentuales (colaboradores) o 3,0 (clientes): los porcentajes se informan siempre junto a la frecuencia.<<}

La unidad de análisis operativa son las solicitudes de cotización. Para la línea base se revisan las solicitudes y cotizaciones de los tres meses anteriores, anonimizadas y con autorización de la gerencia; para la evaluación, todas las solicitudes que ingresen durante la validación del diseño en operación experimental controlada.

## Técnicas e instrumentos de recolección de datos

La Tabla 1 resume qué se aplica, a quién y para qué meta. Los instrumentos completos van en los anexos.{>>La tabla se arma con formato UPS en la v0.2 (rótulo arriba, 10 pt, solo líneas horizontales). Por ahora va como lista para que la revises más fácil.<<}

- Encuesta a colaboradores (I1): censo de 30, en papel o en formulario en una sesión supervisada. Mide cómo circula la información entre la oficina y la obra, la capacidad de recuperar el historial de un cliente, el seguimiento de las solicitudes y las prioridades del equipo. Incluye la escala de usabilidad SUS en su versión validada en español (Sevilla-Gonzalez et al., 2020), que se aplica solo a quienes usan la herramienta. Metas M4 y M6.

- Encuesta a clientes (I2): censo de 33, por teléfono o con un enlace individual. Mide el tiempo de respuesta percibido, la calidad de la cotización y lo que no les ha satisfecho de la atención. Es el insumo de empatía del *Design Thinking*.

- Entrevista semiestructurada (I3): de tres a cinco personas de la gerencia y de quienes preparan cotizaciones, de 30 a 40 minutos. Sirve para reconstruir el proceso actual, que luego se dibuja en notación BPMN, y para explicar las causas de las demoras.

- Cronometraje de cotizaciones (P2-A): observación directa, con una hoja de registro, del tiempo de trabajo que toma cada cotización. Meta M2.

- Muestra documental (P2-B): revisión anonimizada de las solicitudes y cotizaciones de los últimos tres meses, en la que solo se anotan fechas y horas: solicitud, primer contacto y cotización enviada. Metas M1 y M3.

- Prueba de recuperación de información: cada colaborador que atiende clientes busca cinco datos del historial de un cliente que atiende otro compañero; se registran el tiempo y los aciertos, antes y después. Meta M4.

- Casos de prueba funcionales: cuatro casos con criterios de aceptación definidos de antemano, que se ejecutan con el equipo comercial.

- Prueba de integridad: se alteran a propósito copias de registros del sistema para comprobar que la verificación con huellas SHA-256 detecta cada alteración. Meta M5.

- Registros del sistema: los eventos que guarda el sistema (ingreso de la solicitud, aviso, primer contacto, cotización) y el historial de versiones de la bóveda, que dan los tiempos de la evaluación sin depender de la memoria de las personas.{>>Decisión D6: sin anclajes de OpenTimestamps; la integridad se prueba con huellas SHA-256 y un registro que solo se puede ampliar. El diseño aprobado decía que se «reaplicaban» los cuatro cuestionarios del diagnóstico; como sus datos eran simulados, ahora se aplican por primera vez (I1, I2) y se repiten al cierre.<<}

Para la confiabilidad de las escalas de la encuesta a colaboradores se calcula el alfa de Cronbach. Todos los instrumentos se prueban antes con una o dos personas ajenas a Torvesa para corregir preguntas confusas.

## Procedimiento

El trabajo se ejecuta en sprints semanales entre octubre de 2026 y enero de 2027:

- Revisión de la literatura y redacción de los capítulos I a III (octubre de 2026).

- Trabajo de campo para la línea base: encuestas, entrevistas, cronometraje, muestra documental y prueba de recuperación inicial, en cuanto la gerencia lo autorice y a más tardar en la semana del 2 de noviembre de 2026 [FALTA-DATO: fecha de autorización de Torvesa].

- Diseño del sistema: requisitos, procesos objetivo, arquitectura, herramientas, costos y evaluación de protección de datos (2 al 8 de noviembre de 2026).

- Prototipo funcional y evaluación financiera: construcción de los componentes y cálculo del valor actual neto y la tasa interna de retorno del sistema para Torvesa (9 al 15 de noviembre de 2026).

- Casos de prueba y capacitación del equipo (16 al 22 de noviembre de 2026).

- Validación del diseño en operación experimental controlada (23 de noviembre al 5 de diciembre de 2026).

- Medición posterior, análisis antes y después y redacción de resultados (7 al 13 de diciembre de 2026).

- Revisión con la tutora, ajustes y entrega del documento final para revisión (hasta el 4 de enero de 2027).{>>Las fechas salen de la hoja de cada sprint del cronograma vigente (D5, escenario B). El diseño aprobado tenía los sprints A–D en octubre; se movieron por el retraso del campo.<<}

## Variables e indicadores

Las variables de evaluación son cinco: la velocidad de respuesta (mediana del tiempo de primer contacto y tiempo de elaboración de la cotización), la fuga de prospectos antes del primer contacto, la continuidad de la atención (capacidad de retomar el historial de un cliente ajeno), la trazabilidad (completitud de la ficha del cliente e integridad del registro) y la usabilidad (puntaje SUS). Cada una corresponde a una meta de validación (M1 a M6, capítulo I) y se mide igual antes y después, con el mismo procedimiento y durante un período de la misma duración.

## Técnicas de análisis de datos

Los datos se procesan en Python (con las librerías pandas y SciPy) y en Jamovi. Se usa estadística descriptiva: medianas y rangos intercuartílicos para los tiempos, que suelen ser asimétricos, y frecuencias con porcentajes para las proporciones. Para comparar el antes y el después se aplican pruebas no paramétricas, adecuadas para poblaciones pequeñas, con un nivel de significación de 0,05 y el tamaño del efecto:

- Wilcoxon para mediciones pareadas de las mismas personas (SUS y prueba de recuperación).

- McNemar para preguntas de sí o no respondidas por las mismas personas antes y después (historial completo y confianza en retomar una cartera ajena).

- U de Mann-Whitney para los tiempos de primer contacto, porque las solicitudes de antes y de después son distintas.

- Prueba z de proporciones o chi-cuadrado para la fuga y el cumplimiento de la meta de 15 minutos.

Si en la validación ingresan pocas solicitudes, los resultados de M1 y M3 se informan solo de forma descriptiva [FALTA-DATO: volumen de solicitudes por semana]. Los casos de prueba se evalúan por su tasa de aprobación frente a los criterios de aceptación. Las entrevistas y las respuestas abiertas se analizan por temas: se codifican, se agrupan en categorías y se presentan en una tabla con la frecuencia de cada categoría y una cita representativa.{>>Pruebas del diseño aprobado, sin cambios. Falta una fuente para las pruebas no paramétricas con poblaciones pequeñas (sale del mismo texto de métodos de la biblioteca).<<} [FALTA-FUENTE: pruebas no paramétricas en poblaciones pequeñas — texto de métodos, biblioteca UPS]

## Aspectos éticos y protección de datos

El trabajo cumple la Ley Orgánica de Protección de Datos Personales (LOPDP, 2021) y su Reglamento General (Decreto Ejecutivo 904, 2023). Cada participante firma un consentimiento informado antes de responder (C1). El consentimiento es libre, específico, informado e inequívoco, y se puede revocar en cualquier momento (LOPDP, 2021, art. 8). El documento informa los fines del estudio, la base legal, el tiempo de conservación de los datos, el contacto del responsable y cómo ejercer los derechos (LOPDP, 2021, art. 12).

Los datos se recogen con el mínimo necesario y se conservan solo el tiempo que exige su finalidad (LOPDP, 2021, art. 10, lit. i). Los datos que identifican a una persona se guardan aparte, en una carpeta que no se comparte ni se sube a la nube; los datos con los que se trabaja están anonimizados, y los participantes se identifican con códigos. La empresa recibe solo resultados agregados. En el registro verificable no se guardan datos personales, solo las huellas digitales de los documentos.{>>El plazo de 12 meses para archivar los datos de prospectos es un plazo que fija este trabajo como responsable: la ley no fija un número, pide fijar plazos (A45, verificado el 18-oct). Se dice así en el capítulo IV.<<} [DECIDIR-TUTORA: quién figura como responsable del tratamiento (los estudiantes o la UPS) y si se necesita la aprobación de un comité de ética]

El uso de herramientas de inteligencia artificial generativa en la elaboración de este trabajo se declara en los anexos, con las fechas, las tareas y las secciones en que se usó.{>>Según el manual de estilo de la carrera, la declaración de IA va en los anexos. [DECIDIR-TUTORA: si el certificado de autoría necesita además la frase de uso de IA (DEC-11)]<<}

## Referencias de este capítulo (provisional)

Asamblea Nacional del Ecuador. (2021, 26 de mayo). *Ley Orgánica de Protección de Datos Personales*. Registro Oficial Quinto Suplemento n.º 459.

Cuadrado Torres, L. (2023). Aplicación Design Thinking y Agile Inception para el desarrollo de microempresas de servicio de cafetería. *Revista Científica Ciencia y Tecnología, 23*(38), 44–62. https://doi.org/10.47189/rcct.v23i39.615{>>Número 38 o 39: confirmar en la web de la revista.<<}

Dawadi, S., Shrestha, S., y Giri, R. A. (2021). Mixed-methods research: A discussion on its types, challenges, and criticisms. *Journal of Practical Studies in Education, 2*(2), 25–36. https://doi.org/10.46809/jpse.v2i2.20

Presidencia de la República del Ecuador. (2023, 13 de noviembre). *Reglamento General de la Ley Orgánica de Protección de Datos Personales* (Decreto Ejecutivo 904). Registro Oficial Tercer Suplemento n.º 435.{>>Autor institucional asumido como «Presidencia de la República» porque es un decreto ejecutivo. [DECIDIR-VÍCTOR: confirmar el formato con la guía de la UTPL]. En el texto se cita «(Decreto Ejecutivo 904, 2023)»; hay que hacer coincidir la cita con el autor que se elija.<<}

Sassa, A. C., Almeida, I. A. de, Pereira, T. N. F., y Oliveira, M. S. de. (2023). Scrum: A systematic literature review. *International Journal of Advanced Computer Science and Applications, 14*(4), 173–181. https://doi.org/10.14569/IJACSA.2023.0140420

Schwaber, K., y Sutherland, J. (2020). *La Guía Scrum: la guía definitiva de Scrum: las reglas del juego*. Scrumguides.org. https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-Latin-South-American.pdf

Sevilla-Gonzalez, M. D. R., Moreno Loaeza, L., Lazaro-Carrera, L. S., Bourguet Ramirez, B., Vázquez Rodríguez, A., Peralta-Pedrero, M. L., y Almeda-Valdes, P. (2020). Spanish version of the System Usability Scale for the assessment of electronic tools: Development and validation. *JMIR Human Factors, 7*(4), Artículo e21161. https://doi.org/10.2196/21161

Tuunanen, T., Winter, R., y vom Brocke, J. (2024). Dealing with complexity in design science research: A methodology using design echelons. *MIS Quarterly, 48*(2). https://doi.org/10.25300/MISQ/2023/16700
