import cls_carta_en_juego


class Mano:
    def __init__(self):
        self.cartas: list[cls_carta_en_juego.Carta_en_juego] = []

    def add_carta(self, carta: cls_carta_en_juego.Carta_en_juego):
        self.cartas.append(carta)

    def test(self):
        for carta in self.cartas:
            print(carta.get_nombre())
