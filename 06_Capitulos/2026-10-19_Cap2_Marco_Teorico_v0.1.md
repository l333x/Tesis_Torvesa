---
titulo: "Capítulo II · Marco teórico (partes 1 y 2, con lo verificado al 19-oct)"
version: "0.1"
fecha: 2026-10-19
autor_borrador: "Claude Opus 5.5 (Víctor edita)"
tarea: "S2-T05 y S2-T07 (#14), adelantadas del 21 y 22-oct"
base: "Diseño aprobado (Marco teórico 1–4) + 37 fichas verificadas (7 nuevas del 19-oct)"
word: "2026-10-19_Cap2_Marco_Teorico_v0.1.docx"
marcadores: "FALTA-FUENTE 13 · DECIDIR-VÍCTOR 1"
tags: [capitulo2, marco_teorico, borrador]
---

<!--
Versión para la IA. La de Víctor es el Word del mismo nombre.
Texto nuevo (sin tachados): las diferencias con el diseño aprobado van en comentarios. Notación: {>>comentario<<} *cursiva*.
Regla: solo se cita lo verificado; lo del borrador aprobado sin verificar queda como [FALTA-FUENTE].
-->

# CAPÍTULO II{>>Capítulo II en v0.1, con lo verificado hasta hoy. Hoy se verificaron 7 fuentes nuevas para este capítulo: Rodriguez et al. (2025), Chatterjee et al. (2023), Wu et al. (2024), Böhm y Durst (2026), Stark (2024), Hyzy et al. (2022) y Hernández Vega et al. (2026). Lo que el diseño aprobado citaba sin verificar (Ohiomah, Habel, Alqershi, Gil-Gómez, Nonaka y Takeuchi, Walsh y Ungson, Lewis, Kleppmann, Dumas, Haber y Stornetta) queda marcado; no se cita hasta abrirlo.<<}

# MARCO TEÓRICO

Este capítulo reúne los antecedentes y las bases teóricas, legales y normativas del trabajo. Primero revisa los estudios recientes sobre la gestión comercial con apoyo tecnológico y sobre la inteligencia artificial en las ventas y en las pymes. Luego define los conceptos que sustentan el diseño del sistema: la gestión de clientes y de prospectos, el tiempo de respuesta, la gestión del conocimiento, la IA con recuperación de documentos propios y la usabilidad. Cierra con el marco legal ecuatoriano y una discusión crítica de los vacíos que este trabajo atiende.

## Antecedentes

### La gestión comercial con apoyo tecnológico

Los sistemas de gestión de la relación con el cliente (*customer relationship management*, CRM) se consideran una herramienta eficaz para identificar a los mejores clientes, aumentar su satisfacción y retenerlos; la capacidad de una organización en este campo se mide por cómo analiza los datos de sus clientes (Chatterjee et al., 2023, p. 1299). A medida que crece el volumen de esos datos, analizarlos a mano se vuelve difícil, y las empresas incorporan IA a sus sistemas de CRM. En una encuesta a 315 usuarios de organizaciones en India, la calidad del CRM con IA y la satisfacción con él influyeron en la actitud y en la intención de usarlo, mientras que la compatibilidad con los sistemas existentes pesó poco (Chatterjee et al., 2023, p. 1299). La lección para el diseño es que la adopción depende de que el usuario encuentre útil y satisfactoria la herramienta, y no solo de que esta se integre con lo que ya hay.

La calificación de prospectos es otra pieza de la gestión comercial. Una revisión sistemática de 44 estudios distingue dos enfoques: el tradicional, que depende de la experiencia y el conocimiento de los vendedores, y el predictivo, que usa datos y algoritmos de aprendizaje automático; el segundo tiene un impacto positivo en el desempeño de ventas (Wu et al., 2024, p. 69). En una empresa donde la información de los clientes está dispersa, solo es posible el enfoque tradicional: la calidad de la atención depende de lo que recuerda cada vendedor.

