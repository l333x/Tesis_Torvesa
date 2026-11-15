---
titulo: "Caso de negocio: de la necesidad de Torvesa a un servicio por suscripción"
version: v0.1
fecha: 2026-11-15
autor_borrador: "Claude (Frente B); Víctor revisa"
base: "Por qué nosotros v0.1 · Pitch v0.1 · Proceso estrella v0.1 · Guía de negociación v0.1 · Análisis financiero y matriz de herramientas v0.1 (10-nov) · Estudio de costos v0.3 (15-nov) · Necesidad, contexto y FODA v0.1 · Cap. IV v0.3 · Resumen de la prueba de concepto (8-nov) · censo n = 5 (Informe Final, p. 10) · DEC-16 (Estándar y Premium)"
publico: "Directora de carrera (Contabilidad y Auditoría) y tutora"
marcadores: "FALTA-DATO 13 · FALTA-FUENTE 3 · VERIFICAR 4 · DECIDIR-VÍCTOR 3"
uso: "Insumo del Cap. I (justificación), del Cap. IV (viabilidad) y de la exposición"
tags: [caso-de-negocio, modelo-negocio, propuesta-valor, comparativa, phva, saas, viabilidad, sprint5]
---

# Caso de negocio

> [!summary] En cuatro frases
> 1. **La necesidad:** en Torvesa, 4 de 5 personas dicen que un cliente no debe esperar más de 15 minutos, pero 3 de 5 revisan los mensajes cada 3 o 4 horas o al llegar a casa. Nadie registra quién atendió ni por qué se perdió un cliente.
> 2. **La oportunidad:** la construcción vuelve a crecer después de dos años de caída, el cliente ya está en línea y la IA cuesta centavos por consulta. Las pymes constructoras siguen entre las menos digitalizadas.
> 3. **La propuesta:** un servicio por suscripción en dos modelos. El **Estándar** garantiza el primer contacto y guarda la memoria comercial. El **Premium** agrega un asistente que arma borradores de cotización citando los documentos de la empresa, siempre revisados por una persona.
> 4. **La viabilidad** se muestra con el Excel del hilo principal. Aquí van la estructura y los marcadores, no las cifras.

> [!warning] Reglas de este documento
> - Toda cifra lleva fuente con ficha verificada, o un marcador.
> - Los datos del diagnóstico N = 30 y el Excel de ingresos 2025 son simulados: **no se usan**.
> - Del Informe Final de TEAMSLASH solo se usa el censo real de 5 personas (p. 10), confirmado por Diego el 8-nov.
> - La prueba de concepto del 8-nov usó **datos ficticios**. Torvesa todavía no usa el sistema.

---

## 1. La necesidad: qué pierde Torvesa hoy y por qué

### 1.1 El caso

Torvesa es una constructora de Quito. Su equipo comercial es el mismo equipo que dirige las obras: socios e ingenieros que pasan la jornada fuera de la oficina. Los clientes nuevos escriben al celular de quien conocen.

**Lo que dice su propio equipo** (censo a la gerencia y la operación, mayo de 2026):

| Hallazgo | Frecuencia |
|---|---|
| Pasa más de la mitad de la jornada en obra | 3 de 5 |
| Revisa los mensajes de clientes cada 3 o 4 horas | 2 de 5 |
| Revisa los mensajes solo al llegar a casa | 1 de 5 |
| Los clientes le escriben a su WhatsApp personal | 4 de 5 |
| El primer contacto debería ser en menos de 15 minutos | 4 de 5 |
| Le parece crítico revisar cada semana por qué se pierden clientes | 3 de 5 |
| Prefiere una alerta de texto simple o una tarjeta con enlace | 2 de 5 y 2 de 5 |

*Nota.* Bermeo y Segura (2026, p. 10). Es un censo de 5 personas, no una muestra: sirve de antecedente, no de línea base.

### 1.2 Qué se pierde

| Qué se pierde | Por qué | Evidencia | ¿Se mide hoy? |
|---|---|---|---|
| **Tiempo de respuesta** | Quien recibe el mensaje está en obra y lo ve horas después | Censo: 3 de 5 revisan cada 3–4 h o al llegar a casa | No |
| **Clientes** | El cliente que espera busca a otra empresa | El 83 % de los clientes espera atención inmediata (Salesforce Research, 2022, p. 16) | No: no se sabe cuántos se van [FALTA-DATO: solicitudes al mes y solicitudes perdidas, muestra documental de 3 meses] |
| **El motivo de cada pérdida** | Nadie lo anota | Censo: 3 de 5 lo consideran crítico, pero no hay registro | No |
| **La memoria comercial** | Las conversaciones y cotizaciones viven en celulares personales; si alguien se va, se las lleva | La rotación del personal agrava la amnesia institucional (Stark, 2024, p. 3) | No |
| **Horas de trabajo** | Cada cotización se arma desde cero | Los vendedores dedican el 70 % de su tiempo a tareas que no son vender (Salesforce Research, 2024, p. 13) | No [FALTA-DATO: M2, horas por cotización, CP-01] |
| **Cumplimiento legal** | Datos de clientes en teléfonos personales, sin consentimiento registrado | La LOPDP exige consentimiento libre, específico, informado e inequívoco (Ley Orgánica de Protección de Datos Personales [LOPDP], 2021, art. 8, p. 15) | No |

### 1.3 La brecha, en una frase

> Torvesa quiere responder en menos de 15 minutos y hoy responde en horas. No lo sabe con exactitud porque **no queda registro** de cuándo llegó cada solicitud, quién la atendió ni por qué se perdió.

