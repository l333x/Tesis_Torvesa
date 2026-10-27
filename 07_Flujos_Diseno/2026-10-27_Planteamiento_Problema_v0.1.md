---
titulo: Planteamiento del problema (problem statement) — Atención comercial en Torvesa
version: v0.1
fecha: 2026-10-27
autor_borrador: "Claude Opus 5.5 (Víctor y Diego revisan)"
plantilla: "Problem Statement Template (IPM), adaptada al español"
relacion: "Anexo H del documento de elicitación y análisis de requerimientos v0.1"
word: 2026-10-27_Planteamiento_Problema_v0.1.docx
tags: [requerimientos, problem-statement, torvesa]
---

# Planteamiento del problema

## Control del documento

| Campo | Contenido |
|---|---|
| Identificador | ELIC-H-01 |
| Responsables | Víctor Segura Heredia · Diego Bermeo Torres |
| Fecha de emisión | 27-oct-2026 |
| Versión | 0.1 (borrador para revisión) |

| Versión | Fecha | Cambios |
|---|---|---|
| 0.1 | 27-oct-2026 | Primera versión, con la información del proyecto integrador TEAMSLASH y de la revisión documental de octubre de 2026 |

| Rol | Nombre | Firma | Fecha |
|---|---|---|---|
| Patrocinador (organización beneficiaria) | Gerencia de Torvesa Constructora | | |
| Revisión académica | Ing. Tania Chicaiza, tutora | | |
| Equipo del proyecto | Víctor Segura Heredia · Diego Bermeo Torres | | |

## Definición del problema

El equipo comercial de la Constructora Torvesa no tiene un lugar común donde lleguen, se asignen y se registren las solicitudes de cotización. Las solicitudes entran por el WhatsApp personal de socios e ingenieros que pasan buena parte de la jornada en obra, por lo que nadie se entera a tiempo, nadie queda como responsable y cada cotización se prepara casi desde cero. El conocimiento de cada cliente queda en la memoria y en el celular de quien lo atendió. El problema es medible por tres vías:
- el tiempo hasta el primer contacto;
- el tiempo de elaboración de cada cotización;
- la capacidad de recuperar el historial de un cliente cuando su vendedor no está.

Las tres se miden en la línea base de la tesis.

## Antecedentes del problema

- **Organización:**
  - Torvesa es una constructora de Quito, activa desde 2010;
  - tiene 30 colaboradores y 33 clientes en cartera, datos por confirmar con la nota de la gerencia;
  - vende por proyecto: cada solicitud exige una cotización a medida.
- **Cómo se generó el problema:** la estructura es esbelta y el mismo personal vende y supervisa obra. El problema surge del choque entre ambos roles (Informe Final de TEAMSLASH, 22-jul-2026, p. 7).
- **Censo de validación de mayo de 2026,** aplicado a cinco personas de la gerencia y la operación:
  - más de la mitad de la jornada transcurre en obra;
  - el 40 % revisa los mensajes de clientes cada 3 o 4 horas y el 20 % solo al llegar a casa;
  - 4 de 5 reciben clientes en su WhatsApp personal.
- **Respuesta previa:** el equipo construyó el MVP TEAMSLASH:
  - formulario web;
  - API propia;
  - registro con semáforo;
  - alertas en Slack.

  En simulacros, la alerta llegó en 3,2 segundos y el primer contacto se dio entre 4 y 11 minutos. Aún faltan tres cosas: conservar el conocimiento (plantillas y cotizaciones anteriores), ayudar a preparar las cotizaciones y dar una prueba verificable del historial. Eso es lo que aborda la tesis.
- **Contexto sectorial:**
  - la construcción es uno de los sectores menos digitalizados (Manyika et al., 2015, p. 5);
  - en Ecuador su producción cayó en 2023 y 2024 y se recuperó un 2,7 % en 2025 (Banco Central del Ecuador, 2026, pp. 22–23), un mercado donde perder clientes pesa más.

## Alcance del problema

| Incluido | Excluido |
|---|---|
| Recepción de solicitudes de clientes privados por cualquier canal | Contratación pública (Sistema Nacional de Contratación Pública) |
| Primer contacto, asignación y seguimiento hasta ganar o perder la solicitud | Negociación, facturación y cobranza |
| Elaboración de cotizaciones | Ejecución y avance de obra |
| Conservación y recuperación del historial de cada cliente | Dotación de personal y cargas de trabajo (decisiones de la gerencia) |
| Tratamiento de los datos personales de los clientes (LOPDP) | — |

