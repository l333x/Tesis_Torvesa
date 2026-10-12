"""Genera el cronograma día a día (Scrum, sprints semanales) en Excel + CRONOGRAMA.md.

    python generar_cronograma.py            crea 11_Planificacion/Cronograma_Tesis.xlsx (no sobrescribe)
    python generar_cronograma.py --md       solo regenera CRONOGRAMA.md desde el Excel (versión para la IA)

El Excel es la fuente de verdad para las personas: ahí se marcan estado y fecha real. Este script solo
lo CREA una vez; después, `--md` lee el Excel y actualiza CRONOGRAMA.md (que usa sincronizar_github.py).
"""
from __future__ import annotations

import argparse, sys
from datetime import date, timedelta
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.formatting.rule import FormulaRule, DataBarRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

BOVEDA = Path(__file__).resolve().parents[2]
XLSX = BOVEDA / "11_Planificacion" / "Cronograma_Tesis.xlsx"
MD = BOVEDA / "11_Planificacion" / "CRONOGRAMA.md"
AZUL, COBRE, CLARO = "0B1F3A", "B87333", "EEF2F7"
V, D, A = "Víctor", "Diego", "Ambos"
F_PRO, F_CON, F_MET, F_EVI, F_TEC, F_CAS, F_NOR, F_COS = (f"02_Fuentes/{x}/" for x in (
    "Problema", "Contexto", "Metodologia", "Evidencia_Datos", "Tecnologia_IA", "Casos_Estudio", "Normativa", "Costos_Viabilidad"))
INS, LB, CAP, MN, FL, TU, PL, MAT = ("04_Instrumentos/", "05_Datos_Campo/LineaBase_2026-10/", "06_Capitulos/",
                                     "06_Capitulos/Modelo_Negocio/", "07_Flujos_Diseno/", "08_Reuniones_Tutora/",
                                     "11_Planificacion/", "03_Matriz_Objetivos/")
TOR, UPS, LLAM = "Torvesa (oficina, Quito)", "UPS Quito, en persona", "Llamada Víctor–Diego"
REV = ("Revisar el sprint (qué hicimos, qué no, qué aprendimos), hacer 20 min de «explícame lo tuyo» y planificar el siguiente",
       f"{LLAM} · {PL}Bitacora_Semanal.md y {PL}Cronograma_Tesis.xlsx", "Sección de la semana en la bitácora + hoja del sprint siguiente ajustada",
       "El informe del domingo (21:00) sale con la sección nueva")

