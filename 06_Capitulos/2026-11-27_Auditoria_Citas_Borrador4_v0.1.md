---
tipo: auditoria
tarea: H-01 (adelantada)
fecha: 2026-11-27
version: v0.1
autor: Claude (IA), para revisión de Victor
documento_auditado: 06_Capitulos/2026-11-23_Tesis_Borrador4_v0.3.docx
capitulos_fuente:
  - 2026-11-22_Cap1_Introduccion_p1_v0.6.md
  - 2026-11-22_Cap1_Introduccion_p2_v0.6.md
  - 2026-11-22_Cap2_Marco_Teorico_v0.5.md
  - 2026-11-22_Cap3_Metodologia_v0.6.md
  - 2026-11-23_Cap4_Desarrollo_Tecnico_v0.7.md
  - 2026-11-23_Cap5_Cap6_v0.6.md
---

# Auditoría de citas del borrador 4 v0.3 (v0.1)

**Qué se hizo.** Se extrajeron con un script todas las citas del cuerpo del Word ensamblado (capítulos I a VI y tablas) y de los seis `.md` fuente; las dos fuentes coinciden. Se cruzaron con la lista «Referencias bibliográficas» del Word (80 entradas) y con las fichas de `02_Fuentes/` (campo `estado`, `acceso`, `pagina`, cita textual y notas de verificación). En los casos dudosos se abrió el PDF local de `_Textos/` (LOPDP, OCDE 2025b) o el informe TEAMSLASH de `10_Antecedentes_Propios/`. No se buscó nada en la web. No se tocó ningún capítulo ni ficha.

**Regla aplicada (MANUAL_TESIS §3.2 y §11).** «Verificada» = ficha con `estado: verificada`, fuente abierta, dato y página. Las fichas `candidata` o `acceso: solo_resumen`/`pago` sin abrir **no** se citan.

## Resumen en números

| Indicador | Valor |
|---|---|
| Apariciones de cita en el cuerpo (conteo automático, ±3) | **≈179** |
| Obras distintas citadas en el cuerpo (incluidas las que solo están dentro de marcadores) | **90** |
| … con ficha **verificada** | **75** |
| … con ficha **no verificada** (candidata / solo resumen / de pago sin abrir) | **5**: Oldroyd 2011, Ohiomah 2019, Habel 2025, Rodriguez y Boyer 2020, Auernhammer y Roth 2021 |
| … **sin ficha** | **10**: Kano 1984, Agile Business Consortium s. f., Bermeo y Segura 2026 (obra propia), Nonaka y Takeuchi 1995, Walsh y Ungson 1991, Pollitt 2000, Haber y Stornetta 1991, Peffers 2007, Creswell y Plano Clark 2018, Hernández-Sampieri y Mendoza 2018 |
| Citas **activas** (fuera de un marcador) de obras no verificadas o sin ficha | **9 obras**: Oldroyd, Ohiomah, Habel, Rodriguez y Boyer, Nonaka y Takeuchi, Walsh y Ungson, Kano, Agile Business Consortium, Bermeo y Segura |
| Entradas de la lista de referencias | 80 (79 citadas; 1 sin cita) |
| Citas en el texto que no están en la lista | 11 obras (ver §2) |
| Contradicciones o desajustes cifra/página frente a la ficha | **6 de fondo** + 7 menores (ver §4) |
| Marcadores en el cuerpo del Word | 21 FALTA-FUENTE · 3 VERIFICAR-PÁG · 56 FALTA-DATO · 11 DECIDIR-TUTORA · 7 DECIDIR-VÍCTOR |

Ninguna ficha verificada tiene todavía el visto bueno humano: todas dicen «falta visto bueno de Víctor» (o «de Diego» en las que verificó la IA de Diego: Magesh, Béchard, OMG, Martínez Mendoza, Radhakrishnan, Nizioł, Zambrano Loor, Kommo, Anthropic). Cuentan como verificadas según el manual, pero conviene que la revisión humana empiece por las de §4.

---

## 1. Tabla de citas en el texto

Leyenda. **Estado:** V = verificada · NV = candidata / solo resumen / de pago sin abrir · SF = sin ficha. **¿Coincide?:** «sí» = el dato y la página del borrador están en la ficha; «sí*» = el dato está, con un matiz anotado; «NO» = desajuste (detalle en §4). **(m)** = la cita solo aparece dentro de un marcador `[FALTA-FUENTE]`.

### Capítulo I (partes 1 y 2)

