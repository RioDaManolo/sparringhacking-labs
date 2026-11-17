# Ficha del laboratorio 5 — Acceso oculto (control de acceso roto)

Dificultad: Fácil.

**Objetivo de aprendizaje**: comprender que ocultar una página sin
enlazarla no es un control de acceso real ("seguridad por oscuridad"), y
practicar dos técnicas básicas de descubrimiento de rutas: vista de código
fuente y `robots.txt`.

**Conocimientos previos**: uso de un navegador web, qué es el código
fuente HTML de una página y para qué sirve `robots.txt`.

**Contexto del desafío**: sitio web público de eventos de un instituto
ficticio. Existe una página administrativa que el equipo de desarrollo
dejó sin enlazar, pensando que eso bastaba para protegerla.

**Condición vulnerable**: la ruta `/panel-interno-2024` no exige sesión ni
credenciales; solo no está enlazada desde la interfaz. Aparece además en
`robots.txt`, lo que la revela igual.

**Recursos disponibles**: un navegador. No se necesita ninguna herramienta
de línea de comandos ni cuenta de usuario.

**Acción esperada**: ver el código fuente de la página principal o
visitar `/robots.txt`, identificar la ruta `/panel-interno-2024` y
visitarla directamente.

**Evidencia de resolución**: captura de la página `/panel-interno-2024`
mostrando la flag.

**Pistas**: ver `guia-corner-ia.md` (4 niveles, de "revisa el código
fuente" hasta la URL exacta).

**Solución docente**: abrir `/robots.txt` o el código fuente de `/`, leer
la ruta `/panel-interno-2024`, visitarla en el navegador.

**Riesgos de seguridad**: ninguno más allá de los genéricos de la
plataforma. La página no realiza ninguna acción destructiva ni expone
datos de otros usuarios (no hay usuarios en este laboratorio).

**Criterios de evaluación**: el alumno presenta la flag y explica cuál de
las dos técnicas usó para encontrar la ruta oculta (código fuente o
`robots.txt`), y puede explicar por qué ocultar un enlace no es lo mismo
que proteger una página.
