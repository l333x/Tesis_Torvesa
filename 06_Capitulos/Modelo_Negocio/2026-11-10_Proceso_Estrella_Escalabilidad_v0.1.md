---
titulo: "El proceso estrella y cómo se escala a otras empresas"
version: v0.1
fecha: 2026-11-10
autor_borrador: "Claude Opus 5.5 (frente B); Víctor revisa"
base: "Cap. IV v0.1 (puntos críticos, RQ-01 a RQ-24, TO-BE en 3 partes) · prueba de concepto del 8-nov · censo n = 5 (Informe Final, p. 10) · 06_Capitulos/2026-11-10_Necesidad_Contexto_FODA_v0.1.md"
marcadores: "FALTA-FUENTE 4 · FALTA-DATO 2 · DECIDIR-VÍCTOR 2"
para_frente_C: "La sección 6 es la especificación de los diagramas (Miro)"
tags: [modelo-negocio, proceso-estrella, escalabilidad, calidad, kpi, sprint5]
---

# El proceso estrella y cómo se escala

> [!summary] En tres frases
> 1. El proceso estrella es el **«Primer contacto garantizado en 15 minutos»**: cada solicitud tiene un responsable, un aviso inmediato, la ficha del cliente a mano y un registro que nadie puede alterar sin que se note.
> 2. Es el proceso que conviene vender porque **se puede medir** (minutos hasta el primer contacto) y **se puede auditar** (registro con huellas). Otra constructora lo puede contratar sin cambiar su forma de construir.
> 3. La cotización asistida y la bóveda son el segundo nivel: se venden después, a quien ya tiene el primer contacto bajo control.

## 1. Por qué este proceso y no otro

Se compararon los cinco puntos críticos del proceso actual (Cap. IV, Tabla 1) con cuatro preguntas: ¿duele hoy?, ¿se puede medir?, ¿se puede mostrar funcionando?, ¿lo compraría otra empresa?

| Punto crítico | ¿Duele hoy? | ¿Se mide? | ¿Ya funciona? | ¿Lo compraría otra empresa? |
|---|---|---|---|---|
| 1. Espera | Sí: 3 de 5 revisan los mensajes cada 3–4 h o al llegar a casa (Bermeo y Segura, 2026, p. 10) | Sí: minutos hasta el primer contacto (M1) | Sí: aviso en Slack y botón «Tomar», con la hora guardada | Sí: es igual en cualquier empresa que recibe solicitudes |
| 2. Asignación informal | Sí: la delegación no deja rastro | Sí: % de solicitudes con responsable | Sí | Sí |
| 3. Cotización desde cero | Sí | Sí, en condiciones controladas (M2, CP-01) | Como prueba de concepto | Sí, pero hay que adaptar las plantillas a cada rubro |
| 4. Seguimiento de memoria | Sí | En parte | Parcial | Sí |
| 5. Historial en los celulares | Sí | Sí, en condiciones controladas (M4, CP-02) | Como prueba de concepto | Sí, pero exige ordenar datos antes |

**Conclusión:** los puntos 1 y 2 juntos son el proceso estrella. Se confirma la propuesta inicial («primer contacto en menos de 15 minutos con historial y registro verificable») con un ajuste: **el registro verificable va dentro del proceso estrella, y el historial completo (bóveda) pasa al segundo nivel**. La razón es práctica: el registro ya funciona en el servidor, mientras que la bóveda exige que la empresa primero ordene sus datos, y esa falta de datos ordenados es justo la barrera principal de las mipymes ecuatorianas (Pérez-Campdesuñer et al., 2025).

**Evidencia que lo respalda:**
- 4 de 5 personas de Torvesa fijan en menos de 15 minutos el tiempo máximo aceptable para el primer contacto (Bermeo y Segura, 2026, p. 10).
- El 83 % de los clientes espera interactuar con alguien de inmediato (Salesforce Research, 2022, p. 16).
- 635 de 1.000 empresas B2B nunca respondieron a una solicitud en una prueba de «cliente incógnito» (Koushik, 2024).
- La meta de 15 minutos es una **decisión de diseño**, no un óptimo probado: la literatura revisada no respalda un plazo exacto (Cap. I v0.3).

## 2. El proceso estrella paso a paso

**Nombre comercial propuesto:** *Primer contacto garantizado* (PCG). [DECIDIR-VÍCTOR: nombre comercial]

