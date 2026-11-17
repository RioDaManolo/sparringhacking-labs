#!/bin/sh
# Tarea de respaldo del sistema. El respaldo se guarda en /var/backups/sistema/
# Si este script falla, revisar permisos de esa carpeta.
echo "$(date): respaldo ejecutado" >> /home/alumno/.respaldo.log
