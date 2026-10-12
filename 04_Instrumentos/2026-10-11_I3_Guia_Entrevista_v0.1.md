---
titulo: I3 — Guía de entrevista semiestructurada (proceso AS-IS)
version: v0.1
fecha: 2026-10-11
autor_borrador: Claude Opus 5.5
estado: borrador
duracion_estimada: 30–40 min
tags: [instrumentos, entrevista, as_is, bpmn]
---

# I3 — Entrevista semiestructurada (v0.1)

**A quién:** 3–5 personas (gerencia, coordinación comercial y quienes preparan cotizaciones). **Código:** `ENT-01`… **Consentimiento:** C1-A firmado, con la casilla de audio aparte. Sin audio, se toman notas textuales.

**Objetivo:** reconstruir el proceso real (AS-IS) de **solicitud → primer contacto → cotización → seguimiento**, para el BPMN de Diego, y averiguar de dónde sale el dato de «30–44 min por cotización».

**Reglas del entrevistador:** preguntas abiertas, sin sugerir respuestas. Pedir **ejemplos concretos y recientes** («la última vez que…»). No juzgar. Repreguntar con «¿cómo?», «¿quién?» y «¿qué pasa si…?».

## 1. Apertura (2 min)
- Recordar la finalidad, la voluntariedad y la confidencialidad; confirmar si se graba el audio.
- «¿Cuál es su rol y desde cuándo está en Torvesa?»

## 2. Entrada de solicitudes (8 min)
1. ¿Por dónde llegan las solicitudes de cotización? ¿Cuál es el canal más frecuente?
2. Cuando llega una, ¿quién se entera primero y cómo decide quién la atiende?
3. Cuénteme la **última** solicitud que llegó: ¿qué pasó paso a paso?
4. ¿Qué pasa si llega cuando el vendedor está en obra o fuera de horario?

## 3. Elaboración de la cotización (10 min)
5. ¿Qué información necesita para cotizar? ¿De dónde la saca?
6. ¿Usa cotizaciones anteriores o plantillas? ¿Dónde están guardadas? ¿Cuánto tarda en encontrarlas?
7. ¿Qué parte del trabajo toma más tiempo? ¿Qué parte es espera (por datos de obra, de proveedores, de aprobación)?
8. **Origen del dato:** en el diseño de la tesis se dice que una cotización toma entre 30 y 44 minutos. ¿Le parece real? ¿De dónde cree que sale esa cifra? ¿Hay algún registro?
9. ¿Quién revisa o aprueba la cotización antes de enviarla?

## 4. Seguimiento e historial (8 min)
10. Después de enviar la cotización, ¿qué pasa? ¿Quién hace el seguimiento y cuándo?
11. Si hoy un vendedor deja la empresa, ¿qué pasa con sus clientes? ¿Ha pasado? Cuénteme ese caso.
12. ¿Dónde queda la historia de cada cliente? ¿Quién más puede verla?

## 5. Herramientas y cierre (5 min)
13. ¿Qué herramientas usa hoy (TEAMSLASH, Excel, WhatsApp…)? ¿Qué funciona y qué no?
14. Si pudiera cambiar una sola cosa del proceso, ¿cuál sería?
15. ¿Hay algo que no le pregunté y que debería saber?

## Después de la entrevista (aplicador, en máximo 24 h)
- Transcribir o pasar las notas a `05_Datos_Campo/_crudo/` (no va a Git) y anonimizar: nombres → roles, clientes → `CLI-xx`.
- Llenar el registro P1: fecha, duración, modalidad, aplicador, con o sin audio, y hash del archivo crudo.
- Borrar el audio una vez transcrito y verificado, si así lo dice el consentimiento.
- Pasar a Diego los pasos del proceso para el BPMN AS-IS (`07_Flujos_Diseno/`).
