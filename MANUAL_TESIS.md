---
titulo: "Manual de redacción de la tesis (para la IA)"
version: "0.2"
fecha: 2026-10-13
tipo: manual-ia
tags: [manual, apa7, estructura, redaccion]
---

# Manual de redacción de la tesis (para la IA)

> **Qué es:** las reglas que sigue la IA para **armar, redactar, citar y presentar** la tesis. **No se cita en la tesis.** Es la guía de trabajo.
> **Cuándo se lee:** antes de redactar o revisar **cualquier** parte de un capítulo, de un resumen o de las referencias.
> **Orden de prioridad cuando dos reglas chocan:**
> 1. Lo que diga la tutora (actas en `08_Reuniones_Tutora/`).
> 2. El **Manual de estilo oficial de la carrera (proyecto técnico)**: `02_Fuentes/Formatos_UPS/` (recibido el 13-oct-2026; análisis y contradicciones C1–C8 en `_Analisis_Formatos_UPS.md`).
> 3. La práctica observada en tesis UPS recientes (§2), sobre todo Collaguazo (2026), la tesis real que trae el paquete de formatos.
> 4. APA 7 oficial (apastyle.apa.org).
> 5. Las adaptaciones al español de guías universitarias ecuatorianas (UTPL, ESPE).

---

## 1. Datos fijos del trabajo
Fuente: `01_Borrador_Aprobado/2026-09-29_Diseno_Titulacion_APROBADO.md`.

| Campo | Valor |
|---|---|
| Universidad / carrera | Universidad Politécnica Salesiana · Carrera de **Negocios Digitales** |
| Tipo de trabajo | **Proyecto Técnico** (no «proyecto de investigación» ni «artículo académico») |
| Título | Diseño de un sistema de automatización para la gestión comercial en la Constructora Torvesa |
| Período | Período 69 (septiembre 2026 – febrero 2027) |
| Tutora | Tania Alexandra Chicaiza Villalba |
| Autores | Diego Jhoel Bermeo Torres; Víctor Alexander Segura Heredia |
| Objetivos de aprendizaje (OVA) | 4.1, 4.2, 4.3 · 5.1, 5.3, 5.4 · 6.1, 6.2, 6.3 |
| Título a obtener | Licenciado en Negocios Digitales (así figura en la tesis UPS de la carrera de 2026) |

Reglas de vocabulario que **no se negocian** (ver `CLAUDE.md`):
- **«validación del diseño en operación experimental controlada»**, nunca «piloto» ni «implementado».
- Los datos simulados (N = 30) **no existen** para la tesis.

---

## 2. Estructura del documento

### 2.1 Estructura oficial (Manual de estilo de la carrera, proyecto técnico)
Fuente: `02_Fuentes/Formatos_UPS/MANUAL DE ESTILO – CARRERA DE NEGOCIOS DIGITALES_proyecto_técnico.docx`. El manual se declara **obligatorio**. También se revisaron tesis reales: Collaguazo (2026, Negocios Digitales, proyecto técnico, viene en el paquete), Ordoñez (2026, Negocios Digitales, proyecto de investigación) y Carrión (2024, Computación, artículo).

**Parte pretextual** (números romanos en minúsculas; la portada se cuenta pero no se numera), **en este orden**:

1. **Portada:** «UNIVERSIDAD POLITÉCNICA SALESIANA / SEDE QUITO / CARRERA DE NEGOCIOS DIGITALES», el título en mayúsculas, «Trabajo de titulación previo a la obtención del / Título de Licenciado en Negocios Digitales.», «Autores: NOMBRES EN MAYÚSCULAS», «Tutor: NOMBRE EN MAYÚSCULAS» (la plantilla oficial **no** pone título académico), «Quito – Ecuador» y el año. Plantilla: `portadaTrabajoTitulacion.docx`.
2. **Certificado de responsabilidad y autoría:** firmado por cada autor con su cédula. La plantilla oficial **no trae** la frase de uso de IA que sí aparece en Ordoñez (2026); el manual manda la declaración de IA a los **anexos** (§10).
3. **Certificado de cesión de derechos de autor** a la UPS (nombra la opción «Proyecto Técnico»).
4. **Certificado de dirección:** lo firma la tutora. Usar el texto del esqueleto Word: la plantilla `.odt` trae por error a los estudiantes en el bloque de firma (C6).
5. Dedicatoria y agradecimientos (opcionales).
6. **Índice de contenido**, **índice de tablas** e **índice de figuras**: automáticos, alineados a la izquierda, con puntos guía; incluyen las páginas pretextuales.
7. **Resumen** (una hoja, **≤ 250 palabras**) y **Abstract** (otra hoja, ≤ 250 palabras).
8. **Palabras clave:** de **3 a 5**, justo después del resumen; el rótulo «Palabras claves» va en cursiva y con sangría de 1,27 cm; en minúsculas salvo nombres propios, separadas por comas y **sin punto final**. Lo mismo para *Keywords*.

