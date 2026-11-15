---
citekey: aws_sfd
referencia_apa: "Amazon Web Services. (s. f.-d). *Comparing Retrieval Augmented Generation and fine-tuning*. AWS Prescriptive Guidance. Recuperado el 10 de noviembre de 2026, de https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/rag-vs-fine-tuning.html"
doi_url: "https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/rag-vs-fine-tuning.html"
anio: s.f.
tipo: pagina_web
categoria: Costos_Viabilidad
objetivos: [5.3]
afirmaciones: []
afirmacion: "AWS recomienda empezar por RAG para responder preguntas sobre documentos propios; el ajuste fino tarda de horas a días, puede requerir un científico de datos, no cita la fuente en sus respuestas y puede aumentar el riesgo de alucinación."
cita_textual: "If you need to build a question-answering solution that references your custom documents, then we recommend that you start from a RAG-based approach."
pagina: "Página web (sin paginación): tabla de ventajas y desventajas y párrafo siguiente"
cita_en_texto: "(AWS, s. f.-d)"
confianza: alto
estado: verificada
vigencia: vigente
verificada_por: "Claude (lectura de la fuente); falta visto bueno de Víctor"
fecha_verificacion: 2026-11-10
acceso: "abierto"
texto_local: ""
origen_busqueda: "Página oficial · Frente A: modelo financiero y matriz de herramientas (S4-T08, S4-T10, S4-T12, S5-T01) · 2026-11-10 (búsqueda manual)"
seminal: false
tags: [fuente, verificada, vigente, pagina_web, viabilidad]
---

# Comparing Retrieval Augmented Generation and fine-tuning

## Qué respalda
Guía oficial de AWS que compara RAG con el ajuste fino:

- **RAG:** incorpora documentos nuevos en minutos, cita la fuente y reduce el riesgo de alucinación. No sirve bien para resumir documentos enteros.
- **Ajuste fino:** tarda de horas a días, puede requerir un científico de datos, no cita la fuente y puede aumentar el riesgo de alucinación.
- Recomienda empezar por RAG y usar el ajuste fino para tareas adicionales, como resumir.

## Cita textual
> «If you need to build a question-answering solution that references your custom documents, then we recommend that you start from a RAG-based approach.» (Página web)

Literal (tabla): «Fine-tuning might require a data scientist.»; «Fine-tuned models do not provide a reference to the source in their responses.»; «There can be an increased risk of hallucination when using a fine-tuned model to answer questions.»; «RAG can incorporate the latest documents in a few minutes.»; «In its response, a RAG model provides a reference to the information source.»

## Cómo se usa en la tesis
Matriz de herramientas (hojas `Evidencia` y `Ruta_AWS`) y `2026-11-10_Analisis_Financiero_v0.1.md`, sección 4: por qué hoy no conviene entrenar un modelo propio con los datos de Torvesa. Complementa a Lewis et al. (2020) en el Cap. II.

## Notas de verificación
- Se leyó el texto completo de la página (no un resumen).
- Es documentación de un proveedor: sirve para decir qué recomienda AWS, no como evidencia académica independiente.
