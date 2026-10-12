---
titulo: Guía de Diego
version: v2.0
fecha: 2026-10-11
tipo: guia
tags: [guia, diego, colaboracion]
---

# Guía de Diego

## 1. El proyecto en un minuto

**Tema aprobado (29-sep-2026):** «Diseño de un sistema de automatización para la gestión comercial en la Constructora Torvesa». Es la tesis de Víctor y tuya en Negocios Digitales (UPS). La tutora es la Ing. Tania Chicaiza.

**El problema:** en Torvesa, cada cotización se hace casi desde cero. Lo que se sabe de cada cliente está en el celular del vendedor y las solicitudes esperan horas o días.

**Lo que vamos a diseñar:** el CRM TEAMSLASH (el sistema de clientes que ustedes hicieron en el proyecto integrador) más tres piezas nuevas:
1. una **bóveda de conocimiento** en Obsidian, con fichas de clientes, plantillas y cotizaciones anteriores;
2. un **asistente de IA** que lee esa bóveda y propone un borrador de cotización;
3. un **registro de lo que pasa con cada cliente**, que no se puede alterar.

Es **solo diseño**. Se prueba durante unos días con el equipo de Torvesa en una **«validación del diseño en operación experimental controlada»**. Nunca decimos «implementado» ni «piloto».

> ⚠️ **Importante:** los datos del «diagnóstico N = 30» del proyecto integrador eran **simulados** (de práctica). No se usan. Los datos reales se levantan en Torvesa si la empresa lo autoriza.

## 2. Quién hace qué

| Víctor | Diego (tú) |
|---|---|
| El documento de tesis, las fuentes y la metodología | **Todo lo técnico y digital** |
| El modelo de negocio y la evaluación financiera (costos, VAN, TIR) | Los procesos dibujados (cómo funciona hoy y cómo funcionará), la arquitectura y la bóveda del sistema |
| Cómo se «vende» la idea (propuesta de valor, pitch) | La búsqueda con IA (RAG), la prueba de concepto y las pruebas |
| Explicarte los conceptos de negocio para que tú los traduzcas a tecnología | Explicarle a Víctor lo técnico en lenguaje simple |

