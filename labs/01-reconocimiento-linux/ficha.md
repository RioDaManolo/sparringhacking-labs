# Ficha del laboratorio 4 — Reconocimiento de entorno Linux

Dificultad: Fácil.

**Objetivo de aprendizaje**: identificar archivos, permisos, usuarios y
tareas programadas en un sistema Linux ya accesible, sin necesidad de
explotar ninguna vulnerabilidad.

**Conocimientos previos**: uso básico de una terminal Linux (`ls`, `cat`,
`cd`), qué es un usuario y una tarea programada (concepto, no sintaxis
exacta).

**Contexto del desafío**: el alumno recibe credenciales SSH válidas de
entrada. No hay nada que "romper" para entrar; el ejercicio es explorar el
sistema una vez dentro.

**Condición vulnerable**: no aplica — este laboratorio no tiene una
vulnerabilidad deliberada, es de reconocimiento. La única condición es que
la flag no está en un lugar obvio y requiere seguir pistas del propio
sistema (crontab → script → carpeta de respaldo).

**Recursos disponibles**: acceso SSH con usuario y clave entregados en la
descripción del laboratorio. Ninguna herramienta externa es necesaria.

**Acción esperada**: revisar `crontab -l`, leer el script que esa tarea
ejecuta, listar la carpeta que el script menciona y leer `flag.txt` ahí.

**Evidencia de resolución**: captura o copia de la flag obtenida con el
comando `cat` sobre la ruta correcta.

**Pistas**: ver `guia-corner-ia.md` (4 niveles, de "revisa tus tareas
programadas" hasta los comandos exactos).

**Solución docente**:
```
crontab -l
cat /usr/local/bin/respaldo.sh
ls -la /var/backups/sistema/
cat /var/backups/sistema/flag.txt
```

**Riesgos de seguridad**: ninguno más allá de los genéricos de la
plataforma (contenedor aislado, sin salida a internet, recursos limitados
por el broker). No hay escalada de privilegios en este laboratorio: la
flag es propiedad del mismo usuario con el que se inicia sesión.

**Criterios de evaluación**: el alumno presenta la flag con formato válido
(`SH{...}`) y puede explicar en qué archivo o carpeta la encontró y qué
comando usó para llegar ahí (no basta con pegar la flag sin explicar el
camino, si se evalúa comprensión y no solo finalización).
