---
tipo: analisis-formato
fecha: 2026-10-13
fuente: formato_documento final Tesis.zip (descargado por Víctor el 13-oct-2026, carpeta de la carrera)
estado: borrador para revisión de Víctor; las diferencias con MANUAL_TESIS.md aún NO se aplican
---

# Formatos oficiales UPS — Negocios Digitales: análisis y brechas

## 1. Qué hay en esta carpeta

| Archivo | Qué es | Uso para nosotros |
|---|---|---|
| `MANUAL DE ESTILO – …_proyecto_técnico.docx` | **Norma oficial** de la carrera para el informe final de proyecto técnico. Se declara «de carácter obligatorio». | **Fuente de verdad del formato.** |
| `MANUAL DE ESTILO – …_articulo.docx` | Igual, para la opción artículo académico. Solo cambia la estructura textual (ver §3). | Referencia; no aplica si la opción es proyecto técnico. |
| `ejemploInformeTesis.docx` / `…Articulo.docx` | Esqueleto de ejemplo (Bitcoin, Quito 2025) con datos ficticios. | Muestra de portada, certificados, resumen y numeración. Tiene contradicciones (§4). |
| `EjemploInformeFinal.docx` | **Tesis real aprobada**: Collaguazo (2026), *Sistema automático de alertas y seguimiento de vencimientos… en Menatics*, proyecto técnico, Quito, enero de 2026. | **El mejor modelo**: automatización comercial, Scrum, costo-beneficio, ROI y *payback*. Ver §5. |
| `portadaTrabajoTitulacion.docx`, `portadaTitulacionNG.odt` | Portada (mismo texto en Word y LibreOffice). | Plantilla de portada. |
| `CertificadoResponsabilidadND.odt`, `CertificadoCesionDerechosND.odt`, `certificadoDireccion.odt` | Los tres certificados de la parte pretextual. | Plantillas para llenar al final. `certificadoDireccion.odt` trae un error (§4). |

⚠️ **Datos personales:** los ejemplos traen números de cédula. Los de Bitcoin parecen ficticios; los de `EjemploInformeFinal.docx` son de personas reales (autor y tutor). Antes de subir esta carpeta a GitHub, decidir si se excluye ese archivo (ver §8).

## 2. Lo que el manual oficial fija (proyecto técnico)

### 2.1 Orden pretextual (paginación romana en minúsculas)
1. Portada (se cuenta pero no se numera)
2. Certificado de responsabilidad y autoría
3. Certificado de cesión de derechos de autor a la UPS
4. Certificado de dirección del trabajo de titulación (lo firma la tutora)
5. Dedicatoria y agradecimientos (opcional)
6. Índice de contenido
7. Índice de tablas
8. Índice de figuras
9. **Resumen:** una hoja, **máximo 250 palabras**
10. **Abstract:** otra hoja, máximo 250 palabras
11. **Palabras clave:** de **3 a 5**, justo después del resumen; el rótulo «Palabras claves» va en cursiva y con sangría de 1,27 cm; en minúsculas (salvo nombres propios), separadas por comas y **sin punto final**

### 2.2 Estructura textual (paginación arábiga desde la Introducción)
1. **Introducción:** problema, justificación, objetivos y alcance
2. **Marco teórico**
3. **Metodología**
4. **Desarrollo técnico**
5. **Evaluación y resultados**
6. **Conclusiones y recomendaciones**

### 2.3 Estructura postextual
- **Referencias bibliográficas** en APA (el manual remite a un «Anexo 3» de APA que **no vino en el zip**).
- **Anexos**, que incluyen la **declaración de uso de herramientas de IA generativa** (el manual nombra Gemini, ChatGPT y DeepSeek).

### 2.4 Formato

