---
titulo: "Pedido de datos a Torvesa para la línea base (M1 y M3)"
version: v0.1
fecha: 2026-11-27
autor_borrador: "Claude (Victor revisa; Diego lo pasa a la empresa)"
base: "Cap. III v0.7 (Tablas 2 y 4, revisión documental) · Protocolo de validación v0.2 §4"
estado: "propuesta; depende de DEC-21 (tutora) y de la autorización de Torvesa"
marcadores: "DECIDIR-VÍCTOR 2 · FALTA-DATO 1"
tags: [linea-base, M1, M3, pedido, torvesa, anonimizacion]
---

# Pedido de datos a Torvesa para la línea base

## 1. Para qué sirve

Con estos datos se calcula el valor de antes (línea base) de dos metas:

- **M1:** mediana del tiempo entre que llega un pedido y la primera respuesta de Torvesa.
- **M3:** proporción de pedidos que se pierden antes de la primera respuesta.

Las demás metas (M2, M4, M5 y M6) se miden con los casos de prueba y no necesitan datos de la empresa. Es el anexo 10 del Cap. III v0.7.

## 2. Qué se pide (mínimo)

### 2.1 Una fila por pedido de cotización

| N.º | Columna | Qué se escribe | Valores permitidos | Obligatoria | Para qué meta |
|---|---|---|---|---|---|
| 1 | `codigo` | Número consecutivo del pedido | S001, S002, … | Sí | Todas |
| 2 | `fecha_llegada` | Día en que llegó el pedido | AAAA-MM-DD | Sí | M1, M3 |
| 3 | `hora_llegada` | Hora en que llegó | HH:MM (24 horas) | Sí | M1 |
| 4 | `canal` | Por dónde llegó | WhatsApp · Llamada · Correo · Página web · En persona · Referido · Otro | Sí | M1, M3 |
| 5 | `hubo_respuesta` | ¿Torvesa respondió alguna vez? | Sí · No | Sí | M3 |
| 6 | `fecha_primera_respuesta` | Día de la primera respuesta de una persona de Torvesa | AAAA-MM-DD o vacío | Sí, si hubo respuesta | M1 |
| 7 | `hora_primera_respuesta` | Hora de esa respuesta | HH:MM o vacío | Sí, si hubo respuesta | M1 |
| 8 | `cliente_desistio_antes` | ¿El cliente avisó que ya no seguía antes de recibir la respuesta? | Sí · No · No se sabe | Sí | M3 |
| 9 | `hubo_cotizacion` | ¿Se envió una cotización? | Sí · No | Sí | Contexto |
| 10 | `fecha_cotizacion` | Día en que se envió | AAAA-MM-DD o vacío | Si la hay | Contexto |
| 11 | `resultado` | Cómo terminó | Ganado · Perdido · En curso · No se sabe | Sí | M3, contexto |
| 12 | `motivo_perdida` | Por qué se perdió | Sin respuesta a tiempo · Precio · Eligió otra empresa · Cliente desistió · Otro · No se sabe | Solo si se perdió | M3, contexto |
| 13 | `tipo_obra` | Tipo de trabajo pedido | Remodelación · Construcción nueva · Acabados · Mantenimiento · Otro | Opcional | Contexto (CP-01) |
| 14 | `hora_exacta` | ¿Las horas salen de un registro (Sí) o se reconstruyeron de memoria o aproximadas (No)? | Sí · No | Sí | Calidad del dato |
| 15 | `fuente` | De dónde se sacó la fila | Cuaderno · Hoja de cálculo · WhatsApp · Correo · Otro | Sí | Calidad del dato |

**Primera respuesta** = la primera vez que una persona de Torvesa le contesta al cliente (llamada, mensaje o correo). No cuenta una respuesta automática. [DECIDIR-VÍCTOR: que esta definición sea la misma que usa el sistema para el primer contacto; ver Cap. III v0.7]

**Qué NO se escribe en ninguna columna:** nombres, teléfonos, correos, direcciones, cédulas o RUC, montos, nombres de obras, capturas de pantalla, fotos ni audios. No hay columna de observaciones libres para que no se cuele un dato personal.

Las listas de valores de las columnas 4, 12 y 13 son una propuesta: si la empresa usa otras categorías, se ajustan antes de llenar. [DECIDIR-VÍCTOR: aprobar las listas]

### 2.2 Datos generales (una sola vez, sin nombres)

| Dato | Para qué |
|---|---|
| Horario de atención de la oficina (días y horas) | Separar en M1 los pedidos que llegan fuera de horario |
| Cuántas personas responden pedidos de clientes (solo el número) | Describir el proceso actual |
| Si en el periodo hubo días sin atención (feriados, vacaciones) | Explicar valores atípicos |
| Cómo guarda hoy los pedidos (cuaderno, Excel, solo WhatsApp…) | Saber si las horas son exactas o reconstruidas |