**Área afectada:**
- el área comercial y técnica que atiende clientes;
- la gerencia, que necesita visibilidad del embudo.

**Restricciones del análisis:**
- el trabajo de campo depende de la autorización de la empresa;
- los datos del diagnóstico simulado (N = 30) no se usan.

## Impacto actual o potencial

| Área de impacto | Descripción | Métrica cuantitativa o cualitativa |
|---|---|---|
| Ventas | Clientes que se van con la competencia antes del primer contacto | Fuga previa al primer contacto, en % de solicitudes (M3). El antecedente estimó USD 15.000 de facturación potencial por cliente perdido; es una estimación interna sin respaldo documental que se reemplaza por la medición |
| Eficiencia operativa | Solicitudes desatendidas durante horas o días | Mediana del tiempo de primer contacto en minutos (M1). El antecedente la sitúa en más de 24 horas, según lo que reportó el personal |
| Eficiencia operativa | Cotizaciones preparadas casi desde cero | Minutos por cotización (M2), con cronometraje |
| Conocimiento organizacional | El historial se pierde si el vendedor no está o se va | Tiempo y aciertos en una prueba de recuperación del historial (M4) |
| Control de la gerencia | No se sabe cuántas cotizaciones hay en curso ni por qué se pierden clientes | Existencia de un reporte semanal con estados y motivos de pérdida (cualitativa) |
| Legal | Datos de clientes en celulares y chats personales, fuera del control de la empresa | Cumplimiento de la LOPDP: consentimiento, minimización y plazos de conservación (lista de verificación) |
| Satisfacción del cliente | Esperas largas y respuestas incompletas | Tiempo de respuesta percibido y calidad de la cotización (encuesta I2 a los 33 clientes) |

## Interesados afectados

**Registro de interesados**

| Nombre o grupo | Rol | Poder | Interés | Contacto |
|---|---|---|---|---|
| Gerencia y representante legal | Patrocinador; decide la adopción | Alto | Alto | Por medio de Diego Bermeo |
| Coordinadores comerciales, socios e ingenieros | Usuarios principales | Medio | Alto | En la empresa |
| Personal que prepara cotizaciones | Usuarios | Medio | Alto | En la empresa |
| Resto de colaboradores | Usuarios secundarios | Bajo | Medio | Encuesta I1 |
| Clientes y prospectos | Afectados; titulares de los datos | Medio | Medio | Encuesta I2 |
| Tutora de la UPS | Revisión académica | Alto | Medio | Revisiones programadas |
| Superintendencia de Protección de Datos Personales | Regulador | Alto | Bajo | — |

Los datos de contacto de las personas no se incluyen en este documento; se guardan aparte, según la LOPDP.

**Mapa de interesados**

| | Interés bajo | Interés medio | Interés alto |
|---|---|---|---|
| Influencia alta | Regulador: mantener satisfecho | Tutora: mantener satisfecha | Gerencia: gestionar de cerca |
| Influencia media | Proveedores de plataformas: monitorear | Clientes: mantener informados | Coordinadores y quienes cotizan: gestionar de cerca e informar |
| Influencia baja | — | Resto de colaboradores: monitorear | — |

## Periodo del problema

El problema existe desde antes de mayo de 2026, cuando el censo lo confirmó; su inicio exacto no está documentado. Persiste porque no hay ningún cambio de proceso en marcha: el MVP TEAMSLASH está desplegado, pero su uso real no se ha medido. No hay datos para saber si empeora; la muestra documental de los últimos tres meses (solo fechas y horas) permitirá ver su evolución reciente.

## Ubicación del problema

- **Física:**
  - la oficina de Torvesa en Quito, donde se preparan las cotizaciones;
  - los frentes de obra, donde se reciben los mensajes con conectividad limitada.
- **Virtual:**
  - los WhatsApp personales y las redes sociales, donde llegan las solicitudes;
  - los celulares, chats y cuadernos, donde quedan las cotizaciones anteriores.

## Análisis de brechas

