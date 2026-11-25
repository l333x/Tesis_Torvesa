---
titulo: "Práctica resuelta parte 2: validar, verificar, gestionar el cambio y escribir historias de usuario"
examen: 2026-11-26
fuente: "Clases VVG (27 págs.) y AG (19 págs.)"
fecha: 2026-11-24
autor_borrador: "Claude (revisa Victor)"
---

# Práctica parte 2: los 8 tipos de ejercicio que pueden caer

> [!tip] Receta general
> Para cualquier ejercicio de estas clases usa el mismo orden que el profe en su caso de Quito: **1) Validar** (¿para qué lo quieren? pregunta a cada stakeholder), **2) Verificar** (lista de chequeo y las 3 C), **3) Gestionar** (impacto, decisión, versión, traza). Si piden historias: **Como/Quiero/Para → INVEST → Dado/Cuando/Entonces**.

---

## Ejercicio A. ¿Validación o verificación?

**Enunciado tipo:** clasifica cada actividad.

| Actividad | Respuesta | Por qué |
|---|---|---|
| Mostrar un prototipo al cliente para ver si es lo que necesita | **Validación** | con cliente, intención |
| Revisar con una lista de chequeo que cada RF tenga ID y criterio de aceptación | **Verificación** | interno, calidad del documento |
| Un par revisor detecta que RF-002 y RF-007 se contradicen | **Verificación** | coherencia, revisión técnica |
| Preguntar al Municipio qué decisión tomará con el dato | **Validación** | intención |
| Derivar casos de prueba de aceptación con el usuario | **Validación** | técnica de validación (p. 7) |
| Inspección formal del documento de requerimientos | **Verificación** | técnica de verificación (p. 11) |
| Walkthrough guiado sobre la especificación con stakeholders | **Validación** | técnica de validación (p. 7) |

**Truco:** ¿está el cliente en la sala y se discute el **para qué**? → validación. ¿Solo el equipo revisando **cómo está escrito**? → verificación.

**Tu turno:** «El analista nota que "rápido" aparece en 5 requerimientos sin cifra».
> [!success]- Respuesta
> Verificación, criterio de **claridad** (término vago). Se corrige con una cifra medible.

---

## Ejercicio B. Validar un pedido vago (modelo p. 8-9)

**Enunciado tipo:** el gerente de una cadena de farmacias pide: «La app debe tener un buscador fácil de usar». Valídalo.

**Paso 1, preguntas al cliente (las 3 de la p. 8):**
- ¿Qué significa «fácil» para usted?
- ¿En qué tareas debe ser fácil?
- ¿Quién es el usuario objetivo?

**Paso 2, preguntar a cada stakeholder para qué (p. 9):**
- Clientes: para encontrar el medicamento y saber en qué sucursal hay stock.
- Farmacéuticos: para buscar por principio activo, no solo por marca.
- Gerencia: para medir qué productos se buscan y no hay.

**Paso 3, resultado validado:**
«El 90 % de los clientes debe encontrar un medicamento por nombre comercial o principio activo y ver la sucursal con stock en menos de 30 segundos sin ayuda». Más un reporte de búsquedas sin stock solo para gerencia.

**Frase de cierre (copia la del profe):** la validación cambió la intención: no era «un buscador bonito», era saber **dónde hay stock**.

---

## Ejercicio C. Verificar un requerimiento mal escrito (modelo p. 20). EL MÁS PROBABLE

**Método fijo en 3 pasos:**
1. Pasa la **lista de chequeo de 12 puntos** (p. 18) y anota cada falla con su criterio.
2. Busca la palabra **«y»** → si une dos objetivos, **parte en dos** (atómico).
3. Reescribe con: **condición + sistema debe + acción + cifra + excepción**.

**Ejemplo 1.** «RF-010: El sistema debe permitir registrarse y recuperar la contraseña de forma rápida y segura usando MySQL».

| Problema | Criterio |
|---|---|
| «rápida», «segura» vagos | claridad |
| registrarse **y** recuperar: dos objetivos | no atómico |
| «usando MySQL» impone solución | mezcla QUÉ con CÓMO |
| no hay criterio de aceptación | no verificable |
| sin prioridad ni stakeholder origen | lista de chequeo (puntos 4 y 9) |

**Verificado:**
- **RF-010:** el sistema debe permitir que un visitante se registre con cédula y correo, y confirmar la cuenta en menos de 5 segundos. Prioridad: Must. Origen: área comercial. Aceptación: 95 % de registros confirmados en < 5 s en prueba con 100 usuarios.
- **RF-011:** el sistema debe enviar un enlace de recuperación de contraseña al correo registrado, válido por 30 minutos.
- (La seguridad se especifica aparte como RNF medible; la base de datos se decide en diseño.)

**Ejemplo 2 (coherencia).** RF-002 «el registro requiere email» y RF-007 «el registro debe hacerse solo con cédula».
> [!success]- Respuesta
> Incoherencia (p. 17): se contradicen. Se resuelve con el stakeholder (validación) y se deja un solo criterio, por ejemplo «cédula obligatoria y correo opcional», actualizando los dos RF con la misma terminología.

