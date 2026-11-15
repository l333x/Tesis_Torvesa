"""Genera las figuras de la tesis (PNG) a partir de datos_figuras.json.

Uso:
    python generar_figuras.py              -> crea solo las figuras que todavía no existen
    python generar_figuras.py --forzar     -> vuelve a crear todas (pisa los PNG)
    python generar_figuras.py --solo FODA  -> solo las figuras cuyo nombre contiene «FODA»
    python generar_figuras.py --destino C:/otra/carpeta -> deja los PNG en otra carpeta

Los textos están en datos_figuras.json; aquí solo está el dibujo.
Salida: 06_Capitulos/Figuras/. Paleta y fuentes: 99_Scripts/gestion/diagramas.py.
"""
import json
import sys
import textwrap
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
DEST = RAIZ / "06_Capitulos" / "Figuras"
sys.path.insert(0, str(AQUI.parent / "gestion"))
import diagramas as d  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle  # noqa: E402

AZUL, COBRE, CLARO, GRIS, VERDE = d.AZUL, d.COBRE, d.CLARO, d.GRIS, d.VERDE
ROJO = "#9B3B22"
ROJO_T, AMAR_T, VERDE_T, AZUL_T = "#F8E3DC", "#FFF3D6", "#E3F1E7", "#E4ECF7"
COLOR = {"azul": AZUL, "cobre": COBRE, "verde": VERDE, "gris": GRIS}
NEGRO = "#1a1a1a"

DATOS = json.loads((AQUI / "datos_figuras.json").read_text(encoding="utf-8"))
FORZAR = "--forzar" in sys.argv
if "--destino" in sys.argv:
    DEST = Path(sys.argv[sys.argv.index("--destino") + 1])
SOLO = sys.argv[sys.argv.index("--solo") + 1].lower() if "--solo" in sys.argv else ""
hechas, saltadas = [], []


def w(t, n):
    return "\n".join(textwrap.wrap(t, n))


def toca(archivo):
    """True si hay que dibujar esta figura."""
    if SOLO and SOLO not in archivo.lower():
        return False
    if (DEST / archivo).exists() and not FORZAR:
        saltadas.append(archivo)
        return False
    return True


def guardar(fig, archivo):
    d._guardar(fig, DEST / archivo)
    hechas.append(archivo)


# ------------------------------------------------------------------ flujos con carriles
ESTILO = {"inicio": (VERDE_T, VERDE), "paso": ("white", AZUL), "sistema": (AZUL_T, AZUL), "decision": (AMAR_T, COBRE),
          "alerta": (ROJO_T, ROJO), "fin": (VERDE_T, VERDE), "fin_mal": (ROJO_T, ROJO)}
BW, BH, COLW, HC = 1.95, 1.0, 2.8, 2.7     # caja, ancho de columna, alto de carril
DW, DH = 1.2, 0.88                         # medio ancho y medio alto del rombo


def ancla(p, lado):
    x, y, hw, hh = p
    return {"R": (x + hw, y), "L": (x - hw, y), "T": (x, y + hh), "B": (x, y - hh)}[lado]


def lados(p1, p2, opc):
    """Lado por el que sale y por el que entra una flecha."""
    x1, y1 = p1[0], p1[1]; x2, y2 = p2[0], p2[1]
    sal, ent = opc.get("sal"), opc.get("ent")
    if not sal:
        if abs(y1 - y2) < 0.01:
            sal, ent = ("R", "L") if x2 > x1 else ("L", "R")
        elif abs(x1 - x2) < 0.01:
            sal, ent = ("B", "T") if y2 < y1 else ("T", "B")
        else:
            sal, ent = ("R" if x2 > x1 else "L"), ("T" if y2 < y1 else "B")
    return sal, ent


def ruta(p1, p2, opc):
    """Puntos de una flecha en ángulo recto entre dos cajas."""
    sal, ent = lados(p1, p2, opc)
    a, b = ancla(p1, sal), ancla(p2, ent)
    if sal in "RL" and ent in "TB":
        return [a, (b[0], a[1]), b]
    if sal in "TB" and ent in "RL":
        return [a, (a[0], b[1]), b]
    if sal in "RL":
        return [a, b] if abs(a[1] - b[1]) < 0.01 else [a, ((a[0] + b[0]) / 2, a[1]), ((a[0] + b[0]) / 2, b[1]), b]
    return [a, b] if abs(a[0] - b[0]) < 0.01 else [a, (a[0], (a[1] + b[1]) / 2), (b[0], (a[1] + b[1]) / 2), b]