| Elemento | Norma oficial |
|---|---|
| Papel | A4 (29,7 × 21 cm), bond de 75 g, una sola cara |
| Márgenes | **superior 3 cm, inferior 3 cm, izquierdo 2,5 cm, derecho 2,5 cm** |
| Interlineado | **1,5** |
| Espaciado | doble entre párrafos; simple entre título y párrafo; doble entre párrafo y título, figura o tabla |
| Extensión | **mínimo 60 y máximo 100 páginas**, sin contar anexos |
| Numeración | abajo y centrada, **Times New Roman 10**; romanos en minúsculas en las páginas pretextuales (se incluyen en el índice); arábigos desde la Introducción |
| Tablas | rótulo **arriba**, tamaño 10, **solo «Tabla N.» en negrita** y el título normal; tabla autoajustada a la ventana; fuente o nota al final si hace falta; **referencia cruzada en el texto antes de que aparezca** |
| Figuras | rótulo «Figura N. Título»; una línea en blanco a doble espacio entre la figura y el texto; referencia cruzada antes de que aparezca |
| Títulos (APA 7) | nivel 1 centrado y en negrita; nivel 2 a la izquierda y en negrita; nivel 3 a la izquierda en negrita y cursiva |
| Índice | automático, alineado a la izquierda, con puntos guía hasta el número de página; incluye los elementos pretextuales |

**Lo que el manual NO dice:** tipo y tamaño de letra del cuerpo, alineación (justificado o a la izquierda), sangría de primera línea, si los títulos llevan números (1.1, 1.1.1), persona gramatical, comillas, «y» o «&».
→ Valores observados en la tesis real (§5): **Times New Roman 12, justificado, sangría de 1,25 cm en la primera línea**.

## 3. Proyecto técnico o artículo
Los dos manuales son idénticos salvo la estructura textual:
- **Proyecto técnico:** … Desarrollo técnico → **Evaluación y resultados** → Conclusiones.
- **Artículo:** … **Desarrollo/Resultados** → **Discusión** → Conclusiones.

El borrador y `MANUAL_TESIS.md` asumen **proyecto técnico**, lo que coincide con el certificado de dirección («bajo la opción Proyecto Técnico»). [DECIDIR-TUTORA]: confirmar.

## 4. Contradicciones dentro del propio material (no las resolvemos nosotros)

| # | Contradicción | Dónde | Qué hacemos |
|---|---|---|---|
| C1 | El manual pide márgenes de 3/3/2,5/2,5, pero el archivo del manual está en 2,54 y las plantillas de portada y certificados están en 2 cm. | Manual, portada, certificados | Seguimos el **texto del manual** (3/3/2,5/2,5), igual que la tesis real. Preguntar si la portada y los certificados pueden ir a 2 cm. |
| C2 | El manual pide interlineado de 1,5, pero la tesis real usa **doble** en el cuerpo. | `EjemploInformeFinal.docx` | Seguimos el manual (1,5). |
| C3 | El esqueleto numera los títulos («1.1 Problema», «Tabla 2.1», «Figura 2.1»); la tesis real **no los numera** («CAPÍTULO I / INTRODUCCIÓN», subtítulos sin número, «Tabla 1» corrida). | Esqueleto o tesis real | [DECIDIR-TUTORA]. Por defecto, como la tesis real: «CAPÍTULO I» + nombre, subtítulos APA sin número y tablas y figuras numeradas de corrido. |
| C4 | El esqueleto «proyecto técnico» usa la estructura del **artículo** (Desarrollo/Resultados + Discusión). La tesis real usa I Introducción, II Marco teórico, III Metodología, IV Desarrollo del sistema, V Discusión (costos, ROI, *payback*), VI Conclusiones. | Esqueleto o tesis real | Seguir el **manual** (§2.2) y preguntar si «Evaluación y resultados» puede llamarse como en la tesis real. |
| C5 | En el esqueleto, el resumen trae 8 palabras clave con mayúscula inicial y punto final. | Esqueleto | Seguir el manual: de 3 a 5, minúsculas, sin punto. |
| C6 | En `certificadoDireccion.odt`, el bloque de firma trae a **los estudiantes**, cuando debería traer a **la tutora**. En el esqueleto Word está bien. | `certificadoDireccion.odt` | Usar el texto del esqueleto Word. |
| C7 | El certificado de cesión dice «Licenciados» aunque haya un solo autor. | Plantilla de cesión | En nuestro caso son dos autores, así que el plural está bien. |
| C8 | Esta plantilla de **responsabilidad y autoría NO trae la frase de uso de IA** que vimos en Ordoñez (2026). El manual la manda a los **anexos**. | Certificado y manual | Resuelve en parte `MANUAL_TESIS.md` §10: la declaración va en un anexo. Falta confirmar si el certificado también la lleva. |

