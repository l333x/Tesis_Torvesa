---
titulo: "Documento maestro del proyecto: tesis Torvesa (para leer o subir a cualquier IA)"
version: v0.1
fecha: 2026-11-10
autor_borrador: "Claude (Víctor revisa)"
uso: "Se sube a cualquier asistente de IA para que sepa de qué trata el proyecto, qué está hecho, qué se evalúa y qué falta. No reemplaza a la bóveda: es su resumen."
tags: [maestro, resumen, estado]
---

# Documento maestro del proyecto (10 de noviembre de 2026)

> [!important] Cómo usar este documento con una IA
> Súbelo completo y dile: «Este es el estado de mi tesis. Úsalo como contexto y respeta sus reglas». Las reglas de la sección 2 son obligatorias: no inventar cifras ni fuentes, y distinguir siempre **dato**, **supuesto** y **prueba con datos ficticios**.

## 1. Qué es el proyecto

- **Tesis** de la Universidad Politécnica Salesiana (Quito), carrera de Negocios Digitales, modalidad Proyecto Técnico.
- **Título:** «Diseño de un sistema de automatización para la gestión comercial en la Constructora Torvesa».
- **Autores:** Víctor Segura (tesis, fuentes, metodología, modelo de negocio y finanzas) y Diego Bermeo (todo lo técnico). **Tutora:** Ing. Tania Chicaiza.
- **Fecha límite:** lunes 4 de enero de 2027, con el documento final completo para la revisión de la tutora.
- **El problema:** los clientes de Torvesa escriben al WhatsApp personal de socios e ingenieros que están en obra. El mensaje se lee horas después, se delega sin dejar rastro, cada cotización se arma desde cero y, si alguien se va de la empresa, se lleva el historial en su celular. Nadie sabe cuántos clientes se pierden ni por qué.
- **La solución que se diseña:** sobre TEAMSLASH (un registro de solicitudes que los autores ya habían hecho) se agregan tres componentes:
  1. una **bóveda de conocimiento comercial** en Obsidian (la memoria de la empresa: fichas de clientes, historial y plantillas);
  2. un **asistente de IA** que propone borradores de cotización a partir de la bóveda, sin precios, citando los documentos que usó y siempre revisado por una persona;
  3. un **registro verificable** de eventos con huellas SHA-256, sin datos personales.
- **Metas que se medirán (M1 a M6):** tiempo de primer contacto (menos de 15 minutos), tiempo de cotización, clientes perdidos, recuperación del historial, detección de alteraciones del registro y usabilidad.

## 2. Reglas que no se negocian

1. **Nunca decir «piloto» ni «implementado».** Se dice «validación del diseño en operación experimental controlada».
2. **Fuentes:** solo se cita lo verificado (abierto, con el dato y la página). Nunca inventar autores, DOI, páginas ni cifras. Si la evidencia contradice el borrador, se dice.
3. **Los datos del diagnóstico de 30 personas son simulados: no se usan.** El censo de 5 personas del Informe Final (p. 10) sí es real y se usa como antecedente, no como línea base.
4. **Datos personales:** no se recogen datos de personas (encuestas, entrevistas) mientras la tutora no decida; la prueba de concepto usa solo datos ficticios.
5. **Marcadores en los borradores:** `[FALTA-FUENTE]`, `[FALTA-DATO]`, `[DECIDIR-TUTORA]`, `[DECIDIR-VÍCTOR]`, `[VERIFICAR-PÁG]`. Nunca llegan a la versión final.
6. **Dos públicos:** los archivos `.md` son para la IA; los Word y PDF son para personas, en lenguaje simple.
7. **Versiones:** la IA genera, Víctor edita, sale una versión nueva. Nunca se sobrescribe una versión que Víctor editó.
8. **Formato:** APA 7 en español y estructura UPS (ver `MANUAL_TESIS.md` en la bóveda).

## 3. Estado al 10 de noviembre de 2026

