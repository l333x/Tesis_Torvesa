@echo off
rem Genera las figuras de la tesis con un doble clic.
chcp 65001 >nul
set PYTHONUTF8=1
"F:\IA\venvs\tesis_rag\Scripts\python.exe" "%~dp0generar_figuras.py" %*
if errorlevel 1 echo. & echo Hubo un error. Copia el texto de arriba y pasaselo a Claude.
if not defined SIN_ABRIR explorer "%~dp0..\..\06_Capitulos\Figuras"
if not defined SIN_ABRIR pause