**Parte textual** (números arábigos desde la Introducción): Introducción → Marco teórico → Metodología → Desarrollo técnico → Evaluación y resultados → Conclusiones y recomendaciones (§2.2).
- La **Introducción** es el primer capítulo y contiene **problema, justificación, objetivos y alcance**. En Collaguazo (2026) aparece como «CAPÍTULO I» y, en la línea siguiente, «INTRODUCCIÓN». Cierra con un párrafo que describe la estructura del documento.
- **Conclusiones** organizadas **por objetivo específico**, y luego las **recomendaciones**.

**Parte postextual:**
- **Referencias** (APA). El manual dice «Referencias bibliográficas»; nunca «Bibliografía» (§6.4).
- **Anexos** numerados («Anexo 1.»): instrumentos, tablas extensas, documentos y la **declaración de uso de IA generativa**.

**Contradicciones del propio material oficial** (detalle en `_Analisis_Formatos_UPS.md` §4): márgenes de 2 cm en las plantillas de portada y certificados (C1); títulos numerados en el esqueleto pero no en la tesis real (C3); el esqueleto «proyecto técnico» usa la estructura del artículo (C4). Se llevan a la tutora (§12).

### 2.2 Estructura propuesta para nuestra tesis (Proyecto Técnico + DSR)
El marco es la investigación en ciencia del diseño (**DSR**). Sus seis actividades (Peffers et al., 2007) deben verse en el documento: (1) identificar el problema, (2) definir los objetivos de la solución, (3) diseñar y desarrollar, (4) demostrar, (5) evaluar y (6) comunicar. Según Gregor y Hevner (2013), en DSR **la descripción del artefacto ocupa el lugar de la sección de resultados** de un trabajo empírico.

| Parte | Contenido | Actividad DSR | Objetivo / OVA | Insumos en la bóveda | Sprint |
|---|---|---|---|---|---|
| **Cap. I · Introducción** | Contexto (IA desde 2021, Ecuador, construcción), Torvesa, problema, pregunta, justificación, objetivos, alcance y delimitación; cierra con la estructura del documento | 1 y 2 | 4.1 | `02_Fuentes/Base_Fuentes_2021-2026`, matriz en `03_Matriz_Objetivos/`, afirmaciones A1–A10 | S2 (el párrafo final, en S9) |
| **Cap. II · Marco teórico** | Antecedentes 2021+, bases teóricas (CRM y CRM móvil, tiempo de respuesta, gestión del conocimiento, RAG), bases legales (LOPDP), discusión crítica y vacíos (A27–A29) | 1 | 4.2 | Fichas verificadas por categoría | S2 |
| **Cap. III · Metodología** | Enfoque mixto con predominio cuantitativo, DSR + Design Thinking + Scrum, población (dos censos), instrumentos, procedimiento, análisis y ética (LOPDP, consentimiento) | marco | 4.3 | `04_Instrumentos/`, decisiones D2 y D4 | S2 |
| **Cap. IV · Desarrollo técnico** — 4.1 Diagnóstico | Proceso actual (AS-IS en BPMN) y línea base **real** (M1–M6) | 1 (evidencia) | 5.1 | `05_Datos_Campo/` (solo datos reales anonimizados) | S7 |
| **Cap. IV · Desarrollo técnico** — 4.2 Diseño del sistema y viabilidad | Requisitos, proceso TO-BE, arquitectura, herramientas, costos, VAN y TIR, riesgos, ley de datos | 3 (artefacto) | 5.3, 5.4, 6.1 | `07_Flujos_Diseno/`, anexo A del borrador | S4 |
| **Cap. V · Evaluación y resultados** | Demostración y evaluación: antes y después en operación experimental controlada, SUS, discusión y limitaciones | 4 y 5 | 6.2, 6.3 | Datos de la validación | S9 |
| **Cap. VI · Conclusiones y recomendaciones** | Una conclusión por objetivo específico; recomendaciones para Torvesa y para futuras investigaciones | 6 | — | — | S9 |
| Anexos | Instrumentos, consentimiento, diccionario de datos, BPMN, costos, declaración de IA | — | — | — | — |

