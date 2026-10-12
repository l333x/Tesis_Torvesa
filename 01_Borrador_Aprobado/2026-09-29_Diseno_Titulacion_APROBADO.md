---
titulo: Diseño de Trabajo de Titulación — versión aprobada (texto extraído)
fecha: 2026-09-29
tipo: borrador_aprobado
estado: solo_lectura
fuente: "[[2026-09-29_Diseno_Titulacion_APROBADO.pdf]]"
tags: [tesis, torvesa, borrador_aprobado]
---

> [!warning] Solo lectura
> Texto extraído automáticamente (pypdf) del PDF aprobado. Ante cualquier duda manda el PDF. No editar: las versiones nuevas van en `06_Capitulos/`.

 
  
## Carta aval de la tutora

 Quito, 29 de septiembre de 2026 
 
 
Ing. Paola Torres 
Directora de la Carrera de Negocios Digitales 
Universidad Politécnica Salesiana 
 
Presente.- 
 
Yo, Tania Alexandra Chicaiza Villalba, con cédula de ciudadanía No. ____________, en calidad 
de docente tutora, por medio de la presente informo que he revisado el plan de trabajo de 
titulación, con el tema "Diseño de un sistema de automatización para la gestión comercial en la 
Constructora Torvesa", a ser desarrollado por los estudiantes Diego Jhoel Bermeo Torres, 
portador de la cédula de identidad N.º [CÉDULA RESERVADA], y Víctor Alexander Segura Heredia, 
portador de la cédula de identidad N.º [CÉDULA RESERVADA]. El menc ionado plan cumple con los 
parámetros necesarios para ser presentado ante el Consejo de Carrera para que continúe con el 
proceso de titulación. 
Por la atención que se digne dar a la presente, anticipo mis agradecimientos. 
 
Atentamente, 
 
 
 
__________________________ 
Tania Alexandra Chicaiza Villalba 
Docente Tutora 
CI: ____________ 

## CARTA DE AUTORIZACIÓN DE LA EMPRESA

Quito, 29 de septiembre de 2026 
Ingeniera 
Paola Torres 
Directora de la Carrera de Negocios Digitales 
UNIVERSIDAD POLITÉCNICA SALESIANA 
Presente.- 
De mis consideraciones: 
Reciba un cordial y atento saludo de quienes conformamos Torvesa Constructora, empresa del 
sector de la construcción de la ciudad de Quito dedicada al desarrollo y ejecución de proyectos 
de construcción. 
Por medio de la presente informo a usted que los señores Diego Jhoel Bermeo Torres, con C.I. 
No. [CÉDULA RESERVADA], y Víctor Alexander Segura Heredia, con C.I. No. [CÉDULA RESERVADA], estudiantes de 
la Carrera de Negocios Digitales, van a realizar su Proyecto Técnico de titulación en nuestra 
empresa. 
En calidad de Representante Legal de Torvesa Constructora, autorizo el desarrollo del proyecto 
técnico denominado “Diseño de un sistema de automatización para la gestión comercial en la 
Constructora Torvesa”, que comprende: 
•  el levantamiento y análisis de información sobre los procesos comerciales, los flujos de 
trabajo y los mecanismos de comunicación de la empresa; 
•  la aplicación de encuestas, entrevistas y pruebas al personal y a los clientes de la 
empresa; 
•  el diseño del sistema propuesto y su prueba piloto con el equipo comercial. 
Asimismo, autorizo el uso y la divulgación con fines académicos de los datos que se obtengan 
dentro de la empresa, siempre con respeto a la confidencialidad de la información reservada de 
Torvesa Constructora, a la protección de los datos personales de col aboradores y clientes 
conforme a la Ley Orgánica de Protección de Datos Personales, y con el aval oportuno de los 
involucrados. 
Por la atención que se digne dar a la presente, anticipo mis agradecimientos. 
Atentamente, 
______________________________ 
Ing. Mentor Eduardo Torres Cunalata 
Representante Legal 
Torvesa Constructora 
C.I. [CÉDULA RESERVADA] 
  
 
 
 UNIVERSIDAD 
POLITÉCNICA SALESIANA 
CARRERA DE NEGOCIOS DIGITALES - SEDE QUITO 
UNIDAD DE TITULACIÓN / INTEGRACIÓN 
CURRICULAR 
 
DISEÑO DE TRABAJO DE TITULACIÓN 
 

## DATOS INFORMATIVOS

 
TÍTULO: Diseño de un sistema de automatización para la gestión comercial en la 
Constructora Torvesa. 
TIPO DE TRABAJO: Proyecto Técnico 
PERIODO: Período 69 (septiembre 2026 – febrero 2027) 
DOCENTE TUTOR: Tania Alexandra Chicaiza Villalba 
ESTUDIANTES: Diego Jhoel Bermeo Torres; Víctor Alexander Segura Heredia 
LÍNEA(S) DE INVESTIGACIÓN:  
GRUPO DE INVESTIGACIÓN VINCULADO: No aplica 
OBJETIVOS VINCULADOS AL APRENDIZAJE: OV A 4 (indicadores 4.1, 4.2 y 4.3), 
OV A 5 (indicadores 5.1, 5.3 y 5.4) y OV A 6 (indicadores 6.1, 6.2 y 6.3). 
 

## PROBLEMA DE ESTUDIO


### 1. Contexto general

Torvesa Constructora es una sociedad con personería jurídica domiciliada en Quito (Pichincha) 
que inició actividades el 5 de agosto de 2010. Su actividad principal registrada es la 
construcción de carreteras, calles y otras vías para vehículos o peatones, y 
complementariamente ejecuta obras de ingeniería civil en general (Servicio de Rentas Internas 
[SRI], 2026). Cuenta con 30 colaboradores entre personal administrativo, comercial y técnico, 
y atiende principalmente a clientes privados —empresas, inmobiliar ias y promotores de 
proyectos habitacionales, y personas naturales — que solicitan cotizaciones de forma directa; 
según los registros de la empresa, su cartera actual es de 33 clientes. Su oferta se vende por 
proyecto: cada solicitud exige una cotización o proforma a medida, cuyo detalle técnico —
materiales, cantidades, rubros y plazos— hace que su elaboración dependa del conocimiento y 
del tiempo del vendedor que la prepara. 
El sector económico de la construcción es uno de los menos digitalizados de la economía: el 
índice de digitalización industrial del McKinsey Global Institute lo ubica en el penúltimo lugar 
entre los sectores analizados, solo por delante de la agricultura y la caza (Agarwal et al., 2016). 
Su lógica B2B, su estructura fragmentada y su organización por proyectos frenan la adopción 
de tecnologías de gestión (Samuelson y Stehn, 2023; Nyqvist et al., 2024). La Constructora 
Torvesa ilustra esta brecha: atiende a c lientes que esperan respuestas rápidas, pero gestiona la 
relación comercial y la elaboración de cotizaciones con procesos manuales, y su personal 
comercial y técnico divide la jornada entre la oficina y obras con conectividad limitada (Bermeo 
y Segura, 2026). 

