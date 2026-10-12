"""Diagramas simples (matplotlib) con la paleta de la tesis, para los documentos Word.

Cada función guarda un PNG y devuelve su ruta. Fuentes: Poppins (títulos) y Lato (texto).
"""
from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

AZUL, COBRE, CLARO, GRIS, VERDE = "#0B1F3A", "#B87333", "#EEF2F7", "#55606E", "#2E6B45"
_F = Path.home() / "AppData/Local/Microsoft/Windows/Fonts"
for f in _F.glob("*.ttf"):
    if f.stem.startswith(("Poppins", "Lato")):
        font_manager.fontManager.addfont(str(f))
plt.rcParams.update({"font.family": "Lato", "font.size": 10})


def _caja(ax, x, y, w, h, texto, fondo=AZUL, color="white", tam=9.5, negrita=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.06", fc=fondo, ec=COBRE, lw=1.4))
    ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", color=color, fontsize=tam,
            fontweight="bold" if negrita else "normal", wrap=True, family="Poppins" if negrita else "Lato")


def _flecha(ax, x1, y1, x2, y2, txt=""):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=14, color=COBRE, lw=1.6))
    if txt:
        ax.text((x1 + x2) / 2, (y1 + y2) / 2 + 0.06, txt, ha="center", fontsize=8, color=GRIS)


def _lienzo(ancho=10, alto=3.2):
    fig, ax = plt.subplots(figsize=(ancho, alto)); ax.set_xlim(0, ancho); ax.set_ylim(0, alto); ax.axis("off")
    return fig, ax


def _guardar(fig, ruta) -> Path:
    ruta = Path(ruta); ruta.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(ruta, dpi=170, bbox_inches="tight", facecolor="white"); plt.close(fig); return ruta


def flujo(pasos: list[str], ruta, titulo: str = "", alto_caja=0.95, destacar: set[int] | None = None) -> Path:
    """Cajas en fila unidas por flechas."""
    n = len(pasos); ancho = max(10, n * 2.0)
    fig, ax = _lienzo(ancho, 2.4 if not titulo else 2.9)
    w = (ancho - 0.6 * (n - 1) - 0.4) / n
    for i, p in enumerate(pasos):
        x = 0.2 + i * (w + 0.6)
        _caja(ax, x, 0.7, w, alto_caja, p, fondo=COBRE if destacar and i in destacar else AZUL, tam=9)
        if i < n - 1:
            _flecha(ax, x + w + 0.03, 0.7 + alto_caja / 2, x + w + 0.57, 0.7 + alto_caja / 2)
    if titulo:
        ax.text(0.2, 2.45, titulo, fontsize=12, fontweight="bold", color=AZUL, family="Poppins")
    return _guardar(fig, ruta)


def embudo(etapas: list[tuple[str, int]], ruta, titulo="") -> Path:
    fig, ax = plt.subplots(figsize=(8, 3.6)); ax.axis("off")
    mx = max(v for _, v in etapas)
    for i, (nombre, v) in enumerate(etapas):
        w = 0.9 * v / mx; y = len(etapas) - i
        ax.barh(y, w, left=(1 - w) / 2, height=0.75, color=AZUL if i % 2 == 0 else "#1D3A63", edgecolor=COBRE)
        ax.text(0.5, y, f"{nombre} · {v}", ha="center", va="center", color="white", fontsize=10, family="Poppins", fontweight="bold")
    if titulo:
        ax.set_title(titulo, loc="left", color=AZUL, family="Poppins", fontsize=12, fontweight="bold")
    ax.set_xlim(0, 1)
    return _guardar(fig, ruta)


def cuadrantes(cuatro: list[tuple[str, str]], ruta, titulo="") -> Path:
    fig, ax = _lienzo(8, 5)
    pos = [(0.3, 2.6), (4.1, 2.6), (4.1, 0.3), (0.3, 0.3)]
    for (t, d), (x, y) in zip(cuatro, pos):
        ax.add_patch(FancyBboxPatch((x, y), 3.6, 2.0, boxstyle="round,pad=0.02,rounding_size=0.08", fc=CLARO, ec=COBRE, lw=1.4))
        ax.text(x + 1.8, y + 1.6, t, ha="center", fontsize=11.5, fontweight="bold", color=AZUL, family="Poppins")
        ax.text(x + 1.8, y + 0.85, d, ha="center", va="center", fontsize=9, color="#222", wrap=True)
    _flecha(ax, 3.95, 3.6, 4.05, 3.6); _flecha(ax, 5.9, 2.55, 5.9, 2.35); _flecha(ax, 4.05, 1.3, 3.95, 1.3); _flecha(ax, 2.1, 2.35, 2.1, 2.55)
    if titulo:
        ax.text(0.3, 4.75, titulo, fontsize=12, fontweight="bold", color=AZUL, family="Poppins")
    return _guardar(fig, ruta)


