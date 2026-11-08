---
titulo: Casos de prueba v0.1 — M2, M4 y M5, con la evaluación heurística propuesta para M6
version: v0.1
fecha: 2026-11-08
autor: Diego Bermeo
ia: Claude (Claude Code)
tarea: S5-05 (bloque U)
estado: propuesta; la aprueba Víctor
base: "00_Inbox/2026-11-02_aviso_sin_encuestas_ni_entrevistas.md · 06_Capitulos/2026-11-07_Cap5_Cap6_Esquema_v0.1.md · elicitación v0.1 (sección 12) · prueba de concepto (repos teamslash-api y teamslash-poc)"
tags: [diego, casos-de-prueba, validacion, M2, M4, M5, M6, sprint5]
---

# Casos de prueba v0.1

> [!warning] Depende de la propuesta sin datos de personas
> Estos casos siguen la propuesta del 2-nov: no se recogen datos de personas (DEC-21 a DEC-23, al inicio del Cap. III del borrador). Solo los ejecutamos **nosotros dos, con datos ficticios**, y solo registramos nuestros propios tiempos y aciertos. Si la tutora no la acepta, M2 vuelve al cronometraje de quien cotiza (P2-A) y M4, a la prueba con vendedores e I1. [DECIDIR-TUTORA: aprobación de la propuesta]

## 1. Qué casos son

Son tres casos, uno por meta que se mide en condiciones controladas, como dice el esquema del Cap. V:

| Caso | Meta | Requisitos | Qué compara |
|---|---|---|---|
| **CP-01** Cotización con y sin asistente | M2 | RQ-10, RQ-11, RQ-12, RQ-21 | Tiempo para dejar lista una cotización, con el asistente y sin él |
| **CP-02** Recuperación del historial de un cliente ajeno | M4 | RQ-09, RQ-13 | Tiempo y aciertos para responder 5 preguntas sobre un cliente, con la bóveda y sin ella |
| **CP-03** Detección de alteraciones del registro | M5 | RQ-15, RQ-16, RQ-17 | Porcentaje de alteraciones simuladas que la verificación detecta |

Además:
- **Anexo A:** la evaluación heurística que reemplazaría al cuestionario SUS (M6 reformulada). Es una propuesta y depende de la tutora.
- **Anexo B:** lo que ya se comprobó de cada requisito en la prueba de concepto del 8-nov. No es un caso de prueba; sirve de evidencia para el Cap. V.

[DECIDIR-VÍCTOR: el Cap. I y el Cap. III dicen «cuatro casos de prueba», y el cronograma (S5-05) y el Cap. V dicen tres. Si la evaluación heurística cuenta como el cuarto, se puede dejar «cuatro»; si no, hay que corregir el Cap. I, el Cap. III y la presentación.]

## 2. Reglas para los tres casos

- **Solo datos ficticios.** Las solicitudes, los clientes y los historiales los inventamos nosotros y se marcan como ficticios. No se usa nada de Torvesa ni de sus clientes.
- **Los ejecutamos nosotros dos.** No participan otras personas. Lo que se registra es el tiempo y los aciertos de cada uno de nosotros, con un código (E1 = Diego, E2 = Víctor).
- **Quien prepara el material no lo ejecuta**, cuando conocer las respuestas cambia el resultado (CP-02).
- **Orden contrabalanceado.** Cada uno hace la mitad de las tareas con el sistema y la mitad sin él, en orden cruzado, para que lo aprendido en la primera tarea no favorezca siempre a la misma condición.
- **Análisis descriptivo.** Con tan pocas mediciones se reportan medianas, mínimos y máximos, sin pruebas estadísticas ni generalización.
- **Dónde se registra:** `07_Flujos_Diseno/Resultados_Casos_Prueba/` (S8-04), con una tabla por caso como las de abajo.
- **Fechas:** se ejecutan en el sprint 8 (S8-04), con la prueba de concepto ya terminada.

## 3. CP-01 · Cotización con y sin el asistente (M2)

**Objetivo.** Saber si el borrador del asistente reduce el tiempo de dejar lista una cotización.

