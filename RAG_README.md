---
titulo: RAG local de la bóveda — cómo levantarlo
fecha: 2026-10-11
tipo: sistema
responsable: Diego
tags: [sistema, rag]
---

# RAG local de la bóveda

Busca por significado (no por palabra exacta) en todas las notas `.md` de la bóveda y devuelve los fragmentos con **ruta de la nota, sección y referencia APA**. Así cada respuesta se puede rastrear a una ficha de `02_Fuentes`.

- **Todo local:** embeddings `intfloat/multilingual-e5-base` (español/inglés, ~1,1 GB) y ChromaDB. Ningún texto sale a una API externa.
- **La base vectorial no está en Git.** Vive en `.rag/` (carpeta oculta e ignorada) y cada PC la reconstruye.
- **Incremental:** guarda el hash SHA-256 de cada nota en `.rag/estado.json` y solo reprocesa las que cambiaron.
- **Fragmentación:** una sección por encabezado Markdown (las secciones de más de 1500 caracteres se parten por párrafos con un solape de 200). El frontmatter viaja como metadatos: `categoria`, `objetivos`, `anio`, `estado`, `referencia_apa`, `ruta`…
- **No se indexan:** `99_Scripts/`, `05_Datos_Campo/_crudo/`, `.obsidian/` ni los documentos del sistema (`RAG_README`, `COLABORACION`, `ARRANQUE`). Lo que el sistema escribe sobre sí mismo no debe competir con las fuentes.

## Levantarlo en una PC nueva (Diego)

Requisito: Python 3.11–3.13.

```powershell
# 1. Entorno virtual FUERA de la bóveda (pesa ~1,5 GB con torch)
py -3.13 -m venv C:\IA\venvs\tesis_rag
C:\IA\venvs\tesis_rag\Scripts\python.exe -m pip install -r 99_Scripts\rag\requirements.txt

# 2. Construir el índice (la primera vez descarga el modelo, ~1,1 GB)
$env:PYTHONUTF8 = "1"
C:\IA\venvs\tesis_rag\Scripts\python.exe 99_Scripts\rag\rag.py indexar --reconstruir
```

Variables opcionales:
- `HF_HOME`: dónde guardar el modelo.
- `TESIS_BOVEDA`: si se corre el script desde fuera de la bóveda.
- `EMBED_DEVICE=cuda`: si hay GPU NVIDIA.

En la PC de Víctor, el entorno está en `F:\IA\venvs\tesis_rag` y el modelo en `F:\IA\hf`.

## Uso

```powershell
$py = "F:\IA\venvs\tesis_rag\Scripts\python.exe"     # Diego: su ruta
& $py 99_Scripts\rag\rag.py indexar                    # después de cambiar notas (el lanzador lo hace solo)
& $py 99_Scripts\rag\rag.py consultar "tiempo de respuesta a leads"
& $py 99_Scripts\rag\rag.py consultar "speed to lead" --solo-fuentes --estado verificada -k 8
& $py 99_Scripts\rag\rag.py consultar "LOPDP consentimiento" --json   # salida para otros scripts
& $py 99_Scripts\rag\rag.py estado
```

Cada resultado se marca así:
- **✅ citable**: es una ficha de `02_Fuentes` con `estado: verificada`.
- **⛔ NO citable**: es una ficha que todavía no está verificada.
- **ℹ️ nota interna**: no es una fuente (borrador, planificación, datos).

**Regla de la tesis: solo se cita lo marcado ✅.**

## Si algo falla
| Síntoma | Arreglo |
|---|---|
| Resultados viejos o raros | `rag.py indexar --reconstruir` |
| `El índice está vacío` | `rag.py indexar` |
| Error SSL al descargar el modelo | Red con certificado propio: descarga el modelo en otra red una vez; después funciona sin internet |
| Se cambió `EMBED_MODEL` | El script lo detecta y reconstruye todo solo |
