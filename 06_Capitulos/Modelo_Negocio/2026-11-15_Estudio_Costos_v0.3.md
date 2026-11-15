---
titulo: "Estudio de costos: cuánto cuesta, cuánto se gana y cuándo se paga"
version: v0.3
fecha: 2026-11-15
autor_borrador: "Claude; Víctor revisa y aprueba"
base: "Estudio de costos v0.2 (10-nov), que no se modifica · decisión de Víctor del 15-nov: techo de 20 empresas y precio según el tipo de empresa · precios oficiales consultados entre el 21-oct y el 10-nov-2026"
reemplaza: "Amplía la v0.2. Cambia la parte A (TEAMSLASH como negocio). Las partes B (Torvesa) y C (bóveda y asistente) mantienen sus cifras"
marcadores: "FALTA-DATO 10 · FALTA-FUENTE 8 · VERIFICAR 8 · DECIDIR-VÍCTOR 2"
tags: [costos, modelo-negocio, punto-equilibrio, viabilidad, segmentos, sprint5]
---

# Estudio de costos v0.3

## Resumen de una página

> [!warning] Antes de leer las cifras
> Los **precios de los proveedores** son oficiales, con su página y fecha. Todo lo que es **de las empresas cliente** (solicitudes al mes, clientes perdidos, valor de un trabajo, margen, sueldos) es **SUPUESTO**. Los **precios de venta de TEAMSLASH** son una propuesta nuestra, no un precio probado.

**Qué cambió frente a la v0.2:**
- **Techo de 20 empresas.** En el mejor de los casos, vendiendo por página web y aplicaciones, se llega a 20 empresas cliente. Nada en este estudio supone más. El tamaño «formal» de la v0.2, que pedía 126 clientes, se quitó.
- **El precio depende del tipo de empresa.** Una constructora y una veterinaria no ganan igual con el sistema, ni reciben la plata igual. Se compararon cuatro tipos: constructora pequeña, remodelación, ferretería y veterinaria.
- **Proyección a 3 años**, empresa por empresa.

**Para cada tipo de empresa (al mes, escenario base):**

| | Constructora | Remodelación | Ferretería | Veterinaria |
|---|---|---|---|---|
| Lo que el sistema le deja | USD 818 | USD 417 | USD 257 | USD 167 |
| Cada cuánto llega una venta recuperada | Cada 3,3 meses | Cada 2 meses | Algo más de 1 al mes | 2 al mes |
| Precio propuesto | **USD 149** | **USD 79** | **USD 39** | **USD 25** |
| Parte del beneficio que se lleva el precio | 18 % | 19 % | 15 % | 15 % |

**Para TEAMSLASH (nosotros como negocio):**

| Pregunta | Respuesta |
|---|---|
| ¿Cuántas empresas para no perder plata de caja? | **4** al arrancar |
| ¿Se paga el tiempo de los dos fundadores? | **No del todo.** Con 20 empresas quedan unos **USD 280 al mes para cada uno** |
| ¿Cuánto se gana por hora? | Con 20 empresas, unos **USD 9,75 la hora**, apenas sobre lo que cuesta una hora de desarrollo (USD 8,50). Con 8 empresas, USD 6,16 |
| ¿Y el primer año? | Se pierde un poco de plata en los tres escenarios: entre USD 230 y USD 920 en todo el año |

**La conclusión honesta:** con 20 empresas como techo, TEAMSLASH es un **ingreso complementario** para los dos fundadores, no un sueldo. No alcanza para contratar personal ni para tener oficina. Lo que sí hace es pagar su propia caja desde unas 4 empresas y, en los escenarios base y optimista, dejar algo desde el segundo año. Para Torvesa, el sistema conviene, como en la v0.2.

## 1. Cómo se armó