## 5. La tesis real de Menatics (Collaguazo, 2026) como modelo
**Por qué importa:** es casi nuestro mismo tipo de proyecto (automatizar la gestión comercial de una empresa ecuatoriana) y está aprobada en la misma carrera.
- **Capítulos:** I Introducción (problemática, justificación, objetivos, alcance) · II Marco teórico (contexto, leyes, metodología ágil, herramientas) · III Metodología (cronograma de *sprints*, roles Scrum, *product backlog*, detalle por *sprint*) · IV Desarrollo del sistema (despliegue, modelo de datos, mapa navegacional, prototipo, desarrollo por *sprint*) · V Discusión (situación actual, costo del proceso manual, costo de la herramienta, antes y después, ROI y *payback*) · VI Conclusiones.
- **Anexos:** informe de actividades, especificación de requisitos según ISO/IEC/IEEE 29148:2018 y prototipo en Figma.
- **Formato:** Times New Roman 12, justificado, sangría de primera línea de 1,25 cm, márgenes 3/3/2,5/2,5, rótulo de tabla arriba («Tabla 1 Cronograma de los Sprints»), índices automáticos de tablas y figuras.
- **Lo que NO se copia:**
  - dice «implementación del prototipo»; nosotros decimos «validación del diseño en operación experimental controlada»;
  - las referencias tienen pocas fuentes académicas (mucha documentación de empresas, IBM, GoDaddy) y una de 2001;
  - el capítulo III dice «MEDOTOLOGÍA» (errata).
- **Lo que sí sirve:** su capítulo V (costo del proceso manual en horas por costo por hora con beneficios de ley; ROI; *payback*; proyección a 12 meses) es justo el tipo de análisis de viabilidad que va en nuestro capítulo de diseño y viabilidad (VAN y TIR). La usamos como **referencia de estructura**, no como fuente de datos.

## 6. Brechas con `MANUAL_TESIS.md` (propuesta de cambios, NO aplicada)

