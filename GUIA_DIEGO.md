---
titulo: Guía de Diego
version: v1.0
fecha: 2026-10-11
tipo: sistema
tags: [guia, diego, colaboracion]
---

# Guía de Diego

## 1. El proyecto en 1 minuto

**Tema aprobado (29-sep-2026):** «Diseño de un sistema de automatización para la gestión comercial en la Constructora Torvesa». Es un Proyecto Técnico (DSR) en la carrera de Negocios Digitales de la UPS, con la tutora Ing. Tania Chicaiza.

**El problema:** en Torvesa cada cotización se arma casi desde cero, el historial de cada cliente vive en el teléfono del vendedor y las solicitudes esperan horas o días.

**Lo que diseñamos:** sobre TEAMSLASH (landing → API → PostgreSQL → Slack) se agregan tres componentes:
1. una **bóveda Obsidian** con fichas, plantillas y cotizaciones;
2. un **asistente de IA** que consulta la bóveda y propone borradores de cotización;
3. un **registro de eventos verificable**.

Se valida en una **operación experimental controlada** de 2 semanas (24-nov → 5-dic). **Nunca se dice «implementado».**

**Tu rol:** todo lo técnico y digital: bóveda del sistema, RAG, flujogramas (AS-IS/TO-BE), arquitectura, prueba de concepto, casos de prueba y pruebas.
**Rol de Víctor:** documento de tesis, investigación y fuentes, APA, instrumentos, análisis financiero, y la relación con la tutora y con Torvesa.

> ⚠️ **Importante:** los datos del «diagnóstico N = 30» del proyecto integrador eran **simulados**. No se usan. La línea base real se levanta en campo el **jueves 15 y el viernes 16 de octubre**, y tú estás en el cronometraje y la muestra documental.

## 2. Cómo está organizado el repo

Empieza por el portal [`README.md`](README.md). Tus carpetas:

| Carpeta | Qué haces ahí |
|---|---|
| `07_Flujos_Diseno/` | BPMN AS-IS/TO-BE, arquitectura, modelo de datos, inventario de herramientas |
| `99_Scripts/` | RAG (`rag/`), auditoría PII, sincronización con GitHub e informes (`gestion/`) |
| `05_Datos_Campo/` | análisis de los datos de campo (solo **anonimizados**) |

Las demás carpetas son de Víctor o compartidas. Puedes leer y comentar en todas.

## 3. Tu primera semana, paso a paso

1. **Acepta la invitación:** <https://github.com/l333x/Tesis_Torvesa/invitations> → *Accept*. Caduca a los 7 días del envío (11-oct).
2. **Instala, inicia sesión y clona:** sigue la sección «Primera vez — Diego» de [`COLABORACION.md`](COLABORACION.md):
   - `gh auth login` con **tu propia** clave SSH;
   - `gh repo clone l333x/Tesis_Torvesa` en una carpeta **fuera de OneDrive**;
   - abre la carpeta como bóveda en Obsidian.
