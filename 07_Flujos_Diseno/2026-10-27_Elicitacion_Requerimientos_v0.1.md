---
titulo: Proceso de elicitación y análisis de requerimientos — Sistema de automatización comercial Torvesa
version: v0.1
fecha: 2026-10-27
autor_borrador: "Claude Opus 5.5 (Víctor y Diego revisan)"
asignatura: Ingeniería de Requerimientos, Usabilidad y UX
plantilla: "Plantilla del proceso de elicitación y análisis de requerimientos (ISO/IEC/IEEE 29148:2018 + SWEBOK V4.0a)"
estado: borrador para revisión; no es línea base
word: 2026-10-27_Elicitacion_Requerimientos_v0.1.docx
tags: [requerimientos, elicitacion, iso29148, swebok, teamslash, diego, victor]
---

# Proceso de elicitación y análisis de requerimientos

> [!warning] Versión 0.1 — borrador para revisión
> Las sesiones de la iteración 1 (proyecto integrador TEAMSLASH, mayo–julio de 2026) y la revisión documental de octubre ya se realizaron. Las sesiones en la Constructora Torvesa de la iteración 2 (entrevistas, encuestas, observación y taller de validación) están **planificadas** y se realizan cuando la empresa autorice el trabajo de campo. Ningún dato de este documento proviene del diagnóstico simulado (N = 30), que no se usa.

## 0. Datos generales del proyecto

| Campo | Contenido |
|---|---|
| Título del proyecto de titulación | Diseño de un sistema de automatización para la gestión comercial en la Constructora Torvesa |
| Carrera | Negocios Digitales — Universidad Politécnica Salesiana, sede Quito |
| Estudiantes responsables | Víctor Segura Heredia · Diego Bermeo Torres |
| Tutora | Ing. Tania Chicaiza |
| Organización beneficiaria | Torvesa Constructora (Quito, Pichincha) |
| Fecha de inicio del proceso | Mayo de 2026 (iteración 1, proyecto integrador TEAMSLASH); 11 de octubre de 2026 (iteración 2, trabajo de titulación) |
| Versión del documento | 0.1 |

**Control de versiones**

| Versión | Fecha | Autor | Descripción del cambio |
|---|---|---|---|
| 0.1 | 27-oct-2026 | Equipo de titulación (borrador con apoyo de IA) | Primera versión: integra la iteración 1 (TEAMSLASH) y la planificación de la iteración 2 en Torvesa |
| 1.0 | Prevista tras la validación con Torvesa | Equipo de titulación | Línea base de requerimientos (sección 15) |

## 1. Introducción

### 1.1 Propósito del documento

El presente documento registra el proceso de elicitación y análisis de requerimientos del proyecto de titulación «Diseño de un sistema de automatización para la gestión comercial en la Constructora Torvesa», con el fin de obtener un conjunto de requerimientos de interesados bien formulados, priorizados, validados y trazables, que sirva como base para el diseño del sistema (objetivo específico OE2) y para el prototipo funcional (OE3).

### 1.2 Alcance del documento

El documento cubre la elicitación y el análisis de requerimientos de los cuatro componentes del sistema: (a) el CRM móvil TEAMSLASH, ya desplegado como producto mínimo viable; (b) la bóveda de conocimiento comercial; (c) el asistente de inteligencia artificial que propone borradores de respuesta y de cotización; y (d) el registro verificable de eventos. No cubre la especificación formal completa (SRS), la arquitectura detallada ni la construcción, que corresponden a los sprints de diseño (2 a 8 de noviembre de 2026) y de prueba de concepto.

### 1.3 Definiciones, acrónimos y abreviaturas

| Término | Definición |
|---|---|
| Solicitud (lead o prospecto) | Pedido de información o de cotización que un cliente potencial hace a Torvesa por cualquier canal |
| Primer contacto | Primera respuesta de una persona de Torvesa al cliente después de recibir su solicitud |
| Tiempo de primer contacto | Minutos entre el ingreso de la solicitud y el primer contacto (meta M1) |
| Fuga | Solicitud que se pierde antes del primer contacto (meta M3) |
| Cotización o proforma | Documento con rubros, cantidades, precios y plazos que Torvesa envía al cliente |
| Bóveda de conocimiento | Conjunto de notas en Obsidian (formato Markdown) con fichas de clientes, plantillas y cotizaciones anteriores |
| Ficha de cliente | Nota de la bóveda identificada con un código (por ejemplo, CLI-0001) que reúne el historial de un cliente |
| RAG | Generación aumentada por recuperación: el modelo de lenguaje responde a partir de documentos propios que recupera de la bóveda |
| LLM | Modelo de lenguaje de gran tamaño, servicio externo que usa el asistente |
| Huella SHA-256 | Resumen criptográfico de 256 bits que cambia si el documento cambia (norma FIPS 180-4 del NIST) |
| Registro de solo agregar | Registro en el que solo se pueden añadir entradas, no modificarlas ni borrarlas |
| SUS | System Usability Scale, escala de usabilidad de 10 ítems; se usa la versión validada en español |
| Validación del diseño en operación experimental controlada | Uso del sistema durante dos semanas con solicitudes reales para medir las metas M1–M6. No es una implementación |
| LOPDP | Ley Orgánica de Protección de Datos Personales del Ecuador (2021) |
| M1–M6 | Metas de validación definidas en el capítulo I de la tesis |

### 1.4 Referencias del proyecto

| Referencia | Fecha o versión |
|---|---|
| Diseño del trabajo de titulación aprobado por la carrera | 29-sep-2026 |
| Informe Final del proyecto integrador «TEAMSLASH: ecosistema digital de gestión de clientes para la Constructora Torvesa» | 22-jul-2026 (vigente) |
| Pitch deck de TEAMSLASH, versiones b y c | 22-jul-2026 |
| Manual de usuario de TEAMSLASH | 10-jul-2026 |
| Capítulos I, II y III de la tesis | v0.2, 20-oct-2026 |
| Proceso actual de atención a un cliente (AS-IS), BPMN 2.0 | v0.1, 25-oct-2026 (borrador sin validar en campo) |
| Inventario de herramientas candidatas | v0.2, 25-oct-2026 |
| Instrumentos de campo: C1 (consentimiento), I1 (encuesta a colaboradores), I2 (encuesta a clientes), I3 (guía de entrevista), P1 y P2 (protocolos) | C1 e I1 v0.2 (18-oct-2026); I2, I3, P1 y P2 v0.1 (11-oct-2026) |
| Ley Orgánica de Protección de Datos Personales | Registro Oficial 5.º Suplemento n.º 459, 26-may-2021 |
| Reglamento General a la LOPDP | Decreto Ejecutivo 904, 2023 |
| Ley de Comercio Electrónico, Firmas y Mensajes de Datos | 2002 |
| FIPS 180-4, Secure Hash Standard (NIST) | Agosto de 2015 |
| ISO/IEC/IEEE 29148:2018 y SWEBOK V4.0a | Marco de esta plantilla |
| ISO/IEC 25010:2023 | Modelo de calidad de producto |

## 2. Análisis del problema u oportunidad

### 2.1 Descripción del problema u oportunidad

Las solicitudes de cotización llegan a Torvesa de manera informal, sobre todo al WhatsApp personal de socios e ingenieros, que pasan buena parte de la jornada en obra. Nadie se entera a tiempo de cada solicitud, no hay un responsable claro y cada cotización se prepara casi desde cero, buscando cotizaciones anteriores en celulares, chats y cuadernos. El conocimiento de cada cliente vive en la memoria y en el teléfono del vendedor que lo atendió: si ese vendedor está en obra sin señal o deja la empresa, el historial se pierde («amnesia institucional»). Las consecuencias son clientes que esperan horas o días, clientes que se van con la competencia sin que quede registrado el motivo y una gerencia que no sabe cuántas cotizaciones están en curso. El documento complementario «Planteamiento del problema» (Anexo H) desarrolla el problema con la estructura de *problem statement*.

### 2.2 Contexto organizacional o del dominio

Torvesa Constructora es una sociedad de Quito, activa desde 2010, cuya actividad registrada es la construcción de vías y obras de ingeniería civil. Tiene 30 colaboradores y una cartera de 33 clientes, datos pendientes de la nota de respaldo de la gerencia. Vende por proyecto: cada solicitud exige una cotización a medida. Su estructura es esbelta: el personal comercial y técnico reparte la jornada entre la oficina y las obras. No existe un sistema comercial: los canales son WhatsApp personal, redes sociales, teléfono y correo. Como antecedente, el equipo de titulación desarrolló en el proyecto integrador el MVP TEAMSLASH, compuesto por:
- una página de captación con formulario en Vercel;
- una API propia en Node.js sobre Railway, que recibe el formulario por *webhook*;
- un registro de solicitudes con semáforo de estados;
- alertas en Slack con un botón «Ver ficha».

Las reglas de negocio actuales no están escritas. Se reconstruyen en el AS-IS v0.1 y se confirman en campo.

### 2.3 Objetivos del negocio o de la misión

| ID | Objetivo | Criterio de éxito |
|---|---|---|
| OBJ-01 | Responder rápido a cada solicitud nueva | Mediana del tiempo de primer contacto menor a 15 minutos durante la validación (M1). Es una meta de diseño, no un estándar probado |
| OBJ-02 | Preparar cotizaciones en menos tiempo | Tiempo de elaboración con el asistente menor que el de la línea base en los casos de prueba (M2) |
| OBJ-03 | No perder clientes antes del primer contacto | Fuga previa al primer contacto menor que la de la línea base (M3) |
| OBJ-04 | Que el historial comercial sea de la empresa y no de cada vendedor | En la prueba de recuperación, menos tiempo y más aciertos que en la línea base (M4) |
| OBJ-05 | Tener un historial que no pueda alterarse sin que se note | 100 % de las alteraciones simuladas detectadas (M5) |
| OBJ-06 | Que la herramienta se pueda usar en obra, desde el celular | Puntaje SUS igual o mayor a 68 (M6) |
| OBJ-07 | Tratar los datos de los clientes conforme a la LOPDP | Lista de verificación LOPDP sin hallazgos abiertos antes de la validación |

### 2.4 Caracterización del espacio de solución

