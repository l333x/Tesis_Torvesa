---
titulo: Guía de puntos para armar la elicitación y análisis de requerimientos
fecha: 2026-10-29
version: v1.0
base: 2026-10-27_Elicitacion_Requerimientos_v0.1.md (borrador completo, solo de consulta)
asignatura: Ingeniería de Requerimientos, Usabilidad y UX
uso: Víctor y Diego redactan el documento con sus palabras; esta guía da los puntos y el respaldo de cada sección
tags: [requerimientos, elicitacion, guia, iso29148, swebok]
---

# Guía de puntos · Elicitación y análisis de requerimientos

> **Cómo se usa esta guía.** Por cada sección de la plantilla hay cuatro cosas: **qué pide**, **los puntos que ustedes escriben con sus palabras**, **de dónde sale cada dato** y **un cuidado**. No es un texto para copiar: son los puntos, ya revisados, para que ustedes redacten. Cada dato tiene su respaldo, así que nada queda inventado.

> ⚠ **Regla de honestidad.** Lo que ya se hizo se escribe en pasado: el censo de TEAMSLASH, la prueba del MVP, la revisión de documentos, el análisis de herramientas y el proceso actual. Lo que todavía no se hace en Torvesa (entrevistas, encuestas, observación y taller) se escribe en futuro, como **planificado**. Las cifras del antecedente (más de 24 h de respuesta y USD 15.000 por cliente perdido) van como **hipótesis**, nunca como dato medido.

## Reparto sugerido

| Secciones | Quién la redacta | Por qué |
|---|---|---|
| 0, 1, 2, 3, 4 y 9 | Víctor | Problema, negocio, interesados y necesidades |
| 5, 6, 7 y 8 | Víctor y Diego | Fuentes, técnicas, sesiones y escenarios: los dos estuvieron |
| 10, 11 y 13 | Diego | Requerimientos, análisis y trazabilidad: es la parte técnica |
| 12, 14, 15 y 16 | Los dos, al final | Validación, pendientes, firmas y anexos |

**Fechas que se usan en todo el documento:** la validación del diseño en operación experimental controlada va del **24-nov al 5-dic-2026** (la capacitación es el 23-nov). La revisión con la tutora es el **29-oct-2026**. La entrega final es el **4-ene-2027**.

## 0. Datos generales

**Qué pide:** la ficha del proyecto y el control de versiones.

**Puntos:**
- Título, carrera (Negocios Digitales, UPS Quito), estudiantes, tutora (Ing. Tania Chicaiza) y empresa (Torvesa Constructora, Quito).
- Inicio en dos tiempos: **mayo de 2026** (proyecto integrador TEAMSLASH) y **octubre de 2026** (tesis).
- Versión 0.1. La 1.0 se declara después del taller con Torvesa.

**Respaldo:** diseño de titulación aprobado (29-sep-2026).

## 1. Introducción

**Qué pide:** propósito, alcance, glosario y documentos de referencia.

**Puntos:**
- **Propósito:** obtener requerimientos claros, priorizados y trazables, que sirvan para diseñar el sistema (OE2) y el prototipo (OE3).
- **Alcance:** los cuatro componentes del sistema:
  - el CRM móvil TEAMSLASH, que ya existe como MVP;
  - la bóveda de conocimiento (Obsidian);
  - el asistente de IA, que propone borradores;
  - el registro verificable (huellas SHA-256).
- **No cubre:** la especificación completa (SRS), la arquitectura detallada ni la construcción.
- **Glosario mínimo:** solicitud, primer contacto, fuga, cotización, bóveda, ficha de cliente, RAG, LLM, huella SHA-256, SUS, LOPDP y metas M1–M6.

**Respaldo:** diseño aprobado; el glosario de la tesis.

**Cuidado:** en todo el documento se dice «validación del diseño en operación experimental controlada». Nunca «piloto» ni «implementación».

## 2. Análisis del problema u oportunidad

**Qué pide:** el problema, el contexto, los objetivos del negocio, las alternativas, la elegida, el alcance y las restricciones.

**Puntos del problema (2.1):**
- Las solicitudes llegan al **WhatsApp personal** de socios e ingenieros, que pasan mucho tiempo en obra.
- Nadie se entera a tiempo y no hay un responsable claro.
- Cada cotización se arma casi desde cero.
- El historial del cliente vive en el celular y en la memoria del vendedor («amnesia institucional»).
- Consecuencia: clientes que esperan, clientes que se van sin que quede registrado el motivo y una gerencia que no sabe cuántas cotizaciones están en curso.

