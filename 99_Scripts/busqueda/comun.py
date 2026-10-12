"""Base de fuentes (SQLite + CSV) y creación de fichas candidatas. Común a buscar.py y procesar_descargas.py."""
from __future__ import annotations

import csv, json, re, sqlite3, unicodedata
from datetime import date
from pathlib import Path

BOVEDA = Path(__file__).resolve().parents[2]
DB = BOVEDA / "99_Scripts" / "datos" / "fuentes.sqlite"
CSV = BOVEDA / "99_Scripts" / "datos" / "fuentes.csv"
FUENTES = BOVEDA / "02_Fuentes"
DESCARGAS = BOVEDA / "00_Inbox" / "descargas"
TEXTOS = FUENTES / "_Textos"
CONSULTAS = json.loads((Path(__file__).parent / "consultas.json").read_text(encoding="utf-8"))
CAMPOS = ["citekey", "doi", "titulo", "autores", "anio", "revista", "tipo", "url", "pdf_abierto", "resumen", "origen",
          "consulta_id", "afirmaciones", "objetivos", "categoria", "estado", "fecha_alta", "ficha"]


def conectar() -> sqlite3.Connection:
    DB.parent.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(DB)
    c.execute(f"CREATE TABLE IF NOT EXISTS fuentes (id INTEGER PRIMARY KEY, {', '.join(f'{x} TEXT' for x in CAMPOS)}, titulo_norm TEXT)")
    c.execute("CREATE UNIQUE INDEX IF NOT EXISTS ux_cite ON fuentes(citekey)")
    c.execute("CREATE TABLE IF NOT EXISTS busquedas (id INTEGER PRIMARY KEY, fecha TEXT, consulta_id TEXT, origen TEXT, query TEXT, resultados INTEGER, nuevos INTEGER)")
    return c


def norm(t: str) -> str:
    t = unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


def citekey(c: sqlite3.Connection, autores: list[str], anio) -> str:
    # «Apellido1 Apellido2, Nombre» (Crossref) -> primer apellido; «Nombre Apellido» (OpenAlex) -> última palabra
    if autores and "," in autores[0]:
        ap = norm(autores[0].split(",")[0]).split(" ")[0]
    else:
        ap = norm(autores[0]).split(" ")[-1] if autores else "anonimo"
    base = f"{ap or 'anonimo'}_{anio or 'sf'}"
    k, i = base, 0
    while c.execute("SELECT 1 FROM fuentes WHERE citekey=?", (k,)).fetchone():
        i += 1; k = f"{base}{'abcdefghijklmnopqrstuvwxyz'[i - 1]}"
    return k


def apa(r: dict) -> str:
    """Referencia APA 7 aproximada a partir de los metadatos. SIEMPRE se revisa al verificar la fuente."""
    aut = r.get("autores_lista") or []
    def ini(nombre: str) -> str:
        if "," in nombre:
            ape, nom = [x.strip() for x in nombre.split(",", 1)]
        else:
            partes = nombre.split(); ape, nom = (partes[-1], " ".join(partes[:-1])) if len(partes) > 1 else (nombre, "")
        return f"{ape}, {' '.join(p[0] + '.' for p in nom.split() if p)}".strip().rstrip(",")
    if not aut:
        a = r.get("revista") or "Autor desconocido"
    elif len(aut) == 1:
        a = ini(aut[0])
    elif len(aut) <= 20:
        a = ", ".join(ini(x) for x in aut[:-1]) + ", & " + ini(aut[-1])
    else:
        a = ", ".join(ini(x) for x in aut[:19]) + ", … " + ini(aut[-1])
    s = f"{a} ({r.get('anio') or 's. f.'}). {r.get('titulo', '').rstrip('.')}."
    if r.get("revista"):
        s += f" *{r['revista']}*."
    if r.get("doi"):
        s += f" https://doi.org/{r['doi']}"
    elif r.get("url"):
        s += f" {r['url']}"
    return s


