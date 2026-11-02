---
titulo: Reporte de Diego — 2-nov-2026
fecha: 2026-11-02
autor: Diego Bermeo
ia: Claude (Claude Code)
bloques: [L, N, M, O, P]
tags: [diego, reporte, sprint3, sprint4]
---

# Reporte de Diego · lunes 2-nov

## Qué se hizo
- **Bloque L, elicitación (S3-T17):** `07_Flujos_Diseno/2026-10-27_Elicitacion_Requerimientos_v0.1_Diego.docx`, con control de cambios y 11 comentarios. La v0.1 no se tocó. Claude saca la v0.2 cuando Víctor revise.
  - **PEN-01 y CON-04 cerrados:** revisé el código de TEAMSLASH. La versión 2 (23-jul-2026) guarda en **PostgreSQL** en Railway; Google Sheets era la versión 1, hecha con Apps Script. El Informe Final describe la v1 y el pitch, la v2.
  - **Hallazgo:** el MVP **no está desplegado**. Al 2-nov, Railway responde «Application not found». Cambié el supuesto de 14.3 y agregué el riesgo **RIE-07**.
  - **Requerimiento nuevo RQ-24:** guardar la hora del primer contacto. Sin él, M1 no se puede medir, porque el MVP solo guarda la hora de ingreso.
  - **Criterios más medibles:**
    - RQ-14: 5 fichas en modo avión y sincronización en 10 minutos o menos;
    - RQ-15: la cuenta de la base de datos solo puede agregar eventos.
  - **RQ-02:** propongo sacar el teléfono y el correo de la alerta, por minimización de datos (LOPDP).
  - **Correcciones de hechos:** CON-01 (el MVP tiene 4 estados, no 3), FNT-04 y la sección 8.1.
- **Bloque N, resumen del AS-IS (S3-T19):** `07_Flujos_Diseno/2026-11-01_Resumen_AS-IS.md`. Una página con los 5 puntos de pérdida, la función del sistema que ataca cada uno y qué ya existe en TEAMSLASH frente a lo que es nuevo.

- **Bloque M, modelos (S3-T18 y S3-T12; cierra PEN-11):**
  - **Casos de uso:** `07_Flujos_Diseno/2026-10-31_Casos_Uso_v0.1.png`, con su `.drawio` editable. Son 12 casos y todos tienen escenario.
  - **Modelo conceptual:** `2026-10-31_Modelo_Conceptual_v0.1.png`, también con su `.drawio`. Tiene 9 conceptos, con colores según dónde vive cada uno.
  - **Explicación y tabla de trazabilidad** (caso de uso → actores → escenario → requerimientos): `2026-10-31_Casos_Uso_y_Modelo_Conceptual_v0.1.md`.
  - **Plantilla TO-BE:** `2026-10-31_Plantilla_TO-BE_v0.1.md` y `.bpmn`, con los 6 pasos P1–P6, los carriles, las reglas de dibujo y la ficha que se llena en cada parte.

- **Bloque O, TO-BE v0.1 (S4-T01, S4-T03, S4-T05), adelantado al lunes:**
  - Hay tres partes: `07_Flujos_Diseno/2026-11-04_TO-BE_v0.1_parte1`, `_parte2` y `_parte3`. Cada una tiene un `.bpmn` que se edita en bpmn.io o en Camunda, su `.png` y una ficha `.md`.
    - **Parte 1:** recepción, asignación, aviso y primer contacto (P1–P4).
    - **Parte 2:** cotización asistida y traspaso del cliente (P5–P6).
    - **Parte 3:** recordatorios, seguimiento y reasignación.
  - **Se cumple lo que pedía el bloque:** cada paso tiene disparador y responsable, y quedan cubiertos los 6 pasos del flujo y los 5 puntos del AS-IS.
  - **Validación:** revisé con un script que el BPMN sea correcto (referencias, flujos dentro de cada pool, ningún nodo suelto). No lo abrí en bpmn.io.
  - Lo que no está confirmado con Torvesa va marcado en el diagrama como «por validar» (PEN-08, CON-06 y la regla de asignación).
  - **Quedan fuera:**
    - el reporte semanal (RQ-08);
    - la verificación de integridad (RQ-16);
    - la eliminación de datos (RQ-19).

    No son pasos del flujo de atención. Se pueden dibujar como parte 4.

