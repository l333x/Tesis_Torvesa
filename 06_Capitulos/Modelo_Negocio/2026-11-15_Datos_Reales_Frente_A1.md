---
titulo: "Datos reales para el modelo financiero — Frente A1"
fecha: 2026-11-15
autor: "Claude (Frente A1, investigación de cifras); falta visto bueno de Víctor"
estado: borrador
uso: "Insumo del modelo financiero rehecho («80 % real»). Las fichas están en 02_Fuentes/."
---

# Datos reales para el modelo financiero (Frente A1)

**Regla:** «verificada» = se abrió la página o el PDF y se vio el dato. «Candidata» = solo se vio en un resumen o en un resultado de búsqueda: **no se cita** hasta verificarla. Las fichas nuevas (21) tienen `fecha_verificacion: 2026-11-15`. Las que dicen «extracción automática» se leyeron con WebFetch: abrir la página antes de citar entre comillas.

Columnas: Código sugerido | Concepto | Valor | Unidad | Fuente (cita en texto APA) | Página | Fecha de consulta | Confianza | Estado | Nota.

## 1. Laboral y tributario (Ecuador 2026)

| Código | Concepto | Valor | Unidad | Fuente | Página | Consulta | Confianza | Estado | Nota |
|---|---|---|---|---|---|---|---|---|---|
| LAB-01 | Salario básico unificado 2026 | 482 | USD/mes | (Ministerio del Trabajo, 2026); (Farfán, 2025) | p. web | 15-nov-2026 | alta | verificada | Confirma el dato actual. Ficha `ministerio_2026` (ya existía) y `farfan_2025`. |
| LAB-02 | Aporte patronal IESS (sector privado) | 11,15 | % del sueldo | (IESS, 2014); (Farfán, 2025) | p. 1; p. web | 15-nov-2026 | alta | verificada | IVM 3,10 + salud 5,71 + riesgos 0,55 + cesantía 1,00 + campesino 0,35 + administración 0,44. Tabla de 2014, vigente según Farfán (2025). |
| LAB-03 | Aporte personal IESS | 9,45 | % del sueldo | (IESS, 2014) | p. 1 | 15-nov-2026 | alta | verificada | Lo paga el trabajador (se descuenta del sueldo). |
| LAB-04 | SECAP + IECE (a cargo del empleador) | 0,5 + 0,5 = 1,0 | % de la planilla | (González, 2026b) | p. web | 15-nov-2026 | media | verificada | **Costo patronal total = 12,15 %**, no 11,15 %. Hay proyectos de ley sobre el 0,5 % del IECE. |
| LAB-05 | Decimotercera remuneración | 1/12 de lo percibido en el año (≈ 8,33 %) | % del sueldo | (Código del Trabajo, 2005, art. 111) | pp. 44–45 | 15-nov-2026 | alta | verificada | Mensual o acumulada hasta el 24-dic. No aporta al IESS (art. 112). |
| LAB-06 | Decimocuarta remuneración | 1/12 del SBU al mes = 40,17 | USD/mes | (Código del Trabajo, 2005, art. 113) | p. 45 | 15-nov-2026 | alta | verificada | 482 / 12 = 40,17 (cálculo nuestro). |
| LAB-07 | Vacaciones | 15 | días/año | (Código del Trabajo, 2005, art. 69) | p. 33 | 15-nov-2026 | alta | verificada | Provisión ≈ 1/24 del sueldo (4,17 %), cálculo nuestro; +1 día por año después del 5.º. |
| LAB-08 | Fondo de reserva | 1 sueldo por año (≈ 8,33 %), desde el 2.º año | % del sueldo | (Código del Trabajo, 2005, art. 196) | p. 75 | 15-nov-2026 | alta | verificada | No aplica el primer año. |
| LAB-09 | Participación de trabajadores en utilidades | 15 | % de la utilidad líquida | (Código del Trabajo, 2005, art. 97) | p. 40 | 15-nov-2026 | alta | verificada | Se reparte a «sus trabajadores». **Una SAS sin empleados en relación de dependencia no tendría a quién pagarla** (interpretación; los socios no son trabajadores). Confirmar con contador. |
| LAB-10 | Costo total de un empleado con sueldo de USD 1.000 | ≈ 1.287 (año 1) y ≈ 1.370 (año 2 en adelante) | USD/mes | Cálculo con LAB-04 a LAB-08 | — | 15-nov-2026 | media | cálculo | 1.000 × (1 + 12,15 % + 8,33 % + 4,17 %) + 40,17 = 1.286,67; + 8,33 % de fondo de reserva = 1.370. |
| TRI-01 | Impuesto a la renta de sociedades (régimen general) | 25 | % de la base imponible | (Mora, 2026) | p. web | 15-nov-2026 | media | verificada | Fuente primaria (LRTI, art. 37) no abierta. |
| TRI-02 | RIMPE Emprendedor: tabla sobre ingresos brutos | 20.000–50.000: 60 + 1 %; –75.000: 360 + 1,25 %; –100.000: 672,50 + 1,5 %; –200.000: 1.047,50 + 1,75 %; –300.000: 2.797,52 + 2 % | USD + % marginal | (SRI, s. f.) | p. web | 15-nov-2026 | alta | verificada | Aplica a sociedades con ingresos ≤ USD 300.000. **Excluye «actividades profesionales»**: hay que ver si una SAS de software entra. Con USD 40.000 de ingresos pagaría ≈ USD 260 (cálculo nuestro) en vez del 25 % de la utilidad. |
| TRI-03 | IVA | 15 | % | Decreto Ejecutivo 198 (RO 520, 18-mar-2024) | — | 15-nov-2026 | media | candidata | Solo visto en prensa y resúmenes (Sovos, El Oriente: ratificado en 2025 por el Decreto 470). Falta abrir el decreto o la página del SRI. |
| TRI-04 | Depreciación: equipos de cómputo y software | 33 | % anual (máximo deducible) | (SRI, 2015, art. 28) | p. 19 | 15-nov-2026 | media | verificada | Compilación de 2015 (histórica). Muebles 10 %, vehículos 20 %, inmuebles 5 %. |
| TRI-05 | Retención en la fuente: honorarios de personas naturales (intelecto) | 10 | % | (NMS Abogados, 2026) | p. web | 15-nov-2026 | media | verificada | Resolución NAC-DGERCGC26-00000009, desde el 1-mar-2026. |
| TRI-06 | Retención: servicios profesionales de sociedades | 5 | % | (NMS Abogados, 2026) | p. web | 15-nov-2026 | media | verificada | Si TEAMSLASH factura como SAS, Torvesa retiene 5 % (si el servicio es «profesional»); si no, la regla general de 3 %. |
| TRI-07 | Retención: regla general / mano de obra | 3 | % | (NMS Abogados, 2026) | p. web | 15-nov-2026 | media | verificada | Antes 2,75 %. |

