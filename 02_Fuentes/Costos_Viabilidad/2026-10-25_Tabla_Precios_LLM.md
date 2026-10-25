---
titulo: Tabla de precios de modelos de lenguaje (A36)
version: v0.1
fecha: 2026-10-25
autor: Diego Bermeo
ia: Claude (Claude Code)
afirmaciones: [A36]
fuentes: [anthropic_sf, openai_sf, google_2026]
tags: [diego, precios, llm, a36, sprint2]
---

# Precios de los modelos de lenguaje para el asistente (A36)

> [!info] Para qué sirve
> A36 pide los precios oficiales del proveedor de IA para el costo variable (OPEX) del asistente. Todavía **no se elige proveedor**: eso se decide en el inventario de herramientas (bloque G). Aquí se comparan tres proveedores con la misma regla de cálculo.

**Fecha de consulta:** 25-oct-2026, en las páginas oficiales. Todo en **USD por millón de tokens** (MTok), sin impuestos. Un *token* es un pedazo de palabra: en español, unas 100 palabras son 130–150 tokens.

## 1. Precios oficiales (nivel estándar, por MTok)

Se toman tres gamas por proveedor: la más capaz, la intermedia y la más barata.

| Proveedor | Modelo | Gama | Entrada | Salida | Fuente |
|---|---|---|---|---|---|
| Anthropic | Claude Opus 5.5 | Alta | 4,00 | 20,00 | `anthropic_sf` |
| Anthropic | Claude Sonnet 5.5 | Media | 2,00 | 10,00 | `anthropic_sf` |
| Anthropic | Claude Haiku 5.5 (≤ 100 000 tokens) | Económica | 0,10 | 0,50 | `anthropic_sf` |
| OpenAI | gpt-6-astra | Alta | 10,00 | 50,00 | `openai_sf` |
| OpenAI | gpt-6.1-sol | Media | 2,00 | 10,00 | `openai_sf` |
| OpenAI | gpt-6-luna | Económica | 0,10 | 0,50 | `openai_sf` |
| Google | Gemini 3.1 Pro Preview (≤ 200 000 tokens) | Alta | 2,00 | 12,00 | `google_2026` |
| Google | Gemini 3.8 Flash, hasta el 31-dic-2026 | Media | 0,75 | 3,75 | `google_2026` |
| Google | Gemini 3.8 Flash, desde el 1-ene-2027 | Media | 1,50 | 7,50 | `google_2026` |
| Google | Gemini 3.5 Flash-Lite | Económica | 0,30 | 2,50 | `google_2026` |

## 2. Costo ilustrativo del asistente

> [!warning] Supuestos, no datos de Torvesa
> El volumen real sale del campo (P2-B: solicitudes de los últimos 3 meses). Mientras tanto se usan estos **supuestos**, que hay que reemplazar:
> - **Cada consulta:** 4 000 tokens de entrada (la pregunta del vendedor más los fragmentos que el RAG trae de la bóveda) y 500 de salida (el borrador de respuesta).
> - **Volumen:** 1 000 consultas al mes.

Fórmula: costo por consulta = (4 000 × precio de entrada + 500 × precio de salida) ÷ 1 000 000.

| Modelo | Por consulta | Al mes (1 000) | Al año |
|---|---|---|---|
| gpt-6-astra | 0,065 | 65,00 | 780,00 |
| Claude Opus 5.5 | 0,026 | 26,00 | 312,00 |
| Gemini 3.1 Pro Preview | 0,014 | 14,00 | 168,00 |
| Claude Sonnet 5.5 | 0,013 | 13,00 | 156,00 |
| gpt-6.1-sol | 0,013 | 13,00 | 156,00 |
| Gemini 3.8 Flash (precio 2027) | 0,00975 | 9,75 | 117,00 |
| Gemini 3.5 Flash-Lite | 0,00245 | 2,45 | 29,40 |
| Claude Haiku 5.5 | 0,00065 | 0,65 | 7,80 |
| gpt-6-luna | 0,00065 | 0,65 | 7,80 |

**Lectura:** incluso con el modelo más caro, el costo de la IA es bajo frente al resto del sistema. La gama media, que es la candidata razonable para redactar respuestas a clientes, cuesta **entre USD 10 y 14 al mes** con estos supuestos. Esto respalda la frase del Cap. I: «un costo por consumo acotado».

## 3. Lo que hay que tener en cuenta

1. **Fechas:** la validación en operación experimental cae en 2027. Gemini 3.8 Flash dobla su precio el 1-ene-2027, así que para el VAN se usa el precio de 2027.
2. **LOPDP:** en el nivel gratuito de Gemini, Google usa los datos para mejorar sus productos. Con datos de clientes de Torvesa solo sirve un nivel pagado. Falta revisar las condiciones de datos de Anthropic y OpenAI (bloque G).
3. **Modelos «Preview»:** Gemini 3.1 Pro Preview puede cambiar o retirarse. Para el diseño conviene un modelo estable.
4. **Procesamiento por lotes (−50 %):** no sirve para el asistente, que tiene que responder al momento. Sí sirve para tareas nocturnas, como volver a indexar la bóveda.
5. **Impuestos:** los precios no incluyen impuestos. Si aplica IVA a servicios digitales del exterior en Ecuador, lo confirma Víctor en la parte financiera (**sin fuente aún**).
6. **Vigencia:** los precios cambian. Hay que volver a consultarlos antes de cerrar el Cap. 5.

## 4. Propuesta para la matriz (la actualiza Víctor)

- **A36 → 🟡 Parcial:** hay precios oficiales verificados de tres proveedores (`anthropic_sf`, `openai_sf` y `google_2026`). Pasa a ✅ cuando se elija el proveedor en el bloque G.
- **Texto para el Cap. I, viabilidad (e):** reemplazar `[FALTA-FUENTE: A36]` por las tres páginas oficiales con la fecha de consulta: (Anthropic, s.f.; Google, 2026; OpenAI, s.f.).