| Paso | Qué pasa | Quién | Tiempo objetivo | Requisito |
|---|---|---|---|---|
| 1. Captura | La solicitud entra por el formulario (con consentimiento) o se registra desde el celular si llegó por WhatsApp o teléfono | Cliente o coordinador | Al llegar | RQ-01, RQ-03, RQ-18 |
| 2. Código y registro | El sistema le da un código y guarda la hora de llegada en el registro con huellas | Sistema | ≤ 5 s | RQ-01, RQ-15 |
| 3. Aviso | Llega una tarjeta al celular del equipo con un enlace a la ficha | Sistema | ≤ 5 s | RQ-02 |
| 4. Tomar | Alguien pulsa «Tomar» y queda como único responsable | Responsable | Minuto 0 a 15 | RQ-04 |
| 5. Primer contacto | El responsable contacta al cliente; el sistema guarda la hora | Responsable | Antes del minuto 15 | RQ-24 (M1) |
| 6. Escalamiento | Si nadie tomó la solicitud a los 15 minutos, se recuerda al equipo y se avisa a la gerencia | Sistema → gerencia | Minuto 15 | RQ-06 |
| 7. Cierre con motivo | Si se pierde, el motivo es obligatorio, de una lista cerrada | Responsable | Al cerrar | RQ-07 |
| 8. Reporte del lunes | Mediana del tiempo de primer contacto, estados y motivos de pérdida, y la última huella del registro | Sistema → gerencia | Cada lunes | RQ-08 |

**Lo que el proceso estrella entrega a la gerencia, cada lunes:** cuántas solicitudes llegaron, en cuántos minutos se atendieron (mediana), cuántas se perdieron y por qué. Hoy no sabe ninguna de esas cuatro cosas.

## 3. Los tres niveles del producto

| Nivel | Qué incluye | Para quién | Requisitos |
|---|---|---|---|
| **1. Primer contacto garantizado** (estrella) | Captura, aviso, responsable único, recordatorio a los 15 min, motivo de pérdida, reporte del lunes, registro con huellas | Toda empresa que recibe solicitudes de clientes | RQ-01 a RQ-08, RQ-15 a RQ-18, RQ-24 |
| **2. Memoria comercial** | Bóveda con la ficha de cada cliente, historial, plantillas por tipo de trabajo, consulta sin conexión | Empresas con rotación de personal o con varios vendedores | RQ-09, RQ-10, RQ-13, RQ-14, RQ-19, RQ-20 |
| **3. Cotización asistida** | Borrador de cotización con IA, sin precios, con los documentos citados, siempre revisado por una persona | Empresas que cotizan trabajos parecidos con frecuencia | RQ-11, RQ-12, RQ-21 |

Cada nivel necesita el anterior: no hay borrador útil sin bóveda, y la bóveda no sirve si las solicitudes se pierden en el primer contacto.

## 4. Cómo se escala a otras empresas

El núcleo (nivel 1) es el mismo para todas. Lo que cambia es la configuración: los tipos de trabajo, las plantillas, los estados, el plazo objetivo y los canales.

| Ejemplo | Qué le duele | Qué se configura | Plazo objetivo sugerido | Nivel con el que entra |
|---|---|---|---|---|
| **Torvesa** (constructora, obra residencial, comercial y remodelación) | Mensajes al WhatsApp personal; equipo en obra | Tipos de obra; formulario de la web; registro manual de WhatsApp | 15 min (lo fija la empresa) | 1 → 2 → 3 |
| **Otra constructora** | Lo mismo, con otros tipos de obra | Plantillas y catálogo propios; su canal de avisos | Lo fija la empresa | 1 |
| **Remodelación** (cocinas, baños, acabados) | Muchas solicitudes pequeñas; el cliente compara varias ofertas a la vez | Formulario con fotos y medidas; plantillas por ambiente | Lo fija la empresa; el cliente compara rápido [FALTA-FUENTE: evidencia de cuántas cotizaciones pide un cliente de remodelación] | 1 + 3 |
| **Inmobiliaria** (venta de departamentos o casas) | Prospectos de portales y redes que se enfrían; agendar visitas | Estado «Visita agendada»; asignación por proyecto | Lo fija la empresa | 1 + 2 |
| **Ferretería o proveedor de materiales** | Pedidos de cotización de listas de materiales; recompra | Plantilla de lista de materiales; vínculo con su catálogo de precios; recordatorio de recompra | Lo fija la empresa | 1 + 3 (el asistente sí podría usar precios del catálogo) |

