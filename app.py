from flask import Flask

app = Flask(__name__)

# Ruta principal
@app.route('/')
def inicio():
    return "Bienvenido al Sistema de Gestión Operativa de la UNMO"

# Ruta dinámica para Servidor Policial
@app.route('/servidor/<nombre>')
def servidor(nombre):
    return f"Bienvenido, {nombre}. Este es tu sistema operativo de la UNMO."

# Ruta dinámica para Equipo Táctico
@app.route('/equipo/<tipo>')
def equipo(tipo):
    return f"Equipo: {tipo} – estado operativo y disponibilidad actual en la UNMO."

# Ruta dinámica para Servicio Operativo
@app.route('/servicio/<tipo_evento>')
def servicio(tipo_evento):
    return f"Servicio Operativo: {tipo_evento} – asignado según planificación de la UNMO."

# Ruta dinámica para Reporte Operativo
@app.route('/reporte/<int:id_reporte>')
def reporte(id_reporte):
    return f"Reporte Operativo N° {id_reporte} – información registrada y disponible."

# Ruta dinámica para Mantenimiento de Equipos
@app.route('/mantenimiento/<int:id_equipo>')
def mantenimiento(id_equipo):
    return f"Mantenimiento registrado para el equipo N° {id_equipo} – estado actualizado en la UNMO."

if __name__ == '__main__':
    app.run(debug=True)
