---
titulo: "Mensaje a Diego: correcciones del Deber 1, cómo armar el Deber 2, Strix y el PR del código"
para: "Diego Bermeo"
canal: WhatsApp o correo
estado: BORRADOR (lo envía Víctor)
fecha: 2026-11-23
---

# Mensaje a Diego (23-nov)

Diego, revisé tu Deber 1 junto al mío. Está bien hecho: usamos los mismos 7 encuestados y nos salen las mismas categorías de Kano. Te paso lo que hay que corregir, cómo armar el Deber 2 y lo del código.

**1. Correcciones de tu Deber 1** (si todavía lo puedes cambiar, si no, anótalo para la tesis)
1. **APA:** citas tres presentaciones como "Proaño Delgado (2026)". Si tienen el mismo autor y el mismo año, van 2026a, 2026b y 2026c, en la lista y en el texto.
2. **Fecha vieja:** dice "la prueba en Torvesa (del 23 de noviembre al 5 de diciembre)". Ahora es la validación del diseño, prevista desde el 30 de noviembre. Mejor no decir "prueba".
3. **Códigos sin explicar:** OBJ-01 a OBJ-07, NEC-03 y CON-06. Agrega una nota como la que pusiste para los INT.
4. **Cantidad de requisitos:** dices 23 y son 24. RQ-24 es la hora del primer contacto, que está en la tesis.
5. **Detalles:**
   - iniciales con el mismo formato ("M. M.", "E. R.", "C. R.");
   - "Atención" con tilde;
   - cargos en minúscula ("analista de compras").

**2. En qué pensamos distinto (no es un error, pero hay que decidirlo para la tesis)**
- **Must:** yo dejé 4 (30 h, 23 %) y tú 6 (54 h, 50 %). Tu argumento de las dependencias me parece más sólido: RF-003 necesita las cuentas (RNF-003) y el borrador necesita el historial. Propongo que en la tesis vayan como Must el registro, el aviso, el responsable, el permiso y las cuentas. Hablémoslo.
- **Horas:** yo estimé 130 h y tú 108 h. Para la tesis necesitamos una sola estimación, y tú conoces mejor el código.
- **Lista de 12 puntos:** yo usé la de la plantilla de elicitación (sección 11.1) y tú la de las diapositivas 18 y 19 de "Validación, Verificación y Gestión". Pásame esa presentación. En el Deber 2 tenemos que verificar con la misma lista los dos.

**3. Tu Deber 2** (va en el mismo PDF que el mío: `Deber2_Historias_Validacion_Segura_Bermeo.pdf`)
- **Historias:** salen de tus 9 requerimientos de prioridad alta y media. Son 8 historias: mete RNF-002 como criterio de la historia del borrador, igual que hice yo. Cada una lleva:
  - "Como [rol] quiero… para…";
  - al menos 2 criterios Dado/Cuando/Entonces;
  - prioridad, puntos (1, 2, 3, 5, 8, 13) y el requerimiento de origen.

  Usa al menos 2 roles concretos, nunca "usuario".
- **INVEST:** la tabla de las 8 historias y una épica dividida. Te sirve el historial (RF-005, 16 h) o el borrador con IA (RF-006, 24 h).
- **Historia técnica:** que no sea la misma que la mía, porque yo usé la refactorización de los estados (Cerrado = Ganada, Archivado = Perdida). Tú puedes usar la deuda técnica DT-02, las consultas a la base fuera de `db.js`, con el formato de la plantilla de clase:
  - problema (antes) y cambio (después);
  - beneficio y riesgo;
  - cómo se verifica.
- **Spike:** también distinto al mío, que mide el tiempo del aviso en el servidor real. Te propongo uno sobre tu RF-003: cómo evitar que dos personas tomen la misma solicitud a la vez (bloqueo en PostgreSQL o transacción). Lleva:
  - pregunta, tiempo límite y alcance;
  - opciones que se comparan;
  - criterio de terminado.