**Tu turno:** «RF-020: el sistema debe ser intuitivo y mostrar las notas y enviar alertas».
> [!success]- Respuesta
> «intuitivo» vago (claridad); tres cosas en una (no atómico); sin criterio de aceptación. Partir: RF-020 mostrar las notas del periodo actual al ingresar, en menos de 2 s; RF-021 enviar alerta por correo cuando se publique una nota nueva, en máx. 1 h. «Intuitivo» se vuelve RNF medible: «el 90 % de estudiantes encuentra sus notas sin ayuda en < 1 min».

---

## Ejercicio D. Completitud: ¿qué falta? (p. 16)

**Enunciado tipo:** un sistema de reservas de canchas tiene solo: RF-1 reservar cancha, RF-2 pagar en línea, RF-3 ver mis reservas. ¿Está completo?

**Respuesta guiada por las 5 preguntas de completitud:**
1. Flujos alternativos: ¿cancelar o reprogramar una reserva? **Falta.**
2. Errores y excepciones: ¿qué pasa si el pago falla o dos personas reservan la misma hora? **Falta.**
3. RNF: ¿tiempos de respuesta, disponibilidad? **Falta.**
4. Integraciones: ¿pasarela de pago, correo de confirmación? **Falta mencionarlas.**
5. Restricciones legales o de negocio: ¿política de reembolso, facturación electrónica del SRI? **Falta.**

Recuerda: la completitud se juzga **sobre el conjunto**.

---

## Ejercicio E. Control de cambios y análisis de impacto (modelo pp. 23-24)

**Enunciado tipo:** sistema de matrícula con línea base v1.0 aprobada. Esfuerzo planificado del lanzamiento: 30 de 30 semanas-persona. Bienestar Estudiantil pide «notificar por WhatsApp cuando se abra la matrícula». Estimación: 3 semanas-persona. Depende de contratar la API de WhatsApp Business. Haz el control de cambios.

| Paso | Respuesta |
|---|---|
| 1. Solicitud | Quién: Bienestar Estudiantil. Qué: notificación por WhatsApp de apertura de matrícula. Por qué: muchos estudiantes no leen el correo y se les pasa la fecha. |
| 2. Análisis de impacto | **Afectados:** RF nuevo (RF-040 notificar por WhatsApp); RF existente de notificaciones por correo (se amplía); módulo de calendario de matrícula (dependencia). **Esfuerzo:** +3 semanas-persona. **Plazo:** el lanzamiento usa 30 de 30 → **no entra en v1**. **Riesgo:** medio (p. ej. 0,3): depende de contratar la API y de tener los números autorizados. |
| 3. Decisión | **Diferir:** aprobado para la siguiente versión. Decide el **Product Owner o comité** (aquí, el Vicerrectorado como sponsor). |
| 4. Actualización | Nueva línea base **v1.1** (cambio menor); historial: versión, fecha, cambio, quién aprobó. Se agrega la fila a la matriz de trazabilidad. |
| 5. Comunicación | Se informa al equipo y a Bienestar Estudiantil de la decisión y la fecha estimada. |

**En ágil:** la solicitud entra al **backlog** como historia y compite por prioridad.

**¿Cuándo sería v2.0?** Si el cambio es de alcance mayor, por ejemplo «agregar todo el módulo de pagos de aranceles».

**Tu turno:** si el riesgo fuera alto y el valor bajo, ¿qué decisión tomas?
> [!success]- Respuesta
> Rechazar (o diferir indefinidamente), documentando el motivo. Recuerda las 3 decisiones: aprobar, rechazar o diferir.

---

## Ejercicio F. Matriz de trazabilidad (modelo p. 25)

**Enunciado tipo:** arma la matriz para los RF del ejercicio C (registro y recuperación).

| Necesidad | Stakeholder | Requerimiento | Diseño | Prueba |
|---|---|---|---|---|
| Crear cuenta sin ir a la oficina | Clientes | RF-010 | Pantalla «Registro» | CP-010: registro con cédula válida confirmado en < 5 s |
| Recuperar acceso sin llamar a soporte | Clientes | RF-011 | Servicio de correo | CP-011: enlace caduca a los 30 min |
| Evitar cuentas duplicadas | Área comercial | RF-010 | Validación de cédula | CP-012: una cédula repetida muestra error |

- **Hacia atrás** = columnas Necesidad y Stakeholder. **Hacia adelante** = Diseño y Prueba.
- Para qué sirve: si cambia RF-010, la matriz dice qué pantalla, servicio y pruebas revisar.

---

## Ejercicio G. Escribir historias de usuario con INVEST y criterios de aceptación

**Enunciado tipo:** escribe 3 historias para una app de la biblioteca universitaria, valida INVEST y escribe criterios Dado/Cuando/Entonces para una.

**HU-01.** Como **estudiante de pregrado** quiero **reservar un libro físico desde la app** para **retirarlo sin hacer fila en el mostrador**.
**HU-02.** Como **bibliotecario** quiero **ver la lista de reservas del día ordenada por hora** para **preparar los libros antes de que lleguen los estudiantes**.
**HU-03.** Como **docente** quiero **recibir un aviso cuando un libro de mi bibliografía quede sin ejemplares** para **pedir la compra a tiempo**.