| Autor (año) | Cap. | Afirmación que respalda | Ficha | Estado | ¿Coincide? |
|---|---|---|---|---|---|
| Singla et al. (2025) | I | 78 % de organizaciones usa IA (55 % un año antes), 71 % IA generativa (pp. 14 y 16) — CTX-IA | mckinsey_2025 | V | sí |
| OECD (2025a) | I, II | Empresas con IA: 5,6 % → 14 %; pequeñas 11,9 % frente a grandes 40 % (p. 6) — CTX-IA, A28 | oecd_2025a | V | sí |
| McKinsey & Company (2026) | I | 54 % de las organizaciones con ≥ USD 1.000 M escala la IA, frente a un tercio de las más pequeñas (sección «Key takeaways») | mckinsey_2026 | V | sí (la ficha pide el tamaño de muestra si se usa como dato principal) |
| OECD (2025b) | I | 31 % de las pymes de siete países usa IA generativa (p. 6) | oecd_2025b | V | sí («siete países» comprobado en el PDF, pp. 5 y 10 del PDF) |
| Salesforce Research (2024) | I, II | Los vendedores dedican el 30 % de la semana a vender; cotizar es automatizable (p. 13) — A4 | salesforce_2024 | V | sí |
| Manyika et al. (2015) | I, II | Construcción en el puesto 21 de 22 del índice MGI (p. 5) — A5 | manyika_2015 | V | sí (anterior a 2021; va con Cathles 2023, cumple §11.1) |
| Cathles et al. (2023) | I, II | 68 % de las micro y pequeñas constructoras chilenas en etapas iniciales de digitalización (p. 5) — A5 | cathles_2023 | V | sí |
| Samuelson y Stehn (2023) | I, II | Lógica B2B y organización fragmentada frenan la digitalización (p. 400); el conocimiento se transfiere mal entre proyectos (p. 388) — A6 | samuelson_2023 | V | sí (la p. 388 está en «Cómo se usa», no en el campo `pagina`) |
| McKinsey & Company (2023) | I | USD 50.000 M invertidos en 2020–2022, 85 % más; fragmentación y bajo gasto en TI — A5, A6 | mckinsey_2023 | V | sí* (la ficha ubica el dato en «Exhibit 1»: el `[VERIFICAR-PÁG]` se puede resolver citando la figura) |
| Banco Central del Ecuador (2026a) | I, IV | Construcción −1,7 % (2023), −7,9 % (2024), +2,7 % (2025) (pp. 22–23); 4,1 % del PIB (p. 22); 6,4 % del empleo (p. 45) — CTX-EC | bce_2026 | V | sí |
| Redacción Empresas (2024) | I | 36 % de trabajadores usa IA (Multitrabajos) — CTX-EC | multitrabajos_2024 | V | sí (confianza media: encuesta sin método publicado) |
| CEPAL (2025) | I | Ecuador en la categoría «adoptante» del ILIA 2025 — CTX-IA | cepal_2025 | V | sí* (se leyó el comunicado en inglés; el informe ILIA completo sigue pendiente) |
| Pérez-Campdesuñer et al. (2025) | I, II, IV | IA poco usada en mipymes; barreras: profesionales y bases de datos; 385 mipymes — A28, A29, A8 | perezcampdesuner_2025 | V | sí (citado por «resumen», MDPI sin páginas) |
| Servicio de Rentas Internas (2026) | I, IV | Torvesa: sociedad activa desde 5-ago-2010, régimen general, actividad F4210 (carreteras) | sri_2026 | V | sí |
| Superintendencia de Compañías, Valores y Seguros (2026b) | I, IV | Torvesa no figura como compañía | scvs_2026b | V | sí |
| Stark (2024) | I, II | Amnesia institucional (p. 3); depósitos formales de memoria (p. 4) — A8 | stark_2024 | V | sí |
| Pollitt (2000) | I, II (m) | Origen del término «amnesia institucional» — A8 | — | SF | — |
| **Oldroyd et al. (2011)** | **I (cita activa)**, II (m) | Responder en la primera hora: ~7 veces más probabilidad de calificar — A9 | oldroyd_2011 | **NV (candidata, solo resumen)** | **NO verificable**: está citada en el Cap. I y en la lista de referencias |
| Koushik (2024) | I | 635 de 1.000 empresas B2B de software no respondieron — A9, A10 | revenuehero_2024 | V | sí (proveedor de software: confianza media) |
| Salesforce Research (2022) | I, II | 83 % espera hablar con alguien de inmediato (p. 16) — A10 | salesforce_2022 | V | sí |
| LOPDP (2021) / Asamblea Nacional | I, II, III, IV | Consentimiento (art. 8), conservación (art. 10, lit. i), información (art. 12), encargado (art. 34, pp. 33–34), evaluación de impacto (art. 42, p. 38), delegado (art. 48, p. 42) — A42, A45 | lopdp_2021 | V | sí* (arts. 7, 8, 10 y 12 están en la ficha; los arts. 34, 42 y 48 **no** están en la ficha. En el PDF se comprobó que el art. 34 empieza en la p. 33 y el art. 48 está en la p. 42; el art. 42 no se pudo ubicar por el OCR) |
| **Ohiomah et al. (2019)** | **I (cita activa)**, II (m) | CRM y gestión de prospectos en empresas grandes — A21 | ohiomah_2019 | **NV (candidata, de pago)** | — |
| **Rodriguez y Boyer (2020)** | **I (cita activa)**, II (m ×2) | CRM móvil, autorreporte — A24, A26 | rodriguez_2020 | **NV (candidata, solo resumen)** | — |
| **Habel et al. (2025)** | **I (cita activa)**, II (m) | Automatización del seguimiento — A22 | habel_2025 | **NV (candidata, de pago)** | — |
| Brehme et al. (2025) | I, II, V | 12 de 13 participantes calificaron sus casos por debajo de TRL 7 (p. 10) — A37, A29 | brehme_2025 | V | sí* en Cap. II y V; **Cap. I dice «12 de 13 casos estudiados»**: la fuente habla de participantes (§4) |
| Peña-Ramírez et al. (2024) | I, II | Inteligencia de negocios en compras públicas de pymes constructoras chilenas — A28 | penaramirez_2024 | V | sí |
| Bakiyalakshmi et al. (2026) | I, II | RAG para redactar propuestas en empresas — A29 | bakiyalakshmi_2026 | V | sí |
| **Nonaka y Takeuchi (1995)** | **I (cita activa)**, II (m) | Gestión del conocimiento (SECI) | — | **SF** | — |
| **Walsh y Ungson (1991)** | **I (cita activa)**, II (m) | Memoria organizacional | — | **SF** | — |
| Obsidian (2025) | I | Obsidian es gratuito para uso comercial — A31 | obsidian_2025 | V | sí (la ficha pide reconsultar antes de la versión final) |
| Vinzent03 (s. f.) | I | El complemento de Git es muy inestable en el móvil — A34 | vinzent03_sf | V | sí |
| Anthropic (s. f.) | I | USD 2 / USD 10 por millón de *tokens* (gama media) — A36 | anthropic_sf | V | sí (Sonnet 5.5; precio cambiante, reconsultar antes del cierre) |
| Hyzy et al. (2022) | I, II | SUS: media 68 (DE 12,5), 446 estudios y 5.000 respuestas (p. 2); 114 aplicaciones (p. 1) — A20 | hyzy_2022 | V | sí |
| Sevilla-Gonzalez et al. (2020) | I, II, III, V | Versión en español validada de la SUS (México, salud) — A20 | sevillagonzalez_2020 | V | sí |
| Obsidian (s. f.) | I, IV | Sin permisos por usuario en una bóveda compartida — A33 | obsidian_sfb | V | sí |

