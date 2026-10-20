---
titulo: "Capítulo I · Introducción — parte 2 (justificación, objetivos, preguntas, metas y alcance)"
version: "0.2"
fecha: 2026-10-20
autor_borrador: "Claude Opus 5.5 (Víctor edita)"
tarea: "S2-T03 (#13), adelantada del 20-oct"
base: "01_Borrador_Aprobado/2026-09-29_Diseno_Titulacion_APROBADO.md: Justificación, Objetivos, Preguntas orientadoras, Metas y Alcance"
word: "2026-10-20_Cap1_Introduccion_p2_v0.2.docx"
base_v02: "v0.1 aprobada por Víctor el 20-oct (cambios aceptados) + búsqueda documentada A28/A29"
marcadores: "FALTA-FUENTE 7 · FALTA-DATO 7 · DECIDIR-TUTORA 1"
tags: [capitulo1, introduccion, borrador]
---

<!--
Versión para la IA. La de Víctor es el Word del mismo nombre.
Notación: inserción *cursiva*. El texto sin marcas es el del diseño aprobado.
-->

## Justificación

### Relevancia práctica

El estudio responde a una necesidad concreta de la empresa: un historial centralizado del cliente. La bóveda convierte el conocimiento que hoy reside en la memoria de cada vendedor en un activo de la empresa: si el vendedor está en obra sin señal, consulta la ficha del cliente desde su celular, y si deja la organización, el historial de trabajo con cada cliente queda en la empresa. Las plantillas y las cotizaciones anteriores, consultadas por el asistente de IA, reducen el tiempo de preparar cada respuesta, y la información acumulada permite generar reportes para la gerencia sobre clientes, cotizaciones y tiempos de atención. Además, el registro verificable da a la gerencia una prueba de quién atendió a cada cliente, qué se le ofreció y cuándo, útil para resolver discrepancias con clientes y para asignar el mérito comercial entre vendedores. El registro controlado de los datos contribuye también al cumplimiento de la Ley Orgánica de Protección de Datos Personales (LOPDP), que exige, entre otras cosas, el consentimiento del titular y conservar los datos solo el tiempo necesario (LOPDP, 2021, arts. 8 y 10, lit. i).

### Relevancia académica

La evidencia sobre la gestión de clientes con apoyo tecnológico (CRM, por sus siglas en inglés) móvil proviene casi siempre de empresas grandes o de ventas internas en economías desarrolladas, y se basa en percepciones autorreportadas (Ohiomah et al., 2019; Rodriguez y Boyer, 2020; Habel et al., 2025) [FALTA-FUENTE: A21, A22 y A24 — abrir los tres artículos y verificar con página]. Este trabajo aporta una medición basada en registros del sistema en una pyme constructora latinoamericana. Los estudios recientes sobre IA en pymes ecuatorianas miden su adopción con encuestas, pero no evalúan herramientas concretas en una empresa (Pérez-Campdesuñer et al., 2025), y el uso de IA con recuperación de documentos propios (RAG) sigue, en la industria, en etapa de prototipo: 12 de 13 casos estudiados no habían llegado a un uso a gran escala (Brehme et al., 2025, p. 10).{+ En la búsqueda realizada en SciELO, Redalyc, el repositorio de la UPS y OpenAlex (2021–2026) no se encontraron estudios sobre CRM o IA para la atención comercial en pymes constructoras latinoamericanas: lo más cercano aplica inteligencia de negocios a sus compras públicas (Peña-Ramírez et al., 2024), y la IA con recuperación de documentos ya se ha probado para redactar propuestas en empresas, pero no en pymes de la región ni midiendo el tiempo de respuesta (Bakiyalakshmi et al., 2026).+}{>>Vacíos A28 y A29 con búsqueda documentada (20-oct). Víctor aprobó las frases nuevas.<<} Además, articula dos campos que suelen estudiarse por separado: la gestión de prospectos y la gestión del conocimiento y la memoria organizacional (Nonaka y Takeuchi, 1995; Walsh y Ungson, 1991) [FALTA-FUENTE: clásicos de gestión del conocimiento — verificar en la biblioteca UPS y sumar una fuente de 2021 en adelante].

### Viabilidad del estudio

El estudio es viable porque: (a) la línea base se levanta en la empresa con la autorización de la gerencia [FALTA-DATO: autorización del trabajo de campo]; (b) el producto mínimo viable de TEAMSLASH está desplegado y la bóveda se construye sobre él sin licencias, ya que Obsidian es gratuito para uso comercial [FALTA-FUENTE: A31 — página oficial de licencias de Obsidian, con fecha] y la sincronización puede hacerse con Git; (c) se cuenta con la carta de autorización de la Constructora Torvesa, que permite usar sus datos, y con el tema aprobado por la carrera; (d) el registro verificable usa huellas digitales SHA-256 y un registro al que solo se pueden agregar entradas, que no requiere servicios externos, criptomonedas ni contratos inteligentes; y (e) el asistente de IA usa un servicio de modelos de lenguaje con un costo por consumo acotado durante la validación del diseño en operación experimental controlada [FALTA-FUENTE: A36 — precios oficiales del proveedor elegido].

