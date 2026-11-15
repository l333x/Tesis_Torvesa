---
titulo: "El capítulo I en 1 página (actualizado al 16-nov) — para Diego"
version: v0.2
fecha: 2026-11-16
autor_borrador: "Claude (Frente B); Víctor lo revisa antes de enviarlo"
tarea: "S2-T13"
para: Diego
base: "Cap. I p1 y p2 v0.3 (27-oct) · resumen v0.1 del 19-oct · hallazgos del 15-nov"
reemplaza: "06_Capitulos/2026-10-19_Resumen_Cap1.md (se conserva)"
tags: [resumen, capitulo1, diego]
---

# El capítulo I en 1 página

## Qué dice

1. **Contexto.** La IA crece en las empresas grandes, pero poco en las pequeñas: en la OCDE la usa el 11,9 % de las pymes. La construcción es de los sectores menos digitalizados. En Ecuador cayó 7,9 % en 2024 y volvió a crecer 2,7 % en 2025.
2. **El problema de Torvesa.** Las solicitudes esperan horas, cada cotización se arma casi desde cero y el historial del cliente vive en el celular de quien lo atiende. Si esa persona se va, se lleva sus clientes.
3. **Pregunta central.** ¿Cómo diseñar un sistema que permita responder más rápido, dar continuidad a la atención y conservar un historial verificable de cada cliente?
4. **Objetivos.**
   - OE1: diagnóstico.
   - OE2: diseño, con viabilidad económica para Torvesa (VAN y TIR).
   - OE3: prototipo funcional de los componentes.
   - OE4: validación del diseño en operación experimental controlada, del 23-nov al 5-dic.
5. **Metas M1 a M6.**
   - M1: primer contacto en menos de 15 minutos. Es una meta de diseño, no un dato probado.
   - M2: menos tiempo por cotización.
   - M3: menos clientes perdidos antes del primer contacto.
   - M4: recuperar mejor el historial de un cliente ajeno.
   - M5: el 100 % de las alteraciones del registro detectadas.
   - M6: usabilidad.

## Qué cambió desde el 19-oct (y te afecta)

- **La forma de medir es una propuesta para la tutora:** no recoger datos de personas (DEC-21 a DEC-23). Si la acepta, M2 y M4 salen de **tus casos de prueba** CP-01 y CP-02, M5 de CP-03 y M6 de una evaluación heurística en lugar del SUS.
- **Tres casos de prueba, no cuatro.** El Cap. I dice «cuatro» y hay que corregirlo, salvo que la evaluación heurística cuente como el cuarto.
- **Torvesa en el SRI:** aparece como constructora de **carreteras** (actividad F4210) y no está en la Superintendencia de Compañías. Hay que confirmar con la empresa qué hace y qué tipo de sociedad es, porque cambia la descripción del capítulo.
- **El estudio de costos ya tiene cifras** (15-nov): Premium USD 275 al mes + USD 311; VAN para Torvesa USD 13.618. Casi todo lo de Torvesa sigue siendo supuesto.

## Lo que necesitamos de Torvesa (tu frente)

| Dato | Para qué | Marcador en el capítulo |
|---|---|---|
| Qué hace la empresa (vías, edificación o ambas) y qué tipo de sociedad es | Describir bien a Torvesa en el capítulo I | FALTA-DATO A1 |
| Número de colaboradores y cuántos atienden clientes | Alcance de la validación | FALTA-DATO A2, A3 |
| Fechas y horas de 3 meses de solicitudes, sin datos de clientes | Línea base de M1 y M3 | FALTA-DATO M1, M3 |
| Cuántas solicitudes llegan por semana | Saber si dos semanas alcanzan | FALTA-DATO (limitaciones) |
| Autorización escrita y fechas de la validación | Arrancar el 23-nov | — |
| Formularios 101 de 2023 a 2025 | Estudio de costos con cifras reales | — |

El borrador del mensaje está en la bandeja de entrada, con la fecha de hoy.