### Capítulo II

| Autor (año) | Cap. | Afirmación que respalda | Ficha | Estado | ¿Coincide? |
|---|---|---|---|---|---|
| Chatterjee et al. (2023) | II (×5) | CRM con IA: 315 usuarios en India; calidad y satisfacción influyen, compatibilidad pesa poco (p. 1299) — A26 | chatterjee_2023a | V | sí |
| Wu et al. (2024) | II (×2) | Revisión de 44 estudios; enfoque tradicional y predictivo (p. 69) — A27 | wu_2023 | V | sí (el citekey dice 2023; el año correcto es 2024) |
| AlQershi et al. (2020) | II | 284 pymes de Yemen; efectos por dimensión del CRM (pp. 9–12) — A23 | alqershi_2020 | V | sí (ya corregido según la ficha). Anterior a 2021 y sin fuente reciente que la acompañe (§11.1) |
| Gil-Gomez et al. (2020) | II | CRM como herramienta para innovar el modelo de negocio (p. 2733), no comprobado (p. 2745) — A25 | gilgomez_2020 | V | sí. Anterior a 2021, sin fuente reciente que la acompañe |
| Rodriguez et al. (2025) | II (×5) | IA generativa en ventas: β = 0,487, 0,484 y 0,274 (p. 20); libera tiempo (p. 14); 163 vendedores de una empresa de salud — A26, A28 | rodriguez_2025 | V | **NO en la página**: p. 20 y p. 14 son del manuscrito aceptado; la referencia es la versión publicada (pp. 2013–2027) (§4) |
| Gartner (2025) | II | Para 2028, diez veces más agentes que vendedores; < 40 % verá mejora — CTX-IA | gartner_2025 | V | sí (se presenta como predicción) |
| Gartner (2026) | II | 67 % de compradores B2B prefiere no hablar con un vendedor — CTX-IA | gartner_2026 | V | sí |
| Hernández Vega et al. (2026) | II (×2) | IA incipiente en pymes de América Latina; barreras (p. 1080) — A28 | hernandezvega_2026 | V | sí |
| Bermeo y Segura (2026) | II, III, IV (×9) | TEAMSLASH: formulario, API, Slack (p. 5); canales del cliente (p. 4); delegación informal (p. 7); censo (p. 10); tasa de 15 % (p. 28) | — | **SF** (obra propia; PDF en `10_Antecedentes_Propios/2026-07-22_Informe_Final.pdf`) | sí* (por palabras clave, las páginas 4, 5, 7, 10 y 28 del PDF contienen los temas citados; no se leyó completo) |
| Böhm y Durst (2026) | II (×5) | SECI (pp. 107–108); externalización y límites de la IA generativa (p. 110) — A8 | bohm_2026 | V | sí |
| Lewis et al. (2020) | II | RAG: definición (p. 9459) y menos invenciones (p. 9464) — A37 | lewis_2020 | V | sí (origen del término, va con Brehme 2025) |
| Béchard y Marquez Ayala (2024) | II | Invenciones de hasta 21 % a menos de 7,5 % (p. 233) — A37 | bechard_2024 | V | sí |
| Magesh et al. (2025) | II | Herramientas jurídicas con RAG se equivocan entre 17 % y 33 % (p. 216) — A37 | magesh_2025 | V | sí* (el dato está en el resumen, p. 216, como dicen las notas; el campo `pagina` de la ficha dice 217) |
| Kleppmann et al. (2019) | II | *Local-first*: datos en el dispositivo, sin conexión (p. 157) — A38 | kleppmann_2019 | V | sí. Anterior a 2021 y sin fuente reciente que la acompañe |
| Object Management Group (2013) | II, III, IV | BPMN entendible por negocio y técnicos (p. 1); carriles (pp. 25–26) — CTX-PROC | omg_2013 | V | sí |
| Martínez Mendoza et al. (2023) | II, IV | Procesos sin registros de operación (p. 4836) — CTX-PROC | mendoza_2024b | V | sí (citekey con año y apellido distintos; la ficha propone renombrarla) |
| Radhakrishnan (2025) | II | Del proceso actual al mejorado con IA y BPMN — CTX-PROC | radhakrishnan_2025 | V | sí (sin página; verificado en la versión del autor) |
| NIST (2015) | II, III | Cualquier cambio produce otra huella (p. iv) — A30, A35 | nist_2015 | V | sí |
| Haber y Stornetta (1991) | II (m) | Encadenamiento de registros | — | SF | — |
| Decreto Ejecutivo 904 (2023) / Presidencia de la República | II, III, IV | Existencia del Reglamento General de la LOPDP — A43 | reglamento_lopdp_2023 | V | sí (solo se cita su existencia) |
| Ley de Comercio Electrónico (2002) | II | Mensajes de datos con valor jurídico (art. 2); art. 9 derogado — A44 | lce_2002 | V | sí |
| Revelo (2026) | II, IV | 70 % sin regulación interna de IA; 33 % usa cuentas personales — A46, A42 | primicias_2026 | V | sí (la nota se contradice entre subtítulo y cuerpo; el borrador usa el cuerpo, como pide la ficha) |