### 2. Descripción clara del problema

El problema se expresa en el tiempo de respuesta al cliente. Cada solicitud de cotización obliga 
al vendedor a preparar la respuesta casi desde cero: buscar cotizaciones anteriores, recalcular 
rubros y armar el documento a partir de archivos dispersos y de su propia memoria. Según los 
registros de la empresa, la elaboración de cada cotización toma entre 30 y 44 minutos de trabajo 
del vendedor; como ese mismo vendedor reparte la jornada entre la oficina y la obra, ese tiempo 
solo puede dedicarse al volver a la oficina, y las solicitudes quedan sin atender durante horas o 
días. A la lentitud se suma la falta de un historial: el conocimiento de cada cliente —qué pidió, 
qué se le ofreció, qué está pendiente — vive en el teléfono y en la memoria del vendedor 
asignado, y no existe un repositorio que la empresa conserve si ese vendedor está en obra sin 
señal o deja la organización. El diagnóstico denominó a este fenómeno «amnesia institucional»: 
el cliente debe repetir su historia o, en el peor caso, se va con la competencia. 
Aumentar el personal o reorganizar las cargas de trabajo son decisiones de gestión que 
corresponden a la gerencia y no forman parte de este trabajo. El problema que aborda el 
proyecto es tecnológico: no existe una herramienta que conserve el conocimiento comercial de 
la empresa —historial de clientes, plantillas y cotizaciones anteriores — y que lo ponga a 
disposición del vendedor para responder en menos tiempo. 

### 3. Evidencias y datos

Las empresas que responden a un lead dentro de la primera hora tienen cerca de siete veces más 
probabilidades de calificarlo que las que tardan más, y más de sesenta veces más que las que esperan 24 horas o más (Oldroyd et al., 2011). El diagnóstico previo aplicado a los 30 
colaboradores de Torvesa (Bermeo y Segura, 2026) encontró que: 
•  solo el 13,3 % de los primeros contactos ocurre dentro de 15 minutos, y el 23,3 % de los 
leads espera más de 24 horas; 
•  la etapa modal de pérdida del embudo es previa al primer contacto (30,0 %); 
•  el 50,0 % del equipo no encuentra información completa al buscar el historial de un cliente 
antiguo, y el 43,3 % no confía en poder retomar la cartera de un compañero ausente; 
•  el 36,7 % señala que las confirmaciones desde obra «a veces nunca llegan», y el 56,7 % 
de la comunicación urgente circula por canales no trazables; 
•  el «historial completo y centralizado del cliente» fue la función n.º 1 en el ranking forzado 
de prioridades (53,3 %); 
•  la versión inicial del sistema obtuvo un SUS de 53,83, por debajo del umbral normativo 
de 68 (Sauro, 2011; Lewis, 2018). 

### 4. Delimitación del problema

El estudio se centra en tres procesos del área comercial de la Constructora Torvesa (Quito): la 
recepción de las solicitudes de los prospectos, la elaboración de la respuesta o cotización y la 
conservación del historial de cada cliente. Sobre el ecosistema  TEAMSLASH (landing, API 
propia, PostgreSQL y alertas por Slack) se diseñan tres componentes: (a) una bóveda de 
conocimiento comercial en Obsidian con fichas de clientes, plantillas y cotizaciones anteriores; 
(b) un asistente de inteligencia artificial que  consulta la bóveda y propone al vendedor un 
borrador de respuesta; y (c) un registro verificable de las interacciones. La propuesta se valida 
con cuatro casos de prueba y un piloto de dos semanas de operación experimental. 

### 5. Planteamiento del problema (pregunta central)

¿Cómo debe diseñarse un sistema de automatización que permita a la Constructora Torvesa 
responder a sus prospectos en el menor tiempo posible, dar continuidad a la atención con el 
vendedor titular y conservar un historial verificable de cada cliente? 

## JUSTIFICACIÓN


### 1. Relevancia social o práctica

El estudio responde a la necesidad que el propio equipo priorizó en primer lugar: un historial 
centralizado del cliente. La bóveda convierte el conocimiento que hoy reside en la memoria de cada vendedor en un activo de la empresa: si el vendedor está en obra sin señal, consulta la 
ficha del cliente desde su celular, y si deja la organización, el historial de trabajo con cada 
cliente queda en la empresa. Las plantillas y las cotizaciones ante riores, consultadas por el 
asistente de IA, reducen el tiempo de preparar cada respuesta, y la información acumulada 
permite generar reportes para la gerencia sobre clientes, cotizaciones y tiempos de atención. 
Además, el registro verificable da a la gerencia una prueba de quién atendió a cada cliente, qué 
se le ofreció y cuándo, útil para resolver discrepancias con clientes y para asignar el mérito 
comercial entre vendedores. El registro controlado de los datos contribuye también al 
cumplimiento de la Ley Orgánica de Protección de Datos Personales (LOPDP). 

### 2. Relevancia académica o científica

La evidencia sobre CRM móvil proviene casi siempre de empresas grandes o de ventas internas 
en economías desarrolladas, y se basa en percepciones autorreportadas (Ohiomah et al., 2019; 
Rodriguez y Boyer, 2020; Habel et al., 2025). Este trabajo aporta una m edición basada en 
registros del sistema en una pyme constructora latinoamericana. Además, articula dos campos 
que suelen estudiarse por separado: la gestión de leads y la gestión del conocimiento y la 
memoria organizacional (Nonaka y Takeuchi, 1995; Walsh y Ungson, 1991). 

### 3. Viabilidad del estudio

