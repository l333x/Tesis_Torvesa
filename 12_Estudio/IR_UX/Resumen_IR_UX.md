---
titulo: Resumen para el examen de Ingeniería de Requerimientos, Usabilidad y UX
materia: INGENIERÍA DE REQUERIMIENTO, USABILIDAD Y EXPERIENCIA USUARIO, Grupo 1 (Ing. Joshua Proaño)
examen: 2026-11-26 (jueves, 1 hora, teoría y práctica)
fuente: 9 presentaciones y 2 plantillas de clase (12_Estudio/IR_UX/diapositivas/)
fecha: 2026-11-21
autor_borrador: "Claude (revisa Víctor)"
tags: [estudio, examen, requerimientos, swebook, moscow, kano]
---

# Ingeniería de Requerimientos: lo que entra el jueves

> [!tip] Cómo leer esto
> Cada tema tiene: **lo que dice la diapositiva** (casi textual, porque así lo pregunta el profe), **la analogía** y **la trampa típica** de opción múltiple. Entre paréntesis va la presentación y la página: (Intro, p. 2).
> Siglas: **RF** = requerimiento funcional. **RNF** = no funcional. **SWEBOK** = *Software Engineering Body of Knowledge* (guía de la IEEE Computer Society).

## Mapa del curso (orden de las clases)

| # | Clase | Pregunta que responde |
|---|---|---|
| 1 | Introducción a los requerimientos | ¿Qué es un requerimiento y de qué tipos hay? |
| 2 | Importancia en el ciclo de vida (IR + UX) | ¿Por qué importa? ¿Cuánto cuesta equivocarse? |
| 3 | Elicitación | ¿Cómo saco la información a la gente? (entrevista, encuesta, observación) |
| 4 | Técnicas de elicitación | Brainstorming, focus group, análisis de documentos, prototipos |
| 5 | Especificación | ¿Cómo lo escribo bien? (8 características, 8 campos) |
| 6 | Representación | ¿En qué formato? (lenguaje natural estructurado, listas, tablas) |
| 7 | Priorización | ¿Qué hago primero? (MoSCoW, Kano, valor contra esfuerzo) |
| P | Plantillas (elicitación y análisis; TP de Quito) | La práctica: fichas, lista de 12 puntos, 5 porqués, verificación |

**Analogía maestra (Minecraft):** construir software es como armar una base enorme en survival.
- **Elicitación:** preguntarle a tu pana qué quiere: ¿granja?, ¿portal?, ¿defensa contra creepers?
- **Análisis:** descubrir que pidió una base subterránea y también una con vista al mar.
- **Especificación:** escribir el plano con medidas.
- **Validación:** que tu pana lo mire y diga «sí, eso es».
- **Gestión:** cuando a mitad de obra pide una piscina, se anota y se evalúa el impacto.

Si te saltas el plano, rompes y reconstruyes bloques todo el rato.

---

## 1. ¿Qué es un requerimiento? (Intro; Importancia)

- **IEEE Std 610.12:** «Condición o capacidad que un sistema debe satisfacer para cumplir un contrato, estándar o especificación» (Intro, p. 2).
- **SWEBOK v4:** «una propiedad que debe exhibir el software desarrollado o adaptado para resolver un problema particular del mundo real» (Importancia, p. 4).
- Sirve como: necesidad o deseo del usuario o del sistema; base para diseñar, desarrollar y probar; y **estado de acuerdo entre clientes y el equipo**. La analogía del profe son los **planos de la obra** (Intro, p. 2).
- **Cifras que salen en las diapositivas:**
  - **56 %** de proyectos fracasan por requerimientos mal definidos (Intro, p. 3). Ojo: en Importancia, p. 8, el mismo **56 %** aparece como el porcentaje de **defectos que se originan en requerimientos**.
  - **68 %** de proyectos fallan o se retrasan (Importancia, p. 8).
  - Causa **n.º 1** de fracaso: requerimientos incompletos o incorrectos.
  - Corregir en desarrollo cuesta **2x** y en producción **10x** (Intro, p. 3).
  - El profe cita el *Standish Group CHAOS Report* y el SWEBOK.

### Tipos (Importancia, p. 4; Especificación, p. 5)

| Tipo | Pregunta | Ejemplos |
|---|---|---|
| **Funcional (RF)** | ¿**Qué HACE** el sistema? | Acciones del usuario, procesamiento de datos, flujos de negocio. «El sistema DEBE permitir registrarse con correo y contraseña» |
| **No funcional (RNF)** | ¿**Cómo lo HACE** / cómo debe SER? | Rendimiento, seguridad, usabilidad, disponibilidad, escalabilidad, mantenibilidad. «Responder en < 2 s» |
| **De dominio** | Viene del negocio o la ley | «Aplicar el IVA según la legislación local» (la diapositiva dice 12 %; hoy en Ecuador es 15 %) |
| **Emergente** | Sale de la **interacción entre componentes**; no se atribuye a un solo subsistema | La seguridad total de una app (depende de todas sus partes) |

