FROM ubuntu:24.04

LABEL sparring.flag.ruta="/root/flag.txt"
LABEL sparring.flag.uid="0"

RUN apt-get update && \
    apt-get install -y --no-install-recommends openssh-server build-essential && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir -p /var/run/sshd

# ubuntu:24.04 trae un usuario "ubuntu" de serie en el uid 1000; lo quitamos
# para poder reservar ese uid para nuestro propio usuario de práctica.
RUN userdel -r ubuntu 2>/dev/null || true

RUN useradd --create-home --shell /bin/bash --uid 1000 soporte && \
    echo "soporte:soporte2026" | chpasswd

COPY app/verificar_backup.c /tmp/verificar_backup.c
RUN gcc -o /usr/local/bin/verificar_backup /tmp/verificar_backup.c && \
    chown root:root /usr/local/bin/verificar_backup && \
    chmod 4755 /usr/local/bin/verificar_backup && \
    rm /tmp/verificar_backup.c && \
    apt-get purge -y build-essential && apt-get autoremove -y

RUN ssh-keygen -A && \
    sed -i \
        -e 's/^#\?PermitRootLogin.*/PermitRootLogin no/' \
        -e 's/^#\?PasswordAuthentication.*/PasswordAuthentication yes/' \
        -e 's/^#\?UsePAM.*/UsePAM yes/' \
        /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
