---
titulo: "Guía para la reunión con la gerencia de Torvesa: cómo presentar la propuesta"
version: v0.1
fecha: 2026-11-10
autor_borrador: "Claude Opus 5.5 (frente B); Víctor y Diego revisan"
base: "02_Fuentes/Metodologia (subramanian_2026, influenceatwork_sf) · 06_Capitulos/2026-11-10_Necesidad_Contexto_FODA_v0.1.md · Proceso estrella v0.1 · Resumen de la prueba de concepto (8-nov)"
marcadores: "VERIFICAR-PÁG 4 · FALTA-DATO 2 · DECIDIR-VÍCTOR 2"
uso: "Material de trabajo para la reunión con el Ing. Torres. No va en la tesis; como mucho, en el anexo del modelo de negocio"
tags: [negociacion, gerencia, torvesa, pitch, sprint5]
---

# Guía para la reunión con la gerencia de Torvesa

> [!summary] En tres frases
> 1. La meta de la reunión no es «vender un sistema». Es conseguir **tres sí pequeños**: dos semanas de validación, las fechas y horas de 3 meses de solicitudes (sin datos de clientes) y los datos para el aviso de privacidad.
> 2. Se gana mostrando el problema con los números de la propia empresa y el sistema funcionando en vivo, no con presión.
> 3. Si dice que no, hay un plan B que no detiene la tesis.

> [!warning] Reglas de la reunión
> - Solo cifras con fuente. Si no hay fuente, se dice «no lo sabemos todavía; lo medimos en la validación».
> - Nunca se dice «piloto» ni «implementado». Se dice **«validación del diseño en operación experimental controlada»**, o en la conversación, «una prueba controlada de dos semanas».
> - Nada de urgencia falsa («solo hoy», «últimos cupos»). La persuasión es honesta o no sirve: el gerente va a seguir tratando con nosotros.

## 1. Qué técnica usamos y para qué

| Técnica | Idea central | Cómo la usamos con Torvesa | Fuente |
|---|---|---|---|
| Negociación por principios (Fisher y Ury) | Separar a las personas del problema; hablar de **intereses**, no de posiciones; buscar opciones de beneficio mutuo; usar criterios objetivos | El interés del gerente no es «tener un sistema», es no perder clientes y saber qué pasa con ellos. El criterio objetivo: minutos hasta el primer contacto | Fisher, Ury y Patton [VERIFICAR-PÁG: *Getting to Yes*]; concepto de BATNA en Subramanian (2026) |
| BATNA (mejor alternativa si no hay acuerdo) | Saber qué hacemos si dice que no, con alternativas reales | Nuestro plan B (sección 7) y el suyo: seguir igual o contratar un CRM comercial | Subramanian (2026) |
| SPIN (Rackham) | Preguntas en cuatro pasos: Situación, Problema, Implicación y Necesidad de solución | El gerente llega solo a la conclusión de que el problema cuesta (sección 3) | Rackham [VERIFICAR-PÁG: *SPIN Selling*] |
| Venta con enseñanza (*Challenger*, Dixon y Adamson) | Llevar una idea nueva que cambie cómo el cliente ve su problema | «Torvesa no pierde clientes en la obra; los pierde en la primera hora» | Dixon y Adamson [VERIFICAR-PÁG: *The Challenger Sale*] |
| Empatía táctica (Voss) | Nombrar la emoción del otro, preguntas abiertas que empiezan con «cómo» o «qué», adelantarse a lo negativo | «Seguramente piensa que esto es una carga más para el equipo en obra…» | Voss [VERIFICAR-PÁG: *Never Split the Difference*] |
| Principios de persuasión (Cialdini) | Reciprocidad, coherencia, prueba social, autoridad, simpatía, escasez y unidad | Reciprocidad: le dejamos el diagnóstico gratis. Coherencia: pedimos primero un sí pequeño. Unidad: «es su empresa y la nuestra, somos del mismo proyecto». **Escasez: no se usa**, sería falsa | Influence At Work (s. f.) |
| Venta de valor | Hablar del resultado para el cliente, no de la tecnología | No decimos «API, PostgreSQL, SHA-256»; decimos «nadie pierde un cliente sin que usted se entere» | — |

## 2. Antes de la reunión

**Lo que llevamos:**
1. El celular con la página del formulario abierta, para la demostración en vivo.
2. Una hoja impresa con la tabla del censo (p. 10 del Informe Final) y la brecha de la sección 2.2 de *La necesidad de Torvesa*.
3. El pitch de 1 minuto ensayado (documento del pitch).
4. La carta de solicitud con los tres pedidos, para dejarla firmada si dice que sí.
5. El aviso de privacidad (borrador v0.1) impreso, con los tres datos que faltan marcados.