### Capítulo III

| Autor (año) | Cap. | Afirmación que respalda | Ficha | Estado | ¿Coincide? |
|---|---|---|---|---|---|
| Dawadi et al. (2021) | III | Prioridad cuantitativa en un diseño mixto (p. 28) — A39 | dawadi_2021 | V | sí |
| Creswell y Plano Clark (2018) | III (m) | Texto base del método mixto | — | SF | — |
| Hernández-Sampieri y Mendoza (2018) | III (m ×2) | Método mixto; censo en poblaciones pequeñas — A40 | — | SF | — |
| Tuunanen et al. (2024) | III (×2) | Definición de DSR; dividir el proyecto en partes — A39 | tuunanen_2024 | V | sí* (sin página: la ficha leyó la versión autoarchivada; `[VERIFICAR-PÁG]` vigente) |
| Peffers et al. (2007) | III (m) | Las seis actividades de la DSR | — | SF | — |
| Cuadrado Torres (2023) | III (×2) | *Design Thinking* centrado en las personas (p. 44); caso de Manta — A47 | torres_2023 | V | sí* (volumen 38 en el PDF frente a 39 en el DOI, sin resolver) |
| Auernhammer y Roth (2021) | III (m) | Texto base de *Design Thinking* | auernhammer_2021 | NV (candidata, ficha vacía) | — |
| Schwaber y Sutherland (2020) | III (×2) | Scrum (p. 3); *sprints* de un mes o menos (p. 7) — A47 | schwaber_2020 | V | sí |
| Sassa et al. (2023) | III | Scrum flexible, también fuera del software (p. 173) — A47 | sassa_2023 | V | sí |

### Capítulo IV