| Alternativa | Ventajas | Desventajas | Viabilidad (técnica, económica, temporal) |
|---|---|---|---|
| A. CRM comercial (HubSpot, Zoho CRM, Pipedrive, Kommo) | Producto maduro, app móvil y soporte; HubSpot y Zoho tienen planes gratuitos para 2 y 3 usuarios | No incluye la bóveda ni el registro verificable; datos en la nube del proveedor; Kommo es el único con WhatsApp oficial, pero exige un plazo mínimo de 6 meses; costo por usuario | Técnica alta; económica media; temporal alta. No cumple el objetivo general aprobado |
| B. Extender TEAMSLASH con bóveda en Obsidian, asistente de IA con RAG y registro SHA-256 | Es el diseño aprobado; se aprovecha el MVP ya desplegado; Obsidian es gratuito para uso comercial; datos locales (*local-first*); activo propio del equipo | Más integración propia; Obsidian no tiene permisos por usuario dentro de una bóveda; depende de servicios de terceros (Slack, LLM) | Técnica media; económica alta (costo por consumo de la IA, acotado); temporal media (dos sprints de diseño y prototipo) |
| C. Aplicación móvil nativa a medida | Control total y experiencia a medida | Alto costo y meses de desarrollo; riesgo de no adopción; fuera del plazo del período 69 | Técnica media; económica baja; temporal baja |
| D. Solución sin software nuevo (WhatsApp Business con un número de la empresa, turnos y una hoja compartida) | Costo casi nulo; usa lo que el personal ya conoce | No conserva el historial de forma estructurada; no mide tiempos; depende de la disciplina manual | Técnica alta; económica alta; no resuelve OBJ-02, OBJ-04 ni OBJ-05 |

Fuente de precios y condiciones: inventario de herramientas v0.2 (páginas oficiales consultadas el 21 y el 25 de octubre de 2026).

### 2.5 Alternativa seleccionada y justificación

Se selecciona la alternativa B, porque es la única que cubre los siete objetivos del negocio. Además, corresponde al diseño aprobado por la carrera y reutiliza el MVP TEAMSLASH, lo que reduce el riesgo temporal. De la alternativa D se toma una idea: dar a los clientes que escriben por WhatsApp un enlace al formulario y permitir el registro manual rápido de esas solicitudes (RQ-03). Así, el canal que hoy usan los clientes no queda fuera del sistema.

### 2.6 Alcance preliminar de la solución

| Dentro del alcance | Fuera del alcance |
|---|---|
| Captación de solicitudes (formulario y registro manual de las que llegan por WhatsApp o teléfono) | Negociación, facturación y cobranza |
| Alerta inmediata, asignación de responsable y estados de la solicitud | Ejecución y avance de obra (incluido el módulo de avance con fotos que pidió la gerencia en el censo) |
| Bóveda con fichas de clientes, plantillas y cotizaciones anteriores | Contratación pública (Sistema Nacional de Contratación Pública) |
| Asistente de IA que propone borradores revisados por el vendedor | Envío automático de cotizaciones sin revisión humana |
| Registro verificable de eventos con huellas SHA-256 | Decisiones de dotación y cargas de trabajo del personal |
| Reporte semanal para la gerencia | Integración oficial con la API de WhatsApp Business |
| Controles de protección de datos (LOPDP) | Aplicación móvil nativa |

### 2.7 Restricciones del proyecto

- **Plazo:** período académico 69. La validación del diseño en operación experimental controlada va del 23-nov al 5-dic-2026 y el documento final se entrega el 4-ene-2027.
- **Personas:** un equipo de dos estudiantes. Víctor se encarga del negocio, la metodología y las fuentes; Diego, de lo técnico.
- **Recursos:** presupuesto propio y limitado. Se prefieren planes gratuitos o de costo por consumo.
- **Tecnologías impuestas por el diseño aprobado:** TEAMSLASH, Obsidian, un LLM con RAG y huellas SHA-256 sin cadena de bloques.
- **Normativa:** LOPDP y su reglamento; reglamento de titulación de la UPS (instructivo vigente por confirmar con la tutora).
- **Disponibilidad de los interesados:** el trabajo de campo depende de la autorización de la gerencia de Torvesa, todavía pendiente.

## 3. Planificación de la elicitación

### 3.1 Estrategia de elicitación

La elicitación se organiza en dos iteraciones, conforme a la naturaleza iterativa del proceso (ISO/IEC/IEEE 29148, 2018, cl. 5.3; Washizaki, 2025, sec. 7.1).

- **Iteración 1 (mayo–julio de 2026, proyecto integrador TEAMSLASH).**
  - Se aplicó una entrevista estructurada en modalidad de censo a cinco personas de la gerencia y de la operación.
  - Se construyó un MVP y se probó con el equipo comercial.
  - Sus resultados son la base de los requerimientos de captación, alerta y estados (RQ-01 a RQ-08).
- **Iteración 2 (octubre–noviembre de 2026, trabajo de titulación).**
  - Primero, con técnicas que no dependen de la empresa: análisis de documentos, análisis de herramientas competidoras y modelado del proceso actual.
  - Después, en Torvesa: entrevistas semiestructuradas, encuestas censales a colaboradores y clientes, observación con cronometraje, revisión de una muestra documental y un taller de validación y priorización.
  - Se agregan los requerimientos de la bóveda, el asistente de IA, el registro verificable y la protección de datos (RQ-09 a RQ-22).

Para las necesidades opuestas se parte de las áreas de consenso: hoy todos los interesados coinciden en la necesidad de enterarse a tiempo y de no perder el historial. Desde ahí se construye. Los conflictos se registran en la sección 11.7 y se resuelven en el taller con la gerencia, nunca de forma unilateral.

### 3.2 Cronograma de elicitación

| Actividad | Técnica | Interesados | Fecha prevista | Responsable |
|---|---|---|---|---|
| Censo de validación del problema (realizado) | Entrevista estructurada en censo | INT-01, INT-02, INT-03 | Mayo de 2026 | Víctor y Diego |
| Prueba del MVP con el equipo comercial (realizada) | Prototipo funcional y retroalimentación | INT-02 | Sprint 3 del proyecto integrador (julio de 2026) | Diego |
| Revisión documental y de literatura (realizada) | Análisis de documentos | — | 11 al 25-oct-2026 | Víctor |
| Análisis de herramientas candidatas (realizado) | Análisis de mercado y de sistemas competidores | — | 19 al 25-oct-2026 | Diego |
| Modelado del proceso actual (realizado, sin validar) | Modelado BPMN a partir de documentos | — | 25-oct-2026 | Diego |
| Revisión de alcance con la tutora | Revisión del documento | INT-07 | 28-oct-2026 | Víctor y Diego |
| Entrevistas a gerencia y a quienes cotizan | Entrevista semiestructurada (I3) | INT-01, INT-02, INT-03 | Semana siguiente a la autorización de Torvesa | Víctor |
| Observación y cronometraje de cotizaciones | Observación pasiva (P2-A) | INT-03 | Semana siguiente a la autorización | Diego |
| Muestra de solicitudes de los últimos 3 meses | Análisis de documentos (P2-B), solo fechas y horas | — | Semana siguiente a la autorización | Diego |
| Encuesta a colaboradores | Cuestionario censal (I1) | INT-02, INT-03, INT-04 | Semana siguiente a la autorización | Víctor |
| Encuesta a clientes | Cuestionario censal (I2) | INT-05 | Semana siguiente a la autorización | Víctor |
| Taller de validación y priorización | Taller facilitado con prototipo de baja fidelidad y recorrido de escenarios | INT-01, INT-02, INT-03 | Al cerrar las entrevistas (antes del 8-nov si el campo se autoriza a tiempo) | Víctor y Diego |

### 3.3 Recursos y herramientas de apoyo

- **Instrumentos:** guía de entrevista, cuestionarios en papel o en formulario, hoja de cronometraje y consentimiento informado (C1).
- **Modelado:** BPMN 2.0 (bpmn.io o Camunda Modeler) para los procesos AS-IS y TO-BE; diagramas de casos de uso.
- **Prototipado:** pantallas de baja fidelidad de la ficha del cliente, de la alerta y del borrador del asistente.
- **Repositorio de requerimientos:** la bóveda del proyecto con control de versiones en Git; este documento y su matriz de trazabilidad.
- **Organización del trabajo:** cronograma del proyecto en Excel, que es la fuente de verdad.
- **Acceso necesario:**
  - autorización de la gerencia para entrevistar, observar y revisar una muestra anonimizada de solicitudes;
  - acceso al MVP TEAMSLASH desplegado.

### 3.4 Consideraciones éticas

- **Consentimiento:** cada participante firma un consentimiento informado (C1 v0.2) antes de responder. El consentimiento es libre, específico, informado e inequívoco, y se puede revocar en cualquier momento (LOPDP, 2021, art. 8).
- **Grabaciones:** solo se graba con autorización expresa.
- **Anonimización:** las respuestas se identifican con códigos.
- **Datos personales:** los que identifican a una persona se guardan aparte, en una carpeta local que no se comparte ni se sube a la nube.
- **Resultados para la empresa:** la empresa recibe solo resultados agregados.
- **Muestra documental:** se anotan solo fechas y horas, sin nombres ni datos de clientes.
- **Pendiente con la tutora:** quién figura como responsable del tratamiento de los datos (los estudiantes o la UPS) y si hace falta la aprobación de un comité de ética (PEN-05).

## 4. Identificación y análisis de interesados

### 4.1 Criterio de identificación

Se consideró interesado a toda persona, grupo u organización que participa en el proyecto, que se ve afectada por su resultado o que puede influir en él (Washizaki, 2025, sec. 2.1). Se recorrieron las etapas de desarrollo, operación, soporte y retiro del sistema. Así se incluyeron, además de los usuarios y el adquirente, el equipo que desarrolla y mantiene, los proveedores de plataformas y la autoridad regulatoria (ISO/IEC/IEEE 29148, 2018, cl. 5.2.2).

### 4.2 Clases de interesados