3. **Levanta el RAG:** [`RAG_README.md`](RAG_README.md). Comprueba que `rag.py consultar "tiempo de elaboración de cotizaciones"` devuelva resultados.
4. **Commit de prueba:** crea `00_Inbox/hola_diego.md`, haz commit con `S1-10: commit de prueba (closes #10)` y push. Eso cierra tu primer issue.
5. **Prepara el campo** (miércoles 14): lee `04_Instrumentos/2026-10-11_P2_Protocolo_Cronometraje_v0.1.md` y `2026-10-11_P1_Protocolo_Aplicacion_Procedencia_v0.1.md`, e imprime las hojas de cronometraje.
6. **Campo** (jueves 15 y viernes 16): cronometraje P2-A, muestra documental P2-B y apoyo en I2 (clientes). Llena el registro P1 en cada aplicación.
7. **Fin de semana:** tabulación con Víctor. Los datos **crudos** van a `_crudo/`; al repo solo suben los anonimizados, y antes de subir corres la auditoría.
8. **Análisis de la bóveda 1** (#11): Víctor te comparte una copia de lectura de `99_Sistema/` de su Segundo Cerebro (sin las carpetas CRISFE). Anota en `07_Flujos_Diseno/ideas_boveda1.md` qué patrones reutilizar:
   - ingestor con watchdog;
   - enlazador de wikilinks;
   - RAG con exclusiones;
   - plantillas con frontmatter.

## 4. Tus tareas por semana

Cada tarea es un issue. Ciérralo con `closes #n` en el commit; Víctor marca el `[x]` en el cronograma, o lo hace el script de sincronización.

| Semana | Tarea | Issue |
|---|---|---|
| S1 · 12–18 oct | Campo: I2 clientes + cronometraje P2-A + muestra P2-B | [#9](https://github.com/l333x/Tesis_Torvesa/issues/9) |
| | Aceptar la invitación, clonar y levantar el RAG | [#10](https://github.com/l333x/Tesis_Torvesa/issues/10) |
| | Analizar la bóveda 1 y extraer ideas | [#11](https://github.com/l333x/Tesis_Torvesa/issues/11) |
| | Tabulación y consolidación (con Víctor) | [#12](https://github.com/l333x/Tesis_Torvesa/issues/12) |
| S2 · 19–25 oct | Análisis descriptivo de los datos de campo | [#16](https://github.com/l333x/Tesis_Torvesa/issues/16) |
| | Mapa del proceso AS-IS (BPMN) | [#17](https://github.com/l333x/Tesis_Torvesa/issues/17) |
| | Inventario de herramientas candidatas con criterios | [#18](https://github.com/l333x/Tesis_Torvesa/issues/18) |
| S3 · 26–30 oct | AS-IS y datos listos para la Revisión 1 | [#21](https://github.com/l333x/Tesis_Torvesa/issues/21) |
| S4 · 2–8 nov | Flujogramas TO-BE (2–4 nov) | [#22](https://github.com/l333x/Tesis_Torvesa/issues/22) |
| | Levantar la bóveda del sistema desde los flujos aprobados (5–8 nov) | [#24](https://github.com/l333x/Tesis_Torvesa/issues/24) |
| S5 · 9–15 nov | Prueba de concepto: front conversacional → back → bóveda | [#31](https://github.com/l333x/Tesis_Torvesa/issues/31) |
| | Diseño de los 3 casos de prueba | [#32](https://github.com/l333x/Tesis_Torvesa/issues/32) |
| S6 · 16–22 nov | Revisión 2: presentar diseño, flujos y datos (con Víctor) | [#33](https://github.com/l333x/Tesis_Torvesa/issues/33) |
| S7 · 23–29 nov | Incorporar observaciones (con Víctor) · arrancar la validación del diseño en operación experimental controlada el 24-nov | [#35](https://github.com/l333x/Tesis_Torvesa/issues/35) · [#37](https://github.com/l333x/Tesis_Torvesa/issues/37) |
| S8 · 30 nov–6 dic | Herramientas elegidas y descartadas · modelo de datos · plantillas + spec del asistente · casos de prueba · manual | [#38](https://github.com/l333x/Tesis_Torvesa/issues/38) · [#39](https://github.com/l333x/Tesis_Torvesa/issues/39) · [#40](https://github.com/l333x/Tesis_Torvesa/issues/40) · [#41](https://github.com/l333x/Tesis_Torvesa/issues/41) · [#42](https://github.com/l333x/Tesis_Torvesa/issues/42) |
| S9 · 7–13 dic | Medición post (con Víctor) · pruebas de uso y de carga | [#43](https://github.com/l333x/Tesis_Torvesa/issues/43) · [#45](https://github.com/l333x/Tesis_Torvesa/issues/45) |
| S10 · 14–20 dic | Hito del 90 % (con Víctor) | [#47](https://github.com/l333x/Tesis_Torvesa/issues/47) |
| Ene–feb | Entrega, resumen de contribuciones, simulacros, defensa | [#50](https://github.com/l333x/Tesis_Torvesa/issues/50) · [#51](https://github.com/l333x/Tesis_Torvesa/issues/51) · [#52](https://github.com/l333x/Tesis_Torvesa/issues/52) · [#53](https://github.com/l333x/Tesis_Torvesa/issues/53) |

**Dependencias que te afectan:**
- No levantes la bóveda del sistema (#24) sin los flujos TO-BE **aprobados** por Víctor (#22 → S4-02).
- La PoC (#31) es requisito de la validación del diseño en operación experimental controlada (#37).

## 5. Reglas

- **Datos personales:** nunca en el repo. Nombres, teléfonos, correos, cédulas, audios y escaneos van a `05_Datos_Campo/_crudo/`, que Git ignora.
- **Antes de cada push con datos:**
  ```powershell
  <tu-venv>\Scripts\python.exe 99_Scripts\auditoria_pii.py    # debe decir: 0 hallazgos
  ```
- **Nombres de archivo:** `AAAA-MM-DD_tema_vX.Y.ext`, por ejemplo `2026-11-04_TO-BE_Proceso1_v0.1.md`.
- **Commits:** `ID: qué hiciste (#n)`, por ejemplo `S2-05: AS-IS en Mermaid (#17)`. Con `closes #n` se cierra el issue.
- **Uso de IA:** si una herramienta de IA te ayudó, ponlo en el commit (`[IA: Claude]`) y en `09_Registro_Contribuciones`. La tesis tiene que declararlo.
- **Nunca** `git push --force`, ni mover o renombrar carpetas de Víctor sin avisar.
- Ejemplos con clientes: siempre ficticios o codificados (`CLI-0001`), nunca reales.

## 6. Cómo reportar avances

1. **Durante la semana:** mueve tus issues en el tablero (Por hacer → En curso → En revisión → Hecho) y comenta en el issue lo que bloquee.
2. **Al cerrar un entregable:** `closes #n` en el commit + una fila en `09_Registro_Contribuciones/Registro_Contribuciones.md`.
3. **Domingo, antes de las 21:00:** todo lo de la semana tiene que estar en `main`. A esa hora se genera el informe automático de avance (commits por autor, tareas cerradas y pendientes).
4. **Bloqueos urgentes:** WhatsApp a Víctor, y luego deja el registro en el issue.

## 7. A quién preguntar qué

| Tema | Pregunta a |
|---|---|
| Qué dice el diseño aprobado, alcance, metas, tutora, Torvesa, permisos | Víctor |
| Fuentes, APA, instrumentos, consentimientos | Víctor |
| Git, RAG, scripts, bóveda del sistema, flujos, PoC | tú decides; consulta a Víctor si cambia el alcance |
| Datos de campo: ¿esto es dato personal? | ante la duda, **es**: va a `_crudo/` y se le pregunta a Víctor |
| Algo del sistema de la bóveda (lanzadores, respaldos) | `ARRANQUE.md` |