**Preparación (E1).**
- Cuatro solicitudes ficticias de complejidad parecida, ingresadas por el formulario web para que pasen por todo el sistema:

| Solicitud | Tipo de obra | Descripción ficticia |
|---|---|---|
| S-A | Remodelación | Cocina de unos 12 m²: cambiar piso, mesón y la instalación del fregadero |
| S-B | Remodelación | Baño de unos 6 m²: cambiar cerámica de piso y paredes, sanitarios y grifería |
| S-C | Construcción residencial | Casa de una planta de unos 90 m² en terreno propio, con dos dormitorios |
| S-D | Construcción residencial | Ampliación de un segundo piso de unos 60 m² sobre una losa existente |

- La bóveda de la prueba de concepto con las plantillas de remodelación y de construcción residencial.

**Las dos condiciones.**
- **Sin asistente:** se copia la plantilla del tipo de obra en una nota nueva y se llenan a mano los rubros, las cantidades que se puedan deducir, las preguntas que faltan y el mensaje al cliente.
- **Con asistente:** se corre `python borrador.py SOL-xxxx`, y el borrador se revisa y se corrige hasta que cumpla la misma lista de verificación. Al final se llena «Revisión humana» en la nota (RQ-12).

La condición sin asistente ya parte de una plantilla, y hoy Torvesa no tiene plantillas. Así la comparación es conservadora: si el asistente ahorra tiempo frente a una plantilla, también lo ahorraría frente a empezar de cero.

**Orden.**

| Ejecutor | S-A | S-B | S-C | S-D |
|---|---|---|---|---|
| E1 | sin | con | sin | con |
| E2 | con | sin | con | sin |

Cada solicitud se hace una vez con el asistente y una vez sin él. En total son 8 mediciones, 4 por condición.

**Qué se mide.**
- **Tiempo de elaboración:** con cronómetro, desde abrir la solicitud hasta que la cotización cumple la lista de verificación. En la condición con asistente se incluye la espera del borrador.
- **Tiempo del asistente:** el campo `segundos_borrador`, que el sistema guarda solo.
- **Lista de verificación** (la misma en las dos condiciones):
  1. rubros pertinentes al tipo de obra;
  2. cantidades solo donde la solicitud da medidas, marcadas como estimadas;
  3. preguntas sobre lo que falta saber;
  4. mensaje al cliente;
  5. ningún precio, plazo ni condición inventados.
- En la condición con asistente se revisa además:
  - si el borrador cita al menos un documento de la bóveda (RQ-11);
  - si alguna celda de precio vino llena;
  - si el texto enviado al asistente pasó la verificación de datos personales (RQ-21).

**Criterio de aceptación.**
- La mediana del tiempo con asistente es menor que la mediana sin asistente (M2).
- El 100 % de los borradores cita al menos un documento (RQ-11).
- Ningún borrador queda como enviado sin revisión (RQ-12).
- El asistente no pone ningún precio.

**Qué puede sesgar el resultado y cómo se cuida.**
- *Aprendizaje entre tareas:* el orden cruzado de arriba.
- *Los ejecutores somos los autores del sistema:* se declara como limitación. Los dos llevamos el cronómetro con la misma regla de inicio y de fin.
- *Las cotizaciones no llevan precios:* las plantillas no tienen precios hasta que la gerencia los dé (PEN-12). El tiempo medido no incluye ponerlos, y se declara como limitación.
- *No hay línea base de «hoy»:* la referencia del proceso actual sale del antecedente y se presenta como hipótesis, no como medición.

**Registro.**

| Ejecutor | Solicitud | Condición | Inicio | Fin | Minutos | Lista completa (sí/no) | Documentos citados | Precio inventado (sí/no) | Observaciones |
|---|---|---|---|---|---|---|---|---|---|
| E1 | S-A | sin | | | | | — | — | |

## 4. CP-02 · Recuperación del historial de un cliente ajeno (M4)

**Objetivo.** Saber si con la bóveda se encuentra más rápido y mejor lo que se sabe de un cliente que atiende otra persona.

**Preparación.** Dos clientes ficticios equivalentes, X e Y, cada uno con:
- dos solicitudes;
- una cotización enviada;
- tres notas de seguimiento;
- una fecha de seguimiento pendiente.