| Clase | Descripción | Representante(s) | Influencia (A/M/B) | Interés (A/M/B) |
|---|---|---|---|---|
| Adquirente | Gerencia que autoriza, financia y decide la adopción | INT-01 | A | A |
| Usuarios principales | Quienes reciben solicitudes y hacen el primer contacto, a menudo desde la obra | INT-02 | M | A |
| Usuarios de cotización | Quienes preparan cotizaciones y presupuestos | INT-03 | M | A |
| Usuarios secundarios | Resto de colaboradores que consultan el historial | INT-04 | B | M |
| Clientes y prospectos | Titulares de los datos; afectados por la rapidez y la calidad de la respuesta | INT-05 | M | M |
| Desarrolladores y mantenimiento | Equipo de titulación | INT-06 | A | A |
| Autoridad académica | Tutora del trabajo de titulación | INT-07 | A | M |
| Ente regulador | Superintendencia de Protección de Datos Personales | INT-08 | A | B |
| Proveedores de sistemas externos | Obsidian, Slack, proveedor del LLM, Railway, Vercel, Google | INT-09 | M | B |

### 4.3 Fichas de interesados

| Campo | INT-01 | INT-02 | INT-03 |
|---|---|---|---|
| Nombre o rol | Gerencia y representante legal | Coordinadores comerciales, socios e ingenieros que reciben solicitudes | Personal que prepara cotizaciones |
| Clase | Adquirente | Usuario principal | Usuario de cotización |
| Relación con el sistema | Autoriza, financia y recibe los reportes | Recibe alertas, contacta al cliente, actualiza estados | Usa plantillas y el asistente de IA |
| Responsabilidades | Decidir la adopción; aprobar cotizaciones (por confirmar en I3) | Primer contacto y seguimiento | Calcular rubros, cantidades y plazos |
| Expectativas y preocupaciones | Control del embudo; motivos de pérdida al cierre de cada semana (60 % en el censo); costo bajo | Enterarse a tiempo sin dejar la obra; no saturarse de mensajes; interfaz simple | No empezar de cero; que la IA no invente precios |
| Conocimiento del dominio y de la tecnología | Dominio alto; tecnología media (por confirmar) | Dominio alto; usa el celular la mayor parte del tiempo | Dominio técnico alto; usa hojas de cálculo (por confirmar) |
| Disponibilidad | Baja; reuniones cortas | Baja en horario de obra | Media, en oficina |
| Técnicas adecuadas | Entrevista, taller de validación | Entrevista, encuesta, observación, prototipo | Observación con cronometraje, entrevista, prototipo |

| Campo | INT-04 | INT-05 | INT-06 |
|---|---|---|---|
| Nombre o rol | Colaboradores (de los 30 en total) | Clientes en cartera (33) y prospectos | Víctor Segura (negocio) y Diego Bermeo (técnico) |
| Clase | Usuario secundario | Cliente y titular de datos | Desarrollador y mantenimiento |
| Relación con el sistema | Consultan fichas cuando el titular no está | Envían solicitudes; sus datos se guardan | Diseñan, construyen el prototipo y lo validan |
| Responsabilidades | Retomar la atención de un cliente ajeno | — | Requerimientos, diseño, prototipo y medición |
| Expectativas y preocupaciones | Encontrar la información completa y confiar en ella | Respuesta rápida; cotización clara; privacidad | Cumplir las metas M1–M6 dentro del plazo |
| Conocimiento | Variable | Variable | Alto en negocio digital y en tecnología |
| Disponibilidad | Media | Baja; encuesta telefónica de 6 minutos | Alta |
| Técnicas adecuadas | Encuesta I1 | Encuesta I2 | Lluvia de ideas, revisión de documentos |

| Campo | INT-07 | INT-08 | INT-09 |
|---|---|---|---|
| Nombre o rol | Ing. Tania Chicaiza, tutora | Superintendencia de Protección de Datos Personales | Proveedores de plataformas |
| Clase | Autoridad académica | Ente regulador | Sistemas externos |
| Relación con el sistema | Aprueba el alcance y el método | Fija las obligaciones de la LOPDP | Imponen condiciones de uso, precios y tratamiento de datos |
| Expectativas | Rigor, trazabilidad y cumplimiento del reglamento de titulación | Cumplimiento de la ley | — |
| Técnica adecuada | Revisión del documento | Análisis de la normativa | Análisis de la documentación oficial |

### 4.4 Matriz de poder e interés

| Cuadrante | Interesados | Estrategia de participación |
|---|---|---|
| Gestionar de cerca (poder alto, interés alto) | INT-01, INT-06 | Entrevista y taller de validación; aprobación de la línea base |
| Mantener satisfecho (poder alto, interés medio o bajo) | INT-07, INT-08 | Revisiones con la tutora (28-oct y Revisión 2); cumplimiento verificable de la LOPDP |
| Mantener informado (poder medio o bajo, interés alto) | INT-02, INT-03 | Entrevista, observación, prototipo y encuesta; resumen de resultados |
| Monitorear | INT-04, INT-05, INT-09 | Encuestas; seguimiento de las condiciones de los proveedores |

**Sesgo detectado.** La información de la iteración 1 proviene de un solo nivel jerárquico: cinco personas de la gerencia y de la operación. Ningún cliente ni colaborador de base fue consultado. La norma advierte que eso sesga la visión del problema. La iteración 2 lo corrige con las dos encuestas censales: I1 a los colaboradores e I2 a los 33 clientes.

## 5. Fuentes de requerimientos no humanas

| ID | Fuente | Tipo | Información que aporta | Fecha o versión |
|---|---|---|---|---|
| FNT-01 | Diseño del trabajo de titulación aprobado | Documento institucional | Objetivos, componentes, metas y alcance | 29-sep-2026 |
| FNT-02 | Informe Final de TEAMSLASH | Documentación de la versión previa | Censo n = 5, perfil de usuario, backlog HU-01 a HU-07, arquitectura, resultados de la prueba del MVP | 22-jul-2026 |
| FNT-03 | Pitch deck de TEAMSLASH (b y c) | Documentación de la versión previa | Propuesta de valor y planes; difiere del informe en el almacenamiento (CON-04) | 22-jul-2026 |
| FNT-04 | MVP TEAMSLASH desplegado (formulario, API, registro, alertas en Slack) | Sistema existente | Interfaces y datos reales del sistema sobre el que se construye | En operación (por confirmar) |
| FNT-05 | Manual de usuario de TEAMSLASH | Documentación de la versión previa | Pasos de uso actuales | 10-jul-2026 |
| FNT-06 | Proceso actual (AS-IS) en BPMN | Modelo de proceso | Pasos, actores y cinco puntos de pérdida de tiempo o de información | v0.1, 25-oct-2026 |
| FNT-07 | Registro Único de Contribuyentes de Torvesa (SRI) | Registro público | Actividad económica y fecha de inicio | Consultado el 28-sep-2026 |
| FNT-08 | LOPDP y su Reglamento General | Normativa | Consentimiento, minimización, conservación, derechos del titular | 2021 y 2023 |
| FNT-09 | Ley de Comercio Electrónico, Firmas y Mensajes de Datos | Normativa | Valor de los mensajes de datos | 2002 |
| FNT-10 | FIPS 180-4 (NIST) | Norma técnica | Algoritmo SHA-256 del registro verificable | 2015 |
| FNT-11 | ISO/IEC 25010:2023 | Norma técnica | Características de calidad del producto | 2023 |
| FNT-12 | Literatura verificada (matriz de afirmaciones) | Literatura | Tiempo de respuesta, CRM móvil, gestión del conocimiento, RAG, *local-first* | Matriz v0.4, 21-oct-2026 |
| FNT-13 | Inventario de herramientas candidatas | Sistemas competidores (*benchmarking*) | Precios, app móvil, WhatsApp, tratamiento de datos y madurez | v0.2, 25-oct-2026 |
| FNT-14 | Escala SUS validada en español (Sevilla-Gonzalez et al., 2020) | Instrumento validado | Medición de la usabilidad (M6) | 2020 |

## 6. Selección de técnicas de elicitación

### 6.1 Técnicas seleccionadas

| Técnica | Objetivo | Interesados | Justificación | Instrumento |
|---|---|---|---|---|
| Entrevista estructurada en censo (iteración 1) | Validar la existencia del problema | INT-01, INT-02, INT-03 | Grupo pequeño y clave; permite cuantificar (n = 5) | Cuestionario P1–P8 del Informe Final (Anexo C) |
| Prototipo funcional (MVP) | Descubrir requerimientos ocultos de uso | INT-02 | Los usuarios «ven» el producto; reveló la fricción de salir de Slack para buscar al cliente | MVP TEAMSLASH (Anexo D) |
| Análisis de documentos | Comprender el dominio, la normativa y los requerimientos no funcionales | — | No depende de la agenda de la empresa; el SWEBOK lo considera clave para los requerimientos no funcionales | Matriz de afirmaciones; fichas de fuentes |
| Análisis de mercado y de sistemas competidores | Comparar soluciones y precios | INT-09 | Sustenta el espacio de solución (sección 2.4) | Inventario de herramientas v0.2 |
| Modelado de procesos (BPMN) | Hacer visible el proceso actual y sus puntos de pérdida | — | Base común para hablar con la gerencia | AS-IS v0.1 (Anexo E) |
| Entrevista semiestructurada | Explicar las causas de las demoras y validar el AS-IS | INT-01, INT-02, INT-03 | Profundidad y aclaración en el momento | Guía I3 (Anexo A) |
| Encuesta censal | Cuantificar la percepción de colaboradores y clientes | INT-02 a INT-05 | Muchos interesados, poco tiempo; corrige el sesgo de nivel jerárquico | I1 v0.2 e I2 v0.1 (Anexo B) |
| Observación con cronometraje | Ver lo que se hace, no solo lo que se dice; medir M2 | INT-03 | Revela tareas implícitas y atajos | Protocolo P2-A |
| Taller de validación y priorización con prototipo de baja fidelidad | Validar requerimientos, resolver conflictos y priorizar | INT-01, INT-02, INT-03 | Reúne perfiles distintos y hace visibles los conflictos (CON-01 a CON-06) | Guion del taller y pantallas (por elaborar) |

### 6.2 Dificultades previstas y medidas de mitigación

