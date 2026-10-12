# 99_Scripts/busqueda — búsqueda asistida de fuentes (técnico)

Guía para personas: `Guia_Busqueda.pdf` (esta carpeta).

| Archivo | Qué hace |
|---|---|
| `consultas.json` | Las consultas (P = problema, M = metodología, N = normativa, T = tecnología, D = Diego) ligadas a afirmaciones A1–A47 y OVA |
| `apis.py` | OpenAlex, Crossref y Semantic Scholar (se prefieren al navegador). `truststore` para el certificado de la red |
| `navegador.py` | Playwright conectado por CDP a TU Chrome (puerto 9222). Redalyc, SciELO, repositorio UPS y modo asistido. Pausa si hay login o verificación; ritmo humano 8–20 s; no evade CAPTCHAs; no descarga en masa; no automatiza Google Académico |
| `iniciar_chrome.py` | Abre Chrome con perfil propio en `F:\IA\chrome_tesis` (las sesiones quedan guardadas) |
| `buscar.py` | Comando principal → `99_Scripts/datos/fuentes.sqlite` + `fuentes.csv` + fichas candidatas en `02_Fuentes/<categoría>/` (deduplica por DOI o título) |
| `procesar_descargas.py` | PDF de `00_Inbox/descargas/` → `02_Fuentes/_Textos/<citekey>.pdf` (empareja por DOI o título) y actualiza la ficha |

Requisitos: `pip install playwright truststore requests pymupdf` (no hace falta `playwright install`: usa el Chrome instalado).
