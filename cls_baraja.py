import random

import cls_carta


class Baraja:
    def __init__(self):
        self.cartas = []
        self.num_cartas = 0

    def add_carta(self, carta: cls_carta.Carta):
        self.cartas.append(carta)
        self.num_cartas = len(self.cartas)

    def get_carta(self, indice: int):
        return self.cartas[indice]

    def get_carta_aleatoria(self):
        return self.get_carta(random.randint(0, self.num_cartas-1))