# ---------------- ENTREGABLES (= issues de GitHub) ----------------
# id: (issue existente o None, nombre simple, responsable, entregable, criterio de hecho)
ENT = {
 "S1-01": (1, "Buscar y verificar fuentes del problema (tiempo de respuesta, digitalización de la construcción, datos de Torvesa), para respaldar el capítulo 1", V, f"fichas en {F_PRO}", "afirmaciones A1–A10 con estado definido"),
 "S1-02": (2, "Buscar fuentes de metodología, ley de datos (LOPDP), escala SUS en español e IA 2023–2026, para justificar el método", V, f"fichas en {F_MET}, {F_NOR} y {F_TEC}", "afirmaciones A39–A47 con estado"),
 "S1-03": (3, "Armar la matriz afirmación–fuente–estado (corte del miércoles), para decidir qué entra al capítulo 1", V, f"{MAT}2026-10-14_Matriz_Afirmaciones_v0.1.xlsx", "las 47 afirmaciones con estado"),
 "S1-04": (4, "Corregir los instrumentos de campo a la versión 0.2, para aplicarlos en Torvesa", V, f"{INS}2026-10-14_*_v0.2", "aprobados por Víctor e impresos"),
 "S1-05": (5, "Pedir a Torvesa el permiso de campo, la nota de respaldo y el catálogo de servicios, para trabajar con datos oficiales", V, "correo enviado + respuesta", "respuesta recibida o plazo vencido el 14-oct"),
 "S1-06": (6, "Confirmar con Torvesa a qué se dedica (vías, edificios, inmuebles), para usar las palabras correctas en encuestas y tesis", V, "respuesta de Torvesa", "afirmaciones A1–A1d resueltas"),
 "S1-07": (7, "Conversar con la tutora sobre los 5 cambios, para tener su aprobación antes de la Revisión 1", V, f"{TU}2026-10-12_Acta_Conversacion.md", "acta con sus respuestas"),
 "S1-08": (8, "Aplicar la encuesta, las entrevistas y la encuesta a clientes en Torvesa (si autoriza), para tener la línea base real", V, f"{LB}registro_aplicacion.csv", "cada aplicación en el registro de procedencia"),
 "S1-09": (9, "Cronometrar cotizaciones y revisar solicitudes pasadas en Torvesa (si autoriza), para medir los tiempos reales", D, f"{LB}P2A_cronometraje.csv y P2B_muestra_documental.csv", "todas las cotizaciones observables registradas"),
 "S1-10": (10, "Aceptar la invitación, clonar el repo y levantar el buscador RAG, para trabajar en la bóveda compartida", D, "commit de prueba de Diego en GitHub", "rag.py consultar funciona en su PC"),
 "S1-12": (12, "Tabular y anonimizar los datos de campo con el protocolo de procedencia, para que sean confiables", A, LB, "auditoría de datos personales en 0"),
 "S1-13": (None, "Investigar cómo consolidar bóvedas de conocimiento y arquitecturas RAG para negocio, para diseñar la bóveda del sistema", D, f"fichas en {F_TEC} + resumen de 1 página", "≥10 fichas y resumen leído por Víctor"),
 "S1-14": (None, "Investigar flujos de información y diseño de procesos (BPMN), para dibujar los procesos de Torvesa", D, f"fichas en {F_MET}", "≥5 fichas"),
 "S1-15": (None, "Investigar CRMs móviles y herramientas existentes con sus precios, para comparar opciones y calcular costos", D, f"fichas en {F_CAS} y {F_COS}", "≥6 herramientas con precio y fecha de consulta"),
 "S1-16": (None, "Revisar el sprint 1 y planificar el sprint 2", A, f"{PL}Bitacora_Semanal.md", "sección de la semana escrita"),
 "S2-01": (13, "Escribir el capítulo 1 (problema, justificación, objetivos), para tener el primer borrador", V, f"{CAP}2026-10-20_Cap1_Problema_v0.1.docx", "cada cifra con ficha verificada"),
 "S2-02": (14, "Escribir el capítulo 2 (marco teórico), para sustentar el diseño", V, f"{CAP}2026-10-22_Cap2_Marco_Teorico_v0.1.docx", "solo fuentes verificadas"),
 "S2-03": (15, "Escribir el capítulo 3 (metodología), para explicar cómo se investiga", V, f"{CAP}2026-10-25_Cap3_Metodologia_v0.1.docx", "coherente con las decisiones D1 y D2"),
 "S2-04": (16, "Analizar los datos de campo (tablas y gráficos), para la línea base de las metas", D, f"{LB}analisis/", "línea base de M1–M4 y M6 calculada"),
 "S2-05": (17, "Dibujar el proceso actual de Torvesa (AS-IS) en BPMN, para ver dónde se pierde tiempo", D, f"{FL}2026-10-22_AS-IS_v0.1", "validado con lo dicho en las entrevistas"),
 "S2-06": (18, "Hacer el inventario de herramientas candidatas con criterios, para elegir con argumentos", D, f"{FL}2026-10-24_Inventario_Herramientas_v0.1.xlsx", "≥3 opciones por componente"),
 "S2-07": (None, "Armar el lienzo del modelo de negocio y la propuesta de valor, para explicar cómo se vende la idea", V, f"{MN}2026-10-23_Lienzo_Modelo_Negocio_v0.1.docx", "9 bloques completos"),
 "S2-08": (None, "Revisar el sprint 2 y planificar el sprint 3", A, f"{PL}Bitacora_Semanal.md", "sección de la semana escrita"),
 "S3-01": (19, "Presentar el avance a la tutora (capítulos 1–3 y fuentes) en la Revisión 1", V, f"{TU}presentación", "reunión realizada"),
 "S3-02": (20, "Escribir el acta de la Revisión 1 y corregir según sus observaciones", V, f"{TU}acta + capítulos v0.2", "cada observación con responsable y plazo"),
 "S3-03": (21, "Preparar el proceso actual y las gráficas de datos para mostrarlos en la Revisión 1", D, f"{FL}figuras", "incluidas en la presentación"),
 "S3-04": (None, "Escribir cómo estructuré mi bóveda 1 (patrones, no datos), para que Diego diseñe la bóveda del sistema", V, f"{FL}2026-10-30_Patrones_Boveda1_v0.1.docx", "Diego lo leyó y anotó preguntas"),
 "S3-05": (None, "Revisar el sprint 3 y explicarle a Diego los conceptos de negocio", A, f"{PL}Bitacora_Semanal.md", "sesión hecha con Conceptos_Negocio.pdf"),
 "S4-01": (22, "Dibujar los procesos con el sistema (TO-BE), para definir cómo funcionará", D, f"{FL}2026-11-04_TO-BE_v0.1", "cubren los 6 pasos del flujo de atención"),
 "S4-02": (23, "Validar los procesos TO-BE contra los requisitos", V, f"comentarios en {FL}", "cada requisito ligado a un flujo"),
 "S4-03": (24, "Construir la bóveda del sistema a partir de los flujos aprobados", D, f"{FL}Boveda_Sistema/", "estructura y plantillas funcionando"),
 "S4-04": (25, "Escribir los requisitos funcionales y no funcionales", V, f"{CAP}2026-11-03_Requisitos_v0.1.docx", "cada requisito con su origen"),
 "S4-05": (26, "Armar la matriz de decisión de herramientas en Excel (fórmulas vivas)", V, f"{MN}2026-11-05_Matriz_Decision_Herramientas_v0.1.xlsx", "ponderaciones y sensibilidad"),
 "S4-06": (27, "Calcular CAPEX (inversión) y OPEX (gasto mensual) con fuente para cada precio", V, f"{MN}2026-11-07_Modelo_Financiero_v0.1.xlsx (hoja Costos)", "cada precio con enlace y fecha"),
 "S4-07": (None, "Revisar el sprint 4 y planificar el sprint 5", A, f"{PL}Bitacora_Semanal.md", "sección escrita"),
 "S5-01": (28, "Calcular beneficios, VAN, TIR y período de recuperación en 3 escenarios con sensibilidad", V, f"{MN}Modelo_Financiero (hojas Beneficios y Escenarios)", "supuestos con fuente; 3 escenarios"),
 "S5-02": (29, "Escribir la matriz de riesgos", V, f"{CAP}2026-11-12_Riesgos_v0.1.xlsx", "probabilidad × impacto + mitigación"),
 "S5-03": (30, "Escribir el capítulo de normativa (LOPDP)", V, f"{CAP}2026-11-13_Normativa_v0.1.docx", "artículos del texto oficial"),
 "S5-04": (31, "Construir la prueba de concepto (formulario → servidor → bóveda → borrador de cotización)", D, "repositorio de la prueba de concepto", "flujo completo demostrable"),
 "S5-05": (32, "Diseñar los 3 casos de prueba", D, f"{FL}2026-11-14_Casos_Prueba_v0.1.md", "aprobados por Víctor"),
 "S5-06": (None, "Escribir el pitch de 1 página para inversionista", V, f"{MN}2026-11-14_Pitch_1pagina_v0.1.docx", "una página con VAN, TIR y propuesta de valor"),
 "S5-07": (None, "Revisar el sprint 5 y planificar el sprint 6", A, f"{PL}Bitacora_Semanal.md", "sección escrita"),
 "S6-01": (33, "Presentar diseño, flujos, datos y viabilidad a la tutora en la Revisión 2", A, f"{TU}presentación", "reunión realizada"),
 "S6-02": (34, "Escribir el acta de la Revisión 2", V, f"{TU}acta", "observaciones con responsable y plazo"),
 "S6-03": (None, "Revisar el sprint 6 y planificar el sprint 7", A, f"{PL}Bitacora_Semanal.md", "sección escrita"),
 "S7-01": (35, "Incorporar las observaciones de la Revisión 2", A, "versiones nuevas de capítulos y flujos", "cada observación cerrada en el acta"),
 "S7-02": (36, "Preparar la validación del diseño en operación experimental controlada (protocolo, capacitación, permisos)", V, f"{INS}protocolo de validación", "aprobado por Torvesa"),
 "S7-03": (37, "Arrancar la validación del diseño en operación experimental controlada (24-nov) y monitorearla", D, "registro de eventos del sistema", "eventos registrados sin errores"),
 "S7-04": (None, "Escribir el capítulo de diagnóstico con la línea base real", V, f"{CAP}2026-11-28_Cap4_Diagnostico_v0.1.docx", "solo datos con registro de procedencia"),
 "S7-05": (None, "Revisar el sprint 7 y planificar el sprint 8", A, f"{PL}Bitacora_Semanal.md", "sección escrita"),
 "S8-01": (38, "Documentar las herramientas elegidas y descartadas, con justificación", D, f"{FL}Herramientas", "cada decisión con criterio"),
 "S8-02": (39, "Documentar el modelo de datos y el registro de eventos", D, f"{FL}Modelo_Datos", "coincide con la prueba de concepto"),
 "S8-03": (40, "Documentar las plantillas de cotización y la especificación del asistente de IA", D, f"{FL}Asistente_IA", "revisadas por Víctor"),
 "S8-04": (41, "Ejecutar los casos de prueba", D, f"{FL}Resultados_Casos_Prueba", "resultado por caso"),
 "S8-05": (42, "✂ Escribir el manual básico de usuario", D, f"{FL}Manual_Usuario", "un usuario de Torvesa lo puede seguir"),
 "S8-06": (None, "Escribir el capítulo de diseño del sistema y viabilidad", V, f"{CAP}2026-12-04_Cap5_Diseno_Viabilidad_v0.1.docx", "integra flujos, costos y VAN/TIR"),
 "S8-07": (None, "Revisar el sprint 8 y planificar el sprint 9", A, f"{PL}Bitacora_Semanal.md", "sección escrita"),
 "S9-01": (43, "Hacer la medición «después» (7–9 dic)", A, f"05_Datos_Campo/ (carpeta Post)", "mismos instrumentos e indicadores que la línea base"),
 "S9-02": (44, "Comparar el antes y el después (análisis pre-post) y escribir resultados", V, f"{CAP}2026-12-12_Cap6_Resultados_v0.1.docx", "pruebas del borrador + tamaño del efecto"),
 "S9-03": (45, "✂ Hacer pruebas de uso y de carga simuladas con scripts", D, f"{FL}Pruebas_Carga", "escenarios reproducibles"),
 "S9-04": (None, "Revisar el sprint 9 y planificar el sprint 10", A, f"{PL}Bitacora_Semanal.md", "sección escrita"),
 "S10-01": (46, "✂ Ciclos con la tutora (un día revisión, un día corrección)", V, f"{TU}actas", "observaciones cerradas"),
 "S10-02": (47, "HITO: tener la tesis al 90 % (18-dic; 11-dic en el escenario A)", A, f"{CAP}tesis completa", "todos los capítulos + bibliografía verificada"),
 "S10-03": (None, "Revisar el sprint 10 y planificar la holgura", A, f"{PL}Bitacora_Semanal.md", "sección escrita"),
 "H-01": (48, "Revisar APA, citas y bibliografía en bloques cortos", V, f"{CAP}tesis pulida", "0 citas sin ficha verificada"),
 "E-01": (49, "Lograr la revisión final, la aprobación y la firma de la tutora", V, "tesis firmada", "firmada"),
 "E-02": (50, "Entregar la tesis a la carrera", A, "comprobante de entrega", "comprobante recibido"),
 "D-01": (51, "Escribir el resumen de contribuciones (quién hizo qué)", A, f"09_Registro_Contribuciones/", "aprobado por los dos"),
 "D-02": (52, "Dividir la exposición, ensayar y armar el banco de preguntas del tribunal", A, "guion + banco de preguntas", "≥2 simulacros cronometrados"),
 "D-03": (53, "Defender la tesis (1–12 feb)", A, "—", "aprobada"),
}


def T(f, r, tarea, donde, resultado, como, h, ent, nota=""):
    return dict(fecha=f, resp=r, tarea=tarea, donde=donde, resultado=resultado, como=como, horas=h, ent=ent, nota=nota)


d = lambda m, dd: date(2026 if m >= 10 else 2027, m, dd)  # noqa: E731
SPRINTS = []

