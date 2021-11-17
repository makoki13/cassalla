import cls_carta
import cls_estados_carta


class Carta_en_juego:
    def __init__(self, carta: cls_carta.Carta, estado: cls_estados_carta.Estados):
        self.carta = carta
        self.estado = estado

    def print_carta(self):
        print(f'<Test carta:{self.carta.get_nombre()} estado:{self.estado}')
