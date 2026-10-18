---
titulo: El problema de Torvesa y sus fuentes — resumen de 1 página para Diego
fecha: 2026-10-18
autor_borrador: Claude Opus 5.5 (borrador; Víctor lo revisa antes de enviarlo)
para: Diego
tags: [resumen, problema, fuentes]
---

# El problema y sus fuentes (en 1 página)

## El problema, en tres frases
1. En Torvesa, **las solicitudes de clientes esperan**: no hay un aviso inmediato ni un responsable claro, y la respuesta puede tardar horas o días.
2. **Cada cotización se arma casi desde cero**: las cotizaciones anteriores y lo que se habló con cada cliente están dispersos (celulares, WhatsApp, cuadernos).
3. Si alguien se va o falta, **la empresa pierde lo que esa persona sabía del cliente**. En la tesis lo llamamos «amnesia institucional».

## Lo que dicen las fuentes verificadas (abiertas, con página)

| Idea | Qué dice la evidencia | Fuente |
|---|---|---|
| La construcción es de los sectores menos digitalizados | 21.º de 22 sectores en EE. UU. (dato de 2015); en Chile, el 68 % de las micro y pequeñas constructoras está en la etapa inicial de digitalización | Manyika et al. (2015, histórica); Cathles et al. (2023) |
| Por qué cuesta digitalizar la construcción | Trabaja entre empresas, por proyectos y de forma fragmentada | Samuelson y Stehn (2023) |
| Ecuador | La construcción cayó 7,9 % en 2024 y creció 2,7 % en 2025: no se pueden perder clientes por demoras | Banco Central del Ecuador (2026) |
| Mipymes ecuatorianas | Una barrera central para usar IA es la **falta de bases de datos estructuradas**: es el problema de Torvesa | Pérez-Campdesuñer et al. (2025) |
| Adopción de IA | Las grandes empresas la adoptan mucho (McKinsey: 78 %), pero las pymes poco (OCDE: 11,9 % en empresas de 10 a 49 personas). **Hay que citar las dos** para no exagerar | McKinsey (2025); OCDE (2025) |

## Cuidado: lo que NO está probado
- **«Responder en 5–15 minutos»** no tiene respaldo académico. Lo que sí hay es que la probabilidad de calificar al cliente cae mucho después de **la primera hora** (Oldroyd et al., 2011; falta abrir el PDF). En la tesis, los **15 minutos son una meta de diseño nuestra**, no un dato probado.
- **«30–44 minutos por cotización»** no tiene fuente: se va a **medir con cronómetro** en Torvesa (eso es tuyo, cuando la empresa autorice).
- Los **datos del diagnóstico N = 30 eran simulados**: no se usan para nada.

## Qué significa para tu parte (lo técnico)
- El sistema tiene que atacar las tres frases de arriba: **aviso inmediato** (solicitud → celular), **historial en un solo lugar** (la bóveda) y **borrador de cotización** desde cotizaciones anteriores (el asistente con RAG).
- Tus fuentes de esta semana (bóvedas, RAG, BPMN, CRMs) tienen que conectar con esas tres piezas.

Todas las fuentes, con su estado, están en la matriz: `03_Matriz_Objetivos/2026-10-18_Matriz_Afirmaciones_v0.1.xlsx`.
