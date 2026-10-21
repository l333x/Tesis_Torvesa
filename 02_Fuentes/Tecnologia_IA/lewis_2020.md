---
citekey: lewis_2020
referencia_apa: "Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *Advances in Neural Information Processing Systems, 33*, 9459–9474."
doi_url: "https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html"
anio: 2020
tipo: articulo
categoria: Tecnologia_IA
objetivos: [5.3]
afirmaciones: [A37]
afirmacion: "Origen del término RAG: los modelos que solo usan su memoria interna pueden «alucinar»; combinarlos con la recuperación de documentos permite revisar y ampliar el conocimiento e inspeccionar de dónde sale la respuesta. En sus pruebas, RAG «alucina» menos que el modelo sin recuperación."
cita_textual: "Qualitatively, we find that RAG models hallucinate less and generate factually correct text more often than BART."
pagina: "p. 9464 (§4.2; p. 6 del PDF). Problema de las «hallucinations» y ventaja de la memoria recuperable: p. 9459 (p. 1 del PDF). Broader Impact: p. 9468 (p. 10 del PDF)"
confianza: alto
estado: verificada
vigencia: vigente
verificada_por: "Claude (lectura de la fuente); falta visto bueno de Víctor"
fecha_verificacion: 2026-10-21
acceso: "abierto"
texto_local: "02_Fuentes/_Textos/lewis_2020.pdf"
seminal: true
tags: [fuente, verificada, vigente, articulo]
---

# Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

## Qué respalda
Es el artículo que acuña RAG (NeurIPS 2020). P. 9459: los modelos de lenguaje sin memoria externa no pueden revisar ni ampliar fácilmente lo que saben, no muestran de dónde sale la predicción y pueden producir «hallucinations»; los modelos híbridos con memoria recuperable permiten revisar, ampliar e inspeccionar el conocimiento. P. 9464: en la evaluación cualitativa, RAG alucina menos y genera texto correcto con más frecuencia que BART.

## Cita textual
> «Qualitatively, we find that RAG models hallucinate less and generate factually correct text more often than BART.» (p. 9464)

## Cómo se usa en la tesis
Cap. II, § IA y RAG: origen del término (reemplaza el [FALTA-FUENTE] de A37 junto con Brehme, 2025). Cap. 5: justifica que el asistente responda apoyado en las fichas de la bóveda.

## Notas de verificación
PDF oficial de NeurIPS (16 págs.), bajado el 21-oct de proceedings.neurips.cc. Las páginas del volumen (9459–9474) se calculan desde la p. 1 del PDF = 9459. **Ojo:** «alucina menos» es una observación cualitativa en tareas de preguntas abiertas sobre Wikipedia, no una medición en empresas: no decir que RAG «elimina» los errores. Es de 2020 (origen del concepto); va con Brehme (2025) como evidencia reciente.
