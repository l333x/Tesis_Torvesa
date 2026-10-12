---
titulo: Fase 1 — Recopilación bibliográfica (plan y reglas)
fecha: 2026-10-11
periodo: 2026-10-12 → 2026-10-14 (corte el miércoles en la noche)
estado: aprobado
tags: [fase1, bibliografia, planificacion]
---

# Fase 1 — Plan aprobado por Víctor (2026-10-11)

## Prioridades (en este orden)
1. **Planteamiento del problema + meta M2.** Incluye corregir la cita de Oldroyd («primera hora») y buscar evidencia de 2023+ sobre el tiempo de respuesta a leads (la ventana de 5–15 min). Afirmaciones A1–A10, A4 y M2.
2. **Metodología:** DSR (Hevner, Peffers); Design Thinking y Scrum dentro de DSR; censo con poblaciones pequeñas; enfoque mixto con predominio cuantitativo. A39, A40, A47 y D2.
3. **Normativa:** LOPDP desde el texto oficial (Registro Oficial) y su Reglamento. Después, **agregar los artículos a C1** (en una versión nueva, C1 v0.2). A42–A45.
4. **SUS validada en español** para reemplazar el bloque D de I1 (en una versión nueva de I1).
5. **Adopción empresarial de IA y automatización comercial 2023–2026.**
6. El resto de las 47 afirmaciones.
- **D6 (OpenTimestamps → SHA-256 + log de solo-anexión):** 1 página, **solo cuando haya 3 o más fuentes verificadas**, en un bloque corto.

## Reglas
- **Verificada** = abrí la fuente y el dato está ahí, **con página**. Si solo tengo acceso al resumen → `acceso: solo_resumen`, y la fuente **no cuenta como verificada**.
- Solo APIs y fuentes permitidas (OpenAlex, Crossref, Semantic Scholar, CORE, arXiv, SciELO, Redalyc, DSpace, informes oficiales, normativa oficial). Nada de scraping de Google Scholar ni de Sci-Hub. Respetar los límites de tasa.
- Prioridad para 2023–2026. Lo seminal se acepta si es el origen del concepto o del dato, **y se acompaña de evidencia reciente que lo confirme**.
- Si una afirmación no tiene respaldo después de una búsqueda razonable → **propuesta de reformularla o eliminarla**. No se maquilla.
- **Lo más importante del reporte:** las afirmaciones del borrador que la evidencia **contradice**.

## Ritmo
- Al final de cada día: `11_Planificacion/F1_reporte_AAAA-MM-DD.md` con:
  - candidatas / verificadas / descartadas;
  - afirmaciones cubiertas sobre 47;
  - huecos;
  - contradicciones.
- Después: `auditoria_pii.py` → commit → push.
- **Miércoles 14, en la noche:** corte + **matriz afirmación → fuentes → estado** (`03_Matriz_Objetivos/`), para decidir qué entra al capítulo 1.

## Metas de la fase
150–300 candidatas · 60–100 verificadas · 25–40 citadas. Cada OVA con 3 o más verificadas. Cada metodología con 2–3 fuentes frente a sus alternativas. Cada cifra del borrador con su fuente original.
