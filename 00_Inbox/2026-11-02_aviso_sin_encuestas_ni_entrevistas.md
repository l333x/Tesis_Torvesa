---
titulo: Aviso para Víctor — no se recogen datos de personas (encuestas, entrevistas ni nada parecido)
fecha: 2026-11-02
autor: Diego Bermeo
ia: Claude (Claude Code)
tipo: cambio de plan (propuesta; decide Víctor)
tags: [diego, metodologia, campo, instrumentos, cambio-de-plan]
---

# No vamos a recoger datos de personas

> [!danger] Qué pasó
> Según la **directora de carrera**, sacar información de personas con encuestas, entrevistas o técnicas parecidas lleva a **otro proceso de autorización**, que tarda más. Por eso **recomiendo no hacerlo**: el plazo (documento final el 4-ene-2027) no aguanta ese trámite. Me lo dijo a mí, Diego; lo anoto el 2-nov-2026.

## Qué queda fuera y qué queda
- **Queda fuera todo lo que recoge datos de personas:**
  - encuestas a colaboradores (I1) y a clientes (I2);
  - entrevistas (I3);
  - observación con cronómetro de quien cotiza (P2-A);
  - taller de validación con la gerencia y el equipo (SES-11);
  - cuestionario SUS al final de la validación (M6).
- **Queda lo que no recoge datos de personas,** siempre que la empresa lo autorice:
  - **documentos de la empresa:** la muestra de solicitudes de los últimos 3 meses, solo fechas y horas (P2-B);
  - **datos de la empresa:** colaboradores, cartera, tipos de obra y ventas 2025;
  - **registros del propio sistema** durante la validación (horas, estados, eventos).

## Qué se cae y qué propongo en su lugar

| Meta o pieza | Hoy se mide con | Propuesta sin datos de personas |
|---|---|---|
| **M1** (respuesta en < 15 min) | Muestra documental (P2-B) y registro del sistema | **Igual**: muestra documental (solo fechas y horas) y registros del sistema durante la validación |
| **M2** (cotización con IA, más rápida) | Cronometrar a quien cotiza (P2-A) | **Casos de prueba cronometrados por nosotros dos** (S5-05 y S8-04): la misma cotización con y sin asistente. La referencia de «hoy» sale del antecedente, marcada como hipótesis |
| **M3** (menos clientes perdidos) | Muestra documental y registro | Igual que M1 |
| **M4** (encontrar el historial de un cliente ajeno) | Prueba de recuperación con vendedores e I1 | **Prueba de recuperación hecha por el equipo** sobre la bóveda de ejemplo (datos ficticios), con y sin la bóveda |
| **M5** (detectar alteraciones) | Prueba técnica | **Sin cambio** |
| **M6** (SUS ≥ 68) | Cuestionario SUS a usuarios | **Evaluación heurística** del diseño por el equipo, con una lista reconocida de principios de usabilidad [FALTA-FUENTE]. Se pierde el número SUS: hay que reformular la meta |
| **AS-IS** (validar el proceso actual) | Entrevistas I3 | Contrastarlo con la muestra documental |
| **Requerimientos, iteración 2** | Entrevistas, encuestas y taller | Documentos, análisis de herramientas, modelado y prototipo. La iteración 1 (censo n = 5 del proyecto integrador) ya está hecha y se cita como antecedente |
| **Design Thinking (empatía)** | Encuestas y entrevistas | El censo del proyecto integrador y los documentos |
| **Enfoque mixto** (Cap. III) | Las entrevistas y las preguntas abiertas son la parte cualitativa | Queda **cuantitativo**, con datos del sistema, de documentos y de pruebas. Víctor decide cómo se describe |

## Qué hay que cambiar (cada quien lo suyo)
- **Víctor:**
  - Cap. III: enfoque, población, instrumentos, procedimiento y análisis;
  - instrumentos: I1, I2, I3, C1 y P2-A pasan a «no se usan»;
  - cronograma: quitar o reprogramar S1-09, S1-12, S2-04, S4-T16, S4-T17 y la medición «después» con encuestas (S9-01);
  - matriz: las afirmaciones «de campo».
- **Diego (con su IA), cuando Víctor apruebe el cambio:**
  - elicitación v0.2: quitar SES-06 a SES-11 y ajustar las secciones 3 y 12;
  - AS-IS, TO-BE y bóveda: cambiar «por validar en campo» por «por validar con documentos»;
  - casos de prueba (S5-05): agregar M2, M4 y la evaluación heurística.
- **Correo a Torvesa:** hay una versión nueva en `tesis-torvesa/Correo_Torvesa_2026-11-02.txt`, fuera del repositorio. Ya no pide encuestas, entrevistas ni observación: solo la muestra documental y los datos de la empresa.

## Lo bueno
- El diseño (AS-IS, TO-BE, bóveda, casos de uso) **no depende** de las encuestas: ya está hecho con documentos.
- Deja de depender de que Torvesa autorice el campo. Esa era la **ruta crítica** del cronograma.
- Las metas M2, M4 y M5 pasan a medirse con pruebas que controlamos nosotros.
