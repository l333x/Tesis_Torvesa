---
titulo: "Guion de ensayo: Revisión 2 con la tutora"
version: v0.2
fecha: 2026-11-18
tarea: "S6-T01 (presentación) · S6-T02 (ensayo) · S6-T04 (Revisión 2)"
presentacion: "2026-11-18_Revision2_Presentacion_v0.2.pptx (10 diapositivas)"
borrador: "Borrador 3 de la tesis (Frente A, 16-nov)"
duracion_objetivo: "unos 10 min de exposición + diálogo"
reemplaza: "2026-11-16_Revision2_Guion_v0.1.md (queda igual). Cambios: CP-04, claves separadas, avance y fecha de la validación"
tags: [tutora, revision2, ensayo]
---

# Guion de ensayo de la Revisión 2

**Qué cambió en la v0.2 (18-nov):**
- Diapositiva 6: cuatro casos de prueba. CP-04 es la evaluación heurística (M6) y solo cuenta si la tutora acepta DEC-23 (propuesta de Diego, 15-nov). CP-03 pasa a 20 alteraciones al azar.
- Diapositiva 5 (notas): las claves del servidor ya están separadas desde el 16-nov.
- Diapositiva 9: la validación empieza cuando Torvesa autorice (estaba prevista del 23-nov al 5-dic); el avance va del 37 % al 43 %, con el 45 % del tiempo transcurrido.
- Preguntas 4 y 10, y pregunta nueva 11.
- La parte de Diego está en `00_Inbox/2026-11-15_Guion_Diego_Diapositivas_4a6.md`.

Ensayen una vez completo con cronómetro. Si pasan de 11 minutos, en las diapositivas 4, 5 y 6 digan solo el mensaje.

**Reglas al hablar:**
- decir siempre «validación del diseño en operación experimental controlada», nunca «piloto» ni «implementado»;
- no dar cifras de Torvesa que aún no se midieron; el censo de 5 personas es un antecedente, no la línea base;
- la forma de medir sin datos de personas es una **propuesta**: la decide la tutora.

## El mensaje de la reunión

Traemos el **borrador 3 de la tesis** para que nos corrija sobre él, el **estudio de costos** y la **prueba de concepto**. Le pedimos **seis decisiones**; con ellas reescribimos el capítulo III y arrancamos la validación.

## Quién dice qué y cuánto tiempo

| # | Diapositiva | Quién | Tiempo | Mensaje que debe quedar |
|---|---|---|---|---|
| 1 | Portada | Víctor | 0:20 | Qué traemos y que al final pedimos seis decisiones |
| 2 | Qué traemos | Víctor | 0:40 | Borrador 3, estudio de costos y prueba de concepto. Lo amarillo del borrador es lo que falta o lo que ella decide |
| 3 | El problema | Víctor | 1:00 | La atención depende de una persona y de su celular. El censo es antecedente, no línea base |
| 4 | Proceso actual | Diego | 1:00 | Cinco puntos críticos, y cada uno da una función y una meta |
| 5 | Diseño | Diego | 1:15 | De un mensaje que espera a una solicitud con responsable. Son 24 requisitos trazables, y la IA no ve datos personales |
| 6 | Prueba de concepto | Diego | 1:00 | El recorrido funciona con datos ficticios, y hay tres casos de prueba listos, más un cuarto si acepta la heurística |
| 7 | Datos (propuesta) | Víctor | 2:00 | Cómo se mide cada meta sin datos de personas. Lo que perdemos es el SUS |
| 8 | Viabilidad | Víctor | 1:30 | Con un solo cliente, solo el Premium alcanza. Casi todo lo de Torvesa es todavía supuesto |
| 9 | Cronograma | Víctor | 0:40 | La fecha límite sigue en el 4 de enero. La validación empieza cuando Torvesa autorice, y esa es la ruta crítica |
| 10 | Decisiones | Víctor | 1:00 + diálogo | Leer las seis preguntas y acordar cómo y cuándo nos devuelve las observaciones |
| | **Total** | | **≈ 10:25** | |

