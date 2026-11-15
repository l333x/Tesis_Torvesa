---
fecha: 2026-11-15
autor: "Claude (Frente A2: datos reales de la empresa)"
estado: v0.1 para revisión de Víctor
fuentes: [sri_2026, scvs_2026a, scvs_2026b]
---

# Datos públicos de Torvesa para el modelo financiero (2023–2025)

## Resultado en una línea
**No existen cifras financieras públicas de Torvesa.** El SRI confirma que es una sociedad activa en régimen general, pero **no está registrada en la Superintendencia de Compañías**, así que no tiene estados financieros publicados ni aparece en el ranking empresarial. Para el modelo se dejan los agregados reales del sector en Pichincha como referencia y las cifras propias se piden a la empresa (Diego). `[FALTA-DATO]`

## 1. Qué se consultó (15-nov-2026)

| # | Fuente y dirección | Resultado | Ficha |
|---|---|---|---|
| 1 | SRI, servicio público de consulta de RUC: `srienlinea.sri.gob.ec/sri-catastro-sujeto-servicio-internet/rest/ConsolidadoContribuyente/obtenerPorNumerosRuc?&ruc=1792266424001` y `…/Establecimiento/consultarPorNumeroRuc?numeroRuc=1792266424001` | Respondió sin CAPTCHA. Datos de registro (tabla 2). Sin cifras financieras. | sri_2026 |
| 2 | Superintendencia de Compañías, portal de consulta: https://appscvsgen.supercias.gob.ec/consultaCompanias/societario/busquedaCompanias.jsf | Por R.U.C.: «No existe ninguna compañía cuyo R.U.C. coincida…». Por nombre «TORVESA» y «TORVES»: tampoco. Control con Corporación Favorita: sí la encuentra. | scvs_2026b |
| 3 | Superintendencia, directorio completo `bi_compania.csv` (actualizado el 15-nov-2026), en https://appscvsmovil.supercias.gob.ec/ranking/reporte.html → Recursos | Sin «TORVES» ni «1792266424». | scvs_2026b |
| 4 | Superintendencia, ranking empresarial 2023, 2024 y 2025 (xlsx, corte 22-oct-2026), misma página → Recursos | Torvesa no aparece. Se calcularon agregados del sector (tabla 4). | scvs_2026a |
| 5 | Superintendencia, `indicadores_sector.csv` (2018–2023) | Promedios de razones con valores absurdos para construcción (margen bruto −305 en 2023). **No se usa.** | — |
| 6 | SERCOP, datos abiertos de contratación pública (`datosabiertos.compraspublicas.gob.ec/PLATAFORMA/api/search_ocds`) | No respondió (tiempo de espera agotado, 4 intentos). Queda para Víctor. | — |

## 2. Ficha de la empresa (dato real, SRI)

| Dato | Valor | Fuente |
|---|---|---|
| Razón social | TORVESA CONSTRUCTORA | sri_2026, campo `razonSocial` |
| RUC | 1792266424001 | sri_2026 |
| Tipo de contribuyente | Sociedad | sri_2026, `tipoContribuyente` |
| Forma jurídica (S.A., Cía. Ltda., SAS) | **No determinada.** No está en la Superintendencia, así que probablemente no es una compañía mercantil; el SRI no dice qué tipo de sociedad es. `[FALTA-DATO]` | scvs_2026b |
| Estado | Activo | sri_2026, `estadoContribuyenteRuc` |
| Inicio de actividades | 5-ago-2010 | sri_2026, `fechaInicioActividades` |
| Actividad principal | Construcción de carreteras, calles, autopistas y otras vías (CIIU F4210) | sri_2026, `actividadEconomicaPrincipal` |
| Régimen | General (no RIMPE) | sri_2026, `regimen` |
| Obligada a llevar contabilidad | Sí | sri_2026 |
| Contribuyente especial / agente de retención | No / No | sri_2026 |
| Establecimientos | 1 (matriz, abierto), Quito, Pichincha | sri_2026, servicio de establecimientos |
| Representante legal | Existe uno registrado (nombre no copiado por privacidad) | sri_2026 |
| Capital, empleados | No públicos | — |

**Atención:** el SRI registra a Torvesa como constructora de **vías**, no de edificios. Si la tesis la presenta como constructora de vivienda o edificios, hay que confirmar con Diego cuál es su actividad real y, si hace falta, decirlo en el Cap. I.

## 3. Cifras de Torvesa por año

| Cuenta | 2023 | 2024 | 2025 | Fuente |
|---|---|---|---|---|
| Ingresos (ventas) | `[FALTA-DATO]` | `[FALTA-DATO]` | `[FALTA-DATO]` | No públicas |
| Costo de ventas | `[FALTA-DATO]` | `[FALTA-DATO]` | `[FALTA-DATO]` | No públicas |
| Utilidad bruta | `[FALTA-DATO]` | `[FALTA-DATO]` | `[FALTA-DATO]` | No públicas |
| Gastos | `[FALTA-DATO]` | `[FALTA-DATO]` | `[FALTA-DATO]` | No públicas |
| Utilidad neta | `[FALTA-DATO]` | `[FALTA-DATO]` | `[FALTA-DATO]` | No públicas |
| Activos / pasivos / patrimonio | `[FALTA-DATO]` | `[FALTA-DATO]` | `[FALTA-DATO]` | No públicas |
| Empleados | `[FALTA-DATO]` | `[FALTA-DATO]` | `[FALTA-DATO]` | No públicas |

Indicadores (margen bruto, margen neto, crecimiento de ventas): **no se pueden calcular** sin las cifras anteriores. No se inventa ninguna.

