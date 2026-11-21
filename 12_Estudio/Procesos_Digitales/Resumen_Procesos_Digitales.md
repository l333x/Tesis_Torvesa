---
titulo: "Resumen para el examen de Procesos para Negocios Digitales"
materia: "Procesos para Negocios Digitales (Grupo 1)"
examen: 2026-11-24
fuente: "Diapositivas Clase 1 a Clase 5 (PDF en 12_Estudio/Procesos_Digitales/diapositivas/)"
fecha: 2026-11-21
autor_borrador: "Claude (revisa Víctor)"
---

# Procesos para Negocios Digitales: resumen para el examen

Cómo leer esto:
- La página entre paréntesis es la del PDF de cada clase: (Clase 2, p. 4).
- Lo que no sale de las diapositivas va marcado **(fuera de las diapositivas)**.
- Las analogías son para recordar. No las escribas en el examen.

Avisos sobre el material:
- El PDF «Clase 4» trae al inicio 3 páginas de **Componentes BPM** (pp. 1-3) y recién en la p. 4 empieza «Clase 4: Certificaciones».
- Las diapositivas del PDF «Clase 5» tienen el rótulo **«Unidad 2 · Estructura del BPM · Clase 6»**. Aquí se llama Clase 5 porque así se llama el archivo.
- En la Clase 3 los beneficios están numerados del 2 al 8. **No hay diapositiva del beneficio 1** (la p. 2 es la «situación actual»). No se inventa cuál es.
- **No aparece BPMN** en ninguna diapositiva. La única notación gráfica es la tabla de **símbolos de diagrama de flujo** (Clase 4, p. 3).

---

## Clase 1: Visión por procesos

### 1.1 Proyecto (PMP) vs. proceso (BPM) (Clase 1, pp. 3-5)
- **PMP (Project Management Professional)**: se enfoca en la **gestión de proyectos individuales**, que son **esfuerzos temporales con un inicio y un fin definidos** (p. 3).
- **BPM (Business Process Management)**: se centra en la **optimización de procesos de negocio continuos y repetitivos** dentro de una organización (p. 3).
- Tabla de ejemplos por sector (p. 4):

| Sector | Proyecto (PMP) | Proceso (BPM) |
|---|---|---|
| Arquitectura | Construir una casa | Gestionar solicitudes de mantenimiento |
| Tecnología | Crear una aplicación móvil | Procesar los pedidos que llegan a la aplicación |
| Comercio electrónico | Crear una tienda virtual | Recibir, cobrar y entregar pedidos |
| Universidad | Implementar una nueva plataforma educativa | Matricular estudiantes cada semestre |
| Banco | Implementar una nueva aplicación bancaria | Procesar transferencias de dinero |
| Salud | Construir un nuevo hospital | Atender y registrar pacientes diariamente |

- Comparación (p. 5):
  - **PMP, dirección de proyectos**: planificar, organizar y dar seguimiento a proyectos de cualquier tipo y sector. Herramientas: **Microsoft Project, Microsoft Planner, Trello, Jira** (4). Ejemplo: construir un edificio (inicio, fin, presupuesto y resultado específico). Palabra clave: **Temporal**, «el proyecto termina cuando se entrega el resultado».
  - **BPM, gestión de procesos de negocio**: analizar, mejorar y automatizar los procesos de una empresa y **representarlos visualmente**. Los procesos se repiten continuamente (ventas, compras, atención al cliente, entregas). Herramientas: **Bizagi, Appian, Camunda, Azure DevOps** (4). Ejemplo: Recibir pedido → Validar pago → Preparar pedido → Entregar producto. Palabra clave: **Recurrente**, «se ejecuta continuamente mientras la empresa opere».
- Ejercicio calificado 1: «Encontrar empleo, match con herramientas» (p. 6). La p. 2 solo dice «Despertarse» (ejemplo de proceso cotidiano).

> **Analogía:** Construir tu base en Minecraft es un **proyecto** (empieza, se termina y queda la base). La granja automática de hierro que corre todos los días es un **proceso**. En tu trabajo, implantar Business Central sería un proyecto. Cada requerimiento que pasa por cotización, cuadro comparativo, aprobación, OC y factura es el proceso.

### 1.2 Qué es la visión por procesos (Clase 1, p. 7)
- **Definición literal:** «Es entender y gestionar el trabajo como un **flujo de actividades conectadas** que **transforman entradas en resultados** que generan **valor para el cliente**».

### 1.3 Necesidad → Proceso → Resultado (Clase 1, p. 8)
- «Todo proceso nace de una **necesidad** y termina generando un **resultado** para el cliente».
- Ejemplo con Rappi: 1. Necesidad, Pancho tiene hambre. 2. Proceso, pide comida en la app (hamburguesa clásica, $6,50). 3. Resultado, recibe su hamburguesa.

### 1.4 Entrada → Actividades → Salida (Clase 1, p. 9)
- «Todo proceso **transforma** algo que recibimos en algo que entregamos».
- **Entrada:** pedido del cliente (información de la orden y pago confirmado).
- **Actividades (transformación), 4:**
  1. Recibir y validar el pedido (la app registra la orden y confirma el pago).
  2. Preparar el pedido (el restaurante elabora la comida).
  3. Asignar y despachar al repartidor (la app asigna al mejor repartidor disponible).
  4. Traslado y entrega (el repartidor lleva el pedido a la puerta).