| Autor (año) | Cap. | Afirmación que respalda | Ficha | Estado | ¿Coincide? |
|---|---|---|---|---|---|
| Nizioł et al. (2021) | IV | Los carriles BPMN muestran mejor quién hace cada paso (p. 199) — CTX-PROC | nizio_2021 | V | sí |
| Zambrano Loor y García Vera (2025) | IV | Levantar procesos con documentos y contrastarlos (p. 79) — CTX-PROC | loor_2025 | V | sí |
| Tapia (2024) | IV | Cortes de hasta 12 horas en 2024 | tapia_2024 | V | sí |
| Redacción Primicias (2025) | IV | Pérdidas de USD 1.916 M por los apagones | primicias_2025a | V | sí (solo se usa para las pérdidas, como pide la ficha) |
| Kemp (2026) | IV | 83,9 % de la población usa internet a finales de 2025 | datareportal_2026 | V | sí |
| SCVS (2026a) | IV (×3) | Constructoras pequeñas F41 de Pichincha: 273/306/321; mediana de 4 empleados; margen neto mediano 1,4/1,7/1,9 %; ventas medianas USD 320.229 | scvs_2026a | V | sí (cálculo propio sobre el ranking, documentado en la ficha) |
| **Kano et al. (1984)** | IV | Modelo de Kano para priorizar requisitos | — | **SF** | — (además depende de la DEC-25) |
| **Agile Business Consortium (s. f.)** | IV | Recomienda que lo imprescindible no pase del **60 %** del esfuerzo | — | **SF** | **cifra sin verificar** |
| Amazon Web Services (s. f.-a) | IV | Servir un modelo ajustado cuesta USD 23,50 por hora | aws_sfb | V | sí (la ficha usa la letra «b»; en la lista es «a», lo que está bien por orden de título) |
| AWS (s. f.-b) | IV | AWS recomienda empezar por RAG | aws_sfd | V | sí |
| Kommo (s. f.) | IV | USD 16,67 por usuario al mes con pago anual | kommo_sf | V | sí (precio de la página en español; varía por región) |
| Leadsales (s. f.) | IV | Plan avanzado, cinco usuarios: USD 247 al mes | leadsales_sf | V | sí |
| IFRS Interpretations Committee (2021) | IV | La mensualidad de un SaaS es gasto, no activo | ifric_2021 | V | sí* (la decisión es de las NIIF completas; la NIIF para las PYMES no se verificó, §4) |
| Ekos Negocios (2025) | IV | Salario pretendido semi-senior en tecnología: USD 1.084 | ekos_2025 | V | sí (es salario pretendido, no pagado) |
| IESS (2014) | IV | Aporte patronal 11,15 % (p. 1) | iess_2014 | V | sí en la cifra; **NO en la frase de la conclusión** (§4). PDF de 2014: la ficha remite a Farfán (2025) para 2026, que no se cita |
| González (2026b) | IV | 1 % adicional (SECAP 0,5 % + IECE 0,5 %) | gonzalez_2026b | V | sí* («un punto para la capacitación»: la fuente dice «temas educativos», §4) |
| Código del Trabajo (2005) | IV | Décimos, vacaciones y fondos de reserva | ct_2005 | V | sí |
| Servicio de Rentas Internas (2021) | IV | El IVA de servicios digitales se causa al pagar (p. 1) | sri_2021 | V | sí (el 15 % sigue sin fuente, ya marcado) |
| Damodaran (2026) | IV (×2) | Prima de riesgo de las acciones de Ecuador: 17,18 % | damodaran_2026 | V | sí en la cifra; **uso inconsistente** (§4) |
| Damodaran (2026b) | IV | Márgenes de constructoras de mercados emergentes | damodaran_2026b | V | sí |
| Banco Central del Ecuador (2026b) | IV | Tasa activa máxima pymes: 9,87 % | bce_2026b | V | sí |
| Amaya et al. (2026) | IV | 9,09 % de adultos cerró un negocio; 27,71 % por no ser rentable (pp. 24 y 26) | amaya_2026 | V | sí* (la fuente se contradice: el texto de la p. 25 da 24,07 %; la ficha pide anotarlo y el borrador no lo hace) |
| U.S. Bureau of Labor Statistics (2026) | IV | 79,1 % sobrevive al año 1 y 47,2 % al año 5 | bls_2026 | V | sí |
| CB Insights (2026) | IV | 70 % sin capital, 43 % sin encaje producto-mercado | cbinsights_2026 | V | sí |

### Capítulos V y VI
Solo citan Sevilla-Gonzalez et al. (2020) y Brehme et al. (2025, p. 10), ya listadas arriba. Cap. V trae un `[FALTA-FUENTE]` sin autor (heurísticas de usabilidad) y el Cap. III uno sobre ISO/IEC 25010 e ISO 9001.

---

## 2. Cruce entre citas y lista de referencias

### 2.1 Citas en el texto que no están en la lista (11)

| Obra | Dónde | Tipo |
|---|---|---|
| Ohiomah et al. (2019) | Cap. I p2 (cita activa entre paréntesis); Cap. II (m) | **Cita activa sin referencia** |
| Rodriguez y Boyer (2020) | Cap. I p2 (activa); Cap. II (m ×2) | **Cita activa sin referencia** |
| Habel et al. (2025) | Cap. I p2 (activa); Cap. II (m) | **Cita activa sin referencia** |
| Nonaka y Takeuchi (1995) | Cap. I p2 (activa); Cap. II (m) | **Cita activa sin referencia** |
| Walsh y Ungson (1991) | Cap. I p2 (activa); Cap. II (m) | **Cita activa sin referencia** |
| Pollitt (2000) | Cap. I, II (m) | Solo en marcador |
| Haber y Stornetta (1991) | Cap. II (m) | Solo en marcador |
| Peffers et al. (2007) | Cap. III (m) | Solo en marcador |
| Creswell y Plano Clark (2018) | Cap. III (m) | Solo en marcador |
| Hernández-Sampieri y Mendoza (2018) | Cap. III (m ×2) | Solo en marcador |
| Auernhammer y Roth (2021) | Cap. III (m) | Solo en marcador |

La lista de «Sin verificar todavía» al final del Cap. I p2 ya avisa de las cinco primeras, pero en el párrafo de justificación (Cap. I p2, línea 21 del `.md`) están escritas como citas normales y el lector las verá así.

**Claves que no coinciden con su referencia** (están en la lista, pero con otro primer elemento):
- «(LOPDP, 2021, …)» → la referencia empieza por «Asamblea Nacional del Ecuador». El lector buscará en la L y no la encontrará.
- «(Decreto Ejecutivo 904, 2023)» → la referencia empieza por «Presidencia de la República del Ecuador».
- «(Damodaran, 2026)» → hay dos obras de Damodaran del mismo año: debe ser 2026a.
- «(González, 2026b)» → en la lista no hay un González 2026a: debe ser 2026 a secas (o citar también gonzalez_2026).
- En el `.md` del Cap. I la referencia del BCE figura como «(2026)»; en el Word ya es «2026a». Bien en el Word.

### 2.2 Referencias que no se citan (1)

- **Ministerio del Trabajo (2026)**: está en la lista, pero no aparece en el texto (salario básico de USD 482, ficha ministerio_2026 verificada). Se cita donde se use el salario básico (¿décimo cuarto en el Cap. IV?) o se quita.

---

## 3. Formato APA 7 de la lista (Word v0.3)

