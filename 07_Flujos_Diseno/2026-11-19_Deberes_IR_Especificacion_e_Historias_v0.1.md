---
titulo: Deberes 1 y 2 de Ingeniería de Requerimientos (especificación, priorización e historias de usuario)
version: v0.1
fecha: 2026-11-19
autor_borrador: "Claude Opus 5.5 (Víctor revisa)"
asignatura: Ingeniería de Requerimientos, Usabilidad y UX (Ing. Joshua Proaño)
base: "2026-10-27_Elicitacion_Requerimientos_v0.1 · 2026-11-17_Revision_Codigo_Limpio_v0.1 · Resumen_Prueba_Concepto · 02_Fuentes/Metodologia/martin_2008"
entregables: "Escritorio/DEBERES REQUERIMIENTOS 19-nov (Word, PDF y Kano_Calculadora.xlsx)"
estado: borrador; faltan datos de campo reales (Kano, validación, revisión cruzada)
tags: [deber, requerimientos, moscow, kano, invest, historias-de-usuario, victor]
---

# Deberes 1 y 2 de Ingeniería de Requerimientos

> [!warning] Lo que no se inventa
> La encuesta Kano (3 personas reales), la validación con el stakeholder y la verificación del compañero quedan **en amarillo** en los Word hasta tener datos reales. Los generadores están en el scratchpad de la sesión del 19-nov (`deberes/datos.py`, donde `KANO_DATOS` se llena con las respuestas, y `deber1.py`, `deber2.py`, `extras.py`, `leeme.py`). Si el scratchpad se borra, se rehacen desde esta nota.

## Deber 1: los 10 requerimientos

| ID | Origen | Título | Horas | MoSCoW | Valor | Cuadrante | Final |
|---|---|---|---|---|---|---|---|
| RF-01 | RQ-01 | Registro de la solicitud web | 6 | Must | 5 | Quick win | Alta |
| RF-02 | RQ-02 | Aviso de solicitud nueva (≤5 s en 19 de 20) | 8 | Must | 5 | Quick win | Alta |
| RF-03 | RQ-04, RQ-24 | Toma con canal y hora del primer contacto | 10 | Must | 5 | Quick win | Alta |
| RF-04 | RQ-06 | Recordatorio a los 15 min (una vez) | 12 | Must | 4 | Quick win | Alta |
| RF-05 | RQ-09, RQ-13 | Historial del cliente (CP-02, ≤2 min) | 16 | Should | 4 | Estratégico | Media |
| RF-06 | RQ-10/11/12 | Borrador de cotización con asistente | 30 | Could | 4 | Estratégico | Media |
| RNF-01 | RQ-18 | Consentimiento LOPDP | 6 | Must | 5 | Quick win | Alta |
| RNF-02 | RQ-21 | Sin datos personales al servicio de IA | 8 | Must | 4 | Quick win | Alta |
| RNF-03 | RQ-20 | Cuentas individuales | 10 | Must | 3 | Fill-in | Media |
| RNF-04 | RQ-14 | Consulta sin conexión | 24 | Won't | 2 | Evitar | Baja |