- **Salida:** pedido entregado; el cliente recibe su comida y **la necesidad queda satisfecha**.

> **Analogía:** En Genshin, la mesa de alquimia: entran materiales (entrada), se transforma (actividad) y sale el objeto (salida). En PedidosYa, en Quito, es lo mismo que Rappi en la diapositiva.

### 1.5 Actores del proceso (Clase 1, p. 10)
- «Un proceso siempre involucra a diferentes **actores** que trabajan juntos para generar el resultado final». Son 5:
  1. **Cliente:** tiene la necesidad, hace el pedido y recibe el resultado.
  2. **Plataforma:** recibe el pedido, procesa el pago, asigna repartidor y da seguimiento.
  3. **Restaurante:** recibe la orden, prepara la comida y la deja lista.
  4. **Repartidor:** recoge el pedido y lo entrega.
  5. **Otros soportes:** pasarelas de pago, soporte técnico, mapas, atención al cliente.

### 1.6 Las actividades dependen unas de otras (Clase 1, p. 11)
- «Si una actividad no se completa, las siguientes no pueden continuar y el **proceso se detiene**».
- Ejemplo: 1. Pedido (ok). 2. Preparación (ok). 3. Repartidor llega (alerta). 4. Preparación no terminada (falla). 5. Entrega no realizada.

> **Analogía:** En Valorant, si nadie planta la spike, el post-plant no existe. En compras, sin cuadro comparativo no hay aprobación, y sin OC el proveedor no puede facturar.

### 1.7 Los procesos generan valor (Clase 1, p. 12)
- «Un proceso exitoso **transforma recursos en resultados** que generan **valor para el cliente y la organización**».
- **Recursos (entradas), 5:** pago del cliente, ingredientes, plataforma y tecnología, repartidor y transporte, personas y conocimiento.
- **Proceso (transformación), 4 pasos:** 1. Pedido, 2. Preparación, 3. Entrega, 4. **Control y soporte** (se monitorea el pedido y se brinda soporte si hace falta).
- **Valor generado, 4:** satisfacción del cliente; entrega rápida y confiable; fidelización y recomendación; eficiencia y rentabilidad para la organización.
- Ejercicio calificado 2: «Replique con un proceso de una app web en POST/MIRO, 8 a la 12» (p. 13), es decir, replicar las diapositivas 8 a 12 con otra app.

---

## Clase 2: BPM (Unidad 1, Introducción del BPM)

### 2.1 Qué es BPM (Clase 2, p. 2)
- **BPM = Business Process Management.**
- **Definición literal:** «BPM es un enfoque para **diseñar, ejecutar, monitorear y mejorar** los procesos de la organización con el objetivo de **generar valor** para el **cliente** y para el **negocio**».
- **Idea clave:** «BPM no es solo dibujar procesos. Es **gestionarlos de punta a punta** para entregar valor al cliente».
- Ejemplo (Pancho compra audífonos): Cliente → Pedido y pago → Preparación (se verifica el stock) → Entrega → Resultado (audífonos recibidos, satisfecho).
- **Por qué es importante (3):** enfoca a la organización en lo que necesita el cliente; mejora la eficiencia y reduce costos y tiempos; asegura calidad, cumplimiento y mejora continua.

### 2.2 BPM: más que dibujar procesos (Clase 2, p. 3)
- «Un diagrama muestra el flujo. BPM busca **gestionarlo y mejorarlo**».
- **Solo dibujar (5 limitaciones):** solo representa cómo se hace; no garantiza que se cumpla; no mide resultados; no identifica problemas; no mejora el proceso.
- **Ciclo BPM, 5 fases en círculo:**
  1. **Diseñar:** entender y modelar el proceso.
  2. **Ejecutar:** poner el proceso en marcha.
  3. **Monitorear:** medir el desempeño y detectar problemas.
  4. **Analizar:** entender causas y oportunidades.
  5. **Mejorar:** implementar cambios y optimizar el proceso.
- Ejemplo: Pancho ve en la app que pagó, pero eso no asegura que reciba sus audífonos (Pedido → Pago → Preparación → Retiro → Entrega).
- Cita: «Ver el proceso completo nos permite tomar mejores decisiones y mejorar cada día».

> Ojo: en la definición (p. 2) hay **4 verbos** (diseñar, ejecutar, monitorear, mejorar). En el ciclo (p. 3) hay **5 fases**, porque se agrega **Analizar** entre monitorear y mejorar.

> **Analogía:** Ver el replay de una partida de Valorant es «dibujar». Revisarlo, ver por qué perdiste el site (analizar) y cambiar la estrategia es BPM.

### 2.3 Los 5 elementos que gestiona BPM (Clase 2, p. 4)
1. **Actividades:** qué se hace y en qué orden.
2. **Responsables:** quién hace cada actividad.
3. **Información:** qué datos se usan, se generan y se comparten.
4. **Reglas:** políticas, condiciones y criterios que guían el proceso.
5. **Resultados:** qué se obtiene y qué valor genera al cliente y al negocio.
- Idea clave: BPM los gestiona integrados para que el proceso sea **eficiente, eficaz y consistente**.
- Ejemplo: Pedido (actividad: registrar pedido; regla: datos completos) → Pago (responsable: plataforma; información: pago aprobado) → Preparación (responsable: bodega; regla: stock disponible) → Despacho (responsable: logística; información: guía y tracking) → Entrega (resultado: audífonos recibidos).