def linea_tiempo(eventos: list[tuple[str, str]], ruta, titulo="", hoy: int | None = None) -> Path:
    """eventos = [(fecha, texto)]; hoy = índice del evento actual (se destaca)."""
    n = len(eventos); fig, ax = _lienzo(11, 2.8)
    ax.plot([0.4, 10.6], [1.3, 1.3], color=AZUL, lw=3)
    for i, (f, t) in enumerate(eventos):
        x = 0.5 + i * (10 / max(n - 1, 1))
        ax.plot(x, 1.3, "o", ms=12 if i == hoy else 9, color=COBRE if i == hoy else AZUL, mec="white", mew=1.5)
        ax.text(x, 1.75 if i % 2 == 0 else 0.55, f"{f}\n{t}", ha="center", va="center", fontsize=8,
                color=COBRE if i == hoy else "#222", fontweight="bold" if i == hoy else "normal")
    if titulo:
        ax.text(0.4, 2.55, titulo, fontsize=12, fontweight="bold", color=AZUL, family="Poppins")
    return _guardar(fig, ruta)


def arquitectura(ruta) -> Path:
    """El sistema que se diseña, en una imagen."""
    fig, ax = _lienzo(10.5, 4.6)
    ax.text(0.2, 4.3, "Lo que se diseña (sobre el CRM TEAMSLASH)", fontsize=12.5, fontweight="bold", color=AZUL, family="Poppins")
    _caja(ax, 0.2, 2.5, 2.0, 1.2, "Cliente pide\ncotización\n(web, WhatsApp)", fondo="#1D3A63")
    _caja(ax, 2.9, 2.5, 2.2, 1.2, "TEAMSLASH\nregistra y asigna\nal vendedor", fondo=AZUL)
    _caja(ax, 5.8, 2.5, 2.1, 1.2, "Bóveda de\nconocimiento\n(fichas, plantillas)", fondo=COBRE)
    _caja(ax, 8.5, 2.5, 1.9, 1.2, "Asistente IA\npropone el\nborrador", fondo=COBRE)
    _caja(ax, 2.9, 0.4, 2.2, 1.2, "Registro de\neventos que no\nse puede alterar", fondo=VERDE)
    _caja(ax, 5.8, 0.4, 4.6, 1.2, "Vendedor revisa y envía · el historial queda en la empresa", fondo="#1D3A63")
    _flecha(ax, 2.2, 3.1, 2.9, 3.1); _flecha(ax, 5.1, 3.1, 5.8, 3.1); _flecha(ax, 7.9, 3.1, 8.5, 3.1)
    _flecha(ax, 4.0, 2.5, 4.0, 1.6); _flecha(ax, 9.45, 2.5, 9.0, 1.6)
    return _guardar(fig, ruta)


def mapa_carpetas(carpetas: list[tuple[str, str, str]], ruta) -> Path:
    """carpetas = [(nombre, para qué, responsable)] en una cuadrícula."""
    n = len(carpetas); cols = 3; filas = (n + cols - 1) // cols
    fig, ax = _lienzo(11, 1.25 * filas + 0.5)
    for i, (nom, para, resp) in enumerate(carpetas):
        c, f = i % cols, i // cols
        x, y = 0.15 + c * 3.65, 1.25 * (filas - f - 1) + 0.15
        color = {"Víctor": AZUL, "Diego": COBRE, "Ambos": "#1D3A63", "Nadie": GRIS}.get(resp, AZUL)
        ax.add_patch(FancyBboxPatch((x, y), 3.45, 1.05, boxstyle="round,pad=0.02,rounding_size=0.06", fc=color, ec="white"))
        ax.text(x + 0.12, y + 0.78, nom, fontsize=9.5, color="white", fontweight="bold", family="Poppins")
        ax.text(x + 0.12, y + 0.42, para, fontsize=8, color="#F3E6D8")
        ax.text(x + 3.33, y + 0.12, resp, fontsize=7.5, color="white", ha="right", style="italic")
    return _guardar(fig, ruta)
