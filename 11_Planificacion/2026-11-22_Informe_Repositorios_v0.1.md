# Informe de 9 repositorios para el flujo de trabajo de la tesis Torvesa

Fecha: 22-nov-2026. Los 9 repos se clonaron con `git clone --depth 1` en `scratchpad\repos\<repo>\` (hooks desactivados, sin submódulos, sin enlaces simbólicos). Solo se leyeron archivos. No se ejecutó ningún script, instalador, hook ni binario, y no se copió nada a `~/.claude`. Las rutas de este informe son relativas a esa carpeta, por ejemplo `unslop/skills/unslop/SKILL.md`.

Se comparó todo contra las 3 skills propias de Víctor (`voz-victor`, `diapositivas-pdf` y `estudio-gamificado`, solo su SKILL.md).

## 1. Tabla resumen

| Repo | Qué es | Licencia | Madurez (API de GitHub, 22-nov-2026) | Utilidad para ustedes | Riesgo |
|---|---|---|---|---|---|
| heydamir/unslop | Skill que convierte una interfaz "hecha por IA" en una diseñada: auditoría de señales, dirección en 5 líneas y 9 pasadas con valores exactos | CC BY 4.0 (exige dar crédito al autor en copias y adaptaciones) | 20 193 estrellas, último push 15-nov-2026 | **Alta** (páginas, tableros, gráficos de diapositivas) | Bajo. Los scripts (`snapshot.mjs`, `story.mjs`) piden Playwright y ffmpeg, no hacen falta |
| worldflowai/everything-claude-code | Colección de agentes, comandos, reglas, hooks y skills para Claude Code (copia adaptada del repo de affaan-m para los proyectos "synapse" y "arbiter" de WorldFlowAI) | **No tiene archivo LICENSE**. El README dice MIT y sus insignias apuntan a `affaan-m/everything-claude-code`. Licencia incierta | 6762 estrellas, último push 23-ene-2026 (10 meses sin cambios) | **Media-baja** (checklist de seguridad, ideas de contexto) | Medio. Sus hooks bloquean crear archivos `.md` (rompería la bóveda) y obligan a usar tmux |
| DietrichGebert/ponytail | Un solo prompt de "senior perezoso": el cambio más pequeño que resuelve todo, más comandos de revisión y auditoría | MIT | 196 817 estrellas, último push 22-nov-2026 | **Media** (revisión del código de Diego, respuestas más cortas) | Bajo-medio. El plugin instala hooks de Node en cada sesión y subagente, y una "band" que guarda métricas en `~/.config/ponytail/` |
| nextlevelbuilder/ui-ux-pro-max-skill | Base de datos en CSV (estilos, paletas, fuentes, 141 reglas UX, 25 tipos de gráfico) con buscador BM25 en Python, más skills de diapositivas, marca y logos | MIT | 152 804 estrellas, último push 22-nov-2026 | **Media-alta** (reglas de formularios, gráficos y accesibilidad) | Bajo. `search.py` no usa red; hay que correrlo para aprovecharlo |
| leonxlnx/taste-skill | Skill pesada para sitios web de empresa: reparte dirección de arte, busca fotos con licencia y revisa la página en Chrome con un "gate" | MIT | 120 059 estrellas, último push 22-nov-2026 | **Media** (solo las reglas de redacción `copy-*.md`); el resto es para sitios comerciales | Medio. El SKILL.md declara un hook `Stop` que ejecuta `gate.mjs` con Node; descarga fotos e íconos de Wikimedia y jsDelivr; un build dura de 30 a 45 min según tasteskill.dev |
| VoltAgent/awesome-claude-design | Lista de 68 enlaces a archivos DESIGN.md (inspirados en marcas como Notion, Linear, Claude) para Claude Design | MIT (los DESIGN.md enlazados están fuera del repo) | 4666 estrellas, último push 20-jun-2026 | **Media** (la estructura de 9 secciones de un DESIGN.md) | Bajo. Solo hay README y LICENSE. Aviso del propio repo: no copiar marcas 1 a 1 |
| bergside/design-md-chrome | Extensión de Chrome (MV3) que lee estilos de una página y genera DESIGN.md o SKILL.md | MIT | 3206 estrellas, último push 25-may-2026 | **Baja-media** (la plantilla de DESIGN.md y sus "Quality Gates") | Bajo. Permisos `activeTab`, `scripting`, `storage`, `downloads`; no vi llamadas de red salvo enlaces a typeui.sh |
| Panniantong/agent-reach | CLI en Python para que el agente lea X, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu, LinkedIn y otros, reutilizando sesiones del navegador | MIT | 113 989 estrellas, último push 22-nov-2026 | **Baja** (no tiene ninguna fuente académica) | **Alto** en privacidad: copia cookies de sesión de Chrome, manda URL a Jina y Exa, y se instala pidiéndole al agente que lea un archivo remoto |
| usestrix/strix | Herramienta de pruebas de penetración con agentes de IA que explotan y validan vulnerabilidades dentro de un contenedor Docker | Apache 2.0 | 77 058 estrellas, último push 19-nov-2026 | **Media** para Diego (solo contra su propia prueba de concepto) | **Alto** si se usa mal: ataca de verdad, el contenedor pide NET_ADMIN, NET_RAW y SYS_ADMIN, gasta API y tiene telemetría activa por defecto |

## 2. Análisis por repositorio

### 2.1 unslop (heydamir)

**Qué contiene.** `unslop/skills/unslop/SKILL.md` (237 líneas, el método), `references/signs.md` (lista de señales de "slop" con su arreglo), `references/tokens.md` (valores exactos de espaciado, rampas neutras, tipografía, radios y movimiento), `references/visuals.md` (cómo elegir y pedir una imagen), `references/effects.md`, `references/rtl.md` y `references/refs.md` con imágenes de referencia. `scripts/snapshot.mjs` guarda una página en vivo con Playwright y `scripts/story.mjs` arma un video con ffmpeg. `examples/` trae 3 HTML (dashboard, hero, tienda).

**Ideas que valen la pena.**
- **Dirección en 5 líneas antes de tocar nada** (`SKILL.md`, sección Direction): Producto, Carácter (2 o 3 palabras concretas; prohíbe "clean, modern, sleek, minimal, premium"), Mundo (el lugar o material del producto), Momentos (1 o 2 sitios con color rico) y Firma (un solo detalle propio). Se le muestra al usuario y se espera su respuesta.
- **Decidir cuánto cambiar** (`SKILL.md`, Run it, paso 3): mucho slop = proceso completo; poco = modo pulido, solo lo que salió en la auditoría; nada = decirlo y sugerir 2 o 3 ajustes como máximo. "Never change a good screen just to make it different."
- **Nueve pasadas en orden**: espaciado, color, íconos, texto, tipo, layout, detalles, visuales, movimiento. El espaciado va primero porque cambia cómo se lee todo; el texto antes que el tipo porque el largo del titular decide su tamaño.
- **Riqueza en el contenido, no en el marco** (`SKILL.md`, intro): la navegación, botones y bordes quedan quietos y el color va a 1 o 2 "momentos" (un gráfico bien hecho, un objeto real).
- **Gráficos** (`SKILL.md`, sección 7 Details): un gráfico principal claramente más grande; los demás datos en otra forma (lista con barras finas o tabla corta); un solo acento por gráfico en lo que importa y lo demás en grises; tipo de gráfico según el dato (tendencia = línea, comparación = barras, proporción = una barra apilada o lista con barras, meta = barra de progreso). Las tarjetas de cifras son "label, número grande y cambio con su referencia", sin sparklines de relleno.
- **Texto de interfaz** (`SKILL.md`, sección 4 Copy): sin signos de exclamación; un cambio siempre dice contra qué compara ("+12 % vs. el mes pasado"); sin punto final en títulos, etiquetas y botones; datos de ejemplo verosímiles, nunca "[X]" ni "123,456"; afirmaciones no comprobables se confirman o se quitan.
- **Tokens concretos** (`references/tokens.md`): escala de espaciado 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128; rampas neutras "warm" (página #f7f4ee, texto #1f1b16) que encajan con el papel #F5F1E8 y la tinta #1B2430 de `diapositivas-pdf`; pesos 400 y 500 (600 rara vez); letra de menos de 16 px sin tracking negativo; radio anidado = radio exterior menos el padding; una sola curva de animación `cubic-bezier(0.22, 1, 0.36, 1)`.
- **Prueba de plantilla** (`SKILL.md`, último ítem del Checklist): si cambias el nombre del producto por otro y la pantalla igual encaja, falta dirección.

**Cómo adaptarlo.**
- Artefactos HTML y tableros (Bitácora Torvesa, Arena de estudio, tableros del modelo de negocio): usar la auditoría de `signs.md` y el checklist final como revisión obligatoria antes de publicar.
- Diapositivas (`diapositivas-pdf`): ya siguen casi todo (paleta propia, un mensaje por diapositiva). Faltan las reglas de gráficos: un acento por gráfico, tarjetas de cifra sin adornos, cambio con referencia, cifras con `font-variant-numeric: tabular-nums`.
- Formulario web de la prueba de concepto: las pasadas 1 a 5 sirven tal cual para el formulario y la vista de Slack/tablero.
- Word y PDF de la tesis: solo el principio "sin mayúsculas con tracking, pocas negritas, jerarquía por tamaño y color", que coincide con `voz-victor`.

**Qué no usar.** El "story video" (`scripts/story.mjs`, necesita Playwright y ffmpeg, es para redes sociales). La parte de imágenes generadas para héroes de landing (no tienen landing). `rtl.md` (no aplica). Si se adapta el texto a una skill propia, la licencia CC BY 4.0 obliga a dar crédito a Damir Sokolovsky.

### 2.2 everything-claude-code (worldflowai)

**Qué contiene.** `agents/` (planner, architect, tdd-guide, code-reviewer, security-reviewer, build-error-resolver, e2e-runner, refactor-cleaner, doc-updater), `commands/` (/plan, /tdd, /verify, /checkpoint, /learn…), `rules/` (coding-style, security, testing, performance, git-workflow, agents, hooks, patterns), `skills/` (security-review, verification-loop, strategic-compact, continuous-learning, eval-harness, frontend/backend-patterns, clickhouse-io), `hooks/hooks.json`, `mcp-configs/mcp-servers.json` (todos con `npx`), y `WORLDFLOWAI.md`, una guía para dos proyectos internos de esa empresa (Rust y Python ML).

**Ideas que valen la pena.**
- **Checklist de seguridad antes de cada commit** (`rules/security.md`): sin secretos en el código, entradas validadas, consultas parametrizadas, XSS, CSRF, autenticación verificada, límite de peticiones en todos los endpoints y errores que no filtran datos sensibles. Protocolo si aparece un problema: parar, arreglar lo crítico, **rotar cualquier secreto expuesto** y buscar el mismo error en todo el código.
- **Skill de revisión de seguridad** (`skills/security-review/SKILL.md`): 10 bloques con casillas. Los útiles para Diego: secretos (incluye "no secrets in git history" y "production secrets in hosting platform (Vercel, Railway)"), validación con esquemas y lista blanca, SQL parametrizado, tokens en cookies httpOnly, CSP, SameSite, límite por IP y por usuario, logs sin contraseñas ni tokens, sin stack traces al usuario, y auditoría de dependencias.
- **Bucle de verificación** (`skills/verification-loop/SKILL.md`): build, tipos, lint, pruebas, búsqueda de secretos con grep (`sk-`, `api_key`), `console.log` y revisión del diff, en ese orden, deteniéndose si falla el build.
- **Manejo de contexto** (`rules/performance.md` y README): no usar el último 20 % de la ventana de contexto para refactorizaciones grandes; no tener todos los MCP activos a la vez ("Your 200k context window can shrink to 70k with too many tools enabled"); usar `disabledMcpServers` por proyecto.
- **Compactar en límites lógicos** (`skills/strategic-compact/SKILL.md`): después de explorar y antes de ejecutar, al terminar un hito, y nunca en medio de una implementación.
- **Modo investigación** (`contexts/research.md`): leer antes de concluir, formar hipótesis, verificar con evidencia, "Findings first, recommendations second".

**Cómo adaptarlo.** El checklist de seguridad, recortado a Node.js, Railway, PostgreSQL y Slack, para Diego (ver sección 3). La regla de compactar por hitos encaja con sus bloques dobles: compactar al cerrar cada bloque.

**Qué no usar.**
- `hooks/hooks.json`: uno bloquea escribir cualquier `.md` que no sea README, CLAUDE, AGENTS o CONTRIBUTING. En una bóveda de Obsidian rompe todo el trabajo. Otro bloquea servidores de desarrollo fuera de tmux (no existe en Windows sin WSL).
- `continuous-learning` (hook `Stop` que guarda "patrones" en `~/.claude/skills/learned/` sin revisión) choca con su regla de infraestructura congelada y con la memoria que ya llevan.
- `rules/coding-style.md` impone inmutabilidad y archivos de 200 a 400 líneas como dogma, y `rules/testing.md` un 80 % de cobertura: excesivo para una prueba de concepto.
- `rules/performance.md` habla de modelos "Haiku 4.5, Sonnet 4.5, Opus 4.5": desactualizado.
- La licencia no está clara (no hay archivo LICENSE en este fork). Si se copian textos, mejor tomar las ideas y redactarlas de nuevo.

### 2.3 ponytail (DietrichGebert)

**Qué contiene.** El núcleo es un solo prompt: `ponytail/skills/ponytail/SKILL.md` (3,5 KB), con versión compacta en `AGENTS.md`. Además `skills/ponytail-review`, `ponytail-audit`, `ponytail-debt`, `ponytail-gain` y `ponytail-help`. `hooks/` tiene adaptadores para 20 agentes y la "band" (panel con costo, tokens y tiempo). `benchmarks/results/` tiene las mediciones.

**Cómo ahorra tokens.** No comprime contexto ni usa trucos de caché. Ahorra porque **el agente escribe menos código y responde más corto**:
- La "escalera" (`SKILL.md`, The smallest complete change): ¿hace falta?, ¿ya existe en el código?, ¿lo hace la biblioteca estándar o la plataforma?, ¿lo hace una dependencia instalada?, ¿cabe en una línea clara?, y solo al final el mínimo código que funcione.
- Cierre fijo: "End your reply with one or two lines: what you skipped or did not check, and any risk the user must know."
- El benchmark de junio (`benchmarks/results/2026-06-12-caveman-vs-ponytail.md`) cuenta dos cosas útiles: la v1 ahorraba código pero "wrote minimal code, then long 'skipped on purpose' essays. Prose ate the code savings", y por eso la v2 puso un tope ("if the explanation is longer than the code, delete the explanation"); y en tareas ya mínimas cada skill cuesta unos 3000 tokens de lectura ("skill-read tax").
- Los números del README (-45 % tokens, -26 % costo, 39 tareas, 5 corridas) los midió el mismo autor: tomarlos como orientación.

**Ideas que valen la pena.**
- **Nunca recortar** (`SKILL.md`): validación en los límites de confianza, manejo de errores que evita pérdida de datos, seguridad y accesibilidad.
- **Atajos marcados** (`SKILL.md` y `skills/ponytail-debt/SKILL.md`): un límite conocido se anota en el código como `shortcut: <el límite>, <cuándo mejorarlo>`, y luego se juntan todos en un registro. Un atajo sin "cuándo" se marca `no-trigger`.
- **Formato de revisión para personas** (`skills/ponytail-review/SKILL.md`): orden de importancia (correcto, seguro, aguanta la carga, probado, rápido, sin sobrante); cada hallazgo necesita un caso concreto ("No case, no finding"); grupos Must fix, Should fix y Nice to have numerados; cada hallazgo con 4 partes (qué es, problema, arreglo, qué pasa si no se arregla) en inglés muy simple; cierre con "Verdict" y "Not checked". También pide decir qué carga se asumió (un usuario o muchos).

**Cómo adaptarlo.**
- Revisión del código de Diego: usar el formato de 4 partes en español para que Víctor y la tutora entiendan los hallazgos sin leer código (cumple la regla de "ningún código sin explicar").
- Los comentarios `shortcut:` del código de la prueba de concepto alimentan directo la sección de limitaciones de la tesis: cada límite con su condición de mejora.
- La regla "si la explicación es más larga que el resultado, se borra la explicación" y el cierre de 1 o 2 líneas sirven para las respuestas de Claude en la bóveda.

**Qué no usar.** El plugin completo con hooks (`SessionStart`, `SubagentStart`, `UserPromptSubmit`) y la band: inyectan instrucciones en cada sesión y en cada subagente, también cuando se redacta la tesis. El tono "lazy" no sirve para textos académicos. Si se quiere, basta con copiar 5 o 6 reglas al `CLAUDE.md` del repositorio de Diego (no al de la bóveda).

### 2.4 ui-ux-pro-max-skill (nextlevelbuilder)

**Qué contiene.** La fuente está en `src/ui-ux-pro-max/` (datos CSV y `scripts/search.py`, `core.py`, `design_system.py`) y se replica en `.claude/skills/` y `cli/assets/`. Datos: `styles.csv` (89 filas), `colors.csv` y `products.csv` (194), `typography.csv` (74 pares), `ux-guidelines.csv` (141), `charts.csv` (25 tipos), `icons.csv`, `motion.csv`, `google-fonts.csv` (1934). Skills extra en `.claude/skills/`: `slides`, `design`, `brand`, `design-system`, `banner-design`, `ui-styling`. La skill principal es `.claude/skills/ui-ux-pro-max/SKILL.md` con `references/quick-reference.md` (todas las reglas UX) y `references/pro-rules.md` (checklist de app móvil).

**Ideas que valen la pena.**
- **Prioridades** (`SKILL.md`, Rule Categories by Priority): 1 accesibilidad (contraste 4,5:1, texto alternativo, teclado), 2 interacción táctil (44×44 px), 3 rendimiento (reservar espacio, CLS menor a 0,1), 4 estilo, 5 layout responsive (sin scroll horizontal), 6 tipo y color (base 16 px, interlineado 1,5, colores como tokens), 7 animación, 8 formularios, 9 navegación, 10 gráficos.
- **Reglas de formularios** (`references/quick-reference.md`, sección 8): etiqueta visible por campo (no solo placeholder), error debajo de su campo con causa y forma de arreglarlo, validar al salir del campo y no mientras escribe, no marcar un campo vacío antes de que el usuario pase por él, **conservar todo lo escrito cuando falla el envío**, no desactivar el botón de enviar antes de tiempo (solo mientras la petición está en curso, con clave de idempotencia), resumen de errores enfocable arriba, confirmación antes de acciones destructivas, autoguardado en formularios largos, aviso de tiempo agotado con opción de reintentar.
- **Gráficos** (`src/ui-ux-pro-max/data/charts.csv`): tendencia con menos de 4 puntos va como tarjeta de cifra; barras siempre ordenadas de mayor a menor; más de 15 categorías van a tabla; torta solo con 5 categorías o menos y diferencias mayores al 5 %, si no, barra apilada al 100 %; nunca distinguir series solo por color (usar etiquetas directas o estilos de línea); acompañar con tabla de datos visible.
- **Regla de honestidad del buscador** (`SKILL.md`, If a search returns 0 results): no inventar resultados; reintentar una vez; si falla, decir que la recomendación viene de valores por defecto. Es la misma lógica de su regla de fuentes.
- **Master + overrides** (`SKILL.md`, Step 2b): un `MASTER.md` de diseño y archivos por página que lo sobrescriben, sin sobrescribir el maestro sin permiso (`--force` solo con autorización). Coincide con su ciclo de versiones.
- **Diapositivas** (`.claude/skills/slides/references/slide-strategies.md`): estructuras por objetivo (Problema-Solución-Beneficio de 3 a 5 diapositivas, QBR, caso de estudio) y el patrón "Duarte Sparkline" que alterna "lo que es" y "lo que podría ser".

**Cómo adaptarlo.**
- Formulario de la prueba de concepto: las reglas de la sección 8 son la mejor lista de revisión del formulario de Diego.
- Excel y gráficos de `diagramas.py` o de diapositivas: las reglas de `charts.csv` (orden descendente, límites de categorías, nada solo por color).
- No hace falta instalar la skill: se pueden leer los CSV como referencia. Si algún día se usa `search.py`, no tiene dependencias externas y no usa red, pero ejecutarlo requiere permiso de Víctor (infraestructura congelada).

**Qué no usar.** Las paletas y estilos de `styles.csv` (glassmorphism, aurora, neumorfismo) traen justo lo que unslop y taste llaman slop: degradados morados y brillos. Las skills `brand`, `banner-design` y logos no aplican. Las reglas de `pro-rules.md` son para apps nativas.

### 2.5 taste-skill (leonxlnx) y tasteskill.dev

**Qué contiene.** Una sola skill, `taste-skill/skills/taste-skill/SKILL.md` (`design-taste-frontend`, 2.5.1), con 22 referencias en `references/`, librerías `library/palettes.json` y `type.json`, un kit en `assets/` y 12 scripts de Node en `scripts/` (gate, copy-lint, consistency, photos, icons, perf, shoot…). La página tasteskill.dev la describe como gratuita y MIT, con Node 22 y Chrome, sin claves de API, "a build takes roughly 30 to 45 minutes", y que reparte 3 de 20 direcciones de arte por build. La página no tenía instrucciones dirigidas a agentes.

**Ideas que valen la pena.** Lo más valioso para ustedes no es el diseño web, son las reglas de redacción:
- **`references/copy-tells.md`** (fechado nov-2026) separa los rasgos de IA en generaciones. Primera generación: palabras prohibidas (delve, tapestry, seamless, robust, leverage, unlock, empower…), frases hechas ("In today's fast-paced world", "It's not just X, it's Y", "Not only X but also Y"), restos de chat ("Certainly!", "[Company Name]"), el gerundio colgado al final (", ensuring a smooth start"), la pregunta que se responde sola ("¿El resultado? Tres horas menos."), "serves as / plays a key role" en vez de "es / tiene", rayas por todas partes.
- **Segunda generación** (la que hoy pasa las revisiones): **datos inventados para parecer específicos** ("Batch No. 047", "38 % menos"), **la franja de 3 o 4 cifras con una palabra debajo**, **títulos de dos fragmentos** ("Doce cuartos. Tres formas de quedarse."), **marcos de contraste y sus sustitutos** ("no es X", "en lugar de", "sin el"), **series de negaciones**, **palabras de virtud sobre uno mismo** (honesto, tranquilo, realmente, simplemente, cuidadosamente), **la frase final ingeniosa en cada párrafo**, **hablar del propio texto** ("Esta sección muestra", "A continuación encontrarás") y **la uniformidad perfecta** (todos los párrafos del mismo largo).
- **Tabla de sobrecorrección** (`copy-tells.md`): cada regla anti-IA produce otro vicio. Sin rayas → todo con puntos; sin "no X sino Y" → "en lugar de"; sin palabras de moda → vocabulario "tranquilo"; evitar tríadas → todo en pares (**contramedida: listar tantos elementos como haya**); ser específico → inventar números (**contramedida: solo hechos de la fuente o una frase más simple**); terminar fuerte → moraleja en cada párrafo (**terminar con información**).
- **"Not tells"** (`copy-tells.md`, última sección): gramática perfecta, "es" y "tiene", un conector solo, una lista de tres cuando hay tres cosas. No hay que castigar eso.
- **`references/copy.md`, Five rules**: cada título lleva un sustantivo que nombra algo; botones como verbo más lo que se obtiene, nunca "Ver más" o "Descubrir"; la primera pantalla tiene un dato duro (número, lugar, precio o fecha).
- **`references/copy-voice.md`**: primero una ficha de hechos sacada del encargo; "nada se inventa"; "hechos donde quieren ir los adjetivos" (si dices "rápido", la cifra va en la misma oración); la prueba de "nueve otros rubros" (si la voz le queda a cualquier negocio, no es una voz).
- **SKILL.md, Never**: nada de reseñas, citas, clientes o cifras inventadas; nada de copiar código, textos o efectos de un sitio de referencia.

**Cómo adaptarlo.** Las reglas de segunda generación y la tabla de sobrecorrección encajan directo en `voz-victor` y en `revisar_voz.py` (ver propuesta 1). Varias ya existen en su skill (tríadas, gerundios, rayas, "no solo… sino también"); lo nuevo es: datos inventados, franja de cifras, títulos de dos fragmentos, sustitutos del contraste, palabras de virtud, cierre ingenioso, hablar del propio texto y la tabla de sobrecorrección.

**Qué no usar.** El resto de la skill: está pensada para sitios de empresa (cafés, SaaS, juegos), exige "una sección por pantalla", fotos de stock con licencia y efectos de shader, y su hook `Stop` corre `gate.mjs` al terminar cada turno en Claude Code. Para la tesis y sus artefactos es demasiado pesada y choca con la infraestructura congelada.

### 2.6 awesome-claude-design (VoltAgent)

**Qué contiene.** Solo `README.md` (230 líneas) y `LICENSE`. Es una lista de 68 enlaces a DESIGN.md alojados en getdesign.md, agrupados por rubro (IA, herramientas de desarrollo, SaaS, fintech…), y explica cómo subirlos a Claude Design.

**Ideas que valen la pena.**
- **Las 9 secciones de un DESIGN.md** (`README.md`, What Claude produces from a DESIGN.md): 1 tema visual y atmósfera, 2 paleta y roles de color, 3 reglas de tipografía, 4 estilos de componentes, 5 principios de layout, 6 profundidad y elevación, 7 qué sí y qué no, 8 comportamiento responsive, 9 guía de prompts para el agente.
- **La idea central** (`README.md`, What is DESIGN.md?): poner "token, regla y razón en el mismo archivo", porque la razón le permite al agente decidir bien en casos que el archivo no cubre.
- **Aviso legal** (`README.md`, License & disclaimer): los DESIGN.md son inspiración, no sistemas oficiales; usar como base para un sistema propio y no clonar una marca.

**Cómo adaptarlo.** Escribir un único `DESIGN.md` de la tesis y de Torvesa con esas 9 secciones, tomando lo que ya está en `diapositivas-pdf` (paleta tinta, papel, arena, cobre, ladrillo, salvia, azul, dorado; Archivo y Source Sans 3; íconos SVG de trazo 1.8) y la razón de cada decisión. Lo leerían `diapositivas-pdf`, `estilo_docx.py`, los Excel y los artefactos. El de Notion o el de Claude en getdesign.md podría servir como ejemplo de formato (no lo abrí: está fuera del repo).

**Qué no usar.** Los DESIGN.md de marcas ajenas como estilo final (problema de marca y la regla de no imitar organizaciones reales en artefactos). Claude Design no es parte de su flujo.

### 2.7 design-md-chrome (bergside / TypeUI)

**Qué contiene.** Extensión MV3: `manifest.json`, `content-script.js` (lee estilos de la pestaña), `service-worker.js`, `popup/`, `lib/normalize.mjs`, `lib/generate-design-md.mjs`, `lib/generate-skill-md.mjs`, `lib/validate.mjs` y `DESIGN.md`, que en realidad es la plantilla para escribir skills de sistemas de diseño.

**Ideas que valen la pena.**
- **Estructura** (`DESIGN.md`, Required skill.md Structure): Misión, Marca (producto, público, superficie), Fundamentos de estilo (tokens), Accesibilidad (WCAG 2.2 AA, teclado, foco visible, contraste), Tono de escritura, Reglas Do, Reglas Don't, Flujo de redacción, Estructura de salida, Expectativas por componente, Quality Gates.
- **Quality Gates** (`DESIGN.md`): toda regla obligatoria usa "must" y toda recomendación "should"; cada regla de accesibilidad debe poder probarse; consistencia del sistema antes que excepciones locales.
- **Do y Don't concretos** (`DESIGN.md`): definir todos los estados (default, hover, foco visible, activo, deshabilitado, cargando, error); no permitir texto de bajo contraste ni foco oculto; no inventar excepciones de espaciado o tipografía; no usar etiquetas ambiguas.
- **Acceptance Checklist** (`DESIGN.md`): frontmatter válido y SKILL.md de menos de 500 líneas cuando se pueda (útil también para ahorrar tokens).

**Cómo adaptarlo.** Usar esta plantilla junto con las 9 secciones de awesome-claude-design para el `DESIGN.md` propio. En español, el par "debe / conviene" reemplaza "must / should". La extensión en sí no hace falta: ustedes no copian sitios ajenos.

**Qué no usar.** Instalar la extensión en el perfil `F:\IA\chrome_tesis` no aporta nada a la tesis y agrega permisos de scripting en todas las pestañas activas.

### 2.8 agent-reach (Panniantong)

**Qué fuentes permite.** Según `agent-reach/docs/README_en.md` (tabla Supported Platforms): por defecto github, youtube (info, búsqueda, subtítulos; la transcripción de voz pide clave de Groq u OpenAI), web (búsqueda con Exa y lectura con Jina Reader), v2ex y bilibili. Opcionales con sesión iniciada: reddit, linkedin, xiaohongshu, xueqiu, boss, xiaoyuzhou (pide clave de Groq). Experimentales con sesión: twitter, facebook, instagram.

**Qué cuentas y claves pide.** Groq u OpenAI para transcribir audio; cuentas propias en las redes con sesión. El código (`agent_reach/runtime/session_reuse.py`, `backends/opencli.py`) **exporta las cookies de sesión del sitio desde el Chrome local** y las inyecta en su propio navegador por CDP. El propio README recomienda usar una cuenta secundaria porque "platforms may restrict accounts used for automation". Usa además la extensión OpenCLI de la Chrome Web Store.

**Riesgos.**
- Privacidad: copia cookies de cuentas reales; las URL que lee el canal web se envían a `r.jina.ai` y a `mcp.exa.ai` (`agent_reach/channels/web.py`).
- Términos de servicio: X, Reddit, LinkedIn, Facebook e Instagram prohíben o limitan el acceso automatizado; el README admite que la plataforma "fights automation harder and it can break at any time". Los patrocinadores son servicios de proxys residenciales y desbloqueo anti-bots.
- Instalación: se hace pidiéndole al agente que lea `https://raw.githubusercontent.com/Panniantong/Agent-Reach/main/docs/install.md`, un archivo que dice "For the AI doing the work. Run every command yourself" y que puede cambiar en cualquier momento. Eso es darle instrucciones remotas al agente. Lo anoto como riesgo y no lo seguí. El README también avisa que el paquete `agent-reach` de PyPI es otro proyecto.

