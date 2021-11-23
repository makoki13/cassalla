
from cls_jugador import Jugador

class Reglas:

    @staticmethod
    def evalua_envido(jugadores):
        jugador: Jugador
        max_puntuacion: int = 0
        jugador_con_la_max_puntuacion = None
        for jugador in jugadores:
            puntos = jugador.get_puntos_envido();
            if (puntos > max_puntuacion):
                max_puntuacion = puntos
                jugador_con_la_max_puntuacion = jugador
        d = dict();
        d['jugador'] = jugador_con_la_max_puntuacion
        d['puntuacion']   = max_puntuacion

        return d