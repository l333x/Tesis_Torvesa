---
titulo: "Capítulo I · Introducción — parte 1 (contexto, empresa, problema, evidencias, delimitación y pregunta)"
version: "0.1"
fecha: 2026-10-19
autor_borrador: "Claude Opus 5.5 (Víctor edita)"
tarea: "S2-T01 (#13)"
base: "01_Borrador_Aprobado/2026-09-29_Diseno_Titulacion_APROBADO.md, secciones «Problema de estudio» 1–5"
word: "2026-10-19_Cap1_Introduccion_p1_v0.1.docx"
marcadores: "FALTA-FUENTE 3 · FALTA-DATO 8 · VERIFICAR-PÁG 1"
tags: [capitulo1, introduccion, borrador]
---

<!--
Versión para la IA. La de Víctor es el Word del mismo nombre.
Notación del control de cambios (la lee el generador del Word):
  texto sin marcas = texto del diseño aprobado que se conserva
  {+texto+}        = inserción de Claude (cambio con control)
  {-texto-}        = eliminación de Claude (cambio con control)
  {>>texto<<}      = comentario de Word sobre el fragmento anterior
  *texto*          = cursiva
-->

# CAPÍTULO I{>>Cómo revisar: el control de cambios ya está activado, así que lo que escribas queda marcado con tu nombre. Lo que agregó Claude aparece subrayado y lo que quitó, tachado; cada cambio importante tiene un comentario que explica por qué. Acepta o rechaza en Revisar › Aceptar / Rechazar. Lo resaltado en amarillo son marcadores ([FALTA-…]): no se borran hasta resolverlos. Guarda con otro nombre (v0.2) si quieres, no hace falta: Claude no sobrescribe este archivo.<<}

# INTRODUCCIÓN

## Contexto general

{+Desde 2021, el uso de la inteligencia artificial (IA) en las organizaciones ha crecido con rapidez. Según la encuesta global de McKinsey & Company, el 78 % de las organizaciones usaba IA en al menos una función del negocio a finales de 2024, frente al 55 % de un año antes, y el 71 % usaba IA generativa con regularidad; marketing y ventas está entre las funciones donde más se usa (Singla et al., 2025, pp. 14 y 16). Esa encuesta, sin embargo, refleja sobre todo a empresas grandes. La estadística oficial de la Organización para la Cooperación y el Desarrollo Económicos (OCDE) muestra otra realidad: entre 2020 y 2024, la proporción de empresas que usa IA en los países miembros pasó del 5,6 % al 14 %, y en las pequeñas empresas, de 10 a 49 empleados, llega apenas al 11,9 %, frente al 40 % de las grandes (OECD, 2025a, p. 6). La brecha no se cierra: en 2026, el 54 % de las organizaciones con ingresos anuales de al menos 1.000 millones de dólares escala la IA en toda la empresa, frente a un tercio de las más pequeñas (McKinsey & Company, 2026, sección «Key takeaways»).+}{>>Se citan juntas McKinsey (empresas grandes) y la OCDE (estadística oficial) para no exagerar la adopción, como pide la matriz (CTX-IA). El Stanford AI Index 2025 repite el mismo 78 % de la misma encuesta de McKinsey, así que no se presenta como una segunda prueba.<<}

{+La IA generativa abarató el acceso para las empresas pequeñas: el 31 % de las pymes encuestadas por la OCDE en siete países ya la usa (OECD, 2025b, p. 6). En el área comercial, el interés se explica por el uso del tiempo: los vendedores dedican solo el 30 % de su semana a vender, y tareas como priorizar prospectos, registrar datos y generar cotizaciones pueden automatizarse (Salesforce Research, 2024, p. 13).+}{>>Salesforce vende software de gestión de clientes (CRM): confianza media. Se usa como contexto, nunca como única prueba. La encuesta de la OCDE es de países desarrollados; no hay dato equivalente para América Latina.<<}