**¿Sirve para buscar fuentes académicas?** **No.** Busqué en todo `agent_reach/` y no hay ningún canal de OpenAlex, Semantic Scholar, Crossref, arXiv, PubMed ni Google Académico. Lo único cercano es leer subtítulos de conferencias en YouTube o repos de GitHub, que ya pueden hacer con Chrome por CDP, `gh` o WebFetch. Para la tesis, lo que ya tienen (APIs de OpenAlex y Semantic Scholar, Consensus, Chrome por CDP con su perfil) es mejor y más seguro. Un tuit, un post de Reddit o un video no cuentan como fuente "verificada" según su CLAUDE.md, salvo como dato de contexto con su fecha.

**Qué rescatar.** Solo dos ideas de diseño, sin instalar nada (`agent_reach/skill/SKILL_en.md`): "Prefer your own tools for public content; Reach fills the gaps", y la tabla de errores que dice cuándo **no** reintentar (`RATE_LIMITED`, `PLATFORM_BLOCKED`: parar; nunca cambiar de cuenta o de backend para saltar un bloqueo; "never retry in a loop"). Encaja con su regla de no automatizar Google Académico.

### 2.9 strix (usestrix)

**Qué hace.** Agentes de IA que hacen pruebas de penetración: reconocen la aplicación, intentan explotar fallas reales (inyección SQL y NoSQL, XSS, SSRF, IDOR, fallas de autenticación y JWT, lógica de negocio, carreras) y solo reportan lo que pudieron probar con una prueba de concepto (`strix/README.md`, Features). Puede revisar código fuente (`--target ./carpeta`), un repo, una URL en vivo o un contrato OpenAPI o Postman. Tiene modos `quick`, `standard` y `deep` (`docs/usage/cli.mdx`); el modo por defecto es `deep`. Los resultados quedan en `strix_runs/<corrida>/` y se ven con `strix view` en 127.0.0.1.