- **Características de un RF** (Intro, p. 6): específicos y medibles, verificables con pruebas, **expresados con verbos de acción**, vinculados a casos de uso e **identificados con un ID único**.
- **Las 6 familias de RNF** (Intro, p. 7):
  - **rendimiento:** tiempo de respuesta, *throughput*, latencia;
  - **seguridad:** autenticación, cifrado, autorización;
  - **usabilidad:** facilidad de uso, accesibilidad, UX;
  - **disponibilidad:** *uptime*, tolerancia a fallos, SLA;
  - **escalabilidad:** crecer bajo mayor demanda;
  - **mantenibilidad:** facilidad para actualizar y corregir.

**Comparación (Intro, p. 8):**

| Aspecto | RF | RNF |
|---|---|---|
| Describe | comportamiento | cualidades |
| Pregunta | ¿qué hace? | ¿cómo lo hace? |
| Ejemplo | login con usuario y contraseña | respuesta en < 1 s |
| Prueba | funcional o unitaria | de rendimiento o carga |
| Se relaciona con | casos de uso e historias | **ISO 25010**, SLA, normativas |

**Casos reales (Intro, p. 9):**
- **Banca móvil:** RF «transferir con clave y monto»; RNF «< 3 s con 99,9 % de disponibilidad».
- **Amazon:** RF «carrito y pago»; RNF «10 000 usuarios concurrentes sin degradación».
- **Zoho:** RF «reportes por fecha, región y KPI»; RNF «gráficos en < 2 s con hasta 1 millón de filas».

> **Analogía Valorant:** el **RF** es lo que hace tu agente: Jett hace *dash*. El **RNF** es cómo lo hace: el *dash* sale en menos de 0,1 s y el servidor aguanta a 10 jugadores sin lag (*tick rate*). Un dash que sale a los 2 segundos cumple el RF y falla el RNF.

> **Trampa:** «El sistema debe cifrar las contraseñas» parece funcional, pero es de **seguridad**, o sea **RNF**. Si la frase habla de una **cualidad** (rápido, seguro, disponible, usable), es RNF aunque tenga verbo.

---

## 2. SWEBOK y el proceso (Importancia; Elicitación)

- El **SWEBOK** es la guía de la **IEEE Computer Society** que define las áreas de conocimiento de la ingeniería de software. **Requerimientos es 1 de 15 áreas** (*Knowledge Areas*) (Importancia, p. 3). La versión que se usa en clase es la **v4 (4.0a, Washizaki, 2025)**.
- Otras áreas que muestra la diapositiva: diseño, construcción, testing, mantenimiento, gestión de configuración y gestión de ingeniería.
- **Norma ligada: ISO/IEC/IEEE 29148:2018**, sobre los procesos de requisitos (Elicitación, p. 3).

### Las 5 etapas de la Ingeniería de Requerimientos (Importancia, p. 6). Mnemotecnia: «**E-A-E-V-G**: *El Analista Escribe, Valida y Gestiona*»

1. **Elicitación:** descubrir y recopilar con entrevistas, talleres, prototipos, observación y análisis de documentos.
2. **Análisis:** detectar **conflictos, omisiones e inconsistencias**, negociar prioridades y clasificar. **La priorización es parte del análisis** según el SWEBOK (Priorización, p. 3).
3. **Especificación:** documentar de forma estructurada (SRS, *user stories*, casos de uso), clara y verificable.
4. **Validación:** confirmar que reflejan las necesidades reales con revisiones, prototipos y pruebas de aceptación.
5. **Gestión:** controlar cambios, mantener la trazabilidad, versionar y evaluar el impacto durante todo el ciclo.

### Ciclo de vida del software, SDLC (Importancia, p. 7): 7 fases

**Planificación → Requerimientos → Diseño → Implementación → Testing → Despliegue → Mantenimiento.**

Los requerimientos influyen en **todas** las fases. Un error se propaga como **efecto dominó**: diseño incorrecto → código inútil → pruebas que no detectan → despliegue fallido → mantenimiento caro.

> **Trampa:** no confundas las **5 etapas de la IR** (dentro de requerimientos) con las **7 fases del SDLC** (el proyecto entero). «Validación» es etapa de la IR; «Testing» es fase del SDLC.

### Regla 1-10-100 (Importancia, p. 9): costo de corregir un error según la fase

| Fase | Costo | Con $10K de base |
|---|---|---|
| Requerimientos | **1x** | $10 000 (cambiar un documento) |
| Diseño | **5x** | $50 000 |
| Implementación | **10x** | $100 000 |
| Testing | **20x** | $200 000 |
| Producción | **100x** | $1 000 000 (recall, parches, clientes perdidos) |

Cada dólar invertido en requerimientos ahorra entre **$10 y $100** después.

> **Analogía de compras:** cambiar el cuadro comparativo antes de aprobar (1x) es fácil. Cambiar la orden de compra ya enviada (10x) es más trabajo. Devolver la mercadería que ya llegó y se facturó (100x) es el peor caso.

### Impacto en tiempos (Importancia, p. 10): 5 efectos

