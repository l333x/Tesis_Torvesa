---
titulo: Análisis financiero y matriz de herramientas — texto para la viabilidad (Cap. IV/V)
version: v0.1
fecha: 2026-11-10
autor: Víctor Segura (revisa) · borrador de Claude
ia: Claude (Claude Code)
tareas: [S4-T08, S4-T10, S4-T12, S5-T01, S5-T03, S5-T05]
archivos: ["06_Capitulos/Modelo_Negocio/2026-11-10_Modelo_Financiero_v0.1.xlsx", "06_Capitulos/Modelo_Negocio/2026-11-10_Matriz_Herramientas_v0.1.xlsx"]
estado: propuesta; la aprueba Víctor
tags: [finanzas, van, tir, roi, capex, opex, matriz-herramientas, viabilidad, sprint5]
---

# Análisis financiero y matriz de herramientas v0.1

> [!warning] Con supuestos, no con datos de Torvesa
> Todas las cifras salen de los dos Excel. Los **precios son oficiales**, con su página y la fecha de consulta. Los **volúmenes, tasas y montos de Torvesa son SUPUESTOS**, porque la empresa todavía no entrega la línea base (P2-B) ni autoriza el campo.
>
> - No se usa el diagnóstico N = 30, que es simulado.
> - Del censo real n = 5 (Informe Final, p. 10) solo se toma el número de usuarios.
> - Los USD 15.000 por cliente perdido (Informe Final, p. 5) no tienen respaldo. Aquí son una hipótesis, y el escenario pesimista no cuenta ventas recuperadas.

## 1. Qué se calculó

| Pregunta | Dónde está |
|---|---|
| ¿Con qué plataforma conviene operar el sistema? | Matriz de herramientas, hojas `Puntuacion` y `Sensibilidad` |
| ¿Cuánto cuesta empezar (CAPEX) y cuánto cuesta al mes (OPEX)? | Modelo financiero, hojas `CAPEX` y `OPEX` |
| ¿Qué gana Torvesa? | Hoja `Beneficios` |
| ¿Vale la pena? (VAN, TIR, ROI, recuperación) | Hojas `Flujo`, `Escenarios` y `Resumen` |
| ¿Qué supuesto pesa más? | Hoja `Sensibilidad` (tornado) |

Los dos Excel tienen **fórmulas vivas**. Al cambiar un supuesto azul de la hoja `Supuestos`, todo se recalcula. Se recalcularon en Excel con **0 errores de fórmula**, y el VAN de la hoja de sensibilidad cuadra con el de la hoja `Flujo`.

## 2. CAPEX y OPEX desde el punto de vista de Torvesa

**La regla:** Torvesa no compra software, compra acceso. Por eso **toda suscripción en la nube es OPEX**: Railway, Vercel, Slack, Obsidian Sync, el asistente de IA y WhatsApp.

El Comité de Interpretaciones de las NIIF lo resolvió así en 2021. En un acuerdo SaaS, el cliente «often would not recognise an intangible asset» y reconoce la configuración como gasto «when it receives the configuration or customisation services» (IFRS Interpretations Committee, 2021, decisión de agenda sobre la NIC 38).

**Lo que sí es inversión inicial** (salida de caja del año 0):
- el desarrollo del código propio: la API, el registro con huellas y la sincronización con la bóveda. Este código lo controla Torvesa y **podría** reconocerse como intangible según la NIC 38;
- la capacitación, que contablemente es gasto [VERIFICAR-PÁG: NIC 38, párr. 69];
- una contingencia.

No hace falta comprar equipos: el personal ya tiene celular con datos (elicitación v0.1, §14.3, supuesto).

> [!note] CAPEX financiero frente a CAPEX contable
> En el VAN, «CAPEX» significa salida de caja inicial. En el balance, casi todo sería gasto, salvo el código propio. La clasificación contable la confirma un contador; el VAN no cambia, porque mira la caja.

**IVA.** Los servicios digitales del exterior pagan IVA con tarifa distinta de cero (Servicio de Rentas Internas [SRI], 2021, p. 1). La guía no dice el porcentaje: la tarifa general del 15 % desde el 1-abr-2024 todavía no está verificada en una fuente abierta [VERIFICAR-PÁG: Decreto Ejecutivo 198 y Circular NAC-DGECCGC24-00000002]. El modelo lo suma al OPEX, porque Torvesa lo paga si no lo recupera como crédito tributario.

### Tabla de precios (S4-T10, S4-T12)

