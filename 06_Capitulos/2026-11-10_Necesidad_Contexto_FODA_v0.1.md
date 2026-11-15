---
titulo: "La necesidad de Torvesa: contexto de Ecuador 2023–2026 y análisis FODA"
version: v0.1
fecha: 2026-11-10
autor_borrador: "Claude Opus 5.5 (frente B); Víctor revisa"
base: "02_Fuentes (bce_2026, primicias_2025a, tapia_2024, inec_2026, datareportal_2026, salesforce_2022, salesforce_2024, revenuehero_2024, oecd_2025a, perezcampdesuner_2025, primicias_2026, stark_2024, cepal_2025, multitrabajos_2024) · censo n = 5 del Informe Final (p. 10) · 00_Inbox/2026-11-08_respuesta_Diego_censo_TEAMSLASH.md · 07_Flujos_Diseno/2026-11-15_Resumen_Prueba_Concepto.md · Cap. IV v0.1"
marcadores: "FALTA-FUENTE 4 · FALTA-DATO 3"
uso: "Insumo para el Cap. I (contexto), el Cap. IV (diagnóstico), el pitch y la guía de negociación"
tags: [necesidad, contexto, ecuador, foda, sprint5]
---

# La necesidad de Torvesa: contexto de Ecuador y FODA

> [!summary] En tres frases
> 1. La construcción en Ecuador salió de dos años de caída (−1,7 % en 2023 y −7,9 % en 2024) y volvió a crecer en 2025 (+2,7 %). En un mercado que recién se recupera, **cada cliente que se pierde por demora pesa más**.
> 2. En Torvesa, 4 de cada 5 personas de la gerencia y la operación dicen que el cliente no debería esperar más de 15 minutos. Pero 3 de cada 5 revisan los mensajes cada 3 o 4 horas, o solo al llegar a casa. **Esa brecha es el problema.**
> 3. El sistema ya funciona como prueba de concepto con datos ficticios. Lo que falta es la autorización de Torvesa para validarlo con su equipo.

## 1. Qué cambió en Ecuador entre 2023 y 2026

### 1.1 La construcción cayó dos años y se está recuperando

| Año | Crecimiento de la construcción | Crecimiento del PIB |
|---|---|---|
| 2022 | +7,5 % | +5,9 % |
| 2023 | −1,7 % | +1,8 % |
| 2024 | **−7,9 %** | −1,9 % (provisional) |
| 2025 | +2,7 % | +3,7 % (preliminar) |

*Nota.* Banco Central del Ecuador (2026, tabla 1, p. 22).

- En 2025 la construcción pesa el 4,1 % del PIB (Banco Central del Ecuador, 2026, p. 22) y concentra el 6,4 % del empleo del país (Banco Central del Ecuador, 2026, figura 42, p. 45, con datos del INEC).
- La recuperación de 2025 se apoyó en más producción de cemento, más importación de materiales y más empleo en el sector (Banco Central del Ecuador, 2026, p. 23).
- El empleo adecuado subió del 33,0 % al 37,1 % entre diciembre de 2024 y diciembre de 2025 (Instituto Nacional de Estadística y Censos [INEC], 2026).

**Qué significa para Torvesa:** la demanda vuelve, pero después de dos años malos. Las constructoras que respondan primero se quedarán con los clientes que reaparecen.

### 1.2 La crisis eléctrica de 2024

- En septiembre y octubre de 2024 hubo cortes de luz de hasta 12 horas diarias en algunos sectores (Tapia, 2024).
- Las cámaras industriales estimaron unos USD 12 millones de pérdida por cada hora sin luz. Es una estimación gremial, no una cifra oficial (Tapia, 2024).
- Según el BCE, las pérdidas por los cortes llegaron a USD 1.916 millones, con un impacto de −1,4 % sobre el PIB de 2024 (Redacción Primicias, 2025).
- El suministro de electricidad y agua cayó 12,1 % en 2024 (Banco Central del Ecuador, 2026, p. 22).

**Qué significa para Torvesa:** el equipo trabaja en obra, a veces sin luz ni buena señal. Por eso el diseño exige que las fichas de los clientes se puedan consultar sin conexión (RQ-14).

### 1.3 El cliente ya está en línea; la empresa no siempre