El estudio es viable porque: (a) la línea base ya fue levantada (N = 30); (b) el MVP está 
desplegado y la bóveda se construye sobre él sin licencias, ya que Obsidian es gratuito para uso 
comercial y la sincronización puede hacerse con Git; (c) se cuenta con la carta de autorización 
de la Constructora Torvesa, que permite usar sus datos, y con el tema aprobado por la carrera; 
(d) el registro verificable usa OpenTimestamps, un servicio gratuito que no requiere 
criptomonedas ni contratos inteligentes; y (e) el  asistente de IA usa un servicio de modelos de 
lenguaje con un costo por consumo acotado durante el piloto. 

### 4. Impacto esperado

Con una correcta implementación por parte de la empresa —que no depende de este trabajo—, 
se proyecta reducir el tiempo de primer contacto por debajo de 15 minutos, acortar la 
elaboración de las cotizaciones mediante plantillas y respuestas asistidas, y lograr que cualquier 
miembro del equipo recupere el historial de un cliente en minutos, aunque el vendedor titular 
cambie. El piloto de dos semanas aportará una primera evidencia de ese efecto; sus resultados sustentarán la decisión de Torvesa sobre la adopción definitiva y la validación de TEAMSLASH 
como emprendimiento SaaS. 

## OBJETIVOS


### Objetivo general

Diseñar un sistema de automatización para la gestión comercial de la Constructora Torvesa, que 
integre el CRM móvil TEAMSLASH con una bóveda de conocimiento comercial en Obsidian, 
un asistente de inteligencia artificial para la elaboración de respuestas y cotizaciones y un 
registro verificable de eventos, y validarlo mediante un piloto de dos semanas que mida su 
efecto sobre el tiempo de respuesta, la continuidad de la atención y la trazabilidad del historial 
de cada cliente. 

### Objetivos específicos

•  Diagnosticar los procesos actuales de captación, cotización y atención de clientes (AS-IS) 
y establecer la línea base de tiempos de respuesta, fuga, capacidad de recuperar 
información y usabilidad, incluida la percepción de los clientes. 
•  Diseñar la arquitectura y los procesos objetivo (TO -BE) del sistema —bóveda de 
conocimiento, asistente de IA con plantillas de cotización y registro verificable —, con 
requisitos funcionales, análisis de viabilidad técnica y económica, y controles confor me 
a la LOPDP. 
•  Desarrollar los componentes del sistema mediante sprints incrementales sobre la 
infraestructura existente de TEAMSLASH. 
•  Validar el sistema mediante cuatro casos de prueba y un piloto de dos semanas de 
operación experimental, midiendo los indicadores definidos frente a la línea base. 
•  Documentar el manual de operación, los lineamientos de gobierno de la información y la 
transferencia al equipo de Torvesa. 

### Relación con los Objetivos Vinculados al Aprendizaje (OV A)

•  OE1 (diagnóstico): OV A 4.1, identificar y analizar problemas complejos; OV A 5.1, analizar 
datos de desempeño organizacional. 
•  OE2 (diseño): OV A 4.2, formular alternativas de solución fundamentadas; OV A 6.2, evaluar 
la viabilidad técnica y económica; OV A 6.3, aplicar principios de seguridad y normativa digital. 
•  OE3 (desarrollo): OV A 4.3, aplicar métodos y herramientas de la profesión; OV A 6.1, 
desarrollar soluciones digitales innovadoras. 
•  OE4 (validación): OV A 5.4, evaluar el impacto de la gestión digital mediante indicadores 
clave de desempeño. 
•  OE5 (documentación y transferencia): OV A 5.3, proponer planes de implementación 
considerando recursos, cronograma y gestión de riesgos. MARCO HIPOTÉTICO O PREGUNTAS DE INVESTIGACIÓN (Aplica para opción 
de artículo académico) 
En un Proyecto Técnico no se formula un marco hipotético. En su lugar se plantean preguntas 
orientadoras y metas de validación que guían el desarrollo y la evaluación del sistema. 

### Preguntas orientadoras

•  PO1. ¿Qué pasos del proceso actual provocan demoras y pérdida de información entre la 
oficina y la obra? 
•  PO2. ¿Qué información mínima deben contener la ficha del cliente y las plantillas de 
cotización para que el vendedor —o quien lo reemplace si deja la empresa — responda 
sin reconstruir la historia del cliente? 
•  PO3. ¿Qué reglas de asignación, alerta y seguimiento garantizan que ninguna solicitud 
quede sin respuesta? 
•  PO4. ¿Cómo garantizar que el historial comercial no pueda alterarse sin que se note, sin 
exponer datos personales? 

### Metas de validación

•  M1. Mediana del speed -to-lead menor a 15 minutos (línea base: 13,3 % de contactos 
dentro de 15 minutos; 23,3 % después de 24 horas). 
•  M2. Reducción del tiempo de elaboración de una cotización con el asistente de IA frente 
a la línea base (entre 30 y 44 minutos por cotización), medida en los casos de prueba. 
•  M3. Fuga previa al primer contacto menor que el 30,0 % de la línea base. 
•  M4. En la prueba de recuperación, menor tiempo y más aciertos que en la línea base; 
disminución del 50,0 % que no encuentra información completa y del 43,3 % que no 
confía en retomar una cartera ajena. 
•  M5. El 100 % de las alteraciones simuladas del registro detectadas por la verificación de 
integridad. 
•  M6. Puntaje SUS igual o superior a 68 (línea base: 53,83). 

## MARCO TEÓRICO REFERENCIAL


### 1. Antecedentes del tema

Gestión de leads y CRM móvil.  Oldroyd et al. (2011) documentaron la «corta vida» de los 
leads en línea: la probabilidad de calificarlos cae con cada hora de demora. Ohiomah et al. (2019), con 108 profesionales de ventas y PLS-SEM, demostraron que los sistemas de gestión 
de leads mejoran el desempeño a través de una mayor intensidad de seguimiento, variable que 
junto con otras explica el 55 % de la varianza. Rodriguez y Boyer (2020) hallaron que el CRM 
móvil eleva el desempeño solo cuando está respaldado por un proceso definido y por 
colaboración entre vendedores, lo que respalda acompañar la herramienta con un proceso de 
atención estandarizado. Habel et al. (2025) mostraron que la au tomatización del seguimiento 
aumenta la conversión entre 0 y 23 puntos porcentuales según el contexto. 
Pymes y construcción.  Alqershi et al. (2020), en 284 pymes, encontraron que solo algunas 
dimensiones del CRM —la tecnológica y la organizativa— afectan el desempeño. Gil-Gómez 
et al. (2020) vincularon el CRM con la innovación del modelo de negocio. Samuelson y Stehn 
(2023) y N yqvist et al. (2024) identifican la fragmentación y la organización por proyectos 
como barreras de la transformación digital en construcción, y la estandarización de procesos 
como impulsor. 
Antecedente local. El diagnóstico de Bermeo y Segura (2026), aplicado a los 30 colaboradores 
de Torvesa, es el antecedente directo de este proyecto: documentó la dependencia de canales 
informales, el bajo cumplimiento del estándar de 15 minutos y la pérdida de historial cuando el 
vendedor asignado no está disponible. 

