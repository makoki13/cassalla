
import cls_ronda


class Tablero:
    rondas = []
    rondas_ganadas = []
    num_jugadores: int

    @staticmethod
    def inicializa(num_jugadores: int):
        Tablero.num_jugadores = num_jugadores

    @staticmethod
    def inicializa_ronda():
        Tablero.rondas = []

    @staticmethod
    def add_ronda(ronda: cls_ronda.Ronda):
        if (len(Tablero.rondas) == Tablero.num_jugadores):
            return
        Tablero.rondas.append(ronda)

    @staticmethod
    def get_ronda():
        return Tablero.rondas

    @staticmethod
    def print_ronda(indice: int):
        Tablero.rondas[indice].test()

    @staticmethod
    def inicializa_ronda_ganada():
        Tablero.rondas_ganadas = []

    @staticmethod
    def add_ronda_ganada(indice: int):
        Tablero.rondas_ganadas.append(indice)

    @staticmethod
    def get_num_rondas_ganadas(indice: int):
        ganadas = 0
        for ronda in Tablero.rondas_ganadas:
            if ronda == indice:
                ganadas = ganadas + 1
        return ganadas