**Qué necesita.**
- Docker en ejecución; la primera corrida descarga la imagen del sandbox.
- Una clave de API de un proveedor de modelos (`STRIX_LLM` y `LLM_API_KEY`). Con modelos locales (Ollama) el propio `docs/llm-providers/local.mdx` dice que los de menos de 70B "struggle".
- Instalación con `curl -sSL https://strix.ai/install | bash`, o por pipx o uv (`strix-agent`).
- Opcional: claves de Perplexity o Exa para búsqueda web (`strix/config/settings.py`).

**Riesgos.**
- **Ataca de verdad.** Apuntarlo a un servidor que no es de ustedes es ilegal. El propio `skills/penetration-testing-with-strix/SKILL.md` dice "Only scan targets the user owns or is authorized to test", y la versión de código abierto no verifica el dominio (la nube sí).
- **Privilegios del contenedor:** `strix/runtime/docker_client.py` agrega NET_ADMIN y NET_RAW (para `nmap -sS`) y SYS_ADMIN en algunos casos.
- **Datos al proveedor de IA:** el código, las respuestas del servidor y las credenciales que se pasen en `--instruction` viajan al modelo en la nube. Nunca usar datos reales de Torvesa ni de clientes.
- **Telemetría activa por defecto** (`strix/config/settings.py`: `STRIX_TELEMETRY` en True; `strix/telemetry/README.md`): manda a PostHog y Scarf datos anónimos (sistema, modo, modelo, conteos de vulnerabilidades por severidad). Se apaga con `STRIX_TELEMETRY=0`.
- **Costo:** sin límite salvo que se pase `--max-budget` (en dólares); `--max-turns` es 500 por defecto.
- **Daño al objetivo:** un modo `deep` contra una base de datos real puede escribir o borrar registros y llenar Slack de mensajes de prueba.
- El enlace de `strix view` lleva un token que da acceso a la corrida: no compartirlo.

