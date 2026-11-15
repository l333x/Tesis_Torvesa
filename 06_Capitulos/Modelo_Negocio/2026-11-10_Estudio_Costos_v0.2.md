---
titulo: "Estudio de costos: cuánto cuesta, cuánto se gana y cuándo se paga"
version: v0.2
fecha: 2026-11-10
autor_borrador: "Claude (frente 1); Víctor revisa y aprueba"
base: "Modelo financiero v0.1 y matriz de herramientas v0.1 (10-nov) · censo n = 5 (Informe Final, p. 10) · proceso estrella v0.1 · precios oficiales consultados entre el 21-oct y el 10-nov-2026"
reemplaza: "No reemplaza al modelo v0.1: lo amplía. La opción 1 de Torvesa repite sus supuestos"
marcadores: "FALTA-DATO 9 · FALTA-FUENTE 8 · VERIFICAR 8"
tags: [costos, modelo-negocio, punto-equilibrio, viabilidad, sprint5]
---

# Estudio de costos v0.2

## Resumen de una página

> [!warning] Antes de leer las cifras
> Los **precios** son oficiales, con su página y fecha. Todo lo que es **de Torvesa** (solicitudes al mes, clientes perdidos, valor de una obra, sueldos) es **SUPUESTO**, porque la empresa aún no entrega esos datos. Los **precios de venta de TEAMSLASH** son una propuesta nuestra, no un precio probado.

**Se calcula como el costo de una salchipapa:** primero se suma todo lo que entra en un mes de trabajo (sueldos, lugar, luz, internet, equipos y programas) y después se divide para lo que se vende.

**Para Torvesa (el cliente), en el escenario base:**

| Pregunta | Respuesta |
|---|---|
| ¿Cuánto gasta? | **USD 162 al mes** si lo contrata como servicio; USD 265 al mes si lo arma por su cuenta |
| ¿Cuánto gana? | **USD 804 al mes**: USD 354 en tiempo (unas 42 horas que se liberan) y USD 450 en obras que deja de perder |
| ¿Cuándo se paga? | En **1 a 2 meses** como servicio; en unos 8 meses por su cuenta |
| ¿Qué tiene que pasar? | Recuperar **1,3 obras al año** (servicio) o 2,1 (por su cuenta), aunque no ahorre ni un minuto |
| ¿Y si sale mal? | En el escenario pesimista **pierde plata** con el nivel completo. Por eso conviene empezar por el nivel 1, de USD 49 al mes |

**Para TEAMSLASH (nosotros como negocio):**

| Pregunta | Respuesta |
|---|---|
| ¿Cuánto cuesta una hora de trabajo? | Una persona de desarrollo con sueldo de USD 1.000 cuesta **USD 1.360 al mes y USD 8,50 la hora**: un 36 % más que su sueldo |
| ¿Cuánto cuesta operar? | Al arrancar, **USD 161 al mes de caja**; USD 1.571 si se valora el tiempo de los dos fundadores |
| ¿Cuánto cuesta atender a un cliente? | Entre **USD 11 y USD 41 al mes**, según el nivel |
| ¿Cuántos clientes hacen falta? | **3 empresas** para no perder plata de caja; **27** para pagar el medio tiempo de los fundadores; **126** para sostener un equipo formal |

**Tres decisiones:** trabajar desde casa (USD 18 por persona al mes frente a USD 217 en coworking); usar las laptops propias y comprar cuando se contrate; encargar módulos a independientes con cesión de derechos y sumar un pasante desde unos 10 clientes.

**La bóveda y el asistente:** bóveda con Obsidian Sync (USD 23 al mes) y asistente pagado por consulta (unos USD 2 al mes). Entrenar un modelo propio cuesta USD 17.155 al mes y no hace falta. La capa gratuita de AWS no es permanente: son USD 100 a 200 de crédito y 6 meses.

## 1. Cómo se armó

- Todo está en una hoja de cálculo con fórmulas vivas, que acompaña a este documento (`2026-11-10_Estudio_Costos_v0.2.xlsx`, en la misma carpeta). Se recalculó en Excel sin errores.
- Tiene tres partes: **A**, TEAMSLASH como negocio; **B**, Torvesa como cliente; **C**, dónde viven la bóveda y el asistente.
- En la parte B hay tres escenarios: pesimista, base y optimista. En la parte A hay tres tamaños de empresa: arranque, crecimiento y formal.
- Los 30 colaboradores y los 33 clientes en cartera vienen del diseño aprobado y no tienen documento de respaldo. No se usan como dato [FALTA-DATO: nota de la gerencia].
- El diagnóstico de 30 personas es simulado y no se usa.