- Todo está en una hoja de cálculo con fórmulas vivas, que acompaña a este documento: `2026-11-15_Estudio_Costos_v0.3.xlsx`, en la misma carpeta. Se recalculó en Excel sin errores.
- Tiene tres partes:
  - **A**, TEAMSLASH como negocio: hojas A1 a A6. Las hojas **A5** (tipos de empresa) y **A6** (3 años) son nuevas;
  - **B**, Torvesa como cliente: hojas B1 a B3, sin cambios;
  - **C**, dónde viven la bóveda y el asistente: hojas C1 y C2, sin cambios.
- Los valores que se pueden cambiar están en azul con fondo amarillo. Si se cambia el techo, los precios o la cantidad de empresas por año, todo se recalcula.
- Los 30 colaboradores y los 33 clientes en cartera de Torvesa vienen del diseño aprobado y no tienen documento de respaldo. No se usan como dato [FALTA-DATO: nota de la gerencia].
- El diagnóstico de 30 personas es simulado y no se usa.

## 2. Parte A · TEAMSLASH como negocio

### 2.1 Cuánto cuesta una hora de trabajo

Igual que en la v0.2. El sueldo no es el costo: a la empresa una persona le cuesta el sueldo más lo que manda la ley.

| Concepto | Desarrollo | Soporte o ventas |
|---|---|---|
| Sueldo (SUPUESTO) | USD 1.000 | USD 600 |
| **Costo real al mes** (IESS, décimos, vacaciones y fondos de reserva) | **USD 1.360** | **USD 832** |
| **Costo por hora** (160 horas al mes) | **USD 8,50** | **USD 5,20** |

*Nota.* El salario básico es de USD 482 (Ministerio del Trabajo, 2026, p. 2). Los sueldos son supuestos [FALTA-FUENTE: tabla de salarios mínimos sectoriales 2026]. Los porcentajes de ley están sin página [VERIFICAR-PÁG: IESS, Resolución C.D. 515] [FALTA-FUENTE: Código del Trabajo].

Estos USD 8,50 sirven de vara para medir: si TEAMSLASH paga menos que eso por hora, a los fundadores les conviene más un empleo.

### 2.2 Cuánto cuesta operar al mes, en tres tamaños

| Concepto | Arranque (1 a 5 empresas) | Crecimiento (6 a 12) | Techo (13 a 20) |
|---|---|---|---|
| Quiénes trabajan | Los 2 fundadores, unas 10 horas por semana cada uno | Unas 15 horas por semana cada uno | Unas 20 horas por semana cada uno y 10 horas al mes de un independiente |
| Dónde | Desde casa | Desde casa | Desde casa |
| Contador | No | USD 80 | USD 100 |
| Publicidad | USD 30 | USD 60 | USD 100 |
| **Costo fijo al mes, todo incluido** | **USD 891** | **USD 1.341** | **USD 1.861** |
| De eso, lo que sale de caja | USD 161 | USD 271 | USD 451 |
| Por año, todo incluido | USD 10.691 | USD 16.091 | USD 22.330 |

- «Todo incluido» valora el tiempo de los fundadores a USD 8,50 la hora, aunque no cobren, más el desgaste de las laptops.
- «Lo que sale de caja» al arrancar es: servidor y página (USD 46), dos suscripciones de IA para programar (USD 46), publicidad (USD 30), internet y luz (USD 36) y firma electrónica y dominio (USD 3).
- **No hay personal contratado, pasante ni oficina en ningún tamaño.** Con 20 empresas no se pagan (ver 2.3 y 2.5).
- Constituir la empresa como SAS no cuesta nada y no pide capital mínimo (Superintendencia de Compañías, Valores y Seguros, s. f.). La firma electrónica cuesta USD 31,05 por 2 años (Dirección General de Registro Civil, Identificación y Cedulación, s. f.).
- La tarifa del contador es un supuesto [FALTA-FUENTE: tarifa de un contador].

### 2.3 Decisión 1: dónde trabajar

