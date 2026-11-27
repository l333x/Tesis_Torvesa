---
titulo: "Cap3 Metodologia v0.7"
fecha: 2026-11-27
base: "2026-11-22_Cap3_Metodologia_v0.6.md (no se modifica)"
autor_borrador: "Claude (Victor revisa)"
estado: "propuesta; aplica el sí que el equipo propone a DEC-21, DEC-22 y DEC-23. Si la tutora acepta, se quitan los marcadores [DECIDIR-TUTORA]; si no, se vuelve a la v0.6 en las secciones marcadas"
cambios: "Enfoque cuantitativo; medición con documentos de Torvesa, registros del sistema y casos de prueba CP-01 a CP-04; M6 por evaluación heurística; ética y LOPDP sin datos de personas; una tabla por meta. Lista completa al final"
marcadores: "DECIDIR-TUTORA 13 · FALTA-FUENTE 6 · FALTA-DATO 8 · DECIDIR-VÍCTOR 2 · VERIFICAR-PÁG 1 (30 en total)"
---

<!--
Versión para la IA. La v0.6 queda igual. Todo lo que depende de la respuesta de la tutora lleva [DECIDIR-TUTORA: DEC-xx].
Si la tutora dice que no a DEC-21: vuelven el enfoque mixto, la población de dos censos, las encuestas I1 e I2, la entrevista I3, el cronometraje P2-A, el SUS y el consentimiento C1 de la v0.6.
-->

# CAPÍTULO III

# METODOLOGÍA

Este capítulo describe cómo se desarrolla el trabajo: el enfoque y el tipo de investigación, el marco de diseño que organiza las actividades, la unidad de análisis, las técnicas e instrumentos de recolección, el procedimiento, los indicadores de cada meta, el análisis de los datos y los resguardos éticos y legales.

## Enfoque de la investigación

El trabajo adopta un enfoque cuantitativo. [DECIDIR-TUTORA: DEC-22, enfoque cuantitativo en lugar de mixto con predominio cuantitativo] Todo lo que se evalúa se expresa en cifras: tiempos de respuesta y de elaboración de cotizaciones, proporciones de solicitudes perdidas, aciertos en la recuperación de información, alteraciones detectadas en el registro y número de problemas de usabilidad según su gravedad. [FALTA-FUENTE: texto de base del enfoque cuantitativo, Hernández-Sampieri y Mendoza (2018), biblioteca UPS]

Un diseño mixto puede dar prioridad al componente cuantitativo y dejar al cualitativo un papel secundario (Dawadi et al., 2021, p. 28). Esa fue la propuesta inicial de este trabajo, con entrevistas y preguntas abiertas a los colaboradores y a los clientes. El trabajo no recoge datos de personas (encuestas, entrevistas, observación ni cuestionarios), porque la autorización que exige la carrera para hacerlo toma más tiempo que el plazo de entrega. Sin un componente cualitativo, el diseño mixto ya no se sostiene y el enfoque queda como cuantitativo. [DECIDIR-TUTORA: DEC-21, medir sin datos de personas]

Los datos salen de tres fuentes que no dependen de la memoria ni de la opinión de nadie: los documentos de la empresa, de los que solo se toman fechas, horas y estados de las solicitudes; los registros que el propio sistema guarda de cada evento; y los casos de prueba que ejecutan los autores en condiciones controladas.

## Tipo de investigación

Es una investigación aplicada y de desarrollo tecnológico. Produce un artefacto, que es el diseño del sistema y un prototipo funcional de sus componentes, y lo somete a prueba mediante cuatro casos de prueba y una validación del diseño en operación experimental controlada de dos semanas en Torvesa. Por su alcance, combina un nivel descriptivo, en el diagnóstico de la situación actual, con una comparación antes y después en un solo grupo durante la validación. [DECIDIR-TUTORA: DEC-19, nombre del diseño: comparación antes y después en un solo grupo o diseño preexperimental]

En este trabajo, el grupo es el proceso comercial de la empresa y no un conjunto de personas: se comparan las solicitudes de cotización que llegaron antes del sistema con las que llegan durante la validación. Por eso las mediciones de antes y de después no son pareadas.

## Marco metodológico: investigación en ciencia del diseño