### Impacto esperado

Con una correcta adopción por parte de la empresa —que no depende de este trabajo—, se proyecta reducir el tiempo de primer contacto por debajo de 15 minutos, acortar la elaboración de las cotizaciones mediante plantillas y respuestas asistidas, y lograr que cualquier miembro del equipo recupere el historial de un cliente en minutos, aunque el vendedor titular cambie. La validación del diseño en operación experimental controlada, de dos semanas, aportará una primera evidencia de ese efecto; sus resultados sustentarán la decisión de Torvesa sobre la adopción definitiva.

## Objetivos

### Objetivo general

Diseñar un sistema de automatización para la gestión comercial de la Constructora Torvesa, que integre el CRM móvil TEAMSLASH con una bóveda de conocimiento comercial en Obsidian, un asistente de inteligencia artificial para la elaboración de respuestas y cotizaciones y un registro verificable de eventos, y validarlo mediante una validación del diseño en operación experimental controlada de dos semanas que mida su efecto sobre el tiempo de respuesta, la continuidad de la atención y la trazabilidad del historial de cada cliente.

### Objetivos específicos

- OE1. Diagnosticar los procesos actuales de captación, cotización y atención de clientes (AS-IS) y establecer la línea base de tiempos de respuesta, fuga, capacidad de recuperar información y usabilidad, incluida la percepción de los clientes.

- OE2. Diseñar la arquitectura y los procesos objetivo (TO-BE) del sistema —bóveda de conocimiento, asistente de IA con plantillas de cotización y registro verificable—, con requisitos funcionales, análisis de viabilidad técnica y económica para Torvesa (valor actual neto y tasa interna de retorno), y controles conforme a la LOPDP.

- OE3. Desarrollar un prototipo funcional de los componentes del sistema mediante sprints incrementales sobre la infraestructura existente de TEAMSLASH.

- OE4. Validar el diseño del sistema mediante cuatro casos de prueba y una validación del diseño en operación experimental controlada de dos semanas, midiendo los indicadores definidos frente a la línea base.

- OE5. Documentar el manual de operación, los lineamientos de gobierno de la información y la transferencia al equipo de Torvesa.

### Relación con los objetivos vinculados al aprendizaje

La Tabla 1 muestra a qué objetivo vinculado al aprendizaje (OVA) de la carrera responde cada objetivo específico.

- OE1 (diagnóstico): OVA 4.1, identificar y analizar problemas complejos; OVA 5.1, analizar datos de desempeño organizacional.

- OE2 (diseño): OVA 4.2, formular alternativas de solución fundamentadas; OVA 6.2, evaluar la viabilidad técnica y económica; OVA 6.3, aplicar principios de seguridad y normativa digital.

- OE3 (desarrollo del prototipo): OVA 4.3, aplicar métodos y herramientas de la profesión; OVA 6.1, desarrollar soluciones digitales innovadoras.

- OE4 (validación): OVA 5.4, evaluar el impacto de la gestión digital mediante indicadores clave de desempeño.

- OE5 (documentación y transferencia): OVA 5.3, proponer planes de implementación considerando recursos, cronograma y gestión de riesgos.

## Preguntas orientadoras

En un proyecto técnico no se formula una hipótesis. En su lugar se plantean preguntas orientadoras y metas de validación que guían el desarrollo y la evaluación del sistema.

- PO1. ¿Qué pasos del proceso actual provocan demoras y pérdida de información entre la oficina y la obra?

- PO2. ¿Qué información mínima deben contener la ficha del cliente y las plantillas de cotización para que el vendedor —o quien lo reemplace si deja la empresa— responda sin reconstruir la historia del cliente?

- PO3. ¿Qué reglas de asignación, alerta y seguimiento garantizan que ninguna solicitud quede sin respuesta?

- PO4. ¿Cómo garantizar que el historial comercial no pueda alterarse sin que se note, sin exponer datos personales?

## Metas de validación

- M1. Mediana del tiempo de primer contacto menor a 15 minutos. Es una meta de diseño, no un estándar probado (véase la sección de evidencias); la línea base se mide en la empresa [FALTA-DATO: M1 — línea base real].

- M2. Reducción del tiempo de elaboración de una cotización con el asistente de IA frente a la línea base, medida en los casos de prueba [FALTA-DATO: M2 — cronometraje de cotizaciones].

- M3. Fuga previa al primer contacto menor que la de la línea base [FALTA-DATO: M3 — tasa de fuga medida con las solicitudes reales].

- M4. En la prueba de recuperación, menor tiempo y más aciertos que en la línea base, y menos colaboradores que no encuentran información completa o que no confían en retomar una cartera ajena [FALTA-DATO: M4 — encuesta I1, preguntas A5 y A6].

- M5. El 100 % de las alteraciones simuladas del registro detectadas por la verificación de integridad.