El problema no es de voluntad: es de diseño del proceso. Responder rápido ya es una ventaja en el mercado: en una prueba con 1.000 empresas B2B, 635 nunca respondieron a una solicitud (Koushik, 2024).

---

## 2. La oportunidad: por qué ahora

| Hecho | Dato | Qué significa para la propuesta |
|---|---|---|
| **La demanda de construcción vuelve** | La construcción cayó 1,7 % en 2023 y 7,9 % en 2024, y creció 2,7 % en 2025 (Banco Central del Ecuador [BCE], 2026, tabla 1, p. 22) | Los clientes reaparecen. Quien responde primero se los queda |
| **La construcción es de las menos digitalizadas** | En América Latina, la construcción está entre los sectores con menor madurez digital, sobre todo en las empresas pequeñas (Cathles et al., 2023, p. 5). Su estructura fragmentada y por proyectos frena la transformación digital (Samuelson y Stehn, 2023, p. 400) | Hay espacio para una herramienta simple, hecha para quien está en obra |
| **El cliente ya está en línea** | 83,9 % de la población de Ecuador usaba internet a fines de 2025 (Kemp, 2026) | El canal digital ya existe; falta que la empresa responda a tiempo |
| **WhatsApp es el canal real** | En Torvesa, 4 de 5 reciben clientes por WhatsApp personal (Bermeo y Segura, 2026, p. 10). La plataforma oficial cobra por mensaje y da 1.000 mensajes de servicio gratis al mes por número (Meta, s. f.) | Conectar WhatsApp de forma oficial es barato para el volumen de una pyme [FALTA-FUENTE: cifra nacional del uso de WhatsApp en negocios] |
| **Las pymes usan poca IA** | En la OCDE, 11,9 % de las pequeñas empresas usa IA, frente al 40 % de las grandes (OECD, 2025a, p. 6). En otra encuesta, 31 % de las pymes ya usa IA generativa (OECD, 2025b, p. 6). Son mediciones distintas; las dos muestran una brecha | Quien ordene primero sus datos se adelanta |
| **A las pymes de Ecuador les faltan datos ordenados** | La falta de bases de datos estructuradas es una de las barreras principales de la IA en las mipymes ecuatorianas (Pérez-Campdesuñer et al., 2025) | El primer paso no es «poner IA», sino ordenar la memoria comercial: eso es el modelo Estándar |
| **La IA se usa sin reglas** | 33 % de los empleados en Ecuador usa cuentas personales de IA en el trabajo y 70 % de las organizaciones no tiene reglas internas (Revelo, 2026) | El Premium ofrece IA con reglas: sin datos personales y con revisión humana |
| **La IA es accesible** | La API de Claude Sonnet 5.5 cuesta USD 2 por millón de tokens de entrada y USD 10 de salida (Anthropic, s. f.) | Unas 150 consultas al mes cuestan alrededor de USD 2 (Estudio de costos v0.3, §2.7) |
| **La ley obliga a ordenar los datos** | LOPDP (2021) y su reglamento (Reglamento General de la LOPDP, 2023) | El sistema ayuda a cumplir: consentimiento, datos separados, conservación limitada |

---

## 3. La propuesta: Estándar y Premium

### 3.1 Los dos modelos (DEC-16)

| | **Estándar** · Primer contacto garantizado + memoria comercial | **Premium** · Estándar + cotización asistida |
|---|---|---|
| **Qué incluye** | Captura de solicitudes (formulario con consentimiento y registro desde el celular de lo que llega por WhatsApp o teléfono) · aviso al celular en segundos · botón «Tomar» y responsable único · recordatorio a los 15 min y aviso a la gerencia · motivo de pérdida obligatorio · reporte del lunes · registro con huellas · bóveda con fichas de clientes, historial y plantillas, consultable sin conexión | Todo el Estándar · asistente de IA que arma borradores de respuesta y de cotización con la plantilla del tipo de obra, **sin precios**, diciendo qué documentos usó · revisión obligatoria de una persona antes de enviar · ajuste de plantillas y del asistente · más horas de soporte y mejoras |
| **Para quién** | Toda empresa que recibe solicitudes y tiene a su gente fuera de la oficina | Empresas que cotizan trabajos parecidos con frecuencia y ya tienen el primer contacto bajo control |
| **Qué problema resuelve** | Clientes que esperan horas · nadie responsable · pérdidas sin motivo · memoria en celulares personales | Cotizaciones armadas desde cero · conocimiento que solo tiene una persona |
| **Qué costo cubre** | Servidor y base de datos · sincronización de la bóveda · soporte básico · parte del mantenimiento del núcleo | Además: consumo de IA · soporte del asistente (revisar la calidad de los borradores, actualizar plantillas, cambiar de modelo si sube el precio) · **los costos fijos que el Estándar no alcanza a cubrir** |
| **Precio mensual** | USD 175 | USD 275 |
| **Cobro de implementación** | USD 222 | USD 311 |
| **Indicadores que se reportan** | M1 (minutos al primer contacto), M3 (pérdidas con responsable y motivo), M4 (tiempo para encontrar el historial), M5 (registro íntegro) | Los del Estándar + M2 (tiempo por cotización) |
| **Requisitos del diseño** | RQ-01 a RQ-10, RQ-13 a RQ-20, RQ-24 | + RQ-11, RQ-12, RQ-21 |

