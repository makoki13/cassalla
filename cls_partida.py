
import cls_arbitro
import cls_tablero
import cls_marcador
import cls_jugador
import cls_mano


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
    def inicializa_mano():
        Partida.tablero.inicializa_mano()

    @staticmethod
    def inicializa_mano_ganada():
        Partida.tablero.inicializa_mano_ganada()

    @staticmethod
    def add_mano(mano: cls_mano.Mano):
        Partida.tablero.add_mano(mano)

    @staticmethod
    def get_cartas_mano():
        return Partida.tablero.get_mano()

    @staticmethod
    def add_mano_ganada(indice: int):
        Partida.tablero.add_mano_ganada(indice)

    @staticmethod
    def add_puntos(jugador: cls_jugador.Jugador, puntos: int):
        Partida.marcador.add_puntos(jugador, puntos)

    @staticmethod
    def get_num_manos_ganadas(indice: int):
        return Partida.tablero.get_num_manos_ganadas(indice)

    @staticmethod
    def get_ganador():
        return Partida.marcador.get_ganador()
