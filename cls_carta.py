import cls_palo


class Carta:
    def __init__(self, numero: int, palo: cls_palo.Palos, nombre: str, valor: int):
        self.numero = numero
        self.palo = palo
        self.nombre = nombre
        self.valor = valor

    def get_nombre(self):
        return self.nombre

    def get_valor(self):
        return self.valor
