---
titulo: Práctica resuelta para el examen de Ingeniería de Requerimientos (parte práctica)
examen: 2026-11-26
fecha: 2026-11-21
autor_borrador: "Claude (revisa Víctor)"
tags: [estudio, practica, requerimientos]
---

# Práctica resuelta: los 10 tipos de ejercicio que pueden caer

> [!info] Cómo usarla
> Cada ejercicio trae: **enunciado**, **cómo se resuelve** (los pasos) y **la solución**. Al final de cada uno hay un **«Tu turno»** con la respuesta escondida: tápala, resuélvelo y compara.
> Caso base de todos: **la app «Quito Te Mueve 2.0»**. Recarga la tarjeta del Metro y del trolebús, muestra cuándo llega el bus y avisa de cierres de vía. Los usuarios: estudiantes, trabajadores, **adultos mayores** y **personas con discapacidad visual**, con **celulares de gama media** y datos móviles. El Municipio la paga.
> **Tiempo sugerido en el examen:** 1 hora en total. Si la mitad es práctica, son **unos 6 minutos por ejercicio**.

---

## Ejercicio 1. Clasificar (RF, RNF o de dominio)

**Enunciado.** Clasifique cada uno. Si es RNF, diga de qué familia.

| # | Enunciado |
|---|---|
| a | El sistema debe permitir recargar la tarjeta con tarjeta de débito. |
| b | La pantalla de saldo debe cargar en menos de 2 s en el 95 % de las consultas con 4G. |
| c | La tarifa preferencial del 50 % para adultos mayores se aplica según la ordenanza municipal. |
| d | La app debe estar disponible el 99,5 % del tiempo en horario de servicio (05:30 a 22:00). |
| e | El usuario debe poder guardar sus rutas frecuentes. |
| f | Los datos de la cédula se guardan cifrados y solo con el consentimiento del usuario (LOPDP). |
| g | La app debe soportar 50 000 usuarios a la vez en hora pico sin degradarse. |
| h | Todas las pantallas deben poder leerse con el lector de pantalla del celular. |

**Cómo se resuelve.** Pregunta: ¿describe una **acción** del sistema (qué hace), una **cualidad** (cómo, cuánto o qué tan) o una **regla del negocio o la ley**?

**Solución.**

| # | Tipo | Por qué |
|---|---|---|
| a | **RF** | acción del usuario o del sistema (recargar) |
| b | **RNF, rendimiento** | tiempo de respuesta |
| c | **De dominio** | regla que viene de la ordenanza (el negocio o la ley) |
| d | **RNF, disponibilidad** | *uptime* |
| e | **RF** | acción (guardar rutas) |
| f | **RNF, seguridad y privacidad.** También vale «de dominio» si la pregunta lo enfoca como norma legal | cifrado, consentimiento, LOPDP |
| g | **RNF, escalabilidad o rendimiento** | usuarios concurrentes |
| h | **RNF, usabilidad (accesibilidad)** | cualidad de la interfaz |

> **Tu turno.** Clasifique: (1) «El sistema envía un recibo por correo después de cada recarga». (2) «El código se documenta para que un desarrollador nuevo corrija un error en menos de 1 día». (3) «La app funciona en Android 10 o superior».
> > [!success]- Respuesta
> > (1) RF. (2) RNF, mantenibilidad. (3) RNF, una restricción de compatibilidad o portabilidad. Si solo hay 6 opciones, la más cercana es mantenibilidad o disponibilidad; lee bien las opciones.

---

## Ejercicio 2. Detectar el error y corregir (lista de chequeo)

**Enunciado.** Diga qué característica falla en cada uno y reescríbalo.

1. «La app debe ser rápida y fácil de usar.»
2. «El sistema debe usar Firebase para guardar los viajes.»
3. «El sistema debe permitir recargar la tarjeta, ver el historial y reportar un bus dañado.»
4. «Si es posible, la app debe avisar de los cierres de vía.»
5. RF-07: «Solo usuarios registrados pueden recargar». RF-09: «Cualquier persona puede recargar sin cuenta».

