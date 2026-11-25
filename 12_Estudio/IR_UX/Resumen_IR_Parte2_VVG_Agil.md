---
titulo: "Resumen parte 2: Validación, Verificación y Gestión + Requerimientos Ágiles e Historias de Usuario"
materia: Ingeniería de Requerimientos, Usabilidad y UX (Ing. Joshua Proaño)
examen: 2026-11-26 (jueves 17:00)
fuente: "VVG = «Validación, Verificación y Gestión de Requerimientos» (27 págs.); AG = «Requerimientos Ágiles e Historias de Usuario» (19 págs.)"
fecha: 2026-11-24
autor_borrador: "Claude (revisa Victor)"
tags: [estudio, examen, requerimientos, validacion, verificacion, gestion, agil, historias-de-usuario, invest]
---

# Parte 2: las dos últimas clases

> [!tip] Cómo leer esto
> Igual que el resumen 1: lo que dice la diapositiva (casi textual), la analogía y la trampa. (VVG, p. 4) = clase de Validación, Verificación y Gestión, página 4. (AG, p. 11) = clase de Ágiles e Historias de Usuario.

> [!warning] No confundir con el resumen 1
> En la clase de Importancia (p. 6) las etapas eran **5** (Elicitación, Análisis, Especificación, Validación, Gestión). En la clase VVG (p. 2) el profe las abre en **6**, separando **Validación (4)** y **Verificación (5)**, y **Gestión (6)**. Si la pregunta viene de esta clase, responde 6.

---

## 1. Dónde estamos (VVG, p. 2)

Las 6 etapas según SWEBOK v4, en la clase VVG:

| # | Etapa | Qué hace (textual) |
|---|---|---|
| 1 | Elicitación | obtener los requerimientos |
| 2 | Análisis | entender, clasificar y resolver conflictos |
| 3 | Especificación | documentar de forma clara |
| 4 | **Validación** | confirmar que son los **CORRECTOS** |
| 5 | **Verificación** | confirmar que están **BIEN escritos** |
| 6 | **Gestión** | mantener actualizados durante el ciclo de vida |

**Mnemotecnia:** «**E-A-E-V-V-G**: *El Analista Escribe, Valida, Verifica y Gestiona*».

**El caso que usa toda la clase (VVG, p. 3):** app de transporte público de Quito, requerimientos en **línea base v1.1**. El RQ-08 («publicar indicadores de puntualidad por operadora») quedó fuera del lanzamiento porque las operadoras se oponían. Ahora aceptan **con una condición: reglas de medición acordadas**. El Municipio pide: «La app debe mostrar qué operadora es la más puntual». Tres preguntas:
- **Validación:** ¿es lo que realmente se necesita?
- **Verificación:** ¿está bien escrito?
- **Gestión:** ¿qué impacto tiene y quién lo aprueba?

---

## 2. Validación: ¿construimos el producto CORRECTO? (VVG, pp. 4-9)

**Definición (p. 4):** confirmar que los requerimientos reflejan lo que el usuario necesita.
- Pregunta: **¿estamos construyendo el producto CORRECTO?**
- Se hace **junto al cliente y a los stakeholders**.
- No es solo revisar la redacción, sino **validar la intención**.
- Según SWEBOK v4: **previene construir el producto equivocado**.
- Puede revelar requerimientos **malentendidos o faltantes**.

**Importancia (p. 5), 6 puntos:**
1. Detectar problemas al validar cuesta **horas**; en producción cuesta **semanas**.
2. El desarrollo invierte esfuerzo en lo correcto.
3. Reduce reprocesos y conflictos contractuales.
4. Aumenta la satisfacción del cliente al final.
5. Refuerza la confianza entre equipo técnico y stakeholders.
(Conecta con la regla 1-10-100 del resumen 1.)

**Errores comunes que detecta la validación (p. 6): 7**
1. Requerimientos que no resuelven el problema real del usuario.
2. Funcionalidades innecesarias agregadas por suposición.
3. Faltantes críticos que el cliente daba por obvios.
4. Interpretaciones distintas del mismo requerimiento.
5. Requerimientos contradictorios entre stakeholders.
6. Casos de uso no contemplados (excepciones, errores).
7. Restricciones legales o de negocio omitidas.