**Cómo podría usarla Diego, solo contra su propia prueba de concepto** (no lo ejecuté; es un plan para que Diego lo apruebe con Víctor):
1. Copia local o de staging: levantar la API de Node.js y un PostgreSQL de prueba con Docker en su máquina, con los **datos simulados**, un webhook de Slack de un canal de pruebas y claves de prueba. Nada contra el Railway de producción ni contra la bóveda real.
2. Instalación con versión fija por pipx o uv (`strix-agent`), mejor que `curl | bash`.
3. Variables: `STRIX_TELEMETRY=0`, una clave de API con límite de gasto, `--max-budget 5` o 10.
4. Primera pasada solo sobre el código: `strix -n --target ./api --scan-mode quick`. El modo `quick` (`strix/skills/scan_modes/quick.md`) prioriza bypass de autenticación, control de acceso, ejecución remota, inyección SQL, SSRF (webhooks) y secretos expuestos.
5. Segunda pasada contra la copia local: `--target ./api --target http://localhost:<puerto>` con una instrucción que diga el alcance ("solo esta API; no enviar mensajes a Slack reales; dos usuarios de prueba").
6. Para el asistente con RAG: leer antes `strix/skills/technologies/llm_applications.md` y `strix/skills/vulnerabilities/llm_prompt_injection.md` (inyección de instrucciones por documentos de la bóveda, fuga de datos entre usuarios, el modelo con más permisos de los necesarios, salida del modelo mostrada como HTML).
7. Verificar a mano cada prueba de concepto antes de creer el reporte y volver a correr después de cada arreglo. Un código de salida 0 solo significa "nada probado en lo analizado".
8. En la tesis se describe como "pruebas de seguridad del diseño en un entorno controlado", sin decir "piloto".

