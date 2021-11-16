
import cls_mano


class Tablero:
    manos = []
    num_jugadores: int

    @staticmethod
    def inicializa(num_jugadores: int):
        Tablero.num_jugadores = num_jugadores

    @staticmethod
    def add_mano(mano: cls_mano.Mano):
        if (len(Tablero.manos) == Tablero.num_jugadores):
            return
        Tablero.manos.append(mano)

    @staticmethod
    def print_mano(indice: int):
        Tablero.manos[indice].test()
