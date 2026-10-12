"""RAG local de la bóveda Tesis_Torvesa.

    python rag.py indexar [--reconstruir]     indexa solo lo que cambió (hash SHA-256)
    python rag.py consultar "pregunta" [-k 6] [--solo-fuentes] [--estado verificada] [--json]
    python rag.py estado                       resumen del índice

Nada sale de la PC: embeddings locales (multilingual-e5-base) y ChromaDB en
<bóveda>/.rag/ (carpeta oculta: Obsidian no la indexa y Git la ignora).
Cada fragmento = una sección bajo un encabezado Markdown, con el frontmatter
de la nota como metadatos, para que toda respuesta sea trazable a su ficha.
"""
from __future__ import annotations

import argparse, hashlib, json, os, re, sys
from pathlib import Path

BOVEDA = Path(os.getenv("TESIS_BOVEDA", Path(__file__).resolve().parents[2]))
DIR_RAG = BOVEDA / ".rag"
ESTADO = DIR_RAG / "estado.json"
COLECCION = "tesis_torvesa"
MODELO = os.getenv("EMBED_MODEL", "intfloat/multilingual-e5-base")
os.environ.setdefault("HF_HOME", os.getenv("HF_HOME", r"F:\IA\hf" if Path(r"F:\IA\hf").exists() else str(Path.home() / ".cache/huggingface")))
if (Path(os.environ["HF_HOME"]) / "hub" / f"models--{MODELO.replace('/', '--')}" / "snapshots").exists():
    os.environ.setdefault("HF_HUB_OFFLINE", "1")  # sin red si el modelo ya está en caché
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")
os.environ.setdefault("TRANSFORMERS_VERBOSITY", "error")
os.environ.setdefault("TQDM_DISABLE", "1")

# Lo que el sistema escribe sobre sí mismo no compite con las fuentes.
EXCLUIR_DIRS = {".obsidian", ".rag", ".git", ".trash", "99_Scripts", "_crudo", "node_modules"}
EXCLUIR_ARCHIVOS = {"RAG_README.md", "COLABORACION.md", "ARRANQUE.md", "README.md", "GUIA_DIEGO.md"}
MAX_CHARS, SOLAPE = 1500, 200
# Campos del frontmatter que viajan como metadatos (ver 99_Scripts/plantillas/ficha_fuente.md)
CAMPOS = ("tipo", "categoria", "objetivos", "anio", "estado", "confianza", "referencia_apa",
          "doi_url", "afirmacion", "pagina", "titulo", "fecha", "version")

for s in (sys.stdout, sys.stderr):
    try: s.reconfigure(encoding="utf-8")
    except Exception: pass


# ---------- lectura y fragmentación ----------
def notas() -> list[Path]:
    out = []
    for p in BOVEDA.rglob("*.md"):
        rel = p.relative_to(BOVEDA)
        if any(parte in EXCLUIR_DIRS for parte in rel.parts) or p.name in EXCLUIR_ARCHIVOS:
            continue
        out.append(p)
    return sorted(out)


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def leer(p: Path) -> tuple[dict, str]:
    import frontmatter
    try:
        post = frontmatter.loads(p.read_text(encoding="utf-8", errors="replace"))
        return dict(post.metadata), post.content
    except Exception:  # frontmatter roto: se indexa igual, sin metadatos
        return {}, p.read_text(encoding="utf-8", errors="replace")


def escalar(v) -> str | int | float | bool:
    if isinstance(v, (list, tuple, set)):
        return "; ".join(str(x) for x in v)
    if isinstance(v, (int, float, bool)):
        return v
    return "" if v is None else str(v)


def secciones(texto: str) -> list[tuple[str, str]]:
    """Corta por encabezados Markdown (ignora los que están dentro de bloques de código)."""
    pila: list[tuple[int, str]] = []  # (nivel, título): robusto aunque falten niveles intermedios
    actual: list[str] = []
    out: list[tuple[str, str]] = []
    en_codigo = False

    def cerrar():
        cuerpo = "\n".join(actual).strip()
        if cuerpo:
            out.append((" > ".join(t for _, t in pila), cuerpo))

    for linea in texto.splitlines():
        if linea.lstrip().startswith("```"):
            en_codigo = not en_codigo
        m = None if en_codigo else re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", linea)
        if m:
            cerrar(); actual = []
            nivel = len(m.group(1))
            while pila and pila[-1][0] >= nivel:
                pila.pop()
            pila.append((nivel, m.group(2).strip()))
        else:
            actual.append(linea)
    cerrar()
    return out


def trozos(cuerpo: str) -> list[str]:
    if len(cuerpo) <= MAX_CHARS:
        return [cuerpo]
    partes, buf = [], ""
    for parrafo in re.split(r"\n\s*\n", cuerpo):
        if buf and len(buf) + len(parrafo) > MAX_CHARS:
            partes.append(buf.strip()); buf = buf[-SOLAPE:] + "\n\n"
        while len(parrafo) > MAX_CHARS:  # párrafo gigante (tablas, texto extraído de PDF)
            partes.append((buf + parrafo[:MAX_CHARS]).strip()); buf = ""
            parrafo = parrafo[MAX_CHARS - SOLAPE:]
        buf += parrafo + "\n\n"
    if buf.strip():
        partes.append(buf.strip())
    return partes


def fragmentos(p: Path) -> list[tuple[str, str, dict]]:
    meta, cuerpo = leer(p)
    rel = p.relative_to(BOVEDA).as_posix()
    base = {"ruta": rel, "carpeta": rel.split("/")[0], "nota": p.stem}
    for c in CAMPOS:
        if c in meta:
            base[c] = escalar(meta[c])
    out = []
    for i_sec, (encab, texto) in enumerate(secciones(cuerpo) or [("", cuerpo)]):
        for i_tr, t in enumerate(trozos(texto)):
            md = {**base, "encabezado": encab}
            out.append((f"{rel}::{i_sec}.{i_tr}", f"{p.stem} | {encab}\n{t}", md))
    return out


# ---------- índice ----------
_modelo = None
def modelo():
    global _modelo
    if _modelo is None:
        from sentence_transformers import SentenceTransformer
        _modelo = SentenceTransformer(MODELO, device=os.getenv("EMBED_DEVICE", "cpu"))
    return _modelo


def coleccion():
    import chromadb
    DIR_RAG.mkdir(exist_ok=True)
    cli = chromadb.PersistentClient(path=str(DIR_RAG / "chroma"))
    return cli.get_or_create_collection(COLECCION, metadata={"hnsw:space": "cosine"})


def cargar_estado() -> dict:
    if ESTADO.exists():
        return json.loads(ESTADO.read_text(encoding="utf-8"))
    return {"modelo": MODELO, "archivos": {}}


def indexar(reconstruir: bool = False) -> int:
    est = cargar_estado()
    if reconstruir or est.get("modelo") != MODELO:
        import shutil
        shutil.rmtree(DIR_RAG / "chroma", ignore_errors=True)
        est = {"modelo": MODELO, "archivos": {}}
    col = coleccion()
    actuales = {p.relative_to(BOVEDA).as_posix(): p for p in notas()}
    borrados = [r for r in est["archivos"] if r not in actuales]
    cambiados = [r for r, p in actuales.items() if est["archivos"].get(r) != sha(p)]
    for r in borrados + cambiados:
        col.delete(where={"ruta": r})
    for r in borrados:
        est["archivos"].pop(r, None)
    n_frag = 0
    for r in cambiados:
        frs = fragmentos(actuales[r])
        if frs:
            ids, docs, metas = zip(*frs)
            emb = modelo().encode([f"passage: {d}" for d in docs], normalize_embeddings=True,
                                  batch_size=16, show_progress_bar=False)
            col.add(ids=list(ids), documents=list(docs), metadatas=list(metas), embeddings=emb.tolist())
            n_frag += len(frs)
        est["archivos"][r] = sha(actuales[r])
    ESTADO.write_text(json.dumps(est, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"RAG: {len(actuales)} notas · {len(cambiados)} reindexadas ({n_frag} fragmentos) · "
          f"{len(borrados)} eliminadas · {col.count()} fragmentos en total")
    return 0


def consultar(pregunta: str, k: int, solo_fuentes: bool, estado: str | None, como_json: bool) -> int:
    col = coleccion()
    if col.count() == 0:
        print("El índice está vacío: corre primero  python rag.py indexar"); return 1
    filtros = []
    if solo_fuentes:
        filtros.append({"carpeta": "02_Fuentes"})
    if estado:
        filtros.append({"estado": estado})
    where = None if not filtros else filtros[0] if len(filtros) == 1 else {"$and": filtros}
    emb = modelo().encode([f"query: {pregunta}"], normalize_embeddings=True)
    res = col.query(query_embeddings=emb.tolist(), n_results=k, where=where)
    hits = [{"similitud": round(1 - d, 3), "ruta": m["ruta"], "encabezado": m.get("encabezado", ""),
             "referencia_apa": m.get("referencia_apa", ""), "estado": m.get("estado", ""),
             "texto": doc.split("\n", 1)[-1]}
            for doc, m, d in zip(res["documents"][0], res["metadatas"][0], res["distances"][0])]
    if como_json:
        print(json.dumps(hits, ensure_ascii=False, indent=1)); return 0
    print(f"\nConsulta: {pregunta}\n")
    if not hits:
        print("Sin resultados con esos filtros (¿todavía no hay fichas en 02_Fuentes con ese estado?).")
    for i, h in enumerate(hits, 1):
        citable = "✅ citable" if h["estado"] == "verificada" else "⛔ NO citable (no verificada)"
        if not h["ruta"].startswith("02_Fuentes/"):
            citable = "ℹ️ nota interna (no es fuente)"
        print(f"[{i}] {h['similitud']:.3f}  {h['ruta']}  §{h['encabezado'] or '—'}")
        print(f"    APA: {h['referencia_apa'] or '—'}   {citable}")
        print("    " + h["texto"][:400].replace("\n", " ") + ("…" if len(h["texto"]) > 400 else ""))
    return 0


def resumen() -> int:
    est = cargar_estado()
    print(f"Bóveda: {BOVEDA}\nModelo: {est.get('modelo')}\nNotas indexadas: {len(est['archivos'])}")
    if (DIR_RAG / "chroma").exists():
        print(f"Fragmentos: {coleccion().count()}")
    pend = [r for r, p in ((p.relative_to(BOVEDA).as_posix(), p) for p in notas())
            if est["archivos"].get(r) != sha(p)]
    print(f"Pendientes de indexar: {len(pend)}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    i = sub.add_parser("indexar"); i.add_argument("--reconstruir", action="store_true")
    c = sub.add_parser("consultar"); c.add_argument("pregunta"); c.add_argument("-k", type=int, default=6)
    c.add_argument("--solo-fuentes", action="store_true"); c.add_argument("--estado")
    c.add_argument("--json", action="store_true")
    sub.add_parser("estado")
    a = ap.parse_args()
    if a.cmd == "indexar":
        return indexar(a.reconstruir)
    if a.cmd == "consultar":
        return consultar(a.pregunta, a.k, a.solo_fuentes, a.estado, a.json)
    return resumen()


if __name__ == "__main__":
    sys.exit(main())