**Técnicas de validación según SWEBOK v4 (p. 7): 7**
1. Revisiones formales con stakeholders.
2. **Walkthroughs** (recorridos guiados sobre la especificación).
3. **Prototipos** para validar visual o funcionalmente.
4. **Casos de prueba de aceptación** derivados de los requerimientos.
5. Listas de chequeo (checklists).
6. Modelado y simulación cuando aplique.
7. Validación basada en estándares (ej. ISO/IEC/IEEE 29148).

Mnemotecnia: «**RE-WA-PRO-CA-LI-MO-ES**» → *Revisa, Walkea, Prototipa, Acepta, Lista, Modela, Estandariza*.

**Ejemplo de la diapositiva (p. 8):**
- Original: «el sistema debe ser fácil de usar».
- Preguntas al cliente: ¿qué significa fácil para usted? ¿en qué tareas? ¿quién es el usuario objetivo?
- Validado: «**el 90 % de los usuarios objetivo debe completar el registro en menos de 3 minutos sin asistencia**». Claro, verificable y concreto.

**El caso, validado (p. 9):** se pregunta a cada stakeholder **para qué** quiere el dato.

| Stakeholder | Pregunta | Respuesta |
|---|---|---|
| Usuarios | ¿para qué usarían ese dato? | para elegir ruta y saber cuánto esperar, **no para un ranking** |
| Operadoras | ¿qué condiciones piden? | medir solo rutas **con GPS** y **no contar retrasos por cierres de vía** |
| Municipio | ¿qué decisión tomarán? | **controlar el cumplimiento de los contratos** |

Resultado validado: **puntualidad por ruta para los usuarios** y **reporte por operadora solo para el Municipio**. Frase clave: **«La validación cambió la intención: el ranking público no era la necesidad real».**

> **Analogía (compras):** te llega un requerimiento «comprar 50 laptops gamer». Validar es llamar al área y preguntar para qué: resulta que es para Excel y correo. La necesidad real era «50 equipos de oficina». No cambiaste la redacción, cambiaste **lo que se va a comprar**.
>
> **Analogía (Valorant):** tu duelista pide «quiero un Jett». Validar es preguntar «¿para qué?»: «para entrar primero a B». Quizá lo que el equipo necesita es un iniciador que limpie la entrada. Validar = confirmar la **intención**, no el nombre.

---

## 3. Verificación: ¿especificamos CORRECTAMENTE? (VVG, pp. 10-20)

**Definición (p. 10):** comprobar que los requerimientos están **BIEN ESCRITOS**.
- Pregunta: **¿estamos especificando los requerimientos CORRECTAMENTE?**
- Se hace **internamente**, con criterios técnicos.
- **No requiere necesariamente al cliente.**
- Es una **revisión de calidad de la documentación**.
- SWEBOK v4: garantiza que cumplen estándares.
- ISO/IEC/IEEE 29148 define qué características debe cumplir cada uno.

### Validación contra verificación (pp. 11-12). ESTA TABLA CAE SÍ O SÍ

| | **Validación** | **Verificación** |
|---|---|---|
| Pregunta | ¿Construimos el producto **CORRECTO**? | ¿Especificamos **correctamente** los requerimientos? |
| Foco | lo que el cliente **NECESITA**; la **intención** | cómo está **ESCRITO**; calidad de la especificación |
| Se hace con | el cliente, usuarios finales, stakeholders | equipo técnico, analistas, pares revisores |
| Técnicas | revisiones con cliente, **prototipos**, **casos de aceptación** | revisiones técnicas, **listas de chequeo**, **inspecciones formales** (p. 12: análisis formal) |
| Detecta | necesidades mal entendidas, funcionalidades faltantes | **ambigüedades, contradicciones**, redacciones poco claras |

**Frase de cierre (p. 12):** «Ambos son complementarios y necesarios. **Ninguno reemplaza al otro**».

> **Truco para no confundirlas:** **vaLIdación = cLIente** (las dos tienen «li»). **veRIFIcación = REvisar la escRItura** (la hace el equipo, como un corrector de ortografía).
>
> **Analogía (Minecraft):** validar es que tu pana vea la base y diga «sí, eso quería». Verificar es revisar que el plano tenga las medidas bien puestas y que dos paredes no ocupen el mismo bloque.
>
> **Analogía (comida):** validar = preguntarle al cliente si quería pizza o hamburguesa. Verificar = revisar que la comanda de cocina diga bien «pizza mediana, sin cebolla» y no «pizza rica y rápida».