El diseño aprobado citaba además estudios sobre los sistemas de gestión de prospectos, el CRM móvil y el CRM en pymes [FALTA-FUENTE: A21 Ohiomah et al. (2019), A22 Habel et al. (2025), A23 Alqershi et al. (2020), A24 Rodriguez y Boyer (2020) y A25 Gil-Gómez et al. (2020) — abrir y verificar con página; los de 2020 o antes van con una fuente de 2021 en adelante].{>>Rodriguez y Boyer (2020) y Alqershi et al. (2020) son de acceso abierto, pero Springer y MDPI bloquean la descarga automática: van a tu lista de PDF a mano (5 minutos). Con ellos se completa este apartado en la v0.2.<<}

### La inteligencia artificial en las ventas

La evidencia académica sobre IA generativa en ventas es reciente. En una empresa de salud que la incorporó a su proceso de ventas, el uso de IA generativa por 163 vendedores se relacionó de forma positiva con la eficacia del proceso de ventas (β = 0,487), con la eficiencia administrativa (β = 0,484) y con el desempeño en ventas (β = 0,274), y el apoyo de la alta gerencia favoreció su uso (Rodriguez et al., 2025, p. 20). Los autores explican el efecto por el tiempo que se libera: la IA generativa ayuda a preparar propuestas, actualizar el CRM y redactar notas de las reuniones con clientes, y así el vendedor dedica más tiempo a vender (Rodriguez et al., 2025, p. 14). Los informes de la industria apuntan en la misma dirección: los vendedores dedican solo el 30 % de su semana a vender, y tareas como generar cotizaciones pueden automatizarse (Salesforce Research, 2024, p. 13).{>>Rodriguez et al. (2025) se leyó en el manuscrito aceptado (repositorio de Kansas State University): la página es la del manuscrito. Antes de la versión final, confirmar la página de la revista (pp. 2013–2027) o citar la sección.<<}

Esta evidencia tiene límites. El estudio de Rodriguez et al. (2025) analiza una sola empresa y se basa en lo que los vendedores declaran, como reconocen sus autores (Rodriguez et al., 2025, resumen), y los informes de la industria provienen de empresas que venden software comercial. Las predicciones también llaman a la cautela: Gartner (2025) proyecta que para 2028 habrá diez veces más agentes de IA que vendedores, pero que menos del 40 % de los vendedores dirá que esos agentes mejoraron su productividad.{>>Gartner es una predicción, no un dato medido: se dice así. Es un comunicado de prensa (confianza media).<<}

### La inteligencia artificial en las pymes de América Latina y del Ecuador

En las pymes latinoamericanas, la adopción de IA sigue siendo incipiente, aunque empiezan a usar herramientas sin código, IA generativa y análisis predictivo; las barreras más comunes son la falta de talento, de financiamiento y de cultura digital (Hernández Vega et al., 2026, p. 1080). En el Ecuador, un estudio con 385 mipymes encontró que la IA se usa poco y sobre todo en marketing, y que los obstáculos más críticos son la falta de profesionales calificados y la falta de bases de datos estructuradas (Pérez-Campdesuñer et al., 2025). En los países de la OCDE, la proporción de pequeñas empresas que usa IA es del 11,9 %, frente al 40 % de las grandes (OECD, 2025a, p. 6). La brecha no es solo de herramientas: sin datos ordenados, la IA no tiene de dónde aprender ni qué consultar.{>>Hernández Vega et al. (2026) es de una revista nueva y de bajo impacto (confianza media) y tiene una inconsistencia (28 o 25 estudios), así que no se da el número. Se usa solo para el contexto regional, junto con Pérez-Campdesuñer et al. (2025).<<}

### La transformación digital de la construcción

La construcción es uno de los sectores menos digitalizados (Manyika et al., 2015, p. 5; Cathles et al., 2023, p. 5). Una revisión de la literatura identifica dos condiciones que frenan su transformación digital: su orientación empresa a empresa, que limita el diálogo directo con el cliente y el uso de sus datos, y su organización fragmentada y por proyectos (Samuelson y Stehn, 2023, p. 400). Como cada proyecto reúne una combinación nueva de empresas, el conocimiento se transfiere con dificultad de un proyecto a otro (Samuelson y Stehn, 2023, p. 388). Este trabajo atiende esa transferencia dentro de una sola empresa: que lo aprendido con cada cliente quede disponible para la siguiente cotización.

