# Ficha del laboratorio 2 — Escalada de privilegios (IDOR)

Dificultad: Media.

**Objetivo de aprendizaje**: comprender el control de acceso roto a nivel
de objeto (IDOR): una aplicación que autentica correctamente pero no
verifica que el recurso solicitado pertenezca al usuario de la sesión.

**Conocimientos previos**: qué es una sesión web, qué es un identificador
numérico en una URL, concepto de autenticación vs. autorización.

**Contexto del desafío**: panel de perfiles de alumnos del Instituto
TecnoSur. El alumno inicia sesión con una cuenta propia de alumno regular.

**Condición vulnerable**: la ruta `/perfil/<id>` muestra el perfil
correspondiente al `id` de la URL sin comprobar que ese `id` sea el del
alumno de la sesión activa. Cambiando el número en la URL se puede ver el
perfil de cualquier otro usuario, incluido uno de administración que
contiene la flag.

**Recursos disponibles**: credenciales de alumno regular entregadas
(`ana.torres` / `alumno2026`), el navegador.

**Acción esperada**: iniciar sesión, observar el propio `/perfil/<id>`, y
probar otros valores de `id` (empezando por números bajos como 1) hasta
encontrar un perfil de administración.

**Evidencia de resolución**: captura del perfil con `id=1` mostrando la
flag, estando autenticado con una cuenta distinta (`ana.torres`).

**Pistas**: ver `guia-corner-ia.md` (4 niveles).

**Solución docente**: iniciar sesión como `ana.torres`, visitar
`/perfil/1` directamente en la barra de direcciones.

**Riesgos de seguridad**: ninguno más allá de los genéricos de la
plataforma. Verificado además que sin sesión activa `/perfil/<id>`
redirige al login (no hay fuga de datos a usuarios no autenticados), y que
con sesión activa un `id` inexistente devuelve 404 en vez de filtrar
información.

**Criterios de evaluación**: el alumno presenta la flag y explica que la
causa no es una falla de autenticación (sí inició sesión correctamente)
sino de autorización: la aplicación nunca comprobó que el `id` solicitado
perteneciera a su propia cuenta.
