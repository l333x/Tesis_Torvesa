"""Búsqueda asistida de fuentes para la tesis.

    python buscar.py --lista                            ver las consultas (P01…, M01…, D01…)
    python buscar.py --consulta P01 M05                 consultas concretas (APIs + navegador)
    python buscar.py --afirmacion A9 A10                todas las consultas ligadas a esas afirmaciones
    python buscar.py --para Diego                       todas las consultas de Diego
    python buscar.py --consulta P01 --solo-api          sin navegador
    python buscar.py --consulta P01 --sitios redalyc scielo   elegir sitios del navegador (por defecto: redalyc)
    python buscar.py --consulta N01 --asistido          tú buscas en la biblioteca UPS y el script lee los resultados
    python buscar.py --desde 2015                       ampliar años (por defecto 2023–2026; lo seminal va aparte)

Guarda en 99_Scripts/datos/fuentes.sqlite + fuentes.csv y crea fichas candidatas en 02_Fuentes/<categoría>/.
"""
from __future__ import annotations

import argparse, sys, time
from datetime import date

sys.path.insert(0, __import__("os").path.dirname(__file__))
for s in (sys.stdout,):
    try: s.reconfigure(encoding="utf-8")
    except Exception: pass
from comun import CONSULTAS, DESCARGAS, conectar, exportar_csv, guardar  # noqa: E402
import apis  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lista", action="store_true"); ap.add_argument("--consulta", nargs="*", default=[])
    ap.add_argument("--afirmacion", nargs="*", default=[]); ap.add_argument("--para", choices=["Víctor", "Victor", "Diego"])
    ap.add_argument("--solo-api", action="store_true"); ap.add_argument("--asistido", action="store_true")
    ap.add_argument("--sitios", nargs="*", default=["redalyc"]); ap.add_argument("--apis", nargs="*", default=["openalex", "crossref", "semantic"])
    ap.add_argument("--desde", type=int, default=2023); ap.add_argument("--hasta", type=int, default=2026)
    ap.add_argument("--max", type=int, default=12, help="resultados por fuente y consulta")
    a = ap.parse_args()
    if a.lista:
        for c in CONSULTAS:
            print(f"{c['id']}  [{c['para']:<6}] {c['tema']:<42} afirmaciones: {', '.join(c['afirmaciones']) or '—'}")
        return 0
    para = "Víctor" if a.para == "Victor" else a.para
    sel = [c for c in CONSULTAS if c["id"] in a.consulta or set(c["afirmaciones"]) & set(a.afirmacion) or (para and c["para"] == para)]
    if not sel:
        print("No hay consultas seleccionadas. Usa --lista para verlas."); return 1
    db = conectar(); total_nuevos = 0
    ctx = pw = None
    if not a.solo_api:
        import navegador
        pw, _, ctx = navegador.conectar(); navegador.descargas_a(ctx, DESCARGAS)
    try:
        for c in sel:
            print(f"\n== {c['id']} · {c['tema']}")
            for idioma in ("en", "es"):
                q = c[idioma]
                for nombre in a.apis:
                    try:
                        res = apis.API[nombre](q, a.desde, a.hasta, a.max)
                    except Exception as e:
                        print(f"  {nombre}: no respondió ({type(e).__name__})"); continue
                    nuevos = [k for r in res if (k := guardar(db, r, c))]
                    db.execute("INSERT INTO busquedas (fecha, consulta_id, origen, query, resultados, nuevos) VALUES (?,?,?,?,?,?)",
                               (date.today().isoformat(), c["id"], nombre, q, len(res), len(nuevos)))
                    print(f"  {nombre:<9} «{q}»: {len(res)} resultados, {len(nuevos)} nuevos"); total_nuevos += len(nuevos)
                    time.sleep(1.5)
            for titulo in c.get("seminal", []):  # fuente fundadora: se busca por título, sin filtro de años
                for r in apis.openalex(titulo, 1900, a.hasta, 3)[:1]:
                    r["seminal"] = True
                    if (k := guardar(db, r, c)):
                        print(f"  seminal: {k}"); total_nuevos += 1
            if ctx:
                import navegador
                for sitio in (["asistido"] if a.asistido else a.sitios):
                    q = c["es"]
                    try:
                        res = [r for r in navegador.buscar(ctx, sitio, q) if not r["anio"] or r["anio"] >= a.desde]
                    except Exception as e:
                        print(f"  {sitio}: error ({str(e)[:80]})"); continue
                    nuevos = [k for r in res if (k := guardar(db, r, c))]
                    db.execute("INSERT INTO busquedas (fecha, consulta_id, origen, query, resultados, nuevos) VALUES (?,?,?,?,?,?)",
                               (date.today().isoformat(), c["id"], sitio, q, len(res), len(nuevos)))
                    print(f"  {sitio:<9} «{q}»: {len(res)} resultados ({a.desde}+), {len(nuevos)} nuevos"); total_nuevos += len(nuevos)
                    navegador.pausa_humana()
            db.commit()
    finally:
        db.commit(); exportar_csv(db)
        if pw:
            pw.stop()
    print(f"\nListo: {total_nuevos} fuentes nuevas (candidatas). Base: 99_Scripts/datos/fuentes.sqlite · fichas en 02_Fuentes/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