### ISO/IEC/IEEE 29148 (p. 13)
Estándar internacional sobre procesos de requerimientos; complementa a SWEBOK v4 con criterios operativos. Características que cada requerimiento debe cumplir (**9**, en inglés en la diapositiva):
**necessary, implementation-free, unambiguous, consistent, complete, singular, feasible, traceable, verifiable.**
(necesario, libre de implementación, no ambiguo, consistente, completo, singular, factible, trazable, verificable).

Hoy se usan **los 3 más usados en la práctica: claridad, completitud, coherencia** (mnemotecnia **«las 3 C»**).

### Los 3 criterios fundamentales (pp. 14-17)

| Criterio | Qué es | Evitar / incluir / revisar | Preguntas para verificar |
|---|---|---|---|
| **1. Claridad** (p. 15) | se entiende sin esfuerzo y sin ambigüedad | **Evitar:** rápido, fácil, amigable, intuitivo | ¿usa términos vagos? ¿se entiende a la primera? ¿terminología consistente? ¿**una sola interpretación**? |
| **2. Completitud** (p. 16) | el **conjunto** cubre toda la información necesaria | **Incluir:** casos de error y excepciones | ¿faltan casos de uso o flujos alternativos? ¿errores y excepciones? ¿RNF cubiertos? ¿integraciones? ¿restricciones técnicas, legales o de negocio omitidas? |
| **3. Coherencia** (p. 17) | no hay contradicciones internas | **Revisar:** términos y prioridades uniformes | ¿términos con significados distintos? ¿reglas que se contradicen? ¿prioridades consistentes? |

- **Trampa:** «La completitud se evalúa sobre **el conjunto, no sobre un único requerimiento**» (p. 16).
- **Ejemplo de incoherencia (p. 17):** RF-002 «el registro requiere email» contra RF-007 «el registro debe hacerse solo con cédula». Las inconsistencias pasan desapercibidas en proyectos grandes.

### La lista de chequeo para verificar (p. 18): 12 puntos
1. Tiene **ID único** y consistente.
2. Lenguaje claro y **sin términos vagos**.
3. **Verificable** mediante un criterio medible.
4. Tiene **prioridad** asignada.
5. Tiene **criterio de aceptación**.
6. **No contradice** a otros requerimientos.
7. **Terminología consistente** con el documento.
8. Cubre los casos **normales y de excepción**.
9. **Trazable** a un stakeholder origen.
10. **Factible** técnica y económicamente.
11. Describe el **QUÉ, no el CÓMO**.
12. Aporta **valor real** al usuario o al negocio.

«Usar esta lista en el ejercicio para revisar cada requerimiento» → **es la herramienta de la hoja práctica.**

### Errores típicos al verificar (p. 19): 4
1. **Mezclar QUÉ con CÓMO:** «usar MySQL para guardar usuarios» (impone solución).
2. **Palabras subjetivas:** rápido, simple, robusto, flexible.
3. **Falta de criterio de aceptación:** no se puede probar si se cumple.
4. **Varios objetivos en uno (no atómicos):** «permitir registrarse y recuperar contraseña».

### El caso, verificado (p. 20). EL MODELO DE EJERCICIO
Primer borrador: «RF-031: el sistema debe mostrar la puntualidad de las rutas de forma **rápida y confiable** y **permitir exportar reportes**».

| Problema detectado | Criterio |
|---|---|
| «rápida» y «confiable» son vagos | claridad |
| dos objetivos en uno (mostrar **y** exportar) | no es atómico |
| «puntualidad» no está definida | coherencia del vocabulario |
| no tiene criterio de aceptación | no es verificable |

Versión verificada (se parte en **dos**):
- **RF-031:** cuando el usuario consulte una ruta piloto, el sistema debe mostrar el **% de salidas con menos de 3 min de desvío** del horario en los **últimos 7 días**, **sin contar los cierres de vía registrados**.
- **RF-032:** el sistema debe generar **para el Municipio** un **reporte mensual** de puntualidad **por operadora en PDF**.

---

## 4. Gestión de requerimientos (VVG, pp. 21-26)