| | Desde casa | Coworking | Oficina privada flexible |
|---|---|---|---|
| Costo por persona al mes | USD 18 | USD 217 | USD 236 |
| Equipo de 2, al año | USD 436 | USD 5.216 | USD 5.658 |
| Qué da | Cero arriendo | Dirección, sala de reuniones, internet y limpieza | Espacio cerrado propio |
| Qué arriesga | No hay dónde recibir clientes | Costo fijo desde el primer mes | El más caro, con contrato |

*Nota.* Coworking, USD 189 por puesto al mes; oficina privada flexible, mediana de USD 205; ambos sin IVA y con todo incluido (Workin.space, 2026). Casa: la mitad de un plan de internet de USD 33,93 (Netlife, s. f.) más la luz de una laptop.

**Recomendación:** trabajar desde casa y reunirse con los clientes en su local, su oficina o la obra. **Con un techo de 20 empresas no se arrienda nada:** un solo puesto de coworking se come el margen de 4 clientes.

### 2.4 Decisión 2: equipos

| | Usar las propias | Comprar | Alquilar |
|---|---|---|---|
| Costo al mes por laptop | USD 0 | USD 25 | USD 45 |
| Costo en 3 años | USD 0 | USD 900 | USD 1.620 |

*Nota.* Precios de compra y alquiler: supuestos [FALTA-FUENTE: cotizaciones]. Vida útil de 3 años [FALTA-FUENTE: Reglamento de la Ley de Régimen Tributario Interno, art. 28].

**Recomendación:** usar las laptops propias. Comprar solo cuando haya que reponer una.

### 2.5 Decisión 3: quién hace el trabajo técnico

| | Contratar | Independiente por módulo | Pasante | Compañeros de otras carreras |
|---|---|---|---|---|
| Costo real por hora | USD 8,50 | USD 15,85 | USD 4,17 | USD 2,97 |
| Compromiso | Fijo cada mes, haya o no clientes | Solo cuando hay trabajo | Hasta 6 meses y 30 horas por semana | Ninguno |
| ¿Cabe con 20 empresas? | **No**: USD 1.360 al mes son 27 empresas promedio | Sí, por encargo | No: USD 245 al mes son 5 empresas | Sí, con acuerdo escrito |

*Nota.* Pasante: un tercio del salario básico más el 17,5 % de un salario básico al IESS (González, 2026). Esa regla de pago está cuestionada por la Corte Constitucional desde 2022 [VERIFICAR en el texto oficial]. Tarifa del independiente: supuesto [FALTA-FUENTE].

**Recomendación:**
- el núcleo (servidor, registro y seguridad) lo mantienen los fundadores;
- los módulos que se pueden separar se encargan a un independiente, con contrato de cesión de derechos, y **se pagan con el cobro de configuración del cliente que los pide**;
- no se contrata a nadie a tiempo completo ni se toma un pasante mientras el techo sea de 20 empresas;
- compañeros de otras carreras, solo con acuerdo escrito de autoría.

### 2.6 El precio depende del tipo de empresa (nuevo)

No es lo mismo venderle el sistema a una constructora que a una veterinaria:
- **La constructora** cobra mucho por una obra (USD 15.000 en el supuesto), pero a ella le queda solo su margen, alrededor del 10 %: el resto se va en material y mano de obra. Además, esa plata llega de golpe y cada varios meses.
- **La veterinaria** vive de lo que factura cada mes, con ventas pequeñas (una consulta de USD 30) que se repiten: el cliente vuelve a vacunar o a control.

Por eso el precio se pone según lo que el sistema le deja a cada una, con una regla: **el precio no se lleva más del 25 % de lo que el sistema le deja al cliente**. El cliente se queda con al menos 3 de cada 4 dólares.

**Datos de cada tipo (todos SUPUESTOS):**

