from enum import Enum


class Decisiones(Enum):
    ME_VOY = 0
    USO_CARTA = 1
    ENVIDO = 2
    TORNE_ENVIDO = 3
    LA_FALTA_ENVIDO = 4
    TRUQUE = 5
    QUIERO = 10

    def test():
        for estado in Decisiones:
            print(estado)