1. **Scope creep:** el alcance crece sin control.
2. **Retrabajo:** del **40 al 50 %** del esfuerzo es retrabajo evitable.
3. **Parálisis por análisis:** sin criterios de priorización, nadie sabe qué hacer primero.
4. **Integración tardía.**
5. **Replanificación.**

### Factores de éxito (Importancia, p. 8)

- Participación de los *stakeholders* desde el inicio.
- Documentación clara, completa y priorizada.
- Gestión formal de cambios.
- Validación temprana con prototipos.
- **Trazabilidad bidireccional:** origen → requerimiento → diseño → código → prueba.

---

## 3. Errores comunes en requerimientos (Importancia, pp. 11-12): 11 errores

| Error | En una línea | Ejemplo de la diapositiva |
|---|---|---|
| **Ambigüedad** | sin métrica, cada quien entiende otra cosa | «debe ser rápido» |
| **Incompletitud** | solo el *happy path* | se olvidan errores, casos límite, permisos, modo *offline*, concurrencia |
| **Inconsistencia** | dos requerimientos se contradicen | «solo premium exporta» frente a «todos generan PDF» |
| **Goldplating** | agregar cosas que **nadie pidió** | el equipo «mejora» con funciones innecesarias |
| **Suposiciones no documentadas** | se asume y no se escribe | «siempre hay internet» y la app falla *offline* |
| **Falta de stakeholders clave** | no incluir al usuario final | el que paga no siempre es el que usa |
| **Requerimientos como solución** | dictar la tecnología | «debe usar MySQL» en vez de «almacenar datos de forma persistente y consultable» |
| **Sin priorización** | todo es alta prioridad | «si todo es urgente, nada es urgente» |
| **Sin criterios de aceptación** | no hay cómo probar | «el usuario puede registrarse», ¿con email?, ¿con Google? |
| **Ignorar los RNF** | solo el qué, no el cómo | ¿cuántos usuarios concurrentes?, ¿99,9 %? |
| **No gestionar cambios** | cambios por chat o en el pasillo | sin evaluar impacto ni aprobación |

> **Analogía Genshin Impact:** **goldplating** es gastar todas tus resinas en subir un artefacto de un personaje que no usas en tu equipo. Brilla, pero no te ayuda a pasar el Abismo.
> **Requerimiento como solución:** «quiero a Raiden» en vez de «necesito un DPS eléctrico que recargue energía».

---

## 4. UX dentro de los requerimientos (Importancia, pp. 13-14)

- La UX **no es una fase posterior**: **empieza en los requerimientos**.
- La **usabilidad es un RNF clave**, y la **ISO 25010** la define como atributo de calidad.
- Herramientas que descubren requerimientos ocultos: **prototipos y wireframes**, *user stories*, ***personas* y *journey maps***, y criterios de aceptación con **métricas de usabilidad**.
- **Mal:** «El usuario puede buscar productos». **Bien:** «…con autocompletado, resultados en < 200 ms, filtros por categoría y precio, y sugerencias si no hay resultados».
- **Valor de negocio:**
  - **retención:** +1 punto de usabilidad da entre 5 y 10 % más de retención;
  - **conversión:** un *checkout* bien requerido puede duplicarla;
  - **soporte:** hasta **60 % menos tickets**, y cada uno cuesta entre $5 y $50;
  - **diferenciación:** la UX es el principal diferenciador;
  - **NPS** (*Net Promoter Score*).

> **Analogía Quito 2026:** la **app del Metro de Quito**. RF: «consultar el saldo de la tarjeta». Requerimiento con UX: «ver el saldo en ≤ 2 toques desde la pantalla de inicio, legible para un adulto mayor (letra ≥ 16 pt) y con aviso si el saldo no alcanza para un viaje».

---

## 5. Elicitación (clase de Elicitación): la etapa 1

- **Qué es:** la actividad de **identificar y obtener** los requisitos. Descubre **necesidades, restricciones y expectativas**. No es solo «preguntarle al cliente»: es **construir una comprensión compartida** (p. 5).
- **Hay que entender el «por qué» del usuario, no solo el «qué» que pide** (p. 6).
- **Stakeholders típicos (6), p. 7:**
  - usuarios finales;
  - clientes que pagan;
  - equipo de desarrollo y operaciones;
  - área de negocio o patrocinadores;
  - **reguladores y auditores**;
  - proveedores y sistemas externos.
- **Fuentes de información (5), p. 8:**
  - personas;
  - documentos;
  - sistemas existentes (el legado);
  - contexto (la observación);
  - mercado (la competencia y los estándares).

  El SWEBOK recomienda **triangular** varias fuentes.

### Los 3 métodos base

