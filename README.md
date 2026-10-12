# Tesis Torvesa · centro de coordinación

**Diseño de un sistema de automatización para la gestión comercial en la Constructora Torvesa**
Proyecto Técnico · Negocios Digitales · Universidad Politécnica Salesiana (Quito) · Período 69
Autores: **Víctor Segura** (documento, investigación, APA, instrumentos, finanzas, tutora y Torvesa) · **Diego Bermeo** (bóveda del sistema, RAG, flujos, arquitectura, prototipo, pruebas) · Tutora: Ing. Tania Chicaiza

> **Estado (2026-10-11):** empieza el sprint 1 (12–18 oct): buscar fuentes, conversar con la tutora y con Torvesa · entrega prevista en **enero (escenario B)**, salvo que la tutora confirme el 15-dic.

## Empieza aquí
| Para… | Abre |
|---|---|
| **Leer todo el proyecto en un solo documento** (se actualiza cada domingo) | [`00_DOCUMENTO_MADRE.pdf`](00_DOCUMENTO_MADRE.pdf) · versión Obsidian: [`00_INICIO.md`](00_INICIO.md) |
| Entender un código o una palabra (A1–A47, M1–M6, OVA, RAG…) | [`Glosario.pdf`](Glosario.pdf) |
| Ver qué toca hoy y marcar avances | [`11_Planificacion/Cronograma_Tesis.xlsx`](11_Planificacion/Cronograma_Tesis.xlsx) · [issues](https://github.com/l333x/Tesis_Torvesa/issues) |
| Empezar (Diego) | [`GUIA_DIEGO.pdf`](GUIA_DIEGO.pdf) |
| Conceptos de negocio explicados | [`Conceptos_Negocio.pdf`](Conceptos_Negocio.pdf) |
| Buscar fuentes con Chrome | [`99_Scripts/busqueda/Guia_Busqueda.pdf`](99_Scripts/busqueda/Guia_Busqueda.pdf) |
| Último informe semanal | [`11_Planificacion/Informes/`](11_Planificacion/Informes/) |
| Reglas de Git y conflictos | [`COLABORACION.md`](COLABORACION.md) |
| Levantar todo después de apagar la PC | [`ARRANQUE.md`](ARRANQUE.md) |

## Qué vive aquí y qué no
**Sí:** lo que trabajamos, decidimos y entregamos; el cronograma; fichas de fuentes; instrumentos; datos **anonimizados**; flujos; capítulos; actas; registro de contribuciones.
**No:** datos crudos o personales (van a `05_Datos_Campo/_crudo/`, ignorado por Git) · documentos con cédulas · la base vectorial (`.rag/`) · archivos pesados que no aportan (versiones intermedias, duplicados).

## Reglas que no se negocian
1. Toda cifra lleva una fuente **verificada** (abierta, con página), en APA 7.
2. Nada de datos personales en el repo: `python 99_Scripts/auditoria_pii.py` antes de cada push con datos.
3. El sistema se presenta como **diseño validado en operación experimental controlada**, nunca como «implementado».
4. Cada entregable se registra en `09_Registro_Contribuciones` (autor, fecha, herramienta de IA).
5. Cada commit menciona su issue: `S1-04: instrumentos v0.2 (#4)` · `closes #4` lo cierra.

## Nombres de archivo
`AAAA-MM-DD_tema_vX.Y.ext`, por ejemplo `2026-10-14_I1_Encuesta_Colaboradores_v0.2.md`.
Excepciones: documentos vivos (`README.md`, `CRONOGRAMA.md`, `Registro_Contribuciones.md`), plantillas (`_Plantilla_*.md`) y fichas de fuentes (`citekey.md`, por ejemplo `oldroyd_2011.md`).

## Carpetas
| | Carpeta | Responsable |
|---|---|---|
| 00 | `00_Inbox` — todo lo nuevo sin clasificar | ambos |
| 01 | `01_Borrador_Aprobado` — diseño aprobado (solo lectura) | nadie |
| 02 | `02_Fuentes` — una ficha por fuente | Víctor |
| 03 | `03_Matriz_Objetivos` — afirmaciones ↔ fuentes ↔ OVA ↔ capítulos | Víctor |
| 04 | `04_Instrumentos` — encuestas, guías, consentimientos, protocolos | Víctor |
| 05 | `05_Datos_Campo` — datos anonimizados | Víctor (campo: ambos) |
| 06 | `06_Capitulos` — borradores versionados | Víctor |
| 07 | `07_Flujos_Diseno` — BPMN, arquitectura, diseño del sistema | Diego |
| 08 | `08_Reuniones_Tutora` — actas | Víctor |
| 09 | `09_Registro_Contribuciones` | ambos |
| 10 | `10_Antecedentes_Propios` — trabajo previo (citar como Bermeo y Segura, 2026) | ambos |
| 11 | `11_Planificacion` — cronograma, planes, informes, reportes | Víctor |
| 99 | `99_Scripts` — RAG, auditoría, informes, sincronización con GitHub | Diego |
