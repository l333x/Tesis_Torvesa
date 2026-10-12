---
titulo: Cómo trabajamos Víctor y Diego en esta bóveda
fecha: 2026-10-11
tipo: sistema
tags: [sistema, git, colaboracion]
---

# Colaboración con Git

Repositorio **privado** en GitHub. Lo pueden ver solo Víctor y Diego.

## Primera vez — Diego (una sola vez, ~30 min)

**1. Aceptar la invitación.** GitHub te manda un correo, o entra directo a <https://github.com/notifications> o a <https://github.com/l333x/Tesis_Torvesa/invitations> → **Accept invitation**. La invitación caduca a los 7 días: si caduca, pide a Víctor que la reenvíe.

**2. Instalar las herramientas** (PowerShell normal):
```powershell
winget install --id Git.Git -e
winget install --id GitHub.cli -e
winget install --id Python.Python.3.13 -e
winget install --id Obsidian.Obsidian -e
```
Cierra y vuelve a abrir la terminal.

**3. Identidad y login.** Las contraseñas y passphrases las escribes tú; nunca las pegues en una nota ni en un chat.
```powershell
git config --global user.name "Diego Bermeo"
git config --global user.email "<tu correo de GitHub>"
gh auth login --hostname github.com --git-protocol ssh --web
#   Generate a new SSH key? -> Yes · passphrase -> la tuya · Title -> PC-Diego-Tesis
#   copia el código, Enter, pégalo en el navegador -> Authorize
gh auth status            # debe decir: Logged in to github.com account PiscesLivie
ssh -T git@github.com     # debe decir: Hi PiscesLivie! You've successfully authenticated
```

**4. Clonar el repo.** Elige una carpeta **fuera de OneDrive**, porque OneDrive y Git se pelean:
```powershell
cd C:\        # o D:\ si tienes otro disco
gh repo clone l333x/Tesis_Torvesa
cd Tesis_Torvesa
git config core.sshCommand "C:/Windows/System32/OpenSSH/ssh.exe"
```

**5. Abrirlo en Obsidian:** *Abrir otra bóveda → Abrir carpeta como bóveda →* la carpeta `Tesis_Torvesa` que acabas de clonar.

**6. Levantar el RAG:** sigue `RAG_README.md`, sección «Levantarlo en una PC nueva». Resumen:
```powershell
py -3.13 -m venv C:\IA\venvs\tesis_rag
C:\IA\venvs\tesis_rag\Scripts\python.exe -m pip install -r 99_Scripts\rag\requirements.txt
$env:PYTHONUTF8 = "1"
C:\IA\venvs\tesis_rag\Scripts\python.exe 99_Scripts\rag\rag.py indexar --reconstruir
C:\IA\venvs\tesis_rag\Scripts\python.exe 99_Scripts\rag\rag.py consultar "tiempo de elaboración de cotizaciones"
```
La primera vez descarga el modelo (~1,1 GB). Si da error SSL, mira la tabla «Si algo falla» del README.

**7. (Opcional) No escribir la passphrase en cada `pull`:** en PowerShell **como administrador**, `Set-Service ssh-agent -StartupType Automatic; Start-Service ssh-agent`. Luego, en PowerShell normal, `ssh-add`, y escribes la passphrase una sola vez por sesión.

**8. Prueba de que todo quedó bien:** crea `00_Inbox/hola_diego.md`, y luego `git add -A`, `git commit -m "00_Inbox: prueba de Diego"` y `git push`. Avísale a Víctor; él hace `git pull` y lo ve.

## Quién toca qué

| Carpeta | Dueño | El otro puede… |
|---|---|---|
| `02_Fuentes`, `03_Matriz_Objetivos`, `04_Instrumentos`, `06_Capitulos`, `08_Reuniones_Tutora` | **Víctor** | leer y comentar (callout `> [!question] Diego:`) |
| `07_Flujos_Diseno`, `99_Scripts`, RAG (`RAG_README.md`) | **Diego** | leer y comentar (`> [!question] Víctor:`) |
| `00_Inbox`, `09_Registro_Contribuciones`, `11_Planificacion` | ambos | agregar; cada uno edita solo sus propias entradas |
| `01_Borrador_Aprobado` | nadie | solo lectura |
| `05_Datos_Campo` | Víctor | **solo datos anonimizados**; lo crudo va en `_crudo/`, que nunca sube |
| `10_Antecedentes_Propios` | ambos | solo agregar, no editar |

Si necesitas cambiar algo de la carpeta del otro, **avísale primero** (WhatsApp) o deja el comentario en la nota. Así casi no hay conflictos.

## Rutina de cada sesión

1. **Antes de trabajar:** `git pull`. El lanzador «Claude Tesis Torvesa» lo hace solo; desde Obsidian puede hacerlo el plugin *Obsidian Git* («Pull»).
2. **Mientras trabajas:** commits pequeños, uno por tarea terminada:
   ```powershell
   git add -A
   git commit -m "02_Fuentes: 5 fichas verificadas de speed-to-lead (A9, A10)"
   ```
   Formato del mensaje: `carpeta: qué hiciste (afirmaciones u objetivos)`. Si usaste IA, agrégalo: `[IA: Claude]`.
3. **Al terminar:** `git pull` y luego `git push`.
4. Registra el entregable en `09_Registro_Contribuciones/` (autor, fecha y herramienta de IA usada).

## Si aparece un conflicto

Pasa cuando los dos editan las mismas líneas del mismo archivo.

1. `git pull` avisa: `CONFLICT (content): Merge conflict in <archivo>`.
2. Abre el archivo. Vas a ver:
   ```
   <<<<<<< HEAD
   tu versión
   =======
   la versión del otro
   >>>>>>> origin/main
   ```
3. Deja el texto correcto (puede ser una mezcla), **borra las tres líneas de marcas** y guarda.
4. `git add <archivo>`, después `git commit -m "merge: resuelve conflicto en <archivo>"` y por último `git push`.
5. Si no sabes cuál versión vale, **no adivines**: `git merge --abort` deja todo como estaba antes del pull, y lo hablan.

En un `.docx` (binario) Git no puede mezclar. Para esos archivos, el autor del capítulo es el único que lo edita, y el otro comenta en la nota `.md` del capítulo.

## Antes de subir datos de campo
```powershell
F:\IA\venvs\tesis_rag\Scripts\python.exe 99_Scripts\auditoria_pii.py    # debe decir: 0 hallazgos
```
Revisa correos, teléfonos y cédulas en todo lo que Git sube (también dentro de PDF y Word). Si encuentra algo, **no hagas push**: el dato va a `05_Datos_Campo/_crudo/`, que nunca se sube.

## Nunca
- Subir claves, tokens, contraseñas ni archivos `.env`. El `.gitignore` los bloquea, pero el responsable eres tú.
- Subir datos de campo sin anonimizar.
- `git push --force`.
- Renombrar o mover carpetas del otro sin avisar.

> Nota: el `.gitignore` excluye cualquier archivo cuyo nombre contenga `token` o `secret`. Si una ficha legítima lleva esa palabra en el nombre, cámbiale el nombre.
