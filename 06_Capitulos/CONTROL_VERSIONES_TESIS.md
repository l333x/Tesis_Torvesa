---
titulo: "Control de versiones de la tesis (borradores completos)"
actualizado: 2026-11-22
tipo: referencia
tags: [tesis, versiones, control]
---

# Control de versiones de la tesis

**Regla:**
- Cada borrador completo se guarda con fecha y versión y nunca se sobrescribe.
- Los capítulos fuente son `.md` en `06_Capitulos/` (`AAAA-MM-DD_CapN_..._vX.Y.md`). Cada versión nueva es una copia; lo nuevo va entre `{+ +}` y lo quitado entre `{- -}`.
- El armador acepta esos cambios al generar el Word.
- Ninguna versión que Víctor haya editado se toca.

| Borrador | Fecha | Págs. | Capítulos fuente | Qué cambió | Detalle |
|---|---|---|---|---|---|
| 1 (v0.1) | 2026-11-07 | 55 | I–III v0.3, IV v0.1, V–VI esquema v0.1 | Primer documento completo | Registro de contribuciones, 07-nov |
| 2 (v0.2 / v0.3) | 2026-11-10 | 65 / 66 | IV v0.2 / v0.3, V–VI esquema v0.2 | Finanzas v0.1, FODA, prototipo revisado | Bitácora, 10-nov |
| 3 (v0.1) | 2026-11-16 | 76 | I v0.4, II v0.3, III v0.4, IV v0.4, V–VI v0.3 | Seis capítulos completos, LOPDP, trazabilidad, viabilidad con un cliente, riesgos | `2026-11-16_Cambios_Borrador3.md` |
| 4 (v0.1) | 2026-11-22 | 77 | I v0.5, II v0.4, III v0.5, IV v0.5, V–VI v0.4 | Priorización y backlog (Deberes de IR), DEC-24, validación desde el 30-nov, redacción sin rasgos de IA | `2026-11-22_Cambios_Borrador4.md` |
| 4 (v0.2) | 2026-11-22 | 83 | I v0.6, II v0.5, III v0.6, IV v0.6, V–VI v0.5 | Cada sigla, código y término se explica en su primer uso; al inicio van el control de versiones, la lista de 37 siglas y códigos y el glosario de 17 términos | `2026-11-22_Cambios_Borrador4.md` |

## Regla de claridad (desde la v0.2 del borrador 4)
La tesis tiene que entenderse sin conocer el proyecto. Por eso:
- **Siglas y códigos:** cada sigla o código (M1–M6, RQ, CP, CU, OE, TEAMSLASH, AS-IS/TO-BE, SHA-256, VAN/TIR…) se explica entre paréntesis la primera vez que aparece en el cuerpo, y además va en la "Lista de siglas, abreviaturas y códigos".
- **Términos técnicos:** cada término (backlog, sprint, bóveda, línea base, fuga, prueba de concepto, validación…) va en el "Glosario de términos".
- **Códigos internos:** DEC-xx, A1–A47 y los nombres de archivos no van en el cuerpo del texto. Solo aparecen dentro de las marcas amarillas, que desaparecen en la versión final.
- **Armado:** se hace con `armar_borrador4b.py` (scratchpad del 22-nov). Para un borrador nuevo: copiarlo, cambiar FUENTES y FECHA, y sumar una fila al control de versiones dentro del armador y en esta tabla.