**Quién hace qué:**
- **Víctor:** apertura, el problema y el cierre.
- **Diego:** la demostración en vivo y las preguntas técnicas.

**Lo que no sabemos y no inventamos:** cuántas solicitudes llegan al mes y cuántas se pierden [FALTA-DATO]. Si pregunta, se responde: «Eso es lo primero que queremos medir con usted».

## 3. Guion de la reunión (30 minutos)

### Minuto 0–3 · Apertura
- Agradecer el permiso del 29 de septiembre (reciprocidad: él ya nos ayudó; le devolvemos algo útil).
- Dar el objetivo en una frase: «Venimos a mostrarle algo que funciona y a pedirle tres cosas pequeñas para probarlo con su equipo durante dos semanas».
- Adelantarse a lo negativo (Voss): «Seguramente piensa que es otro sistema que el equipo no va a usar en obra. Por eso lo diseñamos para que sea un solo botón en el celular».

### Minuto 3–10 · Preguntas SPIN (que hable él)
| Tipo | Pregunta |
|---|---|
| Situación | «¿Por dónde le llegan hoy los clientes nuevos?» · «¿Quién los atiende cuando el ingeniero está en obra?» |
| Problema | «¿Le ha pasado que un cliente escribió y nadie le respondió a tiempo?» · «¿Sabe cuántas cotizaciones se enviaron el mes pasado?» |
| Implicación | «Si un cliente espera tres horas, ¿qué cree que hace en ese tiempo?» · «Cuando un ingeniero se va de la empresa, ¿qué pasa con sus clientes y sus cotizaciones?» · «¿Cómo se entera usted de que se perdió un cliente y por qué?» |
| Necesidad de solución | «Si cada lunes supiera cuántos clientes llegaron, en cuántos minutos se atendieron y por qué se perdieron, ¿qué decisiones tomaría?» |

Técnica de Voss durante las respuestas: **etiquetar** («Parece que esto le ha costado clientes antes») y **repetir** sus últimas palabras para que siga hablando.

### Minuto 10–13 · La idea nueva (Challenger)
- «Su propio equipo dice que un cliente no debería esperar más de 15 minutos: 4 de cada 5. Pero 3 de cada 5 revisan los mensajes cada 3 o 4 horas, o solo al llegar a casa. No es falta de ganas: están en obra.»
- «Torvesa no pierde clientes en la obra. Los pierde en la primera hora, y hoy no queda rastro.»
- Contexto, solo si ayuda: la construcción cayó 7,9 % en 2024 y volvió a crecer en 2025 (Banco Central del Ecuador, 2026, p. 22): «los clientes están volviendo; el que responde primero se los queda».

### Minuto 13–20 · Demostración en vivo
1. Diego llena el formulario con datos inventados y marca la casilla de consentimiento.
2. A los segundos llega la tarjeta al celular. Víctor pulsa «Tomar».
3. Se muestra que quedó la hora del primer contacto y el responsable.
4. Se muestra el borrador de cotización: sin precios, con preguntas para completar, y que lo revisa una persona.
5. Frase de cierre de la demo: «Todo lo que vio son datos inventados. Lo que le pedimos es probarlo dos semanas con su equipo».

### Minuto 20–27 · Objeciones (sección 4)

### Minuto 27–30 · Cierre (sección 5)

## 4. Objeciones probables y cómo responder

