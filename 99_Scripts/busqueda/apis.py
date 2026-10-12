"""Búsqueda por API (se prefiere siempre a la del navegador): OpenAlex, Crossref, Semantic Scholar."""
from __future__ import annotations

import os, re, time

try:
    import truststore; truststore.inject_into_ssl()  # la red usa un certificado propio: confiar en el almacén de Windows
except Exception:
    pass
import requests

UA = {"User-Agent": "TesisTorvesa-UPS/1.0 (investigacion academica; uso no comercial)"}
MAILTO = os.getenv("TESIS_MAILTO", "")  # opcional: pool «educado» de OpenAlex/Crossref (no se envía si está vacío)


def _get(url: str, params: dict, intentos: int = 3):
    for i in range(intentos):
        r = requests.get(url, params=params, headers=UA, timeout=30)
        if r.status_code == 429:
            time.sleep(5 * (i + 1)); continue
        r.raise_for_status(); return r.json()
    return None


def _abstract_openalex(inv: dict | None) -> str:
    if not inv:
        return ""
    pos = sorted((p, w) for w, ps in inv.items() for p in ps)
    return " ".join(w for _, w in pos)


def openalex(q: str, desde: int, hasta: int, n: int = 15) -> list[dict]:
    p = {"search": q, "per-page": n, "filter": f"from_publication_date:{desde}-01-01,to_publication_date:{hasta}-12-31"}
    if MAILTO: p["mailto"] = MAILTO
    j = _get("https://api.openalex.org/works", p) or {}
    out = []
    for w in j.get("results", []):
        loc = (w.get("primary_location") or {}).get("source") or {}
        out.append({"titulo": w.get("title") or w.get("display_name"), "anio": w.get("publication_year"),
                    "autores_lista": [a["author"]["display_name"] for a in w.get("authorships", []) if a.get("author")],
                    "doi": (w.get("doi") or "").replace("https://doi.org/", ""), "revista": loc.get("display_name", ""),
                    "tipo": {"article": "articulo", "book": "libro", "dissertation": "tesis"}.get(w.get("type"), w.get("type") or "articulo"),
                    "url": w.get("id"), "pdf_abierto": (w.get("open_access") or {}).get("oa_url") or "",
                    "resumen": _abstract_openalex(w.get("abstract_inverted_index")), "origen": "OpenAlex"})
    return out


def crossref(q: str, desde: int, hasta: int, n: int = 10) -> list[dict]:
    p = {"query": q, "rows": n, "filter": f"from-pub-date:{desde},until-pub-date:{hasta}"}
    if MAILTO: p["mailto"] = MAILTO
    j = _get("https://api.crossref.org/works", p) or {}
    out = []
    for it in (j.get("message") or {}).get("items", []):
        anio = ((it.get("issued") or {}).get("date-parts") or [[None]])[0][0]
        out.append({"titulo": (it.get("title") or [""])[0], "anio": anio,
                    "autores_lista": [f"{a.get('family', '')}, {a.get('given', '')}".strip(", ") for a in it.get("author", [])],
                    "doi": it.get("DOI", ""), "revista": (it.get("container-title") or [""])[0],
                    "tipo": {"journal-article": "articulo", "book": "libro", "book-chapter": "libro", "dissertation": "tesis", "report": "informe"}.get(it.get("type"), "articulo"),
                    "url": it.get("URL", ""), "resumen": re.sub(r"<[^>]+>", "", it.get("abstract", "") or ""), "origen": "Crossref"})
    return out


def semantic_scholar(q: str, desde: int, hasta: int, n: int = 10) -> list[dict]:
    j = _get("https://api.semanticscholar.org/graph/v1/paper/search",
             {"query": q, "limit": n, "year": f"{desde}-{hasta}",
              "fields": "title,authors,year,externalIds,abstract,venue,url,openAccessPdf"}) or {}
    return [{"titulo": p.get("title"), "anio": p.get("year"), "autores_lista": [a["name"] for a in p.get("authors", [])],
             "doi": (p.get("externalIds") or {}).get("DOI", ""), "revista": p.get("venue", ""), "url": p.get("url", ""),
             "pdf_abierto": (p.get("openAccessPdf") or {}).get("url", ""), "resumen": p.get("abstract") or "",
             "origen": "Semantic Scholar"} for p in j.get("data", [])]


API = {"openalex": openalex, "crossref": crossref, "semantic": semantic_scholar}