| Servicio | Precio usado | Unidad | Página oficial | Consulta |
|---|---|---|---|---|
| Railway Pro (servidor y PostgreSQL) | 20 + uso | USD/mes por espacio | https://railway.com/pricing | 10-nov-2026 |
| Vercel Pro (página y formulario) | 20 | USD/mes por puesto | https://vercel.com/pricing | 10-nov-2026 |
| Slack Pro | 7,25 | USD/usuario/mes, anual | https://slack.com/pricing | 25-oct-2026 |
| Obsidian Sync | 4 | USD/usuario/mes, anual | https://obsidian.md/pricing | 21-oct-2026 |
| Claude Sonnet 5.5 | 2 / 10 | USD por millón de tokens (entrada / salida) | https://platform.claude.com/docs/en/about-claude/pricing | 25-oct-2026 |
| WhatsApp Business, mensaje de servicio (Ecuador) | 0,0113 (los primeros 1.000 al mes, gratis) | USD/mensaje | https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing | 25-oct-2026 |
| HubSpot Starter (lista) | 20 | USD/puesto/mes | https://www.hubspot.com/pricing/crm | 25-oct-2026 |
| Zoho CRM Standard | 12 | USD/usuario/mes, anual | https://www.zoho.com/es-xl/crm/zohocrm-pricing.html | 25-oct-2026 |
| Pipedrive Lite | 14 | USD/puesto/mes, anual | https://www.pipedrive.com/en/pricing | 25-oct-2026 |
| Bitrix24 Basic (5 usuarios) | 49 | USD/mes por empresa, anual | https://www.bitrix24.com/prices/ | 10-nov-2026 |
| Odoo Standard | 8,95 [VERIFICAR] | USD/usuario/mes, anual | https://www.odoo.com/pricing | 10-nov-2026 |
| Dynamics 365 Sales Professional / Enterprise | 65 / 105 | USD/usuario/mes, anual | https://www.microsoft.com/en-us/dynamics-365/products/sales/pricing | 10-nov-2026 |
| Amazon Q Business Lite / índice Starter | 3 / 0,14 por hora | USD/usuario/mes · USD/hora | https://aws.amazon.com/q/business/pricing/ | 10-nov-2026 |
| Bedrock, capacidad dedicada para un modelo ajustado | 23,50 por hora | USD/hora por unidad | https://aws.amazon.com/bedrock/pricing/ | 10-nov-2026 |
| Bedrock AgentCore Runtime | 0,0895 por vCPU-hora | uso | https://aws.amazon.com/bedrock/agentcore/pricing/ | 10-nov-2026 |
| Salario básico unificado 2026 | 482 | USD/mes | Ministerio del Trabajo (2026, p. 2) | 10-nov-2026 |
| Aporte patronal IESS | 11,15 % | del sueldo | IESS, Resolución C.D. 515 [VERIFICAR-PÁG] | 10-nov-2026 |
| Tasa activa máxima, productivo PYMES (nov-2026) | 9,87 % (referencial: 8,56 %) | anual | BCE, https://contenido.bce.fin.ec/documentos/Estadisticas/SectorMonFin/TasasInteres/Indice.htm | 10-nov-2026 |

**Fichas creadas el 10-nov en `02_Fuentes/Costos_Viabilidad/`** (12, solo de lo que se abrió y verificó): `ifric_2021`, `aws_sfa`, `aws_sfb`, `aws_sfc`, `aws_sfd`, `railway_sf`, `vercel_sf`, `bitrix24_sf`, `microsoft_sf`, `ministerio_2026`, `bce_2026b` y `sri_2021`.

**Sin ficha, y por eso no se citan todavía:**
- IESS, Resolución C.D. 515: solo se vio en resultados de búsqueda;
- Odoo: la página muestra dos precios;
- el Decreto Ejecutivo 198 y la circular del SRI sobre el 15 % de IVA;
- la NIC 38, párr. 69.

## 3. Resultados

**Tasa de descuento:**
- optimista: la tasa activa máxima PYMES del BCE (9,87 %);
- base: 12 % (esa tasa más unos 2 puntos por riesgo tecnológico, SUPUESTO);
- pesimista: 15 %, la misma TMAR del Informe Final (p. 28), para poder comparar.

**Horizonte:** 3 años. El primer año solo se logra una parte del beneficio (adopción: 50 %, 70 % u 85 %).