*Nota.* Los modelos siguen DEC-16 (aprobada el 20-oct): la bóveda va en el Estándar y el asistente de IA solo en el Premium. Los requisitos son los del Cap. IV v0.3. El recordatorio a los 15 min, el motivo de pérdida y el reporte del lunes se construyen en el sprint 6; el resto ya funciona en la prueba de concepto.

**Por qué el Premium tiene que pagar más que su costo directo.** El consumo de IA es pequeño: unos USD 2 al mes en el escenario base (Análisis financiero v0.1, §3). Lo caro del Premium es el trabajo de personas: revisar que los borradores salgan bien, ajustar las plantillas de cada tipo de obra y responder cuando el asistente se equivoca. Además, el Estándar no devuelve las horas ya invertidas en el levantamiento. El Premium sí: suma USD 51 al mes para eso y 3 horas más de mantenimiento (modelo financiero v0.2, hoja 2). Por eso, con un solo cliente, solo el Premium hace viable el proyecto [FALTA-DATO: horas reales de soporte del asistente, cuando Torvesa lo use].

**Qué no incluye ninguno de los dos:** equipos (el personal ya usa su celular), los mensajes de WhatsApp sobre el nivel gratuito de Meta, y las integraciones a medida (contabilidad, catálogo de precios), que se cotizan aparte.

[DECIDIR-VÍCTOR: los precios por tipo de empresa (constructora, remodelación, ferretería, veterinaria) se deciden después; la v0.3 del estudio de costos trae una propuesta.]

### 3.2 Cómo cobran los fundadores su trabajo

Los dos fundadores trabajan como independientes. Su tiempo tiene un costo: la vara es una hora de desarrollo con cargas de ley (Estudio de costos v0.3, §2.1). Se cobra en tres momentos:

| Momento | Qué se cobra | Cómo se recupera | Cifra |
|---|---|---|---|
| **Antes del lanzamiento** | El levantamiento ya hecho: entrevistas, censo, diseño, prueba de concepto | Es una **inversión**. Se recupera con el cobro de implementación de cada empresa y con parte de la mensualidad | 200 horas (supuesto) × USD 9,26 = USD 1.852 |
| **Al lanzar en cada empresa** | Configuración: tipos de obra, plantillas, plazo objetivo, cuentas, capacitación | Cobro único de implementación | USD 222 (Estándar) o USD 311 (Premium) |
| **Después del lanzamiento** | Mantenimiento (actualizaciones, seguridad, respaldo) y soporte | Incluido en la mensualidad | 4 horas (Estándar) o 7 horas (Premium) |
| | Mejoras nuevas que pide la empresa | Bolsa de horas o cotización por mejora | USD 11,11 la hora (tarifa de USD 9,26 + 20 % de margen) |

**Desde la contabilidad de Torvesa:** la mensualidad es un gasto de operación. En un acuerdo de software como servicio, el cliente normalmente no reconoce un activo intangible por la configuración, porque no controla el software, y la registra como gasto cuando recibe el servicio (IFRS Interpretations Committee, 2021). Torvesa no compra un activo: paga un servicio.

[DECIDIR-VÍCTOR: qué se ofrece a Torvesa después de la tesis (pendiente desde la guía de negociación v0.1): soporte por un plazo, entrega con manuales, o servicio mensual.]

---

## 4. Por qué nosotros y no la competencia

### 4.1 Comparativa analítica

Las filas son los criterios que importan a Torvesa según su censo y la LOPDP. Las columnas son las alternativas reales. Los precios son oficiales, sin IVA, para 5 usuarios.

**Leyenda:** ✓ sí, con evidencia · **parcial** · ✗ no (según su página oficial o el estado actual) · **s/v** sin verificar (no se afirma ni se niega).

| Criterio | TEAMSLASH Estándar | TEAMSLASH Premium | Pipedrive Lite | HubSpot Starter | Zoho CRM Standard | Bitrix24 Basic | Odoo | WhatsApp Business + Excel (hoy) |
|---|---|---|---|---|---|---|---|---|
| 1. Primer contacto por WhatsApp | parcial ¹ | parcial ¹ | ✗ ² | ✗ ² | ✗ ² | s/v ³ | s/v ³ | parcial ⁴ |
| 2. Aviso, responsable y recordatorio a los 15 min | ✓ ⁵ | ✓ ⁵ | parcial ⁶ | parcial ⁶ | parcial ⁶ | parcial ⁶ | parcial ⁶ | ✗ |
| 3. Memoria del cliente que queda en la empresa | ✓ ⁷ | ✓ ⁷ | parcial ⁸ | parcial ⁸ | parcial ⁸ | parcial ⁸ | parcial ⁸ | ✗ ⁹ |
| 4. Borrador de cotización que cita sus fuentes | ✗ | ✓ ¹⁰ | s/v ¹¹ | s/v ¹¹ | s/v ¹¹ | s/v ¹¹ | s/v ¹¹ | ✗ |
| 5. Funciona sin conexión en obra | parcial ¹² | parcial ¹² | s/v | parcial ¹³ | parcial ¹³ | s/v | s/v | parcial ¹⁴ |
| 6. Datos y LOPDP | parcial ¹⁵ | parcial ¹⁵ | ✓ ¹⁶ | ✓ ¹⁶ | parcial ¹⁷ | s/v | s/v | ✗ ¹⁸ |
| 7. Registro que delata alteraciones | ✓ ¹⁹ | ✓ ¹⁹ | parcial ²⁰ | parcial ²⁰ | parcial ²⁰ | parcial ²⁰ | parcial ²⁰ | ✗ |
| 8. Precio al mes para 5 usuarios (sin IVA) | USD 175 | USD 275 | USD 70 con pago anual; USD 95 mensual ²¹ | USD 100 de lista; oferta temporal más baja ²¹ | USD 60 con pago anual; USD 90 mensual; gratis hasta 3 usuarios ²¹ | USD 49 con pago anual; USD 69 mensual, por empresa ²¹ | ≈ USD 45 [VERIFICAR: precio de Odoo] | USD 0 adicional |
| 9. Costo a 3 años, con lo que le falta para cubrir el proceso | USD 6.522 (implementación + 36 meses, sin IVA) | USD 10.211 (implementación + 36 meses, sin IVA) | USD 9.529 | USD 10.771 | USD 9.115 | USD 8.959 | USD 9.383 | USD 0 en licencias; el costo son los clientes perdidos [FALTA-DATO: M3] |
| 10. Idioma y soporte local | ✓ ²² | ✓ ²² | parcial ²³ | parcial ²³ | parcial ²³ | parcial ²³ | parcial ²³ | — |
| 11. Adaptación a una constructora | ✓ ²⁴ | ✓ ²⁴ | parcial ²⁵ | parcial ²⁵ | parcial ²⁵ | parcial ²⁵ | parcial ²⁵ | ✗ |

