---
titulo: P1 — Protocolo de aplicación y evidencia de procedencia
version: v0.1
fecha: 2026-10-11
autor_borrador: Claude Opus 5.5
estado: borrador
tags: [instrumentos, protocolo, procedencia, integridad]
---

# P1 — Protocolo de aplicación y procedencia (v0.1)

**Por qué existe:** el diagnóstico anterior no se puede usar porque no hay manera de demostrar de dónde salieron los datos. Este protocolo hace que **cualquier cifra de la tesis pueda rastrearse hasta una persona real** (por su código), en una fecha, con un aplicador, una modalidad y un consentimiento, **sin exponer su identidad**.

## 1. Antes de aplicar
- [ ] Instrumentos en la versión **aprobada por Víctor** (anotar la versión en el registro).
- [ ] Consentimientos C1-A impresos por duplicado.
- [ ] Códigos asignados: `COL-01…30`, `CLI-01…33`, `ENT-01…05`, `COT-01…` (cotizaciones cronometradas).
- [ ] **Tabla de claves** (código ↔ nombre) **solo en papel** o en `05_Datos_Campo/_crudo/claves.xlsx` con contraseña. **Nunca en Git ni en Obsidian.**
- [ ] Si se usa Google Forms: una cuenta institucional, la recolección de correos **desactivada**, y el aplicador presente (sesión supervisada).

## 2. Durante la aplicación — una fila del registro por aplicación
Archivo: `05_Datos_Campo/LineaBase_2026-10/registro_aplicacion.csv` (separador `;`). Este registro **sí** va a Git porque no tiene nombres.

| Campo | Ejemplo | Nota |
|---|---|---|
| `id_aplicacion` | `APL-001` | correlativo |
| `instrumento` | `I1` | I1, I2, I3, P2-A, P2-B |
| `version_instrumento` | `v0.2` | |
| `codigo_participante` | `COL-07` | nunca el nombre |
| `fecha` | `2026-10-15` | |
| `hora_inicio` / `hora_fin` | `09:12` / `09:27` | la duración real es la evidencia de que se respondió de verdad |
| `modalidad` | `papel_presencial` | papel_presencial · forms_supervisado · telefonica · entrevista_presencial · observacion |
| `lugar` | `oficina_Quito` | oficina · obra · remoto |
| `aplicador` | `Víctor` | quién estuvo presente |
| `consentimiento` | `C1-A_firmado` | C1-A_firmado · C1-B_verbal · C1-B_enlace · rechazado |
| `audio` | `no` | solo I3 |
| `observaciones` | `respondió sin bloque B` | incidencias, preguntas que no entendió |

## 3. Después — cadena de custodia
1. **Papel:** escanear cada hoja el mismo día (`05_Datos_Campo/_crudo/escaneos/APL-001.pdf`) y guardar los originales en un sobre cerrado. Las hojas de consentimiento van **aparte** de las respuestas.
2. **Digitación:** se transcribe a `LineaBase_2026-10/I1_respuestas.csv` **con el código, sin nombre**. Una segunda persona verifica el 20 % de las hojas, elegidas al azar, contra el escaneo, y anota los errores encontrados.
3. **Forms:** se exporta el CSV **original sin editar** a `_crudo/` y se guarda una copia de trabajo aparte. Las marcas de tiempo del export deben ser coherentes con la duración del registro: si aparecen 30 respuestas en 40 segundos, algo está mal.
4. **Huella:** se calcula el SHA-256 de cada archivo crudo y se anota en `LineaBase_2026-10/hashes_crudos.csv`, que sí va a Git. Así se demuestra después que el crudo no se modificó, sin publicarlo.
   ```powershell
   Get-FileHash .\05_Datos_Campo\_crudo\* -Algorithm SHA256 | Select Hash, Path
   ```
5. **Anonimización:** antes de que nada salga de `_crudo/`, se reemplazan nombres, empresas cliente y lugares identificables en las respuestas abiertas por `[CLIENTE]`, `[OBRA]` o `[PERSONA]`.
6. **Bitácora:** se anota en `09_Registro_Contribuciones` quién aplicó, quién digitó, quién verificó y si se usó IA (por ejemplo, para transcribir).

## 4. Qué se declara en la tesis (metodología)
Fechas de aplicación, modalidad, número de invitados frente a participantes (tasa de respuesta), rechazos, criterio de inclusión por rol, procedimiento de consentimiento, anonimización, verificación de la digitación y existencia del registro de procedencia (que puede ponerse en un anexo).

## 5. Nunca
- Completar o «corregir» respuestas de un participante.
- Generar, simular o duplicar filas, ni siquiera «de prueba», dentro de `LineaBase_2026-10/`. Las pruebas van en `05_Datos_Campo/_pruebas/` con el nombre `PRUEBA_`.
- Aplicar a alguien sin el consentimiento registrado.