**Puntos del contexto (2.2):**
- Torvesa: Quito, activa desde 2010, construcción de vías y obra civil (RUC en el SRI).
- 30 colaboradores y 33 clientes en cartera. Son cifras **por confirmar** con la nota de la gerencia.
- No hay un sistema comercial: se usan WhatsApp, redes, teléfono y correo.
- **Antecedente propio:** el MVP TEAMSLASH (formulario web, API propia, registro con semáforo y alertas en Slack con el botón «Ver ficha»).

**Objetivos del negocio (2.3):** son 7, uno por cada meta.

| Objetivo | Se mide con |
|---|---|
| Responder rápido | M1: mediana del primer contacto menor a 15 min (es una meta de diseño) |
| Cotizar en menos tiempo | M2: menos que la línea base |
| No perder clientes antes del primer contacto | M3: menos fuga que la línea base |
| El historial es de la empresa | M4: prueba de recuperación |
| Historial que no se puede alterar sin que se note | M5: 100 % de alteraciones detectadas |
| Uso desde el celular en obra | M6: SUS ≥ 68 |
| Cumplir la LOPDP | Lista de verificación sin hallazgos |

**Alternativas (2.4):** cuatro, cada una con una ventaja y una desventaja.

| Alternativa | A favor | En contra |
|---|---|---|
| A. CRM comercial (HubSpot, Zoho, Pipedrive, Kommo) | Producto maduro, con app móvil | No trae la bóveda ni el registro verificable; los datos quedan en la nube del proveedor |
| **B. TEAMSLASH + bóveda + IA + registro (elegida)** | Es el diseño aprobado y reutiliza el MVP | Más integración propia |
| C. App nativa a medida | Control total | Cara y no cabe en el plazo |
| D. Sin software nuevo (WhatsApp Business y una hoja) | Casi gratis | No guarda el historial ni mide tiempos |

**Por qué B (2.5):** es la única que cubre los 7 objetivos. De la D se toma una idea: registrar a mano, rápido, lo que llega por WhatsApp.

**Alcance (2.6):**
- **Entra:** captación de solicitudes, alerta, responsable y estados, bóveda, borradores con IA revisados por una persona, registro verificable, reporte semanal y controles LOPDP.
- **No entra:** facturación, avance de obra, contratación pública, envío automático sin revisión, API oficial de WhatsApp y app nativa.

**Restricciones (2.7):** plazo del período 69; dos estudiantes; presupuesto bajo; tecnologías fijadas por el diseño aprobado; LOPDP; el campo depende de que Torvesa autorice.

**Respaldo:** Informe Final de TEAMSLASH (22-jul-2026); RUC de Torvesa; inventario de herramientas v0.2 (páginas oficiales de precios, 21 y 25-oct-2026); proceso actual (AS-IS) v0.1.

## 3. Planificación de la elicitación

**Qué pide:** la estrategia, el cronograma, los recursos y la ética.

**Puntos (3.1):** dos iteraciones, porque la norma dice que la elicitación es iterativa.
- **Iteración 1 (mayo–julio 2026, hecha):** censo a 5 personas y prueba del MVP.
- **Iteración 2 (octubre–noviembre 2026):**
  - lo hecho, sin depender de la empresa: documentos, herramientas y proceso actual;
  - lo planificado en Torvesa: entrevistas, encuestas, observación y taller.
- Los conflictos se resuelven en el taller con la gerencia, nunca de forma unilateral.

**Cronograma (3.2):**

| Actividad | Estado | Cuándo |
|---|---|---|
| Censo a 5 personas | Hecho | Mayo 2026 |
| Prueba del MVP | Hecho | Julio 2026 |
| Revisión de documentos y literatura | Hecho | 11–25 oct |
| Análisis de herramientas | Hecho | 19–25 oct |
| Proceso actual en BPMN | Hecho, sin validar | 25 oct |
| Revisión con la tutora | Hecho / por registrar | 29 oct |
| Entrevistas, observación, muestra de solicitudes y encuestas | Planificado | Semana siguiente a la autorización |
| Taller de validación | Planificado | Al cerrar las entrevistas |