**Notas de evidencia:**
1. La solicitud que llega por WhatsApp se registra desde el celular con su hora real (RQ-03) y desde ahí corre el aviso y el reloj de 15 minutos. La conexión con la plataforma oficial de WhatsApp todavía no está hecha (matriz de herramientas v0.1, criterio K5).
2. La página de precios no menciona WhatsApp (Pipedrive, s. f.; Zoho, s. f.-a). HubSpot menciona Facebook Messenger, no WhatsApp (HubSpot, s. f.). Que no lo mencione no prueba que no exista una integración de terceros.
3. Bitrix24 tiene canales abiertos de mensajería; su integración con WhatsApp y las funciones de Odoo no se verificaron (matriz v0.1).
4. Hoy el cliente sí escribe por WhatsApp (4 de 5), pero al celular personal: nadie más se entera y no queda la hora.
5. El aviso en segundos y el botón «Tomar» funcionan en la prueba de concepto (8-nov). El recordatorio a los 15 min (RQ-06) se construye en el sprint 6.
6. Los CRM asignan un dueño a cada oportunidad. El recordatorio automático depende del plan y de configurarlo [VERIFICAR: automatizaciones de cada plan].
7. La bóveda son archivos de texto que la empresa puede abrir, copiar y llevarse (RQ-09; matriz v0.1, K7).
8. Los CRM guardan contactos e historial, pero la lógica queda en la plataforma; se exportan los datos, no el sistema (matriz v0.1, K7).
9. Las conversaciones quedan en el celular de cada persona.
10. Prueba de concepto del 8-nov, con datos ficticios: borrador de una cocina de 12 m² en 15 segundos, sin precios, con 11 preguntas para completarlo y los documentos usados. Una persona lo revisa siempre (RQ-12). La técnica de buscar en los documentos antes de responder permite ver de dónde sale cada dato (Lewis et al., 2020, p. 9459).
11. Varios CRM venden funciones de IA. Ninguna ficha verificada muestra que armen cotizaciones citando los documentos de la propia empresa [VERIFICAR: funciones de IA de cada plan].
12. Las fichas ya sincronizadas se leen sin conexión (RQ-14). El aviso y el formulario sí necesitan red. Es relevante: en 2024 hubo cortes de luz de hasta 12 horas diarias (Tapia, 2024).
13. Tienen aplicación móvil (HubSpot, s. f.; Zoho, s. f.-a), pero trabajan en línea (matriz v0.1, K3).
14. Lo que está en un celular se ve sin conexión, pero solo en ese celular.
15. Consentimiento obligatorio, datos personales separados y un asistente que no recibe nombres ni teléfonos (prueba del 8-nov). Por defecto, Anthropic no usa lo enviado por la API para entrenar (Anthropic, 2026). **Pendientes:** la clave del servidor está expuesta y se corrige antes de usar datos reales; los datos salen a servidores fuera del país (LOPDP, 2021, arts. 56 y 57, pp. 46–47); falta el contrato de encargado entre TEAMSLASH y Torvesa [FALTA-DATO: modelo de contrato de encargado del tratamiento].
16. El acuerdo de tratamiento de datos (DPA) viene incluido en los términos de servicio (HubSpot, 2026; Pipedrive, 2026).
17. Zoho firma el DPA solo si el administrador lo pide por correo (Zoho, s. f.-b).
18. Datos de clientes en teléfonos personales, sin consentimiento registrado.
19. Registro de solo agregar con huellas SHA-256 encadenadas: detectó 3 de 3 alteraciones en la prueba (M5, datos ficticios).
20. Historial de cambios sin verificación con huellas (puntaje del equipo en la matriz v0.1, K8).
21. Pipedrive Lite, USD 14 por puesto con pago anual y USD 19 mensual (Pipedrive, s. f.). HubSpot Starter, USD 20 por puesto de lista (HubSpot, s. f.). Zoho Standard, USD 12 con pago anual y USD 18 mensual (Zoho, s. f.-a). Bitrix24 Basic, USD 49 por empresa con 5 usuarios (Bitrix24, s. f.). Odoo no tiene ficha: su página muestra dos precios.
22. Producto en español, soporte en persona por los fundadores. Los proveedores de nube dan soporte en inglés, pero eso lo absorbe TEAMSLASH.
23. Interfaz en español o traducida; soporte remoto. La página de Zoho para Latinoamérica está en español (Zoho, s. f.-a). Lo demás es puntaje del equipo (matriz v0.1, K9) [VERIFICAR: idioma del soporte].
24. Plantillas por tipo de obra (RQ-10); el plazo de 15 minutos lo fijó el equipo de Torvesa (censo); alertas de texto simple, como pidió el censo.
25. Configurables, pero genéricos. Odoo es un ERP modular con implementación más larga (matriz v0.1, K4).