## Bases teóricas

### Gestión de la relación con el cliente y gestión de prospectos

El CRM es una estrategia apoyada en tecnología para registrar, dar seguimiento y retener a los clientes, cuyo valor depende de la calidad de los datos que reúne (Chatterjee et al., 2023, p. 1299). La gestión de prospectos (*lead management*) es la parte del CRM que va desde que una persona o empresa muestra interés hasta que se convierte en cliente, e incluye la calificación de cada prospecto según su probabilidad de compra (Wu et al., 2024, p. 69). En el CRM móvil, estas funciones se llevan al celular del vendedor, lo que permite atender desde el campo [FALTA-FUENTE: A24 y A26 — definición de CRM móvil, Rodriguez y Boyer (2020) y una revisión reciente].

### Tiempo de respuesta al prospecto

El tiempo de respuesta, o *speed-to-lead*, es el tiempo entre el ingreso de una solicitud y el primer contacto de la empresa. Un estudio publicado en *Harvard Business Review* encontró que las empresas que responden dentro de la primera hora tienen cerca de siete veces más probabilidades de calificar al prospecto [FALTA-FUENTE: A9 — Oldroyd et al. (2011), PDF a mano]. Los clientes, además, esperan inmediatez: el 83 % espera hablar con alguien de inmediato al contactar a una empresa (Salesforce Research, 2022, p. 16), y el 67 % de los compradores entre empresas prefiere informarse sin un vendedor (Gartner, 2026). Si el comprador llega a la empresa ya informado, lo que espera es una respuesta concreta y rápida, como una cotización. Ninguna de las fuentes revisadas fija un plazo exacto; por eso la meta de 15 minutos de este trabajo es una decisión de diseño.{>>Corrección frente al diseño aprobado: decía «la ventana de referencia es de 5 a 15 minutos (Oldroyd et al., 2011)». Oldroyd habla de la primera hora; los 5 minutos vendrían de otro estudio (Elkington y MIT, 2007), que no se ha verificado. Se dice así, sin maquillarlo. Gartner (2026) es un comunicado de prensa con 646 compradores, sobre todo de EE. UU. y Europa.<<}

### Gestión del conocimiento y memoria organizacional

La gestión del conocimiento estudia cómo las organizaciones crean, guardan, comparten y usan lo que saben. Su modelo más difundido es el SECI de Nonaka y Takeuchi, que explica la creación de conocimiento como una conversión continua entre el conocimiento tácito, el que la persona sabe pero no ha escrito, y el explícito, el que está registrado, en cuatro fases: socialización, externalización, combinación e internalización (Böhm y Durst, 2026, pp. 107–108). La fase clave para este trabajo es la externalización: convertir el conocimiento interiorizado en información codificada, de modo que exista independientemente de quien lo tiene (Böhm y Durst, 2026, p. 110). Eso es lo que hace una ficha de cliente: saca de la memoria del vendedor lo que pidió el cliente, lo que se le ofreció y lo que está pendiente. [FALTA-FUENTE: Nonaka y Takeuchi (1995) como origen — biblioteca UPS]{>>Böhm y Durst (2026) es de 2026 (VINE, CC BY): actualiza el SECI y lo relaciona con la IA generativa. Es la fuente 2021+ que pide la regla de la tesis para acompañar a Nonaka y Takeuchi (1995).<<}

Cuando el conocimiento no se externaliza, la organización lo pierde con la rotación del personal. La literatura llama a este fenómeno *amnesia institucional*: la incapacidad de una organización de recordar y usar el conocimiento del pasado, que se considera propia de toda organización grande por la rotación y el cambio constantes (Stark, 2024, p. 3). El concepto nació en el estudio del sector público y de las organizaciones grandes; en este trabajo se adapta a la memoria comercial de una pyme, donde la salida de un solo vendedor puede llevarse el historial de varios clientes. La memoria de una organización se guarda en distintos lugares, y los depósitos formales, como los archivos y los sistemas, son el terreno propio de la gestión del conocimiento (Stark, 2024, p. 4). [FALTA-FUENTE: Pollitt (2000) como origen del término y Walsh y Ungson (1991) para la memoria organizacional]

