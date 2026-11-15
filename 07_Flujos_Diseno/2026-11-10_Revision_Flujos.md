---
titulo: Revisión de los diagramas de flujo (qué estaba mal, qué se corrigió, qué falta decidir)
version: v0.1
fecha: 2026-11-10
autor: Claude (frente 3); revisan Víctor y Diego
base: "AS-IS v0.1 · TO-BE v0.1 partes 1–3 · recorrido de la prueba de concepto · proceso estrella v0.1 (sección 6) · censo n = 5"
tags: [revision, flujos, bpmn, figuras, sprint5]
---

# Revisión de los diagramas de flujo

> [!summary] En tres frases
> 1. Los diagramas BPMN de Diego (proceso actual y proceso con el sistema) **están bien armados**, pero son densos para una persona que no conoce el proyecto y **no dicen cuánto tarda cada paso**.
> 2. El diagrama del proceso estrella que salió por script el 10-nov **tenía tres pasos en el carril equivocado** y le faltaba el camino «sigue abierta». Se corrigió en la versión 0.2.
> 3. Se hicieron **versiones simples con tiempos** de cada flujo y una **vista general en una página**. Los BPMN originales no se tocaron: siguen siendo la versión técnica.

## Cómo se revisó

Seis criterios: un inicio y un fin claros · cada decisión con sus salidas rotuladas · ninguna flecha cruza una caja · cada paso en el carril de quien lo hace · todos los caminos posibles · poca información (unas 12 a 14 cajas, de 3 a 6 palabras).

## Qué se encontró

| Diagrama | Qué está bien | Qué estaba mal o falta |
|---|---|---|
| **Proceso actual** (`2026-10-25_AS-IS_v0.1.png`) | Inicio, fines y decisiones claros; 8 pasos; los 5 puntos críticos marcados | No dice tiempos. El censo sí da uno: 3 de 5 revisan los mensajes cada 3–4 h o al llegar a casa |
| **Con el sistema, parte 1** | Cubre las dos entradas (formulario, WhatsApp o teléfono) y el temporizador de 15 min | El nombre del carril «Registro y alertas» sale cortado. Tres flechas pasan por encima de textos (RQ-18, «Recibe el primer contacto» y la nota amarilla). Usa códigos sin explicar (RQ-, CLI-0001, MVP). Dice que el sistema «asigna un responsable», pero hoy el responsable es quien pulsa «Tomar» |
| **Con el sistema, parte 2** | La revisión humana y la aprobación de la gerencia están como decisión | 7 carriles y 14 tareas: es el más denso. El cierre «Ganada o Perdida» es una sola caja, sin caminos separados. El camino «el cliente no responde» solo está en el texto. Un rótulo del registro sale cortado a la derecha |
| **Con el sistema, parte 3** | Tres flujos cortos y claros; cubre al vendedor que se va | La decisión «¿Qué pasa primero?» no rotula sus salidas. El segundo plazo de 15 min es un supuesto |
| **Recorrido de la prueba de concepto** (v0.1) | Lineal y fácil | Sin tiempos |
| **Proceso estrella E1** (PNG v0.1) | Cubre las dos entradas y el escalamiento | **Carriles equivocados:** el recordatorio (lo hace el sistema), el motivo de pérdida (lo elige el responsable) y el reporte del lunes (lo envía el sistema) estaban en Gerencia; «Cerrado: ganado» estaba en Cliente. Faltaba el camino **«sigue abierta»**. La decisión de los 15 min y «Pulsa Tomar» eran dos pasos para una sola cosa. Sin tiempos. En Miro los carriles sí estaban bien |

## Qué se corrigió (figuras nuevas, en `06_Capitulos/Figuras/`)