*Nota de la fila 9.* Costo total a 3 años de la matriz de herramientas v0.1: suscripción con IVA, horas de implementación (supuesto de USD 15 la hora), 4 horas de soporte al mes y la captura de solicitudes que el CRM no trae. Es el costo si Torvesa arma la solución por su cuenta. Si armara por su cuenta el mismo sistema de TEAMSLASH, serían USD 9.039. El costo como servicio sale del Excel.

**Un competidor que no está en la tabla y hay que nombrar.** Kommo es el único CRM del inventario que se conecta directo con la plataforma oficial de WhatsApp Business. Cuesta entre USD 16,67 y USD 20 por usuario al mes, con un plazo mínimo de 6 meses (Kommo, s. f.). Si lo único que Torvesa quisiera fuera ordenar su WhatsApp, Kommo sería la alternativa más fuerte. No resuelve la memoria en archivos propios, el asistente que cita fuentes ni el registro con huellas.

### 4.2 Lectura de la tabla

1. **No ganamos por precio de licencia.** Bitrix24 y Zoho son más baratos por mes. A 3 años, con lo que cada uno necesita para cubrir el proceso, las cinco alternativas comerciales están entre USD 8.959 y USD 10.771: la diferencia es menor al 20 %. **La decisión se toma por ajuste al problema, no por precio.** Solo Dynamics 365 sale caro: entre USD 21.286 y USD 29.866 (matriz v0.1).
2. **Los CRM ganan en lo que da la trayectoria:** contratos de datos ya firmados, aplicaciones maduras, soporte global y escala.
3. **Ganamos en una combinación que ningún CRM revisado ofrece junta:** primer contacto medido contra la meta que fijó la empresa, memoria en archivos que son de la empresa, asistente que cita sus documentos con revisión humana y registro que delata alteraciones.
4. **Frente a «seguir como hoy»,** el costo de no hacer nada no aparece en ninguna factura: son los clientes que se van sin respuesta. Hasta tener la muestra documental, ese costo es un supuesto [FALTA-DATO: M3].

### 4.3 Valor agregado, medible

| # | Valor agregado | Cómo se mide | Meta | Indicador |
|---|---|---|---|---|
| 1 | **El primer contacto deja de depender de quién revisa el celular** | Mediana de minutos entre la llegada y el primer contacto; % atendidas dentro del plazo | < 15 min; ≥ 80 % dentro del plazo [DECIDIR-VÍCTOR: meta del %] | M1 |
| 2 | **Ningún cliente se pierde sin nombre ni motivo** | % de solicitudes con responsable; % de pérdidas con motivo | 100 % y 100 % | M3 |
| 3 | **La gerencia ve cuatro números cada lunes** | Reporte semanal: llegadas, minutos, pérdidas y motivos | 52 reportes al año, sin armar nada a mano | M1, M3 |
| 4 | **La memoria comercial queda en la empresa** | Tiempo para encontrar el historial de un cliente, con y sin la bóveda (CP-02) | [FALTA-DATO: línea base de M4] | M4 |
| 5 | **Cotizar toma menos tiempo** (solo Premium) | Horas por cotización, con y sin asistente (CP-01) | [FALTA-DATO: línea base de M2] | M2 |
| 6 | **Un registro que nadie altera sin que se note, y una IA que no ve datos personales** | Alteraciones detectadas ÷ simuladas; solicitudes con datos personales enviadas a la IA | 100 % y 0 % | M5, RQ-21 |

Al final de la validación se mide también la facilidad de uso con la escala SUS (M6) [FALTA-DATO: M6].

### 4.4 Desventajas honestas frente a la competencia

| Desventaja | Por qué pesa | Qué se hace |
|---|---|---|
| **Somos dos personas** | Si uno falta, el soporte se resiente | Manuales, bóveda documentada y código y datos que Torvesa puede llevarse |
| **No tenemos trayectoria ni clientes** | Torvesa sería el primero | Validación corta y reversible de dos semanas: si no sirve, se apaga sin costo (Pitch v0.1) |
| **No hay resultados con datos reales** | Todo lo mostrado es con datos ficticios | La validación en operación experimental controlada depende de la autorización de Torvesa |
| **Dependemos de un proveedor de IA y de tres servicios de nube** | Los precios y las condiciones pueden cambiar | Modelo de respaldo más barato, la variante con Gemini casi empata en la matriz (3,99 frente a 4,14) y modo sin IA. **El primer contacto no depende de la IA** |
| **WhatsApp oficial aún no conectado** | Lo que llega por WhatsApp se registra a mano (1 min por solicitud) | Conectar la plataforma oficial cuando el volumen lo justifique |
| **La bóveda compartida no tiene permisos por usuario** | Con Obsidian Sync, todos los colaboradores tienen los mismos permisos (Obsidian, s. f.) | Los datos personales van aparte, en el servidor, no en la bóveda |
| **Hay un pendiente de seguridad** | La clave del servidor está visible en la página pública | Se separa antes de usar datos reales |
| **Hoy es una sola instalación** | No está lista para varias empresas a la vez | Se separa por empresa antes del segundo cliente (sección 7) |
| **No es un CRM completo** | No trae embudo de marketing, facturación ni catálogo de precios | No compite en eso: se puede conectar a un CRM si la empresa crece |

