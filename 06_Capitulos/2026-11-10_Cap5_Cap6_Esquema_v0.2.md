---
titulo: "Capítulos V y VI · Esquema (evaluación y resultados; conclusiones y recomendaciones)"
version: "0.2"
fecha: 2026-11-10
autor_borrador: "Claude Opus 5.5 (Víctor edita)"
nota: "Solo el esquema: estos capítulos se escriben con los resultados de la validación (sprint 9). Va en el borrador 1 para que la tutora vea la estructura completa."
tags: [capitulo5, capitulo6, esquema, borrador]
---

# CAPÍTULO V

# EVALUACIÓN Y RESULTADOS

Este capítulo corresponde a las actividades de demostración y evaluación de la investigación en ciencia del diseño. Se escribe con los resultados de los casos de prueba y de la validación del diseño en operación experimental controlada. Su estructura prevista es la siguiente.

## Prueba de concepto

La prueba de concepto se construyó el 8 de noviembre de 2026 y recorre el flujo completo con datos ficticios: el cliente llena el formulario y da su consentimiento, el servidor guarda la solicitud con su hora de llegada, el equipo recibe el aviso, quien pulsa «Tomar» queda como responsable, la solicitud y la ficha del cliente aparecen en la bóveda sin datos personales, y el asistente propone un borrador de cotización que una persona revisa.

En la primera prueba, con una solicitud ficticia de una cocina de 12 m², el asistente entregó el borrador en 15 segundos, sin precios y con 11 preguntas para completar la cotización; el teléfono escrito en la descripción no llegó al asistente. En la prueba del registro, la verificación detectó tres de tres alteraciones. Son comprobaciones de funcionamiento, no resultados de la evaluación: las metas se miden con los casos de prueba y con la validación. Faltan por publicar y probar el recordatorio a los 15 minutos, el motivo de pérdida obligatorio y el reporte semanal [FALTA-DATO: prueba de estas funciones, sprint 6].

## Casos de prueba

Se diseñaron tres casos de prueba. Los ejecutan los dos autores, con datos ficticios, la mitad de las tareas con el sistema y la mitad sin él, en orden cruzado; quien prepara el material de un caso no lo ejecuta cuando conocer las respuestas cambia el resultado. Con tan pocas mediciones se reportan medianas, mínimos y máximos, sin pruebas estadísticas. [DECIDIR-VÍCTOR: aprobar los casos de prueba; los capítulos I y III dicen «cuatro casos» y aquí son tres más la evaluación de la usabilidad] [DECIDIR-TUTORA: que los casos los ejecuten los autores depende de la propuesta de no recoger datos de personas]

Resultados de los casos de prueba, uno por meta que se mide en condiciones controladas: el tiempo de elaboración de una cotización con y sin el asistente (M2), la recuperación del historial de un cliente ajeno con y sin la bóveda (M4) y la detección de alteraciones del registro (M5) [FALTA-DATO: resultados de los casos de prueba].

## Validación del diseño en operación experimental controlada

Comparación del antes y el después con las solicitudes reales que ingresen durante la validación: tiempo de primer contacto (M1) y clientes perdidos antes del primer contacto (M3), con la mediana, el rango intercuartílico y, si el número de solicitudes lo permite, una prueba no paramétrica [FALTA-DATO: resultados de la validación].

## Evaluación de la usabilidad

Resultado de la evaluación de la usabilidad (M6), con el instrumento que se acuerde con la tutora [DECIDIR-TUTORA: cuestionario SUS a los usuarios o evaluación heurística hecha por el equipo].

## Discusión y limitaciones

Contraste de los resultados con los antecedentes del capítulo II y con las limitaciones declaradas en el capítulo I.

# CAPÍTULO VI

# CONCLUSIONES Y RECOMENDACIONES

## Conclusiones

Se redacta una conclusión por cada objetivo específico:

- Sobre el OE1 (diagnóstico del proceso actual y línea base).
- Sobre el OE2 (diseño de la arquitectura, los procesos TO-BE y la viabilidad).
- Sobre el OE3 (prototipo funcional de los componentes).
- Sobre el OE4 (validación del diseño frente a la línea base).
- Sobre el OE5 (manual de operación, gobierno de la información y transferencia).

## Recomendaciones

Recomendaciones para la Constructora Torvesa, sobre la adopción del sistema y el gobierno de su información comercial, y para futuras investigaciones.