- **Avance real: 36 %** de las tareas, con el 35 % del tiempo transcurrido. Diego 47 %, Víctor 39 %.
- **Tesis:** borrador 2 completo (65 páginas). Caps. I a III en versión 0.3; Cap. IV (diagnóstico, diseño y viabilidad) en 0.2; Caps. V y VI en esquema con la prueba de concepto descrita.
- **Fuentes:** más de 100 fichas verificadas en la bóveda.
- **Prototipo (todo con datos ficticios):** el recorrido completo funciona en internet: formulario web con consentimiento → servidor → aviso al equipo en Slack → botón «Tomar» → ficha en la bóveda → borrador de cotización del asistente → revisión de una persona.
  - Primera prueba: borrador de una cocina de 12 m² en 15 segundos, sin precios y con 11 preguntas.
  - El registro detectó 3 de 3 alteraciones.
  - Programado pero sin publicar ni probar: recordatorio a los 15 minutos, motivo de pérdida obligatorio, estado «Cotizada» y reporte de los lunes.
- **La tutora todavía no ha visto el borrador** (la Revisión 1 no se ha hecho; el mensaje para pedir la cita está sin enviar).
- **Torvesa todavía no autoriza** el acceso a sus documentos ni la validación con su equipo. Es la ruta crítica.

## 4. El censo de la empresa (único dato real de Torvesa)

Censo a 5 personas de la gerencia y la operación, mayo de 2026 (Informe Final, p. 10):

| Hallazgo | Frecuencia |
|---|---|
| Pasa más de la mitad de su jornada en obra | 3 de 5 |
| Revisa los mensajes cada 3 o 4 horas, o solo al llegar a casa | 3 de 5 |
| Los clientes le escriben a su WhatsApp personal | 4 de 5 |
| El primer contacto debería darse en menos de 15 minutos | 4 de 5 |
| Considera crítico revisar cada semana por qué se pierden clientes | 3 de 5 |

**La brecha:** la empresa quiere responder en 15 minutos y hoy revisa los mensajes cada 3 o 4 horas.

## 5. El proceso estrella

**«Primer contacto garantizado en 15 minutos»** (nombre por decidir): captura de la solicitud → código y hora de llegada → aviso al celular en 5 segundos → alguien pulsa «Tomar» y queda como responsable → hora del primer contacto → si nadie la toma en 15 minutos, aviso a la gerencia → cierre con motivo de pérdida obligatorio → reporte cada lunes.

- **Tres niveles del producto:** (1) primer contacto garantizado; (2) memoria comercial (la bóveda); (3) cotización asistida. Cada uno necesita el anterior.
- **Escala** a otras constructoras, remodelación, inmobiliarias y proveedores de materiales cambiando solo la configuración. Cada empresa tiene su propia base de datos y su propia bóveda.

## 6. Por qué nosotros y no otra empresa

1. **Hecho con los datos de la propia empresa:** la meta de 15 minutos la fijó el equipo de Torvesa.
2. **Pensado para quien está en obra:** un aviso de texto y un botón.
3. **Se vende un resultado medible, no licencias:** cada lunes, cuántos clientes llegaron, en cuántos minutos se atendieron, cuántos se perdieron y por qué.
4. **La memoria es de la empresa:** la bóveda son archivos de texto que Torvesa puede llevarse.
5. **La IA ayuda, no decide:** no pone precios ni envía nada sola.
6. **Protección de datos desde el diseño** (ley ecuatoriana de datos personales, LOPDP).

Los CRM comerciales (HubSpot, Zoho, Pipedrive, Bitrix24, Odoo) cubren el seguimiento de ventas, pero no la memoria comercial, ni el asistente que cita los documentos de la empresa, ni el registro verificable.

**Lo que todavía no se puede prometer:** no hay resultados con datos reales; el equipo es de dos personas; el beneficio en dinero es un cálculo con supuestos.

## 7. Cuánto cuesta y cuánto se gana

> [!warning] Los precios de los servicios son oficiales. Los sueldos, volúmenes y montos de Torvesa son **supuestos** hasta que la empresa entregue sus datos.

### 7.1 Torvesa como cliente (escenario base, estudio de costos v0.2)

| | Lo opera por su cuenta | Lo contrata como servicio (nivel 3) |
|---|---|---|
| Inversión inicial | USD 2.893 | USD 470 |
| Gasto total al mes | USD 265 | USD 162 |
| VAN a 3 años (pesimista / base / optimista) | −10.378 / 12.388 / 69.301 | −3.490 / 15.832 / 70.357 |
| ROI base a 3 años | 173 % | 347 % |
| Meses para recuperar la inversión (base) | 7,6 | 1,1 |
| Obras recuperadas al año que pagan el sistema | 2,1 | 1,3 |

