
import cls_arbitro
from cls_decision import Decisiones, Decision
import cls_tablero
import cls_marcador
import cls_jugador
import cls_ronda


class Partida:
    id: int
    tablero: cls_tablero.Tablero
    marcador: cls_marcador.Marcador
    ronda_actual: int
    envido_actual: int

    @staticmethod
    def inicializa(tablero: cls_tablero.Tablero, marcador: cls_marcador.Marcador):
        Partida.id = 0  # provisional
        Partida.tablero = tablero
        Partida.marcador = marcador
        Partida.ronda_actual = 0
        Partida.envido_actual = Decisiones.SIN_DECISION
        Partida.truc_actual = Decisiones.SIN_DECISION

    # devuelve True si la partida esta completa.
    @staticmethod
    def add_jugador(jugador: cls_jugador.Jugador):
        return Partida.marcador.add_jugador(jugador)

    @staticmethod
    def get_lista_jugadores():
        return Partida.marcador.get_lista_jugadores()

    @staticmethod
    def inicializa_ronda():
        Partida.ronda_actual = Partida.ronda_actual + 1
        Partida.tablero.inicializa_ronda()

    @staticmethod
    def inicia_contador_rondas():
        Partida.ronda_actual = 0

    @staticmethod
    def get_ronda_actual():
        return Partida.ronda_actual

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