- A finales de 2025, 15,4 millones de personas usaban internet en Ecuador, el 83,9 % de la población (Kemp, 2026).
- El 83 % de los clientes espera interactuar con alguien de inmediato cuando contacta a una empresa (Salesforce Research, 2022, p. 16).
- En una prueba con 1.000 empresas B2B, 635 nunca respondieron a una solicitud (Koushik, 2024).
- El uso de WhatsApp para negocios en Ecuador no tiene todavía una fuente verificada [FALTA-FUENTE: cifra nacional de uso de WhatsApp, p. ej. INEC TIC o el informe de Mentinno con página]. Para Torvesa sí hay dato: 4 de 5 personas del censo dicen que los clientes escriben al WhatsApp personal de los socios o ingenieros (Bermeo y Segura, 2026, p. 10).
- La regla de que responder en la primera hora multiplica la calificación del prospecto («siete veces») sigue sin verificar [FALTA-FUENTE: A9 — Oldroyd et al. (2011), PDF por la biblioteca UPS].

### 1.4 Las pymes adoptan poco la IA y les faltan datos ordenados

- En las mipymes ecuatorianas la IA se usa poco, sobre todo en marketing. Las barreras: falta de profesionales, **falta de bases de datos estructuradas** y poca capacidad financiera (Pérez-Campdesuñer et al., 2025).
- En la OCDE, el 11,9 % de las pequeñas empresas usa IA, frente al 40 % de las grandes (OECD, 2025, p. 6).
- Ecuador está en la categoría «adoptante» del Índice Latinoamericano de IA 2025 (Comisión Económica para América Latina y el Caribe [CEPAL], 2025).
- El 33 % de los empleados en Ecuador usa cuentas personales de IA para tareas de trabajo, y el 70 % de las organizaciones no tiene reglas internas para la IA (Revelo, 2026).

**Qué significa para Torvesa:** el primer paso no es «poner IA», sino **ordenar la memoria comercial** (la bóveda) para que la IA tenga de dónde sacar información, y hacerlo con reglas de protección de datos desde el inicio.

### 1.5 La memoria de la empresa vive en celulares

- La amnesia institucional es la incapacidad de una organización de recordar y usar lo que ya sabía; la rotación del personal la agrava (Stark, 2024, p. 3).
- Los vendedores dedican el 70 % de su tiempo a tareas que no son vender (Salesforce Research, 2024, p. 13).

## 2. La necesidad, en el caso de Torvesa

### 2.1 Lo que dice el censo de la empresa (n = 5)

| Hallazgo | Frecuencia |
|---|---|
| Pasa más de la mitad de su jornada en obra | 3 de 5 |
| Revisa los mensajes de clientes cada 3 o 4 horas | 2 de 5 |
| Revisa los mensajes solo al llegar a casa | 1 de 5 |
| Los clientes le escriben a su WhatsApp personal | 4 de 5 |
| El tiempo máximo aceptable para el primer contacto es menos de 15 minutos | 4 de 5 |
| Le parece crítico revisar cada semana por qué se pierden clientes | 3 de 5 |
| Prefiere una alerta de texto simple o una tarjeta con enlace | 2 de 5 y 2 de 5 |

*Nota.* Bermeo y Segura (2026, p. 10). Censo de la gerencia y la operación de Torvesa, mayo de 2026. Es pequeño y no es una muestra: se presenta como antecedente, no como línea base.

### 2.2 La brecha

- **Lo que la empresa quiere:** responder en menos de 15 minutos (4 de 5).
- **Lo que pasa hoy:** 3 de 5 revisan los mensajes cada 3 o 4 horas o solo al llegar a casa.
- **Lo que no queda registrado:** quién atendió, a qué hora y por qué se perdió el cliente.

> [!important] Hallazgo para el Cap. I
> El Cap. I v0.3 dice que la meta de 15 minutos «es una decisión de diseño» porque la literatura no respalda un plazo exacto. **El censo le da un respaldo de la empresa:** 4 de 5 personas de Torvesa fijan ese mismo límite. Se propone decir: «la meta de 15 minutos es una decisión de diseño que coincide con el límite que fijó la propia empresa (Bermeo y Segura, 2026, p. 10)». No es evidencia de que 15 minutos sea el óptimo.

### 2.3 Planteamiento de la necesidad (para usar con la gerencia)

> Torvesa pierde clientes en la primera hora, no en la obra. El cliente escribe a un celular personal; quien lo recibe está en obra y lo ve horas después; nadie sabe quién lo atendió ni por qué se fue. En un sector que viene de caer 7,9 % y recién se recupera, ese cliente que se va en silencio es el costo más caro de la empresa, y hoy no se mide.

[FALTA-DATO: cuántas solicitudes recibe Torvesa al mes y cuántas se pierden. Sale de la muestra documental de los últimos 3 meses, cuando Torvesa la autorice.]

## 3. Análisis FODA de la propuesta

El FODA analiza **la propuesta** (el sistema para la gestión comercial de Torvesa), no a la empresa entera. Cada punto dice de dónde sale.

### 3.1 Matriz FODA

