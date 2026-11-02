---
titulo: Resumen para Víctor — la bóveda del sistema en 1 página
version: v0.1
fecha: 2026-11-02
autor: Diego Bermeo
ia: Claude (Claude Code)
tarea: S4-T13 (bloque Q)
base: 07_Flujos_Diseno/Boveda_Sistema/00_Inicio.md
tags: [diego, resumen, boveda, sprint4]
---

# La bóveda del sistema en 1 página

> [!summary] En tres frases
> 1. La bóveda es una carpeta de notas en Obsidian donde queda la **memoria comercial de la empresa**: una ficha por cliente, sus solicitudes, sus cotizaciones y las plantillas. Ya no depende del celular de cada vendedor (punto ❺ del AS-IS, meta M4).
> 2. Los **datos personales** (nombre, teléfono y correo) van **en una sola carpeta aparte**, que el asistente de IA no lee. Así se cumplen RQ-21 y la LOPDP, y borrar a un cliente es borrar una nota.
> 3. Los **tableros** muestran los pendientes de cada vendedor sin preguntarle a nadie. Funcionan con Bases, que viene con Obsidian: no hace falta instalar nada más.

> [!warning] Todo lo de la bóveda es de ejemplo
> Clientes, solicitudes y cotizaciones **ficticios**, para probar la estructura. No hay datos de Torvesa.

## Qué hay adentro

| Carpeta | Qué guarda | Qué meta o requerimiento atiende |
|---|---|---|
| Clientes | Una ficha por cliente (`CLI-0001`), **sin datos personales** | M4, RQ-09 |
| Solicitudes | Estado, responsable, hora de ingreso y de primer contacto | M1, M3, RQ-05 |
| Cotizaciones | Cada cotización enviada, qué documentos usó el asistente y su huella | M2, M5, RQ-11, RQ-15 |
| Plantillas de cotización | Una por tipo de obra; los rubros sin precios | M2, RQ-10 |
| Equipo | Un vendedor por nota (rol y si está activo) | RQ-20 |
| `_Contactos` | Nombre, teléfono y correo: **lo único personal** | RQ-19, RQ-21, LOPDP |

**Tableros:**
- pendientes por vendedor, con una vista de las solicitudes «sin primer contacto»;
- clientes por responsable;
- cotizaciones que esperan respuesta.

## Cómo encaja con el resto del sistema
- **El registro de solicitudes** (TEAMSLASH, base de datos) es el que **guarda las horas oficiales** para medir M1 y M3. En la prueba de concepto, el sistema **copia cada solicitud a la bóveda** para que el equipo vea sus pendientes en Obsidian.
- **El asistente de IA** lee clientes, solicitudes, cotizaciones y plantillas para proponer borradores. **Nunca lee `_Contactos`.**
- **El registro verificable** guarda las huellas de cada evento, aparte de la bóveda (M5).

## Qué tienes que decidir tú

| Decisión | Opciones | Qué cambia |
|---|---|---|
| **Sincronización en el celular** | Plugin de Git: gratis, pero su autor dice que es muy inestable en el móvil (A34). Obsidian Sync: USD 4 por usuario al mes con pago anual (A32) | El costo mensual del Cap. 5 y RQ-14 (ver fichas sin señal) |
| **¿`_Contactos` va en una bóveda aparte?** | Misma bóveda: todos los que la tienen ven todo, porque Obsidian no permite permisos por usuario (A33). Bóveda aparte: solo la ve quien atiende | La protección de datos (LOPDP) y un poco más de trabajo para el equipo |
| **Tipos de obra de las plantillas** | Partir de los del formulario web (residencial, comercial, remodelación, mantenimiento…) o esperar el catálogo de Torvesa | Las plantillas reales (PEN-12) |

## Lo que todavía no hace
- **No se conecta sola con TEAMSLASH:** eso es la prueba de concepto del sprint 5. Además, TEAMSLASH hay que volver a desplegarlo.
- **No tiene el asistente de IA funcionando:** también es del sprint 5.
- **Falta abrirla en Obsidian** para confirmar que los tableros se ven. El filtro se comprobó con un script.
