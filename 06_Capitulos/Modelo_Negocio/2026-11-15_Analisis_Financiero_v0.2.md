---
titulo: "Análisis financiero: un solo cliente, dos planes"
version: v0.2
fecha: 2026-11-15
autor_borrador: "Claude; Víctor revisa y aprueba"
base: "Modelo financiero v0.2 (2026-11-15_Modelo_Financiero_v0.2.xlsx) · datos reales de los frentes A1 y A2 del 15-nov (fichas en 02_Fuentes) · caso de negocio v0.1"
reemplaza: "Al análisis financiero v0.1 (10-nov) y, para Torvesa, al estudio de costos v0.3. El estudio de costos v0.3 queda para el escalamiento por tipo de empresa"
marcadores: "FALTA-DATO 8 · FALTA-FUENTE 2 · VERIFICAR 4 · DECIDIR-VÍCTOR 4"
tags: [finanzas, van, tir, punto-equilibrio, estandar, premium, sprint5]
---

# Análisis financiero v0.2

## Resumen

> [!warning] Qué es dato y qué no
> Los **costos, los precios de los proveedores, la ley laboral y tributaria, la tasa de descuento y los márgenes del sector** salen de fuentes verificadas: el 71 % de las entradas que dependen de nosotros. Lo que **Torvesa** tiene que entregar (solicitudes al mes, clientes perdidos, valor de una obra, sueldos) **sigue siendo supuesto**: solo el 6 % es dato. Ese es el 20 % que falta investigar, y depende de la empresa.

**La pregunta:** ¿le conviene a TEAMSLASH levantar y mantener el sistema para **un solo cliente**, Torvesa? ¿Le conviene a Torvesa pagarlo?

**La respuesta, en el escenario base:**

| | Plan Estándar | Plan Premium |
|---|---|---|
| Qué incluye | Primer contacto garantizado + memoria comercial (bóveda) | Lo mismo + asistente de IA para borradores de cotización |
| Precio al mes, sin IVA | USD 175 | USD 275 |
| Implementación (una vez) | USD 222 | USD 311 |
| ¿Devuelve las horas ya invertidas? | No | Sí, en 36 meses |
| VAN de TEAMSLASH a 3 años | Negativo (−USD 1.153) | **USD 427** |
| TIR | Negativa | 26 % (TMAR 15 %) |
| Recuperación de la inversión | Más de 3 años | Unos 25 meses |
| Relación beneficio/costo | 0,79 | 1,03 |
| VAN para Torvesa | USD 13.081 | **USD 13.618** |
| Obras al año que pagan el sistema | 1,2 | 1,9 |

**Tres conclusiones:**
1. **Con un solo cliente, solo el Premium hace viable el proyecto**, y por poco: beneficio/costo de 1,03. El Estándar cubre la operación, pero no devuelve las 200 horas que ya pusieron Víctor y Diego.
2. **A Torvesa le conviene**, pero por las obras que recupera, no por el tiempo que ahorra. Para una constructora pequeña típica de Pichincha, el sistema costaría el **56 % de su utilidad neta anual** (1 % de sus ventas). El argumento de venta es: «se paga con 2 obras al año que hoy se pierden por no contestar a tiempo».
3. **Los fundadores cobran poco:** unos USD 77 al mes cada uno, por 7 horas de trabajo al mes entre los dos. Eso es USD 14,53 por hora de trabajo, más que la tarifa de referencia de USD 9,26. Es un ingreso extra, no un sueldo.

## 1. Cómo está armado el Excel

El libro sigue el orden de un estudio financiero de proyectos. Cualquier persona de contabilidad lo reconoce:

| Hoja | Qué tiene | Cómo se lee |
|---|---|---|
| Portada | Índice con enlaces, colores, cómo está armado | Empezar aquí |
| Panel | Dos listas desplegables: escenario (pesimista, base, optimista) y plan (Estándar, Premium). Debajo, los resultados | Cambiar solo las dos celdas amarillas |
| Supuestos | Las 63 entradas, cada una con qué significa, valor en cada escenario, **tipo** (DATO, SUPUESTO o DECISIÓN), fuente y qué investigar | La única hoja con números escritos a mano |
| 1 Inversión | Inversión inicial (año 0) y de dónde sale la plata | El trabajo ya hecho es un aporte de los socios |
| 2 Costos | Costo del mes por plan, y por hora, semana, año y solicitud | Lo de «la salchipapa» |
| 3 Precio | Costo + margen = precio; comparación con 6 competidores y con el beneficio de Torvesa | Rojo si el precio se lleva más del 25 % del beneficio |
| 4 Ingresos | Presupuesto de ingresos, años 1 a 3 | Un solo cliente |
| 5 Estado de resultados | Ingresos − costo del servicio − gastos − amortización − participación − impuesto | Estructura estándar |
| 6 Flujo de caja | Utilidad + amortización − inversión + capital de trabajo; y lo que reciben los fundadores | Año 0 a año 3 |
| 7 Evaluación | VAN, TIR, periodo de recuperación, beneficio/costo, punto de equilibrio | Cada indicador se lee solo: «conviene» o «no conviene» |
| 8 Torvesa | Beneficio mensual, flujo a 3 años y peso del sistema para una constructora real | Datos reales del sector al final |
| 9 Escenarios | Los 3 escenarios en los 2 planes | Foto del 15-nov |
| 10 Escalamiento | De 1 a 20 empresas: cómo baja el costo por empresa | Va al final |
| Glosario y Fuentes | Términos en palabras simples; 30 referencias con su ficha | |

**Para que se entienda sin explicarlo:**
- cada hoja empieza con «Para qué sirve» y «Cómo se lee»;
- cada fila tiene una columna «Qué significa»;
- al pasar el mouse sobre los encabezados aparece qué es cada columna;
- las fórmulas usan nombres, no celdas: por ejemplo, el mantenimiento es `=horas_mant_std*tarifa_hora`, no `=Supuestos!H40*Supuestos!H38`.

## 2. Qué cambió con los datos reales

| Supuesto | Antes (v0.1 y v0.3) | Ahora (v0.2) | Fuente |
|---|---|---|---|
| Aporte patronal | 11,15 % | **12,15 %** (con SECAP e IECE) | IESS (2014, p. 1); González (2026b) |
| Hora de trabajo de los fundadores | USD 8,50–15, supuesta | **USD 9,26**, calculada desde el sueldo de un desarrollador semi-senior (USD 1.084) con las cargas de ley | Ekos Negocios (2025); Código del Trabajo (2005) |
| TMAR pesimista | 15 % | **17,18 %** | Prima de riesgo de Ecuador (Damodaran, 2026) |
| Margen de Torvesa por obra | 8 %, 10 % y 12 %, supuestos | **2,35 %, 11,88 % y 24,40 %** | Damodaran (2026b): margen neto y bruto de constructoras de mercados emergentes, y bruto de vivienda |
| Competencia | 4 CRM | + Kommo y Leadsales, que trabajan con WhatsApp | Kommo (s. f.); Leadsales (s. f.) |
| Referencia de una constructora pequeña | No había | Ventas de USD 320.229 y margen neto de 1,89 % (mediana 2025, Pichincha) | Superintendencia de Compañías, Valores y Seguros (2026a) |

**Dos cifras que contradicen lo que teníamos, y se dicen:**
- **La TMAR del 12 % no se sostiene.** Solo la prima de riesgo de Ecuador ya es 17,18 % (Damodaran, 2026). Por eso el escenario base pasa a 15 %, la misma TMAR del Informe Final (p. 28). Falta la tasa libre de riesgo para armar la TMAR completa [FALTA-FUENTE: bono del Tesoro de EE. UU. a 10 años].
- **El 10 % de margen de obra está alto si es margen neto.** Las constructoras pequeñas de Pichincha ganan 1,89 % neto. El modelo usa el margen **bruto** (11,88 %) en el escenario base, porque una obra extra no aumenta los costos fijos de la empresa. El pesimista usa el margen neto (2,35 %), y ahí el sistema no se paga: harían falta 25 obras al año.

