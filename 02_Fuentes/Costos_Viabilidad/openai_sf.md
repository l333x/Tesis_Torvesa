---
citekey: openai_sf
referencia_apa: "OpenAI. (s.f.). *Pricing*. OpenAI API Docs. Recuperado el 25 de octubre de 2026, de https://developers.openai.com/api/docs/pricing"
doi_url: "https://developers.openai.com/api/docs/pricing"
anio: s.f.
tipo: pagina_web
categoria: Costos_Viabilidad
objetivos: [5.3]
afirmaciones: [A36]
afirmacion: "La API de OpenAI (nivel Standard, contexto corto) cobra por millón de tokens, en USD: gpt-6-astra, USD 10 de entrada y USD 50 de salida; gpt-6.1-sol, USD 2 y USD 10; gpt-6-luna, USD 0,10 y USD 0,50."
cita_textual: "gpt-6.1-sol | $2.00 | $0.10 | $2.50 | $10.00"
pagina: "Página web (sin paginación): tabla «Text tokens», pestaña «Standard»"
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
Precios oficiales de la API de OpenAI al 25-oct-2026, nivel «Standard» y contexto corto (hasta 272 000 tokens de entrada), por millón de tokens y en USD:

| Modelo | Entrada | Entrada en caché | Salida |
|---|---|---|---|
| gpt-6-astra | 10,00 | 1,00 | 50,00 |
| gpt-6.1-sol | 2,00 | 0,10 | 10,00 |
| gpt-6-luna | 0,10 | 0,01 | 0,50 |

## Cita textual
> «gpt-6.1-sol | $2.00 | $0.10 | $2.50 | $10.00» (Página web, tabla «Text tokens», «Standard»; columnas: entrada, entrada en caché, escritura de caché, salida)

## Cómo se usa en la tesis
Cap. 5, costos (A36): alternativa en la tabla comparativa `2026-10-25_Tabla_Precios_LLM.md`.

## Notas de verificación
- Consultada el 25-oct-2026. La página no tiene fecha de actualización, por eso va con «s.f.».
- `openai.com/api/pricing` devolvió 403 y `platform.openai.com/docs/pricing` redirige a la URL de esta ficha.
- La página arma la tabla con JavaScript. Las cifras se leyeron en los datos de la tabla y el orden de las columnas se confirmó con el script de la página.
- Con contexto largo (más de 272 000 tokens) los precios suben: gpt-6.1-sol pasa a USD 4 de entrada y USD 15 de salida. El asistente no llega a ese tamaño.
