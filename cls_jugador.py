
from cls_decision import Decisiones
import cls_usuario
import cls_ronda
import cls_arbitro
import cls_estados_carta


class Jugador:
    def __init__(self, usuario: cls_usuario.Usuario, ordinal: int):
        self.usuario = usuario
        self.ordinal = ordinal
        self.ronda = None
        self.puntos = 0

    def add_ronda(self, ronda: cls_ronda.Ronda):
        self.ronda = ronda

    def add_puntos(self, puntos: int):
        self.puntos = self.puntos + puntos

    def get_puntos(self):
        return self.puntos

    def set_puntos(self, puntos: int):
        self.puntos = puntos

    def print_ronda(self):
        for carta in self.ronda.get_cartas():
            carta.print_carta()

    def get_nombre(self):
        return self.usuario.get_nombre()

    def get_ordinal(self):
        return self.ordinal

    # En esta funcion se debe de implementar la inteligencia del jugador
    def juega(self):
        decision = Decisiones.USO_CARTA
        carta_a_enviar = None
        for carta in self.ronda.get_cartas():
            if carta.estado == cls_estados_carta.Estados.EN_MANO:
                carta_a_enviar = carta
                carta.estado = cls_estados_carta.Estados.EN_TABLERO
                break
        cls_arbitro.Arbitro.recoge_decision(decision, carta_a_enviar.carta)

    def juego_erroneo(self):
        pass