- **Antes y después:** se liberan unas 41,7 horas al mes (USD 354) y las obras recuperadas suman USD 450: beneficio de unos USD 804 al mes.
- **Capacitar al equipo:** unas 20 horas, alrededor de USD 170.
- **La clave:** el sistema se paga si la empresa recupera unas 2 o 3 obras al año. Solo con el ahorro de tiempo casi no se paga.
- **El escenario pesimista pierde dinero**, y se dice. En ese caso lo sensato es solo el nivel 1.

### 7.2 TEAMSLASH como negocio (nosotros como proveedores)

| | Arranque | Crecimiento | Formal |
|---|---|---|---|
| Costo al mes, con el tiempo de los fundadores | USD 1.571 | USD 2.989 | USD 7.436 |
| Lo que sale de caja al mes | USD 161 | USD 874 | USD 4.566 |
| Clientes para no perder caja | 3 | 15 | 78 |
| Clientes para cubrir todo (punto de equilibrio) | 27 | 51 | 126 |

- **Precios propuestos (sin prueba de mercado):** USD 49, 99 y 149 al mes por nivel. Atender a un cliente cuesta USD 10,95, 36,55 y 41,39.
- **Costo de una hora de trabajo:** desarrollo, USD 8,50; soporte o ventas, USD 5,20 (sueldos supuestos, con cargas de ley).
- **Recomendaciones:** trabajar desde casa (USD 18 por persona al mes, frente a unos USD 217 en coworking); usar los equipos propios; los fundadores mantienen el núcleo y los módulos separables se encargan a un independiente con cesión de derechos; un pasante desde unos 10 clientes.
- **Punto débil:** al tamaño formal harían falta 126 clientes y el equipo solo atiende 119: a ese tamaño el precio no alcanza. Lo que más pesa es el soporte.

### 7.3 Herramientas, bóveda y AWS

- **Gana el conjunto de herramientas del prototipo** (servidor Railway, página en Vercel, avisos por Slack, Obsidian y Claude por consumo): 4,14 de 5 y unos USD 9.039 en 3 años, frente a CRM comerciales, Microsoft y AWS.
- **Dónde vive la bóveda:** Obsidian con sincronización (unos USD 23 al mes). **Asistente:** pago por consulta (unos USD 2 al mes por 150 consultas). Una suscripción de USD 20 al mes por persona solo conviene desde unas 1.538 consultas al mes.
- **Si la IA falla o se acaban las consultas:** tope de gasto, modelo de respaldo, borradores guardados y modo sin IA. El primer contacto en 15 minutos no depende de la IA.
- **«Entrenar» un modelo en AWS con la bóveda no conviene hoy:** mantenerlo cuesta unos USD 17.155 al mes, no cita sus fuentes y guarda datos personales dentro. Lo correcto es **buscar en la bóveda** (RAG). La capa gratuita de AWS (crédito de USD 100 a 200, 6 meses) sirve para probar, no para operar. AWS queda como ruta para crecer con varias empresas.

## 8. FODA en resumen

- **Fortalezas:** prueba de concepto funcionando · registro que detecta alteraciones · datos personales protegidos · una persona revisa siempre · costo bajo.
- **Debilidades:** sin datos reales aún · censo pequeño · depende de terceros · equipo de dos personas · clave del servidor expuesta.
- **Oportunidades:** la construcción se recupera (+2,7 % en 2025, tras −7,9 % en 2024) · el 83,9 % de la población usa internet · pocas pymes usan IA · la ley obliga a ordenar los datos · el proceso sirve a otras empresas.
- **Amenazas:** cortes de luz (hasta 12 horas en 2024) · falta de autorización · IA personal sin reglas · CRM comerciales · que el equipo no lo adopte.

## 9. Decisiones tomadas y pendientes

**Tomadas:** validación en lugar de «piloto» (D1); marco DSR + Design Thinking + Scrum (D2); dos censos (D4, en revisión por el cambio de método); entrega el 4-ene-2027 (D5); huellas SHA-256 en lugar de OpenTimestamps (D6); VAN y TIR para Torvesa y el negocio TEAMSLASH como anexo (D7).

**Pendientes de la tutora:** medir sin datos de personas (DEC-21 a DEC-23); enfoque cuantitativo; cómo se evalúa la usabilidad (M6); criterios y pesos de la matriz de herramientas.

