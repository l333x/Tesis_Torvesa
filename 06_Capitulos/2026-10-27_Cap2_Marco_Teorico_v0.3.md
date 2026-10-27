---
titulo: "Capítulo II · Marco teórico (partes 1 y 2, con lo verificado al 20-oct)"
version: "0.3"
fecha: 2026-10-27
autor_borrador: "Claude Opus 5.5 (Víctor edita)"
tarea: "S2-T05 y S2-T07 (#14), adelantadas del 21 y 22-oct"
base: "v0.1 aprobada por Víctor el 20-oct (cambios aceptados) + 40 fichas verificadas (3 nuevas del 20-oct) + DEC-17 + búsqueda documentada A28/A29"
word: "2026-10-27_Cap2_Marco_Teorico_v0.3.docx"
base_v03: "v0.2 (20-oct) sin ediciones de Víctor, con sus cambios aceptados + cambios del reporte F1 del 21-oct + fichas de Diego del 25-oct (Béchard, Magesh, OMG, Martínez Mendoza, Radhakrishnan). Solo lo del 27-oct va marcado."
marcadores: "FALTA-FUENTE 6 · FALTA-DATO 1"
tags: [capitulo2, marco_teorico, borrador]
---

<!--
Versión para la IA. La de Víctor es el Word del mismo nombre.
Texto nuevo (sin tachados): las diferencias con el diseño aprobado van en comentarios. Notación: *cursiva*.
Regla: solo se cita lo verificado; lo del borrador aprobado sin verificar queda como [FALTA-FUENTE].
-->

# CAPÍTULO II

# MARCO TEÓRICO

Este capítulo reúne los antecedentes y las bases teóricas, legales y normativas del trabajo. Primero revisa los estudios recientes sobre la gestión comercial con apoyo tecnológico y sobre la inteligencia artificial en las ventas y en las pymes. Luego define los conceptos que sustentan el diseño del sistema: la gestión de clientes y de prospectos, el tiempo de respuesta, la gestión del conocimiento, la IA con recuperación de documentos propios y la usabilidad. Cierra con el marco legal ecuatoriano y una discusión crítica de los vacíos que este trabajo atiende.

## Antecedentes

### La gestión comercial con apoyo tecnológico

Los sistemas de gestión de la relación con el cliente (*customer relationship management*, CRM) se consideran una herramienta eficaz para identificar a los mejores clientes, aumentar su satisfacción y retenerlos; la capacidad de una organización en este campo se mide por cómo analiza los datos de sus clientes (Chatterjee et al., 2023, p. 1299). A medida que crece el volumen de esos datos, analizarlos a mano se vuelve difícil, y las empresas incorporan IA a sus sistemas de CRM. En una encuesta a 315 usuarios de organizaciones en India, la calidad del CRM con IA y la satisfacción con él influyeron en la actitud y en la intención de usarlo, mientras que la compatibilidad con los sistemas existentes pesó poco (Chatterjee et al., 2023, p. 1299). La lección para el diseño es que la adopción depende de que el usuario encuentre útil y satisfactoria la herramienta, y no solo de que esta se integre con lo que ya hay.

La calificación de prospectos es otra pieza de la gestión comercial. Una revisión sistemática de 44 estudios distingue dos enfoques: el tradicional, que depende de la experiencia y el conocimiento de los vendedores, y el predictivo, que usa datos y algoritmos de aprendizaje automático; el segundo tiene un impacto positivo en el desempeño de ventas (Wu et al., 2024, p. 69). En una empresa donde la información de los clientes está dispersa, solo es posible el enfoque tradicional: la calidad de la atención depende de lo que recuerda cada vendedor.

{+En las pymes, el efecto del CRM depende de qué parte de él se aplica. En 284 pymes manufactureras de Yemen, el enfoque en clientes clave y el CRM basado en tecnología mejoraron el desempeño, la organización del CRM no tuvo un efecto directo, y el capital relacional reforzó el efecto del CRM tecnológico y de su organización (AlQershi et al., 2020, pp. 9–12). Gil-Gomez et al. (2020) proponen, además, considerar el CRM una herramienta crítica para innovar el modelo de negocio de las pymes (p. 2733), aunque su modelo todavía no se ha comprobado con datos (p. 2745).+}{>>A23: la evidencia contradice el diseño aprobado, que decía que «solo las dimensiones tecnológica y organizativa» afectan el desempeño. En el efecto directo, la organización del CRM no es significativa (Tabla 5, p. 9); «tecnológica y organizativa» son las dimensiones en que modera el capital relacional (p. 12). Se corrige, no se maquilla. A25 es un artículo conceptual: «proponen», nunca «demuestran».<<}