**Cómo se resuelve.**
1. Busca las **palabras prohibidas** (rápido, fácil, amigable, si es posible, todos, siempre, y/o).
2. Busca la **tecnología impuesta** (marca, producto, base de datos).
3. Cuenta los **verbos de capacidad**: si hay más de uno, falla Singular.
4. Compara con los otros requerimientos para ver si hay contradicción.
5. Al corregir, pon **medida, condición y una sola capacidad**.

**Solución.**

| # | Falla | Versión corregida |
|---|---|---|
| 1 | **Inequívoco o claro** y **verificable** («rápida», «fácil»). También **Singular** (dos cualidades) | RNF-01: «La pantalla de saldo carga en menos de 2 s en el 95 % de las consultas con 4G». RNF-02: «El 90 % de los usuarios nuevos recarga su tarjeta en menos de 3 minutos sin ayuda, en una prueba con 10 personas» |
| 2 | **Apropiado** (impone diseño): requerimiento como solución | «El sistema debe guardar cada viaje con la fecha, la hora y la estación, de forma persistente y consultable durante 12 meses» |
| 3 | **Singular** (tres capacidades) | RF-01 Recargar la tarjeta. RF-02 Consultar el historial. RF-03 Reportar un bus dañado |
| 4 | **Vacío o escapatoria** («si es posible»): falla inequívoco y verificable | «Cuando el Municipio registre un cierre de vía, el sistema debe notificar en máximo 10 minutos a los usuarios que siguen esa ruta» |
| 5 | **Consistente** (se contradicen) | Se resuelve con el cliente, por ejemplo: «La recarga con tarjeta bancaria exige cuenta; la recarga en efectivo en la taquilla no la exige». Y se **documenta la decisión** |

> **Tu turno.** «El sistema siempre debe mostrar la mejor ruta a todos los usuarios.»
> > [!success]- Respuesta
> > Hay totalidades («siempre», «todos») y un superlativo («la mejor»): falla Inequívoco y Verificable. Corrección: «Cuando el usuario ingrese un origen y un destino, el sistema debe mostrar hasta 3 rutas ordenadas por tiempo estimado de viaje, en menos de 3 s».

---

## Ejercicio 3. Especificar un requerimiento completo (los 8 campos)

**Enunciado.** Especifique el requerimiento «recarga con tarjeta de débito» con la estructura básica.

**Cómo se resuelve.** Llena los 8 campos en orden: **I**D, **T**ítulo, **D**escripción, **T**ipo, **P**rioridad, **C**riterio de aceptación (**con números**), **A**ctor y **D**ependencias.

**Solución.**

| Campo | Valor |
|---|---|
| ID | RF-004 |
| Título | Recarga con tarjeta de débito |
| Descripción | El sistema debe permitir al usuario registrado recargar el saldo de su tarjeta del Metro con tarjeta de débito, por un monto de $1 a $50, y mostrar el comprobante |
| Tipo | Funcional |
| Prioridad | Alta |
| Criterio de aceptación | En 20 recargas de prueba, el saldo se actualiza en menos de 10 s en al menos 19 (95 %), el comprobante muestra el monto, la fecha y la hora, y un monto fuera del rango se rechaza con un mensaje |
| Actor | Usuario registrado |
| Dependencias | RF-001 (registro de usuario) y RNF-003 (protección de datos de pago) |

> **Trampa:** el criterio de aceptación **no** es «que funcione bien». Lleva **cantidad de pruebas, medida y umbral**.