**Pendientes de Víctor:**
- las 7 respuestas a Diego (tres casos de prueba o cuatro; cuándo cuenta el primer contacto; cinco estados; ancla semanal de la huella; 20 alteraciones en la prueba; modelo de IA; carpeta de contactos);
- nombre del proceso estrella y meta de solicitudes atendidas a tiempo (se propone 80 %);
- qué se ofrece a Torvesa después de la tesis;
- si el Cap. IV pasa a las cifras del estudio de costos v0.2;
- cuál de los dos tableros de Trello se queda;
- los 29 cambios de estado propuestos para el cronograma.

## 10. Lo que falta (ruta crítica al 4 de enero)

1. **Cita con la tutora** (Revisión 1): el mensaje está redactado y sin enviar.
2. **Autorización de Torvesa.** Fecha tope propuesta: 20 de noviembre. Si no llega, plan B: medir solo con casos de prueba (M2, M4 y M5).
3. **Separar las claves del servidor** antes de usar datos reales (hoy la clave de la página pública también permite leer las solicitudes).
4. **Validación:** 23 de noviembre a 5 de diciembre → medición → resultados → envío a la tutora el 14 de diciembre, sin holgura.
5. **Sin verificar todavía:** IVA del 15 % (decreto), aporte patronal al seguro social, normas ISO, la cifra de «siete veces» de Oldroyd (2011), uso de WhatsApp en Ecuador, normativa de pasantías, y varios precios leídos por extracción automática.

## 11. Dónde está cada cosa (en la bóveda `Tesis_Torvesa`)

| Qué | Dónde |
|---|---|
| Borrador de la tesis | `06_Capitulos/2026-11-10_Tesis_Borrador2_v0.3.docx` y `.pdf` |
| Estudio de costos (Excel con fórmulas, Word y PDF) | `06_Capitulos/Modelo_Negocio/2026-11-10_Estudio_Costos_v0.2.*` |
| Modelo financiero y matriz de herramientas v0.1 | `06_Capitulos/Modelo_Negocio/2026-11-10_Modelo_Financiero_v0.1.xlsx` y `..._Matriz_Herramientas_v0.1.xlsx` |
| Necesidad, contexto de Ecuador y FODA | `06_Capitulos/2026-11-10_Necesidad_Contexto_FODA_v0.1.*` |
| Proceso estrella, pitch, guía de negociación, por qué nosotros | `06_Capitulos/Modelo_Negocio/2026-11-10_*` |
| Figuras y su índice | `06_Capitulos/Figuras/` |
| Revisión de los flujos | `07_Flujos_Diseno/2026-11-10_Revision_Flujos.md` |
| Gantt y revisión del cronograma | `11_Planificacion/2026-11-10_Gantt_Tesis_v0.1.xlsx` y `2026-11-10_Revision_Cronograma.md` |
| Respuestas propuestas a Diego | `00_Inbox/2026-11-10_respuestas_Victor_a_Diego_PROPUESTA.md` |
| Fichas de fuentes | `02_Fuentes/` |
| Tablero de Miro (privado) | https://miro.com/app/board/uXjVEP28Oyg=/ |
| Tablero de Trello (privado) | https://trello.com/b/VdkwofqC |
| Prototipo en línea (datos ficticios) | https://teamslash-torvesa.vercel.app |

## 12. Pitch de un minuto

> Ingeniero, su equipo ya nos dio la respuesta: 4 de cada 5 dicen que un cliente no debería esperar más de 15 minutos. Pero 3 de cada 5 revisan los mensajes cada 3 o 4 horas, o al llegar a casa. No es falta de ganas: están en obra.
>
> Torvesa no pierde clientes en la obra. Los pierde en la primera hora, en un WhatsApp personal, y nadie se entera de por qué.
>
> La construcción cayó 7,9 % en 2024 y volvió a crecer en 2025. Los clientes están volviendo. El que responde primero se los queda.
>
> Nuestro sistema avisa en segundos al celular, un solo botón asigna al responsable y, si a los 15 minutos nadie respondió, le avisa a usted. Cada lunes sabrá cuántos clientes llegaron, en cuántos minutos se atendieron y por qué se perdieron.
>
> Ya funciona con datos de prueba. Le pedimos dos semanas para probarlo con su equipo.