La IA generativa abre una vía nueva para la externalización: puede transformar datos y conocimiento tácito en documentos, informes o narrativas que otros miembros de la organización pueden usar (Böhm y Durst, 2026, p. 110). Pero todavía falla al dar explicaciones concisas o referencias precisas (Böhm y Durst, 2026, p. 110), lo que justifica que sus respuestas se apoyen en documentos propios y verificables de la empresa.

### Inteligencia artificial con recuperación de información

La generación aumentada por recuperación (*retrieval-augmented generation*, RAG) combina un modelo de lenguaje con la búsqueda de documentos propios de la organización: antes de responder, el sistema recupera los documentos relevantes y la respuesta se apoya en ellos [FALTA-FUENTE: A37 — Lewis et al. (2020) como origen del término y un estudio de 2023 en adelante sobre la reducción de errores con RAG]. En la industria, esta tecnología todavía está en una etapa temprana: en un estudio con 13 profesionales que la aplican, 12 calificaron sus casos de uso por debajo del nivel 7 de madurez tecnológica, es decir, en desarrollo o prototipo y no en uso a gran escala (Brehme et al., 2025, p. 10). En este trabajo, el asistente consulta la bóveda —fichas de clientes, plantillas y cotizaciones anteriores— y propone al vendedor un borrador de respuesta, que el vendedor revisa antes de enviarlo.{>>Brehme et al. (2025) es un preprint (arXiv); se dice así en la referencia. Lo de «el vendedor revisa antes de enviar» es una decisión de diseño que viene del diseño aprobado (Anexo A).<<}

### Software que funciona sin conexión

Las aplicaciones que guardan los datos primero en el dispositivo y los sincronizan después permiten trabajar sin conexión y no dependen de un proveedor externo [FALTA-FUENTE: A38 — Kleppmann et al. (2019), *Local-first software* (Diego)]. Este principio justifica el uso de Obsidian, cuyas fichas son archivos de texto que el vendedor puede consultar en la obra aunque no tenga señal.

### Gestión de procesos de negocio

La gestión de procesos de negocio (BPM) modela cómo se hace hoy el trabajo (AS-IS) y cómo se hará con el sistema (TO-BE), con la notación BPMN [FALTA-FUENTE: Dumas et al. (2018) o una fuente oficial de BPMN — Diego, CTX-PROC]. En este trabajo se modela el flujo de captación, asignación, aviso, primer contacto, cotización y traspaso de un cliente.

### Registro verificable

Para comprobar que el historial comercial no se alteró, cada documento se identifica con una huella digital (SHA-256): cualquier cambio en el documento cambia su huella. Las huellas se guardan en un registro al que solo se pueden agregar entradas, de modo que una alteración posterior se nota al comparar la huella guardada con la del documento [FALTA-FUENTE: estándar SHA-256 (NIST FIPS 180-4) y Haber y Stornetta (1991) para el encadenamiento de registros]. A diferencia de una cadena de bloques pública, este registro no requiere criptomonedas ni servicios externos, y en él no se guardan datos personales.{>>Decisión D6 (tutora sin objeciones): sin OpenTimestamps ni Bitcoin. Por eso sale la afirmación A30 («¿necesita una blockchain?», Wüst y Gervais, 2018) y la A35 (Todd, 2016). La norma del SHA-256 es pública (NIST): la verifico mañana.<<}

### Aceptación tecnológica y usabilidad

La adopción de una herramienta depende de que el usuario la encuentre útil y satisfactoria (Chatterjee et al., 2023, p. 1299). Para medir la usabilidad se usa la Escala de Usabilidad del Sistema (*System Usability Scale*, SUS), de diez preguntas, con un puntaje de 0 a 100. Su valor de referencia es una media de 68 (DE 12,5), que surge de 446 estudios y 5.000 respuestas: la mitad de los productos queda por encima de ese valor y la mitad por debajo (Hyzy et al., 2022, p. 2). Un metaanálisis reciente con 114 aplicaciones confirmó que ese valor sigue siendo adecuado (Hyzy et al., 2022, p. 1). La versión en español de la escala está validada (Sevilla-Gonzalez et al., 2020).{>>Con Hyzy et al. (2022) la afirmación A20 (umbral de 68) queda respaldada sin esperar el PDF bloqueado de Lewis y Sauro (2018). Ojo: 68 es un promedio de referencia, no un «aprobado». La meta M6 dice «igual o superior a 68», que significa «al menos en el promedio».<<}

