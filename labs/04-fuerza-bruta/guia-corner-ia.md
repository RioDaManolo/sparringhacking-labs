# Guía para Corner IA — Laboratorio 1: Fuerza bruta

Texto para pegar en el panel de administración, campo "Guía para Corner IA"
(docs/Corner-IA.md, sección 2). No se sube al repo como parte de la imagen;
este archivo es solo el borrador de trabajo.

```
Objetivo: iniciar sesión en el panel docente del Portal Campus (Instituto TecnoSur).
Vulnerabilidad: el formulario de login en /login no tiene límite de intentos
(sin bloqueo de cuenta, sin CAPTCHA, sin demora progresiva) y la cuenta de la
profesora usa una contraseña débil y común.
Camino:
1. Abrir la página: hay un formulario con campos "usuario" y "clave".
2. El usuario correcto es el nombre de la profesora que aparece en el contexto
   del instituto (no está escondido, se puede intentar con nombres plausibles
   o deducir mirando la página).
3. La contraseña es débil y está en cualquier diccionario común de contraseñas
   filtradas (tipo rockyou.txt), cerca del principio.
4. Se prueba con Hydra contra el formulario POST, usando los nombres de los
   campos del formulario (usuario, clave) y el texto exacto del mensaje de
   error como condición de fallo.
5. Al acertar, el panel docente muestra la flag directamente.
Errores comunes: buscar otros puertos o servicios (no hay ninguno más
abierto); intentar inyección SQL en el login (el formulario no es vulnerable
a eso, es un problema de fuerza bruta, no de inyección); no saber qué
herramienta usar para probar muchas contraseñas rápido.
Herramientas útiles: nmap (para confirmar que solo el puerto 80 está
abierto), Hydra, un diccionario de contraseñas comunes.
Ubicación de la flag: /root/flag.txt (NO escribas aquí la flag: es distinta
para cada alumno).
```

## Pistas por nivel (si se usan como respaldo escrito, además de Corner IA)
1. "¿Qué le pasa al formulario si escribes la contraseña incorrecta muchas
   veces seguidas? ¿Te bloquea en algún momento?"
2. "Cuando un formulario no limita los intentos, se puede probar una lista
   de contraseñas comunes de forma automática. ¿Qué herramienta de Kali
   sirve para eso contra un formulario web?"
3. "Prueba Hydra contra `/login` con el módulo `http-post-form`. Fíjate en
   los nombres de los campos del formulario y en el texto que aparece
   cuando la contraseña es incorrecta."
4. "El comando es `hydra -l <usuario> -P <diccionario> <IP> http-post-form
   \"/login:usuario=^USER^&clave=^PASS^:incorrectos\"`. Usa un diccionario
   de contraseñas comunes, como rockyou.txt."