| | Positivo | Negativo |
|---|---|---|
| **Interno** (la propuesta y el equipo) | **Fortalezas** | **Debilidades** |
| | F1. El flujo completo ya funciona en internet con datos ficticios: formulario, aviso, bóveda y borrador (prueba de concepto, 8-nov). | D1. Sin datos reales de Torvesa todavía: no hay línea base de M1 a M4 [FALTA-DATO]. |
| | F2. Registro con huellas que detectó 3 de 3 alteraciones en la prueba (M5). | D2. El censo es de 5 personas: sirve de antecedente, no de prueba. |
| | F3. Protección de datos desde el diseño: consentimiento obligatorio, el asistente no recibe nombres ni teléfonos (RQ-18, RQ-21). | D3. Depende de servicios de terceros (servidor, avisos, IA) con precios que pueden cambiar. |
| | F4. El asistente no pone precios ni envía nada solo: una persona revisa (RQ-12). | D4. El equipo es de dos estudiantes: el soporte después de la tesis no está resuelto. |
| | F5. Costo bajo: la bóveda usa Obsidian, gratuito para uso comercial (Obsidian, 2025). | D5. La clave de acceso del servidor está en la página pública: hay que separarla antes de usar datos reales (revisión del código, 10-nov). |
| **Externo** (el mercado y el país) | **Oportunidades** | **Amenazas** |
| | O1. La construcción vuelve a crecer en 2025 (+2,7 %) después de dos años de caída (Banco Central del Ecuador, 2026, p. 22). | A1. Cortes de luz y mala señal en obra: en 2024 hubo cortes de hasta 12 horas (Tapia, 2024). |
| | O2. El cliente ya está conectado: 83,9 % usa internet (Kemp, 2026). | A2. Desconfianza o falta de autorización de la empresa: sin ella no hay validación (ruta crítica). |
| | O3. Pocas pymes usan IA (Pérez-Campdesuñer et al., 2025; OECD, 2025, p. 6): quien ordene primero sus datos se adelanta. | A3. Uso de IA con cuentas personales sin reglas en el 70 % de las organizaciones (Revelo, 2026): riesgo de fuga de datos de clientes. |
| | O4. La LOPDP y su reglamento (2023) obligan a ordenar los datos personales: el sistema ayuda a cumplir (Ley Orgánica de Protección de Datos Personales [LOPDP], 2021; Reglamento General de la LOPDP, 2023). | A4. Competidores con CRM comerciales listos para usar [FALTA-FUENTE: oferta y precios de CRM para constructoras en Ecuador]. |
| | O5. El mismo proceso sirve a otras constructoras, remodeladoras e inmobiliarias (ver el documento del proceso estrella). | A5. Que el equipo de obra no adopte la herramienta si le quita tiempo: por eso la alerta es de texto simple (censo P7). |

### 3.2 Matriz cruzada (estrategias)

| Tipo | Código | Estrategia | Combina |
|---|---|---|---|
| **FO** (fortalezas para aprovechar oportunidades) | FO1 | Presentar la prueba de concepto funcionando a la gerencia ahora, mientras la demanda se recupera | F1 + O1 |
| | FO2 | Vender el cumplimiento de la LOPDP como beneficio, no como costo | F3 + O4 |
| | FO3 | Empaquetar el «primer contacto en 15 minutos» como servicio para otras empresas del sector | F1 + O5 |
| **DO** (corregir debilidades con las oportunidades) | DO1 | Pedir a Torvesa solo fechas y horas de 3 meses, sin datos de clientes, para tener la línea base | D1 + O4 |
| | DO2 | Elegir servicios con plan gratuito o por consumo y documentar una alternativa para cada uno | D3 |
| | DO3 | Separar las claves del servidor antes de cualquier dato real | D5 + O4 |
| **FA** (fortalezas para frenar amenazas) | FA1 | Fichas sin conexión en el celular para trabajar con cortes de luz | RQ-14 + A1 |
| | FA2 | Ofrecer el asistente con reglas claras como alternativa al uso de IA personal sin control | F3 + F4 + A3 |
| | FA3 | Proponer una validación corta y reversible, de dos semanas, que no compromete a la empresa | F1 + A2 |
| **DA** (reducir debilidades y amenazas a la vez) | DA1 | Empezar con lo mínimo que la gente usa: aviso de texto y botón «Tomar» | D4 + A5 |
| | DA2 | Dejar manuales y la bóveda documentada para que el sistema no dependa de los autores | D4 |
| | DA3 | Comparar con un CRM comercial en la matriz de herramientas, con precios oficiales | A4 |

### 3.3 Resumen del FODA (para la imagen)

