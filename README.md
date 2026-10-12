# Tesis Torvesa · centro de coordinación

**Diseño de un sistema de automatización para la gestión comercial en la Constructora Torvesa**
Proyecto Técnico · Negocios Digitales · Universidad Politécnica Salesiana (Quito) · Período 69
Autores: **Víctor Segura** (documento, investigación, APA, instrumentos, finanzas, tutora y Torvesa) · **Diego Bermeo** (bóveda del sistema, RAG, flujos, arquitectura, prototipo, pruebas) · Tutora: Ing. Tania Chicaiza

> **Estado (2026-10-11):** fase 0.5 cerrada (infraestructura lista) · arranca S1: fase 1 de fuentes (12–14 oct) y campo (15–16 oct) · escenario de entrega **B (enero)**, a la espera de que la tutora confirme si el 15-dic es fecha dura.

## Enlaces rápidos
| Para… | Ir a |
|---|---|
| Ver qué toca esta semana | [`11_Planificacion/CRONOGRAMA.md`](11_Planificacion/CRONOGRAMA.md) · [issues por milestone](https://github.com/l333x/Tesis_Torvesa/milestones) |
| Empezar (Diego) | [`GUIA_DIEGO.md`](GUIA_DIEGO.md) |
| Reglas de trabajo, Git y conflictos | [`COLABORACION.md`](COLABORACION.md) |
| Último informe de avance | [`11_Planificacion/Informes/`](11_Planificacion/Informes/) |
| Levantar todo después de apagar la PC | [`ARRANQUE.md`](ARRANQUE.md) |
| Buscar en la bóveda (RAG local) | [`RAG_README.md`](RAG_README.md) |
| Quién hizo qué | [`09_Registro_Contribuciones/`](09_Registro_Contribuciones/Registro_Contribuciones.md) |
| El borrador aprobado (solo lectura) | [`01_Borrador_Aprobado/`](01_Borrador_Aprobado/) |

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