## 2. Parte A · TEAMSLASH como negocio

### 2.1 Cuánto cuesta una hora de trabajo

El sueldo no es el costo. A la empresa una persona le cuesta el sueldo más lo que manda la ley:

| Concepto | Desarrollo | Soporte o ventas |
|---|---|---|
| Sueldo (SUPUESTO) | USD 1.000 | USD 600 |
| Aporte patronal al IESS (11,15 %) | USD 112 | USD 67 |
| Décimo tercero | USD 83 | USD 50 |
| Décimo cuarto (un salario básico de USD 482 al año) | USD 40 | USD 40 |
| Vacaciones | USD 42 | USD 25 |
| Fondos de reserva (desde el segundo año) | USD 83 | USD 50 |
| **Costo real al mes** | **USD 1.360** | **USD 832** |
| **Costo por hora** (160 horas al mes) | **USD 8,50** | **USD 5,20** |
| Costo por semana | USD 340 | USD 208 |
| Costo por año | USD 16.320 | USD 9.985 |

*Nota.* El salario básico es de USD 482 (Ministerio del Trabajo, 2026, p. 2). Los sueldos son supuestos [FALTA-FUENTE: tabla de salarios mínimos sectoriales 2026]. Los porcentajes de ley están sin página [VERIFICAR-PÁG: IESS, Resolución C.D. 515] [FALTA-FUENTE: Código del Trabajo].

### 2.2 Cuánto cuesta operar al mes

| Concepto | Arranque | Crecimiento | Formal |
|---|---|---|---|
| Quiénes trabajan | 2 fundadores a medio tiempo | Fundadores a 3/4 de tiempo, 1 pasante y 20 horas de un independiente | Fundadores a tiempo completo, 3 contratados y 1 pasante |
| Dónde | Desde casa | Desde casa | Coworking (3 puestos) |
| **Costo fijo al mes, todo incluido** | **USD 1.571** | **USD 2.989** | **USD 7.436** |
| De eso, lo que sale de caja | USD 161 | USD 874 | USD 4.566 |
| Por hora de operación | USD 9,82 | USD 18,68 | USD 46,48 |
| Por semana | USD 363 | USD 690 | USD 1.716 |
| Por año | USD 18.850 | USD 35.869 | USD 89.234 |

- «Todo incluido» valora el tiempo de los fundadores a USD 8,50 la hora, aunque no cobren, y el desgaste de las laptops. Es lo que el negocio debería poder pagar.
- «Lo que sale de caja» al arrancar es: servidor y página (USD 46), dos suscripciones de IA para programar (USD 46), publicidad (USD 30), internet y luz (USD 36), firma electrónica y dominio (USD 3).
- Constituir la empresa como SAS no cuesta nada y no pide capital mínimo (Superintendencia de Compañías, Valores y Seguros, s. f.). La firma electrónica cuesta USD 31,05 por 2 años (Dirección General de Registro Civil, Identificación y Cedulación, s. f.).
- La contabilidad externa (USD 80 a 150) es un supuesto [FALTA-FUENTE: tarifa de un contador].

### 2.3 Decisión 1: dónde trabajar

| | Desde casa | Coworking | Oficina privada flexible |
|---|---|---|---|
| Costo por persona al mes | USD 18 | USD 217 | USD 236 |
| Equipo de 2, al año | USD 436 | USD 5.216 | USD 5.658 |
| Equipo de 4, al año | USD 873 | USD 10.433 | USD 11.316 |
| Qué da | Cero arriendo | Dirección, sala de reuniones, internet y limpieza | Espacio cerrado propio |
| Qué arriesga | No hay dónde recibir clientes | Costo fijo desde el primer mes | El más caro, con contrato |

*Nota.* Coworking, USD 189 por puesto al mes; oficina privada flexible, mediana de USD 205; ambos sin IVA y con todo incluido (Workin.space, 2026). Casa: la mitad de un plan de internet de USD 33,93 (Netlife, s. f.) más la luz de una laptop. El arriendo tradicional por metro cuadrado no tiene fuente [FALTA-FUENTE].

