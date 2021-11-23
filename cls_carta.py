import cls_palo


class Carta:
    def __init__(self, numero: int, palo: cls_palo.Palos, nombre: str, valor: int, valor_envido: int):
        self.numero = numero
        self.palo = palo
        self.nombre = nombre
        self.valor = valor
        self.valor_envido = valor_envido
        self.usada = False

    def get_nombre(self):
        return self.nombre

    def get_valor(self):
        return self.valor

    def get_valor_envido(self):
        return self.valor_envido

    def set_usada(self):
        self.usada = True

    def set_no_usada(self):
        self.usada = False

    def get_usada(self):
        return self.usada
