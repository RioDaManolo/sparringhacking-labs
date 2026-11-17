FROM ubuntu:24.04

LABEL sparring.flag.ruta="/var/backups/sistema/flag.txt"
LABEL sparring.flag.uid="1000"

RUN apt-get update && \
    apt-get install -y --no-install-recommends openssh-server cron && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir -p /var/run/sshd

# ubuntu:24.04 trae un usuario "ubuntu" de serie en el uid 1000; lo quitamos
# para poder reservar ese uid para nuestro propio usuario de práctica.
RUN userdel -r ubuntu 2>/dev/null || true

# Usuario de práctica (credenciales públicas: este laboratorio es de reconocimiento, no de fuerza bruta)
RUN useradd --create-home --shell /bin/bash --uid 1000 alumno && \
    echo "alumno:practica2026" | chpasswd && \
    useradd --create-home --shell /usr/sbin/nologin --uid 1001 svc-metrica && \
    useradd --create-home --shell /usr/sbin/nologin --uid 1002 svc-respaldo

# Carpeta donde el broker deja la flag (debe existir antes de arrancar)
RUN mkdir -p /var/backups/sistema && chmod 755 /var/backups/sistema

# Pistas de reconocimiento repartidas por el sistema de archivos
COPY app/bienvenida.txt /home/alumno/bienvenida.txt
COPY app/notas_falsas.txt /home/alumno/.notas_viejas
COPY app/respaldo.sh /usr/local/bin/respaldo.sh
COPY app/crontab-alumno /tmp/crontab-alumno

RUN chmod 755 /usr/local/bin/respaldo.sh && \
    chown alumno:alumno /home/alumno/bienvenida.txt /home/alumno/.notas_viejas && \
    crontab -u alumno /tmp/crontab-alumno && \
    rm /tmp/crontab-alumno && \
    ssh-keygen -A

RUN sed -i \
    -e 's/^#\?PermitRootLogin.*/PermitRootLogin no/' \
    -e 's/^#\?PasswordAuthentication.*/PasswordAuthentication yes/' \
    -e 's/^#\?UsePAM.*/UsePAM yes/' \
    /etc/ssh/sshd_config

EXPOSE 22

CMD ["/bin/sh", "-c", "cron && exec /usr/sbin/sshd -D"]
