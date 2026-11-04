---
titulo: Guion de ensayo — Revisión 1 con la tutora (versión 4-nov)
fecha: 2026-11-04
tarea: S3-T03 (ensayo) · S3-T05 (Revisión 1)
presentacion: 2026-11-04_Presentacion_Revision1.pptx (16 diapositivas)
hoja: 2026-11-04_Puntos_Revision1.pdf (5 páginas)
duracion_objetivo: 13 min de exposición + diálogo
reemplaza: 2026-10-29_Guion_Ensayo.md (la reunión del 29-oct no se hizo)
tags: [tutora, revision1, ensayo]
---

# Guion de ensayo · Revisión 1 (jueves 5 o viernes 6 de noviembre)

> Ensayar una vez completo con cronómetro. Si pasa de 14 min, en las diapositivas 7, 8 y 12 decir solo el mensaje.
> Reglas al hablar:
> - decir «validación del diseño en operación experimental controlada» (nunca «piloto» ni «implementado»);
> - no dar cifras de Torvesa que aún no se han medido;
> - el cambio de método es una **propuesta**: la decide la tutora.

## El mensaje de la reunión
Traemos el diseño casi completo y una propuesta: **medir sin recoger datos de personas**. Necesitamos su visto bueno para reescribir el Cap. III.

## Quién dice qué y cuánto tiempo

| # | Diapositiva | Quién | Tiempo | Mensaje que debe quedar |
|---|---|---|---|---|
| 1 | Portada | Víctor | 0:20 | Qué traemos y que al final le pedimos seis decisiones |
| 2 | Qué traemos hoy | Víctor | 0:40 | Capítulos en v0.3, fuentes verificadas, seis piezas de diseño y un cambio de método |
| 3 | El problema | Víctor | 1:00 | La atención depende de una persona y de su celular |
| 4 | Objetivos | Víctor | 0:45 | OE1 ahora usa documentos de la empresa; OE3 se precisa |
| 5 | Metodología (DSR) | Víctor | 1:00 | Se mantiene la DSR y el antes y después; cambia qué se analiza y con qué |
| 6 | **Propuesta: sin datos de personas** | Víctor | 2:00 | Por qué (lo que dijo la directora a Diego), cómo se mide cada meta y qué perdemos (el número SUS). **Diego confirma lo que le dijeron** |
| 7 | Marco teórico | Víctor | 0:30 | Seis ideas, cada una con fuentes verificadas |
| 8 | Fuentes | Víctor | 0:45 | 93 verificadas; lo que la evidencia corrigió |
| 9 | Proceso actual (AS-IS) | Diego | 1:00 | Cinco puntos donde se pierde tiempo o información; se contrasta con la muestra de solicitudes |
| 10 | Proceso con el sistema (TO-BE) | Diego | 1:15 | Seis pasos en tres diagramas; cada paso con disparador y responsable |
| 11 | Casos de uso y bóveda | Diego | 1:15 | 12 casos de uso; la memoria comercial queda en la empresa; datos personales aparte, que la IA no lee |
| 12 | Herramientas | Diego | 0:40 | Ocho criterios; el de más peso es la protección de datos |
| 13 | Requerimientos | Diego | 0:40 | 24 requerimientos trazables; el nuevo guarda la hora del primer contacto (sin él no se mide M1) |
| 14 | Cronograma | Víctor | 0:30 | El diseño va adelantado; la validación sigue del 24-nov al 5-dic |
| 15 | Riesgos | Víctor | 0:40 | Los documentos de Torvesa y volver a publicar TEAMSLASH (9-nov) |
| 16 | Decisiones | Víctor | 1:00 + diálogo | Leer las cinco preguntas y entregar la hoja para el resto |
| | **Total** | | **≈ 13:00** | |

## Qué anotar durante la reunión
- La respuesta a cada punto de la sección 3 de la hoja (del 1 al 9) y de la sección 4 (del 10 al 17).
- Cada observación con responsable y plazo, en la sección 5 de la hoja.
- Si ofrece la carta de respaldo para Torvesa.
- La fecha de la Revisión 2 (en el cronograma, hacia el 18-nov).

Todo va al acta (`2026-11-0X_Acta_Revision1.md`) y a la app: DEC-18, DEC-19 y DEC-20, y las decisiones nuevas del cambio de método, del enfoque y de M6.

## Preguntas probables de la tutora y respuesta corta

1. **¿Quién les dijo lo de la autorización?**
   La directora de carrera, a Diego, el 2-nov. Por eso se lo traemos a usted: queremos que lo confirme y nos diga si hay que hacer algo con la Dirección.

2. **¿Sin encuestas la tesis sigue teniendo datos?**
   Sí. Hay tres fuentes:
   - la muestra de solicitudes de 3 meses (solo fechas y horas), que da la línea base de M1 y M3;
   - el registro del propio sistema durante la validación;
   - pruebas que hacemos nosotros: M2, M4 y M5.

3. **¿Y la usabilidad (M6)?**
   Sin usuarios no hay SUS. Proponemos una evaluación heurística del diseño, hecha por el equipo con una lista reconocida de principios. Es más débil que el SUS y lo declaramos como limitación. La fuente se verifica antes de citarla.

4. **¿Sigue siendo «mixto»?**
   Sin entrevistas ni preguntas abiertas a personas, no hay parte cualitativa con personas. Proponemos «cuantitativo»; el nombre lo decide usted.

5. **¿Por qué no hay datos de Torvesa todavía?**
   Porque el diagnóstico anterior (N = 30) era simulado y lo descartamos. Ahora solo pedimos documentos (fechas y horas), y eso es más fácil de autorizar. Si no responden, le pedimos una carta de respaldo.

6. **¿De dónde salen los 15 minutos de M1?**
   Es una meta de diseño, no un estándar probado. Lo dice el capítulo I.

7. **¿El TO-BE y la bóveda están validados?**
   Son la versión 0.1, con datos ficticios. Lo que no está confirmado por Torvesa va marcado «por validar», por ejemplo la regla para elegir al responsable. Se contrasta con los documentos y con el prototipo.

8. **¿TEAMSLASH funciona?**
   El código existe y guarda en PostgreSQL, pero hoy el servicio no está en línea. Diego lo vuelve a publicar el 9-nov, antes de la prueba de concepto.

9. **¿Por qué DSR y no un diseño experimental clásico?**
   Porque el trabajo construye y evalúa un artefacto. La evaluación es una comparación antes y después en un solo grupo. El nombre exacto lo decide usted (punto 4 de la hoja).

## Antes de entrar (5 min)
1. Imprimir 2 copias de `2026-11-04_Puntos_Revision1.pdf`: una para la tutora y otra para anotar.
2. Confirmar con Diego:
   - que habla unos 5 minutos (diapositivas 9 a 13);
   - que puede contar en una frase qué le dijo la directora y cuándo.
3. Llevar abiertos en el portátil:
   - el Cap. III v0.3;
   - el aviso de Diego (`00_Inbox/2026-11-02_aviso_sin_encuestas_ni_entrevistas.md`);
   - el TO-BE parte 1.
