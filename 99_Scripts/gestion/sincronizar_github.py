"""Sincroniza 11_Planificacion/CRONOGRAMA.md <-> GitHub (etiquetas, milestones, issues).

    python sincronizar_github.py            sincroniza (idempotente)
    python sincronizar_github.py --simular  muestra qué haría, sin tocar nada

Reglas:
- Una tarea sin '#n' -> se crea su issue y se escribe '#n' en el cronograma.
- '[x]' en el cronograma con el issue abierto -> se cierra el issue.
- Issue cerrado en GitHub con '[ ]' en el cronograma -> se marca '[x]' con la fecha de cierre.
- Responsables: @Victor -> l333x, @Diego -> psiceslivie (solo si ya aceptó la invitación).
- El tablero (Project) se descartó el 2026-10-11 por decisión de Víctor: no se intenta crear.
Requiere gh autenticado. No lee ni guarda tokens.
"""
from __future__ import annotations

import json, re, subprocess, sys
from datetime import date
from pathlib import Path

BOVEDA = Path(__file__).resolve().parents[2]
CRONO = BOVEDA / "11_Planificacion" / "CRONOGRAMA.md"
REPO = "l333x/Tesis_Torvesa"
USUARIOS = {"Victor": "l333x", "Diego": "psiceslivie"}
PROYECTO = "Tesis Torvesa"
SIMULAR = "--simular" in sys.argv
import shutil
GH = shutil.which("gh") or r"C:\Program Files\GitHub CLI\gh.exe"  # no depender del PATH heredado

ETIQUETAS = {
    "investigacion": ("1D4E89", "Fuentes, verificación, matriz de afirmaciones"),
    "documento": ("B87333", "Redacción de la tesis, planes, requisitos, finanzas"),
    "tecnico": ("0B1F3A", "Bóveda del sistema, RAG, flujos, PoC, pruebas"),
    "campo": ("2E8B57", "Instrumentos, aplicación y datos de campo"),
    "tutora": ("8E44AD", "Revisiones, actas y comunicación con la tutora"),
}
MILESTONES = {  # prefijo de ID -> (título, fecha límite)
    "S1": ("S1 · Levantamiento", "2026-10-18"), "S2": ("S2 · Redacción por capítulos", "2026-10-25"),
    "S3": ("S3 · Revisión 1 tutora", "2026-10-30"), "S4": ("S4 · Diseño", "2026-11-08"),
    "S5": ("S5 · Mejora continua", "2026-11-15"), "S6": ("S6 · Revisión 2 tutora", "2026-11-22"),
    "S7": ("S7 · Feedback + validación controlada", "2026-11-29"), "S8": ("S8 · Documentación del sistema", "2026-12-06"),
    "S9": ("S9 · Medición post y análisis", "2026-12-13"), "S10": ("S10 · Cierre e hito 90 %", "2026-12-20"),
    "H": ("Holgura · APA y pulido", "2027-01-03"), "E": ("Entrega", "2027-01-08"), "D": ("Defensa", "2027-02-12"),
}
LINEA = re.compile(r"^- \[(?P<x>[ xX])\] \*\*(?P<id>[A-Z]+\d*-\d+)\*\* (?P<tarea>.+?) · (?P<resp>(?:@\w+ ?)+) · "
                   r"entregable: (?P<ent>.+?) · hecho: (?P<hecho>.+?) · cierre: (?P<cierre>.+?) · #(?P<n>\d*)\s*$")

for s in (sys.stdout,):
    try: s.reconfigure(encoding="utf-8")
    except Exception: pass


def gh(*args: str, entrada: str | None = None, ok_falla: bool = False):
    r = subprocess.run([GH, *args], capture_output=True, text=True, encoding="utf-8", input=entrada)
    if r.returncode != 0 and not ok_falla:
        raise RuntimeError(f"gh {' '.join(args[:3])}…: {r.stderr.strip()}")
    return json.loads(r.stdout) if r.stdout.strip().startswith(("[", "{")) else r.stdout


def etiqueta_de(t: dict) -> str:
    txt = (t["tarea"] + " " + t["ent"]).lower()
    if re.search(r"tutora|revisión \d|acta", txt): return "tutora"
    if re.search(r"campo|instrumento|permiso|giro del negocio|tabulación|cronometraje", txt): return "campo"
    if re.search(r"fuentes|matriz afirmación|apa|bibliograf", txt): return "investigacion"
    if t["resp"].strip() == "@Diego": return "tecnico"
    return "documento"


def leer() -> tuple[list[str], list[dict]]:
    lineas = CRONO.read_text(encoding="utf-8").split("\n")
    tareas = []
    for i, l in enumerate(lineas):
        m = LINEA.match(l)
        if m:
            d = m.groupdict(); d["i"] = i; tareas.append(d)
    return lineas, tareas