El trabajo se organiza con la investigación en ciencia del diseño (*Design Science Research*, DSR). La DSR genera conocimiento a partir del diseño y la evaluación de artefactos innovadores que resuelven problemas reales (Tuunanen et al., 2024) [VERIFICAR-PÁG: Tuunanen et al. 2024: la página de la versión publicada]. Es, por eso, el marco propio de un proyecto técnico que diseña un sistema de información para una empresa. Además, la DSR admite dividir un proyecto en partes más pequeñas que se diseñan y evalúan por separado (Tuunanen et al., 2024), lo que encaja con el trabajo por ciclos cortos que se describe más adelante.

Las seis actividades del proceso de la DSR [FALTA-FUENTE: Peffers et al. (2007), las seis actividades: PDF por conseguir] se cumplen así en este trabajo:

- Identificación del problema: diagnóstico de la atención comercial actual, es decir, del proceso tal como funciona hoy (llamado AS-IS), y cálculo de la línea base, que es el valor de cada indicador antes del sistema, con los documentos de la empresa (capítulo IV).

- Definición de los objetivos de la solución: requisitos funcionales y metas de validación M1 a M6, que son las seis condiciones medibles que el diseño debe cumplir (capítulo I).

- Diseño y desarrollo: arquitectura, procesos objetivo (el proceso tal como debería funcionar con el sistema, llamado TO-BE) y prototipo funcional de los componentes, construido en ciclos cortos (capítulo IV).

- Demostración: ejecución de los cuatro casos de prueba, identificados como CP-01 a CP-04, por los autores y con datos ficticios.

- Evaluación: validación del diseño en operación experimental controlada durante dos semanas y comparación con la línea base (capítulo V).

- Comunicación: el presente documento, el manual de operación y la defensa.

### Design Thinking para diseñar con el usuario

Dentro de la actividad de diseño se usa el *Design Thinking*, una metodología centrada en las personas que se apoya en la empatía, la generación de ideas y la experimentación (Cuadrado Torres, 2023, p. 44). El caso de Cuadrado Torres (2023), en microempresas de Manta, muestra que el *Design Thinking* se combina con métodos ágiles en empresas pequeñas del Ecuador. [FALTA-FUENTE: texto teórico base de Design Thinking: Auernhammer y Roth (2021), PDF a mano]

Como el trabajo no recoge datos nuevos de personas, la empatía se construye con lo que ya existe. La fuente principal es el informe final de TEAMSLASH, el proyecto integrador de la carrera que los autores hicieron con Torvesa en 2026 y que incluyó un censo de cinco personas de la empresa (Bermeo y Segura, 2026). A eso se suman las fechas y horas de los documentos de la empresa. Esos hallazgos definen los requisitos (definición), las alternativas de diseño se comparan antes de elegir una (ideación) y el prototipo se prueba con los casos de prueba y en la validación (prototipo y prueba).

Como antecedente para priorizar funciones, en la asignatura de Ingeniería de Requerimientos se aplicó una encuesta exploratoria basada en el modelo de Kano a siete personas de otras empresas, ninguna de Torvesa. No forma parte de la medición de las metas y, si se cita, se presenta con esa limitación. [DECIDIR-TUTORA: DEC-25, si se cita la encuesta exploratoria de Kano] [FALTA-FUENTE: modelo de Kano, solo si la tutora acepta citarla]

### Scrum para organizar el trabajo

El trabajo de diseño y desarrollo se organiza con Scrum, un marco de trabajo liviano basado en el empirismo que ayuda a los equipos a generar valor mediante soluciones adaptativas para problemas complejos (Schwaber y Sutherland, 2020, p. 3). Scrum organiza el trabajo en ciclos de duración fija llamados *sprints*, de un mes o menos (Schwaber y Sutherland, 2020, p. 7). En este proyecto, cada sprint dura una semana y cierra con una revisión de lo hecho y la planificación del siguiente. Una revisión sistemática reciente confirma que Scrum es un marco flexible y adaptable que se aplica también fuera del desarrollo de software (Sassa et al., 2023, p. 173).

## Unidad de análisis y población

La unidad de análisis es la solicitud de cotización: cada pedido de un cliente o de un interesado que llega a Torvesa por cualquier canal. Se trabaja con todas las solicitudes de dos períodos, sin calcular una muestra:

- Línea base: todas las solicitudes que llegaron entre el 1 de septiembre y el 29 de noviembre de 2026, los tres meses anteriores a la validación. La empresa entrega solo fechas, horas, canal y estado de cada una, sin datos de los clientes [FALTA-DATO: documentos de Torvesa para la línea base].