El sector {-económico -}de la construcción es uno de los menos digitalizados de la economía: el índice de digitalización industrial del McKinsey Global Institute{+, que comparó 22 sectores de Estados Unidos con datos de 2015,+} lo ubica en el penúltimo lugar{- entre los sectores analizados-}, solo por delante de la agricultura y la caza ({-Agarwal et al., 2016-}{+Manyika et al., 2015, p. 5+}).{>>El borrador aprobado citaba a Agarwal et al. (2016), que solo reproduce el índice. Se cita el original (Manyika et al., 2015, figura E2) y se aclara que es de EE. UU. y de 2015. Agarwal sale de las referencias de este capítulo.<<}{+ El dato es antiguo y de otro país, pero la evidencia reciente de América Latina apunta en la misma dirección: en Chile, el 68 % de las micro y pequeñas empresas de construcción está en las etapas iniciales de la digitalización, el porcentaje más alto entre los sectores analizados (Cathles et al., 2023, p. 5).+} Su lógica {+empresa a empresa (+}B2B{+)+}, su estructura fragmentada y su organización por proyectos frenan {-la adopción de tecnologías de gestión-}{+su transformación digital y le impiden recoger y aprovechar los datos de sus clientes+} (Samuelson y Stehn, 2023{+, p. 400+}{-; Nyqvist et al., 2024-}).{>>Nyqvist et al. (2024) todavía no está verificada: la editorial bloquea la descarga y está en tu lista de PDF a mano. Si al leerla respalda la idea, vuelve con su página.<<}{+ El freno no es la falta de inversión: entre 2020 y 2022 se invirtieron cerca de 50.000 millones de dólares en tecnología para la construcción, un 85 % más que en los tres años anteriores, pero la fragmentación, el bajo gasto en tecnología frente a otros sectores y las formas de trabajo analógicas siguen limitando su uso (McKinsey & Company, 2023) [VERIFICAR-PÁG: McKinsey & Company 2023 — confirmar si la cifra está en el texto o en la figura 1].+}

{+En Ecuador, la construcción sale de dos años de caída: su producción cayó 1,7 % en 2023 y 7,9 % en 2024, y en 2025 se recuperó con un crecimiento del 2,7 % (Banco Central del Ecuador [BCE], 2026, pp. 22–23). En un mercado que apenas se recupera, perder clientes por demoras en la atención pesa más. Al mismo tiempo, la IA ya forma parte del trabajo diario: en 2024, el 36 % de los trabajadores ecuatorianos encuestados por el portal Multitrabajos decía usarla en sus tareas (Redacción Empresas, 2024), y el Índice Latinoamericano de Inteligencia Artificial 2025 ubica al país en la categoría «adoptante», un nivel intermedio (Comisión Económica para América Latina y el Caribe [CEPAL], 2025). En las micro, pequeñas y medianas empresas (mipymes) ecuatorianas, en cambio, la IA se usa poco y sobre todo en marketing; las barreras principales son la falta de profesionales calificados y la falta de bases de datos estructuradas (Pérez-Campdesuñer et al., 2025, resumen).+}{>>Se usa la cifra del BCE (−7,9 %), no la de la prensa (−7,8 %), porque el BCE la revisó. Multitrabajos es un portal de empleo sin método publicado: confianza media. Pérez-Campdesuñer et al. (2025) es la mejor evidencia nacional y reciente: la «falta de bases de datos estructuradas» es justo el historial disperso de Torvesa.<<}

La Constructora Torvesa ilustra esta brecha: atiende a clientes que esperan respuestas rápidas, pero gestiona la relación comercial y la elaboración de cotizaciones con procesos manuales, y su personal comercial y técnico divide la jornada entre la oficina y obras con conectividad limitada ({-Bermeo y Segura, 2026-}{+[FALTA-DATO: confirmar con las entrevistas en Torvesa]+}).{>>Bermeo y Segura (2026) es el informe del proyecto integrador, y su diagnóstico usó datos simulados. La descripción se mantiene porque viene del conocimiento de la empresa, pero se confirma en las entrevistas antes de citarla.<<}

## La Constructora Torvesa