**Encaje con la estructura oficial:** los seis capítulos siguen el orden del manual de estilo (§2.1). El diagnóstico y el diseño comparten el Cap. IV «Desarrollo técnico», igual que en Collaguazo (2026). Su capítulo V, con el costo del proceso manual, la inversión, el ROI, el *payback* y la proyección a 12 meses, sirve de **modelo de estructura** para nuestra viabilidad (§4.2); **no** es fuente de datos. [DECIDIR-TUTORA]: si el diagnóstico puede ser un capítulo propio.

**Regla de coherencia («hilo rojo»):** cada objetivo específico debe aparecer en cuatro sitios. Debe tener (a) su método en el Cap. III, (b) su resultado en el Cap. IV o V y (c) su conclusión. Además, (d) la tabla de la §11.4 lo registra. Si algo no cierra, la IA lo avisa antes de redactar.

---

## 3. Protocolo de la IA para redactar cualquier sección

```
1. UBICAR    → ¿Qué sección es? ¿Qué objetivo, OVA y actividad DSR cubre? (tabla §2.2)
2. INVENTARIO → Listar lo que la sección necesita: afirmaciones, fuentes verificadas,
               datos reales, decisiones tomadas, figuras y tablas.
3. FALTANTES → Comparar con lo que existe en la bóveda. Lo que falta NO se inventa:
               se marca y se pregunta a Víctor (lista corta, priorizada).
4. BORRADOR  → Redactar en .md con los marcadores de §3.1. Una idea por párrafo;
               cada cifra con su cita verificada.
5. VERIFICAR → Lista de verificación §11 (citas↔referencias, cifras, vocabulario, formato).
6. ENTREGAR  → Generar el Word (vX.Y), anotar en la bitácora y en el registro de
               contribuciones (lo que hizo la IA), y esperar la edición de Víctor.
               Nunca sobrescribir una versión que Víctor editó.
```

### 3.1 Marcadores estándar (se usan en los borradores y nunca llegan a la versión final)
| Marcador | Significa | Quién lo resuelve |
|---|---|---|
| `[FALTA-FUENTE: A9 — qué se necesita]` | La afirmación no tiene fuente verificada | Claude busca; Víctor baja el PDF si hace falta |
| `[FALTA-DATO: M1 línea base]` | El dato depende del campo | Campo (Víctor y Diego) |
| `[DECIDIR-TUTORA: …]` | Es una regla que define la tutora | Víctor en la reunión |
| `[DECIDIR-VÍCTOR: …]` | Es una decisión de contenido o de redacción | Víctor |
| `[VERIFICAR-PÁG: autor año]` | La cita existe, pero falta la página | Claude |

La IA **cuenta los marcadores** de cada versión y los reporta: «Cap. I v0.2: 3 FALTA-FUENTE, 1 FALTA-DATO».

### 3.2 Lo que la IA nunca hace
- Inventar autores, años, páginas, DOI, cifras o citas textuales.
- Citar una fuente con `estado: candidata` o `acceso: solo_resumen`.
- Usar datos simulados o del diagnóstico de N = 30.
- Copiar el resumen de una fuente como si fuera paráfrasis.
- Presentar como dos pruebas distintas dos fuentes que usan la misma encuesta (por ejemplo, McKinsey y Stanford 2025).
- Escribir «piloto» o «implementado».

---

## 4. Redacción (APA 7, caps. 4–6, adaptado al español)

- **Claridad y concisión:** frases variadas, sin relleno. No usar párrafos de una sola oración ni párrafos de más de una página. No usar coloquialismos ni jerga sin definir.
- **Persona gramatical:** APA permite la primera persona («realizamos»); la tesis UPS de 2026 usa la forma impersonal («se desarrolla»). **Por defecto, la forma impersonal**, hasta que la tutora decida (§12).
- **Tiempos verbales:** pasado para lo que se hizo (método y resultados); presente para lo que dicen los autores y para las conclusiones vigentes.
- **Voz activa** siempre que se pueda.
- **Siglas:** definirlas la primera vez («Design Science Research [DSR]»), solo si se usan tres veces o más. No definir las de uso común.
- **Números:**
  - En letras del cero al nueve; en cifras del 10 en adelante.
  - **Siempre en cifras:** porcentajes, decimales, dinero, fechas, tiempos, puntajes, estadísticos y unidades.
  - Decimal con **coma** y porcentaje con espacio («7,9 %»), como el BCE; mantenerlo igual en todo el documento.
- **Lenguaje sin sesgos:** personas, no etiquetas («colaboradores», «clientes»). Los participantes se identifican con códigos («C07», «Cl12»), nunca con su nombre (LOPDP).
- **Términos clave:** cursiva solo la primera vez que se definen. Los extranjerismos sin traducir van en cursiva (*lead*, *pipeline*); se prefiere el término en español del `Glosario.md`.

