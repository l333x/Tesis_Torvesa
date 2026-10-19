---
titulo: Capítulo I (Introducción) en 1 página — para Diego
fecha: 2026-10-19
autor_borrador: Claude Opus 5.5 (borrador; Víctor lo revisa antes de enviarlo)
tarea: "S2-T13 (#13), adelantada del 24-oct"
para: Diego
base: "06_Capitulos/2026-10-19_Cap1_Introduccion_p1_v0.1 y _p2_v0.1"
tags: [resumen, capitulo1]
---

# El capítulo I en 1 página

## Qué dice
1. **Contexto:** la IA crece en las empresas grandes (78 %), pero poco en las pequeñas (11,9 % en la OCDE). La construcción es de los sectores menos digitalizados, y en Ecuador sale de dos años de caída (−7,9 % en 2024). Las mipymes ecuatorianas no usan IA, sobre todo por **falta de datos ordenados**.
2. **El problema de Torvesa:** las solicitudes esperan horas o días, cada cotización se arma casi desde cero y el historial del cliente vive en el celular del vendedor («amnesia institucional»).
3. **Pregunta central:** ¿cómo diseñar un sistema que permita responder más rápido, dar continuidad con el vendedor titular y conservar un historial verificable de cada cliente?
4. **Objetivos (OE1–OE5):** diagnóstico → diseño (con VAN y TIR para Torvesa) → **prototipo funcional** → validación del diseño en operación experimental controlada (23-nov a 5-dic) → manual y transferencia.
5. **Metas M1–M6:** primer contacto en menos de 15 min (meta de diseño, no un dato probado), menos tiempo por cotización, menos fuga, mejor recuperación del historial, 100 % de alteraciones detectadas y SUS de al menos 68.

## Lo que cambió frente al diseño aprobado (y te afecta)
- **Ya no hay cifras de línea base:** las del diagnóstico N = 30 eran simulados. Todas las metas se comparan contra lo que **midamos en el campo** (tu cronometraje y la revisión de solicitudes de 3 meses).
- **Los «30 a 44 minutos por cotización» no tienen fuente.** Tu cronometraje es el que da el dato real de M2.
- **Registro verificable:** sin OpenTimestamps; huellas SHA-256 + registro al que solo se agregan entradas (D6).
- **OE3 dice «prototipo funcional»:** no entregamos un sistema en producción.

## Lo que necesitamos de Torvesa (tu frente)
| Dato | Para qué | Marcador en el capítulo |
|---|---|---|
| Captura del RUC en el SRI y confirmación del giro (¿vías, edificación, venta de inmuebles?; ¿qué parte es pública y qué parte es privada?) | A1 y alcance | FALTA-DATO A1 |
| Nota firmada: número de colaboradores, cuántos cotizan y número de clientes | A2, A3 | FALTA-DATO A2, A3 |
| **Cuántas solicitudes de cotización llegan por semana** | Saber si en 2 semanas de validación hay datos suficientes | FALTA-DATO (limitación i) |
| Permiso para el campo (encuestas, entrevistas, cronometraje, muestra de 3 meses) | Línea base M1–M6 | FALTA-DATO M1–M6 |

**Fecha clave:** si Torvesa no responde hasta el **viernes 24-oct**, Víctor escala (llamada al Ing. Torres o carta de la tutora).