**Recursos (3.3):** guía de entrevista, cuestionarios, hoja de cronometraje, consentimiento, BPMN y pantallas de baja fidelidad.

**Ética (3.4):**
- consentimiento informado (LOPDP, art. 8);
- se graba solo con permiso;
- respuestas con códigos;
- los datos personales no se suben a la nube;
- la empresa recibe solo resultados agregados;
- de la muestra de solicitudes se anotan solo fechas y horas.

**Respaldo:** ISO/IEC/IEEE 29148 (2018, cl. 5.3); SWEBOK v4 (sec. 7.1); LOPDP (2021, art. 8); consentimiento C1 v0.2.

## 4. Interesados

**Qué pide:** criterio, clases, fichas y matriz de poder e interés.

**Puntos:**
- **Criterio:** todo el que participa, se ve afectado o puede influir, en todo el ciclo de vida del sistema (SWEBOK, sec. 2.1).
- **Las 9 clases:**

| Código | Interesado | Poder / interés |
|---|---|---|
| INT-01 | Gerencia (decide y financia) | Alto / alto |
| INT-02 | Quienes reciben solicitudes (en obra) | Medio / alto |
| INT-03 | Quienes preparan cotizaciones | Medio / alto |
| INT-04 | Otros colaboradores | Bajo / medio |
| INT-05 | Clientes (dueños de sus datos) | Medio / medio |
| INT-06 | Equipo de tesis (Víctor y Diego) | Alto / alto |
| INT-07 | Tutora | Alto / medio |
| INT-08 | Superintendencia de Protección de Datos | Alto / bajo |
| INT-09 | Proveedores (Obsidian, Slack, IA, Railway, Vercel) | Medio / bajo |

- **Matriz de poder e interés:**
  - gestionar de cerca: INT-01 e INT-06;
  - mantener satisfechos: INT-07 e INT-08;
  - mantener informados: INT-02 e INT-03;
  - monitorear: el resto.
- **Sesgo que ustedes mismos detectan:** el censo de la iteración 1 fue solo a gerencia y operación (5 personas). Se corrige con las encuestas a los 30 colaboradores y a los 33 clientes.

**Cuidado:** en las fichas basta con 4 datos por interesado: qué espera, qué le preocupa, cuándo está disponible y con qué técnica se le consulta.

## 5. Fuentes no humanas

**Qué pide:** los documentos y sistemas de donde salen requerimientos.

**Puntos (listar con su fecha):**
- diseño aprobado (29-sep);
- Informe Final de TEAMSLASH (22-jul);
- pitch deck b y c (22-jul);
- manual de usuario de TEAMSLASH (10-jul);
- el MVP desplegado;
- AS-IS v0.1;
- RUC del SRI;
- LOPDP y su reglamento;
- Ley de Comercio Electrónico;
- norma SHA-256 (NIST FIPS 180-4);
- ISO/IEC 25010;
- matriz de afirmaciones;
- inventario de herramientas;
- escala SUS en español.

**Cuidado:** el informe dice que TEAMSLASH guarda en **Google Sheets** y el pitch dice **PostgreSQL**. Diego lo confirma. Mientras tanto se escribe «por confirmar».

## 6. Técnicas de elicitación

**Qué pide:** qué técnica, para qué y por qué; dificultades y cómo se enfrentan.

**Puntos (una línea por técnica):**
- **Entrevista en censo:** validar que el problema existe (n = 5).
- **Prototipo (MVP):** descubrir lo que el usuario no dice. De ahí salió el botón «Ver ficha».
- **Análisis de documentos:** normativa y requisitos de calidad.
- **Análisis de herramientas:** comparar soluciones y precios.
- **Modelado BPMN:** ver dónde se pierde tiempo.
- **Entrevista semiestructurada:** causas de las demoras (planificada).
- **Encuesta censal:** opinión de colaboradores y clientes (planificada).
- **Observación con cronómetro:** lo que se hace, no solo lo que se dice (planificada).
- **Taller con prototipo de papel:** validar y priorizar (planificado).

**Dificultades y respuesta:**