def existe(c: sqlite3.Connection, r: dict) -> bool:
    if r.get("doi") and c.execute("SELECT 1 FROM fuentes WHERE lower(doi)=lower(?)", (r["doi"],)).fetchone():
        return True
    return bool(c.execute("SELECT 1 FROM fuentes WHERE titulo_norm=?", (norm(r.get("titulo", "")),)).fetchone())


def guardar(c: sqlite3.Connection, r: dict, consulta: dict) -> str | None:
    """Inserta si no está (deduplica por DOI o título) y crea la ficha candidata. Devuelve el citekey si es nuevo."""
    if not r.get("titulo") or existe(c, r):
        return None
    k = citekey(c, r.get("autores_lista") or [], r.get("anio"))
    carpeta = FUENTES / consulta["categoria"]; carpeta.mkdir(parents=True, exist_ok=True)
    ficha = carpeta / f"{k}.md"
    fila = {"citekey": k, "doi": r.get("doi", ""), "titulo": r["titulo"], "autores": "; ".join(r.get("autores_lista") or []),
            "anio": str(r.get("anio") or ""), "revista": r.get("revista", ""), "tipo": r.get("tipo", "articulo"),
            "url": r.get("url", ""), "pdf_abierto": r.get("pdf_abierto", ""), "resumen": (r.get("resumen") or "")[:3000],
            "origen": r["origen"], "consulta_id": consulta["id"], "afirmaciones": ", ".join(consulta.get("afirmaciones", [])),
            "objetivos": ", ".join(consulta.get("objetivos", [])), "categoria": consulta["categoria"], "estado": "candidata",
            "fecha_alta": date.today().isoformat(), "ficha": ficha.relative_to(BOVEDA).as_posix()}
    c.execute(f"INSERT INTO fuentes ({', '.join(CAMPOS)}, titulo_norm) VALUES ({', '.join('?' * (len(CAMPOS) + 1))})",
              [fila[x] for x in CAMPOS] + [norm(r["titulo"])])
    if not ficha.exists():
        esc = lambda s: (s or "").replace('"', "'")  # noqa: E731
        ficha.write_text(f"""---
citekey: {k}
referencia_apa: "{esc(apa(r))}"
doi_url: "{('https://doi.org/' + r['doi']) if r.get('doi') else esc(r.get('url'))}"
anio: {r.get('anio') or ''}
tipo: {fila['tipo']}
categoria: {consulta['categoria']}
objetivos: [{', '.join(consulta.get('objetivos', []))}]
afirmaciones: [{', '.join(consulta.get('afirmaciones', []))}]
afirmacion: ""
cita_textual: ""
pagina: ""
confianza: medio
estado: candidata
verificada_por: ""
fecha_verificacion:
acceso: "{'abierto' if r.get('pdf_abierto') else 'por_revisar'}"
texto_local: ""
origen_busqueda: "{r['origen']} · consulta {consulta['id']} · {date.today().isoformat()}"
seminal: {'true' if r.get('seminal') else 'false'}
tags: [fuente, candidata]
---

# {esc(r['titulo'])}

> [!warning] Candidata: no se puede citar
> Ficha creada automáticamente desde **{r['origen']}**. La referencia APA es aproximada. Para pasarla a `estado: verificada`: abre la fuente, comprueba el dato, anota la página y la cita textual.

## Resumen (de la base de datos, no de la lectura)
{esc(r.get('resumen')) or '—'}

## Qué respalda
<!-- La idea con tus palabras (no copies el resumen). -->

## Cita textual
> «…» (p. X)

## Notas de verificación
""", encoding="utf-8")
    return k


def exportar_csv(c: sqlite3.Connection) -> None:
    with CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";"); w.writerow(CAMPOS)
        for row in c.execute(f"SELECT {', '.join(CAMPOS)} FROM fuentes ORDER BY consulta_id, anio DESC"):
            w.writerow(row)