## 2. Costo del desarrollo

| Código | Concepto | Valor | Unidad | Fuente | Página | Consulta | Confianza | Estado | Nota |
|---|---|---|---|---|---|---|---|---|---|
| DEV-01 | Salario pretendido, Tecnología y Sistemas, junior (may-2025) | 579 | USD/mes | (Ekos Negocios, 2025) | p. web | 15-nov-2026 | media | verificada | Index de Multitrabajos. Es lo que **piden** los candidatos en Ecuador, no lo pagado. |
| DEV-02 | Salario pretendido, Tecnología y Sistemas, semi-senior y senior (may-2025) | 1.084 | USD/mes | (Ekos Negocios, 2025) | p. web | 15-nov-2026 | media | verificada | El supuesto de USD 1.000 queda cerca. |
| DEV-03 | Salario pretendido, Tecnología y Sistemas, junior (dic-2024) | 573 | USD/mes | (CCQ, 2025) | p. web | 15-nov-2026 | media | verificada | Promedio junior de todas las áreas: 540; senior/semi-senior: 872. |
| DEV-04 | Sueldo de desarrollador junior (Talently) | 1.200–1.500 (medio 1.350) | USD/mes | (Talently, 2026) | p. web | 15-nov-2026 | baja | verificada | Datos internos de una plataforma de reclutamiento; sin muestra ni método. |
| DEV-05 | Sueldo de desarrollador semi-senior (Talently) | 2.170–3.075 (medio 2.622,50) | USD/mes | (Talently, 2026) | p. web | 15-nov-2026 | baja | verificada | Más del doble del supuesto; sesgo a contratos remotos. |
| DEV-06 | Tarifa por hora, desarrollador ecuatoriano nivel medio (Q3 2026) | 34 | USD/h | (Lemon.io, 2026) | p. web | 15-nov-2026 | media | verificada | 178 contratos activos con clientes extranjeros; excluye juniors. Senior: USD 45/h. |
| DEV-07 | Mantenimiento anual de software | 10–15 | % del costo de desarrollo | Jeong et al. (2015), citando la guía coreana de costos de proyectos de software | — | 15-nov-2026 | baja | candidata | Solo se vio el resumen (Consensus), y es anterior a 2023. El 15–25 % que se repite en la web sale de blogs sin fuente. **No hay fuente seria verificada.** |
| DEV-08 | Mantenimiento anual en SaaS (benchmark de proveedor) | 21–26 | % del costo de construcción | Wavect (blog, 24 SaaS de la región DACH) | — | 15-nov-2026 | baja | candidata | Visto solo en el resultado de búsqueda; es un blog de proveedor. |