---

## 5. Cómo se mejora de forma continua y cómo funciona como negocio digital

### 5.1 El ciclo planificar-hacer-verificar-actuar (PHVA)

La norma ISO 9001 trata la calidad como procesos con entradas, salidas, responsables e indicadores, que se mejoran con el ciclo PHVA [FALTA-FUENTE: ISO 9001:2015, enfoque a procesos y ciclo PHVA]. Aquí se usa **como marco para ordenar la mejora, no como certificación**: decir «cumple ISO 9001» sería falso.

El ciclo corre en dos niveles:

| Paso | En cada empresa cliente (cada semana) | En el producto (cada trimestre, con lo aprendido en todas las empresas) |
|---|---|---|
| **Planificar** | La gerencia fija el plazo objetivo (Torvesa: 15 min), la lista de motivos de pérdida y los turnos de quién recibe los avisos | Se priorizan mejoras según los motivos de pérdida y los pedidos repetidos de las empresas |
| **Hacer** | El equipo atiende con el proceso: aviso, «Tomar», contacto, cierre con motivo | Se construyen las mejoras; cada cambio queda en el historial del código |
| **Verificar** | **Reporte del lunes:** solicitudes que llegaron, mediana de minutos (M1), % dentro del plazo, pérdidas y motivos (M3), y la última huella del registro (M5) | Indicadores de todas las empresas sin datos personales: M1 a M5, horas de soporte por cliente, borradores aceptados o rehechos (Premium), SUS (M6) |
| **Actuar** | La gerencia corrige: reasigna turnos, ajusta plantillas, cambia el plazo si no es realista | Se ajustan plantillas comunes y precios; se retira lo que nadie usa |

**Qué se mide cada lunes, en una tabla:**

| Número | De dónde sale | Para qué sirve |
|---|---|---|
| Solicitudes que llegaron | Registro | Saber el volumen real |
| Mediana de minutos al primer contacto | Hora de llegada y hora de «Tomar» | Ver si se cumple la meta |
| % atendidas dentro del plazo | Ídem | Ver los casos que se escapan |
| Pérdidas y sus motivos | Motivo obligatorio | Decidir qué corregir |
| Última huella del registro | Registro con huellas | Comprobar que nadie alteró nada |

### 5.2 Cómo encaja como negocio digital

| Rasgo | En la propuesta |
|---|---|
| **Suscripción** | La empresa paga un mes a la vez; no compra licencias ni equipos. Ingreso recurrente para TEAMSLASH |
| **Costo marginal bajo** | Atender a una empresa más cuesta poco frente al costo fijo: en la v0.3 del estudio de costos, entre unos USD 11 y USD 41 al mes por empresa, según el modelo en el modelo v0.2, cada empresa adicional cuesta unos USD 48 (Estándar) o USD 51 (Premium) al mes, con su soporte |
| **Un núcleo, muchas configuraciones** | El código es el mismo; cambian los tipos de trabajo, las plantillas y el plazo (Proceso estrella v0.1, §4) |
| **Datos de cada empresa separados** | Cada empresa tiene su base de datos y su bóveda. Nunca se mezclan clientes de dos empresas (LOPDP). El asistente no entrena con los datos (Anthropic, 2026) |
| **Mejora con el uso** | Lo aprendido en una empresa (plantillas, motivos de pérdida) mejora el producto para las demás, sin compartir sus datos |
| **Escala con techo** | El techo es de 20 empresas (sección 7): crece sin personal fijo |

El CRM se propone en la literatura como herramienta para innovar el modelo de negocio de las pymes, por la gestión del conocimiento del cliente; es una propuesta todavía no comprobada con datos (Gil-Gomez et al., 2020, pp. 2733, 2745).

---

## 6. Viabilidad: qué se va a mostrar

> [!note] Solo estructura
> Las cifras las llena el hilo principal con el Excel. Se muestran dos miradas: **Torvesa como cliente** (¿le conviene pagar?) y **TEAMSLASH como negocio** (¿se sostiene?). Horizonte de 3 años, en dólares constantes, antes de impuesto a la renta. Tres escenarios: pesimista, base y optimista.

### 6.1 Torvesa como cliente

| Indicador | Qué muestra | Cifra (base) |
|---|---|---|
| Inversión inicial | Implementación + horas del equipo en capacitarse | USD 482 (USD 311 de implementación + 20 horas de su equipo) |
| Costo anual | Mensualidad × 12, con IVA | USD 2.415 / USD 3.795 |
| Beneficio anual | Horas liberadas (no es dinero que entra) + margen de obras que no se pierden (sí es dinero) | USD 10.698 (Premium; USD 6.415 en plata que entra por obras recuperadas) |
| VAN | Lo que queda a favor en 3 años, en dinero de hoy | USD 13.618 |
| Periodo de recuperación | Meses para recuperar la inversión | menos de 1 mes para recuperar la implementación |
| Relación beneficio/costo | Cuántos dólares de beneficio por cada dólar pagado | no se calcula; el retorno a 3 años es de 178 % (hoja 8) |
| Obras al año que pagan el sistema | Umbral sin contar el ahorro de tiempo: la pregunta que la gerencia puede contestar con su experiencia | 1,9 obras al año |