Cada historial se arma en dos formatos con la **misma información**:
- **Sin bóveda (como hoy):** información dispersa, como la describe el AS-IS. Un chat de WhatsApp exportado a texto, notas sueltas en un documento y la cotización en un archivo aparte. Todo es ficticio y se arma a mano.
- **Con bóveda:** la ficha del cliente, sus solicitudes y su cotización en Obsidian, enlazadas entre sí.

Para que nadie responda de memoria, **E1 prepara el material que ejecuta E2, y E2 el que ejecuta E1.**

**Las 5 preguntas** (las mismas para los dos clientes):
1. ¿Qué tipo de obra pidió la última vez?
2. ¿En qué estado está su solicitud más reciente?
3. ¿Quién lo atiende ahora?
4. ¿Qué cotización se le envió y con qué plantilla se hizo?
5. ¿Cuándo es el próximo seguimiento y qué quedó pendiente?

Quien prepara el material escribe también la **hoja de respuestas**.

**Orden.**

| Ejecutor | Cliente X | Cliente Y |
|---|---|---|
| E1 | sin bóveda | con bóveda |
| E2 | con bóveda | sin bóveda |

**Qué se mide.**
- **Tiempo:** con cronómetro, desde que se recibe la lista de preguntas hasta la última respuesta.
- **Aciertos:** de 0 a 5, contra la hoja de respuestas. Una respuesta incompleta no cuenta como acierto.

**Criterio de aceptación.** Con la bóveda, menos tiempo y al menos los mismos aciertos que sin ella (M4).

**Qué puede sesgar el resultado y cómo se cuida.**
- *Conocer las respuestas:* el material lo prepara la otra persona.
- *El cliente X sea más fácil que el Y:* los dos se arman con la misma estructura y la misma cantidad de información.
- *Que el formato sin bóveda se arme más desordenado de lo que es la realidad:* se sigue el AS-IS v0.1 y se declara que es una simulación del proceso actual, no una medición en la empresa.

**Registro.**

| Ejecutor | Cliente | Condición | Minutos | Aciertos (0–5) | Preguntas falladas | Observaciones |
|---|---|---|---|---|---|---|
| E1 | X | sin bóveda | | | | |

## 5. CP-03 · Detección de alteraciones del registro (M5)

**Objetivo.** Comprobar que la verificación con huellas SHA-256 detecta cada alteración del registro de eventos.

**Qué ya existe** (bloque T, 8-nov):
- La tabla de eventos de la API, donde cada evento guarda su huella encadenada con la del anterior.
- La verificación `GET /api/eventos/verificar`.
- La prueba automática `test/eventos.smoke.js` del repo `teamslash-api`, que simula tres alteraciones y comprueba que se detectan:
  1. cambiar el contenido de un evento;
  2. cambiar el contenido y recalcular su huella para taparlo;
  3. borrar un evento intermedio.
- Primera corrida, el 8-nov: **3 de 3 detectadas.**

**Procedimiento en S8-04.**
1. Hacer una copia de prueba de los eventos registrados durante la validación. Nunca se tocan los originales.
2. Aplicar a la copia un conjunto de alteraciones de los tres tipos. Un programa elige el evento y el campo al azar, con una semilla fija para poder repetirlo. [DECIDIR-VÍCTOR: cuántas; se propone 20.]
3. Correr la verificación sobre la copia y anotar, para cada alteración, si se detectó y en qué evento.
4. Correr la verificación sobre el registro original, que debe salir íntegro.

**Criterio de aceptación.** El 100 % de las alteraciones simuladas se detecta (M5), y el registro original sale íntegro.

**Límite conocido, que se declara.** Si se borran los **últimos** eventos de la cadena, la verificación no lo nota, porque no queda ningún evento posterior que delate el hueco. Se propone publicar cada lunes la última huella en el reporte semanal (RQ-08), para que sirva de ancla. [DECIDIR-VÍCTOR: si se agrega a RQ-08.] También se declara que la verificación prueba que un evento no cambió desde que se guardó, no que su contenido fuera cierto cuando se guardó (limitación f del Cap. I).