| Figura | Qué es | Caminos que cubre |
|---|---|---|
| `2026-11-10_Fig_Vista_General_v0.1.png` | **Vista general en una página:** hoy frente a con el sistema, con el tiempo de cada paso | De punta a punta |
| `2026-11-10_Fig_Proceso_Actual_Tiempos_v0.1.png` | Proceso actual en 11 cajas, con tiempos y los puntos críticos | Lo atiende quien recibe o lo reenvía; el cliente acepta o se va |
| `2026-11-10_Fig_Proceso_Estrella_E1_v0.2.png` | Proceso estrella corregido, 15 cajas | Formulario, o WhatsApp y teléfono; se toma a tiempo o no; gana, pierde o sigue abierta |
| `2026-11-10_Fig_Flujo_Cotizacion_v0.1.png` | Cotización con el asistente, 13 cajas | Con o sin aprobación de la gerencia; acepta, dice que no, o no responde |
| `2026-11-10_Fig_Flujo_Casos_Especiales_v0.1.png` | Un vendedor se va; un cliente llama y su vendedor no está | Los dos casos |
| `2026-11-10_Fig_Recorrido_Prueba_Concepto_v0.2.png` | El recorrido, con tiempos | Lineal |

- Las figuras v0.1 no se sobrescribieron.
- **Miro:** el marco 8 (proceso estrella) quedó en la versión 0.2 y hay un marco nuevo, el 13, con la vista general. Los marcos 1 a 5 no cambiaron.
- En las figuras no hay códigos de requisitos ni nombres de archivos.

## De dónde sale cada tiempo

| Tiempo | Qué es | De dónde sale |
|---|---|---|
| Cada 3–4 h o al llegar a casa (3 de 5) | Lo que pasa hoy | Censo de Torvesa, n = 5 (Bermeo y Segura, 2026, p. 10). Es un antecedente, no una medición |
| 5 s o menos (registro y aviso) | Objetivo de diseño | Requisitos RQ-01 y RQ-02. Aún no medido |
| 1 min o menos (registro manual) | Objetivo de diseño | Requisito RQ-03 |
| Menos de 15 min (primer contacto) | Meta M1 | Decisión de diseño; coincide con lo que piden 4 de 5 en el censo |
| Otros 15 min (reasignación) | Supuesto | TO-BE parte 3; por validar con la empresa |
| 15 s (borrador del asistente) | Una prueba con datos ficticios | Prueba de concepto del 8-nov |
| «Sin dato» | No se sabe | Primer contacto, cotización y reenvío de hoy: salen de la muestra documental y de los casos de prueba |

No se puso ningún tiempo de «hoy» sin respaldo. En particular, **no se usó «30 a 44 minutos por cotización»**, que aparece en la meta M2 del Glosario: hay que confirmar de dónde sale antes de dibujarlo. [DECIDIR-VÍCTOR: origen de esa cifra; si viene del diagnóstico simulado, no se usa]

## Dónde se puede optimizar más (estrella en las figuras)

1. **Registro manual de los mensajes de WhatsApp.** Depende de que el coordinador se acuerde. Más adelante se puede registrar solo, con la API de WhatsApp Business.
2. **«Tomar».** Hoy se espera a que alguien pulse. Con una regla de turnos, el sistema podría asignar de una vez.
3. **Segundo plazo de reasignación.** Los «otros 15 minutos» son un supuesto; hay que fijarlo con la empresa.
4. **Aprobación de la gerencia antes de enviar la cotización.** Si existe, es el paso que más puede demorar; se puede limitar a las cotizaciones que pasen de cierto monto.

## Qué queda por decidir

- [DECIDIR-VÍCTOR: ¿las figuras simples van en el cuerpo de la tesis y los BPMN completos al Anexo 4, o al revés?]
- [DECIDIR-VÍCTOR: en la parte 1, ¿se dibuja «alguien pulsa Tomar» (lo que hoy funciona) o «el sistema asigna» (lo que dice el BPMN)? Las figuras nuevas usan «Tomar»]
- **Para Diego (BPMN v0.2):** arreglar el carril cortado y las flechas sobre textos, separar «Ganada» y «Perdida», dibujar «no responde» y rotular las salidas de «¿Qué pasa primero?».
- **Para la empresa:** si la gerencia aprueba las cotizaciones, si hay visita a la obra antes de cotizar (faltaría un paso) y qué pasa a los 15 minutos.

## Cómo se regeneran

Doble clic en `99_Scripts/figuras/Generar_Figuras.bat`. Los textos están en `datos_figuras.json` y las instrucciones, en el `README.md` de esa carpeta.
