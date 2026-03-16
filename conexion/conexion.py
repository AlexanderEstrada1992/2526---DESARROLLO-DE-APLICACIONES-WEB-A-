import mysql.connector

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="inventario_web"
        )
        print("Conexión exitosa a MySQL")
        return conexion
    except mysql.connector.Error as err:
        print("Error de conexión:", err)