| Método | Qué es | Para qué | Preparación | Ojo |
|---|---|---|---|---|
| **Entrevista** | conversación **estructurada, semiestructurada o abierta** | profundidad, motivaciones, conflictos (cualitativo) | definir el objetivo, preguntas guía, grabar **con autorización**, **cerrar con una síntesis validada** | riesgos: **sesgo** del entrevistador y del entrevistado, depende de la habilidad del analista, toma tiempo |
| **Encuesta** | preguntas cerradas o abiertas a **muchos** | **cuantificar** opiniones y prioridades; gente numerosa o dispersa | objetivo y población, preguntas sin sesgo, **pilotar con un grupo pequeño**, análisis estadístico | — |
| **Observación** | ver al usuario en su **contexto real** | ver **lo que hace, no lo que dice que hace**: tareas implícitas, atajos, dolores ocultos | modalidades: **pasiva** (sin intervenir) y **participante** (el analista hace la tarea) | combinarla con entrevistas |

**Comparación (p. 13):**
- **Entrevista:** profundidad, pocos usuarios, cualitativa.
- **Encuesta:** amplitud, muchos usuarios, cuantitativa.
- **Observación:** realidad del contexto, pocos usuarios, cualitativa.

**Ningún método aislado es suficiente.**

### Técnicas adicionales (clase de Técnicas)

| Técnica | Clave | Detalle que preguntan |
|---|---|---|
| **Brainstorming** | sesión grupal, muchas ideas en poco tiempo | **4 reglas:** no criticar, **cantidad antes que calidad**, construir sobre las ideas de otros, registrar todo. Después se agrupan, priorizan y filtran |
| **Focus group** | grupo pequeño de **6 a 10 personas** con un **moderador** | requiere guion, **moderador neutral**, observadores que toman notas y análisis posterior; revela **conflictos entre perfiles** |
| **Análisis de documentos** | revisión sistemática de material existente | manuales, **regulaciones**, contratos, sistemas heredados, reportes. El SWEBOK lo considera **clave para los RNF** |
| **Prototipos** | representación temprana, total o parcial | **baja fidelidad:** papel, *wireframes*. **Alta fidelidad:** *mockups* interactivos. Sirven para que el cliente «vea» el producto |

**Cuándo usar cada una (p. 8):**
- **brainstorming:** exploración inicial;
- **focus group:** validar percepciones y comparar perfiles;
- **documentos:** entender el dominio y las reglas de negocio;
- **prototipos:** validar la comprensión y descubrir necesidades ocultas.

**Riesgos al elicitar (p. 9):**
- *stakeholders* que no saben lo que quieren;
- requisitos contradictorios;
- supuestos no explícitos;
- **sesgo de confirmación** del analista;
- documentación obsoleta.

La mitigación es la **trazabilidad y la validación continua**.

> **Analogía Valorant:**
> - **Entrevista:** hablar 1 a 1 con tu duelista sobre por qué siempre entra solo.
> - **Encuesta:** el *poll* a los 5 del equipo sobre qué mapa banear.
> - **Observación:** ver la repetición (VOD) de la partida. Ves lo que **hicieron**, no lo que dicen que hicieron.
> - **Focus group:** la reunión del equipo con el coach como moderador.
> - **Brainstorming:** armar estrategias nuevas sin decir «eso es tonto».
> - **Análisis de documentos:** leer las notas del parche.
> - **Prototipo:** probar la estrategia en una partida personalizada antes de la competitiva.

> **Analogía de compras:** cuando el área pide «ropa de trabajo», la entrevista es preguntar para quién y para qué. El análisis de documentos es leer la política de compras y la norma de seguridad. La observación es ir a planta y ver que los guantes que piden se rompen en una semana.

---

## 6. Especificación (clase de Especificación): la etapa 3

- **Qué es:** documentar de forma **precisa y comunicable**, convertir lo elicitado en algo escrito. Sirve de **contrato** entre el cliente y el equipo y es la base del diseño, el desarrollo y las pruebas. Es **uno de los entregables más críticos** y el **insumo principal de QA** (pp. 3-4).
- **Según el SWEBOK v4, debe ser:** comprensible, completa y consistente.

### Las 8 características de un buen requerimiento (Especificación, p. 6). Mnemotecnia: «**CVC-CNNTF**: *Con Valor Constante, Construye Nuevos Niveles Tan Firmes*»

1. **Claro:** se entiende sin esfuerzo, sin palabras vagas. ✗ «debe ser rápido» → ✓ «responde a las consultas en < 2 s».
2. **Verificable:** se puede comprobar si se cumple, con una medida. ✗ «interfaz amigable» → ✓ «el 90 % completa el registro en < 3 min».
3. **Consistente:** no contradice a otros requerimientos y usa una terminología uniforme. Ejemplo: «registro con email» frente a «registro solo con cédula». Se resuelve con el cliente.
4. **Completo:** incluye toda la información necesaria.
5. **No ambiguo:** una sola interpretación.
6. **Necesario:** aporta valor real.
7. **Trazable:** identificable en todo el ciclo de vida.
8. **Factible:** viable técnica y económicamente.

> **No confundir con las propiedades de la clase de Importancia (p. 5): son 8 «propiedades de buenos requerimientos»:** correcto, no ambiguo, completo, consistente, verificable, **rastreable**, **modificable** y **priorizable**.
> Si la pregunta dice «según la clase de especificación», usa la lista de arriba (claro… factible). Si dice «propiedades», incluye modificable y priorizable.