| § de MANUAL_TESIS | Dice hoy | Debe decir según la norma oficial |
|---|---|---|
| §2.1 punto 1 | «tutor (con título académico)» | La portada oficial pone «Tutor: NOMBRE EN MAYÚSCULAS», sin título académico. |
| §2.1 punto 7 | Resumen ¿350 palabras? «verificar» | **≤ 250** palabras de resumen y ≤ 250 de abstract, en hojas separadas; **3 a 5** palabras clave. |
| §2.1 punto 8 | «Introducción sin numeración» | La Introducción es la **primera sección textual** y contiene problema, justificación, objetivos y alcance; en la tesis real es el «CAPÍTULO I – INTRODUCCIÓN». |
| §2.1, §2.2 | Siete capítulos propios (I Problema … VI Validación) | Encajar en los seis apartados oficiales: **I Introducción** (= nuestro Cap. I) · **II Marco teórico** · **III Metodología** · **IV Desarrollo técnico** (= nuestro diagnóstico AS-IS + diseño TO-BE + viabilidad) · **V Evaluación y resultados** (= validación) · **VI Conclusiones y recomendaciones**. La tabla DSR no cambia; solo se reagrupan los capítulos. [DECIDIR-TUTORA]: si el diagnóstico puede ser un capítulo propio. |
| §2.1, §9 | 2,54 cm | **3 / 3 / 2,5 / 2,5 cm** |
| §9 | Interlineado 1,5 [DECIDIR-TUTORA] | **1,5** (resuelto) + espaciado doble entre párrafos |
| §9 | Paginación romana en preliminares | Confirmado: **romanos en minúsculas**, la portada no se numera; TNR 10, abajo y centrado. |
| §9 | Tablas y figuras «APA» (número en negrita y título en cursiva en otra línea) | **«Tabla N.» en negrita + título normal en la misma línea, arriba, tamaño 10**. |
| §9 | Títulos «numerados como la UPS» | El manual pide la jerarquía APA (centrado y negrita / izquierda y negrita / izquierda, negrita y cursiva); la numeración es una contradicción abierta (C3). |
| §9 (nuevo) | — | **Extensión: de 60 a 100 páginas sin anexos.** |
| §10 | Declaración de IA en el certificado [DECIDIR-TUTORA] | El manual la pone **en los anexos**. Se mantiene el *AI Contribution Statement* de APA como contenido de ese anexo. |
| §12 | Siete preguntas para la tutora | Quedan resueltas la 1 (sí hay manual oficial), la 2 (A4, 1,5; la alineación sigue abierta), la 5 (250 palabras, 3 a 5 palabras clave) y, en parte, la 6 (anexo). Se agregan C1, C3 y C4 de este documento. |

## 7. Requisitos para la futura plantilla o *skill* de formato
Solo es una especificación, porque la infraestructura está congelada. Se construye cuando Víctor lo pida y la tutora confirme C1, C3 y C4.

1. **`plantilla_tesis.docx`**, con secciones separadas: (a) portada sin número; (b) pretextuales con números romanos en minúsculas; (c) cuerpo con arábigos desde 1 en la Introducción.
2. **Estilos con nombre:** Normal (TNR 12, 1,5, justificado y sangría de 1,25 cm, por confirmar), Título 1, 2 y 3 según APA; «Rótulo tabla» y «Rótulo figura» (10 pt, número en negrita); Bibliografía con sangría francesa de 1,27 cm; pie de página con campo PAGE en TNR 10.
3. **Campos automáticos:** índice de contenido con puntos guía, índice de tablas, índice de figuras y referencias cruzadas.
4. **Generador `.md` → `.docx`:** lee los capítulos de `06_Capitulos/` y vuelca el contenido en la plantilla. Sería una herramienta aparte de `estilo_docx.py`, que es solo para documentos de trabajo.
5. **Verificador de formato**, que amplía la lista de `MANUAL_TESIS.md` §11.3:
   - número de palabras del resumen y del abstract (≤ 250);
   - de 3 a 5 palabras clave sin punto final;
   - páginas sin anexos (de 60 a 100);
   - cada «Tabla N» o «Figura N» mencionada antes de aparecer;
   - márgenes y tamaño de página;
   - que no aparezcan «piloto» ni «implementado»;
   - que cada cita tenga su referencia.
6. **Certificados:** se llenan al final con los datos de los autores, que **no** se guardan en la bóveda pública (las cédulas solo en `05_Datos_Campo/_crudo/` o fuera del repositorio).

## 8. Pendientes de Víctor
- [ ] Aprobar que se apliquen los cambios de la §6 en `MANUAL_TESIS.md` (v0.2).
- [ ] Decidir si `02_Fuentes/Formatos_UPS/` se sube a GitHub o se agrega a `.gitignore` (por las cédulas reales de `EjemploInformeFinal.docx`). Propuesta: subir los manuales y las plantillas y excluir `EjemploInformeFinal.docx`.
- [ ] Conseguir el «Anexo 3» (guía APA) que cita el manual y no vino en el zip.
- [ ] Llevar a la tutora: C1, C3, C4, la alineación y la letra del cuerpo, y si el diagnóstico puede ser un capítulo propio.
