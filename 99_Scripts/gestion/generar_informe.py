"""Informe de avance semanal en Word + PDF (azul marino + cobre, Poppins/Lato).

    python generar_informe.py                       semana más reciente de la bitácora, últimos 7 días
    python generar_informe.py --seccion 2026-10-11 --desde 2026-10-11 --hasta 2026-10-11
    python generar_informe.py --sin-copia-repo      no copia el PDF al repo

Fuentes: 11_Planificacion/Bitacora_Semanal.md (resumen, decisiones, riesgos, atención, próxima semana),
11_Planificacion/CRONOGRAMA.md (tareas) y git log (commits por autor).
Salida: F:\\Respaldos_Tesis\\Informes\\AAAA-MM-DD_Informe_Avance.docx/.pdf y, si la auditoría PII del PDF
sale limpia, una copia del PDF en 11_Planificacion/Informes/.
"""
from __future__ import annotations

import argparse, re, shutil, subprocess, sys
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI)); sys.path.insert(0, str(AQUI.parent))
from estilo_docx import Doc  # noqa: E402
from auditoria_pii import PATRONES, PERMITIDOS, texto as texto_de  # noqa: E402

BOVEDA = AQUI.parents[1]
BITACORA = BOVEDA / "11_Planificacion" / "Bitacora_Semanal.md"
CRONO = BOVEDA / "11_Planificacion" / "CRONOGRAMA.md"
SALIDA = Path(r"F:\Respaldos_Tesis\Informes")
COPIA_REPO = BOVEDA / "11_Planificacion" / "Informes"
TAREA = re.compile(r"^- \[(?P<x>[ xX])\] \*\*(?P<id>[A-Z]+\d*-\d+)\*\* (?P<tarea>.+?) · (?P<resp>(?:@\w+ ?)+) · "
                   r"entregable: (?P<ent>.+?) · hecho: (?P<hecho>.+?) · cierre: (?P<cierre>.+?) · #(?P<n>\d*)\s*$")
SEMANA = re.compile(r"^## (?P<sem>.+)$", re.M)
MILESTONE_FIN = {"S1": "2026-10-18", "S2": "2026-10-25", "S3": "2026-10-30", "S4": "2026-11-08", "S5": "2026-11-15",
                 "S6": "2026-11-22", "S7": "2026-11-29", "S8": "2026-12-06", "S9": "2026-12-13", "S10": "2026-12-20",
                 "H": "2027-01-03", "E": "2027-01-08", "D": "2027-02-12"}

for s in (sys.stdout,):
    try: s.reconfigure(encoding="utf-8")
    except Exception: pass


def seccion_bitacora(clave: str | None) -> tuple[str, dict[str, list[str]]]:
    t = BITACORA.read_text(encoding="utf-8")
    partes = [(m.group("sem"), m.end()) for m in SEMANA.finditer(t) if re.match(r"\d{4}-\d{2}-\d{2}", m.group("sem"))]
    if not partes:
        raise SystemExit("La bitácora no tiene secciones '## AAAA-MM-DD · título'.")
    elegida = next((p for p in partes if clave and p[0].startswith(clave)), partes[-1])
    i = partes.index(elegida)
    fin = t.find("\n## ", elegida[1]) if i == len(partes) - 1 else t.find(f"## {partes[i + 1][0]}")
    cuerpo = t[elegida[1]: fin if fin > 0 else None]
    sub: dict[str, list[str]] = {}
    actual = None
    for l in cuerpo.split("\n"):
        m = re.match(r"^### (.+)", l)
        if m:
            actual = m.group(1).strip(); sub[actual] = []
        elif actual and re.match(r"^\s*[-*] ", l):
            sub[actual].append(re.sub(r"^\s*[-*] ", "", l).strip())
    return elegida[0], sub


def tareas() -> list[dict]:
    out = []
    for l in CRONO.read_text(encoding="utf-8").split("\n"):
        m = TAREA.match(l)
        if m:
            d = m.groupdict(); d["hecha"] = d["x"].lower() == "x"
            d["fin"] = MILESTONE_FIN.get(re.match(r"[A-Z]+\d*", d["id"]).group(0), "2099-01-01")
            out.append(d)
    return out


def commits(desde: str, hasta: str) -> list[dict]:
    r = subprocess.run(["git", "log", f"--since={desde} 00:00", f"--until={hasta} 23:59:59",
                        "--format=%h%x1f%an%x1f%ad%x1f%s", "--date=short"], cwd=BOVEDA, capture_output=True,
                       text=True, encoding="utf-8")
    return [dict(zip(("hash", "autor", "fecha", "asunto"), l.split("\x1f"))) for l in r.stdout.strip().split("\n") if l]