# ---------------- SPRINT 1 · 12–18 oct ----------------
SPRINTS.append(("S1", "Sprint 1 · 12–18 oct · Recopilar información", "Buscar fuentes, hablar con la tutora y con Torvesa, preparar el campo", [
 T(d(10, 12), V, "Conversar con la tutora sobre los 5 cambios, para tener su aprobación", f"{UPS} · llevar {TU}2026-10-12_Puntos_Tutora.pdf", "Respuestas de la tutora anotadas", "Las 5 preguntas tienen respuesta (sí / no / pendiente)", 1, "S1-07"),
 T(d(10, 12), V, "Escribir el acta de la conversación, para que quede por escrito lo que decidió", TU, f"{TU}2026-10-12_Acta_Conversacion.md", "Acta con decisiones y fechas", 0.5, "S1-07"),
 T(d(10, 12), V, "Enviar el correo a Torvesa (giro, nota de respaldo, catálogo, permisos), para trabajar con datos oficiales", f"Correo electrónico · borrador en {PL}2026-10-12_Correo_Torvesa_borrador.docx", "Correo enviado con el catálogo adjunto", "Copia del correo enviado", 0.5, "S1-05"),
 T(d(10, 12), D, "Aceptar la invitación de GitHub y clonar el repo, para trabajar en la bóveda compartida", "PC de Diego · pasos en GUIA_DIEGO.pdf (raíz)", "Repo clonado + 00_Inbox/hola_diego.md", "El commit de prueba aparece en GitHub", 1, "S1-10"),
 T(d(10, 12), D, "Levantar el buscador RAG en su PC, para consultar la bóveda", "PC de Diego · pasos en RAG_README.md (raíz)", "Consulta de prueba con resultados", "rag.py consultar devuelve fragmentos", 1, "S1-10"),
 T(d(10, 13), V, "Buscar y verificar fuentes sobre el tiempo de respuesta a clientes (Oldroyd y estudios 2023+), para respaldar el problema (A9, A10)", f"{F_PRO} · con 99_Scripts/busqueda/", "≥5 fichas, ≥2 verificadas con página", "Cada ficha con estado y página", 1, "S1-01"),
 T(d(10, 13), V, "Buscar fuentes sobre la digitalización de la construcción, para respaldar el contexto (A5, A6)", F_PRO, "≥4 fichas", "Cada ficha con estado", 1, "S1-01"),
 T(d(10, 13), D, "Investigar cómo consolidar bóvedas de conocimiento, para diseñar la bóveda del sistema", f"{F_TEC} · con 99_Scripts/busqueda/", "≥5 fichas", "Cada ficha dice qué respalda", 1.5, "S1-13"),
 T(d(10, 13), D, "Leer el Documento madre y el Glosario, para entender el proyecto completo", "00_DOCUMENTO_MADRE.pdf y Glosario.pdf (raíz)", "Dudas anotadas en el issue #10", "Dudas enviadas a Víctor", 0.5, "S1-10"),
 T(d(10, 14), V, "Revisar la respuesta de Torvesa y ajustar el campo del jueves y viernes, para saber qué se puede aplicar", f"Correo · {PL}Cronograma_Tesis.xlsx", "Campo confirmado o reprogramado", "Notas de esta fila actualizadas", 0.25, "S1-05", "Plazo pedido a Torvesa: hoy"),
 T(d(10, 14), V, "Corregir los instrumentos a la versión 0.2, para aplicarlos en Torvesa", INS, f"{INS}2026-10-14_*_v0.2 (.md + Word)", "Aprobados e impresos", 0.75, "S1-04"),
 T(d(10, 14), V, "Hacer el corte de fuentes: armar la matriz afirmación–fuente–estado, para decidir qué entra al capítulo 1", MAT, f"{MAT}2026-10-14_Matriz_Afirmaciones_v0.1.xlsx", "Las 47 afirmaciones tienen estado", 1, "S1-03", "En la noche"),
 T(d(10, 14), D, "Investigar arquitecturas RAG para negocio, para proponer cómo el asistente consultará la bóveda", F_TEC, "≥5 fichas", "Cada ficha dice qué respalda", 1.5, "S1-13"),
 T(d(10, 14), D, "Escribir un resumen de 1 página para Víctor sobre bóvedas y RAG, para compartir lo aprendido", F_TEC, f"{F_TEC}2026-10-14_Resumen_Bovedas_RAG.md", "Víctor lo leyó", 0.5, "S1-13"),
 T(d(10, 15), V, "Aplicar la encuesta a colaboradores y 2 entrevistas en Torvesa (si autorizó), para la línea base real", f"{TOR} · registro en {LB}", f"Hojas firmadas + {LB}registro_aplicacion.csv", "Cada aplicación está en el registro", 2, "S1-08", "Si Torvesa no autorizó: adelantar la búsqueda de la ley de datos (fila del sábado)"),
 T(d(10, 15), D, "Cronometrar las cotizaciones del día en Torvesa (si autorizó), para medir el tiempo real (meta M2)", TOR, f"{LB}P2A_cronometraje.csv", "Todas las cotizaciones observadas registradas", 2, "S1-09", "Si no hay autorización: adelantar la investigación de CRMs (fila del sábado)"),
 T(d(10, 16), V, "Llamar a los clientes para la encuesta corta (si autorizó), para conocer su experiencia", "Teléfono · lista solo en 05_Datos_Campo/_crudo/ (privada)", "Respuestas codificadas CLI-xx", "Cada llamada con consentimiento verbal registrado", 2, "S1-08"),
 T(d(10, 16), D, "Revisar solicitudes y cotizaciones de los últimos 3 meses (solo fechas y horas), para medir el tiempo de respuesta (meta M1)", TOR, f"{LB}P2B_muestra_documental.csv", "≥20 solicitudes o todas las disponibles", 2, "S1-09"),
 T(d(10, 17), V, "Buscar el texto oficial de la ley de datos (LOPDP) y agregar sus artículos al consentimiento, para cumplir la ley", f"{F_NOR} y {INS}", "Ficha LOPDP + consentimiento v0.2 con artículos", "Artículos citados desde el Registro Oficial", 1.5, "S1-02"),
 T(d(10, 17), V, "Buscar la versión validada en español de la escala SUS, para medir la usabilidad correctamente", F_MET, "Ficha verificada + encuesta I1 v0.2 con la traducción", "Traducción con fuente", 1, "S1-02"),
 T(d(10, 17), V, "Buscar fuentes de metodología (DSR, Design Thinking, Scrum, censo), para justificar el método", F_MET, "≥6 fichas", "Cada método con 2–3 fuentes", 1.5, "S1-02"),
 T(d(10, 17), D, "Investigar flujos de información y diseño de procesos (BPMN), para dibujar el proceso de Torvesa", F_MET, "≥5 fichas", "Cada ficha dice qué respalda", 1.5, "S1-14"),
 T(d(10, 17), D, "Investigar CRMs móviles y herramientas existentes con sus precios, para comparar y calcular costos", f"{F_CAS} y {F_COS}", "Tabla de ≥6 herramientas con precio y fecha", "Cada precio con enlace oficial", 2, "S1-15"),
 T(d(10, 18), A, "Tabular y anonimizar los datos de campo, para que estén listos y sean confiables", LB, "CSV anonimizados + hashes + auditoría", "auditoria_pii.py dice 0 hallazgos", 2, "S1-12", "Si no hubo campo, se mueve a la fecha nueva"),
 T(d(10, 18), V, "Escribir un resumen de 1 página para Diego sobre el problema y sus fuentes", F_PRO, f"{F_PRO}2026-10-18_Resumen_Problema.md", "Diego lo leyó", 0.5, "S1-01"),
 T(d(10, 18), D, "Escribir un resumen de 1 página para Víctor sobre CRMs y flujos", F_CAS, f"{F_CAS}2026-10-18_Resumen_CRM_Flujos.md", "Víctor lo leyó", 0.5, "S1-15"),
 T(d(10, 18), A, *REV, 1, "S1-16"),
]))

# ---------------- SPRINT 2 · 19–25 oct ----------------
SPRINTS.append(("S2", "Sprint 2 · 19–25 oct · Redactar capítulos", "Primeros borradores de los capítulos 1–3; Diego analiza los datos y dibuja el proceso actual", [
 T(d(10, 19), V, "Escribir el capítulo 1, parte 1 (problema y evidencias), para tener el primer borrador", CAP, "Cap1 v0.1 (primera mitad)", "Cada cifra enlazada a su ficha verificada", 2, "S2-01"),
 T(d(10, 19), D, "Analizar los datos de campo (tablas y gráficos simples), para calcular la línea base", LB, f"{LB}analisis/ (tablas y script)", "Tablas de M1–M4 y M6", 2, "S2-04", "Si no hubo campo: analizar la muestra documental disponible"),
 T(d(10, 20), V, "Escribir el capítulo 1, parte 2 (justificación y objetivos)", CAP, f"{CAP}2026-10-20_Cap1_Problema_v0.1.docx", "Capítulo completo, revisado una vez", 2, "S2-01"),
 T(d(10, 20), D, "Terminar el análisis de datos y escribir lo que muestran, en lenguaje simple", LB, f"{LB}analisis/2026-10-20_Resultados_LineaBase_v0.1.md", "Víctor entiende cada número", 2, "S2-04"),
 T(d(10, 21), V, "Escribir el capítulo 2, parte 1 (CRM, tiempo de respuesta, gestión del conocimiento)", CAP, "Cap2 v0.1 (primera mitad)", "Solo fuentes verificadas", 2, "S2-02"),
 T(d(10, 21), D, "Dibujar el proceso actual (AS-IS) en BPMN con lo dicho en las entrevistas", FL, "AS-IS v0.1 (borrador)", "Cada paso tiene quién lo hace", 2, "S2-05"),
 T(d(10, 22), V, "Escribir el capítulo 2, parte 2 (IA, RAG, normativa)", CAP, f"{CAP}2026-10-22_Cap2_Marco_Teorico_v0.1.docx", "Capítulo completo", 2, "S2-02"),
 T(d(10, 22), D, "Terminar el proceso actual (AS-IS) y marcar dónde se pierde tiempo", FL, f"{FL}2026-10-22_AS-IS_v0.1", "Validado contra las entrevistas", 2, "S2-05"),
 T(d(10, 23), V, "Buscar fuentes de adopción de IA y automatización comercial 2023–2026, para el marco teórico", F_TEC, "≥5 fichas", "Cada ficha con estado", 1, "S2-02"),
 T(d(10, 23), V, "Armar el lienzo del modelo de negocio y la propuesta de valor (primer borrador)", MN, f"{MN}2026-10-23_Lienzo_Modelo_Negocio_v0.1.docx", "9 bloques completos", 1, "S2-07"),
 T(d(10, 23), D, "Hacer el inventario de herramientas candidatas, con criterios de comparación", FL, "Inventario v0.1 (borrador)", "≥3 opciones por componente", 2, "S2-06"),
 T(d(10, 24), V, "Escribir el capítulo 3, parte 1 (enfoque, DSR y población)", CAP, "Cap3 v0.1 (primera mitad)", "Coherente con D1 y D2", 3, "S2-03"),
 T(d(10, 24), V, "Escribir un resumen de 1 página para Diego del capítulo 1", CAP, f"{CAP}2026-10-24_Resumen_Cap1.md", "Diego lo leyó", 0.5, "S2-01"),
 T(d(10, 24), D, "Terminar el inventario de herramientas con precios y criterios", FL, f"{FL}2026-10-24_Inventario_Herramientas_v0.1.xlsx", "Cada precio con fuente", 2.5, "S2-06"),
 T(d(10, 24), D, "Escribir un resumen de 1 página para Víctor del proceso actual", FL, f"{FL}2026-10-24_Resumen_AS-IS.md", "Víctor lo leyó", 0.5, "S2-05"),
 T(d(10, 25), V, "Escribir el capítulo 3, parte 2 (instrumentos, análisis y ética)", CAP, f"{CAP}2026-10-25_Cap3_Metodologia_v0.1.docx", "Capítulo completo", 2, "S2-03"),
 T(d(10, 25), D, "Preparar las gráficas de datos para la Revisión 1", LB, f"{LB}analisis/figuras/", "Gráficas legibles con título", 2, "S2-04"),
 T(d(10, 25), A, *REV, 1, "S2-08"),
]))