El guion de cada diapositiva está en las notas del orador de la presentación.

## Qué anotar durante la reunión

- La respuesta a DEC-18, DEC-19, DEC-20, DEC-21, DEC-22 y DEC-23.
- Cada observación, con su responsable y su plazo.
- Si ofrece una carta de respaldo para Torvesa.
- Cómo y cuándo devuelve las observaciones del borrador 3.
- La fecha de la siguiente reunión.

Todo va al acta. La plantilla es `2026-11-16_Acta_Revision2_PLANTILLA.md`, en la carpeta de planificación. Las respuestas se pasan también a la app Bitácora Torvesa.

## Preguntas probables y respuesta corta

1. **¿Por qué no se hizo la Revisión 1?**
   No llegamos a coordinar la cita a tiempo. Por eso hoy juntamos las dos y traemos un borrador más completo.

2. **¿Sin encuestas, la tesis sigue teniendo datos?**
   Sí, de tres fuentes:
   - las fechas y horas de 3 meses de solicitudes de la empresa, que dan la línea base de M1 y M3;
   - el registro del propio sistema durante la validación;
   - los tres casos de prueba que hacemos nosotros, para M2, M4 y M5.

3. **¿Y la usabilidad (M6)?**
   Sin usuarios no hay SUS. Proponemos una evaluación heurística hecha por el equipo con una lista reconocida de principios. Es más débil, y lo declaramos como limitación.

4. **¿Cuántos casos de prueba son?**
   Cuatro, como dice el Cap. I: CP-01 a CP-03 y la evaluación heurística como CP-04, si usted acepta la propuesta de M6 (DEC-23). Si no la acepta, quedan tres y corregimos el Cap. I.

5. **¿De dónde salen los 15 minutos de M1?**
   Es una meta de diseño, no un estándar probado. Lo dice el capítulo I.

6. **¿Las cifras de viabilidad son reales?**
   Las de nuestro lado (costos, sueldos, impuestos, mercado) son datos con fuente en el 71 % de los casos. Las de Torvesa son reales solo en el 6 %. Por eso le pediremos a Torvesa sus formularios 101 de 2023 a 2025. El modelo marca, fila por fila, qué es dato y qué es supuesto.

7. **¿Por qué una TMAR del 15 % y no del 12 %?**
   Solo la prima de riesgo de Ecuador ya es 17,18 % (Damodaran, 2026). El 12 % no se sostenía. El 15 % es la TMAR del Informe Final, y el escenario pesimista usa 17,18 %.

8. **¿Qué pasa si Torvesa no autoriza a tiempo?**
   Es la ruta crítica. Diego la está gestionando. Si usted puede darnos una carta de respaldo, la usamos. Si no hay respuesta, le pedimos a usted cómo seguir [DECIDIR-TUTORA].

9. **¿Torvesa hace edificios o vías?**
   Según el SRI, está registrada como constructora de carreteras. Lo estamos confirmando con la empresa, porque cambia la descripción del capítulo I.

10. **¿La IA inventa precios?**
    No. El borrador del asistente sale sin precios, cita los documentos de la bóveda que usó y siempre lo revisa una persona (RQ-12). La IA solo ve códigos de cliente, nunca nombres ni teléfonos (RQ-21). Además, desde el 16-nov la clave del formulario público solo puede crear solicitudes; leerlas exige otra clave que nunca está en el navegador.

11. **La validación empieza el 23-nov y Torvesa no ha autorizado. ¿Se llega?**
    La validación dura dos semanas y arranca el día que Torvesa autorice. Si se corre, se acorta la etapa de medición, no la entrega del 4 de enero. Por eso le pedimos la carta de respaldo y la respuesta a DEC-21, que es lo que necesitamos para enviar las fechas a Torvesa.