**Recomendación:** trabajar desde casa mientras el equipo sea de 2 o 3 personas y reunirse con los clientes en su oficina o en la obra. Con 2 personas, el coworking cuesta 12 veces más. Pasar a coworking cuando haya personal contratado que necesite un lugar fijo. No arrendar oficina propia: con menos de 100 clientes, el ingreso no la paga.

### 2.4 Decisión 2: equipos

| | Usar las propias | Comprar | Alquilar |
|---|---|---|---|
| Costo al mes por laptop | USD 0 | USD 25 | USD 45 |
| Costo en 3 años | USD 0 | USD 900 | USD 1.620 |
| Desembolso inicial | USD 0 | USD 900 | USD 0 |

*Nota.* Precio de compra y de alquiler: supuestos [FALTA-FUENTE: cotizaciones]. Vida útil de 3 años [FALTA-FUENTE: Reglamento de la Ley de Régimen Tributario Interno, art. 28; visto solo en fuente secundaria].

**Recomendación:** empezar con las laptops propias. Comprar al contratar a alguien: en 3 años cuesta casi la mitad que alquilar. Alquilar solo para alguien que estará 6 meses.

### 2.5 Decisión 3: quién hace el trabajo técnico

| | Contratar | Independiente por módulo | Pasante | Compañeros de otras carreras |
|---|---|---|---|---|
| Costo real por hora | USD 8,50 | USD 15,85 | USD 4,17 | USD 2,97 |
| Un módulo de 80 horas | USD 680 | USD 1.268 | USD 333 | USD 238 |
| Compromiso | Fijo cada mes, haya o no clientes | Solo cuando hay trabajo | Hasta 6 meses y 30 horas por semana | Ninguno |
| Continuidad | Alta | Media | Baja | Muy baja |
| De quién es el programa | De la empresa | Hay que firmar la cesión de derechos | Hay que escribirlo en el convenio | En duda si no se firma un acuerdo |

*Nota.* El costo por hora incluye el tiempo de explicar y revisar (supuesto). Pasante: un tercio del salario básico (USD 161) más el 17,5 % de un salario básico al IESS (USD 84), hasta 6 meses y 30 horas por semana (González, 2026). Esa regla de pago está cuestionada por la Corte Constitucional desde 2022 [VERIFICAR en el texto oficial]. Tarifa del independiente: supuesto [FALTA-FUENTE].

**Lectura crítica:** contratar parece barato por hora, pero es el único que se paga con o sin clientes: USD 1.360 al mes son 23 clientes solo para ese sueldo. El pasante y los compañeros son baratos, pero se van, y lo que saben se va con ellos: es el mismo problema que el sistema quiere resolverle a Torvesa.

**Recomendación:**
- el núcleo (servidor, registro y seguridad) lo mantienen los fundadores;
- los módulos que se pueden separar (plantillas, reportes, integraciones) se encargan a un independiente, con contrato de cesión de derechos;
- un pasante para soporte y documentación desde unos 10 clientes;
- compañeros de otras carreras, solo con acuerdo escrito de autoría y entregas cortas;
- contratar a tiempo completo cuando los ingresos cubran ese sueldo durante 6 meses.

### 2.6 Costo de atender a un cliente, precio y margen

| | Nivel 1 · Primer contacto | Nivel 2 · + Memoria comercial | Nivel 3 · + Cotización asistida |
|---|---|---|---|
| Precio al mes por empresa (propuesta) | USD 49 | USD 99 | USD 149 |
| Servidor y base de datos del cliente | USD 5,75 | USD 5,75 | USD 5,75 |
| Sincronización de la bóveda (5 usuarios) | — | USD 23,00 | USD 23,00 |
| Asistente de IA (150 consultas) | — | — | USD 2,24 |
| Soporte (1, 1,5 y 2 horas) | USD 5,20 | USD 7,80 | USD 10,40 |
| **Costo de atenderlo al mes** | **USD 10,95** | **USD 36,55** | **USD 41,39** |
| **Margen por cliente** | **USD 38,05** | **USD 62,45** | **USD 107,61** |
| Margen sobre el precio | 78 % | 63 % | 72 % |
| Costo por solicitud gestionada | USD 0,37 | USD 1,22 | USD 1,38 |

