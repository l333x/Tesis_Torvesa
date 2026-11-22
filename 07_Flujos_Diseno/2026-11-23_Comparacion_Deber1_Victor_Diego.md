---
titulo: "Comparación del Deber 1 de IR: Víctor y Diego"
fecha: 2026-11-23
fuentes: "Deber1_Especificacion_Priorizacion_Segura_Victor (entregado) · Deber1_Especificacion_Priorizacion_Bermeo_Diego.pdf (22-nov, 20 páginas)"
tags: [deber, requerimientos, diego, comparacion]
---

# Comparación del Deber 1 (Víctor y Diego)

**En una línea:** el deber de Diego está bien hecho, usa los mismos 7 encuestados y le salen las mismas categorías de Kano. Tiene 4 errores para corregir, y él y Víctor priorizan distinto. Esa diferencia no es un error, porque cada informe es individual, pero la tesis necesita una sola versión.

## Lo que coincide
- Los 10 requerimientos son los mismos (registro, aviso, responsable, recordatorio, historial, borrador con IA, permiso, datos ante la IA, cuentas y sin señal).
- **Kano:** los mismos datos y las mismas categorías por persona. Resultado igual: 6 indiferentes, RF-01 y RF-03 de rendimiento, RF-04 de deleite y RF-06 básico, con los mismos 3 desempates. También coinciden la lectura de la confusión con "Lo espero" y las limitaciones (perfil de los encuestados y E5, E6 y E7 respondiendo en serie).
- **Los dos bajaron el borrador con IA y los datos ante la IA juntos** ("uno no sale sin el otro").

## Diferencias que hay que decidir (no son errores)
| Tema | Víctor | Diego | Qué conviene |
|---|---|---|---|
| Requisitos de la elicitación | 24 | 23 | La tesis (Tabla 5) tiene 24: RQ-24 es la hora del primer contacto. Diego tiene que confirmar y corregir |
| Formato de los ID | RF-01 | RF-001 | Da igual en el deber; en la tesis se usa RQ-xx |
| Esfuerzo total | 130 h (RF-06 30 h, RNF-04 24 h) | 108 h (RF-006 24 h, RNF-004 14 h) | Para la tesis hace falta una sola estimación: decidirla con Diego, que conoce mejor el código |
| Must (MoSCoW) | 4: RF-01, RF-02, RF-03, RNF-01 (30 h, 23 %) | 6: más RF-005 (historial) y RNF-003 (cuentas) (54 h, 50 %) | **El argumento de Diego es más sólido por las dependencias:** RF-003 necesita saber quién toma el pedido (RNF-003), y RF-006 necesita el historial (RF-005). La diapositiva 13 dice que no se deja un Must que dependa de algo de menor prioridad. Propuesta para la tesis: Must = RF-01, RF-02, RF-03, RNF-01 y RNF-03 (40 de 130 h, 30,8 %), y RF-05 queda Should porque RF-06 es Could [DECIDIR-VÍCTOR] |
| RF-06 (borrador con IA) | Could | Should | Coherente con lo anterior |
| RNF-04 (sin señal) | Won't | Could | Las dos son defendibles |
| Prioridad final | 4 alta, 5 media, 1 baja | 6 alta, 3 media, 1 baja | Sigue a la decisión de MoSCoW |
| Lista de 12 puntos | Plantilla de elicitación, sección 11.1 (ISO 29148 + SWEBOK) | Diapositivas 18 y 19 de "Validación, Verificación y Gestión" | **Son dos listas distintas.** Para el Deber 2 (verificación cruzada) los dos deben usar la misma. Pedirle a Diego esa presentación y confirmar cuál usó el profe |

## Errores del deber de Diego (para corregir si todavía puede)
1. **APA:** cita tres presentaciones como "Proaño Delgado, J. G. (2026)". Con el mismo autor y el mismo año van 2026a, 2026b y 2026c, en la lista y en el texto.
2. **Fechas viejas:** dice "la prueba en Torvesa (del 23 de noviembre al 5 de diciembre de 2026)". Ahora es "la validación del diseño, prevista desde el 30 de noviembre". Mejor no decir "prueba": el vocabulario de la tesis es "validación del diseño en operación experimental controlada".
3. **Códigos sin explicar:** usa OBJ-01 a OBJ-07, NEC-03 y CON-06 sin decir qué son. INT sí lo explica. Hay que agregar una nota como la de INT.
4. **Cantidad de requisitos:** dice 23; son 24.
5. **Detalles:**
   - iniciales sin el mismo formato ("M.M", "ER", "CR"; mejor "M. M.", "E. R.", "C. R.");
   - "Atencion" sin tilde;
   - mayúsculas en cargos ("Analista de Compras", "Director de Abastecimiento").
6. **Fecha de la encuesta:** dice que fue "el 22 de noviembre". El de Víctor no pone fecha. No es un error, pero si el profe compara, conviene que los dos digan lo mismo.

## Lo que Víctor podría tomar de Diego
- **Casos de excepción en los criterios:** formulario incompleto, aviso que falla y se reintenta, dos personas tomando el mismo pedido, cliente que no existe, sin cotizaciones anteriores. Es el punto 8 de su lista y mejora los criterios de aceptación de la tesis.
- **El aviso va "al equipo comercial" y no "al responsable":** cuando llega el pedido todavía no hay responsable. Aplica también a RQ-02 en la tesis.