| Dificultad | Qué hacemos |
|---|---|
| Torvesa aún no autoriza | Avanzar con lo que no depende de ella y pedir una carta de la tutora |
| Personal en obra | Entrevistas cortas (30–40 min) en la oficina |
| «Siempre se ha hecho así» | Observar y recorrer el AS-IS paso a paso |
| Piden soluciones en vez de problemas | 5 porqués |
| Sesgo nuestro (ya hicimos TEAMSLASH) | Preguntas abiertas antes de mostrar el prototipo |

## 7. Registro de sesiones

**Qué pide:** una ficha por sesión realizada.

**Puntos (solo las 5 hechas):**

| Sesión | Qué fue | Lo que encontramos | Evidencia |
|---|---|---|---|
| SES-01 · Mayo 2026 | Censo a 5 personas | Más de la mitad de la jornada en obra; el 40 % revisa mensajes cada 3–4 h; 4 de 5 reciben clientes en su WhatsApp personal; 4 de 5 creen que el cliente «se enfría» en menos de 15 min; 4 de 5 piden un módulo de avance de obra | Informe Final, pp. 9–10, Tabla 1 |
| SES-02 · Julio 2026 | Prueba del MVP, 10 envíos | Alerta en 3,2 s de promedio; 10 de 10 registrados; primer contacto de 4 a 11 min en simulacros; salir de Slack para buscar al cliente hacía perder tiempo, así que se agregó «Ver ficha» | Informe Final, pp. 23–24, Tabla 3 |
| SES-03 · 11–25 oct | Documentos y literatura | 93 fuentes verificadas; la LOPDP exige consentimiento y plazos; **ninguna fuente respalda un plazo exacto de respuesta**, así que los 15 min son una meta de diseño | Matriz de afirmaciones |
| SES-04 · 19–25 oct | Herramientas | Solo Kommo trae WhatsApp oficial, con un contrato mínimo de 6 meses; Obsidian es gratis para uso comercial; la IA elegida no entrena con los datos | Inventario v0.2 |
| SES-05 · 25 oct | Proceso actual (BPMN) | 5 puntos de pérdida: espera, asignación informal, cotización desde cero, seguimiento de memoria e historial en celulares | AS-IS v0.1 |

**Cuidado:** las sesiones SES-06 a SES-11 (Torvesa) se nombran como **planificadas**, sin hallazgos.

## 8. Contexto de uso y escenarios

**Qué pide:** dónde y cómo se usa el sistema, quiénes lo usan, escenarios y casos de uso.

**Puntos de contexto:**
- **Dónde:** oficina en Quito y obras con mala señal.
- **Con qué:** el celular personal; la computadora solo en la oficina.
- **Cuándo:** las solicitudes llegan a cualquier hora y en obra el celular se revisa a ratos.
- **Riesgos del entorno:** pérdida del celular, caídas de servicios y fuga de datos por chats personales.
- **Usuario típico en obra:** usa mucho WhatsApp y tiene poco tiempo. Necesita pantallas que se lean de un vistazo y un solo toque.

**Los 8 escenarios:** basta una frase con inicio, acción y resultado.
- **Escenario 1.** Llega un formulario y el coordinador está en obra: alerta, «Ver ficha», llama. Primer contacto en menos de 15 min.
- **Escenario 2.** El cliente escribe al WhatsApp personal: el ingeniero lo registra en 1 minuto o le manda el enlace del formulario.
- **Escenario 3.** Cotización con el asistente: borrador con plantillas y cotizaciones anteriores, que una persona revisa antes de enviar.
- **Escenario 4.** El vendedor no está: otro colaborador busca al cliente y lee su historial.
- **Escenario 5.** El lunes, la gerencia ve el reporte de la semana.
- **Escenario 6.** Un cliente reclama otro precio: se verifica la huella de la cotización enviada.
- **Escenario 7.** Pasan 15 min sin atender: recordatorio al responsable y aviso a la gerencia.
- **Escenario 8.** El cliente pide borrar sus datos: se borran y el registro conserva solo códigos.

**Casos de uso:** 11, de CU-01 «Enviar solicitud» a CU-11 «Ejercer derechos sobre sus datos». Diego los dibuja en el diagrama.

## 9. Necesidades

**Qué pide:** la lista de necesidades, con su origen y prioridad.

**Puntos (15 necesidades, una frase cada una):**

