"""Migración inicial bóveda 1 -> bóveda 2 (Tesis_Torvesa). SOLO COPIA.

Aprobada por Víctor el 2026-10-11 (Fase 0, §4). Idempotente: si el destino ya
existe con el mismo hash, no hace nada. Duplicados exactos (mismo hash) se copian
una sola vez. Deja registro en 11_Planificacion/migracion_2026-10-11.csv.
"""
import csv, hashlib, shutil, sys
from datetime import datetime
from pathlib import Path

B1 = Path(r"F:\Obsidian\Mejor elemento de compras")
B2 = Path(__file__).resolve().parents[1]
INBOX, RAW, OUT = B1 / "00_Inbox", B1 / "01_Raw/UPS/Tesis_TeamSlash", B1 / "03_Out/UPS"

CARPETAS = [
    "00_Inbox", "01_Borrador_Aprobado/cartas", "01_Borrador_Aprobado/_historico",
    *[f"02_Fuentes/{c}" for c in ("Problema", "Contexto", "Metodologia", "Evidencia_Datos",
                                  "Tecnologia_IA", "Casos_Estudio", "Normativa",
                                  "Costos_Viabilidad", "_Textos")],
    "03_Matriz_Objetivos", "04_Instrumentos", "05_Datos_Campo/Diagnostico_2026",
    "05_Datos_Campo/_crudo", "06_Capitulos", "07_Flujos_Diseno", "08_Reuniones_Tutora",
    "09_Registro_Contribuciones", "10_Antecedentes_Propios", "11_Planificacion/_historico",
    "99_Scripts/datos",
]

# (origen, carpeta destino, nombre destino o None = mismo nombre)
PLAN = [
    (INBOX / "BORRADOR DE TESIS.pdf", "01_Borrador_Aprobado", "2026-09-29_Diseno_Titulacion_APROBADO.pdf"),
    (INBOX / "Carta_Aval_Docente_Tutor_Bermeo_Segura.docx", "01_Borrador_Aprobado/cartas", None),
    (INBOX / "Carta_Autorizacion_Constructora_Torvesa.docx", "01_Borrador_Aprobado/cartas", None),
    (INBOX / "Diseno_Titulacion_TEAMSLASH_Bermeo_Segura_final.docx", "01_Borrador_Aprobado/_historico", "2026-09-28_Diseno_Titulacion_Implementacion_SUPERADO.docx"),
    (RAW / "2026-09-27_BORRADOR DE TESIS.docx", "01_Borrador_Aprobado/_historico", "2026-09-27_Borrador_IA_SUPERADO.docx"),
    (RAW / "Bermeo_Segura_TEAMSLASH_Informe_Final.docx", "10_Antecedentes_Propios", "2026-07-22_Informe_Final.docx"),
    (INBOX / "Bermeo_Segura_TEAMSLASH_Informe_Final (1).pdf", "10_Antecedentes_Propios", "2026-07-22_Informe_Final.pdf"),
    (RAW / "Bermeo_Segura_TEAMSLASH_Informe_Final_v4.docx", "10_Antecedentes_Propios", "2026-07-20_Informe_Final_v4.docx"),
    (INBOX / "Bermeo_Segura_TEAMSLASH_Informe_Final_v4.pdf", "10_Antecedentes_Propios", "2026-07-20_Informe_Final_v4.pdf"),
    (RAW / "Bermeo, Segura- PROYECTO INTEGRADOR -12-05-26.pdf", "10_Antecedentes_Propios", "2026-05-18_Proyecto_Integrador_12-05.pdf"),
    (INBOX / "Bermeo, Segura- PROYECTO INTEGRADOR -12-05-26.pdf", "10_Antecedentes_Propios", "2026-05-25_Proyecto_Integrador_12-05.pdf"),
    (RAW / "Bermeo_Segura_PROYECTO_INTEGRADOR_Sprint5.pdf", "10_Antecedentes_Propios", "2026-07-07_Proyecto_Integrador_Sprint5.pdf"),
    (INBOX / "Pitch Deck TEAMSLASH.pdf", "10_Antecedentes_Propios", "2026-07-10_Pitch_Deck.pdf"),
    (INBOX / "Pitch Deck TEAMSLASH (1).pdf", "10_Antecedentes_Propios", "2026-07-22_Pitch_Deck_a.pdf"),
    (INBOX / "Pitch Deck TEAMSLASH (2).pdf", "10_Antecedentes_Propios", "2026-07-22_Pitch_Deck_b.pdf"),
    (INBOX / "Pitch Deck TEAMSLASH (3).pdf", "10_Antecedentes_Propios", "2026-07-22_Pitch_Deck_c.pdf"),
    (RAW / "Pitch Deck TEAMSLASH.pdf", "10_Antecedentes_Propios", "2026-07-10_Pitch_Deck.pdf"),  # idéntico (hash) -> se omite
    (INBOX / "Master Brief Tesis Torvesa.pdf", "10_Antecedentes_Propios", "2026-06-26_Master_Brief.pdf"),
    (RAW / "Master Brief Tesis Torvesa.pdf", "10_Antecedentes_Propios", "2026-07-01_Master_Brief.pdf"),
    (RAW / "TEAMSLASH Propuesta Concurso.docx", "10_Antecedentes_Propios", "2026-07-10_Propuesta_Concurso.docx"),
    (INBOX / "TEAMSLASH Propuesta Concurso (1).pdf", "10_Antecedentes_Propios", "2026-07-10_Propuesta_Concurso.pdf"),
    (RAW / "TEAMSLASH_Manual_de_Usuario.docx", "10_Antecedentes_Propios", "2026-07-10_Manual_de_Usuario.docx"),
    (RAW / "teamslash.pdf", "10_Antecedentes_Propios", "2026-07-16_teamslash.pdf"),
    (RAW / "proyecto.pdf", "10_Antecedentes_Propios", "proyecto.pdf"),
    (INBOX / "TEAMSLASH_Tablas_Comparativas_Herramientas.pdf", "10_Antecedentes_Propios", "2026-07-10_Tablas_Comparativas_Herramientas.pdf"),
    (INBOX / "Capitulo_IV_Diagnostico_y_Analisis_de_Resultados.md", "10_Antecedentes_Propios", "2026-10-10_Capitulo_IV_Diagnostico.md"),
    *[(INBOX / f"ENCUESTA{n}.csv", "05_Datos_Campo/Diagnostico_2026", f"ENCUESTA{n}.csv") for n in range(1, 5)],
    (OUT / "2026-09-27_Analisis_Borrador_Tesis.md", "11_Planificacion/_historico", None),
    *[(OUT / "Tesis_Plan" / f, "11_Planificacion/_historico", f) for f in
      ("plan_soluciones.json", "busquedas.json", "busquedas_log.csv", "Plan_Soluciones_Tesis.md",
       "Plan_Soluciones_Tesis.docx", "Resumen_Tesis.docx")],
    (OUT / "2026-10-11_F0_Validacion_Tesis.md", "11_Planificacion", None),
]


