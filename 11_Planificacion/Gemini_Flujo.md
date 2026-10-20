---
titulo: Flujo con Gemini Pro (búsqueda, imágenes y estudio)
actualizado: 2026-10-20
tipo: guia
tags: [gemini, notebooklm, fuentes, figuras, flujo]
---

# Flujo con Gemini Pro

> Lo pidió Víctor el 20-oct. Gemini Pro y NotebookLM ayudan a **buscar, explicar e ilustrar**. Ninguno de los dos **verifica fuentes ni datos**: eso lo hace Claude abriendo el PDF, según las reglas de la bóveda. Ver también [[NotebookLM_Flujo]].

## El flujo, de punta a punta

| Paso | Herramienta | Qué hace | Qué sale | ¿Entra a la tesis? |
|---|---|---|---|---|
| 1. Buscar | **Gemini Deep Research** (modelo 3.1 Pro) | Rastrea la web y la literatura según la lista de vacíos de la matriz | Informe con candidatas (DOI, URL, dato, página) | **No.** Es una lista de candidatas |
| 2. Verificar | **Claude** | Abre cada candidata (PDF o página oficial) y confirma el dato y la página | Ficha en `02_Fuentes/` con `estado: verificada` | **Sí**, solo lo verificado |
| 3. Bajar | **Víctor** | Baja a mano los PDF que las editoriales bloquean | PDF en `00_Inbox/descargas/` | — |
| 4. Estudiar | **NotebookLM** | Cuaderno con las fuentes verificadas: chat con cita de página, audio, video, mapa mental | Material de estudio para los dos | **No** se cita |
| 5. Ilustrar | **Gemini · Crear imagen** | Figuras con estética suave a partir de lo que ya dice el capítulo | Imagen PNG | **Solo** como figura con nota «Elaboración propia con apoyo de IA (Gemini)», después de que Víctor la revise |
| 6. Registrar | **Claude** | Anota cada uso en el registro de contribuciones | Fila en `09_Registro_Contribuciones` | Va a la declaración de uso de IA (DEC-11) |

## Qué es viable y qué no (prueba del 20-oct)

| Uso | Resultado | Veredicto |
|---|---|---|
| Imagen del flujo con el sistema (7 pasos) | Texto en español exacto, sin errores; estética crema y pastel | ✅ **Viable** para presentaciones, la defensa, el resumen para Torvesa y como figura ilustrativa |
| Imagen de la arquitectura (4 componentes) | Texto exacto y relaciones correctas | ✅ **Viable**. Para la figura formal del Cap. 5 conviene además un diagrama editable (`diagramas.py`) |
| Diagrama BPMN formal (AS-IS / TO-BE) | No se probó como imagen: una imagen no se puede editar ni validar con la notación | ⚠️ **No recomendado** como imagen. El BPMN lo hace Diego en una herramienta de BPMN; Gemini puede ilustrar la versión simple |
| Deep Research para fuentes | En curso al cierre (ver la conversación «Fuentes para Tesis de Negocios Digitales» en Gemini) | ⚠️ **Útil para encontrar**, no para citar. Cada candidata pasa por el paso 2 |
| Cifras de Torvesa o del campo en Gemini | — | ❌ **No.** Los datos de campo y de la empresa no se suben a Gemini ni a NotebookLM (LOPDP) |
| Citar un texto de Gemini como fuente | — | ❌ **Nunca** |

## Prompts que funcionaron

**Imagen (estilo de la casa):**
> Infografía horizontal 16:9, estética suave y profesional: fondo crema muy claro, colores pastel (azul grisáceo, salvia, terracota suave), íconos planos minimalistas, esquinas redondeadas, mucho espacio en blanco, tipografía sans-serif limpia. Título: «…». [Pasos o bloques con su texto exacto entre comillas]. Sin personas, sin logotipos, sin texto adicional.

Reglas para que el texto salga bien: etiquetas cortas, el texto exacto entre comillas «», en español, y pedir «sin texto adicional».

**Deep Research (fuentes):** contexto de la tesis + la lista de afirmaciones sin fuente de la matriz + qué entregar por cada fuente (APA 7, DOI, acceso, dato, página) + reglas estrictas («no inventes»; «marca solo resumen»; «di si la cifra no aparece en la original») + una tabla final con nivel de confianza. Lo que devuelva se pega en `00_Inbox/` como `AAAA-MM-DD_DeepResearch_<tema>.md` para que Claude lo verifique.

## Figuras generadas el 20-oct
1. «Atención comercial con el sistema propuesto»: 7 pasos, del formulario al registro verificable.
2. «Componentes del sistema»: TEAMSLASH, la bóveda, el asistente de IA, el registro verificable y la LOPDP.

Descargadas el 20-oct (con permiso de Víctor) a `06_Capitulos/Figuras/`:
- `2026-10-20_Fig_Flujo_Sistema_Propuesto_v0.1.jpeg` (2752×1536): texto correcto.
- `2026-10-20_Fig_Componentes_Sistema_v0.1.jpeg` (2752×1536): **falta la flecha del asistente al vendedor**, porque la flecha va directo al registro. Se corrige en la v0.2 pidiéndoselo a Gemini en la misma conversación.

## Estado de Deep Research al cierre del 20-oct
A los 15 minutos todavía no había mostrado ni el plan ni el informe. Si mañana sigue vacío, se relanza con un prompt más corto: un tema por consulta (p. ej., solo el 1, tiempo de respuesta).
