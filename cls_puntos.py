
from cls_decision import Decisiones


class Puntos:
    @staticmethod
    def get_puntos_envido(decision: Decisiones, tipo_envido: Decisiones):
        puntos: int
        if decision == Decisiones.NO_QUIERO_ENVIDO:
            if tipo_envido == Decisiones.ENVIDO:
                puntos = 1
            elif decision == Decisiones.TORNE_ENVIDO:
                puntos = 2
        elif decision == Decisiones.QUIERO_ENVIDO:
            if tipo_envido == Decisiones.ENVIDO:
                puntos = 2
            elif decision == Decisiones.TORNE_ENVIDO:
                puntos = 4
        return puntos
