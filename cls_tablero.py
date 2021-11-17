
import cls_mano


class Tablero:
    manos = []
    manos_ganadas = []
    num_jugadores: int

    @staticmethod
    def inicializa(num_jugadores: int):
        Tablero.num_jugadores = num_jugadores

    @staticmethod
    def inicializa_mano():
        Tablero.manos = []

    @staticmethod
    def add_mano(mano: cls_mano.Mano):
        if (len(Tablero.manos) == Tablero.num_jugadores):
            return
        Tablero.manos.append(mano)

    @staticmethod
    def get_mano():
        return Tablero.manos

    @staticmethod
    def print_mano(indice: int):
        Tablero.manos[indice].test()

    @staticmethod
    def inicializa_mano_ganada():
        Tablero.manos_ganadas = []

    @staticmethod
    def add_mano_ganada(indice: int):
        Tablero.manos_ganadas.append(indice)

    @staticmethod
    def get_num_manos_ganadas(indice: int):
        ganadas = 0
        for mano in Tablero.manos_ganadas:
            if mano == indice:
                ganadas = ganadas + 1
        return ganadas