def flujo_carriles(f):
    carr = f["carriles"]
    ncol = max(n[1] for n in f["nodos"].values()) + 1
    ancho = 1.55 + ncol * COLW + 0.25
    pie = 1.75
    alto = HC * len(carr) + 0.9 + pie
    fig, ax = plt.subplots(figsize=(ancho, alto)); ax.set_xlim(0, ancho); ax.set_ylim(0, alto); ax.axis("off")
    ax.text(0.2, alto - 0.5, f["titulo"], fontsize=15, fontweight="bold", color=AZUL, family="Poppins")
    for i, c in enumerate(carr):
        y = alto - 0.9 - (i + 1) * HC
        ax.add_patch(Rectangle((0.2, y), ancho - 0.4, HC, fc=CLARO if i % 2 == 0 else "white", ec="#C9D1DC", lw=1))
        ax.add_patch(Rectangle((0.2, y), 1.05, HC, fc=AZUL, ec=AZUL))
        ax.text(0.72, y + HC / 2, w(c, 18), rotation=90, ha="center", va="center", color="white", fontsize=10, fontweight="bold")
    pos = {}
    for k, (carril, col, texto, tipo, extra) in f["nodos"].items():
        cy = alto - 0.9 - (carr.index(carril) + 1) * HC + HC / 2 + 0.12
        cx = 1.55 + col * COLW + COLW / 2
        pos[k] = (cx, cy, DW, DH) if tipo == "decision" else (cx, cy, BW / 2 + 0.02, BH / 2 + 0.02)
    abajo = set()   # cajas con una flecha por debajo: su tiempo se escribe a un lado
    for a, b, _, opc in f["flechas"]:
        sal, ent = lados(pos[a], pos[b], opc)
        if sal == "B": abajo.add(a)
        if ent == "B": abajo.add(b)
    for k, (carril, col, texto, tipo, extra) in f["nodos"].items():
        cx, cy = pos[k][0], pos[k][1]
        fc, ec = ESTILO[tipo]
        if tipo == "decision":
            ax.add_patch(Polygon([(cx, cy + DH), (cx + DW, cy), (cx, cy - DH), (cx - DW, cy)], fc=fc, ec=ec, lw=1.5, zorder=3))
            ax.text(cx, cy, w(texto, 15), ha="center", va="center", fontsize=8.6, color=NEGRO, zorder=4)
            pos[k] = (cx, cy, DW, DH)
        else:
            r = 0.42 if tipo in ("inicio", "fin", "fin_mal") else 0.08
            ax.add_patch(FancyBboxPatch((cx - BW / 2, cy - BH / 2), BW, BH, boxstyle=f"round,pad=0.02,rounding_size={r}",
                                        fc=fc, ec=ec, lw=1.5, zorder=3))
            ax.text(cx, cy, w(texto, 20), ha="center", va="center", fontsize=9, color=NEGRO, zorder=4)
            pos[k] = (cx, cy, BW / 2 + 0.02, BH / 2 + 0.02)
        hh = pos[k][3]
        if extra.get("tiempo"):
            lado = k in abajo
            ax.text(cx + (0.12 if lado else 0), cy - hh - 0.1, w(extra["tiempo"], 20 if lado else 27),
                    ha="left" if lado else "center", va="top", fontsize=8, color=COBRE,
                    fontweight="bold", zorder=4, bbox=dict(fc="white", ec="none", pad=1.2, alpha=0.9))
        if extra.get("opt"):
            ax.plot(cx + pos[k][2] - (0.55 if tipo == "decision" else 0.05), cy + hh - (0.4 if tipo == "decision" else 0.02),
                    marker="*", ms=17, color=COBRE, mec="white", mew=0.8, zorder=6)
        if extra.get("critico"):
            ax.add_patch(plt.Circle((cx + BW / 2 - 0.02, cy + BH / 2), 0.17, color=ROJO, zorder=6))
            ax.text(cx + BW / 2 - 0.02, cy + BH / 2, str(extra["critico"]), ha="center", va="center", color="white",
                    fontsize=8.5, fontweight="bold", zorder=7)
    for a, b, etq, opc in f["flechas"]:
        pts = ruta(pos[a], pos[b], opc)
        ls = "--" if opc.get("punteada") else "-"
        if len(pts) > 2:
            ax.plot([p[0] for p in pts[:-1]], [p[1] for p in pts[:-1]], color=COBRE, lw=1.5, ls=ls, zorder=2,
                    solid_capstyle="round", solid_joinstyle="round")
        ax.add_patch(FancyArrowPatch(pts[-2], pts[-1], arrowstyle="-|>", mutation_scale=14, color=COBRE, lw=1.5,
                                     linestyle=ls, shrinkA=0, shrinkB=0, zorder=2))
        if etq:
            (x0, y0), (x1, y1) = pts[0], pts[1]
            if abs(y0 - y1) < 0.01:      # sale en horizontal
                ax.text(x0 + (0.1 if x1 > x0 else -0.1), y0 + 0.1, etq, ha="left" if x1 > x0 else "right", fontsize=8.4,
                        color=GRIS, fontweight="bold", zorder=5)
            else:                        # sale en vertical
                ax.text(x0 + 0.1, y0 + (0.22 if y1 > y0 else -0.22), etq, ha="left", va="center", fontsize=8.4,
                        color=GRIS, fontweight="bold", zorder=5, bbox=dict(fc="white", ec="none", pad=0.8, alpha=0.85))
    # leyenda
    yl = pie - 0.45; x = 0.3
    for txt, (fc, ec) in [("Persona", ESTILO["paso"]), ("Sistema", ESTILO["sistema"]), ("Decisión", ESTILO["decision"]),
                          ("Aviso o pérdida", ESTILO["alerta"]), ("Inicio o fin", ESTILO["inicio"])]:
        ax.add_patch(FancyBboxPatch((x, yl - 0.11), 0.36, 0.22, boxstyle="round,pad=0.01,rounding_size=0.04", fc=fc, ec=ec, lw=1.2))
        ax.text(x + 0.46, yl, txt, va="center", fontsize=8.8, color=NEGRO); x += 0.62 + 0.105 * len(txt)
    ax.text(x + 0.1, yl, "Texto en cobre: tiempo de cada paso", va="center", fontsize=8.8, color=COBRE, fontweight="bold")
    x += 3.35
    if any(n[4].get("opt") for n in f["nodos"].values()):
        ax.plot(x, yl, marker="*", ms=14, color=COBRE); ax.text(x + 0.18, yl, "Se puede optimizar", va="center", fontsize=8.8, color=NEGRO)
    ax.text(0.2, yl - 0.32, w(f["nota"], int(ancho * 9.6)), fontsize=8.6, color=GRIS, style="italic", va="top", linespacing=1.3)
    guardar(fig, f["archivo"])


