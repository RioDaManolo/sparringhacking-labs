# Guía para Corner IA — Laboratorio 4: Reconocimiento de entorno Linux

Texto para pegar en el panel de administración, campo "Guía para Corner IA"
(docs/Corner-IA.md, sección 2). Borrador de trabajo, no se sube a la imagen.

Dificultad: Fácil. Es el primer laboratorio recomendado para quien recién
empieza: no hay nada que "romper", solo explorar un sistema Linux ya con
sesión iniciada.

```
Objetivo: encontrar flag.txt en algun lugar del sistema de archivos al que
el alumno ya tiene acceso de lectura, aunque no este en su carpeta personal.
No hay vulnerabilidad que explotar: es un ejercicio de reconocimiento puro.
El alumno entra por SSH con credenciales que se le entregan directamente
(usuario alumno, clave practica2026). No hace falta adivinar nada para entrar.

Camino:
1. Revisar las tareas programadas propias con "crontab -l". Ahi aparece una
   tarea que ejecuta /usr/local/bin/respaldo.sh.
2. Leer ese script con "cat" (es de lectura publica). El comentario dentro
   dice que el respaldo se guarda en /var/backups/sistema/.
3. Listar esa carpeta con "ls -la /var/backups/sistema/" y leer flag.txt
   con "cat" (el archivo es del mismo alumno, por eso puede leerlo aunque
   el permiso sea 0400).

Error comun: encontrar el archivo /home/alumno/.notas_viejas (un dotfile,
hay que usar "ls -la" para verlo) con un texto que PARECE una flag pero no
tiene el formato SH{32 caracteres hexadecimales}. Esa no es la flag real,
es una nota vieja a proposito para ensenar a fijarse en el formato exacto.

Herramientas utiles: ningun escaner. Basta con comandos basicos: ls -la,
cat, crontab -l, find / -user alumno 2>/dev/null, cat /etc/passwd (para ver
que otros usuarios existen y con que shell, aunque ninguno es explotable
en este laboratorio: es solo para practicar a leerlo).
Ubicacion de la flag: /var/backups/sistema/flag.txt
```

## Pistas por nivel
1. "Este servidor no pide adivinar nada: ya entraste. El objetivo es encontrar
   un archivo. ¿Revisaste si tienes alguna tarea programada propia?"
2. "El comando `crontab -l` muestra las tareas programadas del usuario con el
   que entraste. Una de ellas ejecuta un script: ¿qué dice ese script si lo
   lees con `cat`?"
3. "El script de respaldo menciona una carpeta fuera de tu carpeta personal.
   Prueba `ls -la` en esa carpeta."
4. "Prueba exactamente: `crontab -l`, después `cat /usr/local/bin/respaldo.sh`,
   después `ls -la /var/backups/sistema/` y `cat /var/backups/sistema/flag.txt`."
