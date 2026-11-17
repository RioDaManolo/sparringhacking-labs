# Guía para Corner IA — Laboratorio 5: Acceso oculto (control de acceso roto)

Texto para pegar en el panel de administración, campo "Guía para Corner IA"
(docs/Corner-IA.md, sección 2). Borrador de trabajo, no se sube a la imagen.

Dificultad: Fácil. Variante simple de control de acceso roto: a diferencia
del laboratorio de escalada de privilegios (que exige manipular un ID
numerico), aqui basta con encontrar una URL que nadie enlaza.

```
Objetivo: llegar a /panel-interno-2024 y ver la flag. Esa pagina no pide
sesion ni contrasena: la unica razon por la que un visitante normal no
llega ahi es que ningun enlace del sitio apunta a ella.

Camino (dos formas de encontrar la misma URL escondida):
1. Ver el codigo fuente de la pagina principal (click derecho > Ver codigo
   fuente, o Ctrl+U). Cerca del final hay un comentario HTML que menciona
   la ruta /panel-interno-2024.
2. O bien, visitar /robots.txt: ese archivo le dice a los buscadores que no
   indexen /panel-interno-2024, lo que de hecho revela que esa ruta existe.
Cualquiera de los dos caminos lleva a la misma URL. Solo hay que escribirla
en la barra de direcciones: no requiere usuario ni contrasena.

Error comun: pensar que hace falta iniciar sesion o probar usuarios y
contrasenas. Esta maquina no tiene formulario de login: el problema es
que una pagina sensible quedo expuesta sin ningun control.

Herramientas utiles: el navegador basta (ver codigo fuente, /robots.txt).
No hace falta ningun escaner.
Ubicacion de la flag: /root/flag.txt (se muestra directamente en la pagina
/panel-interno-2024, no hace falta leer el archivo del sistema).
```

## Pistas por nivel
1. "Esta pagina no tiene ningun formulario para iniciar sesion. A veces los
   desarrolladores dejan paginas sensibles sin enlazar, pensando que nadie
   las va a encontrar. ¿Revisaste el codigo fuente de la pagina principal?"
2. "Busca comentarios HTML (texto entre `<!--` y `-->`) en el codigo fuente.
   También existe un archivo estandar que los sitios usan para decirle a
   los buscadores que paginas NO indexar: ¿sabes cual es?"
3. "El archivo /robots.txt de este sitio tiene una linea 'Disallow'. Esa
   linea apunta justo a la pagina que buscas."
4. "Visita /robots.txt o mira el comentario al final del codigo fuente de
   la pagina principal: ambos mencionan la ruta /panel-interno-2024. Entra
   directamente a esa URL."