| Dificultad | Medida de mitigación |
|---|---|
| La empresa aún no autoriza el trabajo de campo | Avanzar con técnicas que no dependen de ella (documentos, mercado, modelado); escalar con una llamada a la gerencia o una carta de respaldo de la tutora |
| Personal en obra con poca disponibilidad | Entrevistas cortas (30–40 min) y encuesta de 15 min; visitas en la oficina al inicio o al final de la jornada |
| Requerimientos tácitos («siempre se ha hecho así») | Observación directa y recorrido del AS-IS paso a paso |
| Interesados que piden soluciones en vez de problemas (por ejemplo, «queremos un módulo de avance de obra») | Técnica de los 5 porqués (sección 11.4) |
| Cifras del antecedente sin respaldo (USD 15.000 por cliente perdido; más de 24 horas de respuesta) | Se usan como hipótesis y se reemplazan por la línea base medida |
| Sesgo de confirmación del equipo, que ya diseñó TEAMSLASH | Preguntas abiertas antes de mostrar el prototipo; la validación la hacen los interesados |

## 7. Registro de sesiones de elicitación

| Campo | SES-01 | SES-02 |
|---|---|---|
| Fecha y duración | Mayo de 2026 (fecha exacta por confirmar con el registro del proyecto integrador) | Sprint 3 del proyecto integrador (julio de 2026) |
| Técnica | Entrevista estructurada en modalidad de censo | Prototipo funcional (MVP) con prueba de latencia y retroalimentación |
| Lugar o modalidad | Torvesa, Quito | Torvesa; red móvil 4G de obra |
| Facilitadores | Víctor Segura y Diego Bermeo | Diego Bermeo y Víctor Segura |
| Participantes | INT-01, INT-02, INT-03 (5 personas de la gerencia y la operación) | INT-02 (equipo comercial) |
| Objetivo | Validar el problema y las prioridades | Comprobar la latencia de la alerta y la usabilidad del flujo |
| Desarrollo resumido | Se aplicaron 8 preguntas (P1–P8) a los cinco miembros clave de la operación y la gerencia | Se simularon 10 envíos de solicitudes desde el formulario y se cronometró el tiempo hasta la alerta en el celular |
| Hallazgos principales | Más del 50 % de la jornada en obra; el 40 % revisa mensajes cada 3 o 4 horas y el 20 % solo al llegar a casa; 4 de 5 reciben clientes en su WhatsApp personal; 4 de 5 fijan en menos de 15 minutos el plazo antes de que el cliente «se enfríe»; 3 de 5 quieren auditar los motivos de pérdida cada semana; las limitaciones en campo se reparten entre falta de computadoras, mala conectividad e interfaces complejas (40 % cada una); 4 de 5 piden a futuro un módulo de avance de obra | Latencia media de 3,2 s; primer contacto de 4 a 11 minutos en los simulacros; 100 % de los envíos registrados. El equipo indicó que salir de Slack y buscar al cliente en la hoja hacía perder tiempo, y se agregó el botón «Ver ficha» |
| Necesidades identificadas | NEC-01, NEC-02, NEC-06, NEC-07, NEC-08, NEC-13 | NEC-08, NEC-07 |
| Requerimientos implícitos | La alerta debe funcionar con poca señal; la interfaz debe leerse de un vistazo | Acceso de un solo toque a la ficha |
| Dudas o temas pendientes | Muestra pequeña y de un solo nivel jerárquico | Simulacros, no solicitudes reales; se mide de nuevo en la validación |
| Evidencia | Informe Final, pp. 9–10, Tabla 1 (Anexo C) | Informe Final, pp. 23–24, Tabla 3 |

| Campo | SES-03 | SES-04 | SES-05 |
|---|---|---|---|
| Fecha y duración | 11 al 25-oct-2026 | 19 al 25-oct-2026 | 25-oct-2026 |
| Técnica | Análisis de documentos y de literatura | Análisis de mercado y de sistemas competidores | Modelado del proceso actual (BPMN) |
| Modalidad | Trabajo de escritorio | Trabajo de escritorio | Trabajo de escritorio |
| Facilitador | Víctor Segura | Diego Bermeo | Diego Bermeo |
| Participantes | — | — | — |
| Objetivo | Fundamentar el problema y las restricciones normativas y de calidad | Caracterizar el espacio de solución | Representar el proceso actual y sus puntos de pérdida |
| Hallazgos principales | 93 fuentes verificadas en la base del proyecto; la LOPDP exige consentimiento, minimización y plazos de conservación; ningún plazo exacto de respuesta (como 5–15 min) está respaldado por la literatura, así que la meta de 15 min es de diseño; la IA con recuperación de documentos sigue en etapa de prototipo en la industria | Solo Kommo integra WhatsApp oficial, pero exige un plazo mínimo de 6 meses; HubSpot y Zoho tienen planes gratuitos para 2–3 usuarios; Obsidian es gratuito para uso comercial; el LLM preseleccionado no entrena con los datos enviados por la API | Cinco puntos críticos: espera, asignación informal, cotización desde cero, seguimiento de memoria e historial en celulares |
| Necesidades | NEC-09, NEC-10, NEC-14 | NEC-14, NEC-02 | NEC-03, NEC-04, NEC-05, NEC-11 |
| Dudas | Contradicción del borrador con la evidencia en A23 (CRM en pymes) | Visto bueno del LLM elegido (PEN-06) | Validación en campo pendiente (siete preguntas para I3) |
| Evidencia | Matriz de afirmaciones v0.4 | Inventario de herramientas v0.2 | AS-IS v0.1 (Anexo E) |

**Sesiones planificadas (iteración 2):** SES-06, entrevistas I3; SES-07, observación y cronometraje; SES-08, muestra documental; SES-09, encuesta I1; SES-10, encuesta I2; SES-11, taller de validación y priorización. Sus fichas se completan al realizarlas.

## 8. Contexto de uso y concepto operacional

### 8.1 Contexto de uso

- **Lugares:** la oficina de Torvesa en Quito y los frentes de obra, donde la conectividad móvil es variable y a veces nula.
- **Dispositivos:** celulares personales del equipo comercial; computadoras solo en la oficina.
- **Horarios:**
  - las solicitudes pueden llegar a cualquier hora;
  - la atención se da en horario laboral, y en obra el celular se revisa de forma intermitente.
- **Carga de trabajo:**
  - volumen semanal de solicitudes bajo, pero de alto valor unitario, según el antecedente; el volumen real es un dato pendiente (PEN-03);
  - el coordinador maneja a la vez entre 3 y 5 proyectos.
- **Sistemas con los que interopera:**
  - formulario en Vercel;
  - API en Railway;
  - registro de solicitudes (Google Sheets o PostgreSQL, por confirmar);
  - Slack;
  - Obsidian con sincronización por Git;
  - API del LLM.
- **Amenazas del entorno:**
  - pérdida o robo del celular;
  - caídas de servicios de terceros;
  - fuga de datos por canales personales.

### 8.2 Características de los usuarios y operadores

- **Coordinadores comerciales (INT-02):**
  - expertos en el dominio y usuarios intensivos de WhatsApp;
  - poco tiempo y atención dividida;
  - necesitan pantallas que se lean de un vistazo y acciones de un solo toque.
- **Quienes cotizan (INT-03):**
  - trabajan en la oficina, con hojas de cálculo;
  - necesitan plantillas y referencias confiables.
- **Gerencia (INT-01):**
  - uso ocasional;
  - lee reportes semanales.
- **Accesibilidad:**
  - texto legible al sol en obra (contraste alto);
  - uso con una mano;
  - mensajes cortos.

### 8.3 Entorno organizacional

Torvesa tiene una estructura esbelta, sin procesos comerciales escritos y con una cultura de comunicación oral y por WhatsApp. El sistema no debe imponer cambios no planificados (ISO/IEC/IEEE 29148, 2018, cl. 6.3.3.4): se conserva el WhatsApp como canal de los clientes (RQ-03) y se usan herramientas que el personal ya conoce, como el chat y la hoja de cálculo. El único cambio de proceso nuevo es registrar el estado de cada solicitud, que se valida con la gerencia en el taller.

### 8.4 Escenarios operacionales

| ID | Escenario | Actores | Situación inicial | Secuencia de acciones | Resultado esperado | Variantes o excepciones |
|---|---|---|---|---|---|---|
| ESC-01 | Solicitud por formulario con el coordinador en obra | Prospecto, coordinador | El coordinador supervisa una obra | El prospecto envía el formulario → el sistema registra la solicitud y la asigna → llega la alerta al celular → el coordinador toca «Ver ficha» y llama | Primer contacto en menos de 15 min, con hora registrada | Sin señal: la alerta llega al recuperar la conexión; a los 15 min sin contacto, recordatorio y aviso a la gerencia (ESC-07) |
| ESC-02 | Solicitud por WhatsApp personal | Prospecto, coordinador | El cliente escribe al WhatsApp de un ingeniero | El ingeniero registra la solicitud desde el celular con los campos mínimos o responde con el enlace al formulario | La solicitud entra al mismo flujo que ESC-01 | El ingeniero olvida registrarla: no se mide (riesgo RIE-03) |
| ESC-03 | Cotización con el asistente | Quien cotiza, asistente de IA | Hay una solicitud asignada con datos de la obra | Se abre la ficha → se pide un borrador → el asistente lo arma con plantillas y cotizaciones anteriores, citando cuáles usó → la persona revisa y corrige → se envía | Cotización enviada en menos tiempo que en la línea base (M2) | El asistente no encuentra antecedentes: lo dice y propone solo la plantilla |
| ESC-04 | Vendedor titular ausente | Colaborador, cliente | El cliente llama y su vendedor está en obra o ya no trabaja en la empresa | El colaborador busca al cliente por código, nombre o tipo de obra → lee el historial → responde | El cliente no repite su historia (M4) | Ficha incompleta: se registra como falla de la prueba de recuperación |
| ESC-05 | Revisión semanal | Gerencia | Es lunes | La gerencia abre el reporte: solicitudes, mediana de primer contacto, estados y motivos de pérdida | La gerencia conoce el embudo sin preguntar a cada vendedor | — |
| ESC-06 | Discrepancia con un cliente | Gerencia | El cliente dice que se le ofreció otro precio | Se verifica la integridad del registro y se compara la huella de la cotización enviada | Se demuestra si la cotización fue alterada después de su fecha | La verificación detecta una alteración: se reporta el evento afectado |
| ESC-07 | Solicitud sin atender | Sistema, coordinador, gerencia | Pasan 15 min sin primer contacto | El sistema envía un recordatorio al responsable y un aviso a la gerencia | Alguien atiende la solicitud | Por definir en el taller: si se reasigna de forma automática (CON-06) |
| ESC-08 | El cliente pide eliminar sus datos | Cliente, gerencia | El cliente ejerce su derecho de eliminación (LOPDP) | Se localiza la ficha por código → se eliminan los datos personales → el registro conserva solo huellas y códigos | Derecho atendido sin romper la verificación del registro | — |

