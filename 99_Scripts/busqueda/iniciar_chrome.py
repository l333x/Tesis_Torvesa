"""Abre TU Chrome con un perfil propio para la tesis y depuración remota (puerto 9222).

El perfil vive en F:\\IA\\chrome_tesis: ahí quedan guardados tus inicios de sesión (por ejemplo, la biblioteca
virtual de la UPS), separados de tu Chrome personal. Si ya está abierto, no abre otro.
"""
import socket, subprocess, sys
from pathlib import Path

CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
PERFIL = Path(r"F:\IA\chrome_tesis")
PUERTO = 9222


def abierto() -> bool:
    with socket.socket() as s:
        s.settimeout(1)
        return s.connect_ex(("127.0.0.1", PUERTO)) == 0


if __name__ == "__main__":
    if abierto():
        print("El Chrome de búsqueda ya está abierto (puerto 9222)."); sys.exit(0)
    if not CHROME.exists():
        sys.exit(f"No encuentro Chrome en {CHROME}")
    if not Path("F:/").exists():
        sys.exit("La unidad F: no está disponible: el perfil de búsqueda vive en F:\\IA\\chrome_tesis")
    PERFIL.mkdir(parents=True, exist_ok=True)
    subprocess.Popen([str(CHROME), f"--remote-debugging-port={PUERTO}", f"--user-data-dir={PERFIL}",
                      "--no-first-run", "--no-default-browser-check", "https://www.redalyc.org/"])
    print(f"Chrome de búsqueda abierto (perfil {PERFIL}). Inicia sesión donde lo necesites; la sesión queda guardada.")
