# Cambios a los Excel de costos: modelo v0.3, estudio v0.4, matriz v0.3 y tablero v0.2 (23-nov-2026)

Para la IA. Aplica los hallazgos de `2026-11-22_Revision_Excel_y_Tablero_v0.1.md` (MF-1 a MF-13, EC-1 a EC-11, MH-1 a MH-7). **Ningún original se tocó** (`git status` no marca como modificados los libros del 15-nov ni el tablero v0.1). Todo se editó con Excel por COM (se conservan formatos, validaciones, formatos condicionales y gráficos), se recalculó con `CalculateFull` y se revisaron todas las celdas de todas las hojas: **0 errores** en los cuatro libros. Cada libro tiene una hoja `Cambios v0.x` (después de la portada; en el tablero, después de la hoja Tablero) con hallazgo, celda, qué se cambió, por qué y efecto, en lenguaje simple. Scripts en el scratchpad de la sesión (no en la bóveda).

Archivos nuevos (en `06_Capitulos/Modelo_Negocio/`):
- `2026-11-23_Modelo_Financiero_v0.3.xlsx` (desde MF v0.2)
- `2026-11-23_Estudio_Costos_v0.4.xlsx` (desde EC v0.3)
- `2026-11-23_Matriz_Herramientas_v0.3.xlsx` (desde MH v0.2)
- `2026-11-23_Tablero_Costos_v0.2.xlsx` (desde el tablero v0.1, Datos rellenada desde MF v0.3)
- Copia del tablero v0.2 y del modelo v0.3 en `C:\Users\vasha\Desktop\TESIS - ENVIO TUTORA 23-nov\`.

## 1. Modelo financiero v0.3

| # | Celdas | Qué se hizo |
|---|---|---|
| MF-1 | `Panel!C26:C30` | Denominador `COUNTA(Supuestos!$I$7:$I$82)` (solo filas con tipo). Solo con este arreglo: 44,4 / 47,6 / 7,9 %. Con las etiquetas y filas nuevas: **42,6 % DATO (29), 50,0 % SUPUESTO (34), 7,4 % DECISIÓN (5) sobre 68**. Proyecto DATO o DECISIÓN: 69,6 %. |
| MF-2 | `Supuestos!I8`, `I27`, `J27`, `B3`; `Panel!C30`, `B30`, `D30` | `usuarios` = DATO-TORVESA (censo); `margen_obra` = DATO-SECTOR. C30 cuenta solo `DATO-TORVESA` en el bloque Torvesa: **1 de 22 = 4,5 %** (antes 1 de 18 = 6 %, que era verdad por casualidad). |
| MF-3 | `2_Costos!B19:G19` | Firma fuera del costo mensual: `=p_dominio/12` (1,25 al mes). La firma queda solo en `1_Inversion!E9` (62,10). Nota en C19, G19 y `1_Inversion!F9`. La renovación de la firma del año 3 (20,70 c/u, ficha dgrcic_sf) no está en el modelo: se dijo en la hoja Cambios. |
| MF-4 | Filas nuevas `Supuestos!A18:L21` (bloque Torvesa); `8_Torvesa!E9:F10, E13:F13` | Nombres `min_asignar_con` (1), `min_seguimiento_con` (4), `pct_whatsapp` (0,8), `min_reporte_semana` (15), SUPUESTO. Mismos valores en los 3 escenarios para no mover cifras. El EC usa 5/4/3 (T04D) y 20/15/10 (T07) por escenario: **[DECIDIR-VÍCTOR]**. |
| MF-5 | Fila nueva `Supuestos!A41:L41`; `5_Estado_Resultados!F13:H15` | `tasa_participacion` = 15 % (DATO, Código del Trabajo art. 97, p. 40). Amortización `=inversion_levantamiento/(meses_recuperacion/12)`. |
| MF-6 | `8_Torvesa!F18` | `=F16*valor_obra*margen_obra`. |
| MF-7 | `9_Escenarios!B7:G17` | Foto regenerada con la v0.3 (23-nov). |
| MF-8 | `Supuestos!J37` (rosado) y `Panel!B35` | Valor 160 h sin cambiar; nota visible de la incoherencia con 52 ÷ 12 de la hoja 8 **[DECIDIR-VÍCTOR]**. |
| MF-9 | `Supuestos!I42:J42` | TMAR = SUPUESTO con base en dato (17,18 % es solo prima de riesgo; 9,87 % es tasa de crédito). |
| MF-10 | `Panel!B33` (texto en rojo) | Aviso: Premium base USD 270 se lleva el **30,3 %** del beneficio y pasa el 25 %; Estándar base USD 175 cumple con **23,2 %**; en la v0.2 eran 275 y 30,8 %. |
| MF-11 | `5_Estado_Resultados!I13`, `Supuestos!J47` | **Resuelto**: ficha `02_Fuentes/Normativa/sri_2015.md` verificada (art. 28, num. 6, lit. a, p. 19 del PDF, 33 % anual). Se quitó [FALTA-FUENTE]. |
| MF-12 | `Fuentes!C7` | **Resuelto**: la ficha `ministerio_2026.md` ya explica que el título es el del documento y el nombre del archivo es otro (revisado contra el PDF, p. 2). Nota agregada. |
| MF-13 | `Panel!B34` | Aviso: el Estándar solo no paga el levantamiento. |
| Otros | `Portada!B2, B3, C31, C34, B22:C22`; `10_Escalamiento!A17` | v0.3, fecha, portada honesta sobre números en fórmulas (quedan solo conversiones 60/12/52 y los 2 fundadores), enlace a Cambios v0.3, referencia al EC v0.4. |

Filas de Supuestos que se movieron (para quien cite celdas): todo lo que estaba en la fila 18 o más baja +4; lo que estaba en la 37 o más baja, +5. Ejemplos: `tarifa_hora` H40 → **H45**; `tasa_descuento` H37 → **H42**; `horas_mes` H33 → H37; `margen_obra` H23 → H27; `meses_recuperacion` H42 → H47.

### Cifras presentadas a la tutora (Premium, base): solo cambian por la firma

Comprobado por COM: se aplicó **solo** el arreglo de la firma a una copia del v0.2 y dio las mismas cifras que la v0.3 en los 6 casos (diferencia 0). MF-4, MF-5 y MF-6 no mueven nada.

| Indicador | v0.2 | v0.3 | Cambio |
|---|---|---|---|
| Precio mensual Premium | 275 | **270** | −5 (el costo baja 2,59 y el redondeo a múltiplo de 5 cae en 270) |
| Implementación | 311,14 | 311,14 | 0 |
| Hora de los fundadores | 9,26 | 9,26 | 0 |
| Costo total del mes | 225,84 | 223,26 | −2,59 |
| Inversión inicial | 2.242,84 | 2.235,08 | −7,76 (capital de trabajo) |
| VAN TEAMSLASH | 426,74 | **379,82** | −46,92 |
| TIR TEAMSLASH | 25,7 % | **24,6 %** | −1,1 puntos |
| B/C | 1,028 (1,03) | **1,023 (1,02)** | −0,005 |
| Recuperación | 24,7 meses | 25,1 meses | +0,33 |
| VAN Torvesa | 13.618 | **13.755** | +137 |
| Obras/año que pagan | 1,91 | **1,88** | −0,03 |
| % del beneficio | 30,8 % | 30,3 % | −0,6 puntos |
| Datos de Torvesa | 6 % | 4,5 % | no es por la firma: MF-2 y MF-4 |

Lectura: TEAMSLASH gana un poco menos (el precio baja 5 y el costo solo 2,59) y Torvesa un poco más. El Premium sigue viable (B/C 1,02 a 1,05) y sigue pasando la regla del 25 % en base.

### Los 6 casos, v0.2 → v0.3

| Indicador | Est. · Pesimista | Est. · Base | Est. · Optimista | Prem. · Pesimista | Prem. · Base | Prem. · Optimista |
|---|---|---|---|---|---|---|
| Precio (USD/mes) | 250 → 245 | 175 (=) | 160 → 155 | 380 (=) | 275 → 270 | 230 (=) |
| Implementación (USD) | 266,69 (=) | 222,24 (=) | 177,79 (=) | 377,81 (=) | 311,14 (=) | 244,46 (=) |
| Costo total del mes (USD) | 204,40 → 201,81 | 144,38 → 141,79 | 129,37 → 126,78 | 315,25 → 312,67 | 225,84 → 223,26 | 190,84 → 188,25 |
| Inversión inicial (USD) | 3.101 → 3.094 | 2.236 → 2.228 | 1.848 → 1.841 | 3.107 → 3.099 | 2.243 → 2.235 | 1.854 → 1.846 |
| VAN TEAMSLASH (USD) | -1.580 → -1.641 | -1.153 → -1.080 | -675 → -746 | 402 → 457 | 427 → 380 | 517 → 577 |
| TIR TEAMSLASH (%) | -15,4 → -16,9 | -17,2 → -15,1 | -10,7 → -13,1 | 24,7 → 25,8 | 25,7 → 24,6 | 24,4 → 26,1 |
| B/C | 0,79 → 0,78 | 0,79 (=) | 0,85 → 0,83 | 1,01 → 1,02 | 1,03 → 1,02 | 1,04 → 1,05 |
| Recuperación (meses) | Más de 36 (=) | Más de 36 (=) | Más de 36 (=) | 25,0 → 24,7 | 24,7 → 25,1 | 25,4 → 24,8 |
| VAN Torvesa (USD) | -6.247 → -6.115 | 13.081 (=) | 98.550 → 98.700 | -9.504 (=) | 13.618 → 13.755 | 112.143 (=) |
| Obras/año que pagan | 16,43 → 16,11 | 1,22 (=) | 0,45 → 0,44 | 24,93 (=) | 1,91 → 1,88 | 0,65 (=) |
| % del beneficio | 657,3 → 644,2 | 23,2 (=) | 4,4 → 4,2 | 735,2 (=) | 30,8 → 30,3 | 5,4 (=) |

Donde el redondeo no cambia el precio (Est. base, Prem. pesimista y optimista), TEAMSLASH mejora un poco (el costo baja y el precio no). El beneficio de Torvesa al mes no cambia en ningún caso.

## 2. Estudio de costos v0.4

| # | Celdas | Qué se hizo |
|---|---|---|
| EC-1 | `Supuestos!D15:F15` | IESS 11,15 % → 12,15 % (fuente del MF). `A1_Costo_hora!G5` dice 12,15 %. |
| EC-2 | `Supuestos!D51:F51` | Sueldo desarrollo 1.000 → 1.084 (Ekos, DATO). Hora de desarrollo 8,50 → **9,26**. Textos 8,50 → 9,26 en `Resumen!G39`, `A4_Equilibrio!G29`, `A6_Tres_Anios!G33, G46, G59`. `A3_Decisiones!A26` actualizado (USD 1.482 al mes son 30 clientes promedio). |
| EC-3 | `Supuestos!D24:F24` | Tasa 15/12/9,87 % → 17,18/15/9,87 % (igual que MF, SUPUESTO con base en dato). |
| EC-4 | `Supuestos!D22:F22` | Margen de obra 8/10/12 % → 2,35/11,88/24,40 % (DATO-SECTOR). `A5_Segmentos!A2` dice 11,88 %. |
| EC-5/EC-6 | `Resumen!A50:H54`, `Supuestos!G67`, `B2_Implementacion!A17, G23`, `Resumen!B13:B14` | Escrito que USD 149 es el precio de lista del nivel 3 con 20 empresas; con un solo cliente vale el MF v0.3 (Premium 270 + 311,14; Estándar 175 + 222,24; VAN Torvesa 13.755; 1,88 obras). La opción 2 del EC es la lectura a precio de lista. |
| EC-7 | `Supuestos!G16:G17` | Fondos de reserva y 160 h como DATO (Código del Trabajo); las 160 h con [VERIFICAR-PÁG] y [DECIDIR-VÍCTOR] por MF-8. |
| EC-8 | `Supuestos!G32` | Se mantiene USD 15: es otra persona (técnico independiente externo), no la hora de los fundadores (9,26). Referencia alta Lemon.io 34. |
| EC-9 | `A6_Tres_Anios!B65, G65` | Explicado: este VAN no resta levantamiento ni laptops; el MF sí (1.852 en base). |
| EC-10 | `A2_Costo_operar!D33:F33` | 2 firmas (una por fundador). Aquí la firma va en el costo del mes porque el EC no tiene inversión: se cuenta una vez. 2,54 → 3,84 al mes. |
| EC-11 | `Leeme!A1, A16, A22`, `Supuestos!A5` | Ya no dicen "mismos valores que el modelo v0.1". |
| Escondidos | Filas nuevas `Supuestos!A88:G94`; `A1!E21`, `A2!D33:F33`, `A4!D28:F28` | `IND_S` 10 %, `DOM` 15, `N_FIRMAS` 2, `MESES_FIRMA` 24, `SOP_MITAD` 50 %. |
| Frágil | `A1_Costo_hora!D4:F4` | Las tres leen la columna D de Supuestos (antes D51, E52, F53). |

Cifras del Resumen (base salvo que se diga): hora 8,50 → 9,26; beneficio Torvesa 804,30 → 891,50 (ahora igual al MF Premium base); VAN opción 1 12.388 → 13.688; VAN opción 2 (precio de lista) 15.832 → 17.082; obras opción 2 1,30 → 1,09; VAN opción 2 pesimista -3.490 → -3.382, optimista 70.357 → 114.769; empresas para cubrir todo 18/27/37 → 19/29/40; pago por hora año 3 base 6,16 → 6,12; VAN de TEAMSLASH con varias empresas 2.360 → 2.142.

## 3. Matriz de herramientas v0.3

| # | Celdas | Qué se hizo |
|---|---|---|
| MH-1 | `TCO!C8:D8`, `TCO!H23` | Tarifa 15 → **9,26** (hora de los fundadores del MF v0.3). |
| MH-2 | `Precios!G7`, `TCO!H14` (rosado) | **No resuelto**: [DECIDIR: confirmar con Diego] Slack Pro, Slack gratuito o WhatsApp. Si se quita Slack Pro, el TCO de A baja unos USD 1.500. |
| MH-3 | `Precios!E5` | Referencia a `consumo_servidor` del MF v0.3. |
| MH-4 | `Portada!C16` | Gana siempre el stack propio (A, o D si se pesa la escala). |
| MH-5 | `TCO!D14:D24` | Fondo amarillo de supuesto. |
| MH-6 | `Por_que_nosotros!D16:G16` | Enlazados a Precios × usuarios (70, 100, 60, 49). |
| MH-7 | `Puntuacion!O4:O15` | Control de evidencia con COUNTIFS: hoy las 11 dicen Completa. |
| Otros | `Portada!B2, B3, B5, C23, B18:C18`, `Leeme!A1`, `Por_que_nosotros!B16:C16` | v0.3, rango de los CRM actualizado (USD 7.674 a 9.600), enlace a Cambios v0.3. |

**¿Cambia la decisión con 9,26?** No. Ganador A y segundo D; los 4 primeros iguales (A, D, B3, B1). Solo **Zoho (B2) y Odoo (B5) intercambian los puestos 5 y 6** (Odoo tiene 120 h de implementación y la hora más barata lo favorece: 3,34 frente a 3,33). En Sensibilidad el ganador de los 6 juegos de pesos es el mismo (A en cinco, D en escalar); el mismo cruce B2/B5 aparece en Propuesta y en Costo primero. TCO a 3 años: A 9.039 → 7.295; D 9.019 → 7.274; B4 8.959 → 7.674; B1 10.771 → 9.600.

## 4. Tablero v0.2

- Mismas hojas (Tablero, Datos, Cómo usar, Glosario) y mismos selectores (C4 plan, F4 escenario) más `Cambios v0.2`.
- `Datos!D6:I63`: 52 indicadores × 6 combos copiados del MF v0.3 por COM (Panel C4/C5 de cada combo, `CalculateFull`). Orígenes en la columna J dicen `Modelo_Financiero_v0.3` y las celdas nuevas (tarifa H45, TMAR H42).
- Franja dato/supuesto con el % correcto del MF v0.3: **43 % dato, 50 % supuesto, 7 % decisión, 5 % (4,5 %) datos propios de Torvesa**, con texto que explica que el único dato de Torvesa es el censo y que el margen es del sector (`Tablero!B25:D26`, `Cómo usar!C19`).
- `Datos!B30` y `Tablero!L31`: "Dominio web" (la firma salió del costo mensual).
- Gráfico 4 (costo por herramienta): la zona de apoyo `L27:M34` ahora ordena sola de mayor a menor con LARGE/INDEX sobre `P27:Q34` (con el orden fijo se desordenaba en pesimista y en base).
- Verificación por COM: 0 errores en cada uno de los 6 combos; las tarjetas coinciden con el MF v0.3 (tabla de la sección 1). PDF de Premium·Base y Estándar·Pesimista revisados: sin cortes ni textos montados; el % del beneficio en rojo cuando pasa el 25 %.

## 5. Queda para decidir

1. **[DECIDIR-VÍCTOR] MF-8**: 160 h (4 semanas) frente a 4,33 semanas. Si se usa 173,3 h, la hora baja a unos 8,55 y cambian todos los precios. Falta además la página del art. 47 del Código del Trabajo [VERIFICAR-PÁG].
2. **[DECIDIR: confirmar con Diego] MH-2**: Slack Pro en el TCO, que el MF no cobra.
3. **[DECIDIR-VÍCTOR]** Minutos con recordatorio y del reporte: el MF usa 4 y 15 fijos; el EC usa 5/4/3 y 20/15/10 por escenario.
4. Renovación de la firma en el año 3 (2 × 20,70) no está en el MF: decidir si se suma a la inversión o a un gasto del año 3.
5. Decir a la tutora que el precio Premium base pasa de 275 a 270 (y VAN 427 → 380, TIR 25,7 → 24,6 %, B/C 1,03 → 1,02, VAN Torvesa 13.618 → 13.755, obras 1,91 → 1,88, datos de Torvesa 6 → 4,5 %), y que el Premium base sigue pasando la regla del 25 % (30,3 %).
6. Los textos de los capítulos y del borrador 4 que citan 275, 427, 25,7 %, 1,03, 13.618, 1,91 o 6 % quedan desactualizados: actualizarlos en la próxima versión que edite Víctor.
7. Lo que sigue pendiente de la revisión del 22-nov y no se tocó: el EC conserva la tarifa 15 de un independiente (documentada), y en el MF quedan las conversiones de unidades y el número de fundadores (2) dentro de fórmulas.