**Definición (p. 21):** mantener los requerimientos **actualizados, controlados y trazables durante todo el ciclo de vida**.
- Cambian porque cambian el negocio, la ley, los usuarios y la tecnología.
- «**Gestionar no es impedir los cambios, sino decidir sobre ellos con información**».
- **4 actividades principales:**
  1. línea base y control de versiones;
  2. control de cambios con análisis de impacto;
  3. trazabilidad;
  4. seguimiento de la estabilidad y la volatilidad.
- SWEBOK v4: el proceso es **iterativo y continúa hasta el retiro del sistema**.

### Línea base y versiones (p. 22)
- **Línea base:** conjunto de requerimientos **revisado y aprobado** que sirve de referencia. Desde ahí, todo cambio pasa por control de cambios.
- Versiones: **v1.0** primera línea base aprobada; **v1.1, v1.2…** cambios menores aprobados; **v2.0** cambio mayor de alcance.
- El historial registra: **versión, fecha, cambio y quién lo aprobó**.
- En el caso: **v1.1 (lanzamiento) → v1.2 (agrega RF-031 y RF-032)**.

> **Analogía (Genshin / juegos):** la línea base es el parche oficial. v1.0 sale el juego; 1.1, 1.2 son parches; 2.0 es la expansión con mapa nuevo. Nadie mete un personaje nuevo sin las notas del parche.
>
> **Analogía (tesis):** es exactamente nuestro control de versiones del borrador: v0.1, v0.2… y quién lo aprobó.

### Control de cambios (p. 23): 5 pasos
1. **Solicitud:** quién pide el cambio, qué cambia y por qué.
2. **Análisis de impacto:** requerimientos afectados, **esfuerzo, plazo y riesgo**.
3. **Decisión:** **aprobar, rechazar o diferir**; decide el **product owner o comité**.
4. **Actualización:** línea base, versión y trazas.
5. **Comunicación:** equipo y stakeholders informados.

- **En ágil:** la solicitud entra al **backlog** y compite por prioridad como cualquier otra historia.
- Frase: «**Un cambio sin análisis de impacto es un cambio sin control**».
- Mnemotecnia: «**S-A-D-A-C**: *Solicito, Analizo, Decido, Actualizo, Comunico*» (o «*Si Aprueban, Después Actualizo y Cuento*»).

> **Analogía (compras, la mejor):** es tu ciclo de compras. **Solicitud** = el requerimiento que llega del área. **Análisis de impacto** = el cuadro comparativo (cuánto cuesta, cuánto demora, qué riesgo). **Decisión** = la aprobación del jefe (aprueba, rechaza o «para el otro mes» = diferir). **Actualización** = la PO en el portal. **Comunicación** = el correo al proveedor y al área. Si pagas sin PO, es «un cambio sin control».

### Análisis de impacto del caso (p. 24). MEMORIZA LAS CIFRAS

| Aspecto | Resultado |
|---|---|
| Requerimientos afectados | RF-031 y RF-032 (nuevos); **RQ-02 tiempo real** (dependencia); **RQ-12 panel del Municipio** (se amplía) |
| Esfuerzo | **+7 semanas-persona** (RF-031: **5**, RF-032: **2**) |
| Plazo | el lanzamiento ya usa **48 de 48** semanas-persona: **no entra en la versión 1** |
| Riesgo | **0,4**: depende de los GPS de las rutas piloto y de las reglas de medición acordadas |
| Decisión | **aprobado para la versión 2**, con un piloto de **un mes**. Aprueba: **el Municipio (sponsor)** |
| Nueva línea base | **v1.2** |

### Trazabilidad (p. 25)
- **Hacia atrás:** ¿de qué **necesidad** y de qué **stakeholder** viene?
- **Hacia adelante:** ¿dónde se **diseña, se construye y se prueba**?

Matriz del caso: Necesidad → Stakeholder → Requerimiento → Diseño → Prueba

| Necesidad | Stakeholder | Req. | Diseño | Prueba |
|---|---|---|---|---|
| Elegir ruta según puntualidad | Usuarios | RF-031 | Pantalla «Detalle de ruta» | CP-031: ruta piloto con 7 días de datos |
| Controlar contratos | Municipio | RF-032 | Módulo de reportes | CP-032: reporte mensual en PDF |
| Medición justa | Operadoras | RF-031 | Servicio de cálculo | CP-033: un cierre de vía no cuenta como retraso |

