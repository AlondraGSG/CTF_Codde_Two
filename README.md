# Checkpoint
<p> funciona como un punto de control que permite guardar el progreso de una tarea mientras se está ejecutando. Su objetivo es evitar que se pierda todo el trabajo si ocurre un error o se interrumpe el proceso. Cuando se necesita continuar, el programa puede recuperar la información guardada y seguir desde el último punto de control, sin tener que empezar desde cero. </p>

### ¿como funciona el programa?
<p> El programa simula la extracción de datos de ocho páginas web y guarda el progreso en un archivo llamado `scraper_checkpoint.pkl` después de procesar cada página. Al completar tres páginas, se detiene automáticamente para simular un fallo. Cuando se presiona nuevamente Run, carga el checkpoint guardado y continúa desde la cuarta página, evitando repetir el trabajo anterior. Al finalizar la extracción de todas las páginas, muestra los datos recopilados y elimina el archivo de checkpoint. </p>

