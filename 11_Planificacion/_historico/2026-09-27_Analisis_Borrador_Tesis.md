---
titulo: Análisis del borrador de tesis (Diseño de Titulación Torvesa)
tipo: out
area: UPS
subtipo: informe
fecha: 2026-09-27
destinatario: yo mismo (y Diego) antes de la revisión con la tutora
estado: borrador
basado_en:
  - "[[2026-09-27_borrador-de-tesis]]"
  - "[[Tesis_TeamSlash]]"
  - "[[2026-09-21_bermeo-segura-teamslash-informe-final-v4]]"
  - "[[Metodo_Memoria_Loci_Chunking_Repaso]]"
generado_por: claude
confidencial: false
tags: [out, ups, tesis, revision, teamslash]
enlazado: 2026-09-27
---

# Análisis del borrador de tesis

> [!summary] En una frase
> El diseño es sólido y bien argumentado (DSR, metas ligadas a hallazgos, LOPDP, limitaciones honestas). Lo que puede tumbarlo en revisión son **cuatro problemas de medición** y **una contradicción con el informe final de julio**; lo demás es pulido.

## Lo que ya está fuerte (no tocar)

- **Problema en dos caras** (velocidad + continuidad) y el concepto de «amnesia institucional»: claro y memorable.
- **Tabla A.1** (hallazgo → función → indicador): cada componente se justifica con un dato del diagnóstico. Es lo mejor del documento.
- **Separación PostgreSQL / bóveda** y la regla «la API y los vendedores nunca editan el mismo archivo». Es exactamente la lección que aprendimos en la bóveda propia.
- **Blockchain acotado**: solo hash, sin datos personales, con la relación con el derecho de supresión resuelta. Bien defendido.
- **Limitaciones** (a)–(g) honestas, incluida la (f): «prueba que no se alteró, no que sea verdad».
- Presupuesto cuadra: subtotal 322,00 + 10 % = **354,20** ✔.

## 🔴 Prioridad 1 — problemas que un tribunal detecta

### 1. Contradicción con el informe final de julio
El informe final (v4 y la versión del 22-jul) dice que **«la hipótesis central queda validada: la arquitectura híbrida redujo el tiempo de respuesta de más de 24 h a menos de 15 min»**. El borrador plantea ese mismo resultado como **meta futura (M1)** y parte de una línea base donde solo el 13,3 % se contacta en 15 min.
**Arreglo:** una frase explícita en *Antecedente local* o *Viabilidad*: el informe de julio validó el MVP en **pruebas controladas/demostración**, no en operación medida; esta tesis mide el efecto en operación real con registros del sistema. Así la contradicción se vuelve la justificación.

### 2. M3 compara cosas distintas
El 30,0 % es la **etapa modal de pérdida** (de los leads perdidos, en qué etapa se perdieron), no la **tasa de fuga** (de todos los leads, cuántos se pierden antes del primer contacto). «Fuga previa < 30 %» mezcla una distribución con una proporción.
**Arreglo:** definir fuga previa = leads sin evento `contactado` / leads ingresados, y fijar la meta contra la línea base documental (punto 3), no contra el 30 %.

### 3. Línea base autorreportada vs. post registrada
M1 compara una **mediana registrada por el sistema** con **porcentajes de encuesta**. La metodología ya prevé una muestra documental de conversaciones, pero no aparece en el cronograma ni se dice su tamaño.
**Arreglo:** en la actividad 1 del cronograma: «reconstrucción de línea base documental: n conversaciones de WhatsApp comerciales (p. ej. últimos 3 meses), anonimizadas antes de extraer». Medir ahí **la misma** métrica que en el post (mediana y % en 15 min). Con eso Mann-Whitney compara peras con peras.

### 4. ¿Cuántos eventos habrá en 8 semanas?
M2 (respaldo) y M1 dependen del **volumen**: si Torvesa recibe, por ejemplo, 15 leads y hay 3 ausencias del titular en 8 semanas, M2 = 80 % se decide con 3 casos. Además, las semanas 10–17 caen en **diciembre–enero**, temporada baja en construcción.
**Arreglo:** declarar el volumen esperado de leads/mes (pedir el dato a Torvesa); complementar M2 con **ausencias simuladas** (CP2/CP3 repetidos N veces) y añadir la estacionalidad a las limitaciones.

### 5. La población no es la misma en cada instrumento
Censo N = 30, pero la bóveda es solo del **equipo comercial** (A.7) y la prueba de recuperación es «cada vendedor» (asesores = 36,7 % ≈ 11 personas). Reaplicar SUS y McNemar a los 30 mezcla usuarios con no usuarios.
**Arreglo:** una tabla «instrumento → quién lo responde → n». SUS y recuperación: solo usuarios del sistema (n ≈ 11–14); diagnóstico de clima/comunicación: los 30.

## 🟠 Prioridad 2 — mejora el diseño