### 8.5 Actores y casos de uso de alto nivel

| Actor | Objetivo | Casos de uso relacionados |
|---|---|---|
| Prospecto o cliente | Pedir una cotización y recibir respuesta rápida | CU-01 Enviar solicitud; CU-11 Ejercer derechos sobre sus datos |
| Coordinador comercial | Atender a tiempo y dar seguimiento | CU-02 Recibir alerta; CU-03 Registrar una solicitud manual; CU-04 Cambiar el estado; CU-06 Consultar la ficha |
| Quien cotiza | Preparar cotizaciones más rápido | CU-05 Generar un borrador con el asistente; CU-06 Consultar la ficha |
| Gerencia | Controlar el embudo y resolver discrepancias | CU-07 Ver el reporte semanal; CU-08 Verificar la integridad del registro; CU-09 Gestionar las cuentas autorizadas |
| Servicio LLM (sistema externo) | Generar texto a partir del contexto recuperado | CU-05 |
| Slack (sistema externo) | Entregar la alerta | CU-02 |
| Reloj del sistema | Disparar el recordatorio y el reporte | CU-10 Recordar una solicitud sin atender; CU-07 |

### 8.6 Interacción entre usuarios y sistema

- **En obra:** uso breve, con una mano, al sol y con señal intermitente. Por eso: alertas cortas, acceso de un toque, pocos campos obligatorios y consulta sin conexión de las fichas ya sincronizadas.
- **En la oficina:** uso más largo para cotizar; se aceptan pantallas con más detalle.
- **Habilidades esperadas:** uso de WhatsApp y de una hoja de cálculo. No se exige capacitación formal larga, y la meta de usabilidad es SUS ≥ 68.

## 9. Necesidades de los interesados

### 9.1 Registro de necesidades

| ID | Necesidad | Interesado o fuente | Sesión | Tipo | Justificación | Medida de efectividad | Prioridad preliminar | Estado |
|---|---|---|---|---|---|---|---|---|
| NEC-01 | Enterarse de inmediato de cada solicitud aunque se esté en obra | INT-02, INT-01 | SES-01 | Explícita | El 40 % revisa mensajes cada 3–4 h | M1 | Alta | Aceptada |
| NEC-02 | Un registro único de solicitudes, fuera de los WhatsApp personales | INT-01 | SES-01, SES-04 | Explícita | 4 de 5 reciben clientes en su WhatsApp personal | M3 | Alta | Aceptada |
| NEC-03 | Saber quién es responsable de cada solicitud y en qué estado está | INT-01 | SES-05 | Explícita | La gerencia no sabe cuántas cotizaciones hay en curso | M1, M3 | Alta | Aceptada |
| NEC-04 | Preparar cotizaciones sin empezar de cero | INT-03 | SES-05 | Implícita | Cotizaciones anteriores dispersas | M2 | Alta | Aceptada |
| NEC-05 | Recuperar el historial de un cliente aunque el vendedor titular no esté | INT-04, INT-01 | SES-03, SES-05 | Implícita | Amnesia institucional (A8) | M4 | Alta | Aceptada |
| NEC-06 | Conocer los motivos de pérdida de clientes cada semana | INT-01 | SES-01 | Explícita | 3 de 5 en el censo | Reporte semanal | Media | Aceptada |
| NEC-07 | Usar la herramienta desde el celular, con mala conectividad y sin interfaces complejas | INT-02 | SES-01, SES-02 | Explícita | Limitaciones en campo (40 % cada una) | M6 | Alta | Aceptada |
| NEC-08 | Acceder a la ficha del cliente con un solo toque desde la alerta | INT-02 | SES-02 | Explícita | Fricción detectada en la prueba del MVP | M1 | Alta | Aceptada |
| NEC-09 | Probar quién atendió, qué se ofreció y cuándo | INT-01 | SES-03 | Implícita | Discrepancias con clientes y mérito comercial (FNT-01) | M5 | Media | Aceptada |
| NEC-10 | Proteger los datos personales de los clientes | INT-05, INT-08 | SES-03 | Implícita | LOPDP, arts. 8, 10 y 12 | OBJ-07 | Alta | Aceptada |
| NEC-11 | Recordar el seguimiento de cotizaciones enviadas | INT-02 | SES-05 | Implícita | El cliente «se enfría» sin recordatorios | Ninguna meta lo mide hoy | Media | En análisis |
| NEC-12 | Reportes para la gerencia sobre solicitudes y tiempos | INT-01 | SES-01 | Explícita | Necesidad del perfil de usuario | Reporte semanal | Media | Aceptada |
| NEC-13 | Módulo de avance de obra con reporte fotográfico | INT-01 | SES-01 | Explícita | 4 de 5 en el censo | — | Baja | Descartada (fuera del alcance) |
| NEC-14 | Costo de operación bajo, sin licencias caras | INT-01 | SES-03, SES-04 | Explícita | Pyme; los CRM tradicionales están fuera de su presupuesto | Costo mensual (PEN-10) | Alta | Aceptada |
| NEC-15 | Medir las metas M1–M6 frente a la línea base | INT-06, INT-07 | SES-03 | Explícita | Objetivo OE4 | M1–M6 | Alta | Aceptada |

### 9.2 Priorización y selección de necesidades

Se priorizó según tres criterios:
- la frecuencia con que aparece la necesidad en el censo;
- su relación directa con una meta de validación (M1–M6);
- el riesgo de no atenderla.

Se descartó NEC-13 (módulo de avance de obra) porque responde a la gestión de obra y no al problema comercial (véase la sección 11.4). Queda como línea futura del plan Premium de TEAMSLASH. NEC-11 sigue en análisis porque ninguna meta la mide: se decide en el taller si entra como recordatorio simple o se difiere.

## 10. Transformación de necesidades en requerimientos

### 10.1 Restricciones de la solución

| ID | Restricción | Origen | Requerimientos afectados |
|---|---|---|---|
| RES-01 | Construir sobre la infraestructura existente de TEAMSLASH | Diseño aprobado (OE3) | RQ-01 a RQ-08 |
| RES-02 | Bóveda en Obsidian, en archivos Markdown | Diseño aprobado | RQ-09, RQ-10, RQ-13, RQ-14 |
| RES-03 | Registro verificable con SHA-256 y registro de solo agregar, sin cadena de bloques | Decisión D6, sin objeciones de la tutora | RQ-15 a RQ-17 |
| RES-04 | Cumplir la LOPDP y su reglamento | Normativa | RQ-17 a RQ-21 |
| RES-05 | Validación del 23-nov al 5-dic-2026; entrega el 4-ene-2027 | Proyecto | RQ-23 |
| RES-06 | Equipo de dos estudiantes; presupuesto limitado | Proyecto | Todos |
| RES-07 | Conectividad limitada en obra | Contexto de uso | RQ-02, RQ-14 |
| RES-08 | No usar los datos simulados del diagnóstico (N = 30) | Decisión del equipo, sin objeciones de la tutora | RQ-23 |
| RES-09 | Obsidian no ofrece permisos por usuario dentro de una bóveda | Documentación oficial de Obsidian | RQ-20, RQ-21 |

### 10.2 Características de calidad críticas

Según el modelo ISO/IEC 25010:2023:
- **Seguridad** (confidencialidad e integridad): RQ-15 a RQ-21.
- **Fiabilidad** (disponibilidad y tolerancia a fallos de la alerta): RQ-01, RQ-02, RQ-14.
- **Usabilidad** (capacidad de aprendizaje y operabilidad en obra): RQ-02, RQ-03, RQ-22.
- **Mantenibilidad:** el equipo es de dos personas, por lo que se prefieren componentes estándar.
- **Eficiencia de desempeño:** latencia de la alerta y tiempo de recuperación del historial.

### 10.3 Convenciones de redacción

- **deberá:** requerimiento obligatorio.
- **debería:** preferencia u objetivo deseable; no es requerimiento.
- **podrá:** sugerencia o permiso; no es requerimiento.
- **será / es:** texto descriptivo.
- Se redacta en voz activa y en forma positiva.

### 10.4 Estructura sintáctica

[Condición] [Sujeto] deberá [Acción] [Objeto] [Restricción o criterio medible]. Ejemplo: «Cuando se registre una solicitud, el sistema deberá enviar una alerta al celular del responsable en un máximo de 5 segundos».

### 10.5 Clasificación de requerimientos

- **F:** funcional.
- **NF-T:** no funcional, restricción tecnológica.
- **NF-C:** no funcional, restricción de calidad de servicio.
- **N:** normativo.
- **P:** del proyecto.

### 10.6 Requerimientos

