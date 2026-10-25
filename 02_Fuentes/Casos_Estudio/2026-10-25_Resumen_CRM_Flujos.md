---
titulo: Resumen para Víctor — CRM, mensajería y flujos
version: v0.1
fecha: 2026-10-25
autor: Diego Bermeo
ia: Claude (Claude Code)
tarea: S1-T26 (bloque H)
tags: [diego, resumen, crm, flujos, inventario, sprint2]
---

# CRM, mensajería y flujos en 1 página

> [!summary] En tres frases
> 1. Hoy los clientes llegan por **WhatsApp personal** y la información se pierde en cinco puntos del proceso (AS-IS v0.1). Ninguno se arregla solo con un CRM: el centro del diseño sigue siendo la **bóveda** más el **asistente de IA**.
> 2. En el inventario, **Obsidian** (bóveda), **Claude Sonnet 5.5** (LLM, ya elegido) y **WhatsApp Business** (canal con el cliente) salen primeros sin discusión. **Slack** queda para los avisos internos, porque ya está en TEAMSLASH.
> 3. En **CRM** hay empate entre **Zoho** y **Kommo**, y el CRM **no es un componente del diseño aprobado**. Antes de elegir uno hay que decidir si entra.

## 1. Flujos: qué dice el AS-IS (bloque F)

| Punto donde se pierde tiempo | Qué lo resuelve en el diseño | Meta |
|---|---|---|
| ❶ Nadie ve el mensaje hasta revisar el celular | Aviso inmediato (WhatsApp → Slack) | M1, M3 |
| ❷ El reenvío no deja rastro | Asignación con responsable y registro | M1, M3 |
| ❸ Cotización desde cero | Bóveda + asistente con RAG | M2 |
| ❹ Seguimiento de memoria | Recordatorios (aquí podría entrar un CRM) | Ninguna: duda 4 del reporte |
| ❺ Historial en celulares | Bóveda con el historial de cada cliente | M4 |

Las fuentes de procesos ya verificadas respaldan cómo se levantó: BPMN muestra mejor quién hace cada paso (Nizioł et al., 2021, p. 199); en empresas sin registros se pueden levantar los procesos con BPMN y visitas (Martínez Mendoza et al., 2023, p. 4848); y automatizar reduce tiempos y mejora la trazabilidad, sobre todo en procesos repetitivos (Sánchez-García et al., 2026, p. 127).

## 2. CRM: qué dice la literatura

| Idea | Fuente (página) | Ojo |
|---|---|---|
| El CRM con tecnología mejora el desempeño de las pymes, pero la «organización del CRM» no tiene efecto directo | AlQershi et al. (2020, p. 9) | Contradice el borrador (A23) |
| El CRM sirve para gestionar el conocimiento del cliente e innovar | Gil-Gomez et al. (2020, p. 2733) | Modelo sin datos todavía |
| La calidad del CRM con IA influye en la intención de usarlo | Chatterjee et al. (2023, p. 1299) | — |

**Vacío:** la búsqueda D05 (CRM móvil en pymes) dejó **7 candidatas sin verificar**. Las mejores para leer son Kučera y Cmuntová (2023), un CRM en una pyme comercial, y Pérez-Vega et al. (2022), sobre CRM social, en *Journal of Business Research*. Ninguna está lista para citarse.

## 3. Herramientas: resultado del inventario v0.2

Puntaje de 1 a 3 con los pesos propuestos (en la hoja «Puntuación»; los apruebas tú):

| Componente | Primero | Después | Por qué |
|---|---|---|---|
| Bóveda | **Obsidian 2,81** | Logseq 1,94 · Notion 1,69 | Archivos locales, app móvil gratis, es la del diseño aprobado |
| LLM | **Claude Sonnet 5.5 2,70** | Gemini 2,50 · OpenAI 2,20 | No entrena ni guarda el contenido por defecto. Con pesos iguales empata con Gemini, que es más barato |
| Mensajería | **WhatsApp 3,00** | Slack 2,13 · Telegram 1,88 | Es el canal del cliente; 1 000 mensajes de servicio gratis al mes |
| CRM | **Zoho 2,39 = Kommo 2,39** | HubSpot 2,33 · Pipedrive 2,11 | Zoho: barato y gratis para 3 usuarios. Kommo: único con WhatsApp oficial, pero 6 meses mínimo y sin DPA |

*DPA: el contrato que fija cómo el proveedor trata los datos personales por cuenta de Torvesa (en la LOPDP, el proveedor es el «encargado»).*

**Costo ilustrativo** (supuestos: 3 usuarios, 1 000 consultas y 600 mensajes al mes): Obsidian Sync USD 12 + Claude USD 13 + WhatsApp USD 0 + Slack Free USD 0 ≈ **USD 25 al mes** sin CRM. Con Zoho Standard, unos USD 61. Los supuestos se reemplazan con los datos de campo.

## 4. Para decidir (tú, y la tutora en la Revisión 1)
1. **¿Entra un CRM al diseño?** No está entre los componentes aprobados (bóveda, asistente de IA y registro verificable). Sin CRM, el punto ❹ (seguimiento) queda sin herramienta ni meta.
2. **Pesos de los criterios:** propuse que los datos (LOPDP) pesen 25 % y el costo 15 %, porque todas las opciones son baratas.
3. **A36 → ✅** con Claude Sonnet 5.5 (`anthropic_sf`, `anthropic_2026`, `anthropic_sfb`).