### 2.10 Comparación con sus skills propias

- `voz-victor` ya cubre la mitad de la lista de taste-skill (conectores de manual, punto y coma, rayas, tríadas, gerundios). Le faltan los rasgos de segunda generación y la tabla de sobrecorrección. Ojo con una tensión: `voz-victor` prohíbe tríadas y taste-skill avisa que eso lleva a "todo en pares". La regla correcta es "tantos elementos como haya".
- `diapositivas-pdf` ya aplica pirámide de Minto, un mensaje por diapositiva, paleta propia, íconos SVG propios y revisión visual por PNG. Le sumarían las reglas de gráficos de unslop y `charts.csv`.
- `estudio-gamificado` y la Arena son artefactos HTML: allí sirven la auditoría de unslop (sin emojis como íconos, un acento, sin animaciones en bucle) y las reglas de formularios y accesibilidad de ui-ux-pro-max. Ojo: la Arena usa XP, rangos y rachas a propósito; eso no es slop, es el diseño que Víctor pidió.

## 3. Propuesta de adaptación (priorizada)

Ninguna se ejecuta sin el visto bueno de Víctor (infraestructura congelada). Todas son cambios en archivos que ya existen o un archivo nuevo de texto; ninguna instala software.

| # | Qué se hace | Dónde | Esfuerzo | Riesgo |
|---|---|---|---|---|
| 1 | Agregar a `voz-victor` una sección "Rasgos de IA de segunda generación" (datos inventados, franja de cifras, títulos de dos fragmentos, "no es X" y sus sustitutos "en lugar de" / "sin el", palabras de virtud, cierre ingenioso, hablar del propio texto, uniformidad) y la tabla de sobrecorrección. Sumar contadores a `revisar_voz.py` para "en lugar de", "no es… es", "esta sección", "a continuación", "realmente", "simplemente" usado como virtud y títulos con dos fragmentos. Fuente: `taste-skill/.../references/copy-tells.md` | `C:\Users\vasha\.claude\skills\voz-victor\SKILL.md` y `revisar_voz.py` | 3 h | Bajo. Cuidar que "simplemente" ya es muletilla aceptada de Víctor: contarlo solo si pasa de 2 por página |
| 2 | Escribir un `DESIGN.md` único (tesis y Torvesa) con las 9 secciones de awesome-claude-design y los Quality Gates de TypeUI: paleta con roles y razones, tipografías, escala de espaciado de 4 px, radios, íconos, gráficos, qué sí y qué no, versiones para Word, PDF, Excel y web | Nuevo, por ejemplo en la carpeta de la skill `diapositivas-pdf` o en `99_Scripts/gestion/` (proponer ruta a Víctor) | 2 a 3 h | Bajo |
| 3 | Crear una skill `diseno-paginas` para artefactos HTML y tableros: dirección en 5 líneas, auditoría con `signs.md`, tokens, reglas de gráficos y tarjetas, formularios, revisión visual a 1440, 768 y 390 px con un máximo de 3 renders, prueba de plantilla. Lee el `DESIGN.md` del punto 2. Crédito a unslop (CC BY 4.0) | `C:\Users\vasha\.claude\skills\diseno-paginas\SKILL.md` | 5 h | Bajo. Mantener el SKILL.md corto (menos de 200 líneas) y dejar detalles en `references/` |
| 4 | Sumar a `diapositivas-pdf` las reglas de gráficos: un acento por gráfico, un gráfico principal por diapositiva, tarjetas de cifra solo con etiqueta, número y cambio "vs." algo, barras ordenadas de mayor a menor, cifras con `tabular-nums`, nada que se distinga solo por color | `C:\Users\vasha\.claude\skills\diapositivas-pdf\SKILL.md`, sección 3 | 1 h | Bajo |
| 5 | Checklist de seguridad para Diego, en español y para su stack (Node.js en Railway, PostgreSQL, webhook del formulario, Slack, RAG, huellas SHA-256): ver las reglas 41 a 50 de abajo | Agregar a `IA_DIEGO.md` o a un archivo en su repo de código | 2 h | Bajo |
| 6 | Formato de revisión de código "para personas" (4 partes por hallazgo, grupos Debe arreglarse / Conviene / Opcional, veredicto, "No revisado") tomado de `ponytail-review`, para que Víctor y la tutora lean las revisiones del código de Diego | `IA_DIEGO.md` y, si se usa, el informe de revisión en `07_Flujos_Diseno/` (ya existe `2026-11-17_Revision_Codigo_Limpio_v0.1.md`) | 1 h | Bajo |
| 7 | Convención `atajo: <límite>, <cuándo mejorarlo>` en los comentarios del código de la prueba de concepto, y un registro de atajos que alimente la sección de limitaciones de la tesis | Repo de Diego + `MANUAL_TESIS.md` (marcador nuevo) | 1 h + 30 min por revisión | Bajo |
| 8 | Prueba de seguridad con Strix solo contra una copia local de la prueba de concepto, con datos simulados, `STRIX_TELEMETRY=0`, `--scan-mode quick` y `--max-budget`. Pasos en la sección 2.9 | Máquina de Diego, fuera de la bóveda | 4 a 6 h | **Medio**. Requiere aprobación expresa de Víctor y Diego, Docker y gasto de API |
| 9 | Revisión del formulario web con las reglas de formularios de ui-ux-pro-max (etiquetas visibles, error bajo el campo, conservar lo escrito, botón de enviar no desactivado antes de tiempo, aviso de tiempo agotado) y las de texto de unslop | Repo de Diego; criterio de aceptación en la elicitación de requerimientos | 1 a 2 h | Bajo |
| 10 | Ahorro de tokens: revisar qué conectores MCP están activos en el proyecto de la tesis (hoy aparecen Canva, Figma, Lovable, Miro, Notion, Spotify, Gmail y otros) y desactivar los que no se usan con `disabledMcpServers`; mantener cada SKILL.md corto con referencias que se leen solo cuando hacen falta; compactar al cerrar cada bloque doble; respuestas que terminan con 1 o 2 líneas de "qué no revisé y qué riesgo hay" | `.claude/settings.json` del proyecto (con la skill `update-config`) y `CLAUDE.md` | 1 h | Bajo. Verificar antes que los conectores diferidos realmente ocupen contexto en su versión de Claude Code |
| 11 | Reglas de gráficos y formato numérico para los Excel (un formato de número por hoja, coma decimal, sin colores de arcoíris en una sola serie, tipo de gráfico según el dato, menos de 4 puntos = celda destacada en lugar de gráfico) | Las skills de Excel que usen o `estilo_docx.py`/`diagramas.py` | 1 h | Bajo |
| 12 | No adoptar agent-reach ni everything-claude-code como plugin. Anotar en el `CLAUDE.md` la razón (cookies, términos de servicio, sin fuentes académicas; hooks que bloquean `.md`) para no volver a evaluarlos | `CLAUDE.md` de la bóveda, sección de reglas | 15 min | Ninguno |