**INVEST sobre HU-01:**
- I: no depende de HU-02 ni HU-03. ✔
- N: se puede negociar cuántos días dura la reserva. ✔
- V: ahorra la fila. ✔
- E: el equipo puede estimarla (p. ej. 5 puntos). ✔
- S: cabe en un sprint de 2 semanas. ✔
- T: se prueba con los criterios de abajo. ✔

**Criterios de aceptación de HU-01:**
- **Dado** que inicié sesión y el libro tiene ejemplares disponibles, **cuando** presiono «Reservar», **entonces** veo la confirmación con la fecha límite de retiro (48 h).
- **Dado** que el libro no tiene ejemplares, **cuando** intento reservar, **entonces** veo «Sin ejemplares» y la opción de lista de espera. (Escenario de excepción: completitud.)

**Tu turno:** convierte la mala «Como usuario quiero que la app de la biblioteca sea más fácil».
> [!success]- Respuesta
> Problemas (p. 16): rol genérico, «fácil» subjetivo, sin beneficio, no medible ni testeable. Buena: «Como estudiante nuevo quiero buscar un libro por título o autor y ver si está disponible en menos de 3 segundos para saber si vale la pena ir a la biblioteca». Aceptación: Dado que estoy en el buscador, Cuando escribo «Pressman», Entonces veo resultados con su disponibilidad en < 3 s.

---

## Ejercicio H. Detectar el error en historias (p. 18) y clasificar ítems del backlog (p. 19)

| Historia / ítem | Error o tipo | Corrección |
|---|---|---|
| «Como usuario quiero pagar con tarjeta» | rol genérico + sin beneficio | «Como cliente frecuente quiero pagar con tarjeta guardada para terminar la compra en menos de 1 min» |
| «Como admin quiero crear, editar y borrar productos y ver reportes» | varias funcionalidades | dividir en 4 historias |
| «Como cliente quiero un botón rojo en la esquina» | solución técnica, no necesidad | «Como cliente quiero acceder a soporte rápidamente para resolver mi problema sin salir de la app» |
| «Como cliente quiero ver mis pedidos» | falta el «para» | agregar el beneficio: «para saber cuándo llega cada uno» |
| «Actualizar el servidor a la versión nueva de PostgreSQL» | **historia técnica** | va al backlog |
| «Investigar si la pasarela de pagos X funciona con bancos de Ecuador» | **spike** | va al backlog, con tiempo limitado |

---

## Ejercicio integrador (como el caso de clase). Hazlo cronometrado: 20 min

**Caso:** app de una cooperativa de taxis de Quito, línea base v1.0 (esfuerzo 40/40 semanas-persona). La gerencia pide: «La app debe mostrar el ranking de los conductores mejor calificados de forma rápida y permitir descargar el historial».

Responde: (1) validación, (2) verificación, (3) control de cambios, (4) una historia de usuario con INVEST y criterios.

> [!success]- Respuesta modelo
> **1. Validación** (preguntar para qué):
> - Pasajeros: para sentirse seguros al pedir un taxi → quieren ver la calificación **del conductor asignado**, no un ranking.
> - Conductores: piden que no cuenten calificaciones de viajes cancelados por el pasajero.
> - Gerencia: para dar bonos mensuales.
> Validado: calificación del conductor asignado para pasajeros + reporte mensual de calificaciones solo para gerencia. «El ranking público no era la necesidad real.»
>
> **2. Verificación:** «rápida» vaga (claridad); mostrar **y** descargar = dos objetivos (atómico); «mejor calificados» no definido (coherencia de vocabulario); sin criterio de aceptación (verificable).
> - RF-050: al asignarse un viaje, el sistema debe mostrar al pasajero la calificación promedio del conductor de los últimos 30 días (escala 1 a 5), sin contar los viajes cancelados por el pasajero, en menos de 2 s.
> - RF-051: el sistema debe generar para gerencia un reporte mensual de calificaciones por conductor en PDF.
>
> **3. Gestión:** Solicitud (gerencia, qué, por qué) → Impacto: RF-050 y RF-051 nuevos, RF de asignación de viaje (dependencia), módulo de reportes (se amplía); esfuerzo p. ej. +4 semanas-persona; plazo 40/40 → no entra en v1; riesgo p. ej. 0,3 → Decisión: aprobado para la versión 2, aprueba la gerencia (sponsor) → Actualización: línea base v1.1, matriz de trazabilidad → Comunicación.
>
> **4. Historia:** Como pasajera que viaja de noche quiero ver la calificación y la foto del conductor asignado antes de que llegue para decidir si acepto el viaje con tranquilidad.
> Dado que pedí un taxi, Cuando se asigna un conductor, Entonces veo su foto y calificación promedio de 30 días en menos de 2 s.
> INVEST: independiente, negociable (30 o 60 días), valiosa (seguridad), estimable, pequeña (un sprint), testeable (el criterio).
