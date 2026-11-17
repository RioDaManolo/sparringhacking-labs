import os

from flask import Flask, Response, render_template

app = Flask(__name__)

EVENTOS = [
    {"nombre": "Semana de la Ciberseguridad", "fecha": "12 de noviembre", "lugar": "Auditorio TecnoSur"},
    {"nombre": "Taller de Redes para Principiantes", "fecha": "19 de noviembre", "lugar": "Sala B-204"},
    {"nombre": "Charla: Carreras en TI", "fecha": "26 de noviembre", "lugar": "Auditorio TecnoSur"},
]


def leer_flag():
    ruta = "/root/flag.txt"
    if not os.path.exists(ruta):
        return "SH{0000000000000000000000000000000}"
    with open(ruta, encoding="utf-8") as archivo:
        return archivo.read().strip()


@app.get("/")
def index():
    return render_template("index.html", eventos=EVENTOS)


@app.get("/robots.txt")
def robots():
    contenido = "User-agent: *\nDisallow: /panel-interno-2024\n"
    return Response(contenido, mimetype="text/plain")


@app.get("/panel-interno-2024")
def panel_interno():
    # Falta a proposito: cualquiera que llegue a esta URL ve el panel,
    # sin pedir sesion ni credenciales. La unica "proteccion" es que
    # la ruta no esta enlazada en el sitio.
    return render_template("panel.html", flag=leer_flag())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
