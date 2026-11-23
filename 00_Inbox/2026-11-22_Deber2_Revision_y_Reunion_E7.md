---
titulo: "Deber 2: revisión del PDF combinado, verificación de Víctor a Diego y guía de la reunión con E7"
fecha: 2026-11-22
fuente: "Downloads/Deber2_Historias_Validacion_Segura_Bermeo_FINAL.pdf (23 páginas)"
estado: BORRADOR (lo envía Víctor)
---

# Mensaje para Diego (copiar a WhatsApp)

Diego, revisé el PDF final. Tu parte está bien armada. Te paso tres cosas.

**1. Mi parte ya está corregida.** Reemplaza las páginas 1 a 13 por `Deber2_Historias_Validacion_Segura_Bermeo_parte_Victor_v3.pdf`. Le apliqué todo lo que me marcaste:
- HU-01 en «Parcial»;
- HU-02 con los 5 s y el caso de Slack caído;
- HU-03 «al llamar»;
- HU-04 sin «reasignar», con el criterio 4;
- HU-05 con «4 de 5»;
- HU-06a, b y c en la tabla INVEST;
- HU-06c sin dependencia;
- HU-08 con la cuenta desactivada;
- «Dada» y «Dadas»;
- la explicación de 2 y 3 puntos.

También arreglé la Tabla 16, que tenía la fecha y la duración fuera de las celdas. Decía que validamos con «una persona de Torvesa» y lo cambié, porque E7 no es de Torvesa: así coincide con tu parte. Quité además a Martin (2008), que estaba en las referencias y no se citaba.

**2. Mi verificación de tus historias.** Pon esto en tu Tabla 18 en lugar de «todo OK». El profe va a desconfiar si una revisión no encuentra nada, y tu reflexión ya dice que la verificación sirve para encontrar estas cosas.

| Historia | Tipo | Criterio que falla | Por qué falla | Propuesta de mejora |
|---|---|---|---|---|
| HU-02 | Verificación | Punto 7 (consistente con el documento) | El criterio 1 dice «10 de 10 pruebas» y «llegó al celular», pero la medida del RF-002 es en el canal del equipo y sobre 20 pruebas (19 de 20). «Llegó al celular» no se puede comprobar en una prueba | «…entonces el aviso ya está en el canal del equipo comercial, en al menos 19 de 20 pruebas» (o la medida exacta de tu RF-002) |
| HU-05b | Verificación | Punto 8 (cubre todo el requerimiento) | Al dividir la épica se perdió la medida de los 2 minutos para encontrar el historial de un cliente ajeno (meta M4, CP-02). HU-05a mide 2 segundos de búsqueda, que es otra cosa | Agregar el criterio 3: «Dado un cliente atendido por otra persona, cuando un colaborador lo busca, entonces encuentra su historial en 2 minutos o menos» |
| HU-06 | Verificación | INVEST: pequeña | Tiene 4 criterios que cubren 3 cosas distintas: armar el borrador, proteger los datos ante la IA y no enviar sin aprobación. La aprobación no depende del asistente | Dejar el criterio 4 como historia aparte («Como gerente, quiero que ningún borrador llegue al cliente sin aprobación…», 2 o 3 puntos) o justificar en la Tabla 9 por qué queda junta. La S pasa a «Parcial» |
| HU-07 | Verificación | Punto 5 (completo) | Guarda la fecha y la hora del permiso, pero no qué versión del aviso de privacidad aceptó el cliente. Sin la versión no se puede probar qué aceptó (LOPDP) | «…el permiso queda guardado con la fecha, la hora y la versión del aviso aceptado» |
| HU-05b | Verificación | INVEST: independiente | Está con I = Sí porque «la ficha se abre desde el aviso», pero el aviso es HU-02 | I = Parcial: «Se abre desde el aviso de HU-02 o desde la búsqueda de HU-05a» |
| HU-01, HU-03, HU-04, HU-05, HU-05a, HU-05c, HU-08, HT-01, SP-01 | Verificado OK | | | |

Con esto:
- **cambia tu reflexión:** «la verificación de Víctor no encontró problemas» ya no va. Pon algo como: «encontró una medida que no coincidía con mi Deber 1 (HU-02), una medida que se perdió al dividir la épica (HU-05b), una historia que hacía tres cosas (HU-06) y un dato que faltaba para la LOPDP (HU-07)»;
- **aplica los cambios** en tu sección 2 y anota debajo de la Tabla 18: «Los cambios ya están aplicados en la sección 2».

**3. Detalles de tu parte**
- HT-01 dice «Tipo: Deuda técnica». Pon «Refactorización (deuda técnica DT-02)», porque el deber pide una historia técnica y esto es una refactorización.
- En la portada, «Usabilidad y UX» va con mayúscula, igual que en la mía.

**4. La reunión con E7** está puesta para hoy a las 18:30. Los hallazgos de las Tablas 17 todavía no son datos: tienen que salir de lo que él diga. Si dice algo distinto, se cambian.

# Guía de la reunión (30 min, Teams)

**Antes:**
- Mandarle el enlace.
- Tener abiertos el guion (`Validacion_Deber2_Guion_Reunion_Teams`) y las historias de los dos.
- Pedirle permiso para la captura de pantalla; se puede tomar con la cámara apagada.

**Primeras preguntas (abiertas, sin darle la respuesta):**
1. Cuando entra un pedido nuevo, ¿cómo se entera hoy y en cuánto tiempo llama?
2. ¿En qué momento se da por «tomado» un cliente: cuando lo ve, cuando lo llama o cuando le manda la cotización? Confirma HU-03.
3. Si está en obra, ¿quién atiende? ¿Le parece posible contactar en 15 minutos? Confirma HU-04.
4. ¿Le sirve un aviso en Slack o el equipo usa WhatsApp? Confirma HU-02.

**Recorrido:**
- Leer las historias de cada uno (las tuyas primero, luego las de Diego), en una línea cada una.
- Preguntar «¿así trabajan?», «¿qué cambiaría?» y «¿el criterio es realista?».

**Anotar:**
- la hora de inicio y de fin, que es la duración;
- sus palabras textuales en cada hallazgo;
- todo cambio que pida, aunque sea uno solo.

**Al final:**
- Leerle los hallazgos y que firme el acta (`Validacion_Deber2_Acta_Stakeholder`).
- El acta firmada y la captura van a `05_Datos_Campo/_crudo/` y no se suben a GitHub.
- En el PDF va solo la captura, sin su nombre completo.

**Después:**
- Completar en las dos partes la duración y la Figura 1.
- Si cambió algún hallazgo, ajustar las Tablas 17, las historias y la reflexión.
- Unir los dos PDF y entregar.