**De dónde salen:** como sociedad obligada a llevar contabilidad, Torvesa presenta cada año al SRI el **formulario 101** (declaración de impuesto a la renta de sociedades), que trae el estado de situación y el estado de resultados completos. No es público: solo lo puede entregar la empresa. Se pide por medio de Diego (ver sección 6).

## 4. Referencia del sector (dato real, Superintendencia; cálculo propio)

Compañías de **Pichincha** en el ranking empresarial, con ventas entre USD 100 001 y 1 000 000 (corte propio por ingresos).

| Indicador | 2023 | 2024 | 2025 | Fuente |
|---|---|---|---|---|
| **F41 Construcción de edificios** — compañías en el tramo | 273 | 306 | 321 | scvs_2026a, hojas Ranking2023/2024/2025 |
| F41 — ventas promedio (USD) | 348 577 | 370 750 | 379 865 | ídem, col. «Ingreso por ventas» |
| F41 — ventas medianas (USD) | 270 174 | 300 979 | 320 229 | ídem |
| F41 — crecimiento de las ventas promedio | — | +6,4 % | +2,5 % | cálculo propio |
| F41 — crecimiento de las ventas medianas | — | +11,4 % | +6,4 % | cálculo propio |
| F41 — margen neto mediano (utilidad neta / ventas) | 1,39 % | 1,65 % | 1,89 % | ídem, col. «Utilidad neta» |
| F41 — margen neto agregado (Σ utilidad / Σ ventas) | 0,82 % | 1,73 % | 3,87 % | ídem |
| F41 — empleados (mediana) | 4 | 4 | 4 | ídem, col. «Cant. Empleados» |
| **F4210 Carreteras** (actividad de Torvesa en el SRI) — compañías en el tramo | 40 | 41 | 36 | ídem |
| F4210 — ventas promedio (USD) | 390 496 | 367 905 | 304 609 | ídem |
| F4210 — ventas medianas (USD) | 277 829 | 245 395 | 256 872 | ídem |
| F4210 — margen neto mediano | 1,16 % | 1,18 % | 1,44 % | ídem |
| F4210 — empleados (mediana) | 4,5 | 4 | 4 | ídem |

Contexto de todo el sector F41 en Pichincha (todas las compañías con ventas > 0): 760 (2023), 857 (2024) y 902 (2025); ventas medianas USD 116 701, 97 492 y 100 367; margen neto mediano 1,08 %, 1,13 % y 1,34 %. Registradas en total (con o sin ventas): 1387, 1508 y 1636.

**Límites:**
- El ranking no trae costo de ventas: **no hay margen bruto sectorial** en esta fuente.
- 2025 puede estar incompleto (corte 22-oct-2026).
- El tramo F4210 es pequeño (36–41 compañías); sus márgenes agregados salen negativos en 2024 y 2025 por pocas empresas con pérdidas grandes, por eso se usa la mediana.
- Los márgenes del sector son bajos (1–2 %): sirven para comparar, no para suponer el margen de Torvesa.

Archivos (locales, no se suben): `02_Fuentes/_Textos/scvs_2026a_ranking_2023.xlsx`, `…_2024.xlsx`, `…_2025.xlsx`, `scvs_2026a_extracto_construccion_pichincha.csv` (filas filtradas, sin nombres), `scvs_2026a_referencia_indicadores.pdf` y `sri_2026_catastro_ruc_torvesa.json` (sin el nombre del representante).

## 5. Qué se puede usar ya en el modelo financiero
1. La ficha de la empresa (tabla 2) en la descripción de Torvesa.
2. La tabla 4 como **rango de referencia** de una constructora pequeña de Pichincha: ventas de USD 250 000–380 000 al año, unos 4 empleados registrados y margen neto de 1–2 %. Debe decirse que es el sector, no Torvesa.
3. Escenarios del modelo: mientras no lleguen las cifras reales, usar la mediana del sector como escenario base y marcarlo `[FALTA-DATO]`.

## 6. Para que Víctor lo haga a mano (o lo pida a Diego)
1. **Pedir a Torvesa (vía Diego) las cifras 2023–2025.** Lo más simple: copia de los **formularios 101** de impuesto a la renta de 2023, 2024 y 2025 (o los estados financieros que firma su contador). Campos que necesita el modelo: ingresos por ventas, costo de ventas, gastos administrativos y de ventas, utilidad neta, activo, pasivo, patrimonio y número de empleados en nómina. Guardarlos en `05_Datos_Campo/_crudo/` (no se suben).
2. **Preguntar a Diego qué tipo de sociedad es Torvesa** (por qué no está en la Superintendencia) y si su actividad real es vías, edificios o ambas.
3. **SERCOP (contratos públicos):** abrir https://datosabiertos.compraspublicas.gob.ec/PLATAFORMA/ en Chrome; en el buscador poner `1792266424001` o `TORVESA` y filtrar los años 2023, 2024 y 2025. Si aparecen contratos adjudicados, anotar monto, entidad y fecha. Hoy el sitio no respondió desde aquí (posible caída o bloqueo); si pide CAPTCHA, resolverlo a mano.
4. **Consulta del SRI en la web (opcional, para captura de pantalla):** https://srienlinea.sri.gob.ec/sri-en-linea/SriRucWeb/ConsultaRuc/Consultas/consultaRuc → escribir `1792266424001` → resolver el CAPTCHA si aparece → guardar la captura en `02_Fuentes/_Textos/`. Debe dar los mismos datos de la tabla 2.