### 2. Bases teóricas

•  CRM y CRM móvil:  estrategia apoyada en tecnología para registrar, dar seguimiento y 
convertir prospectos; su versión móvil lleva estas funciones al campo (Rodriguez y Boyer, 
2020). 
•  Speed-to-lead: el tiempo entre el ingreso del prospecto y el primer contacto determina su 
calificación; la ventana de referencia es de 5 a 15 minutos (Oldroyd et al., 2011). 
•  Gestión del conocimiento y modelo SECI:  el conocimiento tácito del vendedor (lo que 
«sabe» del cliente) debe externalizarse en conocimiento explícito y compartido para que 
la organización no dependa de una sola persona (Nonaka y Takeuchi, 1995). Los sistemas 
de gestión del conocimiento son la i nfraestructura que soporta ese proceso (Alavi y 
Leidner, 2001). 
•  Memoria organizacional: la información sobre decisiones y relaciones pasadas se retiene 
en «depósitos» que la organización puede recuperar (Walsh y Ungson, 1991); la bóveda 
es un depósito explícito de la memoria comercial. •  Software local-first: las aplicaciones que guardan los datos primero en el dispositivo y 
sincronizan después permiten trabajar sin conexión y evitan la dependencia del proveedor 
(Kleppmann et al., 2019); este principio justifica el uso de Obsidian en obras sin señal. 
•  Inteligencia artificial generativa con recuperación de información (RAG): los modelos de 
lenguaje pueden generar respuestas apoyadas en documentos propios de la organización, 
recuperados en el momento de la consulta, lo que mantiene la respuesta anclada  al 
historial de la empresa y reduce errores (Lewis et al., 2020); este principio sustenta el 
asistente que redacta borradores de cotización a partir de la bóveda. 
•  Aceptación tecnológica y usabilidad: la facilidad de uso percibida determina la adopción 
(Davis, 1989); la usabilidad se mide con la SUS, cuya referencia normativa es 68 (Brooke, 
1996; Bangor et al., 2008; Lewis, 2018). 
•  Gestión de procesos de negocio (BPM):  modelado AS -IS/TO-BE en BPMN y 
automatización del flujo de captación, asignación, alerta, escalamiento y traspaso (Dumas 
et al., 2018). 
•  Sellado de tiempo y registros encadenados (blockchain ligero):  encadenar cada 
documento con el hash del anterior hace evidente cualquier alteración posterior (Haber y 
Stornetta, 1991). Bitcoin generalizó este principio en una cadena de bloques pública 
(Nakamoto, 2008), y OpenTimestamps permite anclar en ella el hash de un registro sin 
costo ni datos personales (Todd, 2016). 

### 3. Bases legales y normativas

•  Ley Orgánica de Protección de Datos Personales (2021) y su Reglamento General (2023): 
regulan el consentimiento en el formulario de captación, la minimización de datos en la 
bóveda, el control de acceso y la anonimización de los datos del estudio. 
•  Ley de Comercio Electrónico, Firmas Electrónicas y Mensajes de Datos (2002): da validez 
jurídica a los mensajes de datos usados en la captación y el seguimiento. 

### 4. Discusión crítica

La literatura coincide en que el CRM mejora el desempeño comercial, pero condiciona el efecto 
al proceso, a la colaboración y a la aceptación del usuario (Rodriguez y Boyer, 2020; Habel et 
al., 2025). Por su parte, la gestión del conocimiento subraya que l a tecnología solo captura 
conocimiento si existe una práctica que obligue a externalizarlo (Alavi y Leidner, 2001). Se identifican tres vacíos: (a) casi no se miden tiempos reales registrados por el sistema; (b) no hay 
evidencia en pymes constructoras latinoamericanas con trabajo de campo sin conectividad; y 
(c) casi no se ha estudiado el uso de repositorios de conocimient o consultados con IA para 
acelerar la elaboración de cotizaciones en pymes. Respecto de blockchain, la literatura aplicada 
advierte que muchas implementaciones empresariales no la necesitan. Por eso este proyecto 
adopta solo su propiedad útil —la evidencia de integridad y de fecha — sin tokens, contratos 
inteligentes ni datos personales en la cadena, lo que también evita el conflicto con el derecho 
de supresión de la LOPDP. Este trabajo se ubica en esa intersección. 

## ALCANCE

•  Temático: diseño y validación del sistema: captación, primer contacto, elaboración 
asistida de respuestas y cotizaciones, continuidad de la atención con el vendedor titular, 
bóveda de conocimiento, registro verificable y usabilidad, aplicados a los clientes 
privados de la empresa. No se abordan la negociación, la facturación, la ejecución de obra 
ni las decisiones de gestión del personal (dotación y asignación de cargas), que 
corresponden a la gerencia; tampoco los procesos de contratación pública, que se rigen 
por los plazos y formatos del Sistema Nacional de Contratación Pública. 
•  Geográfico: Constructora Torvesa, Quito, Ecuador. 
•  Temporal: ocho semanas, del 5 de octubre al 29 de noviembre de 2026, con un piloto de 
dos semanas de operación experimental; la presentación está prevista para diciembre de 
2026, dentro del Período 69. 
•  Poblacional: los 30 colaboradores de Torvesa, sus 33 clientes y la totalidad de las 
solicitudes que ingresen durante el piloto. 
•  Metodológico: enfoque cuantitativo y diseño experimental (cuasi -experimental pre-post 
de un solo grupo) aplicado a un piloto. 
•  Limitaciones: (a) caso único sin grupo de control, sin generalización ni causalidad 
estricta; (b) la línea base es parcialmente autorreportada; (c) población pequeña, por lo 
que se usan pruebas no paramétricas; (d) posible efecto Hawthorne; (e) Obsidian no 
ofrece permisos por usuario dentro de una bóveda, lo que se mitiga con minimización de 
datos y control de dispositivos (Anexo A); (f) el registro verificable prueba que un evento 
no fue alterado desde su fecha, pero no que su contenido haya sido verdadero al registrarse; (g) la evaluación financiera del modelo SaaS es contexto y no objeto del 
proyecto. 