El diseño aprobado citaba además estudios sobre los sistemas de gestión de prospectos{- , el CRM móvil y el CRM en pymes-}{+ y el CRM móvil+} [FALTA-FUENTE: A21 Ohiomah et al. (2019), A22 Habel et al. (2025){-, A23 Alqershi et al. (2020)-}{+ y+} A24 Rodriguez y Boyer (2020){- y A25 Gil-Gómez et al. (2020)-} — {+son de pago: biblioteca UPS; +}abrir y verificar con página; los de 2020 o antes van con una fuente de 2021 en adelante].

### La inteligencia artificial en las ventas

La evidencia académica sobre IA generativa en ventas es reciente. En una empresa de salud que la incorporó a su proceso de ventas, el uso de IA generativa por 163 vendedores se relacionó de forma positiva con la eficacia del proceso de ventas (β = 0,487), con la eficiencia administrativa (β = 0,484) y con el desempeño en ventas (β = 0,274), y el apoyo de la alta gerencia favoreció su uso (Rodriguez et al., 2025, p. 20). Los autores explican el efecto por el tiempo que se libera: la IA generativa ayuda a preparar propuestas, actualizar el CRM y redactar notas de las reuniones con clientes, y así el vendedor dedica más tiempo a vender (Rodriguez et al., 2025, p. 14). Los informes de la industria apuntan en la misma dirección: los vendedores dedican solo el 30 % de su semana a vender, y tareas como generar cotizaciones pueden automatizarse (Salesforce Research, 2024, p. 13).

Esta evidencia tiene límites. El estudio de Rodriguez et al. (2025) analiza una sola empresa y se basa en lo que los vendedores declaran, como reconocen sus autores (Rodriguez et al., 2025, resumen), y los informes de la industria provienen de empresas que venden software comercial. Las predicciones también llaman a la cautela: Gartner (2025) proyecta que para 2028 habrá diez veces más agentes de IA que vendedores, pero que menos del 40 % de los vendedores dirá que esos agentes mejoraron su productividad.

### La inteligencia artificial en las pymes de América Latina y del Ecuador

En las pymes latinoamericanas, la adopción de IA sigue siendo incipiente, aunque empiezan a usar herramientas sin código, IA generativa y análisis predictivo; las barreras más comunes son la falta de talento, de financiamiento y de cultura digital (Hernández Vega et al., 2026, p. 1080). En el Ecuador, un estudio con 385 mipymes encontró que la IA se usa poco y sobre todo en marketing, y que los obstáculos más críticos son la falta de profesionales calificados y la falta de bases de datos estructuradas (Pérez-Campdesuñer et al., 2025). En los países de la OCDE, la proporción de pequeñas empresas que usa IA es del 11,9 %, frente al 40 % de las grandes (OECD, 2025a, p. 6). La brecha no es solo de herramientas: sin datos ordenados, la IA no tiene de dónde aprender ni qué consultar.

### Antecedente propio: el proyecto integrador TEAMSLASH

En el proyecto integrador de la carrera, los autores desarrollaron TEAMSLASH, un ecosistema digital de gestión de clientes para la Constructora Torvesa: un formulario web capta la solicitud del prospecto, una API propia en Node.js la valida y la registra, y una notificación en Slack avisa al equipo comercial en obra (Bermeo y Segura, 2026, p. 5). Este trabajo parte de ese producto y le agrega la bóveda de conocimiento, el asistente de IA y el registro verificable. No se usan las cifras de su diagnóstico, porque eran simuladas.

### La transformación digital de la construcción