### 6.2 TEAMSLASH como negocio

| Bloque | Qué contiene | Cifra |
|---|---|---|
| **Inversión** | Levantamiento ya hecho (horas valoradas), constitución de la SAS, firma electrónica, dominio | USD 2.243 (USD 1.852 en horas ya trabajadas + USD 391 en efectivo) |
| **Ingresos** | Mensualidades Estándar y Premium + cobros de implementación + mejoras por hora | USD 3.611, 3.300 y 3.300 (un solo cliente, Premium) |
| **Costos variables** | Por empresa: servidor, bóveda, IA y soporte | unos USD 51 al mes por empresa adicional (Premium) |
| **Costos fijos** | Servidor base, herramientas, publicidad, contador, internet | USD 189 al mes (servidor y página base, administración, mantenimiento del núcleo y recuperación del levantamiento) |
| **Estado de resultados** | Ingresos − costos variables = margen de contribución; − costos fijos = resultado antes del pago a los fundadores; − horas de los fundadores = resultado antes de impuestos [FALTA-FUENTE: régimen tributario aplicable a la SAS] | utilidad neta de USD 481, 442 y 442 (margen neto del 13 %) |
| **Flujo de caja** | Entradas y salidas reales de dinero por año (el tiempo de los fundadores se muestra aparte, como costo de oportunidad) | −USD 2.243 (año 0); USD 1.099, 1.060 y 1.388 |
| **VAN** | Con la tasa de descuento del escenario | USD 427 (Premium, TMAR 15 %); negativo con el Estándar solo |
| **TIR** | Se informa, con la advertencia de que con inversiones pequeñas sale muy alta y dice poco | 26 % |
| **Periodo de recuperación** | Meses para recuperar la inversión, incluido el levantamiento | unos 25 meses |
| **Relación beneficio/costo** | Valor presente de ingresos ÷ valor presente de costos | 1,03 |
| **Punto de equilibrio** | Empresas necesarias para cubrir (a) la caja y (b) la caja más las horas de los fundadores | 1 empresa (Torvesa) ya cubre la caja / 1 empresa en Premium cubre también las horas y el levantamiento; en Estándar no |
| **Pago por hora de los fundadores** | Lo que queda ÷ horas trabajadas, comparado con la vara de una hora de desarrollo | USD 14,53 por hora de trabajo, frente a USD 9,26 de la tarifa |

**Cómo se va a leer:** primero el escenario base, después qué supuesto mueve más el resultado (análisis de sensibilidad) y al final el pesimista, que se presenta aunque salga negativo. Los cinco supuestos que más pesan son de ventas y solo Torvesa puede darlos (Análisis financiero v0.1, §3): por eso la muestra documental es también la ruta crítica de las finanzas.

---

## 7. Escalamiento (al final)

| Etapa | A quién | Con qué modelo | Condición para pasar a la siguiente |
|---|---|---|---|
| 1 | **Torvesa** | Estándar, y Premium cuando la bóveda tenga datos | Validación terminada y primer reporte de M1 a M5 con datos reales |
| 2 | **Otras constructoras y empresas de remodelación** | Estándar o Premium, con las mismas plantillas por tipo de obra | Instalación separada por empresa y contrato de encargado de datos listo |
| 3 | **Otros rubros** (ferreterías, inmobiliarias, veterinarias) | Sobre todo Estándar | Precios por tipo de empresa probados con al menos una empresa real |

- **Techo realista: 20 empresas** (decisión de Víctor, 15-nov). Con ese techo no se contrata personal ni se arrienda oficina.
- **Las constructoras sostienen el negocio:** en la v0.3, una constructora deja lo mismo que ocho veterinarias.
- **La ruta de AWS no hace falta con 20 empresas;** es para cientos (Análisis financiero v0.1, §4).

**Qué habría que investigar antes de escalar:**
- [FALTA-DATO: cuántas constructoras y empresas de remodelación pequeñas hay en Quito, para saber si 20 es alcanzable]
- [FALTA-DATO: cuánto pagaría cada tipo de empresa, con al menos una entrevista por tipo]
- [FALTA-DATO: cuántos clientes se van al año]
- [FALTA-DATO: horas reales de soporte por empresa, medidas en Torvesa]

---

## 8. Qué falta y referencias

### 8.1 Marcadores de esta versión

| Marcador | Cantidad | Cuáles |
|---|---|---|
| CIFRA-EXCEL | 36 | Precios Estándar, Premium e implementación; costo no cubierto; levantamiento y tarifas; costo de atender; todas las cifras de la sección 6 |
| FALTA-DATO | 13 | Solicitudes y pérdidas de Torvesa (M3, dos veces); M2 (dos veces), M4 y M6; horas de soporte del asistente; contrato de encargado; datos para escalar (4) |
| FALTA-FUENTE | 3 | Uso de WhatsApp en negocios en Ecuador; ISO 9001:2015 (PHVA); régimen tributario de la SAS |
| VERIFICAR | 4 | Precio de Odoo; automatizaciones de cada CRM; funciones de IA de cada CRM; idioma del soporte |
| DECIDIR-VÍCTOR | 3 | Precios por tipo de empresa; qué se ofrece después de la tesis; meta del % dentro del plazo |

### 8.2 Referencias

Solo fuentes con ficha verificada en `02_Fuentes/`. Los documentos internos (estudio de costos, matriz, prueba de concepto) no van en las referencias: se citan como anexos.

