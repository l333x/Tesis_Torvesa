---
titulo: Respuesta de Víctor a las dudas de Diego (reporte del 19-oct)
fecha: 2026-10-19
autor: Víctor Segura (redacción con IA)
ia: Claude (Claude Code)
para: Diego
responde_a: 00_Inbox/2026-10-19_reporte_Diego.md
tags: [diego, respuesta, sprint2]
---

# Respuesta a tus dudas del 19-oct

Bien hecho el arranque. Aquí van las respuestas para que sigas sin frenarte.

## 1. Calendario de esta semana: sigue `IA_DIEGO.md`
- Esta semana mandan los **bloques C–H de `IA_DIEGO.md`**:
  - mar 20: bóvedas y RAG;
  - mié 21: documentación oficial y precios, más el resumen;
  - jue 22: procesos y AS-IS;
  - vie 23 y sáb 24: herramientas y cierre.
- Las tareas de **análisis de datos de campo** (S2-T02, S2-T04 y S2-T17) quedan **en pausa hasta que Torvesa autorice el campo**. Sin campo no hay línea base, y no se inventa.
- **Lo primero, mañana a primera hora:** el **correo a Torvesa** (punto 6). Es lo que más nos frena.

## 2. Dónde va el inventario de herramientas
Manda el cronograma:
- **Inventario:** `07_Flujos_Diseno/2026-10-24_Inventario_Herramientas_v0.1.xlsx`. Pide al menos 3 opciones por componente: bóveda, CRM, LLM y mensajería.
- **Fichas de precios** (una por proveedor, con URL oficial y fecha de consulta): `02_Fuentes/Costos_Viabilidad/`.

`IA_DIEGO.md` ya quedó corregido así.

## 3. Fichas en `02_Fuentes`: sí puedes escribir
Puedes **crear fichas nuevas** en:
- `02_Fuentes/Tecnologia_IA/`
- `02_Fuentes/Metodologia/`
- `02_Fuentes/Costos_Viabilidad/`
- `02_Fuentes/Casos_Estudio/`, para tu resumen del sábado.

Las fichas que ya existen **no las edites**: si ves algo, déjame un comentario `> [!question] Diego:`. Antes de crear una ficha, busca si ya existe una con ese citekey. Nos pasó hoy con `chatterjee_2023`. Ya actualicé `COLABORACION.md` con esta excepción.

## 4. A36, precios del LLM: tu propuesta va
- Toma **Claude (Anthropic)** como referencia y compáralo con **OpenAI**, **Gemini** y **un modelo local**: por ejemplo, uno que corra con Ollama.
- Usa **solo precios de la página oficial**, en USD y con la fecha de consulta: precio por millón de tokens de entrada y de salida, y si hay plan gratuito o límites.
- No es la elección final del proveedor: esa se hace en el diseño (sprint 3), con criterios.
- Para el modelo local, el costo no es por token sino de equipo: anota qué computadora pide (RAM o GPU).

## 5. AS-IS: sí, haz el borrador con lo que ya sabemos
- Bases para el borrador:
  - el diseño aprobado;
  - el resumen del problema;
  - el Cap. I, parte 1: `06_Capitulos/2026-10-19_Cap1_Introduccion_p1_v0.1.md`.
- Marca **cada paso** como «por validar».
- Entregable: `07_Flujos_Diseno/2026-10-22_AS-IS_v0.1`.
- Cuando haya entrevistas, se valida y pasa a v0.2. El criterio «validado con las entrevistas» se cumple después, no esta semana.

## 6. Nuevo y urgente: el correo a Torvesa (ingresos 2025 y datos que faltan)
El Excel de ingresos 2025 que nos pasaste ya está analizado:
- `05_Datos_Campo/Ingresos_2025/2026-10-19_Analisis_Ingresos_2025_PROVISIONAL.pdf`
- La copia original está en `_crudo/`.

El problema: **el propio archivo dice «clientes ficticios», «contratos ficticios» y «resultado del modelo de avance de obra»**. Mira las celdas A2 y B4 de la primera hoja. Así no lo podemos usar en la tesis hasta que la empresa confirme por escrito que **los montos son reales** y que solo cambiaron los nombres. Si lo usamos sin esa confirmación, el tribunal lo puede tumbar.

Las preguntas del correo están en **`00_Inbox/2026-10-19_Correo_Torvesa_preguntas.txt`**: ábrelo, revísalo y mándalo **mañana 20-oct**. Cuando respondan, avísame el mismo día. Si no responden hasta el **viernes 24-oct**, escalamos (llamada al Ing. Torres o carta de la tutora).

## 7. Corrección hecha
Tu usuario de GitHub es **`psiceslivie`**: ya está corregido en `IA_DIEGO.md`, `COLABORACION.md` y `CLAUDE.md`. Tu entorno en `D:` está bien; no hace falta moverlo.
