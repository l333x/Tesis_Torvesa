---
titulo: Plantilla para los procesos con el sistema (TO-BE)
version: v0.1
fecha: 2026-11-02
autor: Diego Bermeo
ia: Claude (Claude Code)
tarea: S3-T12 (bloque M)
archivos: [2026-10-31_Plantilla_TO-BE_v0.1.bpmn]
uso: se copia para cada parte del TO-BE (2026-11-04_TO-BE_v0.1_parteN.*); este archivo no se edita
tags: [diego, to-be, bpmn, plantilla, sprint3]
---

# Plantilla TO-BE · v0.1

> [!info] Cómo se usa
> 1. Copia `2026-10-31_Plantilla_TO-BE_v0.1.bpmn` como `2026-11-04_TO-BE_v0.1_parteN.bpmn` y dibuja en https://demo.bpmn.io o en Camunda Modeler. Ya trae los carriles.
> 2. Copia la sección «Ficha de la parte» de abajo en `2026-11-04_TO-BE_v0.1_parteN.md` y llénala.
> 3. Exporta el PNG con el mismo nombre.

## Los 6 pasos del flujo de atención

Salen del Cap. 2 v0.3 («captación, asignación, aviso, primer contacto, cotización y traspaso de un cliente»):

| Paso | Nombre | Qué pasa con el sistema | Parte del TO-BE |
|---|---|---|---|
| P1 | Captación | La solicitud entra por el formulario o se registra a mano desde WhatsApp o el teléfono | 1 |
| P2 | Asignación | Queda un único responsable, con hora | 1 |
| P3 | Aviso | La alerta llega al celular del responsable con el enlace a la ficha | 1 |
| P4 | Primer contacto | El responsable contacta al cliente y lo marca: queda la hora (M1) | 1 |
| P5 | Cotización | Borrador con el asistente a partir de la bóveda, revisión humana y envío con huella | 2 |
| P6 | Traspaso | Si el titular no está o se va, otra persona retoma al cliente desde su ficha | 2 |
| — | Recordatorios y reasignación | A los 15 min sin contacto: recordatorio, aviso a la gerencia y, si se acuerda en el taller, reasignación (CON-06) | 3 (cruza P2–P4) |

> [!warning] Para Víctor: numeración
> `IA_DIEGO.md` dice que la parte 2 «cubre los pasos 3 y 4». Con el orden del Cap. 2, la cotización y el historial son los pasos **P5 y P6**. Propongo usar la numeración de esta tabla. Si no, hay que corregir una de las dos.

## Carriles (cada parte usa los que necesita, con estos nombres y en este orden)

| Carril | Quién o qué | Tipo |
|---|---|---|
| Prospecto o cliente | INT-05 | Pool aparte: se comunica con mensajes |
| Coordinador comercial | INT-02 | Persona |
| Quien cotiza | INT-03 | Persona |
| Gerencia | INT-01 | Persona |
| Otro vendedor o colaborador | INT-04 | Persona (traspaso, P6) |
| Registro y alertas (TEAMSLASH) | Formulario, API, base de datos, Slack | Sistema |
| Bóveda y asistente de IA | Obsidian, plantillas, LLM | Sistema |
| Registro verificable | Eventos con huella SHA-256 | Sistema |

## Reglas de dibujo

- **Nombres de tareas:** verbo en infinitivo + objeto. Por ejemplo, «Registrar la solicitud», no «Registro».
- **Compuertas:** una pregunta que se responde con sí o no, por ejemplo «¿Contactó en 15 min?». Cada salida lleva su respuesta.
- **Tareas del sistema:** tipo «tarea de servicio» (el ícono de engranaje). Tareas de personas: «tarea de usuario».
- **Tiempos:** los plazos van como evento de temporizador en el borde de la tarea (por ejemplo, 15 min).
- **Cada tarea que cambia algo** deja un evento en el carril «Registro verificable» (RQ-15). Se dibuja con una flecha punteada de datos, no de secuencia.
- **Sin datos reales:** los ejemplos usan `CLI-0001`.
- **Nada inventado:** lo que todavía no se sabe de Torvesa va como anotación «Por validar en campo (PEN-xx)».

## Ficha de la parte (copiar y llenar)

```markdown
---
titulo: Proceso con el sistema (TO-BE) · parte N: <nombre>
version: v0.1
fecha: AAAA-MM-DD
autor: Diego Bermeo
tareas: [S4-T0x]
pasos: [P1, P2]
estado: borrador sin validar con Torvesa
---

# TO-BE parte N · <nombre>

![TO-BE parte N](2026-11-04_TO-BE_v0.1_parteN.png)

## Los pasos

| # | Paso del flujo | Tarea | Carril (responsable) | Disparador | Entra | Sale | Evento que se registra | Requerimientos | Meta | Punto del AS-IS que resuelve |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | P1 | | | | | | | | | ❶–❺ |

## Compuertas y excepciones

| Compuerta o excepción | Qué pasa en cada salida | Escenario |
|---|---|---|

## Qué se valida en el taller
- (decisiones abiertas: CON-xx, PEN-xx)

## Supuestos
- (lo que no viene de una fuente ni de Torvesa)
```

**Cómo sé que una parte está terminada:** cada paso tiene **disparador y responsable**, cada requerimiento de la parte aparece al menos una vez y cada punto ❶–❺ del AS-IS que le toca está resuelto o explicado.
