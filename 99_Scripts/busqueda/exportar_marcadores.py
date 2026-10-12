"""Exporta la base de fuentes a un archivo de marcadores de Chrome (formato HTML estándar, se importa en un paso).

    python exportar_marcadores.py            -> 02_Fuentes/Marcadores_Fuentes_AAAA-MM-DD.html

Estructura: Tesis Torvesa / 1 Sirven (verificadas) · 2 Por revisar · 3 Por bajar a mano · 4 Videos por ver ·
5 No sirven (descartadas) · 6 Dónde buscar más · 7 Documentos y app. Cada carpeta se divide por categoría.
En Chrome: Configuración > Importar favoritos y configuración > «Archivo HTML de favoritos».
"""
from __future__ import annotations

import html, re, sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from comun import BOVEDA, conectar  # noqa: E402

HOY = date.today().isoformat()
SALIDA = BOVEDA / "02_Fuentes" / f"Marcadores_Fuentes_{HOY}.html"
CATS = {"Problema": "Problema", "Contexto": "Contexto (Ecuador y sector)", "Tecnologia_IA": "Tecnología e IA",
        "Evidencia_Datos": "Evidencia y datos (CRM, ventas)", "Metodologia": "Metodología", "Normativa": "Normativa",
        "Casos_Estudio": "Casos de estudio", "Costos_Viabilidad": "Costos y viabilidad"}

# PDF que hay que bajar a mano (bloqueo de editorial o sitios .gob.ec que no abren desde las herramientas)
POR_BAJAR = [
    ("Oldroyd 2011 · HBR · A9 (7× y 60×)", "https://www.researchgate.net/publication/298137032_The_short_life_of_online_sales_leads"),
    ("LOPDP 2021 · Registro Oficial 5.º Supl. 459 · A42", "https://www.registroficial.gob.ec/"),
    ("Reglamento LOPDP 2023 · Decreto 904 · A43", "https://spdp.gob.ec/"),
    ("INEC · Registro Estadístico de Empresas 2024", "https://www.ecuadorencifras.gob.ec/directoriodeempresas/"),
    ("CEPAL · Índice Latinoamericano de IA 2025 (informe completo)", "https://www.cepal.org/en/pressreleases/latin-america-and-caribbean-accelerate-adoption-artificial-intelligence-though"),
    ("Carguachi 2025 · tesis UEES constructoras · A28", "https://repositorio.uees.edu.ec/items/bb313b3e-d136-46ee-91a7-07d6fc192a6b"),
    ("Nyqvist 2024 · CME · A6", "https://doi.org/10.1080/01446193.2024.2416033"),
    ("Pollitt 2000 · Institutional amnesia · A8", "https://doi.org/10.1080/08109020050000627"),
    ("Galan 2023 · Knowledge loss and turnover · A8", "https://doi.org/10.1108/TLO-09-2022-0107"),
    ("Gregor y Hevner 2013 · MISQ · estructura DSR", "https://aisel.aisnet.org/misq/vol37/iss2/3/"),
    ("Zhang 2023 · Buildings · digitalización construcción", "https://www.mdpi.com/2075-5309/13/4/1092"),
]

