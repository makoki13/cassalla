
import cls_usuario
import cls_mano


class Jugador:
    def __init__(self, usuario: cls_usuario.Usuario, ordinal: int, mano: cls_mano.Mano):
        self.usuario = usuario
        self.ordinal = ordinal
        self.mano = mano
        self.puntos = 0

    def add_puntos(self, puntos: int):
        self.puntos = self.puntos + puntos

    def get_puntos(self):
        return self.puntos