- Validación: todas las solicitudes que ingresen durante las dos semanas de la validación del diseño en operación experimental controlada, tomadas de los registros del sistema.

Se usan tres meses para la línea base, y no dos semanas, porque una empresa pequeña recibe pocas solicitudes y un período corto daría muy pocos casos para calcular una mediana estable [FALTA-DATO: volumen de solicitudes por semana en Torvesa]. Los indicadores de las metas M1 y M3 son medianas y proporciones, que no dependen de la duración del período.

Los casos de prueba no trabajan con solicitudes reales. Los ejecutan los dos autores, identificados como E1 y E2, con datos ficticios marcados como tales. Los colaboradores y los clientes de Torvesa no responden encuestas ni entrevistas: el equipo comercial usa el sistema durante la validación, pero lo que se analiza son los registros de las solicitudes, no las personas. [DECIDIR-TUTORA: DEC-21]

## Técnicas e instrumentos de recolección de datos

La Tabla 1 resume las cuatro técnicas que se usan, de dónde sale cada dato y a qué meta sirve. Los instrumentos completos van en los anexos.

**Tabla 1.** *Técnicas de recolección de datos, fuente y metas*

| Técnica | Fuente del dato | Qué registra | Metas |
|---|---|---|---|
| Revisión documental | Documentos de Torvesa de los tres meses anteriores (cuaderno, hoja de cálculo, correo o chat del teléfono de la empresa) | Fecha y hora de llegada, canal, fecha y hora de la primera respuesta, si hubo cotización y el resultado; sin datos de clientes | M1 y M3 (línea base) |
| Registros del sistema | Registro de eventos del sistema durante la validación | Hora de llegada, hora del primer contacto, estado y motivo de pérdida de cada solicitud | M1 y M3 (validación) |
| Casos de prueba | Ejecución de CP-01 a CP-04 por los autores, con datos ficticios | Tiempos, aciertos, alteraciones detectadas y problemas de usabilidad | M2, M4, M5 y M6 |
| Verificación de integridad | Copia del registro con alteraciones introducidas a propósito | Alteraciones detectadas entre las simuladas | M5 |

*Nota.* Elaboración propia. Si la tutora no acepta la propuesta de no recoger datos de personas, se suman las encuestas, la entrevista, el cronometraje y el cuestionario de usabilidad de la versión anterior del capítulo. [DECIDIR-TUTORA: DEC-21]

- Revisión documental: la empresa llena una plantilla con una fila por solicitud y solo con fechas, horas, canal y estado, sin nombres, teléfonos, correos ni direcciones (Anexo 10). Si Torvesa no guarda un registro ordenado de sus solicitudes, la plantilla se llena a partir del chat y del correo del teléfono de la empresa, y la propia empresa copia solo las horas. Es un riesgo previsto: las micro y pequeñas empresas suelen no guardar registro de sus operaciones, lo que complica mejorar sus procesos (Martínez Mendoza et al., 2023, p. 4836). Cada fila indica si la hora es exacta o reconstruida.

- Registros del sistema: el sistema guarda cada evento (ingreso de la solicitud, aviso, toma por un responsable, primer contacto, cotización y cierre) en un registro de solo agregar, en el que los eventos nuevos se suman y los anteriores no se pueden cambiar. Para el análisis se exporta solo el código de la solicitud, las horas, el canal, el estado y el motivo de pérdida, sin datos de los clientes ni de los usuarios. Se cuenta como primer contacto la primera respuesta de una persona de Torvesa al cliente, por llamada o por mensaje; el aviso automático y la sola toma de la solicitud no cuentan. [DECIDIR-VÍCTOR: confirmar qué cuenta como primer contacto en el sistema; hoy la prueba de concepto guarda la hora en que alguien toma la solicitud]

- Casos de prueba funcionales: cuatro casos, uno por cada meta que se mide en condiciones controladas: CP-01, tiempo de elaboración de una cotización (M2); CP-02, recuperación del historial de un cliente (M4); CP-03, detección de alteraciones del registro (M5); y CP-04, evaluación heurística de la usabilidad (M6). Cada caso tiene criterios de aceptación definidos de antemano (Anexo 9). Los autores hacen la mitad de las tareas con el sistema y la mitad sin él, en orden cruzado, para que lo aprendido en la primera tarea no favorezca siempre a la misma condición; y quien prepara el material de un caso no lo ejecuta cuando conocer las respuestas cambia el resultado.

