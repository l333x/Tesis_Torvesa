"""Tarea automática de los domingos 21:00: sincroniza GitHub, genera el informe y sube el PDF.

1. sincronizar_github.py  (CRONOGRAMA <-> issues)
2. generar_informe.py     (Word + PDF en F:\\Respaldos_Tesis\\Informes; copia del PDF al repo si la auditoría PII da 0)
3. git add/commit/push SOLO de CRONOGRAMA.md y del PDF del informe (nunca 'git add -A')
Todo queda en F:\\Respaldos_Tesis\\Informes\\log_tarea_domingo.md. Si algo falla, lo anota y sigue con lo que pueda.
"""
import subprocess, sys
from datetime import date, datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BOVEDA = AQUI.parents[1]
PY = sys.executable.replace("pythonw.exe", "python.exe")
LOG = Path(r"F:\Respaldos_Tesis\Informes\log_tarea_domingo.md")


def correr(cmd: list[str]) -> tuple[int, str]:
    r = subprocess.run(cmd, cwd=BOVEDA, capture_output=True, text=True, encoding="utf-8", errors="replace",
                       env={**__import__("os").environ, "PYTHONUTF8": "1"}, creationflags=0x08000000)
    lineas = (r.stdout + r.stderr).strip().splitlines()
    return r.returncode, (lineas[-1] if lineas else "")


def main() -> int:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    filas = []
    c, s = correr([PY, str(AQUI / "sincronizar_github.py")]); filas.append(("sincronizar GitHub", c, s))
    c, s = correr([PY, str(AQUI / "generar_informe.py")]); filas.append(("generar informe", c, s))
    pdf = f"11_Planificacion/Informes/{date.today().isoformat()}_Informe_Avance.pdf"
    if c == 0 and (BOVEDA / pdf).exists():
        correr(["git", "add", "11_Planificacion/CRONOGRAMA.md", pdf])
        c2, s2 = correr(["git", "commit", "-m", f"Informe de avance {date.today().isoformat()} (automático)"])
        filas.append(("commit", c2, s2))
        if c2 == 0:
            c3, s3 = correr(["git", "push", "-q"]); filas.append(("push", c3, s3 or "ok"))
    if not LOG.exists():
        LOG.write_text("# Log de la tarea del domingo\n\n| Fecha | Paso | Resultado | Detalle |\n|---|---|---|---|\n", encoding="utf-8")
    with LOG.open("a", encoding="utf-8") as f:
        for paso, cod, det in filas:
            f.write(f"| {datetime.now():%Y-%m-%d %H:%M} | {paso} | {'ok' if cod == 0 else f'⛔ código {cod}'} | {det[:120]} |\n")
    return 0 if all(c == 0 for _, c, _ in filas) else 1


if __name__ == "__main__":
    sys.exit(main())
