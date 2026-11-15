---
titulo: "Estudio de costos y viabilidad de TEAMSLASH: guía de lectura"
version: v0.1
fecha: 2026-11-16
autor_borrador: "Claude (Frente B); Víctor revisa antes de entregar"
para: "Directora de carrera (Contabilidad y Auditoría)"
base: "Modelo financiero v0.2 · Análisis financiero v0.2 · Caso de negocio v0.1 (15-nov)"
tags: [guia, modelo-negocio, profe]
---

# Guía de lectura

**Qué es esto.** Es el estudio de costos y viabilidad del sistema que proponemos para la Constructora Torvesa, como parte de nuestra tesis. Partimos de **un solo cliente, Torvesa**. Primero mostramos la necesidad y la oportunidad, y después los números. El crecimiento hacia otras empresas va al final y como anexo, con un techo realista de 20 empresas.

## En qué orden leerlo

| # | Archivo | Qué tiene | Tiempo |
|---|---|---|---|
| 1 | Esta guía | Orden de lectura, cifras clave y preguntas | 3 min |
| 2 | Presentación de 1 minuto | La idea completa en 5 diapositivas | 1 min |
| 3 | Caso de negocio | Necesidad, oportunidad, propuesta, viabilidad y crecimiento | 10 min |
| 4 | Análisis financiero | Cómo se armó cada cifra, qué cambió con datos reales y qué falta | 10 min |
| 5 | **Modelo financiero (Excel)** | El estudio completo: supuestos → inversión → costos → precio → ingresos → estado de resultados → flujo de caja → VAN, TIR, periodo de recuperación, beneficio/costo y punto de equilibrio | 15 min |
| 6 | Matriz de herramientas (Excel) | Por qué elegimos estas herramientas y no un CRM comercial | 5 min |
| 7 | Por qué nosotros | Comparación con la competencia, valor agregado y desventajas | 5 min |
| 8 | Anexo: estudio de costos por tipo de empresa (Excel) | Cómo cambia la recuperación si el cliente es una constructora, una ferretería o una veterinaria; techo de 20 empresas | Opcional |
| 9 | Exposición en 1 página | Una idea por diapositiva, con su fuente | 2 min |

**Cómo usar el Excel.** En la hoja **Panel** hay dos listas desplegables: el escenario (pesimista, base u optimista) y el plan (Estándar o Premium). Todo el libro se recalcula al cambiarlas. Cada fila tiene una columna «Qué significa» y cada encabezado tiene una nota. En la hoja **Supuestos**, la columna **Tipo** dice si el valor es DATO (con fuente), DECISIÓN (nuestra) o SUPUESTO (por investigar), y la columna **Qué investigar** dice qué falta.

## Las 5 cifras clave (escenario base, sin IVA)

| Cifra | Valor | Qué significa |
|---|---|---|
| Precio del plan Premium | USD 275 al mes + USD 311 de implementación | Es el plan que hace viable el proyecto; el Estándar (USD 175) no recupera las horas ya trabajadas |
| Inversión inicial de TEAMSLASH | USD 2.243 | USD 1.852 en horas ya trabajadas (200 h a USD 9,26) y USD 391 en efectivo |
| VAN y TIR del proyecto (Premium) | VAN USD 427 · TIR 26 % con TMAR 15 % | Viable, pero por poco: beneficio/costo 1,03 y recuperación en unos 25 meses |
| Beneficio para Torvesa | VAN USD 13.618 | El sistema se paga si Torvesa recupera 1,9 obras al año que hoy pierde |
| Peso del sistema en una constructora pequeña típica | 56 % de su utilidad neta anual | Por eso se vende por las obras que recupera, no por el tiempo que ahorra |

**La tarifa por hora no es inventada.** Sale del sueldo de un desarrollador semi-senior en Ecuador (USD 1.084 al mes, Ekos Negocios, 2025), más el aporte patronal (12,15 %), los décimos, las vacaciones y los fondos de reserva del Código del Trabajo: USD 9,26 la hora.

## Qué es dato y qué es supuesto

- **Lo que depende de nosotros** (costos, precios, leyes, mercado): el **71 %** de los valores es dato verificado o decisión nuestra. Hay 30 fuentes en la hoja Fuentes del Excel.
- **Lo que depende de Torvesa** (sus ventas, su margen, cuántas obras pierde): solo el **6 %** es dato. Es lo que más falta, y por eso pediremos a Torvesa sus declaraciones de impuesto a la renta (formulario 101) de 2023 a 2025.
- **Datos reales que nos obligaron a cambiar cifras:** la TMAR del 12 % no se sostiene, porque solo la prima de riesgo de Ecuador es 17,18 %; el margen neto de las constructoras de Pichincha es de 1,89 %, no de 10 %; el aporte patronal es 12,15 % con SECAP e IECE.
- **Hallazgo pendiente:** según el SRI, Torvesa está registrada como constructora de carreteras y no aparece en la Superintendencia de Compañías. Lo estamos confirmando.

## Las 4 preguntas que le queremos hacer

1. **Estructura.** ¿El orden del estudio (inversión → costos → precio → ingresos → estado de resultados → flujo de caja → evaluación) es el correcto para un estudio de factibilidad, o falta algún estado o indicador?
2. **Tasa de descuento.** ¿Le parece razonable una TMAR del 15 % para un proyecto pequeño en Ecuador, sabiendo que la prima de riesgo del país es 17,18 %? ¿Cómo la armaría usted?
3. **Forma legal e impuestos.** ¿Conviene trabajar como personas naturales independientes o como una SAS desde el inicio? ¿Aplica el RIMPE a servicios de software, y aplica el 15 % de participación de trabajadores si no tenemos empleados?
4. **Horas ya trabajadas.** ¿Es correcto tratar las 200 horas del levantamiento como inversión (activo intangible amortizado al 33 % anual) y recuperarlas en el precio, o deben ir como gasto?
