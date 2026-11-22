# Revisión de los Excel de costos y tablero de costos v0.1 (22-nov-2026)

Para la IA. Revisión de los tres Excel vigentes del 15-nov y entrega del tablero nuevo. **No se modificó ningún original** (`git status` solo muestra el tablero nuevo). Revisión hecha con fórmulas y valores, recalculando copias con Excel por COM.

Archivos revisados:
- `2026-11-15_Modelo_Financiero_v0.2.xlsx` (MF)
- `2026-11-15_Estudio_Costos_v0.3.xlsx` (EC)
- `2026-11-15_Matriz_Herramientas_v0.2.xlsx` (MH)

Resultado general: **ninguna celda con error** (#REF!, #DIV/0!, #NAME?, #VALUE!) en los tres libros, ni vínculos a otros archivos. Al recalcular con Excel, los valores guardados no cambian. Las cifras ya presentadas a la tutora coinciden con el MF: Premium USD 275 + 311,14; hora 9,26; VAN 427; TIR 25,7 %; B/C 1,03; VAN Torvesa 13.618; 1,91 obras/año; 6 % de datos de Torvesa. Los problemas son de **coherencia**, **supuestos escondidos en fórmulas** y **etiquetas**, no de cálculo roto.

## 1. Modelo_Financiero_v0.2 (MF)

| # | Hoja!celda | Qué pasa | Cómo corregirlo (en una v0.3, no en el original) | Gravedad |
|---|---|---|---|---|
| MF-1 | `Panel!C26:C28` | El denominador `COUNTA(Supuestos!A7:A77)` cuenta las 8 filas de título (A7, A26, A29, A38, A49, A56, A67, A74). Da 71 en vez de 63 entradas: DATO 39 %, SUPUESTO 42 %, DECISIÓN 7 % (suman 89 %). | Contar solo filas con tipo: `COUNTA(Supuestos!I7:I77)`. Valores correctos: DATO 28/63 = **44,4 %**, SUPUESTO 30/63 = **47,6 %**, DECISIÓN 5/63 = **7,9 %**. | Media (cifra visible) |
| MF-2 | `Panel!C30` y `Supuestos!I23`/`L23` | El 6 % de "datos de Torvesa" es 1 de 18, y ese único DATO es `margen_obra` (Damodaran, promedio del sector), no un dato de Torvesa. En cambio `usuarios` (fila 8) dice SUPUESTO aunque su fuente es el censo real de 5 personas. | Marcar `margen_obra` como "DATO-SECTOR" (no de Torvesa) y `usuarios` como DATO-TORVESA (censo). Así el 6 % sigue saliendo, pero por la razón correcta. Decirlo así a la tutora. | Media |
| MF-3 | `1_Inversion!E9` y `2_Costos!E19:F19` | La firma electrónica se cuenta dos veces: como inversión del año 0 (2 × 31,05 = 62,10) y otra vez repartida en el costo mensual (2 × 31,05 ÷ 24 = 2,59/mes). | Dejarla en un solo lugar: o se quita I2 de la inversión, o se quita la firma de C10 (dejar solo el dominio). Efecto pequeño (unos USD 60-90 en 3 años). | Baja |
| MF-4 | `8_Torvesa!E9`, `E10`, `E13:F13` | Supuestos escritos dentro de la fórmula y no en la hoja Supuestos: 1 minuto para asignar con «Tomar» (`-1`), 4 minutos de seguimiento con recordatorio (`-4`), 80 % de solicitudes por WhatsApp (`0.8`) y 15 minutos semanales de reporte (`15*52/12/60`). La Portada dice que "ninguna hoja tiene números escritos a mano". | Pasarlos a Supuestos como SUPUESTO (el EC ya los tiene: T02D, T04D, T06S, T07). | Media |
| MF-5 | `5_Estado_Resultados!E15:H15` y `E13:H13` | `0.15` (participación) y `/3` (años de amortización) escritos en la fórmula. | Usar un nombre `tasa_participacion` y `meses_recuperacion/12`. | Baja |
| MF-6 | `8_Torvesa!F18` | `=E16*valor_obra*margen_obra`: la columna Premium usa la celda de Estándar (E16). Hoy da igual porque E16 = F16. | `=F16*valor_obra*margen_obra`. | Baja |
| MF-7 | `9_Escenarios!B7:G17` | Son valores fijos (foto del 15-nov). Lo dice la hoja, pero si cambia un supuesto la foto queda vieja. **Se comprobó hoy por COM: coincide con el modelo en los 6 casos.** | Regenerar la foto en cada versión o cambiarla por una tabla de datos (`Datos > Análisis de hipótesis`). | Baja |
| MF-8 | `Supuestos!H33` (horas_mes = 160) frente a `8_Torvesa!E11` (52 ÷ 12 semanas) | Incoherencia interna: el mes tiene 4 semanas para el costo hora (160 h) y 4,33 semanas para las horas ahorradas. Con 173,3 h la hora bajaría de 9,26 a unos 8,55. La fuente dice [VERIFICAR-PÁG]. | Decidir una sola convención y citar la página del Código del Trabajo. Verificar además qué divisor usa la práctica ecuatoriana para el valor hora [VERIFICAR]. | Media |
| MF-9 | `Supuestos!E37` (TMAR pesimista 17,18 %) | Etiquetado DATO, pero es solo la prima de riesgo de Ecuador, sin la tasa libre de riesgo (la columna K lo admite). No es una TMAR completa. La optimista (9,87 %) es una tasa activa máxima de crédito, no un costo de oportunidad. | Etiquetar como SUPUESTO con base en dato, o armar la TMAR completa (libre de riesgo + prima). | Media |
| MF-10 | `3_Precio!F17` y `Panel!C10` | El precio Premium base se lleva el **30,8 %** del beneficio de Torvesa y pasa la regla del 25 % del propio modelo. Es la cifra presentada a la tutora: el libro la marca en rojo, pero el discurso no lo dice. | No maquillar: decirlo en la tesis (el Estándar base, 23,2 %, sí cumple). | Media (de discurso) |
| MF-11 | `5_Estado_Resultados!I13` y `Supuestos!J42` frente a `Fuentes!A14` | Dicen [FALTA-FUENTE] para el art. 28 del Reglamento LRTI, pero la hoja Fuentes ya lista `sri_2015` para "Depreciación y amortización (33 %)". | Si la ficha está verificada con página, quitar el marcador; si no, quitar la fila de Fuentes. | Baja |
| MF-12 | `Fuentes!B7` (ministerio_2026) | El título ("Informe de gestión... 2025") no coincide con la URL ("Anexo-Fijacion-Salario-Basico..."). | Revisar la ficha contra el PDF [VERIFICAR]. | Baja |
| MF-13 | `7_Evaluacion!E8:E12` con plan Estándar | En Estándar el VAN es negativo en los 3 escenarios porque carga la inversión del levantamiento y no la cobra. Es coherente con DEC-24, pero conviene que el texto lo diga: "el Estándar solo no paga el levantamiento". | Solo de redacción. | Informativo |

## 2. Estudio_Costos_v0.3 (EC)

El problema principal: **el EC y el MF son ambos "vigentes" del 15-nov y usan supuestos distintos para lo mismo.** Quien lea los dos verá dos precios y dos VAN para Torvesa.

| # | EC (hoja!celda) | EC dice | MF v0.2 dice | Cómo corregirlo |
|---|---|---|---|---|
| EC-1 | `Supuestos!D15:F15` (P10) | IESS patronal 11,15 % [VERIFICAR-PÁG] | 12,15 % (con SECAP e IECE, DATO) | Usar 12,15 % y la fuente del MF. |
| EC-2 | `Supuestos!D51` (S_DEV) → `A1_Costo_hora!D12` | Sueldo 1.000 (SUPUESTO) → hora **8,50** | Sueldo 1.084 (Ekos 2025) → hora **9,26** | Alinear con el MF; actualizar los textos que dicen "USD 8,50" (`Resumen!G39`, `A4_Equilibrio!G29`). |
| EC-3 | `Supuestos!D24:F24` (P18) | Tasa 15 / 12 / 9,87 % (base 12 % = SUPUESTO) | 17,18 / 15 / 9,87 % | Alinear: la TMAR base presentada es 15 %. |
| EC-4 | `Supuestos!D22:F22` (P16) | Margen de obra 8 / 10 / 12 % (SUPUESTO) | 2,35 / 11,88 / 24,40 % (Damodaran) | Alinear con el MF. |
| EC-5 | `Supuestos!D67` (PR3) y `B2_Implementacion!D23` | Torvesa paga **USD 149** (nivel 3) | Premium **USD 275** + 311 | Explicar que 149 es el precio de lista con 20 empresas y 275 el de un solo cliente, o reemplazar la parte B por el MF. |
| EC-6 | `B3_Torvesa!E28`, `E32`; `Resumen!E13`, `E14` | VAN Torvesa (opción 2) **15.832**; 1,30 obras/año | 13.618; 1,91 obras/año | Consecuencia de EC-1 a EC-5. |
| EC-7 | `Supuestos!D16`, `D17` | Fondos de reserva y 160 h como SUPUESTO [FALTA-FUENTE] | DATO (Código del Trabajo) | Unificar las etiquetas. |
| EC-8 | `Supuestos!D32` (P23) y `B2_Implementacion` | Tarifa técnica independiente USD 15 | 9,26 | Aclarar si es otra persona (independiente externo) o alinear. |
| EC-9 | `A6_Tres_Anios!D65:F65` | "VAN sin inversión: las laptops ya existen". No resta las horas del levantamiento. | El MF sí las trata como inversión (USD 1.852 en base). | Criterio distinto: decirlo o restar el levantamiento. |
| EC-10 | `A2_Costo_operar!D33:F33` | 1 firma (31,05 ÷ 24) | 2 firmas | Alinear (2 fundadores). |
| EC-11 | `Leeme!A16`/`Supuestos!A5` | "Mismos códigos y valores que el modelo v0.1" | Ya no son los mismos | Actualizar el texto. |

Supuestos escondidos en fórmulas del EC (pasarlos a Supuestos):
- `A1_Costo_hora!E21`: 10 % de supervisión de un independiente (`0.1*`).
- `A2_Costo_operar!D33:F33`: dominio `15/12` escrito a mano.
- `A4_Equilibrio!D28:F28`: "la mitad de sus horas" (`*0.5`).
- `A1_Costo_hora!D4:F4`: toma D51, E52 y F53 (columnas distintas de la misma tabla). Funciona porque las tres columnas son iguales, pero es frágil: usar la misma columna.

No hay errores de cálculo: se revisó en particular `B1_Antes_Despues!D44:F44` (resta los trabajos nuevos divididos por el costo hora: unidades correctas).

## 3. Matriz_Herramientas_v0.2 (MH)

| # | Hoja!celda | Qué pasa | Cómo corregirlo |
|---|---|---|---|
| MH-1 | `TCO!C8` | Tarifa de implementación USD 15 "igual que el modelo financiero (P23)". P23 es un código del EC; el MF v0.2 usa 9,26. | Cambiar la referencia del texto o alinear la tarifa. Con 9,26 el TCO del stack propio baja de 9.039 a unos 7.295 (las demás alternativas también bajan; hay que recalcular la puntuación, pero el orden probablemente se mantiene) [VERIFICAR al rehacer]. |
| MH-2 | `TCO!C14` y `MF 2_Costos` | El TCO del stack propio incluye Slack Pro × 5 (USD 36,25/mes), pero el costo mensual del MF no tiene Slack. | Confirmar con Diego si los avisos van por Slack (gratis o Pro) o por WhatsApp y alinear los dos libros. |
| MH-3 | `Precios!E5` | "Supuesto (ver modelo financiero, P27)": P27 es código del EC; en el MF es `consumo_servidor`. | Corregir la referencia. |
| MH-4 | `Portada!C16` | "6 juegos de pesos: la decisión no cambia". En `Sensibilidad!G27` (escalar a otras constructoras) gana D (stack propio con Gemini), no A. | Decir: "gana siempre el stack propio (A, o su variante D si se pesa la escala)". |
| MH-5 | `TCO!D14:D24` | Horas de implementación (160, 60, 80...) escritas a mano sin marcar SUPUESTO en la celda (el encabezado sí lo dice). | Marcar con el fondo amarillo de supuesto. |
| MH-6 | `Por_que_nosotros!D16:G16` | Precios de la competencia escritos a mano (70, 100, 60, 49) en vez de enlazados a `Precios`. Coinciden hoy. | Enlazar. |
| MH-7 | `Puntuacion!D5:K15` | `SUMIFS` devuelve 0 si falta la evidencia de un criterio (no avisa). Hoy no hay ningún 0. | Agregar un control "falta evidencia" con `COUNTIFS`. |

## 4. Tablero nuevo: `2026-11-22_Tablero_Costos_v0.1.xlsx`

Copia también en `C:\Users\vasha\Desktop\TESIS - ENVIO TUTORA 23-nov\`.

- **Tablero**: selectores de plan (Estándar/Premium) y escenario (Pesimista/Base/Optimista) con lista desplegable (C4 y F4). Tiene 12 tarjetas en 3 franjas: lo que paga Torvesa (precio, implementación, costo hora, costo del mes), la viabilidad para TEAMSLASH (VAN, TIR frente a la TMAR, B/C, meses de recuperación) y la de Torvesa (beneficio al mes, VAN, obras que pagan, % del beneficio). Las lecturas en rojo se ponen solas cuando el indicador no conviene. Hay una franja de "Qué es dato real y qué es supuesto" (con el conteo corregido de MF-1) y 4 gráficos: del costo al precio, flujo de caja por año, VAN en los 3 escenarios × 2 planes y costo por herramienta. Las fórmulas son `INDEX/MATCH` contra la hoja Datos. La zona de apoyo de los gráficos está en L:O, fuera del área de impresión.
- **Datos**: 52 indicadores × 6 combinaciones, copiados sin redondear, con archivo, hoja y celda de origen, tipo y nota. Seis filas de "Datos que faltan" quedan vacías a propósito (fondo rosado, tipo FALTA).
- **Cómo usar** y **Glosario**: lenguaje simple, sin «» ni rayas.
- Verificación por COM: 0 errores en todas las celdas; los 6 combos cambian las cifras (tabla abajo); los valores coinciden con `9_Escenarios` del MF. Se renderizó a PDF (Premium·Base y Estándar·Pesimista) y se corrigió el ancho de los gráficos (se cortaban a la derecha), las barras negativas huecas y una regla de color mal anclada.
- Formato: Excel muestra coma decimal y punto de miles porque el equipo de Víctor tiene configuración regional de Ecuador (los formatos son "USD #,##0.00").
- Es una foto del MF v0.2: si se corrige el MF, hay que volver a copiar la hoja Datos (el script quedó en el scratchpad de la sesión, no en la bóveda).

### Cifras del tablero en los 6 combos (verificadas por COM)

| Indicador | Estándar · Pesimista | Estándar · Base | Estándar · Optimista | Premium · Pesimista | Premium · Base | Premium · Optimista |
|---|---|---|---|---|---|---|
| Precio mensual sin IVA (USD) | 250 | 175 | 160 | 380 | 275 | 230 |
| Implementación (USD) | 266,69 | 222,24 | 177,79 | 377,81 | 311,14 | 244,46 |
| Costo hora fundadores (USD) | 9,26 | 9,26 | 9,26 | 9,26 | 9,26 | 9,26 |
| Costo total del mes (USD) | 204,40 | 144,38 | 129,37 | 315,25 | 225,84 | 190,84 |
| Inversión inicial (USD) | 3.101 | 2.236 | 1.848 | 3.107 | 2.243 | 1.854 |
| VAN TEAMSLASH (USD) | -1.580 | -1.153 | -675 | 402 | 427 | 517 |
| TIR TEAMSLASH | -15,4 % | -17,2 % | -10,7 % | 24,7 % | 25,7 % | 24,4 % |
| B/C | 0,79 | 0,79 | 0,85 | 1,01 | 1,03 | 1,04 |
| Recuperación (meses) | Más de 36 | Más de 36 | Más de 36 | 25,0 | 24,7 | 25,4 |
| TMAR | 17,2 % | 15,0 % | 9,9 % | 17,2 % | 15,0 % | 9,9 % |
| Beneficio Torvesa/mes (USD) | 38 | 753 | 3.667 | 52 | 892 | 4.224 |
| VAN Torvesa (USD) | -6.247 | 13.081 | 98.550 | -9.504 | 13.618 | 112.143 |
| Obras/año que pagan | 16,4 | 1,2 | 0,5 | 24,9 | 1,9 | 0,6 |
| % del beneficio de Torvesa | 657,3 % | 23,2 % | 4,4 % | 735,2 % | 30,8 % | 5,4 % |

Lectura rápida: el Premium es viable para TEAMSLASH en los 3 escenarios, aunque por poco (B/C entre 1,01 y 1,04). El Estándar solo no lo es en ninguno. Para Torvesa, el resultado depende casi por completo de supuestos suyos: va de -9.504 a 112.143 de VAN. Esa amplitud es justamente el argumento para pedir los datos.

## 5. Qué falta que aporte Torvesa (lo que mueve las cifras)

Ordenado por peso en el resultado:
1. **Solicitudes nuevas al mes** (hoy 15/30/40): muestra documental de mensajes de 3 meses (P2-B).
2. **Parte de las solicitudes que hoy se pierde** (10/20/25 %) y **tasa de cierre** (10/20 %): línea base M3 y registro de ventas.
3. **Valor promedio de una obra** (8.000/15.000/18.000; los 15.000 del Informe Final no tienen respaldo) y **margen real por obra**: contratos 2023-2025 y formulario 101 del SRI.
4. **Sueldo de quien atiende o cotiza** (700/1.000/1.300): rol de pagos.
5. **Tiempos actuales**: horas por cotización (CP-01), horas semanales buscando historial (CP-02), minutos para asignar y para dar seguimiento.
6. **Número real de usuarios** (5, del censo) y **ventas anuales de Torvesa** (hoy se usa la mediana del sector, USD 320.229).

De TEAMSLASH (Víctor y Diego), no de Torvesa: horas reales del levantamiento (registro de contribuciones + Git), factura real de Railway, si se usa Slack Pro (MH-2) y el régimen tributario (contador).
