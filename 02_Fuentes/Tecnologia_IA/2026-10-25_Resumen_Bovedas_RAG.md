---
titulo: Resumen para Víctor — bóvedas de conocimiento y RAG
version: v0.1
fecha: 2026-10-25
autor: Diego Bermeo
ia: Claude (Claude Code)
tarea: S1-T14 (bloque E)
tags: [diego, resumen, boveda, rag, sprint2]
---

# Bóvedas de conocimiento y RAG en 1 página

> [!summary] En tres frases
> 1. En las pymes, y más en las constructoras, el conocimiento está en la cabeza de pocas personas y se guarda disperso. La literatura recomienda un **repositorio ordenado**, que es lo que hará la bóveda.
> 2. El **RAG** (el asistente busca en la bóveda antes de responder) **reduce** las respuestas inventadas, pero **no las elimina**. Por eso el vendedor revisa el borrador antes de enviarlo.
> 3. En América Latina ya hay casos de RAG local en español, incluido uno en Ecuador (CNEL), con buenos resultados de uso pero respuestas lentas.

## 1. Bóvedas de conocimiento (D01)

| Idea | Fuente (página) | Para qué afirmación |
|---|---|---|
| En una pyme el conocimiento clave está en pocas personas y se pierde cuando se van | Durst et al. (2023, sección 2) | A8 (por confirmar) |
| Las constructoras pequeñas descuidan guardar el conocimiento: poco personal, rotación, pocos recursos | Khoa et al. (2025, p. 295) | Problema, cap. I |
| En las constructoras, lo aprendido en cada obra queda disperso y casi no se reutiliza | Debs y Hubbard (2023, p. 74) | Problema, cap. I |
| Un repositorio guarda, ordena y clasifica lo que se sabe para que otros lo reutilicen | Dei et al. (2024, p. 10) | Marco teórico de la bóveda |
| Para una pyme constructora se propone una base de conocimientos ordenada | Zepeda Estrada et al. (2021, p. 623) | Antecedente (confianza baja: diseño preliminar) |
| Las pymes colombianas valoran el conocimiento, pero casi no usan tecnología para gestionarlo | Riascos-Erazo y Aguilera-Castro (2024, p. 1390; 2024, pp. 35–36) | Brecha que cubre la bóveda |

**Vacío:** no hay fuentes académicas serias, de 2021 en adelante, sobre bóvedas personales tipo Obsidian. La bóveda se justifica con la gestión del conocimiento en pymes (tabla de arriba) y con la documentación oficial de Obsidian que ya verificaste (A31–A34). El *local-first* (los datos viven en el equipo y funcionan sin internet) lo respalda Kleppmann et al. (2019, p. 157), que también verificaste tú.

## 2. RAG: qué tanto ayuda (D02, A37)

| Idea | Fuente (página) |
|---|---|
| Origen del término | Lewis et al. (2020, p. 9464), ficha tuya |
| Reduce las respuestas inventadas en más del 60 % en conversación | Shuster et al. (2021, p. 3785) |
| **Estudio 2023+ que pedía la matriz:** en una aplicación empresarial, los errores bajaron de hasta 21 % a menos de 7,5 % | Béchard y Marquez Ayala (2024, p. 233) |
| No los elimina: herramientas comerciales con RAG se equivocaron entre 17 % y 33 % de las veces | Magesh et al. (2025, p. 217) |
| En la industria, el RAG sigue en etapa de prototipo | Brehme et al. (2025, p. 10), ficha tuya |

**Propuesta para A37:** «RAG reduce las respuestas inventadas (Shuster et al., 2021; Béchard y Marquez Ayala, 2024), pero no las elimina (Magesh et al., 2025), por lo que el vendedor revisa cada borrador antes de enviarlo».

## 3. Casos cercanos (para el Cap. 5)

- **Ecuador, CNEL EP:** asistente RAG local sobre documentos técnicos. Puntuó 4,5/5 en funcionalidad y 4,8/5 en usabilidad, pero tardó 8,38 s por consulta y se usa como apoyo, no como reemplazo (González Ortega et al., 2026, p. 533).
- **Argentina:** en un RAG local en español, mejorar la búsqueda rindió más que usar un modelo más grande (Barsotti et al., 2026, p. 110). Eso apoya invertir en ordenar bien la bóveda antes que en el modelo más caro.
- **Empresa grande:** 82 % de recomendaciones correctas frente a 46 % con búsqueda por palabras clave (Baqar, 2026, p. 1412). **Confianza baja**: las cifras no cuadran del todo, así que solo sirve como apoyo.

## 4. Qué decides tú
1. ¿A8 con Durst et al. (2023)?
2. ¿Va la frase de A37 de arriba?
3. ¿Se renombra `ortega_2026a` a `gonzalez_2026`? El primer autor es González Ortega.
4. Las dos de Riascos usan la misma muestra: se citan juntas, no como dos evidencias.
