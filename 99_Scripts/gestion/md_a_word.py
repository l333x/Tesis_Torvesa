"""Convierte una nota Markdown de la bóveda en .docx (+ .pdf) con el estilo de la tesis.

    python md_a_word.py GUIA_DIEGO.md [--salida CARPETA] [--sin-pdf]
"""
import argparse, re, sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from estilo_docx import Doc  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("md"); ap.add_argument("--salida"); ap.add_argument("--sin-pdf", action="store_true")
    a = ap.parse_args()
    md = Path(a.md).resolve()
    texto = md.read_text(encoding="utf-8")
    fm = re.match(r"^---\n(.*?)\n---\n", texto, re.S)
    meta = dict(re.findall(r"^(\w+):\s*(.+)$", fm.group(1), re.M)) if fm else {}
    titulo = meta.get("titulo", md.stem.replace("_", " ")).strip('"')
    sub = f"Versión {meta['version']}" if "version" in meta else ""
    cuerpo = re.sub(r"^---\n.*?\n---\n", "", texto, count=1, flags=re.S)
    cuerpo = re.sub(r"^# .*\n", "", cuerpo, count=1, flags=re.M)  # el H1 ya va en la portada
    d = Doc(titulo, sub, meta.get("fecha", date.today().isoformat()))
    d.markdown(cuerpo)
    destino = Path(a.salida) if a.salida else md.parent
    for f in d.guardar(destino / f"{md.stem}.docx", pdf=not a.sin_pdf):
        print("ok", f)
    return 0


if __name__ == "__main__":
    sys.exit(main())
