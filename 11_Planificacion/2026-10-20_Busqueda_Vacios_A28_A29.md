---
titulo: Búsqueda documentada de los vacíos A28 y A29
fecha: 2026-10-20
tipo: registro_busqueda
afirmaciones: [A28, A29]
tags: [fuentes, vacios, busqueda]
---

# Búsqueda documentada de los vacíos A28 y A29 (20-oct-2026)

Sirve para respaldar en el Cap. II que «no se encontraron estudios». Así, la afirmación descansa en una búsqueda que se puede repetir, no en una impresión.

## Registro
| # | Base | Consulta | Filtro | Resultados | Pertinentes |
|---|---|---|---|---|---|
| 1 | SciELO | (inteligencia artificial OR CRM) AND (construcción OR constructora) AND (pyme* OR pequeñas empresas) | 2021–2026 | 1 | 1: Peña-Ramírez et al. (2024), inteligencia de negocios en pymes constructoras de Chile, aplicada a compras públicas |
| 2 | SciELO | ("artificial intelligence" OR CRM OR "customer relationship") AND construction AND (SME* OR "small and medium") | 2021–2026 | 0 | — |
| 3 | SciELO | ("inteligencia artificial" OR RAG OR "modelos de lenguaje") AND (cotización* OR presupuesto* OR "gestión del conocimiento") AND (pyme* OR empresa*) | 2023–2026 | 0 | — |
| 4 | SciELO | inteligencia artificial cotizaciones | sin filtro | pocos; ninguno sobre cotizar (p. ej., predicción bursátil) | 0 |
| 5 | SciELO | retrieval augmented generation | sin filtro | 0 | — |
| 6 | Repositorio UPS | inteligencia artificial (control) | — | 669 | (control: el buscador funciona) |
| 7 | Repositorio UPS | inteligencia artificial constructora | — | 0 | — |
| 8 | Repositorio UPS | CRM constructora | — | 0 | — |
| 9 | Repositorio UPS | inteligencia artificial cotizaciones | — | 0 | — |
| 10 | Redalyc | "inteligencia artificial" +"pymes" +"construcción" | — | 248 324 (Redalyc une los términos con «o»); se revisaron los 10 primeros por relevancia | 0 (lo más cercano: IA en proyectos de inversión pública del Ministerio de Vivienda del Perú, 2022, sector público) |
| 11 | Redalyc | "inteligencia artificial" cotizaciones pymes conocimiento | — | 410 414; 10 primeros revisados | 0 |
| 12 | Redalyc | CRM constructora pymes | — | 24 738; 10 primeros revisados | 0 (CRM en pymes de Milagro, 2011, fuera del núcleo 2021+) |
| 13 | OpenAlex | construction SME CRM artificial intelligence Latin America | 2021+ | 297; 8 primeros revisados | 0 específicos (revisiones generales de CRM y martech en pymes) |
| 14 | OpenAlex | retrieval-augmented generation quotation SME | 2021+ | 120; 8 primeros | 1 candidata: revisión de búsqueda de conocimiento con IA en proyectos de infraestructura (Infrastructures, 2025) |
| 15 | OpenAlex | retrieval augmented generation sales proposal small business | 2021+ | 1214; 8 primeros | 1: Bakiyalakshmi et al. (2026), RAG para propuestas comerciales en empresas (India) |

Bases: search.scielo.org, dspace.ups.edu.ec (buscador simple), redalyc.org y api.openalex.org. Las consultas se hicieron el 20-oct-2026 desde Chrome y la API. Google Académico no se automatiza (regla de la bóveda).

## Qué se concluye
- **A28:** no se encontraron estudios sobre CRM ni IA para la atención comercial en pymes constructoras latinoamericanas. Lo más cercano es Peña-Ramírez et al. (2024, p. 1), que trata la inteligencia de negocios para compras públicas. La parte «sin conectividad» de la frase original no apareció en ninguna búsqueda. Se propone quitarla.
- **A29:** el uso de RAG para redactar propuestas **sí se ha estudiado**, pero como prototipo en empresas en general (Bakiyalakshmi et al., 2026, p. 1) y en etapa de prueba en la industria (Brehme et al., 2025, p. 10). No se encontraron estudios en pymes, en América Latina ni con medición del tiempo de respuesta. La frase «no se ha estudiado» hay que reformularla.

## Frases propuestas para la v0.2 del Cap. II (Víctor decide)
- **A28:** «En la búsqueda realizada en SciELO, Redalyc, el repositorio de la UPS y OpenAlex (2021–2026) no se encontraron estudios sobre CRM o IA para la atención comercial en pymes constructoras latinoamericanas; el trabajo más cercano aplica inteligencia de negocios a las compras públicas de pymes constructoras chilenas (Peña-Ramírez et al., 2024).»
- **A29:** «La IA con recuperación de documentos propios ya se ha probado para redactar propuestas comerciales en empresas (Bakiyalakshmi et al., 2026) y en la industria sigue en etapa de prototipo (Brehme et al., 2025); no se encontraron estudios que la apliquen a cotizaciones en pymes latinoamericanas ni que midan su efecto en el tiempo de respuesta.»

## Pendiente
- La candidata de la consulta 14 (Infrastructures, 2025, MDPI) no se pudo bajar porque MDPI bloquea la descarga automática. Víctor puede bajarla a mano si se quiere sumar al Cap. II.