| Indicador | Pesimista | Base | Optimista |
|---|---|---|---|
| Inversión inicial (año 0) | USD 4.451 | USD 2.893 | USD 1.723 |
| OPEX anual (con IVA y soporte) | USD 3.066 | USD 2.213 (≈ USD 184 al mes) | USD 1.707 |
| Beneficio anual en régimen | USD 633 | USD 9.262 | USD 30.773 |
| — por ahorro de tiempo (B1 + B2) | USD 633 | USD 3.862 | USD 12.629 |
| — por obras recuperadas (B3) | USD 0 | USD 5.400 (3,6 obras al año) | USD 18.144 |
| **VAN** | **−USD 10.282** | **USD 11.557** | **USD 66.526** |
| **TIR** | No existe | 171 % | 1.436 % |
| **ROI a 3 años** | −88 % | 162 % | 1.182 % |
| **Recuperación** | Más de 3 años | 0,7 años (≈ 8 meses) | < 1 mes |
| VAN sin ventas recuperadas | −USD 10.282 | USD 33 | USD 23.778 |
| **Obras al año que pagan el sistema sin ningún ahorro de tiempo** | 9,7 | **2,6** | 1,2 |

### Cómo se lee

1. **En el escenario base, el sistema se paga.** El VAN es positivo y la inversión se recupera en unos 8 meses. La TIR es muy alta porque la inversión es chica (unos USD 2.900): con montos tan bajos, la TIR exagera. **Es mejor mirar el VAN y el umbral de obras.**
2. **El caso depende de recuperar clientes, no del ahorro de tiempo.** Sin ventas recuperadas, el VAN base es casi cero (USD 33): el ahorro de horas apenas cubre el costo.
3. **El argumento para la gerencia:** el sistema se paga solo si «salva» unas **3 obras al año**. Esto vale con el valor y el margen supuestos (USD 15.000 y 10 %), aunque no ahorre ni un minuto. Es una meta que Torvesa puede comparar con su propia experiencia: ¿cuántos clientes se van al año porque nadie les contestó a tiempo?
4. **El pesimista sale negativo, y eso se dice.** Si casi no llegan solicitudes (15 al mes), no se recupera ninguna obra y el ahorro de tiempo es mínimo, el sistema no se paga en 3 años. Para pagarlo haría falta salvar casi 10 obras de USD 8.000 al año, con un 8 % de margen.
5. **El optimista no es una promesa:** junta todos los supuestos favorables a la vez.

**Frase propuesta para el capítulo:**

> «Con los supuestos del escenario base, el sistema tiene un VAN de USD 11.557 a tres años, con una tasa del 12 %, y recupera la inversión en menos de un año. El resultado depende sobre todo de cuántos clientes deja de perder la empresa: basta con recuperar alrededor de tres obras al año para cubrir la inversión y la operación. Este umbral se contrastará con la línea base de Torvesa [FALTA-DATO: M3 y valor promedio de obra].»

### Sensibilidad (tornado, escenario base)

Se movió un supuesto a la vez a su valor pesimista y a su valor optimista. Del que más mueve el VAN al que menos:

| Orden | Supuesto | Rango del VAN |
|---|---|---|
| 1 | Reducción de la fuga con el sistema (P13) | USD 16.133 |
| 2 | Solicitudes nuevas por mes (P02) | USD 12.487 |
| 3 | Fuga antes del primer contacto (P12) | USD 8.643 |
| 4 | Valor promedio de una obra (P15) | USD 7.682 |
| 5 | Tasa de cierre (P14) | USD 5.762 |
| 6 | Horas por semana buscando historial (P06) | USD 4.716 |
| 7 | Sueldo de quien cotiza (P08) | USD 4.690 |
| … | Tasa de descuento (P18) y consultas al asistente (P20) | USD 1.363 y USD 65 (lo que menos pesa) |

**Lectura:**
- Los 5 supuestos que más pesan son de **ventas** (fuga, volumen, cierre y valor de la obra), y todos los tiene que dar Torvesa. Por eso la muestra documental (P2-B) es la ruta crítica también para las finanzas.
- El costo de la IA casi no importa: unos USD 2 al mes en el escenario base.

## 4. Matriz de decisión de herramientas (S4-T08)

Se comparan **11 alternativas** con **9 criterios ponderados**:

| Criterio | Peso |
|---|---|
| Costo total a 3 años | 20 |
| Datos y LOPDP | 20 |
| Adopción | 15 |
| Mala conexión en obra | 10 |
| WhatsApp y Slack | 10 |
| Escalabilidad | 10 |
| Dependencia del proveedor | 5 |
| Registro verificable | 5 |
| Español | 5 |

Cada peso tiene su justificación en la hoja `Criterios`, apoyada en el censo n = 5 y en la LOPDP:
- art. 56: transferencia a países con nivel adecuado (p. 46);
- art. 57: garantías adecuadas en un instrumento vinculante (p. 47).