> **No confundir:** en la Clase 2 son **5 elementos**. En la Clase 4-5 son **6 componentes**, porque se agrega **Tecnología** y «Responsables» pasa a llamarse **Roles** e «Información» pasa a llamarse **Datos**.

### 2.4 Personas + Procesos + Tecnología (Clase 2, p. 5)
- «El éxito del proceso depende de la coordinación de estos **tres pilares**».
  - **Personas:** realizan las actividades, toman decisiones y **resuelven excepciones**.
  - **Procesos:** definen el flujo de trabajo, las reglas y la forma en que se genera valor.
  - **Tecnología:** sistemas y herramientas que permiten ejecutar, integrar y controlar.
- Idea clave: BPM no depende solo de la tecnología ni de las personas, sino de **cómo trabajan juntos** en un proceso alineado.
- Ejemplo: Pedido (el cliente lo hace) → Pago (el sistema valida y aprueba) → Preparación (personas preparan) → Despacho (logística gestiona el envío) → Entrega.

> **Analogía:** En Valorant: los jugadores (personas), la estrategia o ejecución del site (proceso) y las habilidades y el equipo comprado (tecnología). Con buena puntería y sin plan, se pierde.

### 2.5 Del proceso informal al proceso gestionado (Clase 2, p. 6)

| Proceso informal | Proceso gestionado con BPM |
|---|---|
| Se hace como siempre se ha hecho | Actividades y flujo **definidos** |
| No hay responsables claros | Responsables **asignados** |
| Información incompleta o desactualizada | Información **correcta y disponible** |
| Errores, retrabajos y retrasos frecuentes | Menos errores, mayor eficiencia y mejores resultados |

- Idea clave: BPM convierte procesos improvisados en procesos **claros, medibles y mejorables**. Del «caos operativo» a la «gestión inteligente». Genera **resultados predecibles**.

### 2.6 ¿Dónde está el pedido? Visibilidad con datos (Clase 2, pp. 7 y 10, repetida)
- 4 datos del tablero: **Estado** (en bodega), **Tiempo** (26 horas), **Responsable** (despacho), **Alerta** (tiempo excedido).
- «**Los datos hacen visible lo que ocurre en el proceso**».
- Pancho no necesita escuchar «creemos que mañana sale». La empresa debe saber **dónde** está el pedido, **cuánto tiempo** lleva ahí y **quién** debe actuar.

> **Analogía:** Es tu semáforo de requerimientos: estado, días estancado, responsable y alerta. También es Quito Te Mueve o el Metro de Quito mostrando cuánto falta para que llegue (fuera de las diapositivas).

### 2.7 BPM conecta áreas y funciones (Clase 2, p. 8)
- «Un pedido atraviesa varias áreas. BPM integra el trabajo para que el flujo no se detenga».
- 5 pasos: **Pago** (confirma y valida la transacción) → **Inventario** (verifica disponibilidad) → **Bodega** (prepara para despacho) → **Logística** (transporta y hace el seguimiento) → **Cliente** (recibe y valora la experiencia).
- Idea clave: BPM alinea áreas, información y decisiones para que el cliente reciba valor **sin interrupciones**. Proceso conectado = entrega a tiempo y cliente satisfecho.

### 2.8 Por qué es importante gestionar procesos (Clase 2, p. 9)
- «BPM genera **valor** para el cliente y **eficiencia** para el negocio». Son **5 razones**:
  1. **Enfoque al cliente:** lo que el cliente necesita, con mejor experiencia.
  2. **Eficiencia:** menos tiempos, retrabajos y uso de recursos.
  3. **Calidad y consistencia:** procesos estables, resultados predecibles.
  4. **Visibilidad:** medir y monitorear para decidir mejor.
  5. **Mejora continua:** detectar oportunidades y mejorar de forma constante.
- Idea clave: «BPM no es solo trabajar más rápido, es **trabajar mejor**, todos alineados para generar **valor sostenible**».
- Mejores procesos = **cliente satisfecho + negocio eficiente**.

---

## Clase 3: Beneficios de BPM (negocios digitales)

### 3.1 Situación de partida (Clase 3, p. 2)
- Un e-commerce crece rápido: pasa de **100 a 800 pedidos diarios**.
- Indicadores: **800** pedidos diarios, **18 %** retrasos, **7 %** errores, **35** reclamos diarios.
- «Cuando gestionamos los procesos de forma estructurada, el negocio funciona mejor y el cliente recibe más valor».

### 3.2 Beneficio 2: menos tiempo, procesos más rápidos (Clase 3, p. 3)
- BPM **elimina esperas innecesarias** y **acelera** el ciclo completo.
- Ejemplo: audífonos premium. **Antes, 72 h; después, 24 h. Reducción del 67 %.**
  - Antes: recepción 2 h, verificación de stock 12 h, preparación 6 h, **esperar transportista 24 h**, transporte 28 h («mucho tiempo en esperas»).
  - Después: recepción 1 h, **verificación y preparación en paralelo** 6 h, despacho sin esperas 4 h, entrega más rápida 13 h.
