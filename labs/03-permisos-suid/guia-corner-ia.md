# Guía para Corner IA — Laboratorio 6: Revisión de permisos (binario SUID)

Texto para pegar en el panel de administración, campo "Guía para Corner IA"
(docs/Corner-IA.md, sección 2). Borrador de trabajo, no se sube a la imagen.

Dificultad: Fácil. Es la introducción clásica a escalada de privilegios en
Linux: encontrar un binario con el bit SUID mal puesto. No requiere exploits
complejos, solo un comando de enumeracion y entender qué significa SUID.

```
Objetivo: leer /root/flag.txt estando conectado como un usuario normal
(soporte / soporte2026, credenciales que se entregan directamente: este
laboratorio no es de fuerza bruta).
Vulnerabilidad: existe un binario en /usr/local/bin/verificar_backup con el
bit SUID activo y dueño root. El programa abre /root/flag.txt directamente
con fopen(), sin comprobar quien lo esta ejecutando, asi que cualquiera
que lo ejecute hereda el efectivo root del binario mientras corre y la
apertura del archivo se evalua con esos privilegios.

Camino:
1. Conectarse por SSH con las credenciales entregadas.
2. Buscar binarios con el bit SUID activo:
   find / -perm -4000 -type f 2>/dev/null
3. La lista incluye binarios normales del sistema (passwd, su, sudo, mount,
   etc.) y uno que no es estandar: /usr/local/bin/verificar_backup.
4. Ejecutarlo: /usr/local/bin/verificar_backup
   El programa imprime el contenido de /root/flag.txt directamente.

Error comun: intentar leer /root/flag.txt directamente con "cat" como el
usuario soporte. Eso falla (permiso denegado): el archivo es 0400 y de
root. La unica forma de leerlo es a traves del binario SUID, no accediendo
al archivo de forma directa.

Herramientas utiles: ningun escaner externo. find es suficiente para
encontrar el binario.
Ubicacion de la flag: /root/flag.txt (el binario la imprime por pantalla,
no hace falta copiarla a otro lado).
```

## Pistas por nivel
1. "Si intentas leer /root/flag.txt directamente te va a decir 'permiso
   denegado'. En Linux hay un tipo de permiso especial que hace que un
   programa se ejecute con los privilegios de su dueño, no de quien lo
   corre. ¿Sabes cual es?"
2. "Se llama bit SUID. Hay un comando para buscar todos los archivos del
   sistema que tengan ese bit activo: busca 'find' combinado con el permiso
   4000."
3. "El comando es `find / -perm -4000 -type f 2>/dev/null`. La lista tiene
   varios binarios normales del sistema operativo. Busca uno que no
   deberia estar ahi, fuera de las carpetas tipicas del sistema."
4. "El binario se llama /usr/local/bin/verificar_backup. Ejecutalo
   directamente: al tener el bit SUID y ser dueño root, imprime el
   contenido de /root/flag.txt aunque tu usuario no tenga permiso para
   leerlo por si mismo."
