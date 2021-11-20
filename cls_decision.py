from enum import Enum

import cls_carta


class Decisiones(Enum):
    USO_CARTA = 1
    ENVIDO = 2
    TORNE_ENVIDO = 3
    LA_FALTA_ENVIDO = 4
    TRUQUE = 5
    QUIERO_ENVIDO = 10
    QUIERO_TRUC = 11
    NO_QUIERO_ENVIDO = 20
    NO_QUIERO_TRUC = 21
    SIN_DECISION = -1
    DECISION_YA_TOMADA = -2

    def test():
        for estado in Decisiones:
            print(estado)


class Decision():
    def __init__(self, decision: Decisiones, carta: cls_carta.Carta):
        self.decision = decision
        self.carta = carta
