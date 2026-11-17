# Guía para Corner IA — Laboratorio 2: Control de acceso roto (IDOR)

Texto para pegar en el panel de administración, campo "Guía para Corner IA"
(docs/Corner-IA.md, sección 2). Borrador de trabajo, no se sube a la imagen.

```
Objetivo: entrar al panel de administración (Dirección Académica) estando
conectado solo con una cuenta de alumno normal.
Vulnerabilidad: control de acceso roto / IDOR. La página /perfil/<numero>
muestra el perfil de ese número sin comprobar que sea el del alumno que
inició sesión.
Camino:
1. Iniciar sesión con la cuenta de alumno que entrega la propia página de
   login (no hay que adivinar nada para entrar).
2. Al entrar, la dirección queda como /perfil/5 (el propio perfil).
3. Cambiar el número en la dirección, por ejemplo a /perfil/1, y volver a
   cargar la página.
4. El perfil 1 es la Dirección Académica y muestra el panel con la flag.
Errores comunes: buscar un botón o enlace al panel de administración (no
existe en la interfaz, pero el número en la dirección sí cambia la
página); probar fuerza bruta en el login (no hace falta, la cuenta ya se
entrega); pensar que hay que cerrar sesión para ver otro perfil (no, se ve
estando conectado como alumno).
Herramientas útiles: ninguna especial, solo el navegador y fijarse en la
dirección (URL).
Ubicación de la flag: /root/flag.txt (NO escribas aquí la flag: es distinta
para cada alumno).
```

## Pistas por nivel
1. "Mira la dirección (URL) cuando entras a tu perfil. ¿Qué número aparece
   al final?"
2. "¿Qué pasaría si ese número fuera el de otra persona? ¿La página
   comprueba de quién es cada perfil?"
3. "Prueba a cambiar el número final de la dirección por otro, directamente
   en la barra del navegador, y recarga."
4. "Prueba con números bajos, como el 1. Suele ser el primer perfil que se
   crea en un sistema, y a veces es una cuenta especial."