El costo se puntúa con fórmula. Los demás criterios, con un puntaje de 1 a 5 y su evidencia, en la hoja `Evidencia`.

| Puesto | Alternativa | Puntaje (de 5) | TCO a 3 años |
|---|---|---|---|
| 1 | **Stack actual del prototipo** (Railway, Vercel, Slack, Obsidian, Claude) | **4,14** | USD 9.039 |
| 2 | El mismo stack con Gemini (Google) | 3,99 | USD 9.019 |
| 3 | Pipedrive Lite + captura actual | 3,55 | USD 9.529 |
| 4 | HubSpot Starter + captura | 3,52 | USD 10.771 |
| 5 | Zoho CRM + captura | 3,39 | USD 9.115 |
| 6 | Odoo + captura | 3,36 | USD 9.383 |
| 7 | AWS con RAG gestionado (Amazon Q Business) | 3,23 | USD 13.583 |
| 8 | Bitrix24 + captura | 3,15 | USD 8.959 |
| 9–10 | Dynamics 365 Professional / Enterprise | 3,09 / 2,99 | USD 21.286 / USD 29.866 |
| 11 | **AWS con modelo propio ajustado** | **2,06** | **USD 724.428** |

**Sensibilidad de los pesos:** se probaron 6 juegos de pesos:
- propuesta;
- pesos iguales;
- costo primero;
- LOPDP primero;
- adopción primero;
- escalar a otras constructoras.

El stack actual gana en 5. Solo en «escalar a otras constructoras» lo pasa su variante con Gemini, por 0,06 puntos: la diferencia entre los dos es solo el modelo de IA. **La decisión es robusta.**

**Lo que no dice el número:**
- Los CRM SaaS cubren el embudo de ventas, pero no la memoria comercial (la bóveda), ni el asistente que cita los documentos de la empresa, ni el registro verificable (M5). Por eso se les suma la captura actual.
- El stack actual tiene un pendiente de seguridad: la clave de la API está visible en la página pública. Hay que separarla antes de usar datos reales (hallazgo del 10-nov). Eso ya le resta un punto en LOPDP.

### ¿Y las IA autónomas de AWS para entrenar modelos?

**Hoy no conviene, y se puede explicar con evidencia** (hoja `Ruta_AWS`):

1. **No hay con qué entrenar.** Las cotizaciones y conversaciones de Torvesa están en celulares y cuadernos (AS-IS v0.1).
2. **AWS misma recomienda empezar por RAG:** «If you need to build a question-answering solution that references your custom documents, then we recommend that you start from a RAG-based approach» (Amazon Web Services [AWS], s. f.-d).
   - El ajuste fino «might require a data scientist».
   - Sus respuestas no citan la fuente.
   - Tiene «increased risk of hallucination».
   - El diseño exige citar los documentos (RQ-11) y revisión humana (RQ-12): eso es RAG (Lewis et al., 2020).
3. **El costo no cierra.** Servir un modelo ajustado en Bedrock pide capacidad dedicada a USD 23,50 la hora: unos **USD 17.155 al mes**, más de 80 veces el OPEX del stack actual.
4. **LOPDP.** Entrenar con conversaciones de clientes mete datos personales dentro del modelo, lo que choca con la conservación limitada (art. 10 i, p. 18).

**Cuándo sí** (disparadores propuestos; son SUPUESTO):
- cuando el sistema se ofrezca a varias constructoras (anexo SaaS, D7);
- cuando la bóveda pase de unos 20.000 documentos (el límite de una unidad del índice Starter de Q Business);
- cuando haya un equipo técnico que mantenga AWS;
- cuando exista un historial digitalizado y anonimizado.

Ahí la ruta es **AWS con RAG gestionado** (puesto 7, TCO de USD 13.583), no el modelo propio. Los agentes autónomos (AgentCore) se usarían solo para tareas sin riesgo: recordatorios, el reporte de los lunes y reindexar la bóveda. Ningún borrador sale sin aprobación humana (RQ-12).

## 5. Lo que solo Torvesa puede dar (marcadores)

- [FALTA-DATO: solicitudes nuevas por mes — P2-B]: es el supuesto n.º 2 del tornado.
- [FALTA-DATO: M3 — fuga antes del primer contacto, línea base]: n.º 3.
- [FALTA-DATO: valor promedio de una obra y margen de contribución]: n.º 4 y n.º 8.
- [FALTA-DATO: tasa de cierre de solicitudes]: n.º 5.
- [FALTA-DATO: sueldos de quien cotiza y atiende].
- [FALTA-DATO: cuántas personas usarán el sistema].
- [FALTA-DATO: M2 — horas por cotización (CP-01)] y [FALTA-DATO: M4 — tiempo buscando historial (CP-02)]: los ejecutan Víctor y Diego.