# ------------------------------------------------------------------ filas de pasos con tiempos
def filas_pasos(f):
    bw, gap, hf = 2.25, 0.5, 2.25
    nmax = max(len(r["pasos"]) for r in f["filas"])
    etiqueta = any(r["nombre"] for r in f["filas"])
    x0 = 2.0 if etiqueta else 0.3
    ancho = x0 + nmax * bw + (nmax - 1) * gap + 0.3
    pie = 1.05
    alto = hf * len(f["filas"]) + 0.9 + pie
    fig, ax = plt.subplots(figsize=(ancho, alto)); ax.set_xlim(0, ancho); ax.set_ylim(0, alto); ax.axis("off")
    ax.text(0.3, alto - 0.5, f["titulo"], fontsize=15, fontweight="bold", color=AZUL, family="Poppins")
    for i, r in enumerate(f["filas"]):
        gris = r["color"] == "gris"
        yb = alto - 0.9 - (i + 1) * hf + 0.35
        if etiqueta:
            ax.text(0.3, yb + 0.55, w(r["nombre"], 9), fontsize=12, fontweight="bold", va="center", family="Poppins",
                    color=ROJO if gris else AZUL)
        for j, (texto, tiempo) in enumerate(r["pasos"]):
            x = x0 + j * (bw + gap)
            dest = j in r.get("destacar", [])
            fc = "#E9ECEF" if gris else (COBRE if dest else AZUL)
            ax.add_patch(FancyBboxPatch((x, yb), bw, 1.1, boxstyle="round,pad=0.02,rounding_size=0.07", fc=fc,
                                        ec=GRIS if gris else COBRE, lw=1.4))
            ax.text(x + bw / 2, yb + 0.55, w(texto, 23), ha="center", va="center", fontsize=9.2, color=NEGRO if gris else "white")
            if tiempo:
                ax.text(x + bw / 2, yb + 1.26, w(tiempo, 26), ha="center", va="bottom", fontsize=9, fontweight="bold",
                        color=ROJO if gris else COBRE)
            if j < len(r["pasos"]) - 1:
                ax.add_patch(FancyArrowPatch((x + bw + 0.05, yb + 0.55), (x + bw + gap - 0.05, yb + 0.55), arrowstyle="-|>",
                                             mutation_scale=14, color=GRIS if gris else COBRE, lw=1.6))
    ax.text(0.3, pie - 0.2, w(f["nota"], int(ancho * 9.4)), fontsize=8.8, color=GRIS, style="italic", va="top", linespacing=1.3)
    guardar(fig, f["archivo"])