## 3. Supervivencia, fracaso y churn

| Código | Concepto | Valor | Unidad | Fuente | Página | Consulta | Confianza | Estado | Nota |
|---|---|---|---|---|---|---|---|---|---|
| EMP-01 | Actividad emprendedora temprana (TEA), Ecuador 2025 | 29,63 (2024: 33,37) | % de adultos de 18–64 años | (Amaya et al., 2026) | p. 24, tabla 5 | 15-nov-2026 | alta | verificada | 1.º en Latinoamérica, 2.º en el mundo. |
| EMP-02 | Tasa de cierre de negocios, Ecuador | 9,09 (2025); 13,51 (2024); 9,75 (2023) | % de adultos | (Amaya et al., 2026) | p. 25, figura 11 | 15-nov-2026 | alta | verificada | Negocios cerrados en los últimos 12 meses. |
| EMP-03 | Negocios establecidos (más de 3,5 años), Ecuador 2025 | 6,52 (región: 7,63) | % de adultos | (Amaya et al., 2026) | p. 26, tabla 7 | 15-nov-2026 | alta | verificada | 13,26 % en 2024. Muchos nacen, pocos se consolidan. |
| EMP-04 | Motivos de cierre, Ecuador 2025 | No rentable 27,71; personales 23,41; venta 12,77; financiamiento 12,51; otra oportunidad 9,47; burocracia 2,26 | % de los cierres | (Amaya et al., 2026) | p. 26, tabla 6 | 15-nov-2026 | alta | verificada | **El texto de la p. 25 da otras cifras** (rentabilidad 24,07 %; delincuencia y extorsión 13,12 %). Citar la tabla y anotar la diferencia. |
| EMP-05 | Supervivencia de establecimientos nuevos, EE. UU. (cohorte mar-2021) | 79,1 al año 1; 47,2 al año 5 | % | (BLS, 2026) | tabla 7 | 15-nov-2026 | alta | verificada | Cohorte 2019: 79,2 y 51,5. Es EE. UU.; Ecuador no publica una serie equivalente (no se encontró). |
| EMP-06 | Motivos de cierre de startups con capital de riesgo (desde 2023) | Sin capital 70; mal encaje producto-mercado 43; momento o entorno 29; economía unitaria 19 | % de 385 casos (respuesta múltiple) | (CB Insights, 2026) | p. web | 15-nov-2026 | media | verificada | Startups de EE. UU.; útil para los riesgos, no para las tasas. |
| EMP-07 | Churn mensual de SaaS para pymes | 3–7 | % mensual | Blogs (UserJot, Focus Digital y otros) | — | 15-nov-2026 | baja | candidata | Sin fuente primaria. Recurly (julio 2026) publica 3,21–3,44 % para servicios B2B, pero la página dice «anual» y eso no cuadra: revisar a mano. ChartMogul no se pudo revisar. |

