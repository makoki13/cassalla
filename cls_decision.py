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
    QUIERO_TORNE_ENVIDO = 12
    QUIERO_LA_FALTA = 13
    QUIERO = 14
    NO_QUIERO_ENVIDO = 20
    NO_QUIERO_TRUC = 21
    NO_QUIERO_TORNE_ENVIDO = 22
    NO_QUIERO = 23
    SIN_DECISION = -1
    DECISION_YA_TOMADA = -2

    def test():
        for estado in Decisiones:
            print(estado)


class Decision():
    def __init__(self, decision: Decisiones, carta: cls_carta.Carta):
        self.decision = decision
        self.carta = carta
