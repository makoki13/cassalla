
import cls_arbitro
from cls_decision import Decisiones, Decision
import cls_tablero
import cls_marcador
import cls_jugador
import cls_ronda
from cls_puntos import Puntos


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
        Partida.jugador_envida = None
        Partida.jugador_truca = None
        Partida.lista_jugadores_jugada = None

    # devuelve True si la partida esta completa.
    @staticmethod
    def add_jugador(jugador: cls_jugador.Jugador):
        return Partida.marcador.add_jugador(jugador)

    @staticmethod
    def get_lista_jugadores():
        return Partida.marcador.get_lista_jugadores()

    # TODO implementar la lista de jugadores según turno en el juego
    def reordena_lista_jugadores():
        Partida.lista_jugadores_jugada = Partida.get_lista_jugadores()

    def get_lista_jugadores_jugada():
        return Partida.lista_jugadores_jugada

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

    @staticmethod
    def get_envido_actual():
        return Partida.envido_actual

    @staticmethod
    def set_envido_actual(decision: Decisiones):
        Partida.envido_actual = decision
        return decision

    @staticmethod
    def get_truc_actual():
        return Partida.truc_actual

    @staticmethod
    def set_truc_actual(decision: Decisiones):
        Partida.truc_actual = decision

    @staticmethod
    def get_jugador_truca():
        return Partida.jugador_truca

    @staticmethod
    def set_jugador_truca(jugador: cls_jugador.Jugador):
        Partida.jugador_truca = jugador

    @staticmethod
    def get_jugador_envida():
        return Partida.jugador_envida

    @staticmethod
    def set_jugador_envida(jugador: cls_jugador.Jugador, decision: Decision):        
        Partida.jugador_envida = jugador
        jugador.set_decision_envido(decision)

    @staticmethod
    def envia_puntos_envido(jugador: cls_jugador.Jugador, decision: Decisiones):
        puntos = Puntos.get_puntos_envido(Partida.get_envido_actual, decision)
        Partida.add_puntos(jugador, puntos)
        pass
