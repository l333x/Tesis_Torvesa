---
titulo: "Guion de Diego para la Revisión 2: diapositivas 4, 5 y 6"
fecha: 2026-11-15
autor: Diego Bermeo
ia: Claude (Claude Code)
basado_en: "08_Reuniones_Tutora/2026-11-16_Revision2_Guion_v0.1.md y las notas del orador de la presentación v0.1"
duracion: "≈ 3 min 15 s"
tags: [diego, revision2, ensayo]
---

# Mi parte de la Revisión 2 (diapositivas 4, 5 y 6)

**Reglas:** decir «validación del diseño en operación experimental controlada», nunca «piloto» ni «implementado». No dar cifras de Torvesa que todavía no se midieron.

## Diapositiva 4 · Proceso actual (1:00)

> «Este es el proceso actual, como lo levantamos en el AS-IS. Marcamos cinco puntos donde se pierde tiempo o información.
>
> Uno, **la espera**: el mensaje del cliente llega y nadie lo ve hasta que alguien revisa el celular.
> Dos, **la asignación es informal**: no queda claro quién se encarga.
> Tres, **cada cotización se hace desde cero**.
> Cuatro, **el seguimiento depende de la memoria** de cada vendedor.
> Y cinco, **el historial del cliente vive en los celulares** de cada persona: si esa persona no está, nadie más lo encuentra.
>
> Cada punto nos dio una función del sistema y una meta. La espera y la asignación van a M1 y M3, la cotización a M2 y el historial a M4. Donde dice "sin dato" es porque eso lo vamos a medir con los documentos de la empresa, no lo estamos suponiendo.»

## Diapositiva 5 · Diseño (1:15)

> «Con el sistema pasamos de un mensaje que espera a **una solicitud con responsable**.
>
> La solicitud entra con su hora registrada y avisa al responsable. Si en 15 minutos nadie la toma, le recuerda y avisa a la gerencia. Para cotizar, el asistente con IA propone un borrador, pero **no pone precios** y **siempre lo revisa una persona** antes de que salga algo al cliente.
>
> Son **24 requisitos**, y cada uno está ligado a una meta. Los modelamos en **12 casos de uso** y un modelo de **9 entidades**.
>
> Y el número que más nos importa es el **cero**: la IA no lee ningún dato personal. Solo ve códigos de cliente, nunca nombres ni teléfonos. Los contactos quedan aparte, en una carpeta a la que la IA no entra.»

## Diapositiva 6 · Prueba de concepto (1:00)

> «La prueba de concepto ya hace **el recorrido completo, con datos ficticios**: el formulario, el servidor, la bóveda y el borrador del asistente.
>
> Para medir en condiciones controladas tenemos tres casos de prueba:
> CP-01, la misma cotización con y sin el asistente, para M2.
> CP-02, recuperar el historial de un cliente que no es tuyo, para M4.
> Y CP-03, alterar el registro a propósito y ver si la verificación lo detecta, para M5. En la prueba del 8 de noviembre detectó las tres alteraciones que hicimos.
>
> Los tiempos que ven ahí son objetivos de diseño, todavía no están medidos. Y una cosa que queremos que usted decida: el capítulo I dice cuatro casos. Si la evaluación heurística cuenta como el cuarto, se queda así.»

## Si pregunta (respuestas cortas)

- **¿La IA puede inventar precios?** No. El borrador sale sin precios, dice qué documentos usó y siempre lo revisa una persona (RQ-12).
- **¿Y la seguridad de los datos?** La IA solo ve códigos (RQ-21). El registro tiene huellas encadenadas, así que una alteración se detecta (RQ-15 y RQ-16). Y separamos las claves: la del formulario público solo puede crear solicitudes, no leerlas.
- **¿Qué pasa si se borran los últimos eventos del registro?** Eso no se detecta solo. Por eso cada lunes se publica la última huella en el reporte semanal, como ancla, y lo declaramos como limitación.
- **¿Ya lo usan en Torvesa?** No. Todo es con datos ficticios. La validación del diseño en operación experimental controlada empieza cuando Torvesa autorice y usted apruebe la forma de medir.
- **¿Qué modelo de IA usan?** El de la prueba de concepto es Claude Sonnet 5.5. La elección final la cerramos con Víctor.