- Evaluación heurística (CP-04): cada autor recorre por separado el formulario, el aviso, la ficha del cliente, el borrador de cotización y los tableros, y anota los problemas que encuentra contra una lista reconocida de principios de usabilidad, con una escala de gravedad de 0 a 4. Después se unen las dos listas y se acuerda la gravedad de cada problema. Reemplaza al cuestionario de usabilidad del sistema (SUS, por sus siglas en inglés), que es un cuestionario a personas. [DECIDIR-TUTORA: DEC-23, M6 por evaluación heurística como CP-04] [FALTA-FUENTE: fuente vigente de las heurísticas de usabilidad y de su escala de gravedad]

- Verificación de integridad (dentro de CP-03): se alteran a propósito copias del registro para comprobar que la verificación con huellas SHA-256 detecta cada alteración. Una huella SHA-256 es un código que se calcula a partir del contenido de un documento; cualquier cambio en el documento produce, con una probabilidad muy alta, una huella distinta (National Institute of Standards and Technology [NIST], 2015, p. iv).

El proceso actual se dibuja en notación BPMN (*Business Process Model and Notation*), con un carril por cada participante (Object Management Group, 2013, pp. 25–26). El modelo se preparó con el informe final de TEAMSLASH (Bermeo y Segura, 2026) y se contrasta con las fechas y horas de los documentos, sin entrevistas.

## Procedimiento

El trabajo se ejecuta en sprints semanales entre octubre de 2026 y enero de 2027:

- Revisión de la literatura y redacción de los capítulos I a III (octubre de 2026).

- Diseño del sistema: requisitos, procesos objetivo, arquitectura, herramientas, costos y evaluación de protección de datos (2 al 8 de noviembre de 2026).

- Prototipo funcional y evaluación financiera: construcción de los componentes y cálculo del valor actual neto y la tasa interna de retorno del sistema para Torvesa (9 al 15 de noviembre de 2026).

- Casos de prueba CP-01 a CP-03, primera ronda de la evaluación heurística (CP-04) y capacitación del equipo comercial en el uso del sistema (16 al 29 de noviembre de 2026).

- Pedido de los documentos de la línea base a Torvesa, desde el 27 de noviembre de 2026 [FALTA-DATO: fecha de entrega de los documentos y autorización escrita de Torvesa].

- Validación del diseño en operación experimental controlada: dos semanas desde el 30 de noviembre de 2026, sujetas a la respuesta de la tutora sobre el método y a la autorización de Torvesa [FALTA-DATO: fechas confirmadas], según su protocolo: requisitos para empezar, roles, registro diario, criterios para detenerla y cierre (Anexo 8).

- Cierre del registro, verificación de su integridad, segunda ronda de la evaluación heurística, análisis antes y después y redacción de resultados (hasta el 20 de diciembre de 2026).

- Revisión con la tutora, ajustes y entrega del documento final para revisión (hasta el 4 de enero de 2027).

## Indicadores de las metas de validación

Cada meta de validación tiene un indicador, una fuente, una forma de cálculo, un valor de antes, un valor de después y una regla de cumplimiento, que se fijan antes de medir para no ajustarlos a lo que salga. Las Tablas 2 a 7 los presentan meta por meta.

**Tabla 2.** *Meta M1: tiempo hasta el primer contacto*

| Elemento | Definición |
|---|---|
| Indicador | Mediana, en minutos, del tiempo entre la llegada de la solicitud y el primer contacto; además, el porcentaje de solicitudes con primer contacto en 15 minutos o menos |
| Fuente del dato | Antes: plantilla llenada por Torvesa con sus documentos. Después: registro de eventos del sistema |
| Cómo se calcula | Hora del primer contacto menos hora de llegada, en minutos corridos. Las solicitudes sin primer contacto no entran en la mediana y se cuentan en M3. Las que llegan fuera del horario de atención se informan también por separado |
| Línea base (antes) | Solicitudes del 1 de septiembre al 29 de noviembre de 2026 [FALTA-DATO: M1, línea base con los documentos de Torvesa] |
| Medición después | Todas las solicitudes de las dos semanas de la validación |
| Meta | Mediana menor a 15 minutos en la validación |

*Nota.* Elaboración propia. La meta de 15 minutos es una decisión de diseño que coincide con el plazo que fijó la propia empresa en el censo de TEAMSLASH; no es un estándar probado (véase el capítulo I).

**Tabla 3.** *Meta M2: tiempo de elaboración de una cotización*