- Clave: el ahorro sale de **hacer tareas en paralelo** y quitar esperas.

> **Analogía:** En Minecraft, poner varios hornos en paralelo en vez de uno solo. En compras: pedir las 3 cotizaciones al mismo tiempo, no una por una.

### 3.3 Beneficio 3: menos errores y retrabajos (Clase 3, p. 4)
- BPM **estandariza** las actividades y reduce errores que generan **trabajo duplicado**.
- Antes: pedido → dirección incorrecta → devolución → nuevo envío. Impacto: **+48 h, +$8,40**, cliente molesto.
- Después: pedido → **validación automática** → envío correcto → entrega. Impacto: **24 h, $0** extra, cliente satisfecho.
- **Tipos de errores comunes (3):** direcciones mal registradas, productos incorrectos, información incompleta.
- «Cada error no solo cuesta dinero, también afecta la **confianza y la reputación** de la empresa».

### 3.4 Beneficio 4: menores costos operativos (Clase 3, p. 5)
- BPM **elimina actividades sin valor** y evita retrabajos.
- Devolución por dirección incorrecta: envío original → devolución → reprocesamiento en almacén → nuevo envío. «Un solo error genera **trabajo dos veces**».
- **Costo por devolución:** transporte ida $3,20 + transporte vuelta $3,20 + atención al cliente $0,80 + embalaje y materiales $1,20 = **$8,40**.
- **56 devoluciones diarias (7 % de 800) × $8,40 = $470,40 al día.**
- Con BPM: menos errores en el origen, menos retrabajos y devoluciones, menos costos ocultos, más rentabilidad. «Ahorrar costos hoy es invertir en crecimiento mañana».

> **Analogía:** Es como una factura sin OC que se devuelve al proveedor. Se hace el trabajo dos veces y el pago se va a otro viernes.

### 3.5 Beneficio 5: mejor experiencia del cliente (Clase 3, p. 6)
- BPM entrega lo que el cliente espera: **información clara, tiempos confiables y servicio consistente**.
- Ejemplo: María compra un regalo de cumpleaños que debe llegar el viernes.
  - Sin BPM: no hay información clara, las respuestas son lentas o diferentes y llega el lunes. Cliente frustrado.
  - Con BPM: información en tiempo real, tiempos confiables y entrega el viernes. Cliente satisfecho que recompra y recomienda.
- Journey del cliente:
  - Sin BPM: consulta «¿Dónde está mi pedido?» → espera → atención revisa varios sistemas → respuesta poco clara → incertidumbre y desconfianza.
  - Con BPM: consulta en la app → ve el estado en tiempo real → entrega estimada confiable → comunicación clara → confianza y satisfacción.
- **Impacto: +25 % satisfacción, +18 % recompra, −30 % reclamos.**
- «Un cliente informado, atendido y satisfecho es el **mejor promotor** de tu marca».

### 3.6 Beneficio 6: mayor productividad de los equipos (Clase 3, p. 7)
- BPM elimina **tareas repetitivas** para que el equipo se enfoque en lo que **genera valor**.
- **Sin BPM, 330 min/día:** buscar información en correos y Excel 120; copiar y actualizar datos 90; revisar pedidos manualmente 60; responder preguntas repetitivas 60.
- **Con BPM, 150 min/día:** información centralizada 30; automatización de registros y validaciones 45; alertas y seguimiento automático 15; atención personalizada y solución de casos 60.

### 3.7 Beneficio 7: decisiones basadas en datos (Clase 3, p. 8)
- BPM permite medir y analizar para decidir **con datos y no con suposiciones**.
- Sin BPM (intuición o experiencia): no sabemos qué falla, reaccionamos tarde, repetimos problemas, más costo y clientes insatisfechos.
- Con BPM (datos y métricas): sabemos qué falla, actuamos a tiempo, mejoramos continuamente, menos costo y más satisfacción.

### 3.8 Beneficio 8: escalabilidad y crecimiento (Clase 3, p. 9)
- «Un proceso puede funcionar con poco volumen y **colapsar** cuando el negocio crece».
- Caso **ClickShop**: pasó de 100 a 1.000 pedidos diarios tras una campaña en redes.

| Indicador | Antes | Ahora | Cambio |
|---|---|---|---|
| Pedidos/día | 100 | 1.000 | ↑ 10X |
| Pedidos con error | 3 % | 12 % | ↑ 4X |
| Tiempo de preparación | 4 h | 18 h | ↑ 4,5X |
| Reclamos diarios | 5 | 85 | ↑ 17X |
| Personal | 2 | 6 | ↑ 3X |

- Situación actual: pedidos en Excel → envío por correo → bodega revisa manualmente → inventario se actualiza al final del día. «Mucho trabajo manual = más errores y retrasos».
- Reto (4 preguntas): ¿dónde está el **cuello de botella**? ¿Contratar más personas solucionaría el problema? (el personal se triplicó y los reclamos subieron 17 veces). ¿Qué parte mejorarían primero? ¿Qué indicador demostraría la mejora?

