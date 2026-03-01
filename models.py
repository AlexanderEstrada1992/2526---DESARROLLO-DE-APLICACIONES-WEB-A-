class EquipoTactico:
    def __init__(self, id_equipo, nombre, estado, disponibilidad):
        self._id_equipo = id_equipo
        self._nombre = nombre
        self._estado = estado
        self._disponibilidad = disponibilidad

    # Getters
    def get_id(self):
        return self._id_equipo

    def get_nombre(self):
        return self._nombre

    def get_estado(self):
        return self._estado

    def get_disponibilidad(self):
        return self._disponibilidad

    # Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_estado(self, estado):
        self._estado = estado

    def set_disponibilidad(self, disponibilidad):
        self._disponibilidad = disponibilidad

    # Método para convertir a diccionario
    def to_dict(self):
        return {
            "id_equipo": self._id_equipo,
            "nombre": self._nombre,
            "estado": self._estado,
            "disponibilidad": self._disponibilidad
        }

class InventarioEquipos:
    def __init__(self):
        # Diccionario donde la clave será el ID del equipo
        self.equipos = {}

    # Añadir equipo
    def agregar_equipo(self, equipo):
        self.equipos[equipo.get_id()] = equipo

    # Eliminar equipo por ID
    def eliminar_equipo(self, id_equipo):
        if id_equipo in self.equipos:
            del self.equipos[id_equipo]

    # Actualizar estado o disponibilidad
    def actualizar_equipo(self, id_equipo, estado=None, disponibilidad=None):
        if id_equipo in self.equipos:
            if estado is not None:
                self.equipos[id_equipo].set_estado(estado)
            if disponibilidad is not None:
                self.equipos[id_equipo].set_disponibilidad(disponibilidad)

    # Buscar equipo por nombre
    def buscar_por_nombre(self, nombre):
        resultado = []
        for equipo in self.equipos.values():
            if nombre.lower() in equipo.get_nombre().lower():
                resultado.append(equipo)
        return resultado

    # Mostrar todos los equipos
    def mostrar_todos(self):
        return list(self.equipos.values())

class Equipo:

    def __init__(self, id, nombre, estado, disponibilidad):
        self.id = id
        self.nombre = nombre
        self.estado = estado
        self.disponibilidad = disponibilidad

    def obtener_datos(self):
        return (self.id, self.nombre, self.estado, self.disponibilidad)

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def actualizar_disponibilidad(self, nueva_disponibilidad):
        self.disponibilidad = nueva_disponibilidad