| Elemento | Definición |
|---|---|
| Indicador | Mediana, en minutos, del tiempo para dejar lista una cotización, con el asistente de inteligencia artificial (IA) y sin él |
| Fuente del dato | CP-01: cuatro solicitudes ficticias, ejecutadas por E1 y E2 en orden cruzado (ocho mediciones) |
| Cómo se calcula | Tiempo desde que se abre la solicitud hasta que la cotización queda lista para revisión. Se informan la mediana, el mínimo y el máximo de cada condición |
| Línea base (antes) | Condición sin asistente, con las plantillas de la bóveda pero sin borrador propuesto |
| Medición después | Condición con asistente |
| Meta | La mediana con el asistente es menor que sin él; el 100 % de los borradores cita al menos un documento; ninguno sale sin revisión de una persona; ninguno trae precios |

*Nota.* Elaboración propia a partir de los casos de prueba (Anexo 9). Sin datos de personas, la línea base de M2 es la condición sin asistente del caso de prueba y no el cronometraje de quien cotiza en la empresa. [DECIDIR-TUTORA: DEC-21] La bóveda es el repositorio de notas donde el sistema guarda las fichas de los clientes, las plantillas y el historial.

**Tabla 4.** *Meta M3: solicitudes perdidas antes del primer contacto*

| Elemento | Definición |
|---|---|
| Indicador | Proporción de solicitudes perdidas antes del primer contacto (fuga previa al primer contacto) |
| Fuente del dato | Antes: plantilla llenada por Torvesa. Después: estados y motivos de pérdida del registro del sistema |
| Cómo se calcula | Solicitudes que nunca recibieron respuesta, más las que el cliente retiró antes de recibirla, dividido para el total de solicitudes del período. Se informa como frecuencia sobre el total y porcentaje con un decimal |
| Línea base (antes) | Solicitudes del 1 de septiembre al 29 de noviembre de 2026 [FALTA-DATO: M3, línea base con los documentos de Torvesa] |
| Medición después | Todas las solicitudes de las dos semanas de la validación |
| Meta | Proporción en la validación menor que la de la línea base |

*Nota.* Elaboración propia. Una solicitud cuenta como perdida antes del primer contacto aunque se haya respondido después, si el cliente ya había avisado que no seguía.

**Tabla 5.** *Meta M4: recuperación del historial de un cliente ajeno*

| Elemento | Definición |
|---|---|
| Indicador | Tiempo, en minutos, y aciertos, de 0 a 5, al responder cinco preguntas sobre un cliente ficticio que atiende otra persona |
| Fuente del dato | CP-02, ejecutado por E1 y E2; el material lo prepara la otra persona |
| Cómo se calcula | Tiempo desde que se reciben las preguntas hasta la última respuesta; aciertos contra la hoja de respuestas preparada de antemano. Mediana, mínimo y máximo por condición |
| Línea base (antes) | Condición sin bóveda: la información está repartida en archivos y mensajes sueltos, como hoy |
| Medición después | Condición con bóveda |
| Meta | Con la bóveda, menos tiempo y al menos los mismos aciertos |

*Nota.* Elaboración propia a partir de los casos de prueba (Anexo 9). Sin datos de personas, M4 deja de medir cuántos colaboradores no encuentran la información completa o no confían en retomar una cartera ajena, que venían de la encuesta a colaboradores. [DECIDIR-TUTORA: DEC-21]

**Tabla 6.** *Meta M5: detección de alteraciones del registro*

| Elemento | Definición |
|---|---|
| Indicador | Porcentaje de alteraciones simuladas que la verificación de integridad detecta |
| Fuente del dato | CP-03, sobre una copia del registro |
| Cómo se calcula | Alteraciones detectadas dividido para las simuladas. Se simulan 20 alteraciones al azar: 7 de contenido, 7 de contenido con la huella recalculada y 6 de borrado de un evento intermedio |
| Línea base (antes) | No aplica: hoy no existe un registro que se pueda verificar |
| Medición después | Al cierre de la validación, sobre una copia del registro real; el original debe salir íntegro |
| Meta | 100 % de las alteraciones detectadas y el registro original íntegro |

*Nota.* Elaboración propia. Límite que se declara: si se borran los últimos eventos de la cadena, la verificación no lo nota; por eso se propone publicar la última huella en el reporte semanal. [DECIDIR-VÍCTOR: aprobar las 20 alteraciones de CP-03]