> **Analogía:** En Minecraft, tu granja de 1 cofre funciona, pero cuando pones 10 tolvas el sistema se atasca. No se arregla poniendo más aldeanos, sino rediseñando la granja.

**Lista de beneficios para memorizar (2 a 8):** Tiempo, Errores, Costos, Cliente, Productividad, Datos, Escala. Mnemotecnia: «**T**odos **E**rran, **C**uesta **C**aro, **P**ero **D**atos **E**scalan».

---

## Clase 4: Componentes BPM (pp. 1-3) y Certificaciones (pp. 4-12)

### 4.1 Los 6 componentes (Clase 4, p. 2; repetido en Clase 5, p. 3)
Hexágono alrededor de «PROCESO»:
1. **Actividades:** ¿qué se hace?
2. **Roles:** ¿quién lo hace?
3. **Reglas:** ¿bajo qué condiciones se decide?
4. **Datos:** ¿con qué información se trabaja?
5. **Tecnología:** ¿con qué se ejecuta y se automatiza?
6. **Resultados:** ¿qué se obtiene y qué valor genera?

### 4.2 Símbolos del diagrama de flujo (Clase 4, p. 3)

| Símbolo | Nombre | Función |
|---|---|---|
| Óvalo o rectángulo redondeado | **Inicio / Final** | Representa el inicio y el final de un proceso |
| Flecha | **Línea de flujo** | Indica el orden de ejecución; la flecha señala la siguiente instrucción |
| **Paralelogramo** | **Entrada / Salida** | Lectura de datos en la entrada e impresión de datos en la salida |
| **Rectángulo** | **Proceso** | Representa cualquier tipo de operación |
| **Rombo** | **Decisión** | Analiza una situación con base en los valores **verdadero y falso** |

Mnemotecnia: «**O**jo, **F**lecha, **Pa**ra, **Re**ce, **Ro**mbo» → Óvalo inicio/fin, Flecha flujo, Paralelogramo entrada/salida, Rectángulo proceso, Rombo decisión.

> BPMN tiene su propia notación (eventos en círculo, compuertas en rombo, carriles). **No está en las diapositivas** (fuera de las diapositivas).

> **Analogía:** El rombo es el «¿hay cuadro comparativo aprobado? Sí → OC; No → vuelve a cotización».

### 4.3 BPM también es una profesión (Clase 4, p. 5)
- **Sarah Kelley**, Certified Business Process Professional (**CBPP®**), experta en mejora continua y excelencia operacional (Swinerton, ABPMP International).
- Cita: «La certificación CBPP valida que puedes analizar, diseñar y mejorar procesos que generan valor real en las organizaciones».
- Un profesional BPM (4): **mejora** procesos, **genera** valor al negocio, **impulsa** la eficiencia, **lidera** el cambio.

### 4.4 Qué hace un profesional BPM (Clase 4, p. 6)
- «Diseña, analiza y mejora procesos para que las organizaciones sean más eficientes y generen valor».
- En la práctica (4 pasos): **Analiza** (entiende los procesos actuales) → **Diseña** (modela y documenta) → **Mide** (desempeño con datos e indicadores) → **Mejora** (propone e implementa cambios).
- **Caso real adidas (con Bizagi):** cadena de suministro en **400 fábricas**: **60 %** menos costos operativos, **50 %** menos tiempo al incorporar fábricas, **87 %** menos tiempo en aprobación de contratos. Fuente: caso de éxito adidas, Bizagi.

### 4.5 Dónde se aplica BPM (Clase 4, p. 7)
5 sectores:
1. **Comercio electrónico:** pedidos, pagos y entregas.
2. **Banca y finanzas:** crédito, cumplimiento y atención.
3. **Manufactura:** estandariza operaciones y reduce errores.
4. **Sector público:** agiliza trámites y mejora el servicio al ciudadano.
5. **Salud:** mejora la atención y el uso de recursos.

### 4.6 BPM en Ecuador (Clase 4, p. 8)
- **ABPMP Ecuador**: comunidad profesional (3 funciones): **comunidad profesional** (conecta y comparte mejores prácticas); **formación y certificación** (estándares internacionales y competencias BPM); **impacto en organizaciones**. «Ecuador está en el mapa global del BPM».

### 4.7 Competencias de un profesional BPM (Clase 4, p. 9)
5 competencias en secuencia:
1. **Analizar datos:** extraer, limpiar e interpretar datos.
2. **Entender procesos:** modelar y documentar cómo funcionan hoy.
3. **Detectar problemas:** cuellos de botella, variaciones y causas raíz.
4. **Comunicar hallazgos:** de forma clara y basada en evidencia.
5. **Proponer mejoras:** soluciones viables y cambios que generen valor.
- **Caso real:** una organización pública de EE. UU. analizada con **IBM Process Mining**. Tenían datos del proceso de compras, pero necesitaban descubrir cómo se ejecutaba realmente; la herramienta mostró el flujo real, variaciones, cuellos de botella y oportunidades.
- **Conclusión:** «**Tener datos no es lo mismo que entender el proceso**. Un profesional BPM convierte datos en decisiones».

### 4.8 Certificaciones BPM (Clase 4, p. 10)
- **Certificación BPM:** «credenciales que validan tus conocimientos y habilidades en gestión de procesos de negocio».