- M6. Puntaje SUS igual o superior a 68, medido con la versión validada en español (Sevilla-Gonzalez et al., 2020) [FALTA-FUENTE: A20 — el umbral de 68, Lewis y Sauro (2018), PDF a mano].

## Alcance

- Temático: diseño y validación del sistema: captación, primer contacto, elaboración asistida de respuestas y cotizaciones, continuidad de la atención con el vendedor titular, bóveda de conocimiento, registro verificable y usabilidad, aplicados a los clientes privados de la empresa. No se abordan la negociación, la facturación, la ejecución de obra ni las decisiones de gestión del personal (dotación y asignación de cargas), que corresponden a la gerencia; tampoco los procesos de contratación pública, que se rigen por los plazos y formatos del Sistema Nacional de Contratación Pública.

- Geográfico: Constructora Torvesa, Quito, Ecuador.

- Temporal: de octubre de 2026 a enero de 2027, dentro del Período 69. La validación del diseño en operación experimental controlada dura dos semanas, del 23 de noviembre al 5 de diciembre de 2026, y el documento final se entrega para revisión el 4 de enero de 2027.

- Poblacional: los 30 colaboradores de Torvesa, sus 33 clientes [FALTA-DATO: A2 y A3 — nota de respaldo de la gerencia] y la totalidad de las solicitudes que ingresen durante la validación.

- Metodológico: enfoque mixto con predominio cuantitativo, dentro de la investigación en ciencia del diseño (DSR), con una comparación antes y después en un solo grupo durante la validación del diseño en operación experimental controlada.

- Limitaciones: (a) caso único sin grupo de control, sin generalización ni causalidad estricta; (b) la línea base es parcialmente autorreportada; (c) población pequeña, por lo que se usan pruebas no paramétricas; (d) posible efecto Hawthorne; (e) Obsidian no ofrece permisos por usuario dentro de una bóveda, lo que se mitiga con minimización de datos y control de dispositivos (Anexo A) [FALTA-FUENTE: A33 — documentación oficial de Obsidian sobre permisos]; (f) el registro verificable prueba que un evento no fue alterado desde su fecha, pero no que su contenido haya sido verdadero al registrarse; (g) la evaluación financiera del modelo SaaS va como anexo de contexto y no es objeto del proyecto; (h) la versión en español de la SUS se validó en México y con herramientas de salud, no en el sector de la construcción (Sevilla-Gonzalez et al., 2020); y (i) si en las dos semanas de validación entran pocas solicitudes, las pruebas estadísticas pierden potencia, y los resultados se informan como descriptivos [FALTA-DATO: volumen de solicitudes por semana en Torvesa].

[DECIDIR-TUTORA: el párrafo final con la estructura del documento se escribe al cerrar la tesis (sprint 9), como pide el manual de estilo]

## Referencias de esta parte (provisional)

Asamblea Nacional del Ecuador. (2021, 26 de mayo). *Ley Orgánica de Protección de Datos Personales*. Registro Oficial Quinto Suplemento n.º 459.

{+Bakiyalakshmi, S., Sanjay, C., y Sriram, D. (2026). Retrieval augmented generation with LLMs for enterprise proposal automation. *ITM Web of Conferences, 85*, Artículo 02007. https://doi.org/10.1051/itmconf/20268502007+}

Brehme, L., Dornauer, B., Ströhle, T., Ehrhart, M., y Breu, R. (2025). *Retrieval-augmented generation in industry: An interview study on use cases, requirements, challenges, and evaluation* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2508.14066

{+Peña-Ramírez, C., Espinoza-Brito, L., Forcael, E., Garcés, G., y Cea, C. (2024). Leveraging business intelligence for strategic growth: A case study of small and medium-sized enterprises (SMEs) in the construction industry. *Ingeniare. Revista chilena de ingeniería, 32*, 39. https://doi.org/10.4067/s0718-33052024000100240+}

Pérez-Campdesuñer, R., Sánchez-Rodríguez, A., García-Vidal, G., Martínez-Vivar, R., y De Miguel-Guzmán, M. (2025). Artificial intelligence in Ecuadorian SMEs: Drivers and obstacles to adoption. *Information, 16*(6), Artículo 443. https://doi.org/10.3390/info16060443

Sevilla-Gonzalez, M. D. R., Moreno Loaeza, L., Lazaro-Carrera, L. S., Bourguet Ramirez, B., Vázquez Rodríguez, A., Peralta-Pedrero, M. L., y Almeda-Valdes, P. (2020). Spanish version of the System Usability Scale for the assessment of electronic tools: Development and validation. *JMIR Human Factors, 7*(4), Artículo e21161. https://doi.org/10.2196/21161

Sin verificar todavía (no se citan en la versión final hasta abrirlas): Habel et al. (2025); Nonaka y Takeuchi (1995); Ohiomah et al. (2019); Rodriguez y Boyer (2020); Walsh y Ungson (1991). [FALTA-FUENTE: cinco referencias del diseño aprobado]
