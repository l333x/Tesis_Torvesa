---
titulo: Instrumentos de campo — índice y plan de aplicación (15–16 oct 2026)
version: v0.1
fecha: 2026-10-11
autor_borrador: Claude Opus 5.5 (borrador para corrección de Víctor)
estado: borrador
tags: [instrumentos, campo, linea_base]
---

# Instrumentos de campo v0.1

> [!info] Ciclo
> Claude genera la v0.1 → Víctor corrige → v0.2. **No se sobrescribe una versión que Víctor haya editado**: cada versión nueva es un archivo nuevo. La versión final se exporta a Word o Google Forms **después** de que la apruebes.

> [!warning] Pendientes que bloquean la versión final
> - **[VOCAB]** El giro de Torvesa está pendiente (A1–A1d). Donde aparezca `[VOCAB: …]`, se ajusta cuando Torvesa confirme si cotiza obra vial, edificación o inmuebles.
> - Las fuentes metodológicas citadas aquí son **candidatas sin verificar**. Ninguna va a la tesis hasta que se verifique en la fase 1.
> - **Permiso de gerencia** (Ing. Mentor Torres) para: (1) aplicar en horario laboral, (2) observar y cronometrar cotizaciones, (3) revisar una muestra documental de solicitudes y cotizaciones pasadas. La carta del 29-sep cubre «encuestas, entrevistas y pruebas»; conviene confirmarlo de palabra y anotarlo en el registro.

## Qué se aplica, a quién y para qué

| Código | Instrumento | Población | Modalidad | Mide (línea base) | Metas y OE |
|---|---|---|---|---|---|
| **I1** | Encuesta a colaboradores | Censo de 30 (los bloques por rol se filtran) | Presencial en papel o Google Forms en sesión supervisada | Flujo oficina–obra, recuperación de historial, seguimiento, prioridades; SUS solo si usa TEAMSLASH | M4, M6 · OE1 |
| **I2** | Encuesta a clientes | Censo de 33 | Teléfono o enlace individual | Tiempo de respuesta **percibido**, calidad de la cotización, insatisfacciones | OE1 (empatía DT) |
| **I3** | Entrevista semiestructurada | 3–5 personas: gerencia + quienes cotizan | Presencial, 30–40 min, audio solo con consentimiento | Proceso AS-IS (para BPMN), origen del dato 30–44 min, causas | OE1, OE2 |
| **P2-A** | Cronometraje de cotizaciones en vivo | Todas las cotizaciones del jueves y el viernes | Observación directa + hoja de registro | **Tiempo de esfuerzo** por cotización | **M2** |
| **P2-B** | Muestra documental retrospectiva | Solicitudes y cotizaciones de los últimos 3 meses | Revisión de correo, WhatsApp o CRM **anonimizada** | **Tiempo transcurrido**: solicitud → primer contacto → cotización enviada | **M1, M3** |
| **C1** | Consentimiento informado (LOPDP) | Todos los que participan en I1, I2, I3 y P2-A | Papel firmado u opción obligatoria en el formulario | — | Normativa (OVA 6.3) |
| **P1** | Protocolo de aplicación y procedencia | Lo usan los aplicadores | — | Evidencia de que los datos son reales | Integridad |

## Agenda propuesta

| Día | Mañana | Tarde | Responsable |
|---|---|---|---|
| **Mié 14** | Víctor corrige la v0.1 → v0.2 · se imprimen I1, C1 y las hojas de P1 y P2 · se arma el Google Forms (si se usa) | Prueba piloto de I1 con 1–2 personas **ajenas** a Torvesa (claridad y duración) | Víctor (instrumentos) · Diego (formularios y hojas) |
| **Jue 15** | Sesión de I1 con colaboradores (consentimiento → encuesta) · arranca P2-A | I3: entrevistas 1–2 · P2-A continúa · P2-B: extracción de la muestra documental con quien autorice gerencia | Víctor aplica · Diego cronometra |
| **Vie 16** | I1 para los rezagados · I2: llamadas a clientes | I3: entrevistas 3–5 · P2-A continúa · cierre: digitar, anonimizar, calcular hashes y llenar el registro P1 | ambos |
| **Sáb–dom** | Consolidación: datos anonimizados en `05_Datos_Campo/LineaBase_2026-10/` y primer análisis descriptivo | | Víctor |

## Cambios frente a los instrumentos simulados (trazabilidad)

| Problema en el original | Ejemplo | Cambio en la v0.1 |
|---|---|---|
| Vocabulario inmobiliario no confirmado | «disponibilidad de inmuebles», «financiamiento» | Términos neutros + `[VOCAB]` |
| Ítems que inducen la respuesta | «Siento que perdemos ventas **simplemente porque**…» | Redacción neutra, con la causa como opción y no como premisa |
| Lenguaje cargado | «lo usaran **religiosamente**» | «¿Qué haría que lo usara a diario?» |
| Percepción usada como medición | «¿cuánto tiempo pasa hasta el primer contacto?» (respondido por todos) | El tiempo se **mide** con P2-B; en I1 solo lo responden quienes atienden clientes, y se reporta como percepción |
| Preguntas sin filtro de rol | personal de obra respondiendo sobre leads | Bloques condicionados por rol |
| Abiertas con respuestas tipo | 30 respuestas armadas por plantilla | Texto libre, sin ejemplos que sugieran la respuesta |
| SUS a quien no usa el sistema | 13 de 30 «no lo uso» | SUS solo para quien lo usó al menos una vez |
| Cuatro encuestas a la misma población | fatiga, «composición por rol inestable» | **Una** encuesta con un código de participante (rol constante) |