### 2.3 Opcional, si la empresa puede

- De 3 a 5 cotizaciones antiguas **sin el nombre ni los datos del cliente y sin precios si así lo prefiere**, para armar las plantillas de los casos de prueba (M2).

## 3. Periodo

- **Del 1 de septiembre al 29 de noviembre de 2026** (los tres meses anteriores a la validación), todos los pedidos de clientes privados.
- No entran los procesos de contratación pública.
- Si la validación empieza en otra fecha, el periodo termina el día anterior a ese inicio.
- Fecha de entrega: [FALTA-DATO: la acuerda Diego con la empresa; lo ideal es antes de que termine la validación].

## 4. Formato

- Un archivo de Excel o Google Sheets, o un CSV, con las columnas de la §2.1 en la primera fila y una fila por pedido. Se entrega la plantilla vacía para que la empresa solo la llene.
- Si la empresa no tiene registro ordenado, una persona de Torvesa revisa el chat y el correo del teléfono de la empresa y copia **solo las fechas y las horas**, marcando `hora_exacta = Sí` (salen del chat con hora) o `No`.
- Lo entrega una persona autorizada por la gerencia, por correo o en memoria USB a Diego.

## 5. Cómo se anonimiza

1. **La anonimización la hace Torvesa antes de entregar.** Los autores nunca ven nombres ni contactos. Si la empresa guarda una lista que une el código S001 con el cliente, esa lista se queda en Torvesa.
2. Al recibir el archivo, se guarda primero en `05_Datos_Campo/_crudo/` (no se sube a Git).
3. Se revisa a mano y con `99_Scripts/auditoria_pii.py` que no haya nombres, teléfonos, correos, cédulas ni textos libres. Si aparece un dato personal, se borra el archivo y se pide uno nuevo a la empresa.
4. La versión limpia se guarda en `05_Datos_Campo/LineaBase_2026-12/` (carpeta que aún no existe: se crea al recibir los datos) con un registro de procedencia: quién lo entregó (cargo), fecha y huella SHA-256 del archivo.
5. A la empresa solo se le devuelven resultados agregados (medianas y porcentajes).

Base legal (Cap. III v0.7): la LOPDP no se aplica a datos anonimizados mientras no se pueda identificar a su titular (art. 2, lit. c) y define la anonimización en el art. 4.

## 6. Qué se calcula con cada columna

| Meta | Cálculo | Columnas |
|---|---|---|
| M1 | Mediana de (primera respuesta − llegada) en minutos, solo pedidos con respuesta; además el % con respuesta en 15 minutos o menos; aparte, los que llegan fuera de horario | 2, 3, 6, 7, 14 y horario |
| M3 | (Pedidos con `hubo_respuesta = No` + pedidos con `cliente_desistio_antes = Sí`) ÷ total de pedidos | 5, 8, 1 |
| Contexto | Pedidos por semana, por canal y por tipo de obra; % cotizados; % ganados | 4, 9, 11, 12, 13 |

---

## 7. Mensaje corto para la empresa (lo envía Diego)

> **Asunto:** Datos para la tesis: horas de los pedidos de clientes (sin nombres)
>
> Buenos días, [nombre de la persona de contacto].
>
> Para la tesis que hacemos con Torvesa necesitamos saber cuánto se tardaba la empresa en responder a los clientes antes del sistema nuevo. Así podremos comparar con lo que pase durante las dos semanas de prueba.
>
> Le pedimos llenar la hoja adjunta con **los pedidos de cotización que llegaron entre el 1 de septiembre y el 29 de noviembre de 2026**. En cada fila va un pedido, con estos datos:
>
> - el día y la hora en que llegó y por dónde (WhatsApp, llamada, correo, etc.);
> - el día y la hora en que alguien de Torvesa le respondió por primera vez, o si nunca se le respondió;
> - si el cliente avisó que ya no seguía antes de que le respondieran;
> - si se envió cotización y cómo terminó (ganado, perdido o en curso).
>
> **No necesitamos ningún nombre, teléfono, correo, dirección ni monto.** Cada pedido va solo con un número (S001, S002…). Si no tienen un registro, basta con revisar el WhatsApp y el correo de la empresa y copiar solo las fechas y las horas; si una hora es aproximada, se marca en la columna de hora exacta.
>
> También nos ayudaría saber el horario de atención de la oficina y cuántas personas responden a los clientes (solo el número).
>
> Los datos se usan solo para la tesis y a la empresa le entregamos los resultados en promedios y porcentajes. Si tiene dudas, me escribe o me llama.
>
> Muchas gracias,
> Diego Bermeo
