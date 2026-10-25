---
citekey: bechard_2024
referencia_apa: "Béchard, P., & Marquez Ayala, O. (2024). Reducing hallucination in structured outputs via Retrieval-Augmented Generation. En Y. Yang, A. Davani, A. Sil, & A. Kumar (Eds.), *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 6: Industry Track)* (pp. 228–238). Association for Computational Linguistics. https://doi.org/10.18653/v1/2024.naacl-industry.19"
doi_url: "https://doi.org/10.18653/v1/2024.naacl-industry.19"
anio: 2024
fecha_publicacion: "2024-06"
tipo: articulo
categoria: Tecnologia_IA
objetivos: [6.1]
afirmaciones: [A37]
afirmacion: "En una aplicación empresarial real, RAG bajó los elementos inventados de hasta 21 % a menos de 7,5 %, pero no eliminó el riesgo y se mantuvo una revisión del usuario."
cita_textual: "Table 4 shows that without a retriever (only LLM fine-tuning), the % of hallucinated steps and tables can be as high as 21% on the \"Human Eval\" split. Using a retriever, this decreases to less than 7.5% for steps and less than 4.5% for tables with all StarCoderBase LLMs."
pagina: "p. 233"
confianza: alto
estado: verificada
vigencia: vigente
verificada_por: "IA de Diego (lectura del texto completo); falta visto bueno de Diego"
fecha_verificacion: 2026-10-21
acceso: "abierto"
texto_local: "02_Fuentes/_Textos/bechard_2024.pdf"
origen_busqueda: "ACL Anthology · consulta D02 · 2026-10-21 (búsqueda manual)"
seminal: false
tags: [fuente, verificada, vigente, articulo]
---

# Reducing hallucination in structured outputs via Retrieval-Augmented Generation

## Qué respalda
Caso industrial (ServiceNow): un sistema que convierte pedidos en lenguaje natural en flujos de trabajo. Sin recuperación, hasta el 21 % de los pasos y tablas generados no existían; con RAG bajó a menos del 7,5 % (pasos) y 4,5 % (tablas). Los autores aclaran que el riesgo no desaparece y que el sistema desplegado marca al usuario lo que no existe para que lo corrija antes de seguir.

## Cita textual
> «Table 4 shows that without a retriever (only LLM fine-tuning), the % of hallucinated steps and tables can be as high as 21% on the "Human Eval" split. Using a retriever, this decreases to less than 7.5% for steps and less than 4.5% for tables with all StarCoderBase LLMs.» (p. 233)

Sobre el límite (no elimina):
> «While our work proposes an approach to reduce hallucination in structure output tasks, we do not claim that the risk of harm due to hallucination is eliminated.» (p. 234)

## Cómo se usa en la tesis
Cap. 2, marco teórico (A37): estudio de 2024, revisado por pares y en un producto empresarial, de que RAG reduce los errores sin eliminarlos. Cap. 5, diseño del asistente: respalda que el borrador lo revise el vendedor antes de enviarlo (el sistema de ServiceNow también pide al usuario corregir antes de continuar).

## Notas de verificación
PDF de ACL Anthology (NAACL 2024, Industry Track, revisado por pares) abierto el 21-oct. Datos en §5.2, p. 233 (Tabla 4); la advertencia está en «Ethical Considerations», p. 234. **Orden de autores**: en el artículo y en ACL Anthology el primer autor es Patrice Béchard y el segundo Orlando Marquez Ayala; por eso el citekey es bechard_2024 (no «Ayala & Béchard»). Limitación: la tarea es generar JSON de flujos de trabajo, no redactar textos; el modelo fue ajustado (fine-tuning) además de usar RAG.
