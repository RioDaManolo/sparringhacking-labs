# Guía para Corner IA — Laboratorio 3: Inyección SQL (dos caminos)

Texto para pegar en el panel de administración, campo "Guía para Corner IA"
(docs/Corner-IA.md, sección 2). Borrador de trabajo, no se sube a la imagen.

Este laboratorio tiene **dos caminos distintos** hasta la misma flag. Es el
indicado para que Corner IA, además de tutor, actúe como evaluador: que el
alumno cuente qué camino siguió y la IA le muestre cuál era el otro.

```
Objetivo: obtener la flag del Catálogo de Cursos. Hay dos caminos posibles.
Vulnerabilidad: ninguna de las dos consultas SQL de la página usa parámetros;
arman el SQL concatenando directamente lo que escribe el usuario.

CAMINO A — Saltarse el login (/login)
1. El formulario de coordinadores comprueba usuario y clave en una sola
   consulta SQL.
2. Escribiendo en el campo "usuario" algo como ' OR '1'='1' -- (con un
   espacio al final) y cualquier texto en "clave", la condición de la
   clave queda comentada y la consulta siempre resulta verdadera.
3. Eso entrega acceso al panel de coordinación, que muestra la flag.
Error común en este camino: probar solo ' OR '1'='1 sin el comentario final
(-- ). Sin comentar el resto de la consulta, la condición de la clave sigue
exigiéndose y el intento falla. Hay que cortar el resto de la consulta.

CAMINO B — Extraer el dato desde el buscador (/buscar), sin iniciar sesión
1. El buscador de cursos es público y también arma la consulta SQL sin
   parámetros.
2. Escribir una sola comilla (') en el buscador produce un error de sintaxis
   visible: es la señal de que el campo es vulnerable.
3. Con una inyección UNION SELECT se puede agregar una fila falsa a los
   resultados con datos de OTRA tabla de la base, no solo de cursos.
4. Existe una tabla llamada "configuracion" con una fila cuya clave es
   "flag_evento" y cuyo valor es la flag. Una consulta como:
   algo' UNION SELECT 1, clave, valor FROM configuracion --
   agrega esas filas a los resultados de la búsqueda, incluida la flag.
Error común en este camino: no ajustar el número de columnas del UNION
SELECT al de la consulta original (son 3: id, nombre, descripcion). Si no
coinciden, SQLite devuelve un error que lo indica.
Pista avanzada (opcional, para quien ya sabe UNION): se puede descubrir el
nombre de la tabla "configuracion" sin que nadie lo diga, consultando antes
la tabla interna de SQLite: ' UNION SELECT 1, name, sql FROM sqlite_master
WHERE type='table' --

Herramientas útiles: el navegador basta para los dos caminos; no hace falta
sqlmap ni otra herramienta, aunque se puede usar para explorar más rápido.
Ubicación de la flag: /root/flag.txt (NO escribas aquí la flag: es distinta
para cada alumno; el laboratorio la copia también a una fila de la base de
datos al iniciar, para que el camino B funcione).
```

## Pistas por nivel (comunes a los dos caminos)
1. "Hay dos formularios en esta página: el buscador de cursos y el acceso
   de coordinadores. Prueba a escribir una sola comilla (') en cualquiera
   de los dos. ¿Qué pasa?"
2. "Ese error significa que el texto que escribes se mete directo en una
   instrucción de base de datos. ¿Conoces la inyección SQL?"
3. "Si vas por el login: busca cómo hacer que la condición de la contraseña
   deje de importar, comentando el resto de la consulta. Si vas por el
   buscador: busca cómo agregar una consulta UNION SELECT a los
   resultados."
4. "Camino del login: prueba `' OR '1'='1' -- ` como usuario, con cualquier
   contraseña. Camino del buscador: prueba `' UNION SELECT 1, clave, valor
   FROM configuracion -- ` y fíjate en el número de columnas."

## Evaluador de caminos (para cuando el alumno ya resolvió el laboratorio)
Si el alumno dice que entró por el login (camino A), la IA explica que
también existía un camino sin iniciar sesión: inyectar el buscador público
con una consulta UNION para leer directamente la tabla de configuración.
Si el alumno dice que usó el buscador (camino B), la IA explica que
también se podía entrar al panel saltándose la contraseña con una
inyección en el formulario de login. En ambos casos, la IA destaca que la
causa de fondo es la misma: ninguna de las dos consultas usa parámetros.
