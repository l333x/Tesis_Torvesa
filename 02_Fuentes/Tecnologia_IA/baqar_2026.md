---
citekey: baqar_2026
referencia_apa: "Baqar, M. (2026). Retrieval-augmented generation in enterprise knowledge systems: Architecture, benefits, and applications. *International Journal of Electrical and Computer Engineering (IJECE)*, *16*(3), 1407–1416. https://doi.org/10.11591/ijece.v16i3.pp1407-1416"
doi_url: "https://doi.org/10.11591/ijece.v16i3.pp1407-1416"
anio: 2026
fecha_publicacion: "2026-06"
tipo: articulo
categoria: Tecnologia_IA
objetivos: [6.1]
afirmaciones: []
afirmacion: "En una empresa grande, un asistente RAG sobre su documentación interna dio más recomendaciones correctas (82 % frente a 46 %) que la búsqueda por palabras clave."
cita_textual: "For solution quality, independent evaluators marked 82% of RAG-generated recommendations as correct compared with 46% for the baseline workflow. Because the generation step was constrained by retrieved evidence, the system reduced unsupported suggestions while still synthesizing a usable answer."
pagina: "p. 1412"
confianza: bajo
estado: verificada
vigencia: vigente
verificada_por: "IA de Diego (lectura del texto completo); falta visto bueno de Diego"
fecha_verificacion: 2026-10-21
acceso: "abierto"
texto_local: "02_Fuentes/_Textos/baqar_2026.pdf"
origen_busqueda: "OpenAlex · consulta D02 · 2026-10-21"
seminal: false
tags: [fuente, verificada, vigente, articulo]
---

# Retrieval-augmented generation in enterprise knowledge systems: architecture, benefits, and applications

## Qué respalda
Caso de RAG sobre el conocimiento interno de una empresa (documentación, tickets, código y reuniones): 500 consultas reales y seis semanas de uso con unos 120 usuarios. Frente a la búsqueda por palabras clave, mejoró la relevancia de lo recuperado, las recomendaciones correctas y el tiempo para resolver problemas. Entre los riesgos pendientes, el autor lista las respuestas incorrectas o no verificables y la falta de confianza si no se muestran las fuentes.

## Cita textual
> «For solution quality, independent evaluators marked 82% of RAG-generated recommendations as correct compared with 46% for the baseline workflow. Because the generation step was constrained by retrieved evidence, the system reduced unsupported suggestions while still synthesizing a usable answer.» (p. 1412)

## Cómo se usa en la tesis
Cap. 5, diseño del asistente: ejemplo de arquitectura RAG empresarial (ingesta de varias fuentes, índice semántico, citas a la fuente) y de qué medir al validar (relevancia, respuestas correctas, tiempo). **No** respalda A37: la comparación es contra la búsqueda por palabras clave, no contra un modelo de lenguaje sin recuperación.

## Notas de verificación
PDF del editor (IJECE, editorial IAES, acceso abierto CC BY-SA) abierto el 21-oct. Revisado por pares (recibido sep-2025, aceptado abr-2026). Dato en §4.2, p. 1412; riesgos en la Tabla 2, p. 1413. **Confianza baja**: un solo autor (ingeniero de Cisco), sin intervalos de confianza (él mismo lo admite en p. 1413) y la empresa del piloto no se nombra; el resumen habla de horas de resolución (18,4 h → 7,2 h, Tabla 1) y el texto, de minutos en sesiones simuladas (34 → 12 min), que son medidas distintas. No comprobé la indexación actual de la revista. Usar solo como ejemplo de diseño, no como evidencia principal.