| | Constructora pequeña | Remodelación | Ferretería | Veterinaria |
|---|---|---|---|---|
| Solicitudes o contactos al mes | 30 | 40 | 80 | 120 |
| Valor de un trabajo o venta | USD 15.000 | USD 3.000 | USD 400 | USD 30 |
| Margen que le queda a la empresa | 10 % | 20 % | 15 % | 50 % |
| Compras al año de un cliente recuperado | 1 | 1 | 3 | 4 |
| Contactos que hoy se pierden sin respuesta | 20 % | 25 % | 15 % | 10 % |
| Personas que usan el sistema | 5 | 3 | 2 | 2 |
| Nivel del producto con el que entra | 3 (todo) | 2 (con memoria) | 1 (primer contacto) | 1 (primer contacto) |

*Nota.* La constructora repite los supuestos del escenario base de Torvesa (parte B). En los cuatro tipos, el sistema reduce en una cuarta parte los contactos que se pierden [FALTA-DATO: línea base de M3 por tipo de empresa]. Los demás valores son estimaciones del equipo [FALTA-DATO: datos de al menos una empresa de cada tipo].

**Lo que el sistema le deja a cada una, y cuánto puede pagar:**

| | Constructora | Remodelación | Ferretería | Veterinaria |
|---|---|---|---|---|
| Ahorro de tiempo al mes | USD 368 | USD 117 | USD 41 | USD 41 |
| Ventas recuperadas al mes | 0,3 | 0,5 | 1,2 | 2,1 |
| Cada cuánto llega una | **Cada 3,3 meses** | Cada 2 meses | Algo más de 1 al mes | 2 al mes |
| Margen de esas ventas (plata que entra) | USD 450 | USD 300 | USD 216 | USD 126 |
| **Beneficio total al mes** | **USD 818** | **USD 417** | **USD 257** | **USD 167** |
| **Precio propuesto** | **USD 149** | **USD 79** | **USD 39** | **USD 25** |
| Parte del beneficio que se lleva | 18 % | 19 % | 15 % | 15 % |
| Precio máximo con la regla del 25 % | USD 205 | USD 104 | USD 64 | USD 42 |
| Le queda solo en plata, después de pagar | USD 301 | USD 221 | USD 177 | USD 101 |
| Cobro único de configuración | USD 300 | USD 200 | USD 100 | USD 80 |
| Meses para recuperar ese cobro | Menos de 1 | Menos de 1 | Menos de 1 | Menos de 1 |

**Cómo se lee:**
1. **El ahorro de tiempo no es plata que entra.** Las personas siguen cobrando su sueldo. Es tiempo que pueden usar en otra cosa. Por eso se separa lo que sí entra en efectivo: el margen de las ventas que el sistema ayuda a no perder.
2. **La constructora gana más con el sistema, pero cobra a saltos.** Recupera una obra cada 3 o 4 meses, en promedio. Durante esos meses paga USD 149 sin ver la venta; cuando llega, le deja unos USD 1.500. Por eso le conviene el pago mensual y no un pago grande al inicio.
3. **La veterinaria paga poco, pero ve el resultado cada mes.** Con USD 25 cumple la regla con holgura. Más caro no tiene sentido: el sistema le deja USD 167 en total.
4. **Los cuatro tipos cumplen la regla del 25 %** con los precios propuestos. Si se cobrara el máximo de la regla, con las 20 empresas entrarían unos USD 2.150 al mes en vez de USD 1.516.

[DECIDIR-VÍCTOR: precios por tipo de empresa; si se cobra el precio propuesto o se acerca al máximo de la regla.]

### 2.7 Costo de atender a un cliente y margen

El costo depende del nivel del producto, no del tipo de empresa:

| | Nivel 1 · Primer contacto | Nivel 2 · + Memoria comercial | Nivel 3 · + Cotización asistida |
|---|---|---|---|
| Servidor y base de datos | USD 5,75 | USD 5,75 | USD 5,75 |
| Sincronización de la bóveda (5 usuarios) | — | USD 23,00 | USD 23,00 |
| Asistente de IA (150 consultas) | — | — | USD 2,24 |
| Soporte (1, 1,5 y 2 horas) | USD 5,20 | USD 7,80 | USD 10,40 |
| **Costo de atenderlo al mes** | **USD 10,95** | **USD 36,55** | **USD 41,39** |

