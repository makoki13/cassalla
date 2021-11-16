
class Usuario:
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre
