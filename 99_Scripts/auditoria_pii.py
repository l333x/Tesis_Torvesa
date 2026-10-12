"""Auditoría de datos personales en lo que Git va a subir.

    python auditoria_pii.py          revisa los archivos rastreados (git ls-files)

Busca correos, teléfonos de Ecuador y números de 10 dígitos (cédula o celular),
también dentro de PDF y .docx/.xlsx. Sale con código 1 si encuentra algo que no
esté en la lista PERMITIDOS. Correr antes de cada push con datos de campo.
"""
import re, subprocess, sys, zipfile
from pathlib import Path

BOVEDA = Path(__file__).resolve().parents[1]
PATRONES = {
    "correo": re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"),
    "telefono_ec": re.compile(r"(?:\+?593[\s-]?\d[\d\s-]{7,10}|\b0[2-9]\d{7,8}\b)"),
    "10_digitos": re.compile(r"(?<![-/.\d])\b[0-2]\d{9}\b(?![-/.]?\d)"),  # no DOIs (…/MIS0742-1222240302)
}
# Coincidencias que no son datos personales (correos genéricos de ejemplo, etc.)
PERMITIDOS = {"noreply@anthropic.com", "git@github.com"}

for s in (sys.stdout,):
    try: s.reconfigure(encoding="utf-8")
    except Exception: pass


def texto(p: Path) -> str:
    suf = p.suffix.lower()
    try:
        if suf == ".pdf":
            import pypdf
            return "\n".join((pg.extract_text() or "") for pg in pypdf.PdfReader(str(p)).pages)
        if suf in (".docx", ".xlsx", ".pptx"):
            with zipfile.ZipFile(p) as z:
                xml = " ".join(z.read(n).decode("utf-8", "ignore") for n in z.namelist() if n.endswith(".xml"))
            return re.sub(r"<[^>]+>", " ", xml)
        return p.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        return f"<<no legible: {e}>>"


def main() -> int:
    archivos = subprocess.run(["git", "ls-files"], cwd=BOVEDA, capture_output=True, text=True,
                              encoding="utf-8").stdout.split("\n")
    hallazgos = 0
    for rel in filter(None, archivos):
        t = texto(BOVEDA / rel)
        for tipo, rx in PATRONES.items():
            for m in sorted(set(rx.findall(t))):
                if m in PERMITIDOS:
                    continue
                hallazgos += 1
                print(f"{tipo:<12} {rel}  ->  {m[:4]}…{m[-2:]}")  # se enmascara al imprimir
    print(f"\n{len([a for a in archivos if a])} archivos revisados · {hallazgos} hallazgos")
    return 1 if hallazgos else 0


if __name__ == "__main__":
    sys.exit(main())
