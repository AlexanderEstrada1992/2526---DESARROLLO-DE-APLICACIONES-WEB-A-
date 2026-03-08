import json
import csv


# =========================
# GUARDAR EN TXT
# =========================

def guardar_txt(id_equipo, nombre, estado, disponibilidad):

    ruta = "inventario/data/datos.txt"

    with open(ruta, "a") as archivo:
        archivo.write(f"{id_equipo},{nombre},{estado},{disponibilidad}\n")


# =========================
# GUARDAR EN JSON
# =========================

def guardar_json(id_equipo, nombre, estado, disponibilidad):

    ruta = "inventario/data/datos.json"

    equipo = {
        "id": id_equipo,
        "nombre": nombre,
        "estado": estado,
        "disponibilidad": disponibilidad
    }

    try:
        with open(ruta, "r") as archivo:
            datos = json.load(archivo)
    except:
        datos = []

    datos.append(equipo)

    with open(ruta, "w") as archivo:
        json.dump(datos, archivo, indent=4)


# =========================
# GUARDAR EN CSV
# =========================

def guardar_csv(id_equipo, nombre, estado, disponibilidad):

    ruta = "inventario/data/datos.csv"

    with open(ruta, "a", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow([id_equipo, nombre, estado, disponibilidad])


# =========================
# LEER JSON
# =========================

def leer_json():

    ruta = "inventario/data/datos.json"

    try:
        with open(ruta, "r") as archivo:
            datos = json.load(archivo)
    except:
        datos = []

    return datos


# =========================
# LEER CSV
# =========================

def leer_csv():

    ruta = "inventario/data/datos.csv"

    datos = []

    try:
        with open(ruta, "r") as archivo:
            reader = csv.reader(archivo)

            for fila in reader:
                datos.append(fila)
    except:
        pass

    return datos