| ID | Enunciado | Tipo | Necesidad | Fuente | Escenario | Criterio de aceptación | Verificación |
|---|---|---|---|---|---|---|---|
| RQ-01 | Cuando un prospecto envíe el formulario, el sistema deberá registrar la solicitud con fecha y hora de ingreso en el registro central en un máximo de 5 segundos | F | NEC-02 | INT-01, FNT-02 | ESC-01 | En 10 envíos de prueba, 10 registros con hora y ninguno a más de 5 s | Prueba |
| RQ-02 | Cuando se registre una solicitud, el sistema deberá enviar una alerta al celular del responsable en un máximo de 5 segundos, con el nombre del prospecto, el tipo de obra y un enlace directo a su ficha | F | NEC-01, NEC-08 | INT-02, SES-01, SES-02 | ESC-01 | Dado un envío, cuando se registra, entonces la alerta llega en ≤ 5 s y el enlace abre la ficha | Prueba |
| RQ-03 | El sistema deberá permitir registrar desde el celular una solicitud recibida por WhatsApp o por teléfono, con los mismos campos mínimos del formulario y la hora real de llegada | F | NEC-02 | INT-02, SES-01 | ESC-02 | Registro completo en 1 minuto o menos en la prueba con usuarios | Demostración |
| RQ-04 | El sistema deberá asignar cada solicitud a un único responsable y registrar la asignación con fecha y hora | F | NEC-03 | INT-01, SES-05 | ESC-01 | Ninguna solicitud sin responsable en el reporte | Inspección |
| RQ-05 | El sistema deberá registrar el estado de cada solicitud con los valores Nueva, En contacto, Cotizada, Ganada y Perdida | F | NEC-03 | INT-01, FNT-02 | ESC-05 | Cada cambio de estado queda con fecha, hora y responsable | Prueba |
| RQ-06 | Cuando una solicitud cumpla 15 minutos sin primer contacto, el sistema deberá enviar un recordatorio al responsable y un aviso a la gerencia | F | NEC-01, NEC-03 | INT-01, SES-01 | ESC-07 | Recordatorio emitido entre los minutos 15 y 16 en la prueba | Prueba |
| RQ-07 | Cuando el responsable marque una solicitud como Perdida, el sistema deberá exigir un motivo elegido de una lista cerrada | F | NEC-06 | INT-01, SES-01 | ESC-05 | No se puede guardar el estado Perdida sin motivo | Prueba |
| RQ-08 | El sistema deberá generar cada lunes un reporte con las solicitudes de la semana, la mediana del tiempo de primer contacto, los estados y los motivos de pérdida | F | NEC-06, NEC-12 | INT-01 | ESC-05 | Reporte generado con datos que coinciden con el registro | Inspección |
| RQ-09 | La bóveda deberá contener una ficha por cliente, identificada con un código, con su historial de solicitudes, contactos y cotizaciones | F | NEC-05 | INT-01, FNT-01 | ESC-04 | Cada cliente del registro tiene ficha y código | Inspección |
| RQ-10 | La bóveda deberá contener plantillas de cotización por tipo de obra | F | NEC-04 | INT-03, FNT-01 | ESC-03 | Una plantilla por cada tipo de obra del catálogo de Torvesa | Inspección |
| RQ-11 | Cuando el usuario pida un borrador, el asistente deberá generar una respuesta o una cotización a partir de la ficha, las plantillas y las cotizaciones anteriores de la bóveda, e indicar qué documentos usó | F | NEC-04 | INT-03, FNT-01 | ESC-03 | En los casos de prueba, cada borrador cita al menos un documento de la bóveda | Prueba |
| RQ-12 | El sistema deberá requerir la revisión y la aprobación del usuario antes de enviar al cliente cualquier borrador del asistente | NF-C | NEC-04, NEC-10 | INT-03, SES-03 | ESC-03 | Ningún envío sin la acción explícita del usuario | Demostración |
| RQ-13 | El sistema deberá permitir a un usuario autorizado buscar un cliente por código, nombre o tipo de obra y mostrar su historial completo | F | NEC-05 | INT-04 | ESC-04 | En la prueba de recuperación, menos tiempo y más aciertos que en la línea base (M4) | Prueba |
| RQ-14 | La aplicación móvil de la bóveda deberá mostrar sin conexión las fichas ya sincronizadas y sincronizar los cambios al recuperar la señal | NF-C | NEC-07 | INT-02, SES-01 | ESC-04 | Ficha visible en modo avión; cambios sincronizados al reconectar | Demostración |
| RQ-15 | El sistema deberá guardar cada evento (solicitud, asignación, cambio de estado, cotización enviada) en un registro de solo agregar, con la huella SHA-256 del evento y la del evento anterior | F | NEC-09 | INT-01, FNT-10 | ESC-06 | Cada evento tiene su huella y la del anterior | Inspección |
| RQ-16 | El sistema deberá verificar la integridad del registro y señalar cada evento alterado | F | NEC-09 | FNT-01 | ESC-06 | 100 % de las alteraciones simuladas detectadas (M5) | Prueba |
| RQ-17 | El registro verificable deberá contener solo huellas y códigos, sin datos personales | N | NEC-10 | INT-08, FNT-08 | ESC-08 | Inspección sin datos personales en el registro | Inspección |
| RQ-18 | El formulario deberá pedir el consentimiento del prospecto para el tratamiento de sus datos, con un enlace al aviso de privacidad, antes de enviar la solicitud | N | NEC-10 | INT-08, FNT-08 | ESC-01 | No se puede enviar el formulario sin marcar el consentimiento | Prueba |
| RQ-19 | El sistema deberá eliminar o anonimizar los datos personales de los prospectos perdidos al cumplirse el plazo de conservación que fije la gerencia | N | NEC-10 | INT-08, FNT-08 | ESC-08 | Plazo definido (PEN-04) y procedimiento probado | Demostración |
| RQ-20 | El sistema deberá dar acceso solo a cuentas individuales autorizadas por la gerencia | NF-C | NEC-10 | INT-01, RES-09 | — | Lista de cuentas aprobada; ninguna cuenta compartida | Inspección |
| RQ-21 | El asistente deberá enviar al servicio LLM solo códigos de cliente, nunca nombres, teléfonos ni correos | N | NEC-10 | INT-08, SES-04 | ESC-03 | Revisión de 10 solicitudes al LLM sin datos personales | Inspección |
| RQ-22 | El sistema deberá alcanzar un puntaje SUS de 68 o más entre sus usuarios al final de la validación | NF-C | NEC-07 | INT-02, FNT-14 | — | Puntaje SUS ≥ 68 (M6) | Análisis |
| RQ-23 | La validación del diseño en operación experimental controlada deberá durar dos semanas (23-nov al 5-dic-2026) con solicitudes reales de Torvesa | P | NEC-15 | INT-07, FNT-01 | — | Registro de las dos semanas completo | Inspección |

**Atributos comunes de esta versión:**
- versión 0.1;
- estado «Propuesto»;
- propietario: Víctor Segura para los requerimientos de negocio y Diego Bermeo para los técnicos;
- estabilidad media en RQ-05, RQ-06, RQ-07 y RQ-19, que dependen del taller, y alta en los demás.

## 11. Análisis de requerimientos

### 11.1 Verificación de características de cada requerimiento

Se aplicó la lista a los 23 requerimientos. Resultado: todos son necesarios, singulares, verificables y conformes con la plantilla. Las observaciones:

| Requerimiento | Característica que falla | Observación y acción correctiva |
|---|---|---|
| RQ-05 | Aceptable | Los estados aún no están acordados con la gerencia (CON-01). Validar en el taller |
| RQ-06 | Aceptable | El aviso a la gerencia puede percibirse como control excesivo (CON-06). Validar en el taller |
| RQ-07 | Completo | Falta la lista cerrada de motivos (PEN-07) |
| RQ-10 | Completo | Falta el catálogo de tipos de obra de Torvesa (pedido en el correo a la gerencia) |
| RQ-11 | Factible | El riesgo técnico es alto; los RAG en la industria siguen en etapa de prototipo. Se acota a borradores con revisión humana (RQ-12) |
| RQ-19 | Completo | El plazo de conservación está por definir (PEN-04) |
| RQ-13 | Inequívoco | «Historial completo» se define en la plantilla de la ficha (PO2 de la tesis) |

### 11.2 Verificación del conjunto de requerimientos

| Característica | ¿Cumple? | Observación |
|---|---|---|
| Completo | No | Quedan pendientes abiertos (sección 14.1); no se completa hasta validar en campo |
| Consistente | Sí | La terminología se unificó con el glosario (sección 1.3) |
| Consistente con las fuentes | Parcial | El almacenamiento de TEAMSLASH difiere entre el informe y el pitch (CON-04) |
| Factible | Sí, con condición | Factible en el plazo si el campo se autoriza antes de la semana del 2-nov |
| Comprensible | Sí | Cada requerimiento tiene un escenario asociado |
| Conciso | Sí | — |
| Validable | Sí | Cada objetivo tiene una meta M1–M6 o una lista de verificación |

### 11.3 Revisión del lenguaje

| Requerimiento o fuente | Término detectado | Redacción corregida |
|---|---|---|
| HU-03 del antecedente | «apenas ingrese» | «en un máximo de 5 segundos» (RQ-02) |
| Informe Final, sección 3.4 | «fricción cero», «ultraveloz» | Se reemplaza por la meta SUS ≥ 68 (RQ-22) y por tiempos medibles |
| HU-01 del antecedente | «formulario claro» y «en pocos pasos» | Campos mínimos definidos y registro en 1 minuto o menos (RQ-03) |
| Informe Final, sección 4.4 | «trazabilidad y auditoría» | Registro de solo agregar con huellas encadenadas (RQ-15) y verificación (RQ-16) |
| Informe Final, sección 4.1 | «garantizando que ningún lead se pierda» (totalidad) | Recordatorio a los 15 minutos (RQ-06); la fuga se mide (M3) |
| Borrador de RQ-13 | «rápidamente» | «menos tiempo que en la línea base» (M4) |

### 11.4 Identificación del problema real (5 porqués)

| Paso | Caso 1: «Necesitamos alertas en Slack» | Caso 2: «Queremos un módulo de avance de obra con fotos» |
|---|---|---|
| Enunciado original | Pedido de la iteración 1 | Pedido de 4 de 5 en el censo (P8) |
| ¿Por qué? 1 | Porque nadie ve las solicitudes a tiempo | Porque la gerencia no sabe cómo avanzan las obras |
| ¿Por qué? 2 | Porque llegan a celulares personales y el personal está en obra | Porque los reportes de obra son verbales |
| ¿Por qué? 3 | Porque no existe un registro de la empresa ni un responsable asignado, y el conocimiento de cada cliente queda en cada persona | Es un problema de gestión de obra, no de la atención comercial |
| Problema real | El conocimiento comercial no es de la empresa y no hay un flujo con responsable | Fuera del problema de la tesis |
| Requerimiento reformulado | RQ-01 a RQ-04 y RQ-09; la alerta (RQ-02) es un medio, no el fin | NEC-13 descartada; línea futura (sección 11.9) |

