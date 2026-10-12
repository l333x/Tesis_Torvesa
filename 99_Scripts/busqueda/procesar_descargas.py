"""Procesa los PDF que bajaste a 00_Inbox/descargas/ y los manda a 02_Fuentes/_Textos/<citekey>.pdf.

    python procesar_descargas.py            empareja cada PDF con su ficha (por DOI o por título) y lo mueve
    python procesar_descargas.py --simular  muestra qué haría

Si no encuentra la ficha, deja el PDF en descargas y lo reporta (créala con buscar.py o a mano).
Los PDF NO se suben a GitHub (pueden ser de bases con licencia): 02_Fuentes/_Textos/ está en .gitignore.
"""
from __future__ import annotations

import difflib, re, shutil, sys

sys.path.insert(0, __import__("os").path.dirname(__file__))
for s in (sys.stdout,):
    try: s.reconfigure(encoding="utf-8")
    except Exception: pass
from comun import BOVEDA, DESCARGAS, TEXTOS, conectar, exportar_csv, norm  # noqa: E402

RX_DOI = re.compile(r"10\.\d{4,9}/[^\s\"<>,;)\]]+", re.I)


def texto_pdf(p) -> str:
    try:
        import pymupdf
        d = pymupdf.open(p); return " ".join(d[i].get_text() for i in range(min(3, len(d))))
    except Exception:
        import pypdf
        r = pypdf.PdfReader(str(p)); return " ".join((r.pages[i].extract_text() or "") for i in range(min(3, len(r.pages))))


def main() -> int:
    simular = "--simular" in sys.argv
    db = conectar(); TEXTOS.mkdir(parents=True, exist_ok=True)
    pdfs = sorted(DESCARGAS.glob("*.pdf")) if DESCARGAS.exists() else []
    if not pdfs:
        print("No hay PDF en 00_Inbox/descargas/."); return 0
    filas = db.execute("SELECT citekey, doi, titulo_norm, ficha FROM fuentes").fetchall()
    for p in pdfs:
        t = texto_pdf(p); k = None
        m = RX_DOI.search(t)
        if m:
            doi = m.group(0).rstrip(".").lower()
            k = next((f for f in filas if f[1] and f[1].lower() == doi), None)
        if not k:
            cabeza = norm(t[:600])
            mejor = max(filas, key=lambda f: difflib.SequenceMatcher(None, f[2] or "", cabeza[:len(f[2] or "") + 40]).ratio(), default=None)
            if mejor and mejor[2] and mejor[2][:60] in cabeza:
                k = mejor
        if not k:
            print(f"  ?  {p.name}: no encontré su ficha (DOI {'sí' if m else 'no'} detectado). Se queda en descargas."); continue
        destino = TEXTOS / f"{k[0]}.pdf"
        print(f"  ✓  {p.name} → 02_Fuentes/_Textos/{destino.name}  (ficha {k[3]})")
        if simular:
            continue
        shutil.move(str(p), destino)
        ficha = BOVEDA / k[3]
        if ficha.exists():
            s = ficha.read_text(encoding="utf-8")
            s = re.sub(r'^texto_local: .*$', f'texto_local: "02_Fuentes/_Textos/{destino.name}"', s, count=1, flags=re.M)
            ficha.write_text(s, encoding="utf-8")
    exportar_csv(db)
    return 0


if __name__ == "__main__":
    sys.exit(main())
