"""Genera Plan_Tesis_Torvesa_vX.Y.docx (+ PDF) desde CRONOGRAMA.md y las decisiones vigentes.

    python generar_plan.py --version 0.1

Versionado: Víctor edita el .docx (control de cambios o comentarios) → Claude lee sus cambios →
se actualizan las fuentes (.md) → se genera la versión siguiente. Nunca se sobrescribe una versión existente.
"""
from __future__ import annotations

import argparse, re, shutil, sys
from datetime import date
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from estilo_docx import Doc  # noqa: E402
from generar_informe import TAREA, MILESTONE_FIN, CRONO  # noqa: E402

BOVEDA = AQUI.parents[1]
DESTINO = BOVEDA / "11_Planificacion"
INFORMES = Path(r"F:\Respaldos_Tesis\Informes")
SEMANAS = [("S1", "S1 · 12–18 oct · Levantamiento"), ("S2", "S2 · 19–25 oct · Redacción por capítulos"),
           ("S3", "S3 · 26–30 oct · Revisión 1 con la tutora"), ("S4", "S4 · 2–8 nov · Diseño"),
           ("S5", "S5 · 9–15 nov · Mejora continua"), ("S6", "S6 · 16–22 nov · Revisión 2 con la tutora"),
           ("S7", "S7 · 23–29 nov · Feedback + arranque del piloto"), ("S8", "S8 · 30 nov–6 dic · Documentación del sistema"),
           ("S9", "S9 · 7–13 dic · Medición post y análisis"), ("S10", "S10 · 14–20 dic · Cierre e hito del 90 %"),
           ("H", "Holgura · 21 dic–3 ene"), ("E", "Entrega · 4–8 ene (A: 15-dic)"), ("D", "Defensa · 11 ene–12 feb")]