# ------------------------------------------------------------------ FODA
def foda(f):
    fig = plt.figure(figsize=(16, 21))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 16); ax.set_ylim(0, 21); ax.axis("off")
    ax.text(0.4, 20.45, "Análisis FODA de la propuesta", fontsize=20, fontweight="bold", color=AZUL, family="Poppins")
    ax.text(0.4, 20.05, "El FODA analiza la propuesta (el sistema para la gestión comercial de Torvesa), no a la empresa entera.",
            fontsize=11, color=GRIS)
    ax.text(5.05, 19.55, "Positivo", ha="center", fontsize=12, fontweight="bold", color=GRIS)
    ax.text(12.15, 19.55, "Negativo", ha="center", fontsize=12, fontweight="bold", color=GRIS)
    ax.text(0.55, 16.5, "Interno", rotation=90, va="center", fontsize=12, fontweight="bold", color=GRIS)
    ax.text(0.55, 11.6, "Externo", rotation=90, va="center", fontsize=12, fontweight="bold", color=GRIS)
    cuad = [(1.0, 14.15, "Fortalezas", f["F"], VERDE_T, VERDE), (8.6, 14.15, "Debilidades", f["D"], AMAR_T, COBRE),
            (1.0, 9.25, "Oportunidades", f["O"], AZUL_T, AZUL), (8.6, 9.25, "Amenazas", f["A"], ROJO_T, ROJO)]
    for x, y, tit, items, fondo, borde in cuad:
        ax.add_patch(FancyBboxPatch((x, y), 7.3, 4.75, boxstyle="round,pad=0.02,rounding_size=0.12", fc=fondo, ec=borde, lw=1.6))
        ax.text(x + 0.25, y + 4.35, tit, fontsize=15, fontweight="bold", color=borde, family="Poppins")
        yy = y + 3.95
        for it in items:
            t = w(it, 92)
            ax.text(x + 0.25, yy, t, fontsize=9.6, color=NEGRO, va="top", linespacing=1.25)
            yy -= 0.24 * (t.count("\n") + 1) + 0.2
    ax.text(0.4, 8.7, "Matriz cruzada (estrategias)", fontsize=15, fontweight="bold", color=AZUL, family="Poppins")
    col = {"FO": VERDE, "DO": COBRE, "FA": AZUL, "DA": ROJO}
    nombre = {"FO": "FO · fortalezas para aprovechar oportunidades", "DO": "DO · corregir debilidades con las oportunidades",
              "FA": "FA · fortalezas para frenar amenazas", "DA": "DA · reducir debilidades y amenazas a la vez"}
    for k, tipo in enumerate(["FO", "DO", "FA", "DA"]):
        x = 0.4 + (k % 2) * 7.7; y0 = 8.2 - (k // 2) * 3.35
        ax.text(x, y0, nombre[tipo], fontsize=11, fontweight="bold", color=col[tipo])
        yy = y0 - 0.38
        for _, cod, est, comb in [e for e in f["estrategias"] if e[0] == tipo]:
            txt = w(f"{cod}. {est} ({comb})", 88)
            ax.text(x, yy, txt, fontsize=9.6, color=NEGRO, va="top", linespacing=1.25)
            yy -= 0.24 * (txt.count("\n") + 1) + 0.22
    ax.add_patch(FancyBboxPatch((0.4, 0.95), 15.2, 0.85, boxstyle="round,pad=0.02,rounding_size=0.1", fc=AZUL, ec=AZUL))
    ax.text(8.0, 1.375, w(f["central"], 135), ha="center", va="center", fontsize=11.5, color="white", fontweight="bold")
    ax.text(0.4, 0.55, w(f["nota"], 180), fontsize=8.8, color=GRIS, style="italic", va="top")
    guardar(fig, f["archivo"])


# ------------------------------------------------------------------ tablas
def tabla(t):
    env, anchos = t["envolver"], t["anchos"]
    celdas = [[w(str(v), env[j]) for j, v in enumerate(fila)] for fila in t["filas"]]
    lineas = [max(c.count("\n") + 1 for c in fila) for fila in celdas]
    total = 1.6 + sum(lineas) + 0.9 * len(celdas)
    fig, ax = plt.subplots(figsize=(sum(anchos), 0.22 * total)); ax.axis("off")
    fig.subplots_adjust(left=0.01, right=0.99, top=0.97, bottom=0.03)
    tb = ax.table(cellText=celdas, colLabels=t["columnas"], colWidths=[a / sum(anchos) for a in anchos],
                  bbox=[0, 0, 1, 1], cellLoc="left", colLoc="left")
    tb.auto_set_font_size(False); tb.set_fontsize(9.5)
    for (r, c), cel in tb.get_celld().items():
        cel.set_edgecolor("#C9D1DC"); cel.set_linewidth(0.6); cel.PAD = 0.03
        if r == 0:
            cel.set_facecolor(AZUL); cel.get_text().set_color("white"); cel.get_text().set_fontweight("bold")
            cel.set_height(1.6 / total)
        else:
            cel.set_facecolor(CLARO if r % 2 == 0 else "white"); cel.set_height((lineas[r - 1] + 0.9) / total)
    fig.text(0.01, 0.985, t["titulo"], fontsize=12, fontweight="bold", color=AZUL, family="Poppins", va="bottom")
    fig.text(0.01, 0.015, w(t["nota"], 150), fontsize=8.5, color=GRIS, va="top", style="italic")
    guardar(fig, t["archivo"])


# ------------------------------------------------------------------ pirámide, núcleo, línea de tiempo y ciclo
def piramide(p):
    fig, ax = d._lienzo(11, 6.4)
    ax.text(0.2, 6.0, p["titulo"], fontsize=14, fontweight="bold", color=AZUL, family="Poppins")
    for k, ((t, s), fc, x0, wid) in enumerate(zip(p["niveles"], [COBRE, AZUL, VERDE], [0.8, 1.6, 2.4], [8.4, 6.8, 5.2])):
        y = 0.6 + k * 1.6
        ax.add_patch(Polygon([(x0, y), (x0 + wid, y), (x0 + wid - 0.8, y + 1.4), (x0 + 0.8, y + 1.4)], fc=fc, ec="white", lw=2))
        ax.text(x0 + wid / 2, y + 0.85, t, ha="center", fontsize=11.5, color="white", fontweight="bold", family="Poppins")
        ax.text(x0 + wid / 2, y + 0.42, s, ha="center", fontsize=10, color="white")
    ax.add_patch(FancyArrowPatch((9.9, 0.7), (9.9, 5.2), arrowstyle="-|>", mutation_scale=18, color=GRIS, lw=2))
    ax.text(10.15, 2.95, p["lateral"], rotation=90, va="center", fontsize=10.5, color=GRIS)
    ax.text(0.2, 0.15, p["nota"], fontsize=8.5, color=GRIS, style="italic")
    guardar(fig, p["archivo"])


def nucleo(n):
    fig, ax = d._lienzo(14, 7.6)
    ax.text(0.2, 7.2, n["titulo"], fontsize=14, fontweight="bold", color=AZUL, family="Poppins")
    cx, cy = 7.0, 4.1
    d._caja(ax, cx - 2.2, cy - 0.85, 4.4, 1.7, n["centro"], fondo=COBRE, tam=10)
    for (t, s), (x, y) in zip(n["tarjetas"], [(0.3, 5.3), (9.8, 5.3), (0.3, 2.2), (9.8, 2.2), (5.05, 0.95)]):
        d._caja(ax, x, y, 3.9, 1.35, f"{t}\n\n{s}", fondo=AZUL, tam=9)
        tx, ty = x + 1.95, y + 0.675
        ax.add_patch(FancyArrowPatch((cx + (tx - cx) * 0.38, cy + (ty - cy) * 0.45), (tx - (tx - cx) * 0.33, ty - (ty - cy) * 0.3),
                                     arrowstyle="-|>", mutation_scale=13, color=GRIS, lw=1.3))
    ax.add_patch(FancyBboxPatch((0.3, 0.1), 13.4, 0.6, boxstyle="round,pad=0.02,rounding_size=0.08", fc=CLARO, ec=GRIS))
    ax.text(7.0, 0.4, n["banda"], ha="center", va="center", fontsize=10, color=AZUL, fontweight="bold")
    guardar(fig, n["archivo"])


def linea(l):
    fig, ax = d._lienzo(14, 4.6)
    ax.text(0.2, 4.25, l["titulo"], fontsize=14, fontweight="bold", color=AZUL, family="Poppins")
    ax.add_patch(FancyBboxPatch((0.3, 3.1), 13.4, 0.65, boxstyle="round,pad=0.02,rounding_size=0.08", fc=ROJO_T, ec=ROJO))
    ax.text(7.0, 3.42, l["hoy"], ha="center", va="center", fontsize=10.5, color=ROJO, fontweight="bold")
    ax.plot([0.6, 13.4], [2.2, 2.2], color=AZUL, lw=3)
    for k, (t, s, c) in enumerate(l["hitos"]):
        x = 0.9 + k * 2.45
        ax.add_patch(plt.Circle((x, 2.2), 0.16, color=COLOR[c]))
        ax.text(x, 1.7, t, ha="center", fontsize=11, fontweight="bold", color=COLOR[c], family="Poppins")
        ax.text(x, 1.35, s, ha="center", va="top", fontsize=9.5, color=NEGRO)
    ax.text(0.2, 0.15, l["nota"], fontsize=8.5, color=GRIS, style="italic")
    guardar(fig, l["archivo"])


def ciclo(c):
    fig, ax = d._lienzo(10, 7.4)
    ax.text(0.2, 7.0, c["titulo"], fontsize=14, fontweight="bold", color=AZUL, family="Poppins")
    for (t, s), (x, y), col in zip(c["cajas"], [(0.6, 4.0), (5.4, 4.0), (5.4, 0.8), (0.6, 0.8)], [AZUL, COBRE, VERDE, GRIS]):
        d._caja(ax, x, y, 4.0, 2.2, f"{t}\n\n{s}", fondo=col, tam=10)
    for p1, p2 in [((4.65, 5.1), (5.35, 5.1)), ((7.4, 3.95), (7.4, 3.05)), ((5.35, 1.9), (4.65, 1.9)), ((2.6, 3.05), (2.6, 3.95))]:
        ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=18, color=COBRE, lw=2))
    ax.text(0.2, 0.2, c["nota"], fontsize=8.5, color=GRIS, style="italic")
    guardar(fig, c["archivo"])


if __name__ == "__main__":
    for f in DATOS["flujos"]:
        toca(f["archivo"]) and flujo_carriles(f)
    for f in DATOS["filas"]:
        toca(f["archivo"]) and filas_pasos(f)
    for clave, fn in (("foda", foda), ("piramide", piramide), ("nucleo", nucleo), ("linea", linea), ("ciclo", ciclo)):
        toca(DATOS[clave]["archivo"]) and fn(DATOS[clave])
    for t in DATOS["tablas"]:
        toca(t["archivo"]) and tabla(t)
    print(f"Figuras creadas: {len(hechas)}")
    for a in hechas:
        print("  +", a)
    if saltadas:
        print(f"Ya existían y no se tocaron: {len(saltadas)} (usa --forzar para rehacerlas)")
    print("Carpeta:", DEST)