| Certificación | Emisor | Nivel / perfil | Costo |
|---|---|---|---|
| **CBPA®** | ABPMP International | Nivel básico; analista o inicio profesional | US$ 400-550 (+ US$ 40 de solicitud) |
| **CBPP®** | ABPMP International | Nivel profesional; profesional BPM con experiencia | US$ 500-650 (+ US$ 75 de solicitud) |
| **Bizagi** | Bizagi | Analista o diseñador de procesos | US$ 300 |
| **OCEB 2** | OMG (Object Management Group) | Profesionales de procesos y modelado | US$ 350 (referencial) |

- **Importante:** **Curso ≠ Certificación ≠ Experiencia**. En el curso aprendes; en la certificación te evalúan y acreditan; con la experiencia aplicas y generas resultados.

### 4.9 CBPA vs. CBPP (Clase 4, p. 11)

| | **CBPA®** Certified Business Process **Associate** | **CBPP®** Certified Business Process **Professional** |
|---|---|---|
| Nivel | Básico, inicio profesional | Profesional, con experiencia |
| Objetivo | Conocimiento fundamental en BPM y terminología básica | Experiencia y capacidad para **liderar** iniciativas BPM |
| Perfil ideal | Estudiantes, analistas, asistentes de procesos | Profesionales BPM, consultores, coordinadores y líderes |
| Experiencia requerida | **1.250 horas** en disciplinas BPM (o título universitario de 4 años que califique) | **Mínimo 4 años** en procesos de negocio (roles BPM) |
| Enfoque | Conceptos clave, ciclo de vida BPM, herramientas y buenas prácticas | Estrategia BPM, gobierno, mejora continua, medición de valor y liderazgo |
| Costo | US$ 400-550 + 40 | US$ 500-650 + 75 |

- «CBPA es tu punto de partida. CBPP es tu siguiente nivel profesional». Precios referenciales a mayo de 2024.
- Mnemotecnia: **A** de **A**sociado y **A**prendiz; **P** de **P**rofesional con **P**ráctica (4 años).

> **Analogía:** CBPA es como subir de Hierro a Plata en Valorant. CBPP es Inmortal: requiere horas de juego reales, no solo saber las reglas.

### 4.10 Reto: ruta profesional BPM (Clase 4, p. 12)
5 pasos: **1. Define** tu objetivo (analista, consultor, líder de procesos) → **2. Aprende** y practica (modelado, análisis, mejora continua, herramientas) → **3. Certifícate** y valida (CBPA, Bizagi, OCEB 2...) → **4. Gana** experiencia (proyectos reales, portafolio) → **5. Crece** y lidera.
- Preguntas: ¿Dónde estás hoy? ¿A dónde quieres llegar? ¿Qué pasos darás en 12-24 meses? «El mejor proceso que puedes diseñar es el de tu propio crecimiento».

---

## Clase 5: Componentes BPM (rótulo «Unidad 2 · Estructura del BPM · Clase 6»)

### 5.1 Qué necesita un proceso para funcionar (Clase 5, p. 2)
- Ejemplo: **reserva digital** en una plataforma de alojamiento (Hotel Vista Mar, Quito, 15-17 de junio de 2026, 2 huéspedes).
- Elementos:
  - **Personas:** cliente, recepción, limpieza, finanzas, soporte.
  - **Reglas:** disponibilidad, políticas de cancelación, verificación de pago, tarifas.
  - **Tecnología:** plataforma web, pasarela de pago, **PMS**, integraciones, automatizaciones.
  - **Actividades:** buscar, verificar disponibilidad, registrar reserva, cobrar, confirmar, asignar habitación.
  - **Datos:** datos del cliente, fechas, tipo de habitación, precio, inventario, métodos de pago.
  - **Resultado:** reserva confirmada, habitación disponible, cliente satisfecho, ingresos generados.
- **6 preguntas clave:** ¿Qué se hace? ¿Quién interviene? ¿Qué reglas se aplican? ¿Qué información se usa? ¿Qué tecnología lo hace posible? ¿Qué resultado se obtiene?
- **Idea clave:** «Un proceso no es solo una secuencia de pasos. **Es un sistema** donde varios componentes trabajan juntos para entregar valor».

### 5.2 Los 6 componentes clave del BPM (Clase 5, p. 3)
- Igual que la Clase 4, p. 2: Actividades, Roles, Reglas, Datos, Tecnología, Resultados. «Todo proceso está compuesto por seis elementos que trabajan juntos para entregar valor».
- Mnemotecnia: «**A**l **R**ato **R**egreso **D**e **T**u **R**ancho» → **A**ctividades, **R**oles, **R**eglas, **D**atos, **T**ecnología, **R**esultados.

### 5.3 Actividades + Roles (Clase 5, p. 4)
- «Toda actividad del proceso es realizada por alguien. Saber qué se hace y quién lo hace **evita retrasos y errores**».

| Actividad (¿qué se hace?) | Rol (¿quién lo hace?) |
|---|---|
| 1. Recibir pedido | Cliente (inicia el pedido y da sus datos) |
| 2. Validar pago | Plataforma / sistema (valida y confirma la transacción) |
| 3. Preparar pedido | Personal de bodega (prepara y empaqueta) |
| 4. Despachar pedido | Transportista (entrega al cliente final) |