## Bases legales y normativas

- Ley Orgánica de Protección de Datos Personales (LOPDP, 2021) y su Reglamento General (Decreto Ejecutivo 904, 2023). El tratamiento de datos debe tener una base legal, como el consentimiento del titular (art. 7); el consentimiento debe ser libre, específico, informado e inequívoco, y se puede revocar (art. 8); los datos se conservan solo el tiempo necesario para su finalidad (art. 10, lit. i); y el titular debe ser informado de los fines, la base legal, el tiempo de conservación y sus derechos (art. 12). En el sistema, estas reglas se aplican al formulario de captación, a la minimización de datos en la bóveda, al control de acceso y a la anonimización de los datos del estudio.

- Ley de Comercio Electrónico, Firmas Electrónicas y Mensajes de Datos (2002): da validez jurídica a los mensajes de datos usados en la captación y el seguimiento [FALTA-FUENTE: A44 — verificar el texto en el Registro Oficial].

- Uso de IA en las organizaciones: en el Ecuador, el 70 % de las organizaciones no tiene una regulación interna para la IA, y el 33 % de los empleados usa cuentas personales de IA para tareas de trabajo (Revelo, 2026). Por eso el sistema incluye una política de uso del asistente.{>>Revelo (2026) es una nota de prensa (Primicias) que cita informes de GMS y ESET sin muestra: confianza media. Falta buscar el informe original de GMS.<<}

## Discusión crítica

La literatura coincide en que la tecnología mejora la gestión comercial cuando el usuario la acepta y la encuentra útil (Chatterjee et al., 2023), y en que la IA generativa libera tiempo de tareas administrativas como preparar propuestas (Rodriguez et al., 2025). La gestión del conocimiento agrega una condición: la tecnología solo conserva el conocimiento si el trabajo diario obliga a externalizarlo (Böhm y Durst, 2026). De la revisión surgen tres vacíos:

- La evidencia sobre IA en ventas se basa sobre todo en percepciones declaradas por los vendedores y en empresas grandes o de un solo sector; casi no se miden tiempos reales registrados por el sistema (Rodriguez et al., 2025, resumen).

- Los estudios sobre IA en pymes latinoamericanas y ecuatorianas miden su adopción con encuestas, pero no evalúan herramientas concretas en una empresa, y no se encontraron estudios en pymes constructoras (Hernández Vega et al., 2026; Pérez-Campdesuñer et al., 2025) [FALTA-FUENTE: A28 — documentar la búsqueda en SciELO, Redalyc y el repositorio UPS sin resultados].

- El uso de IA con recuperación de documentos propios sigue en etapa de prototipo en la industria (Brehme et al., 2025), y casi no se ha estudiado para acelerar la elaboración de cotizaciones en pymes [FALTA-FUENTE: A29 — misma búsqueda documentada].

Este trabajo se ubica en esa intersección: diseña y valida, con tiempos registrados por el sistema, una herramienta que conserva el conocimiento comercial de una pyme constructora ecuatoriana y lo pone a disposición del vendedor con apoyo de IA.

[DECIDIR-VÍCTOR: el diseño aprobado tenía un antecedente local (el diagnóstico de Bermeo y Segura, 2026). Como sus datos eran simulados, sale. ¿Se menciona el proyecto integrador TEAMSLASH como antecedente propio, sin cifras?]

## Referencias de este capítulo (provisional)

Asamblea Nacional del Ecuador. (2021, 26 de mayo). *Ley Orgánica de Protección de Datos Personales*. Registro Oficial Quinto Suplemento n.º 459.

Böhm, K., y Durst, S. (2026). Knowledge management in the age of generative artificial intelligence – from SECI to GRAI. *VINE Journal of Information and Knowledge Management Systems, 56*(1), 106–121. https://doi.org/10.1108/VJIKMS-10-2024-0357

