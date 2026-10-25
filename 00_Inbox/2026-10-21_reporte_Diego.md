---
titulo: Reporte de Diego — miércoles 21-oct
fecha: 2026-10-21
autor: Diego Bermeo
ia: Claude (Claude Code)
tags: [diego, reporte, sprint2]
---

# Reporte de Diego · mié 21-oct (bloque C, con un día de retraso)

## Qué se hizo
- **C · Bóvedas de conocimiento (S1-T08, D01):** 7 fichas verificadas, todas sobre gestión del conocimiento en pymes y en constructoras: `durst_2023`, `khoa_2025`, `debs_2023`, `dei_2024`, `zepeda_2021`, `riascos_2024` y `riascos_2024a`.
- **C · Arquitecturas RAG (S1-T13, D02):** 6 fichas verificadas (también se verificó `lewis_2020`, pero Víctor la subió ese mismo día y quedó la suya; ver el reporte del 25-oct): `shuster_2021`, `bechard_2024`, `magesh_2025`, `baqar_2026`, `ortega_2026a` (caso CNEL, Ecuador) y `barsotti_2026` (caso Argentina, RAG local en español).
- **Búsqueda:** `buscar.py --consulta D01 D02 --solo-api --desde 2021` dio 62 candidatas. Quedaron así:
  - 3 verificadas;
  - 4 candidatas;
  - 55 descartadas, con el motivo en `## Descarte (21-oct)` de cada ficha: fuera de tema, preprints de Zenodo o SSRN, revistas sin revisión confiable, tesis de grado o capítulos de pago.

  Las otras 10 verificadas salieron de búsqueda manual (OpenAlex, ACL Anthology, arXiv) y se marcan con `origen_busqueda: ... (búsqueda manual)`.
- En cada ficha verificada se abrió el texto completo y la cita textual se comparó automáticamente contra el PDF.

## Afirmaciones con fuente
- **A37 (RAG ancla las respuestas y reduce errores): cubierta.** Propuesta para el `[FALTA-FUENTE: A37]` del Cap. 2:
  - **Origen del término:** Lewis et al. (2020, p. 9464), según la ficha de Víctor.
  - **Reduce errores:** Béchard y Marquez Ayala (2024, p. 233). Sin recuperación, los elementos inventados llegan hasta el 21 %; con recuperación bajan a menos del 7,5 %. Como apoyo, Shuster et al. (2021, p. 3785): «reducing hallucinated responses by over 60%».
  - **No los elimina:** Magesh et al. (2025, p. 217), «the hallucination problem persists at significant levels». En la p. 233 dice que el usuario debe verificar, lo que respalda que el vendedor revise el borrador antes de enviarlo.
- **A8 (amnesia institucional):** `durst_2023` (sección 2) respalda que en una pyme el conocimiento está en pocas personas y se pierde cuando se van. Le puse `[A8]`; **confírmalo tú**. El término sigue anclado a Pollitt (2000).

## PDF para bajar a mano
Todos son de acceso abierto, pero bloquean la descarga automática:
- Aviv, Hadar y Levy (2021), *Knowledge Management Infrastructure Framework for Enhancing Knowledge-Intensive Business Processes*, Sustainability. https://www.mdpi.com/2071-1050/13/20/11387/pdf. Es la más útil de las pendientes de D01.
- López y Yepes (2024), *Visualizing the Future of Knowledge Sharing in SMEs in the Construction Industry*, Advances in Civil Engineering. https://doi.org/10.1155/2024/6657677. Todavía no tiene ficha.
- Altinok et al. (2026), comparación de arquitecturas RAG para la base de conocimiento de una empresa, IEEE IISEC. https://doi.org/10.1109/iisec69317.2026.11418525. Es de pago: probar con el acceso UPS a IEEE Xplore.
- Durst (2026), *Knowledge at Risk* (editorial, baja prioridad). https://doi.org/10.1080/14778238.2026.2719483

## Dudas para Víctor
1. **Error en `buscar.py`:** `comun.citekey()` se cae con `IndexError` cuando ya existen 26 citekeys `anonimo_<año>` del mismo año, porque se acaban las letras a–z. Por eso la búsqueda de D01 quedó incompleta en OpenAlex y Crossref. No lo toqué porque el script es tuyo.
2. ~~**La base `fuentes.sqlite` no está sincronizada.**~~ Resuelto el 25-oct: se unió con la tuya y quedó al día (ver el reporte del 25-oct).
3. **Citekey `ortega_2026a`:** el primer autor es González Ortega, así que por la regla correspondería `gonzalez_2026`. ¿Lo renombro con `git mv`?
4. **`riascos_2024` y `riascos_2024a`:**
   - Usan la misma muestra de 256 pymes colombianas, así que no son dos evidencias independientes.
   - En APA 7, las letras van al revés que los citekeys: la de RVG sería 2024a y la de JOTMI 2024b.
5. **`khoa_2025`:** Crossref pone «Khoa» como apellido, pero en vietnamita el apellido sería «Vo». Hay que confirmarlo antes de citar.
6. **Gestión del conocimiento personal o tipo Obsidian:** no apareció ninguna fuente académica seria de 2021 en adelante. Para la bóveda conviene apoyarse en la gestión del conocimiento en pymes (las 7 fichas de D01) y en la documentación oficial de Obsidian (bloque D).
7. **`baqar_2026`** quedó con confianza baja: las cifras del resumen y del texto no cuadran del todo. Solo la propongo para el Cap. 5.