def main() -> int:
    lineas, tareas = leer()
    print(f"{len(tareas)} tareas en el cronograma")
    colaboradores = {c["login"] for c in gh("api", f"repos/{REPO}/collaborators")}
    # etiquetas
    existentes = {e["name"] for e in gh("api", f"repos/{REPO}/labels?per_page=100")}
    for nombre, (color, desc) in ETIQUETAS.items():
        if nombre not in existentes and not SIMULAR:
            gh("api", f"repos/{REPO}/labels", "-f", f"name={nombre}", "-f", f"color={color}", "-f", f"description={desc}")
            print(f"  + etiqueta {nombre}")
    # milestones
    ms = {m["title"]: m["number"] for m in gh("api", f"repos/{REPO}/milestones?state=all&per_page=100")}
    for clave, (titulo, fecha) in MILESTONES.items():
        if titulo not in ms and not SIMULAR:
            r = gh("api", f"repos/{REPO}/milestones", "-f", f"title={titulo}", "-f", f"due_on={fecha}T23:59:00Z",
                   "-f", f"description=Ver 11_Planificacion/CRONOGRAMA.md")
            ms[titulo] = r["number"]; print(f"  + milestone {titulo} ({fecha})")
    # issues existentes
    issues = {i["number"]: i for i in gh("api", f"repos/{REPO}/issues?state=all&per_page=100", "--paginate")
              if "pull_request" not in i}
    cambios = 0
    for t in tareas:
        clave = re.match(r"[A-Z]+\d*", t["id"]).group(0)
        titulo_ms = MILESTONES[clave][0]
        asignar = [USUARIOS[u] for u in re.findall(r"@(\w+)", t["resp"]) if USUARIOS.get(u) in colaboradores]
        if not t["n"]:
            cuerpo = (f"**{t['id']}** · responsable: {t['resp'].strip()}\n\n**Entregable:** {t['ent']}\n\n"
                      f"**Hecho cuando:** {t['hecho']}\n\nFuente de verdad: `11_Planificacion/CRONOGRAMA.md`. "
                      f"Al cerrar: marcar [x] y la fecha en el cronograma, y registrar en `09_Registro_Contribuciones`.")
            if SIMULAR:
                print(f"  (simular) crear issue {t['id']} [{etiqueta_de(t)}] -> {titulo_ms} -> {asignar}"); continue
            args = ["api", f"repos/{REPO}/issues", "-f", f"title={t['id']} · {t['tarea']}", "-f", f"body={cuerpo}",
                    "-F", f"milestone={ms[titulo_ms]}", "-f", f"labels[]={etiqueta_de(t)}"]
            for a in asignar:
                args += ["-f", f"assignees[]={a}"]
            r = gh(*args)
            t["n"] = str(r["number"]); issues[r["number"]] = r
            lineas[t["i"]] = lineas[t["i"]].rstrip()[:-1] + f"#{r['number']}"
            cambios += 1; print(f"  + #{r['number']} {t['id']}")
            if t["x"].lower() == "x":
                gh("api", "-X", "PATCH", f"repos/{REPO}/issues/{r['number']}", "-f", "state=closed")
            continue
        iss = issues.get(int(t["n"]))
        if not iss:
            print(f"  ! {t['id']} apunta a #{t['n']}, que no existe"); continue
        marcada = t["x"].lower() == "x"
        if marcada and iss["state"] == "open":
            if not SIMULAR: gh("api", "-X", "PATCH", f"repos/{REPO}/issues/{t['n']}", "-f", "state=closed")
            print(f"  ✓ cierro #{t['n']} ({t['id']} marcada en el cronograma)"); cambios += 1
        elif not marcada and iss["state"] == "closed":
            fecha = (iss.get("closed_at") or date.today().isoformat())[:10]
            lineas[t["i"]] = lineas[t["i"]].replace("- [ ]", "- [x]", 1).replace("cierre: —", f"cierre: {fecha}")
            print(f"  ✓ marco [x] {t['id']} (issue #{t['n']} cerrado el {fecha})"); cambios += 1
        # asignar a Diego cuando acepte (idempotente)
        faltan = [a for a in asignar if a not in {x["login"] for x in iss.get("assignees", [])}]
        if faltan and not SIMULAR:
            args = ["api", f"repos/{REPO}/issues/{t['n']}/assignees"]
            for a in faltan:
                args += ["-f", f"assignees[]={a}"]
            gh(*args)
            print(f"  → asigno #{t['n']} a {', '.join(faltan)}"); cambios += 1
    if not SIMULAR:
        CRONO.write_text("\n".join(lineas), encoding="utf-8")
    # proyecto(tareas)  # tablero descartado (2026-10-11): no se intenta
    pend = "PiscesLivie" not in colaboradores
    print(f"\n{cambios} cambios." + ("  Diego aún no acepta la invitación: sus issues quedan sin asignar." if pend else ""))
    return 0


def proyecto(tareas: list[dict]) -> None:
    r = subprocess.run([GH, "project", "list", "--owner", "l333x", "--format", "json"], capture_output=True,
                       text=True, encoding="utf-8")
    if r.returncode != 0:
        print("  · Project: falta el permiso 'project' -> ejecuta tú:  gh auth refresh -s project"); return
    if SIMULAR: return
    pj = next((p for p in json.loads(r.stdout)["projects"] if p["title"] == PROYECTO), None)
    if not pj:
        pj = gh("project", "create", "--owner", "l333x", "--title", PROYECTO, "--format", "json")
        gh("project", "link", str(pj["number"]), "--owner", "l333x", "--repo", REPO, ok_falla=True)
        print(f"  + Project «{PROYECTO}» #{pj['number']}")
    hechos = {i["content"]["number"] for i in gh("project", "item-list", str(pj["number"]), "--owner", "l333x",
                                                  "--format", "json", "--limit", "500")["items"] if i.get("content")}
    for t in tareas:
        if t["n"] and int(t["n"]) not in hechos:
            gh("project", "item-add", str(pj["number"]), "--owner", "l333x",
               "--url", f"https://github.com/{REPO}/issues/{t['n']}")
    print(f"  · Project «{PROYECTO}»: {len(tareas)} issues en el tablero")


if __name__ == "__main__":
    sys.exit(main())