### La lista de 12 puntos (Plantilla de elicitación, sec. 11.1): la del deber

**9 características de la ISO/IEC/IEEE 29148 (cl. 5.2.5) y 3 del SWEBOK.**

| # | Característica | Criterio |
|---|---|---|
| 1 | Necesario | define una capacidad, restricción o factor de calidad **esencial** |
| 2 | Apropiado | nivel de detalle adecuado y **no impone diseño innecesario** |
| 3 | Inequívoco | una sola interpretación |
| 4 | Completo | se entiende **sin información adicional** |
| 5 | Singular | **una sola** capacidad o restricción |
| 6 | Factible | con riesgo aceptable dentro de las restricciones |
| 7 | Verificable | su cumplimiento se demuestra de forma objetiva |
| 8 | Correcto | representa con exactitud la necesidad de origen |
| 9 | Conforme | sigue la **plantilla y el estilo** acordados |
| 10 | Vinculante (SWEBOK) | el cliente lo **financia** y no quiere prescindir de él |
| 11 | Vocabulario (SWEBOK) | usa el **vocabulario de los interesados** |
| 12 | Aceptable (SWEBOK) | es aceptable para **todos** los interesados |

**Características del conjunto completo (sec. 11.2), son 7:**
- completo, sin TBD sin resolver;
- consistente;
- consistente con las fuentes;
- factible;
- comprensible;
- conciso;
- validable.

### Las 10 familias de palabras prohibidas (sec. 11.3; ISO 29148, cl. 5.2.7)

| Familia | Ejemplos |
|---|---|
| Superlativos | «el mejor», «el más» |
| Lenguaje subjetivo | «amigable», «fácil de usar», «rentable» |
| Pronombres vagos | «esto», «eso», «lo» |
| Adverbios y adjetivos ambiguos | «casi siempre», «significativo», «mínimo» |
| Conectores ambiguos | «o», «y/o»: mejor separar en dos requerimientos |
| Términos abiertos | «brindar soporte», «entre otros», «como mínimo» |
| Comparativos | «mejor que» |
| Vacíos o escapatorias | «si es posible», «según corresponda» |
| Totalidades | «todos», «siempre», «nunca» |
| Referencias incompletas | sin fecha, versión o sección |

### Los 5 porqués (sec. 11.4)

Cuando el usuario pide una **solución** («quiero un botón para exportar a Excel»), se pregunta «¿por qué?» varias veces hasta llegar al **problema real**. Se para cuando la respuesta es: «si no se hace, el problema del interesado no queda resuelto».

### Estructura básica de un requerimiento: 8 campos (Especificación, p. 11). Mnemotecnia: «**I-T-D-T-P-C-A-D**: *Íbamos Todos De Turismo Para Conocer Aves Distintas*»

1. **Identificador** único (RF-001).
2. **Título** corto.
3. **Descripción** detallada.
4. **Tipo** (F o NF).
5. **Prioridad** (alta, media, baja).
6. **Criterio de aceptación.**
7. **Actor** o *stakeholder*.
8. **Dependencias** o referencias.

**Ejemplo de la diapositiva (p. 12):**
- **ID:** RF-005.
- **Título:** recuperación de contraseña.
- **Descripción:** el sistema debe permitir al usuario recuperar su contraseña mediante un enlace enviado al correo registrado.
- **Tipo:** funcional.
- **Prioridad:** alta.
- **Criterio de aceptación:** el enlace llega en **< 60 s** y **expira a los 30 min**.
- **Actor:** usuario registrado.
- **Dependencias:** RF-001 (registro).

### Errores al especificar (p. 13): 7

1. Lenguaje ambiguo.
2. Mezclar requerimientos con soluciones técnicas.
3. Especificar la implementación en vez de lo que se necesita.
4. **Omitir los criterios de aceptación.**
5. Requerimientos contradictorios.
6. **Confundir requerimientos con funciones del competidor.**
7. No actualizar la especificación.

---

## 7. Representación (clase de Representación)

- **Por qué importa:** el mismo requerimiento se puede escribir de muchas formas, y la forma afecta la lectura, la comprensión de cada *stakeholder*, la trazabilidad y el uso en diseño y pruebas. Se alinea con la **ISO 29148**.
- **Las 3 formas vistas:**
  1. lenguaje natural estructurado;
  2. listas organizadas;
  3. tablas simples.

  **Otras formas:** modelos formales, diagramas (**casos de uso, BPMN**), *user stories* y prototipos.

| Forma | Qué es | Ventajas | Limitaciones | Para quién |
|---|---|---|---|---|
| **Lenguaje natural estructurado** | lenguaje natural **con plantilla** y **sintaxis controlada**. **La más común en la industria** | accesible para no técnicos, no requiere herramientas, facilita hablar con el cliente | ambiguo si no se sigue la plantilla, difícil de procesar automáticamente, repetitivo en proyectos grandes | **el cliente** |
| **Lista organizada** | ítems enumerados en orden lógico, agrupados por **módulo, tipo, actor o prioridad** | fácil de leer y mantener, visión general rápida, agrupación temática | **no muestra las relaciones**, no trae el detalle, **puede ocultar dependencias** | **visión general del proyecto** (el equipo) |
| **Tabla simple** | **fila = requerimiento, columna = atributo** (ID, título, descripción, tipo, prioridad, criterio, actor, dependencias, **estado**). Se usa en Excel, Jira y Confluence | información compacta, permite filtrar, ordenar y sacar reportes | detalle limitado por celda, difícil de leer cuando son muchos, exige disciplina con las columnas | **gestión y trazabilidad** (desarrollo y pruebas) |