## 4. Sector construcción

| Código | Concepto | Valor | Unidad | Fuente | Página | Consulta | Confianza | Estado | Nota |
|---|---|---|---|---|---|---|---|---|---|
| CON-01 | Empresas de construcción en Ecuador (universo REEM 2025) | 31.798 (2,64 % del total) | empresas | (INEC, 2026b) | tabulados, cuadro 1.1.7 | 15-nov-2026 | alta | verificada | Incluye RIMPE y personas naturales. Datos provisionales. |
| CON-02 | Constructoras con ventas y empleo (actividades productivas, 2025) | 5.382 (6,24 %) | empresas | (INEC, 2026b) | tabulados, cuadro 2.1.6 | 15-nov-2026 | alta | verificada | Mercado más realista para TEAMSLASH. No se halló el cruce con Pichincha. |
| CON-03 | Microempresas en el total de empresas | 93 | % | (INEC, 2026b) | boletín, p. 9 | 15-nov-2026 | alta | verificada | Todas las ramas; 1.204.276 empresas en 2025. Pichincha: 328.591 (27,3 %). |
| CON-04 | Participación de la construcción en las ventas nacionales (2024) | 2,4 | % | (INEC, 2026b) | boletín, p. 10 | 15-nov-2026 | alta | verificada | El sector con menos ventas. |
| CON-05 | Crecimiento del PIB de la construcción | 2023: −1,7; 2024: −7,9; 2025: +2,7 | % anual | (Banco Central del Ecuador, 2026) | pp. 22–23 | 12-oct-2026 | alta | verificada | Ya estaba en `bce_2026` (no se repitió). Peso en el PIB 2025: 4,1 %. |
| CON-06 | Margen neto, Engineering/Construction, mercados emergentes | 2,35 | % de las ventas | (Damodaran, 2026b) | hoja Industry Averages, fila 39 | 15-nov-2026 | media | verificada | 999 empresas cotizadas. Margen bruto 11,88 %; operativo antes de impuestos 4,40 %. |
| CON-07 | Margen operativo antes de impuestos, Homebuilding, emergentes | 10,69 (neto 6,48; bruto 24,40) | % de las ventas | (Damodaran, 2026b) | fila 51 | 15-nov-2026 | media | verificada | Lo más cercano al «10 %» actual. |
| CON-08 | Margen de constructoras ecuatorianas (Supercías, CIIU F) | — | — | — | — | — | — | no encontrada | No se llegó a los estados financieros de Supercías: para que Víctor lo abra a mano. |

## 5. Competencia con WhatsApp

| Código | Concepto | Valor | Unidad | Fuente | Página | Consulta | Confianza | Estado | Nota |
|---|---|---|---|---|---|---|---|---|---|
| COM-01 | Leadsales Básico | 97 (anual: 77,60) | USD/mes por empresa, 3 usuarios | (Leadsales, s. f.) | p. web | 15-nov-2026 | media | verificada | Profesional 133 (4 usuarios); Avanzado 247 (5). Usuario adicional con precio no publicado. |
| COM-02 | Callbell Chat multiagente | 14 (Plus: 18) | EUR por agente al mes | (Callbell, s. f.) | p. web | 15-nov-2026 | media | verificada | + cuenta de WhatsApp desde 20 €/mes; campañas 0,02 €/contacto; tarifas de Meta aparte. |
| COM-03 | Kommo (amoCRM) | 20 / 30 / 45 (6 meses); 16,67 / 25 / 37,50 (1 año) | USD por usuario al mes | (Kommo, s. f.) | p. web | 25-oct-2026 | media | verificada | Ya estaba en `kommo_sf`. |
| COM-04 | Treble | — | — | treble.ai/pricing | — | 15-nov-2026 | — | no verificable | Precios detrás de contraseña. |
| COM-05 | CRM ecuatoriano para constructoras con precio público | — | — | — | — | 15-nov-2026 | — | no encontrado | Solo aparecen extranjeros (Multifox, de Colombia; SINCO). Ninguno publica precios para Ecuador. |