## METODOLOGÍA


### 1. Enfoque de la investigación

Cuantitativo: se miden tiempos de respuesta y de elaboración de cotizaciones, proporciones, 
puntajes y resultados de pruebas antes y después del piloto. Las entrevistas de cierre se usan 
solo como apoyo para interpretar los resultados. 

### 2. Tipo de investigación

Experimental y tecnológica: produce un artefacto —el sistema— y lo somete a prueba mediante 
cuatro casos de prueba y un piloto en la organización. 

### 3. Método o diseño de investigación

Se adopta la Investigación en Ciencia del Diseño (Design Science Research, DSR), propia de 
los proyectos que construyen y evalúan artefactos de sistemas de información (Hevner et al., 
2004), en las seis actividades de Peffers et al. (2007): 
•  Identificación del problema:  diagnóstico existente (N = 30) y nuevo levantamiento de 
procesos AS-IS. 
•  Objetivos de la solución: requisitos y metas de validación M1–M6. 
•  Diseño y desarrollo: sprints con Scrum y tablero Kanban (Sprints A–D). 
•  Demostración: ejecución de los cuatro casos de prueba del Anexo A.9. 
•  Evaluación: piloto de dos semanas de operación experimental con comparación pre -post 
de un solo grupo. 
•  Comunicación: informe técnico, manual y defensa. 
Las variables de evaluación son la velocidad (speed -to-lead, % dentro de 15 min y tiempo de 
elaboración de la cotización), la fuga previa al primer contacto, la continuidad (capacidad de 
retomar el historial de un cliente), la trazabilidad (completitud de la ficha, prueba de 
recuperación e integridad del registro) y la usabilidad (SUS). 

### 4. Población y muestra

La población tiene dos grupos. El primero son los 30 colaboradores de Torvesa, con quienes se 
trabaja por censo, por lo que no se calcula muestra; los indicadores de atención se analizan con el personal que atiende clientes. El segundo son los clientes: la empresa cuenta con una cartera 
de 33 clientes y, dado su tamaño, también se trabaja por censo, encuestando a la totalidad, por 
ser quienes mejor conocen los tiempos de respuesta y las fallas  de la atención. La unidad de 
análisis operativa son todas las solicitudes y cotizaciones registradas durante el piloto. La línea 
base de tiempos se reconstruirá con una muestra documental de conversaciones y cotizaciones 
comerciales anonimizada y autorizada por la gerencia. 
 

### 5. Técnicas e instrumentos de recolección de datos

Estudios nuevos (no incluidos en el diagnóstico anterior): 
•  Levantamiento de procesos AS-IS/TO-BE en BPMN mediante entrevistas y observación 
de una jornada comercial. 
•  Encuesta estructurada a clientes, con enfoque de empatía con el usuario (design thinking): 
tiempo de respuesta percibido, calidad de la cotización y aspectos de la atención que no 
les han satisfecho. 
•  Prueba de recuperación de información: cada vendedor localiza cinco datos del historial 
de un cliente de otro compañero; se registran el tiempo y los aciertos antes y después. 
•  Cuatro casos de prueba funcionales con criterios de aceptación (Anexo A.9). 
•  Prueba de integridad: alteraciones simuladas del registro para comprobar su detección. 
•  Registro de eventos del sistema (lead_events), historial de versiones de la bóveda (Git) y 
anclajes de OpenTimestamps. 
Instrumentos existentes que se reaplican: 
•  Cuatro cuestionarios del diagnóstico, incluidos la SUS y los ítems de historial y retoma de 
cartera, con confiabilidad por alfa de Cronbach. 
•  Entrevista semiestructurada de cierre a gerencia y coordinadores (3 a 5 personas). 

### 6. Procedimiento

•  Revisión bibliográfica, levantamiento AS-IS y prueba de recuperación inicial. 
•  Definición de requisitos, diseño TO-BE y evaluación de protección de datos. 
•  Sprint A: modelo de datos y registro de eventos. •  Sprint B: bóveda en Obsidian, generador de fichas y plantillas de cotización. 
•  Sprint C: asistente de IA para respuestas y cotizaciones (consulta a la bóveda). 
•  Sprint D: registro verificable y anclaje en blockchain. 
•  Ejecución de los cuatro casos de prueba y capacitación del equipo. 
•  Piloto: operación experimental y medición durante dos semanas. 
•  Reaplicación de instrumentos, análisis y elaboración del informe, del manual y de la 
defensa. 

### 7. Técnicas de análisis de datos

Los datos se procesarán en Python (pandas, SciPy) y Jamovi. Se usará estadística descriptiva 
(medianas, rangos intercuartílicos y proporciones) y se aplicarán las siguientes pruebas, con α 
= 0,05 y reporte del tamaño del efecto: 
•  Wilcoxon para mediciones pareadas (SUS y prueba de recuperación). 
•  McNemar para ítems dicotómicos pareados (historial completo y confianza en retomar 
cartera). 
•  U de Mann-Whitney para los tiempos de primer contacto. 
•  Prueba z de proporciones o chi-cuadrado para la fuga y el cumplimiento de los 15 minutos. 
Los casos de prueba se evaluarán por tasa de aprobación frente a sus criterios de aceptación, y 
las entrevistas mediante análisis temático. 

## RESULTADOS ESPERADOS

•  Prácticos: un sistema diseñado y probado en un piloto en Torvesa que integra el CRM 
móvil, la bóveda de conocimiento comercial, el asistente de IA y el registro verificable, 
con cumplimiento de las metas M1 a M6 (OE3 y OE4). 
•  Metodológicos: los procesos AS -IS/TO-BE en BPMN, cuatro casos de prueba 
reutilizables, la prueba de recuperación de información y un protocolo de medición del 
embudo y de los tiempos de cotización, replicables en otras pymes (OE1, OE2 y OE4). 
•  Documentales y de transferencia:  manual de operación de la bóveda, lineamientos de 
gobierno de la información conforme a la LOPDP y capacitación del equipo comercial 
(OE5). •  Académicos: evidencia, basada en registros verificables, sobre el efecto de un CRM móvil 
con bóveda de conocimiento en una pyme constructora, publicable como artículo 
derivado del proyecto (OE4). 
CRONOGRAMA 
 