---

## 5. Citas en el texto (APA 7, cap. 8)

| Caso | Parentética | Narrativa |
|---|---|---|
| 1 autor | (Samuelson, 2023) | Samuelson (2023) |
| 2 autores | (Samuelson y Stehn, 2023) | Samuelson y Stehn (2023) |
| 3 o más | (Cathles et al., 2023) | Cathles et al. (2023) |
| Autor institucional | (Banco Central del Ecuador [BCE], 2026) y luego (BCE, 2026) | Banco Central del Ecuador (BCE, 2026) |
| Sin fecha | (Autor, s. f.) | Autor (s. f.) |
| Varias obras | (Cathles et al., 2023; Samuelson y Stehn, 2023): orden alfabético con punto y coma | — |
| Ley | (Ley Orgánica de Protección de Datos Personales [LOPDP], 2021, art. 8) | La LOPDP (2021, art. 8) |

- **«y» o «&»:** APA en inglés usa «&» en las citas parentéticas. Las guías en español usan «y». **Por defecto, «y»** en el texto y en las referencias; confirmar con la tutora (§12).
- **Cita textual de menos de 40 palabras:** entre comillas, con la página: (Salesforce Research, 2024, p. 13). Si no hay páginas, se usa el párrafo o la sección: (McKinsey & Company, 2026, sección «Key takeaways»).
- **Cita textual de 40 palabras o más:** en bloque con sangría de 1,27 cm, sin comillas.
- **Paráfrasis** (lo preferido): la página es opcional, pero **en esta tesis siempre se pone** cuando el dato es una cifra. Así se puede verificar.
- **Fuente secundaria:** solo si no hay acceso al original. Formato: (Oldroyd et al., 2011, como se citó en Koushik, 2024). Solo la fuente leída va a las referencias.
- **No citar en cada oración** cuando el tema y la fuente siguen siendo los mismos; basta con citar una vez por párrafo.
- **Participantes propios** (entrevistas y encuestas en Torvesa): **no son comunicaciones personales**. Se citan sus palabras con un código anónimo («Asesor A3, entrevista, octubre de 2026») y **no van en las referencias**.
- **Comunicación personal** (por ejemplo, un correo de la gerencia de Torvesa): (A. Pérez, comunicación personal, 15 de octubre de 2026). Solo va en el texto, nunca en las referencias.

---

## 6. Lista de referencias (APA 7, caps. 9–10)

### 6.1 Reglas generales
- Título «Referencias», centrado y en negrita, en una página nueva.
- Sangría francesa de 1,27 cm, orden alfabético por el primer apellido y mismo interlineado que el cuerpo.
- Cuatro elementos: **Autor. (Fecha). Título. Fuente.**
- **Autores:** «Apellido, I. I.», separados por comas, con «y» antes del último (o «&», según la decisión de §12). Hasta 20 autores; si hay más, los 19 primeros, «…» y el último.
- **Títulos en tipo oración:** solo la primera palabra y los nombres propios con mayúscula.
  - Van en *cursiva* las obras independientes: libros, informes, tesis, páginas web, videos y conjuntos de datos.
  - Los artículos y capítulos van **sin cursiva**; en ellos va en cursiva la revista o el libro, y el volumen.