def md5(p: Path) -> str:
    return hashlib.md5(p.read_bytes()).hexdigest()


def main() -> int:
    for c in CARPETAS:
        (B2 / c).mkdir(parents=True, exist_ok=True)
    vistos, filas, errores = {}, [], 0
    for origen, carpeta, nombre in PLAN:
        destino = B2 / carpeta / (nombre or origen.name)
        if not origen.exists():
            filas.append([origen, destino, "", "FALTA_ORIGEN"]); errores += 1; continue
        h = md5(origen)
        if h in vistos:
            filas.append([origen, vistos[h], h, "DUPLICADO_OMITIDO"]); continue
        if destino.exists() and md5(destino) == h:
            accion = "YA_EXISTIA"
        elif destino.exists():
            filas.append([origen, destino, h, "CONFLICTO_NO_SOBRESCRITO"]); errores += 1; continue
        else:
            shutil.copy2(origen, destino); accion = "COPIADO"
            if md5(destino) != h:
                accion = "ERROR_HASH"; errores += 1
        vistos[h] = destino
        filas.append([origen, destino, h, accion])
    log = B2 / "11_Planificacion" / "migracion_2026-10-11.csv"
    nuevo = not log.exists()
    with log.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        if nuevo:
            w.writerow(["fecha", "origen", "destino", "md5", "accion"])
        ahora = datetime.now().isoformat(timespec="seconds")
        for r in filas:
            w.writerow([ahora, *r])
    for r in filas:
        print(f"{r[3]:<26} {Path(r[1]).relative_to(B2) if str(r[1]).startswith(str(B2)) else r[1]}")
    print(f"\n{sum(r[3]=='COPIADO' for r in filas)} copiados · {errores} errores")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
