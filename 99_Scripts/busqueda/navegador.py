"""Búsqueda asistida con TU Chrome (perfil propio con depuración remota) para sitios sin API.

Reglas: ritmo humano (pausa aleatoria entre búsquedas), nunca evade CAPTCHAs ni verificaciones (pausa y avisa),
si una página pide iniciar sesión se pausa y espera a que tú entres, y NO descarga en masa: los PDF los bajas tú.
Google Académico NO se automatiza (sus términos lo prohíben).
"""
from __future__ import annotations

import ctypes, random, re, time
from urllib.parse import quote_plus

PUERTO = 9222
SITIOS = {
    "redalyc": {"url": "https://www.redalyc.org/busquedaArticuloFiltros.oa?q={q}", "tarjeta": "article"},
    "scielo": {"url": "https://search.scielo.org/?q={q}&lang=es&count=15&from=0&output=site&sort=&format=summary&page=1", "tarjeta": ".item"},
    "ups": {"url": "https://dspace.ups.edu.ec/discover?query={q}", "tarjeta": ".ds-artifact-item, .artifact-description"},
    # Biblioteca virtual UPS / bases suscritas: modo asistido (tú buscas; el script lee la página de resultados)
    "asistido": {"url": "", "tarjeta": ""},
}
RX_DOI = re.compile(r"10\.\d{4,9}/[^\s\"<>,;]+")


def aviso(titulo: str, msg: str) -> None:
    """Ventana de Windows que detiene el script hasta que aceptes."""
    print(f"\n>>> {titulo}: {msg}\n")
    ctypes.windll.user32.MessageBoxW(None, msg, f"Búsqueda tesis · {titulo}", 0x40 | 0x1000)


def pausa_humana(min_s: float = 8, max_s: float = 20) -> None:
    time.sleep(random.uniform(min_s, max_s))


def conectar():
    from playwright.sync_api import sync_playwright
    pw = sync_playwright().start()
    try:
        b = pw.chromium.connect_over_cdp(f"http://localhost:{PUERTO}")
    except Exception:
        pw.stop()
        raise SystemExit("No encuentro tu Chrome de búsqueda. Ábrelo primero con:  python iniciar_chrome.py")
    ctx = b.contexts[0] if b.contexts else b.new_context()
    return pw, b, ctx


def descargas_a(ctx, carpeta) -> None:
    carpeta.mkdir(parents=True, exist_ok=True)
    try:
        s = ctx.browser.new_browser_cdp_session()
        s.send("Browser.setDownloadBehavior", {"behavior": "allow", "downloadPath": str(carpeta), "eventsEnabled": True})
    except Exception:
        print("  (no pude fijar la carpeta de descargas: guarda los PDF a mano en 00_Inbox/descargas)")


def _bloqueos(pg) -> None:
    """Si hay login o verificación humana, se detiene y te deja resolverlo."""
    html = (pg.content() or "")[:200000].lower()
    url = pg.url.lower()
    if pg.query_selector("input[type=password]") or any(k in url for k in ("login", "signin", "auth", "shibboleth", "ezproxy", "sso")):
        aviso("Inicio de sesión", "La página pide iniciar sesión.\n\nInicia sesión TÚ en la ventana de Chrome y, cuando veas los resultados, presiona Aceptar.")
    if any(k in html for k in ("captcha", "verify you are human", "verifica que eres humano", "cf-challenge", "just a moment")):
        aviso("Verificación", "La página muestra una verificación (CAPTCHA).\n\nResuélvela TÚ en Chrome (el script no la evade) y presiona Aceptar.")


def _extraer(pg, sitio: str, tarjeta: str) -> list[dict]:
    if sitio == "redalyc":
        datos = pg.evaluate("""() => [...document.querySelectorAll('article')].map(a => {
            const l = [...a.querySelectorAll('a')];
            const anio = (l[2] && l[2].innerText.match(/(19|20)\\d{2}/)) ? l[2].innerText.match(/(19|20)\\d{2}/)[0] : '';
            return {titulo: l[0] ? l[0].innerText.trim() : '', url: l[0] ? l[0].href : '', revista: l[1] ? l[1].innerText.trim().replace(/,$/, '') : '',
                    anio, resumen: a.innerText.split('\\n').slice(2).join(' ').trim().slice(0, 1200),
                    pdf: (l.find(x => /\\.pdf/i.test(x.href)) || {}).href || ''};
        })""")
    else:
        sel = tarjeta or "article, .item, .result, li"
        datos = pg.evaluate("""(sel) => [...document.querySelectorAll(sel)].slice(0, 30).map(a => {
            const t = a.querySelector('h1 a, h2 a, h3 a, h4 a, .title a, a') || {};
            const txt = a.innerText || '';
            const y = txt.match(/(19|20)\\d{2}/);
            return {titulo: (t.innerText || '').trim(), url: t.href || '', revista: '', anio: y ? y[0] : '',
                    resumen: txt.slice(0, 1200), pdf: ''};
        })""", sel)
    out = []
    for d in datos:
        if len(d.get("titulo", "")) < 15:
            continue
        doi = RX_DOI.search(d.get("resumen", "") + " " + d.get("url", ""))
        out.append({"titulo": d["titulo"], "anio": int(d["anio"]) if d.get("anio") else None, "autores_lista": [],
                    "doi": doi.group(0).rstrip(".") if doi else "", "revista": d.get("revista", ""), "url": d.get("url", ""),
                    "pdf_abierto": d.get("pdf", ""), "resumen": d.get("resumen", ""), "origen": sitio.capitalize()})
    return out


def buscar(ctx, sitio: str, q: str) -> list[dict]:
    cfg = SITIOS[sitio]
    pg = ctx.new_page()
    try:
        if sitio == "asistido":
            pg.goto("about:blank")
            aviso("Modo asistido", f"Busca TÚ en la pestaña nueva de Chrome (biblioteca UPS u otra base) este tema:\n\n«{q}»\n\nCuando veas la lista de resultados, presiona Aceptar y el script la leerá.")
            pg = ctx.pages[-1]
        else:
            pg.goto(cfg["url"].format(q=quote_plus(q)), timeout=60000, wait_until="domcontentloaded")
            pg.wait_for_timeout(4000)
        _bloqueos(pg)
        return _extraer(pg, sitio, cfg["tarjeta"])
    finally:
        if sitio != "asistido":
            pg.close()