- **Pregunta para el aula:** ¿qué pasaría si la actividad 2 no tiene un responsable claro? A. Se aprueba más rápido. **B. Nadie la ejecuta y el pedido se retrasa.** C. El cliente paga más. D. Se reduce el inventario. La respuesta lógica es **B**.

> **Analogía:** En Valorant, si nadie toma el rol de controlador, nadie tira humos y el ataque fracasa. En compras: si no está claro quién aprueba, el requerimiento se queda en «En aprobación» y no sale el viernes.

### 5.4 Reglas + Datos (Clase 5, p. 5)
- «Definen las **condiciones** y la **información** que necesita el proceso».
- **Reglas (¿bajo qué condición?):** pago aprobado → continúa; pago rechazado → se detiene.
- **Datos (¿con qué información?), 5:** cliente, producto, stock, dirección, pago.
- Ejemplo: un cliente compra un celular, el pago se aprueba, pero la **dirección está incorrecta**. La regla funcionó, pero un **dato incorrecto** hizo fallar el resultado.
- **Idea memorable:** «**Una buena regla con malos datos también produce un mal resultado**».

> **Analogía:** La regla «sin OC no hay factura» funciona, pero si el RUC del proveedor está mal cargado, la factura igual se rechaza. En de Una o en una transferencia bancaria: el pago se aprueba, pero si el número de cuenta está mal, el dinero no llega.

### 5.5 Tecnología (Clase 5, p. 6)
- «Es lo que permite **ejecutar, automatizar y dar soporte** al proceso».
- 5 elementos:
  1. **Plataforma web / app:** interfaz donde el cliente hace la reserva.
  2. **Pasarela de pago:** procesa y valida el pago de forma segura.
  3. **Base de datos:** almacena reservas, clientes, habitaciones y pagos.
  4. **Integraciones y APIs:** conectan con inventario, correo de confirmación y sistemas contables.
  5. **Infraestructura y soporte:** disponibilidad, seguridad y rendimiento.
- Idea clave: la tecnología adecuada hace que el proceso sea **más rápido, confiable y escalable**.

### 5.6 Medición + Indicadores (Clase 5, p. 7)
- «Permiten saber si el proceso funciona bien y dónde podemos mejorar». Sirven para evaluar el desempeño, tomar decisiones y mejorar continuamente.
- **4 indicadores clave:**
  1. **Tiempo de ciclo:** tiempo total desde que el cliente inicia la compra hasta que recibe el pedido.
  2. **Tasa de conversión:** porcentaje de **visitas** que se convierten en **compras**.
  3. **Costo por pedido:** costo promedio de procesar y entregar cada pedido.
  4. **Satisfacción del cliente:** nivel de satisfacción con el proceso y el servicio.
- **Idea clave:** «**Lo que no se mide, no se puede mejorar**».

> **Analogía:** Tu tracker de Valorant: el ACS y el porcentaje de headshots son los indicadores. En compras, el tiempo de ciclo va desde el requerimiento hasta la factura.

### 5.7 Resultados (Clase 5, p. 8)
- «Son los productos o servicios que el proceso entrega y el **impacto** que genera en el cliente y en la organización».
- **No es resultado:** solo recibir el pedido; recibirlo por sí solo no asegura que el proceso generó valor.
- **Sí es resultado:** pedido correcto + entrega a tiempo + cliente satisfecho. **Valor entregado = cliente satisfecho.**
- Un buen proceso no solo se mide por lo que hace, sino por el **valor** que entrega al cliente y al negocio. Los indicadores permiten comprobar si los resultados se cumplen.
- **Idea clave:** «El objetivo del proceso es entregar **valor real al cliente**. Ese es el resultado».

---

## Tabla «no confundir»

| Concepto A | Concepto B | Diferencia |
|---|---|---|
| **Proyecto (PMP)** | **Proceso (BPM)** | El proyecto es temporal, con inicio y fin; el proceso es continuo, repetitivo y recurrente |
| Herramientas PMP: Project, Planner, Trello, Jira | Herramientas BPM: Bizagi, Appian, Camunda, Azure DevOps | Trello y Jira son de proyectos; Bizagi y Camunda son de procesos |
| **4 verbos** de la definición BPM (diseñar, ejecutar, monitorear, mejorar) | **5 fases** del ciclo (+ **analizar**) | Analizar va entre monitorear y mejorar |
| **5 elementos** que gestiona BPM (Clase 2): actividades, responsables, información, reglas, resultados | **6 componentes** (Clase 4-5): actividades, roles, reglas, datos, **tecnología**, resultados | Se agrega tecnología |
| **3 pilares**: personas, procesos, tecnología | **5 actores** (Clase 1): cliente, plataforma, restaurante, repartidor, otros soportes | Pilares de BPM vs. participantes de un proceso concreto |
| Entrada → Actividades → Salida | Necesidad → Proceso → Resultado | La primera mira qué se transforma; la segunda, por qué existe y qué gana el cliente |
| Rectángulo = **proceso** | Rombo = **decisión** | El rombo tiene salida verdadero/falso |
| Paralelogramo = **entrada/salida** de datos | Óvalo = **inicio/final** | No intercambiarlos |
| **CBPA** (Associate) | **CBPP** (Professional) | CBPA: 1.250 h o título de 4 años, US$ 400-550 + 40. CBPP: 4 años, US$ 500-650 + 75 |
| ABPMP (emite CBPA y CBPP) | OMG (emite OCEB 2) | Bizagi certifica en su herramienta, US$ 300 |
| Curso | Certificación | Curso = aprendes; certificación = te evalúan y acreditan; experiencia = aplicas |
| **Tener datos** | **Entender el proceso** | Caso IBM Process Mining: no son lo mismo |
| Regla buena | Datos malos | Una buena regla con malos datos también produce un mal resultado |
| **Recibir el pedido** | **Resultado** | Resultado = pedido correcto + a tiempo + cliente satisfecho |
| Tiempo de ciclo | Tasa de conversión | Tiempo total de la compra a la entrega vs. % de visitas que compran |
| Proceso informal | Proceso gestionado | Lo informal se hace «como siempre»; lo gestionado es claro, medible y mejorable |
| Contratar más personal | Mejorar el proceso | ClickShop triplicó el personal y los reclamos subieron 17 veces |

