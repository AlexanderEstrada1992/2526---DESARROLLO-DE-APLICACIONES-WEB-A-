from flask import Flask, render_template, request, redirect
from conexion.conexion import obtener_conexion
from database import (
    crear_tabla,
    insertar_equipo,
    obtener_equipos,
    eliminar_equipo,
    actualizar_equipo
)

from inventario.inventario import (
    guardar_txt,
    guardar_json,
    guardar_csv,
    leer_json,
    leer_csv
)

import os

app = Flask(__name__)
conexion = obtener_conexion()

# Crear tabla al iniciar
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
# RUTAS DINÁMICAS
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

@app.route("/usuarios")
def ver_usuarios():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template("usuarios.html", usuarios=usuarios)

@app.route("/agregar_usuario")
def agregar_usuario():
    return render_template("agregar_usuario.html")

@app.route("/guardar_usuario", methods=["POST"])
def guardar_usuario():

    nombre = request.form["nombre"]
    email = request.form["email"]
    password = request.form["password"]

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = "INSERT INTO usuarios (nombre, mail, password) VALUES (%s,%s,%s)"
    cursor.execute(sql, (nombre, email, password))

    conexion.commit()

    cursor.close()
    conexion.close()

    return redirect("/usuarios")

@app.route("/eliminar_usuario/<int:id>")
def eliminar_usuario(id):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = "DELETE FROM usuarios WHERE id_usuario=%s"
    cursor.execute(sql, (id,))

    conexion.commit()

    cursor.close()
    conexion.close()

    return redirect("/usuarios")

@app.route("/editar_usuario/<int:id>")
def editar_usuario(id):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = "SELECT * FROM usuarios WHERE id_usuario=%s"
    cursor.execute(sql, (id,))
    usuario = cursor.fetchone()

    cursor.close()
    conexion.close()

    return render_template("editar_usuario.html", usuario=usuario)

@app.route("/actualizar_usuario", methods=["POST"])
def actualizar_usuario():

    id = request.form["id"]
    nombre = request.form["nombre"]
    email = request.form["email"]
    password = request.form["password"]

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = "UPDATE usuarios SET nombre=%s, mail=%s, password=%s WHERE id_usuario=%s"
    cursor.execute(sql, (nombre, email, password, id))

    conexion.commit()

    cursor.close()
    conexion.close()

    return redirect("/usuarios")

# =========================
# AGREGAR EQUIPO
# =========================

@app.route("/agregar_equipo", methods=["GET", "POST"])
def agregar_equipo():

    if request.method == "POST":

        id_equipo = request.form["id"]
        nombre = request.form["nombre"]
        estado = request.form["estado"]
        disponibilidad = request.form["disponibilidad"]

        # Guardar en SQLite
        insertar_equipo(id_equipo, nombre, estado, disponibilidad)

        # Guardar en archivos
        guardar_txt(id_equipo, nombre, estado, disponibilidad)
        guardar_json(id_equipo, nombre, estado, disponibilidad)
        guardar_csv(id_equipo, nombre, estado, disponibilidad)

        return redirect("/ver_equipos")

    return render_template("agregar_equipo.html")


# =========================
# VER EQUIPOS (SQLite)
# =========================

@app.route("/ver_equipos")
def ver_equipos():

    equipos = obtener_equipos()

    return render_template("ver_equipos.html", equipos=equipos)


# =========================
# ELIMINAR EQUIPO
# =========================

@app.route("/eliminar_equipo/<int:id_equipo>")
def eliminar_equipo_route(id_equipo):

    eliminar_equipo(id_equipo)

    return redirect("/ver_equipos")


# =========================
# EDITAR EQUIPO
# =========================

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
# VER DATOS JSON
# =========================

@app.route("/ver_json")
def ver_json():

    datos = leer_json()

    return render_template("ver_json.html", datos=datos)


# =========================
# VER DATOS CSV
# =========================

@app.route("/ver_csv")
def ver_csv():

    datos = leer_csv()

    return render_template("ver_csv.html", datos=datos)


# =========================
# EJECUCIÓN
# =========================

if __name__ == '__main__':

    port = int(os.environ.get("PORT", 5000))

    app.run(debug=True, host='0.0.0.0', port=port)