## 3. Cómo se formó el precio

| Concepto, al mes | Estándar | Premium |
|---|---|---|
| Servicios en la nube (servidor, página, bóveda, WhatsApp, IA), con IVA | USD 80,50 | USD 82,74 |
| Honorarios de mantenimiento (4 y 7 horas × USD 9,26) | USD 37,04 | USD 64,82 |
| Recuperación del levantamiento (USD 1.852 ÷ 36) | — | USD 51,44 |
| Gastos administrativos (firmas, dominio, herramienta de IA) | USD 26,84 | USD 26,84 |
| **Costo total** | **USD 144,38** | **USD 225,84** |
| Margen del 20 % | USD 28,88 | USD 45,17 |
| **Precio, redondeado a USD 5** | **USD 175** | **USD 275** |

- **Frente a la competencia:** el Estándar cuesta 1,7 veces y el Premium 2,7 veces el promedio de seis competidores. Hay dos razones. Ellos reparten sus costos entre miles de clientes. Y ninguno trae la bóveda, el asistente que cita los documentos ni el registro con huellas (matriz de herramientas v0.2, hoja «Por qué nosotros»). Con 20 empresas, el costo por empresa baja a USD 59 (hoja 10).
- **Frente a lo que gana Torvesa:** el Estándar se lleva el 23 % de su beneficio y el Premium el 31 %, por encima de la regla del 25 %. Lo que hace aceptable al Premium es que recupera la inversión de los fundadores.

[DECIDIR-VÍCTOR: margen del 20 %; si el levantamiento se recupera en 36 meses o en más, para bajar el Premium.]

## 4. Riesgo: qué dicen los datos sobre los negocios nuevos

- En Ecuador, el 9,1 % de los adultos cerró un negocio en 2025. El motivo más común fue que **no era rentable**: 27,7 % de los cierres (Amaya et al., 2026, pp. 25–26).
- En EE. UU., de cada 100 negocios nuevos, 79 siguen al año 1 y 47 al año 5 (U.S. Bureau of Labor Statistics, 2026).
- Las startups que cierran citan sobre todo la falta de capital (70 %) y el mal encaje con el mercado (43 %) (CB Insights, 2026).

**Por eso:** el modelo parte de un solo cliente y no de una proyección de ventas. El escalamiento va al final y con un techo de 20 empresas, que serían el 6 % de las 321 constructoras pequeñas de Pichincha.

## 5. Lo que pide la directora para que sea «dato real»

**Solo Torvesa lo puede dar** (Diego lo gestiona):
- [FALTA-DATO: formularios 101 del SRI de 2023 a 2025]: ventas, costos y utilidad reales. La empresa está en régimen general y obligada a llevar contabilidad (SRI, 2026), pero **no aparece en la Superintendencia de Compañías** (Superintendencia de Compañías, Valores y Seguros, 2026b): hay que preguntar qué tipo de sociedad es;
- [FALTA-DATO: solicitudes al mes, clientes perdidos y tasa de cierre]: muestra documental de 3 meses;
- [FALTA-DATO: valor promedio de una obra y sueldos de quienes atienden].

**Atención:** el SRI registra como actividad principal de Torvesa la **construcción de carreteras** (CIIU F4210), no la de edificios (SRI, 2026). Hay que confirmarlo con Diego. Si la tesis la presenta como constructora de vivienda, el Cap. I lo tiene que aclarar.

**Lo medimos nosotros:**
- [FALTA-DATO: horas reales invertidas en el levantamiento, del registro de contribuciones y del historial de Git]: hoy son 200 horas supuestas;
- [FALTA-DATO: horas por cotización y de búsqueda del historial, casos de prueba CP-01 y CP-02];
- [FALTA-DATO: factura real del servidor].