- El cliente promedio (la mitad en el nivel 1, 30 % en el 2 y 20 % en el 3) paga USD 84 y cuesta USD 24,72: deja **USD 59,28 al mes**.
- Además, cada cliente nuevo paga una vez USD 300 por la configuración y la capacitación, que nos cuestan unas 12 horas (USD 62).
- Referencia del mercado: Bitrix24 cobra USD 49 al mes por 5 usuarios y Pipedrive USD 14 por usuario; ninguno incluye la bóveda, el asistente que cita documentos ni el registro verificable.
- [DECIDIR-VÍCTOR: precios por nivel y si se cobra por empresa o por usuario]

### 2.7 Punto de equilibrio

| | Arranque | Crecimiento | Formal |
|---|---|---|---|
| Empresas cliente para **no perder plata de caja** | **3** | 15 | 78 |
| Empresas cliente para **cubrir todo**, incluido el tiempo de los fundadores | **27** | 51 | 126 |
| Ventas al mes en ese punto | USD 2.268 | USD 4.284 | USD 10.584 |
| Clientes que el equipo alcanza a atender en soporte | 59 | 89 | 119 |

La hoja de cálculo trae el gráfico de ingresos y costos según el número de clientes.

**Lectura crítica:**
- Con 3 clientes el negocio ya no pierde caja. Torvesa sería el primero.
- Para que los dos fundadores cobren su medio tiempo hacen falta **27 empresas**. Es una meta de uno a dos años, no de meses [FALTA-DATO: cuántas constructoras pequeñas hay en Quito y cuántas comprarían].
- El tamaño «formal» necesita 126 clientes, pero el equipo solo alcanza a atender 119: **a ese tamaño el precio propuesto no alcanza**. Antes de contratar habría que subir precios, vender más niveles 2 y 3 o automatizar el soporte.
- Lo que más pesa es el soporte, no la nube ni la IA.

## 3. Parte B · Torvesa como cliente

### 3.1 Antes y después, proceso por proceso (escenario base, al mes)

El costo de una hora de quien atiende o cotiza es de **USD 8,50** (sueldo supuesto de USD 1.000, con las cargas de ley).

| Proceso | Antes | Después | Ahorro al mes |
|---|---|---|---|
| 1. Primer contacto | El mensaje espera unas 3,5 horas hasta que alguien lo ve | Meta: 15 minutos (14 veces más rápido) | No es sueldo: vale por las obras que no se pierden |
| 2. Asignación | 8 minutos por solicitud: 4 horas | 1 minuto: media hora | USD 30 |
| 3. Cotización | 3 horas por cotización: 54 horas | 2,1 horas: 37,8 horas | USD 138 |
| 4. Seguimiento | 10 minutos por cotización: 3 horas | 4 minutos: 1,2 horas | USD 15 |
| 5. Historial del cliente | 2 horas por semana por persona: 43,3 horas | 1 hora: 21,7 horas | USD 184 |
| Trabajo nuevo: registrar a mano lo que llega por WhatsApp | No existe | 1 minuto por solicitud | −USD 3 |
| Trabajo nuevo: leer el reporte del lunes | No existe | 15 minutos por semana | −USD 9 |
| **Tiempo: total** | | **41,7 horas liberadas** | **USD 354** |
| Obras que se dejan de perder | | 0,3 al mes (3,6 al año) | USD 450 |
| **Beneficio total al mes** | | | **USD 804** |

*Nota.* Supuestos del escenario base: 30 solicitudes al mes, 60 % llega a cotización, 5 usuarios, se pierde el 20 % antes del primer contacto y el sistema baja esa pérdida en una cuarta parte, se cierra el 20 %, obra de USD 15.000 con 10 % de margen. La espera actual sale del censo de 5 personas (Bermeo y Segura, 2026, p. 10), que no mide solicitud por solicitud [FALTA-DATO: líneas base de M1 a M4].

En los tres escenarios:

| | Pesimista | Base | Optimista |
|---|---|---|---|
| Horas liberadas al mes | 8 | 42 | 105 |
| Ahorro de tiempo al mes | USD 48 | USD 354 | USD 1.151 |
| Obras recuperadas al mes | 0 | 0,3 | 0,7 |
| Beneficio total al mes | USD 48 | USD 804 | USD 2.663 |

### 3.2 Cuánto cuesta y cuánto tarda ponerlo en marcha