Con los precios por tipo:

| | Constructora | Remodelación | Ferretería | Veterinaria |
|---|---|---|---|---|
| Precio | USD 149 | USD 79 | USD 39 | USD 25 |
| Costo de atenderla | USD 41,39 | USD 36,55 | USD 10,95 | USD 10,95 |
| **Margen para TEAMSLASH** | **USD 107,61** | **USD 42,45** | **USD 28,05** | **USD 14,05** |

- Con la mezcla del techo (6 constructoras, 4 de remodelación, 4 ferreterías y 6 veterinarias), la empresa promedio paga **USD 75,80**, cuesta USD 25,20 y deja **USD 50,60 al mes**.
- Una constructora deja lo mismo que 8 veterinarias. **Las constructoras sostienen el negocio**; las veterinarias y ferreterías suman, pero poco.

### 2.8 Punto de equilibrio, con el techo de 20

| | Arranque (1 a 5) | Crecimiento (6 a 12) | Techo (13 a 20) |
|---|---|---|---|
| Empresas para **no perder plata de caja** | **4** | **6** | **9** |
| ¿Cabe en su tamaño? | Sí | Sí | Sí |
| Empresas para **cubrir todo**, con el tiempo de los fundadores a USD 8,50 la hora | 18 | 27 | 37 |
| ¿Cabe en su tamaño? | **No** | **No** | **No** |
| Lo que queda al mes con 20 empresas, después de pagar la caja | USD 851 | USD 741 | USD 561 |
| Precio promedio que haría falta para cubrir todo con 20 | USD 70 | USD 92 | USD 118 |

La hoja de cálculo trae el gráfico de ingresos y costos de 0 a 20 empresas.

**Lectura crítica:**
- **La caja se cubre pronto**, con 4 empresas. Torvesa sería la primera.
- **El tiempo de los fundadores no se cubre por completo en ningún tamaño**, si cada uno reserva 10 a 20 horas por semana y esas horas se valoran a USD 8,50. Para cubrirlo con 20 empresas, el precio promedio tendría que subir de USD 76 a USD 118.
- Pero las horas que el trabajo **pide de verdad** son menos que las que se reservan (ver 2.9). Contando solo esas, con 20 empresas el pago por hora llega a USD 9,75.
- Lo que más pesa es el soporte, no la nube ni la IA.

### 2.9 TEAMSLASH en 3 años (nuevo)

Empresas cliente al final de cada año:

| | Pesimista | Base | Optimista |
|---|---|---|---|
| Año 1 | 1 (Torvesa) | 2 (Torvesa y una veterinaria) | 3 |
| Año 2 | 2 | 5 | 10 |
| Año 3 | 3 | 8 | **20 (el techo)** |

En el optimista, el año 3 tiene 6 constructoras, 4 de remodelación, 4 ferreterías y 6 veterinarias. No se cuentan clientes que se van: si alguno se va, el resultado es peor.

| | Pesimista | Base | Optimista |
|---|---|---|---|
| Lo que queda para los 2 fundadores, año 1 | −USD 923 | −USD 727 | −USD 226 |
| Año 2 | −USD 319 | USD 1.525 | USD 2.507 |
| Año 3 | USD 724 | USD 2.519 | USD 6.747 |
| **Año 3, por fundador al mes** | **USD 30** | **USD 105** | **USD 281** |
| Horas al mes que pide el negocio en el año 3 (los dos) | 25 | 34 | 58 |
| **Año 3, pago por hora** | **USD 2,40** | **USD 6,16** | **USD 9,75** |
| Ingresos en 3 años | USD 6.494 | USD 13.104 | USD 24.708 |
| Lo que queda para los dos en 3 años | −USD 518 | USD 3.317 | USD 9.028 |
| Valor de hoy de lo que queda (VAN) | −USD 568 | USD 2.360 | USD 6.958 |