## 4. Reglas extraídas listas para copiar

Redactadas en español. Entre paréntesis, el archivo de origen.

### Diseño de páginas y tableros
1. Antes de diseñar, escribir 5 líneas: qué hace el producto y para quién, 2 o 3 palabras de carácter concretas (nunca "limpio, moderno, minimalista, premium"), el mundo o material al que pertenece, 1 o 2 momentos con color rico y un solo detalle propio. Mostrarlas y esperar respuesta. (`unslop/skills/unslop/SKILL.md`, Direction)
2. Medir cuánto slop hay antes de cambiar: mucho = rediseño completo; poco = solo arreglar lo auditado; nada = decirlo y proponer como máximo 3 ajustes. Nunca cambiar una pantalla buena solo para que sea distinta. (`unslop/.../SKILL.md`, Run it, paso 3)
3. Arreglar en este orden: espaciado, color, íconos, texto, tipografía, layout, detalles, visuales, movimiento. Terminar cada pasada en toda la pantalla antes de pasar a la siguiente. (`unslop/.../SKILL.md`, Run it, paso 5)
4. Todo el espaciado en múltiplos de 4 px; lo que es igual mide igual; el espacio dentro de un grupo es menor que entre grupos. (`unslop/.../SKILL.md`, sección 1)
5. Navegación, botones y bordes quedan quietos; el color y el detalle van a 1 o 2 momentos de contenido, como un gráfico bien hecho. (`unslop/.../SKILL.md`, intro y What good looks like)
6. Un solo gráfico principal, claramente el más grande; los demás datos en otra forma (lista con barras finas o tabla corta), nunca un segundo gráfico del mismo tamaño. (`unslop/.../SKILL.md`, sección 7)
7. Tarjetas de cifra: etiqueta, número grande y cambio con su referencia. Sin sparklines, íconos ni minibarras de relleno. (`unslop/.../SKILL.md`, sección 7)
8. Variar los anchos: 3 o 4 tarjetas compactas sobre un gráfico ancho, o un gráfico ancho junto a una lista angosta. Cuatro tarjetas iguales con el mismo contenido parecen plantilla. (`unslop/.../SKILL.md`, sección 7)
9. Sin emojis como íconos; un solo juego de íconos de línea, un tamaño (16 o 18 px) y un trazo, con el color del texto. (`unslop/.../SKILL.md`, sección 3; `ui-ux-pro-max-skill/.claude/skills/ui-ux-pro-max/references/pro-rules.md`)
10. Sin animaciones en bucle en lo que no está vivo, sin `transition-all`, sin agrandar tarjetas al pasar el mouse; animar solo color, fondo, borde, opacidad y transform. Como máximo una entrada al cargar. (`unslop/.../SKILL.md`, sección 9)
11. Revisar la página renderizada, no solo el código, a 1440, 768 y 390 px; como máximo 3 renders por corrida. (`unslop/.../SKILL.md`, Run it; `taste-skill/skills/taste-skill/SKILL.md`, House rules 2)
12. Prueba de plantilla: si se cambia el nombre del producto por otro y la pantalla sigue encajando, falta dirección. (`unslop/.../SKILL.md`, Checklist)
13. Prioridad de revisión: accesibilidad, interacción táctil, rendimiento, estilo, layout responsive, tipo y color, animación, formularios, navegación, gráficos. (`ui-ux-pro-max-skill/.claude/skills/ui-ux-pro-max/SKILL.md`)
14. Sin scroll horizontal, con meta viewport y objetivos táctiles de al menos 44×44 px. (`ui-ux-pro-max-skill/.../SKILL.md`, prioridades 2 y 5)