DONDE_BUSCAR = {
    "Buscadores académicos": [
        ("OpenAlex", "https://openalex.org/"), ("Semantic Scholar", "https://www.semanticscholar.org/"),
        ("Google Académico (solo a mano)", "https://scholar.google.com/"), ("CORE (acceso abierto)", "https://core.ac.uk/"),
        ("DOAJ (revistas abiertas)", "https://doaj.org/"), ("arXiv", "https://arxiv.org/"),
    ],
    "América Latina (español)": [
        ("SciELO", "https://scielo.org/"), ("Redalyc", "https://www.redalyc.org/"), ("Dialnet", "https://dialnet.unirioja.es/"),
        ("Latindex", "https://www.latindex.org/"),
    ],
    "Repositorios de universidades (Ecuador)": [
        ("UPS · DSpace (tesis UPS)", "https://dspace.ups.edu.ec/"), ("RRAAE · red de repositorios del Ecuador", "https://rraae.cedia.edu.ec/"),
        ("UEES · repositorio", "https://repositorio.uees.edu.ec/"),
    ],
    "Datos y normas oficiales (Ecuador)": [
        ("INEC · Ecuador en cifras", "https://www.ecuadorencifras.gob.ec/"), ("Banco Central del Ecuador", "https://www.bce.fin.ec/"),
        ("Registro Oficial", "https://www.registroficial.gob.ec/"), ("Superintendencia de Protección de Datos", "https://spdp.gob.ec/"),
        ("SRI · consulta de RUC", "https://srienlinea.sri.gob.ec/"),
    ],
    "Organismos e informes": [
        ("CEPAL · repositorio", "https://repositorio.cepal.org/"), ("BID · publicaciones", "https://publications.iadb.org/"),
        ("OCDE · publicaciones", "https://www.oecd.org/en/publications.html"), ("Stanford AI Index", "https://hai.stanford.edu/ai-index"),
        ("McKinsey · State of AI", "https://www.mckinsey.com/capabilities/operations/our-insights/the-state-of-ai"),
        ("Gartner · sala de prensa (ventas)", "https://www.gartner.com/en/newsroom/topics/sales"),
    ],
    "Normas APA 7": [
        ("APA Style · ejemplos de referencias", "https://apastyle.apa.org/style-grammar-guidelines/references/examples"),
        ("APA · lista de verificación (PDF)", "https://apastyle.apa.org/instructional-aids/publication-manual-formatting-checklist.pdf"),
        ("APA · citar IA", "https://apastyle.apa.org/style-grammar-guidelines/references/examples/ai-references"),
        ("UTPL · APA 7 con leyes ecuatorianas (PDF)", "https://biblioteca.utpl.edu.ec/sites/default/files/manuales/normas_apa_7ma._edicion_biblioteca_utpl.pdf"),
    ],
    "Noticias Ecuador": [
        ("Primicias · tecnología", "https://www.primicias.ec/ciencia-tecnologia/"), ("Primicias · economía", "https://www.primicias.ec/economia/"),
    ],
}


def ficha_campo(ruta: str, campo: str) -> str:
    p = BOVEDA / (ruta or "")
    if not ruta or not p.exists():
        return ""
    m = re.search(rf'^{campo}:\s*"?(.*?)"?\s*$', p.read_text(encoding="utf-8"), re.M)
    return m.group(1).strip() if m else ""


def enlace(r: dict) -> str:
    if r["doi"]:
        return "https://doi.org/" + r["doi"]
    return r["url"] or ""


def nombre(r: dict, con_dato: bool = False) -> str:
    pri = (r["autores"] or "").split(";")[0].strip()
    institucion = re.search(r"Banco|Company|Research|Institut|OECD|OCDE|CEPAL|Redacci|Gartner|Zendesk|Technology|Universidad|Stanford|McKinsey|Salesforce|Asamblea|Ministerio", pri)
    if "," in pri:
        aut = pri.split(",")[0]
    elif institucion or len(pri.split()) > 3:
        aut = pri
    else:
        aut = pri.split()[-1] if pri.split() else ""
    aut = aut.strip() or r["citekey"]
    base = f"{aut} {r['anio'] or 's. f.'} · {(r['titulo'] or '')[:70]}"
    if con_dato:
        dato = ficha_campo(r["ficha"], "afirmacion")
        pag = ficha_campo(r["ficha"], "pagina")
        if dato:
            base += f" — {dato[:90]}" + (f" ({pag[:20]})" if pag else "")
    return base


def a(titulo: str, url: str, sangria: int) -> str:
    return f'{"    " * sangria}<DT><A HREF="{html.escape(url, quote=True)}" ADD_DATE="0">{html.escape(titulo)}</A>\n'


def carpeta(titulo: str, sangria: int, contenido: str) -> str:
    s = "    " * sangria
    return f'{s}<DT><H3 ADD_DATE="0">{html.escape(titulo)}</H3>\n{s}<DL><p>\n{contenido}{s}</DL><p>\n'