**La plantilla del lenguaje natural estructurado (¡sale seguro en la práctica!):**

> **Cuando** [condición], **el sistema debe** [acción] [objeto] **para que** [beneficio].

Ejemplo de la clase: *Cuando un usuario olvida su contraseña, el sistema debe enviar un enlace de recuperación al correo registrado para que el usuario pueda definir una nueva contraseña.*

- **No son excluyentes:** un buen documento suele tener **las tres formas**. Se elige según **el lector y el propósito** (SWEBOK).
- **Buenas prácticas comunes:**
  - IDs únicos;
  - **glosario**;
  - numerar y versionar;
  - actualizar;
  - trazabilidad hasta la prueba;
  - revisar con el cliente;
  - **documentar las decisiones, no solo el resultado**.

> **Analogía Minecraft:**
> - **Lenguaje natural:** contarle a tu pana «cuando caiga la noche, la base debe prender antorchas para que no aparezcan mobs».
> - **Lista:** los capítulos de tu libro de construcción (granja, portal, defensa).
> - **Tabla:** la hoja de Excel con cada bloque, la cantidad y el estado.

---

## 8. Priorización (clase de Priorización): parte del análisis

- **Qué es priorizar:** decidir qué va primero, qué espera y qué se descarta. Es **negociación, no solo técnica**. Los recursos (tiempo, dinero, equipo) **siempre son limitados**.
- **Por qué priorizar (7 razones, p. 4):**
  - tiempo limitado;
  - presupuesto finito;
  - **riesgo:** hacer primero lo riesgoso para detectar problemas temprano;
  - *feedback* temprano;
  - satisfacción del *stakeholder*;
  - evitar el *scope creep*;
  - **los sprints ágiles lo requieren**.

### Los 3 criterios (pp. 5-7)

| Criterio | Mide | Preguntas clave | Ejemplo |
|---|---|---|---|
| **Valor de negocio** | beneficio para el usuario, el negocio o la organización | ¿resuelve un problema crítico?, ¿genera ingresos o reduce costos?, ¿a cuántos beneficia?, ¿diferencia?, **¿es legal u obligatorio?**, ¿mejora la retención, la conversión o el NPS? | pagos > tema oscuro |
| **Complejidad técnica** | dificultad: tiempo, esfuerzo, **riesgo**, dependencias | ¿tecnología nueva?, ¿cambia la arquitectura?, ¿cuántas personas? | pasarela de pago > color de botón |
| **Impacto** | consecuencias de hacerlo **o de NO hacerlo** | alcance, **urgencia** (fecha límite), **efecto dominó** (habilita otros), satisfacción | un *bug* que impide comprar = alto |

### MoSCoW (p. 8)

| Categoría | Significado | Ejemplo de *e-commerce* |
|---|---|---|
| **Must have** | obligatorio; **sin esto no funciona** | carrito, pago, registro |
| **Should have** | importante, pero **no esencial para el lanzamiento** | filtros avanzados, *wishlist*, reseñas |
| **Could have** | deseable **si hay tiempo y presupuesto** | modo oscuro, compartir en redes, cupones |
| **Won't have (this time)** | descartado **para esta versión**; podría entrar después | app nativa, lealtad, chat en vivo |

**Regla: los Must ≤ 60 % del esfuerzo total.** Si se pasa, se reclasifica (un Must baja a Should).

> **Analogía Valorant (compra de ronda):**
> - **Must:** el arma principal y el escudo, porque sin eso pierdes la ronda.
> - **Should:** las habilidades completas.
> - **Could:** la *skin* nueva.
> - **Won't (this time):** el Operator en una ronda de *eco*.
>
> Y la regla del 60 %: si gastas todo en el arma, no te queda para el escudo.

### Modelo Kano (p. 9)

| Categoría | Descripción | Ejemplo |
|---|---|---|
| **Básicos** | **se esperan**. Su ausencia molesta y su presencia **no** deleita | la app no se cae, los pagos funcionan |
| **De rendimiento (lineales)** | **más = mejor**, la satisfacción crece en proporción | velocidad de carga, variedad de productos |
| **De deleite (atractivos)** | **no esperados**, sorprenden | recomendaciones con IA, animaciones, probador con RA |
| **Indiferentes** | no le importan al usuario | la tecnología del *backend*, la versión de la BD |
| **Inversos** | su presencia **genera insatisfacción** | anuncios invasivos, notificaciones excesivas |