# ---------------- SPRINT 3 · 26 oct–1 nov ----------------
SPRINTS.append(("S3", "Sprint 3 · 26 oct–1 nov · Revisión 1 con la tutora", "Mostrar avance, corregir, y preparar el diseño", [
 T(d(10, 26), V, "Preparar la presentación de avance (capítulos 1–3 y fuentes), para la Revisión 1", TU, f"{TU}2026-10-27_Presentacion_Revision1.pptx", "Máx. 12 diapositivas", 2, "S3-01"),
 T(d(10, 26), D, "Exportar el proceso actual y las gráficas para la presentación", FL, "Imágenes en la presentación", "Se leen bien proyectadas", 2, "S3-03"),
 T(d(10, 27), A, "Ensayar la presentación de la Revisión 1", LLAM, "Ensayo cronometrado", "Dura ≤15 min", 1, "S3-01"),
 T(d(10, 27), V, "Escribir cómo estructuré mi bóveda 1 (patrones, no datos), parte 1", FL, "Patrones v0.1 (primera mitad)", "Sin datos de CRISFE", 1, "S3-04"),
 T(d(10, 28), A, "Asistir a la Revisión 1 con la tutora (fecha a confirmar)", UPS, "Observaciones anotadas", "Reunión realizada", 1.5, "S3-01", "Confirmar fecha con la tutora"),
 T(d(10, 28), V, "Escribir el acta de la Revisión 1", TU, f"{TU}2026-10-28_Acta_Revision1.md", "Cada observación con responsable y plazo", 0.5, "S3-02"),
 T(d(10, 29), V, "Corregir los capítulos según las observaciones, parte 1", CAP, "Capítulos v0.2", "Observaciones marcadas como cerradas", 2, "S3-02"),
 T(d(10, 29), D, "Corregir el proceso actual y las gráficas según las observaciones", FL, "AS-IS v0.2", "Observaciones cerradas", 2, "S3-03"),
 T(d(10, 30), V, "Escribir cómo estructuré mi bóveda 1, parte 2", FL, f"{FL}2026-10-30_Patrones_Boveda1_v0.1.docx", "Documento completo, sin datos", 1.5, "S3-04"),
 T(d(10, 30), D, "Leer el documento de patrones de la bóveda 1 y anotar preguntas", FL, "Preguntas en el issue de S3-04", "Preguntas enviadas", 1, "S3-04"),
 T(d(10, 31), V, "Corregir los capítulos según las observaciones, parte 2", CAP, "Capítulos v0.2 completos", "Todas las observaciones cerradas", 3, "S3-02"),
 T(d(10, 31), D, "Preparar la plantilla de los flujos TO-BE (Mermaid o Miro)", FL, "Plantilla de flujos", "Lista para el lunes", 2, "S4-01"),
 T(d(11, 1), A, "Sesión: Víctor explica a Diego los conceptos de negocio (embudo, tiempo de respuesta, propuesta de valor)", f"{LLAM} · Conceptos_Negocio.pdf (raíz)", "Diego traduce cada concepto a una función del sistema", "Lista de funciones anotada", 1, "S3-05"),
 T(d(11, 1), A, *REV, 1, "S3-05"),
]))

# ---------------- SPRINT 4 · 2–8 nov ----------------
SPRINTS.append(("S4", "Sprint 4 · 2–8 nov · Diseñar el sistema", "Flujos TO-BE, bóveda del sistema, requisitos, matriz de herramientas, costos", [
 T(d(11, 2), D, "Dibujar los procesos con el sistema (TO-BE), parte 1: recepción y asignación", FL, "TO-BE v0.1 (parte 1)", "Cada paso con disparador y responsable", 2, "S4-01"),
 T(d(11, 2), V, "Escribir los requisitos funcionales (qué debe hacer el sistema)", CAP, "Requisitos v0.1 (funcionales)", "Cada requisito con su origen", 2, "S4-04"),
 T(d(11, 3), D, "Dibujar los procesos TO-BE, parte 2: cotización asistida e historial", FL, "TO-BE v0.1 (parte 2)", "Cubre los pasos 3–4", 2, "S4-01"),
 T(d(11, 3), V, "Escribir los requisitos no funcionales (seguridad, sin conexión, ley de datos)", CAP, f"{CAP}2026-11-03_Requisitos_v0.1.docx", "Requisitos completos", 2, "S4-04"),
 T(d(11, 4), D, "Dibujar los procesos TO-BE, parte 3: recordatorios y reasignación", FL, f"{FL}2026-11-04_TO-BE_v0.1", "Cubre los 6 pasos", 2, "S4-01"),
 T(d(11, 4), V, "Validar los flujos TO-BE contra los requisitos", FL, "Comentarios en los flujos", "Cada requisito ligado a un flujo", 1.5, "S4-02"),
 T(d(11, 5), D, "Construir la bóveda del sistema: carpetas y plantillas", FL, f"{FL}Boveda_Sistema/", "Estructura creada", 2, "S4-03"),
 T(d(11, 5), V, "Armar la matriz de decisión de herramientas en Excel (fórmulas vivas)", MN, f"{MN}2026-11-05_Matriz_Decision_Herramientas_v0.1.xlsx", "Ponderaciones y sensibilidad", 2, "S4-05"),
 T(d(11, 6), D, "Construir la bóveda del sistema: fichas de ejemplo con datos ficticios", FL, "Fichas CLI-0001…", "Plantillas funcionando", 2, "S4-03"),
 T(d(11, 6), V, "Calcular CAPEX (inversión inicial) con fuente para cada precio", MN, "Hoja Costos del modelo financiero", "Cada precio con enlace y fecha", 2, "S4-06"),
 T(d(11, 7), D, "Construir la bóveda del sistema: tableros y enlaces", FL, "Tableros de pendientes", "Se ven los pendientes por vendedor", 3, "S4-03"),
 T(d(11, 7), V, "Calcular OPEX (gasto mensual) con fuente para cada precio", MN, f"{MN}2026-11-07_Modelo_Financiero_v0.1.xlsx", "Hoja Costos completa", 3, "S4-06"),
 T(d(11, 8), D, "Escribir un resumen de 1 página para Víctor de la bóveda del sistema", FL, f"{FL}2026-11-08_Resumen_Boveda_Sistema.md", "Víctor lo leyó", 0.5, "S4-03"),
 T(d(11, 8), V, "Escribir un resumen de 1 página para Diego de requisitos y costos", MN, f"{MN}2026-11-08_Resumen_Costos.md", "Diego lo leyó", 0.5, "S4-06"),
 T(d(11, 8), A, *REV, 1, "S4-07"),
]))