**Tabla 7.** *Meta M6: usabilidad del sistema*

| Elemento | Definición |
|---|---|
| Indicador | Número de problemas de usabilidad de gravedad 3 o 4, en una escala de 0 a 4, que quedan sin corregir y sin una corrección planificada |
| Fuente del dato | CP-04, evaluación heurística hecha por separado por E1 y E2, con las dos listas unidas |
| Cómo se calcula | Conteo de problemas por gravedad y por pantalla recorrida, después de acordar la gravedad de cada uno |
| Línea base (antes) | Primera ronda, antes de la validación |
| Medición después | Segunda ronda, al cierre de la validación |
| Meta | Ningún problema de gravedad 3 o 4 sin corregir o sin una corrección planificada |

*Nota.* Elaboración propia. [DECIDIR-TUTORA: DEC-23] La meta aprobada era un puntaje igual o superior a 68 en el cuestionario SUS, el valor de referencia de la escala (Hyzy et al., 2022, p. 2), con la versión validada en español (Sevilla-Gonzalez et al., 2020). Si la tutora no acepta el cambio, se vuelve a esa meta y a ese cuestionario.

## Técnicas de análisis de datos

Los datos se procesan en Python, con las librerías pandas y SciPy, y en Jamovi. Se usa estadística descriptiva: medianas y rangos intercuartílicos para los tiempos, que suelen ser asimétricos, y frecuencias con porcentajes para las proporciones. Para comparar el antes y el después de M1 y M3 se aplican pruebas no paramétricas, adecuadas para muestras pequeñas, con un nivel de significación de 0,05 y el tamaño del efecto:

- U de Mann-Whitney para los tiempos de primer contacto (M1), porque las solicitudes de antes y de después son distintas.

- Prueba exacta de Fisher o chi-cuadrado para la proporción de solicitudes perdidas antes del primer contacto (M3) y para el cumplimiento del plazo de 15 minutos; la de Fisher se usa cuando alguna casilla tiene menos de cinco casos.

Si en la validación ingresan pocas solicitudes, los resultados de M1 y M3 se informan solo de forma descriptiva [FALTA-DATO: volumen de solicitudes por semana en Torvesa]. Los casos de prueba (M2, M4, M5 y M6) se informan con medianas, mínimos y máximos o con conteos, sin pruebas estadísticas, porque tienen pocas mediciones, y se evalúan por su cumplimiento frente a los criterios de aceptación. [FALTA-FUENTE: pruebas no paramétricas en muestras pequeñas: texto de métodos, biblioteca UPS]

Las limitaciones del método se declaran desde ahora:

- Un solo caso y dos semanas de validación, sin grupo de control: los resultados no se generalizan ni prueban una relación causal estricta.

- Los casos de prueba los ejecutan los autores, que conocen el sistema mejor que cualquier usuario; la práctica recomendada para la evaluación heurística es contar con varios evaluadores independientes.

- La línea base depende de que Torvesa entregue sus documentos, y parte de las horas puede ser reconstruida.

- El equipo comercial sabe que la validación se está midiendo y puede responder más rápido solo por eso.

- Sin el cuestionario SUS, la usabilidad se mide sin la opinión de los usuarios. [DECIDIR-TUTORA: DEC-23]

## Aspectos éticos y protección de datos

El trabajo cumple la Ley Orgánica de Protección de Datos Personales (LOPDP, 2021) y su Reglamento General (Decreto Ejecutivo 904, 2023). La investigación no recoge datos de personas: no hay encuestas, entrevistas, observación ni cuestionarios, y por eso no se aplica un consentimiento informado a participantes. [DECIDIR-TUTORA: DEC-21]

Lo que se analiza son registros anonimizados de la empresa. La LOPDP define la anonimización como la aplicación de medidas dirigidas a impedir la identificación o reidentificación de una persona natural sin esfuerzos desproporcionados (LOPDP, 2021, art. 4), y no se aplica a los datos anonimizados mientras no sea posible identificar a su titular (LOPDP, 2021, art. 2, lit. c). Para que eso se cumpla:

- Torvesa llena la plantilla de la línea base en sus propias instalaciones y entrega solo fechas, horas, canal y estado; los autores nunca reciben nombres, teléfonos, correos, direcciones ni capturas de pantalla.

- Cada solicitud se identifica con un código consecutivo. Si la empresa guarda la relación entre el código y el cliente, esa relación no sale de Torvesa.