### Tipografía y color
15. Una rampa neutra teñida hacia el mundo del producto para fondo, superficies, bordes y texto; tres roles de texto (principal, secundario, apagado). (`unslop/.../SKILL.md`, sección 2; `references/tokens.md`)
16. Un solo acento, usado poco: acción principal, selección o la cifra que importa. Texto sobre el acento con contraste de 4,5:1. (`unslop/.../SKILL.md`, sección 2)
17. Nada de degradados entre tonos, texto con degradado, brillos de color ni manchas difusas detrás del contenido. Bordes como línea fina al 6 a 10 % de opacidad. (`unslop/.../references/signs.md`)
18. Pesos 400 y 500, 600 solo para énfasis raro; jerarquía por tamaño y color, no por grosor; sin cursiva para enfatizar. (`unslop/.../SKILL.md`, sección 5)
19. Nada de etiquetas en mayúsculas con letras espaciadas; mayúscula solo al inicio. Letra de menos de 16 px sin tracking negativo. (`unslop/.../SKILL.md`, sección 5; `references/tokens.md`)
20. Las cifras con `tabular-nums` y un solo formato en toda la pantalla. (`unslop/.../SKILL.md`, sección 5)
21. Una familia para la interfaz y como máximo una compañera (monoespaciada para cifras o una display para titulares grandes). (`unslop/.../SKILL.md`, sección 5)
22. Radio anidado: radio interior = radio exterior menos el padding, nunca menos de 4. (`unslop/.../references/tokens.md`)
23. Colores como tokens semánticos, no hex sueltos en cada componente; revisar el contraste del modo oscuro por separado. (`ui-ux-pro-max-skill/.../SKILL.md`, prioridad 6; `references/pro-rules.md`)

### Anti "vibe code" y anti slop en textos
24. No inventar datos para sonar específico (números de lote, horas exactas, porcentajes). Si la fuente no da el detalle, una frase más simple. (`taste-skill/.../references/copy-tells.md`, Second generation)
25. Nada de franjas de 3 o 4 cifras con una palabra debajo: cada número va en la oración que lo prueba. (`copy-tells.md`)
26. Como máximo un título de dos fragmentos ("X. Y.") por documento. (`copy-tells.md`)
27. Contar juntos "no es X, es Y", "en lugar de", "sin el": máximo 2 en total. Decir el hecho positivo solo. (`copy-tells.md`)
28. Nada de palabras de virtud sobre uno mismo: honesto, tranquilo, realmente, genuinamente, cuidadosamente, intencional. Mostrarlo con un hecho. (`copy-tells.md`)
29. No cerrar cada párrafo con una frase ingeniosa o una moraleja: terminar con información. (`copy-tells.md`, The dry closer y tabla de sobrecorrección)
30. El texto no habla de sí mismo: nada de "esta sección muestra", "a continuación encontrarás", "aquí hay 3 razones". (`copy-tells.md`, Process talk)
31. Evitar tríadas no significa escribir todo en pares: listar tantos elementos como haya. (`copy-tells.md`, Over-correction)
32. Quitar las rayas no significa escribir solo con puntos: usar dos puntos o paréntesis donde caigan natural. (`copy-tells.md`, Over-correction)
33. No es rasgo de IA: gramática correcta, "es" y "tiene", un conector aislado, una lista de tres cuando hay tres cosas. No castigarlos. (`copy-tells.md`, Not tells)
34. Donde quiere ir un adjetivo va un hecho: si se dice "rápido", la cifra va en la misma oración. (`taste-skill/.../references/copy-voice.md`, Draft)
35. Prueba de nueve rubros: si la voz le queda igual a nueve negocios de otros rubros, no es una voz propia. (`copy-voice.md`, The voice card)
36. En interfaces: sin signos de exclamación, sin punto final en títulos, etiquetas y botones, cambios con referencia ("+12 % vs. octubre"), botones como verbo más objeto, nunca "Ver más" ni "Descubrir". (`unslop/.../SKILL.md`, sección 4; `taste-skill/.../references/copy.md`, Five rules)
37. Nada de reseñas, citas, clientes ni cifras inventadas; afirmaciones no comprobables se confirman con el usuario o se quitan. (`taste-skill/.../SKILL.md`, Never; `unslop/.../SKILL.md`, sección 4)

