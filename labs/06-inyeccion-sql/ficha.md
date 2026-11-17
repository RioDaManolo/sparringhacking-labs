# Ficha del laboratorio 3 — Inyección SQL (dos caminos)

Dificultad: Media.

**Objetivo de aprendizaje**: comprender la inyección SQL por concatenación
de texto sin parametrizar, en dos variantes distintas que llegan a la
misma flag: bypass de autenticación y extracción de datos vía UNION.

**Conocimientos previos**: sintaxis básica de SQL (SELECT, WHERE, UNION,
comentarios `--`), qué es una consulta parametrizada y por qué su
ausencia es el problema de fondo.

**Contexto del desafío**: catálogo de cursos del Instituto TecnoSur, con
un buscador público y un acceso de coordinadores.

**Condición vulnerable**: ninguna de las dos consultas SQL del sitio
(`/login` y `/buscar`) usa parámetros; ambas concatenan directamente el
texto escrito por el usuario.

**Recursos disponibles**: el navegador basta para ambos caminos; no se
necesita sqlmap ni otra herramienta (aunque se puede usar para explorar
más rápido).

**Acción esperada**:
- Camino A: en `/login`, escribir `' OR '1'='1' -- ` como usuario (con
  cualquier clave) para entrar sin credenciales válidas.
- Camino B: en `/buscar`, usar una inyección UNION SELECT ajustada a 3
  columnas para leer la tabla `configuracion` sin iniciar sesión.

**Evidencia de resolución**: captura del panel de coordinación (camino A)
o de los resultados del buscador con la fila de la flag (camino B).

**Pistas**: ver `guia-corner-ia.md` (4 niveles, comunes a ambos caminos,
más un "evaluador de caminos" para cuando el alumno ya resolvió uno).

**Solución docente**: ver `guia-corner-ia.md`, sección completa con ambos
caminos y el error común de cada uno (olvidar el comentario `-- ` en el
camino A; no ajustar el número de columnas en el camino B).

**Riesgos de seguridad**: ninguno más allá de los genéricos de la
plataforma. Se usa `Jinja2` con autoescape activo (sin `|safe` en ningún
punto), por lo que el resultado reflejado del UNION no se convierte en un
vector de XSS adicional.

**Criterios de evaluación**: el alumno presenta la flag, indica qué camino
siguió y puede explicar el camino alternativo que no usó (evaluador de
caminos), mostrando que entiende que la causa de fondo es la misma en
ambos: ausencia de consultas parametrizadas.
