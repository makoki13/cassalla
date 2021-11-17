
from cls_decision import Decisiones
import cls_usuario
import cls_mano
import cls_arbitro
import cls_estados_carta


class Jugador:
    def __init__(self, usuario: cls_usuario.Usuario, ordinal: int):
        self.usuario = usuario
        self.ordinal = ordinal
        self.mano = None
        self.puntos = 0

    def add_mano(self, mano: cls_mano.Mano):
        self.mano = mano

    def add_puntos(self, puntos: int):
        self.puntos = self.puntos + puntos

    def get_puntos(self):
        return self.puntos

    def set_puntos(self, puntos: int):
        self.puntos = puntos

    def print_mano(self):
        for carta in self.mano.get_cartas():
            carta.print_carta()

    def get_nombre(self):
        return self.usuario.get_nombre()

    def get_ordinal(self):
        return self.ordinal

    def juega(self):
        decision = Decisiones.USO_CARTA
        carta_a_enviar = None
        for carta in self.mano.get_cartas():
            if carta.estado == cls_estados_carta.Estados.EN_MANO:
                carta_a_enviar = carta
                carta.estado = cls_estados_carta.Estados.EN_TABLERO
                break
        cls_arbitro.Arbitro.recoge_decision(decision, carta_a_enviar.carta)