**Lo que está bien:** «y» en todas las referencias (las fichas usan «&», la lista lo convierte bien); DOI como `https://doi.org/`; orden alfabético correcto letra por letra (Agile → Zambrano); revistas y volúmenes en cursiva; sin «Recuperado de» ni «doi:».

**Errores por corregir:**

1. **a/b del mismo autor y año**
   - Damodaran: «(2026)» y «(2026b)» → «(2026a)» y «(2026b)» (por título: *Country…* antes que *Margins…*), en la lista y en las dos citas del texto.
   - González: «(2026b, 22 de abril)» sin un 2026a en la lista → «(2026, 22 de abril)».
2. **Orden de obras del mismo autor:** Obsidian (s. f.) debe ir **antes** que Obsidian (2025, 20 de febrero); en APA 7 las obras sin fecha van primero.
3. **Referencias con marcadores dentro** (no pueden quedar en la versión final):
   - Oldroyd et al. (2011): «[FALTA-FUENTE: páginas…]»;
   - Bermeo y Segura (2026): «[FALTA-DATO…]». Formato sugerido para obra no publicada: `*Título* [Informe final del proyecto integrador no publicado]. Universidad Politécnica Salesiana.`
4. **Falta la URL** en:
   - Asamblea Nacional (LOPDP), Presidencia (Reglamento) y Ley de Comercio Electrónico (las fichas tienen el PDF de FAOLEX, de la Corte Constitucional y de ARCOTEL);
   - Gartner (2025) y Gartner (2026);
   - Revelo (2026);
   - Lewis et al. (2020): falta el enlace a las actas de NeurIPS.
5. **Las cuatro normas tienen formatos distintos:**
   - LOPDP y Reglamento: autor institucional y título en cursiva;
   - Ley de Comercio Electrónico: título en lugar del autor, en redonda;
   - Código del Trabajo: sin fecha entre paréntesis («Código del Trabajo. Codificación n.º 2005-017. Registro Oficial…»).

   Hay que elegir uno (el del manual §6.2, adaptado de la UTPL) y hacer que la cita del texto coincida con el primer elemento (ver §2.1).
6. **Noticias de *Primicias* con dos formatos.** Según el manual (medio solo digital: título en cursiva y medio en redonda):
   - Redacción Empresas (2024) y Revelo (2026) siguen la regla;
   - Redacción Primicias (2025), Tapia (2024) y González (2026b) ponen el título en redonda y *Primicias* en cursiva.

   Hay que unificarlas.
7. **González (2026b):** el título va entre corchetes porque «no se vio». APA usa corchetes solo cuando la obra no tiene título. Hay que abrir la nota y copiar el título real.
8. **Peña-Ramírez et al. (2024):** «*32*, 39.» → «*32*, Artículo 39.», como en las otras revistas con número de artículo.
9. **Tuunanen et al. (2024):** faltan las páginas del volumen 48(2). Hay que confirmarlas en AIS eLibrary, como pide la ficha. No se inventan.
10. **Nizioł et al. (2021):** faltan los editores del volumen de las actas (lo advierte la ficha).
11. **Cuadrado Torres (2023):** dice «*23*(38)», pero el DOI dice «v23i39». Hay que confirmar el número en la web de la revista.
12. **CEPAL (2025):** el título está en español, pero la URL es la del comunicado en inglés, que fue el que se leyó. Hay que usar la URL en español o el título en inglés.
13. **Gartner (2025):** el título de la ficha dice «10X—yet fewer…» y la lista lo cambió a «10X, yet fewer…». El título se copia tal como está.
14. **«Recuperado el … de» con dos puntuaciones:**
    - sin coma en Anthropic, Obsidian ×2 y Vinzent03;
    - con coma («…, de https») en AWS, BCE 2026b, Kommo, Leadsales, SRI 2026 y las dos SCVS.

    Hay que unificar.
15. **Kano et al. (1984):** el artículo original está en japonés, en la revista *Hinshitsu*. En APA, el título traducido va entre corchetes. Se comprueba al crear la ficha; hoy no hay ficha.
16. **Siglas repetidas en el texto** (APA define la sigla una vez):
    - [BCE] se define en el Cap. I, pero el Cap. IV vuelve a escribir «Banco Central del Ecuador, 2026a»;
    - [SRI] se define tres veces y [NIST] dos.
17. **Detalle de forma:** «(Radhakrishnan, 2025) .», con un espacio antes del punto (Cap. II).

---

## 4. Contradicciones entre el borrador y las fichas

Dicho sin maquillaje. Primero las seis de fondo:

1. **Oldroyd et al. (2011): «siete veces» sin verificar.**
   - El Cap. I la cita como una fuente normal: «(Oldroyd et al., 2011 [FALTA-FUENTE…])». También está en la lista de referencias.
   - La ficha es `candidata`, con `acceso: solo_resumen`: nadie abrió el artículo.
   - Por la regla del manual, **hoy no se puede citar**.
2. **Rodriguez et al. (2025): las páginas no existen en la versión citada.**
   - El borrador cita «p. 20» (las β) y «p. 14» (el tiempo liberado).
   - Son páginas del manuscrito aceptado de K-REx. La referencia es la versión publicada, de las pp. 2013–2027, así que «p. 20» no puede estar en ella.
   - La ficha ya lo advertía: «citar la sección o confirmar la página en Emerald».