Anthropic. (s. f.). *Pricing*. Claude Platform Docs. Recuperado el 25 de octubre de 2026, de https://platform.claude.com/docs/en/about-claude/pricing

Anthropic. (2026). *Is my data used for model training?* Recuperado el 25 de octubre de 2026, de https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training

Banco Central del Ecuador. (2026). *Informe de evolución de la economía ecuatoriana en 2025 y perspectivas 2026*. https://contenido.bce.fin.ec/documentos/Administracion/EvolEconEcu_2025pers2026.pdf

Bermeo, D., y Segura, V. (2026). *TEAMSLASH: Ecosistema digital de gestión de clientes para la Constructora Torvesa* [Informe final del proyecto integrador, Universidad Politécnica Salesiana].

Bitrix24. (s. f.). *Bitrix24 plans and pricing*. Recuperado el 10 de noviembre de 2026, de https://www.bitrix24.com/prices/

Cathles, A., Henríquez, P., y Suaznábar, C. (2023). *Impulsando la transformación digital de la construcción: el caso del BIM en Chile*. Banco Interamericano de Desarrollo. https://doi.org/10.18235/0004973

Gil-Gomez, H., Guerola-Navarro, V., Oltra-Badenes, R., y Lozano-Quilis, J. A. (2020). Customer relationship management: Digital transformation and sustainable business model innovation. *Economic Research-Ekonomska Istraživanja, 33*(1), 2733–2750. https://doi.org/10.1080/1331677X.2019.1676283

HubSpot. (s. f.). *Free tools: Pricing (Smart CRM)*. Recuperado el 25 de octubre de 2026, de https://www.hubspot.com/pricing/crm

HubSpot. (2026). *HubSpot data processing agreement*. Recuperado el 25 de octubre de 2026, de https://legal.hubspot.com/dpa

IFRS Interpretations Committee. (2021, marzo). *IFRIC update March 2021*. IFRS Foundation. https://www.ifrs.org/content/ifrs/home/news-and-events/updates/ifric/2021/ifric-update-march-2021.html

Kemp, S. (2026). *Digital 2026: Ecuador*. DataReportal. https://datareportal.com/reports/digital-2026-ecuador

Kommo. (s. f.). *Precios*. Recuperado el 25 de octubre de 2026, de https://www.kommo.com/es/precios/comparar-planes/

Koushik, V. (2024, 20 de marzo). *We tested lead response times of 1000 B2B sales teams. Here are the results*. RevenueHero. https://www.revenuehero.io/blog/b2b-lead-response-times

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., y Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *Advances in Neural Information Processing Systems, 33*, 9459–9474.

Ley Orgánica de Protección de Datos Personales. (2021, 26 de mayo). Registro Oficial, Quinto Suplemento n.º 459.

Meta. (s. f.). *Precios de la plataforma de WhatsApp Business*. Recuperado el 25 de octubre de 2026, de https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing

Obsidian. (s. f.). *Collaborate on a shared vault*. Obsidian Help. Recuperado el 21 de octubre de 2026, de https://obsidian.md/help/sync/collaborate

OECD. (2025a). *AI adoption by small and medium-sized enterprises* (OECD discussion paper for the G7). OECD Publishing.

OECD. (2025b). *Generative AI and the SME workforce: New survey evidence*. OECD Publishing.

Pérez-Campdesuñer, R., Sánchez-Rodríguez, A., García-Vidal, G., Martínez-Vivar, R., y De Miguel-Guzmán, M. (2025). Artificial intelligence in Ecuadorian SMEs: Drivers and obstacles to adoption. *Information, 16*(6), Artículo 443. https://doi.org/10.3390/info16060443

Pipedrive. (s. f.). *CRM pricing plans*. Recuperado el 25 de octubre de 2026, de https://www.pipedrive.com/en/pricing

Pipedrive. (2026). *Pipedrive data processing addendum*. Recuperado el 25 de octubre de 2026, de https://www.pipedrive.com/en/privacy/dpa

Reglamento General de la Ley Orgánica de Protección de Datos Personales. Decreto Ejecutivo 904. (2023, 13 de noviembre). Registro Oficial, Tercer Suplemento n.º 435.

Revelo, R. (2026, 16 de septiembre). El peligro de la «Shadow AI»: el 33 % de empleados en Ecuador usa IA personal en el trabajo. *Primicias*.

Salesforce Research. (2022). *State of the connected customer* (5.ª ed.). Salesforce.

Salesforce Research. (2024). *State of sales* (6.ª ed.). Salesforce.

Samuelson, O., y Stehn, L. (2023). Digital transformation in construction – a review. *Journal of Information Technology in Construction, 28*, 385–404. https://doi.org/10.36680/j.itcon.2023.020

Stark, A. (2024). Institutional amnesia in government: How much is enough? *Policy Quarterly, 20*(1), 3–9. https://doi.org/10.26686/pq.v20i1.9046

Tapia, E. (2024, 23 de octubre). Ecuador cumple un mes con largos apagones que llegaron hasta 12 horas, ¿cuáles son los efectos en el país? *Primicias*. https://primicias.ec/economia/primer-mes-apagones-ecuador-perdidas-industrias-81725

Zoho. (s. f.-a). *Precios y ediciones de Zoho CRM*. Recuperado el 25 de octubre de 2026, de https://www.zoho.com/es-xl/crm/zohocrm-pricing.html

Zoho. (s. f.-b). *GDPR*. Recuperado el 25 de octubre de 2026, de https://www.zoho.com/gdpr.html