| Prioridad | Necesidades |
|---|---|
| Alta | Enterarse a tiempo en obra · un registro único fuera de los WhatsApp personales · saber el responsable y el estado · cotizar sin empezar de cero · recuperar el historial sin el vendedor · usar el celular con mala señal · ficha a un toque · proteger los datos · costo bajo · medir M1–M6 |
| Media | Motivos de pérdida cada semana · probar quién atendió y qué se ofreció · recordar el seguimiento de cotizaciones (en análisis) · reportes para la gerencia |
| Descartada | Módulo de avance de obra con fotos: es gestión de obra, no atención comercial |

**Cómo se priorizó:** cuántos la pidieron en el censo, si se liga a una meta (M1–M6) y el riesgo de no atenderla.

**Respaldo:** SES-01 a SES-05 (sección 7).

## 10. De necesidades a requerimientos

**Qué pide:** restricciones, calidad, cómo se redacta y la lista de requerimientos.

**Restricciones (las 9, una línea cada una):**
- construir sobre TEAMSLASH;
- bóveda en Obsidian;
- huella SHA-256 sin cadena de bloques;
- cumplir la LOPDP;
- validación del 24-nov al 5-dic;
- dos estudiantes y poco presupuesto;
- mala señal en obra;
- no usar los datos simulados;
- Obsidian no da permisos por usuario.

**Calidad (ISO/IEC 25010):** seguridad, fiabilidad, usabilidad, mantenibilidad y eficiencia.

**Fórmula para redactar:**
> [Condición] [Sujeto] **deberá** [Acción] [Objeto] [Criterio medible]
> Ejemplo: «Cuando se registre una solicitud, el sistema **deberá** enviar una alerta al celular del responsable en un máximo de 5 segundos».

**Palabras prohibidas:** rápido, amigable, fácil, todos, siempre, si es posible, entre otros. No se pueden comprobar.

**Los 23 requerimientos, agrupados:** ustedes redactan cada uno con la fórmula.

| Grupo | Requerimientos (idea corta) |
|---|---|
| Captación y alerta (RQ-01 a RQ-08) | Registrar la solicitud con hora (≤ 5 s) · alerta con enlace a la ficha (≤ 5 s) · registro manual de WhatsApp (≤ 1 min) · un solo responsable · 5 estados (Nueva, En contacto, Cotizada, Ganada, Perdida) · recordatorio a los 15 min · motivo obligatorio si se pierde · reporte cada lunes |
| Bóveda (RQ-09, RQ-10, RQ-13, RQ-14) | Ficha por cliente con código · plantillas por tipo de obra · búsqueda por código, nombre u obra · ver fichas sin conexión |
| Asistente de IA (RQ-11, RQ-12, RQ-21) | Borrador que cita los documentos usados · ningún envío sin revisión humana · al LLM solo se mandan códigos, nunca nombres ni teléfonos |
| Registro verificable (RQ-15 a RQ-17) | Cada evento con su huella y la del anterior · verificación que señala lo alterado · sin datos personales |
| Datos y acceso (RQ-18 a RQ-20) | Consentimiento en el formulario · borrar los datos de prospectos perdidos al cumplir el plazo · solo cuentas individuales autorizadas |
| Usabilidad y proyecto (RQ-22, RQ-23) | SUS ≥ 68 · validación de dos semanas con solicitudes reales |

**Tipos:** 14 funcionales, 4 de calidad, 4 normativos y 1 del proyecto.

**Ficha de cada requerimiento (10.6):** la plantilla pide una ficha por requerimiento. Para no repetir 23 fichas largas, basta una tabla con estas columnas y una nota con lo que es igual para todos:
- **En la tabla:** código, enunciado, tipo, necesidad de origen, fuente o interesado, escenario, criterio de aceptación y método de verificación (inspección, análisis, demostración o prueba).
- **En la nota común:**
  - versión 0.1 y estado «Propuesto»;
  - propietario: Víctor en los de negocio y Diego en los técnicos;
  - estabilidad media en RQ-05, RQ-06, RQ-07 y RQ-19, porque dependen del taller, y alta en los demás.
- **Ojo con RQ-23:** la validación es del **24-nov al 5-dic**. El borrador v0.1 todavía dice 23-nov.

## 11. Análisis de requerimientos

**Qué pide:** revisar cada requerimiento y el conjunto, depurar el lenguaje, los 5 porqués, la calidad, los modelos, los conflictos y la priorización.