Frase: «Si mañana cambia RF-031, **la matriz dice qué pantalla, servicio y pruebas revisar**».

> **Analogía (Deuna / Amazon):** la trazabilidad es el rastreo del paquete. Hacia atrás: quién lo pidió y por qué. Hacia adelante: en qué bodega está, en qué camión va y quién firmó la entrega.

### Estabilidad, volatilidad y herramientas (p. 26)
- **Estabilidad:** atributo de **cada** requerimiento (alta, media, baja). Los de estabilidad baja se revisan con más frecuencia.
- **Volatilidad:** cuánto cambia **el conjunto**. Métrica: **% de requerimientos modificados por sprint o por versión**. Volatilidad alta suele indicar **una elicitación incompleta**.
- **Trampa:** estabilidad = uno; volatilidad = el conjunto.
- **Herramientas:** hoja de cálculo (proyectos pequeños); **Jira, Azure DevOps o GitHub Projects** (backlog, historial y enlaces); herramientas especializadas en proyectos grandes.

### Cierre (p. 27)
4 Validación: el ranking público → puntualidad por ruta + reporte para el Municipio. 5 Verificación: «rápida y confiable» → criterio medible y dos requerimientos atómicos. 6 Gestión: +7 semanas-persona, aprobado para versión 2, línea base v1.2. «**Las tres son necesarias: ninguna reemplaza a las otras**».

---

## 5. Tradicional contra ágil (AG, pp. 2-4)

| | Tradicional (Cascada) | Ágil (Scrum, Kanban, XP…) |
|---|---|---|
| Requerimientos | especificación extensa; detalle inicial muy alto; cambios costosos | evolutivos, refinados a tiempo; detalle creciente; **cambios bienvenidos** |
| Proceso | secuencial y por fases; documentación primero; entrega al final | iterativo e incremental; entregas frecuentes; feedback constante |
| Cliente | firma al inicio; ve el producto al final | participa todo el tiempo; ve resultados cada sprint |

**Metodologías ágiles (p. 3):** desarrollo **iterativo, incremental, colaborativo y adaptativo** (4 adjetivos). Origen: **Manifiesto Ágil (2001), firmado por 17 desarrolladores**. Marcos: **Scrum, Kanban, XP, SAFe, Lean** (5). «Lo importante no es la metodología, sino la mentalidad ágil».

**Los 4 valores del Manifiesto Ágil (p. 4):** se prefieren
1. **Individuos e interacciones** sobre procesos y herramientas.
2. **Software funcionando** sobre documentación extensa.
3. **Colaboración con el cliente** sobre negociación contractual.
4. **Responder al cambio** sobre seguir un plan rígido.

«Lo de la derecha sigue siendo importante, pero **lo de la izquierda se valora MÁS**». Trampa: no dice que la documentación no sirva.

Mnemotecnia: «**I-S-C-R**: *Inter Software Colabora Rápido*» (personas, software, cliente, cambio).

> **Analogía (Quito):** cascada es el Metro de Quito: se planificó todo, se construyó años y recién al final la gente lo usó. Ágil es una app como Quito Te Mueve: sale una versión básica, la gente la usa, se queja, y cada dos semanas sale una mejora.

## 6. Los 3 conceptos ágiles (AG, pp. 5-8)

**Concepto 1, Iteraciones (pp. 5-6):** en vez de un entregable grande, varios pequeños incrementales. Ejemplo: Sprint 1 Login básico → 2 Listado de productos → 3 Carrito → 4 Pasarela de pagos → 5 Historial, **2 semanas cada uno**. Una iteración es un ciclo corto con resultado tangible, **entre 1 y 4 semanas**; al final hay un **incremento funcional**. Beneficios (4): feedback temprano, detectar errores rápido, reducir riesgos, priorizar lo más valioso primero. «Cada iteración entrega un producto, no solo documentación».

**Concepto 2, Colaboración (p. 7):** el cliente es parte del equipo. Características: comunicación cara a cara o por video; reuniones cortas y frecuentes; transparencia; responsabilidad compartida. **Roles en Scrum:**
- **Product Owner:** representa al cliente y **prioriza**.
- **Scrum Master:** **facilita** el proceso.
- **Equipo de desarrollo:** **ejecuta**.
- El **analista de requerimientos suele apoyar al Product Owner**.