**No tendrás acceso a la bóveda personal de Víctor (bóveda 1).** Más adelante (sprint 3, issue #60), Víctor escribirá un documento con los **patrones** de cómo la organizó (sin datos), para que lo uses al diseñar la bóveda del sistema.

**La bóveda del sistema se construye en el sprint 4 (2–8 nov), no ahora.**

## 3. Tu primera semana (12–18 oct): investigar con fuentes

Esta semana investigas, igual que Víctor: buscas estudios y documentos, los lees y llenas una ficha por cada fuente.

| Día | Qué haces | Dónde | Tiempo |
|---|---|---|---|
| Lun 12 | Aceptar la invitación de GitHub y clonar el repo | Tu PC: sección 6 de esta guía | 1 h |
| Lun 12 | Levantar el buscador RAG (búsqueda con IA en las notas) | Tu PC: `RAG_README.md` | 1 h |
| Mar 13 | Investigar **cómo consolidar bóvedas de conocimiento** (≥5 fuentes) | `02_Fuentes/Tecnologia_IA/` | 1,5 h |
| Mar 13 | Leer el Documento madre y el Glosario | `00_DOCUMENTO_MADRE.pdf` y `Glosario.pdf` (raíz) | 0,5 h |
| Mié 14 | Investigar **arquitecturas RAG para negocio** (≥5 fuentes) | `02_Fuentes/Tecnologia_IA/` | 1,5 h |
| Mié 14 | Escribir un resumen de 1 página para Víctor (bóvedas y RAG) | `02_Fuentes/Tecnologia_IA/2026-10-14_Resumen_Bovedas_RAG.md` | 0,5 h |
| Jue 15 | Cronometrar cotizaciones en Torvesa (**solo si Torvesa autoriza**) | Oficina de Torvesa | 2 h |
| Vie 16 | Revisar solicitudes pasadas, solo fechas y horas (**si autoriza**) | Oficina de Torvesa | 2 h |
| Sáb 17 | Investigar **flujos de información y diseño de procesos (BPMN)** (≥5 fuentes) | `02_Fuentes/Metodologia/` | 1,5 h |
| Sáb 17 | Investigar **CRMs móviles y herramientas existentes, con precios** (≥6 herramientas) | `02_Fuentes/Casos_Estudio/` y `02_Fuentes/Costos_Viabilidad/` | 2 h |
| Dom 18 | Tabular los datos de campo con Víctor (si hubo campo) | `05_Datos_Campo/LineaBase_2026-10/` | 2 h |
| Dom 18 | Resumen de 1 página para Víctor (CRMs y flujos) | `02_Fuentes/Casos_Estudio/2026-10-18_Resumen_CRM_Flujos.md` | 0,5 h |
| Dom 18 | Revisión de la semana con Víctor (más abajo) | Llamada | 1 h |

Si Torvesa **no** autoriza el campo, el jueves y el viernes adelantas la investigación del sábado.

**Cómo buscar fuentes:** con los scripts de búsqueda (`99_Scripts/busqueda/`; la guía de uso es `99_Scripts/busqueda/Guia_Busqueda.pdf`). Cada fuente lleva su ficha, hecha con la plantilla `99_Scripts/plantillas/ficha_fuente.md`. Una fuente está «verificada» solo si la abriste y el dato está ahí, con página.

## 4. Tus tareas de todo el semestre

Todo está, día por día, en **`11_Planificacion/Cronograma_Tesis.xlsx`**, con una hoja por semana (sprint). En GitHub, cada entregable tiene su ficha (*issue*): <https://github.com/l333x/Tesis_Torvesa/issues>

| Semana | Lo principal tuyo |
|---|---|
| S1 · 12–18 oct | Investigar bóvedas, RAG, flujos y CRMs (#54, #55, #56) · campo si Torvesa autoriza (#9) |
| S2 · 19–25 oct | Analizar los datos de campo (#16) · dibujar el proceso actual (AS-IS) (#17) · comparar herramientas (#18) |
| S3 · 26 oct–1 nov | Preparar figuras para la Revisión 1 con la tutora (#21) · leer los patrones de la bóveda de Víctor (#60) |
| S4 · 2–8 nov | Dibujar el proceso con el sistema (TO-BE) (#22) · **construir la bóveda del sistema** (#24) |
| S5 · 9–15 nov | Prueba de concepto: formulario → servidor → bóveda → borrador con IA (#31) · 3 casos de prueba (#32) |
| S6 · 16–22 nov | Revisión 2 con la tutora (#33) · dejar estable la prueba de concepto |
| S7–S8 · 23 nov–6 dic | Validación del diseño en Torvesa (#37) · documentar herramientas, datos, asistente y manual (#38–#42) |
| S9–S10 · 7–20 dic | Medición del «después» (#43) · pruebas (#45) · tesis al 90 % (#47) |
| Ene–feb | Entrega y preparación de la defensa (#50–#53) |

## 5. Conocimiento compartido (para la defensa)

En la defensa el tribunal nos pregunta **a los dos lo mismo**. Por eso:
- **Cada entregable tiene un resumen de 1 página para el otro.** Está como tarea en el cronograma; por ejemplo, el miércoles 14 tu resumen de bóvedas y RAG.
- **Cada domingo en la noche hay revisión de la semana (1 h):** qué hicimos, qué no y qué aprendimos; **20 minutos de «explícame lo tuyo»**; y la planificación de la semana siguiente.
- Víctor te explica los conceptos de negocio con `Conceptos_Negocio.pdf` (raíz del repo). Para cada concepto, ese documento dice qué tendrías que construir tú.

## 6. Primera vez: instalar, iniciar sesión y clonar

1. **Acepta la invitación:** <https://github.com/l333x/Tesis_Torvesa/invitations> → *Accept*. Caduca 7 días después del envío (11-oct).
2. **Instala** (PowerShell): `winget install --id Git.Git -e`, `winget install --id GitHub.cli -e`, `winget install --id Python.Python.3.13 -e`, `winget install --id Obsidian.Obsidian -e`.
3. **Inicia sesión:** `gh auth login --hostname github.com --git-protocol ssh --web`. Genera una clave nueva con tu propia contraseña de clave (passphrase) y autoriza en el navegador hasta ver «Congratulations».
4. **Clona** en una carpeta **fuera de OneDrive**: `gh repo clone l333x/Tesis_Torvesa`.
5. **Abre la carpeta en Obsidian:** *Abrir carpeta como bóveda*.
6. **Prueba:** crea `00_Inbox/hola_diego.md`, haz commit con `S1-10: prueba (closes #10)` y push.

## 7. Reglas

- **Datos personales:** nunca en el repo. Nombres, teléfonos, correos, cédulas, audios y escaneos van a `05_Datos_Campo/_crudo/`, una carpeta que GitHub ignora.
- **Antes de subir datos:** ejecuta `python 99_Scripts/auditoria_pii.py`. Tiene que decir «0 hallazgos».
- **Nombres de archivo:** `AAAA-MM-DD_tema_vX.Y`, por ejemplo `2026-11-04_TO-BE_Proceso1_v0.1.md`.
- **Mensaje de cada commit:** el código de la tarea y su issue, por ejemplo `S1-13: 5 fichas de bóvedas (#54)`.
- **Uso de IA:** si una IA te ayudó, ponlo en el commit (`[IA: Claude]`) y en `09_Registro_Contribuciones`.
- **Nunca** `git push --force`, ni mover o renombrar carpetas de Víctor sin avisar.

## 8. Cómo reportar y a quién preguntar

- **Durante la semana:** marca el estado de tus tareas en el Excel del cronograma y comenta en el issue lo que te bloquee.
- **Domingo antes de las 21:00:** todo subido. A esa hora se genera solo el informe semanal y se actualiza el Documento madre.
- **Pregúntale a Víctor:** lo del negocio, la tutora, Torvesa, las fuentes y la tesis.
- **Decides tú:** lo técnico; avísale a Víctor si cambia el alcance.
- **Ante la duda sobre si algo es dato personal:** trátalo como si lo fuera.