- La exportación de los registros del sistema para el análisis lleva solo códigos, horas, estados y motivos de pérdida.

- En el registro verificable no se guardan datos personales, solo las huellas digitales de los documentos y un seudónimo de quien hizo cada cambio.

- Los archivos se revisan antes de guardarse para comprobar que no traen datos personales; si alguno los trae, se devuelve a la empresa y no se usa.

Durante la validación, el sistema sí trata datos de los clientes, porque es parte de la operación comercial de Torvesa: quien llena el formulario da su consentimiento, que es libre, específico, informado e inequívoco y se puede revocar en cualquier momento (LOPDP, 2021, art. 8), y recibe la información que exige la ley sobre los fines, la base legal, el tiempo de conservación, el contacto del responsable y la forma de ejercer sus derechos (LOPDP, 2021, art. 12). Los datos se conservan solo el tiempo que exige su finalidad (LOPDP, 2021, art. 10, lit. i); al terminar la validación se eliminan o se anonimizan los de los prospectos que no siguieron. El asistente de IA recibe solo códigos de cliente, nunca nombres, teléfonos ni correos, y ningún borrador llega al cliente sin la revisión de una persona. [DECIDIR-TUTORA: DEC-20, quién figura como responsable del tratamiento de los datos de los clientes (Torvesa, los estudiantes o la UPS) y si se necesita la aprobación de un comité de ética]

El uso de herramientas de inteligencia artificial generativa en la elaboración de este trabajo se declara en los anexos, con las fechas, las tareas y las secciones en que se usó.

## Referencias de este capítulo (provisional)

Asamblea Nacional del Ecuador. (2021, 26 de mayo). *Ley Orgánica de Protección de Datos Personales*. Registro Oficial Quinto Suplemento n.º 459.

Bermeo, D., y Segura, V. (2026). *TEAMSLASH: Ecosistema digital de gestión de clientes para la Constructora Torvesa* [Informe final del proyecto integrador, Universidad Politécnica Salesiana]. [FALTA-DATO: confirmar con la carrera si se cita como trabajo no publicado]

Cuadrado Torres, L. (2023). Aplicación Design Thinking y Agile Inception para el desarrollo de microempresas de servicio de cafetería. *Revista Científica Ciencia y Tecnología, 23*(38), 44–62. https://doi.org/10.47189/rcct.v23i39.615

Dawadi, S., Shrestha, S., y Giri, R. A. (2021). Mixed-methods research: A discussion on its types, challenges, and criticisms. *Journal of Practical Studies in Education, 2*(2), 25–36. https://doi.org/10.46809/jpse.v2i2.20

Hyzy, M., Bond, R., Mulvenna, M., Bai, L., Dix, A., Leigh, S., y Hunt, S. (2022). System Usability Scale benchmarking for digital health apps: Meta-analysis. *JMIR mHealth and uHealth, 10*(8), Artículo e37290. https://doi.org/10.2196/37290

Martínez Mendoza, E., Jiménez Antonio, D., y Fernández Echeverría, E. (2023). Definición y mejora de procesos en ausencia de registros de operación. *Ciencia Latina Revista Científica Multidisciplinar, 7*(6), 4836–4852. https://doi.org/10.37811/cl_rcm.v7i6.9039

National Institute of Standards and Technology. (2015). *Secure Hash Standard (SHS)* (FIPS PUB 180-4). U.S. Department of Commerce. https://doi.org/10.6028/NIST.FIPS.180-4

Object Management Group. (2013). *Business Process Model and Notation (BPMN), version 2.0.2* (OMG Document No. formal/2013-12-09). https://www.omg.org/spec/BPMN/2.0.2/PDF

Presidencia de la República del Ecuador. (2023, 13 de noviembre). *Reglamento General de la Ley Orgánica de Protección de Datos Personales* (Decreto Ejecutivo 904). Registro Oficial Tercer Suplemento n.º 435.

Sassa, A. C., Almeida, I. A. de, Pereira, T. N. F., y Oliveira, M. S. de. (2023). Scrum: A systematic literature review. *International Journal of Advanced Computer Science and Applications, 14*(4), 173–181. https://doi.org/10.14569/IJACSA.2023.0140420

Schwaber, K., y Sutherland, J. (2020). *La Guía Scrum: la guía definitiva de Scrum: las reglas del juego*. Scrumguides.org. https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-Latin-South-American.pdf