> **Tu turno.** Especifique «Aviso de llegada del bus» (te avisa cuando el bus está a 5 minutos).
> > [!success]- Respuesta
> > - **ID:** RF-006.
> > - **Título:** aviso de llegada del bus.
> > - **Descripción:** cuando el usuario active el aviso para una parada y una ruta, el sistema debe enviarle una notificación cuando el bus esté a 5 minutos estimados de esa parada.
> > - **Tipo:** F.
> > - **Prioridad:** media.
> > - **Criterio de aceptación:** en 10 viajes de prueba, el aviso llega entre 4 y 6 minutos antes de la llegada real en al menos 8.
> > - **Actor:** usuario.
> > - **Dependencias:** RF-005 (ubicación de los buses en tiempo real).

---

## Ejercicio 4. Lenguaje natural estructurado

**Enunciado.** Reescriba con la plantilla «**Cuando** [condición], **el sistema debe** [acción] [objeto] **para que** [beneficio]»:
(a) el aviso de saldo bajo; (b) un RNF de accesibilidad.

**Cómo se resuelve.** Separa primero en 4 columnas (condición, acción, objeto y beneficio) y después junta la frase. Pon una **medida** en la acción.

**Solución.**

| ID | Cuando | El sistema debe [acción] [objeto] | Para que |
|---|---|---|---|
| RF-08 | el saldo de la tarjeta baje de $0,90 (el valor de 2 pasajes de $0,45) | enviar una notificación al usuario en menos de 1 minuto | pueda recargar antes de llegar al torniquete |
| RNF-04 | una persona con discapacidad visual use el lector de pantalla del celular | leer en voz alta el 100 % de los botones y campos de las pantallas de recarga y saldo | pueda recargar sin ayuda de otra persona |

**Frases completas:**
- *Cuando el saldo de la tarjeta baje de $0,90, el sistema debe enviar una notificación al usuario en menos de 1 minuto para que pueda recargar antes de llegar al torniquete.*
- *Cuando una persona con discapacidad visual use el lector de pantalla del celular, el sistema debe leer en voz alta el 100 % de los botones y campos de las pantallas de recarga y saldo para que pueda recargar sin ayuda de otra persona.*

(La tarifa de $0,45 es solo un ejemplo para el ejercicio; en el examen usa los datos que te den.)

> **Tu turno.** Plantilla para «horas pico».
> > [!success]- Respuesta
> > *Cuando haya más de 30 000 usuarios conectados a la vez (hora pico), el sistema debe responder la consulta de llegada del bus en menos de 3 s en el 95 % de los casos para que el usuario decida si espera o cambia de ruta.*

---

## Ejercicio 5. MoSCoW con la regla del 60 %

**Enunciado.** Con estos requerimientos y horas, clasifique con MoSCoW y verifique la regla.

| ID | Requerimiento | Horas |
|---|---|---|
| R1 | Registro de usuario | 10 |
| R2 | Recarga con débito | 20 |
| R3 | Consulta de saldo | 6 |
| R4 | Llegada del bus en tiempo real | 30 |
| R5 | Rutas favoritas | 8 |
| R6 | Modo oscuro | 4 |
| R7 | Programa de puntos | 22 |

**Cómo se resuelve.**
1. Total = 10 + 20 + 6 + 30 + 8 + 4 + 22 = **100 h**.
2. Primera clasificación por «¿sin esto funciona la app?».
3. Suma los Must y divide para el total.
4. Si pasa del 60 %, **baja el Must menos crítico** a Should y explícalo.

**Solución.**
- **1.ª ronda:** Must = R1, R2, R3 y R4 = 66 h, el **66 %**: no cumple (más del 60 %).
- **Reclasificación:** R4 (tiempo real) pasa a **Should**. La app puede salir con recarga y saldo, y el tiempo real entra en la siguiente versión.
- **Final:**
  - **Must:** R1, R2 y R3 = 36 h, el **36 %**. ✓ Cumple.
  - **Should:** R4 y R5.
  - **Could:** R6.
  - **Won't (this time):** R7.
- **Nota:** si el profe usa la regla del DSDM «los Won't no cuentan», el total sin R7 es de 78 h. Los Must darían 36 / 78 = **46 %**, que también cumple.

