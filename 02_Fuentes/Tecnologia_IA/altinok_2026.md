---
citekey: altinok_2026
referencia_apa: "Altinok, H., Tekgöz, H., Erdoğan, H., & Uz, H. (2026). A Comparative Analysis of Retrieval-Augmented Generation Architectures with Semantic Hashing for Enterprise Knowledge Systems. *International Informatics and Software Engineering Conference (IISEC)*. https://doi.org/10.1109/iisec69317.2026.11418525"
doi_url: "https://doi.org/10.1109/iisec69317.2026.11418525"
anio: 2026
tipo: conference-paper
categoria: Tecnologia_IA
objetivos: [6.1]
afirmaciones: []
afirmacion: ""
cita_textual: ""
pagina: ""
confianza: medio
estado: candidata
verificada_por: ""
fecha_verificacion:
acceso: "institucional"
texto_local: ""
origen_busqueda: "OpenAlex · consulta D02 · 2026-10-21"
seminal: false
tags: [fuente, candidata]
---

# A Comparative Analysis of Retrieval-Augmented Generation Architectures with Semantic Hashing for Enterprise Knowledge Systems

> [!warning] Candidata: no se puede citar
> Ficha creada automáticamente desde **OpenAlex**. La referencia APA es aproximada. Para pasarla a `estado: verificada`: abre la fuente, comprueba el dato, anota la página y la cita textual.

## Resumen (de la base de datos, no de la lectura)
Large Language Models (LLMs) have significant potential to transform enterprise knowledge management. The Retrieval-Augmented Generation (RAG) architecture has become the industry standard for producing accurate, domain-specific responses while mitigating hallucinations. However, the retrieval stage in standard RAG implementations presents challenges in terms of latency, computational cost, and accuracy when scaling to large document collections. This paper presents a systematic comparative analysis of four distinct RAG retrieval architectures evaluated on a real-world enterprise wiki dataset containing 279 documents across 14 categories. The architectures examined include: (1) Dense Retrieval using FAISS, (2) Hybrid Retrieval combining FAISS with BM25, (3) Semantic Hashing-only retrieval, and (4) a novel two-stage hybrid model employing Semantic Hashing for candidate filtering followed by vector-based reranking. We evaluate these architectures using 84 domain-specific questions, measuring answer accuracy through semantic similarity, query latency, and memory consumption. Our experimental results demonstrate that the two-stage hybrid architecture achieves the highest accuracy rate of 82.14% with a mean response time of 2.96 seconds, outperforming both pure dense retrieval (78.57%) and hybrid BM25 approaches (64.29%). We provide detailed analysis of prompt engineering strategies that contributed to these results and discuss the trade-offs between retrieval speed, accuracy, and resource utilization for enterprise-scale RAG deployments.

## Qué respalda
<!-- La idea con tus palabras (no copies el resumen). -->

## Cita textual
> «…» (p. X)

## Notas de verificación
Para bajar a mano (21-oct): ponencia IEEE de pago (OpenAlex la marca cerrada), revisada por pares y pertinente: compara cuatro arquitecturas RAG sobre la wiki real de una empresa. Probar con el acceso de la UPS a IEEE Xplore. Sin leer el texto no se le asigna afirmación (tenía A37 puesto de forma automática).
