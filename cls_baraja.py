import cls_carta


class Baraja:
    def __init__(self):
        self.cartas = []

    def add_carta(self, carta: cls_carta.Carta):
        self.cartas.append(carta)

    def get_carta(self, indice: int):
        return self.cartas[indice]

    def test(self):
        for carta in self.cartas:
            carta.test()