> **Trampa:** «Won't» **no** significa «nunca», significa **«no en esta versión»**.

> **Tu turno.** Total de 80 h y Must de 52 h. ¿Cumple? ¿Cuántas horas tienes que bajar como mínimo?
> > [!success]- Respuesta
> > 52 / 80 = **65 %**: no cumple. El 60 % de 80 son 48 h, así que hay que bajar **al menos 4 h** de Must a Should.

---

## Ejercicio 6. Kano: de las respuestas a la categoría

**Enunciado.** Tres usuarios respondieron sobre el «aviso de llegada del bus»:

| Encuestado | Si SÍ lo tiene | Si NO lo tiene |
|---|---|---|
| E1 (estudiante, 20 años) | Me gusta | Me disgusta |
| E2 (trabajadora, 35 años) | Lo espero | Me disgusta |
| E3 (adulto mayor, 68 años) | Me gusta | Puedo tolerarlo |

**Cómo se resuelve.** Busca **la fila con la respuesta presente** y **la columna con la ausente** en la tabla. Después toma la categoría **más repetida**.

**Solución.**
- E1: Me gusta / Me disgusta = **R** (rendimiento).
- E2: Lo espero / Me disgusta = **B** (básico).
- E3: Me gusta / Puedo tolerarlo = **D** (deleite).
- Hay un **empate triple** (R, B, D).
  - **Cómo desempatar** (hay que justificarlo): usa la regla usual de la literatura de Kano (B > R > D > I: primero lo básico) o la importancia que declaró cada encuestado.
  - Con B > R > D, queda **Básico**.
  - Sin regla de desempate, se reporta el empate y se decide con el objetivo del proyecto.

**Más casos para memorizar:**
- Lo espero / Me disgusta = **B**.
- Me gusta / Me es indiferente = **D**.
- Me gusta / Me disgusta = **R**.
- Me es indiferente / Me es indiferente = **I**.
- Me disgusta / Me gusta = **Inv**.
- Me gusta / Me gusta = **C** (se descarta).

> **Tu turno.** (a) Puedo tolerarlo / Me disgusta. (b) Me disgusta / Lo espero. (c) Lo espero / Lo espero.
> > [!success]- Respuesta
> > (a) **B**. (b) **Inv**. (c) **I**.

---

## Ejercicio 7. Matriz valor contra esfuerzo

**Enunciado.** Con las horas del ejercicio 5 y estos valores (de 1 a 5), ubique el cuadrante de cada uno: R1 = 5, R2 = 5, R3 = 4, R4 = 4, R5 = 3, R6 = 1, R7 = 2.

**Cómo se resuelve.**
1. **Promedio de horas** = 100 / 7 = **14,3 h**. El esfuerzo es alto si pasa de 14,3.
2. **Valor alto si es ≥ 4.** Declara siempre el umbral que usas.
3. Cruza los dos.

**Solución.**

| ID | Valor | Horas | Esfuerzo | Cuadrante |
|---|---|---|---|---|
| R1 | 5 | 10 | bajo | **Quick win** |
| R2 | 5 | 20 | alto | **Proyecto estratégico** |
| R3 | 4 | 6 | bajo | **Quick win** |
| R4 | 4 | 30 | alto | **Proyecto estratégico** (dividir en fases) |
| R5 | 3 | 8 | bajo | **Fill-in** |
| R6 | 1 | 4 | bajo | **Fill-in** |
| R7 | 2 | 22 | alto | **Evitar** |

**Orden:** R1 y R3 → R2 y R4 → R5 y R6 → R7.

> **Tu turno.** Un requerimiento de valor 2 y 9 h, con un promedio de 12 h: ¿en qué cuadrante va?
> > [!success]- Respuesta
> > Valor bajo con esfuerzo bajo: **Fill-in**.

---

## Ejercicio 8. Contraste de las tres técnicas y prioridad final