- **Bloque P, bóveda del sistema v0.1 (S4-T07, S4-T09, S4-T11), adelantado:** está en `07_Flujos_Diseno/Boveda_Sistema/` (29 archivos). Se abre en Obsidian con «Abrir carpeta como bóveda».
  - **Carpetas:** clientes, solicitudes, cotizaciones, plantillas de cotización, equipo, `_Contactos` y plantillas de notas. Todo se explica en `00_Inicio.md`.
  - **Ejemplos ficticios:** 4 clientes, 6 solicitudes en los 5 estados, 2 cotizaciones sin precios, 3 vendedores genéricos («Vendedor A, B y C») y 2 plantillas de cotización con rubros propuestos. Cada nota dice que es ficticia.
  - **Tableros con Bases**, que viene con Obsidian; la sintaxis la revisé en la ayuda oficial el 2-nov:
    - pendientes por vendedor, con una vista «Sin primer contacto»;
    - clientes;
    - cotizaciones.
  - **Comprobado con un script** que reproduce el filtro del tablero: el Vendedor A tiene 2 pendientes, el B tiene 2 y el C ninguno. **Falta abrirla en Obsidian** para confirmar que los tableros se ven.
  - **Decisión de diseño:** los datos personales van solo en `_Contactos`. La ficha `CLI-xxxx` no los tiene. Así el asistente no lee esa carpeta (RQ-21), y borrar a un cliente (ESC-08) es borrar una nota. Con esto cambia un poco el modelo conceptual: los datos marcados con «*» pasan de la ficha a una nota aparte. Va en su v0.2.

## Afirmaciones (A31–A38)
Hoy no se trabajaron fuentes.

## Para bajar a mano
Nada.

## Dudas y decisiones para Víctor
1. **RQ-02:** ¿la alerta deja de llevar el teléfono y el correo? Es mi propuesta.
2. **RQ-24:** falta puntuarlo en la priorización (11.8) y sumarlo a la trazabilidad (OBJ-01).
3. **Catálogo de servicios (PEN-12):** el formulario web ya ofrece obra residencial, comercial, remodelación, mantenimiento, consultoría y proyecto especial. Propongo partir de esa lista para las plantillas; la gerencia la confirma en el taller. La actividad registrada en el SRI no limita los servicios que Torvesa puede dar, así que no se usa para esto.
4. **NEC-11 (seguimiento):** el MVP ya crea un evento en Google Calendar cuando se pone una fecha de seguimiento. Sirve como argumento para que entre en el taller.
5. **Revisión 1 (28-oct):** no hay acta en el repositorio. Para hacer el AS-IS v0.2 (bloque K) necesito las observaciones de la tutora.
6. **S3-T10 (documento de patrones de tu bóveda 1):** no tengo acceso a la bóveda 1. Pásame el documento por otro lado si quieres que lo lea.

7. **Casos de uso (para la elicitación v0.2):**
   - **CU-12 «Registrar evento verificable»:** propongo agregarlo, porque RQ-15 no tenía caso de uso.
   - **ESC-09 «Alta y baja de un vendedor»:** propongo agregarlo, porque CU-09 no tenía escenario.
   - **Colaborador:** propongo sumarlo como actor de CU-06.
8. **Numeración de los 6 pasos:**
   - `IA_DIEGO.md` dice que la parte 2 del TO-BE cubre «los pasos 3 y 4».
   - Con el orden del Cap. 2 v0.3 (captación, asignación, aviso, primer contacto, cotización, traspaso), la cotización y el traspaso son P5 y P6.
   - Propongo P1–P6 como en la plantilla.

9. **Bóveda, decisiones de costo y LOPDP:**
   - **Sincronización en el celular:** el plugin de Git es inestable en el móvil (A34). Obsidian Sync cuesta USD 4 por usuario al mes con pago anual (A32). Hay que elegir uno: cambia el Cap. 5 y RQ-14.
   - **`_Contactos`:** ¿va en una bóveda aparte? Obsidian no tiene permisos por usuario (A33).
10. **Orden de los bloques:** el bloque P (bóveda) se adelantó antes de que revises el TO-BE (S4-02). Si cambias algo de los flujos, ajusto la bóveda.

11. **Lo más urgente:** leer `00_Inbox/2026-11-02_aviso_sin_encuestas_ni_entrevistas.md`.
    - La directora de carrera dice que recoger datos de personas (encuestas, entrevistas y técnicas parecidas) lleva a otro proceso de autorización, más largo.
    - Recomiendo no hacerlo. El aviso trae qué se cae y cómo se reemplaza cada meta.

## Pendiente de Diego
- **Bloque K:** espera las observaciones de la tutora.
- **Campo:** sigue bloqueado; Torvesa no ha autorizado.
- **Lo siguiente:** bloque Q (domingo 8):
  - el resumen de 1 página de la bóveda (S4-T13);
  - la revisión del sprint 4.

  El análisis de la línea base depende de que haya campo.