# ---------------- SPRINT 5 · 9–15 nov ----------------
SPRINTS.append(("S5", "Sprint 5 · 9–15 nov · Prueba de concepto y finanzas", "Diego construye la prueba de concepto; Víctor calcula VAN, TIR y riesgos", [
 T(d(11, 9), V, "Estimar los beneficios con supuestos explícitos (horas ahorradas, clientes no perdidos)", MN, "Hoja Beneficios", "Cada supuesto con fuente o dato de campo", 2, "S5-01"),
 T(d(11, 9), D, "Construir la prueba de concepto, parte 1: formulario → servidor", "Repositorio de la prueba de concepto", "Formulario guarda en la base de datos", "Demo funcionando", 2, "S5-04"),
 T(d(11, 10), V, "Calcular VAN, TIR y período de recuperación en 3 escenarios", MN, "Hoja Escenarios", "Pesimista, base y optimista", 2, "S5-01"),
 T(d(11, 10), D, "Construir la prueba de concepto, parte 2: servidor → bóveda", "Repositorio de la prueba de concepto", "La ficha del cliente aparece en la bóveda", "Demo funcionando", 2, "S5-04"),
 T(d(11, 11), V, "Hacer el análisis de sensibilidad (qué pasa si cambian los supuestos)", MN, "Hoja Sensibilidad", "Tabla y gráfico", 2, "S5-01"),
 T(d(11, 11), D, "Construir la prueba de concepto, parte 3: borrador de cotización con IA", "Repositorio de la prueba de concepto", "Borrador generado desde la bóveda", "Demo funcionando", 2, "S5-04"),
 T(d(11, 12), V, "Escribir la matriz de riesgos", CAP, f"{CAP}2026-11-12_Riesgos_v0.1.xlsx", "Probabilidad × impacto + mitigación", 2, "S5-02"),
 T(d(11, 12), D, "Construir la prueba de concepto, parte 4: alertas y registro de eventos", "Repositorio de la prueba de concepto", "Eventos registrados", "Demo funcionando", 2, "S5-04"),
 T(d(11, 13), V, "Escribir el capítulo de normativa (LOPDP)", CAP, f"{CAP}2026-11-13_Normativa_v0.1.docx", "Artículos del texto oficial", 2, "S5-03"),
 T(d(11, 13), D, "Probar la prueba de concepto completa y corregir errores", "Repositorio de la prueba de concepto", "Flujo completo sin errores", "Demo de punta a punta", 2, "S5-04"),
 T(d(11, 14), V, "Escribir el pitch de 1 página para inversionista", MN, f"{MN}2026-11-14_Pitch_1pagina_v0.1.docx", "Una página con VAN, TIR y propuesta de valor", 2, "S5-06"),
 T(d(11, 14), V, "Terminar el capítulo de normativa", CAP, "Normativa v0.1 completa", "Revisado una vez", 1.5, "S5-03"),
 T(d(11, 14), D, "Diseñar los 3 casos de prueba", FL, f"{FL}2026-11-14_Casos_Prueba_v0.1.md", "Cada caso con criterio de aceptación", 3, "S5-05"),
 T(d(11, 15), A, "Intercambiar resúmenes de 1 página (finanzas ↔ prueba de concepto)", f"{MN} y {FL}", "2 resúmenes", "Leídos por el otro", 1, "S5-07"),
 T(d(11, 15), A, *REV, 1, "S5-07"),
]))

# ---------------- SPRINT 6 · 16–22 nov ----------------
SPRINTS.append(("S6", "Sprint 6 · 16–22 nov · Revisión 2 con la tutora", "Mostrar diseño, flujos, datos y viabilidad; preparar la validación", [
 T(d(11, 16), A, "Preparar la presentación de la Revisión 2 (diseño, flujos, datos y viabilidad)", TU, f"{TU}2026-11-17_Presentacion_Revision2.pptx", "Máx. 15 diapositivas", 2, "S6-01"),
 T(d(11, 17), A, "Ensayar la presentación de la Revisión 2", LLAM, "Ensayo cronometrado", "Dura ≤20 min", 1, "S6-01"),
 T(d(11, 17), D, "Estabilizar la prueba de concepto para la demostración", "Repositorio de la prueba de concepto", "Demo sin fallas", "3 corridas seguidas sin error", 1, "S5-04"),
 T(d(11, 18), A, "Asistir a la Revisión 2 con la tutora (fecha a confirmar)", UPS, "Observaciones anotadas", "Reunión realizada", 1.5, "S6-01", "Confirmar fecha con la tutora"),
 T(d(11, 18), V, "Escribir el acta de la Revisión 2", TU, f"{TU}2026-11-18_Acta_Revision2.md", "Observaciones con responsable y plazo", 0.5, "S6-02"),
 T(d(11, 19), V, "Preparar el protocolo de la validación del diseño en operación experimental controlada", INS, f"{INS}2026-11-19_Protocolo_Validacion_v0.1.md", "Fechas, participantes y mediciones definidos", 2, "S7-02"),
 T(d(11, 19), D, "Dejar estable la prueba de concepto para la validación", "Repositorio de la prueba de concepto", "Versión congelada", "Etiqueta de versión en el repositorio", 2, "S5-04"),
 T(d(11, 20), V, "Pedir a Torvesa la autorización y las fechas de la validación", "Correo electrónico", "Autorización escrita", "Respuesta recibida", 1, "S7-02"),
 T(d(11, 20), D, "Probar la prueba de concepto con los 3 casos de prueba antes de la validación", FL, "Resultados preliminares", "Los 3 casos pasan", 2, "S5-05"),
 T(d(11, 21), V, "Incorporar las observaciones de la Revisión 2 (documento)", CAP, "Versiones nuevas", "Observaciones cerradas", 3, "S7-01"),
 T(d(11, 21), D, "Incorporar las observaciones de la Revisión 2 (técnicas)", FL, "Versiones nuevas", "Observaciones cerradas", 3, "S7-01"),
 T(d(11, 22), A, *REV, 1, "S6-03"),
]))

# ---------------- SPRINT 7 · 23–29 nov ----------------
SPRINTS.append(("S7", "Sprint 7 · 23–29 nov · Arranca la validación", "Capacitar a Torvesa y arrancar la validación del diseño en operación experimental controlada", [
 T(d(11, 23), A, "Capacitar al equipo de Torvesa para la validación", TOR, "Equipo capacitado", "Lista de asistentes", 1.5, "S7-02"),
 T(d(11, 22), D, "Preparar el sistema para la validación (accesos, respaldo)", "Repositorio de la prueba de concepto", "Accesos listos", "Prueba de acceso de cada usuario", 1, "S7-03"),
 T(d(11, 24), D, "Arrancar la validación del diseño en operación experimental controlada", TOR, "Primeros eventos registrados", "Eventos sin errores", 1, "S7-03"),
 T(d(11, 24), V, "Escribir el capítulo de diagnóstico, parte 1 (línea base real)", CAP, "Cap4 v0.1 (primera mitad)", "Solo datos con registro de procedencia", 2, "S7-04"),
 T(d(11, 25), D, "Monitorear la validación y anotar incidencias", "Registro de eventos del sistema", "Bitácora de incidencias", "Revisada a diario", 0.5, "S7-03"),
 T(d(11, 25), D, "Incorporar observaciones técnicas pendientes", FL, "Versiones nuevas", "Observaciones cerradas", 1.5, "S7-01"),
 T(d(11, 25), V, "Escribir el capítulo de diagnóstico, parte 2", CAP, "Cap4 v0.1", "Capítulo completo", 2, "S7-04"),
 T(d(11, 26), D, "Monitorear la validación y anotar incidencias", "Registro de eventos del sistema", "Bitácora de incidencias", "Revisada a diario", 0.5, "S7-03"),
 T(d(11, 26), V, "Incorporar observaciones pendientes del documento", CAP, "Versiones nuevas", "Observaciones cerradas", 2, "S7-01"),
 T(d(11, 27), D, "Monitorear la validación y anotar incidencias", "Registro de eventos del sistema", "Bitácora de incidencias", "Revisada a diario", 0.5, "S7-03"),
 T(d(11, 27), V, "Revisar el capítulo de diagnóstico", CAP, f"{CAP}2026-11-28_Cap4_Diagnostico_v0.1.docx", "Revisado una vez", 2, "S7-04"),
 T(d(11, 28), D, "Monitorear la validación y empezar a documentar las herramientas", f"Registro de eventos · {FL}", "Bitácora + borrador de herramientas", "Revisada", 3, "S8-01"),
 T(d(11, 28), V, "Escribir un resumen de 1 página para Diego del diagnóstico", CAP, f"{CAP}2026-11-28_Resumen_Cap4.md", "Diego lo leyó", 0.5, "S7-04"),
 T(d(11, 29), A, *REV, 1, "S7-05"),
]))

