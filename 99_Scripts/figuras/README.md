# Figuras de la tesis con un clic

1. **Para generar las figuras:** doble clic en `Generar_Figuras.bat`. Al terminar se abre la carpeta `06_Capitulos/Figuras/` con los PNG.
2. **Para cambiar un texto:** abre `datos_figuras.json` con el Bloc de notas, cambia el texto y sube la versión en el nombre del archivo (`v0.2` → `v0.3`). Guarda y vuelve a dar doble clic.
3. **No pisa nada:** si un PNG ya existe, no lo toca. Para rehacer todo, abre una terminal aquí y escribe `Generar_Figuras.bat --forzar`. Para una sola figura: `Generar_Figuras.bat --forzar --solo FODA`.
4. **Qué figuras hace:** los flujos con carriles y tiempos (proceso actual, proceso estrella, cotización, casos especiales), la vista general, el recorrido de la prueba de concepto, el FODA, las tablas (censo, metas, requisitos) y los diagramas E2 a E5.
5. **No gasta tokens ni usa internet:** es un programa de Python (`generar_figuras.py`) con el entorno `F:\IA\venvs\tesis_rag`. Los colores y las letras salen de `99_Scripts/gestion/diagramas.py`.
6. **Si falla:** la ventana muestra el error. Lo más común es una coma o una comilla de más en `datos_figuras.json`.
7. **Lo que este programa no hace:** las ilustraciones de Gemini (se piden a mano en gemini.google.com) y los diagramas BPMN de `07_Flujos_Diseno/` (se editan en https://demo.bpmn.io).
8. **Miro:** el tablero no se puede actualizar con un clic. Hoy lo dibuja Claude con el conector de Miro. La otra vía sería la API de Miro, que pide crear una aplicación y un token en la cuenta de Miro; no está hecho y solo se hace si Víctor lo pide.
9. **Atajo para Miro sin tokens:** arrastra los PNG de `06_Capitulos/Figuras/` al tablero; quedan como imágenes.
10. **Antes de usar una figura en la tesis:** ábrela y revisa que ningún texto se salga de su caja.