Sevilla-Gonzalez, M. D. R., Moreno Loaeza, L., Lazaro-Carrera, L. S., Bourguet Ramirez, B., Vázquez Rodríguez, A., Peralta-Pedrero, M. L., y Almeda-Valdes, P. (2020). Spanish version of the System Usability Scale for the assessment of electronic tools: Development and validation. *JMIR Human Factors, 7*(4), Artículo e21161. https://doi.org/10.2196/21161

Tuunanen, T., Winter, R., y vom Brocke, J. (2024). Dealing with complexity in design science research: A methodology using design echelons. *MIS Quarterly, 48*(2). https://doi.org/10.25300/MISQ/2023/16700

## Cambios frente a v0.6

<!-- Sección para Victor y la IA; no va al borrador. -->

- Enfoque: de mixto con predominio cuantitativo a cuantitativo (DEC-22). Dawadi et al. (2021) se mantiene para explicar por qué el mixto ya no se sostiene.
- Se declara que no se recogen datos de personas y por qué (DEC-21). Salen la encuesta a colaboradores (I1), la encuesta a clientes (I2), la entrevista (I3), el cronometraje (P2-A), el alfa de Cronbach y el análisis por temas de respuestas abiertas.
- Tipo de investigación: cuatro casos de prueba en lugar de tres; se aclara que el grupo es el proceso comercial y que las mediciones no son pareadas; marcador de DEC-19 sobre el nombre del diseño.
- DSR: la demostración la hacen los autores con datos ficticios (ya no "con el equipo comercial o"); se explican AS-IS, TO-BE, línea base y M1 a M6 en su primer uso.
- Design Thinking: la empatía sale del informe de TEAMSLASH y de los documentos, no de encuestas nuevas. Se agrega la encuesta Kano exploratoria como antecedente condicionado a DEC-25.
- Población: pasa a "Unidad de análisis y población". Ya no hay censos de 30 colaboradores y 33 clientes; la unidad es la solicitud de cotización, en dos períodos (1-sep a 29-nov de 2026 y las dos semanas de la validación). Salen los marcadores A2, A3 y A40 de este capítulo (siguen en el Cap. I).
- Se quita la frase "durante un período de la misma duración": la línea base usa tres meses y la validación dos semanas; se explica por qué no afecta a medianas y proporciones.
- Técnicas: nueva Tabla 1 (la v0.6 la anunciaba pero no la tenía). Revisión documental con plantilla (Anexo 10, nuevo; ver `05_Datos_Campo/2026-11-27_Pedido_Datos_Torvesa_v0.1.md`), registros del sistema, CP-01 a CP-04 y verificación de integridad. Se define primer contacto y se agrega un DECIDIR-VÍCTOR, porque la prueba de concepto guarda la hora de "Tomar".
- Nueva cita verificada: Martínez Mendoza et al. (2023, p. 4836), ficha `mendoza_2024b`, para el riesgo de que la empresa no tenga registros.
- Procedimiento: sale el trabajo de campo con personas; entran el pedido de documentos (desde el 27-nov), la primera y la segunda ronda de la heurística y el cierre del registro.
- Nueva sección "Indicadores de las metas de validación" con las Tablas 2 a 7, una por meta (reemplaza "Variables e indicadores"). M2 y M4 toman como línea base la condición "sin" del caso de prueba; M6 pasa a problemas graves sin corregir (DEC-23). Se cita Hyzy et al. (2022, p. 2), ya usado en el Cap. I, para recordar la meta SUS original.
- Análisis: salen Wilcoxon y McNemar (eran para las mismas personas antes y después); queda Mann-Whitney para M1; para M3, Fisher exacta o chi-cuadrado en lugar de la prueba z. Se agrega la lista de limitaciones del método.
- Ética: sin consentimiento a participantes; se citan, verificados hoy en el facsímil del Registro Oficial, el art. 4 (definición de anonimización, p. 11) y el art. 2, lit. c (la ley no se aplica a datos anonimizados, p. 9). Los arts. 8, 10 y 12 pasan al consentimiento del formulario del sistema, que es operación de Torvesa. DEC-20 sigue abierta.
- Referencias: se agregan Hyzy et al. (2022) y Martínez Mendoza et al. (2023).
- Pendiente de alinear en otros capítulos si la tutora acepta: Cap. I (M2, M4 y M6, alcance poblacional y metodológico, limitaciones b y h), Cap. IV (línea base) y Cap. V (Tabla 18 con CP-04, Tabla 19 con M6).
