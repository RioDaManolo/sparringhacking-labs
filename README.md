# SparringHacking — Laboratorios

Máquinas vulnerables de práctica del proyecto SparringHacking. Cada carpeta es una imagen Docker independiente, con su guía de solución y su ficha de laboratorio.

| # | Carpeta | Dificultad | De qué se trata |
|---|---|---|---|
| 1 | `01-reconocimiento-linux` | Fácil | Sin vulnerabilidad que explotar: solo explorar el sistema (tareas programadas, archivos, permisos) hasta encontrar la flag. |
| 2 | `02-acceso-oculto` | Fácil | Página administrativa sin enlazar ni autenticar; se descubre por el código fuente o por `robots.txt`. |
| 3 | `03-permisos-suid` | Fácil | Binario con el bit SUID mal configurado; se encuentra enumerando y se ejecuta para leer la flag. |
| 4 | `04-fuerza-bruta` | Media | Login sin límite de intentos y contraseña débil. |
| 5 | `05-escalada-privilegios` | Media | IDOR en `/perfil/<id>`: control de acceso roto. |
| 6 | `06-inyeccion-sql` | Media | Login bypass y extracción de datos por UNION SQLi, dos caminos distintos a la misma flag. |

Los laboratorios 1 a 3 son los que recomendó el profesor en la revisión del Avance 1/2. Los laboratorios 4 a 6 son los que diseñó originalmente el equipo.

## Cómo levantar una máquina

```bash
cd <carpeta-del-laboratorio>
docker build -t sparring/<nombre>:1.0 .
docker run -d --name <nombre> -p <puerto-local>:<80-o-22> sparring/<nombre>:1.0
```

El broker todavía no las conecta, así que la flag se mete a mano para probar (esto lo hará el broker automáticamente más adelante):

```bash
docker exec <nombre> sh -c "echo -n 'SH{...32 caracteres hex...}' > <ruta-de-la-flag> && chown <uid> <ruta> && chmod 400 <ruta>"
```

La ruta y el uid de cada flag están en el `Dockerfile` de cada carpeta (`LABEL sparring.flag.ruta` y `LABEL sparring.flag.uid`).

El camino de solución completo de cada laboratorio está en su propio `guia-corner-ia.md`.