- **Fortalezas:** prueba de concepto funcionando · registro que detecta alteraciones · datos personales protegidos · persona revisa siempre · costo bajo.
- **Debilidades:** sin datos reales aún · censo pequeño · depende de terceros · equipo de dos personas · clave del servidor expuesta.
- **Oportunidades:** construcción se recupera · cliente conectado · pocas pymes con IA · la ley obliga a ordenar datos · sirve a otras empresas.
- **Amenazas:** cortes de luz y mala señal · falta de autorización · IA personal sin reglas · CRM comerciales · que el equipo no lo adopte.
- **Estrategia central:** demostrar ahora, con una validación corta y reversible, que el primer contacto en menos de 15 minutos es posible y queda registrado.

## 4. Qué tan viable es

| Criterio | Estado | Por qué |
|---|---|---|
| Técnico | Alto | El flujo completo funciona en la prueba de concepto (8-nov), con datos ficticios |
| Legal (LOPDP) | Medio-alto | Consentimiento, minimización y separación de contactos ya diseñados; falta separar la clave del servidor y el plazo de conservación [FALTA-DATO] |
| Organizacional | **Pendiente** | Depende de que Torvesa autorice la validación: es la ruta crítica |
| Económico | Lo calcula el frente A | VAN, TIR y ROI en el modelo financiero; aquí no van cifras |

## Referencias

Banco Central del Ecuador. (2026). *Informe de evolución de la economía ecuatoriana en 2025 y perspectivas 2026*. https://contenido.bce.fin.ec/documentos/Administracion/EvolEconEcu_2025pers2026.pdf

Bermeo, D., y Segura, V. (2026). *TEAMSLASH: Ecosistema digital de gestión de clientes para la Constructora Torvesa* [Informe final del proyecto integrador, Universidad Politécnica Salesiana]. [FALTA-DATO: confirmar con la carrera cómo se cita]

Comisión Económica para América Latina y el Caribe. (2025, 3 de octubre). *América Latina y el Caribe aceleran la adopción de la inteligencia artificial, aunque persisten desafíos en inversión, talento y gobernanza* [Comunicado].

Instituto Nacional de Estadística y Censos. (2026, 8 de enero). *INEC presenta resultados de la ENEMDU – diciembre 2025* [Comunicado]. https://www.ecuadorencifras.gob.ec/institucional/inec-presenta-resultados-de-la-enemdu-diciembre-2025/

Kemp, S. (2026). *Digital 2026: Ecuador*. DataReportal. https://datareportal.com/reports/digital-2026-ecuador

Koushik, V. (2024, 20 de marzo). *We tested lead response times of 1000 B2B sales teams. Here are the results*. RevenueHero. https://www.revenuehero.io/blog/b2b-lead-response-times

Ley Orgánica de Protección de Datos Personales. (2021, 26 de mayo). Registro Oficial, Quinto Suplemento n.º 459.

Obsidian. (2025, 20 de febrero). *Obsidian license agreement*. Recuperado el 21 de octubre de 2026, de https://obsidian.md/license

OECD. (2025). *AI adoption by small and medium-sized enterprises* (OECD discussion paper for the G7). OECD Publishing.

Pérez-Campdesuñer, R., Sánchez-Rodríguez, A., García-Vidal, G., Martínez-Vivar, R., y De Miguel-Guzmán, M. (2025). Artificial intelligence in Ecuadorian SMEs: Drivers and obstacles to adoption. *Information, 16*(6), 443.

Redacción Primicias. (2025, 15 de abril). La economía de Ecuador cayó en recesión en 2024, confirma el Banco Central. *Primicias*. https://primicias.ec/economia/economia-ecuador-recesion-bce-crisis-electrica-iva-94029

Reglamento General de la Ley Orgánica de Protección de Datos Personales. Decreto Ejecutivo 904. (2023, 13 de noviembre). Registro Oficial, Tercer Suplemento n.º 435.

Revelo, R. (2026, 16 de septiembre). El peligro de la «Shadow AI»: el 33 % de empleados en Ecuador usa IA personal en el trabajo. *Primicias*.

Salesforce Research. (2022). *State of the connected customer* (5.ª ed.). Salesforce.

Salesforce Research. (2024). *State of sales* (6.ª ed.). Salesforce.

Stark, A. (2024). Institutional amnesia in government: How much is enough? *Policy Quarterly, 20*(1), 3–9. https://doi.org/10.26686/pq.v20i1.9046

Tapia, E. (2024, 23 de octubre). Ecuador cumple un mes con largos apagones que llegaron hasta 12 horas, ¿cuáles son los efectos en el país? *Primicias*. https://primicias.ec/economia/primer-mes-apagones-ecuador-perdidas-industrias-81725
