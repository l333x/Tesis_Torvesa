---
titulo: "Requisitos y costos en 1 página — para Diego"
version: v0.1
fecha: 2026-11-16
autor_borrador: "Claude (Frente B); Víctor lo revisa antes de enviarlo"
tarea: "S4-T14"
para: Diego
base: "Cap. IV v0.3 (24 requisitos) · Modelo financiero v0.2 · Análisis financiero v0.2 (15-nov)"
tags: [resumen, requisitos, costos, diego]
---

# Requisitos y costos en 1 página

## Los 24 requisitos, agrupados por meta

| Grupo | Requisitos | Meta | Estado en la prueba de concepto |
|---|---|---|---|
| Recibir y avisar | RQ-01 registrar con hora · RQ-02 aviso en 5 s · RQ-03 registrar desde el celular · RQ-24 hora del primer contacto | M1 | RQ-01, RQ-02 y RQ-24 funcionan con datos ficticios (falta medir los 5 s); RQ-03 pendiente |
| Responsable y estados | RQ-04 un único responsable · RQ-05 estados · RQ-06 recordatorio a los 15 min · RQ-07 motivo de pérdida · RQ-08 reporte del lunes | M1, M3 | RQ-04 y RQ-05 funcionan con el botón «Tomar» (falta el estado «Cotizada»); RQ-06 a RQ-08 están en una rama sin unir a la principal |
| Memoria comercial | RQ-09 ficha por cliente · RQ-10 plantillas por tipo de obra · RQ-13 búsqueda · RQ-14 sin conexión | M2, M4 | Bóveda con fichas ficticias |
| Asistente | RQ-11 borrador que cita documentos · RQ-12 revisión humana obligatoria | M2 | Borrador en unos 15 s, en una prueba |
| Registro verificable | RQ-15 registro de solo agregar con huellas · RQ-16 verificación | M5 | 3 de 3 alteraciones detectadas (8-nov) |
| Ley de datos | RQ-17 sin datos personales en el registro · RQ-18 consentimiento · RQ-19 borrar a los perdidos · RQ-21 la IA solo ve códigos | — | RQ-18 en la rama de consentimiento |
| Acceso y uso | RQ-20 cuentas individuales · RQ-22 usabilidad · RQ-23 validación de dos semanas | M6 | Pendiente |

**Lo urgente de tu lado:**
- separar las claves del servidor antes de usar datos reales, porque hoy la clave de la página pública también permite leer las solicitudes;
- unir a la rama principal lo de RQ-05 a RQ-08 y RQ-18.

## Los costos en 5 cifras (escenario base, sin IVA)

| Qué | Cifra | De dónde sale |
|---|---|---|
| Nuestra hora de trabajo | USD 9,26 | Sueldo real de un desarrollador semi-senior en Ecuador (USD 1.084) más las cargas de ley |
| Inversión inicial | USD 2.243 | 200 horas ya trabajadas (supuesto: necesito tus horas reales) + USD 391 en efectivo |
| Precio | Estándar USD 175 · Premium USD 275 al mes | Implementación: USD 222 o USD 311 |
| Viabilidad para nosotros | Premium: VAN USD 427, TIR 26 %, unos 25 meses | Con el Estándar solo no se recuperan las horas ya trabajadas |
| Lo que gana cada uno | Unos USD 77 al mes, a USD 14,53 la hora | Es un ingreso extra, no un sueldo |

**Para Torvesa:** el sistema se paga si recupera 1,9 obras al año (VAN USD 13.618). Casi todos los datos de Torvesa son todavía supuestos.

**Los costos que dependen de ti** (revisa si siguen igual): servidor (Railway), página (Vercel), API del asistente (Anthropic) y WhatsApp (Meta). Todos tienen su fuente en la hoja Fuentes del modelo financiero. Si cambió algún plan o precio, avísame y actualizo el modelo.
