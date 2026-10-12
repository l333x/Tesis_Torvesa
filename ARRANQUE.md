---
titulo: Arranque — cómo levantar todo después de apagar la PC
fecha: 2026-10-11
tipo: sistema
tags: [sistema, arranque]
---

# Arranque de la tesis

## Cada día (2 minutos)

1. **Verifica que F: esté montada:** abre el Explorador y comprueba que existe `F:\Obsidian\Tesis_Torvesa`.
2. **Abre Obsidian** en la bóveda de la tesis. Si es la primera vez: *Abrir otra bóveda → Abrir carpeta como bóveda →* `F:\Obsidian\Tesis_Torvesa`. Después se cambia de bóveda con el ícono de la esquina inferior izquierda.
3. **Doble clic en «Claude Tesis Torvesa»** (escritorio). Hace tres cosas solo:
   1. `git pull`: trae lo que subió Diego;
   2. actualiza el índice RAG (solo las notas que cambiaron);
   3. abre `claude` en la bóveda.

   Lee lo que imprime: si algo sale en **rojo**, mira la sección «Si algo falla».
4. **Revisa los respaldos (una vez por semana):** abre el acceso «Respaldos Tesis» y mira la última fila de `log_respaldos.md`. Debe tener la fecha de ayer a las 22:00 o la de tu último inicio de sesión.
5. **Al terminar:** `git add -A`, después `git commit -m "carpeta: qué hice"` y por último `git push` (detalle en `COLABORACION.md`).

«Claude Bóveda 1» abre Claude en la bóveda de Compras / Segundo Cerebro. No se mezclan.

## Si algo falla

### F: no está montada
- El lanzador muestra una ventana: «La unidad F: no está disponible». No abre nada a medias.
- Arreglo: conecta el disco o revisa en *Administración de discos* que tenga la letra F:. Los respaldos también están en F:, así que sin F: no hay respaldo ese día (queda anotado en el log al volver).

### Git sin acceso (`git pull` en rojo)
| Mensaje | Qué pasa | Qué hacer |
|---|---|---|
| `Could not resolve host` | Sin internet | Trabaja igual, y haz `git pull` y `git push` cuando vuelva la red |
| `Permission denied (publickey)` | La clave SSH no está cargada o cambió | `ssh -T git@github.com`. Si falla: `gh auth status`, y luego `gh auth refresh` o `gh ssh-key list`. **Las contraseñas y passphrases las escribes tú; nunca las pegues en una nota** |
| `Not possible to fast-forward` / `CONFLICT` | Tú y Diego cambiaron lo mismo | Ver «Si aparece un conflicto» en `COLABORACION.md`. No edites hasta resolverlo |
| `not a git repository` | La carpeta perdió `.git` | **No hagas `git init`**: restaura el último zip de `F:\Respaldos_Tesis` o clona de nuevo con `gh repo clone <usuario>/Tesis_Torvesa` |

### RAG desactualizado o con error
- El lanzador dice «El RAG falló»: Claude funciona igual, pero la búsqueda semántica puede estar vieja.
- Reconstruir desde cero (5–10 min):
  ```powershell
  $env:PYTHONUTF8 = "1"
  F:\IA\venvs\tesis_rag\Scripts\python.exe F:\Obsidian\Tesis_Torvesa\99_Scripts\rag\rag.py indexar --reconstruir
  ```
- Si falta el entorno `F:\IA\venvs\tesis_rag`: ver `RAG_README.md`, sección «Levantarlo en una PC nueva».

### Respaldos no corren
- Revisa la tarea: `schtasks /Query /TN "Tesis_Respaldo_Diario"` y `schtasks /Query /TN "Tesis_Respaldo_Logon"`.
- Respaldo manual: `py -3.13 F:\Respaldos_Tesis\respaldo_tesis.py --forzar`
- Restaurar: descomprime el zip en otra carpeta, compara y copia lo que necesites. **Nunca descomprimas encima de la bóveda.**