## CRONOGRAMA DE ACTIVIDADES

\# ACTIVIDAD DURACIÓN OBSERV ACIONES
1 
Revisión bibliográfica, 
levantamiento AS-IS (BPMN), 
encuesta a clientes y prueba de 
recuperación inicial 
Semana 1 (5–11 
oct) DSR: identificación del problema; línea base 
2 
Requisitos, diseño TO-BE y 
evaluación de protección de datos 
Semana 2 (12–
18 oct) DSR: objetivos de la solución 
3 
Sprints A y B: modelo de datos, 
registro de eventos, bóveda en 
Obsidian, fichas y plantillas de 
cotización 
Semana 3 (19–
25 oct) Repositorio Git privado 
4 
Sprints C y D: asistente de IA 
para cotizaciones y registro 
verificable con OpenTimestamps 
Semana 4 (26 
oct–1 nov) Consulta a la bóveda; sin datos personales en la cadena 
5 
Ejecución de los cuatro casos de 
prueba y capacitación del equipo 
Semana 5 (2–8 
nov) DSR: demostración 
6 
Piloto: operación experimental y 
medición 
Semanas 6–7 (9–
22 nov) DSR: evaluación; dos semanas 
7 
Reaplicación de instrumentos, 
análisis de resultados, informe 
técnico y manual 
Semana 8 (23–
29 nov) DSR: comunicación 
8 
Revisión con la tutora, 
correcciones y presentación Diciembre 2026 Entrega a la carrera 
 
 
 
 
 

## REFERENCIAS

Agarwal, R., Chandrasekaran, S., & Sridhar, M. (2016). Imagining construction's digital 
future. McKinsey & Company. 
https://www.mckinsey.com/~/media/mckinsey/business%20functions/operations/our%20insig
hts/imagining%20constructions%20digital%20future/imagining-constructions-digital-
future.pdf 
Alavi, M., & Leidner, D. E. (2001). Review: Knowledge management and knowledge 
management systems: Conceptual foundations and research issues. MIS Quarterly, 
25(1), 107–136. https://doi.org/10.2307/3250961 
Alqershi, N., Mokhtar, S. S. M., & Abas, Z. B. (2020). Innovative CRM and performance of 
SMEs: The moderating role of relational capital. Journal of Open Innovation: Technology, Market, and Complexity, 6(4), 155. 
https://doi.org/10.3390/joitmc6040155 
Asamblea Nacional del Ecuador. (2002). Ley de Comercio Electrónico, Firmas Electrónicas y 
Mensajes de Datos. Registro Oficial Suplemento 557. 
Asamblea Nacional del Ecuador. (2021). Ley Orgánica de Protección de Datos Personales. 
Registro Oficial Quinto Suplemento 459, 26 de mayo de 2021. 
Bangor, A., Kortum, P. T., & Miller, J. T. (2008). An empirical evaluation of the System 
Usability Scale. International Journal of Human-Computer Interaction, 24(6), 574–
594. https://doi.org/10.1080/10447310802205776 
Bermeo, D., & Segura, V . (2026). TEAMSLASH: Ecosistema digital de gestión de clientes 
para la Constructora Torvesa [Informe final de proyecto integrador]. Universidad 
Politécnica Salesiana. 
Brooke, J. (1996). SUS: A "quick and dirty" usability scale. En P. W. Jordan, B. Thomas, B. A. 
Weerdmeester, & I. L. McClelland (Eds.), Usability evaluation in industry (pp. 189–
194). Taylor & Francis. 
Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of 
information technology. MIS Quarterly, 13(3), 319–340. 
https://doi.org/10.2307/249008 
Dumas, M., La Rosa, M., Mendling, J., & Reijers, H. A. (2018). Fundamentals of business 
process management (2.ª ed.). Springer. 
Gil-Gómez, H., Guerola-Navarro, V ., Oltra-Badenes, R., & Lozano-Quilis, J. A. (2020). 
Customer relationship management: Digital transformation and sustainable business 
model innovation. Economic Research-Ekonomska Istraživanja, 33(1), 2733–2750. 
https://doi.org/10.1080/1331677X.2019.1676283 
Haber, S., & Stornetta, W. S. (1991). How to time-stamp a digital document. Journal of 
Cryptology, 3(2), 99–111. https://doi.org/10.1007/BF00196791 
Habel, J., Hartmann, N. N., Wiseman, P., Ahearne, M. J., & Vaid, S. (2025). Sales pipeline 
technology: Automated lead nurturing. Journal of Marketing. 
https://doi.org/10.1177/00222429251321417 Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information 
systems research. MIS Quarterly, 28(1), 75–105. https://doi.org/10.2307/25148625 
Kleppmann, M., Wiggins, A., van Hardenberg, P., & McGranaghan, M. (2019). Local-first 
software: You own your data, in spite of the cloud. En Proceedings of the 2019 ACM 
SIGPLAN International Symposium on New Ideas, New Paradigms, and Reflections 
on Programming and Software (pp. 154–178). ACM. 
https://doi.org/10.1145/3359591.3359737 
Lewis, J. R. (2018). The System Usability Scale: Past, present, and future. International 
Journal of Human-Computer Interaction, 34(7), 577–590. 
https://doi.org/10.1080/10447318.2018.1455307 
Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V ., Goyal, N., Küttler, H., Lewis, M., 
Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). Retrieval-augmented 
generation for knowledge-intensive NLP tasks. Advances in Neural Information 
Processing Systems, 33, 9459–9474. 
Nakamoto, S. (2008). Bitcoin: A peer-to-peer electronic cash system. 
https://bitcoin.org/bitcoin.pdf 
Nonaka, I., & Takeuchi, H. (1995). The knowledge-creating company: How Japanese 
companies create the dynamics of innovation. Oxford University Press. 
Nyqvist, R., Peltokorpi, A., Lavikka, R., & Ainamo, A. (2024). Building the digital age: 
Management of digital transformation in the construction industry. Construction 
Management and Economics. https://doi.org/10.1080/01446193.2024.2416033 
Ohiomah, A., Andreev, P., Benyoucef, M., & Hood, D. (2019). The role of lead management 
systems in inside sales performance. Journal of Business Research, 102, 163–177. 
https://doi.org/10.1016/j.jbusres.2019.05.018 
Oldroyd, J. B., McElheran, K., & Elkington, D. (2011). The short life of online sales leads. 
Harvard Business Review, 89(3), 28. 
Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science 
research methodology for information systems research. Journal of Management 
Information Systems, 24(3), 45–77. https://doi.org/10.2753/MIS0742-1222240302 Rodriguez, M., & Boyer, S. (2020). The impact of mobile customer relationship management 
(mCRM) on sales collaboration and sales performance. Journal of Marketing 
Analytics, 8(3), 137–148. https://doi.org/10.1057/s41270-020-00087-8 
Samuelson, O., & Stehn, L. (2023). Digital transformation in construction – a review. Journal 
of Information Technology in Construction, 28, 385–404. 
https://doi.org/10.36680/j.itcon.2023.020 
Sauro, J. (2011). A practical guide to the System Usability Scale: Background, benchmarks & 
best practices. Measuring Usability LLC. 
Servicio de Rentas Internas. (2026). Consulta de RUC: Torvesa Constructora (RUC 
1792266424001) [Base de datos]. Recuperado el 28 de septiembre de 2026, de 
https://srienlinea.sri.gob.ec 
Todd, P. (2016). OpenTimestamps: Scalable, trust-minimized, distributed timestamping with 
Bitcoin. https://petertodd.org/2016/opentimestamps-announcement 
Walsh, J. P., & Ungson, G. R. (1991). Organizational memory. Academy of Management 
Review, 16(1), 57–91. https://doi.org/10.5465/amr.1991.4278992 
 
 
 
