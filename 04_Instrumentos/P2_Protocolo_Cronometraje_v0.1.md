---
titulo: P2 — Protocolo de cronometraje de cotizaciones y muestra documental
version: v0.1
fecha: 2026-10-11
autor_borrador: Claude Opus 5.5
estado: borrador
metas: [M1, M2, M3]
tags: [instrumentos, protocolo, cronometraje, linea_base]
---

# P2 — Cronometraje de cotizaciones (v0.1)

**Problema que resuelve:** el borrador dice «entre 30 y 44 minutos por cotización» con la fuente «registros de la empresa», que no está identificada (A4). La meta **M2** depende de ese número. Este protocolo lo **mide**.

## Dos tiempos distintos (no mezclarlos)

| | **Tiempo de esfuerzo** (P2-A) | **Tiempo transcurrido** (P2-B) |
|---|---|---|
| Qué es | Minutos de trabajo activo del vendedor para preparar la cotización | Horas o días de calendario desde que llega la solicitud hasta que el cliente recibe algo |
| Meta | **M2** (lo que reduce el asistente de IA) | **M1** (speed-to-lead) y **M3** (pérdida antes del contacto) |
| Cómo | Observación directa con cronómetro | Marcas de tiempo en correo, WhatsApp o CRM |

El «30–44 min» parece ser **esfuerzo**. El problema que plantea la tesis («horas o días») es **transcurrido**. Hay que medir los dos.

---

## P2-A · Cronometraje en vivo (jueves 15 y viernes 16)

**Unidad:** cada cotización que se prepare esos dos días (`COT-01`…). **Censo**: se cronometran todas las que se puedan observar. **Requisitos:** C1-A con la casilla «cronometraje» marcada y la aceptación de gerencia.

**Inicio del reloj:** el vendedor empieza a trabajar en la cotización (abre archivos, busca antecedentes, calcula) **teniendo ya** la solicitud del cliente.
**Fin del reloj:** el documento queda listo para enviar (o se envía).
**Pausas:** si el vendedor deja la cotización para hacer otra cosa, el reloj se pausa y se anota el motivo. Las **esperas** por datos de obra, proveedores o aprobación se registran **aparte**, como espera, no como esfuerzo.

**Segmentos a registrar (hoja `P2A_cronometraje.csv`):**

| Campo | Ejemplo |
|---|---|
| `cot_id` | `COT-03` |
| `fecha` | `2026-10-15` |
| `vendedor` | `COL-07` (código) |
| `observador` | `Diego` |
| `tipo_trabajo` | `[VOCAB: p. ej. adoquinado / acabados / obra civil menor]` |
| `complejidad` | `baja / media / alta` (criterio abajo) |
| `n_rubros` | `6` |
| `t_busqueda_antecedentes_min` | buscar cotizaciones o plantillas anteriores e historial del cliente |
| `t_calculo_min` | cantidades, precios, rubros |
| `t_armado_documento_min` | formato, redacción, PDF |
| `t_revision_min` | revisión propia o de un tercero |
| `t_esfuerzo_total_min` | suma de lo anterior |
| `t_espera_min` | esperas por obra, proveedor o aprobación (no suman al esfuerzo) |
| `reutilizo_plantilla` | `sí / no` |
| `interrupciones` | `2 (llamada; consulta a obra)` |
| `observaciones` | |

**Criterio de complejidad** (provisional, se ajusta con la entrevista I3): **baja** ≤ 3 rubros y sin visita técnica · **media** 4–10 rubros · **alta** > 10 rubros o requiere visita o datos de obra.

**Control de sesgos:**
- **Efecto Hawthorne:** quien es observado trabaja más rápido. Se declara como limitación y se compara con el autorreporte B11 de I1 y con P2-B.
- El observador **no ayuda ni comenta** mientras corre el reloj.
- Si hay muy pocas cotizaciones (por ejemplo, < 5), complementar con un **autorregistro** de cada vendedor durante 2 semanas (misma hoja, en Excel). Se reporta por separado del cronometraje observado.

**Resultado:** mediana y rango intercuartílico del esfuerzo total, por complejidad. Con n pequeño, se reportan los casos individuales y no se hacen pruebas inferenciales.

---

## P2-B · Muestra documental retrospectiva (con autorización C1-C)

**Periodo:** últimos 3 meses (jul–sep 2026) o lo que exista. **Unidad:** cada solicitud de cotización identificable.
**Quién extrae:** una persona de Torvesa, o un investigador supervisado. **Solo se copian marcas de tiempo y categorías**, nunca datos del cliente.

Hoja `P2B_muestra_documental.csv`:

| Campo | Nota |
|---|---|
| `sol_id` | `SOL-001` |
| `canal` | WhatsApp · correo · llamada (con registro) · web · otro |
| `fh_solicitud` | fecha y hora del primer mensaje del cliente |
| `fh_primer_contacto` | primera respuesta de la empresa (no automática) |
| `fh_cotizacion_enviada` | vacío si no se envió |
| `resultado` | ganada · perdida · sin respuesta · en curso · desconocido |
| `perdida_antes_contacto` | sí/no: no hubo primer contacto o el cliente desistió antes |
| `monto_rango` | < 5k · 5–25k · 25–50k · > 50k `[ajustar]` |
| `fuente` | correo / WhatsApp / CRM (de dónde salió la marca de tiempo) |

**Resultado:** mediana del speed-to-lead, % de solicitudes contactadas en ≤ 15 min y en ≤ 1 h, % con más de 24 h, y % de pérdidas antes del contacto. Esa es la **línea base real de M1 y M3**, y reemplaza a la de la encuesta simulada.

**Límites a declarar:** las llamadas sin registro no dejan rastro (subregistro); los WhatsApp personales borrados no se ven; las solicitudes de la muestra son las que dejaron rastro.

---

## Fuentes metodológicas (candidatas, NO verificadas)
- Estudio de tiempos y observación directa: textos clásicos de ingeniería de métodos (por ejemplo, Niebel/Freivalds, *Methods, Standards, and Work Design*). **Por verificar** la edición y el capítulo.
- Speed-to-lead: Oldroyd et al. (2011) para la «primera hora». Para la ventana de 5–15 min, evidencia de 2023+ **por buscar** (fase 1).
- Efecto Hawthorne en estudios de observación: **por buscar** una revisión reciente.
