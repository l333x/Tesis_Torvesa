---
citekey: aws_sfb
referencia_apa: "Amazon Web Services. (s. f.-b). *Amazon Bedrock pricing*. Recuperado el 10 de noviembre de 2026, de https://aws.amazon.com/bedrock/pricing/"
doi_url: "https://aws.amazon.com/bedrock/pricing/"
anio: s.f.
tipo: pagina_web
categoria: Costos_Viabilidad
objetivos: [5.3]
afirmaciones: []
afirmacion: "En Amazon Bedrock, servir un modelo ajustado (Llama 2) exige capacidad dedicada: USD 23,50 por hora por unidad de modelo sin compromiso, USD 21,18 con compromiso de 1 mes y USD 13,08 con 6 meses; guardar el modelo cuesta USD 1,95 al mes."
cita_textual: "Llama 2 Pre-trained models are available only in provisioned throughput after customization."
pagina: "Página web (sin paginación): tablas «Pricing for model customization (fine-tuning)» y «Provisioned Throughput pricing»"
cita_en_texto: "(AWS, s. f.-b)"
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

# Amazon Bedrock pricing

## Qué respalda
Precios oficiales del ajuste fino en Bedrock al 10-nov-2026 (USD), modelos Llama 2:

| Concepto | 13B | 70B |
|---|---|---|
| Entrenar 1 millón de tokens | 1,49 | 7,99 |
| Guardar el modelo, al mes | 1,95 | 1,95 |
| Inferencia, 1 unidad de modelo por hora, sin compromiso | 23,50 | 23,50 |
| Ídem, compromiso de 1 mes | 21,18 | 21,18 |
| Ídem, compromiso de 6 meses | 13,08 | 13,08 |

A USD 23,50 la hora, una unidad encendida todo el mes (730 horas) cuesta **USD 17.155** (cálculo propio).

## Cita textual
> «Llama 2 Pre-trained models are available only in provisioned throughput after customization.» (Página web)

Filas de la tabla (literal): «Llama 2 Pretrained (13B) | $1.49 | $1.95 | $23.50».

## Cómo se usa en la tesis
Matriz de herramientas, alternativa C2 (AWS con modelo propio ajustado): hoja `TCO` y hoja `Ruta_AWS`. Argumento de que entrenar un modelo propio no se justifica frente a RAG.

## Notas de verificación
- Consultada el 10-nov-2026 con WebFetch, que extrae el texto de la página. Antes de citar una frase literal en la tesis, abrir la página y confirmarla.
- **No se pudieron leer** los precios por token de Claude ni de Amazon Nova en esta página (las tablas no cargaron): no se citan.
- La página tiene 119.109 caracteres y solo se leyeron los primeros 100.000.
- Llama 2 es el ejemplo publicado con todas las cifras; otros modelos tienen otras tarifas.

## Ampliación del 10-nov (v0.2)
- **Knowledge Bases gestionado:** almacenamiento del índice, USD 5,00 por GB de datos al mes; búsqueda estándar, USD 1,00 por 1.000 llamadas; búsqueda con agente, USD 4,00 por 1.000. El análisis de documentos, los vectores y el reordenamiento gestionado no se cobran aparte.
- **Importar un modelo propio:** USD 0,05718 por minuto por unidad (ventanas de 5 minutos) y USD 1,95 al mes de almacenamiento.
- Leído con extracción automática en una segunda consulta del mismo día: **abrir la página antes de citar**. Los precios por token de Nova y de Claude siguen sin cargar.