- **DOI como enlace** (https://doi.org/...). Si no hay DOI, poner la URL.
  - **Nunca** escribir «Recuperado de», «Obtenido de» ni «Disponible en», ni poner punto después de la URL.
  - «Recuperado el [fecha] de» solo se usa en páginas que cambian y no tienen archivo.
- **Equivalencias en español:** s. f. (sin fecha), et al., Ed./Eds., p./pp., párr., n.º, [Video], [Comunicado de prensa], [Conjunto de datos], [Modelo de lenguaje grande], [Tesis de licenciatura, Universidad X].
- **Cada cita tiene su referencia y cada referencia su cita.** Sin excepción.

### 6.2 Plantillas con ejemplos de nuestra base
Los ejemplos son las referencias reales de las fichas verificadas.

**Artículo de revista con DOI**
`Apellido, I., & Apellido, I. (Año). Título del artículo. *Revista, vol*(núm.), pág–pág. https://doi.org/...`
> Samuelson, O., y Stehn, L. (2023). Digital transformation in construction – a review. *Journal of Information Technology in Construction, 28*, 385–404. https://doi.org/10.36680/j.itcon.2023.020

**Artículo con número de artículo (MDPI, sin páginas)**
> Pérez-Campdesuñer, R., Sánchez-Rodríguez, A., García-Vidal, G., Martínez-Vivar, R., y De Miguel-Guzmán, M. (2025). Artificial intelligence in Ecuadorian SMEs: Drivers and obstacles to adoption. *Information, 16*(6), Artículo 443. https://doi.org/10.3390/info16060443

**Informe de un organismo** (si el autor es también el editor, no se repite)
> Banco Central del Ecuador. (2026). *Informe de evolución de la economía ecuatoriana en 2025 y perspectivas 2026*. https://contenido.bce.fin.ec/documentos/Administracion/EvolEconEcu_2025pers2026.pdf

> OECD. (2025). *AI adoption by small and medium-sized enterprises*. OECD Publishing. [añadir URL]

**Informe con autores individuales**
> Cathles, A., Henríquez, P., y Suaznábar, C. (2023). *Impulsando la transformación digital de la construcción: el caso del BIM en Chile*. Banco Interamericano de Desarrollo. https://doi.org/10.18235/0004973

**Comunicado de prensa**
> Gartner. (2026, 9 de marzo). *Gartner sales survey finds 67% of B2B buyers prefer a rep-free experience* [Comunicado de prensa]. https://www.gartner.com/en/newsroom/press-releases/2026-03-09-...

**Noticia en un sitio de noticias solo digital** (Primicias: título en cursiva y el medio en redonda)
> Revelo, R. (2026, 16 de septiembre). *El peligro de la «Shadow AI»: el 33 % de empleados en Ecuador usa IA personal en el trabajo*. Primicias. https://www.primicias.ec/...

Si el medio es un **periódico** con edición impresa (*El Universo*, *El Comercio*), el título va en redonda y el periódico en *cursiva*.

**Página web con autor institucional**
> McKinsey & Company. (2026, 25 de agosto). *The state of AI: Global survey 2026*. https://www.mckinsey.com/capabilities/operations/our-insights/the-state-of-ai

**Video de YouTube** (el autor es el canal que lo subió y la fecha es la de publicación)
> IBM Technology. (2023, 23 de agosto). *What is retrieval-augmented generation (RAG)?* [Video]. YouTube. https://www.youtube.com/watch?v=T-D1OfcDW1M

**Tesis en un repositorio** (para pregrado, adaptar la descripción entre corchetes)
> Carguachi Yangol, E. J. (2025). *Impacto en las empresas consultoras-constructoras por la implementación y gestión de la tecnología de la información en varias ciudades del Ecuador* [Tesis de maestría, Universidad de Especialidades Espíritu Santo]. Repositorio UEES. https://repositorio.uees.edu.ec/items/bb313b3e-d136-46ee-91a7-07d6fc192a6b

(Confirmar en el PDF si es de maestría.)

**Preprint (arXiv)**
> Brehme, L., Dornauer, B., Ströhle, T., Ehrhart, M., y Breu, R. (2025). *Retrieval-augmented generation in industry: An interview study on use cases, requirements, challenges, and evaluation*. arXiv. https://doi.org/10.48550/arXiv.2508.14066

**Ley ecuatoriana.** APA no tiene un modelo para leyes de fuera de EE. UU. Se usa la adaptación de la guía de la biblioteca de la UTPL (p. 49 de su manual APA 7):
`Entidad que la expide. (Año, día de mes). *Título de la ley*. Registro Oficial [Suplemento] n.º X. URL`
> Asamblea Nacional del Ecuador. (2021, 26 de mayo). *Ley Orgánica de Protección de Datos Personales*. Registro Oficial Quinto Suplemento n.º 459. [URL oficial pendiente]

Cita: (Ley Orgánica de Protección de Datos Personales [LOPDP], 2021, art. X). **Verificar la fecha y el número contra el Registro Oficial antes de usarla (A42).**

**Herramienta de IA** (APA, «AI references», abril de 2026)
> Anthropic. (2026). *Claude* [Modelo de lenguaje grande]. https://claude.ai

Para una conversación concreta compartida: `Empresa. (Año, día de mes). *Título del chat* [Chat de IA generativa]. Herramienta. URL`

**Conjunto de datos propio** (solo si se publica, por ejemplo, la línea base anonimizada)
`Autores. (Año). *Título del conjunto de datos* (Versión X) [Conjunto de datos]. Editor/Repositorio. URL`

**Software** (Obsidian, n8n, etc.)
`Empresa. (Año). *Nombre* (Versión X) [Software]. URL` (**Por confirmar** en la página oficial de APA; no se pudo abrir el 12-oct.)

### 6.3 Si falta un dato (APA, «Missing reference information»)
| Falta | Solución |
|---|---|
| Autor | El título pasa a ocupar el lugar del autor |
| Fecha | «(s. f.)» |
| Título | [Descripción entre corchetes] |
| Autor y fecha | Título. (s. f.). Fuente. |

### 6.4 Contraejemplo: lo que **no** se hace
La tesis UPS de Negocios Digitales de 2026 trae referencias de este tipo:
`Aguilar. (16 de Mayo de 2023). UCE. doi:https://doi.org/...`

Son el formato automático de Word (APA 6): les falta el título y la revista, ponen «Obtenido de», escriben «doi:» antes del enlace y dejan la fecha completa en un artículo. **La IA nunca genera referencias con el botón de Word** ni copia este estilo.

---

## 7. Tablas y figuras (APA 7, cap. 7)

**Partes:**
1. **Número** en negrita: **Tabla 1** o **Figura 1**.
2. Debajo, el **título** en *cursiva*.
3. El cuerpo o la imagen.
4. **Nota.** debajo, si hace falta.

**Tablas:**
- Solo llevan líneas horizontales: arriba, bajo los encabezados y abajo. **Nunca líneas verticales** ni bordes en cada celda.
- La primera columna va alineada a la izquierda; el resto, centrado (a la izquierda si es texto largo).
- Si la tabla pasa de página, se repite el encabezado.

**Figuras:**
- Letra sin serifa de 8 a 14 pt dentro de la imagen; ejes rotulados con sus unidades.
- La leyenda va dentro de la figura.

**Para las dos:**
- Se mencionan en el texto **antes** de que aparezcan («Como muestra la Tabla 3, …») y se numeran en el orden en que se mencionan.
- Deben entenderse solas, sin leer el texto.

**Origen (práctica en español, en la nota):**
- *Nota.* Elaboración propia con datos del levantamiento en Torvesa (octubre de 2026).
- *Nota.* Adaptado de *Título*, por Autor (Año), p. X.
- *Nota.* Tomado de … (si es una copia exacta, puede requerir permiso).

**Diagramas** (BPMN, arquitectura): son figuras. Se hacen con `99_Scripts/gestion/diagramas.py` o con Bizagi, y siempre llevan número, título y nota.

---

## 8. Presentación de datos y resultados

### 8.1 Diseño mixto (APA JARS–Mixed, 2024)
- Nombrar el **tipo de diseño mixto** en el resumen y en el Cap. III; decir qué parte es cuantitativa y cuál cualitativa.
- Plantear **tres tipos de objetivos**: cuantitativos, cualitativos y mixtos (de integración), en el orden del diseño.
- Explicar **cómo se integran** los dos tipos de datos, por ejemplo con una tabla que pone frente a frente la cifra y la cita del participante.
- En los títulos y objetivos, evitar palabras que inclinen el estudio hacia un solo lado, como «explorar» (cualitativo) o «determinantes» (cuantitativo).

### 8.2 Datos cuantitativos (censos, cronometraje, metas M1–M6)
- Siempre se informa: **N** (población), **n** (respuestas válidas por ítem), los datos perdidos y por qué.
- **Porcentajes** con un decimal, junto a la frecuencia: «13 de 30 (43,3 %)». Con N = 30, **un participante vale 3,3 puntos**: no sobreinterpretar.
- **Estadísticos:** media (M) con desviación estándar (DE), o mediana (Mdn) con rango intercuartílico. Con dos decimales y las unidades.
  - Las pruebas **no paramétricas** se informan con el estadístico, el valor p exacto y el tamaño del efecto.
  - Los símbolos van en cursiva (*M*, *DE*, *p*, *n*).
- **SUS:** puntaje de 0 a 100, frente al umbral de 68 (A20). Indicar la versión en español validada que se usó.
- **Tiempos:** en minutos con un decimal; informar la mediana además de la media, porque los tiempos de respuesta suelen ser asimétricos.
- **Antes y después:** misma métrica, mismo procedimiento, mismo período de duración. La diferencia se reporta y las limitaciones se dicen.

### 8.3 Datos cualitativos (entrevistas)
- Explicar cómo se codificó (categorías) y presentar una tabla de categorías con su frecuencia y una cita representativa.
- Citas de participantes: anónimas, cortas y con contexto. Nunca datos que permitan identificar a alguien (LOPDP; datos crudos solo en `05_Datos_Campo/_crudo/`).

### 8.4 Artefacto (Cap. IV §4.2, en lugar de «resultados» en DSR)
- Describir el artefacto con requisitos → diseño → componentes → flujo TO-BE → decisiones y alternativas descartadas (con su porqué).
- Cada requisito debe venir de un hallazgo del diagnóstico (trazabilidad, anexo A.6 del borrador).

---

## 9. Formato del documento final
| Elemento | Manual de estilo oficial (2026) | Tesis real (Collaguazo, 2026) | Valor que se usa |
|---|---|---|---|
| Papel | A4 (29,7 × 21 cm), bond de 75 g, una cara | A4 | **A4** |
| Márgenes | **sup. 3 · inf. 3 · izq. 2,5 · der. 2,5 cm** | 3 / 3 / 2,5 / 2,5 | **3 / 3 / 2,5 / 2,5 cm**. La portada y los certificados de las plantillas vienen en 2 cm (C1) [DECIDIR-TUTORA] |
| Letra del cuerpo | No lo dice | Times New Roman 12 | **Times New Roman 12** [DECIDIR-TUTORA] |
| Interlineado | **1,5** | Doble (no sigue el manual) | **1,5** |
| Espaciado | Doble entre párrafos; simple entre título y párrafo; doble entre párrafo y título, figura o tabla | — | **Como el manual** |
| Alineación | No lo dice | Justificado | **Justificado** [DECIDIR-TUTORA] |
| Sangría | 1,27 cm (solo la menciona para «Palabras claves») | 1,25 cm en la primera línea | **1,27 cm** en la primera línea |
| Títulos | Jerarquía APA: N1 centrado y negrita; N2 a la izquierda y negrita; N3 a la izquierda, negrita y cursiva | «CAPÍTULO I» + nombre del capítulo; subtítulos sin número | **«CAPÍTULO I» + nombre, subtítulos APA sin número** (C3) [DECIDIR-TUTORA] |
| Paginación | Abajo y centrada, **TNR 10**; romanos en minúsculas en las páginas pretextuales; la portada se cuenta pero no se numera; arábigos desde la Introducción | Igual | **Como el manual** |
| Tablas | Rótulo **arriba**, 10 pt, **solo «Tabla N.» en negrita** y el título normal; autoajuste a la ventana; nota de origen al final; referencia cruzada antes de la tabla | «Tabla 1 Título», arriba | **Como el manual**, numeradas de corrido (Tabla 1, 2…) |
| Figuras | «Figura N. Título»; línea en blanco a doble espacio entre la figura y el texto; referencia cruzada antes de la figura | — | **Como el manual** |
| Extensión | **De 60 a 100 páginas sin anexos** | ≈ 80 | **De 60 a 100** |

**Herramienta:** `99_Scripts/gestion/estilo_docx.py` está hecho para los **documentos de trabajo** (con colores) y **no** para la tesis. Para la tesis hace falta una plantilla Word UPS: los requisitos ya están escritos en `02_Fuentes/Formatos_UPS/_Analisis_Formatos_UPS.md` §7 (plantilla, generador de capítulos y verificador de formato). Se construye **solo cuando Víctor lo pida** (la infraestructura está congelada) y después de que la tutora resuelva C1, C3 y C4.

---

## 10. Declaración de uso de IA
Hay dos capas. Las dos se preparan.

1. **UPS:** el manual de estilo oficial pone la **declaración de uso de IA generativa en los anexos**, y la plantilla oficial del certificado de responsabilidad **no** trae la frase de IA. Ordoñez (2026), en cambio, sí la tenía en el certificado: «solo para efectos de mejorar la redacción y puntuación». **Ojo:** en esta tesis la IA también ayudó a buscar fuentes, planificar y analizar, y **no se puede firmar una frase que no es cierta**. Por defecto: un **anexo de declaración de IA** con el contenido APA del punto 2 y el certificado sin la frase. [DECIDIR-TUTORA]: confirmar que el certificado no la necesita.
2. **APA (AI Contribution Statement, guía del 1-sep-2026):** es un párrafo que dice:
   - **fechas** de uso;
   - **qué se le pidió** a la IA (las instrucciones);
   - **en qué secciones** se usó;
   - **qué ideas salieron** de la IA y cómo se incorporaron.

   Puede ir en una página propia después de la portada, en el capítulo de metodología o en una nota. La fuente es `09_Registro_Contribuciones/`: **cada sesión con IA debe dejar su fila** (fecha, tarea, sección y qué se usó). Esa es la «bitácora de IA» que recomienda APA.
3. **Referencia:** Anthropic. (2026). *Claude* [Modelo de lenguaje grande]. https://claude.ai. También se incluye cualquier otra herramienta usada.

---

## 11. Lista de verificación antes de entregar una versión

### 11.1 Contenido
- [ ] La sección cumple su función de la tabla §2.2 y nombra su objetivo.
- [ ] Toda cifra tiene una cita **verificada** (ficha con `estado: verificada` y página).
- [ ] No quedan marcadores sin listar (se reporta su número).
- [ ] No hay datos simulados; no aparecen «piloto» ni «implementado».
- [ ] Las fuentes de antes de 2021 solo aparecen como origen y van acompañadas de una fuente de 2021 en adelante.
- [ ] Las afirmaciones que la evidencia contradice están corregidas, no maquilladas.

### 11.2 Citas y referencias
- [ ] Cada cita tiene su referencia y viceversa (la IA cruza las dos listas y reporta las diferencias).
- [ ] Los años y la ortografía de los autores coinciden entre la cita y la referencia.
- [ ] No aparecen «Recuperado de» ni «Obtenido de»; los DOI van como https://doi.org/.
- [ ] Tipo oración y cursivas correctas; orden alfabético.

### 11.3 Forma
- [ ] Tablas y figuras numeradas, mencionadas antes de aparecer, con nota de origen.
- [ ] Siglas definidas la primera vez.
- [ ] Los números siguen la regla de §4.
- [ ] Los títulos siguen la numeración UPS.

### 11.4 Trazabilidad (se mantiene en `03_Matriz_Objetivos/`)
| Objetivo específico | Método (Cap. III) | Resultado (Cap. IV–V) | Conclusión | Meta M |
|---|---|---|---|---|
| OE1 … | … | … | … | … |

---

## 12. Decisiones pendientes (se llevan a la tutora)
**Resuelto por el manual de estilo oficial (13-oct-2026):** sí existe un instructivo oficial; hoja A4; interlineado de 1,5; resumen y abstract de ≤ 250 palabras con 3 a 5 palabras clave; «Referencias bibliográficas»; la declaración de IA va en los anexos; de 60 a 100 páginas.

**Sigue abierto:**
1. Alineación (justificado o a la izquierda) y letra del cuerpo (el manual no lo dice; por defecto, TNR 12 justificado).
2. «y» o «&» en las citas y referencias; comillas « » o “ ”.
3. Primera persona del plural o forma impersonal.
4. Si el certificado de responsabilidad debe llevar además una frase de uso de IA (§10), y si el anexo de IA puede seguir el formato APA (*AI Contribution Statement*).
5. **C1:** ¿la portada y los certificados van con márgenes de 2 cm (plantilla) o de 3/3/2,5/2,5 (manual)?
6. **C3:** ¿títulos numerados (1.1, 1.1.1) o sin número (tesis real)?
7. **C4:** ¿se respetan los nombres «Desarrollo técnico» y «Evaluación y resultados» del manual, o se aceptan otros nombres como en la tesis real? ¿El diagnóstico puede ser un capítulo propio?
8. El «Anexo 3» (guía APA) que cita el manual no vino en el paquete: pedirlo.

Cuando la tutora decida, se actualiza este manual (v0.3) y se borra el `[DECIDIR-TUTORA]` correspondiente.

---

## 13. De dónde sale este manual (no se cita en la tesis)
- American Psychological Association (2021). *Publication Manual, 7th Edition: Student paper checklist* (PDF oficial, leído el 12-oct-2026).
- American Psychological Association (2022). *Heading levels template: Student paper*.
- American Psychological Association (2026). *AI contribution statement guide* (actualizado el 1-sep-2026).
- APA Style, páginas oficiales consultadas el 12-oct-2026:
  - ejemplos de referencia: informe de organismo, página web, YouTube, comunicado de prensa, periódico, tesis publicada, preprint, IA, conjunto de datos y actas de congreso;
  - información faltante, fuentes secundarias, comunicaciones personales, citas textuales;
  - configuración de tablas y de figuras;
  - JARS–Mixed;
  - blog «Citing generative AI, Part 3» (9-sep-2025).
- Biblioteca UTPL. *Normas APA 7.ª edición* (ejemplos de leyes ecuatorianas, pp. 26–27 y 49–50).
- Tesis UPS revisadas como ejemplo de estructura:
  - Ordoñez Constante (2026), Negocios Digitales, Quito, TTQ3211 (dspace.ups.edu.ec);
  - Carrión Llerena (2024), Computación, Guayaquil, UPS-GT005364.
- Peffers et al. (2007) y Gregor y Hevner (2013, *MIS Quarterly, 37*(2), 337–355) para la estructura DSR. El esquema de Gregor y Hevner se conoce por su resumen; el PDF no se pudo abrir (bloqueo de la editorial). Ambos son candidatos a fuente **citable** del Cap. III (prioridad 2 de la fase 1).