La construcción es uno de los sectores menos digitalizados (Manyika et al., 2015, p. 5; Cathles et al., 2023, p. 5). Una revisión de la literatura identifica dos condiciones que frenan su transformación digital: su orientación empresa a empresa, que limita el diálogo directo con el cliente y el uso de sus datos, y su organización fragmentada y por proyectos (Samuelson y Stehn, 2023, p. 400). Como cada proyecto reúne una combinación nueva de empresas, el conocimiento se transfiere con dificultad de un proyecto a otro (Samuelson y Stehn, 2023, p. 388). Este trabajo atiende esa transferencia dentro de una sola empresa: que lo aprendido con cada cliente quede disponible para la siguiente cotización.

## Bases teóricas

### Gestión de la relación con el cliente y gestión de prospectos

El CRM es una estrategia apoyada en tecnología para registrar, dar seguimiento y retener a los clientes, cuyo valor depende de la calidad de los datos que reúne (Chatterjee et al., 2023, p. 1299). La gestión de prospectos (*lead management*) es la parte del CRM que va desde que una persona o empresa muestra interés hasta que se convierte en cliente, e incluye la calificación de cada prospecto según su probabilidad de compra (Wu et al., 2024, p. 69). En el CRM móvil, estas funciones se llevan al celular del vendedor, lo que permite atender desde el campo [FALTA-FUENTE: A24 y A26 — definición de CRM móvil, Rodriguez y Boyer (2020) y una revisión reciente].

### Tiempo de respuesta al prospecto

El tiempo de respuesta, o *speed-to-lead*, es el tiempo entre el ingreso de una solicitud y el primer contacto de la empresa. Un estudio publicado en *Harvard Business Review* encontró que las empresas que responden dentro de la primera hora tienen cerca de siete veces más probabilidades de calificar al prospecto [FALTA-FUENTE: A9 — Oldroyd et al. (2011), PDF a mano]. Los clientes, además, esperan inmediatez: el 83 % espera hablar con alguien de inmediato al contactar a una empresa (Salesforce Research, 2022, p. 16), y el 67 % de los compradores entre empresas prefiere informarse sin un vendedor (Gartner, 2026). Si el comprador llega a la empresa ya informado, lo que espera es una respuesta concreta y rápida, como una cotización. Ninguna de las fuentes revisadas fija un plazo exacto; por eso la meta de 15 minutos de este trabajo es una decisión de diseño.

### Gestión del conocimiento y memoria organizacional

La gestión del conocimiento estudia cómo las organizaciones crean, guardan, comparten y usan lo que saben. Su modelo más difundido es el SECI de Nonaka y Takeuchi, que explica la creación de conocimiento como una conversión continua entre el conocimiento tácito, el que la persona sabe pero no ha escrito, y el explícito, el que está registrado, en cuatro fases: socialización, externalización, combinación e internalización (Böhm y Durst, 2026, pp. 107–108). La fase clave para este trabajo es la externalización: convertir el conocimiento interiorizado en información codificada, de modo que exista independientemente de quien lo tiene (Böhm y Durst, 2026, p. 110). Eso es lo que hace una ficha de cliente: saca de la memoria del vendedor lo que pidió el cliente, lo que se le ofreció y lo que está pendiente. [FALTA-FUENTE: Nonaka y Takeuchi (1995) como origen — biblioteca UPS]

Cuando el conocimiento no se externaliza, la organización lo pierde con la rotación del personal. La literatura llama a este fenómeno *amnesia institucional*: la incapacidad de una organización de recordar y usar el conocimiento del pasado, que se considera propia de toda organización grande por la rotación y el cambio constantes (Stark, 2024, p. 3). El concepto nació en el estudio del sector público y de las organizaciones grandes; en este trabajo se adapta a la memoria comercial de una pyme, donde la salida de un solo vendedor puede llevarse el historial de varios clientes. La memoria de una organización se guarda en distintos lugares, y los depósitos formales, como los archivos y los sistemas, son el terreno propio de la gestión del conocimiento (Stark, 2024, p. 4). [FALTA-FUENTE: Pollitt (2000) como origen del término y Walsh y Ungson (1991) para la memoria organizacional]

La IA generativa abre una vía nueva para la externalización: puede transformar datos y conocimiento tácito en documentos, informes o narrativas que otros miembros de la organización pueden usar (Böhm y Durst, 2026, p. 110). Pero todavía falla al dar explicaciones concisas o referencias precisas (Böhm y Durst, 2026, p. 110), lo que justifica que sus respuestas se apoyen en documentos propios y verificables de la empresa.

### Inteligencia artificial con recuperación de información