**Fuentes que faltan:** tasa libre de riesgo; tarifa de un contador; IVA del 15 % en el texto oficial [VERIFICAR: Decreto 198]; régimen tributario (RIMPE o general) para una SAS de servicios de software [VERIFICAR con un contador]; si el 15 % de participación aplica sin empleados [VERIFICAR]; mantenimiento anual de software como porcentaje del desarrollo [FALTA-FUENTE: solo hay un blog y un resumen].

**Decisiones de Víctor:**
- [DECIDIR-VÍCTOR: trabajar como independientes o como SAS desde el inicio];
- [DECIDIR-VÍCTOR: margen de TEAMSLASH];
- [DECIDIR-VÍCTOR: plazo de recuperación del levantamiento];
- [DECIDIR-VÍCTOR: precios por tipo de empresa, para el escalamiento (estudio de costos v0.3, hoja A5)].

## 6. Limitaciones

- Antes del impuesto personal de los fundadores; dólares de 2026, sin inflación.
- Un solo cliente durante los 3 años. No hay cobros por mejoras: si se venden, el resultado mejora.
- Ninguna cifra de Torvesa es real todavía.
- La hoja 9 es una foto: para ver otro caso en vivo, se cambia el Panel.

## Referencias

Amaya, A., Barriga, A., Espinoza, D., Coronel, K., Fernández, M. F., Espinosa, M. P. y Armas, R. (2026). *Global Entrepreneurship Monitor Ecuador 2025*. Ediloja. https://uees.edu.ec/wp-content/uploads/2026/05/GEM-2025.pdf

Bermeo, D., y Segura, V. (2026). *TEAMSLASH: Ecosistema digital de gestión de clientes para la Constructora Torvesa* [Informe final del proyecto integrador, Universidad Politécnica Salesiana].

CB Insights. (2026, 5 de marzo). *The top reasons startups fail*. https://www.cbinsights.com/research/report/startup-failure-reasons-top/

Código del Trabajo. Codificación n.º 2005-017. Registro Oficial Suplemento 167, 16 de diciembre de 2005.

Damodaran, A. (2026). *Country default spreads and risk premiums* [Conjunto de datos]. NYU Stern. https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html

Damodaran, A. (2026b). *Margins by sector: Emerging markets* [Conjunto de datos]. NYU Stern. https://pages.stern.nyu.edu/~adamodar/pc/datasets/marginemerg.xls

Ekos Negocios. (2025, 16 de junio). *El salario pretendido promedio por los hombres es USD 83 más alto que la aspiración salarial de las mujeres en Ecuador*. Ekos Negocios.

González, P. (2026b, 22 de abril). [Proyectos de ley sobre el financiamiento del SECAP con los aportes de los empleadores]. *Primicias*.

Instituto Ecuatoriano de Seguridad Social. (2014). *Tasas de aportación*. https://www.iess.gob.ec/documents/13718/54965/Tasasdeaportacion.pdf

Kommo. (s. f.). *Precios*. Recuperado el 25 de octubre de 2026.

Leadsales. (s. f.). *Precios*. Recuperado el 15 de noviembre de 2026, de https://leadsales.io/precios/

Servicio de Rentas Internas. (2026). *Consulta de RUC: 1792266424001 (Torvesa Constructora)* [Servicio público de consulta del catastro]. Recuperado el 15 de noviembre de 2026.

Superintendencia de Compañías, Valores y Seguros. (2026a). *Ranking empresarial 2023, 2024 y 2025* [Conjunto de datos]. https://appscvsmovil.supercias.gob.ec/ranking/reporte.html

Superintendencia de Compañías, Valores y Seguros. (2026b). *Portal de información: consulta de compañías* [Base de datos]. Recuperado el 15 de noviembre de 2026.

U.S. Bureau of Labor Statistics. (2026). *Business Employment Dynamics: Table 7. Survival of private sector establishments by opening year*. https://www.bls.gov/bdm/us_age_naics_00_table7.txt

*La lista completa, con las 30 fuentes del Excel, está en su hoja «Fuentes».*