**Puntos:**
- **Requerimientos con observación:**
  - RQ-05 (estados) y RQ-06 (aviso a la gerencia): se acuerdan en el taller;
  - RQ-07: falta la lista de motivos;
  - RQ-10: falta el catálogo de obras;
  - RQ-11 (IA): riesgo alto, por eso va siempre con revisión humana;
  - RQ-19: falta el plazo de conservación.
- **El conjunto:** todavía **no está completo**, porque falta el campo. Es consistente y factible si Torvesa autoriza a tiempo.
- **Lenguaje corregido del antecedente** (ejemplos buenos para mostrar):
  - «apenas ingrese» → «en un máximo de 5 segundos»;
  - «fricción cero» → «SUS ≥ 68»;
  - «ningún lead se pierda» → «recordatorio a los 15 min y fuga medida».
- **5 porqués:**
  - «queremos alertas en Slack» → el problema real es que **el conocimiento comercial no es de la empresa**;
  - «queremos un módulo de avance de obra» → es gestión de obra, así que queda fuera.
- **Calidad de servicio (11.5):** para cada meta con número se ponen tres niveles: el mínimo aceptable (punto de falla), el que se busca (objetivo) y aquel a partir del cual mejorar ya no aporta (punto de perfección).

| Requerimiento | Falla | Objetivo | Perfección |
|---|---|---|---|
| RQ-02 · alerta | Más de 60 s | ≤ 5 s (en la prueba del MVP salió 3,2 s) | ≤ 1 s |
| RQ-06 / M1 · primer contacto | Igual o peor que la línea base | < 15 min (meta de diseño) | < 5 min |
| RQ-13 / M4 · recuperar historial | Igual o peor que la línea base | ≤ 2 min (propuesta a validar) | ≤ 30 s |
| RQ-11 / M2 · cotizar | Igual o peor que la línea base | Menos que la línea base | — |
| RQ-22 / M6 · usabilidad | SUS < 68 | SUS ≥ 68 | SUS ≥ 80 |

Relación que hay que mencionar: más avisos mejoran el tiempo de respuesta, pero saturan de mensajes, y eso baja la usabilidad.
- **Modelos (11.6):**
  - **AS-IS en BPMN (hecho):** mostró los 5 puntos de pérdida y que el seguimiento no tenía meta.
  - **Casos de uso y modelo conceptual (Diego, por dibujar):** el modelo conceptual tiene Cliente, Solicitud, Asignación, Estado, Cotización, Plantilla, Evento y Huella. El Evento nombra al cliente solo con su código.
  - **TO-BE:** se hace en el sprint de diseño (2–8 nov).
- **Conflictos (6):** estados de la solicitud · canal WhatsApp frente al formulario · control de la gerencia frente a la privacidad · Google Sheets o PostgreSQL · IA en la nube frente a los datos personales · aviso a la gerencia a los 15 min.
- **Priorización:** Prioridad = Valor × (1 − Riesgo) / Costo (SWEBOK, sec. 7.2).
  - **Alta (9):** registro, alerta, revisión humana, registro sin datos personales, consentimiento, solo códigos al LLM, registro manual, responsable y estados.
  - **Media (10)** y **baja (3)**. RQ-23 (la duración de la validación) es del proyecto y no se prioriza.
  - **Ajuste que hay que explicar:** la IA (RQ-11) y el registro de solo agregar (RQ-15) salen con prioridad baja por costo y riesgo, pero **se mantienen** porque son parte del objetivo aprobado por la carrera. El plazo de conservación (RQ-19) se mantiene porque lo exige la ley.
- **Lo que se quita o se difiere:** avance de obra · API oficial de WhatsApp · envío automático · app nativa.

**Respaldo:** SWEBOK v4 (secs. 5 y 7.2); ISO/IEC/IEEE 29148 (2018, cl. 6.3.3.4); LOPDP (art. 10, lit. i).

## 12. Validación

**Qué pide:** cómo se validan los requerimientos y el registro de cada validación.

**Puntos:**
- **1 · Prototipo (julio 2026):** aprobado con cambios (botón «Ver ficha»). **Hecho.**
- **2 · Revisión con la tutora (29-oct):** se anota lo que dijo. **Hecho / por registrar.**
- **3 · Taller con la gerencia:** recorrer los 8 escenarios y después mostrar las pantallas de papel. **Planificado.**
- **4 · Casos de prueba y validación de dos semanas:** comprueban los criterios de aceptación. **Planificado.**