La generación aumentada por recuperación (*retrieval-augmented generation*, RAG) combina un modelo de lenguaje con la búsqueda de documentos propios de la organización: antes de responder, el sistema recupera los documentos relevantes y la respuesta se apoya en ellos {-[FALTA-FUENTE: A37 — Lewis et al. (2020) como origen del término y un estudio de 2023 en adelante sobre la reducción de errores con RAG]-}{+(Lewis et al., 2020, p. 9459). Quienes propusieron el término observaron que estos modelos inventan menos datos que un modelo sin recuperación (Lewis et al., 2020, p. 9464). La evidencia reciente lo confirma, con un límite: en una aplicación empresarial, la recuperación redujo los elementos inventados de hasta el 21 % a menos del 7,5 % (Béchard y Marquez Ayala, 2024, p. 233), pero no los elimina; herramientas comerciales de consulta jurídica basadas en RAG todavía se equivocaron entre el 17 % y el 33 % de las veces (Magesh et al., 2025, p. 216)+}. En la industria, esta tecnología todavía está en una etapa temprana: en un estudio con 13 profesionales que la aplican, 12 calificaron sus casos de uso por debajo del nivel 7 de madurez tecnológica, es decir, en desarrollo o prototipo y no en uso a gran escala (Brehme et al., 2025, p. 10). En este trabajo, el asistente consulta la bóveda —fichas de clientes, plantillas y cotizaciones anteriores— y propone al vendedor un borrador de respuesta, que el vendedor revisa antes de enviarlo{+, precisamente porque la recuperación reduce los errores, pero no los elimina+}.

### Software que funciona sin conexión

Las aplicaciones que guardan {-los datos primero en el dispositivo y los sincronizan después permiten trabajar sin conexión y no dependen de un proveedor externo [FALTA-FUENTE: A38 — Kleppmann et al. (2019), *Local-first software* (Diego)]-}{+la copia principal de los datos en el dispositivo (*local-first*) permiten leerlos y modificarlos en cualquier momento, incluso sin conexión, y los sincronizan cuando vuelve la red (Kleppmann et al., 2019, p. 157)+}. Este principio justifica el uso de Obsidian, cuyas fichas son archivos de texto que el vendedor puede consultar en la obra aunque no tenga señal.

### Gestión de procesos de negocio

La gestión de procesos de negocio (BPM) modela cómo se hace hoy el trabajo (AS-IS) y cómo se hará con el sistema (TO-BE), con la notación BPMN{+, un estándar pensado para que lo entiendan tanto las personas del negocio como las técnicas (Object Management Group, 2013, p. 1). En pymes se ha usado para documentar procesos que no tenían registros de operación (Martínez Mendoza et al., 2023, p. 4836) y para pasar del proceso actual al mejorado (Radhakrishnan, 2025)+} {-[FALTA-FUENTE: Dumas et al. (2018) o una fuente oficial de BPMN — Diego, CTX-PROC]-}.{>>CTX-PROC: fichas verificadas por la IA de Diego el 25-oct (omg_2013, mendoza_2024b, radhakrishnan_2025). La norma BPMN es de 2013 y sigue vigente; va con fuentes de 2023 y 2025. De Radhakrishnan (2025) solo se verificó el resumen.<<} En este trabajo se modela el flujo de captación, asignación, aviso, primer contacto, cotización y traspaso de un cliente.

### Registro verificable

Para comprobar que el historial comercial no se alteró, cada documento se identifica con una huella digital (SHA-256): cualquier cambio en el documento cambia su huella. Las huellas se guardan en un registro al que solo se pueden agregar entradas, de modo que una alteración posterior se nota al comparar la huella guardada con la del documento (National Institute of Standards and Technology [NIST], 2015, p. iv) [FALTA-FUENTE: Haber y Stornetta (1991) para el encadenamiento de registros]. A diferencia de una cadena de bloques pública, este registro no requiere criptomonedas ni servicios externos, y en él no se guardan datos personales.

### Aceptación tecnológica y usabilidad

