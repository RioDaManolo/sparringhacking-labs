# Ficha del laboratorio 6 — Revisión de permisos (binario SUID)

Dificultad: Fácil.

**Objetivo de aprendizaje**: entender qué es el bit SUID en Linux, por qué
un binario SUID que abre archivos usando sus privilegios efectivos sin
comprobar quién lo ejecuta es peligroso, y practicar la enumeración de
binarios SUID como primer paso de escalada de privilegios.

**Conocimientos previos**: permisos de archivos en Linux (lectura,
escritura, ejecución; dueño/grupo/otros) y uso básico de SSH.

**Contexto del desafío**: el alumno entra como un usuario de soporte sin
privilegios y debe leer un archivo que solo root puede leer directamente.

**Condición vulnerable**: `/usr/local/bin/verificar_backup` tiene el bit
SUID activo, es propiedad de root, y abre `/root/flag.txt` directamente con
`fopen()` sin comprobar quién lo está ejecutando. Cualquiera que lo corra
hereda el efectivo root del binario mientras se ejecuta, así que la
apertura del archivo se evalúa con esos privilegios, no con los del
usuario real.

**Recursos disponibles**: acceso SSH con usuario y clave entregados en la
descripción del laboratorio. Ninguna herramienta externa es necesaria,
solo `find`.

**Acción esperada**: enumerar binarios SUID con
`find / -perm -4000 -type f 2>/dev/null`, identificar el binario no
estándar y ejecutarlo.

**Evidencia de resolución**: salida del comando `verificar_backup`
mostrando la flag, o captura de la sesión SSH.

**Pistas**: ver `guia-corner-ia.md` (4 niveles, de "qué es un permiso
especial" hasta el nombre exacto del binario).

**Solución docente**:
```
find / -perm -4000 -type f 2>/dev/null
/usr/local/bin/verificar_backup
```

**Riesgos de seguridad**: ninguno más allá de los genéricos de la
plataforma. El binario vulnerable solo puede leer `/root/flag.txt` dentro
del propio contenedor; no hay forma de usarlo para salir del laboratorio.

**Criterios de evaluación**: el alumno presenta la flag y puede explicar
qué es el bit SUID, por qué el binario encontrado era sospechoso (ruta no
estándar) y por qué un binario SUID que abre archivos sin comprobar quién
lo ejecuta es una mala práctica.