**Registro.**

| N.º | Tipo de alteración | Evento | Campo | ¿Detectada? | Motivo que dio la verificación |
|---|---|---|---|---|---|
| 1 | contenido | | | | |

## Anexo A · Evaluación heurística (propuesta para reemplazar el SUS en M6)

> [!info] Propuesta, por decidir
> Reemplaza al cuestionario SUS, que recoge datos de usuarios. Se pierde el puntaje SUS ≥ 68 y la meta M6 hay que reformularla. [DECIDIR-TUTORA]

- **Qué es:** cada evaluador recorre el sistema y anota los problemas que encuentra contra una lista reconocida de principios de usabilidad. Se propone la de 10 heurísticas de Nielsen, con una escala de gravedad de 0 a 4. [FALTA-FUENTE: fuente vigente de las heurísticas y de la escala; en la base hay dos candidatas sin verificar, fiandhika_2024 y lianda_2026, que aplican evaluación heurística, la segunda dentro de DSR.]
- **Qué se recorre:**
  1. el formulario web con la casilla de consentimiento;
  2. la tarjeta de Slack con sus botones;
  3. la ficha del cliente y la solicitud en Obsidian;
  4. el borrador de cotización y su revisión;
  5. los tableros.
- **Cómo:**
  - E1 y E2 evalúan **por separado**, cada uno con la misma lista de tareas;
  - después se unen las dos listas y se acuerda la gravedad de cada problema.
- **Meta reformulada (propuesta):** al cierre de la validación no queda ningún problema de gravedad 3 o 4 sin corregir o sin una corrección planificada.
- **Limitación:** los evaluadores somos los autores del sistema, y la práctica recomendada es usar varios evaluadores independientes. [FALTA-FUENTE] Si la tutora acepta a un evaluador externo, se suma.

## Anexo B · Lo que ya se comprobó en la prueba de concepto (8-nov)

Esto no reemplaza a los casos de prueba. Es la evidencia de que cada pieza funciona, para la descripción de la prueba de concepto en el Cap. V. Todo se hizo con datos ficticios.

| Requisito | Qué se comprobó | Cómo | Resultado |
|---|---|---|---|
| RQ-01 | La solicitud del formulario queda registrada con fecha y hora | Envío desde la página publicada (Vercel) a la API (Railway) | Funciona. Falta medir el criterio de 5 segundos |
| RQ-02 | Aviso al responsable | Tarjeta en Slack al llegar la solicitud | Funciona. Falta medir el criterio de 5 segundos |
| RQ-04, RQ-05 | Responsable único y estados | Botón «Tomar» en Slack | Funciona con los 4 estados de TEAMSLASH. «Cotizada» todavía no existe |
| RQ-09 | Ficha por cliente en la bóveda, sin datos personales | `sincronizar.py` | Funciona. Los datos de contacto quedan solo en `_Contactos` |
| RQ-11 | El borrador cita los documentos que usó | `borrador.py` con una solicitud ficticia de cocina | Funciona. Citó la plantilla de remodelación; tardó 15 s |
| RQ-12 | Nada se envía sin revisión humana | El borrador queda como «Borrador», con la sección «Revisión humana» por llenar | Funciona. El sistema no envía nada por su cuenta |
| RQ-15, RQ-16 | Registro con huellas y verificación | Prueba automática y verificación en línea | 3 de 3 alteraciones detectadas; la cadena en línea sale íntegra |
| RQ-17 | El registro no tiene datos personales | La prueba busca nombre, teléfono, correo y usuario en los eventos | No aparecen. Quien hizo el cambio queda como seudónimo |
| RQ-18 | Consentimiento obligatorio | Envío sin la casilla | Se rechaza. Con la casilla se guardan la fecha y la versión del aviso |
| RQ-21 | Al asistente no le llegan datos personales | `prueba_privacidad.py` y la verificación antes de cada llamada | Funciona. Un teléfono escrito en la descripción se omitió |
| RQ-24 | Hora del primer contacto | «Tomar» una solicitud ficticia en línea | Se guarda y no se pisa después. El criterio de cuándo cuenta como primer contacto lo confirma Víctor |