La adopción de una herramienta depende de que el usuario la encuentre útil y satisfactoria (Chatterjee et al., 2023, p. 1299). Para medir la usabilidad se usa la Escala de Usabilidad del Sistema (*System Usability Scale*, SUS), de diez preguntas, con un puntaje de 0 a 100. Su valor de referencia es una media de 68 (DE 12,5), que surge de 446 estudios y 5.000 respuestas: la mitad de los productos queda por encima de ese valor y la mitad por debajo (Hyzy et al., 2022, p. 2). Un metaanálisis reciente con 114 aplicaciones confirmó que ese valor sigue siendo adecuado (Hyzy et al., 2022, p. 1). La versión en español de la escala está validada (Sevilla-Gonzalez et al., 2020).

## Bases legales y normativas

- Ley Orgánica de Protección de Datos Personales (LOPDP, 2021) y su Reglamento General (Decreto Ejecutivo 904, 2023). El tratamiento de datos debe tener una base legal, como el consentimiento del titular (art. 7); el consentimiento debe ser libre, específico, informado e inequívoco, y se puede revocar (art. 8); los datos se conservan solo el tiempo necesario para su finalidad (art. 10, lit. i); y el titular debe ser informado de los fines, la base legal, el tiempo de conservación y sus derechos (art. 12). En el sistema, estas reglas se aplican al formulario de captación, a la minimización de datos en la bóveda, al control de acceso y a la anonimización de los datos del estudio.

- Ley de Comercio Electrónico, Firmas {-Electrónicas -}y Mensajes de Datos (2002): da {-validez jurídica a los mensajes de datos usados en la captación y el seguimiento [FALTA-FUENTE: A44 — verificar el texto en el Registro Oficial]-}{+a los mensajes de datos el mismo valor jurídico que a los documentos escritos (Ley de Comercio Electrónico, Firmas y Mensajes de Datos, 2002, art. 2), lo que respalda los registros de la captación y el seguimiento. Su artículo 9, sobre protección de datos, fue derogado por la LOPDP en 2021, por lo que los datos personales se rigen solo por esta última+}.{>>A44: verificada el 21-oct con el texto codificado publicado por ARCOTEL (última reforma, 7-feb-2023). El nombre oficial no dice «Firmas Electrónicas».<<}

- Uso de IA en las organizaciones: en el Ecuador, el 70 % de las organizaciones no tiene una regulación interna para la IA, y el 33 % de los empleados usa cuentas personales de IA para tareas de trabajo (Revelo, 2026). Por eso el sistema incluye una política de uso del asistente.

## Discusión crítica

La literatura coincide en que la tecnología mejora la gestión comercial cuando el usuario la acepta y la encuentra útil (Chatterjee et al., 2023), y en que la IA generativa libera tiempo de tareas administrativas como preparar propuestas (Rodriguez et al., 2025). La gestión del conocimiento agrega una condición: la tecnología solo conserva el conocimiento si el trabajo diario obliga a externalizarlo (Böhm y Durst, 2026). De la revisión surgen tres vacíos:

- La evidencia sobre IA en ventas se basa sobre todo en percepciones declaradas por los vendedores y en empresas grandes o de un solo sector; casi no se miden tiempos reales registrados por el sistema (Rodriguez et al., 2025, resumen).

- Los estudios sobre IA en pymes latinoamericanas y ecuatorianas miden su adopción con encuestas, pero no evalúan herramientas concretas en una empresa (Hernández Vega et al., 2026; Pérez-Campdesuñer et al., 2025). En la búsqueda realizada en SciELO, Redalyc, el repositorio de la UPS y OpenAlex (2021–2026) no se encontraron estudios sobre CRM o IA para la atención comercial en pymes constructoras latinoamericanas; el trabajo más cercano aplica inteligencia de negocios a las compras públicas de pymes constructoras chilenas (Peña-Ramírez et al., 2024).

- La IA con recuperación de documentos propios ya se ha probado para redactar propuestas comerciales en empresas (Bakiyalakshmi et al., 2026) y en la industria sigue en etapa de prototipo (Brehme et al., 2025); no se encontraron estudios que la apliquen a cotizaciones en pymes latinoamericanas ni que midan su efecto en el tiempo de respuesta.

Este trabajo se ubica en esa intersección: diseña y valida, con tiempos registrados por el sistema, una herramienta que conserva el conocimiento comercial de una pyme constructora ecuatoriana y lo pone a disposición del vendedor con apoyo de IA.

## Referencias de este capítulo (provisional)