def por_categoria(filas: list[dict], sangria: int, con_dato: bool = False) -> str:
    out = ""
    grupos: dict[str, list[dict]] = {}
    for r in filas:
        grupos.setdefault(r["categoria"] or "Otros", []).append(r)
    for cat in sorted(grupos, key=lambda c: list(CATS).index(c) if c in CATS else 99):
        items = "".join(a(nombre(r, con_dato), enlace(r), sangria + 1)
                        for r in sorted(grupos[cat], key=lambda r: (-(int(r["anio"] or 0)), r["citekey"])) if enlace(r))
        out += carpeta(f"{CATS.get(cat, cat)} ({len(grupos[cat])})", sangria, items)
    return out


def main() -> int:
    c = conectar()
    c.row_factory = __import__("sqlite3").Row
    filas = [dict(r) for r in c.execute("SELECT * FROM fuentes")]
    ver = [r for r in filas if r["estado"] == "verificada"]
    vids = [r for r in filas if r["estado"] == "candidata" and r["tipo"] == "video"]
    rev = [r for r in filas if r["estado"] == "candidata" and r["tipo"] != "video"]
    des = [r for r in filas if r["estado"] == "descartada"]
    vig = [r for r in ver if int(r["anio"] or 0) >= 2021]
    his = [r for r in ver if int(r["anio"] or 0) < 2021]

    cuerpo = ""
    cuerpo += carpeta(f"1 Sirven · verificadas 2021+ ({len(vig)})", 2, por_categoria(vig, 3, True)
                      + (carpeta(f"Histórico antes de 2021 ({len(his)})", 3, "".join(a(nombre(r, True), enlace(r), 4) for r in his)) if his else ""))
    cuerpo += carpeta(f"2 Por revisar · candidatas ({len(rev)})", 2, por_categoria(rev, 3))
    cuerpo += carpeta(f"3 Por bajar a mano · PDF ({len(POR_BAJAR)})", 2, "".join(a(t, u, 3) for t, u in POR_BAJAR))
    cuerpo += carpeta(f"4 Videos por ver ({len(vids)})", 2, "".join(a(nombre(r), enlace(r), 3) for r in sorted(vids, key=lambda r: r["citekey"])))
    cuerpo += carpeta(f"5 No sirven · descartadas ({len(des)})", 2, por_categoria(des, 3))
    cuerpo += carpeta("6 Dónde buscar más", 2, "".join(carpeta(k, 3, "".join(a(t, u, 4) for t, u in v)) for k, v in DONDE_BUSCAR.items()))
    docs = [("App · Bitácora Torvesa", "https://claude.ai/artifact/3nSMYJPmZQ24tDKhyK9zwR"),
            ("Documento madre (PDF local)", (BOVEDA / "00_DOCUMENTO_MADRE.pdf").as_uri()),
            ("Base de fuentes 2021–2026 (PDF local)", (BOVEDA / "02_Fuentes/Base_Fuentes_2021-2026.pdf").as_uri()),
            ("Manual de redacción (PDF local)", (BOVEDA / "MANUAL_TESIS.pdf").as_uri()),
            ("Repositorio GitHub", "https://github.com/l333x/Tesis_Torvesa")]
    cuerpo += carpeta("7 Documentos y app", 2, "".join(a(t, u, 3) for t, u in docs))

    doc = ("<!DOCTYPE NETSCAPE-Bookmark-file-1>\n<META HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html; charset=UTF-8\">\n"
           "<TITLE>Bookmarks</TITLE>\n<H1>Bookmarks</H1>\n<DL><p>\n"
           + carpeta("Barra de favoritos", 1, carpeta(f"Tesis Torvesa · fuentes {HOY}", 2, cuerpo).replace("\n        ", "\n        ", 1))
           .replace('<H3 ADD_DATE="0">Barra de favoritos</H3>', '<H3 ADD_DATE="0" PERSONAL_TOOLBAR_FOLDER="true">Barra de favoritos</H3>', 1)
           + "</DL><p>\n")
    SALIDA.write_text(doc, encoding="utf-8")
    print(f"ok {SALIDA.relative_to(BOVEDA)} · sirven {len(vig)} + histórico {len(his)} · por revisar {len(rev)} · "
          f"por bajar {len(POR_BAJAR)} · videos {len(vids)} · descartadas {len(des)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
