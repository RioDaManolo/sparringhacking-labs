# Ficha del laboratorio 1 — Fuerza bruta

Dificultad: Media.

**Objetivo de aprendizaje**: comprender por qué la falta de límite de
intentos de login combinada con contraseñas débiles permite un ataque de
fuerza bruta, y practicar el uso de una herramienta de ataque automatizado
(Hydra) contra un formulario web real.

**Conocimientos previos**: qué es un ataque de fuerza bruta, uso básico de
la línea de comandos y de Hydra (o disposición a aprenderlo con la pista
de nivel 4).

**Contexto del desafío**: panel de acceso de un alumno del Instituto
TecnoSur. El formulario no tiene usuario ni clave visibles; hay que
obtenerlos atacando el propio login.

**Condición vulnerable**: el endpoint `/login` no limita el número de
intentos y la cuenta `camila.rios` usa una contraseña numérica débil
(`123456789`). El mensaje de error es genérico (no distingue si el
usuario existe), por lo que no hay además un canal de enumeración de
usuarios.

**Recursos disponibles**: Hydra (u otra herramienta de fuerza bruta HTTP),
una lista de contraseñas comunes, el navegador para confirmar el login
manualmente.

**Acción esperada**: lanzar Hydra contra `/login` con un diccionario que
incluya contraseñas numéricas comunes, confirmar la credencial válida e
iniciar sesión.

**Evidencia de resolución**: credencial encontrada y captura del panel
mostrando la flag tras iniciar sesión.

**Pistas**: ver `guia-corner-ia.md` (4 niveles).

**Solución docente**: Hydra contra el formulario POST de `/login` con
usuario fijo `camila.rios` y diccionario de contraseñas numéricas;
iniciar sesión con la credencial encontrada.

**Riesgos de seguridad**: ninguno más allá de los genéricos de la
plataforma. El login no tiene relación con otros servicios ni expone
información fuera del propio contenedor. Importante: la herramienta de
ataque solo debe apuntar a la IP del propio laboratorio, nunca a destinos
externos (la red de laboratorios no tiene salida a internet).

**Criterios de evaluación**: el alumno presenta la flag, la credencial
encontrada y puede explicar por qué la falta de límite de intentos vuelve
viable la fuerza bruta aunque la contraseña no sea la más común del mundo.