{+AlQershi, N., Mokhtar, S. S. M., y Abas, Z. B. (2020). Innovative CRM and performance of SMEs: The moderating role of relational capital. *Journal of Open Innovation: Technology, Market, and Complexity, 6*(4), Artículo 155. https://doi.org/10.3390/joitmc6040155+}

Asamblea Nacional del Ecuador. (2021, 26 de mayo). *Ley Orgánica de Protección de Datos Personales*. Registro Oficial Quinto Suplemento n.º 459.

Bakiyalakshmi, S., Sanjay, C., y Sriram, D. (2026). Retrieval augmented generation with LLMs for enterprise proposal automation. *ITM Web of Conferences, 85*, Artículo 02007. https://doi.org/10.1051/itmconf/20268502007

{+Béchard, P., y Marquez Ayala, O. (2024). Reducing hallucination in structured outputs via retrieval-augmented generation. En Y. Yang, A. Davani, A. Sil y A. Kumar (Eds.), *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 6: Industry Track)* (pp. 228–238). Association for Computational Linguistics. https://doi.org/10.18653/v1/2024.naacl-industry.19+}

Bermeo, D., y Segura, V. (2026). *TEAMSLASH: Ecosistema digital de gestión de clientes para la Constructora Torvesa* [Informe final del proyecto integrador, Universidad Politécnica Salesiana]. [FALTA-DATO: confirmar con la carrera si se cita como trabajo no publicado]

Böhm, K., y Durst, S. (2026). Knowledge management in the age of generative artificial intelligence – from SECI to GRAI. *VINE Journal of Information and Knowledge Management Systems, 56*(1), 106–121. https://doi.org/10.1108/VJIKMS-10-2024-0357

Brehme, L., Dornauer, B., Ströhle, T., Ehrhart, M., y Breu, R. (2025). *Retrieval-augmented generation in industry: An interview study on use cases, requirements, challenges, and evaluation* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2508.14066

Cathles, A., Henríquez, P., y Suaznábar, C. (2023). *Impulsando la transformación digital de la construcción: el caso del BIM en Chile*. Banco Interamericano de Desarrollo. https://doi.org/10.18235/0004973

Chatterjee, S., Rana, N. P., Khorana, S., Mikalef, P., y Sharma, A. (2023). Assessing organizational users' intentions and behavior to AI integrated CRM systems: A meta-UTAUT approach. *Information Systems Frontiers, 25*(4), 1299–1313. https://doi.org/10.1007/s10796-021-10181-1

Gartner. (2025, 18 de noviembre). *Gartner predicts by 2028 AI agents will outnumber sellers by 10X—yet fewer than 40% of sellers will report AI agents improved their productivity* [Comunicado de prensa].

Gartner. (2026, 9 de marzo). *Gartner sales survey finds 67% of B2B buyers prefer a rep-free experience* [Comunicado de prensa].

{+Gil-Gomez, H., Guerola-Navarro, V., Oltra-Badenes, R., y Lozano-Quilis, J. A. (2020). Customer relationship management: Digital transformation and sustainable business model innovation. *Economic Research-Ekonomska Istraživanja, 33*(1), 2733–2750. https://doi.org/10.1080/1331677X.2019.1676283+}

Hernández Vega, O., Parra Almada, C. G., y De la Rosa Flores, C. C. (2026). La inteligencia artificial en las pymes: una revisión de literatura para América Latina. *Ciencia y Reflexión, 5*(1), 1080–1098. https://doi.org/10.70747/cr.v5i1.713

Hyzy, M., Bond, R., Mulvenna, M., Bai, L., Dix, A., Leigh, S., y Hunt, S. (2022). System Usability Scale benchmarking for digital health apps: Meta-analysis. *JMIR mHealth and uHealth, 10*(8), Artículo e37290. https://doi.org/10.2196/37290

{+Kleppmann, M., Wiggins, A., van Hardenberg, P., y McGranaghan, M. (2019). Local-first software: You own your data, in spite of the cloud. En *Proceedings of the 2019 ACM SIGPLAN International Symposium on New Ideas, New Paradigms, and Reflections on Programming and Software* (pp. 154–178). ACM. https://doi.org/10.1145/3359591.3359737+}

{+Ley de Comercio Electrónico, Firmas y Mensajes de Datos [Ley 67]. (2002, 17 de abril). Registro Oficial Suplemento 557. Última reforma: 7 de febrero de 2023.+}

{+Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., y Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *Advances in Neural Information Processing Systems, 33*, 9459–9474.+}

{+Magesh, V., Surani, F., Dahl, M., Suzgun, M., Manning, C. D., y Ho, D. E. (2025). Hallucination-free? Assessing the reliability of leading AI legal research tools. *Journal of Empirical Legal Studies, 22*(2), 216–242. https://doi.org/10.1111/jels.12413+}

Manyika, J., Ramaswamy, S., Khanna, S., Sarrazin, H., Pinkus, G., Sethupathy, G., y Yaffe, A. (2015). *Digital America: A tale of the haves and have-mores*. McKinsey Global Institute.

{+Martínez Mendoza, E., Jiménez Antonio, D., y Fernández Echeverría, E. (2023). Definición y mejora de procesos en ausencia de registros de operación. *Ciencia Latina Revista Científica Multidisciplinar, 7*(6), 4836–4852. https://doi.org/10.37811/cl_rcm.v7i6.9039+}

National Institute of Standards and Technology. (2015). *Secure Hash Standard (SHS)* (FIPS PUB 180-4). U.S. Department of Commerce. https://doi.org/10.6028/NIST.FIPS.180-4

{+Object Management Group. (2013). *Business Process Model and Notation (BPMN), version 2.0.2* (OMG Document No. formal/2013-12-09). https://www.omg.org/spec/BPMN/2.0.2/PDF+}

OECD. (2025a). *AI adoption by small and medium-sized enterprises*. OECD Publishing.

Peña-Ramírez, C., Espinoza-Brito, L., Forcael, E., Garcés, G., y Cea, C. (2024). Leveraging business intelligence for strategic growth: A case study of small and medium-sized enterprises (SMEs) in the construction industry. *Ingeniare. Revista chilena de ingeniería, 32*, 39. https://doi.org/10.4067/s0718-33052024000100240

Pérez-Campdesuñer, R., Sánchez-Rodríguez, A., García-Vidal, G., Martínez-Vivar, R., y De Miguel-Guzmán, M. (2025). Artificial intelligence in Ecuadorian SMEs: Drivers and obstacles to adoption. *Information, 16*(6), Artículo 443. https://doi.org/10.3390/info16060443

{+Radhakrishnan, U. (2025). Documenting SME processes with conversational AI: From tacit knowledge to BPMN. *IET Conference Proceedings, 2025*(28), 69–74. https://doi.org/10.1049/icp.2025.3640+}

Revelo, R. (2026, 16 de septiembre). *El peligro de la «Shadow AI»: el 33 % de empleados en Ecuador usa IA personal en el trabajo*. Primicias.

Rodriguez, M., Deeter-Schmelz, D. R., y Krush, M. T. (2025). The impact of generative AI technology on B2B sales process and performance: An empirical study. *Journal of Business & Industrial Marketing, 40*(10), 2013–2027. https://doi.org/10.1108/JBIM-02-2025-0097

Salesforce Research. (2022). *State of the connected customer* (5.ª ed.). Salesforce.

Salesforce Research. (2024). *State of sales* (6.ª ed.). Salesforce.

Samuelson, O., y Stehn, L. (2023). Digital transformation in construction – a review. *Journal of Information Technology in Construction, 28*, 385–404. https://doi.org/10.36680/j.itcon.2023.020

Sevilla-Gonzalez, M. D. R., Moreno Loaeza, L., Lazaro-Carrera, L. S., Bourguet Ramirez, B., Vázquez Rodríguez, A., Peralta-Pedrero, M. L., y Almeda-Valdes, P. (2020). Spanish version of the System Usability Scale for the assessment of electronic tools: Development and validation. *JMIR Human Factors, 7*(4), Artículo e21161. https://doi.org/10.2196/21161

Stark, A. (2024). Institutional amnesia in government: How much is enough? *Policy Quarterly, 20*(1), 3–9. https://doi.org/10.26686/pq.v20i1.9046

Wu, M., Andreev, P., y Benyoucef, M. (2024). The state of lead scoring models and their impact on sales performance. *Information Technology and Management, 25*(1), 69–98. https://doi.org/10.1007/s10799-023-00388-w