Además, para pasar de supuesto a fuente:
- [FALTA-FUENTE: Código del Trabajo, arts. 47 y fondos de reserva];
- [FALTA-FUENTE: tarifa de mercado de una hora de desarrollo];
- [VERIFICAR-PÁG: IESS C.D. 515; NIC 38, párr. 69; Decreto 198 y circular del SRI];
- [VERIFICAR: precio de Odoo en el navegador; factura real de Railway (consumo); DPA de Railway, Vercel, Bitrix24 y Microsoft].

**Recuento de esta versión:**

| Marcador | Cantidad |
|---|---|
| FALTA-DATO | 9 |
| FALTA-FUENTE | 3 |
| VERIFICAR-PÁG | 4 |
| VERIFICAR | 5 |

## 6. Limitaciones

- El análisis es antes del impuesto a la renta, en dólares constantes, a 3 años y sin valor residual.
- Los precios cambian: hay que volver a consultarlos antes de cerrar el capítulo.
- Los puntajes cualitativos de la matriz son una propuesta del equipo y se pueden llevar a la tutora.
- El ahorro de tiempo del asistente (M2) es una hipótesis hasta que se ejecute CP-01 (S8-04).

## Referencias

Solo están las fuentes abiertas y verificadas el 10-nov-2026 que tienen ficha. Las demás fuentes del texto (fichas del 21 y 25-oct, LOPDP, Lewis et al., Salesforce) ya están en la lista general de la tesis. El informe del BCE que ya se cita en la tesis pasa a ser 2026a.

Amazon Web Services. (s. f.-a). *Amazon Bedrock AgentCore pricing*. Recuperado el 10 de noviembre de 2026, de https://aws.amazon.com/bedrock/agentcore/pricing/

Amazon Web Services. (s. f.-b). *Amazon Bedrock pricing*. Recuperado el 10 de noviembre de 2026, de https://aws.amazon.com/bedrock/pricing/

Amazon Web Services. (s. f.-c). *Amazon Q Business pricing*. Recuperado el 10 de noviembre de 2026, de https://aws.amazon.com/q/business/pricing/

Amazon Web Services. (s. f.-d). *Comparing Retrieval Augmented Generation and fine-tuning*. AWS Prescriptive Guidance. Recuperado el 10 de noviembre de 2026, de https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/rag-vs-fine-tuning.html

Banco Central del Ecuador. (2026b). *Tasas de interés activas efectivas máximas y referenciales, noviembre 2026*. Recuperado el 10 de noviembre de 2026, de https://contenido.bce.fin.ec/documentos/Estadisticas/SectorMonFin/TasasInteres/Indice.htm

Bitrix24. (s. f.). *Bitrix24 plans and pricing*. Recuperado el 10 de noviembre de 2026, de https://www.bitrix24.com/prices/

IFRS Interpretations Committee. (2021, marzo). *IFRIC Update March 2021*. IFRS Foundation. https://www.ifrs.org/content/ifrs/home/news-and-events/updates/ifric/2021/ifric-update-march-2021.html

Microsoft. (s. f.). *Dynamics 365 Sales pricing*. Recuperado el 10 de noviembre de 2026, de https://www.microsoft.com/en-us/dynamics-365/products/sales/pricing

Ministerio del Trabajo. (2026). *Informe de gestión, rendición de cuentas, acciones relevantes: Subsecretaría de Empleo y Salarios. Periodo: enero a diciembre 2025*. https://www.trabajo.gob.ec/wp-content/uploads/2026/03/Anexo-Fijacion-Salario-Basico-Planta-Central-2025.pdf

Railway. (s. f.). *Pricing*. Recuperado el 10 de noviembre de 2026, de https://railway.com/pricing

Servicio de Rentas Internas. (2021). *Guía para la interpretación de las directrices del catastro de prestadores de servicios digitales para los intermediarios que actúen como agentes de retención*. https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/b5a61f8e-f8c8-4dc1-9b30-365f2d16b4b6/Gu%C3%ADa%20para%20Implementaci%C3%B3n%20del%20Catastro.pdf

Vercel. (s. f.). *Vercel pricing*. Recuperado el 10 de noviembre de 2026, de https://vercel.com/pricing