### 11.5 Análisis de restricciones de calidad de servicio

| Requerimiento | Métrica | Punto de falla | Nivel objetivo | Punto de perfección | Relación con otros atributos |
|---|---|---|---|---|---|
| RQ-02 | Segundos del registro a la alerta | > 60 s | ≤ 5 s (en el antecedente se midió 3,2 s en promedio) | ≤ 1 s | Depende de la red; más campos en la alerta aumentan el consumo de datos |
| RQ-06 / M1 | Mediana de minutos hasta el primer contacto | Igual o peor que la línea base | < 15 min (meta de diseño) | < 5 min | Más avisos mejoran M1, pero aumentan la saturación de mensajes (usabilidad) |
| RQ-13 / M4 | Minutos para recuperar el historial de un cliente ajeno | Igual o peor que la línea base | ≤ 2 min (propuesta a validar) | ≤ 30 s | Más campos en la ficha mejoran los aciertos, pero cuestan tiempo de registro |
| RQ-11 / M2 | Minutos para elaborar una cotización | Igual o peor que la línea base | Menor que la línea base | — | Contexto más grande para el LLM: mejor borrador, pero más costo por consulta y más exposición de datos (RQ-21) |
| RQ-22 / M6 | Puntaje SUS | < 68 | ≥ 68 | ≥ 80 | Más funciones pueden bajar la usabilidad |

### 11.6 Modelado de requerimientos

| Modelo | Propósito | Hallazgos | Anexo |
|---|---|---|---|
| Proceso actual (AS-IS) en BPMN, con carriles por rol | Ver dónde se pierde tiempo o información | Cinco puntos críticos; el seguimiento (punto 4) no tiene meta que lo mida, lo que originó NEC-11 | E |
| Diagrama de casos de uso (CU-01 a CU-11) | Ordenar actores y funciones | Faltaba un caso para el registro manual de solicitudes de WhatsApp (CU-03, RQ-03) | E (por dibujar, PEN-11) |
| Modelo conceptual del dominio: Cliente, Solicitud, Asignación, Estado, Cotización, Plantilla, Evento, Huella | Definir los datos de la ficha y del registro | El Evento debe referir al Cliente solo por código para cumplir RQ-17 | E (por dibujar, PEN-11) |
| Proceso objetivo (TO-BE) en BPMN | Mostrar el flujo con el sistema | Se elabora en el sprint de diseño (2 a 8 de noviembre) | — |

### 11.7 Gestión de conflictos

| ID | En conflicto | Interesados | Descripción | Alternativas | Resolución |
|---|---|---|---|---|---|
| CON-01 | Estados de la solicitud | INT-01, INT-02 | El MVP usa tres colores (Nuevo, En proceso, Cerrado); el perfil de usuario pide cuatro estados; la gerencia quiere los motivos de pérdida | (a) tres colores; (b) cinco estados con colores (RQ-05) | Propuesta (b); se acuerda en el taller |
| CON-02 | Canal de ingreso | INT-05, INT-02 | Los clientes escriben al WhatsApp personal; el MVP exige el formulario web | (a) solo formulario; (b) registro manual rápido más enlace al formulario; (c) CRM con WhatsApp oficial (Kommo: plazo mínimo de 6 meses) | Propuesta (b) (RQ-03); (c) diferida |
| CON-03 | Control de la gerencia frente a la privacidad del vendedor y del cliente | INT-01, INT-02, INT-05 | El registro de «quién atendió» puede vivirse como vigilancia | Registro solo con huellas y códigos; reportes agregados | RQ-17; se explica en el taller |
| CON-04 | Almacenamiento de TEAMSLASH | Fuentes FNT-02 y FNT-03 | El informe dice Google Sheets; el pitch dice PostgreSQL | Confirmar lo que está desplegado hoy | Pendiente con Diego (PEN-01) |
| CON-05 | Asistente de IA en la nube frente a la protección de datos | INT-05, INT-08 | Las fichas contienen datos personales | Solo códigos al LLM (RQ-21); proveedor que no entrena con los datos de la API | RQ-21; responsable del tratamiento a confirmar con la tutora (PEN-05) |
| CON-06 | Escalar a la gerencia a los 15 minutos | INT-01, INT-02 | Más control frente a más presión sobre el equipo en obra | (a) solo recordatorio; (b) recordatorio y aviso; (c) reasignación automática | Propuesta (b); se acuerda en el taller |

### 11.8 Priorización

Esquema: Prioridad = Valor × (1 − Riesgo) / Costo (Washizaki, 2025, sec. 7.2). Valor, insatisfacción y costo van en una escala de 1 a 5; el riesgo, de 0 a 1. Los requerimientos se agrupan así:
- **Alta:** ≥ 3,0.
- **Media:** de 1,2 a 2,9.
- **Baja:** < 1,2.

| Requerimiento | Valor | Insatisfacción si falta | Costo | Riesgo | Prioridad | Grupo |
|---|---|---|---|---|---|---|
| RQ-01 Registro de la solicitud | 5 | 5 | 1 | 0,1 | 4,5 | Alta |
| RQ-02 Alerta con enlace | 5 | 5 | 1 | 0,1 | 4,5 | Alta |
| RQ-12 Revisión humana de los borradores | 5 | 5 | 1 | 0,1 | 4,5 | Alta |
| RQ-17 Registro sin datos personales | 5 | 5 | 1 | 0,1 | 4,5 | Alta |
| RQ-18 Consentimiento en el formulario | 5 | 5 | 1 | 0,1 | 4,5 | Alta |
| RQ-21 Solo códigos al LLM | 5 | 5 | 1 | 0,1 | 4,5 | Alta |
| RQ-03 Registro manual (WhatsApp) | 5 | 5 | 1 | 0,2 | 4,0 | Alta |
| RQ-04 Responsable único | 4 | 4 | 1 | 0,1 | 3,6 | Alta |
| RQ-05 Estados | 4 | 4 | 1 | 0,1 | 3,6 | Alta |
| RQ-07 Motivo de pérdida | 3 | 3 | 1 | 0,2 | 2,4 | Media |
| RQ-09 Ficha del cliente | 5 | 5 | 2 | 0,2 | 2,0 | Media |
| RQ-13 Búsqueda del historial | 5 | 4 | 2 | 0,2 | 2,0 | Media |
| RQ-10 Plantillas | 4 | 3 | 2 | 0,2 | 1,6 | Media |
| RQ-16 Verificación de integridad | 4 | 3 | 2 | 0,2 | 1,6 | Media |
| RQ-06 Recordatorio a los 15 min | 4 | 3 | 2 | 0,3 | 1,4 | Media |
| RQ-20 Cuentas individuales | 4 | 4 | 2 | 0,3 | 1,4 | Media |
| RQ-22 SUS ≥ 68 | 4 | 3 | 2 | 0,3 | 1,4 | Media |
| RQ-08 Reporte semanal | 3 | 3 | 2 | 0,2 | 1,2 | Media |
| RQ-14 Consulta sin conexión | 4 | 4 | 2 | 0,4 | 1,2 | Media |
| RQ-19 Plazo de conservación | 3 | 3 | 2 | 0,3 | 1,05 | Baja |
| RQ-15 Registro de solo agregar | 4 | 3 | 3 | 0,3 | 0,93 | Baja* |
| RQ-11 Borrador con IA | 4 | 3 | 4 | 0,5 | 0,5 | Baja* |

\* **Ajuste de alcance:** RQ-11 y RQ-15 salen con prioridad baja por su costo y su riesgo, pero son componentes del objetivo general aprobado por la carrera y sustentan las metas M2 y M5. Por eso se mantienen como obligatorios y su riesgo se reduce acotándolos: borradores con revisión humana y un registro simple sin servicios externos. RQ-19 se mantiene porque la ley lo exige (LOPDP, art. 10, lit. i).

### 11.9 Depuración de requerimientos y ajuste del alcance

| Requerimiento eliminado o diferido | Motivo |
|---|---|
| Módulo de avance de obra con reporte fotográfico (NEC-13) | Fuera del problema comercial; línea futura del plan Premium |
| Integración oficial con WhatsApp Business (CON-02 c) | Costo y plazo mínimo de 6 meses; no cabe en la validación de dos semanas |
| Envío automático de cotizaciones sin revisión | Riesgo de errores de precio del LLM; contradice RQ-12 |
| Aplicación móvil nativa | Costo y plazo (alternativa C) |
| Recordatorios de seguimiento después de la cotización (NEC-11) | En análisis; se decide en el taller si entra como recordatorio simple |

Con este ajuste, el conjunto es realizable en dos sprints (diseño del 2 al 8 de noviembre y prueba de concepto del 9 al 15 de noviembre), siempre que el trabajo de campo se autorice a tiempo.

### 11.10 Medidas de desempeño críticas

| Medida | Requerimientos | Valor esperado | Forma de medición |
|---|---|---|---|
| M1 Tiempo de primer contacto (mediana) | RQ-01 a RQ-06 | < 15 min | Horas registradas por el sistema durante la validación, frente a la muestra documental de la línea base |
| M2 Tiempo de elaboración de la cotización | RQ-10 a RQ-12 | Menor que la línea base | Cronometraje en los casos de prueba (P2-A) |
| M3 Fuga previa al primer contacto | RQ-03, RQ-06 | Menor que la línea base | Solicitudes sin primer contacto / total |
| M4 Recuperación del historial | RQ-09, RQ-13, RQ-14 | Menos tiempo y más aciertos que la línea base | Prueba de recuperación con clientes ajenos; I1 (A5, A6) |
| M5 Integridad del registro | RQ-15, RQ-16 | 100 % de las alteraciones detectadas | Alteraciones simuladas |
| M6 Usabilidad | RQ-22 | SUS ≥ 68 | Encuesta SUS en español al final de la validación |
| Latencia de la alerta | RQ-02 | ≤ 5 s | 10 envíos de prueba en red móvil |

## 12. Validación con los interesados

### 12.1 Técnica de validación aplicada