**Enunciado.** Con los resultados de los ejercicios 5 a 7, dé la prioridad final de R2, R4 y R7 y diga qué técnica pesó más.

**Solución.**

| ID | MoSCoW | Kano | Cuadrante | Final | Qué pesó y por qué |
|---|---|---|---|---|---|
| R2 | Must | Básico | Estratégico | **Alta** | Coinciden MoSCoW y Kano: sin recarga la app no sirve. La matriz solo dice que hay que planificarlo bien |
| R4 | Should | Básico (el empate del ejercicio 6) | Estratégico | **Media → Alta en la v2** | Pesa **Kano**: si los usuarios lo dan por hecho, hay que planificarlo pronto; se divide en fases |
| R7 | Won't | Indiferente (supuesto) | Evitar | **Baja** | Las tres coinciden |

**Regla para justificar:**
- Las **obligaciones legales** las decide **MoSCoW** (no se negocian).
- Lo que el usuario **da por hecho** lo decide **Kano**.
- Cuando el valor es parecido, desempata la **matriz** (el costo).

---

## Ejercicio 9. Elegir la técnica de elicitación

**Enunciado.** ¿Qué técnica usaría?
(a) Saber qué piensan 2 000 usuarios del pago con QR.
(b) Entender por qué los adultos mayores no usan la app.
(c) Conocer las reglas de la tarifa preferencial.
(d) Ver cómo compran el pasaje en la estación El Labrador en hora pico.
(e) Generar ideas de funciones nuevas con el equipo.
(f) Confirmar si el diseño de la pantalla de recarga se entiende.

**Solución.**
- (a) **Encuesta:** son muchos y hay que cuantificar.
- (b) **Entrevista** (profundidad, el porqué) o **focus group** de 6 a 10 adultos mayores.
- (c) **Análisis de documentos:** la ordenanza y las regulaciones.
- (d) **Observación:** lo que hacen, no lo que dicen. Puede ser pasiva.
- (e) **Brainstorming:** no se critica, cantidad antes que calidad.
- (f) **Prototipo** (un *wireframe* o un *mockup*) mostrado a los usuarios.

---

## Ejercicio 10. Conflicto y 5 porqués

**Enunciado A (conflicto).** Seguridad pide 2FA en cada ingreso; los usuarios quieren entrar rápido para pagar en el torniquete.

**Solución.** Se resuelve con un ***trade-off*** (compromiso): 2FA solo en recargas mayores a $20 y al cambiar de celular, y el pago en el torniquete con la sesión recordada. Si no hay acuerdo, se **escala** al *product owner* del Municipio. Se **documenta la decisión**: qué, por qué y quién la aprobó.

**Enunciado B (5 porqués).** El usuario dice: «Quiero un botón para exportar mis viajes a Excel».

**Solución.**
1. ¿Por qué? → «Para saber cuánto gasto al mes».
2. ¿Por qué? → «Porque la empresa me reembolsa el transporte».
3. ¿Por qué necesitas el Excel? → «Porque Talento Humano pide un respaldo mensual».

**Problema real:** necesita un **comprobante mensual de gasto en transporte** que acepte su empresa.

**Requerimiento:** «El sistema debe generar un resumen mensual en PDF con los viajes y el total gastado, descargable desde el historial».

El Excel era **una solución**, no la necesidad.

---

## Simulacro cronometrado (hazlo el miércoles, 25 minutos)

1. Clasifique 6 enunciados (RF, RNF con familia, o de dominio) sobre la app **Deuna**, la billetera móvil del Banco Pichincha. Escribe tú los enunciados o usa los del juego.
2. Corrija 3 requerimientos con palabras prohibidas.
3. Especifique 1 requerimiento con los 8 campos.
4. MoSCoW con 6 requerimientos, horas y la regla del 60 %.
5. Kano para 1 función con 3 encuestados.
6. Matriz con el promedio de horas.

Revísalo contra este documento. Cada error es una tarjeta nueva en el juego (sección «Mis errores»).