Torvesa Constructora es una sociedad {-con personería jurídica -}domiciliada en Quito (Pichincha) que inició actividades el 5 de agosto de 2010. Su actividad principal registrada es la construcción de carreteras, calles y otras vías para vehículos o peatones, y complementariamente ejecuta obras de ingeniería civil en general (Servicio de Rentas Internas [SRI], 2026){+ [FALTA-DATO: A1 — captura del RUC en el SRI con fecha y confirmación del giro por la empresa]+}.{>>El correo a Torvesa pregunta si además hacen edificación o venta de inmuebles, y qué parte de su trabajo es privada y qué parte pública. Si la respuesta cambia el giro, este párrafo cambia. Ojo: la frase siguiente habla de inmobiliarias y proyectos habitacionales, que no encajan del todo con «carreteras y calles».<<} Cuenta con 30 colaboradores{+ [FALTA-DATO: A2 — nota de respaldo firmada por la gerencia]+} entre personal administrativo, comercial y técnico, y atiende principalmente a clientes privados —empresas, inmobiliarias y promotores de proyectos habitacionales, y personas naturales— que solicitan cotizaciones de forma directa; según los registros de la empresa, su cartera actual es de 33 clientes{+ [FALTA-DATO: A3 — nota de respaldo o extracto anonimizado del registro de clientes]+}. Su oferta se vende por proyecto: cada solicitud exige una cotización o proforma a medida, cuyo detalle técnico —materiales, cantidades, rubros y plazos— hace que su elaboración dependa del conocimiento y del tiempo del vendedor que la prepara.

## Descripción del problema

El problema se expresa en el tiempo de respuesta al cliente. Cada solicitud de cotización obliga al vendedor a preparar la respuesta casi desde cero: buscar cotizaciones anteriores, recalcular rubros y armar el documento a partir de archivos dispersos y de su propia memoria. {-Según los registros de la empresa, la elaboración de cada cotización toma entre 30 y 44 minutos de trabajo del vendedor; como-}{+Cuánto tarda cada cotización todavía no se ha medido [FALTA-DATO: A4 — cronometraje de las cotizaciones en Torvesa (meta M2)]. Como+}{>>Los «30 a 44 minutos» del borrador no tienen fuente: no están en ningún registro verificado de la empresa. Se miden con cronómetro cuando Torvesa autorice el campo.<<} ese mismo vendedor reparte la jornada entre la oficina y la obra, {-ese tiempo-}{+la cotización+} solo puede {-dedicarse-}{+prepararse+} al volver a la oficina, y las solicitudes quedan sin atender durante horas o días{+ [FALTA-DATO: M1 — tiempo de respuesta real, con las solicitudes de los últimos tres meses]+}. A la lentitud se suma la falta de un historial: el conocimiento de cada cliente —qué pidió, qué se le ofreció, qué está pendiente— vive en el teléfono y en la memoria del vendedor asignado, y no existe un repositorio que la empresa conserve si ese vendedor está en obra sin señal o deja la organización. {-El diagnóstico denominó a este fenómeno-}{+En este trabajo, a ese fenómeno se le llama+} «amnesia institucional»{+ [FALTA-FUENTE: A8 — anclar el término en Pollitt (2000) y Galan (2023), PDF a mano]+}: el cliente debe repetir su historia o, en el peor caso, se va con la competencia.{>>«El diagnóstico denominó…» remitía al diagnóstico simulado. El término tiene origen en la literatura (Pollitt, 2000): cuando bajes el PDF, se cita ahí.<<}{+ El riesgo se repite a escala del sector: como cada proyecto reúne una combinación nueva de empresas, el conocimiento se transfiere con dificultad de un proyecto a otro (Samuelson y Stehn, 2023, p. 388).+}

Aumentar el personal o reorganizar las cargas de trabajo son decisiones de gestión que corresponden a la gerencia y no forman parte de este trabajo. El problema que aborda el proyecto es tecnológico: no existe una herramienta que conserve el conocimiento comercial de la empresa —historial de clientes, plantillas y cotizaciones anteriores— y que lo ponga a disposición del vendedor para responder en menos tiempo.

## Evidencias del problema

{+Un estudio publicado en *Harvard Business Review* encontró que +}{-Las-}{+las+} empresas que responden a un {-lead-}{+prospecto (*lead*)+} dentro de la primera hora tienen cerca de siete veces más probabilidades de calificarlo que las que tardan más{-, y más de sesenta veces más que las que esperan 24 horas o más-} (Oldroyd et al., 2011{+ [FALTA-FUENTE: A9 — confirmar «siete veces» con página en el PDF]+}).{>>El «más de sesenta veces» no aparece en ninguna descripción del artículo; solo RevenueHero (2024) se lo atribuye a la revista. Sale hasta abrir el PDF de Oldroyd (tu lista de esta noche). Si está, vuelve con página.<<}{+ El problema sigue vigente: en 2024, una prueba con clientes incógnitos en 1.000 empresas de software que venden a otras empresas encontró que 635 nunca respondieron a una solicitud de demostración (Koushik, 2024, sección de resultados). Mientras tanto, el 83 % de los clientes espera hablar con alguien de inmediato cuando contacta a una empresa (Salesforce Research, 2022, p. 16). Ninguna de estas dos fuentes es del sector de la construcción y las dos vienen de empresas que venden software comercial, por lo que se usan como contexto y no como prueba del caso de Torvesa.+}