**Regla para escalar sin perder calidad:**
- El código del núcleo no cambia de una empresa a otra; solo cambian sus datos de configuración.
- Cada empresa tiene su propia base de datos y su propia bóveda. **Nunca** se mezclan datos de clientes de dos empresas (LOPDP).
- El plazo objetivo lo fija cada empresa; el sistema mide contra ese plazo.

[DECIDIR-VÍCTOR: si el modelo de negocio TEAMSLASH (anexo) se vende por empresa al mes o por usuario. Lo calcula el frente A.]

## 5. Estándares de calidad y cómo se miden

### 5.1 Qué estándar se usa para qué

| Estándar | Para qué se usa aquí | Cómo se aplica | Fuente |
|---|---|---|---|
| ISO/IEC 25010 (calidad del producto de software) | Decir qué es un sistema «de calidad»: que haga lo que debe, rápido, fiable, seguro y fácil de mantener | Cada característica tiene al menos un indicador (tabla 5.2) | [FALTA-FUENTE: ficha de ISO/IEC 25010:2023; la página de iso.org bloqueó la consulta automática] |
| ISO 9001 (gestión de la calidad, enfoque a procesos) | Tratar la atención comercial como un proceso con entradas, salidas, responsable e indicadores, que se mejora con el ciclo planificar-hacer-verificar-actuar | El reporte del lunes es el «verificar»; el motivo de pérdida alimenta el «actuar» | [FALTA-FUENTE: ficha de ISO 9001:2015 o de los principios de gestión de la calidad de ISO] |
| ISO/IEC 27001 (seguridad de la información) | Ordenar los controles de acceso, claves y registros | Cuentas individuales (RQ-20), claves separadas, registro de eventos | [FALTA-FUENTE: ficha de ISO/IEC 27001:2022] |
| LOPDP y su reglamento | Consentimiento, minimización, conservación limitada | RQ-17, RQ-18, RQ-19, RQ-21 | Ley Orgánica de Protección de Datos Personales (2021, art. 8, p. 15; art. 10, lit. i, p. 18) |
| FIPS 180-4 (SHA-256) | La huella de cada evento del registro | RQ-15, RQ-16 | National Institute of Standards and Technology (2015, p. iv) |

> [!warning] Las normas ISO no se certifican en este trabajo
> Se usan como marco para elegir indicadores. Decir «cumple ISO» sería falso: no hay auditoría ni certificación.

### 5.2 Indicadores (KPI) del proceso estrella

| Indicador | Fórmula | Meta | Característica de calidad | Meta de la tesis |
|---|---|---|---|---|
| Mediana del tiempo de primer contacto | Mediana de (hora del primer contacto − hora de llegada) | < 15 min | Adecuación funcional | M1 |
| Solicitudes atendidas dentro del plazo | Atendidas antes del plazo ÷ total | ≥ 80 % [DECIDIR-VÍCTOR: meta] | Adecuación funcional | M1 |
| Solicitudes con responsable | Con responsable ÷ total | 100 % | Adecuación funcional | M3 |
| Pérdidas con motivo | Perdidas con motivo ÷ perdidas | 100 % | Adecuación funcional | M3 |
| Tiempo del aviso | Hora del aviso − hora de llegada | ≤ 5 s | Eficiencia de desempeño | RQ-02 |
| Disponibilidad del servidor | Minutos en línea ÷ minutos del mes | [FALTA-DATO: meta, según el plan del proveedor] | Fiabilidad | — |
| Alteraciones detectadas | Alteraciones detectadas ÷ alteraciones simuladas | 100 % | Seguridad (integridad) | M5 |
| Datos personales enviados a la IA | Solicitudes con datos personales en lo enviado ÷ total | 0 % | Seguridad (confidencialidad) | RQ-21 |
| Solicitudes de WhatsApp registradas | Registradas ÷ recibidas por WhatsApp | [FALTA-DATO: se mide en la validación] | Adecuación funcional | M1 |

## 6. Especificación de los diagramas (para el frente C)

Cada diagrama dice: carriles (quién), pasos, decisiones, eventos y notas. Lenguaje simple en las cajas.