AUTOR 1: Diego Jhoel Bermeo Torres AUTOR 2: Víctor Alexander Segura 
Heredia 
FIRMA: FIRMA: 
TUTOR: Tania Alexandra Chicaiza Villalba 
FIRMA: 
FECHA DE ENTREGA: 15 de diciembre de 2026 
 
 
 

## ANEXO A. DISEÑO FUNCIONAL DE LA BÓVEDA COMERCIAL Y DEL

PROTOCOLO DE CONTINUIDAD 

### A.1 Alineación entre el diagnóstico y las funciones propuestas

Cada función del sistema responde a un hallazgo medido del diagnóstico (N = 30): 
Hallazgo del diagnóstico Dato Función que lo resuelve Indicador de éxito 
Historial centralizado: 
prioridad n.º 1 del ranking 
forzado 
53,3 % Ficha única por cliente y proyecto en 
la bóveda, generada automáticamente 
Índice de completitud de la 
ficha 
No encuentra información 
completa del historial de un 
cliente antiguo 
50,0 % Bitácora cronológica automática y 
notas de campo enlazadas 
Ítem reaplicado 
(McNemar); aciertos en la 
prueba de recuperación 
No confía en retomar la 
cartera de un compañero 
ausente 
43,3 % Ficha e historial en la bóveda; 
reasignación de cartera sin pérdida de 
historial 
Ítem reaplicado; prueba de 
recuperación 
Al iniciar el día no sabe a qué 
clientes priorizar 
43,3 % Tableros de pendientes por vendedor 
(Dataview) 
Pendientes vencidos por 
semana 
Confirmaciones desde obra 
que «nunca llegan» 
36,7 % Registro de interacciones desde el 
celular y consulta sin conexión 
Interacciones registradas 
por lead 
Primeros contactos dentro de 
15 minutos 
13,3 % Alerta al titular y borrador de 
respuesta generado por el asistente de 
IA 
Speed-to-lead; % dentro de 
15 min 
Demanda modal: que la 
información «llegue sola» 
10 
menciones 
La API escribe la bóveda; el 
vendedor no transcribe nada 
SUS; análisis temático 
 

### A.2 Principio de arquitectura

La bóveda no reemplaza a la base de datos; la complementa. Se separan dos capas: 
•  PostgreSQL es la fuente de verdad transaccional:  quién, qué y cuándo. Guarda leads, 
asignaciones, estados y eventos, con marcas de tiempo que no pueden alterarse desde la 
bóveda. 
•  La bóveda en Obsidian es la capa de conocimiento:  el porqué y el contexto. Son notas 
en Markdown legibles, enlazadas entre sí, disponibles sin conexión en el celular y 
portables: si TEAMSLASH dejara de existir, Torvesa conserva su memoria comercial en 
archivos abiertos. 
Flujo de información: 
•  Formulario (Vercel) → API Node.js (Railway) → PostgreSQL: registro del lead y evento 
«ingreso». 
•  La API asigna el vendedor titular según su especialidad y zona → evento «asignado». 
•  El generador de notas escribe o actualiza la ficha Markdown y la confirma en el repositorio 
Git privado de la bóveda. •  Slack envía la tarjeta al titular con los botones «Contactado», «En proceso», «No 
disponible» y el enlace a la ficha. 
•  El asistente de IA consulta la bóveda (ficha del cliente, plantillas y cotizaciones similares) 
y entrega al titular un borrador de respuesta que él revisa y ajusta antes de enviarlo. 
•  Obsidian (escritorio y celular) sincroniza la bóveda; la ficha se consulta aunque no haya 
señal. 
•  Las notas de campo que el vendedor escribe en Obsidian se sincronizan al volver la señal; 
un proceso de ingesta las registra en PostgreSQL como evento «nota» con autor y hora. 

### A.3 Estructura de la bóveda

Bóveda-Torvesa/ 
├── 00 Tableros/     Pendientes · Sin contacto >15 min · Traspasos 
├── 10 Clientes/     CLI-0001 Inmobiliaria Andes.md 
├── 20 Proyectos/    PRY-0001 Edificio Cumbayá.md  (API) 
│                    PRY-0001 … – notas.md  (vendedores) 
├── 30 Vendedores/   Vendedor A.md (cartera, disponibilidad) 
├── 40 Bitácora/     2026-10-05.md (eventos del día) 
├── 50 Cotizaciones/  COT-0001 Adoquinado de vía.md (enviadas y plantillas) 
└── 90 Plantillas/   proyecto · nota-de-campo · cotización 
 