- **Backlog:** 2 sprints de 2 semanas, que respeten tu prioridad y las dependencias. Lo que no entra queda para después.
- **Validación:** usamos el mismo stakeholder y una sola reunión por Teams: el jefe de equipo de ventas que respondió la encuesta (E7). Ya armé el guion y el acta (`Validacion_Deber2_Guion_Reunion_Teams` y `Validacion_Deber2_Acta_Stakeholder`): en el recorrido metemos también tus historias. Necesitamos su fecha y hora para invitarlo.
- **Verificación cruzada:** tú revisas mis historias y yo las tuyas, con INVEST y la misma lista de 12 puntos, en el formato de 5 campos. Mi informe es `Deber2_Historias_Validacion_Segura_Bermeo_parte_Victor.pdf`. Mándame tus historias apenas las tengas.
- **Reflexión:** un párrafo sobre qué encontró la validación que la verificación no habría visto, y al revés.

**4. Código de la prueba de concepto**
- **El Pull Request en borrador:** te dejé uno en teamslash-api: https://github.com/psiceslivie/teamslash-api/pull/1 (hacia `rq18-consentimiento`, 4 commits; las 6 suites de pruebas pasan: con el cambio el formulario responde en unos 60 ms aunque Slack no conteste; antes tardaba 4 s). Trae:
  - la respuesta al formulario sin esperar los avisos, con un tiempo límite de 4 s;
  - el código muerto quitado;
  - comentarios "atajo:";
  - un `AGENTS.md` con las reglas para tu IA;
  - `docs/TAREAS_DIEGO.md` con lo que te toca, en orden.

  Revísalo, corre `npm test` y, si estás de acuerdo, haz tú el merge. No lo desplegué. **Ojo:** si Railway despliega desde `rq18-consentimiento`, el merge lo publica en producción, así que confírmalo antes.
- **Urgente, seguridad:**
  - en el historial de teamslash-landing (`js/main.js`, commits `4dc05a2`, `d31227b` y `7a948a6`) quedaron claves antiguas del API que hasta el 15-nov podían leer y cambiar solicitudes. Confirma en Railway que la clave privada actual es otra; si no, rótala ya;
  - la revisión encontró, cada una con su caso:
    - no hay límite de peticiones;
    - no hay esquema ni largo máximo (una descripción de 50.000 caracteres pasa);
    - el texto del cliente no se escapa en Slack (`<!channel>` avisa a todo el canal);
    - Telegram acepta cualquier petición si falta el secreto;
    - un JSON mal formado devuelve el error interno.

  Todo está en `docs/TAREAS_DIEGO.md`, en orden.
- **El formulario (landing)** cumple 4 de los 7 puntos de la lista: falta validar al salir del campo, mejorar el aviso de error y poner un aviso de tiempo agotado con "Reintentar".
- **Con tu IA:** abre tu IA en la carpeta del repo y dile "Lee AGENTS.md y docs/TAREAS_DIEGO.md y haz la tarea 1; al terminar corre npm test y explícame qué cambió". Sigue así, tarea por tarea.
- **Strix:** sí lo vamos a usar, para encontrar las vulnerabilidades del código. Reglas:
  - **solo contra una copia local** de la API con datos simulados, nunca contra Railway ni nada real;
  - `STRIX_TELEMETRY=0`, `--max-budget 5` e instalación con versión fija por pipx o uv;
  - los pasos están en `AGENTS.md` y en `IA_DIEGO.md` §8.5;
  - cada hallazgo se verifica a mano antes de arreglarlo, y el reporte me lo pasas con el formato de 4 partes.
- **Antes de la validación:** pasa la lista de seguridad (§8.1) y la del formulario (§8.4).

**5. Torvesa, esta semana**
- Datos de la empresa: actividad en el SRI, tipo de sociedad y formularios 101 de 2023 a 2025.
- Autorización de la validación desde el 30-nov.
- Si la gerencia aprueba las cotizaciones antes de enviarlas, y en qué país está el servidor.

**6. Tus horas** del levantamiento al día de hoy.