**Cómo se aplica (enunciado del deber):**
- dos preguntas por función: «¿cómo se sentiría si **tuviera**…?» (funcional) y «…si **NO tuviera**…?» (disfuncional);
- 5 respuestas: **Me gusta, Lo espero, Me es indiferente, Puedo tolerarlo, Me disgusta**.

**Tabla de evaluación (fila = respuesta con la función presente; columna = respuesta con la función ausente):**

| Presente ↓ / Ausente → | Me gusta | Lo espero | Indiferente | Tolerarlo | Me disgusta |
|---|---|---|---|---|---|
| **Me gusta** | C | D | D | D | **R** |
| **Lo espero** | Inv | I | I | I | **B** |
| **Indiferente** | Inv | I | I | I | **B** |
| **Tolerarlo** | Inv | I | I | I | **B** |
| **Me disgusta** | Inv | Inv | Inv | Inv | C |

**Cómo memorizar la tabla:**
- **Última columna (ausente = me disgusta):** arriba **R**, en el medio **B, B, B** y abajo **C**.
- **Primera fila (presente = me gusta):** **C** y luego **D, D, D**, terminando en **R**.
- **Primera columna (bajo «Me gusta» ausente):** puro **Inv**.
- **Última fila (presente = me disgusta):** **Inv** y al final **C**.
- **El centro (3 × 3):** todo **I**.
- **Las esquinas C:** «me gusta / me gusta» y «me disgusta / me disgusta» son contradictorias y se descartan.

> **Analogía Genshin:**
> - **Básico:** que el juego guarde tu progreso. Nadie lo celebra, pero si falla, desinstalas.
> - **Rendimiento:** los FPS, porque más es mejor.
> - **Deleite:** la primera vez que viste a Paimon cocinar o un evento con minijuego.
> - **Indiferente:** el motor gráfico que usa.
> - **Inverso:** las notificaciones de *push* cada hora.

### Matriz valor contra esfuerzo (p. 10)

|  | **Bajo esfuerzo** | **Alto esfuerzo** |
|---|---|---|
| **Alto valor** | **Quick wins**: hacer primero, **máximo ROI** | **Proyectos estratégicos**: planificar y **dividir en fases** |
| **Bajo valor** | **Fill-ins**: si sobra tiempo | **Evitar**: no vale la inversión |

**Orden de implementación:** 1) quick wins → 2) estratégicos → 3) fill-ins → 4) evitar. En el deber, el **esfuerzo alto** es el que supera el **promedio** de horas.

### Conflictos entre requerimientos (p. 11): ejemplos

- seguridad (2FA, sesiones cortas) **frente a** facilidad (recordar la sesión);
- marketing (muchos datos) **frente a** legal (minimización, GDPR o, aquí, **LOPDP**);
- muchas funciones **frente a** poco tiempo;
- dos departamentos que quieren el mismo equipo;
- animaciones **frente a** carga en < 2 s.

### Resolución de conflictos (p. 12): 7 vías

1. Negociación directa.
2. **Priorización objetiva** (datos, no opiniones).
3. **Compromiso o *trade-off*:** cada uno cede. Ejemplo: 2FA solo en transacciones.
4. **Escalamiento:** el *sponsor* o el *product owner* decide.
5. Solución técnica creativa.
6. **Prototipado:** dos versiones probadas con usuarios.
7. **Documentar la decisión:** qué, por qué y quién aprobó.

### Errores al priorizar (p. 13): 7

1. **Por quién grita más fuerte.**
2. Todo con prioridad alta.
3. Solo por valor, sin ver la complejidad.
4. **Ignorar las dependencias:** uno de baja prioridad puede ser prerrequisito de uno de alta.
5. No involucrar al equipo técnico.
6. **No volver a priorizar** en cada sprint.
7. Priorizar por intuición.

---

## 9. Las plantillas: lo práctico que puede caer

### Plantilla de elicitación y análisis (la de la tesis): secciones que se nombran

- **Fichas de interesado.**
- **Plan de elicitación.**
- **Fichas de sesión.**
- **Necesidades.**
- **Requerimientos** con su estado: *propuesto, analizado, validado, aprobado o descartado*.
- **Restricciones.**
- **Características de calidad críticas** (ISO 25010).
- **Verificación individual (12 puntos)** y **verificación del conjunto (7)**.
- **Revisión del lenguaje.**
- **5 porqués.**
- **Conflictos.**

El proceso es **iterativo**: se vuelve atrás con información nueva. **Toda necesidad debe rastrearse hasta su fuente.**

### TP de Representación: caso de la app de transporte público de Quito

- Se eligen **5 RF** de la lista acordada y se proponen **5 RNF** a partir de las condiciones del caso:
  - horas pico;
  - uso en la parada con **datos móviles y celulares de gama baja o media**;
  - **adultos mayores y personas con discapacidad visual**;
  - **datos personales con la LOPDP**;
  - fecha de lanzamiento **sin caídas**.
- **Luego se representan de tres formas:**
  - **lista** por módulo, para el equipo;
  - **lenguaje natural estructurado** con la plantilla «Cuando / el sistema debe / para que» en 5 de ellos (al menos 1 RNF), para el **Municipio**;
  - **tabla** con ID, título, tipo, prioridad y criterio medible, para el equipo de desarrollo y pruebas.
