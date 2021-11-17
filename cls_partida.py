
import cls_arbitro
import cls_tablero
import cls_marcador
import cls_jugador
import cls_ronda


class Partida:
    id: int
    tablero: cls_tablero.Tablero
    marcador: cls_marcador.Marcador

    @staticmethod
    def inicializa(tablero: cls_tablero.Tablero, marcador: cls_marcador.Marcador):
        Partida.id = 0  # provisional
        Partida.tablero = tablero
        Partida.marcador = marcador

    # devuelve True si la partida esta completa.
    @staticmethod
    def add_jugador(jugador: cls_jugador.Jugador):
        return Partida.marcador.add_jugador(jugador)

    @staticmethod
    def get_lista_jugadores():
        return Partida.marcador.get_lista_jugadores()

    @staticmethod
    def inicializa_ronda():
        Partida.tablero.inicializa_ronda()

    @staticmethod
    def inicializa_ronda_ganada():
        Partida.tablero.inicializa_ronda_ganada()

    @staticmethod
    def add_ronda(ronda: cls_ronda.Ronda):
        Partida.tablero.add_ronda(ronda)

    @staticmethod
    def get_cartas_ronda():
        return Partida.tablero.get_ronda()

    @staticmethod
    def add_ronda_ganada(indice: int):
        Partida.tablero.add_ronda_ganada(indice)

    @staticmethod
    def add_puntos(jugador: cls_jugador.Jugador, puntos: int):
        Partida.marcador.add_puntos(jugador, puntos)

    @staticmethod
    def get_num_rondas_ganadas(indice: int):
        return Partida.tablero.get_num_rondas_ganadas(indice)

    @staticmethod
    def get_ganador():
        return Partida.marcador.get_ganador()
