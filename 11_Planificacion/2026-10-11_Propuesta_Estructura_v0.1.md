---
titulo: Propuesta de ajuste de la estructura del repo
version: v0.1
fecha: 2026-10-11
estado: pendiente_aprobacion
tags: [estructura, planificacion]
---

# Propuesta de ajuste de estructura (v0.1)

> [!warning] Nada se ha movido todavía
> Todo se hace con `git mv`, que conserva el historial, en **un solo commit**, después de tu OK. Lo único que ya se creó, sin mover nada, son los README de cada carpeta, el portal, `11_Planificacion/Informes/` y `99_Scripts/gestion/`.

## Diagnóstico
La estructura aprobada funciona y **no propongo fusionar ni eliminar carpetas numeradas**. Hay cuatro problemas:
1. **Peso innecesario en el repo:** `10_Antecedentes_Propios` sube 20 archivos (~10 MB), con versiones repetidas: 4 pitch decks, 2 master briefs, 2 proyectos integradores, y cada informe en .docx **y** .pdf.
2. **Nombres que no siguen** `AAAA-MM-DD_tema_vX.Y`, sobre todo en `04_Instrumentos`.
3. **El estado de los datos simulados no se ve en el nombre de su carpeta:** `Diagnostico_2026` parece un diagnóstico válido.
4. **Scripts de un solo uso** mezclados con los vivos.

## Cambios propuestos

| # | Acción | De | A | Por qué |
|---|---|---|---|---|
| E1 | `git mv` | `05_Datos_Campo/Diagnostico_2026/` | `05_Datos_Campo/Diagnostico_2026_SIMULADO_no_usar/` | Que nadie, ni el RAG ni Diego, lo tome como dato real |
| E2 | `git mv` ×7 | `04_Instrumentos/I1_Encuesta_Colaboradores_v0.1.md`, etc. | `04_Instrumentos/2026-10-11_I1_Encuesta_Colaboradores_v0.1.md`, etc. | Convención de nombres; la v0.2 del miércoles saldrá como `2026-10-14_…_v0.2` |
| E3 | `git mv` | `11_Planificacion/F1_Plan.md` | `11_Planificacion/2026-10-11_F1_Plan_v1.0.md` | Convención |
| E4 | `git mv` | `11_Planificacion/2026-10-11_F0_Validacion_Tesis.md` | `11_Planificacion/2026-10-11_F0_Validacion_v0.1.md` | Convención (versión explícita) |
| E5 | `git mv` | `99_Scripts/migracion_inicial.py` | `99_Scripts/_historico/migracion_inicial.py` | Script de un solo uso |
| E6 | `git mv` + dejar de rastrear | 13 versiones intermedias y duplicadas de `10_Antecedentes_Propios/` | `10_Antecedentes_Propios/_versiones/` (solo en local, `.gitignore`) | El repo queda con **1 PDF por documento** (la última versión): informe final v4, Sprint 5, master brief 2026-07-01, pitch 2026-07-22 (¿cuál de las 3?), propuesta del concurso, manual, tablas de herramientas, Cap. IV. Baja ~6 MB |
| E7 | crear | — | `12_Defensa/` (en enero) | Guion, banco de preguntas y simulacros. Se crea cuando llegue S-D, no ahora |

**Excepciones a la convención de nombres** (ya documentadas en el portal): documentos vivos (`README`, `CRONOGRAMA`, `Bitacora_Semanal`, `Registro_Contribuciones`, `GUIA_DIEGO`, `COLABORACION`, `ARRANQUE`, `RAG_README`), plantillas (`_Plantilla_*`), fichas de fuentes (`citekey.md`) y el plan maestro (`Plan_Tesis_Torvesa_vX.Y`, el nombre que pediste).

## Decisiones tuyas
1. ¿Apruebas E1–E6? Puede ser todo o una lista, por ejemplo «E1, E2 y E5 sí; E6 no».
2. En E6: de las 3 versiones del pitch deck del 22-jul (a, b, c), ¿cuál es la vigente?
3. Después de mover, reviso y actualizo los enlaces internos (READMEs, GUIA_DIEGO, F0, `rag.py`, `.gitignore`) en el mismo commit.
