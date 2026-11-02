---
clase: portada
version: v0.1
fecha: 2026-11-02
autor: Diego Bermeo
ia: Claude (Claude Code)
tareas: [S4-T07, S4-T09, S4-T11]
estado: borrador para revisión de Víctor; sin validar con Torvesa
---

# Bóveda del sistema · v0.1

Esta es la **bóveda de conocimiento comercial** que propone el diseño: un conjunto de notas en Obsidian donde vive la ficha de cada cliente, sus solicitudes, sus cotizaciones y las plantillas. El asistente de IA lee esta bóveda para proponer borradores (RQ-11).

> [!warning] Todo lo que hay aquí es de ejemplo
> Los clientes, las solicitudes y las cotizaciones son **ficticios**: sirven para probar la estructura y los tableros. Ninguna nota tiene datos reales de Torvesa ni de sus clientes.

## Cómo abrirla
1. Instala Obsidian (gratis para uso comercial, A31).
2. **Abrir carpeta como bóveda** → elige `Boveda_Sistema`.
3. Para crear notas nuevas desde las plantillas: **Ajustes → Plugins principales → Plantillas** (actívalo) y, en sus opciones, pon `_Plantillas_de_notas` como carpeta de plantillas. Después: **Insertar plantilla** desde la paleta de comandos.
4. Los tableros (`.base`) usan **Bases**, que viene con Obsidian; no hace falta instalar plugins de la comunidad.

Los tableros filtran por la propiedad `clase` de cada nota, no por carpeta. Así funcionan igual si se abre solo `Boveda_Sistema` o la bóveda completa de la tesis.

## Tableros
- [[01_Tableros/Pendientes por vendedor.base|Pendientes por vendedor]]: lo que cada vendedor tiene abierto, agrupado por responsable. Incluye una vista **Sin primer contacto** (estado «Nueva»).
- [[01_Tableros/Clientes.base|Clientes]]: todas las fichas, con su responsable actual.
- [[01_Tableros/Cotizaciones.base|Cotizaciones]]: las enviadas y las que esperan respuesta.

## Carpetas

| Carpeta | Qué va | Quién la escribe | ¿La lee el asistente? |
|---|---|---|---|
| `01_Tableros` | Vistas de Bases | Diseño (fijo) | No |
| `02_Clientes` | Una ficha por cliente (`CLI-0001`), **sin datos personales** | Sistema (alta) y vendedores (notas) | Sí |
| `03_Solicitudes` | Una nota por solicitud (`SOL-0001`): estado, responsable, horas | Sistema | Sí |
| `04_Cotizaciones` | Cada cotización enviada (`COT-0001-v1`) con los documentos que usó el asistente y su huella | Quien cotiza y sistema (huella) | Sí |
| `05_Plantillas_cotizacion` | Una plantilla por tipo de obra | Quien cotiza (con la gerencia) | Sí |
| `06_Equipo` | Una nota por vendedor (rol, cuenta, activo) | Gerencia | No |
| `_Contactos` | Nombre, teléfono y correo de cada cliente (`CLI-0001_contacto`) | Sistema | **No, nunca** (RQ-21) |
| `_Plantillas_de_notas` | Plantillas para crear notas nuevas a mano | Diseño (fijo) | No |

## Reglas de diseño
1. **Los datos personales viven solo en `_Contactos`.** La ficha del cliente y todo lo demás usan el código `CLI-0001`. Así:
   - el asistente se configura para no leer esa carpeta, y al LLM no le llega ningún nombre, teléfono ni correo (RQ-21);
   - borrar los datos de un cliente (ESC-08, RQ-19) es borrar una sola nota, y el historial comercial y el registro verificable siguen sirviendo.
2. **La hora que cuenta para M1 la guarda el registro de solicitudes** (TEAMSLASH, PostgreSQL), no la bóveda. En la prueba de concepto, el sistema crea y actualiza las notas de `03_Solicitudes` como copia para que el equipo vea sus pendientes en Obsidian. Aquí están escritas a mano como ejemplo.
3. **Nada se borra del historial:** una cotización corregida es una nota nueva (`-v2`), y la anterior se queda.
4. **Propiedades con los nombres del modelo conceptual** (`07_Flujos_Diseno/2026-10-31_Modelo_Conceptual_v0.1`). Estados: Nueva, En contacto, Cotizada, Ganada, Perdida (RQ-05).

## Lo que falta decidir (Víctor y la gerencia)
- **Cómo se sincroniza en el celular.** El plugin de Git es «very unstable» en el móvil, según su propio autor (vinzent03_sf, A34). La alternativa oficial es Obsidian Sync, a USD 4 por usuario al mes con pago anual (obsidian_sfa, A32). Afecta el costo (Cap. 5) y RQ-14.
- **Permisos.** Obsidian no tiene permisos por usuario dentro de una bóveda compartida (obsidian_sfb, A33): todos los que la tienen ven todo. Por eso `_Contactos` podría ir en una bóveda aparte, solo para quien atiende. Se decide con la gerencia.
- **El catálogo real de tipos de obra** para las plantillas (PEN-12). Las dos plantillas de ejemplo salen de los tipos que ya ofrece el formulario web.
- **La lista cerrada de motivos de pérdida** (PEN-07). La de las plantillas es una propuesta.
