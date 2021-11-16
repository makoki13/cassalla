from enum import Enum


class Palos(Enum):
    BASTOS = 1
    COPAS = 2
    ESPADAS = 3
    OROS = 4

    def test():
        for palo in Palos:
            print(palo)