Brehme, L., Dornauer, B., Ströhle, T., Ehrhart, M., y Breu, R. (2025). *Retrieval-augmented generation in industry: An interview study on use cases, requirements, challenges, and evaluation* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2508.14066

Cathles, A., Henríquez, P., y Suaznábar, C. (2023). *Impulsando la transformación digital de la construcción: el caso del BIM en Chile*. Banco Interamericano de Desarrollo. https://doi.org/10.18235/0004973

Chatterjee, S., Rana, N. P., Khorana, S., Mikalef, P., y Sharma, A. (2023). Assessing organizational users' intentions and behavior to AI integrated CRM systems: A meta-UTAUT approach. *Information Systems Frontiers, 25*(4), 1299–1313. https://doi.org/10.1007/s10796-021-10181-1

Gartner. (2025, 18 de noviembre). *Gartner predicts by 2028 AI agents will outnumber sellers by 10X—yet fewer than 40% of sellers will report AI agents improved their productivity* [Comunicado de prensa].

Gartner. (2026, 9 de marzo). *Gartner sales survey finds 67% of B2B buyers prefer a rep-free experience* [Comunicado de prensa].

Hernández Vega, O., Parra Almada, C. G., y De la Rosa Flores, C. C. (2026). La inteligencia artificial en las pymes: una revisión de literatura para América Latina. *Ciencia y Reflexión, 5*(1), 1080–1098. https://doi.org/10.70747/cr.v5i1.713

Hyzy, M., Bond, R., Mulvenna, M., Bai, L., Dix, A., Leigh, S., y Hunt, S. (2022). System Usability Scale benchmarking for digital health apps: Meta-analysis. *JMIR mHealth and uHealth, 10*(8), Artículo e37290. https://doi.org/10.2196/37290

Manyika, J., Ramaswamy, S., Khanna, S., Sarrazin, H., Pinkus, G., Sethupathy, G., y Yaffe, A. (2015). *Digital America: A tale of the haves and have-mores*. McKinsey Global Institute.

OECD. (2025a). *AI adoption by small and medium-sized enterprises*. OECD Publishing.

Pérez-Campdesuñer, R., Sánchez-Rodríguez, A., García-Vidal, G., Martínez-Vivar, R., y De Miguel-Guzmán, M. (2025). Artificial intelligence in Ecuadorian SMEs: Drivers and obstacles to adoption. *Information, 16*(6), Artículo 443. https://doi.org/10.3390/info16060443

Revelo, R. (2026, 16 de septiembre). *El peligro de la «Shadow AI»: el 33 % de empleados en Ecuador usa IA personal en el trabajo*. Primicias.

Rodriguez, M., Deeter-Schmelz, D. R., y Krush, M. T. (2025). The impact of generative AI technology on B2B sales process and performance: An empirical study. *Journal of Business & Industrial Marketing, 40*(10), 2013–2027. https://doi.org/10.1108/JBIM-02-2025-0097

Salesforce Research. (2022). *State of the connected customer* (5.ª ed.). Salesforce.

Salesforce Research. (2024). *State of sales* (6.ª ed.). Salesforce.

Samuelson, O., y Stehn, L. (2023). Digital transformation in construction – a review. *Journal of Information Technology in Construction, 28*, 385–404. https://doi.org/10.36680/j.itcon.2023.020

Sevilla-Gonzalez, M. D. R., Moreno Loaeza, L., Lazaro-Carrera, L. S., Bourguet Ramirez, B., Vázquez Rodríguez, A., Peralta-Pedrero, M. L., y Almeda-Valdes, P. (2020). Spanish version of the System Usability Scale for the assessment of electronic tools: Development and validation. *JMIR Human Factors, 7*(4), Artículo e21161. https://doi.org/10.2196/21161

Stark, A. (2024). Institutional amnesia in government: How much is enough? *Policy Quarterly, 20*(1), 3–9. https://doi.org/10.26686/pq.v20i1.9046

Wu, M., Andreev, P., y Benyoucef, M. (2024). The state of lead scoring models and their impact on sales performance. *Information Technology and Management, 25*(1), 69–98. https://doi.org/10.1007/s10799-023-00388-w