Se validará en tres momentos:
1. **Revisión del documento con la tutora** (28-oct-2026), para el alcance y el método.
2. **Taller con la gerencia y el equipo comercial,** con lista de verificación, recorrido de los escenarios ESC-01 a ESC-08 y pantallas de baja fidelidad. Las pantallas se muestran después de recorrer los escenarios, para que la discusión no se desvíe a detalles cosméticos (Washizaki, 2025, sec. 5).
3. **Casos de prueba y validación del diseño en operación experimental controlada,** que verifican los criterios de aceptación.

### 12.2 Registro de la validación

| Fecha | Técnica | Participantes | Requerimientos revisados | Observaciones | Cambios | Resultado | Evidencia |
|---|---|---|---|---|---|---|---|
| Julio de 2026 | Prototipo (MVP) | INT-02 | HU-01 a HU-07 del antecedente | Fricción al buscar al cliente | Botón «Ver ficha» | Aprobado con cambios | Informe Final, p. 24 |
| 28-oct-2026 | Revisión del documento | INT-07 | Alcance, RQ-01 a RQ-23 | Por registrar | Por registrar | Pendiente | Acta de la Revisión 1 |
| Por fijar | Taller con lista de verificación y escenarios | INT-01, INT-02, INT-03 | RQ-01 a RQ-23; CON-01 a CON-06 | — | — | Pendiente | Acta del taller (Anexo G) |

## 13. Trazabilidad

| Objetivo | Necesidad | Interesado o fuente | Sesión | Requerimiento | Escenario o caso de uso | Criterio o prueba |
|---|---|---|---|---|---|---|
| OBJ-01 | NEC-01 | INT-02 | SES-01 | RQ-02 | ESC-01 / CU-02 | Alerta ≤ 5 s; M1 |
| OBJ-01 | NEC-02 | INT-01 | SES-01 | RQ-01, RQ-03 | ESC-01, ESC-02 / CU-01, CU-03 | Registro con hora; M1 |
| OBJ-01 | NEC-03 | INT-01 | SES-05 | RQ-04, RQ-05, RQ-06 | ESC-07 / CU-04, CU-10 | Ninguna solicitud sin responsable; recordatorio a los 15 min |
| OBJ-01 | NEC-08 | INT-02 | SES-02 | RQ-02 | ESC-01 / CU-02 | El enlace abre la ficha |
| OBJ-02 | NEC-04 | INT-03 | SES-05 | RQ-10, RQ-11, RQ-12 | ESC-03 / CU-05 | M2 |
| OBJ-03 | NEC-02, NEC-03 | INT-01 | SES-01 | RQ-03, RQ-06 | ESC-02, ESC-07 | M3 |
| OBJ-04 | NEC-05 | INT-04 | SES-03, SES-05 | RQ-09, RQ-13, RQ-14 | ESC-04 / CU-06 | M4 |
| OBJ-04 | NEC-06, NEC-12 | INT-01 | SES-01 | RQ-07, RQ-08 | ESC-05 / CU-07 | El reporte coincide con el registro |
| OBJ-05 | NEC-09 | INT-01 | SES-03 | RQ-15, RQ-16 | ESC-06 / CU-08 | M5 |
| OBJ-06 | NEC-07 | INT-02 | SES-01, SES-02 | RQ-14, RQ-22 | ESC-04 | M6 |
| OBJ-07 | NEC-10 | INT-05, INT-08 | SES-03 | RQ-17 a RQ-21 | ESC-08 / CU-11 | Lista de verificación LOPDP |
| OBJ-01 a OBJ-07 | NEC-14 | INT-01 | SES-04 | Restricción de costo (PEN-10) | — | Costo mensual dentro del tope |
| OE4 | NEC-15 | INT-06, INT-07 | SES-03 | RQ-23 | — | Validación completa |

Revisión: todos los requerimientos tienen origen. NEC-11 no tiene requerimiento (posible faltante, en análisis) y NEC-13 fue descartada.

## 14. Asuntos pendientes y riesgos

### 14.1 Asuntos pendientes (TBD / TBR)

| ID | Descripción | Requerimiento afectado | Responsable | Fecha límite |
|---|---|---|---|---|
| PEN-01 | Confirmar si TEAMSLASH guarda los datos en Google Sheets o en PostgreSQL | RQ-01, RQ-05 | Diego | 30-oct-2026 |
| PEN-02 | Autorización de Torvesa para el trabajo de campo | Todas las sesiones SES-06 a SES-11 | Diego (contacto) y Víctor (escalamiento) | 31-oct-2026 |
| PEN-03 | Volumen semanal de solicitudes | RQ-23, M1, M3 | Diego | Al revisar la muestra documental |
| PEN-04 | Plazo de conservación de los datos de prospectos perdidos | RQ-19 | Gerencia de Torvesa | Taller |
| PEN-05 | Responsable del tratamiento de datos y comité de ética | RQ-17 a RQ-21 | Tutora | 28-oct-2026 |
| PEN-06 | Visto bueno al LLM preseleccionado | RQ-11, RQ-21 | Víctor | 30-oct-2026 |
| PEN-07 | Lista cerrada de motivos de pérdida | RQ-07 | Taller | Taller |
| PEN-08 | ¿Alguien aprueba las cotizaciones antes de enviarlas? | RQ-12 | Entrevista I3 | Entrevistas |
| PEN-09 | ¿Hay visita a la obra antes de cotizar? | RQ-05 | Entrevista I3 | Entrevistas |
| PEN-10 | Presupuesto mensual máximo del sistema para Torvesa | Restricción de costo | Gerencia | Taller |
| PEN-11 | Dibujar el diagrama de casos de uso y el modelo conceptual | Sección 11.6 | Diego | 4-nov-2026 |
| PEN-12 | Catálogo de tipos de obra de Torvesa | RQ-10 | Gerencia | Taller |

### 14.2 Riesgos asociados a los requerimientos

| ID | Descripción | Requerimientos afectados | Probabilidad | Impacto | Mitigación |
|---|---|---|---|---|---|
| RIE-01 | La empresa no autoriza el campo a tiempo | Todos (falta la validación) | Media | Alto | Escalamiento el 31-oct; los requerimientos de la iteración 1 permiten avanzar con el diseño |
| RIE-02 | Requerimientos basados en una muestra pequeña y de un solo nivel jerárquico (n = 5) | RQ-01 a RQ-08 | Alta | Medio | Encuestas censales I1 e I2 y taller |
| RIE-03 | Las solicitudes de WhatsApp no se registran y la medición queda incompleta | RQ-03, M1, M3 | Media | Alto | Registro en 1 minuto o menos; enlace al formulario; revisión diaria en la validación |
| RIE-04 | El asistente inventa precios o rubros | RQ-11 | Media | Alto | Revisión humana obligatoria (RQ-12); citar documentos |
| RIE-05 | Caídas o cambios de precio de servicios de terceros (Slack, LLM, Railway, Vercel) | RQ-02, RQ-11 | Baja | Medio | Planes gratuitos o por consumo; alternativa documentada en el inventario |
| RIE-06 | Pocas solicitudes en las dos semanas de validación | RQ-23, M1, M3 | Media | Medio | Resultados descriptivos; casos de prueba complementarios |

### 14.3 Supuestos y dependencias

- El personal comercial tiene un celular inteligente con datos móviles.
- La gerencia acepta registrar el estado de cada solicitud.
- El MVP TEAMSLASH sigue desplegado y accesible.
- Las cifras del antecedente se toman como hipótesis hasta medir la línea base:
  - más de 24 horas de respuesta;
  - USD 15.000 por cliente perdido;
  - 4 a 11 minutos en los simulacros.
- **Dependencias externas:** autorización de Torvesa; Slack; el proveedor del LLM; Obsidian y Git.

## 15. Línea base y aprobación

| Campo | Contenido |
|---|---|
| Versión de línea base | 1.0 (todavía no declarada) |
| Fecha prevista | Al cerrar el taller de validación con Torvesa |
| Requerimientos aprobados | 0 de 23 (todos en estado «Propuesto») |

| Rol | Nombre | Firma | Fecha |
|---|---|---|---|
| Estudiante | Víctor Segura Heredia | | |
| Estudiante | Diego Bermeo Torres | | |
| Tutora | Ing. Tania Chicaiza | | |
| Representante de la organización beneficiaria | Gerencia de Torvesa Constructora | | |

## 16. Anexos

- **Anexo A.** Guía de entrevista I3 (v0.1, 11-oct-2026), con las siete preguntas de validación del AS-IS.
- **Anexo B.** Cuestionarios I1 (v0.2) e I2 (v0.1). Los resultados se agregan después de aplicarlos.
- **Anexo C.** Censo de validación del proyecto integrador: Informe Final de TEAMSLASH, Tabla 1, pp. 9–10.
- **Anexo D.** Prototipo: MVP TEAMSLASH desplegado. Las pantallas de baja fidelidad para el taller se elaboran en el sprint de diseño.
- **Anexo E.** Modelos: proceso actual (AS-IS) en BPMN v0.1. El diagrama de casos de uso y el modelo conceptual se dibujan en el sprint de diseño (PEN-11).
- **Anexo F.** Consentimiento informado C1 (v0.2).
- **Anexo G.** Actas de validación (después del taller).
- **Anexo H.** Planteamiento del problema (*problem statement*), documento complementario v0.1.

## Referencias

International Organization for Standardization, International Electrotechnical Commission, & Institute of Electrical and Electronics Engineers. (2018). *Systems and software engineering — Life cycle processes — Requirements engineering* (ISO/IEC/IEEE Standard No. 29148:2018, 2.ª ed.). https://doi.org/10.1109/IEEESTD.2018.8559686

Sevilla-Gonzalez, M. D. R., Moreno Loaeza, L., Lazaro-Carrera, L. S., Bourguet Ramirez, B., Vázquez Rodríguez, A., Peralta-Pedrero, M. L., y Almeda-Valdes, P. (2020). Spanish version of the System Usability Scale for the assessment of electronic tools: Development and validation. *JMIR Human Factors, 7*(4), Artículo e21161. https://doi.org/10.2196/21161

Washizaki, H. (Ed.). (2025). *Guide to the Software Engineering Body of Knowledge (SWEBOK Guide)* (versión 4.0a). IEEE Computer Society. https://www.computer.org/swebok

Las referencias de la normativa ecuatoriana y de las fuentes del problema son las de los capítulos I a III de la tesis.