{+La literatura revisada tampoco respalda un plazo exacto de respuesta, como una ventana de 5 a 15 minutos. Por eso, la meta de responder en menos de 15 minutos que se plantea en este trabajo es una decisión de diseño, que se justifica con los objetivos, y no un dato probado.+}{>>Corrección de A10: el borrador aprobado decía en el marco teórico que la ventana de referencia era de 5 a 15 minutos (Oldroyd et al., 2011). Ninguna fuente revisada lo prueba. Se dice así, sin maquillarlo.<<}

{-El diagnóstico previo aplicado a los 30 colaboradores de Torvesa (Bermeo y Segura, 2026) encontró que:-}{>>Todo este bloque sale: son los datos simulados del diagnóstico (N = 30), que no se usan (regla de la tesis). Se reemplaza con la línea base real cuando haya campo.<<}

- {-solo el 13,3 % de los primeros contactos ocurre dentro de 15 minutos, y el 23,3 % de los leads espera más de 24 horas;-}

- {-la etapa modal de pérdida del embudo es previa al primer contacto (30,0 %);-}

- {-el 50,0 % del equipo no encuentra información completa al buscar el historial de un cliente antiguo, y el 43,3 % no confía en poder retomar la cartera de un compañero ausente;-}

- {-el 36,7 % señala que las confirmaciones desde obra «a veces nunca llegan», y el 56,7 % de la comunicación urgente circula por canales no trazables;-}

- {-el «historial completo y centralizado del cliente» fue la función n.º 1 en el ranking forzado de prioridades (53,3 %);-}

- {-la versión inicial del sistema obtuvo un SUS de 53,83, por debajo del umbral normativo de 68 (Sauro, 2011; Lewis, 2018).-}

{+La situación de Torvesa se mide con una línea base real, levantada en la empresa: el tiempo de respuesta a las solicitudes, el tiempo de elaboración de cada cotización, la disponibilidad del historial de los clientes y la percepción de colaboradores y clientes [FALTA-DATO: línea base M1–M6, trabajo de campo en Torvesa]. Sus resultados se presentan en el capítulo IV.+}

## Delimitación del problema

El estudio se centra en tres procesos del área comercial de la Constructora Torvesa (Quito): la recepción de las solicitudes de los prospectos, la elaboración de la respuesta o cotización y la conservación del historial de cada cliente. Sobre el ecosistema TEAMSLASH (landing, API propia, PostgreSQL y alertas por Slack) se diseñan tres componentes: (a) una bóveda de conocimiento comercial en Obsidian con fichas de clientes, plantillas y cotizaciones anteriores; (b) un asistente de inteligencia artificial que consulta la bóveda y propone al vendedor un borrador de respuesta; y (c) un registro verificable de las interacciones{+, con huellas digitales (SHA-256) y un registro al que solo se pueden agregar entradas+}.{>>Decisión D6 (tutora sin objeciones, 12-oct): se quita OpenTimestamps (sello en Bitcoin) y se usa la huella SHA-256 con un registro que solo se puede ampliar.<<} La propuesta se valida con cuatro casos de prueba y {-un piloto de dos semanas de operación experimental-}{+una validación del diseño en operación experimental controlada de dos semanas+}.{>>Decisión D1: nunca «piloto». Según el cronograma, la validación va del 23 de noviembre al 5 de diciembre de 2026.<<}{+ El trabajo se desarrolla entre octubre de 2026 y enero de 2027.+}

## Planteamiento del problema

¿Cómo debe diseñarse un sistema de automatización que permita a la Constructora Torvesa responder a sus prospectos en el menor tiempo posible, dar continuidad a la atención con el vendedor titular y conservar un historial verificable de cada cliente?{>>Pregunta central sin cambios respecto al diseño aprobado. La parte 2 (mañana) sigue con la justificación, los objetivos y el alcance.<<}

## Referencias de esta parte (provisional)