6. **M5 se cumple por construcción.** Un hash encadenado detecta cualquier alteración matemáticamente; como meta es trivial. Pasarla a **caso de prueba** (CP6) y usar como meta algo que sí pueda fallar: p. ej. «100 % de días con anclaje OTS confirmado» o «0 eventos sin hash». Y aclarar la **ventana intradía**: entre dos anclajes, un administrador podría reescribir la cadena del día.
7. **Git en el celular es el riesgo técnico mayor.** Obsidian Git en iOS/Android es lento e inestable con repositorios grandes; la contingencia (Obsidian Sync) está bien, pero conviene decidir con un **criterio medible** en la semana 6 (p. ej. «si > 20 % de sincronizaciones fallan en la primera semana → Sync»). Nosotros ya lo vivimos con iCloud: placeholders, archivos que no bajan, fallos silenciosos.
8. **Sprints de una semana son muy apretados** para A–D (sobre todo B: generador de fichas + sincronización + ingesta de notas de vuelta a PostgreSQL). Proponer B en 2 semanas y absorber con la semana 9, o paralelizar C y D entre Diego y Víctor (y decir quién hace qué: el tribunal pregunta por la autoría).
9. **La prueba de recuperación necesita control del aprendizaje:** clientes distintos pre y post con dificultad equivalente, los 5 datos definidos antes, y un tiempo máximo (p. ej. 5 min).
10. **Los datos del informe que faltan aquí:** el **63,3 %** que reconoce haber perdido oportunidades por información desactualizada (ítem A4) y «revisan mensajes cada 4 horas en obra». Los dos sostienen directamente la bóveda y la continuidad; hoy no aparecen.

## 🧠 Lo que aporta lo que ya levantamos en la bóveda

- **Fundamento para PO2 (ficha mínima):** la teoría de *chunking* (Miller, 1956; Cowan, 2001: la memoria de trabajo maneja ~4 bloques) justifica una ficha con un **resumen de 4–5 datos arriba** — exactamente los 5 datos de la prueba de recuperación. La estructura fija de carpetas (A.3) es el «loci» del equipo: cada cosa en un lugar predecible → búsqueda más rápida. Se puede añadir como una viñeta en *Bases teóricas* (carga cognitiva / diseño de la información), sin volverlo el eje.
- **Patrones ya probados en mi bóveda que el generador de fichas puede reutilizar:** bloques automáticos entre marcadores (`<!-- BITACORA:START/END -->`, como el `INBOX:START/END` del Dashboard), idempotencia por marca, tableros Dataview, `colorGroups` del grafo para ver la cartera por estado. Son evidencia de que el Sprint B es viable.
- **Lección «lo que el sistema escribe sobre sí mismo no debe competir con las fuentes»:** en la ficha, la bitácora automática y las notas humanas separadas (ya lo hace) y los tableros fuera de la búsqueda del equipo.
- **Oratoria de la defensa** con el método loci: una estación por sección (problema → diagnóstico → arquitectura → protocolo → resultados), y los datos duros como tarjetas de repaso.

## 🟡 Prioridad 3 — forma y referencias

- **Campos vacíos:** periodo, línea(s) de investigación, objetivos vinculados al aprendizaje, fecha de entrega.
- **Estilos:** ALCANCE, METODOLOGÍA, RESULTADOS ESPERADOS, CRONOGRAMA y PRESUPUESTO están en estilo *Texto independiente*, no en *Título* → no saldrán en el índice automático.
- **Referencias que faltan:** Reglamento General de la LOPDP (2023) se cita en el texto y no está en la lista; la frase «la literatura aplicada advierte que muchas implementaciones empresariales no necesitan blockchain» no tiene cita (candidata: Wüst y Gervais, 2018, *Do you need a blockchain?*); Scrum/Kanban sin referencia (Schwaber y Sutherland, 2020); alfa de Cronbach sin referencia.
- **Verificar:** que Habel et al. (2025) diga literalmente «0 a 23 puntos porcentuales» y que Ohiomah et al. (2019) reporte el 55 % de varianza como se cita.
- **Título:** largo (3 ideas tras los dos puntos). Opción más corta: «Sistema de comunicación y automatización comercial para Constructora Torvesa: bóveda de conocimiento, continuidad de la atención y registro verificable».
- **Ética:** la muestra documental de WhatsApp implica datos de clientes → decir que se anonimiza **antes** de la extracción y con autorización de la gerencia (ya se insinúa; hacerlo explícito).

## Datos de respaldo

| Dato | Valor | Fuente |
|---|---|---|
| Hipótesis «validada» en julio | > 24 h → < 15 min | [[2026-09-21_bermeo-segura-teamslash-informe-final-v4]] |
| Perdió oportunidades por información desactualizada | 63,3 % (A4, M = 3,57) | informe final v4, §1.7 |
| SUS línea base | 53,83 (DE 11,59; Md 52,5) | informe final v4 |
| Composición N = 30 | asesores 36,7 % · dirección 23,3 % · obra 20 % · admin 20 % | informe final v4 |
| Presupuesto | 354,20 USD (verificado) | [[2026-09-27_borrador-de-tesis]] |

## Próximos pasos

- [ ] Decidir con Diego cuáles de los puntos 1–5 entran en la versión que va a la tutora — Víctor + Diego
- [ ] Pedir a Torvesa el volumen de leads/mes y cuántos vendedores usarán el sistema — Víctor
- [ ] Confirmar fechas del periodo académico para anclar el cronograma de 21 semanas — Víctor
- [ ] Armar el plan de trabajo por bloques (método [[Metodo_Memoria_Loci_Chunking_Repaso]]) — Claude, cuando haya fechas

## Relacionado

[[Tesis_TeamSlash]] · [[MOC_UPS]] · [[TEAMSLASH]]