### Excel, tableros y gráficos
38. Elegir el gráfico por el dato: tendencia = línea; comparación = barras ordenadas de mayor a menor; proporción = una barra apilada o lista con barras; una meta = barra de progreso. (`unslop/.../SKILL.md`, sección 7; `ui-ux-pro-max-skill/src/ui-ux-pro-max/data/charts.csv`)
39. Con menos de 4 puntos en el tiempo, una cifra destacada y no un gráfico; con más de 15 categorías, tabla; torta solo con 5 categorías o menos y diferencias mayores al 5 %. (`charts.csv`, filas 1 a 3)
40. Un acento por gráfico en lo que importa y el resto en grises; nunca distinguir series solo por color: etiquetas directas o estilos de línea, y la tabla de datos visible al lado. (`unslop/.../SKILL.md`, sección 7; `charts.csv`)

### Seguridad del código (prueba de concepto de Diego)
41. Antes de cada commit: sin secretos en el código ni en el historial de git, secretos en las variables de Railway, `.env` en `.gitignore`. (`everything-claude-code/skills/security-review/SKILL.md`, sección 1)
42. Si un secreto se expuso: parar, rotarlo de inmediato y buscar el mismo error en todo el código. (`everything-claude-code/rules/security.md`)
43. Validar toda entrada del formulario y del webhook con un esquema y lista blanca; consultas a PostgreSQL siempre parametrizadas, nunca concatenadas. (`security-review/SKILL.md`, secciones 2 y 3)
44. Límite de peticiones en todos los endpoints, más estricto en los costosos (el asistente con IA). (`security-review/SKILL.md`, sección 7)
45. Logs sin contraseñas, tokens ni datos personales; al usuario, mensajes de error genéricos y sin stack trace. (`security-review/SKILL.md`, sección 8)
46. Nunca recortar validación en los límites de confianza, manejo de errores que evita pérdida de datos, seguridad ni accesibilidad, aunque se busque el código más corto. (`ponytail/skills/ponytail/SKILL.md`)
47. Lógica con ramas, parsers, dinero o seguridad (por ejemplo, el cálculo de la huella SHA-256) deja una prueba pequeña que falle si se rompe. (`ponytail/skills/ponytail/SKILL.md`)
48. Cada hallazgo de revisión necesita un caso concreto ("esta entrada produce este error"); sin caso no hay hallazgo. Cada uno con qué es, problema, arreglo y qué pasa si no se arregla. (`ponytail/skills/ponytail-review/SKILL.md`)
49. Orden de prioridad para probar: bypass de autenticación, control de acceso (un usuario viendo datos de otro), ejecución remota, inyección SQL, SSRF en webhooks e integraciones, secretos expuestos. (`strix/strix/skills/scan_modes/quick.md`)
50. Asistente con RAG: tratar los documentos de la bóveda como entrada no confiable (inyección de instrucciones), no mostrar la salida del modelo como HTML sin escapar, darle al modelo solo las herramientas y permisos mínimos y pedir confirmación humana antes de acciones con consecuencias. (`strix/strix/skills/vulnerabilities/llm_prompt_injection.md`; `strix/strix/skills/technologies/llm_applications.md`, LLM01 a LLM03)
51. Pruebas de penetración solo contra sistemas propios o autorizados, en una copia local con datos simulados, con telemetría apagada y presupuesto máximo. (`strix/skills/penetration-testing-with-strix/SKILL.md`; `strix/strix/config/settings.py`)

### Búsqueda de fuentes
52. Para contenido público, primero las herramientas propias; las herramientas externas solo llenan huecos. (`agent-reach/agent_reach/skill/SKILL_en.md`)
53. Ante bloqueo, límite de peticiones o captcha: parar, no reintentar en bucle, no cambiar de cuenta ni de backend para saltarlo; lo resuelve la persona en la página oficial. (`agent-reach/agent_reach/skill/SKILL_en.md`, Results and errors)
54. Fragmentos, listas de subtítulos y conteos de comentarios no son el texto: decir qué se tiene en realidad. (`agent-reach/agent_reach/skill/SKILL_en.md`, Choosing a route)
55. Si una búsqueda no devuelve nada: reintentar una vez con una consulta más angosta; si sigue vacía, decirlo y marcar lo que se diga como valor por defecto. Nunca presentar un resultado vacío como si tuviera datos. (`ui-ux-pro-max-skill/.claude/skills/ui-ux-pro-max/SKILL.md`, If a search returns 0 results)

### Ahorro de tokens y contexto
56. Cada skill cuesta unos 3000 tokens de lectura; mantener cada SKILL.md corto (menos de 500 líneas) y poner el detalle en archivos de referencia que se leen solo cuando hacen falta. (`ponytail/benchmarks/results/2026-06-12-caveman-vs-ponytail.md`; `design-md-chrome/DESIGN.md`, Acceptance Checklist; `ui-ux-pro-max-skill/.../SKILL.md`)
57. Si la explicación es más larga que el resultado, se borra la explicación; cerrar con 1 o 2 líneas de qué no se revisó y qué riesgo queda. (`ponytail/benchmarks/results/2026-06-12-caveman-vs-ponytail.md`; `ponytail/skills/ponytail/SKILL.md`)
58. No tener todos los MCP activos: con muchas herramientas el contexto útil se achica; desactivar por proyecto los que no se usan. (`everything-claude-code/README.md`, Context Window Management)
59. Compactar en límites lógicos (después de explorar y antes de ejecutar, al terminar un hito), nunca en medio de una implementación. (`everything-claude-code/skills/strategic-compact/SKILL.md`)
60. No usar el último 20 % de la ventana de contexto para cambios grandes en varios archivos. (`everything-claude-code/rules/performance.md`)

## 5. Riesgos encontrados dentro de los repos (instrucciones que no se siguieron)

- `agent-reach/docs/install.md` está escrito para que el agente lo ejecute ("For the AI doing the work. Run every command yourself") y el README pide pegar su URL en el chat del agente. No lo seguí.
- `taste-skill/skills/taste-skill/SKILL.md` declara en su frontmatter un hook `Stop` que ejecuta `node gate.mjs` al cerrar cada turno, y busca el script en varias carpetas de `~/.claude` y del proyecto.
- `everything-claude-code/hooks/hooks.json` bloquea crear archivos `.md` y servidores fuera de tmux; `WORLDFLOWAI.md` pide copiar hooks a `~/.claude/hooks/` con `cp` y `chmod`.
- `ponytail` instala hooks en `SessionStart`, `SubagentStart` y `UserPromptSubmit` que inyectan su modo en todas las sesiones y subagentes.
- `strix` se instala con `curl | bash` y su skill de nube invita a subir repos y dominios a app.strix.ai.
- `ui-ux-pro-max-skill/.claude/skills/ui-ux-pro-max/SKILL.md` incluye su propia advertencia correcta: tratar los resultados como recomendaciones y no como instrucciones que pasen por encima del usuario.