# ---------------- SPRINT 8 · 30 nov–6 dic ----------------
SPRINTS.append(("S8", "Sprint 8 · 30 nov–6 dic · Documentar el sistema", "La validación sigue hasta el 5-dic; Diego documenta, Víctor escribe el capítulo de diseño", [
 T(d(11, 30), D, "Documentar las herramientas elegidas y descartadas, con justificación", FL, f"{FL}Herramientas", "Cada decisión con criterio", 1.5, "S8-01"),
 T(d(11, 30), D, "Monitorear la validación", "Registro de eventos del sistema", "Bitácora", "Revisada", 0.5, "S7-03"),
 T(d(11, 30), V, "Escribir el capítulo de diseño y viabilidad, parte 1 (arquitectura y flujos)", CAP, "Cap5 v0.1 (parte 1)", "Integra los flujos TO-BE", 2, "S8-06"),
 T(d(12, 1), D, "Documentar el modelo de datos y el registro de eventos", FL, f"{FL}Modelo_Datos", "Coincide con la prueba de concepto", 1.5, "S8-02"),
 T(d(12, 1), D, "Monitorear la validación", "Registro de eventos del sistema", "Bitácora", "Revisada", 0.5, "S7-03"),
 T(d(12, 1), V, "Escribir el capítulo de diseño y viabilidad, parte 2 (costos y VAN/TIR)", CAP, "Cap5 v0.1 (parte 2)", "Integra el modelo financiero", 2, "S8-06"),
 T(d(12, 2), D, "Documentar las plantillas de cotización y el asistente de IA", FL, f"{FL}Asistente_IA", "Revisado por Víctor", 1.5, "S8-03"),
 T(d(12, 2), D, "Monitorear la validación", "Registro de eventos del sistema", "Bitácora", "Revisada", 0.5, "S7-03"),
 T(d(12, 2), V, "Escribir el capítulo de diseño y viabilidad, parte 3 (normativa y riesgos)", CAP, "Cap5 v0.1 (parte 3)", "Integra normativa y riesgos", 2, "S8-06"),
 T(d(12, 3), D, "Ejecutar los casos de prueba", FL, f"{FL}Resultados_Casos_Prueba", "Resultado por caso", 1.5, "S8-04"),
 T(d(12, 3), D, "Monitorear la validación", "Registro de eventos del sistema", "Bitácora", "Revisada", 0.5, "S7-03"),
 T(d(12, 3), V, "Revisar los documentos técnicos de Diego", FL, "Comentarios", "Comentarios enviados", 2, "S8-03"),
 T(d(12, 4), D, "✂ Escribir el manual básico de usuario", FL, f"{FL}Manual_Usuario", "Un usuario de Torvesa lo puede seguir", 1.5, "S8-05"),
 T(d(12, 4), V, "Terminar el capítulo de diseño y viabilidad", CAP, f"{CAP}2026-12-04_Cap5_Diseno_Viabilidad_v0.1.docx", "Capítulo completo", 2, "S8-06"),
 T(d(12, 5), D, "Cerrar la validación: congelar el registro y respaldar los datos", f"Registro de eventos · {LB}", "Respaldo con hash", "Hash anotado", 2, "S7-03"),
 T(d(12, 5), V, "Preparar los instrumentos de la medición «después»", INS, "Instrumentos post impresos", "Iguales a los de la línea base", 2, "S9-01"),
 T(d(12, 6), A, "Intercambiar resúmenes de 1 página (capítulo 5 ↔ documentación técnica)", f"{CAP} y {FL}", "2 resúmenes", "Leídos por el otro", 1, "S8-07"),
 T(d(12, 6), A, *REV, 1, "S8-07"),
]))

# ---------------- SPRINT 9 · 7–13 dic ----------------
SPRINTS.append(("S9", "Sprint 9 · 7–13 dic · Medir el «después» y comparar", "Medición post, análisis pre-post y pruebas", [
 T(d(12, 7), A, "Hacer la medición «después», día 1 (encuesta a colaboradores y SUS)", TOR, "Datos post + registro de procedencia", "Cada aplicación registrada", 2, "S9-01"),
 T(d(12, 8), A, "Hacer la medición «después», día 2 (prueba de recuperación)", TOR, "Datos post", "Cada aplicación registrada", 2, "S9-01"),
 T(d(12, 9), A, "Hacer la medición «después», día 3 (clientes y entrevistas de cierre)", TOR, "Datos post", "Cada aplicación registrada", 2, "S9-01"),
 T(d(12, 10), V, "Comparar el antes y el después (análisis pre-post)", LB, "Tablas pre-post", "Pruebas del borrador + tamaño del efecto", 2, "S9-02"),
 T(d(12, 10), D, "✂ Hacer pruebas de carga simuladas con scripts", FL, f"{FL}Pruebas_Carga", "Escenarios reproducibles", 2, "S9-03"),
 T(d(12, 11), V, "Terminar el análisis pre-post", LB, "Resultados listos", "Revisados con Diego", 2, "S9-02"),
 T(d(12, 11), D, "Hacer pruebas de uso y preparar las gráficas de resultados", FL, "Gráficas", "Legibles y con título", 2, "S9-02"),
 T(d(12, 12), V, "Escribir el capítulo de resultados", CAP, f"{CAP}2026-12-12_Cap6_Resultados_v0.1.docx", "Capítulo completo", 3, "S9-02"),
 T(d(12, 12), D, "Revisar el capítulo de resultados (parte técnica)", CAP, "Comentarios", "Comentarios enviados", 2, "S9-02"),
 T(d(12, 13), A, *REV, 1, "S9-04"),
]))

# ---------------- SPRINT 10 · 14–20 dic ----------------
SPRINTS.append(("S10", "Sprint 10 · 14–20 dic · Cierre e hito del 90 %", "Ciclos con la tutora y tesis al 90 %", [
 T(d(12, 14), V, "Enviar a la tutora la tesis completa para revisión", "Correo electrónico", "Tesis enviada", "Acuse de recibo", 1, "S10-01"),
 T(d(12, 14), D, "Revisar anexos técnicos y figuras", CAP, "Anexos revisados", "Sin errores", 2, "S10-02"),
 T(d(12, 15), V, "✂ Ciclo con la tutora: recibir observaciones", TU, "Observaciones", "Acta corta", 1, "S10-01"),
 T(d(12, 16), A, "Corregir según las observaciones", CAP, "Versión corregida", "Observaciones cerradas", 2, "S10-01"),
 T(d(12, 17), V, "✂ Ciclo con la tutora: segunda revisión", TU, "Observaciones", "Acta corta", 1, "S10-01"),
 T(d(12, 18), A, "HITO: dejar la tesis al 90 %", CAP, "Tesis completa", "Todos los capítulos + bibliografía verificada", 2, "S10-02"),
 T(d(12, 19), A, "Integrar todo y revisar coherencia entre capítulos", CAP, "Versión integrada", "Lectura completa hecha", 3, "S10-02"),
 T(d(12, 20), A, *REV, 1, "S10-03"),
]))

SPRINTS.append(("Holgura", "Holgura · 21 dic–3 ene · Pulir", "Revisión APA, citas y bibliografía en bloques cortos", [
 T(d(12, 22), V, "Revisar las citas del capítulo 1 y 2 contra sus fichas", CAP, "Citas verificadas", "0 citas sin ficha", 1.5, "H-01"),
 T(d(12, 23), D, "Revisar los anexos técnicos y su numeración", CAP, "Anexos ordenados", "Índice correcto", 1.5, "H-01"),
 T(d(12, 26), V, "Revisar las citas de los capítulos 3–6", CAP, "Citas verificadas", "0 citas sin ficha", 2, "H-01"),
 T(d(12, 29), V, "Revisar la bibliografía en APA 7", CAP, "Bibliografía final", "Formato APA en todas", 2, "H-01"),
 T(d(12, 30), D, "Revisar figuras, tablas y diagramas", CAP, "Figuras finales", "Numeradas y citadas", 1.5, "H-01"),
 T(d(1, 2), A, "Leer la tesis completa una vez más", CAP, "Lista de últimos cambios", "Lista cerrada", 3, "H-01"),
]))
SPRINTS.append(("Entrega", "Entrega · 4–10 ene · Revisión final y firma", "Escenario A: la entrega es el 15-dic", [
 T(d(1, 4), V, "Enviar la versión final a la tutora", "Correo electrónico", "Versión final enviada", "Acuse de recibo", 1, "E-01"),
 T(d(1, 6), A, "Hacer las últimas correcciones", CAP, "Versión final corregida", "Observaciones cerradas", 2, "E-01"),
 T(d(1, 7), V, "Conseguir la firma de la tutora", UPS, "Tesis firmada", "Firma", 1, "E-01"),
 T(d(1, 8), A, "Entregar la tesis a la carrera", "Sistema de la UPS", "Comprobante", "Comprobante recibido", 1, "E-02"),
]))
SPRINTS.append(("Defensa", "Defensa · 11 ene–12 feb · Preparar y defender", "Los dos deben poder responder sobre todo el proyecto", [
 T(d(1, 12), A, "Escribir el resumen de contribuciones (quién hizo qué)", "09_Registro_Contribuciones/", "Resumen de contribuciones", "Aprobado por los dos", 2, "D-01"),
 T(d(1, 23), A, "Dividir la exposición y armar las diapositivas", LLAM, "Guion + diapositivas", "Cada uno sabe su parte y la del otro", 3, "D-02"),
 T(d(1, 30), A, "Armar el banco de preguntas del tribunal y hacer el simulacro 1", LLAM, "Banco de preguntas + simulacro", "Simulacro cronometrado", 3, "D-02"),
 T(d(2, 6), A, "Hacer el simulacro 2 con preguntas cruzadas (cada uno responde lo del otro)", LLAM, "Simulacro 2", "Ambos responden todo el banco", 3, "D-02"),
 T(d(2, 9), A, "Defender la tesis (fecha a confirmar por la carrera)", UPS, "Defensa", "Aprobada", 2, "D-03"),
]))

# ---------------- Excel ----------------
HDR = ["ID", "Día planificado", "Día", "Tarea (verbo + qué + para qué)", "Responsable", "Dónde se hace", "Resultado esperado",
       "Cómo sé que terminé", "Horas estimadas", "Fecha real", "Estado", "Días de retraso", "Entregable (issue)", "Notas"]
ANCHOS = [8, 12, 10, 52, 11, 38, 36, 30, 9, 12, 12, 10, 26, 34]
fino = Side(style="thin", color="D5DCE6")
BORDE = Border(left=fino, right=fino, top=fino, bottom=fino)


def estilo_hoja(ws, titulo, sub):
    ws["A1"] = titulo; ws["A1"].font = Font(name="Poppins", size=15, bold=True, color="FFFFFF")
    ws["A2"] = sub; ws["A2"].font = Font(name="Lato", size=10, color="E6C3A0")
    for r in (1, 2):
        for c in range(1, len(HDR) + 1):
            ws.cell(r, c).fill = PatternFill("solid", fgColor=AZUL)
    ws.row_dimensions[1].height = 26


