---
citekey: anthropic_sfb
referencia_apa: "Anthropic. (s.f.). *API and data retention*. platform.claude.com. Recuperado el 25 de octubre de 2026, de https://platform.claude.com/docs/en/manage-claude/api-and-data-retention"
doi_url: "https://platform.claude.com/docs/en/manage-claude/api-and-data-retention"
anio: s.f.
tipo: pagina_web
categoria: Costos_Viabilidad
objetivos: [5.3]
afirmaciones: []
afirmacion: "En la API de Claude, los datos que se retienen nunca se usan para entrenar sin permiso expreso. Por defecto no se guarda el contenido de las conversaciones, salvo en algunos modelos que exigen 30 días. Hay retención cero (ZDR) para clientes que la acuerden."
cita_textual: "Retained data is never used for model training without your express permission."
pagina: "Página web (sin paginación): sección «How Anthropic approaches data retention»"
confianza: alto
estado: verificada
vigencia: vigente
verificada_por: "IA de Diego (lectura de la página oficial); falta visto bueno de Diego"
fecha_verificacion: 2026-10-25
acceso: "abierto"
texto_local: ""
origen_busqueda: "Página oficial del proveedor · bloque G (S1-T23, S2-T11) · 2026-10-25 (búsqueda manual)"
seminal: false
tags: [fuente, verificada, vigente, pagina_web, inventario]
---

# API and data retention

## Qué respalda
Retención de datos en la API de Claude, al 25-oct-2026:

- Lo que se retiene **nunca se usa para entrenar** sin permiso expreso.
- Por defecto **no se guarda el contenido** de las conversaciones. La excepción son algunos modelos («Covered Models»), que exigen 30 días.
- Existe la **retención cero** (ZDR, *zero data retention*) para los clientes que la acuerden. No todas las funciones la admiten: por ejemplo, la ejecución de código guarda datos hasta 30 días.

## Cita textual
> «Retained data is never used for model training without your express permission.» (Página web, «How Anthropic approaches data retention»)

> «Conversation content (your prompts and Claude's outputs) is not retained by default; the exception is Covered Models, which require 30-day retention.» (misma sección)

## Cómo se usa en la tesis
Inventario de herramientas (S2-T11), componente **LLM**, criterio de la **LOPDP**. Junto con `anthropic_2026`.

## Notas de verificación
- Consultada el 25-oct-2026 con WebFetch; la página se guardó completa y las frases se buscaron en el texto.
- La página no tiene fecha, por eso va con «s.f.».
