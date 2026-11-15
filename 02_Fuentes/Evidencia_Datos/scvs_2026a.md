---
citekey: scvs_2026a
referencia_apa: "Superintendencia de Compañías, Valores y Seguros. (2026). *Ranking empresarial 2023, 2024 y 2025* [Conjunto de datos, archivos ranking_2023.xlsx, ranking_2024.xlsx y ranking_2025.xlsx; fecha de corte: 22 de octubre de 2026]. Recuperado el 15 de noviembre de 2026, de https://appscvsmovil.supercias.gob.ec/ranking/reporte.html"
doi_url: "https://appscvsmovil.supercias.gob.ec/ranking/reporte.html"
anio: 2026
tipo: base de datos oficial
categoria: Evidencia_Datos
objetivos: [5.3]
afirmaciones: []
afirmacion: "En Pichincha, las compañías de construcción de edificios (CIIU F41) con ventas de USD 100 001 a 1 000 000 fueron 273 en 2023, 306 en 2024 y 321 en 2025; vendieron en promedio USD 348 577, 370 750 y 379 865, con una mediana de 4 empleados y un margen neto mediano de 1,4 %, 1,7 % y 1,9 %."
cita_textual: "Columnas: «Actividad económica», «Provincia», «Cant. Empleados», «Ingreso por ventas», «Utilidad neta» (hojas Ranking2023, Ranking2024 y Ranking2025). Cálculo propio sobre esas columnas."
pagina: "hojas Ranking2023, Ranking2024 y Ranking2025; filas con Provincia = PICHINCHA y Actividad económica que empieza por F41 o F4210"
cita_en_texto: "(Superintendencia de Compañías, Valores y Seguros [SCVS], 2026a)"
confianza: alto
estado: verificada
vigencia: vigente
verificada_por: "Claude (lectura y cálculo sobre los archivos); falta visto bueno de Víctor"
fecha_verificacion: 2026-11-15
acceso: "abierto"
texto_local: "02_Fuentes/_Textos/scvs_2026a_ranking_2023.xlsx; scvs_2026a_ranking_2024.xlsx; scvs_2026a_ranking_2025.xlsx; scvs_2026a_extracto_construccion_pichincha.csv"
origen_busqueda: "Portal oficial (pestaña Recursos del ranking) · Frente A2: datos reales de Torvesa · 2026-11-15"
seminal: false
tags: [fuente, verificada, vigente, viabilidad, sector-construccion]
---

# Ranking empresarial de la Superintendencia de Compañías 2023–2025

## Qué respalda
Agregados reales del sector construcción en Pichincha, para comparar con Torvesa (que no está en la Superintendencia):

| Grupo (Pichincha, ventas USD 100 001–1 000 000) | 2023 | 2024 | 2025 |
|---|---|---|---|
| F41 edificios: compañías | 273 | 306 | 321 |
| F41: ventas promedio (USD) | 348 577 | 370 750 | 379 865 |
| F41: ventas medianas (USD) | 270 174 | 300 979 | 320 229 |
| F41: margen neto mediano | 1,39 % | 1,65 % | 1,89 % |
| F41: margen neto agregado (Σ utilidad neta / Σ ventas) | 0,82 % | 1,73 % | 3,87 % |
| F4210 carreteras: compañías | 40 | 41 | 36 |
| F4210: ventas promedio (USD) | 390 496 | 367 905 | 304 609 |
| F4210: margen neto mediano | 1,16 % | 1,18 % | 1,44 % |

## Cita textual
> Encabezados de los archivos: «Actividad económica», «Provincia», «Cant. Empleados», «Ingreso por ventas», «Utilidad neta». Los promedios, medianas y márgenes son **cálculo propio**, no cifras publicadas por la Superintendencia.

## Cómo se usa en la tesis
Referencia sectorial del modelo financiero mientras no lleguen las cifras de Torvesa: `06_Capitulos/Modelo_Negocio/2026-11-15_Datos_Torvesa_Publicos.md`.

## Notas de verificación
- El ranking no trae costo de ventas ni gastos: no permite calcular margen bruto.
- Fecha de corte 22-oct-2026: el año 2025 puede estar incompleto (empresas que aún no presentaron balances).
- El tramo de ventas USD 100 001–1 000 000 es un corte propio por ingresos; la columna «Tamaño» de la Superintendencia solo viene llena en 2023.
- Los márgenes «agregados» del tramo F4210 salen negativos en 2024 y 2025 por unas pocas empresas con pérdidas grandes; por eso se prefiere la mediana.
- El archivo indicadores_sector.csv de la misma página (2018–2023) da promedios de razones con valores absurdos para la sección F (por ejemplo, margen bruto −305 en 2023): **no se usa**.
