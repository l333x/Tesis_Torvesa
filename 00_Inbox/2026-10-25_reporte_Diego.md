---
titulo: Reporte de Diego — domingo 25-oct
fecha: 2026-10-25
autor: Diego Bermeo
ia: Claude (Claude Code)
tags: [diego, reporte, sprint2]
---

# Reporte de Diego · dom 25-oct (bloques D y E, con retraso)

## Qué se hizo
- **Junté el bloque C con tu trabajo del 21-oct.** Mi trabajo del 21 no se había subido y tu commit tocaba los mismos archivos:
  - **`lewis_2020`:** la verificamos los dos. **Quedó la tuya** y borré la mía antes de subir: tú citas la paginación de NeurIPS (p. 9464) y yo había anotado «p. 2», la página del PDF.
  - **`fuentes.sqlite` y `fuentes.csv`:** uní tu versión con la mía sin tocar tus filas:
    - agregué mis 62 fichas de la búsqueda D01/D02 y sus 7 búsquedas;
    - actualicé el estado de esas fichas (34 cambios) y di de alta mis 10 fichas de búsqueda manual;
    - con eso queda resuelta la duda 2 del reporte del 21.
  - Total en la base: **65 verificadas** (tus 49, mis 13 del bloque C y 3 de hoy), 340 candidatas y 231 descartadas.
- **D · Documentación oficial:**
  - **A31–A34 y A38:** ya los habías respaldado tú el 21-oct, así que no los repetí.
  - **A36:** 3 fichas verificadas en `02_Fuentes/Costos_Viabilidad/`, todas con URL y fecha de consulta: `anthropic_sf`, `openai_sf` y `google_2026`.
  - **Tabla de precios:** `02_Fuentes/Costos_Viabilidad/2026-10-25_Tabla_Precios_LLM.md`. Compara 3 gamas por proveedor y trae un costo ilustrativo con **supuestos**: 1 000 consultas al mes, de 4 000 tokens de entrada y 500 de salida. La gama media sale entre USD 10 y 14 al mes.
- **E · Resumen:** `02_Fuentes/Tecnologia_IA/2026-10-25_Resumen_Bovedas_RAG.md`. Junta mis fichas y las tuyas. `IA_DIEGO.md` pedía la fecha del 21, pero lo fecho hoy, que es cuando se hizo.

## Afirmaciones con fuente
- **A36 → propongo 🟡 Parcial:** ya hay precios oficiales de 3 proveedores. Pasa a ✅ cuando se elija el proveedor en el bloque G. Para el Cap. I, viabilidad (e): (Anthropic, s.f.; Google, 2026; OpenAI, s.f.).
- **A37:** tu matriz pedía «un estudio 2023+ sobre alucinación con RAG». Lo cubre **Béchard y Marquez Ayala (2024, p. 233)**: en una aplicación empresarial, los errores bajaron de hasta 21 % a menos de 7,5 %. Para matizar está Magesh et al. (2025, p. 217): con RAG, las herramientas comerciales todavía se equivocan entre 17 % y 33 % de las veces.

## Hallazgos que importan para el diseño
- **LOPDP:** en el nivel gratuito de Gemini, Google usa los datos para mejorar sus productos. Con datos de clientes de Torvesa solo sirve un nivel pagado.
- **Precio en 2027:** Gemini 3.8 Flash dobla su precio el 1-ene-2027, justo cuando cae la validación en operación experimental.

## PDF para bajar a mano
Los mismos del reporte del 21-oct: Aviv et al. (2021), López y Yepes (2024), Altinok et al. (2026) y Durst (2026).

## Dudas para Víctor
1. **¿Actualizas tú la matriz** con A36 (parcial) y Béchard en A37? No la toqué porque es tuya.
2. **IVA:** ¿aplica IVA en Ecuador a los servicios digitales del exterior, como la API de IA? Lo dejé **sin fuente** en la tabla de precios porque es parte de las finanzas.
3. Siguen abiertas las dudas 1 y 3 a 7 del reporte del 21-oct (error de `citekey()`, `ortega_2026a`, Riascos, Khoa y Baqar).
