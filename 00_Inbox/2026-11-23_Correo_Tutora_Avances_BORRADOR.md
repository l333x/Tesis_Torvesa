---
titulo: "Correo a la tutora: borrador 4 v0.3, presentación v0.4 y cuadro de 9 dudas"
para: "Ing. Tania Chicaiza, tutora"
cc: "Diego Bermeo"
canal: correo (Outlook de la UPS)
estado: BORRADOR (sin enviar; lo envía Victor)
fecha: 2026-11-23
adjuntos: "06_Capitulos/2026-11-23_Tesis_Borrador4_v0.3.pdf y .docx · 08_Reuniones_Tutora/2026-11-23_Revision2_Presentacion_v0.4.pdf"
tareas: "S6-T04 (Revisión 2) · DEC-18 a DEC-23 y DEC-25"
reemplaza: "00_Inbox/2026-11-22_Correo_Tutora_Avances_BORRADOR.md (no se envió; pedía reunión el lunes 23, que ya es hoy, y llevaba las cifras viejas)"
---

# Correo a la tutora (23-nov)

**Asunto:** Tesis Torvesa: borrador 4 para su revisión y reunión esta semana

Buenos días, Ing. Chicaiza. Le saluda Victor Segura, junto con Diego Bermeo (tesis de la Constructora Torvesa).

Como por los horarios no hemos podido coincidir para la revisión, le enviamos los avances por este medio para que pueda verlos con tiempo. Nos gustaría reunirnos con usted el miércoles 25 o el viernes 27, en el horario que le quede mejor, presencial o en línea. ¿Nos podría indicar el día y la hora?

Le adjuntamos:

1. El borrador 4 de la tesis (84 páginas), en PDF y en Word para que pueda corregir sobre él. Al inicio hay una nota con lo que cambió, una lista de siglas y un glosario. Lo resaltado en amarillo es lo que falta o lo que usted decide.
2. La presentación de la revisión (13 diapositivas), que resume el avance y las decisiones que le pedimos.

Desde el borrador 3 avanzamos en el diseño. En el capítulo IV están los mapas del proceso de atención tal como funciona hoy en la empresa y del proceso con el sistema, este último en tres partes, y con ellos comprobamos que 19 de los 24 requisitos ya aparecen en el flujo. Después priorizamos los 10 requisitos clave, de los que 4 quedan como imprescindibles, y armamos el plan de trabajo del sistema en 2 ciclos. También corregimos el análisis económico. Contábamos dos veces las firmas electrónicas, y al quitar el duplicado el plan más completo queda en USD 270 al mes, con un valor actual neto de USD 380 para nosotros y de USD 13.755 para Torvesa. Además dejamos dicho que hoy solo 1 de los 22 datos de la empresa que usa el modelo es propio de Torvesa. El resto son supuestos hasta que la empresa nos entregue su información.

La validación del diseño quedó prevista desde el 30 de noviembre, porque depende de su decisión sobre el método y de la autorización de Torvesa. La entrega del 4 de enero se mantiene.

Por eso le pedimos dos cosas con fechas distintas. La primera es su respuesta sobre el punto 1 del cuadro (medir sin encuestas ni entrevistas) en la reunión de esta semana, porque de ella depende cuándo empezamos en Torvesa. La segunda, si le es posible, es la revisión completa del borrador hasta el lunes 30 de noviembre.

Para ubicarse rápido en el borrador: las metas M1 a M6 son las 6 cosas que medimos para saber si el sistema funciona (capítulo I). M1 es responder al cliente en menos de 15 minutos. M2 es hacer una cotización en menos tiempo. M3 es perder menos clientes antes del primer contacto. M4 es encontrar el historial de un cliente aunque lo haya atendido otra persona. M5 es detectar el 100 % de los cambios hechos a escondidas en el registro. M6 es que el sistema sea fácil de usar. Los casos de prueba (CP-01 a CP-04) son pruebas cronometradas que hacemos nosotros con datos ficticios. La validación del diseño en operación experimental controlada son las 2 semanas en que el equipo de Torvesa usaría el sistema con pedidos reales. Cada decisión que le pedimos tiene un código (DEC) para que la encuentre resaltada en amarillo en el borrador.