*Nota.* «Lo que queda» es lo que entra (mensualidades y cobros de configuración) menos los servicios de cada cliente (nube, bóveda e IA) y el costo fijo de caja. Con eso se paga el tiempo de los fundadores, incluido el soporte. Las horas que pide el negocio suman el soporte, conseguir y configurar cada cliente nuevo (20 horas por cliente, SUPUESTO) y 20 horas al mes para mantener el núcleo (SUPUESTO). No hay inversión inicial: las laptops ya existen y la SAS no cuesta. El VAN usa las mismas tasas que la parte B.

**Lectura crítica:**
1. **El primer año se pierde un poco** en los tres escenarios: entre USD 226 y USD 923 en todo el año, repartido entre los dos. Es el costo de arrancar.
2. **Con 8 empresas (base), el año 3 deja unos USD 105 al mes a cada fundador**, a USD 6,16 la hora: menos que un empleo. Es un ingreso extra, no un sueldo.
3. **Con 20 empresas (optimista, el techo), deja unos USD 280 al mes a cada uno**, a USD 9,75 la hora. Es el mejor caso realista, y aun así es un complemento.
4. **Lo que más mueve el resultado es cuántas constructoras entren**, porque cada una deja lo de 8 veterinarias. Si el optimista tuviera 10 constructoras en vez de 6 (y 2 veterinarias en vez de 6), el resultado sería bastante mejor (se puede probar en la hoja A6 del Excel).
5. **El pesimista no se paga en 3 años**, y se dice: con 3 empresas, el negocio apenas cubre su caja.

## 3. Parte B · Torvesa como cliente

Sin cambios de cifras frente a la v0.2. Torvesa es el tipo «constructora pequeña» de la sección 2.6, con nivel 3 a USD 149 al mes.

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

### 3.3 ¿Le conviene? Tres años

| Indicador | Pesimista | Base | Optimista |
|---|---|---|---|
| **Opción 1 · por su cuenta** | | | |
| VAN | −USD 10.378 | USD 12.388 | USD 69.301 |
| Meses para recuperar | Más de 36 | 7,6 | 0,8 |
| Obras al año que pagan el sistema, sin ahorro de tiempo | 7,1 | 2,1 | 1,1 |
| **Opción 2 · como servicio** | | | |
| VAN | −USD 3.490 | USD 15.832 | USD 70.357 |
| Meses para recuperar | Más de 36 | 1,1 | 0,2 |
| Obras al año que pagan el sistema, sin ahorro de tiempo | 3,0 | 1,3 | 0,9 |

**Cómo se lee:**
1. **VAN** es lo que queda a favor en 3 años, en dinero de hoy. Si es positivo, conviene. La TIR no se muestra aquí: con inversiones tan pequeñas sale enorme y no dice nada útil (está en la hoja B3).
2. **Como servicio, el sistema se le paga a Torvesa si recupera 1,3 obras al año** (una cada 9 meses). En el escenario base, el ahorro de tiempo ya lo cubre solo.
3. **El pesimista pierde en las dos opciones**, y se dice. Ahí lo sensato es el nivel 1, que casi iguala los USD 48 de ahorro.
4. Contratar el servicio es mejor para Torvesa que armarlo: menos inversión, menos riesgo y soporte incluido.

## 4. Parte C · Dónde viven la bóveda y el asistente

Sin cambios frente a la v0.2.

| Opción | Costo al mes | Lo bueno | Lo malo |
|---|---|---|---|
| Bóveda en cada equipo, sincronizada con Git | USD 0 | Gratis; guarda el historial de cambios | En el celular es inestable; pide a alguien que sepa |
| **Bóveda con Obsidian Sync** | **USD 23** | Simple en el celular; cifrado; funciona sin conexión | Pago por usuario |
| **Asistente como hoy: programa propio + pago por consulta** | **USD 2** | Solo se paga lo que se usa; ya funciona | Depende de un proveedor de IA |
| AWS, búsqueda gestionada (Bedrock Knowledge Bases) | USD 5 + el modelo | Crece a muchas empresas | Hay que administrar AWS |
| Amazon Q Business | USD 117 | Asistente listo | El índice cuesta aunque nadie pregunte |
| Modelo propio entrenado en AWS | USD 17.155 | — | No hace falta |

