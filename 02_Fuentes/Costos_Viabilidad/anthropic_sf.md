---
citekey: anthropic_sf
referencia_apa: "Anthropic. (s.f.). *Pricing*. Claude Platform Docs. Recuperado el 25 de octubre de 2026, de https://platform.claude.com/docs/en/about-claude/pricing"
doi_url: "https://platform.claude.com/docs/en/about-claude/pricing"
anio: s.f.
tipo: pagina_web
categoria: Costos_Viabilidad
objetivos: [5.3]
afirmaciones: [A36]
afirmacion: "La API de Claude cobra por millón de tokens (MTok), en USD: Opus 5.5, USD 4 de entrada y USD 20 de salida; Sonnet 5.5, USD 2 y USD 10; Haiku 5.5, USD 0,10 y USD 0,50 (para prompts de hasta 100 000 tokens). El procesamiento por lotes descuenta el 50 %."
cita_textual: "The Batch API allows asynchronous processing of large volumes of requests with a 50 percent discount on both input and output tokens."
pagina: "Página web (sin paginación): tabla «Model pricing» y sección «Batch processing»"
confianza: alto
estado: verificada
vigencia: vigente
verificada_por: "IA de Diego (lectura de la página oficial); falta visto bueno de Diego"
fecha_verificacion: 2026-10-25
acceso: "abierto"
texto_local: ""
origen_busqueda: "Página oficial del proveedor · A36 · 2026-10-25 (búsqueda manual)"
seminal: false
tags: [fuente, verificada, vigente, pagina_web]
---

# Pricing

## Qué respalda
Precios oficiales de la API de Claude (Anthropic) al 25-oct-2026, por millón de tokens y en USD. Se toma la generación más reciente de cada gama:

| Modelo | Entrada | Salida | Lotes (entrada / salida) |
|---|---|---|---|
| Claude Opus 5.5 | 4,00 | 20,00 | 2,00 / 10,00 |
| Claude Sonnet 5.5 | 2,00 | 10,00 | 1,00 / 5,00 (50 %) |
| Claude Haiku 5.5 (prompts ≤ 100 000 tokens) | 0,10 | 0,50 | 0,05 / 0,25 (50 %) |
| Claude Haiku 5.5 (prompts > 100 000 tokens) | 0,50 | 2,50 | — |

Las lecturas repetidas del mismo contexto (caché) cuestan mucho menos: USD 0,10 por MTok en Sonnet 5.5 y USD 0,01 en Haiku 5.5.

## Cita textual
> «The Batch API allows asynchronous processing of large volumes of requests with a 50 percent discount on both input and output tokens.» (Página web, «Batch processing»)

Filas de la tabla «Model pricing» (copiadas literal): «Claude Opus 5.5 | $4 / MTok | … | $20 / MTok», «Claude Sonnet 5.5 | $2 / MTok | … | $10 / MTok», «Claude Haiku 5.5 (for prompts up to 100,000 tokens) | $0.10 / MTok | … | $0.50 / MTok».

## Cómo se usa en la tesis
Cap. 5, costos (A36): costo variable (OPEX) del asistente. Va en la tabla comparativa `2026-10-25_Tabla_Precios_LLM.md`. Los lotes **no** sirven para el asistente del vendedor, que necesita la respuesta al momento: el descuento solo vale para tareas nocturnas, como volver a indexar la bóveda.

## Notas de verificación
- Consultada el 25-oct-2026. La página no tiene fecha de actualización, por eso va con «s.f.».
- Los precios cambian: volver a consultar antes de cerrar el Cap. 5.
- Los precios de los Batch para Sonnet y Haiku 5.5 se calcularon con el 50 % que dice la página. Solo la fila de Opus 5.5 se leyó literal en la tabla de lotes.
