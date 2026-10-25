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

---

# Segunda parte · bloque F (procesos y AS-IS)

## Qué se hizo
- **Búsqueda D03 y D04** (`--solo-api --desde 2021`): salieron 114 candidatas. Quedaron así:
  - **5 verificadas:** `nizio_2021`, `radhakrishnan_2025`, `mendoza_2024b`, `garcia_2026` y `loor_2025`;
  - **7 candidatas:** se quedan por relevantes (motivo en `## Triaje (25-oct)` de cada ficha);
  - **102 descartadas:** fuera de tema, preprints, tesis o fecha anterior a 2021 (motivo en `## Descarte (25-oct)`).
- **Especificación oficial de BPMN:** `omg_2013` (OMG, BPMN 2.0.2), verificada en la p. 1. Es la «fuente oficial de BPMN» que pide el `[FALTA-FUENTE: … CTX-PROC]` del Cap. 2. La frase propuesta está en la ficha.
- **AS-IS v0.1** en `07_Flujos_Diseno/` (S2-T06, S2-T08 y S2-T15 juntas):
  - `2026-10-25_AS-IS_v0.1.md`: los pasos con su fuente, los 5 puntos donde se pierde tiempo, cómo se conectan con M1–M4 y las preguntas para validar en campo;
  - `2026-10-25_AS-IS_v0.1.bpmn`: BPMN 2.0 estándar, se edita en demo.bpmn.io;
  - `2026-10-25_AS-IS_v0.1.png`: la figura para la Revisión 1.
  - Es un **borrador sin validar en campo**, armado con el Informe Final del 22-jul (antecedente vigente).
- Total en la base: **71 verificadas**.

## Afirmaciones con fuente
- **CTX-PROC → propongo ✅:** OMG (2013, p. 1) como fuente oficial, más Nizioł et al. (2021, p. 199), Martínez Mendoza et al. (2023, p. 4836), Radhakrishnan (2025, resumen) y Zambrano Loor y García Vera (2025, p. 79). Así ya no hace falta Dumas et al. (2018). Los 4 videos candidatos de Bizagi no se usan.

## PDF para bajar a mano
- Moreira et al. (2023), *Business Process Automation in SMEs*, LNBIP. El repositorio pide JavaScript: http://hdl.handle.net/10400.2/14004
- Radhakrishnan (2025), la versión publicada en IET (pp. 69–74), para citar otras páginas además del resumen: https://doi.org/10.1049/icp.2025.3640

## Error de `buscar.py`
Volvió a caerse con el `IndexError` de `citekey()` del que te hablé en el reporte del 21. No toqué tu script: lo corrí desde un envoltorio (fuera del repo) que agrega letras dobles solo para esa corrida. Por eso hay un citekey `anonimo_2023aa`.

## Dudas para Víctor
4. **Meta del seguimiento:** el punto ❹ del AS-IS (seguimiento de memoria) no lo mide ninguna meta, porque M3 solo cuenta hasta el primer contacto. ¿Lo dejamos así o se ajusta?
5. **Citekeys por renombrar** (con `git mv`, si estás de acuerdo):
   - `mendoza_2024b` → `martinez_2023`: el apellido es Martínez Mendoza y el número es de 2023;
   - `garcia_2026` → `sanchezgarcia_2026`.
6. **Para la Revisión 1:** el AS-IS va como «modelo preliminar». Las gráficas de datos (S2-T17) no llegan porque no hay datos de campo: Torvesa todavía no autoriza.

---

# Tercera parte · bloque G (herramientas)

## Qué se hizo
- **12 fichas verificadas** en `02_Fuentes/Costos_Viabilidad/`, todas con la página oficial y la fecha de consulta (25-oct):
  - **CRM:** `hubspot_sf`, `zoho_sf`, `pipedrive_sf` y `kommo_sf`;
  - **mensajería:** `meta_sf` (WhatsApp Business), `telegram_sf` y `slack_sf`;
  - **bóveda:** `notion_sf` y `logseq_sf`, para comparar con las fichas de Obsidian del 21-oct;
  - **condiciones de datos de los LLM** (lo que quedó pendiente para la LOPDP): `anthropic_2026`, `anthropic_sfb` y `openai_sfb`.
- **Inventario v0.1** (S2-T11): `07_Flujos_Diseno/2026-10-25_Inventario_Herramientas_v0.1.xlsx`. Tiene 13 herramientas, al menos 3 por componente (bóveda, CRM, LLM y mensajería), con 4 hojas: inventario, criterios C1–C8, costo ilustrativo y pendientes. El cronograma pedía la fecha del 24; va con la de hoy, que es cuando se hizo.
- **Búsqueda D05** (CRM móvil): 13 candidatas de OpenAlex. Quedaron así:
  - **7 candidatas:** se quedan por relevantes (motivo en `## Triaje (25-oct)`);
  - **6 descartadas:** fuera de tema o revista dudosa (motivo en `## Descarte (25-oct)`).
- Total en la base: **83 verificadas**.