def crear() -> None:
    wb = Workbook()
    guia = wb.active; guia.title = "Cómo usar"
    ws_res = wb.create_sheet("Resumen"); ws_carga = wb.create_sheet("Carga")
    dv_estado = lambda: DataValidation(type="list", formula1='"Pendiente,En curso,Hecho,Movido,Cancelado"', allow_blank=True)  # noqa: E731
    dv_resp = lambda: DataValidation(type="list", formula1='"Víctor,Diego,Ambos"', allow_blank=False)  # noqa: E731
    hojas = []
    import re
    nums = dict(re.findall(r"\*\*([A-Z]+\d*-\d+)\*\* .*· #(\d+)\s*$", MD.read_text(encoding="utf-8"), re.M)) if MD.exists() else {}
    for clave, titulo, objetivo, tareas in SPRINTS:
        ws = wb.create_sheet(clave); hojas.append((clave, titulo, ws, len(tareas)))
        estilo_hoja(ws, titulo, f"Objetivo: {objetivo}")
        ws["A3"] = "Avance del sprint:"; ws["A3"].font = Font(name="Lato", bold=True)
        n0, n1 = 6, 5 + len(tareas)
        ws["C3"] = f'=IFERROR(COUNTIF(K{n0}:K{n1},"Hecho")/(COUNTA(D{n0}:D{n1})-COUNTIF(K{n0}:K{n1},"Cancelado")),0)'
        ws["C3"].number_format = "0%"; ws["C3"].font = Font(name="Poppins", bold=True, color=COBRE, size=12)
        ws["D3"] = (f'="Víctor: "&TEXT(IFERROR((COUNTIFS(E{n0}:E{n1},"Víctor",K{n0}:K{n1},"Hecho")+COUNTIFS(E{n0}:E{n1},"Ambos",K{n0}:K{n1},"Hecho"))'
                    f'/(COUNTIF(E{n0}:E{n1},"Víctor")+COUNTIF(E{n0}:E{n1},"Ambos")),0),"0%")&"   ·   Diego: "&TEXT(IFERROR((COUNTIFS(E{n0}:E{n1},"Diego",K{n0}:K{n1},"Hecho")'
                    f'+COUNTIFS(E{n0}:E{n1},"Ambos",K{n0}:K{n1},"Hecho"))/(COUNTIF(E{n0}:E{n1},"Diego")+COUNTIF(E{n0}:E{n1},"Ambos")),0),"0%")'
                    f'&"   ·   Horas: "&TEXT(SUM(I{n0}:I{n1}),"0.0")')
        ws["D3"].font = Font(name="Lato", color=AZUL)
        for j, h in enumerate(HDR, 1):
            c = ws.cell(5, j, h); c.font = Font(name="Poppins", bold=True, color="FFFFFF", size=9.5)
            c.fill = PatternFill("solid", fgColor=COBRE); c.alignment = Alignment(wrap_text=True, vertical="center")
            ws.column_dimensions[get_column_letter(j)].width = ANCHOS[j - 1]
        ws.row_dimensions[5].height = 30
        for i, t in enumerate(sorted(tareas, key=lambda x: x["fecha"]), n0):
            ent = ENT[t["ent"]]
            ent = (ent[0] or nums.get(t["ent"]),) + ent[1:]
            vals = [f"{clave}-T{i - n0 + 1:02d}", t["fecha"], f"=B{i}", t["tarea"], t["resp"], t["donde"], t["resultado"], t["como"],
                    t["horas"], None, "Pendiente",
                    f'=IF(K{i}="Cancelado","",IF(J{i}<>"",J{i}-B{i},IF(AND(K{i}<>"Hecho",TODAY()>B{i}),TODAY()-B{i},0)))',
                    f'{t["ent"]} (#{ent[0]})' if ent[0] else f'{t["ent"]} (issue nuevo)', t["nota"]]
            for j, v in enumerate(vals, 1):
                c = ws.cell(i, j, v); c.font = Font(name="Lato", size=9.5); c.border = BORDE
                c.alignment = Alignment(wrap_text=True, vertical="top")
            ws.cell(i, 2).number_format = "dd-mmm"; ws.cell(i, 3).number_format = "dddd"
            ws.cell(i, 10).number_format = "dd-mmm"; ws.cell(i, 9).number_format = "0.0"
        rng = f"A{n0}:N{n1}"
        ws.conditional_formatting.add(rng, FormulaRule(formula=[f'$K{n0}="Hecho"'], fill=PatternFill("solid", fgColor="D9EFDE"), stopIfTrue=True))
        ws.conditional_formatting.add(rng, FormulaRule(formula=[f'$K{n0}="Movido"'], fill=PatternFill("solid", fgColor="FFF2C7"), stopIfTrue=True))
        ws.conditional_formatting.add(rng, FormulaRule(formula=[f'AND($K{n0}<>"Cancelado",$L{n0}<>"",$L{n0}>0)'], fill=PatternFill("solid", fgColor="F8D3D0"), stopIfTrue=True))
        ws.conditional_formatting.add(rng, FormulaRule(formula=[f'$K{n0}="Cancelado"'], font=Font(color="999999", strike=True)))
        a, b = dv_estado(), dv_resp(); ws.add_data_validation(a); ws.add_data_validation(b)
        a.add(f"K{n0}:K{n1 + 40}"); b.add(f"E{n0}:E{n1 + 40}")
        ws.freeze_panes = "E6"; ws.auto_filter.ref = f"A5:N{n1}"
        ws.sheet_view.zoomScale = 90

    # ---- Resumen ----
    estilo_hoja(ws_res, "Resumen del avance", "Se calcula solo desde las hojas de cada sprint. No escribas aquí.")
    cab = ["Sprint", "Fechas y objetivo", "Tareas", "Hechas", "% avance", "% Víctor", "% Diego", "Horas Víctor", "Horas Diego", "Atrasadas"]
    for j, h in enumerate(cab, 1):
        c = ws_res.cell(4, j, h); c.font = Font(name="Poppins", bold=True, color="FFFFFF", size=9.5); c.fill = PatternFill("solid", fgColor=COBRE)
    for j, w in enumerate([10, 46, 9, 9, 10, 10, 10, 12, 12, 11], 1):
        ws_res.column_dimensions[get_column_letter(j)].width = w
    r = 5
    for clave, titulo, ws, n in hojas:
        R = f"'{clave}'!"; a0, a1 = 6, 5 + n
        E, K, I, L = (f"{R}{x}{a0}:{x}{a1}" for x in "EKIL")
        ws_res.cell(r, 1, clave); ws_res.cell(r, 2, titulo)
        ws_res.cell(r, 3, f'=COUNTA({R}D{a0}:D{a1})-COUNTIF({K},"Cancelado")')
        ws_res.cell(r, 4, f'=COUNTIF({K},"Hecho")')
        ws_res.cell(r, 5, f"=IFERROR(D{r}/C{r},0)")
        ws_res.cell(r, 6, f'=IFERROR((COUNTIFS({E},"Víctor",{K},"Hecho")+COUNTIFS({E},"Ambos",{K},"Hecho"))/(COUNTIF({E},"Víctor")+COUNTIF({E},"Ambos")),0)')
        ws_res.cell(r, 7, f'=IFERROR((COUNTIFS({E},"Diego",{K},"Hecho")+COUNTIFS({E},"Ambos",{K},"Hecho"))/(COUNTIF({E},"Diego")+COUNTIF({E},"Ambos")),0)')
        ws_res.cell(r, 8, f'=SUMIF({E},"Víctor",{I})+SUMIF({E},"Ambos",{I})')
        ws_res.cell(r, 9, f'=SUMIF({E},"Diego",{I})+SUMIF({E},"Ambos",{I})')
        ws_res.cell(r, 10, f'=COUNTIF({L},">0")')
        for j in (5, 6, 7):
            ws_res.cell(r, j).number_format = "0%"
        for j in range(1, 11):
            ws_res.cell(r, j).font = Font(name="Lato", size=10); ws_res.cell(r, j).border = BORDE
        r += 1
    fin = r - 1
    ws_res.cell(r, 1, "TOTAL").font = Font(name="Poppins", bold=True)
    ws_res.cell(r, 3, f"=SUM(C5:C{fin})"); ws_res.cell(r, 4, f"=SUM(D5:D{fin})"); ws_res.cell(r, 5, f"=IFERROR(D{r}/C{r},0)")
    ws_res.cell(r, 8, f"=SUM(H5:H{fin})"); ws_res.cell(r, 9, f"=SUM(I5:I{fin})"); ws_res.cell(r, 10, f"=SUM(J5:J{fin})")
    ws_res.cell(r, 5).number_format = "0%"
    ws_res.conditional_formatting.add(f"E5:G{fin}", DataBarRule(start_type="num", start_value=0, end_type="num", end_value=1, color=COBRE))
    ws_res.conditional_formatting.add(f"J5:J{fin}", FormulaRule(formula=["J5>0"], fill=PatternFill("solid", fgColor="F8D3D0")))
    ch = BarChart(); ch.type = "bar"; ch.title = "% de avance por sprint"; ch.y_axis.title = "avance"; ch.y_axis.scaling.max = 1
    ch.add_data(Reference(ws_res, min_col=5, min_row=4, max_row=fin), titles_from_data=True)
    ch.set_categories(Reference(ws_res, min_col=1, min_row=5, max_row=fin)); ch.height, ch.width = 9, 16
    ch.y_axis.number_format = "0%"; ch.legend = None
    ws_res.add_chart(ch, "L4")

    # ---- Carga por día ----
    estilo_hoja(ws_carga, "Carga por persona y día", "Rojo = más horas que el límite (2 h entre semana, 4 h fin de semana) o más de 4 tareas")
    for j, h in enumerate(["Fecha", "Día", "Límite (h)", "Horas Víctor", "Horas Diego", "Tareas Víctor", "Tareas Diego"], 1):
        c = ws_carga.cell(4, j, h); c.font = Font(name="Poppins", bold=True, color="FFFFFF", size=9.5); c.fill = PatternFill("solid", fgColor=COBRE)
        ws_carga.column_dimensions[get_column_letter(j)].width = 13
    dia, r = date(2026, 10, 12), 5
    while dia <= date(2027, 2, 12):
        ws_carga.cell(r, 1, dia).number_format = "dd-mmm-yy"
        ws_carga.cell(r, 2, f"=A{r}").number_format = "dddd"
        ws_carga.cell(r, 3, f"=IF(WEEKDAY(A{r},2)>5,4,2)")

        def suma(quien, col_valor):
            partes = []
            for clave, _, _, n in hojas:
                R = f"'{clave}'!"
                for q in (quien, "Ambos"):
                    if col_valor == "I":
                        partes.append(f'SUMIFS({R}$I$6:$I${5 + n},{R}$B$6:$B${5 + n},$A{r},{R}$E$6:$E${5 + n},"{q}")')
                    else:
                        partes.append(f'COUNTIFS({R}$B$6:$B${5 + n},$A{r},{R}$E$6:$E${5 + n},"{q}")')
            return "=" + "+".join(partes)
        ws_carga.cell(r, 4, suma("Víctor", "I")); ws_carga.cell(r, 5, suma("Diego", "I"))
        ws_carga.cell(r, 6, suma("Víctor", "N")); ws_carga.cell(r, 7, suma("Diego", "N"))
        for j in range(1, 8):
            ws_carga.cell(r, j).font = Font(name="Lato", size=9.5); ws_carga.cell(r, j).border = BORDE
        dia += timedelta(days=1); r += 1
    ws_carga.conditional_formatting.add(f"D5:E{r - 1}", FormulaRule(formula=["D5>$C5"], fill=PatternFill("solid", fgColor="F8D3D0")))
    ws_carga.conditional_formatting.add(f"F5:G{r - 1}", FormulaRule(formula=["F5>4"], fill=PatternFill("solid", fgColor="F8D3D0")))
    ws_carga.conditional_formatting.add(f"A5:G{r - 1}", FormulaRule(formula=["WEEKDAY($A5,2)>5"], fill=PatternFill("solid", fgColor=CLARO)))
    ws_carga.freeze_panes = "A5"

    # ---- Cómo usar ----
    estilo_hoja(guia, "Cronograma de la tesis · cómo usarlo", "Sprints semanales (Scrum): lunes a sábado tareas; domingo en la noche, revisión y planificación")
    texto = [
        ("Qué es", "Una hoja por sprint (semana de trabajo). Cada fila es una tarea con su día, responsable, lugar, resultado y cómo saber que está terminada."),
        ("Cada día", "Marca el Estado (Pendiente, En curso, Hecho, Movido, Cancelado) y la Fecha real cuando la termines. No borres filas."),
        ("Si una tarea se mueve", "Estado = Movido, escribe la fecha nueva en Notas y copia la fila al día nuevo. La original queda como registro."),
        ("Colores", "Verde = hecho · Amarillo = movido · Rojo = atrasado (pasó el día y no está hecho) · Gris tachado = cancelado."),
        ("Días de retraso", "Se calcula solo: fecha real − día planificado; si no hay fecha real y ya pasó el día, cuenta hasta hoy."),
        ("Resumen", "Avance por sprint y por persona, horas planificadas y tareas atrasadas, con gráfico. Se calcula solo."),
        ("Carga", "Horas y tareas por persona y día. Rojo si pasa de 2 h entre semana, 4 h el fin de semana o 4 tareas."),
        ("Domingo en la noche", "Revisión del sprint (qué hicimos, qué no, qué aprendimos) + 20 minutos de «explícame lo tuyo» + planificación del sprint siguiente. Lo que se decida se anota en 11_Planificacion/Bitacora_Semanal.md."),
        ("Entregable (issue)", "Cada tarea pertenece a un entregable que tiene su ficha en GitHub (issue). Ejemplo: «S1-07 (#7)» = entregable 7 del sprint 1, ficha #7 en github.com/l333x/Tesis_Torvesa/issues/7."),
        ("Códigos", "M1–M6 = metas de validación · A1–A47 = afirmaciones que necesitan fuente · LOPDP = ley de datos personales · BPMN = forma estándar de dibujar procesos. Todo está en Glosario.pdf (raíz del repo)."),
        ("Escenario A", "Si la tutora confirma el 15-dic como fecha obligatoria, se comprime diciembre y se eliminan primero las tareas marcadas con ✂."),
        ("Versión para la IA", "11_Planificacion/CRONOGRAMA.md se regenera desde este Excel (comando: python 99_Scripts/gestion/generar_cronograma.py --md)."),
    ]
    guia.column_dimensions["A"].width = 24; guia.column_dimensions["B"].width = 110
    for i, (k, v) in enumerate(texto, 4):
        guia.cell(i, 1, k).font = Font(name="Poppins", bold=True, color=AZUL)
        c = guia.cell(i, 2, v); c.font = Font(name="Lato", size=10.5); c.alignment = Alignment(wrap_text=True, vertical="top")
        guia.row_dimensions[i].height = 32
    wb.move_sheet("Resumen", offset=-(len(wb.sheetnames) - 2)); wb.move_sheet("Carga", offset=-(len(wb.sheetnames) - 3))
    wb.active = 0
    wb.save(XLSX)
    print("ok", XLSX, "·", sum(n for *_, n in hojas), "tareas en", len(hojas), "hojas de sprint")