for s in (sys.stdout,):
    try: s.reconfigure(encoding="utf-8")
    except Exception: pass


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--version", default="0.1"); a = ap.parse_args()
    nombre = f"Plan_Tesis_Torvesa_v{a.version}"
    if (DESTINO / f"{nombre}.docx").exists():
        print(f"Ya existe {nombre}.docx: no se sobrescribe. Usa --version siguiente."); return 1
    tareas = [m.groupdict() for l in CRONO.read_text(encoding="utf-8").split("\n") if (m := TAREA.match(l))]
    d = Doc("Plan de la tesis", f"Versión {a.version} · borrador para corrección de Víctor",
            f"{date.today().isoformat()} · Víctor Segura · Diego Bermeo")
    par = d.aviso("**Cómo se corrige:** edita este Word con *control de cambios* activado o deja comentarios. "
                  "Claude lee tus cambios, actualiza CRONOGRAMA.md y las notas de origen, y genera la v0.2. "
                  "Esta versión no se sobrescribe.", "info")
    d.comentario(par, "Víctor: cada cambio que hagas aquí se lleva a la v0.2. Lo que no cambies se da por aprobado.")

    # 1. Alcance
    d.h1("1. Resumen del proyecto y alcance")
    d.p("**Tema aprobado (29-sep-2026):** «Diseño de un sistema de automatización para la gestión comercial en la "
        "Constructora Torvesa». Proyecto Técnico · Negocios Digitales · UPS Quito · Período 69. Tutora: Ing. Tania "
        "Alexandra Chicaiza Villalba.")
    d.p("**Objetivo general (aprobado):** diseñar un sistema que integre el CRM móvil TEAMSLASH con una bóveda de "
        "conocimiento comercial en Obsidian, un asistente de IA para respuestas y cotizaciones y un registro "
        "verificable de eventos, y validarlo en una operación experimental controlada de dos semanas.")
    d.tabla([["SÍ incluye", "NO incluye"],
             ["Diagnóstico AS-IS y línea base medida en campo (15–16 oct)", "Implementación definitiva en Torvesa (decisión de la empresa)"],
             ["Diseño TO-BE: bóveda, asistente de IA, registro de eventos", "Negociación, facturación, ejecución de obra"],
             ["Prueba de concepto y validación controlada (24-nov → 5-dic)", "Gestión del personal (dotación, cargas)"],
             ["Viabilidad técnica y económica: CAPEX, OPEX, VAN y TIR del sistema para Torvesa", "Contratación pública (SNCP)"],
             ["Cumplimiento LOPDP: consentimiento, minimización, anonimización", "Evaluación financiera del SaaS TEAMSLASH (solo anexo)"],
             ["Manual básico, gobierno de la información y transferencia", "Datos del diagnóstico simulado del proyecto integrador"]],
            anchos=[8.3, 8.3])

    # 2. Escenarios
    d.h1("2. Escenarios de entrega")
    t = d.tabla([["", "Escenario B (base)", "Escenario A (15-dic, fecha dura)"],
                 ["Cierre", "7–20 dic", "7–11 dic"], ["Hito del 90 %", "18 dic", "11 dic"],
                 ["Entrega", "4–8 ene", "15 dic"], ["Holgura APA", "21 dic–3 ene", "En paralelo desde S8"],
                 ["Se recorta", "—", "Pruebas de carga · ciclos diarios con la tutora (solo 2) · manual básico · APA por capítulo"]])
    d.comentario(t.cell(0, 2).paragraphs[0], "Pendiente: confirmar con la tutora si el 15-dic es fecha dura (D5).")
    d.p("**Intocable en ambos:** el trabajo de campo de S1, las revisiones 1 y 2 con la tutora, la medición post del "
        "piloto y el hito del 90 %. **Piloto:** 24-nov → 5-dic, con medición post del 7 al 9 de diciembre.")

    # 3. Cronograma
    d.h1("3. Cronograma semanal")
    for clave, titulo in SEMANAS:
        filas = [t for t in tareas if re.match(rf"^{clave}-", t["id"])]
        if not filas:
            continue
        d.h2(titulo)
        d.tabla([["ID", "Actividad", "Resp.", "Entregable", "Criterio de «hecho»", "#"]] +
                [[t["id"], t["tarea"], t["resp"].replace("@", "").strip(), t["ent"], t["hecho"], f"#{t['n']}"] for t in filas],
                anchos=[1.5, 4.6, 1.7, 3.8, 4.0, 1.2])

    # 4. Reparto
    d.h1("4. División del trabajo, sincronización y dependencias")
    d.tabla([["Víctor", "Diego"],
             ["Documento de tesis, investigación, fuentes y APA 7", "Bóveda del sistema y RAG"],
             ["Instrumentos, campo y análisis financiero (CAPEX, OPEX, VAN, TIR)", "Flujogramas AS-IS/TO-BE y arquitectura"],
             ["Relación con la tutora y con Torvesa", "Prueba de concepto, casos de prueba, pruebas de uso y de carga"]], anchos=[8.3, 8.3])
    d.h3("Puntos de sincronización")
    for x in ["**Domingo 21:00:** informe automático de avance (tareas, commits por autor, decisiones). Antes de esa hora, todo en `main`.",
              "**Lunes:** 20 min por llamada: qué se cierra esta semana, bloqueos y dependencias.",
              "**Antes de cada revisión con la tutora:** ensayo conjunto de la presentación."]:
        d.vineta(x)
    d.h3("Dependencias críticas")
    d.tabla([["Antes", "→ Después", "Por qué"],
             ["S1-05 permisos de gerencia", "S1-08/09 campo", "Sin autorización no hay cronometraje ni muestra documental"],
             ["S1-12 datos consolidados", "S2-01 Cap. 1 · S2-04 análisis", "La línea base real reemplaza al diagnóstico simulado"],
             ["S4-01 TO-BE + S4-02 validación de Víctor", "S4-03 bóveda del sistema", "Diego no levanta la bóveda sin flujos aprobados"],
             ["S5-04 PoC estable", "S7-03 piloto", "No hay validación controlada sin un prototipo que funcione"],
             ["S7-03 piloto (24-nov → 5-dic)", "S9-01 medición post", "La comparación pre-post necesita las dos semanas completas"]],
            anchos=[5.0, 5.0, 6.6])

    # 5. Carga
    d.h1("5. Carga realista y plan de contingencia")
    d.p("Entre semana, bloques de 1–2 h; fin de semana, 3–4 h. Ninguna semana pide más de unas 12 h por persona.")
    d.tabla([["Orden", "Si se pierde una semana, se recorta…"],
             ["1", "Lo marcado ✂ en el cronograma (pruebas de carga, ciclos diarios con la tutora, manual completo)"],
             ["2", "El inventario de herramientas pasa a una tabla corta"], ["3", "2 casos de prueba en vez de 3"],
             ["4", "La matriz de riesgos baja a 10 riesgos"], ["5", "Se fusiona la documentación del sistema con el capítulo de resultados"],
             ["Nunca", "Campo · revisiones con la tutora · medición post · hito del 90 % · verificación de fuentes"]], anchos=[2.2, 14.4])

    # 6. Matriz
    d.h1("6. Matriz objetivos ↔ fuentes ↔ capítulos")
    t = d.tabla([["OVA", "Objetivo específico", "Capítulo previsto", "Afirmaciones (F0)", "Fuentes verificadas"],
                 ["4.1 Diagnosticar problemas", "OE1", "Cap. 1 y Cap. 4", "A1–A8", "fase 1"],
                 ["5.1 Analizar datos de desempeño", "OE1", "Cap. 4", "línea base de campo", "fase 1"],
                 ["4.2 Formular alternativas", "OE2", "Cap. 5", "A26–A30, A37", "fase 1"],
                 ["6.2 Viabilidad técnica y económica", "OE2", "Cap. 5", "A31–A36", "fase 1"],
                 ["6.3 Seguridad y normativa", "OE2", "Cap. 2 y Cap. 5", "A42–A45", "fase 1"],
                 ["4.3 Métodos de la profesión", "OE3", "Cap. 3", "A39–A41, A47", "fase 1"],
                 ["6.1 Soluciones innovadoras", "OE3", "Cap. 5", "A37, A38", "fase 1"],
                 ["5.4 Impacto con KPI", "OE4", "Cap. 6", "A9–A10, A20–A25", "fase 1"],
                 ["5.3 Plan de implementación", "OE5", "Cap. 6 y anexos", "—", "fase 1"]],
                anchos=[4.4, 2.2, 3.2, 3.6, 3.2])
    d.comentario(t.cell(0, 4).paragraphs[0], "Se completa con el corte de la fase 1 (miércoles 14): matriz afirmación → fuentes → estado.")

    # 7. Reglas
    d.h1("7. Reglas")
    d.h3("Obligatorio")
    for x in ["Toda cifra o afirmación empírica lleva una fuente **verificada** (abierta, con página) y referencia APA 7.",
              "Trazabilidad: cada párrafo se puede rastrear hasta fichas en 02_Fuentes.",
              "Consentimiento informado y anonimización (LOPDP) en encuestas, entrevistas y observación; registro de procedencia P1.",
              "Registrar cada entregable en 09_Registro_Contribuciones: autor, fecha y herramienta de IA.",
              "Declarar el uso de IA según la política de la UPS (por confirmar en la fase 1).",
              "Auditoría PII antes de cada push con datos; los datos crudos solo en _crudo/."]:
        d.vineta(x)
    d.h3("Prohibido")
    for x in ["Inventar fuentes, autores, DOIs, páginas o citas.", "Citar una fuente que no esté «verificada».",
              "Parafrasear pegado al original.", "Usar los datos simulados del diagnóstico como dato empírico.",
              "Guardar datos personales de clientes o colaboradores sin anonimizar fuera de _crudo/.",
              "Presentar el proyecto como «implementado».",
              "Mover, renombrar o borrar archivos sin aprobación; sobrescribir versiones editadas por Víctor.",
              "Avanzar de fase sin la validación de Víctor."]:
        d.vineta(x)

    # 8. Riesgos
    d.h1("8. Riesgos del cronograma y mitigación")
    t = d.tabla([["Riesgo", "Prob.", "Impacto", "Mitigación"],
                 ["La tutora no acepta el cambio de datos simulados → línea base real", "Media", "Alto", "Escribirle antes de la Revisión 1; llevar el protocolo de procedencia y los datos nuevos"],
                 ["Sin permisos de gerencia para el campo del 15–16 oct", "Media", "Alto", "Pedirlos el lunes 12; plan B: autorregistro de cotizaciones por 2 semanas"],
                 ["Pocas solicitudes durante el piloto (33 clientes)", "Alta", "Medio", "Reportar casos individuales; sumar la muestra documental P2-B como línea base; no forzar pruebas inferenciales"],
                 ["El 15-dic resulta fecha dura", "Media", "Alto", "Escenario A ya planificado; recortes ✂ definidos"],
                 ["El formato oficial de capítulos llega tarde", "Media", "Medio", "Redactar por secciones del diseño aprobado; reacomodar al llegar"],
                 ["PoC inestable antes del piloto", "Media", "Alto", "PoC en S5 con una semana de margen; casos de prueba antes del piloto"],
                 ["Fuentes clave sin acceso al texto completo", "Media", "Medio", "Marcar «solo resumen»; buscar alternativas abiertas; reformular la afirmación"],
                 ["Fuga de datos personales en el repo", "Baja", "Alto", "_crudo/ ignorado por Git; auditoría PII antes de cada push; códigos en vez de nombres"]],
                anchos=[6.0, 1.6, 1.8, 7.2])
    d.comentario(t.cell(1, 0).paragraphs[0], "Víctor: este es el riesgo más alto hoy; depende de tu correo a la tutora.")

    # 9. Plantillas
    d.h1("9. Plantillas")
    d.h3("Acta de reunión con la tutora")
    d.tabla([["Campo", "Contenido"], ["Fecha / revisión", "AAAA-MM-DD · Revisión N"], ["Asistentes", "Tania Chicaiza · Víctor Segura · Diego Bermeo"],
             ["Qué se presentó", ""], ["Observaciones (textuales)", "# · observación · capítulo · responsable · plazo · estado"],
             ["Decisiones", ""], ["Cambios pendientes de aprobación", ""], ["Próxima reunión", "fecha · qué se lleva"]], anchos=[5.0, 11.6])
    d.h3("Registro de contribuciones")
    d.tabla([["Fecha", "Entregable", "Autor", "Herramienta de IA y uso", "Revisado por", "Ruta"],
             ["AAAA-MM-DD", "", "Víctor / Diego", "p. ej. Claude: borrador de X", "", "carpeta/archivo"]],
            anchos=[2.2, 4.0, 2.4, 3.8, 2.0, 2.2])

    salida = d.guardar(DESTINO / f"{nombre}.docx", pdf=True)  # comentarios solo en el Word (el PDF con marcas encoge las tablas)
    INFORMES.mkdir(parents=True, exist_ok=True)
    for f in salida:
        shutil.copy2(f, INFORMES / f.name); print("ok", f, "+ copia en Informes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