| N.º | Lo que necesitamos que nos ayude a decidir | Por qué lo preguntamos | Nuestra propuesta |
|---|---|---|---|
| 1 | **Medir sin encuestas ni entrevistas (DEC-21).** ¿Podemos medir las metas solo con documentos de la empresa (fechas y horas de los pedidos), los registros del propio sistema y nuestros casos de prueba? ¿Hay que informar a la Dirección de Carrera? | La Dirección nos indicó el 2 de noviembre que recoger datos de personas necesita otra autorización, más larga que el plazo del 4 de enero. De esta respuesta depende la fecha de la validación en Torvesa. | Sí, y lo declaramos como limitación. |
| 2 | **El enfoque de la investigación (DEC-22).** Si no hay entrevistas, ¿el enfoque pasa de "mixto con predominio cuantitativo" a "cuantitativo"? | Sin parte cualitativa con personas, el enfoque mixto ya no se sostiene. Cambia el capítulo III. | Sí, si acepta el punto 1. |
| 3 | **Cómo medir la facilidad de uso, M6 (DEC-23).** ¿Cambiamos el cuestionario SUS (10 preguntas a los usuarios) por una evaluación heurística, en la que nosotros revisamos el sistema con una lista de principios de diseño? | El SUS es un cuestionario a personas, y por el punto 1 no podríamos aplicarlo. | Sí, como cuarto caso de prueba (CP-04). |
| 4 | **Redacción del tercer objetivo específico (DEC-18).** ¿Puede decir "desarrollar un prototipo funcional de los componentes"? | Así describe mejor lo que entregamos: un prototipo que funciona, no un sistema terminado. | Sí. |
| 5 | **Nombre del diseño (DEC-19).** Medimos un solo grupo (el equipo de Torvesa) antes y después del sistema. ¿Lo llamamos "preexperimental" o "comparación antes y después en un solo grupo"? | Queremos usar el término que usted considere correcto en el capítulo III. | Lo que usted indique. |
| 6 | **Responsable de los datos personales (DEC-20).** ¿Quién figura como responsable del tratamiento de los datos de los clientes: la empresa, nosotros o la universidad? ¿Hace falta un comité de ética? | La Ley Orgánica de Protección de Datos Personales lo exige y la citamos en el capítulo IV. | Lo que usted indique. |
| 7 | **Encuesta de otra materia (DEC-25).** Para la materia de Ingeniería de Requerimientos hicimos una encuesta corta (modelo de Kano) a 7 personas de otras empresas, sobre qué funciones del sistema valoran más. ¿La citamos en la tesis o la dejamos fuera? | Ayuda a priorizar las funciones, pero no es gente de Torvesa y es una encuesta a personas (ver el punto 1). | Citarla solo como antecedente, con su limitación. |
| 8 | **Carta de respaldo.** ¿Nos podría dar una carta corta para que Torvesa autorice la validación? | Torvesa todavía no autoriza las 2 semanas de uso del sistema, y eso es lo que más puede retrasar la tesis. | Una carta de la tutoría. |
| 9 | **Forma de devolver las observaciones.** ¿Prefiere corregir sobre el Word, por correo o en la reunión? | Para organizarnos y tener todo corregido antes del 4 de enero. | Sobre el Word, con control de cambios. |

Muchas gracias por su tiempo.

Saludos cordiales,

Victor Segura Heredia y Diego Bermeo Torres
Tesis: Diseño de un sistema de automatización para la gestión comercial en la Constructora Torvesa

---

**Nota para Victor (no va en el correo):**
- Adjuntos: `2026-11-23_Tesis_Borrador4_v0.3.pdf`, `2026-11-23_Tesis_Borrador4_v0.3.docx` y `2026-11-23_Revision2_Presentacion_v0.4.pdf`. Están solos en el Escritorio, en `TESIS - CORREO TUTORA LISTO 23-nov`.
- Qué cambió frente al borrador del 22-nov: las fechas (el lunes 23 ya es hoy: ahora miércoles 25 o viernes 27, DEC-21 en esa reunión y revisión completa hasta el lunes 30), el borrador v0.3 y la presentación v0.4 con las cifras del Excel v0.3, el párrafo de los mapas de procesos, "Victor" sin tilde y la firma con los dos apellidos.
- Si en Outlook ya tienes el borrador del 22-nov, bórralo para no mandar el viejo.
- Pon a Diego en copia.