3. **Aporte patronal: «12,15 % y no 11,15 %» contradice al IESS.**
   - El Cap. IV («Qué cambió…») dice que «el aporte patronal es de 12,15 % y no de 11,15 %».
   - La fuente (IESS, 2014, p. 1) dice que el aporte patronal **es** 11,15 %. El 12,15 % es una suma propia que agrega el 1 % para el SECAP y el IECE (González, 2026b), y la ficha lo aclara: «la suma 12,15 % es nuestra».
   - Además, ese 1 % no es todo «para la capacitación»: la fuente dice 0,5 % SECAP + 0,5 % IECE, «temas educativos».
   - Redacción correcta: «el costo patronal total es de 12,15 %: 11,15 % de aporte al IESS más 1 % para el SECAP y el IECE».
4. **Tasa de descuento: el argumento se contradice.**
   - El borrador dice que el 12 % «era baja», porque «la sola prima de riesgo de las acciones de Ecuador es de 17,18 %» (Damodaran, 2026), y por eso la base «pasó a 15 %». Pero el 15 % sigue por debajo de ese 17,18 %.
   - Además, el 17,18 % es una prima, no una tasa: le falta la tasa libre de riesgo (el propio borrador lo marca con `[FALTA-FUENTE]`).
   - El 15 % se sostiene en el proyecto integrador (Bermeo y Segura, 2026, p. 28), no en Damodaran. Hay que decirlo así o rehacer el razonamiento con la tutora.
5. **Brehme et al. (2025): «casos» en lugar de «participantes».**
   - El Cap. I dice: «12 de 13 casos estudiados no habían llegado a un uso a gran escala».
   - La fuente (p. 10) dice: «12 out of 13 participants rated their use cases below TRL 7». Son las calificaciones de 13 entrevistados, no 13 casos observados.
   - El Cap. II lo dice bien («13 profesionales»): hay que copiar esa redacción en el I.
6. **Agile Business Consortium (s. f.): la cifra del 60 % no tiene fuente verificada.**
   - El Cap. IV la usa para decir que el 81,5 % del esfuerzo estaba «muy por encima del 60 % que recomienda». No hay ficha.
   - Kano et al. (1984), en el mismo párrafo, tampoco tiene ficha.

Las siete menores:

7. **Amaya et al. (2026):** el borrador usa el 27,71 % de la tabla 6. La ficha avisa de que el texto de la p. 25 del mismo informe da 24,07 % y pide anotar la diferencia; el borrador no la anota.
8. **IFRS Interpretations Committee (2021):** el borrador afirma que «para Torvesa, la mensualidad es gasto de operación». La decisión es para las NIIF completas (NIC 38). La ficha dice que la NIIF para las PYMES **no se verificó**, y Torvesa probablemente aplica esa. Se puede matizar («según el criterio de las NIIF…») o verificar.
9. **Magesh et al. (2025):** el borrador cita p. 216 y la ficha, en `pagina`, dice 217. Por las notas de la misma ficha, la cifra de 17 % a 33 % está en el resumen (p. 216): el borrador está bien y lo que hay que corregir es la ficha.
10. **LOPDP, arts. 34, 42 y 48:** las páginas del Cap. IV no están en la ficha. En el PDF se confirmaron el art. 34 (empieza en la p. 33) y el art. 48 (p. 42); el art. 42 (p. 38) no se pudo ubicar por el OCR. Hay que agregarlos a la ficha mirando la página.
11. **Cuadrado Torres (2023):** el volumen y el número no coinciden (38 frente a 39); está sin resolver desde el 18-oct.
12. **Tuunanen et al. (2024) y McKinsey & Company (2023):** siguen con `[VERIFICAR-PÁG]`. El de McKinsey se resuelve con lo que ya dice la ficha («Exhibit 1»).
13. **Fuentes anteriores a 2021 que van solas** (§11.1 del manual):
    - AlQershi (2020), Gil-Gomez (2020) y Kleppmann (2019);
    - IESS (2014), para una tasa de 2026: la ficha propone apoyarla en Farfán (2025), que no se cita.

---

## 5. Prioridad de arreglo antes del 4-ene-2027

### 5.1 Quitar o marcar `[FALTA-FUENTE]` (urgente: son citas activas de fuentes no verificadas)

| # | Dónde | Acción |
|---|---|---|
| 1 | Cap. I p1, párrafo de *speed-to-lead* | Quitar «(Oldroyd et al., 2011)» de la cita y dejar la frase con `[FALTA-FUENTE: A9]`, o quitar la frase. **Sacar a Oldroyd de la lista de referencias** hasta tener el PDF. |
| 2 | Cap. I p2, párrafo del aporte | Quitar el paréntesis «(Ohiomah et al., 2019; Rodriguez y Boyer, 2020; Habel et al., 2025)» y «(Nonaka y Takeuchi, 1995; Walsh y Ungson, 1991)», y dejar solo el marcador. Hoy aparecen como citas normales sin referencia. |
| 3 | Cap. IV, priorización | Marcar «(Kano et al., 1984)» y el «60 %» del Agile Business Consortium con `[FALTA-FUENTE]` hasta crear sus fichas. Kano está pendiente además de la DEC-25. Ambas se pueden verificar en la web: Claude lo hace sin que Victor baje nada. |
| 4 | Cap. II, IV (Bermeo y Segura) | Crear la ficha de la obra propia (`10_Antecedentes_Propios/2026-07-22_Informe_Final.pdf`) con las páginas 4, 5, 7, 10 y 28, y decidir con la tutora cómo se cita (FALTA-DATO de la referencia). |
| 5 | Cap. II (Rodriguez et al., 2025) | Cambiar «p. 20» y «p. 14» por la sección («Resultados», «Discusión») hasta tener la versión de Emerald. |
| 6 | Cap. IV (aporte patronal y tasa) | Corregir la frase del 12,15 % y el razonamiento de la tasa de descuento (§4, puntos 3 y 4). |
| 7 | Cap. I (Brehme) | «12 de 13 participantes calificaron sus casos por debajo del nivel 7». |
| 8 | Lista | Quitar o citar Ministerio del Trabajo (2026). Arreglar 2026a/b de Damodaran y González y el orden de Obsidian. |

