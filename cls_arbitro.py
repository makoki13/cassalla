
import cls_jugador


class Arbitro:
    jugador_en_turno: cls_jugador.Jugador

    @staticmethod
    def set_jugador_en_turno(jugador: cls_jugador.Jugador):
        Arbitro.jugador_en_turno = jugador

    def get_jugador_en_turno():
        return Arbitro.jugador_en_turno
