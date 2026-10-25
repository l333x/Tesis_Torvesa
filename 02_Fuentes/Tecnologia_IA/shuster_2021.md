---
citekey: shuster_2021
referencia_apa: "Shuster, K., Poff, S., Chen, M., Kiela, D., & Weston, J. (2021). Retrieval augmentation reduces hallucination in conversation. En M.-F. Moens, X. Huang, L. Specia, & S. W. Yih (Eds.), *Findings of the Association for Computational Linguistics: EMNLP 2021* (pp. 3784–3803). Association for Computational Linguistics. https://doi.org/10.18653/v1/2021.findings-emnlp.320"
doi_url: "https://doi.org/10.18653/v1/2021.findings-emnlp.320"
anio: 2021
fecha_publicacion: "2021-11"
tipo: articulo
categoria: Tecnologia_IA
objetivos: [6.1]
afirmaciones: [A37]
afirmacion: "En asistentes conversacionales, sumar recuperación de documentos redujo las respuestas inventadas en más del 60 %."
cita_textual: "We show through automatic and human evaluations that standard (non-retrieval augmented) large language models indeed suffer from hallucination, whereas our best models substantially curtail the issue, reducing hallucinated responses by over 60%."
pagina: "p. 3785"
confianza: alto
estado: verificada
vigencia: vigente
verificada_por: "IA de Diego (lectura del texto completo); falta visto bueno de Diego"
fecha_verificacion: 2026-10-21
acceso: "abierto"
texto_local: "02_Fuentes/_Textos/shuster_2021.pdf"
origen_busqueda: "ACL Anthology · consulta D02 · 2026-10-21 (búsqueda manual)"
seminal: false
tags: [fuente, verificada, vigente, articulo]
---

# Retrieval Augmentation Reduces Hallucination in Conversation

## Qué respalda
Experimento con modelos de diálogo (Facebook AI Research): los modelos sin recuperación inventan datos («alucinan»), y los mismos modelos con recuperación de documentos reducen las respuestas alucinadas en más del 60 %, según evaluación humana. También muestra que el efecto tiene límites: al darle más documentos al modelo, la alucinación vuelve a subir.

## Cita textual
> «We show through automatic and human evaluations that standard (non-retrieval augmented) large language models indeed suffer from hallucination, whereas our best models substantially curtail the issue, reducing hallucinated responses by over 60%.» (p. 3785)

## Cómo se usa en la tesis
Cap. 2, marco teórico (A37): evidencia empírica, revisada por pares, de que la recuperación reduce los errores de contenido en asistentes conversacionales. Es de 2021: complementa a las fuentes de 2023+ (bechard_2024, magesh_2025), no las reemplaza.

## Notas de verificación
PDF de ACL Anthology (Findings of EMNLP 2021, revisado por pares) abierto el 21-oct. El dato del 60 % está en la Introducción, p. 3785. La evaluación humana (§4, p. 3789, Tabla 4) dice: «Hallucination rates drop dramatically for retrieval-augmented models». Limitación anotada por los autores (p. 3792): «all models suffer from more hallucination when we condition on more documents for each generation». Contexto: diálogo de dominio abierto sobre Wikipedia, no documentos de empresa.