> **Analogía (Valorant):** Product Owner = el IGL que decide qué sitio atacar (prioriza). Scrum Master = el coach que quita obstáculos y cuida que se respete el plan, pero no juega. Equipo = los 5 que entran al sitio.

**Concepto 3, Adaptación al cambio (p. 8):** el cambio es una oportunidad. Asume que los requerimientos van a cambiar, el cliente aprende lo que necesita al ver el producto, el negocio cambia y surgen ideas con el feedback. Estrategias: priorizar lo importante al inicio; **refinar los detalles solo cuando se van a usar**; backlog vivo; **evitar diseñar todo de antemano**.

## 7. El Product Backlog (AG, p. 9)
Lista **priorizada** de requerimientos; la gestiona el **Product Owner** con apoyo del equipo y stakeholders. Características: priorizado por **valor de negocio**; refinado constantemente (**Grooming/Refinement**); **ítems más detallados arriba, más generales abajo**; **nunca está «terminado»**. Sus ítems suelen escribirse como **historias de usuario**.

> **Analogía (compras):** el backlog es tu tabla de requerimientos pendientes ordenada por urgencia: arriba lo que sale este viernes, con cotización y todo; abajo, ideas vagas tipo «algún día renovar sillas».

## 8. Historias de usuario (AG, pp. 10-14)

**Qué es (p. 10):** forma **corta y centrada en el usuario** de expresar un requerimiento. Captura el **QUÉ, el QUIÉN y el PORQUÉ**. Promueve la **conversación** en lugar de documentación exhaustiva. Frente a la especificación tradicional: más corta, centrada en el valor, **complementada con criterios de aceptación**, elaborada con el cliente. Reconocida también por ISO/IEC/IEEE 29148.

**Plantilla (p. 11):** **Como** [usuario] **quiero** [funcionalidad] **para** [beneficio].
- [usuario] → ¿quién la pide? **(rol, no nombre)**.
- [funcionalidad] → ¿qué quiere lograr? (acción concreta).
- [beneficio] → ¿para qué le sirve? (valor obtenido).

**Ejemplos (pp. 12-14):**
1. Delivery: «Como **cliente** quiero **ver el tiempo estimado de llegada** de mi pedido para **planificar mi día sin preocuparme**».
2. Universidad: «Como **estudiante** quiero **descargar el certificado de matrícula** desde la app para **no ir presencialmente a secretaría**». Detrás hay una conversación donde se definen los detalles técnicos.
3. E-commerce: «Como **comprador frecuente** quiero **guardar mis tarjetas de forma segura** para **comprar más rápido** sin reingresar datos». Precisión en el rol: comprador frecuente ≠ ocasional.

## 9. INVEST (AG, p. 15). CAE SÍ O SÍ
Propuesto por **Bill Wake**:

| Letra | Inglés | Significa |
|---|---|---|
| **I** | Independent | independiente de otras historias |
| **N** | Negotiable | los detalles se negocian con el cliente |
| **V** | Valuable | aporta valor real al usuario |
| **E** | Estimable | el equipo puede estimar su esfuerzo |
| **S** | Small | **cabe en un sprint** |
| **T** | Testable | se puede probar de forma objetiva |

«Si una historia falla en alguno, conviene **reescribirla o dividirla**».

> **Analogía (Minecraft):** una buena historia es como un bloque: **I**ndependiente (lo pones sin depender de otro), **N**egociable (puede ser de piedra o madera), **V**ale algo, **E**stimas cuánto te demora, es **S**mall (cabe en una sesión de juego) y lo **T**esteas (te paras encima y no se cae).

## 10. Buena contra mala historia (p. 16)
- **Mala:** «Como usuario quiero que la app sea más rápida». Problemas: «usuario» genérico; «más rápida» subjetivo; no se puede medir; no especifica beneficio; no es testeable.
- **Buena:** «Como **estudiante de pregrado** quiero **buscar materias por nombre en menos de 2 segundos** para **inscribirme rápidamente en el periodo de matrículas**». Rol específico, funcionalidad medible, beneficio claro y verificable.