| | Opción 1 · Lo arma y lo opera por su cuenta | Opción 2 · Lo contrata como servicio (nivel 3) |
|---|---|---|
| Inversión inicial | USD 2.893 (160 horas de desarrollo, capacitación y reserva) | USD 470 (USD 300 de configuración + 20 horas del equipo en capacitarse) |
| Tiempo para tenerlo listo | Unas 4 semanas | Unas 2 semanas (supuesto) |
| Gasto de operación al año | USD 2.213 | USD 1.788 |
| Gasto total al mes, con la inversión repartida en 3 años | USD 265 | USD 162 |
| Quién lo mantiene | Torvesa tiene que conseguir soporte | Incluido |

Capacitar a las 5 personas toma 4 horas a cada una: 20 horas, que valen USD 170 de su tiempo.

### 3.3 ¿Le conviene? Tres años

| Indicador | Pesimista | Base | Optimista |
|---|---|---|---|
| **Opción 1 · por su cuenta** | | | |
| VAN | −USD 10.378 | USD 12.388 | USD 69.301 |
| TIR | No existe | 181 % | 1.494 % |
| ROI a 3 años | −89 % | 173 % | 1.231 % |
| Meses para recuperar | Más de 36 | 7,6 | 0,8 |
| Obras al año que pagan el sistema, sin ahorro de tiempo | 7,1 | 2,1 | 1,1 |
| **Opción 2 · como servicio** | | | |
| VAN | −USD 3.490 | USD 15.832 | USD 70.357 |
| TIR | No existe | 1.107 % | 5.479 % |
| ROI a 3 años | −75 % | 347 % | 1.462 % |
| Meses para recuperar | Más de 36 | 1,1 | 0,2 |
| Obras al año que pagan el sistema, sin ahorro de tiempo | 3,0 | 1,3 | 0,9 |

**Cómo se lee:**
1. **VAN** es lo que queda a favor en 3 años, en dinero de hoy. Si es positivo, conviene.
2. La **TIR** sale enorme porque la inversión es muy pequeña. No es una promesa: hay que mirar el VAN y el número de obras.
3. **Punto de equilibrio de Torvesa:** como servicio, el sistema se paga si recupera **1,3 obras al año** (una cada 9 meses). En el escenario base, el ahorro de tiempo ya lo cubre solo.
4. **El pesimista pierde en las dos opciones**, y se dice: con 15 solicitudes al mes y ninguna obra recuperada, el nivel 3 no se paga. Ahí lo sensato es el nivel 1, de USD 49 al mes, que casi iguala los USD 48 de ahorro.
5. Contratar el servicio es mejor para Torvesa que armarlo: menos inversión, menos riesgo y soporte incluido.

### 3.4 Qué cambió frente al modelo v0.1

| | v0.1 | v0.2 | Por qué |
|---|---|---|---|
| Inversión inicial, opción 1 | USD 2.893 | USD 2.893 | Mismos supuestos |
| Gasto de operación al año, opción 1 | USD 2.213 | USD 2.213 | Mismos precios |
| VAN base, opción 1 | USD 11.557 | USD 12.388 | Se sumó el ahorro en asignación y seguimiento (+USD 45 al mes) y se restó el trabajo nuevo (−USD 13 al mes) |
| Obras al año que pagan el sistema | 2,6 | 2,1 | La cuenta es distinta: aquí la inversión se reparte en 3 años, sin interés ni adopción gradual; v0.1 lo calculó de otra forma. Las dos cifras dicen lo mismo: entre 2 y 3 obras |
| Opción de contratarlo como servicio | No estaba | VAN de USD 15.832 | Nueva |
| AWS con búsqueda gestionada | Solo Amazon Q Business (unos USD 117 al mes) | También Bedrock Knowledge Bases (unos USD 5 al mes más el modelo) | Precio que v0.1 no tenía. La matriz de herramientas v0.1 debería revisarse con este dato |

Las cifras del Cap. IV del borrador 2 (VAN de USD 11.557 y «unas 3 obras al año») siguen siendo válidas como orden de magnitud. [DECIDIR-VÍCTOR: si el Cap. IV pasa a usar las cifras de v0.2]

## 4. Parte C · Dónde viven la bóveda y el asistente

### 4.1 Opciones (5 usuarios, menos de 1 GB de notas)