| # | Objeción | Qué hay detrás (interés) | Respuesta |
|---|---|---|---|
| 1 | «Mi gente no tiene tiempo para otro sistema» | No quiere cargar al equipo en obra | «Es un solo botón: "Tomar". El aviso llega como un mensaje de texto, que es lo que prefiere su equipo (2 de 5 eligieron alerta de texto y 2 de 5 una tarjeta con enlace). Si en dos semanas les quita tiempo, lo dejamos.» |
| 2 | «Ya usamos WhatsApp y funciona» | Miedo a cambiar lo conocido | «WhatsApp se queda. Lo que llega por WhatsApp se registra en un minuto desde el celular. Lo que cambia es que usted sabe quién lo atendió y en cuánto tiempo.» |
| 3 | «¿Cuánto cuesta?» | Riesgo de gastar | «Las dos semanas de validación no le cuestan nada. Lo que costaría operarlo después está calculado con precios oficiales en nuestro modelo financiero [cifra del frente A, con fuente], y se lo dejamos por escrito.» |
| 4 | «¿Y los datos de mis clientes?» | Riesgo legal y de reputación | «Va con consentimiento del cliente, como pide la LOPDP. Los nombres y teléfonos están separados, la IA nunca los recibe, y usted fija cuánto tiempo se guardan.» |
| 5 | «¿Qué pasa cuando ustedes terminen la tesis?» | Miedo a quedarse con algo sin soporte | «Le dejamos el manual y la bóveda documentada. Y si sirve, conversamos un acuerdo de soporte; si no, se apaga sin costo.» [DECIDIR-VÍCTOR: qué se ofrece después de la tesis] |
| 6 | «No quiero que la IA mande cotizaciones solas» | Control y precios | «Tampoco nosotros. La IA no pone precios ni envía nada. Prepara un borrador y una persona lo revisa siempre.» |
| 7 | «Esto es para empresas grandes» | Duda de que aplique a una pyme | «Está hecho para el tamaño de Torvesa: formulario, celular y una carpeta de notas. En la OCDE solo el 11,9 % de las pequeñas empresas usa IA (OECD, 2025, p. 6): usted estaría adelante.» |
| 8 | «Mejor compro un CRM conocido» | Busca algo probado | «Es una opción válida, y la comparamos en nuestra matriz de herramientas. La diferencia es que esto está hecho para su forma de trabajar en obra y cuesta menos [cifra del frente A]. Pruébelo dos semanas y compare con datos.» |
| 9 | «No tengo tiempo de revisar nada» | Su agenda | «Solo le llega un reporte el lunes, en una página: cuántos clientes, en cuántos minutos y por qué se perdieron.» |
| 10 | «Déjenme pensarlo» | No ve todavía el valor o le falta algo | Pregunta calibrada (Voss): «¿Qué necesitaría ver para decidir?». Si no hay respuesta, pedir el sí más pequeño: «¿Nos autoriza al menos a revisar las fechas y horas de las solicitudes de los últimos 3 meses, sin datos de clientes?» |

## 5. Cierre: tres sí pequeños, en este orden

Se pide primero lo más fácil (principio de coherencia de Cialdini: quien dice sí a algo pequeño tiende a seguir siendo coherente).

1. **Datos para el aviso de privacidad:** RUC, correo de contacto y plazo de conservación. (Lo más fácil: son datos públicos o una decisión rápida.)
2. **Muestra documental:** fechas y horas de las solicitudes de los últimos 3 meses, sin nombres ni datos de clientes. (Es la línea base.)
3. **Dos semanas de validación** con su equipo, del 23 de noviembre al 5 de diciembre [DECIDIR-VÍCTOR: confirmar fechas con el cronograma], reversible en cualquier momento.

**Cómo cerrar:** «Entonces quedamos en tres cosas: los datos del aviso esta semana, la muestra de fechas y horas, y dos semanas de prueba desde el 23. ¿Está bien si se lo dejamos por escrito para su firma?»

**Después de la reunión:** un correo el mismo día con lo acordado (lo que se acordó por escrito es más fácil de cumplir).

## 6. Lo que el gerente gana aunque diga que no

- El diagnóstico de su proceso (AS-IS) y la brecha de los 15 minutos, con los datos de su propio equipo.
- Esto se le entrega igual: es reciprocidad real, no un truco.

## 7. Plan B (nuestra BATNA)

| Si dice que no a… | Qué hacemos | Efecto en la tesis |
|---|---|---|
| La validación con su equipo | Ejecutamos los casos de prueba CP-01 a CP-03 con datos ficticios (ya diseñados) | La tesis sigue; los resultados son de condiciones controladas, no de operación real. Se declara como limitación |
| La muestra documental | Usamos el censo n = 5 como antecedente y declaramos la línea base como pendiente | Limitación declarada en el Cap. VI |
| Todo | Presentamos el diseño validado en condiciones controladas | La tesis es de diseño (DSR): el artefacto y su evaluación controlada siguen siendo un aporte |

**BATNA del gerente (para entenderlo):** seguir igual (costo: no sabe cuántos clientes pierde) o contratar un CRM comercial (costo de licencias y adaptación). Nuestra propuesta tiene que ser mejor que esas dos para él, no para nosotros.

## Referencias

Banco Central del Ecuador. (2026). *Informe de evolución de la economía ecuatoriana en 2025 y perspectivas 2026*. https://contenido.bce.fin.ec/documentos/Administracion/EvolEconEcu_2025pers2026.pdf

Influence At Work. (s. f.). *The 7 principles of persuasion*. https://www.influenceatwork.com/7-principles-of-persuasion/

OECD. (2025). *AI adoption by small and medium-sized enterprises* (OECD discussion paper for the G7). OECD Publishing.

Subramanian, G. (2026, 30 de septiembre). *Translate your BATNA to the current deal*. Program on Negotiation, Harvard Law School. https://www.pon.harvard.edu/daily/batna/translate-your-batna-to-the-current-deal/

*Libros de apoyo (no abiertos; si se citan, falta la página):* Fisher, Ury y Patton, *Getting to Yes*; Rackham, *SPIN Selling* (1988); Dixon y Adamson, *The Challenger Sale* (2011); Voss, *Never Split the Difference* (2016).