## 6. Tasa de descuento

| Código | Concepto | Valor | Unidad | Fuente | Página | Consulta | Confianza | Estado | Nota |
|---|---|---|---|---|---|---|---|---|---|
| TAS-01 | Prima de riesgo país, Ecuador (ene-2026) | 12,95 | % | (Damodaran, 2026) | tabla, fila Ecuador | 15-nov-2026 | alta | verificada | Calificación Caa3; diferencial de default 8,50 %. |
| TAS-02 | Prima de riesgo de las acciones total, Ecuador | 17,18 | % | (Damodaran, 2026) | ídem | 15-nov-2026 | alta | verificada | Mercado maduro: 4,23 %. Colombia 7,08 %; Perú 6,30 %. |
| TAS-03 | Riesgo país (EMBI), Ecuador, 2-nov-2026 | 569 | puntos básicos | (Mise, 2026) | p. web | 15-nov-2026 | baja | verificada | Medio secundario; confirmar con el BCE. Volátil: la prensa habló de 378 en junio de 2026 (no verificado). |
| TAS-04 | Tasa libre de riesgo (bono del Tesoro de EE. UU. a 10 años) | — | % | — | — | — | — | pendiente | No se buscó; hace falta para la fórmula de la TMAR. |

## (i) No se pudo verificar: para que Víctor lo abra a mano