| Opción | Costo al mes | Lo bueno | Lo malo |
|---|---|---|---|
| Bóveda en cada equipo, sincronizada con Git | USD 0 | Gratis; guarda el historial de cambios | En el celular es inestable; pide a alguien que sepa |
| **Bóveda con Obsidian Sync** | **USD 23** | Simple en el celular; cifrado; funciona sin conexión | Pago por usuario |
| **Asistente como hoy: programa propio + pago por consulta** | **USD 2** | Solo se paga lo que se usa; ya funciona | Depende de un proveedor de IA |
| AWS, búsqueda gestionada (Bedrock Knowledge Bases) | USD 5 + el modelo | Crece a muchas empresas | Hay que administrar AWS |
| AWS, OpenSearch Serverless clásico | USD 175 (el doble en producción) | Potente | Caro para este tamaño |
| Amazon Q Business | USD 117 | Asistente listo | El índice cuesta aunque nadie pregunte |
| Modelo propio entrenado en AWS | USD 17.155 | — | No hace falta: ver 4.4 |

*Nota.* Precios oficiales del 10-nov-2026; los de Bedrock Knowledge Bases se leyeron con extracción automática [VERIFICAR abriendo la página]. El servidor propio no tiene precio verificado [FALTA-FUENTE].

**Recomendación:** Obsidian Sync para la bóveda y pago por consulta para el asistente: unos **USD 25 al mes**. Como la bóveda vive también en cada equipo, se puede consultar sin luz ni señal.

### 4.2 La capa gratuita de AWS

- Da **USD 100 de crédito** al abrir la cuenta y hasta USD 100 más por explorar servicios (AWS, s. f.).
- La cuenta gratuita **se cierra a los 6 meses** o cuando se acaban los créditos, lo que pase primero.
- Hay más de 30 servicios con una cuota mensual gratis permanente, pero no se verificó que los de IA estén entre ellos [VERIFICAR].
- **Conclusión:** sirve para probar durante unos meses, no para operar el sistema de una empresa.

### 4.3 ¿Y si se quedan sin consultas?

Hay dos formas de pagar la IA, y son cosas distintas:

| | Suscripción (Claude Pro, Google AI Pro) | Pago por consulta (API) |
|---|---|---|
| Para qué es | Para que **una persona** converse con la aplicación | Para que **el sistema** haga consultas solo |
| Precio | USD 20 al mes por persona (USD 200 al año). El plan de USD 100 es mensual, no anual | USD 0,013 por consulta |
| Límite | Sí: se renueva cada 5 horas y tiene tope semanal | No hay tope: se paga lo que se usa |
| Costo para Torvesa | 5 personas: USD 100 al mes | 150 consultas: **USD 1,95 al mes** |

- Una suscripción de USD 20 solo sale a cuenta desde **1.538 consultas al mes**. Torvesa usaría 150: diez veces menos.
- Si el uso se multiplica por 10, el pago por consulta sube a USD 19,50 al mes.
- El asistente del sistema no puede «quedarse sin consultas» como una suscripción. Lo que puede pasar es que el servicio se caiga o suba de precio.

**Plan de respaldo:**
1. un tope de gasto mensual en la cuenta del proveedor [VERIFICAR cómo se configura];
2. un modelo de respaldo más barato: con Claude Haiku 5.5 el mismo uso cuesta USD 0,10 al mes;
3. guardar los borradores ya hechos por tipo de obra, para reutilizarlos;
4. modo sin IA: la plantilla se abre vacía y la persona la llena. **El primer contacto en 15 minutos no depende de la IA.**

### 4.4 «Entrenar un modelo con la bóveda» no es lo mismo que «buscar en la bóveda»

| | Buscar en la bóveda (RAG) | Entrenar un modelo propio |
|---|---|---|
| Qué es | El modelo no cambia. Antes de responder, el sistema busca las notas que sirven y se las pasa | El modelo «memoriza» los textos |
| ¿Dice de dónde sacó la respuesta? | Sí | No |
| Si cambian los datos | La respuesta cambia al instante | Hay que volver a entrenarlo |
| Datos personales | Se quedan en la bóveda y se pueden borrar | Quedan dentro del modelo |
| Costo al mes | Unos USD 2 | USD 17.155 por mantenerlo en servicio (unas 8.800 veces más) |

- **La bóveda de la tesis** tiene fuentes, capítulos y planificación: enseñaría a un modelo sobre la tesis, no sobre los clientes de una constructora. Como base de conocimiento para explicar el proyecto sí sirve, y eso también se hace buscando en ella.
- AWS misma recomienda empezar por la búsqueda cuando las respuestas deben apoyarse en documentos propios (AWS, s. f.).

