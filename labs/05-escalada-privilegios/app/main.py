"""Instituto TecnoSur - Portal de Alumnos (laboratorio 2: control de acceso roto / IDOR).

Vulnerabilidad intencional: /perfil/<id> no comprueba que el <id> pedido sea
el del alumno que inició sesión. Con una cuenta de alumno normal, cambiar el
número en la dirección alcanza el perfil de otra persona, incluida la
dirección académica (id 1), sin que el servidor lo impida.
"""

import os
from pathlib import Path

from flask import Flask, abort, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = os.urandom(32)

USUARIO = "ana.torres"
CLAVE = "alumno2026"  # Cuenta de alumno entregada para este laboratorio: no es el objetivo.
ID_SESION = 5  # Perfil de la cuenta de alumno de arriba.
RUTA_FLAG = Path("/root/flag.txt")

PERFILES = {
    1: {"nombre": "Dirección Académica", "rol": "admin", "carrera": "—", "nivel": "—"},
    2: {"nombre": "Mateo Silva", "rol": "alumno", "carrera": "Técnico en Redes", "nivel": "2° semestre"},
    3: {"nombre": "Valentina Rojas", "rol": "alumno", "carrera": "Ingeniería en Ciberseguridad", "nivel": "4° semestre"},
    4: {"nombre": "Diego Fuentes", "rol": "alumno", "carrera": "Análisis de Datos", "nivel": "1° semestre"},
    5: {"nombre": "Ana Torres", "rol": "alumno", "carrera": "Ingeniería en Ciberseguridad", "nivel": "3° semestre"},
    6: {"nombre": "Josefina Muñoz", "rol": "alumno", "carrera": "Desarrollo de Software", "nivel": "5° semestre"},
}


@app.get("/")
def inicio():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        usuario = request.form.get("usuario", "")
        clave = request.form.get("clave", "")
        if usuario == USUARIO and clave == CLAVE:
            session["autenticado"] = True
            return redirect(url_for("perfil", id=ID_SESION))
        error = "Usuario o contraseña incorrectos."
    return render_template("login.html", error=error, usuario_demo=USUARIO, clave_demo=CLAVE)


@app.get("/perfil/<int:id>")
def perfil(id):
    if not session.get("autenticado"):
        return redirect(url_for("login"))
    persona = PERFILES.get(id)
    if persona is None:
        abort(404)
    # Falta a propósito: no se valida que "id" pertenezca al alumno de la sesión.
    es_admin = persona["rol"] == "admin"
    flag = leer_flag() if es_admin else None
    return render_template(
        "perfil.html",
        persona=persona,
        id=id,
        es_admin=es_admin,
        flag=flag,
        propio=(id == ID_SESION),
    )


@app.get("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


def leer_flag():
    try:
        return RUTA_FLAG.read_text(encoding="utf-8").strip()
    except OSError:
        return "No se encontró la flag. Avisa al equipo."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False, use_reloader=False, threaded=True)
