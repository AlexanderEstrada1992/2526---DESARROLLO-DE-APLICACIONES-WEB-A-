from flask import Flask, render_template, request, redirect
from database import (
    crear_tabla,
    insertar_equipo,
    obtener_equipos,
    eliminar_equipo,
    actualizar_equipo
)
import os

app = Flask(__name__)

# Crear tabla al iniciar la aplicación
crear_tabla()

# =========================
# RUTAS PRINCIPALES
# =========================

@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


# =========================
# RUTAS DINÁMICAS ANTERIORES
# =========================

@app.route('/servidor/<nombre>')
def servidor(nombre):
    return f"Bienvenido, {nombre}. Este es tu sistema operativo de la UNMO."


@app.route('/equipo/<tipo>')
def equipo(tipo):
    return f"Equipo: {tipo} – estado operativo y disponibilidad actual en la UNMO."


@app.route('/servicio/<tipo_evento>')
def servicio(tipo_evento):
    return f"Servicio Operativo: {tipo_evento} – asignado según planificación de la UNMO."


@app.route('/reporte/<int:id_reporte>')
def reporte(id_reporte):
    return f"Reporte Operativo N° {id_reporte} – información registrada y disponible."


@app.route('/mantenimiento/<int:id_equipo>')
def mantenimiento(id_equipo):
    return f"Mantenimiento registrado para el equipo N° {id_equipo} – estado actualizado en la UNMO."


# =========================
# CRUD - AGREGAR EQUIPO
# =========================

@app.route("/agregar_equipo", methods=["GET", "POST"])
def agregar_equipo():
    if request.method == "POST":
        id_equipo = request.form["id"]
        nombre = request.form["nombre"]
        estado = request.form["estado"]
        disponibilidad = request.form["disponibilidad"]

        insertar_equipo(id_equipo, nombre, estado, disponibilidad)

        return redirect("/")

    return render_template("agregar_equipo.html")
@app.route("/ver_equipos")
def ver_equipos():
    equipos = obtener_equipos()
    return render_template("ver_equipos.html", equipos=equipos)

@app.route("/eliminar_equipo/<int:id_equipo>")
def eliminar_equipo_route(id_equipo):
    eliminar_equipo(id_equipo)
    return redirect("/ver_equipos")

@app.route("/editar_equipo/<int:id_equipo>", methods=["GET", "POST"])
def editar_equipo(id_equipo):

    equipos = obtener_equipos()
    equipo_actual = None

    for e in equipos:
        if e[0] == id_equipo:
            equipo_actual = e
            break

    if request.method == "POST":
        nombre = request.form["nombre"]
        estado = request.form["estado"]
        disponibilidad = request.form["disponibilidad"]

        actualizar_equipo(id_equipo, nombre, estado, disponibilidad)

        return redirect("/ver_equipos")

    return render_template("editar_equipo.html", equipo=equipo_actual)

# =========================
# EJECUCIÓN
# =========================

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)