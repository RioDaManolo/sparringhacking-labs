"""Instituto TecnoSur - Portal Campus (laboratorio 1: fuerza bruta).

Vulnerabilidad intencional: el formulario de login no limita intentos
(no hay bloqueo de cuenta, no hay CAPTCHA, no hay demora progresiva) y
la cuenta de la profesora usa una contraseña débil. Objetivo del
alumno: encontrar la contraseña con Hydra y un diccionario.
"""

import os
from pathlib import Path

from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
# Clave de sesión aleatoria en cada arranque del contenedor: nunca queda
# fija en el código ni en la imagen, para que la única forma de entrar
# al panel sea adivinando la contraseña real (no falsificando la cookie).
app.secret_key = os.urandom(32)

USUARIO = "camila.rios"
CLAVE = "123456789"  # Débil a propósito: es el objetivo pedagógico del laboratorio.
RUTA_FLAG = Path("/root/flag.txt")


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
            return redirect(url_for("panel"))
        # Mensaje único para usuario y clave incorrectos: no revela si el
        # usuario existe, pero la cuenta sigue sin límite de intentos.
        error = "Usuario o contraseña incorrectos."
    return render_template("login.html", error=error)


@app.get("/panel")
def panel():
    if not session.get("autenticado"):
        return redirect(url_for("login"))
    return render_template("panel.html", flag=leer_flag())


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
