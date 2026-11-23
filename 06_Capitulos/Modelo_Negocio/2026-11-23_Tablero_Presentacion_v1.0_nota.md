---
titulo: "Nota del tablero de presentación v1.0 (para la IA)"
fecha: 2026-11-23
archivos: "2026-11-23_Tablero_Presentacion_v1.0.xlsx (48 KB) y .pdf (11 páginas)"
generador: "armar_tablero.py, en el scratchpad de la sesión del 23-nov (no está en la bóveda)"
---

# Tablero de presentación v1.0

Es un libro liviano para que Victor presente en su laptop a la directora de carrera y a la tutora. **Solo tiene valores copiados**, sin fórmulas ni vínculos externos. Cada número va en la hoja `Datos y origen`, con su archivo, hoja, celda y tipo (133 filas). Si cambia el modelo financiero, el libro se vuelve a generar.

## Hojas
| Hoja | Contenido | Fuente |
|---|---|---|
| Inicio | Lectura en 30 s, índice con vínculos internos (`location`), tres avisos honestos y vínculos **relativos** a `Modelo_Financiero_v0.3.xlsx`, `Tesis_Borrador4_v0.3.pdf`, `Presentacion_Revision2_v0.4.pdf` y `Flujo_Aprendizaje.pdf`, que deben estar en la misma carpeta | — |
| Finanzas | 3 tarjetas, tabla Premium/Estándar base, VAN de los 6 casos, a dónde va cada dólar del precio, costo por día/semana/solicitud y aviso del 30,3 % > 25 % | MF v0.3: `9_Escenarios!B7:G17`, `2_Costos!F13,F16,F17,F22,F24,F30`, `3_Precio!F9,F10,F12,E17,F26`, `Panel!C10,C13,C18,C26:C30` |
| Metricas | M1 a M6: qué mide, unidad, regla, línea base, cómo se mide sin datos de personas (propuesta DEC-21), instrumento, cuándo y estado | Cap. I p2 v0.6 (metas), Cap. V–VI v0.6 (Tablas 18 y 19), Cap. III v0.6 |
| Herramientas | Ranking de 11 alternativas y costo a 3 años; el gráfico de costo excluye C2 (USD 721.306) | MH v0.3: `Puntuacion!L5:M15`, `TCO!G14:G24` |
| Avance | Estado por capítulo, hitos, DEC-18 a DEC-25, marcas del borrador 4 v0.3 (57/22/11/7/3) y tiempo usado (42 de 84 días) | Nota del borrador 4 v0.3, conteo del armador, correo del 23-nov |
| Datos y origen | 133 filas, ordenadas por tipo: DATO-TORVESA, DATO-SECTOR, SUPUESTO, DECISIÓN, DATO y CÁLCULO | — |
| Glosario | 15 términos | — |

## Verificación (23-nov)
- Se abrió con Excel por COM, se corrió `CalculateFull` y se revisaron todas las celdas de las 7 hojas: **0 errores**.
- Las cifras coinciden con el MF v0.3 en el Premium base: 270, 311, VAN 380, TIR 24,6 %, B/C 1,02, 25 meses, VAN Torvesa 13.755 y 1,9 obras (1,876 en el modelo; se muestra 1,9, igual que la tesis). En el Estándar base: 175, 222, VAN −1.080 y VAN Torvesa 13.081.
- El PDF se exportó con Excel (11 páginas: 1 por hoja de presentación y 5 de Datos y origen) y se revisaron todas las páginas renderizadas. Se corrigieron: el formato `USD #,##0` sin comillas, que impedía abrir el libro (ahora `"USD" #,##0`); las barras negativas huecas (`invertIfNegative`); etiquetas cortadas; los gráficos montados en Herramientas; y las áreas de impresión.

## Lo que queda como FALTA
- Las líneas base de M1 y M3 (muestra de fechas y horas de Torvesa) y los resultados de M1 a M6.
- 21 de 22 entradas de Torvesa son supuestos (solicitudes, valor de una obra, tasa de cierre, pérdida) y las 200 horas del levantamiento también.
- El estado por tarea de `Cronograma_Tesis.xlsx` no está al día desde el sprint 3 (S5 y S6 marcan 0 hechas). Por eso el avance se muestra por capítulo.
- M6: el capítulo I dice SUS ≥ 68 y el V dice "según lo que se acuerde"; queda sujeto a la DEC-23.