La ficha generada y las notas humanas se guardan en archivos separados; la ficha incrusta las 
notas con ![[…]]. Así la API y los vendedores nunca editan el mismo archivo, lo que evita 
conflictos de sincronización. 

### A.4 Plantilla de la ficha de proyecto

--- 
id: PRY-0001 
cliente: "[[CLI-0001 Inmobiliaria Andes]]" 
titular: "[[Vendedor A]]" 
estado: en_proceso        # nuevo | en_proceso | cotizado | cerrado | perdido 
ingreso: 2026-10-05T09:12 
primer_contacto: 2026-10-05T09:19 
proxima_accion: Enviar cotización de acabados 
vence: 2026-10-07 
monto_estimado: 85000 
consentimiento_lopdp: true 
--- 
\## Necesidad del cliente
\## Pendientes
- [ ] Enviar cotización de acabados              2026-10-07 
\## Bitácora (automática; no editar)
- 09:12 Ingreso por formulario web 
- 09:12 Asignado a Vendedor A 
- 09:19 Contactado por Vendedor A 
\## Notas de campo
![[PRY-0001 Edificio Cumbayá – notas]] 

### A.5 Flujo de atención con el vendedor titular («Proceso 1»)

Paso Disparador Acción del sistema Evento registrado 
1. Ingreso Nuevo lead desde el
formulario 
Crea la ficha, asigna el titular por 
especialidad y zona, y lo alerta en Slack 
ingreso, asignado 
2. Primer contacto El titular pulsa
«Contactado» 
Actualiza el estado y la bitácora contactado 
3. Preparación de
la respuesta 
El titular pide un borrador 
al asistente 
Consulta cotizaciones similares, plantillas e 
historial, y propone la proforma 
borrador_generado 
4. Envío de la
cotización 
El titular revisa, ajusta y 
envía 
Guarda en la ficha la versión enviada cotizado 
5. Recordatorio Sin acción del titular en 15
min 
Recuerda al titular la solicitud pendiente; 
avisa a gerencia a los 30 min 
recordatorio 
6. Reasignación
formal 
Decisión de gerencia 
(salida o rotación) 
Cambia el titular conservando todo el 
historial 
reasignado 
 

### A.6 Matriz de trazabilidad

Pregunta de trazabilidad Dónde se responde Indicador del estudio 
¿Cuándo llegó el lead y cuándo se le 
contactó? 
lead_events (ingreso, contactado) Speed-to-lead; % dentro de 15 min 
¿Quién lo atendió y qué se le cotizó? lead_events.actor; versiones de la 
cotización en la ficha 
Tiempo de elaboración de la 
cotización 
¿Qué pidió el cliente y qué está 
pendiente? 
Ficha: necesidad y pendientes Índice de completitud 
¿Quién cambió qué en la ficha y 
cuándo? 
Historial de versiones Git Auditoría de cambios 
¿Qué leads se perdieron sin contacto? Estado «perdido» sin evento 
«contactado» 
Fuga previa al primer contacto 
 

### A.7 Controles de protección de datos (LOPDP)

•  Minimización: la bóveda no guarda cédulas, datos bancarios ni documentos; el teléfono 
y el correo del cliente quedan solo en PostgreSQL, y la ficha muestra el código del cliente 
y el contacto comercial. 
•  Acceso: solo el equipo comercial recibe la bóveda, en dispositivos con bloqueo y cifrado; 
el acceso se revoca retirando la credencial del repositorio o del espacio compartido. 
•  Consentimiento: casilla obligatoria en el formulario de captación; el campo 
consentimiento_lopdp queda registrado en la ficha. 
•  Conservación: las fichas de leads perdidos se archivan a los 12 meses. 
•  Datos del estudio: se analizan anonimizados, con códigos en lugar de nombres. 

### A.8 Sincronización: opciones

Criterio A. Git + complemento Obsidian Git 
(recomendada para el MVP) 
B. Obsidian Sync + nodo puente 
Costo Gratuito USD 4–5 por usuario al mes Escritura desde la 
API 
Directa (commit al repositorio) Requiere un equipo de oficina encendido que 
escriba en la carpeta 
Trazabilidad Historial Git completo: autor, fecha y 
diferencia 
Historial de versiones por archivo 
Estabilidad en celular Aceptable; puede ser lenta en Android o iOS Alta, con cifrado de extremo a extremo 
Decisión Se adopta en el piloto Contingencia si el piloto falla en campo 
 

### A.9 Casos de prueba del sistema

Caso Escenario Resultado esperado (criterio de aceptación) 
CP1 Llega un lead y el titular está disponible Ficha creada y alerta al titular en menos de 1 minuto; contacto 
registrado con hora 
CP2 El titular prepara una cotización con el 
asistente de IA 
Borrador generado a partir de cotizaciones similares y 
plantillas; tiempo de elaboración menor que la línea base 
CP3 Un vendedor deja la empresa Reasignación de su cartera sin pérdida de historial; el nuevo 
titular recupera los datos del cliente 
CP4 Alguien altera un registro pasado en la base 
de datos 
La verificación de integridad identifica el evento alterado; el 
anclaje del día no coincide 
 

### A.10 Registro verificable («blockchain ligero»)

Cómo funciona.  Cada evento de la tabla lead_events guarda el hash SHA -256 del evento 
anterior, formando una cadena: modificar o borrar cualquier registro rompe todos los enlaces 
siguientes. Una vez al día, el hash del último evento —que resume todo el historial previo— se 
sella en la blockchain de Bitcoin mediante OpenTimestamps. 
Qué prueba. Que el historial comercial existía en esa forma exacta en esa fecha y que no fue 
modificado después, ni siquiera por un administrador de la base de datos. Sirve para demostrar 
quién atendió a un cliente y cuándo, para resolver discrepancias con clientes o entre vendedores 
y para que el tribunal pueda auditar los datos del propio proyecto. 
Qué no hace. No guarda datos de clientes en la cadena (solo un hash de 64 caracteres), no usa 
criptomonedas ni contratos inteligentes y no tiene costo por transacción. Tampoco garantiza 
que lo registrado sea verdadero: solo que no fue alterado. 
Relación con la LOPDP.  Como en la cadena solo queda un hash sin datos personales, el 
derecho de supresión puede ejercerse en PostgreSQL y en la bóveda sin tocar la blockchain. 