*Nota.* Precios oficiales del 10-nov-2026; los de Bedrock Knowledge Bases se leyeron con extracción automática [VERIFICAR abriendo la página].

**Recomendación:** Obsidian Sync para la bóveda y pago por consulta para el asistente: unos **USD 25 al mes** por empresa de nivel 2 o 3. Con 20 empresas como techo, la ruta de AWS no hace falta: es para cientos de empresas.

- **Capa gratuita de AWS:** USD 100 de crédito al abrir la cuenta y hasta USD 100 más; la cuenta gratuita se cierra a los 6 meses o al acabarse el crédito (AWS, s. f.). Sirve para probar, no para operar.
- **Suscripción frente a pago por consulta:** una suscripción de USD 20 solo sale a cuenta desde 1.538 consultas al mes; Torvesa usaría 150. El pago por consulta cuesta USD 1,95 al mes y no tiene tope.
- **Plan si falla la IA:** tope de gasto [VERIFICAR cómo se configura], un modelo de respaldo más barato (USD 0,10 al mes con Claude Haiku 5.5), borradores guardados por tipo de obra y modo sin IA. **El primer contacto en 15 minutos no depende de la IA.**
- **Buscar en la bóveda, no entrenar un modelo:** buscar cuesta unos USD 2 al mes y cita de dónde sacó cada cosa; entrenar cuesta USD 17.155 al mes y deja los datos personales dentro del modelo.

## 5. Lo que falta para pasar de supuesto a dato

**Solo las empresas lo pueden dar:**
- [FALTA-DATO: solicitudes nuevas al mes, clientes que se pierden antes del primer contacto, valor promedio de una obra y margen, tasa de cierre, sueldos y número de usuarios de Torvesa]
- [FALTA-DATO: número de colaboradores y de clientes en cartera de Torvesa, con respaldo]
- [FALTA-DATO: los mismos datos de al menos una empresa de remodelación, una ferretería y una veterinaria, para probar los precios de la sección 2.6]

**Lo medimos nosotros:**
- [FALTA-DATO: horas por cotización y tiempo de búsqueda del historial, casos de prueba CP-01 y CP-02]
- [FALTA-DATO: consumo real del servidor, con la factura de Diego]
- [FALTA-DATO: cuántas empresas pequeñas de cada tipo hay en Quito, para saber si 20 es alcanzable]
- [FALTA-DATO: horas reales de soporte por cliente, cuando Torvesa use el sistema]

**Fuentes por conseguir:**
- [FALTA-FUENTE: tabla de salarios mínimos sectoriales 2026]
- [FALTA-FUENTE: Código del Trabajo: jornada, décimos, vacaciones y fondos de reserva]
- [FALTA-FUENTE: Reglamento de la Ley de Régimen Tributario Interno, art. 28]
- [FALTA-FUENTE: pliego tarifario eléctrico 2026]
- [FALTA-FUENTE: precio de una laptop y de su alquiler; tarifa de un contador y de un desarrollador independiente]
- [FALTA-FUENTE: titularidad del programa hecho por encargo, Código Ingenios]
- [VERIFICAR: Ley de Pasantías y Resolución 380 del IESS en su texto oficial; IVA del 15 %; aporte patronal; precios de Bedrock abriendo la página]

## 6. Limitaciones

- Antes de impuesto a la renta, en dólares constantes y sin valor de rescate.
- Los precios de venta no se han probado con ningún cliente.
- Los cuatro tipos de empresa son estimaciones del equipo: ninguno tiene datos reales todavía, ni siquiera Torvesa.
- No se cuentan los clientes que se van. Si alguno se va, el resultado de TEAMSLASH es peor.
- El techo de 20 empresas es una decisión del equipo, no un estudio de mercado.
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
