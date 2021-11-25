import random

from cls_carta import Carta


class Baraja:
    def __init__(self):
        self.cartas = []
        self.num_cartas = 0

    def add_carta(self, carta: Carta):
        self.cartas.append(carta)
        self.num_cartas = len(self.cartas)

    def get_carta(self, indice: int):
        carta: Carta
        ha_terminado_mazo = False
        carta = self.cartas[indice];
        while carta.get_usada() == True:
            indice = indice + 1
            if (indice == self.num_cartas):
                if (ha_terminado_mazo == True):
                    return None
                indice = 0
                ha_terminado_mazo = True
            carta = self.cartas[indice];
        return carta
        

        return self.cartas[indice]

    def get_carta_aleatoria(self):
        carta: Carta
        carta = self.get_carta(random.randint(0, self.num_cartas-1))
        carta.set_usada()
        return carta

    def baraja_cartas(self):
        for carta in self.cartas:            
            carta.set_no_usada()

