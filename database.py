import sqlite3


def conectar():
    conn = sqlite3.connect("unmo.db")
    return conn


def crear_tabla():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS equipos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            estado TEXT NOT NULL,
            disponibilidad TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def insertar_equipo(id_equipo, nombre, estado, disponibilidad):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO equipos (id, nombre, estado, disponibilidad)
        VALUES (?, ?, ?, ?)
    """, (id_equipo, nombre, estado, disponibilidad))

    conn.commit()
    conn.close()

def obtener_equipos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM equipos")
    equipos = cursor.fetchall()

    conn.close()
    return equipos

def eliminar_equipo(id_equipo):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM equipos WHERE id = ?", (id_equipo,))

    conn.commit()
    conn.close()

def actualizar_equipo(id_equipo, nombre, estado, disponibilidad):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE equipos
        SET nombre = ?, estado = ?, disponibilidad = ?
        WHERE id = ?
    """, (nombre, estado, disponibilidad, id_equipo))

    conn.commit()
    conn.close()