- Total: 130 h; promedio: 13 h (esfuerzo alto si es > 13). Valor alto si es ≥ 4.
- **MoSCoW:** en la 1.ª ronda, los Must sumaban 106 h (81,5 %). Se reclasificó RF-05 a Should y RF-06 a Could. Los Must quedan en 60 h (46,2 % del total y 56,6 % sin el Won't).
- **Autoverificación:** se corrigieron RF-02 (puntos 3 y 7), RF-03 (5), RF-04 (3 y 4), RNF-03 (3 y 11) y RNF-04 (3, 4 y 7).
- **Lista de 12 puntos:** la reconstruyó Claude con SWEBOK y 29148, porque la lista de clase no está en la bóveda. **Víctor debe confirmarla.**
- **Valores y prioridad final:** son provisionales hasta tener Kano. Se cambian si un requerimiento sale básico con valor bajo, o indiferente con valor alto.

## Deber 2: backlog

- **HU-01 a HU-08**, en ese orden, salen de RF-01 a RF-06, RNF-01 y RNF-03. RNF-02 quedó como criterio de aceptación de HU-06 y RNF-04 no entra.
- **Roles:** prospecto, coordinador comercial, gerente, colaborador y encargado de cotizar.
- **Épica HU-06** (13 puntos), dividida en:
  - HU-06a, plantilla y sin datos personales: 5 puntos;
  - HU-06b, documentos usados: 2 puntos;
  - HU-06c, aprobación antes de enviar: 3 puntos.
- **HT-01** = DT-01 de la revisión de código (respuesta sin esperar los avisos y con tiempo límite): 3 puntos.
- **SP-01** = medir el aviso de ≤5 s en Railway con la huella activa: 1 día, 2 puntos.
- **Sprints** (capacidad supuesta de 13 puntos):
  - S1 = HU-07, HU-01, HT-01, SP-01 y HU-02 (12 puntos);
  - S2 = HU-03, HU-04, HU-08 y HU-05 (13 puntos);
  - backlog = HU-06a, b y c (10 puntos).

## Fuentes citadas (verificadas el 19-nov)
- Kano et al. (1984), *JJSQC* 14(2), **147-156**, doi:10.20684/quality.14.2_147. Ojo: las pp. 39-48 que circulan por ahí son un error.
- Agile Business Consortium (s. f.), DSDM MoSCoW: Must ≤ 60 % del esfuerzo y los Won't fuera del cálculo. https://www.agilebusiness.org/?p=1907
- Wake (2003, 17-ago), INVEST, xp123.com.
- Martin (2008): pp. 2, 26, 35, 63, 118, 138 y 158 (páginas impresas).
- ISO/IEC/IEEE 29148 (2018) y Washizaki (2025), tomadas de la plantilla de clase.

## Pendiente
1. Víctor: confirmar la lista de 12 puntos; aplicar Kano a 3 personas; recorrido con una persona de Torvesa (vía Diego); elegir al compañero e intercambiar la verificación.
2. Claude: con esos datos, completar las tablas 8, 9 y 11 del Deber 1 y las secciones 6 a 8 del Deber 2, y unir los dos informes de la pareja en un PDF.
3. Detectores de IA (GPTZero, Sapling y QuillBot): pasar el texto final sin nombres ni datos de Torvesa. Son poco fiables (Weber-Wulff et al., 2023).

## 21-nov: encuesta Kano v1.0 (reemplaza a `Kano_Encuesta_para_imprimir`)
- Archivo: `Escritorio/DEBERES REQUERIMIENTOS 19-nov/Encuesta_Kano_Funciones_Sistema_v1.0.pdf` (7 páginas: guía para Diego y hojas E1, E2 y E3). La aplica Diego y las respuestas llegan a Víctor por WhatsApp el 21-nov en la tarde.
- Las funciones 1 a 10 son, en orden, RF-01 a RF-06 y RNF-01 a RNF-04. Las descripciones están reescritas en el lenguaje de quien atiende clientes.
- Agrega importancia de 1 a 5 (sirve para desempatar cuando los 3 encuestados dan categorías distintas), la casilla «No entendí» (se cuenta como cuestionable), tres preguntas abiertas y el perfil (iniciales, edad, cargo, años atendiendo clientes, si trabaja en Torvesa y cómo se aplicó).
- Se puede reusar en la tesis. Antes de aplicarla al personal de Torvesa hace falta el permiso de la gerencia; mientras no llegue, sirven personas de otras empresas que hagan el mismo trabajo.
- Las hojas llenas tienen iniciales: van a `05_Datos_Campo/_crudo/`, nunca a la bóveda que se sube.
- Generador: `scratchpad/kano/encuesta_kano.py` (sesión del 21-nov).

## 22-nov: Kano con datos reales (Deber 1 listo)
- La hoja que mandó Diego en la mañana **era una simulación** (lo decía su página 8 y tenía fechas del 25 y el 26-nov). No se usó.
- Se pasó la encuesta a un Google Forms (`Crear_Forms_Kano.gs`, en el Escritorio) y respondieron **5 personas reales el 22-nov**: 4 de compras o abastecimiento y 1 directora o director de un asilo, todas de Quito y ninguna de Torvesa.
- **Resultado:** 8 de 10 Indiferente; RF-04 de deleite (satisfacción 0,60); RF-06 básico por desempate (molestia −0,60). La importancia media va de 3,6 a 4,6.
- **Limitaciones** declaradas en el deber: confusión con «Lo espero», el perfil no es el público objetivo y E5 respondió igual las 10 funciones. Kano no baja ninguna prioridad.
- El Deber 1 se regeneró sin pendientes (Tablas 8 a 10, Tabla 12 y anexo con 5 tablas de respuestas). Las tablas siguientes se renumeraron.
- **Sigue pendiente en el Deber 2:** el recorrido con el stakeholder y la verificación del compañero (Tablas 16 a 18).
- **22-nov, más tarde: 7 respuestas.** Se sumaron E6 (atención al cliente de un negocio artesanal) y E7 (jefe de ventas de una constructora, la única persona del público objetivo).
  - Resultado: 6 de 10 Indiferente; RF-01 y RF-03 De rendimiento; RF-04 De deleite (0,71); RF-06 Básico (−0,57). RF-01, RF-03 y RF-06 se definieron por desempate.
  - E5, E6 y E7 respondieron en serie. Sin ellas: 9 Indiferente y RF-04 De deleite.
  - Se agregaron 2 figuras Kano (barras por categoría y satisfacción contra molestia). La matriz pasa a ser la Figura 3. El deber queda en 18 páginas.
- **22-nov (noche): versión final del Deber 1 (entregado).**
  - MoSCoW con 4 Must: RF-01, RF-02, RF-03 y RNF-01 (30 h, 23,1 %). RF-04, RF-05 y RNF-03 pasan a Should; RF-06 y RNF-02 a Could; RNF-04 queda en Won't.
  - Prioridad final: 4 altas, 5 medias y 1 baja.
  - Formato: todo vertical, sin fechas de las respuestas, perfiles por columnas y lenguaje de estudiante intermedio (skill voz-victor).
  - El Deber 2 de Víctor (`Deber2_Historias_Validacion_Segura_Bermeo_parte_Victor`) pasa a Diego, con HU-04 en Media. Faltan la validación con un stakeholder, la verificación de Diego y la reflexión.
- **22-nov, más tarde: Deber 2 v2 (parte de Víctor).**
  - **HT-01 pasa a ser una refactorización** (RF-01 y RF-02 de la revisión de código del 17-nov): los estados con los nombres del negocio (Nueva, En contacto, Cotizada, Ganada y Perdida) y en una sola lista. Hoy "Cerrado" significa Ganada y "Archivado" significa Perdida.
  - **SP-01** mide el aviso en el servidor real y compara tres opciones (A: responder primero; B: tiempo límite de 4 s; C: dejarlo como está). Se apoya en la DT-01 de la misma revisión.
  - Las dos van con el formato de la plantilla de clase (`Plantilla_HU_Spike_Refactor_DeudaTecnica.docx`).
  - **Stakeholder:** basta con 1 por informe (el enunciado dice "un stakeholder del proyecto"), y puede ser el mismo para los dos integrantes. Es el jefe de equipo de ventas y asesor comercial (E7 del Kano). La técnica es una entrevista semiestructurada más un recorrido guiado por Teams.
  - En el Escritorio quedan el guion (`Validacion_Deber2_Guion_Reunion_Teams`) y el acta para firmar (`Validacion_Deber2_Acta_Stakeholder`).
  - **El acta firmada tiene su nombre:** va a `05_Datos_Campo/_crudo/`, nunca a la bóveda que se sube.
  - **Siguen en amarillo:** fecha, duración, hallazgos, evidencia, la verificación de Diego y los dos huecos de la reflexión.