### Diagrama E1 · Proceso estrella «Primer contacto garantizado» (BPMN, carriles)
- **Carriles:** Cliente · Sistema · Equipo comercial (responsable) · Gerencia.
- **Inicio:** «El cliente envía una solicitud» (formulario web) **o** «Llega un mensaje por WhatsApp o teléfono» (el coordinador lo registra desde el celular).
- **Sistema:** «Asigna un código y guarda la hora» → «Guarda el evento en el registro con huellas» → «Envía el aviso al equipo».
- **Equipo:** «Pulsa Tomar» → «Contacta al cliente» → el sistema «Guarda la hora del primer contacto».
- **Decisión (temporizador de 15 min):** «¿Alguien tomó la solicitud?» — Sí → sigue; No → «Recordatorio al equipo y aviso a la gerencia».
- **Gerencia:** «Reasigna» (si sigue sin atender).
- **Decisión final:** «¿Se ganó el cliente?» — Sí → «Cerrado: ganado»; No → «Elegir motivo de pérdida (obligatorio)».
- **Evento semanal (lunes):** «Reporte a la gerencia: mediana de minutos, estados, motivos y la última huella».
- **Nota al pie:** «Cada paso queda en el registro, sin datos personales».

### Diagrama E2 · Los tres niveles del producto (pirámide o escalera)
- Base: **Nivel 1 · Primer contacto garantizado** (estrella).
- Medio: **Nivel 2 · Memoria comercial** (bóveda, historial, sin conexión).
- Arriba: **Nivel 3 · Cotización asistida** (IA, siempre revisada por una persona).
- Flecha lateral: «Cada nivel necesita el anterior».

### Diagrama E3 · Escalabilidad: un núcleo, cinco configuraciones (estrella o hub)
- Centro: **Núcleo igual para todas** (captura, aviso, responsable, 15 min, motivo, reporte, registro).
- Alrededor, cinco tarjetas: Torvesa · Otra constructora · Remodelación · Inmobiliaria · Ferretería o proveedor. Cada tarjeta lleva «Qué se configura» de la tabla de la sección 4.
- Banda inferior: «Cada empresa con su base de datos y su bóveda; nunca se mezclan clientes (LOPDP)».

### Diagrama E4 · Línea de tiempo del escalamiento (de 0 a 15 minutos y después)
- 0 s: llega la solicitud · ≤ 5 s: aviso · 0–15 min: alguien pulsa «Tomar» y contacta · 15 min: recordatorio + aviso a la gerencia · después: reasignación · lunes: reporte.
- Comparación arriba de la línea: «Hoy: 3 de 5 revisan los mensajes cada 3–4 h o al llegar a casa (censo n = 5)».

### Diagrama E5 · Ciclo de mejora del proceso (planificar-hacer-verificar-actuar)
- Planificar: fijar el plazo objetivo y la lista de motivos de pérdida.
- Hacer: atender con el proceso estrella.
- Verificar: reporte del lunes (mediana, % dentro del plazo, motivos).
- Actuar: la gerencia corrige (reasigna turnos, ajusta plantillas, cambia el plazo).

### Imagen del FODA
- Usar el resumen de la sección 3.3 de *La necesidad de Torvesa: contexto de Ecuador y FODA* (v0.1, 10-nov). Cuatro cuadrantes, cinco puntos cortos cada uno, y la estrategia central abajo.

## Referencias

Bermeo, D., y Segura, V. (2026). *TEAMSLASH: Ecosistema digital de gestión de clientes para la Constructora Torvesa* [Informe final del proyecto integrador, Universidad Politécnica Salesiana].

Koushik, V. (2024, 20 de marzo). *We tested lead response times of 1000 B2B sales teams. Here are the results*. RevenueHero. https://www.revenuehero.io/blog/b2b-lead-response-times

Ley Orgánica de Protección de Datos Personales. (2021, 26 de mayo). Registro Oficial, Quinto Suplemento n.º 459.

National Institute of Standards and Technology. (2015). *Secure Hash Standard (SHS)* (FIPS PUB 180-4). U.S. Department of Commerce. https://doi.org/10.6028/NIST.FIPS.180-4

Pérez-Campdesuñer, R., Sánchez-Rodríguez, A., García-Vidal, G., Martínez-Vivar, R., y De Miguel-Guzmán, M. (2025). Artificial intelligence in Ecuadorian SMEs: Drivers and obstacles to adoption. *Information, 16*(6), 443.

Salesforce Research. (2022). *State of the connected customer* (5.ª ed.). Salesforce.