| Estado actual | Estado deseado | Acciones necesarias |
|---|---|---|
| Las solicitudes llegan a celulares personales y nadie se entera a tiempo | Cada solicitud queda registrada y su responsable recibe una alerta en segundos | Formulario con registro automático, registro manual de las que llegan por WhatsApp y alerta con enlace a la ficha (RQ-01 a RQ-03) |
| No hay responsable ni estado de cada solicitud | Cada solicitud tiene un responsable, un estado y, si se pierde, un motivo | Asignación, estados, recordatorio a los 15 minutos y reporte semanal (RQ-04 a RQ-08) |
| Cada cotización empieza casi de cero | Cotizaciones a partir de plantillas y de cotizaciones anteriores, con un borrador asistido y revisado por una persona | Bóveda con plantillas y asistente de IA con revisión humana (RQ-10 a RQ-12) |
| El historial vive en la memoria de cada vendedor | Cualquier miembro autorizado recupera el historial de un cliente en minutos | Ficha por cliente con código, búsqueda y consulta sin conexión (RQ-09, RQ-13, RQ-14) |
| No hay prueba de quién atendió, qué se ofreció y cuándo | Registro de eventos que no puede alterarse sin que se note | Registro de solo agregar con huellas SHA-256 y verificación (RQ-15 a RQ-17) |
| Datos de clientes en canales personales | Tratamiento conforme a la LOPDP | Consentimiento, cuentas individuales, plazos de conservación y solo códigos hacia la IA (RQ-18 a RQ-21) |

## Causa raíz del problema

**Técnica de los 5 porqués**
1. ¿Por qué los clientes esperan horas o días? Porque nadie ve la solicitud a tiempo.
2. ¿Por qué nadie la ve? Porque llega al celular personal de alguien que está en obra.
3. ¿Por qué llega ahí? Porque la empresa no tiene un canal ni un registro propios para las solicitudes.
4. ¿Por qué no los tiene? Porque la gestión comercial se apoya en las personas, no en procesos ni en herramientas de la empresa: lo que cada uno sabe del cliente no queda escrito en ningún lugar común.
5. ¿Por qué eso afecta también a las cotizaciones y al historial? Porque el mismo conocimiento (precios, rubros, conversaciones) tampoco se conserva, y hay que reconstruirlo cada vez.

**Causa raíz:** el conocimiento comercial es de cada persona y no de la empresa, y no existe un flujo con responsable para cada solicitud. Las alertas resuelven solo el síntoma de la espera. Por eso la solución combina el registro y las alertas (TEAMSLASH) con la bóveda de conocimiento, el asistente y el registro verificable.

**Diagrama de causa y efecto (resumen por categorías)**

| Categoría | Causas |
|---|---|
| Personas | El mismo personal vende y supervisa obra; revisión intermitente del celular |
| Procesos | No hay asignación, estados ni seguimiento definidos; las cotizaciones no se reutilizan |
| Tecnología | No hay un sistema comercial; el WhatsApp personal es el canal principal; el MVP no conserva el conocimiento |
| Entorno | Conectividad limitada en obra; clientes que esperan respuestas inmediatas |
| Información | Cotizaciones y datos de clientes dispersos en celulares, chats y cuadernos |

## Datos, evidencias y anexos de respaldo

- Informe Final del proyecto integrador TEAMSLASH (22-jul-2026):
  - Tabla 1, censo n = 5, pp. 9–10;
  - Tabla 3, resultados del MVP, pp. 23–24.
- Proceso actual (AS-IS) en BPMN, v0.1 (25-oct-2026). Borrador sin validar en campo.
- Capítulo I de la tesis (v0.3, 27-oct-2026): contexto, evidencias y metas M1–M6.
- Inventario de herramientas candidatas, v0.2 (25-oct-2026).
- **Por levantar en Torvesa:**
  - muestra documental de solicitudes de los últimos 3 meses;
  - cronometraje de cotizaciones;
  - encuestas I1 e I2;
  - entrevistas I3.

  Con estos datos se reemplazan las estimaciones del antecedente (más de 24 horas de respuesta y USD 15.000 por cliente perdido) por mediciones.

## Referencias

Banco Central del Ecuador. (2026). *Informe de evolución de la economía ecuatoriana en 2025 y perspectivas 2026*. https://contenido.bce.fin.ec/documentos/Administracion/EvolEconEcu_2025pers2026.pdf

Manyika, J., Ramaswamy, S., Khanna, S., Sarrazin, H., Pinkus, G., Sethupathy, G., y Yaffe, A. (2015). *Digital America: A tale of the haves and have-mores*. McKinsey Global Institute. https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/digital-america-a-tale-of-the-haves-and-have-mores
