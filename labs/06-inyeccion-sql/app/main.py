"""Instituto TecnoSur - Catálogo de Cursos (laboratorio 3: inyección SQL).

Vulnerabilidad intencional: las consultas se arman concatenando texto del
usuario directamente en SQL, sin parámetros, tanto en el buscador público
de cursos como en el login de coordinadores. Hay dos caminos distintos
hasta la misma flag:
  A) Saltarse el login con una inyección en el formulario de /login.
  B) Extraer el valor guardado en la tabla de configuración con una
     inyección UNION en el buscador de /buscar, sin necesidad de login.
"""

import os
import sqlite3
import threading
from pathlib import Path

from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = os.urandom(32)

RUTA_FLAG = Path("/root/flag.txt")
_candado_db = threading.Lock()


def leer_flag():
    try:
        return RUTA_FLAG.read_text(encoding="utf-8").strip()
    except OSError:
        return "No se encontró la flag. Avisa al equipo."


def construir_base_datos():
    conexion = sqlite3.connect(":memory:", check_same_thread=False)
    conexion.execute(
        "CREATE TABLE cursos (id INTEGER PRIMARY KEY, nombre TEXT, descripcion TEXT)"
    )
    conexion.executemany(
        "INSERT INTO cursos (nombre, descripcion) VALUES (?, ?)",
        [
            ("Fundamentos de Redes", "Modelo OSI, direccionamiento IP y cableado estructurado."),
            ("Introducción a Linux", "Consola, permisos y administración básica de archivos."),
            ("Seguridad Web Básica", "OWASP Top 10 y buenas prácticas de desarrollo seguro."),
            ("Programación en Python", "Sintaxis, estructuras de datos y buenas prácticas."),
            ("Bases de Datos I", "Modelo relacional, SQL básico y normalización."),
        ],
    )
    conexion.execute(
        "CREATE TABLE coordinadores (id INTEGER PRIMARY KEY, usuario TEXT, clave TEXT, nombre TEXT)"
    )
    conexion.execute(
        "INSERT INTO coordinadores (usuario, clave, nombre) VALUES (?, ?, ?)",
        ("roberto.pena", os.urandom(16).hex(), "Roberto Peña"),
    )
    conexion.execute("CREATE TABLE configuracion (clave TEXT, valor TEXT)")
    conexion.executemany(
        "INSERT INTO configuracion (clave, valor) VALUES (?, ?)",
        [
            ("nombre_instituto", "Instituto TecnoSur"),
            ("version_portal", "2.1"),
            ("flag_evento", leer_flag()),
        ],
    )
    conexion.commit()
    return conexion


_db = construir_base_datos()


@app.get("/")
def inicio():
    return redirect(url_for("buscar"))


@app.get("/buscar")
def buscar():
    texto = request.args.get("texto", "")
    resultados = []
    error = None
    if texto:
        # Vulnerable a propósito: el texto del buscador se concatena
        # directamente en la consulta SQL, sin parámetros.
        consulta = f"SELECT id, nombre, descripcion FROM cursos WHERE nombre LIKE '%{texto}%'"
        try:
            with _candado_db:
                resultados = _db.execute(consulta).fetchall()
        except sqlite3.Error as exc:
            error = str(exc)
    return render_template("buscar.html", texto=texto, resultados=resultados, error=error)


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        usuario = request.form.get("usuario", "")
        clave = request.form.get("clave", "")
        # Vulnerable a propósito: usuario y clave se concatenan
        # directamente en la consulta SQL, sin parámetros.
        consulta = (
            f"SELECT id, nombre FROM coordinadores "
            f"WHERE usuario = '{usuario}' AND clave = '{clave}'"
        )
        fila = None
        try:
            with _candado_db:
                fila = _db.execute(consulta).fetchone()
        except sqlite3.Error as exc:
            error = str(exc)
        if fila:
            session["autenticado"] = True
            session["nombre"] = fila[1]
            return redirect(url_for("panel"))
        if error is None:
            error = "Usuario o contraseña incorrectos."
    return render_template("login.html", error=error)


@app.get("/panel")
def panel():
    if not session.get("autenticado"):
        return redirect(url_for("login"))
    return render_template("panel.html", nombre=session.get("nombre", "Coordinador"), flag=leer_flag())


@app.get("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False, use_reloader=False, threaded=True)
