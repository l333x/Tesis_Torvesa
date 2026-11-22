---
titulo: "Estado de implementación del manual v1.0 (12 mejoras)"
fecha: 2026-11-22
aprobado_por: "Víctor (chat del 22-nov: 'pon en implementación todo el manual')"
manual: "11_Planificacion/2026-11-22_Manual_Implementacion_v1.1.pdf"
tags: [manual, implementacion, skills, diseno, seguridad]
---

# Estado de implementación del manual

| # | Mejora | Estado | Dónde quedó |
|---|---|---|---|
| 1 | Rasgos de IA de 2.ª generación en voz-victor | **Hecha** | `C:\Users\vasha\.claude\skills\voz-victor\SKILL.md` §2b. El revisor `revisar_voz.py` ahora avisa de: contraste y sus sustitutos (tope 2), texto que habla de sí mismo, palabras de virtud, gerundios colgados, preguntas que se responden solas y exceso de "simplemente" |
| 2 | DESIGN.md único | **Hecha** | `C:\Users\vasha\.claude\skills\diseno-paginas\DESIGN.md` (9 secciones, con la razón de cada regla) |
| 3 | Skill diseno-paginas | **Hecha** | `C:\Users\vasha\.claude\skills\diseno-paginas\`: SKILL.md + `references/senales.md`, `tokens.md` y `graficos-formularios.md`, con crédito a unslop (CC BY 4.0) |
| 4 | Reglas de gráficos en diapositivas-pdf | **Hecha** | `diapositivas-pdf/SKILL.md` §3b, que apunta al DESIGN.md |
| 5 | Lista de seguridad para Diego | **Hecha** (falta que Diego la aplique) | `IA_DIEGO.md` §8.1 |
| 6 | Formato de revisión de código en 4 partes | **Hecha** (falta que Diego la use) | `IA_DIEGO.md` §8.2 |
| 7 | Atajos marcados → limitaciones | **Hecha** (falta en el código de Diego) | `IA_DIEGO.md` §8.3 y `MANUAL_TESIS.md` §11.3 |
| 8 | Prueba con Strix | **Preparada, no ejecutada** | Plan de 8 pasos en `IA_DIEGO.md` §8.5. Requiere la aprobación de Víctor y Diego, Docker y una clave con límite de gasto, y se corre en la máquina de Diego contra una copia local |
| 9 | Lista del formulario web | **Hecha** (falta que Diego la pase) | `IA_DIEGO.md` §8.4 y `diseno-paginas/references/graficos-formularios.md` |
| 10 | Apagar conectores sin uso | **No aplica por ahora** | Los conectores de claude.ai se cargan diferidos: solo su nombre ocupa contexto. Apagarlos ahorra poco y se hace desde claude.ai > Configuración > Conectores, si Víctor quiere |
| 11 | Reglas de Excel | **Hecha** | Skill nueva `C:\Users\vasha\.claude\skills\tablero-excel\SKILL.md` (estructura, fórmulas, formato, verificación por COM) |
| 12 | Anotar por qué no se adoptan agent-reach ni los hooks | **Hecha** | `CLAUDE.md`, sección "Skills y método de trabajo" |

**Extra:**
- Los 8 repositorios útiles quedaron como referencia de solo lectura en `F:\IA\repos_referencia\`, con un `LEEME.md` que trae para qué sirve cada uno, su licencia y cómo actualizarlo.
- `MANUAL_TESIS.md` §4 suma la regla de claridad y la redacción sin rasgos de IA.

## Pendientes que no dependen de Claude
- **Diego:**
  - aplicar §8.1 y §8.4 antes de la validación;
  - empezar a marcar los `atajo:` en el código;
  - escribir sus revisiones con el formato §8.2.
- **Víctor y Diego:** decidir si se hace la prueba con Strix (§8.5).
- **Excel:** corregir en versiones nuevas (v0.3) lo que encontró la revisión del 22-nov. Lo principal:
  - alinear el estudio de costos con el modelo financiero;
  - corregir la etiqueta del "6 %";
  - quitar la firma electrónica contada dos veces;
  - sacar los supuestos escritos dentro de las fórmulas.

## 23-nov: uso y mejoras
- **Skill nueva `investigacion-web`:** búsqueda en internet con rutas por tipo de fuente, verificación con página y fecha, y cuándo parar. Toma las ideas útiles de agent-reach sin instalarlo; la ruta académica (OpenAlex) se probó y funciona.
- **El crédito de unslop** quedó en una línea discreta al final de cada archivo de `diseno-paginas`, como pide la licencia.
- **`tablero-excel` ya se usó:** modelo financiero v0.3, estudio de costos v0.4, matriz v0.3 y tablero v0.2, todos sin errores. Detalle en `06_Capitulos/Modelo_Negocio/2026-11-23_Cambios_Excel_v0.3.md`.
- **Repo de Diego:** PR en borrador https://github.com/psiceslivie/teamslash-api/pull/1 (DT-01, DT-03, atajos, `AGENTS.md`, `docs/TAREAS_DIEGO.md`). Detalle en `07_Flujos_Diseno/2026-11-23_Repo_Diego_Mejoras_v0.1.md`.
- **Strix:** se le pide a Diego que lo use, solo contra una copia local.