- **Al final se hace la verificación** con 3 criterios (**Claro, Verificable y Consistente**: Sí o No) y la corrección aplicada.
- **Ejemplo de la plantilla:** «Cuando el Municipio registre un cierre de vía que afecte a una ruta, el sistema debe enviar una notificación a los usuarios que siguen esa ruta en un plazo máximo de 10 minutos para que puedan cambiar su recorrido antes de llegar a la parada».
- **Ejemplo de RNF en tabla:** «El mapa con las paradas cercanas carga en menos de 3 segundos en el 95 % de las consultas, con conexión 4G».

> Las prácticas resueltas están en `Practica_IR_Resuelta.md`. Ese es el tipo de ejercicio que esperas el jueves.

---

## 10. Las 20 cosas que sí o sí debes saber

1. Definición de requerimiento según la IEEE 610.12 («condición o capacidad…») y según el SWEBOK («propiedad que debe exhibir el software…»).
2. RF = **qué hace**. RNF = **cómo lo hace** (cualidades). De dominio = el negocio o la ley. Emergente = la interacción entre componentes.
3. Las 6 familias de RNF: rendimiento, seguridad, usabilidad, disponibilidad, escalabilidad y mantenibilidad.
4. El SWEBOK es de la **IEEE Computer Society**, tiene **15 áreas** y requerimientos es una de ellas. La norma asociada es la **ISO/IEC/IEEE 29148:2018**.
5. **5 etapas:** elicitación → análisis → especificación → validación → gestión.
6. **SDLC de 7 fases**, con el efecto dominó.
7. **1-10-100:** 1x, 5x, 10x, 20x, 100x.
8. **Goldplating** = agregar lo que nadie pidió. **Scope creep** = el alcance crece sin control.
9. «Debe usar MySQL» es un **requerimiento como solución**: está mal.
10. **Entrevista:** profundidad. **Encuesta:** amplitud. **Observación:** lo que hace, no lo que dice.
11. **Focus group:** 6 a 10 personas, moderador neutral. **Brainstorming:** no criticar, cantidad antes que calidad.
12. **Prototipos** de baja fidelidad (papel, *wireframe*) y de alta (*mockup* interactivo).
13. Las **8 características** de la clase de especificación: claro, verificable, consistente, completo, no ambiguo, necesario, trazable y factible.
14. Los **8 campos** de un requerimiento: ID, título, descripción, tipo, prioridad, criterio de aceptación, actor y dependencias.
15. La plantilla **«Cuando… el sistema debe… para que…»**.
16. **Lista** = visión general. **Tabla** = gestión y trazabilidad. **Lenguaje natural** = el cliente. Se combinan.
17. **MoSCoW** y la regla de **Must ≤ 60 %**. «Won't» significa **this time**.
18. **Kano:** básico, rendimiento, deleite, indiferente, inverso, más la tabla y la C de cuestionable.
19. **Matriz:** quick win → estratégico → fill-in → evitar.
20. Conflictos: negociar, datos, *trade-off*, escalar, solución creativa, prototipar y **documentar la decisión**.

---

## Anexo. Plantilla Problem Statement (PMBOK), material de la Unidad 1

Sirve para **definir el problema antes de pedir requerimientos**. Sus secciones, en orden:

1. **Definición del problema:** qué es, cómo surgió y por qué hay que atenderlo. Tiene que ser específica, medible y relevante para los objetivos.
2. **Antecedentes:** el origen, los factores y los datos históricos.
3. **Alcance:** qué incluye y qué excluye, qué áreas afecta y qué restricciones hay.
4. **Impacto actual o potencial**, con métricas cualitativas y cuantitativas. La tabla tiene tres columnas: área de impacto, descripción y métrica. Por ejemplo, financiero en $ u operativo en horas de parada.
5. **Interesados afectados:**
   - **Registro de interesados:** nombre, rol, **poder**, **interés** y contacto.
   - **Mapa de interesados:** la matriz **poder (influencia) contra interés**.
6. **Tiempo del problema** (cuándo empezó y si empeora) y **lugar** (área, sede o entorno virtual).
7. **Análisis de brechas (*gap analysis*):** **estado actual → estado deseado → acciones requeridas**.
8. **Causa raíz:** **5 porqués**, **diagrama de espina de pescado** (Ishikawa) o análisis causa-efecto.
9. **Datos y evidencia de respaldo.**

**Matriz poder contra interés (la del mapa de interesados):**

|  | Interés bajo | Interés alto |
|---|---|---|
| **Poder alto** | **Mantener satisfecho** (*keep satisfied*) | **Gestionar de cerca** (*manage closely*) |
| **Poder bajo** | **Monitorear** (*monitor*) | **Mantener informado** (*keep informed*) |

> **Analogía de compras:** el gerente financiero que aprueba la orden de compra tiene **poder alto e interés alto**, así que se gestiona de cerca. El proveedor que solo espera la orden tiene **poder bajo e interés alto**, así que se mantiene informado.