## 13. Trazabilidad

**Qué pide:** una tabla que una cada objetivo con su necesidad, su requerimiento y su prueba.

**Puntos:**
- Una fila por objetivo (OBJ-01 a OBJ-07), más una para la medición (OE4).
- Cadena: **objetivo → necesidad → interesado → sesión → requerimiento → escenario → prueba**.
- Ejemplo: responder rápido → enterarse a tiempo → coordinador → censo → alerta en ≤ 5 s → escenario 1 → M1.
- Cierre: todos los requerimientos tienen origen. La necesidad de seguimiento todavía no tiene requerimiento (en análisis) y el avance de obra quedó descartado.

## 14. Pendientes y riesgos

**Pendientes (los que importan):**

| Pendiente | Quién |
|---|---|
| ¿Google Sheets o PostgreSQL? | Diego |
| Autorización de Torvesa para el campo | Diego, y Víctor escala |
| Volumen semanal de solicitudes | Diego, con la muestra |
| Plazo de conservación de datos, motivos de pérdida, catálogo de obras y presupuesto mensual | Gerencia, en el taller |
| Responsable del tratamiento de datos y comité de ética | Tutora |
| ¿Alguien aprueba las cotizaciones? ¿Hay visita a obra antes de cotizar? | Entrevistas |
| Diagrama de casos de uso y modelo conceptual | Diego |

**Riesgos (6):**
- Torvesa no autoriza a tiempo;
- la muestra del censo es pequeña (n = 5);
- las solicitudes por WhatsApp no se registran;
- la IA inventa precios;
- se caen servicios o suben los precios;
- llegan pocas solicitudes en las dos semanas.

Cada riesgo lleva una medida: la carta de la tutora, las encuestas, el registro en 1 minuto, la revisión humana, alternativas en el inventario y resultados descriptivos.

**Supuestos:**
- cada vendedor tiene celular con datos;
- la gerencia acepta registrar los estados;
- el MVP sigue en línea.

## 15. Línea base y aprobación

**Puntos:**
- Versión 1.0, **todavía no declarada**.
- 0 de 23 requerimientos aprobados: todos están «Propuestos».
- Firman: los dos estudiantes, la tutora y la gerencia de Torvesa, después del taller.

## 16. Anexos

- **A.** Guía de entrevista.
- **B.** Cuestionarios a colaboradores y clientes.
- **C.** Censo de TEAMSLASH (Informe Final, Tabla 1).
- **D.** Pantallas del MVP.
- **E.** Proceso actual en BPMN, casos de uso y modelo conceptual.
- **F.** Consentimiento informado.
- **G.** Actas de validación (después del taller).
- **H.** Planteamiento del problema.

## Referencias que sí se citan

- ISO/IEC/IEEE 29148:2018. *Systems and software engineering — Requirements engineering*. https://doi.org/10.1109/IEEESTD.2018.8559686
- Washizaki, H. (Ed.). (2025). *SWEBOK Guide* (v4.0a). IEEE Computer Society. https://www.computer.org/swebok
- Sevilla-Gonzalez et al. (2020). Versión en español de la SUS. *JMIR Human Factors, 7*(4), e21161. https://doi.org/10.2196/21161
- Ley Orgánica de Protección de Datos Personales (2021), Registro Oficial 5.º Suplemento n.º 459.
- Informe Final de TEAMSLASH (22-jul-2026), antecedente propio.

## Antes de entregar: lista de control

- [ ] Cada sección está escrita con nuestras palabras, en forma impersonal («se aplicó», «se identificó»).
- [ ] Lo hecho está en pasado y lo de Torvesa en futuro (planificado).
- [ ] Ninguna cifra de Torvesa se presenta como medida.
- [ ] Las fechas son: validación del 24-nov al 5-dic; tutora el 29-oct; entrega el 4-ene-2027.
- [ ] Los 23 requerimientos usan «deberá» y tienen un criterio medible.
- [ ] Ningún requerimiento usa palabras prohibidas.
- [ ] Cada requerimiento dice de dónde sale (interesado, sesión o fuente).
- [ ] TEAMSLASH aparece como antecedente propio y su almacenamiento, «por confirmar».
- [ ] Se usa la plantilla de la materia sin cambiar los números de sección.