## 11. Criterios de aceptación: Dado/Cuando/Entonces (p. 17)
Definen **cuándo la historia está «terminada»**. Formato **Given/When/Then**:
- **Dado** que estoy en la pantalla de matrícula (contexto)
- **Cuando** escribo el nombre de una materia (acción)
- **Entonces** veo los resultados en menos de 2 segundos (resultado medible)

Facilitan la verificación y **conectan con QA**.

> **Analogía (Deuna):** Dado que tengo saldo, Cuando escaneo el QR y confirmo, Entonces veo «Pago exitoso» y me llega la notificación en menos de 5 segundos. Si no pasa, la historia no está lista.

## 12. Errores al escribir historias (p. 18): 4
1. Usar «usuario» genérico → mejor: «cliente VIP», «administrador», «estudiante nuevo».
2. Mezclar varias funcionalidades → dividir.
3. Olvidar el beneficio («para…») → sin beneficio no se sabe por qué priorizarla.
4. Escribir soluciones técnicas → mal: «quiero un botón rojo en la esquina»; bien: «quiero acceder a soporte rápidamente».

## 13. Historias técnicas y spikes (p. 19)
- **Historias técnicas:** infraestructura, refactor, deuda técnica. Ej.: «migrar la base de datos a una versión más reciente».
- **Spikes:** **investigaciones para resolver incertidumbres**. Ej.: «investigar opciones de pasarela de pago para Ecuador».
- **Ambos van en el backlog junto a las historias de usuario.**

---

## Tabla «no confundir» (parte 2)

| Esto | No es esto | Truco |
|---|---|---|
| Validación (producto correcto, con cliente, intención) | Verificación (bien escrito, interno, redacción) | vaLIdación = cLIente |
| Estabilidad (de cada requerimiento) | Volatilidad (del conjunto, % modificados) | volátil = el grupo entero se mueve |
| Completitud (del conjunto) | Claridad (de cada uno) | completo = no falta nada en el documento |
| Product Owner (prioriza) | Scrum Master (facilita) | Owner = dueño decide |
| Trazabilidad hacia atrás (necesidad, stakeholder) | Hacia adelante (diseño, construcción, prueba) | atrás = origen; adelante = destino |
| Historia técnica (trabajo de infraestructura) | Spike (investigación de incertidumbre) | spike = «averiguar» |
| Diferir (decidir más tarde) | Rechazar (no se hace) | diferir = «para la próxima versión» |
| v1.1 (cambio menor) | v2.0 (cambio mayor de alcance) | |
| 5 etapas (clase de Importancia) | 6 etapas (clase VVG) | |

## Las 15 cosas que sí o sí (parte 2)
1. Validación = ¿producto **correcto**? con cliente; verificación = ¿**bien escrito**? interno.
2. Las 6 etapas: Elicitación, Análisis, Especificación, Validación, Verificación, Gestión.
3. 7 técnicas de validación (revisiones, walkthroughs, prototipos, casos de aceptación, checklists, modelado, estándares).
4. Las 3 C de la verificación: claridad, completitud, coherencia. Completitud = conjunto.
5. Palabras prohibidas: rápido, fácil, amigable, intuitivo, simple, robusto, flexible, confiable.
6. La lista de chequeo de 12 puntos (ID, claro, verificable, prioridad, aceptación, no contradice, terminología, excepciones, trazable, factible, qué no cómo, valor).
7. Partir un requerimiento con «y» en dos (atómico).
8. Gestionar no es impedir cambios; 4 actividades.
9. Línea base = aprobada; v1.x menor, v2.0 mayor.
10. Control de cambios: Solicitud, Análisis de impacto, Decisión (aprobar/rechazar/diferir), Actualización, Comunicación.
11. Caso: +7 semanas-persona (5+2), 48/48, riesgo 0,4, versión 2, Municipio aprueba, v1.2.
12. Trazabilidad atrás/adelante y la matriz Necesidad-Stakeholder-Req-Diseño-Prueba.
13. 4 valores del Manifiesto (2001, 17 firmantes); lo de la izquierda vale más.
14. «Como… quiero… para…» con rol (no nombre) + INVEST (Bill Wake) + Dado/Cuando/Entonces.
15. Historias técnicas y spikes van al backlog.