**Recomendación:** buscar en la bóveda. Cambiaría solo si se cumplen las tres cosas a la vez: miles de cotizaciones aprobadas y anonimizadas con formato fijo, varias empresas cliente que repartan el costo y una persona técnica que mantenga el modelo. Y aun así, el primer paso sería la búsqueda gestionada de AWS (USD 5 al mes más el modelo), no el entrenamiento.

## 5. Lo que falta para pasar de supuesto a dato

**Solo Torvesa lo puede dar:**
- [FALTA-DATO: solicitudes nuevas al mes]
- [FALTA-DATO: clientes que se pierden antes del primer contacto]
- [FALTA-DATO: valor promedio de una obra y margen]
- [FALTA-DATO: tasa de cierre]
- [FALTA-DATO: sueldos de quien cotiza y atiende, y cuántas personas usarán el sistema]
- [FALTA-DATO: número de colaboradores y de clientes en cartera, con respaldo]

**Lo medimos nosotros:**
- [FALTA-DATO: horas por cotización y tiempo de búsqueda del historial, casos de prueba CP-01 y CP-02]
- [FALTA-DATO: consumo real del servidor, con la factura de Diego]
- [FALTA-DATO: tamaño del mercado de constructoras pequeñas en Quito]

**Fuentes por conseguir:**
- [FALTA-FUENTE: tabla de salarios mínimos sectoriales 2026]
- [FALTA-FUENTE: Código del Trabajo: jornada, décimos, vacaciones y fondos de reserva]
- [FALTA-FUENTE: Reglamento de la Ley de Régimen Tributario Interno, art. 28]
- [FALTA-FUENTE: pliego tarifario eléctrico 2026]
- [FALTA-FUENTE: arriendo de oficinas por metro cuadrado en Quito]
- [FALTA-FUENTE: precio de una laptop y de su alquiler; tarifa de un contador y de un desarrollador independiente]
- [FALTA-FUENTE: titularidad del programa hecho por encargo, Código Ingenios]
- [VERIFICAR: Ley de Pasantías y Resolución 380 del IESS en su texto oficial; IVA del 15 %; aporte patronal; precios de Bedrock abriendo la página]

## 6. Limitaciones

- Antes de impuesto a la renta, en dólares constantes y sin valor de rescate.
- Los precios de venta no se han probado con ningún cliente.
- El punto de equilibrio supone que todos los clientes se parecen a Torvesa.
- No se incluye el costo de conseguir cada cliente (visitas, demostraciones) más allá de la publicidad.
- Los precios de los proveedores cambian: hay que volver a consultarlos antes de cerrar el capítulo.

## Referencias

Amazon Web Services. (s. f.). *AWS Free Tier*. Recuperado el 10 de noviembre de 2026, de https://aws.amazon.com/free/

Bermeo, D., y Segura, V. (2026). *TEAMSLASH: Ecosistema digital de gestión de clientes para la Constructora Torvesa* [Informe final del proyecto integrador, Universidad Politécnica Salesiana].

Dirección General de Registro Civil, Identificación y Cedulación. (s. f.). *Adquisición de certificado de firma electrónica en archivo*. Portal Único de Trámites Ciudadanos. Recuperado el 10 de noviembre de 2026, de https://www.gob.ec/dgrcic/tramites/adquisicion-certificado-firma-electronica-archivo

González, P. (2026, 19 de agosto). La afiliación de pasantes al IESS es obligatoria en Ecuador. *Primicias*. https://www.primicias.ec/economia/afiliacion-pasantes-iess-ecuador-empresas-trabajadores-empleo-130565/

Ministerio del Trabajo. (2026). *Informe de gestión, rendición de cuentas, acciones relevantes: Subsecretaría de Empleo y Salarios. Periodo: enero a diciembre 2025*. https://www.trabajo.gob.ec/wp-content/uploads/2026/03/Anexo-Fijacion-Salario-Basico-Planta-Central-2025.pdf

Netlife. (s. f.). *Planes de internet para el hogar*. Recuperado el 10 de noviembre de 2026, de https://www.netlife.ec/planes-hogar/

Superintendencia de Compañías, Valores y Seguros. (s. f.). *Constitución de sociedades por acciones simplificadas*. Portal Único de Trámites Ciudadanos. Recuperado el 10 de noviembre de 2026, de https://www.gob.ec/scvs/tramites/constitucion-sociedades-acciones-simplificadas

Workin.space. (2026, 1 de noviembre). *Oficinas flexibles y coworking en Quito*. Recuperado el 10 de noviembre de 2026, de https://workin.space/es/ecuador/quito