# ---------------- CRONOGRAMA.md (versión para la IA) ----------------
def generar_md() -> None:
    wb = load_workbook(XLSX, data_only=False)
    usados = {}
    filas_dia = []
    for clave, titulo, *_ in SPRINTS:
        ws = wb[clave]
        for row in ws.iter_rows(min_row=6, values_only=True):
            if not row[3]:
                continue
            ent = str(row[12]).split(" ")[0]
            estado = row[10] or "Pendiente"
            usados.setdefault(ent, []).append(estado)
            f = row[1].date() if hasattr(row[1], "date") else row[1]
            fr = row[9].date().isoformat() if hasattr(row[9], "date") else (row[9] or "")
            filas_dia.append((clave, row[0], f.isoformat() if f else "", row[4], row[3], row[5], row[6], estado, fr))
    viejo = MD.read_text(encoding="utf-8") if MD.exists() else ""
    import re
    numeros = dict(re.findall(r"\*\*([A-Z]+\d*-\d+)\*\* .*· #(\d+)\s*$", viejo, re.M))
    L = ["---", "titulo: Cronograma maestro (versión para la IA)", "tipo: documento_vivo", f"actualizado: {date.today().isoformat()}",
         "fuente_de_verdad: 11_Planificacion/Cronograma_Tesis.xlsx", "tags: [cronograma, planificacion]", "---", "",
         "# Cronograma maestro — versión para la IA", "",
         "> [!info] Las personas usan `Cronograma_Tesis.xlsx`. Este archivo se regenera desde el Excel (`generar_cronograma.py --md`).",
         "> Las líneas de «Entregables» las lee `sincronizar_github.py` (formato fijo: no editar a mano).", "",
         "## Entregables (= issues de GitHub)"]
    for eid, (num, nombre, resp, entreg, hecho) in ENT.items():
        estados = usados.get(eid, [])
        x = "x" if estados and all(e in ("Hecho", "Cancelado") for e in estados) else " "
        n = str(num) if num else numeros.get(eid, "")
        arroba = {"Víctor": "@Victor", "Diego": "@Diego", "Ambos": "@Victor @Diego"}[resp]
        L.append(f"- [{x}] **{eid}** {nombre} · {arroba} · entregable: {entreg} · hecho: {hecho} · cierre: — · #{n}")
    L += ["", "## Tareas día a día", "", "| Sprint | ID | Día | Resp. | Tarea | Dónde | Resultado | Estado | Fecha real |", "|---|---|---|---|---|---|---|---|---|"]
    for f in filas_dia:
        L.append("| " + " | ".join(str(x).replace("|", "/") for x in f) + " |")
    MD.write_text("\n".join(L) + "\n", encoding="utf-8")
    print("ok", MD, len(filas_dia), "tareas")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--md", action="store_true"); a = ap.parse_args()
    if not a.md:
        if XLSX.exists():
            print(f"Ya existe {XLSX.name}: no se sobrescribe (tiene tus estados y fechas reales)."); sys.exit(1)
        crear()
    generar_md()