1. **Código del Trabajo con la reforma del 9-abr-2026** (copia del SERCOP; el servidor no respondió): https://portal.compraspublicas.gob.ec/sercop/wp-content/uploads/2026/08/CODIGO-DEL-TRABAJO.pdf. Hay que ver si cambiaron los arts. 69, 97, 111, 113 o 196.
2. **Reglamento de la LRTI vigente (reforma de noviembre de 2025)**, art. 28 (depreciación 33 %): https://www.dspace.espol.edu.ec/bitstream/123456789/55935/3/ (el enlace devolvió una página, no el PDF).
3. **Riesgo país oficial del BCE** (serie diaria): https://www.bce.fin.ec/ (la portada no muestra la cifra).
4. **IVA 15 %, Decreto Ejecutivo 198 y Decreto 470**: página del SRI sobre el IVA (https://www.sri.gob.ec/) o el Registro Oficial 520 del 18-mar-2024.
5. **Resolución NAC-DGERCGC26-00000009** (retenciones 2026), fuente primaria de TRI-05 a TRI-07: https://www.sri.gob.ec/ (normativa).
6. **Supercías, estados financieros por CIIU F (construcción)**, para el margen real de las constructoras ecuatorianas: https://appscvsmovil.supercias.gob.ec/ranking/ (portal de información del sector societario).
7. **Salarios mínimos sectoriales 2026 del Ministerio del Trabajo** (¿hay rama de TI?): https://www.trabajo.gob.ec/
8. **Computrabajo y Paylab, salario de programador en Ecuador**: https://ec.computrabajo.com/salarios/desarrollador-de-software y https://www.paylab.com/ec/salaryinfo/information-technology/programmer (llegaron vacías a la lectura automática).
9. **Recurly, churn por industria** (ver si es mensual o anual): https://recurly.com/research/churn-rate-benchmarks/
10. **Honorarios de un contador para una SAS pequeña en Quito**: no hay fuente publicada; hay que pedir 2–3 cotizaciones.

## (ii) Contradicciones con las cifras que hoy usamos

| Cifra actual | Lo que dicen las fuentes | Efecto |
|---|---|---|
| Sueldo de desarrollo USD 1.000/mes | Lo que **piden** los candidatos de TI en Ecuador: USD 579 (junior) y 1.084 (semi-senior) (Ekos Negocios, 2025). Talently (2026): 1.350 (junior) y 2.622 (semi-senior). | El 1.000 es defendible para un semi-senior local, **pero es sueldo, no costo**: con IESS, SECAP/IECE, décimos, vacaciones y fondo de reserva cuesta ≈ USD 1.287 el año 1 y ≈ 1.370 desde el año 2. |
| Tarifa de independiente USD 15/h | Lemon.io (2026): USD 34/h (nivel medio) y 45/h (senior) para ecuatorianos que trabajan con clientes extranjeros; excluye juniors. | USD 15/h solo vale para un junior local; **no hay fuente verificada del mercado local**. Se recomienda usar 15 como escenario bajo y 34 como alto. |
| Contador USD 80–100/mes | No se encontró ninguna fuente ecuatoriana con precios. | Sigue siendo un **supuesto**: hay que cotizar. |
| Aporte IESS 11,15 % | Correcto como aporte patronal (IESS, 2014; Farfán, 2025), pero el empleador paga además **1 % de SECAP e IECE** (González, 2026b): **12,15 %**. | Sube el costo laboral 1 punto. Además faltan los décimos, las vacaciones y el fondo de reserva. |
| Impuesto a la renta (25 %) | 25 % en el régimen general (Mora, 2026). Una SAS nueva con ingresos ≤ USD 300.000 **podría ir al RIMPE** y pagar 1–2 % sobre ingresos (SRI, s. f.), salvo que su actividad se tome como «profesional». | Puede cambiar mucho la utilidad neta: hay que decidir el régimen con un contador. El 15 % de utilidades **no aplica** si la SAS no tiene empleados. |
| Margen de obra 10 % | Constructoras de mercados emergentes: margen neto 2,35 % y bruto 11,88 %; vivienda (homebuilding): operativo 10,69 % y neto 6,48 % (Damodaran, 2026b). | Si el 10 % es margen neto, **está alto**; como margen de contribución u operativo de vivienda, cabe. Hay que decir qué margen es y usar 2–6 % neto en el escenario pesimista. |
| TMAR 12 % (base) y 15 % (pesimista) | La prima de riesgo de las acciones de Ecuador es 17,18 % (Damodaran, 2026), y el riesgo país 569 pb (Mise, 2026). | **La TMAR del 12 % no se sostiene con CAPM**: solo la prima supera el 17 %. Hay que justificar otra tasa (p. ej., tasa activa PYMES del BCE de 8,56–9,87 % más una prima) o subirla. |

## (iii) Conclusión: qué cifras cambian el modelo

1. **Costo laboral:** el empleado no cuesta su sueldo: cuesta ≈ 29 % más el año 1 y ≈ 37 % más desde el año 2 (12,15 % de IESS más 1 % de SECAP e IECE, décimos, vacaciones y fondo de reserva).
2. **Régimen tributario:** RIMPE frente a régimen general es la decisión de más peso. Con el RIMPE, el impuesto baja de 25 % de la utilidad a 1–2 % de los ingresos, pero hay que confirmar que el software no cuenta como «actividad profesional».
3. **TMAR:** con la prima de Damodaran (17,18 %), la tasa de 12 % queda corta. Si se mantiene, hay que justificarla con el costo de la deuda (BCE) y no con CAPM.
4. **Margen de obra:** el 10 % es optimista como margen neto (en emergentes es 2–3 %). Esto pesa en el argumento de «salvar 3 obras al año».
5. **Proyección «real»:** en Ecuador cierra cada año el 9–13 % de los adultos con negocio y solo el 6,5 % llega a «establecido» (Amaya et al., 2026). En EE. UU., la mitad de los negocios nuevos sigue viva a los 5 años (BLS, 2026). El modelo debería incluir un escenario de cierre o de pérdida del cliente. Falta un churn de SaaS con fuente primaria.

## Fichas creadas el 15-nov-2026 (21)

- Normativa: `ct_2005`, `iess_2014`, `sri_sf`, `sri_2015`, `nms_2026`.
- Costos_Viabilidad: `farfan_2025`, `gonzalez_2026b`, `mora_2026`, `damodaran_2026`, `damodaran_2026b`, `mise_2026`, `talently_2026`, `ccq_2025`, `ekos_2025`, `lemon_2026`, `leadsales_sf`, `callbell_sf`.
- Contexto: `cbinsights_2026`, `bls_2026`, `amaya_2026`, `inec_2026b`.
- Se reutilizaron (no se repitieron): `ministerio_2026`, `bce_2026`, `bce_2026b`, `kommo_sf`.