{+Banco Central del Ecuador. (2026). *Informe de evolución de la economía ecuatoriana en 2025 y perspectivas 2026*. https://contenido.bce.fin.ec/documentos/Administracion/EvolEconEcu_2025pers2026.pdf+}

{+Cathles, A., Henríquez, P., y Suaznábar, C. (2023). *Impulsando la transformación digital de la construcción: el caso del BIM en Chile*. Banco Interamericano de Desarrollo. https://doi.org/10.18235/0004973+}

{+Comisión Económica para América Latina y el Caribe. (2025, 3 de octubre). *América Latina y el Caribe aceleran la adopción de la inteligencia artificial, aunque persisten desafíos en inversión, talento y gobernanza* [Comunicado de prensa]. https://www.cepal.org/en/pressreleases/latin-america-and-caribbean-accelerate-adoption-artificial-intelligence-though+}{>>El comunicado se leyó en inglés (es la URL de la ficha). Falta el enlace de la versión en español, que corresponde a este título, y el informe ILIA 2025 completo para tener el puntaje de Ecuador.<<}

{+Koushik, V. (2024, 20 de marzo). *We tested lead response times of 1000 B2B sales teams. Here are the results*. RevenueHero. https://www.revenuehero.io/blog/b2b-lead-response-times+}

{+Manyika, J., Ramaswamy, S., Khanna, S., Sarrazin, H., Pinkus, G., Sethupathy, G., y Yaffe, A. (2015). *Digital America: A tale of the haves and have-mores*. McKinsey Global Institute. https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/digital-america-a-tale-of-the-haves-and-have-mores+}

{+McKinsey & Company. (2023, 3 de mayo). *From start-up to scale-up: Accelerating growth in construction technology*. https://www.mckinsey.com/industries/private-capital/our-insights/from-start-up-to-scale-up-accelerating-growth-in-construction-technology+}

{+McKinsey & Company. (2026, 25 de agosto). *The state of AI: Global survey 2026*. https://www.mckinsey.com/capabilities/operations/our-insights/the-state-of-ai+}

{+OECD. (2025a). *AI adoption by small and medium-sized enterprises*. OECD Publishing. https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/12/ai-adoption-by-small-and-medium-sized-enterprises_9c48eae6/426399c1-en.pdf+}

{+OECD. (2025b). *Generative AI and the SME workforce: New survey evidence*. OECD Publishing. https://www.oecd.org/en/publications/generative-ai-and-the-sme-workforce_2d08b99d-en.html+}

{+Oldroyd, J. B., McElheran, K., y Elkington, D. (2011). The short life of online sales leads. *Harvard Business Review, 89*(3) [FALTA-FUENTE: páginas, al abrir el PDF].+}

{+Pérez-Campdesuñer, R., Sánchez-Rodríguez, A., García-Vidal, G., Martínez-Vivar, R., y De Miguel-Guzmán, M. (2025). Artificial intelligence in Ecuadorian SMEs: Drivers and obstacles to adoption. *Information, 16*(6), Artículo 443. https://doi.org/10.3390/info16060443+}

{+Redacción Empresas. (2024, 26 de febrero). *Tres de cada 10 ecuatorianos usaron IA en sus tareas diarias de trabajo*. Primicias. https://www.primicias.ec/nota/primicias-empresas/eco-naranja/el-36-de-ecuatorianos-uso-la-ia-en-sus-tareas-diarias-dentro-del-trabajo/+}

{+Salesforce Research. (2022). *State of the connected customer* (5.ª ed.). Salesforce. https://www.salesforce.com/content/dam/web/en_ie/www/PDF/state-of-connected-customer-fifth-ed-comp.pdf+}

{+Salesforce Research. (2024). *State of sales* (6.ª ed.). Salesforce. https://www.salesforce.com/sales/state-of-sales/+}

{+Samuelson, O., y Stehn, L. (2023). Digital transformation in construction – a review. *Journal of Information Technology in Construction, 28*, 385–404. https://doi.org/10.36680/j.itcon.2023.020+}

{+Servicio de Rentas Internas. (2026). *Consulta de RUC: Torvesa Constructora (RUC 1792266424001)* [Base de datos]. Recuperado el 28 de septiembre de 2026 de https://srienlinea.sri.gob.ec [FALTA-DATO: A1 — captura con fecha].+}

{+Singla, A., Sukharevsky, A., Yee, L., Chui, M., y Hall, B. (2025). *The state of AI: How organizations are rewiring to capture value*. McKinsey & Company. https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-how-organizations-are-rewiring-to-capture-value+}