def auditar(pdf: Path) -> int:
    t = texto_de(pdf)
    return sum(1 for rx in PATRONES.values() for m in set(rx.findall(t)) if m not in PERMITIDOS)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seccion"); ap.add_argument("--desde"); ap.add_argument("--hasta")
    ap.add_argument("--sin-copia-repo", action="store_true"); ap.add_argument("--sin-pdf", action="store_true")
    a = ap.parse_args()
    hoy = date.today()
    hasta = a.hasta or hoy.isoformat()
    desde = a.desde or (datetime.fromisoformat(hasta).date() - timedelta(days=6)).isoformat()
    titulo_sem, sec = seccion_bitacora(a.seccion)
    ts = tareas(); cs = commits(desde, hasta)
    cerradas = [t for t in ts if t["hecha"] and desde <= t["cierre"][:10] <= hasta]
    vencidas = [t for t in ts if not t["hecha"] and t["fin"] < hasta]
    proximas = [t for t in ts if not t["hecha"] and hasta <= t["fin"] <= (datetime.fromisoformat(hasta).date()
                                                                          + timedelta(days=14)).isoformat()]
    por_autor = Counter(c["autor"] for c in cs)

    nombre_titulo = titulo_sem.split("·", 1)[-1].strip()
    d = Doc(nombre_titulo, f"Informe de avance · periodo {desde} → {hasta}", f"Generado el {hoy.isoformat()}")

    if titulo_sem[:10] < desde:
        par = d.aviso(f"La bitácora no tiene sección para este periodo: se usó la del {titulo_sem[:10]}. "
                      f"Las tareas y los commits sí son de {desde} → {hasta}.", "alerta")
        d.comentario(par, "Víctor: agrega la sección de esta semana en Bitacora_Semanal.md y regenera el informe.")

    d.h1("Resumen ejecutivo")
    d.tabla([["Tareas cerradas", "Vencidas sin cerrar", "Pendientes (14 días)", "Commits", "Decisiones pendientes"],
             [str(len(cerradas)), str(len(vencidas)), str(len(proximas)), str(len(cs)),
              str(sum("⏳" in x for x in sec.get("Decisiones", [])))]])
    for x in sec.get("Resumen", []):
        d.vineta(x)

    d.h1("Decisiones")
    for x in sec.get("Decisiones", []):
        par = d.vineta(x)
        if "⏳" in x:
            d.comentario(par, "Decisión pendiente: necesita confirmación (tutora o Víctor) antes de avanzar.")

    if sec.get("Hecho"):
        d.h1("Lo que se hizo")
        for x in sec["Hecho"]:
            d.vineta(x)

    d.h1("Tareas del cronograma")
    d.h2(f"Cerradas en el periodo ({len(cerradas)})")
    if cerradas:
        d.tabla([["ID", "Tarea", "Responsable", "Cierre", "Issue"]] +
                [[t["id"], t["tarea"], t["resp"].strip(), t["cierre"], f"#{t['n']}"] for t in cerradas])
    else:
        d.p("Ninguna tarea del cronograma cerrada en este periodo.")
    if vencidas:
        d.h2(f"Vencidas sin cerrar ({len(vencidas)})")
        tv = d.tabla([["ID", "Tarea", "Responsable", "Límite", "Issue"]] +
                     [[t["id"], t["tarea"], t["resp"].strip(), t["fin"], f"#{t['n']}"] for t in vencidas])
        d.comentario(tv.cell(1, 1).paragraphs[0], "Hay tareas vencidas: decidir si se reprograman o se recortan (plan de contingencia del cronograma).")
    d.h2(f"Pendientes de los próximos 14 días ({len(proximas)})")
    d.tabla([["ID", "Tarea", "Responsable", "Límite", "Issue"]] +
            [[t["id"], t["tarea"], t["resp"].strip(), t["fin"], f"#{t['n']}"] for t in proximas] if proximas
            else [["—"], ["Sin pendientes en la ventana"]])

    d.h1("Commits por autor")
    if cs:
        d.tabla([["Autor", "Commits"]] + [[k, str(v)] for k, v in por_autor.most_common()])
        d.tabla([["Fecha", "Autor", "Commit", "Mensaje"]] + [[c["fecha"], c["autor"], c["hash"], c["asunto"][:90]] for c in cs])
    else:
        d.p("Sin commits en el periodo.")

    d.h1("Riesgos y bloqueos")
    for x in sec.get("Riesgos y bloqueos", []):
        d.vineta(x)

    if sec.get("Atención de Víctor"):
        d.h1("Requiere tu atención o decisión")
        for x in sec["Atención de Víctor"]:
            par = d.check(x, False)
            d.comentario(par, f"Víctor: {re.sub(r'[*`]', '', x)}", autor="Claude", iniciales="CL")

    d.h1("Próxima semana")
    for x in sec.get("Próxima semana", []):
        d.vineta(x)

    d.p("")
    d.aviso("Fuentes del informe: Bitacora_Semanal.md, CRONOGRAMA.md y git log del repo l333x/Tesis_Torvesa. "
            "Generado por 99_Scripts/gestion/generar_informe.py.", "info")

    nombre = f"{hasta}_Informe_Avance"
    archivos = d.guardar(SALIDA / f"{nombre}.docx", pdf=not a.sin_pdf, con_comentarios=True)
    for f in archivos:
        print("ok", f)
    if not a.sin_pdf and not a.sin_copia_repo:
        pdf = archivos[-1]
        n = auditar(pdf)
        if n:
            print(f"!! La auditoría PII encontró {n} coincidencias en el PDF: NO se copia al repo.")
            return 1
        COPIA_REPO.mkdir(parents=True, exist_ok=True)
        shutil.copy2(pdf, COPIA_REPO / pdf.name)
        print(f"ok copia al repo (PII: 0) -> {COPIA_REPO / pdf.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