### 5.2 Después (forma, sin cambiar el contenido)
Los puntos 3 a 17 de §3. Las páginas de la LOPDP y de Magesh en las fichas. La nota de Amaya. El matiz de la NIIF para las PYMES. Una fuente de 2021 en adelante que acompañe a AlQershi, Gil-Gomez, Kleppmann y el IESS.

### 5.3 PDF que Victor tendría que bajar a mano
Se cruzó con las fichas y con `11_Planificacion/F1_reporte_2026-10-19.md` §2 (la lista del 19-oct, que sigue abierta en lo que toca a estas obras). Destino: `00_Inbox/descargas/` y luego `procesar_descargas.py`.

| Prioridad | Obra | Por qué | Dónde (según la ficha o el reporte) |
|---|---|---|---|
| **Alta** | Oldroyd et al. (2011), *HBR* 89(3) — A9 | Cita activa del Cap. I y referencia en la lista | ResearchGate 298137032 (pide verificación humana) o EBSCO/Business Source de la biblioteca UPS |
| **Alta** | Rodriguez et al. (2025), versión publicada en *JBIM* | Para las páginas reales (pp. 2013–2027) | https://doi.org/10.1108/JBIM-02-2025-0097 (Emerald; biblioteca UPS) |
| **Alta** | Rodriguez y Boyer (2020) — A24, A26 | Cita activa sin referencia | https://doi.org/10.1057/s41270-020-00087-3 (Springer, de pago; biblioteca UPS) |
| Media | Ohiomah et al. (2019) — A21 | Cita activa sin referencia | https://doi.org/10.1016/j.jbusres.2019.05.018 (Elsevier, de pago) |
| Media | Habel et al. (2025) — A22 | Cita activa sin referencia | https://doi.org/10.1177/00222429251321417 (SAGE, de pago) |
| Media | Nonaka y Takeuchi (1995), libro | Cita activa sin referencia; origen del SECI | Biblioteca UPS (sin ficha; hoy el SECI se sostiene con Böhm y Durst 2026) |
| Media | Tuunanen et al. (2024), versión publicada en *MIS Quarterly* | Página de la definición y páginas del volumen | AIS eLibrary (https://aisel.aisnet.org/misq/vol48/iss2/5) |
| Baja | Pollitt (2000) — A8 | Solo en marcador; Stark (2024) ya sostiene el término | Sin DOI en la bóveda: hay que buscarlo en la biblioteca UPS |
| Baja | Walsh y Ungson (1991) | Solo hace falta si se mantiene la cita | Sin ficha ni DOI en la bóveda |
| Baja | Auernhammer y Roth (2021) | Solo en marcador (Cap. III) | https://doi.org/10.1111/jpim.12594 (Wiley) |
| Baja | Peffers et al. (2007) | Solo en marcador (las seis actividades de la DSR) | Sin ficha ni DOI en la bóveda |
| Baja | Haber y Stornetta (1991) | Solo en marcador | *Journal of Cryptology*, de pago (nota de nist_2015); sin DOI en la bóveda |
| Baja | Creswell y Plano Clark (2018) / Hernández-Sampieri y Mendoza (2018), libros | Solo en marcadores (A40) | Biblioteca UPS |
| Opcional | CEPAL, informe ILIA 2025 completo | Puntaje y página de Ecuador | Sitio de la CEPAL (pendiente en la ficha) |
| Opcional | Pérez-Campdesuñer (2025), Bakiyalakshmi (2026) y Radhakrishnan (2025, versión IET) | Copia local; ya están verificadas | Los sitios bloquearon la descarga automática |

No hace falta que Victor baje nada para: Kano (1984) (DOI de J-STAGE ya anotado en la lista), Agile Business Consortium (página web), Cuadrado Torres (número en la web de la revista), McKinsey (2023) (Exhibit 1). Claude puede verificarlas en la web cuando se pida.

---

*Qué no se revisó:*
- No se volvió a abrir el PDF de cada fuente verificada: se confió en la ficha, salvo en la LOPDP, la OCDE 2025b y el informe TEAMSLASH.
- No se revisaron las citas del correo a la tutora, de la presentación v0.4 ni de los Excel.
- No se verificó en la web ningún DOI.
- Al margen: el Anexo 5 del Word todavía dice «modelo financiero versión 0.2», mientras que el Cap. IV usa la v0.3.