## Hallazgos que importan para el diseño
- **WhatsApp:** Kommo es el único CRM del inventario que se conecta con la plataforma oficial de WhatsApp Business. En las páginas de precios de HubSpot, Zoho y Pipedrive no aparece WhatsApp.
- **Costo de WhatsApp:** desde el 1-oct-2026, Meta da 1 000 mensajes de servicio gratis al mes por número y cobra USD 0,0113 desde el 1 001 (tarifa de Ecuador). Lo que escribe el cliente no se cobra. Si Torvesa responde menos de 1 000 mensajes al mes, ese tramo sale gratis.
- **Kommo pide un mínimo de 6 meses**, más que la validación en operación experimental.
- **LOPDP en los LLM:** Anthropic y OpenAI no entrenan con los datos de la API. La diferencia está en la retención: OpenAI guarda registros de abuso hasta 30 días por defecto; Anthropic no guarda el contenido de las conversaciones por defecto, salvo en algunos modelos que exigen 30 días.
- **Ofertas temporales:** HubSpot muestra Starter a USD 7 o 10 (oferta para clientes nuevos) frente a USD 20 de lista. Para el VAN se usa el precio de lista.

## Decisión: proveedor de LLM
- **Diego eligió Claude Sonnet 5.5 (Anthropic)**, gama media. Tiene el mismo precio que gpt-6.1-sol (USD 2 de entrada y 10 de salida por millón de tokens; unos USD 13 al mes con el supuesto de 1 000 consultas), y por defecto no guarda el contenido de las conversaciones ni entrena con ellas (`anthropic_2026`, `anthropic_sfb`).
- **Propuesta para la matriz (la actualizas tú): A36 → ✅**, con `anthropic_sf` (precios) más `anthropic_2026` y `anthropic_sfb` (datos). Falta tu visto bueno.

## Lo que queda para el bloque H
- Definir pesos y puntuar con los criterios C1–C8.
- Revisar las condiciones de datos del nivel pagado de Gemini y de los CRM.
- Escribir el resumen de 1 página sobre CRM y flujos (S1-T26).

## Error de `buscar.py`, otra vez
En D05 se cayó con el mismo `IndexError` de `citekey()`. Esta vez no usé el envoltorio: OpenAlex alcanzó a guardar sus 13 resultados, pero Crossref se cayó y Semantic Scholar no devolvió nada. Cuando arregles `citekey()` (letras dobles después de la «z»), conviene repetir D05 con Crossref.

## Dudas para Víctor
7. **¿Afirmación para los CRM y la mensajería?** En la matriz no hay ninguna A# para el costo del CRM ni de WhatsApp, así que las fichas nuevas van sin afirmación (solo el objetivo 5.3). ¿Abrimos una o entran en A36 como «costos de herramientas»?
8. **Supuestos del costo ilustrativo:** 3 usuarios, 1 000 consultas al mes y 600 mensajes de WhatsApp al mes. Son supuestos marcados en amarillo y se reemplazan con los datos de campo.

---

# Cuarta parte · bloque H (cierre)

## Qué se hizo
- **10 fichas verificadas** más en `02_Fuentes/Costos_Viabilidad/`, para los criterios que faltaban:
  - **app móvil (C3):** `obsidian_sfc` y `notion_sfb`;
  - **datos y LOPDP (C5):** `google_2026b` (nivel pagado de Gemini), `hubspot_2026`, `zoho_sfb`, `pipedrive_2026`, `kommo_2026`, `whatsapp_2025`, `slack_sfb` y `telegram_2026`.
- **Inventario v0.2** (S2-T14): `07_Flujos_Diseno/2026-10-25_Inventario_Herramientas_v0.2.xlsx`. Es un archivo nuevo: la v0.1 no se tocó. Agrega la hoja **«Puntuación»** (pesos propuestos, puntaje de 1 a 3 por criterio y el porqué de cada nota) y cierra los pendientes de la v0.1.
- **Resumen de 1 página para ti** (S1-T26): `02_Fuentes/Casos_Estudio/2026-10-25_Resumen_CRM_Flujos.md`.
- Total en la base: **93 verificadas**.

## Resultado del inventario
- **Bóveda:** Obsidian (2,81).
- **LLM:** Claude Sonnet 5.5 (2,70), que es el que eligió Diego. Con pesos iguales empata con Gemini (2,67).
- **Mensajería:** WhatsApp para el cliente (3,00) y Slack para los avisos internos.
- **CRM:** empate entre Zoho y Kommo (2,39). Con pesos iguales, Zoho queda primero.

## Dudas para Víctor
9. **¿Entra un CRM al diseño?** No está entre los componentes del diseño aprobado. Sin CRM, el punto ❹ del AS-IS (seguimiento) queda sin herramienta, y además ninguna meta lo mide (duda 4). Es para la tutora en la Revisión 1.
10. **Pesos:** propuse C5 (datos y LOPDP) 25 %, C1 (costo) 15 %, C3 (app móvil) 15 %, C4 (WhatsApp) 15 %, C6 (madurez) 10 %, C8 (encaje con el diseño) 10 %, C2 (plan gratuito) 5 % y C7 (plazo de contrato) 5 %. Si los cambias en la fila 5 de la hoja «Puntuación», los puntajes se recalculan solos.