---

## Las 12 cosas que sí o sí debes saber

1. **Visión por procesos:** entender y gestionar el trabajo como un flujo de actividades conectadas que transforman entradas en resultados que generan valor para el cliente (Clase 1, p. 7).
2. **PMP = proyectos temporales** (inicio y fin); **BPM = procesos continuos y repetitivos** (Clase 1, p. 3).
3. **BPM** es un enfoque para **diseñar, ejecutar, monitorear y mejorar** procesos y generar valor para el cliente y el negocio. No es solo dibujar: es gestionar de punta a punta (Clase 2, pp. 2-3).
4. **Ciclo BPM, 5 fases:** Diseñar → Ejecutar → Monitorear → Analizar → Mejorar (Clase 2, p. 3).
5. **3 pilares:** Personas + Procesos + Tecnología (Clase 2, p. 5).
6. **6 componentes:** Actividades (qué), Roles (quién), Reglas (bajo qué condición), Datos (con qué información), Tecnología (con qué se ejecuta), Resultados (qué valor) (Clase 4, p. 2; Clase 5, p. 3).
7. **Símbolos del diagrama de flujo:** óvalo (inicio/final), flecha (flujo), paralelogramo (entrada/salida), rectángulo (proceso), rombo (decisión verdadero/falso) (Clase 4, p. 3).
8. **Beneficios de BPM:** menos tiempo (72 → 24 h, −67 %), menos errores, menores costos ($8,40 por devolución; $470,40 al día), mejor experiencia, productividad (330 → 150 min/día), decisiones con datos y escalabilidad (Clase 3).
9. **Indicadores clave (4):** tiempo de ciclo, tasa de conversión, costo por pedido y satisfacción del cliente. «Lo que no se mide, no se puede mejorar» (Clase 5, p. 7).
10. **Una buena regla con malos datos también produce un mal resultado** (Clase 5, p. 5).
11. **CBPA vs. CBPP** (ABPMP): CBPA básico, 1.250 h, US$ 400-550; CBPP profesional, 4 años, US$ 500-650. Bizagi US$ 300; OCEB 2 (OMG) US$ 350 (Clase 4, pp. 10-11).
12. **Resultado ≠ recibir el pedido.** Resultado = pedido correcto + a tiempo + cliente satisfecho = valor (Clase 5, p. 8).

---

## Mnemotecnias

- **6 componentes, «ARRDTR»:** «**A**l **R**ato **R**egreso **D**e **T**u **R**ancho» (Actividades, Roles, Reglas, Datos, Tecnología, Resultados). Van en el orden de las preguntas: qué, quién, cuándo decide, con qué información, con qué herramienta y para qué.
- **Ciclo BPM, «DEMAM»:** «**D**iego **E**s **M**uy **A**migo **M**ío» (Diseñar, Ejecutar, Monitorear, Analizar, Mejorar).
- **5 elementos de la Clase 2, «ARIRR»:** Actividades, Responsables, Información, Reglas, Resultados. Son los 6 componentes **sin tecnología**.
- **3 pilares, «PPT»:** Personas, Procesos, Tecnología (como el PowerPoint).
- **Símbolos:** «**O**jo, **F**lecha, **Pa**ra, **Re**ce, **Ro**mbo».
- **PMP vs. BPM:** **P**royecto = **P**unto final; **B**PM = **B**ucle.
- **Herramientas BPM, «BACA»:** Bizagi, Appian, Camunda, Azure DevOps. **Herramientas PMP, «PPTJ»:** Project, Planner, Trello, Jira.
- **Profesional BPM en la práctica:** «**A**na **D**ice **M**ás **M**ejoras» (Analiza, Diseña, Mide, Mejora).
- **Competencias (5):** «Datos, Procesos, Problemas, Comunicar, Proponer»: analizar datos → entender procesos → detectar problemas → comunicar hallazgos → proponer mejoras.
- **Ruta profesional, «DACGC»:** Define, Aprende, Certifícate, Gana experiencia, Crece.
- **Cifra de costo:** 3,20 + 3,20 + 0,80 + 1,20 = **8,40**; × 56 = **470,40**.
